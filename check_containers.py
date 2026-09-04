with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'class="[^"]*max-w-[^"]*"', text)
for m in set(matches[:30]):
    print(m)
