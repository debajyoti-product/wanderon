import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. 90/10 Stack Ratio
# Replace flex-[4] with flex-[9]
html = html.replace('flex-[4]', 'flex-[9]')

# Also update the JS logic
# It already replaces flex-[1] with flex-[9] instead of flex-[4] now.
# Wait, the JS string literally says 'flex-[4]'. Let's replace that too.
# The JS string replace above catches everything including the script!

# 2. Blur the collapsed backgrounds
# Find dom-col and intl-col images
html = re.sub(
    r'(<div id="dom-col".*?<img src="[^"]+" class="[^"]+)( opacity-40)', 
    r'\1 blur-md\2', 
    html, flags=re.DOTALL
)
html = re.sub(
    r'(<div id="intl-col".*?<img src="[^"]+" class="[^"]+)( opacity-40)', 
    r'\1 blur-md\2', 
    html, flags=re.DOTALL
)

# 3. Reduce Card Sizes
# Height: 380px -> 304px (approx 300px)
html = html.replace('h-[380px]', 'h-[300px]')

# Text inside cards:
# Destinations: <h4 class="font-bold text-white text-3xl mb-2"> -> text-2xl
html = html.replace('text-3xl mb-2', 'text-2xl mb-1')
# Activities: <h4 class="font-bold text-white text-3xl mb-1"> -> text-2xl
html = html.replace('text-3xl mb-1', 'text-2xl mb-1')

# What about Packages width? To reduce width by 20%, we can add px-8 or increase gap, or change container max-w.
# If we change `max-w-7xl` to `max-w-[1000px]` (which is roughly 20% less than 1280px) for these sections.
html = re.sub(
    r'(<section class="py-20 relative overflow-hidden bg-\[#[^\]]+\]">\s*<!-- 3D [^>]+-->\s*<div[^>]+>.*?</div>\s*<div class=")max-w-7xl(")',
    r'\1max-w-5xl\2', 
    html, flags=re.DOTALL
)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Updates applied.")
