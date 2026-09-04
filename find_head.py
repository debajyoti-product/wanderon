with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "</head>" in line:
        print(f"--- Found </head> at line {i+1} ---")
        break
