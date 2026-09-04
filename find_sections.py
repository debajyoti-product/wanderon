with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "Events" in line or "Romantic" in line or "India" in line:
        print(f"--- Found at line {i+1} ---")
        start = max(0, i-5)
        end = min(len(lines), i+5)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        print("-" * 40)
