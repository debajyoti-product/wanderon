with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Replace max-w-7xl and max-w-[1400px] with max-w-[1440px]
text = text.replace("max-w-7xl", "max-w-[1440px]")
text = text.replace("max-w-[1400px]", "max-w-[1440px]")

# Replace lg:px-8 with lg:px-[27px] (or lg:px-6)
# Actually, the user asked for 15%. lg:px-[27px] is exactly 15% less than 32px.
text = text.replace("lg:px-8", "lg:px-[27px]")

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated index.html")
