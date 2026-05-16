document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Dark mode toggle
    const themeToggleBtns = document.querySelectorAll('#theme-toggle, #theme-toggle-mobile, #theme-toggle-tablet');
    const themeIcons = document.querySelectorAll('#theme-icon, #theme-icon-mobile, #theme-icon-tablet');
    const htmlElement = document.documentElement;

    const updateThemeUI = (isDark) => {
        if (isDark) {
            htmlElement.classList.add('dark');
            themeIcons.forEach(icon => {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            });
        } else {
            htmlElement.classList.remove('dark');
            themeIcons.forEach(icon => {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            });
        }
    };

    // Check local storage or system preference
    const initialDark = localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches);
    updateThemeUI(initialDark);

    themeToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const isDark = !htmlElement.classList.contains('dark');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
            updateThemeUI(isDark);
        });
    });

    // RTL toggle
    const rtlToggleBtns = document.querySelectorAll('#rtl-toggle, #rtl-toggle-mobile, #rtl-toggle-tablet');
    const rtlIcons = document.querySelectorAll('#rtl-icon, #rtl-icon-mobile, #rtl-icon-tablet');
    
    function updateRtlUI(isRtl) {
        htmlElement.setAttribute('dir', isRtl ? 'rtl' : 'ltr');
        localStorage.setItem('dir', isRtl ? 'rtl' : 'ltr');
        
        rtlIcons.forEach(icon => {
            if (icon.tagName === 'SPAN') {
                icon.textContent = isRtl ? 'LTR' : 'RTL';
            }
        });
    }

    // Initial check
    if (localStorage.getItem('dir') === 'rtl') {
        updateRtlUI(true);
    }

    rtlToggleBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            let isRtl = htmlElement.getAttribute('dir') === 'rtl';
            updateRtlUI(!isRtl);
        });
    });

    // Sticky Navbar
    const navbar = document.getElementById('navbar');
    if (navbar) {
        const isDarkHero = navbar.classList.contains('text-white');
        
        const updateNavbar = () => {
            const isDark = htmlElement.classList.contains('dark');
            if (window.scrollY > 50) {
                navbar.classList.add('glass-panel', 'shadow-md');
                navbar.classList.remove('bg-transparent', 'py-4');
                navbar.classList.add('py-2');
                
                if (isDarkHero && !isDark) {
                    navbar.classList.remove('text-white');
                    navbar.classList.add('text-gray-800');
                } else if (isDarkHero && isDark) {
                    navbar.classList.add('text-white');
                    navbar.classList.remove('text-gray-800');
                }
            } else {
                navbar.classList.remove('glass-panel', 'shadow-md');
                navbar.classList.add('bg-transparent', 'py-4');
                navbar.classList.remove('py-2');
                
                if (isDarkHero) {
                    navbar.classList.add('text-white');
                    navbar.classList.remove('text-gray-800');
                }
            }
        };

        window.addEventListener('scroll', updateNavbar);
        themeToggleBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Wait a tiny bit for the 'dark' class to be toggled by the main theme listener
                setTimeout(updateNavbar, 10);
            });
        });
    }

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if(targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if(targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    // Password visibility toggle
    const togglePasswordBtns = document.querySelectorAll('.toggle-password');
    togglePasswordBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const passwordInput = document.getElementById(targetId);
            const icon = this.querySelector('i');
            
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                icon.classList.replace('fa-eye', 'fa-eye-slash');
            } else {
                passwordInput.type = 'password';
                icon.classList.replace('fa-eye-slash', 'fa-eye');
            }
        });
    });
    
    // Back to Top functionality
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });

        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
});
