with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "explore" in line.lower():
        print(f"Line {i+1}: {line.strip()[:100]}")
