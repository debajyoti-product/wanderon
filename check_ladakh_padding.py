with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
# Find main containers in ladakh.html
matches = re.findall(r'class="[^"]*max-w-[^"]*px-[^"]*"', text)
for m in set(matches[:20]):
    print(m)
