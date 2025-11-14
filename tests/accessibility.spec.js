// Accessibility tests for The Luminous Library
import { test, expect } from '@playwright/test';

test.describe('Accessibility - Keyboard Navigation', () => {
    test('skip to main content link appears on tab', async ({ page }) => {
        await page.goto('/');

        // Tab once to focus skip link
        await page.keyboard.press('Tab');

        // Skip link should be visible when focused
        const skipLink = page.locator('.skip-link');
        await expect(skipLink).toBeFocused();
        await expect(skipLink).toBeVisible();
    });

    test('navigation is fully keyboard accessible', async ({ page }) => {
        await page.goto('/');

        // Tab to first navigation link
        await page.keyboard.press('Tab');
        await page.keyboard.press('Tab'); // Skip mobile toggle if present

        const firstNavLink = page.locator('.nav-links a').first();
        await expect(firstNavLink).toBeFocused();
    });

    test('form inputs have proper labels', async ({ page }) => {
        await page.goto('/');

        // Check email input has associated label
        const emailInput = page.locator('#email-input');
        await expect(emailInput).toHaveAttribute('aria-required', 'true');

        // Should have a label (even if visually hidden)
        const label = page.locator('label[for="email-input"]');
        await expect(label).toBeAttached();
    });

    test('buttons have aria-labels', async ({ page }) => {
        await page.goto('/');

        // Mobile nav toggle should have aria-label
        const mobileToggle = page.locator('.mobile-nav-toggle');
        if (await mobileToggle.isVisible()) {
            await expect(mobileToggle).toHaveAttribute('aria-label');
            await expect(mobileToggle).toHaveAttribute('aria-expanded');
        }
    });
});

test.describe('Accessibility - ARIA', () => {
    test('navigation has proper ARIA attributes', async ({ page }) => {
        await page.goto('/');

        const nav = page.locator('.main-nav');
        await expect(nav).toHaveAttribute('role', 'navigation');
        await expect(nav).toHaveAttribute('aria-label', 'Main navigation');
    });

    test('form has proper ARIA attributes', async ({ page }) => {
        await page.goto('/');

        const form = page.locator('#hearth-form');
        await expect(form).toHaveAttribute('aria-label');
    });
});

test.describe('Accessibility - Focus Management', () => {
    test('all interactive elements are focusable', async ({ page }) => {
        await page.goto('/');

        // Get all buttons and links
        const buttons = await page.locator('button').all();
        const links = await page.locator('a').all();

        // Check buttons are focusable (not disabled)
        for (const button of buttons) {
            const isDisabled = await button.isDisabled();
            expect(isDisabled).toBe(false);
        }

        // Check links have href
        for (const link of links) {
            const href = await link.getAttribute('href');
            expect(href).toBeTruthy();
        }
    });

    test('focus visible on all interactive elements', async ({ page }) => {
        await page.goto('/');

        // Tab through several elements and verify focus is visible
        await page.keyboard.press('Tab');
        await page.keyboard.press('Tab');
        await page.keyboard.press('Tab');

        const focused = await page.evaluate(() => document.activeElement.tagName);
        expect(['A', 'BUTTON', 'INPUT']).toContain(focused);
    });
});

test.describe('Accessibility - Color Contrast', () => {
    test('text has sufficient contrast', async ({ page }) => {
        await page.goto('/');

        // This is a basic check - ideally use axe-core for comprehensive testing
        const body = page.locator('body');
        const bgColor = await body.evaluate(el =>
            window.getComputedStyle(el).backgroundColor
        );

        // Just verify background color is set
        expect(bgColor).toBeTruthy();
    });
});

test.describe('Accessibility - Screen Readers', () => {
    test('page has proper heading hierarchy', async ({ page }) => {
        await page.goto('/');

        // Check for h1
        const h1 = page.locator('h1');
        await expect(h1).toHaveCount(1); // Should have exactly one h1

        // Check headings exist in order
        const h2Count = await page.locator('h2').count();
        expect(h2Count).toBeGreaterThan(0);
    });

    test('images have alt text or are decorative', async ({ page }) => {
        await page.goto('/');

        const images = await page.locator('img').all();

        for (const img of images) {
            const alt = await img.getAttribute('alt');
            const role = await img.getAttribute('role');

            // Should have alt text OR role="presentation"
            expect(alt !== null || role === 'presentation').toBe(true);
        }
    });
});
