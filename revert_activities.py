import re
with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Build original India activities HTML
india_html = """<div id="content-activities" class="mb-8 hidden transition-opacity duration-300">
                <div class="flex gap-4 overflow-x-auto hide-scrollbar pb-4 snap-x snap-mandatory -mx-4 px-4 lg:mx-0 lg:px-0">
                    
                    <div class="flex-shrink-0 snap-start bg-white/90 backdrop-blur rounded-2xl p-4 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-brand-cyan hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-14 h-14 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1479888230021-c24f136d849f?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Winter Expeditions"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-brand-cyan transition-colors">Winter Expeditions</h4>
                            <p class="text-xs text-gray-500 font-medium">8 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/90 backdrop-blur rounded-2xl p-4 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-brand-yellow hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-14 h-14 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1558981806-ec527fa84c39?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Bike Trips"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-brand-yellow transition-colors">Bike Trips</h4>
                            <p class="text-xs text-gray-500 font-medium">12 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/90 backdrop-blur rounded-2xl p-4 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-green-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-14 h-14 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1522163182402-834f871fd851?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Trekking"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-green-500 transition-colors">Trekking</h4>
                            <p class="text-xs text-gray-500 font-medium">20 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/90 backdrop-blur rounded-2xl p-4 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-pink-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-14 h-14 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Leisure"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-pink-500 transition-colors">Leisure</h4>
                            <p class="text-xs text-gray-500 font-medium">15 Trips</p>
                        </div>
                    </div>

                    <div class="flex-shrink-0 snap-start bg-white/90 backdrop-blur rounded-2xl p-4 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-purple-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-14 h-14 rounded-xl overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Backpacking"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-purple-500 transition-colors">Backpacking</h4>
                            <p class="text-xs text-gray-500 font-medium">35 Trips</p>
                        </div>
                    </div>
                </div>
            </div>"""

# Build original Intl activities HTML
intl_html = """<div id="content-intl-activities" class="mb-8 hidden transition-opacity duration-300">
                <div class="flex gap-4 overflow-x-auto hide-scrollbar pb-4 snap-x snap-mandatory -mx-4 px-4 lg:mx-0 lg:px-0">
                    
                    <div class="flex-shrink-0 snap-start bg-white/70 backdrop-blur-md rounded-full p-2.5 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-brand-cyan hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-16 h-16 rounded-full overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Island Hopping"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-brand-cyan transition-colors">Island Hopping</h4>
                            <p class="text-xs text-gray-500 font-medium">18 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/70 backdrop-blur-md rounded-full p-2.5 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-blue-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-16 h-16 rounded-full overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Scuba Diving"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-blue-500 transition-colors">Scuba Diving</h4>
                            <p class="text-xs text-gray-500 font-medium">10 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/70 backdrop-blur-md rounded-full p-2.5 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-indigo-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-16 h-16 rounded-full overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1579033461380-adb47c3eb938?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Northern Lights"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-indigo-500 transition-colors">Northern Lights</h4>
                            <p class="text-xs text-gray-500 font-medium">5 Trips</p>
                        </div>
                    </div>
                    
                    <div class="flex-shrink-0 snap-start bg-white/70 backdrop-blur-md rounded-full p-2.5 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-orange-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-16 h-16 rounded-full overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1516426122078-c23e76319801?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Safari"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-orange-500 transition-colors">Safari</h4>
                            <p class="text-xs text-gray-500 font-medium">8 Trips</p>
                        </div>
                    </div>

                    <div class="flex-shrink-0 snap-start bg-white/70 backdrop-blur-md rounded-full p-2.5 pr-8 shadow-sm border border-gray-100 flex items-center gap-4 cursor-pointer hover:border-purple-500 hover:shadow-md transition-all group min-w-[240px]">
                        <div class="w-16 h-16 rounded-full overflow-hidden flex-shrink-0"><img src="https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?q=80&w=200&auto=format&fit=crop" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Backpacking"></div>
                        <div>
                            <h4 class="font-bold text-brand-dark text-lg group-hover:text-purple-500 transition-colors">Backpacking</h4>
                            <p class="text-xs text-gray-500 font-medium">40 Trips</p>
                        </div>
                    </div>
                </div>
            </div>"""

# Replace the current India activities block with the original one
html = re.sub(r'<div id="content-activities".*?(?=<!-- 3\. FEATURED PACKAGES -->)', india_html + '\n\n            ', html, flags=re.DOTALL)
# Replace the current Intl activities block with the original one
html = re.sub(r'<div id="content-intl-activities".*?(?=<!-- 3\. FEATURED PACKAGES -->)', intl_html + '\n\n            ', html, flags=re.DOTALL)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Successfully reverted activities to original horizontal pills.")
