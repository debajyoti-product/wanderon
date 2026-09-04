with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find selectBudget with different indentation
if "selectBudget" in html:
    lines = html.split("\n")
    new_lines = []
    skip = False
    for i, line in enumerate(lines):
        if "function selectBudget" in line:
            skip = True
            continue
        if skip and "}" in line and "closeHeroModals" not in line:
            skip = False
            continue
        if skip:
            continue
        new_lines.append(line)
    html = "\n".join(new_lines)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Removed selectBudget function")
else:
    print("selectBudget already removed or not found")
