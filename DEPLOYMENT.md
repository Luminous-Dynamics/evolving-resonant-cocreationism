# 🚀 Deployment Guide

> **Complete guide to deploying The Luminous Library**

---

## 📋 Overview

The Luminous Library uses **GitHub Pages** for hosting, with **GitHub Actions** for automated deployment.

**Current Setup:**
- **Hosting**: GitHub Pages
- **Domain**: evolvingresonantcocreationism.com
- **SSL**: Automatic via GitHub Pages
- **CDN**: GitHub's global CDN
- **Cost**: Free ✅

---

## 🎯 Deployment Methods

### Method 1: Automatic Deployment (Recommended)

**Every push to `main` automatically deploys.**

```bash
# 1. Merge your PR to main
# 2. GitHub Actions runs automatically
# 3. Site updates in 1-2 minutes
# 4. Visit https://evolvingresonantcocreationism.com
```

**GitHub Actions Workflow** (`.github/workflows/deploy.yml`):
- Triggers on push to `main`
- Runs tests first (via `test.yml`)
- Builds static site
- Deploys to GitHub Pages
- Updates in ~2 minutes

**Monitor deployment:**
1. Go to [Actions tab](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/actions)
2. Click latest "Deploy to GitHub Pages" run
3. Watch progress in real-time

### Method 2: Manual Deployment

**Trigger deployment without code changes:**

1. Go to [Actions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/actions)
2. Click "Deploy to GitHub Pages" workflow
3. Click "Run workflow" dropdown
4. Select branch: `main`
5. Click "Run workflow" button

Useful for:
- Re-deploying after configuration changes
- Testing deployment process
- Recovering from failed deployments

---

## 🏗️ Deployment Architecture

```
┌─────────────────┐
│  Developer      │
│  Push to main   │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  GitHub Actions             │
│  ┌───────────────────────┐  │
│  │ 1. Checkout code      │  │
│  │ 2. Run tests          │  │
│  │ 3. Validate quality   │  │
│  │ 4. Build (if needed)  │  │
│  │ 5. Upload artifact    │  │
│  │ 6. Deploy to Pages    │  │
│  └───────────────────────┘  │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  GitHub Pages               │
│  • Serves static files      │
│  • HTTPS automatic          │
│  • Global CDN               │
│  • Custom domain support    │
└──────────┬──────────────────┘
           │
           ▼
┌─────────────────────────────┐
│  evolvingresonantcocreationism.com │
│  Users access site          │
└─────────────────────────────┘
```

---

## ⚙️ Configuration

### GitHub Pages Settings

**Already configured ✅**

Location: Repository Settings → Pages

- **Source**: GitHub Actions
- **Custom domain**: evolvingresonantcocreationism.com
- **Enforce HTTPS**: ✅ Enabled
- **Branch**: Deployed from `main` via Actions

### DNS Configuration

**Already configured ✅**

See [DNS_SETUP.md](DNS_SETUP.md) for details.

Current DNS records:
```
A     @     185.199.108.153
A     @     185.199.109.153
A     @     185.199.110.153
A     @     185.199.111.153
CNAME www   luminous-dynamics.github.io
```

### CNAME File

Located at `/CNAME`:
```
evolvingresonantcocreationism.com
```

**Important**: Never delete this file or domain will break!

---

## 🔄 Deployment Workflow

### Standard Release Process

1. **Develop on feature branch**
   ```bash
   git checkout -b feature/amazing-improvement
   # Make changes
   git add .
   git commit -m "Add amazing improvement"
   git push origin feature/amazing-improvement
   ```

2. **Create Pull Request**
   - Open PR on GitHub
   - Automated tests run
   - Request review

3. **Code Review**
   - Address feedback
   - Ensure tests pass
   - Get approval

4. **Merge to Main**
   ```bash
   # Via GitHub UI: Click "Merge pull request"
   # Or via command line:
   git checkout main
   git merge feature/amazing-improvement
   git push origin main
   ```

5. **Automatic Deployment**
   - GitHub Actions triggers
   - Tests run again
   - Deploys to production
   - Monitor at [Actions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/actions)

6. **Verify Deployment**
   - Visit https://evolvingresonantcocreationism.com
   - Check changes appear
   - Test functionality

### Hotfix Process

For urgent fixes:

```bash
# 1. Create hotfix branch from main
git checkout main
git pull origin main
git checkout -b hotfix/critical-issue

# 2. Make minimal fix
# Edit files
git add .
git commit -m "Fix critical issue"

# 3. Push and create PR
git push origin hotfix/critical-issue

# 4. Fast-track review and merge
# 5. Monitor deployment
```

---

## 🧪 Pre-Deployment Checklist

Before merging to `main`:

### Code Quality
- [ ] All tests pass (`npm test`)
- [ ] Code formatted (`npm run format`)
- [ ] No console errors
- [ ] No TypeScript/lint errors

### Functionality
- [ ] Changes work locally
- [ ] Tested in multiple browsers
- [ ] Mobile responsive
- [ ] Accessibility maintained

### Content
- [ ] No typos or grammar errors
- [ ] Links work correctly
- [ ] Images load properly
- [ ] Meta tags updated (if needed)

### Documentation
- [ ] README updated (if needed)
- [ ] CHANGELOG updated
- [ ] Comments added/updated
- [ ] Breaking changes noted

### Security
- [ ] No sensitive data committed
- [ ] Dependencies updated
- [ ] No security warnings
- [ ] XSS/injection prevention verified

---

## 🔍 Monitoring Deployment

### Check Deployment Status

**GitHub Actions**:
```
1. Go to: https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/actions
2. Look for green checkmark (✅) or red X (❌)
3. Click to view details
```

**Deployment URL**:
```
After successful deploy:
https://evolvingresonantcocreationism.com
```

### Deployment Artifacts

GitHub Actions uploads:
- Test results
- Playwright reports
- Lighthouse reports
- JUnit XML

Access via Actions → Workflow run → Artifacts

### Deployment Time

| Stage | Duration |
|-------|----------|
| Checkout | ~10s |
| Install deps | ~30s |
| Run tests | ~2-3min |
| Deploy | ~1min |
| **Total** | **~4-5min** |

---

## 🐛 Troubleshooting Deployments

### Problem: Deployment Failed

**Check GitHub Actions logs:**
1. Go to [Actions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/actions)
2. Click failed workflow
3. Expand failed step
4. Read error message

**Common causes:**
- Tests failed → Fix tests
- Build errors → Check syntax
- Permission issues → Check repo settings
- Network timeout → Retry deployment

### Problem: Site Not Updating

**Possible causes:**

1. **Deployment still running**
   - Wait 5 minutes
   - Check Actions tab

2. **Browser cache**
   - Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
   - Clear browser cache

3. **CDN cache**
   - GitHub Pages CDN caches for ~10 minutes
   - Wait up to 10 minutes

4. **Wrong branch deployed**
   - Verify main branch has your changes
   - Check Actions deployed from main

### Problem: Custom Domain Not Working

**Check DNS:**
```bash
# Check DNS propagation
dig evolvingresonantcocreationism.com

# Should return GitHub Pages IPs:
# 185.199.108.153
# 185.199.109.153
# 185.199.110.153
# 185.199.111.153
```

**Check GitHub Settings:**
1. Settings → Pages
2. Verify custom domain: `evolvingresonantcocreationism.com`
3. Verify HTTPS enforced

**Wait for DNS propagation:**
- Can take up to 48 hours
- Usually completes in 1-2 hours
- Use [whatsmydns.net](https://www.whatsmydns.net/) to check

### Problem: HTTPS Certificate Error

**GitHub generates certificates automatically**

If you see errors:
1. Wait 24 hours after domain setup
2. Uncheck "Enforce HTTPS" in settings
3. Wait 5 minutes
4. Re-check "Enforce HTTPS"
5. Wait for certificate generation

---

## 🌐 Alternative Deployment Options

While we use GitHub Pages, the site can deploy anywhere:

### Netlify

```bash
# 1. Create account on netlify.com
# 2. Connect GitHub repo
# 3. Configure:
Build command: (none - static site)
Publish directory: .
# 4. Deploy!
```

**Benefits:**
- Preview deployments for PRs
- More custom headers
- Functions support
- Analytics

### Vercel

```bash
# 1. Create account on vercel.com
# 2. Import Git repository
# 3. Configure:
Framework Preset: Other
Root Directory: ./
# 4. Deploy!
```

**Benefits:**
- Instant deployments
- Automatic HTTPS
- Edge network
- Analytics

### Self-Hosted

```bash
# On any web server:

# 1. Clone repository
git clone https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism.git
cd evolving-resonant-cocreationism

# 2. Serve with any static server
python -m http.server 8000
# Or: npx serve .
# Or: nginx pointing to directory

# 3. Configure domain/HTTPS (nginx, Apache, etc.)
```

**Benefits:**
- Full control
- Custom server configuration
- No vendor lock-in

---

## 📊 Deployment Metrics

### Performance Budgets

Enforced via Lighthouse CI (`.github/lighthouse/budget.json`):

| Metric | Budget | Current |
|--------|--------|---------|
| First Contentful Paint | < 2.0s | ~1.2s ✅ |
| Largest Contentful Paint | < 2.5s | ~1.8s ✅ |
| Total Blocking Time | < 300ms | ~150ms ✅ |
| Cumulative Layout Shift | < 0.1 | ~0.02 ✅ |
| Total Page Size | < 500KB | ~350KB ✅ |

### Uptime

**Target**: 99.9% uptime

**Monitoring**: GitHub Pages status
- https://www.githubstatus.com

**Historical uptime**: Excellent (GitHub Pages is highly reliable)

---

## 🔐 Security Considerations

### Deployment Security

**Automated checks:**
- Dependabot security updates
- GitHub security scanning
- Workflow permission restrictions

**Manual checks:**
- Review all PRs before merging
- Verify no secrets in code
- Check dependencies regularly

### HTTPS

**Always enforced:**
- Automatic via GitHub Pages
- TLS 1.2+ required
- Certificate auto-renewal

### Headers

GitHub Pages automatically provides:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Strict-Transport-Security` (HSTS)

---

## 📅 Release Schedule

### Regular Releases

**Current pace**: As needed
- Bug fixes: Immediate
- Features: Weekly-monthly
- Major versions: Quarterly

See [ROADMAP.md](ROADMAP.md) for planned releases.

### Version Numbers

Follow [Semantic Versioning](https://semver.org):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes

Current: **v1.0.0**

---

## 📝 Post-Deployment Tasks

After successful deployment:

1. **Verify Functionality**
   - [ ] Site loads correctly
   - [ ] New features work
   - [ ] No broken links
   - [ ] Forms submit properly
   - [ ] PWA installs correctly

2. **Update Documentation**
   - [ ] Update CHANGELOG.md
   - [ ] Tag release (if applicable)
   - [ ] Close related issues
   - [ ] Update project board

3. **Announce**
   - [ ] Post on Ko-fi (if significant)
   - [ ] Update GitHub Discussions
   - [ ] Social media (if major release)

4. **Monitor**
   - [ ] Check analytics (if enabled)
   - [ ] Watch for error reports
   - [ ] Monitor GitHub Issues

---

## 🆘 Getting Help

### Deployment Issues
- [Troubleshooting Guide](TROUBLESHOOTING.md)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [GitHub Actions Docs](https://docs.github.com/en/actions)

### Questions
- [GitHub Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)
- Email: tristan@terra-lumina.com

---

**Last Updated**: November 16, 2025

*Deploy with confidence, co-create with care.* 🚀✨
