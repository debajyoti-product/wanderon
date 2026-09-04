with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# Marker before Similar Trips
sim_start_marker = '<section class="max-w-7xl mx-auto px-4 lg:px-8 pb-20">'
sim_end_marker = '</section>'
sim_start = html.find(sim_start_marker)
sim_end = html.find(sim_end_marker, sim_start) + len(sim_end_marker)
similar_trips_block = html[sim_start:sim_end]

# Marker for Reviews
rev_start_marker = '<!-- Social Proof / Reviews (TourHero Inspiration) -->'
rev_end_marker = '    <!-- Footer placeholder -->'
rev_start = html.find(rev_start_marker)
rev_end = html.find(rev_end_marker)
reviews_block = html[rev_start:rev_end].strip()

# Now construct the swapped version:
# After </main>, put reviews, then similar trips.
between_main_and_sim = html[html.find('</main>') + len('</main>'):sim_start]

# Adjust classes for clean spacing:
# Reviews first:
reviews_block_updated = reviews_block.replace('mt-16 pt-12 border-t border-gray-100 mb-12', 'mt-16 pt-12 border-t border-gray-100 mb-16')
# Similar trips second:
similar_trips_block_updated = similar_trips_block.replace('class="max-w-7xl mx-auto px-4 lg:px-8 pb-20"', 'class="max-w-7xl mx-auto px-4 lg:px-8 pt-12 border-t border-gray-100 pb-20"')

full_old_segment = html[sim_start:rev_end]
full_new_segment = reviews_block_updated + "\n\n    " + similar_trips_block_updated + "\n\n"

html = html.replace(full_old_segment, full_new_segment)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully swapped Similar Trips and Reviews sections.")
