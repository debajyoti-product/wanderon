with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.finditer(r'<header[^>]*>', text)
for m in matches:
    start = m.start()
    print(text[start:start+1500])
    break
