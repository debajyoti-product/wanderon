import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Revert Community Trips
html = html.replace('mb-[18px]', 'mb-5')
html = html.replace('mb-[21px]', 'mb-6')

# Revert India/Intl Headers
# They are currently `<div class="text-center max-w-3xl mx-auto mb-9">`
html = html.replace('<div class="text-center max-w-3xl mx-auto mb-9">', '<div class="text-center max-w-3xl mx-auto mb-10">')

# Revert Tabs
# They are currently `<div class="flex flex-wrap justify-center items-center gap-4 mb-9">`
html = html.replace('<div class="flex flex-wrap justify-center items-center gap-4 mb-9">', '<div class="flex flex-wrap justify-center items-center gap-4 mb-13">')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Reverted spacing changes.")
