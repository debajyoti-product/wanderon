import sys

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    ladakh_html = f.read()

print("--- index.html 'Pine Forests' ---")
idx = index_html.find("Pine Forests")
if idx != -1:
    print(index_html[idx-300:idx+100])

print("\n--- index.html 'Living Root' ---")
idx = index_html.find("Living Root")
if idx != -1:
    print(index_html[idx-300:idx+100])
    
print("\n--- ladakh.html Hero Gallery ---")
idx = ladakh_html.find("Hero Gallery")
if idx != -1:
    print(ladakh_html[idx:idx+1500])

print("\n--- index.html Community Section Cards ---")
idx = index_html.find("Community Trips")
if idx != -1:
    idx2 = index_html.find("bg-white rounded-3xl overflow-hidden", idx)
    print(index_html[idx2-50:idx2+500])
    
