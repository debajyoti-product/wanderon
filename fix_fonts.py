import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace('text-[36px] lg:text-[43px]', 'text-[32px] lg:text-[43px]')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Font size adjusted for mobile.")
