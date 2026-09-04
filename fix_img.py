import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix the broken images first
html = html.replace('1470229722913-7c092bb5ace1', '1459749411175-04bf5292ceea')
html = html.replace('1533174000255-a63b8a1183f1', '1510414842594-a61c69b5ae57')
html = html.replace('1610017173740-4286f9f9b5c8', '1499678329028-101435549a4e')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Images fixed!")
