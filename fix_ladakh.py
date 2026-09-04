with open(r'c:\Users\Debajyoti\.antigravity\wanderon\ladakh.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Overflow on body
if 'overflow-x-hidden' not in html:
    html = html.replace('<body class="', '<body class="overflow-x-hidden ')
    if '<body class=' not in html:
        html = html.replace('<body>', '<body class="overflow-x-hidden">')

# Nav
if '<nav x-data="' not in html:
    html = html.replace('<nav class="', '<nav x-data="{ mobileMenu: false }" class="', 1)

hamburger_html = '''
        <!-- Mobile Menu Button -->
        <button @click="mobileMenu = !mobileMenu" class="lg:hidden text-white p-2 z-50">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path x-show="!mobileMenu" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                <path x-show="mobileMenu" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
        </button>

        <!-- Mobile Drawer -->
        <div x-show="mobileMenu" 
             x-transition:enter="transition ease-out duration-300"
             x-transition:enter-start="opacity-0 translate-x-full"
             x-transition:enter-end="opacity-100 translate-x-0"
             x-transition:leave="transition ease-in duration-200"
             x-transition:leave-start="opacity-100 translate-x-0"
             x-transition:leave-end="opacity-0 translate-x-full"
             class="fixed inset-0 z-40 bg-dark lg:hidden flex flex-col pt-24 px-6">
            
            <div class="flex flex-col gap-6 text-xl font-medium">
                <a href="index.html" class="text-white">Home</a>
                <a href="#" class="text-white">Trips</a>
                <div class="h-px bg-white/20 my-4"></div>
                <button class="px-6 py-3 rounded-full border border-white/30 text-white font-medium">Log In</button>
                <button class="px-6 py-3 rounded-full bg-cyan text-white font-medium">Submit Enquiry</button>
            </div>
        </div>
'''

if '<!-- Mobile Menu Button -->' not in html:
    if '<!-- Login & Enquiry -->' in html:
        html = html.replace('<!-- Login & Enquiry -->', hamburger_html + '\n        <!-- Login & Enquiry -->', 1)
    else:
        # Just insert before </nav> if not found
        html = html.replace('</nav>', hamburger_html + '\n</nav>')

with open(r'c:\Users\Debajyoti\.antigravity\wanderon\ladakh.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated ladakh.html')
