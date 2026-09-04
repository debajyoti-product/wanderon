import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace any remaining mb-13 with mb-9
html = html.replace('mb-13', 'mb-9')

# Replace mb-10 in the section headers for India/Intl Trips
html = html.replace('<div class="text-center max-w-3xl mx-auto mb-10">', '<div class="text-center max-w-3xl mx-auto mb-9">')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("All mb-13 and mb-10 fixed.")
