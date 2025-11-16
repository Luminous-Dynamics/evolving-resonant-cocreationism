# ⚡ Quick Start Guide

> **Get up and running with The Luminous Library in under 5 minutes.**

---

## 🎯 For Users

### Just Want to Read?

Visit **[evolvingresonantcocreationism.com](https://evolvingresonantcocreationism.com)**

No setup required! The site works on all devices and browsers.

### Want to Install as an App?

**Desktop**:
1. Visit the website in Chrome, Edge, or Safari
2. Look for the install icon in the address bar
3. Click "Install"

**Mobile**:
1. Visit the website in your mobile browser
2. Tap the "Share" or "Menu" button
3. Select "Add to Home Screen"

Now you have an app icon and offline access!

---

## 🛠️ For Contributors

### Prerequisites

- **Node.js 18+** ([download](https://nodejs.org))
- **Git** ([download](https://git-scm.com))
- **Code editor** (we recommend [VS Code](https://code.visualstudio.com))

Check your versions:
```bash
node --version  # Should be 18.0.0 or higher
npm --version   # Should be 9.0.0 or higher
git --version   # Any recent version is fine
```

### One-Command Setup

```bash
# Clone the repository
git clone https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism.git
cd evolving-resonant-cocreationism

# Install everything (dependencies + Playwright browsers)
npm run setup

# Start the development server
npm run serve

# Open http://localhost:8000 in your browser
```

**Done!** The site is running locally.

---

## 🧪 Running Tests

```bash
# Run all tests (40+ tests across 6 browsers/devices)
npm test

# Open interactive test UI
npm run test:ui

# Run tests with browser visible
npm run test:headed
```

Tests take 2-3 minutes to complete.

---

## ✏️ Making Changes

### 1. Create a Branch

```bash
git checkout -b your-feature-name
```

### 2. Make Your Changes

Edit files in your code editor. Common files:
- `index.html` - Homepage
- `css/main.css` - Styles
- `js/main.js` - Interactive features
- Any markdown file for documentation

### 3. Test Your Changes

```bash
# Format your code
npm run format

# Run tests
npm test
```

### 4. Commit and Push

```bash
git add .
git commit -m "Brief description of your changes"
git push origin your-feature-name
```

### 5. Create a Pull Request

1. Go to [GitHub](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism)
2. Click "Pull requests" → "New pull request"
3. Select your branch
4. Fill out the template
5. Submit!

We'll review and provide feedback.

---

## 🎨 Using VS Code? (Recommended)

### First Time Setup

```bash
# Open the project in VS Code
code .
```

VS Code will prompt you to:
1. **Install recommended extensions** - Click "Install All"
2. **Use workspace settings** - Already configured!

Extensions we recommend:
- Prettier (code formatting)
- Playwright (test running)
- GitLens (git integration)
- Live Server (live preview)

### Quick Commands in VS Code

- **Format document**: `Shift + Alt + F` (Windows/Linux) or `Shift + Option + F` (Mac)
- **Open integrated terminal**: `` Ctrl + ` ``
- **Run tests**: Click "Testing" icon in sidebar

---

## 📝 Common Tasks

### Local Development

```bash
npm run serve        # Start server
npm run dev          # Same as serve
npm start            # Also same
```

Server runs at `http://localhost:8000`

### Testing

```bash
npm test                    # All tests
npm run test:accessibility  # Accessibility tests only
npm run test:core           # Core functionality tests only
npm run test:performance    # Performance tests only
npm run test:report         # View last test report
```

### Code Quality

```bash
npm run format          # Format all code with Prettier
npm run format:check    # Check if code is formatted
npm run validate        # Format + run all tests
npm run precommit       # Run before committing
```

### Performance

```bash
npm run lighthouse        # Instructions for production audit
npm run lighthouse:local  # Audit local development version
```

### Cleanup

```bash
npm run clean   # Remove test artifacts and cache
```

### Info

```bash
npm run info    # Show version information
```

---

## 📚 Key Documentation

Quick links to essential docs:

| Need | Read |
|------|------|
| **How to contribute** | [CONTRIBUTING.md](CONTRIBUTING.md) |
| **Code standards** | [CONTRIBUTING.md](CONTRIBUTING.md#code-style) |
| **Run tests** | [TESTING.md](TESTING.md) |
| **Architecture** | [ARCHITECTURE.md](ARCHITECTURE.md) |
| **Accessibility** | [ACCESSIBILITY.md](ACCESSIBILITY.md) |
| **Common questions** | [FAQ.md](FAQ.md) |
| **All documentation** | [docs/README.md](docs/README.md) |

---

## 🐛 Troubleshooting

### Port 8000 already in use?

```bash
# Use a different port
python -m http.server 8080
# Then visit http://localhost:8080
```

### Tests failing?

```bash
# Reinstall Playwright browsers
npx playwright install --with-deps

# Clear cache and retry
npm run clean
npm test
```

### Git issues?

```bash
# Reset to latest main
git fetch origin
git reset --hard origin/main

# Start fresh
git checkout -b new-branch-name
```

### VS Code not showing recommended extensions?

1. Press `Ctrl + Shift + P` (Windows/Linux) or `Cmd + Shift + P` (Mac)
2. Type "Show Recommended Extensions"
3. Select and install

---

## 💬 Get Help

### Quick Questions
- [FAQ.md](FAQ.md) - Check here first
- [GitHub Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)

### Bug Reports
- [Open an Issue](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues/new?template=bug_report.md)

### Direct Contact
- Email: tristan@terra-lumina.com

---

## ✨ First Contribution Ideas

New to the project? Try these beginner-friendly tasks:

1. **Fix a typo** in documentation
2. **Improve a comment** in code
3. **Add a test** for existing functionality
4. **Enhance documentation** with examples
5. **Report a bug** you found

Look for issues tagged [`good first issue`](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/labels/good%20first%20issue).

---

## 🎉 You're Ready!

You now have everything you need to:
- ✅ Run the site locally
- ✅ Make changes
- ✅ Test your work
- ✅ Submit contributions

**Welcome to The Luminous Library community!** 💜

---

**Last Updated**: November 16, 2025

*Make it better, infinitely!* ⚡✨
