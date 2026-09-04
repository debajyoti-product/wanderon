with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

idx = html.find('<!-- Dual Vibe Sections: Events & Romantic -->')
if idx != -1:
    print(html[idx:idx+2500])
else:
    print("Not found")
