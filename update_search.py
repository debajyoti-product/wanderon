with open("c:/Users/Debajyoti/.antigravity/wanderon/search.html", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("max-w-7xl", "max-w-[1440px]")
text = text.replace("lg:px-8", "lg:px-[27px]")
text = text.replace(
    'class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8"', 
    'class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6 lg:gap-8"'
)

with open("c:/Users/Debajyoti/.antigravity/wanderon/search.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated search.html")
