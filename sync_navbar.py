import os
import re

root_dir = r'c:\Users\prasa\OneDrive\Desktop\SF\May website 2026\Freelance_FinTech_Compliance_Automation_Consultant'

def get_navbar(active_page):
    home_dropdown = f'''
                    <div class="relative group">
                        <a href="#" class="{"text-accent-blue font-semibold" if active_page == "home" else "hover:text-accent-blue"} transition-colors flex items-center gap-1 py-2 group">Home <i class="fas fa-chevron-down text-[10px] mt-0.5 group-hover:-rotate-180 transition-transform duration-300"></i></a>
                        <div class="absolute top-full left-0 mt-0 w-48 glass-panel rounded-xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 flex flex-col p-2 shadow-xl translate-y-2 group-hover:translate-y-0 text-gray-800 dark:text-gray-200">
                            <a href="index.html" class="px-4 py-2 {"bg-blue-50 dark:bg-blue-900/30 text-accent-blue font-bold" if active_page == "home-1" else "hover:bg-gray-100 dark:hover:bg-navy-800"} rounded-lg transition-colors flex items-center gap-2"><i class="fas fa-home text-accent-blue w-4"></i> Home 1</a>
                            <a href="home-2.html" class="px-4 py-2 {"bg-blue-50 dark:bg-blue-900/30 text-accent-blue font-bold" if active_page == "home-2" else "hover:bg-gray-100 dark:hover:bg-navy-800"} rounded-lg transition-colors flex items-center gap-2"><i class="fas fa-layer-group text-accent-blue w-4"></i> Home 2</a>
                        </div>
                    </div>'''

    nav_links = f'''
                    <a href="about.html" class="{"text-accent-blue font-semibold" if active_page == "about" else "hover:text-accent-blue"} transition-colors">About</a>
                    <a href="services.html" class="{"text-accent-blue font-semibold" if active_page == "services" else "hover:text-accent-blue"} transition-colors">Services</a>
                    <a href="blog.html" class="{"text-accent-blue font-semibold" if active_page == "blog" else "hover:text-accent-blue"} transition-colors">Blog</a>
                    <a href="pricing.html" class="{"text-accent-blue font-semibold" if active_page == "pricing" else "hover:text-accent-blue"} transition-colors">Pricing</a>
                    <a href="contact.html" class="{"text-accent-blue font-semibold" if active_page == "contact" else "hover:text-accent-blue"} transition-colors">Contact</a>'''

    mobile_links = f'''
            <a href="index.html" class="{"text-accent-blue font-semibold" if active_page == "home-1" else "hover:text-accent-blue"} transition-colors block py-2">Home</a>
            <a href="home-2.html" class="{"text-accent-blue font-semibold" if active_page == "home-2" else "hover:text-accent-blue"} transition-colors block py-2">Home 2 (SaaS)</a>
            <a href="about.html" class="{"text-accent-blue font-semibold" if active_page == "about" else "hover:text-accent-blue"} transition-colors block py-2">About</a>
            <a href="services.html" class="{"text-accent-blue font-semibold" if active_page == "services" else "hover:text-accent-blue"} transition-colors block py-2">Services</a>
            <a href="blog.html" class="{"text-accent-blue font-semibold" if active_page == "blog" else "hover:text-accent-blue"} transition-colors block py-2">Blog</a>
            <a href="pricing.html" class="{"text-accent-blue font-semibold" if active_page == "pricing" else "hover:text-accent-blue"} transition-colors block py-2">Pricing</a>
            <a href="contact.html" class="{"text-accent-blue font-semibold" if active_page == "contact" else "hover:text-accent-blue"} transition-colors block py-2">Contact</a>'''

    # Pages with dark hero sections need text-white initially for contrast
    dark_hero_pages = ['about', 'home-2']
    
    header_class = "fixed w-full top-0 z-50 transition-all duration-300 py-3 bg-transparent border-b border-transparent"
    if active_page in dark_hero_pages:
        header_class += " text-white"
    
    brand_span_class = "font-heading font-bold text-xl tracking-tight"
    # Only add dark:text-white if it's not already text-white from the header
    if active_page not in dark_hero_pages:
        brand_span_class += " dark:text-white"

    return f'''
    <header id="navbar" class="{header_class}">
        <div class="container mx-auto px-4 md:px-6 lg:px-8">
            <div class="flex items-center justify-between">
                <a href="index.html" class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-gradient-accent flex items-center justify-center text-white font-bold text-xl shadow-lg shadow-accent-blue/30">C</div>
                    <span class="{brand_span_class}">CompliTech</span>
                </a>

                <!-- Desktop Nav -->
                <nav class="hidden lg:flex items-center gap-6 font-medium text-sm">
                    {home_dropdown}
                    {nav_links}
                </nav>

                <div class="hidden lg:flex items-center gap-4">
                    <button id="rtl-toggle" class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-sm hover:bg-gray-200 dark:hover:bg-navy-800 transition-colors" aria-label="Toggle RTL Mode"><span id="rtl-icon">RTL</span></button>
                    <button id="theme-toggle" class="w-10 h-10 rounded-full flex items-center justify-center hover:bg-gray-200 dark:hover:bg-navy-800 transition-colors" aria-label="Toggle Dark Mode">
                        <i id="theme-icon" class="fas fa-moon text-lg"></i>
                    </button>
                    <a href="login.html" class="px-5 py-2.5 rounded-full font-semibold text-sm border border-gray-200 dark:border-gray-700 hover:border-accent-blue dark:hover:border-accent-blue hover:bg-gray-100 dark:hover:bg-navy-800 hover:text-navy-900 dark:hover:text-white transition-all btn-hover-lift">Login</a>
                    <a href="dashboard.html" class="bg-navy-900 dark:bg-white text-white dark:text-navy-900 px-5 py-2.5 rounded-full font-semibold text-sm hover-glow transition-all">Dashboard</a>
                </div>

                <!-- Mobile Toggle -->
                <div class="flex items-center gap-2 lg:hidden">
                    <button id="rtl-toggle-tablet" class="w-10 h-10 rounded-full flex items-center justify-center font-bold text-xs hover:bg-gray-200 dark:hover:bg-navy-800 transition-colors" aria-label="Toggle RTL Mode"><span id="rtl-icon-tablet">RTL</span></button>
                    <button id="theme-toggle-tablet" class="w-10 h-10 rounded-full flex items-center justify-center hover:bg-gray-200 dark:hover:bg-navy-800 transition-colors" aria-label="Toggle Dark Mode">
                        <i id="theme-icon-tablet" class="fas fa-moon text-lg"></i>
                    </button>
                    <button id="mobile-menu-btn" class="text-2xl p-2 focus:outline-none">
                        <i class="fas fa-bars"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden lg:hidden absolute top-full left-0 w-full bg-white dark:bg-navy-900 border-t border-gray-200 dark:border-gray-800 p-4 flex flex-col gap-4 shadow-xl text-gray-800 dark:text-gray-200">
            {mobile_links}
            <hr class="border-gray-200 dark:border-gray-800">
            <a href="login.html" class="border border-gray-200 dark:border-gray-700 text-center py-3 rounded-xl font-semibold block transition-all hover:bg-gray-50 dark:hover:bg-navy-800">Login / Register</a>
            <a href="dashboard.html" class="bg-accent-blue text-white text-center py-3 rounded-xl font-semibold block mt-2 shadow-lg shadow-blue-500/30">Dashboard</a>
        </div>
    </header>'''

page_mapping = {
    'index.html': 'home-1',
    'home-2.html': 'home-2',
    'about.html': 'about',
    'services.html': 'services',
    'service-details.html': 'services',
    'blog.html': 'blog',
    'blog-details.html': 'blog',
    'pricing.html': 'pricing',
    'contact.html': 'contact',
    '404.html': 'none',
    'maintenance.html': 'none'
}

for filename, active in page_mapping.items():
    filepath = os.path.join(root_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        file_content = f.read()
    
    # Standardize active category
    category = active
    if active in ['home-1', 'home-2']:
        category = 'home'
        
    new_navbar = get_navbar(active)
    
    # Replace header
    new_content = re.sub(r'<header id="navbar".*?</header>', new_navbar, file_content, flags=re.DOTALL)
    
    if new_content != file_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated navbar in {filename}")

print("Navbar sync complete.")
