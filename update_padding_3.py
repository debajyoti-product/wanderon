import os

files = [
    "c:/Users/Debajyoti/.antigravity/wanderon/index.html",
    "c:/Users/Debajyoti/.antigravity/wanderon/search.html"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Change to standard px-8 (32px) to guarantee CDN parsing and give a slightly larger, visible bump
    new_text = text.replace("lg:px-[30.5px]", "lg:px-[34px]")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_text)

print("Updated padding to 34px.")
