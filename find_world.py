with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "International" in line or "World" in line or "Filter Tabs" in line:
        print(f"--- Found at line {i+1} --- {line.strip()}")
