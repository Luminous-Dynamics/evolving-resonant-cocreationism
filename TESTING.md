# Testing Guide

Comprehensive testing guide for The Luminous Library.

## 🧪 Test Overview

We use **Playwright** for end-to-end testing with 40+ tests covering:
- Accessibility (WCAG 2.1)
- Core functionality
- Performance
- Cross-browser compatibility

## 🚀 Quick Start

```bash
# Install dependencies
npm install

# Run all tests
npm test

# Run in headed mode (see browser)
npm run test:headed

# Run in UI mode (interactive)
npm run test:ui

# View test report
npm run test:report
```

## 📋 Test Suites

### 1. Accessibility Tests (`tests/accessibility.spec.js`)

**Keyboard Navigation**
- Skip to main content link
- Tab navigation through elements
- Form input labels
- Button ARIA labels

**ARIA Attributes**
- Navigation roles and labels
- Form ARIA attributes
- Proper semantic HTML

**Focus Management**
- All interactive elements focusable
- Visible focus indicators
- Tab order correct

**Screen Reader Support**
- Proper heading hierarchy
- Image alt text
- Semantic structure

### 2. Core Functionality Tests (`tests/core-functionality.spec.js`)

**Homepage**
- Page loads successfully
- Seven Harmonies display
- Navigation links work
- Kosmic Theory section present

**Navigation**
- Smooth scrolling to sections
- Mobile nav toggle
- Link functionality

**Forms**
- Hearth signup form exists
- Email validation
- Success messages

**Interactive Features**
- Consciousness field canvas
- Harmony card hover effects
- Ko-fi integration

### 3. Performance Tests (`tests/performance.spec.js`)

**Load Performance**
- Page load time <3s
- No console errors
- Reduced motion support

**Responsive Design**
- Mobile viewport (375x667)
- Tablet viewport (768x1024)
- Desktop viewport (1920x1080)

**localStorage**
- Safe error handling
- Graceful degradation

## 🎯 Running Specific Tests

```bash
# Run specific test file
npx playwright test tests/accessibility.spec.js

# Run specific test by name
npx playwright test -g "keyboard navigation"

# Run on specific browser
npx playwright test --project=chromium
npx playwright test --project=firefox
npx playwright test --project=webkit

# Run on mobile
npx playwright test --project="Mobile Chrome"
npx playwright test --project="Mobile Safari"
```

## 🔧 Configuration

Tests are configured in `playwright.config.js`:

**Test Timeout**: 30 seconds
**Retries**: 2 (in CI), 0 (locally)
**Workers**: Parallel execution
**Base URL**: http://localhost:8000

**Projects**:
- Desktop: Chrome, Firefox, Safari
- Mobile: Pixel 5, iPhone 12
- Tablet: iPad Pro

## 📊 Understanding Test Results

### Test Output

```
Running 216 tests using 8 workers

✓ 210 passed
✗ 6 failed
⊘ 0 skipped

Time: 45s
```

### HTML Report

After running tests, view the HTML report:

```bash
npm run test:report
```

This opens an interactive report showing:
- Test results by browser
- Screenshots of failures
- Video recordings
- Test timing data

## 🐛 Debugging Failed Tests

### 1. Run in Headed Mode

```bash
npm run test:headed
```

Watch the browser as tests run.

### 2. Use UI Mode

```bash
npm run test:ui
```

Interactive test explorer with:
- Step-by-step execution
- DOM snapshots
- Network inspection
- Time travel debugging

### 3. Add Debug Statements

```javascript
test('my test', async ({ page }) => {
    await page.pause(); // Opens inspector
    console.log('Debug info:', await page.title());
});
```

### 4. Screenshots on Failure

Screenshots are automatically captured on failure in `test-results/`.

## ✅ Writing New Tests

### Test Structure

```javascript
import { test, expect } from '@playwright/test';

test.describe('Feature Name', () => {
    test('should do something', async ({ page }) => {
        // Navigate
        await page.goto('/');

        // Interact
        await page.click('button');

        // Assert
        await expect(page.locator('h1')).toBeVisible();
    });
});
```

### Best Practices

**1. Use Specific Selectors**
```javascript
// ✅ Good
await page.locator('[data-testid="harmony-card"]')
await page.locator('button[aria-label="Toggle menu"]')

// ❌ Avoid
await page.locator('div > div > button')
```

**2. Wait for Elements**
```javascript
// ✅ Good
await expect(page.locator('.modal')).toBeVisible();

// ❌ Avoid
await page.waitForTimeout(1000);
```

**3. Test Accessibility**
```javascript
// Check ARIA
await expect(button).toHaveAttribute('aria-label');

// Check keyboard navigation
await page.keyboard.press('Tab');
await expect(link).toBeFocused();
```

**4. Test Responsiveness**
```javascript
// Set viewport
await page.setViewportSize({ width: 375, height: 667 });

// Check mobile menu
const toggle = page.locator('.mobile-nav-toggle');
await expect(toggle).toBeVisible();
```

## 🎭 Playwright Features

### Locators

```javascript
// By text
page.locator('text=Click me')

// By role
page.locator('role=button[name="Submit"]')

// By test ID
page.locator('[data-testid="hero"]')

// By CSS
page.locator('.harmony-card')

// Chaining
page.locator('nav').locator('a').first()
```

### Assertions

```javascript
// Visibility
await expect(element).toBeVisible()
await expect(element).toBeHidden()

// Text content
await expect(element).toHaveText('Hello')
await expect(element).toContainText('partial')

// Attributes
await expect(element).toHaveAttribute('href', '/page')
await expect(element).toHaveClass(/active/)

// Count
await expect(page.locator('.card')).toHaveCount(7)
```

### Actions

```javascript
// Click
await page.click('button')

// Type
await page.fill('input', 'text')

// Keyboard
await page.keyboard.press('Enter')

// Hover
await page.hover('.card')

// Screenshot
await page.screenshot({ path: 'screenshot.png' })
```

## 📈 Coverage Goals

| Category | Target | Current |
|----------|--------|---------|
| Critical Paths | 100% | ✅ |
| Accessibility | 100% | ✅ |
| Interactive Features | 90% | ✅ |
| Edge Cases | 80% | 🚧 |

## 🔄 CI/CD Integration

Tests run automatically on:
- Every push to main or claude/* branches
- Every pull request
- Manual workflow dispatch

See `.github/workflows/test.yml` for configuration.

## 🆘 Common Issues

### Issue: Tests timeout

**Solution**: Increase timeout in config
```javascript
test('slow test', async ({ page }) => {
    test.setTimeout(60000); // 60 seconds
});
```

### Issue: Element not found

**Solution**: Wait for element
```javascript
await page.waitForSelector('.element');
```

### Issue: Flaky tests

**Solution**: Use proper waiting
```javascript
// ✅ Good
await expect(element).toBeVisible();

// ❌ Avoid
await page.waitForTimeout(1000);
```

## 📚 Resources

- [Playwright Docs](https://playwright.dev/)
- [Best Practices](https://playwright.dev/docs/best-practices)
- [Accessibility Testing](https://playwright.dev/docs/accessibility-testing)
- [Test Runner API](https://playwright.dev/docs/api/class-test)

## 💜 Consciousness-First Testing

Remember: tests are acts of love for users.

Every test ensures:
- ♿ Accessibility for all beings
- 🔒 Security and safety
- 🚀 Performance and respect
- 💚 Quality and excellence

---

**Thank you for maintaining quality through testing!** ✨
