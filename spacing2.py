with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Search for India Trips header
idx2 = html.find('text-[41px]')
while idx2 != -1:
    snip = html[idx2-100:idx2+200]
    if 'India' in snip:
        print("\n--- India Header ---")
        print(html[idx2-300:idx2+500])
        break
    idx2 = html.find('text-[41px]', idx2+1)

