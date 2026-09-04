import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

match = re.search(r'<div id="content-activities".*?id="content-packages"', html, re.DOTALL)
if match:
    images = re.findall(r'<img src="([^"]+)".*?alt="([^"]+)">.*?<h4[^>]*>(.*?)</h4>.*?<p[^>]*>(.*?)</p>', match.group(0), re.DOTALL)
    for img, alt, title, subtitle in images:
        print(f"India: {title} | {subtitle} | {img}")

