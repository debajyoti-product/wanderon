import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

idx1 = index_html.find("Pine Forests")
start1 = index_html.rfind('<img', 0, idx1)
end1 = index_html.find('>', start1)
print("Pine Forests Img:")
print(index_html[start1:end1+1])
