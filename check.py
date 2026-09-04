with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

print(html.find('id="content-activities"'))
print(html.find('id="content-intl-activities"'))
print(html.find('<!-- 3. FEATURED PACKAGES -->'))

