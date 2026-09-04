import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

def generate_cards(items, color_class):
    cards_html = []
    for title, subtitle, img in items:
        # replace w=200 with w=800
        img = img.replace('w=200', 'w=800')
        card = f"""
                    <div class="group cursor-pointer relative h-[380px] rounded-3xl overflow-hidden shadow-soft hover:shadow-float transition-all duration-500 border-[6px] border-white/90">
                        <img src="{img}" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" alt="{title}">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/30 to-transparent opacity-80 group-hover:opacity-90 transition-opacity"></div>
                        <div class="absolute bottom-0 left-0 w-full p-8 text-center translate-y-4 group-hover:translate-y-0 transition-transform duration-500 flex flex-col items-center">
                            <h4 class="font-bold text-white text-3xl mb-1">{title}</h4>
                            <p class="text-white/80 font-medium text-sm mb-2">{subtitle}</p>
                            <div class="w-12 h-1 bg-{color_class} opacity-0 group-hover:opacity-100 transition-opacity duration-500"></div>
                        </div>
                    </div>"""
        cards_html.append(card)
    return "\n".join(cards_html)

india_items = [
    ("Winter Expeditions", "8 Trips", "https://images.unsplash.com/photo-1479888230021-c24f136d849f?q=80&w=800&auto=format&fit=crop"),
    ("Bike Trips", "12 Trips", "https://images.unsplash.com/photo-1558981806-ec527fa84c39?q=80&w=800&auto=format&fit=crop"),
    ("Trekking", "20 Trips", "https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=800&auto=format&fit=crop"),
    ("Leisure", "15 Trips", "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=800&auto=format&fit=crop"),
    ("Backpacking", "35 Trips", "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=800&auto=format&fit=crop")
]

intl_items = [
    ("Island Hopping", "18 Trips", "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?q=80&w=800&auto=format&fit=crop"),
    ("Scuba Diving", "10 Trips", "https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=800&auto=format&fit=crop"),
    ("Northern Lights", "5 Trips", "https://images.unsplash.com/photo-1579033461380-adb47c3eb938?q=80&w=800&auto=format&fit=crop"),
    ("Safari", "8 Trips", "https://images.unsplash.com/photo-1516426122078-c23e76319801?q=80&w=800&auto=format&fit=crop"),
    ("Backpacking", "40 Trips", "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=800&auto=format&fit=crop")
]

india_html = f"""<div id="content-activities" class="mb-8 hidden transition-opacity duration-300">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
{generate_cards(india_items, "brand-yellow")}
                </div>
            </div>"""

intl_html = f"""<div id="content-intl-activities" class="mb-8 hidden transition-opacity duration-300">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
{generate_cards(intl_items, "brand-cyan")}
                </div>
            </div>"""

html = re.sub(r'<div id="content-activities".*?(?=<!-- 3\. FEATURED PACKAGES -->)', india_html + '\n\n            ', html, flags=re.DOTALL)
html = re.sub(r'<div id="content-intl-activities".*?(?=<!-- 3\. FEATURED PACKAGES -->)', intl_html + '\n\n            ', html, flags=re.DOTALL)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Replacement successful")
