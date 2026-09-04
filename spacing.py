with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import sys
sys.stdout.reconfigure(encoding='utf-8')

# Let's find headings like "Upcoming Community Trips" or similar
idx1 = html.find('Community Trips')
if idx1 != -1:
    print("--- Community Trips ---")
    print(html[idx1-200:idx1+1000])

idx2 = html.find('India Trips')
if idx2 != -1:
    print("\n--- India Trips ---")
    print(html[idx2-200:idx2+1000])

idx3 = html.find('Explore The World')
if idx3 != -1:
    print("\n--- International Trips ---")
    print(html[idx3-200:idx3+1000])

