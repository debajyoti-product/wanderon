import sys

# 1. Image Replacements (The ACTUAL shoe image)
bad_img_id = "1518002171953-a080ee817e1f"
good_img_id = "1464822759023-fed622ff2c3b"

for filepath in ["c:/Users/Debajyoti/.antigravity/wanderon/index.html", "c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html"]:
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace(bad_img_id, good_img_id)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    ladakh_html = f.read()

# 2. Similar Trips Card Design
# Update ladakh.html Similar trips cards to match Community Section Cards design
old_similar_cards = """<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Card 1 -->
            <a href="#" class="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 group hover:shadow-xl transition-all duration-300 block">
                <div class="relative h-56 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-bold text-gray-800 uppercase tracking-wide">6N / 7D</div>
                </div>
                <div class="p-5">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-brand-cyan text-xs font-bold uppercase tracking-widest"><i class="fa-solid fa-location-dot mr-1"></i> Ladakh</span>
                        <div class="flex items-center gap-1 text-sm font-bold text-gray-700">
                            <i class="fa-solid fa-star text-brand-yellow text-[10px]"></i> 4.9
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-lg text-brand-dark leading-tight mb-2 group-hover:text-brand-cyan transition-colors">Leh & Pangong Highlights</h3>
                    <p class="text-xs text-gray-500 mb-4 line-clamp-2">A quick getaway covering the best of Leh and the iconic Pangong Lake.</p>
                    <div class="flex items-center justify-between pt-4 border-t border-gray-100">
                        <div>
                            <div class="text-[10px] text-gray-400 font-bold uppercase">Starting from</div>
                            <div class="font-display font-bold text-lg text-brand-dark">₹18,500</div>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-right -rotate-45"></i>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 2 -->
            <a href="#" class="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 group hover:shadow-xl transition-all duration-300 block">
                <div class="relative h-56 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1595815771614-ade9d652a65d?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-bold text-gray-800 uppercase tracking-wide">8N / 9D</div>
                </div>
                <div class="p-5">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-brand-cyan text-xs font-bold uppercase tracking-widest"><i class="fa-solid fa-location-dot mr-1"></i> Spiti Valley</span>
                        <div class="flex items-center gap-1 text-sm font-bold text-gray-700">
                            <i class="fa-solid fa-star text-brand-yellow text-[10px]"></i> 4.8
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-lg text-brand-dark leading-tight mb-2 group-hover:text-brand-cyan transition-colors">Spiti Circuit Winter Expedition</h3>
                    <p class="text-xs text-gray-500 mb-4 line-clamp-2">Experience the white winter wonderland of the middle land.</p>
                    <div class="flex items-center justify-between pt-4 border-t border-gray-100">
                        <div>
                            <div class="text-[10px] text-gray-400 font-bold uppercase">Starting from</div>
                            <div class="font-display font-bold text-lg text-brand-dark">₹22,000</div>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-right -rotate-45"></i>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 3 -->
            <a href="#" class="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 group hover:shadow-xl transition-all duration-300 block">
                <div class="relative h-56 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-bold text-gray-800 uppercase tracking-wide">5N / 6D</div>
                </div>
                <div class="p-5">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-brand-cyan text-xs font-bold uppercase tracking-widest"><i class="fa-solid fa-location-dot mr-1"></i> Kashmir</span>
                        <div class="flex items-center gap-1 text-sm font-bold text-gray-700">
                            <i class="fa-solid fa-star text-brand-yellow text-[10px]"></i> 4.9
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-lg text-brand-dark leading-tight mb-2 group-hover:text-brand-cyan transition-colors">Paradise on Earth Tour</h3>
                    <p class="text-xs text-gray-500 mb-4 line-clamp-2">Srinagar, Gulmarg, and Pahalgam encapsulated in one sweet trip.</p>
                    <div class="flex items-center justify-between pt-4 border-t border-gray-100">
                        <div>
                            <div class="text-[10px] text-gray-400 font-bold uppercase">Starting from</div>
                            <div class="font-display font-bold text-lg text-brand-dark">₹16,500</div>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-right -rotate-45"></i>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 4 -->
            <a href="#" class="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 group hover:shadow-xl transition-all duration-300 block">
                <div class="relative h-56 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1612438214708-f428a707dd4e?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
                    <div class="absolute top-4 left-4 bg-white/90 backdrop-blur-sm px-3 py-1 rounded-full text-[10px] font-bold text-gray-800 uppercase tracking-wide">7N / 8D</div>
                </div>
                <div class="p-5">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-brand-cyan text-xs font-bold uppercase tracking-widest"><i class="fa-solid fa-location-dot mr-1"></i> Meghalaya</span>
                        <div class="flex items-center gap-1 text-sm font-bold text-gray-700">
                            <i class="fa-solid fa-star text-brand-yellow text-[10px]"></i> 5.0
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-lg text-brand-dark leading-tight mb-2 group-hover:text-brand-cyan transition-colors">Chasing Waterfalls</h3>
                    <p class="text-xs text-gray-500 mb-4 line-clamp-2">Explore the root bridges, cleanest villages, and magical caves.</p>
                    <div class="flex items-center justify-between pt-4 border-t border-gray-100">
                        <div>
                            <div class="text-[10px] text-gray-400 font-bold uppercase">Starting from</div>
                            <div class="font-display font-bold text-lg text-brand-dark">₹21,000</div>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-right -rotate-45"></i>
                        </div>
                    </div>
                </div>
            </a>
        </div>"""

new_similar_cards = """<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Card 1 -->
            <a href="#" class="block h-full cursor-pointer focus:outline-none hover:-translate-y-1 transition-transform group">
                <div class="bg-white rounded-[2rem] p-3 shadow-soft group-hover:shadow-float transition-all duration-500 border border-gray-100 flex flex-col h-full">
                    <div class="relative w-full aspect-[4/3] rounded-3xl overflow-hidden mb-3">
                        <img src="https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Ladakh">
                        <!-- FOMO Tag -->
                        <div class="absolute top-3 left-3 bg-red-500 text-white px-3 py-1.5 rounded-full font-bold text-[10px] uppercase tracking-wider shadow-md animate-pulse">
                            🔥 Selling Fast
                        </div>
                    </div>
                    <div class="px-3 pb-2 flex flex-col flex-grow">
                        <div class="flex items-center gap-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-2.5">
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-calendar-check text-brand-cyan"></i> 15 May</span>
                            <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-clock text-brand-cyan"></i> 6N / 7D</span>
                        </div>
                        <h3 class="font-display font-semibold text-base text-brand-dark leading-snug mb-3 group-hover:text-brand-cyan transition-colors">
                            Leh & Pangong Highlights
                        </h3>
                        <div class="mt-auto pt-4 border-t border-gray-100 flex items-end justify-between">
                            <span class="flex items-center gap-1.5 text-sm font-medium text-gray-500 pb-1">
                                <i class="fa-solid fa-location-dot text-brand-yellow"></i> Leh Airport
                            </span>
                            <div class="text-right">
                                <span class="block text-[11px] text-gray-400 line-through leading-none mb-1">₹21,500</span>
                                <span class="text-brand-cyan font-bold text-base leading-none">₹18,500 <span class="text-[10px] font-medium text-gray-500 uppercase tracking-wide ml-0.5">Onwards</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 2 -->
            <a href="#" class="block h-full cursor-pointer focus:outline-none hover:-translate-y-1 transition-transform group">
                <div class="bg-white rounded-[2rem] p-3 shadow-soft group-hover:shadow-float transition-all duration-500 border border-gray-100 flex flex-col h-full">
                    <div class="relative w-full aspect-[4/3] rounded-3xl overflow-hidden mb-3">
                        <img src="https://images.unsplash.com/photo-1595815771614-ade9d652a65d?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Spiti">
                    </div>
                    <div class="px-3 pb-2 flex flex-col flex-grow">
                        <div class="flex items-center gap-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-2.5">
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-calendar-check text-brand-cyan"></i> 20 May</span>
                            <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-clock text-brand-cyan"></i> 8N / 9D</span>
                        </div>
                        <h3 class="font-display font-semibold text-base text-brand-dark leading-snug mb-3 group-hover:text-brand-cyan transition-colors">
                            Spiti Circuit Winter Expedition
                        </h3>
                        <div class="mt-auto pt-4 border-t border-gray-100 flex items-end justify-between">
                            <span class="flex items-center gap-1.5 text-sm font-medium text-gray-500 pb-1">
                                <i class="fa-solid fa-location-dot text-brand-yellow"></i> Chandigarh
                            </span>
                            <div class="text-right">
                                <span class="block text-[11px] text-gray-400 line-through leading-none mb-1">₹25,000</span>
                                <span class="text-brand-cyan font-bold text-base leading-none">₹22,000 <span class="text-[10px] font-medium text-gray-500 uppercase tracking-wide ml-0.5">Onwards</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 3 -->
            <a href="#" class="block h-full cursor-pointer focus:outline-none hover:-translate-y-1 transition-transform group">
                <div class="bg-white rounded-[2rem] p-3 shadow-soft group-hover:shadow-float transition-all duration-500 border border-gray-100 flex flex-col h-full">
                    <div class="relative w-full aspect-[4/3] rounded-3xl overflow-hidden mb-3">
                        <img src="https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Kashmir">
                    </div>
                    <div class="px-3 pb-2 flex flex-col flex-grow">
                        <div class="flex items-center gap-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-2.5">
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-calendar-check text-brand-cyan"></i> 02 Jun</span>
                            <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-clock text-brand-cyan"></i> 5N / 6D</span>
                        </div>
                        <h3 class="font-display font-semibold text-base text-brand-dark leading-snug mb-3 group-hover:text-brand-cyan transition-colors">
                            Paradise on Earth Tour
                        </h3>
                        <div class="mt-auto pt-4 border-t border-gray-100 flex items-end justify-between">
                            <span class="flex items-center gap-1.5 text-sm font-medium text-gray-500 pb-1">
                                <i class="fa-solid fa-location-dot text-brand-yellow"></i> Srinagar
                            </span>
                            <div class="text-right">
                                <span class="block text-[11px] text-gray-400 line-through leading-none mb-1">₹19,500</span>
                                <span class="text-brand-cyan font-bold text-base leading-none">₹16,500 <span class="text-[10px] font-medium text-gray-500 uppercase tracking-wide ml-0.5">Onwards</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
            
            <!-- Card 4 -->
            <a href="#" class="block h-full cursor-pointer focus:outline-none hover:-translate-y-1 transition-transform group">
                <div class="bg-white rounded-[2rem] p-3 shadow-soft group-hover:shadow-float transition-all duration-500 border border-gray-100 flex flex-col h-full">
                    <div class="relative w-full aspect-[4/3] rounded-3xl overflow-hidden mb-3">
                        <img src="https://images.unsplash.com/photo-1612438214708-f428a707dd4e?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" alt="Meghalaya">
                    </div>
                    <div class="px-3 pb-2 flex flex-col flex-grow">
                        <div class="flex items-center gap-3 text-[11px] font-bold text-gray-400 uppercase tracking-wider mb-2.5">
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-calendar-check text-brand-cyan"></i> 12 Jun</span>
                            <span class="w-1 h-1 rounded-full bg-gray-300"></span>
                            <span class="flex items-center gap-1.5"><i class="fa-regular fa-clock text-brand-cyan"></i> 7N / 8D</span>
                        </div>
                        <h3 class="font-display font-semibold text-base text-brand-dark leading-snug mb-3 group-hover:text-brand-cyan transition-colors">
                            Chasing Waterfalls
                        </h3>
                        <div class="mt-auto pt-4 border-t border-gray-100 flex items-end justify-between">
                            <span class="flex items-center gap-1.5 text-sm font-medium text-gray-500 pb-1">
                                <i class="fa-solid fa-location-dot text-brand-yellow"></i> Guwahati
                            </span>
                            <div class="text-right">
                                <span class="block text-[11px] text-gray-400 line-through leading-none mb-1">₹25,000</span>
                                <span class="text-brand-cyan font-bold text-base leading-none">₹21,000 <span class="text-[10px] font-medium text-gray-500 uppercase tracking-wide ml-0.5">Onwards</span></span>
                            </div>
                        </div>
                    </div>
                </div>
            </a>
        </div>"""
ladakh_html = ladakh_html.replace(old_similar_cards, new_similar_cards)

# 3. Change pp to per person
ladakh_html = ladakh_html.replace('<span class="text-sm text-gray-400 font-normal">/pp</span>', '<span class="text-sm text-gray-400 font-normal">/per person</span>')

# 4. Reduce page header font size by 10%
# Currently text-[29px] md:text-[38px]
old_header = '<h1 class="font-display font-extrabold text-[29px] md:text-[38px] text-brand-dark leading-tight mb-3 tracking-tight">'
new_header = '<h1 class="font-display font-extrabold text-[26px] md:text-[32px] text-brand-dark leading-tight mb-3 tracking-tight">'
ladakh_html = ladakh_html.replace(old_header, new_header)

# 5. Replace age group with solo travelers & 60%
old_age = """<div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Avg Age</div>
                        <div class="font-semibold text-gray-800 text-sm">22-28 Yrs</div>"""
new_age = """<div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Solo Travelers</div>
                        <div class="font-semibold text-gray-800 text-sm">60%</div>"""
ladakh_html = ladakh_html.replace(old_age, new_age)

# 6. Keep icons for pickup & drop
old_logistics = """<div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8">
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
new_logistics = """<div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8">
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
ladakh_html = ladakh_html.replace(old_logistics, new_logistics)

# 7. Add text with icons below the CTA in booking card
# Find the CTA
cta_html = """<button class="w-full bg-brand-cyan text-white py-[14px] rounded-full font-display font-bold text-base shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-phone-volume text-lg"></i> Get a Call Back
                </button>"""
value_props_html = """<button class="w-full bg-brand-cyan text-white py-[14px] rounded-full font-display font-bold text-base shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2 mb-6">
                    <i class="fa-solid fa-phone-volume text-lg"></i> Get a Call Back
                </button>
                
                <!-- Trust / Booking Value Props -->
                <div class="space-y-3 pt-2 border-t border-gray-100">
                    <div class="flex items-start gap-3">
                        <div class="mt-0.5 text-brand-cyan text-sm"><i class="fa-solid fa-wallet"></i></div>
                        <p class="text-xs text-gray-600 font-medium">Pay only 25% upfront, rest of it later.</p>
                    </div>
                    <div class="flex items-start gap-3">
                        <div class="mt-0.5 text-brand-cyan text-sm"><i class="fa-solid fa-pen-to-square"></i></div>
                        <p class="text-xs text-gray-600 font-medium">Easily modify/update your booking.</p>
                    </div>
                    <div class="flex items-start gap-3">
                        <div class="mt-0.5 text-brand-cyan text-sm"><i class="fa-solid fa-arrow-rotate-left"></i></div>
                        <p class="text-xs text-gray-600 font-medium">Cancel & get refund up to 16 days before.</p>
                    </div>
                </div>"""
ladakh_html = ladakh_html.replace(cta_html, value_props_html)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(ladakh_html)
print("Updated all ladakh.html edits.")
