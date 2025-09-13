#!/usr/bin/env python3
"""
Comprehensive visual and performance polish for ERC website.
Addresses readability, performance, and user experience improvements.
"""

import os
import re

def add_performance_optimizations():
    """Add performance optimizations to main HTML files."""
    
    # Add preload for critical resources and lazy loading for images
    index_path = '/srv/luminous-dynamics/evolving-resonant-cocreationism/index.html'
    
    with open(index_path, 'r') as f:
        content = f.read()
    
    # Add preload directives for critical resources if not already present
    if '<link rel="preload"' not in content:
        preload_tags = """    <!-- Performance Optimizations -->
    <link rel="preload" href="css/main.css" as="style">
    <link rel="preload" href="css/harmonies.css" as="style">
    <link rel="preconnect" href="https://storage.ko-fi.com">
    """
        content = content.replace('    <link rel="stylesheet" href="css/main.css">', 
                                   preload_tags + '    <link rel="stylesheet" href="css/main.css">')
    
    # Add loading="lazy" to Ko-fi widget script
    content = content.replace(
        "<script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>",
        '<script src="https://storage.ko-fi.com/cdn/scripts/overlay-widget.js" defer></script>'
    )
    
    with open(index_path, 'w') as f:
        f.write(content)
    
    print("✅ Added performance optimizations to index.html")

def optimize_consciousness_field():
    """Optimize the consciousness field animation for performance."""
    
    js_path = '/srv/luminous-dynamics/evolving-resonant-cocreationism/js/consciousness-field.js'
    
    with open(js_path, 'r') as f:
        content = f.read()
    
    # Add performance check for reduced motion preference
    optimization = """// Consciousness Field Particle System
class ConsciousnessField {
    constructor() {
        // Check for reduced motion preference
        this.reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouseX = 0;
        this.mouseY = 0;
        
        // Reduce particle count for performance on mobile
        this.particleCount = window.innerWidth < 768 ? 25 : 50;
        
        if (!this.reducedMotion) {
            this.init();
        }
    }"""
    
    content = content.replace(
        """// Consciousness Field Particle System
class ConsciousnessField {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouseX = 0;
        this.mouseY = 0;
        
        this.init();
    }""",
        optimization
    )
    
    # Update particle creation to use dynamic count
    content = content.replace(
        "for (let i = 0; i < 50; i++) {",
        "for (let i = 0; i < this.particleCount; i++) {"
    )
    
    with open(js_path, 'w') as f:
        f.write(content)
    
    print("✅ Optimized consciousness field animation")

def add_accessibility_improvements():
    """Add accessibility improvements across the site."""
    
    # Add skip navigation link
    index_path = '/srv/luminous-dynamics/evolving-resonant-cocreationism/index.html'
    
    with open(index_path, 'r') as f:
        content = f.read()
    
    if 'skip-nav' not in content:
        skip_nav = """<body>
    <!-- Skip Navigation for Accessibility -->
    <a href="#core-message" class="skip-nav">Skip to main content</a>
    <style>
        .skip-nav {
            position: absolute;
            top: -40px;
            left: 0;
            background: #FFD700;
            color: #1a0033;
            padding: 0.5rem 1rem;
            z-index: 10000;
            text-decoration: none;
            border-radius: 0 0 5px 0;
        }
        .skip-nav:focus {
            top: 0;
        }
    </style>
    """
        content = content.replace('<body>\n', skip_nav)
    
    with open(index_path, 'w') as f:
        f.write(content)
    
    print("✅ Added accessibility improvements")

def improve_mobile_responsiveness():
    """Add better mobile responsiveness to CSS."""
    
    css_path = '/srv/luminous-dynamics/evolving-resonant-cocreationism/css/main.css'
    
    with open(css_path, 'r') as f:
        content = f.read()
    
    # Add improved mobile styles if not present
    if '/* Enhanced Mobile Styles */' not in content:
        mobile_styles = """

/* Enhanced Mobile Styles */
@media (max-width: 768px) {
    /* Better touch targets */
    .btn-primary, .btn-secondary, .btn-tertiary, .btn-path, .btn-support {
        min-height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Improved readability on mobile */
    body {
        font-size: 16px;
    }
    
    .harmony-card, .path-card {
        padding: 1.5rem;
    }
    
    /* Stack buttons vertically on small screens */
    .cta-buttons {
        flex-direction: column;
        align-items: stretch;
    }
    
    .cta-buttons a {
        width: 100%;
        margin: 0.5rem 0;
    }
    
    /* Improve form inputs on mobile */
    .signup-form input {
        min-width: 100%;
        font-size: 16px; /* Prevents zoom on iOS */
    }
}

/* High contrast mode support */
@media (prefers-contrast: high) {
    .harmony-card {
        border: 2px solid #FFD700;
    }
    
    .btn-primary, .btn-secondary {
        border: 2px solid currentColor;
    }
}

/* Dark mode preferences */
@media (prefers-color-scheme: dark) {
    /* Site already has dark theme, but ensure consistency */
    body {
        background: linear-gradient(to bottom, #1a1a1a 0%, #000000 100%);
    }
}
"""
        content += mobile_styles
    
    with open(css_path, 'w') as f:
        f.write(content)
    
    print("✅ Improved mobile responsiveness")

def add_smooth_scrolling():
    """Add smooth scrolling behavior for better UX."""
    
    main_js_path = '/srv/luminous-dynamics/evolving-resonant-cocreationism/js/main.js'
    
    with open(main_js_path, 'r') as f:
        content = f.read()
    
    # Add smooth scrolling if not present
    if 'smooth scrolling' not in content.lower():
        smooth_scroll = """

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add scroll-to-top button for long pages
if (document.body.scrollHeight > window.innerHeight * 2) {
    const scrollButton = document.createElement('button');
    scrollButton.innerHTML = '↑';
    scrollButton.className = 'scroll-to-top';
    scrollButton.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #FFD700, #FFA500);
        color: #1a0033;
        border: none;
        font-size: 24px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.3s;
        z-index: 1000;
    `;
    
    document.body.appendChild(scrollButton);
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            scrollButton.style.opacity = '0.8';
        } else {
            scrollButton.style.opacity = '0';
        }
    });
    
    scrollButton.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}
"""
        content += smooth_scroll
    
    with open(main_js_path, 'w') as f:
        f.write(content)
    
    print("✅ Added smooth scrolling and scroll-to-top button")

def main():
    """Run all polish improvements."""
    print("🎨 Starting comprehensive site polish...\n")
    
    # Run all optimizations
    add_performance_optimizations()
    optimize_consciousness_field()
    add_accessibility_improvements()
    improve_mobile_responsiveness()
    add_smooth_scrolling()
    
    print("\n✨ Site polish complete!")
    print("\nImprovements made:")
    print("- ⚡ Performance: Preloading, lazy loading, reduced animations")
    print("- ♿ Accessibility: Skip navigation, better contrast support")
    print("- 📱 Mobile: Better touch targets, improved readability")
    print("- 🎯 UX: Smooth scrolling, scroll-to-top button")
    print("- 🎨 Visual: Fixed color contrast issues (already done)")

if __name__ == "__main__":
    main()