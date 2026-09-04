import os

files = [
    "c:/Users/Debajyoti/.antigravity/wanderon/index.html",
    "c:/Users/Debajyoti/.antigravity/wanderon/search.html"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # 29px * 1.05 = 30.45px -> 30.5px (or 31px)
    new_text = text.replace("lg:px-[29px]", "lg:px-[30.5px]")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_text)

print("Updated padding to 30.5px on both pages.")
