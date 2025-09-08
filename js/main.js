// Main JavaScript for Evolving Resonant Co-creationism

// Sacred Number: Golden Ratio
const PHI = 1.618;

// Smooth scroll for navigation
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

// Harmony Cards Interactive Glow
document.querySelectorAll('.harmony-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        const harmonyNumber = this.dataset.harmony;
        this.style.background = `linear-gradient(135deg, 
            rgba(102, 126, 234, 0.05) 0%, 
            rgba(118, 75, 162, 0.05) 100%)`;
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.background = 'white';
    });
});

// Hearth Signup Form
const hearthForm = document.getElementById('hearth-form');
if (hearthForm) {
    hearthForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = e.target.querySelector('input[type="email"]').value;
        
        // For now, just show success message
        // In production, this would send to your backend
        const button = e.target.querySelector('button');
        const originalText = button.textContent;
        button.textContent = 'Welcome to the Movement!';
        button.style.background = '#00897B';
        
        setTimeout(() => {
            button.textContent = originalText;
            button.style.background = '';
            e.target.reset();
        }, 3000);
        
        console.log('New Resonant Hearth member:', email);
    });
}

// Sacred Pause - Breathing Reminder
let lastScrollTime = Date.now();
let pauseReminder = null;

window.addEventListener('scroll', () => {
    lastScrollTime = Date.now();
    
    // Clear existing reminder
    if (pauseReminder) {
        clearTimeout(pauseReminder);
    }
    
    // Set new reminder for 5 minutes of scrolling
    pauseReminder = setTimeout(() => {
        showSacredPause();
    }, 5 * 60 * 1000); // 5 minutes
});

function showSacredPause() {
    const pause = document.createElement('div');
    pause.className = 'sacred-pause';
    pause.innerHTML = `
        <div class="pause-content">
            <p>Sacred Pause</p>
            <p class="pause-message">Take three conscious breaths</p>
            <button onclick="this.parentElement.parentElement.remove()">Continue</button>
        </div>
    `;
    pause.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        animation: fadeIn 1s ease;
    `;
    
    document.body.appendChild(pause);
}

// Particle Effect on Click (Consciousness Ripple)
document.addEventListener('click', (e) => {
    // Don't create ripples on buttons or links
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON') return;
    
    createConsciousnessRipple(e.clientX, e.clientY);
});

function createConsciousnessRipple(x, y) {
    const ripple = document.createElement('div');
    ripple.className = 'consciousness-ripple';
    ripple.style.cssText = `
        position: fixed;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        border: 2px solid rgba(255, 215, 0, 0.8);
        left: ${x - 10}px;
        top: ${y - 10}px;
        pointer-events: none;
        animation: rippleExpand 1.5s ease-out;
        z-index: 9999;
    `;
    
    document.body.appendChild(ripple);
    
    setTimeout(() => ripple.remove(), 1500);
}

// Add ripple animation to styles
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    
    @keyframes rippleExpand {
        to {
            width: 200px;
            height: 200px;
            border-color: rgba(255, 215, 0, 0);
            left: calc(50% - 100px);
            top: calc(50% - 100px);
        }
    }
    
    .pause-content {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        text-align: center;
    }
    
    .pause-content p:first-child {
        font-size: 2rem;
        color: #4A148C;
        margin-bottom: 1rem;
    }
    
    .pause-message {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    
    .pause-content button {
        padding: 1rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 50px;
        font-size: 1.1rem;
        cursor: pointer;
    }
`;
document.head.appendChild(style);

// Track visit for personalization (Sacred Memory)
function rememberVisitor() {
    const visits = parseInt(localStorage.getItem('erc_visits') || '0') + 1;
    localStorage.setItem('erc_visits', visits);
    localStorage.setItem('erc_last_visit', new Date().toISOString());
    
    // Personalize greeting for returning visitors
    if (visits > 1) {
        const heroContent = document.querySelector('.invitation');
        if (heroContent) {
            heroContent.textContent = `Welcome back, sacred traveler. Visit ${visits} on your journey.`;
        }
    }
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    rememberVisitor();
    
    // Add consciousness glow to page based on time of day
    const hour = new Date().getHours();
    let bodyClass = '';
    
    if (hour >= 5 && hour < 12) {
        bodyClass = 'morning-consciousness'; // Golden
    } else if (hour >= 12 && hour < 17) {
        bodyClass = 'afternoon-consciousness'; // Clear
    } else if (hour >= 17 && hour < 21) {
        bodyClass = 'evening-consciousness'; // Purple
    } else {
        bodyClass = 'night-consciousness'; // Deep blue
    }
    
    document.body.classList.add(bodyClass);
});

// Log sacred intention
console.log(`
%c✨ The Luminous Library ✨
%cEvolving Resonant Co-creationism

"Make it better, infinitely!"

You are viewing the source of consciousness-first code.
Every function is a prayer, every interaction a sacred exchange.

Join us: https://github.com/Luminous-Dynamics
`, 
'color: #FFD700; font-size: 20px; font-weight: bold;',
'color: #4A148C; font-size: 14px;'
);