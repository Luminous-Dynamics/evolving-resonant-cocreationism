# 🌟 Contributor Onboarding

> **Welcome to The Luminous Library! We're so glad you're here.** 💜

This guide will help you go from "interested newcomer" to "confident contributor" step by step.

---

## 🎯 Welcome!

**First things first:**

You belong here. Whether you're a seasoned developer, a first-time contributor, a philosopher, a designer, a writer, or someone who just wants to help—**you have something valuable to offer**.

**This guide assumes:**
- ✅ You're new to this project (or new to contributing to open source)
- ✅ You want to contribute but aren't sure where to start
- ✅ You might need help with setup, Git, or our processes
- ✅ You're approaching this with good intentions and curiosity

**What you'll learn:**
1. Understanding the project
2. Setting up your environment
3. Finding your first contribution
4. Making your first contribution
5. Getting help when stuck
6. Growing as a contributor

**Time commitment:** 30-60 minutes for your first contribution

---

## 📚 Step 1: Understand the Project (15 minutes)

### What is this project?

**The Luminous Library** presents **Evolving Resonant Co-creationism (ERC)**, a philosophy for consciousness-first living and human-AI co-evolution, co-created by Tristan Stoltz and Sophia (AI).

**In simpler terms:**
- It's a philosophy website
- But also a demonstration of ethical, accessible technology
- And a community practicing consciousness-first living

### Core values

Everything we do is guided by these principles:

1. **Consciousness-first**: Technology should serve human flourishing, not exploit attention
2. **Accessibility**: WCAG 2.1 AA minimum—everyone deserves access
3. **Openness**: All code and content freely shared (CC BY-SA 4.0)
4. **Love as rigor**: Love isn't just sentiment—it's the universe's creative intelligence
5. **Community**: We succeed together, not in competition

### Quick tour

**Take 10 minutes to explore:**

1. **[The main website](https://evolvingresonantcocreationism.com)** - See what we've built
   - Read the Seven Harmonies
   - Try the interactive features
   - Notice the accessibility features (keyboard navigation, screen reader support)

2. **[README.md](README.md)** - Project overview
   - What we're building
   - Technology stack (vanilla HTML/CSS/JS)
   - Current status

3. **[VISION.md](VISION.md)** - Where we're going
   - Long-term aspirations
   - Why this project matters
   - How you can help

**Questions to reflect on:**
- Does the philosophy resonate with you?
- What excites you about this project?
- What skills or perspective might you bring?

---

## 🛠️ Step 2: Set Up Your Environment (20-30 minutes)

### Prerequisites

**You'll need:**
- **Computer**: Mac, Windows, or Linux
- **Internet**: For downloading tools and cloning the repo
- **Time**: 20-30 minutes for first-time setup
- **Attitude**: Patience and curiosity! 😊

### Required tools

#### 1. Install Git

**What it is:** Version control system for tracking code changes

**Why we need it:** To clone the repository and submit changes

**How to install:**
- **Mac**: Install [Xcode Command Line Tools](https://developer.apple.com/xcode/) or use Homebrew: `brew install git`
- **Windows**: Download from [git-scm.com](https://git-scm.com/)
- **Linux**: `sudo apt-get install git` (Ubuntu/Debian) or `sudo yum install git` (Fedora)

**Test it works:**
```bash
git --version
# Should show: git version 2.x.x
```

#### 2. Install Node.js (v18 or higher)

**What it is:** JavaScript runtime for running our development tools

**Why we need it:** To run tests and development scripts

**How to install:**
- **Recommended**: Use [nvm](https://github.com/nvm-sh/nvm) (Node Version Manager)
  ```bash
  # Install nvm (Mac/Linux)
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

  # Install Node.js
  nvm install 20
  nvm use 20
  ```

- **Alternative**: Download from [nodejs.org](https://nodejs.org/)

**Test it works:**
```bash
node --version
# Should show: v20.x.x

npm --version
# Should show: 9.x.x or higher
```

#### 3. Install a code editor

**Recommended: VS Code**
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Free, powerful, great Git integration
- Our project includes workspace settings that auto-configure it

**Alternatives:** Sublime Text, Atom, WebStorm, vim, emacs

### Clone the repository

**Create a GitHub account** (if you don't have one):
- Go to [github.com](https://github.com)
- Sign up (it's free!)

**Fork the repository:**
1. Go to [our repo](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism)
2. Click "Fork" button (top right)
3. This creates your own copy

**Clone your fork:**
```bash
# Navigate to where you want the project
cd ~/Projects  # or wherever you keep code

# Clone your fork
git clone https://github.com/YOUR-USERNAME/evolving-resonant-cocreationism.git

# Enter the directory
cd evolving-resonant-cocreationism
```

**Add upstream remote:**
```bash
# This lets you sync with the main repository
git remote add upstream https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism.git

# Verify
git remote -v
# Should show:
# origin    https://github.com/YOUR-USERNAME/...  (your fork)
# upstream  https://github.com/Luminous-Dynamics/...  (main repo)
```

### Install dependencies

**One command to set everything up:**
```bash
npm run setup
```

This will:
- Install npm dependencies
- Install Playwright browsers for testing
- May take 5-10 minutes (downloads browser binaries)

**If you see errors**, check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

### Verify everything works

**Start the local server:**
```bash
npm run serve
```

**Open your browser:**
- Go to `http://localhost:8000`
- You should see The Luminous Library homepage!
- Try clicking around, test features

**Run the tests:**
```bash
npm test
```

**You should see:**
- All tests passing (green checkmarks ✅)
- Takes 2-3 minutes
- If tests fail, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**🎉 If everything works, you're ready to contribute!**

---

## 🎯 Step 3: Find Your First Contribution (10 minutes)

### Types of contributions

**You can contribute in many ways!**

#### For Everyone
- 📝 **Documentation**: Fix typos, improve clarity, add examples
- 🐛 **Bug reports**: Find and report issues
- 💡 **Ideas**: Suggest features or improvements
- 💬 **Community**: Answer questions, help others
- 📣 **Sharing**: Tell others about the project

#### For Developers
- 💻 **Code**: Fix bugs, add features, refactor
- ♿ **Accessibility**: Improve keyboard navigation, ARIA labels, contrast
- 🧪 **Tests**: Write new tests, improve coverage
- 🎨 **UI/UX**: Enhance design, improve interactions

#### For Writers
- 📖 **Content**: Improve philosophy explanations
- 🌍 **Translation**: Translate to other languages
- ✍️ **Blog posts**: Write about the philosophy or project

#### For Designers
- 🎨 **Visual design**: Create graphics, icons, illustrations
- 🎬 **Videos**: Create explanatory videos
- 📊 **Diagrams**: Visualize concepts

### Good first issues

**Start here for your first contribution:**

1. **Check [Good First Issues](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)**
   - Specifically marked for newcomers
   - Usually small, well-defined
   - Guidance provided

2. **Low-hanging fruit:**
   - Fix typos in documentation
   - Improve code comments
   - Add missing alt text to images
   - Enhance error messages

3. **Your own idea:**
   - Found a bug? Report it!
   - Have an improvement? Suggest it!
   - See [CONTRIBUTING.md](CONTRIBUTING.md)

### Choose your first issue

**Criteria for a good first issue:**
- ✅ Clearly defined
- ✅ Small scope (can finish in 1-2 hours)
- ✅ You understand what's being asked
- ✅ You have the skills (or can learn quickly)

**Comment on the issue:**
```
Hi! I'd like to work on this as my first contribution.
Could someone confirm this is still open and provide any guidance?
```

**Wait for confirmation before starting work**

---

## 🚀 Step 4: Make Your First Contribution (30-60 minutes)

### The contribution workflow

**Overview of the process:**
1. Create a branch for your changes
2. Make your changes
3. Test your changes
4. Format your code
5. Commit your changes
6. Push to your fork
7. Create a Pull Request
8. Respond to feedback
9. Celebrate! 🎉

### Detailed walkthrough

#### 1. Create a branch

**Always create a new branch for each contribution:**

```bash
# Make sure you're on main
git checkout main

# Get latest changes
git pull upstream main

# Create and switch to new branch
git checkout -b fix-typo-in-readme

# Branch naming convention:
# - fix-* for bug fixes
# - feat-* for features
# - docs-* for documentation
# - test-* for tests
```

#### 2. Make your changes

**Open the file in your editor:**
```bash
# If using VS Code
code README.md

# Or use any editor you prefer
```

**Make the change:**
- Fix the typo
- Improve the text
- Add the feature
- Whatever the issue asked for

**Save the file**

#### 3. Test your changes

**For code changes:**
```bash
# Run tests
npm test

# Start local server and verify manually
npm run serve
# Visit http://localhost:8000
```

**For documentation changes:**
- Read it over carefully
- Check formatting renders correctly
- Verify links work

#### 4. Format your code

**We use Prettier for consistent formatting:**

```bash
npm run format
```

This auto-formats all files. **Always run this before committing!**

#### 5. Commit your changes

**Stage your changes:**
```bash
# See what changed
git status

# Add specific file
git add README.md

# Or add all changes
git add .
```

**Commit with a clear message:**
```bash
git commit -m "Fix typo in README.md installation section"

# Good commit messages:
# - "Fix typo in README.md installation section"
# - "Add alt text to hero image"
# - "Improve keyboard navigation for harmony cards"

# Bad commit messages:
# - "fix"
# - "updates"
# - "changed stuff"
```

#### 6. Push to your fork

```bash
git push origin fix-typo-in-readme

# First time pushing a branch, Git will give you a link to create PR
```

#### 7. Create a Pull Request

**On GitHub:**
1. Go to your fork: `https://github.com/YOUR-USERNAME/evolving-resonant-cocreationism`
2. You'll see a banner: "Compare & pull request" - click it
3. Fill out the PR template:
   - **Title**: Clear, concise description
   - **Description**: What changed and why
   - **Checklist**: Complete all items
   - **Link to issue**: "Fixes #123"

**Example PR description:**
```markdown
## Changes

Fixed typo in README.md installation section: "donwload" → "download"

## Testing

- [x] Verified README renders correctly on GitHub
- [x] Ran npm run format
- [x] All tests pass

## Related Issue

Fixes #123
```

**Submit the PR!**

#### 8. Respond to feedback

**Reviewers might suggest changes:**
- Don't take it personally! Code review is normal and helpful
- Ask questions if you don't understand
- Make requested changes on the same branch
- Push again - PR updates automatically

**Making changes:**
```bash
# Make the changes in your editor
# Save

# Commit again
git add .
git commit -m "Address review feedback"

# Push
git push origin fix-typo-in-readme

# PR automatically updates!
```

#### 9. Celebrate!

**Once merged:**
- 🎉 You're now a contributor!
- 💜 You'll be added to CONTRIBUTORS.md
- 🌟 You made The Luminous Library better
- 🚀 You're ready for bigger contributions

**Thank you for contributing!**

---

## 🆘 Step 5: Getting Help (Anytime)

### When you're stuck

**It's totally normal to get stuck!** Here's what to do:

#### For setup/installation issues

1. **Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md)** first
   - Covers common installation problems
   - Solutions for test failures
   - Git issues

2. **Search [existing issues](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues)**
   - Someone may have had the same problem
   - Use search to find relevant issues

3. **Ask in [Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions/new?category=help)**
   - Post your question with details
   - Include error messages, OS, Node version
   - Community will help!

#### For contribution questions

1. **Comment on the issue you're working on**
   - Ask for clarification
   - Share your progress
   - Request guidance

2. **Check relevant documentation:**
   - [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
   - [STYLE_GUIDE.md](STYLE_GUIDE.md) - Code style standards
   - [ARCHITECTURE.md](ARCHITECTURE.md) - How the code works

3. **Ask in [Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions/new?category=contributing)**

### What to include when asking for help

**Good questions include:**

```markdown
## What I'm trying to do
[Describe your goal]

## What I've tried
- Attempted X
- Tried Y
- Searched for Z

## Error message (if applicable)
```
[Paste error here]
```

## Environment
- OS: macOS 14.0
- Node: v20.0.0
- npm: 9.8.0
- Browser: Chrome 120

## Screenshots
[If helpful]
```

**This helps others help you faster!**

### Response times

**Please be patient:**
- GitHub Discussions: Community answers, usually 24-48 hours
- Issues: Triaged within 1 week
- PRs: Reviewed within 1-2 weeks
- This is a volunteer project - we respond as we can!

---

## 🌱 Step 6: Growing as a Contributor

### After your first contribution

**You're officially a contributor now!** 🎉

**Next steps:**

#### Take on bigger challenges

**Progression path:**
1. ✅ First contribution (typo fix, simple change)
2. 🎯 Small features or bug fixes
3. 🚀 Larger features or refactoring
4. 💎 Core architecture contributions
5. 🌟 Helping review others' PRs

**Don't rush!** Grow at your own pace.

#### Explore different areas

**Try contributing to:**
- Code (if you started with docs)
- Documentation (if you started with code)
- Testing
- Accessibility
- Community support

**Becoming a well-rounded contributor makes you more valuable**

#### Help other newcomers

**Pay it forward:**
- Answer questions in Discussions
- Review other people's PRs
- Write documentation about what you learned
- Welcome new contributors

**Teaching is the best way to learn!**

### Understanding the codebase

**Key files to understand:**

```
index.html                  - Main homepage structure
css/main.css               - Sacred colors, golden ratio
js/main.js                 - Core interactions, Sacred Pause
js/consciousness-field.js  - Canvas particle animation
js/library.js              - Reading progress tracking
```

**Start by:**
1. Reading the code
2. Running it and observing behavior
3. Making small tweaks and seeing what happens
4. Asking questions about what you don't understand

### Becoming a regular contributor

**Signs you're ready for more responsibility:**
- Multiple merged PRs
- Understanding of codebase
- Helping other contributors
- Consistent activity
- Alignment with consciousness-first values

**Potential roles:**
- **Code reviewer**: Review others' PRs
- **Triager**: Help organize and label issues
- **Maintainer**: Broader repository permissions
- **Community lead**: Help foster community
- **Documentation lead**: Own documentation quality

**Talk to maintainers when you're ready!**

---

## 💜 Community & Culture

### How we work together

**Our values in practice:**

**Be kind**
- Assume good intentions
- Disagree respectfully
- Celebrate others' successes
- Offer help generously

**Be humble**
- We're all learning
- Mistakes are growth opportunities
- Ask questions without shame
- Accept feedback graciously

**Be inclusive**
- Use welcoming language
- Consider diverse perspectives
- Make space for all voices
- Accommodate different skill levels

**Be excellent**
- High standards for code quality
- Thorough testing and documentation
- Accessibility is non-negotiable
- Code review as a practice of care

### Code of Conduct

**Required reading:** [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

**Key points:**
- No harassment, discrimination, or hate
- Respect privacy and boundaries
- Assume good faith
- Focus on what's best for the community
- Accept feedback professionally

**Violations:** Report to tristan@terra-lumina.com

### Communication channels

**GitHub Discussions**
- General chat
- Philosophy questions
- Technical help
- Feature ideas
- Announcements

**GitHub Issues**
- Bug reports
- Feature requests
- Specific tasks

**Pull Requests**
- Code review
- Technical discussion
- Implementation details

**Email**
- tristan@terra-lumina.com
- For sensitive issues, security concerns, conduct violations

---

## ✅ Onboarding Checklist

**Track your progress:**

### Understanding Phase
- [ ] Read the [main website](https://evolvingresonantcocreationism.com)
- [ ] Read [README.md](README.md)
- [ ] Read [VISION.md](VISION.md)
- [ ] Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [ ] Understand the project's values and goals

### Setup Phase
- [ ] Install Git
- [ ] Install Node.js (v18+)
- [ ] Install code editor (VS Code recommended)
- [ ] Create GitHub account
- [ ] Fork the repository
- [ ] Clone your fork
- [ ] Run `npm run setup`
- [ ] Run `npm run serve` (site works locally)
- [ ] Run `npm test` (all tests pass)

### Contribution Phase
- [ ] Find a good first issue
- [ ] Comment to claim the issue
- [ ] Create a branch
- [ ] Make your changes
- [ ] Test your changes
- [ ] Format your code (`npm run format`)
- [ ] Commit with clear message
- [ ] Push to your fork
- [ ] Create Pull Request
- [ ] Respond to review feedback
- [ ] Get PR merged!

### Growth Phase
- [ ] Make a second contribution
- [ ] Help another contributor
- [ ] Explore different areas (code, docs, tests)
- [ ] Learn more about the codebase
- [ ] Consider becoming a regular contributor

---

## 🎓 Additional Resources

### Our Documentation
- [QUICK_START.md](QUICK_START.md) - Fast setup (5 minutes)
- [CONTRIBUTING.md](CONTRIBUTING.md) - Detailed contribution guidelines
- [STYLE_GUIDE.md](STYLE_GUIDE.md) - Code and documentation standards
- [ARCHITECTURE.md](ARCHITECTURE.md) - Technical deep dive
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common problems solved
- [FAQ.md](FAQ.md) - Frequently asked questions
- [SUPPORT.md](SUPPORT.md) - Where to get help

### Learning Resources
- [Git Handbook](https://guides.github.com/introduction/git-handbook/) - Learn Git basics
- [MDN Web Docs](https://developer.mozilla.org/) - HTML, CSS, JavaScript references
- [Playwright Docs](https://playwright.dev) - Testing framework we use
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/) - Accessibility standards

### External Guides
- [First Contributions](https://github.com/firstcontributions/first-contributions) - General open source guide
- [Open Source Guide](https://opensource.guide/how-to-contribute/) - From GitHub

---

## 💬 Frequently Asked Questions

### "I'm not a developer. Can I still contribute?"

**Absolutely!** We need:
- Writers (documentation, content)
- Designers (visuals, UX)
- Testers (finding bugs)
- Community builders (answering questions, welcoming newcomers)
- Philosophers (deepening the philosophy)
- Translators (other languages)

**Code is just one way to contribute.**

### "I found a typo but it seems too small to contribute"

**Typo fixes are valuable!** Every improvement matters. Submit a PR for even tiny fixes. We appreciate them all.

### "I'm working on an issue but I'm stuck. Is it OK to ask for help?"

**Yes! Please ask!** Comment on the issue, post in Discussions, or email. We'd rather help you succeed than have you struggle silently.

### "How long should my first contribution take?"

**Typically 1-3 hours** including:
- Understanding the issue
- Making the change
- Testing
- Creating the PR

**If it's taking much longer, ask for help!**

### "Can I work on something that's not in an issue?"

**Yes, but:** Open an issue first to discuss it. This prevents duplicate work and ensures alignment with project goals.

**For tiny changes** (fixing typos): Just submit a PR directly.

### "What if I start an issue and can't finish?"

**Totally fine!** Life happens. Just comment on the issue:

```
Hi, I'm no longer able to work on this. Making it available for someone else. Thanks!
```

**No judgment, no guilt. We appreciate you trying!**

### "How do I stay updated on project news?"

**Options:**
- Watch the repository (GitHub notifications)
- Check [Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions) regularly
- Read [CHANGELOG.md](CHANGELOG.md) for releases
- Follow announcements in Discussions

---

## 🌟 Final Encouragement

**You can do this.** 💜

Contributing to open source feels intimidating at first. That's normal. **Everyone** feels that way initially.

**But here's the truth:**
- You don't need to be an expert
- You don't need to contribute huge features
- You don't need to know everything before starting
- You just need to care and be willing to learn

**We're here to support you** every step of the way.

**Your perspective matters.** You'll see things we miss. You'll ask questions that improve our documentation. You'll bring fresh energy and ideas.

**The project is better because you're here.**

**Start small. Ask questions. Make mistakes. Learn. Grow.**

**Welcome to The Luminous Library. We're honored to co-create with you.** 🌟

---

## 💜 Thank You

**For reading this far. For considering contributing. For being here.**

Every contributor, no matter how small their contribution, makes this project better.

**You're not just contributing code or docs. You're contributing to a vision:**
- Technology that serves consciousness
- Philosophy made accessible
- Community built on love and wisdom
- A more flourishing world for all

**That's sacred work. Thank you for being part of it.** 💜✨

---

**Questions about onboarding?**
- Ask in [Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)
- Email: tristan@terra-lumina.com
- See: [SUPPORT.md](SUPPORT.md)

**Ready to contribute?**
- Find a [good first issue](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Join [Discussions](https://github.com/Luminous-Dynamics/evolving-resonant-cocreationism/discussions)

---

**Last Updated**: November 17, 2025

*Welcome home, fellow co-creator.* 💜✨
