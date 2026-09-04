with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_hub = html.find('<!-- COMBINED TRIPS HUB')
end_hub = html.find('<!-- Trust Corner (Testimonials)')

if start_hub != -1 and end_hub != -1:
    hub_html = html[start_hub:end_hub]
    
    # Extract India
    i_start = hub_html.find('<!-- Discover Incredible India')
    i_end = hub_html.find('</section>', i_start) + 10
    india_str = hub_html[i_start:i_end].replace('max-w-5xl', 'max-w-7xl')
    
    # Extract Intl
    in_start = hub_html.find('<!-- Explore The World')
    in_end = hub_html.find('</section>', in_start) + 10
    intl_str = hub_html[in_start:in_end].replace('max-w-5xl', 'max-w-7xl')
    
    new_html = html[:start_hub] + india_str + "\n\n    " + intl_str + "\n\n    " + html[end_hub:]
    
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Successfully replaced trips-hub with separate sections.")
else:
    print("Could not find bounds.")
