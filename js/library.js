// Library reading experience enhancements

// Reading progress indicator
function updateReadingProgress() {
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPosition = window.scrollY;
    const progress = (scrollPosition / scrollHeight) * 100;
    
    const progressBar = document.querySelector('.reading-progress');
    if (progressBar) {
        progressBar.style.width = `${progress}%`;
    }
    
    // Save reading position
    localStorage.setItem('library_scroll_position', scrollPosition);
}

// Scroll to top button visibility
function updateScrollButton() {
    const scrollButton = document.querySelector('.scroll-to-top');
    if (window.scrollY > 500) {
        scrollButton.classList.add('visible');
    } else {
        scrollButton.classList.remove('visible');
    }
}

// Restore reading position
function restoreReadingPosition() {
    const savedPosition = localStorage.getItem('library_scroll_position');
    if (savedPosition && window.location.hash === '') {
        window.scrollTo(0, parseInt(savedPosition));
    }
}

// Reading time estimate
function calculateReadingTime() {
    const content = document.querySelector('.library-content');
    if (!content) return;
    
    const text = content.textContent;
    const wordsPerMinute = 200;
    const words = text.trim().split(/\s+/).length;
    const minutes = Math.ceil(words / wordsPerMinute);
    
    const readingTimeElement = document.createElement('div');
    readingTimeElement.className = 'reading-time';
    readingTimeElement.innerHTML = `📖 Estimated reading time: ${minutes} minutes`;
    readingTimeElement.style.cssText = `
        text-align: center;
        color: #666;
        font-style: italic;
        margin: 2rem 0;
        padding: 1rem;
        background: rgba(255, 215, 0, 0.1);
        border-radius: 10px;
    `;
    
    const header = document.querySelector('.library-header');
    if (header) {
        header.appendChild(readingTimeElement);
    }
}

// Smooth scroll for anchor links
function setupSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = 100; // Account for fixed nav
                const targetPosition = target.offsetTop - offset;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Add section anchors for easy sharing
function addSectionAnchors() {
    const headers = document.querySelectorAll('.library-content h1, .library-content h2, .library-content h3');
    headers.forEach(header => {
        if (!header.id) {
            // Create ID from header text
            const id = header.textContent.toLowerCase()
                .replace(/[^a-z0-9]+/g, '-')
                .replace(/(^-|-$)/g, '');
            header.id = id;
        }
        
        // Add anchor link
        const anchor = document.createElement('a');
        anchor.href = `#${header.id}`;
        anchor.className = 'section-anchor';
        anchor.innerHTML = '🔗';
        anchor.title = 'Copy link to this section';
        anchor.style.cssText = `
            margin-left: 10px;
            text-decoration: none;
            opacity: 0;
            transition: opacity 0.3s ease;
            font-size: 0.8em;
        `;
        
        header.appendChild(anchor);
        
        // Show on hover
        header.addEventListener('mouseenter', () => {
            anchor.style.opacity = '0.5';
        });
        
        header.addEventListener('mouseleave', () => {
            anchor.style.opacity = '0';
        });
        
        // Copy link on click
        anchor.addEventListener('click', (e) => {
            e.preventDefault();
            const url = `${window.location.origin}${window.location.pathname}#${header.id}`;
            navigator.clipboard.writeText(url);
            
            // Show confirmation
            const confirmation = document.createElement('span');
            confirmation.textContent = ' Copied!';
            confirmation.style.cssText = `
                color: #00897B;
                font-size: 0.8em;
                margin-left: 10px;
            `;
            header.appendChild(confirmation);
            
            setTimeout(() => confirmation.remove(), 2000);
        });
    });
}

// Reading mode toggle (zen mode)
function createZenModeToggle() {
    const toggle = document.createElement('button');
    toggle.className = 'zen-mode-toggle';
    toggle.innerHTML = '🧘 Zen Mode';
    toggle.style.cssText = `
        position: fixed;
        bottom: 30px;
        left: 30px;
        background: white;
        color: #4A148C;
        padding: 10px 20px;
        border: 2px solid #4A148C;
        border-radius: 50px;
        cursor: pointer;
        z-index: 999;
        transition: all 0.3s ease;
    `;
    
    document.body.appendChild(toggle);
    
    let zenMode = false;
    
    toggle.addEventListener('click', () => {
        zenMode = !zenMode;
        
        if (zenMode) {
            document.body.classList.add('zen-mode');
            toggle.innerHTML = '📖 Normal Mode';
            
            // Hide navigation
            document.querySelector('.library-nav').style.display = 'none';
            
            // Increase font size and spacing
            document.querySelector('.library-content').style.cssText += `
                font-size: 1.3rem;
                line-height: 2;
                max-width: 700px;
                margin: 0 auto;
            `;
            
            // Dim background
            document.body.style.background = '#f5f5f5';
        } else {
            document.body.classList.remove('zen-mode');
            toggle.innerHTML = '🧘 Zen Mode';
            
            // Restore navigation
            document.querySelector('.library-nav').style.display = 'flex';
            
            // Restore normal text
            document.querySelector('.library-content').style.cssText = '';
            
            // Restore background
            document.body.style.background = '';
        }
    });
}

// Track reading analytics (local only)
function trackReading() {
    const startTime = Date.now();
    
    window.addEventListener('beforeunload', () => {
        const readingTime = Math.round((Date.now() - startTime) / 1000); // seconds
        const existingTime = parseInt(localStorage.getItem('library_total_reading_time') || '0');
        localStorage.setItem('library_total_reading_time', existingTime + readingTime);
        
        // Track sections read
        const sectionsViewed = JSON.parse(localStorage.getItem('library_sections_viewed') || '[]');
        const currentSection = window.location.hash || 'main';
        if (!sectionsViewed.includes(currentSection)) {
            sectionsViewed.push(currentSection);
            localStorage.setItem('library_sections_viewed', JSON.stringify(sectionsViewed));
        }
    });
}

// Initialize everything
document.addEventListener('DOMContentLoaded', () => {
    calculateReadingTime();
    setupSmoothScroll();
    addSectionAnchors();
    createZenModeToggle();
    restoreReadingPosition();
    trackReading();
    
    // Update on scroll
    window.addEventListener('scroll', () => {
        updateReadingProgress();
        updateScrollButton();
    });
    
    // Initial update
    updateReadingProgress();
    updateScrollButton();
    
    console.log(`
%c📖 Welcome to The Luminous Library
%cYou are reading the source of consciousness itself.

"Make it better, infinitely!"

Reading features:
- Your position is saved automatically
- Click section headers to copy shareable links
- Use Zen Mode for distraction-free reading
- Your reading time helps us understand engagement

Thank you for engaging with this sacred text.
`, 
    'color: #4A148C; font-size: 16px; font-weight: bold;',
    'color: #00897B; font-size: 12px;'
    );
});