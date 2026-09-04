import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's verify markers
print("Left col start:", html.find('<!-- Left Column: Story & Details -->'))
print("Right col start:", html.find('<!-- Right Column: Sticky Booking Widget -->'))
