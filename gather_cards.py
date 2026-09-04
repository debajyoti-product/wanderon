import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Find the card containing "Pine Forests"
idx1 = index_html.find("Pine Forests")
start1 = index_html.rfind('<a href=', 0, idx1)
end1 = index_html.find('</a>', idx1)
print("Pine Forests Card:")
print(index_html[start1:end1+4])

# Find the card containing "Living Root"
idx2 = index_html.find("Living Root")
start2 = index_html.rfind('<a href=', 0, idx2)
end2 = index_html.find('</a>', idx2)
print("\nLiving Root Card:")
print(index_html[start2:end2+4])
