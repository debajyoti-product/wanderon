with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'class="[^"]*grid-cols-[^"]*"', text)
for m in set(matches):
    print(m)
