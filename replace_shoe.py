import sys

# The image to replace
shoe_img_id = "1459749411175-04bf5292ceea"
# A stunning landscape image (mountains)
landscape_img_id = "1464822759023-fed622ff2c3b"

for filepath in ["c:/Users/Debajyoti/.antigravity/wanderon/index.html", "c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace(shoe_img_id, landscape_img_id)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
print("Replaced shoe image across both pages.")
