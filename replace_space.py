import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Community trips
# Header to pills
html = html.replace('<!-- Header -->\n            <div class="mb-5">', '<!-- Header -->\n            <div class="mb-[18px]">')
# Pills to cards
html = html.replace('<!-- Month Filters & View All -->\n            <div class="flex items-center justify-between gap-4 pb-3 mb-6', '<!-- Month Filters & View All -->\n            <div class="flex items-center justify-between gap-4 pb-3 mb-[21px]')

# 2. India Trips
# The header container has mb-10. We change it to mb-9 (10% reduction, 40px -> 36px)
# But only for India and International
india_idx = html.find('Discover Incredible India')
if india_idx != -1:
    header_start = html.rfind('<div class="text-center max-w-3xl mx-auto mb-10">', 0, india_idx)
    if header_start != -1:
        html = html[:header_start] + html[header_start:].replace('mb-10', 'mb-9', 1)
    
    # Tab to cards
    tab_start = html.find('<!-- Interactive Filter Tabs -->', india_idx)
    if tab_start != -1:
        tab_div = html.find('<div class="flex flex-wrap justify-center items-center gap-4 mb-13">', tab_start)
        if tab_div != -1:
            html = html[:tab_div] + html[tab_div:].replace('mb-13', 'mb-9', 1)

# 3. International Trips
intl_idx = html.find('Explore The World')
if intl_idx != -1:
    header_start = html.rfind('<div class="text-center max-w-3xl mx-auto mb-10">', 0, intl_idx)
    if header_start != -1:
        html = html[:header_start] + html[header_start:].replace('mb-10', 'mb-9', 1)
        
    # Tab to cards
    tab_start = html.find('<!-- Interactive Filter Tabs -->', intl_idx)
    if tab_start != -1:
        tab_div = html.find('<div class="flex flex-wrap justify-center items-center gap-4 mb-13">', tab_start)
        if tab_div != -1:
            html = html[:tab_div] + html[tab_div:].replace('mb-13', 'mb-9', 1)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Spacing updated successfully.")
