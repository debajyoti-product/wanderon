import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find("Full Route")
if idx != -1:
    print(html[idx-100:idx+800])
