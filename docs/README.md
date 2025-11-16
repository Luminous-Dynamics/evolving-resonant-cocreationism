# 📚 Documentation Hub

Welcome to The Luminous Library documentation center. All our documentation is designed to serve consciousness-first development while maintaining professional standards.

---

## 🎯 Quick Navigation

### For Users
- **[Main Website](https://evolvingresonantcocreationism.com)** - Experience the philosophy
- **[Seven Harmonies](https://evolvingresonantcocreationism.com/#harmonies)** - Core teachings
- **[Kosmic Theory](https://evolvingresonantcocreationism.com/#kosmic-theory)** - Philosophical foundation
- **[Support the Project](https://evolvingresonantcocreationism.com/support.html)** - Ko-fi donations

### For Contributors
- **[Contributing Guide](../CONTRIBUTING.md)** - How to contribute
- **[Code of Conduct](../CODE_OF_CONDUCT.md)** - Community standards
- **[Development Setup](#development-setup)** - Get started quickly

### For Developers
- **[Architecture](../ARCHITECTURE.md)** - Technical design and decisions
- **[Testing Guide](../TESTING.md)** - How to run and write tests
- **[Performance](../PERFORMANCE.md)** - Optimization strategies
- **[Accessibility](../ACCESSIBILITY.md)** - WCAG 2.1 AA compliance

### For Maintainers
- **[Roadmap](../ROADMAP.md)** - Project vision and timeline
- **[Security Policy](../SECURITY.md)** - Vulnerability reporting
- **[Project Status](../PROJECT_STATUS.md)** - Health dashboard
- **[Changelog](../CHANGELOG.md)** - Version history

---

## 📖 Complete Documentation Index

### Core Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [README.md](../README.md) | Project overview and quick start | Everyone |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | Contribution guidelines | Contributors |
| [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | Community standards | Everyone |
| [LICENSE](../LICENSE) | CC-BY-SA-4.0 license | Everyone |

### Technical Documentation

| Document | Purpose | Audience |
|----------|---------|----------|
| [ARCHITECTURE.md](../ARCHITECTURE.md) | System design and tech stack | Developers |
| [TESTING.md](../TESTING.md) | Test strategy and guides | Developers |
| [PERFORMANCE.md](../PERFORMANCE.md) | Performance optimization | Developers |
| [ACCESSIBILITY.md](../ACCESSIBILITY.md) | A11y features and compliance | Developers/Users |

### Project Management

| Document | Purpose | Audience |
|----------|---------|----------|
| [ROADMAP.md](../ROADMAP.md) | Future vision (2026-2030) | Everyone |
| [CHANGELOG.md](../CHANGELOG.md) | Version history | Everyone |
| [PROJECT_STATUS.md](../PROJECT_STATUS.md) | Current health metrics | Maintainers |
| [SECURITY.md](../SECURITY.md) | Security policy | Security researchers |

### Community

| Document | Purpose | Audience |
|----------|---------|----------|
| [CONTRIBUTORS.md](../CONTRIBUTORS.md) | Contributor recognition | Contributors |
| [humans.txt](../humans.txt) | Team attribution | Web crawlers |

---

## 🚀 Development Setup

### Prerequisites

```bash
# Node.js 20+ (check with node --version)
node --version

# npm 9+ (check with npm --version)
npm --version
```

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism.git
cd evolving-resonant-cocreationism

# 2. Install dependencies and Playwright browsers
npm run setup

# 3. Start local development server
npm run serve
# Open http://localhost:8000

# 4. Run tests
npm test

# 5. View test report
npm run test:report
```

### Available NPM Scripts

```bash
# Development
npm run serve          # Start local server (port 8000)
npm run dev            # Alias for serve
npm start              # Alias for serve

# Testing
npm test               # Run all tests
npm run test:headed    # Run tests with browser visible
npm run test:ui        # Open Playwright test UI
npm run test:debug     # Debug tests
npm run test:accessibility   # Run only accessibility tests
npm run test:core              # Run only core functionality tests
npm run test:performance       # Run only performance tests
npm run test:report    # View last test report

# Code Quality
npm run validate       # Run all tests and validation
npm run format         # Format all code with Prettier
npm run format:check   # Check code formatting
npm run precommit      # Format + validate (run before commits)

# Performance
npm run lighthouse            # Instructions for production audit
npm run lighthouse:local      # Audit local development build

# Utilities
npm run setup          # Install deps + Playwright browsers
npm run clean          # Remove test artifacts
npm run info           # Show version information
```

---

## 🧪 Testing

### Test Suites

1. **Accessibility Tests** (`tests/accessibility.spec.js`)
   - WCAG 2.1 AA compliance
   - Keyboard navigation
   - Screen reader compatibility
   - ARIA attributes

2. **Core Functionality Tests** (`tests/core-functionality.spec.js`)
   - Page loading
   - Navigation
   - Interactive features
   - Meta tags

3. **Performance Tests** (`tests/performance.spec.js`)
   - Load times
   - Responsive design
   - Console errors
   - User preferences

### Running Tests

```bash
# All tests across 6 browser/device configurations
npm test

# Watch mode with browser visible
npm run test:headed

# Interactive UI mode
npm run test:ui

# Specific test suite
npm run test:accessibility
npm run test:core
npm run test:performance

# Debug a specific test
npm run test:debug -- tests/accessibility.spec.js
```

---

## 📝 Writing Documentation

### Documentation Principles

1. **Clarity First**: Write for someone new to the project
2. **Examples Included**: Show, don't just tell
3. **Maintained**: Keep docs updated with code changes
4. **Cross-linked**: Reference related documentation
5. **Accessible**: Use clear language, avoid jargon
6. **Consciousness-First**: Align with project values

### Documentation Style Guide

```markdown
# Use H1 for document title (only one per file)

## H2 for major sections

### H3 for subsections

- Use bullet points for lists
- Keep paragraphs short (3-5 sentences)
- Include code examples in fenced blocks
- Add emoji sparingly for visual scanning
- Use tables for structured comparisons
```

### Where to Document What

| Type | Location |
|------|----------|
| **API changes** | CHANGELOG.md |
| **New features** | README.md + ROADMAP.md |
| **Technical decisions** | ARCHITECTURE.md |
| **Setup instructions** | CONTRIBUTING.md |
| **Bug fixes** | CHANGELOG.md + PR description |
| **Breaking changes** | CHANGELOG.md (prominently) |
| **Security issues** | SECURITY.md |

---

## 🎯 Documentation Goals

### Current (v1.0)
- ✅ Complete core documentation (14 files)
- ✅ Technical architecture documented
- ✅ Accessibility compliance documented
- ✅ Testing procedures documented
- ✅ Contribution guidelines clear

### Near Future (v1.1)
- [ ] API documentation (when API added)
- [ ] Video tutorials
- [ ] Interactive guides
- [ ] Translations (Spanish, French, Mandarin)
- [ ] Simplified language versions

### Long Term (v2.0+)
- [ ] Developer portal
- [ ] Interactive documentation
- [ ] Community wiki
- [ ] Best practices catalog
- [ ] Case studies

---

## 🔗 External Resources

### Learn More About

- **Evolving Resonant Co-creationism**: [Website](https://evolvingresonantcocreationism.com)
- **Tristan's Work**: [Terra Lumina](https://terra-lumina.com)
- **Support**: [Ko-fi](https://ko-fi.com/luminousdynamics)
- **Issues**: [GitHub Issues](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)

### Technologies

- **Playwright**: [Documentation](https://playwright.dev)
- **WCAG 2.1**: [Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- **GitHub Pages**: [Documentation](https://docs.github.com/en/pages)
- **PWA**: [Web.dev Guide](https://web.dev/progressive-web-apps/)

---

## 💜 Philosophy of Documentation

> "Every document is an invitation to co-create."

Our documentation embodies consciousness-first principles:

- **Accessible**: Written for all skill levels
- **Welcoming**: Assumes good faith and curiosity
- **Comprehensive**: Covers the "why" not just the "how"
- **Living**: Updated regularly, never stale
- **Beautiful**: Well-formatted, pleasant to read
- **Truthful**: Honest about limitations and challenges
- **Generous**: Gives more than expected

---

## 📞 Documentation Questions?

- **Typos/Errors**: [Open an Issue](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues/new)
- **Suggestions**: [Start a Discussion](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)
- **Urgent**: Email tristan@terra-lumina.com

---

**Last Updated**: November 16, 2025

*Documentation written with love and attention.* 📚✨
