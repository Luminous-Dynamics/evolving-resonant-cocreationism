# 🔧 Troubleshooting Guide

> **Solutions to common issues when working with The Luminous Library**

---

## 🎯 Quick Troubleshooting

**Before diving into specific issues:**

1. **Update everything**: `npm run setup`
2. **Clear artifacts**: `npm run clean`
3. **Check versions**: `npm run info`
4. **Restart server**: Stop and run `npm run serve` again

If still stuck, search existing [GitHub Issues](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues) or jump to specific sections below.

---

## 📦 Installation Issues

### Problem: `npm install` fails

**Symptoms:**
- Error messages during installation
- Missing dependencies
- Permission errors

**Solutions:**

```bash
# 1. Clear npm cache
npm cache clean --force

# 2. Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# 3. Reinstall
npm install

# 4. If permission errors on Linux/Mac
sudo chown -R $USER ~/.npm
npm install
```

### Problem: `npm run setup` fails during Playwright installation

**Symptoms:**
- "Failed to download browser" error
- Network timeout errors

**Solutions:**

```bash
# 1. Set Playwright download timeout (in seconds)
export PLAYWRIGHT_DOWNLOAD_TIMEOUT=120000

# 2. Retry installation
npx playwright install --with-deps

# 3. If behind proxy, configure:
export HTTPS_PROXY=http://your-proxy:port
npx playwright install --with-deps

# 4. Manual browser installation (one at a time)
npx playwright install chromium
npx playwright install firefox
npx playwright install webkit
```

### Problem: Wrong Node.js version

**Symptoms:**
- "Engine version mismatch" error
- Features not working

**Solutions:**

```bash
# Check current version
node --version

# Install correct version (Node 18+)
# Using nvm (recommended):
nvm install 20
nvm use 20

# Or download from nodejs.org
```

---

## 🧪 Testing Issues

### Problem: All tests fail with "Cannot connect to server"

**Symptoms:**
- Tests timeout
- "ERR_CONNECTION_REFUSED" errors

**Solutions:**

```bash
# Tests expect server on localhost:8000
# Start server before tests:
npm run serve &

# Then in another terminal:
npm test

# Or use test:ui which handles this automatically
npm run test:ui
```

### Problem: Playwright browsers not found

**Symptoms:**
- "Executable doesn't exist" error
- Browser launch failures

**Solutions:**

```bash
# Reinstall all browsers
npx playwright install --with-deps

# If specific browser missing:
npx playwright install chromium --with-deps
```

### Problem: Tests pass locally but fail in CI

**Symptoms:**
- GitHub Actions shows failures
- Local tests pass fine

**Solutions:**

1. **Check viewport differences**: CI may use different screen sizes
2. **Check timing issues**: CI is slower, add longer timeouts
3. **Check dependencies**: Ensure `package-lock.json` is committed
4. **Review logs**: Check GitHub Actions artifacts for screenshots

```javascript
// In test files, increase timeouts for CI:
test('slow operation', async ({ page }) => {
    await page.goto('/', { timeout: 10000 }); // Increase from default
});
```

### Problem: Specific test fails intermittently

**Symptoms:**
- Test passes sometimes, fails other times
- "Timeout" or "Element not found" errors

**Solutions:**

```javascript
// Add explicit waits instead of fixed timeouts:

// ❌ Bad (timing-dependent)
await page.waitForTimeout(1000);

// ✅ Good (condition-dependent)
await page.waitForSelector('.element');
await expect(page.locator('.element')).toBeVisible();

// ✅ Better (with timeout)
await page.waitForSelector('.element', { timeout: 5000 });
```

---

## 🌐 Server Issues

### Problem: Port 8000 already in use

**Symptoms:**
- "Address already in use" error
- Server won't start

**Solutions:**

```bash
# Option 1: Find and kill process using port 8000
# On Linux/Mac:
lsof -ti:8000 | xargs kill -9

# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Option 2: Use different port
python -m http.server 8080
# Then visit http://localhost:8080

# Option 3: Use Node's http-server
npx http-server -p 8000
```

### Problem: Changes not showing up in browser

**Symptoms:**
- Edit files but see old version
- CSS/JS changes not appearing

**Solutions:**

1. **Hard refresh** browser:
   - Chrome/Firefox: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
   - Safari: `Cmd+Option+R`

2. **Clear browser cache**:
   - Open DevTools (F12)
   - Right-click refresh button
   - Select "Empty Cache and Hard Reload"

3. **Disable Service Worker** (if installed as PWA):
   - DevTools → Application → Service Workers
   - Click "Unregister"

4. **Check file actually saved**:
   - Look for unsaved indicator in editor
   - Run `git status` to confirm changes

---

## 💻 VS Code Issues

### Problem: Recommended extensions not showing

**Symptoms:**
- VS Code doesn't prompt to install extensions
- Extensions list is empty

**Solutions:**

```bash
# 1. Open command palette (Ctrl+Shift+P / Cmd+Shift+P)
# 2. Type: "Show Recommended Extensions"
# 3. Install all

# Or manually install via terminal:
code --install-extension esbenp.prettier-vscode
code --install-extension ms-playwright.playwright
code --install-extension eamodio.gitlens
```

### Problem: Prettier not formatting on save

**Symptoms:**
- Code doesn't auto-format
- Formatting is inconsistent

**Solutions:**

1. **Check Prettier is default formatter**:
   - File → Preferences → Settings
   - Search "default formatter"
   - Select "Prettier - Code formatter"

2. **Check format on save enabled**:
   - Settings → Search "format on save"
   - Enable checkbox

3. **Check Prettier extension installed**:
   ```bash
   code --install-extension esbenp.prettier-vscode
   ```

4. **Reload VS Code**:
   - Command Palette → "Reload Window"

### Problem: Workspace settings not applying

**Symptoms:**
- Settings in .vscode/settings.json ignored
- Inconsistent behavior

**Solutions:**

1. **Check settings precedence**: User settings override workspace
   - Command Palette → "Open Workspace Settings (JSON)"
   - Verify .vscode/settings.json is being read

2. **Restart VS Code completely**: Close all windows, reopen

3. **Check for syntax errors** in settings.json:
   - Use JSON validator
   - Look for missing commas, brackets

---

## 🎨 Display & Styling Issues

### Problem: Fonts look different than expected

**Symptoms:**
- System fonts instead of design
- Spacing issues

**Solutions:**

The site uses system fonts intentionally for performance. This is expected behavior. Different operating systems will show different fonts:
- macOS: San Francisco
- Windows: Segoe UI
- Linux: Roboto/system default

This is **by design** for fast loading and native feel.

### Problem: Colors look washed out

**Symptoms:**
- Gradients not vibrant
- Gold looks yellow instead of golden

**Solutions:**

1. **Check browser color management**:
   - Some browsers apply color profiles
   - Try different browser to compare

2. **Check monitor calibration**:
   - Display settings may affect colors
   - Compare on different devices

3. **Check high contrast mode not enabled**:
   - System accessibility settings
   - Browser forced colors mode

### Problem: Animations not working

**Symptoms:**
- Consciousness field static
- No hover effects
- Ripples not appearing

**Solutions:**

1. **Check `prefers-reduced-motion`**:
   - This is intentional accessibility feature
   - Users can disable in OS settings
   - On Windows: Settings → Ease of Access → Display → Show animations
   - On macOS: System Preferences → Accessibility → Display → Reduce motion
   - On Linux: Depends on desktop environment

2. **Check JavaScript enabled**:
   - Site requires JavaScript
   - Check browser console for errors

---

## 🔐 Git Issues

### Problem: Can't push to repository

**Symptoms:**
- "Permission denied" errors
- "Authentication failed"

**Solutions:**

```bash
# 1. Check you're on a feature branch, not main
git branch  # Should show your-branch-name, not main

# 2. Set up authentication
# If using HTTPS:
git config --global credential.helper cache

# If using SSH:
# Generate SSH key if needed:
ssh-keygen -t ed25519 -C "your-email@example.com"
# Add to GitHub: Settings → SSH Keys

# 3. Verify remote URL
git remote -v
# Should show: https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism.git
```

### Problem: Merge conflicts

**Symptoms:**
- "CONFLICT" messages
- Conflicting changes

**Solutions:**

```bash
# 1. Update your branch with latest main
git fetch origin
git merge origin/main

# 2. If conflicts, open files and resolve
# Look for:
# <<<<<<< HEAD
# Your changes
# =======
# Their changes
# >>>>>>> origin/main

# 3. After resolving, stage and commit
git add .
git commit -m "Resolve merge conflicts"

# 4. If too complex, start fresh:
git fetch origin
git reset --hard origin/main
git checkout -b new-feature-branch
# Re-apply your changes
```

### Problem: Committed to wrong branch

**Symptoms:**
- Changes on main instead of feature branch
- Committed to wrong feature branch

**Solutions:**

```bash
# If not yet pushed:
# 1. Create new branch from current position
git branch new-feature-branch

# 2. Reset current branch
git reset --hard origin/main

# 3. Switch to new branch
git checkout new-feature-branch

# Your commits are now on new branch!
```

---

## 📱 Mobile/PWA Issues

### Problem: Can't install as app

**Symptoms:**
- No "Install" prompt
- Add to Home Screen not working

**Solutions:**

1. **Check browser support**:
   - Chrome/Edge: ✅ Supported
   - Firefox: ⚠️ Limited support
   - Safari iOS: ✅ Use "Add to Home Screen"

2. **Check HTTPS**: PWAs require HTTPS (or localhost)
   - Production site has HTTPS ✅
   - Local development uses localhost ✅

3. **Check manifest**: Visit `/site.webmanifest`
   - Should load without errors

4. **Clear browser data** and retry

### Problem: App doesn't work offline

**Symptoms:**
- "No internet" when offline
- App doesn't load

**Solutions:**

Currently, full offline support is planned for v1.1. The current version requires internet connection. See [ROADMAP.md](ROADMAP.md) for timeline.

To improve offline experience now:
- Install as PWA (caches some assets)
- Browser's native caching helps

---

## 🐛 Bug Reporting Best Practices

If you've tried everything and still have issues:

### 1. Gather Information

```bash
# Get versions
npm run info

# Get detailed test output
npm test -- --reporter=list > test-output.txt

# Check console errors
# Open DevTools (F12) → Console tab
# Screenshot any errors
```

### 2. Create Minimal Reproduction

- Simplify to smallest case that shows the bug
- Remove unrelated code
- Test in fresh clone if possible

### 3. Open Issue

Use the [Bug Report template](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues/new?template=bug_report.md) and include:

- **Environment**: OS, browser, Node version
- **Steps to reproduce**: Exact steps
- **Expected behavior**: What should happen
- **Actual behavior**: What actually happens
- **Screenshots/logs**: Visual proof
- **Code**: Minimal reproduction

---

## 📚 Additional Resources

### Documentation
- [FAQ](FAQ.md) - Common questions
- [Quick Start](QUICK_START.md) - Fast setup
- [Contributing](CONTRIBUTING.md) - How to contribute
- [Testing](TESTING.md) - Test documentation

### Community Support
- [GitHub Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions) - Ask questions
- [GitHub Issues](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues) - Report bugs
- Email: tristan@terra-lumina.com - Direct contact

### External Resources
- [Playwright Documentation](https://playwright.dev)
- [Node.js Troubleshooting](https://nodejs.org/en/docs/guides/debugging-getting-started/)
- [Git Documentation](https://git-scm.com/doc)

---

## 💡 Prevention Tips

### Before You Start
- [ ] Read [QUICK_START.md](QUICK_START.md)
- [ ] Check [FAQ.md](FAQ.md)
- [ ] Verify Node.js version (18+)
- [ ] Run `npm run setup`

### While Working
- [ ] Save files frequently
- [ ] Run `npm run precommit` before committing
- [ ] Test locally before pushing
- [ ] Keep dependencies updated

### Common Pitfalls
- ❌ Not running server before tests
- ❌ Forgetting to format code
- ❌ Working on main branch instead of feature branch
- ❌ Not reading error messages carefully
- ❌ Skipping setup steps

---

## 🆘 Still Stuck?

**Don't suffer in silence!**

1. **Search existing issues**: Someone may have solved it
2. **Ask in Discussions**: Community can help
3. **Open an issue**: We want to know about problems
4. **Email directly**: tristan@terra-lumina.com

Remember: Questions help improve documentation for everyone!

---

**Last Updated**: November 16, 2025

*Every problem solved makes the path clearer for others.* 🔧✨
