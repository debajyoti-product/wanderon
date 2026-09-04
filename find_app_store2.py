import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

app_match = re.search(r'<section class="py-16 bg-brand-cream">.*?</section>', html, re.DOTALL)
if app_match:
    print("Length of App Store section:", len(app_match.group(0)))
else:
    print("Regex match failed")
