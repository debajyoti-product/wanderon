import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

print("\n--- PACKAGES ---")
match2 = re.search(r'<div id="content-packages".*?</div>\s*</div>\s*</div>\s*</div>', html, re.DOTALL)
if match2:
    print(match2.group(0)[:1000])

