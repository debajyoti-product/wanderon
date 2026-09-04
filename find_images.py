import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

for filepath in ["c:/Users/Debajyoti/.antigravity/wanderon/index.html", "c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        urls = re.findall(r'src="(https://images.unsplash.com/[^"]+)"', content)
        print(f"--- {filepath} ---")
        for url in set(urls):
            print(url)
