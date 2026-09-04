import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# EXTRACT INDIA
india_match = re.search(r'(<!-- Discover Incredible India.*?)(?=<!-- Trust Corner)', html, re.DOTALL)
if not india_match:
    print("India not found")
india_html = india_match.group(1)

# EXTRACT TRUST
trust_match = re.search(r'(<!-- Trust Corner.*?)(?=<!-- Explore The World)', html, re.DOTALL)
if not trust_match:
    print("Trust not found")
trust_html = trust_match.group(1)

# EXTRACT INTL
intl_match = re.search(r'(<!-- Explore The World.*?</section>)', html, re.DOTALL)
if not intl_match:
    print("Intl not found")
intl_html = intl_match.group(1)

# Strip out outer <section> tags from India and Intl so we don't have nested sections ruining height logic.
# Wait, India and Intl already have <section class="py-20 relative overflow-hidden bg-[...]">
# We can just leave them as they are and wrap them in a div, but they will dictate height if we don't absolute position them.
# It's better to keep them as they are, but inside the expanded view.

print("Extracted successfully.")
