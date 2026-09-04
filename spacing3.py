with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Search for Explore The World
idx = html.find('Explore The World')
print(html[idx-300:idx+800])
