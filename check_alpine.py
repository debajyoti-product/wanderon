import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

main_idx = html.find('<main')
print(html[main_idx:main_idx+200])

travel_styles_idx = html.find('Choose Your Travel Style')
if travel_styles_idx != -1:
    print(html[travel_styles_idx-200:travel_styles_idx+200])
