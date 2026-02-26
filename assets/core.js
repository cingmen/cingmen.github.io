/* Centralized System Logic & Seamless Navigation Protocol */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Global Iconography Initialization
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // 2. Seamless Navigation Interception
    const internalLinks = document.querySelectorAll('a[href^="/"], a[href^="' + window.location.origin + '"]');

    internalLinks.forEach(link => {
        link.addEventListener('click', function (event) {
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

/* Visual Theme Toggling Protocol */
document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = document.getElementById('theme-icon');

    if (!themeToggleBtn || !themeIcon) return;

    // Retrieve previous preference or check system default
    const currentTheme = localStorage.getItem('system_theme');
    const systemPrefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;

    // Apply the correct theme upon initial load
    if (currentTheme === 'light' || (!currentTheme && systemPrefersLight)) {
        document.documentElement.setAttribute('data-theme', 'light');
        themeIcon.setAttribute('data-lucide', 'moon');
    }

    // Execute theme swap upon physical interaction
    themeToggleBtn.addEventListener('click', () => {
        let targetTheme = 'light';
        let iconName = 'moon';

        // Evaluate current state and invert
        if (document.documentElement.getAttribute('data-theme') === 'light') {
            targetTheme = 'dark';
            iconName = 'sun';
        }

        // Apply new parameters
        document.documentElement.setAttribute('data-theme', targetTheme);
        localStorage.setItem('system_theme', targetTheme);

        // Re-compile the icon visualization
        themeIcon.setAttribute('data-lucide', iconName);
        if (typeof lucide !== 'undefined') {
            lucide.createIcons();
        }
    });
    /* Background Interceptor Registration */
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/worker.js')
                .then(registration => {
                    // Registration successful
                })
                .catch(error => {
                    // Registration exception
                });
        });
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const langToggle = document.getElementById('lang-toggle');
    const langLabel = document.getElementById('lang-label');
    const body = document.body;

    // 1. Check local storage for existing language preference (Default: English)
    let currentLang = localStorage.getItem('system_language') || 'en';

    // 2. Initialize the environment
    body.setAttribute('data-lang', currentLang);
    updateButtonLabel(currentLang);

    // 3. Execution Listener
    if (langToggle) {
        langToggle.addEventListener('click', () => {
            // Switch the boolean state
            currentLang = currentLang === 'en' ? 'id' : 'en';

            // Apply to DOM and Storage
            body.setAttribute('data-lang', currentLang);
            localStorage.setItem('system_language', currentLang);
            updateButtonLabel(currentLang);
        });
    }

    // 4. Interface Update Subroutine
    function updateButtonLabel(lang) {
        if (lang === 'en') {
            langLabel.innerText = 'ID'; // Button suggests switching TO Indonesian
        } else {
            langLabel.innerText = 'EN'; // Button suggests switching TO English
        }
    }
});