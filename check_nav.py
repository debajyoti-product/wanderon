with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines[:200]):
    if any(k in line.lower() for k in ["weekends", "global", "community", "corporate"]):
        print(f"Line {i+1}: {line.strip()}")
