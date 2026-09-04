import sys

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the Full Route section
old_route = """<div class="flex-[2]">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Full Route</div>
                    <p class="text-sm text-gray-700 leading-relaxed font-semibold">
                        Delhi <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Manali <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Sarchu <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Tso Moriri <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Hanle <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Umling La <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Pangong <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Nubra Valley <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Leh <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Kargil <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Srinagar
                    </p>
                </div>"""

new_route = """<div class="flex-[2] flex flex-col">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Full Route</div>
                    
                    <div class="flex flex-col justify-between flex-grow text-sm font-semibold text-gray-700">
                        
                        <!-- Row 1 -->
                        <div class="flex items-center justify-between">
                            <span class="hover:text-brand-cyan transition-colors">Delhi</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Manali</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Sarchu</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Tso Moriri</span>
                        </div>
                        
                        <!-- Connecting Turn Right -->
                        <div class="flex justify-end pr-[40px] md:pr-[50px] -my-1">
                            <div class="h-6 border-r-2 border-dashed border-brand-cyan/40"></div>
                        </div>

                        <!-- Row 2 (Right to Left visual flow) -->
                        <div class="flex items-center justify-between">
                            <span class="hover:text-brand-cyan transition-colors">Pangong</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors whitespace-nowrap">Umling La</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Hanle</span>
                        </div>

                        <!-- Connecting Turn Left -->
                        <div class="flex justify-start pl-[30px] md:pl-[40px] -my-1">
                            <div class="h-6 border-l-2 border-dashed border-brand-cyan/40"></div>
                        </div>

                        <!-- Row 3 -->
                        <div class="flex items-center justify-between">
                            <span class="hover:text-brand-cyan transition-colors">Nubra</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Leh</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Kargil</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/40 mx-2 md:mx-4"></div>
                            <span class="hover:text-brand-cyan transition-colors">Srinagar</span>
                        </div>
                        
                    </div>
                </div>"""
                
if old_route in html:
    html = html.replace(old_route, new_route)
    print("Successfully replaced Full Route.")
else:
    print("Could not find the old full route HTML. Please check the exact string.")
    
with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
