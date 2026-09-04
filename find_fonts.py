with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines[:20]):
    if "googleapis.com" in line:
        print(f"--- Found at line {i+1} --- {line.strip()}")
