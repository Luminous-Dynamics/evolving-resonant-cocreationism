// Ko-fi Integration for Luminous Dynamics
// This adds the Ko-fi widget and tracking to your website

// Initialize Ko-fi Widget (Floating button)
function initKofiWidget() {
    // Only initialize if the script is loaded
    if (typeof kofiWidgetOverlay !== 'undefined') {
        kofiWidgetOverlay.draw('luminousdynamics', {
            'type': 'floating-chat',
            'floating-chat.donateButton.text': '☕ Support',
            'floating-chat.donateButton.background-color': '#667eea',
            'floating-chat.donateButton.text-color': '#fff',
            'floating-chat.position.bottom': '20px',
            'floating-chat.position.right': '20px'
        });
    }
}

// Track Ko-fi Events
function trackKofiEvent(action, label, value) {
    // Track in localStorage for now (can add Google Analytics later)
    const events = JSON.parse(localStorage.getItem('kofi_events') || '[]');
    events.push({
        action,
        label,
        value,
        timestamp: new Date().toISOString()
    });
    localStorage.setItem('kofi_events', JSON.stringify(events));
    
    // If Google Analytics is present
    if (typeof gtag !== 'undefined') {
        gtag('event', action, {
            'event_category': 'Ko-fi',
            'event_label': label,
            'value': value
        });
    }
}

// Add Ko-fi button to specific locations
function addKofiButtons() {
    // Add to navigation if exists
    const nav = document.querySelector('nav');
    if (nav && !nav.querySelector('.kofi-nav-button')) {
        const kofiNavButton = document.createElement('a');
        kofiNavButton.href = 'https://ko-fi.com/luminousdynamics';
        kofiNavButton.className = 'kofi-nav-button';
        kofiNavButton.innerHTML = '☕ Support';
        kofiNavButton.target = '_blank';
        kofiNavButton.style.cssText = `
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            text-decoration: none;
            margin-left: 20px;
            transition: transform 0.3s ease;
        `;
        kofiNavButton.onmouseover = () => kofiNavButton.style.transform = 'scale(1.05)';
        kofiNavButton.onmouseout = () => kofiNavButton.style.transform = 'scale(1)';
        kofiNavButton.onclick = () => trackKofiEvent('click', 'nav_button', 1);
        nav.appendChild(kofiNavButton);
    }
    
    // Add to footer if exists
    const footer = document.querySelector('footer');
    if (footer && !footer.querySelector('.kofi-footer-section')) {
        const kofiFooterSection = document.createElement('div');
        kofiFooterSection.className = 'kofi-footer-section';
        kofiFooterSection.innerHTML = `
            <div style="text-align: center; margin: 2rem 0;">
                <h3 style="color: var(--sacred-gold, #FFD700); margin-bottom: 1rem;">Support This Sacred Work</h3>
                <p style="margin-bottom: 1rem; opacity: 0.9;">Every coffee helps sustain consciousness-first technology</p>
                <a href="https://ko-fi.com/luminousdynamics" target="_blank" 
                   onclick="trackKofiEvent('click', 'footer_button', 1)"
                   style="display: inline-block; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                          color: white; padding: 12px 24px; border-radius: 25px; text-decoration: none;
                          transition: transform 0.3s ease;"
                   onmouseover="this.style.transform='translateY(-2px)'"
                   onmouseout="this.style.transform='translateY(0)'">
                    ☕ Buy Me a Coffee
                </a>
            </div>
        `;
        footer.insertBefore(kofiFooterSection, footer.firstChild);
    }
}

// Add supporter counter (uses localStorage for now)
function displaySupporterCount() {
    // This would normally fetch from your backend
    const supporterCount = localStorage.getItem('supporter_count') || '0';
    const elements = document.querySelectorAll('.supporter-count');
    elements.forEach(el => {
        el.textContent = supporterCount;
    });
}

// Thank you message for returning supporters
function checkReturningSupporter() {
    const isSupporter = localStorage.getItem('is_kofi_supporter');
    if (isSupporter === 'true') {
        // Show thank you message
        const thankYouBanner = document.createElement('div');
        thankYouBanner.id = 'supporter-thank-you';
        thankYouBanner.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 10px;
            text-align: center;
            z-index: 1000;
            animation: slideDown 0.5s ease;
        `;
        thankYouBanner.innerHTML = `
            <span>✨ Thank you for supporting consciousness-first computing! ✨</span>
            <button onclick="this.parentElement.remove()" style="
                background: none; border: none; color: white; 
                margin-left: 20px; cursor: pointer; font-size: 18px;">×</button>
        `;
        
        // Add animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideDown {
                from { transform: translateY(-100%); }
                to { transform: translateY(0); }
            }
        `;
        document.head.appendChild(style);
        
        // Show banner after 2 seconds
        setTimeout(() => {
            if (!document.getElementById('supporter-thank-you')) {
                document.body.appendChild(thankYouBanner);
                // Auto-hide after 10 seconds
                setTimeout(() => thankYouBanner.remove(), 10000);
            }
        }, 2000);
    }
}

// Sacred Reciprocity Reminder
function showSacredReciprocityReminder() {
    const lastReminder = localStorage.getItem('last_kofi_reminder');
    const now = Date.now();
    const oneWeek = 7 * 24 * 60 * 60 * 1000;
    
    if (!lastReminder || (now - parseInt(lastReminder)) > oneWeek) {
        // User has been on site for 5+ minutes
        setTimeout(() => {
            if (!localStorage.getItem('is_kofi_supporter')) {
                const reminder = document.createElement('div');
                reminder.style.cssText = `
                    position: fixed;
                    bottom: 80px;
                    right: 20px;
                    background: white;
                    border: 2px solid #667eea;
                    border-radius: 15px;
                    padding: 20px;
                    max-width: 300px;
                    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
                    z-index: 999;
                    animation: slideInRight 0.5s ease;
                `;
                reminder.innerHTML = `
                    <h4 style="color: #667eea; margin-bottom: 10px;">💜 Sacred Reciprocity</h4>
                    <p style="margin-bottom: 15px; font-size: 14px;">
                        If this philosophy resonates, consider supporting its continued development.
                        Even a single coffee helps sustain this work.
                    </p>
                    <div style="display: flex; gap: 10px;">
                        <a href="https://ko-fi.com/luminousdynamics" target="_blank"
                           onclick="trackKofiEvent('click', 'reminder_support', 1)"
                           style="flex: 1; background: #667eea; color: white; padding: 8px; 
                                  border-radius: 8px; text-align: center; text-decoration: none;">
                            Support Now
                        </a>
                        <button onclick="this.parentElement.parentElement.remove(); 
                                       localStorage.setItem('last_kofi_reminder', Date.now())"
                                style="flex: 1; background: #f0f0f0; border: none; 
                                       border-radius: 8px; cursor: pointer;">
                            Maybe Later
                        </button>
                    </div>
                `;
                
                // Add slide-in animation
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes slideInRight {
                        from { transform: translateX(100%); opacity: 0; }
                        to { transform: translateX(0); opacity: 1; }
                    }
                `;
                document.head.appendChild(style);
                
                document.body.appendChild(reminder);
            }
        }, 5 * 60 * 1000); // 5 minutes
    }
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    // Load Ko-fi widget script
    const kofiScript = document.createElement('script');
    kofiScript.src = 'https://storage.ko-fi.com/cdn/scripts/overlay-widget.js';
    kofiScript.onload = () => {
        initKofiWidget();
    };
    document.head.appendChild(kofiScript);
    
    // Add Ko-fi buttons to page
    addKofiButtons();
    
    // Check for returning supporter
    checkReturningSupporter();
    
    // Show reciprocity reminder after time
    showSacredReciprocityReminder();
    
    // Display supporter count
    displaySupporterCount();
});

// Export functions for use in other scripts
window.kofiIntegration = {
    trackEvent: trackKofiEvent,
    markAsSupporter: () => localStorage.setItem('is_kofi_supporter', 'true'),
    updateSupporterCount: (count) => {
        localStorage.setItem('supporter_count', count);
        displaySupporterCount();
    }
};