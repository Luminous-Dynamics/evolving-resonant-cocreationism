# 🎨 Style Guide

> **Code and documentation standards for The Luminous Library**

This guide ensures consistency and quality across all contributions. Following these standards makes the codebase maintainable, accessible, and welcoming to all contributors.

---

## 🎯 Philosophy

Our style guide embodies consciousness-first principles:

- **Clarity over cleverness**: Code should be easy to understand
- **Consistency over personal preference**: Follow established patterns
- **Accessibility first**: Consider all users, all abilities
- **Documentation as love**: Write docs for future you and others
- **Simplicity as elegance**: Avoid unnecessary complexity

---

## 💻 Code Style

### JavaScript

#### General Principles

```javascript
// ✅ Good: Clear, documented, simple
/**
 * Generates a resonance ripple effect at coordinates
 * @param {number} x - X coordinate
 * @param {number} y - Y coordinate
 */
function createRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'ripple';
    ripple.style.left = `${x}px`;
    ripple.style.top = `${y}px`;
    return ripple;
}

// ❌ Bad: Unclear, undocumented, unnecessarily terse
const cr = (x, y) => {
    const r = document.createElement('div');
    r.className = 'ripple';
    r.style.cssText = `left:${x}px;top:${y}px`;
    return r;
};
```

#### Naming Conventions

```javascript
// Variables and functions: camelCase
const userPreferences = {};
function getUserPreferences() {}

// Constants: UPPER_SNAKE_CASE
const MAX_RIPPLES = 50;
const DEFAULT_ANIMATION_DURATION = 1000;

// Classes: PascalCase
class ConsciousnessField {}

// Private variables/functions: _prefix
const _privateHelper = () => {};

// Boolean variables: is/has/should prefix
const isAnimationEnabled = true;
const hasPreferences = false;
const shouldReduceMotion = true;
```

#### Functions

```javascript
// ✅ Good: Single responsibility, clear purpose
function saveToLocalStorage(key, value) {
    try {
        localStorage.setItem(key, JSON.stringify(value));
        return true;
    } catch (error) {
        console.error('Failed to save to localStorage:', error);
        return false;
    }
}

// ❌ Bad: Multiple responsibilities
function handleEverything(key, value, shouldValidate, shouldNotify) {
    // Too many responsibilities!
}

// ✅ Good: Descriptive parameters
function createParticle(x, y, color, velocity) {
    // Clear what each parameter means
}

// ❌ Bad: Unclear parameters
function createParticle(x, y, c, v) {
    // What are c and v?
}
```

#### Comments

```javascript
// ✅ Good: Explain WHY, not WHAT
// Throttle scroll events to prevent performance issues on older devices
const throttledScroll = throttle(handleScroll, 100);

// ✅ Good: Document complex algorithms
/**
 * Implements the Golden Ratio spiral algorithm for particle distribution.
 * This creates a visually pleasing, naturally-occurring pattern that
 * aligns with consciousness-first aesthetics.
 */
function distributeParticlesInSpiral(count) {
    // Implementation...
}

// ❌ Bad: Redundant comment
// Set x to 10
const x = 10;

// ❌ Bad: Commented-out code (remove instead)
// function oldImplementation() {
//     // ...
// }
```

#### Error Handling

```javascript
// ✅ Good: Graceful degradation
function loadUserPreferences() {
    try {
        const stored = localStorage.getItem('preferences');
        return stored ? JSON.parse(stored) : DEFAULT_PREFERENCES;
    } catch (error) {
        console.error('Failed to load preferences, using defaults:', error);
        return DEFAULT_PREFERENCES;
    }
}

// ✅ Good: User-friendly error messages
function validateInput(value) {
    if (!value) {
        throw new Error('Please provide a value for this field');
    }
    if (typeof value !== 'string') {
        throw new Error('Value must be text');
    }
}

// ❌ Bad: Silent failures
function loadUserPreferences() {
    const stored = localStorage.getItem('preferences');
    return JSON.parse(stored); // Crashes if malformed!
}
```

#### Accessibility in JavaScript

```javascript
// ✅ Good: Keyboard-accessible
button.addEventListener('click', handleClick);
button.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        handleClick(e);
    }
});

// ✅ Good: ARIA updates
function updateStatus(message) {
    const status = document.getElementById('status');
    status.textContent = message;
    status.setAttribute('aria-live', 'polite');
}

// ✅ Good: Respect user preferences
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (!prefersReducedMotion) {
    startAnimations();
}
```

#### Modern JavaScript

```javascript
// ✅ Prefer const, use let when needed, never var
const immutableValue = 42;
let mutableValue = 0;

// ✅ Use arrow functions for callbacks
items.map((item) => item.value);

// ✅ Use destructuring
const { x, y } = coordinates;
const [first, second] = array;

// ✅ Use template literals
const message = `Hello, ${name}!`;

// ✅ Use optional chaining
const value = user?.preferences?.theme;

// ✅ Use nullish coalescing
const theme = userTheme ?? 'default';
```

### HTML

#### Structure

```html
<!-- ✅ Good: Semantic HTML -->
<article>
    <header>
        <h1>The Seven Harmonies</h1>
    </header>
    <section>
        <h2>First Harmony: Infinite Love</h2>
        <p>Description...</p>
    </section>
    <footer>
        <p>Last updated: <time datetime="2025-11-17">November 17, 2025</time></p>
    </footer>
</article>

<!-- ❌ Bad: Div soup -->
<div class="article">
    <div class="header">
        <div class="title">The Seven Harmonies</div>
    </div>
</div>
```

#### Accessibility

```html
<!-- ✅ Good: Descriptive alt text -->
<img src="harmony-icon.svg" alt="Icon representing the First Harmony of Infinite Love">

<!-- ❌ Bad: Generic alt text -->
<img src="harmony-icon.svg" alt="icon">

<!-- ✅ Good: Proper heading hierarchy -->
<h1>Main Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>

<!-- ❌ Bad: Skipping levels -->
<h1>Main Title</h1>
<h4>Subsection</h4>

<!-- ✅ Good: ARIA landmarks -->
<nav aria-label="Main navigation">...</nav>
<main>...</main>
<aside aria-label="Related content">...</aside>

<!-- ✅ Good: Focus management -->
<button aria-label="Close dialog" aria-expanded="true">×</button>

<!-- ✅ Good: Form labels -->
<label for="email">Email address</label>
<input type="email" id="email" name="email" required>
```

#### Attributes Order

```html
<!-- Standard order: class, id, data-*, aria-*, other -->
<div
    class="harmony-card"
    id="harmony-1"
    data-harmony="infinite-love"
    aria-labelledby="harmony-1-title"
    tabindex="0">
```

### CSS

#### Organization

```css
/* ✅ Good: Organized by component */

/* ==========================================================================
   Consciousness Field
   ========================================================================== */

.consciousness-field {
    /* Positioning */
    position: fixed;
    top: 0;
    left: 0;

    /* Display & Box Model */
    width: 100vw;
    height: 100vh;

    /* Typography */
    /* (none) */

    /* Visual */
    background: var(--background);
    opacity: 0.9;

    /* Animation */
    transition: opacity 0.3s ease;

    /* Misc */
    pointer-events: none;
}
```

#### Custom Properties (CSS Variables)

```css
/* ✅ Good: Semantic naming */
:root {
    /* Colors */
    --color-primary: #b8860b;
    --color-background: #0a0e27;
    --color-text: #e8e8ff;

    /* Spacing */
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 2rem;

    /* Typography */
    --font-size-base: 1rem;
    --font-size-large: 1.25rem;

    /* Timing */
    --duration-fast: 150ms;
    --duration-normal: 300ms;
}

/* ❌ Bad: Generic naming */
:root {
    --color1: #b8860b;
    --size: 1rem;
}
```

#### Responsive Design

```css
/* ✅ Good: Mobile-first approach */
.harmony-card {
    padding: 1rem;
    font-size: 1rem;
}

@media (min-width: 768px) {
    .harmony-card {
        padding: 2rem;
        font-size: 1.25rem;
    }
}

/* ✅ Good: Logical breakpoints */
/* Mobile: default */
/* Tablet: 768px */
/* Desktop: 1024px */
/* Wide: 1280px */
```

#### Accessibility

```css
/* ✅ Good: Respect user preferences */
@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

@media (prefers-color-scheme: dark) {
    /* Already dark by default! */
}

/* ✅ Good: High contrast support */
@media (prefers-contrast: high) {
    :root {
        --color-text: #ffffff;
        --border-width: 2px;
    }
}

/* ✅ Good: Sufficient color contrast */
.text {
    color: #e8e8ff; /* 15.5:1 contrast on #0a0e27 background (AAA) */
}

/* ✅ Good: Focus indicators */
:focus-visible {
    outline: 3px solid var(--color-primary);
    outline-offset: 2px;
}
```

---

## 📝 Documentation Style

### Markdown

#### Headings

```markdown
<!-- ✅ Good: Clear hierarchy -->
# Document Title (H1 - only one per file)

## Major Section (H2)

### Subsection (H3)

#### Minor Section (H4)

<!-- ❌ Bad: Skipping levels -->
# Title
### Subsection (skipped H2!)
```

#### Formatting

```markdown
<!-- ✅ Good: Consistent formatting -->
**Bold for emphasis**
*Italic for slight emphasis*
`code for technical terms`
[Link text](URL)

<!-- Code blocks with language -->
```javascript
const example = 'code';
```

<!-- Lists with proper spacing -->
- First item
- Second item
  - Nested item
  - Another nested item
- Third item

<!-- Tables with alignment -->
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data     | Data     | Data     |
```

#### Document Structure

```markdown
<!-- ✅ Good: Every doc has this structure -->

# 📚 Document Title

> **Brief description in blockquote**

---

## 🎯 Overview

Brief introduction...

---

## 📋 Main Content

### Section 1

Content...

### Section 2

Content...

---

## 🔗 Related Resources

- [Link 1](URL)
- [Link 2](URL)

---

**Last Updated**: November 17, 2025

*Closing inspiration.* ✨
```

#### Writing Style

```markdown
<!-- ✅ Good: Clear, actionable, kind -->
To install dependencies, run:

```bash
npm install
```

If you encounter errors, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

<!-- ✅ Good: Code examples before/after -->
### Problem: Function is unclear

❌ Bad:
```javascript
function proc(d) { return d.map(x => x.val); }
```

✅ Good:
```javascript
function extractValues(data) {
    return data.map((item) => item.value);
}
```

<!-- ✅ Good: User-focused language -->
"You can..." instead of "One can..."
"Let's..." instead of "We will..."
"This helps..." instead of "This is..."
```

#### Emoji Usage

```markdown
<!-- ✅ Good: Sparingly, for visual scanning -->
## 🎯 Quick Start
## 🐛 Bug Reports
## 💜 Code of Conduct

<!-- ✅ Good: Status indicators -->
- ✅ Completed
- ⏳ In Progress
- ❌ Deprecated

<!-- ❌ Bad: Overuse -->
## 🎉🎊🎈 Welcome 🌟✨💖
Every 🔥 sentence 💯 has emoji! 🎉
```

### Comments in Code

```javascript
// ✅ Good: JSDoc for functions
/**
 * Creates a particle at the specified coordinates
 * @param {number} x - X coordinate
 * @param {number} y - Y coordinate
 * @param {string} [color='gold'] - Particle color
 * @returns {HTMLElement} The created particle element
 */
function createParticle(x, y, color = 'gold') {
    // Implementation...
}

// ✅ Good: Inline comments for complex logic
// Using Fisher-Yates shuffle for uniform random distribution
// This ensures each harmony has equal probability of selection
for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
}

// ❌ Bad: Redundant comments
// Increment i by 1
i++;
```

### README Files

```markdown
<!-- ✅ Good structure for README.md -->

# Project Name

Brief description in one sentence.

## Features

- Feature 1
- Feature 2

## Quick Start

```bash
npm install
npm start
```

## Documentation

- [Guide 1](link)
- [Guide 2](link)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[License name](LICENSE)
```

---

## 🧪 Testing Style

### Test Organization

```javascript
// ✅ Good: Descriptive test names
test('should save user preferences to localStorage', async () => {
    // Test implementation
});

test('should fall back to defaults when localStorage is unavailable', async () => {
    // Test implementation
});

// ❌ Bad: Vague test names
test('it works', async () => {
    // What works?
});

test('test1', async () => {
    // What does this test?
});
```

### Test Structure

```javascript
// ✅ Good: Arrange, Act, Assert (AAA) pattern
test('should create ripple at click coordinates', async ({ page }) => {
    // Arrange
    await page.goto('/');
    const x = 100;
    const y = 200;

    // Act
    await page.click(`body`, { position: { x, y } });

    // Assert
    const ripple = await page.locator('.ripple').first();
    await expect(ripple).toBeVisible();
});
```

### Accessibility Tests

```javascript
// ✅ Good: Test keyboard navigation
test('should navigate harmonies with keyboard', async ({ page }) => {
    await page.goto('/#harmonies');

    // Tab to first harmony
    await page.keyboard.press('Tab');

    // Verify focus
    const focused = await page.locator(':focus');
    await expect(focused).toHaveAttribute('data-harmony', 'infinite-love');

    // Navigate with arrow keys
    await page.keyboard.press('ArrowDown');
    const nextFocused = await page.locator(':focus');
    await expect(nextFocused).toHaveAttribute('data-harmony', 'pan-sentient-flourishing');
});
```

---

## 📦 Commit Style

### Commit Messages

```bash
# ✅ Good: Clear, specific, imperative mood
git commit -m "Add keyboard navigation to harmony cards"
git commit -m "Fix ripple effect not appearing on mobile"
git commit -m "Update CONTRIBUTING.md with testing guidelines"

# ✅ Good: Multi-line for complex changes
git commit -m "$(cat <<'EOF'
Add comprehensive accessibility testing

- Add keyboard navigation tests
- Add screen reader tests
- Add color contrast validation
- Update documentation with a11y guidelines
EOF
)"

# ❌ Bad: Vague
git commit -m "fix stuff"
git commit -m "updates"

# ❌ Bad: Past tense
git commit -m "Added feature"
git commit -m "Fixed bug"
```

### Commit Categories

Use these prefixes when appropriate:

```bash
feat: Add new feature
fix: Bug fix
docs: Documentation only
style: Code style/formatting (no functional changes)
refactor: Code refactoring (no functional changes)
test: Adding or updating tests
perf: Performance improvement
chore: Maintenance tasks
```

---

## 🎨 Design Principles

### Color Usage

```css
/* Use semantic color variables */
var(--color-primary)      /* Gold: #b8860b */
var(--color-background)   /* Deep blue: #0a0e27 */
var(--color-text)         /* Light lavender: #e8e8ff */
var(--color-accent)       /* Soft violet: #9d7bd8 */

/* Ensure AAA contrast (15.5:1) for text */
/* Ensure large text meets AA (4.5:1) minimum */
```

### Typography

```css
/* System font stack for performance */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
             Oxygen, Ubuntu, Cantarell, sans-serif;

/* Relative units for accessibility */
font-size: 1rem;        /* Not: 16px */
line-height: 1.6;       /* 1.5-1.8 for readability */
letter-spacing: 0.02em; /* Slight tracking for elegance */
```

### Spacing

```css
/* Use consistent spacing scale */
var(--spacing-xs)   /* 0.25rem - 4px */
var(--spacing-sm)   /* 0.5rem  - 8px */
var(--spacing-md)   /* 1rem    - 16px */
var(--spacing-lg)   /* 2rem    - 32px */
var(--spacing-xl)   /* 4rem    - 64px */
```

### Animations

```css
/* Respect prefers-reduced-motion */
@media (prefers-reduced-motion: no-preference) {
    .element {
        transition: transform 300ms ease-out;
    }
}

/* Use appropriate timing functions */
ease-out /* For things entering */
ease-in  /* For things exiting */
ease-in-out /* For things moving */

/* Performance: animate only transform and opacity */
/* ✅ */ transform: translateX(100px);
/* ✅ */ opacity: 0.5;
/* ❌ */ left: 100px;  /* Causes layout reflow! */
```

---

## 🔍 Code Review Checklist

### For Reviewers

- [ ] Code follows style guide
- [ ] Changes are well-documented
- [ ] Tests are included
- [ ] Accessibility is maintained
- [ ] No security issues (XSS, injection, etc.)
- [ ] Performance is acceptable
- [ ] Error handling is robust
- [ ] Backwards compatible (or breaking changes documented)
- [ ] Commit messages are clear

### For Authors

Before requesting review:

- [ ] Run `npm run precommit` (format + validate)
- [ ] Run `npm test` (all tests pass)
- [ ] Test manually in browser
- [ ] Test keyboard navigation
- [ ] Check mobile responsiveness
- [ ] Update documentation
- [ ] Update CHANGELOG.md
- [ ] Self-review your diff

---

## 🌐 Internationalization (Future)

### Preparing for Translation

```javascript
// ✅ Good: Separate text from logic
const MESSAGES = {
    welcome: 'Welcome to The Luminous Library',
    loading: 'Loading...',
    error: 'An error occurred'
};

// ✅ Good: Avoid concatenation
const message = `${count} items`; // Will be complex to translate

// ✅ Better: Use placeholders
const message = MESSAGES.itemCount.replace('{count}', count);
```

```html
<!-- ✅ Good: Use lang attribute -->
<html lang="en">

<!-- ✅ Good: Semantic dates -->
<time datetime="2025-11-17">November 17, 2025</time>
```

---

## 📊 File Organization

### Project Structure

```
/
├── index.html              # Main page
├── library.html            # Library page
├── support.html            # Support page
├── css/
│   ├── index.css           # Main styles
│   └── library.css         # Library styles
├── js/
│   ├── consciousness-field.js  # Canvas animation
│   └── preferences.js          # User preferences
├── appendices/
│   └── appendix-*.html     # Appendix pages
├── docs/
│   └── README.md           # Documentation hub
├── tests/
│   ├── accessibility.spec.js
│   ├── core-functionality.spec.js
│   └── performance.spec.js
├── .github/
│   ├── workflows/          # CI/CD
│   └── ISSUE_TEMPLATE/     # Issue templates
└── [root docs]             # README, CONTRIBUTING, etc.
```

### Naming Conventions

```
PascalCase    - Classes, components
camelCase     - Variables, functions, files
kebab-case    - HTML attributes, CSS classes, URLs
UPPER_CASE    - Constants, env variables
```

---

## ✅ Style Guide Checklist

Use this before submitting PRs:

### Code
- [ ] Follows JavaScript style (camelCase, const/let, etc.)
- [ ] Follows HTML semantic standards
- [ ] Follows CSS organization and naming
- [ ] All functions have JSDoc comments
- [ ] Complex logic has explanatory comments
- [ ] No console.logs in production code

### Accessibility
- [ ] Semantic HTML used
- [ ] ARIA labels where needed
- [ ] Keyboard navigation tested
- [ ] Color contrast meets WCAG AA (4.5:1)
- [ ] Animations respect prefers-reduced-motion
- [ ] Focus indicators visible

### Documentation
- [ ] README updated if needed
- [ ] CHANGELOG updated
- [ ] Inline comments for complex code
- [ ] Markdown formatted consistently
- [ ] Links work correctly

### Testing
- [ ] New features have tests
- [ ] All tests pass (`npm test`)
- [ ] Tested in multiple browsers
- [ ] Tested keyboard navigation
- [ ] Tested on mobile

### Git
- [ ] Commit messages are clear
- [ ] Branch name is descriptive
- [ ] No sensitive data in commits
- [ ] Formatted with Prettier (`npm run format`)

---

## 🆘 Questions About Style?

**Not sure about something?**

1. Look at existing code for patterns
2. Ask in [GitHub Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)
3. Reference this guide
4. When in doubt, favor clarity over cleverness

**Disagree with a guideline?**

Open a discussion! This guide evolves with community input.

---

## 📚 Related Resources

### Our Documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical architecture
- [ACCESSIBILITY.md](ACCESSIBILITY.md) - A11y guidelines
- [TESTING.md](TESTING.md) - Testing guide

### External Resources
- [MDN Web Docs](https://developer.mozilla.org/) - HTML, CSS, JS references
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Accessibility
- [Conventional Commits](https://www.conventionalcommits.org/) - Commit messages
- [Semantic Versioning](https://semver.org/) - Version numbering

---

## 🌟 The Spirit of Our Style

> "Code is a love letter to future maintainers."

Good style isn't about rigid rules—it's about:

- **Respect**: For those who'll read your code
- **Clarity**: So anyone can understand
- **Consistency**: So nothing is surprising
- **Care**: In every detail
- **Joy**: In the craft itself

**Write code you'd be proud to read a year from now.** 💜

---

**Last Updated**: November 17, 2025

*Style with substance, code with consciousness.* ✨
