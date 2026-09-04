import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

def replace_in_section(html, section_marker, end_marker):
    start = html.find(section_marker)
    if start == -1: return html
    end = html.find(end_marker, start)
    if end == -1: end = start + 50000
    
    section_html = html[start:end]
    
    # Packages Title: text-lg -> text-base
    section_html = section_html.replace('text-lg text-brand-dark', 'text-base text-brand-dark')
    # Price: text-lg -> text-base
    section_html = section_html.replace('text-lg leading-none', 'text-base leading-none')
    # Destinations/Activities Padding: p-8 -> p-6
    section_html = section_html.replace('w-full p-8 text-center', 'w-full p-6 text-center')
    
    return html[:start] + section_html + html[end:]

html = replace_in_section(html, 'id="dom-exp"', 'id="dom-col"')
html = replace_in_section(html, 'id="intl-exp"', 'id="intl-col"')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Text adjustments complete.")
