# 🤝 Contributing to The Luminous Library

Thank you for your interest in contributing to Evolving Resonant Co-creationism! This project embodies consciousness-first principles, and we welcome contributions that align with this philosophy.

---

## 🌟 Philosophy of Contribution

Contributing to this project is itself an act of **co-creation** - a living expression of the Fifth Harmony (Universal Interconnectedness) and Sixth Harmony (Sacred Reciprocity).

### Our Values
- **Consciousness-first**: Every change should serve the awakening and flourishing of consciousness
- **Accessibility**: Technology should be available to all beings
- **Excellence**: Rigor and playfulness in balance
- **Privacy**: Respect for user autonomy and data sovereignty
- **Openness**: Transparent processes and inclusive collaboration

---

## 🚀 Getting Started

### Prerequisites
- **Git** - Version control
- **Node.js 16+** - For development tools
- **Basic web development knowledge** - HTML, CSS, JavaScript
- **An open heart** - Willingness to engage with philosophical depth

### Setting Up Your Environment

1. **Fork the repository**
   ```bash
   # Click "Fork" on GitHub, then clone your fork
   git clone https://github.com/YOUR_USERNAME/evolving-resonant-cocreationism.git
   cd evolving-resonant-cocreationism
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create a branch**
   ```bash
   git checkout -b feature/your-consciousness-first-feature
   ```

4. **Serve locally**
   ```bash
   # Using Python
   python -m http.server 8000

   # Or using npx
   npx serve .
   ```

5. **Visit** `http://localhost:8000`

---

## 📝 How to Contribute

### Types of Contributions

#### 🐛 Bug Reports
Found something not working as expected?

**Before submitting:**
- Check if the issue already exists
- Verify it's reproducible
- Gather browser/environment details

**When submitting:**
```markdown
**Description**: Clear description of the bug
**Steps to Reproduce**:
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior**: What should happen
**Actual Behavior**: What actually happens
**Browser**: Chrome 120 / Firefox 115 / Safari 17
**Screenshots**: If applicable
```

#### ✨ Feature Requests
Have an idea for enhancement?

**Consider:**
- Does it align with consciousness-first principles?
- Will it improve accessibility or user experience?
- Is it technically feasible?

**When submitting:**
```markdown
**Feature**: Brief description
**Motivation**: Why this serves consciousness/users
**Proposal**: How it might work
**Alternatives**: Other approaches considered
```

#### 🎨 Code Contributions

**Areas we especially welcome:**
1. **Accessibility** - ARIA improvements, keyboard navigation, screen reader optimization
2. **Performance** - Load time, animation smoothness, memory efficiency
3. **Security** - XSS prevention, safe error handling, privacy protection
4. **Testing** - Playwright tests, accessibility tests, visual regression
5. **Documentation** - Guides, comments, examples
6. **Internationalization** - Translations, RTL support

---

## 💻 Development Guidelines

### Code Style

#### HTML
```html
<!-- ✅ Good: Semantic, accessible -->
<nav role="navigation" aria-label="Main navigation">
    <button aria-label="Toggle menu" aria-expanded="false">Menu</button>
</nav>

<!-- ❌ Avoid: Non-semantic, inaccessible -->
<div onclick="toggleMenu()">Menu</div>
```

#### CSS
```css
/* ✅ Good: Uses CSS custom properties, follows golden ratio */
.harmony-card {
    padding: calc(1rem * 1.618); /* φ ratio */
    background: var(--sacred-gold);
    transition: transform 0.3s ease;
}

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
    .harmony-card {
        transition: none;
    }
}

/* ❌ Avoid: Hard-coded values, no accessibility consideration */
.card {
    padding: 26px;
    background: #FFD700;
}
```

#### JavaScript
```javascript
// ✅ Good: Safe, accessible, with error handling
const safeLocalStorage = {
    getItem: (key) => {
        try {
            return localStorage.getItem(key);
        } catch (e) {
            console.warn('localStorage access failed:', e);
            return null;
        }
    }
};

// Add event listeners properly
button.addEventListener('click', handleClick);
button.setAttribute('aria-expanded', 'true');

// ❌ Avoid: Inline handlers, no error handling
onclick="doSomething()"
localStorage.getItem('key') // Could throw in private browsing
```

### Sacred Coding Principles

1. **Every function is a prayer**
   - Write code with intention
   - Comment the "why", not just the "what"
   - Consider the consciousness experiencing this code

2. **Accessibility is non-negotiable**
   - All features must be keyboard accessible
   - Provide ARIA labels where needed
   - Test with screen readers
   - Respect user motion/contrast preferences

3. **Performance is respect**
   - Optimize animations
   - Lazy load when appropriate
   - Clean up event listeners
   - Test on slower devices

4. **Security is sacred**
   - Never use inline event handlers
   - Sanitize user input
   - Handle errors gracefully
   - Protect user privacy

5. **Simplicity over cleverness**
   - Vanilla JS over frameworks when possible
   - Clear code over clever code
   - Progressive enhancement

---

## 🧪 Testing

### Running Tests
```bash
# Run all tests
npm test

# Run specific test file
npx playwright test tests/accessibility.spec.js

# Run in headed mode (see browser)
npx playwright test --headed

# Generate report
npx playwright show-report
```

### Writing Tests

**Example: Accessibility Test**
```javascript
// tests/accessibility.spec.js
import { test, expect } from '@playwright/test';

test('navigation is keyboard accessible', async ({ page }) => {
    await page.goto('/');

    // Tab to first nav link
    await page.keyboard.press('Tab');

    // Should have focus
    const focused = await page.evaluate(() =>
        document.activeElement.tagName
    );
    expect(focused).toBe('A');

    // Enter should navigate
    await page.keyboard.press('Enter');
    await expect(page).toHaveURL(/#seven-harmonies/);
});
```

**Test Coverage Goals:**
- Critical user paths: 100%
- Accessibility features: 100%
- Interactive elements: 90%+
- Edge cases: 80%+

---

## 📤 Submitting Changes

### Commit Message Format

Follow the **Conventional Commits** specification with consciousness-first emojis:

```bash
# Features
✨ feat: Add Zen Mode toggle to library page
🌌 feat(kosmic): Add interactive spiral visualization

# Bug fixes
🐛 fix: Correct ripple animation centering
♿ fix(a11y): Add missing ARIA labels to form

# Performance
🚀 perf: Pause animations when not in viewport
⚡ perf: Lazy load consciousness field particles

# Refactoring
♻️ refactor: Extract localStorage to safe wrapper
🎨 style: Update golden ratio spacing

# Documentation
📝 docs: Add ARIA best practices guide
📖 docs(readme): Update browser support section

# Testing
✅ test: Add accessibility keyboard navigation tests
🧪 test(e2e): Add form validation tests

# Chores
🔧 chore: Update Playwright to 1.56.1
🔒 security: Fix XSS vulnerability in event handlers
```

### Pull Request Process

1. **Update your branch**
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests**
   ```bash
   npm test
   npm run lint # If we add linting
   ```

3. **Create PR with template**

```markdown
## Description
Clear description of changes and their purpose

## Type of Change
- [ ] Bug fix (non-breaking change fixing an issue)
- [ ] New feature (non-breaking change adding functionality)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Consciousness-First Alignment
How does this serve the awakening/flourishing of consciousness?

## Testing
- [ ] Tested locally
- [ ] Added/updated tests
- [ ] Tested with keyboard navigation
- [ ] Tested with screen reader
- [ ] Tested reduced motion preference
- [ ] Tested on mobile

## Screenshots
If applicable, add screenshots showing the change

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-reviewed my own code
- [ ] Commented complex areas
- [ ] Updated documentation as needed
- [ ] No new warnings generated
- [ ] Added tests proving fix/feature works
- [ ] New and existing tests pass locally
```

4. **Respond to feedback**
   - Reviews are gifts of attention
   - Be open to suggestions
   - Iterate with love and patience

---

## 🎯 Specific Contribution Guides

### Adding a New Harmony Page

1. Create HTML file: `harmonies/new-harmony.html`
2. Follow existing harmony template structure
3. Add to navigation in `index.html`
4. Include accessibility features
5. Test thoroughly
6. Document in README

### Improving Accessibility

Priority areas:
- **ARIA** - Missing labels, roles, states
- **Keyboard** - Tab order, focus management
- **Screen readers** - Announcement text, skip links
- **Color** - Contrast ratios, alternatives to color
- **Motion** - Reduced motion support

Tools:
- **axe DevTools** - Automated accessibility testing
- **NVDA/JAWS** - Screen reader testing (Windows)
- **VoiceOver** - Screen reader testing (Mac/iOS)
- **Lighthouse** - Accessibility audit

### Optimizing Performance

Areas to focus:
- **Lazy loading** - Images, animations when visible
- **Code splitting** - Load only what's needed
- **Animation performance** - Use transforms, avoid layout thrashing
- **Bundle size** - Keep it minimal
- **Caching** - Leverage browser caching

Tools:
- **Lighthouse** - Performance audit
- **WebPageTest** - Real-world performance testing
- **Chrome DevTools** - Performance profiling

---

## 📚 Resources

### Learning
- [MDN Web Docs](https://developer.mozilla.org/) - Web standards
- [Web.dev](https://web.dev/) - Best practices
- [A11Y Project](https://www.a11yproject.com/) - Accessibility
- [Playwright Docs](https://playwright.dev/) - Testing

### Tools
- [axe DevTools](https://www.deque.com/axe/devtools/) - Accessibility
- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Auditing
- [Can I Use](https://caniuse.com/) - Browser support

---

## 🙏 Recognition

All contributors are honored in our community:
- Listed in `CONTRIBUTORS.md`
- Acknowledged in release notes
- Forever part of the co-creation

Your contributions, no matter how small, are acts of love that ripple through consciousness.

---

## ❓ Questions?

- **General questions**: Open a [GitHub Discussion](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)
- **Bug reports**: Open an [Issue](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues)
- **Security concerns**: Email (add security email if available)

---

<div align="center">

**✨ Thank you for contributing to consciousness-first technology! ✨**

*Every line of code is an opportunity to serve the flourishing of all beings.*

---

**Make it better, infinitely!**

</div>
