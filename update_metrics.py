import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Quick Stats
stats_start = html.find('<!-- Quick Stats Bar -->')
highlights_start = html.find('<!-- The Vibe / Highlights -->')

new_stats = """<!-- Quick Stats Bar -->
            <div class="flex flex-wrap gap-4 md:gap-8 bg-white p-6 rounded-3xl shadow-sm border border-gray-100 mb-12">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-cyan-50 flex items-center justify-center text-brand-cyan">
                        <i class="fa-regular fa-clock"></i>
                    </div>
                    <div>
                        <div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Duration</div>
                        <div class="font-semibold text-gray-800 text-sm">6N / 7D</div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-orange-50 flex items-center justify-center text-orange-500">
                        <i class="fa-solid fa-fire"></i>
                    </div>
                    <div>
                        <div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Slots Filled</div>
                        <div class="flex items-center gap-2">
                            <div class="font-semibold text-gray-800 text-sm">85%</div>
                            <div class="w-16 h-1.5 bg-gray-200 rounded-full overflow-hidden"><div class="w-[85%] h-full bg-orange-500 rounded-full"></div></div>
                        </div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-purple-50 flex items-center justify-center text-purple-500">
                        <i class="fa-solid fa-venus-mars"></i>
                    </div>
                    <div>
                        <div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Gender Ratio</div>
                        <div class="font-semibold text-gray-800 text-sm">60:40 (M:F)</div>
                    </div>
                </div>
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-green-50 flex items-center justify-center text-green-500">
                        <i class="fa-solid fa-users-viewfinder"></i>
                    </div>
                    <div>
                        <div class="text-[10px] uppercase font-bold text-gray-400 tracking-wider">Avg Age</div>
                        <div class="font-semibold text-gray-800 text-sm">22-28 Yrs</div>
                    </div>
                </div>
            </div>

            """

if stats_start != -1 and highlights_start != -1:
    html = html[:stats_start] + new_stats + html[highlights_start:]

# 2. Update Inclusions & Exclusions
inc_start = html.find('<!-- Inclusions & Exclusions -->')
pack_start = html.find('<!-- Things to Pack (Interactive category tabs) -->')

new_inc = """<!-- Travel Styles & Inclusions -->
            <h2 class="font-display font-bold text-2xl text-brand-dark mb-6">Choose Your Travel Style</h2>
            <div x-data="{ style: 'rented' }" class="mb-16">
                <!-- Style Selector -->
                <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
                    <!-- SUV -->
                    <div @click="style = 'suv'" :class="style === 'suv' ? 'border-brand-cyan bg-cyan-50/30 shadow-md ring-1 ring-brand-cyan' : 'border-gray-200 bg-white hover:border-brand-cyan/50'" class="cursor-pointer border-2 rounded-[2rem] p-5 transition-all duration-300 relative overflow-hidden group">
                        <div x-show="style === 'suv'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider">Selected</div>
                        <div class="w-12 h-12 rounded-full bg-white border border-gray-100 shadow-sm flex items-center justify-center text-xl text-gray-400 mb-4 transition-colors group-hover:text-brand-cyan" :class="style === 'suv' ? '!text-brand-cyan' : ''"><i class="fa-solid fa-van-shuttle"></i></div>
                        <h4 class="font-display font-bold text-lg text-gray-800 mb-1">SUV / Tempo</h4>
                        <p class="text-xs text-gray-500 leading-relaxed font-medium">Relax and let our expert drivers navigate the rugged terrain.</p>
                    </div>
                    <!-- Rented Bike -->
                    <div @click="style = 'rented'" :class="style === 'rented' ? 'border-brand-cyan bg-cyan-50/30 shadow-md ring-1 ring-brand-cyan' : 'border-gray-200 bg-white hover:border-brand-cyan/50'" class="cursor-pointer border-2 rounded-[2rem] p-5 transition-all duration-300 relative overflow-hidden group">
                        <div x-show="style === 'rented'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider" style="display: none;">Selected</div>
                        <div class="w-12 h-12 rounded-full bg-white border border-gray-100 shadow-sm flex items-center justify-center text-xl text-gray-400 mb-4 transition-colors group-hover:text-brand-cyan" :class="style === 'rented' ? '!text-brand-cyan' : ''"><i class="fa-solid fa-motorcycle"></i></div>
                        <h4 class="font-display font-bold text-lg text-gray-800 mb-1">Rented Bike</h4>
                        <p class="text-xs text-gray-500 leading-relaxed font-medium">Solo or dual riding on fully serviced Royal Enfield Himalayans.</p>
                    </div>
                    <!-- Own Bike -->
                    <div @click="style = 'own'" :class="style === 'own' ? 'border-brand-cyan bg-cyan-50/30 shadow-md ring-1 ring-brand-cyan' : 'border-gray-200 bg-white hover:border-brand-cyan/50'" class="cursor-pointer border-2 rounded-[2rem] p-5 transition-all duration-300 relative overflow-hidden group">
                        <div x-show="style === 'own'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider" style="display: none;">Selected</div>
                        <div class="w-12 h-12 rounded-full bg-white border border-gray-100 shadow-sm flex items-center justify-center text-xl text-gray-400 mb-4 transition-colors group-hover:text-brand-cyan" :class="style === 'own' ? '!text-brand-cyan' : ''"><i class="fa-solid fa-key"></i></div>
                        <h4 class="font-display font-bold text-lg text-gray-800 mb-1">Own Bike</h4>
                        <p class="text-xs text-gray-500 leading-relaxed font-medium">Bring your own machine. We provide the backup and itinerary.</p>
                    </div>
                </div>
                
                <!-- Dynamic Content Area -->
                <div class="bg-white border border-gray-200 shadow-sm rounded-[2rem] p-6 md:p-8 relative overflow-hidden">
                    <div class="absolute -right-16 -top-16 text-gray-50 opacity-[0.4] text-[200px] pointer-events-none transition-all duration-500" :class="style === 'suv' ? 'block' : 'hidden'"><i class="fa-solid fa-van-shuttle"></i></div>
                    <div class="absolute -right-16 -top-16 text-gray-50 opacity-[0.4] text-[200px] pointer-events-none transition-all duration-500" :class="style === 'rented' ? 'block' : 'hidden'"><i class="fa-solid fa-motorcycle"></i></div>
                    <div class="absolute -right-16 -top-16 text-gray-50 opacity-[0.4] text-[200px] pointer-events-none transition-all duration-500" :class="style === 'own' ? 'block' : 'hidden'"><i class="fa-solid fa-key"></i></div>
                    
                    <div class="flex flex-col sm:flex-row sm:items-center gap-4 mb-8 pb-5 border-b border-gray-100 relative z-10">
                        <div class="w-12 h-12 rounded-2xl bg-brand-cyan/10 flex items-center justify-center text-brand-cyan shrink-0">
                            <i class="fa-solid fa-list-check text-xl"></i>
                        </div>
                        <div>
                            <h3 class="font-display font-bold text-xl text-brand-dark" x-text="style === 'suv' ? 'SUV / Tempo Inclusions' : (style === 'rented' ? 'Rented Bike Package Specifics' : 'Own Bike Package Specifics')"></h3>
                            <p class="text-sm text-gray-500 font-medium mt-1">Here is exactly what changes based on your selected travel style.</p>
                        </div>
                    </div>

                    <!-- Features Grid -->
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-10 relative z-10">
                        
                        <!-- Shared Inclusions (Left Column) -->
                        <div>
                            <h4 class="text-[11px] font-bold uppercase tracking-widest text-gray-400 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500"></div> Standard Across All</h4>
                            <ul class="space-y-5">
                                <li class="flex items-start gap-4">
                                    <div class="w-8 h-8 rounded-full bg-green-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-house-chimney text-green-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">All Accommodations</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed">Hotels in Leh, Camps in Nubra & Pangong, Homestay in Hanle.</div>
                                    </div>
                                </li>
                                <li class="flex items-start gap-4">
                                    <div class="w-8 h-8 rounded-full bg-green-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-utensils text-green-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">Meals</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed">Breakfast & Dinner on all days at your respective stay.</div>
                                    </div>
                                </li>
                                <li class="flex items-start gap-4">
                                    <div class="w-8 h-8 rounded-full bg-green-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-file-signature text-green-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">Permits & Fees</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed">Inner Line Permits & Environmental Fees included.</div>
                                    </div>
                                </li>
                            </ul>
                        </div>

                        <!-- Style-Specific Rules & Exclusions (Right Column) -->
                        <div>
                            <h4 class="text-[11px] font-bold uppercase tracking-widest text-gray-400 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-brand-cyan"></div> Style Specifics</h4>
                            <ul class="space-y-5">
                                
                                <!-- Transit -->
                                <li class="flex items-start gap-4">
                                    <div class="w-8 h-8 rounded-full bg-blue-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-route text-blue-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">Transit & Route</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'suv'">Travel comfortably in an SUV or Tempo Traveller for the entire circuit.</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'rented'" style="display: none;">Bike provided from Leh to Leh. Standard fuel included.</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'own'" style="display: none;">You must transport/ride your bike to Leh. Fuel is <span class="text-red-500 font-bold">excluded</span>.</div>
                                    </div>
                                </li>

                                <!-- Security Deposit -->
                                <li class="flex items-start gap-4">
                                    <div class="w-8 h-8 rounded-full bg-orange-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-shield-halved text-orange-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">Security & Damage</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'suv'">No security deposit or damage liability needed.</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'rented'" style="display: none;"><span class="font-bold text-gray-700">₹5,000</span> refundable deposit required. Client pays for physical damage.</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'own'" style="display: none;">No deposit, but all maintenance & damage fall on your own pocket.</div>
                                    </div>
                                </li>

                                <!-- Gear -->
                                <li class="flex items-start gap-4" x-show="style === 'rented' || style === 'own'" style="display: none;">
                                    <div class="w-8 h-8 rounded-full bg-purple-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-helmet-safety text-purple-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">Gear & Mechanics</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'rented'">Riding gear (helmet, knee pads, gloves) included. Dedicated mechanic with spares.</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed" x-show="style === 'own'">Bring your own gear. Covered under group mechanical assistance (standard tools).</div>
                                    </div>
                                </li>
                                
                                <!-- General Exclusions -->
                                <li class="flex items-start gap-4" x-show="style === 'suv'">
                                    <div class="w-8 h-8 rounded-full bg-red-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-xmark text-red-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">General Exclusions</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed">Flights to Leh, Lunches, Personal Expenses, Medical Evacuation.</div>
                                    </div>
                                </li>

                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            """

if inc_start != -1 and pack_start != -1:
    html = html[:inc_start] + new_inc + html[pack_start:]

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated quick stats and interactive inclusions.")
