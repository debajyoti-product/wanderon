with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "General Inclusions" in line:
        print(f"--- Found at line {i+1} ---")
        start = max(0, i-10)
        end = min(len(lines), i+30)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        break
