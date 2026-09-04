with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("--- India Tabs ---")
print("".join(lines[850:880]))

print("--- International Tabs ---")
print("".join(lines[1320:1350]))
