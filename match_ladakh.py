import os

files = [
    "c:/Users/Debajyoti/.antigravity/wanderon/index.html",
    "c:/Users/Debajyoti/.antigravity/wanderon/search.html"
]

for filepath in files:
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Revert max-width and padding to match ladakh.html
    text = text.replace("max-w-[1440px]", "max-w-7xl")
    text = text.replace("lg:px-[34px]", "lg:px-8")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

print("Reverted container classes to match ladakh.html")
