import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix Alpine.js x-data
# Current main tag: <main class="max-w-7xl mx-auto px-4 lg:px-8 py-8 flex flex-col lg:flex-row gap-12 relative">
main_start = html.find('<main class="')
main_end = html.find('>', main_start)
main_tag = html[main_start:main_end+1]
if 'x-data' not in main_tag:
    new_main_tag = main_tag.replace('>', ' x-data="{ style: \'rented\' }">')
    html = html.replace(main_tag, new_main_tag)

# 2. Fix Hero Gallery rounding
hero_gallery_old = """<div class="grid grid-cols-1 md:grid-cols-4 md:grid-rows-2 gap-2.5 h-[340px] md:h-[460px] rounded-3xl overflow-hidden cursor-pointer shadow-sm">
            <!-- Large Main Image (Left, spans 2 cols, 2 rows) -->
            <div class="col-span-1 md:col-span-2 md:row-span-2 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=1600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Ladakh Mountains">
                <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent"></div>
            </div>
            <!-- Top Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1595815771614-ade9d652a65d?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Pangong Lake">
            </div>
            <!-- Top Right 2 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Nubra Sand Dunes">
            </div>
            <!-- Bottom Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1612438214708-f428a707dd4e?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Monastery">
            </div>
            <!-- Bottom Right 2 with 12+ Overlay -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Hanle Night Sky">
                <div class="absolute inset-0 bg-black/40 group-hover:bg-black/50 transition-colors flex items-center justify-center">
                    <span class="text-white font-display font-bold text-2xl tracking-wide">12+</span>
                </div>
            </div>
        </div>"""

hero_gallery_new = """<div class="grid grid-cols-1 md:grid-cols-4 md:grid-rows-2 gap-3 md:gap-4 h-[340px] md:h-[460px] cursor-pointer">
            <!-- Large Main Image (Left, spans 2 cols, 2 rows) -->
            <div class="col-span-1 md:col-span-2 md:row-span-2 overflow-hidden relative group rounded-2xl md:rounded-[2rem]">
                <img src="https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=1600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Ladakh Mountains">
                <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent"></div>
            </div>
            <!-- Top Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group rounded-2xl">
                <img src="https://images.unsplash.com/photo-1595815771614-ade9d652a65d?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Pangong Lake">
            </div>
            <!-- Top Right 2 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group rounded-2xl md:rounded-tr-[2rem]">
                <img src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Nubra Sand Dunes">
            </div>
            <!-- Bottom Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group rounded-2xl">
                <img src="https://images.unsplash.com/photo-1612438214708-f428a707dd4e?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Monastery">
            </div>
            <!-- Bottom Right 2 with 12+ Overlay -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group rounded-2xl md:rounded-br-[2rem]">
                <img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Hanle Night Sky">
                <div class="absolute inset-0 bg-black/40 group-hover:bg-black/50 transition-colors flex items-center justify-center">
                    <span class="text-white font-display font-bold text-2xl tracking-wide">12+</span>
                </div>
            </div>
        </div>"""
html = html.replace(hero_gallery_old, hero_gallery_new)

# 3. Update CTA Button Size
old_cta = """<button class="w-full bg-brand-cyan text-white py-4 rounded-full font-display font-bold text-lg shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-phone-volume text-xl"></i> Get a Call Back
                </button>"""
new_cta = """<button class="w-full bg-brand-cyan text-white py-[14px] rounded-full font-display font-bold text-base shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-phone-volume text-lg"></i> Get a Call Back
                </button>"""
html = html.replace(old_cta, new_cta)

# 4. Update Logistics
old_logistics = """<div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8">
                <div class="flex-[0.8]">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Logistics</div>
                    <div class="flex items-center gap-3 font-semibold text-gray-800 text-sm mb-3">
                        <div class="w-6 h-6 rounded-full bg-brand-cyan/20 flex items-center justify-center text-brand-cyan text-xs"><i class="fa-solid fa-plane-arrival"></i></div>
                        <div><span class="text-gray-400 text-xs font-normal block">Pickup</span> Delhi</div>
                    </div>
                    <div class="flex items-center gap-3 font-semibold text-gray-800 text-sm">
                        <div class="w-6 h-6 rounded-full bg-brand-yellow/20 flex items-center justify-center text-brand-yellow text-xs"><i class="fa-solid fa-plane-departure"></i></div>
                        <div><span class="text-gray-400 text-xs font-normal block">Drop</span> Srinagar</div>
                    </div>
                </div>"""
new_logistics = """<div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8">
                <div class="flex gap-8 md:gap-12 flex-[0.8]">
                    <div>
                        <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Pickup</div>
                        <div class="font-semibold text-gray-800 text-sm">Delhi</div>
                    </div>
                    <div>
                        <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Drop</div>
                        <div class="font-semibold text-gray-800 text-sm">Srinagar</div>
                    </div>
                </div>"""
html = html.replace(old_logistics, new_logistics)

# 5. Similar Trips Updates
old_similar_header = """<div class="flex items-end justify-between mb-8">
            <div>
                <h2 class="font-display font-extrabold text-3xl md:text-4xl text-brand-dark mb-3">Similar Trips</h2>
                <p class="text-gray-500 text-sm md:text-base">Explore more adventures that match your vibe.</p>
            </div>
            
            <!-- Category Pills -->
            <div class="hidden md:flex gap-3">
                <button class="px-5 py-2 rounded-full bg-brand-cyan text-white text-sm font-bold shadow-md shadow-cyan-500/20">Super Saver</button>
                <button class="px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold hover:border-brand-cyan hover:text-brand-cyan transition-colors">Best Sellers</button>
                <button class="px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold hover:border-brand-cyan hover:text-brand-cyan transition-colors">Exclusive</button>
            </div>
        </div>"""
        
new_similar_header = """<div class="flex flex-col gap-4 mb-8">
            <h2 class="font-display font-extrabold text-3xl md:text-4xl text-brand-dark">Similar Trips</h2>
            
            <!-- Category Pills -->
            <div class="hidden md:flex flex-wrap gap-3">
                <a href="#" class="px-5 py-2 rounded-full bg-brand-cyan text-white text-sm font-bold shadow-md shadow-cyan-500/20 hover:-translate-y-0.5 transition-transform">Super Saver</a>
                <a href="#" class="px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold hover:border-brand-cyan hover:text-brand-cyan hover:-translate-y-0.5 transition-all">Best Sellers</a>
                <a href="#" class="px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold hover:border-brand-cyan hover:text-brand-cyan hover:-translate-y-0.5 transition-all">Exclusive</a>
            </div>
        </div>"""
html = html.replace(old_similar_header, new_similar_header)

old_card_img = '<img src="https://images.unsplash.com/photo-1596773256086-63044a30e797?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">'
new_card_img = '<img src="https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">'
html = html.replace(old_card_img, new_card_img)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated everything successfully.")
