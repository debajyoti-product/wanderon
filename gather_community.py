import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

idx = index_html.find("Community Trips")
start = index_html.find('<a href="ladakh.html"', idx)
end = index_html.find('</a>', start)
print(index_html[start:end+4])
