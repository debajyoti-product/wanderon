import os

files = [
    "c:/Users/Debajyoti/.antigravity/wanderon/index.html",
    "c:/Users/Debajyoti/.antigravity/wanderon/search.html"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Replace lg:px-[27px] with lg:px-[29px]
    new_text = text.replace("lg:px-[27px]", "lg:px-[29px]")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_text)

print("Updated padding on both pages.")
