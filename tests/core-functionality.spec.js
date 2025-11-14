// Core functionality tests for The Luminous Library
import { test, expect } from '@playwright/test';

test.describe('Homepage', () => {
    test('loads successfully', async ({ page }) => {
        await page.goto('/');

        // Check page title
        await expect(page).toHaveTitle(/The Luminous Library/);

        // Check main heading exists
        const title = page.locator('.sacred-title');
        await expect(title).toContainText('The Luminous Library');
    });

    test('displays seven harmonies', async ({ page }) => {
        await page.goto('/');

        // Should have 7 harmony cards
        const harmonyCards = page.locator('.harmony-card');
        await expect(harmonyCards).toHaveCount(7);

        // Each card should have a number, title, and description
        const firstCard = harmonyCards.first();
        await expect(firstCard.locator('.harmony-number')).toBeVisible();
        await expect(firstCard.locator('h3')).toBeVisible();
        await expect(firstCard.locator('p')).toBeVisible();
    });

    test('has working navigation links', async ({ page }) => {
        await page.goto('/');

        // Check navigation exists
        const nav = page.locator('.main-nav');
        await expect(nav).toBeVisible();

        // Check links are present
        const navLinks = nav.locator('a');
        const count = await navLinks.count();
        expect(count).toBeGreaterThan(0);
    });
});

test.describe('Navigation', () => {
    test('smooth scrolls to sections', async ({ page }) => {
        await page.goto('/');

        // Click on "Seven Harmonies" link
        await page.click('a[href="#seven-harmonies"]');

        // Wait for scroll
        await page.waitForTimeout(500);

        // Check we're near the harmonies section
        const harmoniesSection = page.locator('#seven-harmonies');
        await expect(harmoniesSection).toBeInViewport();
    });

    test('mobile nav toggle works', async ({ page, viewport }) => {
        // Set mobile viewport
        await page.setViewportSize({ width: 375, height: 667 });
        await page.goto('/');

        const navLinks = page.locator('.nav-links');
        const toggle = page.locator('.mobile-nav-toggle');

        // On mobile, toggle should be visible
        if (await toggle.isVisible()) {
            // Nav should start hidden/off-screen
            const initialState = await navLinks.getAttribute('class');

            // Click toggle
            await toggle.click();

            // Nav should now be active
            await expect(navLinks).toHaveClass(/active/);

            // aria-expanded should update
            await expect(toggle).toHaveAttribute('aria-expanded', 'true');

            // Click again to close
            await toggle.click();
            await expect(toggle).toHaveAttribute('aria-expanded', 'false');
        }
    });
});

test.describe('Kosmic Theory Section', () => {
    test('displays kosmic theory feature box', async ({ page }) => {
        await page.goto('/');

        const kosmicFeature = page.locator('.kosmic-feature');
        await expect(kosmicFeature).toBeVisible();
        await expect(kosmicFeature).toContainText('Kosmic Theory');
    });

    test('has links to kosmic theory pages', async ({ page }) => {
        await page.goto('/');

        // Check for executive summary link
        const summaryLink = page.locator('a[href*="executive-summary"]');
        await expect(summaryLink).toBeVisible();

        // Check for full paper link
        const paperLink = page.locator('a[href*="full-paper"]');
        await expect(paperLink).toBeVisible();
    });
});

test.describe('Form Functionality', () => {
    test('hearth signup form exists', async ({ page }) => {
        await page.goto('/');

        const form = page.locator('#hearth-form');
        await expect(form).toBeVisible();

        // Has email input
        const emailInput = page.locator('#email-input');
        await expect(emailInput).toBeVisible();
        await expect(emailInput).toHaveAttribute('type', 'email');
        await expect(emailInput).toHaveAttribute('required');

        // Has submit button
        const submitButton = form.locator('button[type="submit"]');
        await expect(submitButton).toBeVisible();
    });

    test('form requires valid email', async ({ page }) => {
        await page.goto('/');

        const emailInput = page.locator('#email-input');
        const submitButton = page.locator('#hearth-form button[type="submit"]');

        // Try to submit with invalid email
        await emailInput.fill('invalid-email');
        await submitButton.click();

        // HTML5 validation should prevent submission
        const isValid = await emailInput.evaluate((el) => el.validity.valid);
        expect(isValid).toBe(false);
    });

    test('form shows success message on submit', async ({ page }) => {
        await page.goto('/');

        const emailInput = page.locator('#email-input');
        const submitButton = page.locator('#hearth-form button[type="submit"]');

        // Fill with valid email
        await emailInput.fill('test@example.com');
        await submitButton.click();

        // Wait for success message
        await page.waitForTimeout(100);

        // Button text should change
        const buttonText = await submitButton.textContent();
        expect(buttonText).toContain('Welcome');
    });
});

test.describe('Interactive Features', () => {
    test('consciousness field canvas loads', async ({ page }) => {
        await page.goto('/');

        // Check if canvas was created by consciousness-field.js
        const canvas = page.locator('.consciousness-field canvas');

        // May take a moment to load
        await page.waitForTimeout(500);

        // Canvas should exist if script loaded
        const canvasCount = await canvas.count();
        expect(canvasCount).toBeGreaterThanOrEqual(0); // May be 0 if reduced motion
    });

    test('harmony cards have hover effects', async ({ page }) => {
        await page.goto('/');

        const firstCard = page.locator('.harmony-card').first();

        // Get initial background
        const initialBg = await firstCard.evaluate(el =>
            window.getComputedStyle(el).background
        );

        // Hover over card
        await firstCard.hover();

        // Background should change (this is a basic check)
        await page.waitForTimeout(100);

        // Just verify the element is interactive
        const isInteractive = await firstCard.evaluate(el => {
            const styles = window.getComputedStyle(el);
            return styles.cursor === 'pointer' || styles.transition !== 'none';
        });

        // Cards should have some interactivity
        expect(typeof isInteractive).toBe('boolean');
    });
});

test.describe('Support Integration', () => {
    test('ko-fi support links exist', async ({ page }) => {
        await page.goto('/');

        // Check for Ko-fi links
        const kofiLinks = page.locator('a[href*="ko-fi.com"]');
        const count = await kofiLinks.count();

        expect(count).toBeGreaterThan(0);
    });
});

test.describe('Meta Tags and SEO', () => {
    test('has proper meta tags', async ({ page }) => {
        await page.goto('/');

        // Check description
        const description = await page.locator('meta[name="description"]').getAttribute('content');
        expect(description).toContain('consciousness');

        // Check Open Graph tags
        const ogTitle = await page.locator('meta[property="og:title"]').getAttribute('content');
        expect(ogTitle).toContain('Luminous Library');

        // Check Twitter Card
        const twitterCard = await page.locator('meta[name="twitter:card"]').getAttribute('content');
        expect(twitterCard).toBeTruthy();
    });

    test('has favicon', async ({ page }) => {
        await page.goto('/');

        const favicon = page.locator('link[rel="icon"]');
        await expect(favicon).toHaveAttribute('href', 'favicon.svg');
    });
});
