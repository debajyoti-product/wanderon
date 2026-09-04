import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

right_col_start = html.find('<!-- Right Column: Sticky Booking Widget -->')
right_col_end = html.find('</main>', right_col_start)

print(html[right_col_start:right_col_end])
