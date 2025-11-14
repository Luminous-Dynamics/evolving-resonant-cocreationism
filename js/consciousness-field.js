// Consciousness Field Particle System
class ConsciousnessField {
    constructor() {
        this.canvas = document.createElement('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.mouseX = 0;
        this.mouseY = 0;
        this.animationId = null;
        this.isVisible = true;

        this.init();
    }
    
    init() {
        // Insert canvas into consciousness-field div
        const field = document.querySelector('.consciousness-field');
        if (!field) return;
        
        field.appendChild(this.canvas);
        this.resize();
        
        // Create particles
        for (let i = 0; i < 50; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5,
                radius: Math.random() * 3 + 1,
                opacity: Math.random() * 0.5 + 0.3
            });
        }
        
        // Event listeners
        window.addEventListener('resize', () => this.resize());
        window.addEventListener('mousemove', (e) => {
            this.mouseX = e.clientX;
            this.mouseY = e.clientY;
        });

        // Pause animation when not visible (performance optimization)
        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    this.isVisible = entry.isIntersecting;
                    if (this.isVisible && !this.animationId) {
                        this.animate();
                    }
                });
            });
            observer.observe(this.canvas);
        }

        // Check for reduced motion preference
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
        if (prefersReducedMotion.matches) {
            // Don't start animation if user prefers reduced motion
            return;
        }

        // Start animation
        this.animate();
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
            this.animationId = null;
        }
        if (this.canvas && this.canvas.parentNode) {
            this.canvas.parentNode.removeChild(this.canvas);
        }
    }
    
    resize() {
        this.canvas.width = window.innerWidth;
        this.canvas.height = window.innerHeight;
    }
    
    animate() {
        // Only animate if visible
        if (!this.isVisible) {
            this.animationId = null;
            return;
        }

        // Clear canvas with fade effect
        this.ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Update and draw particles
        this.particles.forEach(particle => {
            // Mouse interaction
            const dx = this.mouseX - particle.x;
            const dy = this.mouseY - particle.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (distance < 100) {
                const force = (100 - distance) / 100;
                particle.vx += (dx / distance) * force * 0.1;
                particle.vy += (dy / distance) * force * 0.1;
            }
            
            // Update position
            particle.x += particle.vx;
            particle.y += particle.vy;
            
            // Damping
            particle.vx *= 0.99;
            particle.vy *= 0.99;
            
            // Boundaries
            if (particle.x < 0 || particle.x > this.canvas.width) particle.vx *= -1;
            if (particle.y < 0 || particle.y > this.canvas.height) particle.vy *= -1;
            
            // Draw particle
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = `rgba(255, 215, 0, ${particle.opacity})`;
            this.ctx.fill();
        });
        
        // Draw connections
        this.particles.forEach((p1, i) => {
            this.particles.slice(i + 1).forEach(p2 => {
                const dx = p1.x - p2.x;
                const dy = p1.y - p2.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 150) {
                    const opacity = (150 - distance) / 150 * 0.3;
                    this.ctx.beginPath();
                    this.ctx.moveTo(p1.x, p1.y);
                    this.ctx.lineTo(p2.x, p2.y);
                    this.ctx.strokeStyle = `rgba(255, 215, 0, ${opacity})`;
                    this.ctx.stroke();
                }
            });
        });

        this.animationId = requestAnimationFrame(() => this.animate());
    }
}

// Store instance for cleanup
let consciousnessFieldInstance = null;

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    consciousnessFieldInstance = new ConsciousnessField();
});

// Cleanup on unload
window.addEventListener('beforeunload', () => {
    if (consciousnessFieldInstance) {
        consciousnessFieldInstance.destroy();
    }
});