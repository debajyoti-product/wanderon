with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

idx = html.find('App Store')
if idx == -1:
    idx = html.find('Download')

if idx != -1:
    start = html.rfind('<section', 0, idx)
    end = html.find('</section>', idx) + 10
    print("Found App Store section:")
    print(html[start:start+300])
    print("...")
    print(html[end-300:end])
else:
    print("App Store section not found")
