import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Fonts
old_font = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">'
new_font = '<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Lilita+One&family=Playfair+Display:ital,wght@1,600;1,700&display=swap" rel="stylesheet">'
html = html.replace(old_font, new_font)

# 2. Reduce gap in India section
# Currently: <div class="text-center max-w-3xl mx-auto mb-9"> right above #indiatrips
html = re.sub(
    r'(<div class="text-center max-w-3xl mx-auto) mb-9(">\s*<div class="inline-flex[^>]*>\s*#indiatrips)',
    r'\1 mb-6\2',
    html
)
html = re.sub(
    r'(<div class="flex flex-wrap justify-center items-center gap-4) mb-9(">)',
    r'\1 mb-6\2',
    html
)

# 3. Reduce gap in World section
# Currently: <div class="text-center max-w-3xl mx-auto mb-10"> right above #internationaltrips
html = re.sub(
    r'(<div class="text-center max-w-3xl mx-auto) mb-10(">\s*<div class="inline-flex[^>]*>\s*#internationaltrips)',
    r'\1 mb-7\2',
    html
)
html = re.sub(
    r'(<div class="flex flex-wrap justify-center items-center gap-4) mb-9(">\s*<div class="bg-white/80 backdrop-blur-md p-1.5 rounded-full shadow-soft border border-white flex items-center">\s*<button id="btn-intl-destinations")',
    r'\1 mb-7\2',
    html
)


# 4. Events Header
old_events = '<h2 class="font-display font-semibold text-[32px] lg:text-[43px] text-gray-800 tracking-tight mb-2">\n                                Events &amp; Festivals\n                            </h2>'
new_events = '<h2 class="text-[35px] lg:text-[48px] tracking-wide mb-2" style="font-family: \'Lilita One\', sans-serif; color: black; line-height: 1.1;">\n                                Events &amp; Festivals\n                            </h2>'
html = html.replace(old_events, new_events)

# 5. Romantic Header
old_romantic = '<h2 class="font-display font-semibold text-[32px] lg:text-[43px] text-gray-800 tracking-tight mb-2">\n                                Romantic Escapes\n                            </h2>'
new_romantic = '<h2 class="text-[35px] lg:text-[46px] tracking-tight mb-2" style="font-family: \'Playfair Display\', serif; font-style: italic; font-weight: 700; color: black; line-height: 1.1;">\n                                Romantic Escapes\n                            </h2>'
html = html.replace(old_romantic, new_romantic)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully")
