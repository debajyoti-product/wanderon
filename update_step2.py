import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# Grab a single card template from index.html
start_marker = '<a href="ladakh.html"'
card_start = index_html.find(start_marker)
if card_start == -1: card_start = index_html.find('<div class="bg-white rounded-3xl overflow-hidden')
card_end = index_html.find('</a>', card_start) + 4
if index_html[card_end-4:card_end] != '</a>': 
    card_end = index_html.find('</div>', card_start) # fallback

card_template = index_html[card_start:card_end] if card_start != -1 else ""

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    ladakh_html = f.read()

# Find the end of the Reviews section (or Trust Corner)
reviews_end = ladakh_html.find('<!-- Right Column: Sticky Booking Widget -->')

# Generate Similar Trips section
similar_trips = f"""
        <!-- Similar Trips Section (Spans Full Width Below Content) -->
    </main>

    <section class="max-w-7xl mx-auto px-4 lg:px-8 pb-20">
        <div class="flex items-end justify-between mb-8">
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
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Card 1 -->
            <a href="#" class="bg-white rounded-3xl overflow-hidden shadow-sm border border-gray-100 group hover:shadow-xl transition-all duration-300 block">
                <div class="relative h-56 overflow-hidden">
                    <img src="https://images.unsplash.com/photo-1596773256086-63044a30e797?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
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
                    <img src="https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700">
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
        </div>
        
        <!-- Mobile Pills (shown below grid on small screens) -->
        <div class="flex md:hidden gap-3 mt-6 overflow-x-auto pb-2 snap-x">
            <button class="shrink-0 px-5 py-2 rounded-full bg-brand-cyan text-white text-sm font-bold shadow-md shadow-cyan-500/20 snap-start">Super Saver</button>
            <button class="shrink-0 px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold snap-start">Best Sellers</button>
            <button class="shrink-0 px-5 py-2 rounded-full bg-white border border-gray-200 text-gray-600 text-sm font-bold snap-start">Exclusive</button>
        </div>
    </section>

    <!-- Original Footer (assuming it follows main) -->
"""

# Replace the closing </main> tag with the new section
if '</main>' in ladakh_html:
    ladakh_html = ladakh_html.replace('</main>', similar_trips)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(ladakh_html)
print("Part 2: Similar trips added.")
