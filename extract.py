with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

import re

# 1. India Trips (Discover Incredible India)
india_match = re.search(r'<!-- Discover Incredible India.*?<!-- Trust Corner', html, re.DOTALL)
if india_match:
    india_html = india_match.group(0).replace('<!-- Trust Corner', '')
    print("Found India HTML length:", len(india_html))
else:
    print("India not found")

# 2. Trust Corner (Testimonials)
trust_match = re.search(r'<!-- Trust Corner.*?<!-- Explore The World', html, re.DOTALL)
if trust_match:
    trust_html = trust_match.group(0).replace('<!-- Explore The World', '')
    print("Found Trust HTML length:", len(trust_html))
else:
    print("Trust not found")

# 3. International Trips (Explore The World)
intl_match = re.search(r'<!-- Explore The World.*?</section>', html, re.DOTALL)
if intl_match:
    intl_html = intl_match.group(0)
    print("Found Intl HTML length:", len(intl_html))
else:
    print("Intl not found")

