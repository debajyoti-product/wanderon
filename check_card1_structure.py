import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_idx = html.find('Upcoming Community Trips')
card1_idx = html.find('<!-- Card 1 -->', start_idx)
card2_idx = html.find('<!-- Card 2 -->', start_idx)

if card1_idx != -1 and card2_idx != -1:
    print(html[card1_idx:card2_idx])
