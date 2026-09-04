import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find trips-hub bounds
hub_match = re.search(r'<!-- COMBINED TRIPS HUB \(DOMESTIC & INTL\) -->.*?<section id="trips-hub".*?(?=<!-- Testimonials Section -->)', html, re.DOTALL)
if hub_match:
    hub_html = hub_match.group(0)
    
    # Extract India
    india_match = re.search(r'<!-- Discover Incredible India.*?bg-\[#faf9f6\]">.*?</section>', hub_html, re.DOTALL)
    if not india_match:
        print("Could not find India section inside hub")
        exit(1)
    india_str = india_match.group(0)
    india_str = india_str.replace('max-w-5xl', 'max-w-7xl')
    
    # Extract Intl
    intl_match = re.search(r'<!-- Explore The World.*?bg-\[#f6f9fc\]">.*?</section>', hub_html, re.DOTALL)
    if not intl_match:
        print("Could not find Intl section inside hub")
        exit(1)
    intl_str = intl_match.group(0)
    intl_str = intl_str.replace('max-w-5xl', 'max-w-7xl')
    
    # Replace the hub with the consecutive sections
    new_html = html[:hub_match.start()] + india_str + "\n\n    " + intl_str + "\n\n    " + html[hub_match.end():]
    
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully replaced trips-hub with separate sections.")
else:
    print("Could not find trips-hub")
    
