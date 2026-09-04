with open("c:/Users/Debajyoti/.antigravity/wanderon/search.html", "r", encoding="utf-8") as f:
    text = f.read()

# check sortOptions
start = text.find("sortOptions:")
if start != -1:
    print(text[start:start+400])
