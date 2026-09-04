import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

def extract_section(start_marker):
    start = html.find(start_marker)
    if start == -1: return None, html
    end = html.find('</section>', start) + 10
    
    # Expand start backwards to include leading whitespace/newlines if any
    while start > 0 and html[start-1] in ['\n', ' ', '\t']:
        start -= 1
        
    section_str = html[start:end]
    new_html = html[:start] + html[end:]
    return section_str, new_html

# We need to extract WanderOn Across World and Stories, then re-insert them
# Let's extract them from the bottom up to avoid index shifting

# 1. WanderOn Across The World
wanderon_world, html = extract_section('<!-- WanderOn Across The World')
# 2. Stories
stories, html = extract_section('<!-- Trust Corner')

# Now the remaining HTML has:
# ... Community Trips ...
# ... India Trips ...
# ... Intl Trips ...

# Let's find insertion points
# Insert WanderOn Across The World after Community Trips (before India Trips)
india_start = html.find('<!-- Discover Incredible India')
if india_start != -1:
    html = html[:india_start] + "\n\n" + wanderon_world + "\n\n" + html[india_start:]

# Insert Stories between India and Intl
intl_start = html.find('<!-- Explore The World')
if intl_start != -1:
    html = html[:intl_start] + "\n\n" + stories + "\n\n" + html[intl_start:]

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Reordered successfully!")
