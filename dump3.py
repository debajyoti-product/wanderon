import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

match = re.search(r'<div id="content-activities".*?<div id="content-packages"', html, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Not found")

match_intl = re.search(r'<div id="content-intl-activities".*?<div id="content-intl-packages"', html, re.DOTALL)
if match_intl:
    print("--- INTL ACTIVITIES ---")
    print(match_intl.group(0))
else:
    print("Intl not found")

