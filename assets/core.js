/* Centralized System Logic & Seamless Navigation Protocol */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Global Iconography Initialization
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // 2. Seamless Navigation Interception
    const internalLinks = document.querySelectorAll('a[href^="/"], a[href^="' + window.location.origin + '"]');
    
    internalLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            // Bypass the transition for new tabs or on-page anchor links
            if (this.target === '_blank' || this.getAttribute('href').startsWith('#')) return;
            
            // Suspend the hard server reload
            event.preventDefault();
            
            // Execute the visual fade-out sequence
            document.body.classList.add('navigating-out');
            
            // Hold the redirect until the 300-millisecond mathematical animation completes
            setTimeout(() => { 
                window.location.href = this.href; 
            }, 300);
        });
    });
});

// 3. System Failsafe: Restores opacity if a user navigates backward via browser history
window.addEventListener('pageshow', (event) => { 
    if (event.persisted) {
        document.body.classList.remove('navigating-out'); 
    }
});