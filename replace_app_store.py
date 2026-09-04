import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Build the new section HTML
new_section = """
    <!-- Dual Vibe Sections: Events & Romantic -->
    <section class="py-16 lg:py-24 relative overflow-hidden bg-white">
        <div class="max-w-[1400px] mx-auto px-4 lg:px-8">
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12">
                
                <!-- LEFT: Hyped Events & Festivals -->
                <div class="bg-gray-900 rounded-[2.5rem] p-8 lg:p-12 relative overflow-hidden group/container shadow-2xl">
                    <!-- Dynamic background glow -->
                    <div class="absolute top-0 right-0 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3 group-hover/container:bg-pink-600/30 transition-colors duration-1000"></div>
                    
                    <div class="relative z-10 mb-10 flex flex-col items-start">
                        <div class="inline-flex items-center gap-2 font-bold uppercase text-xs tracking-widest text-purple-400 mb-3 bg-white/5 backdrop-blur-md px-4 py-2 rounded-full border border-white/10">
                            <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                            High Energy
                        </div>
                        <h2 class="font-display font-bold text-4xl lg:text-5xl text-white tracking-tight mb-4">
                            Most Hyped Events <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500">&amp; Festivals</span>
                        </h2>
                        <p class="text-gray-400 max-w-sm">From jungle techno to massive mainstages, experience the world's most electrifying parties.</p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 relative z-10">
                        
                        <!-- Event 1: Tomorrowland -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer">
                            <img src="https://images.unsplash.com/photo-1470229722913-7c092bb5ace1?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Tomorrowland">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent group-hover:from-purple-900/90 transition-colors duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-purple-500/20 backdrop-blur border border-purple-500/50 rounded-full text-[10px] font-bold uppercase tracking-wider text-purple-200 mb-2">EDM Mainstage</div>
                                <h4 class="font-bold text-2xl mb-1">Tomorrowland</h4>
                                <p class="text-xs text-gray-300 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Boom, Belgium
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-purple-300 text-lg">₹1,45,000 <span class="text-[10px] text-gray-400 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center group-hover:bg-purple-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Event 2: Zamna -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer">
                            <img src="https://images.unsplash.com/photo-1514525253161-7a46d19cd819?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Zamna Fest">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent group-hover:from-pink-900/90 transition-colors duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-pink-500/20 backdrop-blur border border-pink-500/50 rounded-full text-[10px] font-bold uppercase tracking-wider text-pink-200 mb-2">Jungle Techno</div>
                                <h4 class="font-bold text-2xl mb-1">Zamna Fest</h4>
                                <p class="text-xs text-gray-300 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Tulum, Mexico
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-pink-300 text-lg">₹1,85,000 <span class="text-[10px] text-gray-400 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center group-hover:bg-pink-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Event 3: Full Moon -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer">
                            <img src="https://images.unsplash.com/photo-1533174000255-a63b8a1183f1?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="Full Moon Party">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent group-hover:from-blue-900/90 transition-colors duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-blue-500/20 backdrop-blur border border-blue-500/50 rounded-full text-[10px] font-bold uppercase tracking-wider text-blue-200 mb-2">Neon Beach Party</div>
                                <h4 class="font-bold text-2xl mb-1">Full Moon</h4>
                                <p class="text-xs text-gray-300 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Koh Phangan
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-blue-300 text-lg">₹45,000 <span class="text-[10px] text-gray-400 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center group-hover:bg-blue-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Event 4: F1 -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer">
                            <img src="https://images.unsplash.com/photo-1511367461989-f85a21fda167?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="F1 Grand Prix">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/40 to-transparent group-hover:from-red-900/90 transition-colors duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-red-500/20 backdrop-blur border border-red-500/50 rounded-full text-[10px] font-bold uppercase tracking-wider text-red-200 mb-2">Night Race</div>
                                <h4 class="font-bold text-2xl mb-1">F1 Grand Prix</h4>
                                <p class="text-xs text-gray-300 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Singapore
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-red-300 text-lg">₹1,10,000 <span class="text-[10px] text-gray-400 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center group-hover:bg-red-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

                <!-- RIGHT: Romantic Getaways -->
                <div class="bg-rose-50/50 border border-rose-100 rounded-[2.5rem] p-8 lg:p-12 relative overflow-hidden group/container shadow-soft">
                    <!-- Soft warm gradient -->
                    <div class="absolute top-0 right-0 w-96 h-96 bg-rose-200/40 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3 group-hover/container:bg-orange-200/40 transition-colors duration-1000"></div>
                    
                    <div class="relative z-10 mb-10 flex flex-col items-start">
                        <div class="inline-flex items-center gap-2 font-bold uppercase text-xs tracking-widest text-rose-500 mb-3 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full border border-rose-100 shadow-sm">
                            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
                            Serene Escapes
                        </div>
                        <h2 class="font-display font-semibold text-4xl lg:text-5xl text-gray-800 tracking-tight mb-4">
                            Romantic <span class="italic font-light text-rose-500">Getaways</span>
                        </h2>
                        <p class="text-gray-500 max-w-sm">Beautiful, serene destinations designed for couples to relax, connect, and create memories.</p>
                    </div>

                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-5 relative z-10">
                        
                        <!-- Getaway 1: Santorini -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer shadow-sm hover:shadow-xl transition-all duration-500">
                            <img src="https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Santorini">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:opacity-90 transition-opacity duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-white/20 backdrop-blur border border-white/30 rounded-full text-[10px] font-bold uppercase tracking-wider text-white mb-2">Cliffside Romance</div>
                                <h4 class="font-bold text-2xl mb-1 drop-shadow-sm">Santorini</h4>
                                <p class="text-xs text-gray-200 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-rose-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Greece
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-rose-300 text-lg drop-shadow-sm">₹1,20,000 <span class="text-[10px] text-gray-300 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/20 backdrop-blur flex items-center justify-center group-hover:bg-rose-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Getaway 2: Maldives -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer shadow-sm hover:shadow-xl transition-all duration-500">
                            <img src="https://images.unsplash.com/photo-1512100356356-de1b84283e18?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Maldives">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:opacity-90 transition-opacity duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-white/20 backdrop-blur border border-white/30 rounded-full text-[10px] font-bold uppercase tracking-wider text-white mb-2">Overwater Villas</div>
                                <h4 class="font-bold text-2xl mb-1 drop-shadow-sm">Maldives</h4>
                                <p class="text-xs text-gray-200 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-rose-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Indian Ocean
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-rose-300 text-lg drop-shadow-sm">₹85,000 <span class="text-[10px] text-gray-300 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/20 backdrop-blur flex items-center justify-center group-hover:bg-rose-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Getaway 3: Amalfi -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer shadow-sm hover:shadow-xl transition-all duration-500">
                            <img src="https://images.unsplash.com/photo-1610017173740-4286f9f9b5c8?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Amalfi Coast">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:opacity-90 transition-opacity duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-white/20 backdrop-blur border border-white/30 rounded-full text-[10px] font-bold uppercase tracking-wider text-white mb-2">Coastal Charm</div>
                                <h4 class="font-bold text-2xl mb-1 drop-shadow-sm">Amalfi Coast</h4>
                                <p class="text-xs text-gray-200 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-rose-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Italy
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-rose-300 text-lg drop-shadow-sm">₹1,40,000 <span class="text-[10px] text-gray-300 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/20 backdrop-blur flex items-center justify-center group-hover:bg-rose-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Getaway 4: Bali -->
                        <div class="group relative overflow-hidden rounded-3xl aspect-[4/5] cursor-pointer shadow-sm hover:shadow-xl transition-all duration-500">
                            <img src="https://images.unsplash.com/photo-1537996194471-e657df975ab4?q=80&w=600&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Bali">
                            <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent group-hover:opacity-90 transition-opacity duration-500"></div>
                            <div class="absolute bottom-0 left-0 w-full p-5 text-white">
                                <div class="inline-block px-3 py-1 bg-white/20 backdrop-blur border border-white/30 rounded-full text-[10px] font-bold uppercase tracking-wider text-white mb-2">Tropical Paradise</div>
                                <h4 class="font-bold text-2xl mb-1 drop-shadow-sm">Bali</h4>
                                <p class="text-xs text-gray-200 flex items-center gap-1 mb-3">
                                    <svg class="w-3 h-3 text-rose-300" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path></svg>
                                    Indonesia
                                </p>
                                <div class="flex items-center justify-between">
                                    <div class="font-bold text-rose-300 text-lg drop-shadow-sm">₹55,000 <span class="text-[10px] text-gray-300 font-normal uppercase tracking-wide">onwards</span></div>
                                    <div class="w-8 h-8 rounded-full bg-white/20 backdrop-blur flex items-center justify-center group-hover:bg-rose-500 transition-colors">
                                        <svg class="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </section>
"""

# Replace the app store section with the new section
app_match = re.search(r'<section class="py-16 bg-brand-cream">.*?</section>', html, re.DOTALL)
if app_match:
    html = html[:app_match.start()] + new_section + html[app_match.end():]
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully replaced App Store section.")
else:
    print("Could not find App Store section.")
