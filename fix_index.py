import re

with open(r'c:\Users\Debajyoti\.antigravity\wanderon\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Priority 4: Footer
html = html.replace('py-13', 'py-12')
html = html.replace('mt-13', 'mt-12')

# Priority 5: Add overflow-x: hidden to html
if 'html, body {' in html:
    html = html.replace('html, body {', 'html, body {\n            overflow-x: hidden;')
elif 'html {' in html:
    html = html.replace('html {', 'html {\n            overflow-x: hidden;')
else:
    # Just insert it before </head>
    html = html.replace('</head>', '<style>\nhtml, body { overflow-x: hidden; }\n</style>\n</head>')

# Priority 2: Hero image
html = html.replace('h-[540px] max-w-[565px]', 'h-[280px] sm:h-[360px] lg:h-[540px] max-w-[565px]')

# Priority 3: Destination cards
# Since we might have replaced h-[300px] in ladakh.html script above by accident? No, we didn't.
# We will do a generic replacement for h-[300px] to h-[200px] md:h-[300px]
html = html.replace('h-[300px]', 'h-[200px] md:h-[300px]')
# For text-3xl and p-6
html = html.replace('text-3xl text-white font-display', 'text-xl md:text-3xl text-white font-display')
html = re.sub(r'absolute bottom-0 left-0 w-full p-6', 'absolute bottom-0 left-0 w-full p-4 md:p-6', html)

# Priority 6: Events & Romantic headers
html = html.replace('p-8 lg:p-12', 'p-5 md:p-8 lg:p-12')
html = html.replace('text-[35px]', 'text-[26px] md:text-[35px]')

# Priority 1: Navbar index.html
if '<nav x-data="' not in html:
    html = html.replace('<nav class="', '<nav x-data="{ mobileMenu: false }" class="', 1)

hamburger_html = '''
        <!-- Mobile Menu Button -->
        <button @click="mobileMenu = !mobileMenu" class="lg:hidden text-dark p-2">
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
             class="fixed inset-0 z-50 bg-white lg:hidden flex flex-col pt-20 px-6">
            
            <button @click="mobileMenu = false" class="absolute top-6 right-6 text-dark p-2">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
            </button>
            
            <div class="flex flex-col gap-6 text-xl font-medium">
                <a href="#" class="text-dark">Trips</a>
                <a href="#" class="text-dark">Corporate</a>
                <a href="#" class="text-dark">Blogs</a>
                <a href="#" class="text-dark">About</a>
                <div class="h-px bg-gray-200 my-4"></div>
                <button class="px-6 py-3 rounded-full border border-gray-200 text-dark font-medium">Log In</button>
                <button class="px-6 py-3 rounded-full bg-cyan text-white font-medium">Submit Enquiry</button>
            </div>
        </div>
'''

if '<!-- Login & Enquiry -->' in html and '<!-- Mobile Menu Button -->' not in html:
    html = html.replace('<!-- Login & Enquiry -->', hamburger_html + '\n        <!-- Login & Enquiry -->', 1)

with open(r'c:\Users\Debajyoti\.antigravity\wanderon\index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated index.html')
