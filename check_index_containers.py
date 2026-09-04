import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Find all max-w-* container classes
matches = re.findall(r'class="[^"]*max-w-(?:7xl|5xl|6xl|\[1400px\])[^"]*"', text)
for m in set(matches):
    print(m)
