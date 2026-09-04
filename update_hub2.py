import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace max-w-7xl with max-w-5xl specifically inside the expanded sections.
# We can find the sections based on their unique headers.
def replace_in_section(html, section_marker):
    idx = html.find(section_marker)
    if idx != -1:
        target = '<div class="max-w-7xl mx-auto px-4 lg:px-8 relative z-10">'
        replacement = '<div class="max-w-5xl mx-auto px-4 lg:px-8 relative z-10">'
        # find the target after idx
        target_idx = html.find(target, idx)
        if target_idx != -1 and target_idx - idx < 1000:
            html = html[:target_idx] + html[target_idx:].replace(target, replacement, 1)
    return html

html = replace_in_section(html, '<!-- Discover Incredible India')
html = replace_in_section(html, '<!-- Explore The World')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("max-w-5xl replaced successfully.")
