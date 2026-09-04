with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "<footer" in line.lower() or "<!-- Footer" in line:
        print(f"--- Footer found around line {i+1} ---")
        start = max(0, i-20)
        end = min(len(lines), i+10)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
        break
