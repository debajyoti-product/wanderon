import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

start = html.find("<!-- Route & Logistics -->")
end = html.find('<h2 class="font-display font-bold text-2xl text-brand-dark mb-8">Daily Itinerary</h2>')
print(html[start:end])
