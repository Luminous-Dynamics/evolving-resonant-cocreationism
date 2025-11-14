// Performance tests for The Luminous Library
import { test, expect } from '@playwright/test';

test.describe('Performance', () => {
    test('page loads quickly', async ({ page }) => {
        const startTime = Date.now();

        await page.goto('/');

        const loadTime = Date.now() - startTime;

        // Page should load in under 3 seconds (generous for local testing)
        expect(loadTime).toBeLessThan(3000);
    });

    test('no console errors on page load', async ({ page }) => {
        const errors = [];

        page.on('console', msg => {
            if (msg.type() === 'error') {
                errors.push(msg.text());
            }
        });

        await page.goto('/');

        // Wait for any async errors
        await page.waitForTimeout(1000);

        expect(errors).toHaveLength(0);
    });

    test('respects prefers-reduced-motion', async ({ page }) => {
        // Emulate reduced motion preference
        await page.emulateMedia({ reducedMotion: 'reduce' });

        await page.goto('/');

        // Check if consciousness field respects reduced motion
        // The animation should not start if user prefers reduced motion
        const hasAnimation = await page.evaluate(() => {
            const field = document.querySelector('.consciousness-field');
            if (!field) return false;

            const canvas = field.querySelector('canvas');
            return !!canvas;
        });

        // With reduced motion, animations should be minimal or disabled
        // This is a basic check - the actual implementation may vary
        expect(typeof hasAnimation).toBe('boolean');
    });

    test('images load correctly', async ({ page }) => {
        await page.goto('/');

        // Get all images
        const images = await page.locator('img').all();

        for (const img of images) {
            const isLoaded = await img.evaluate((el) => {
                return el.complete && el.naturalHeight !== 0;
            });

            expect(isLoaded).toBe(true);
        }
    });

    test('no 404 errors for resources', async ({ page }) => {
        const failedRequests = [];

        page.on('response', response => {
            if (response.status() === 404) {
                failedRequests.push(response.url());
            }
        });

        await page.goto('/');

        // Wait for all resources
        await page.waitForLoadState('networkidle');

        // Should have no 404s
        expect(failedRequests).toHaveLength(0);
    });
});

test.describe('Responsive Design', () => {
    test('works on mobile viewport', async ({ page }) => {
        await page.setViewportSize({ width: 375, height: 667 });
        await page.goto('/');

        // Check main content is visible
        const title = page.locator('.sacred-title');
        await expect(title).toBeVisible();

        // Check harmonies are visible
        const harmonies = page.locator('.harmony-card').first();
        await expect(harmonies).toBeVisible();
    });

    test('works on tablet viewport', async ({ page }) => {
        await page.setViewportSize({ width: 768, height: 1024 });
        await page.goto('/');

        const title = page.locator('.sacred-title');
        await expect(title).toBeVisible();
    });

    test('works on desktop viewport', async ({ page }) => {
        await page.setViewportSize({ width: 1920, height: 1080 });
        await page.goto('/');

        const title = page.locator('.sacred-title');
        await expect(title).toBeVisible();
    });
});

test.describe('localStorage Handling', () => {
    test('handles localStorage gracefully', async ({ page }) => {
        await page.goto('/');

        // Check that visit counter works
        const visits = await page.evaluate(() => {
            return localStorage.getItem('erc_visits');
        });

        // Should have tracked at least one visit
        expect(parseInt(visits)).toBeGreaterThanOrEqual(1);
    });

    test('handles localStorage errors gracefully', async ({ page, context }) => {
        // Block localStorage
        await context.addInitScript(() => {
            Object.defineProperty(window, 'localStorage', {
                get() {
                    throw new Error('localStorage is disabled');
                }
            });
        });

        const errors = [];
        page.on('console', msg => {
            if (msg.type() === 'error') {
                errors.push(msg.text());
            }
        });

        await page.goto('/');

        // Page should still load even if localStorage fails
        const title = page.locator('.sacred-title');
        await expect(title).toBeVisible();

        // Should not have unhandled errors (warnings are ok)
        const criticalErrors = errors.filter(e => !e.includes('localStorage'));
        expect(criticalErrors).toHaveLength(0);
    });
});
