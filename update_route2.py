import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

old_block = """<!-- Route & Logistics -->
            <div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8">
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
                </div>
                <div class="w-px bg-gray-200 hidden md:block"></div>
                <div class="flex-[2]">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Full Route</div>
                    <!-- Typographic Reverse S-Curve -->
                    <div class="flex flex-col text-[11px] lg:text-[13px] font-bold text-gray-700 w-full mt-1">
                        
                        <!-- Row 1 (Left to Right) -->
                        <div class="flex items-center justify-between">
                            <span class="text-brand-dark">Delhi</span>
                            <i class="fa-solid fa-arrow-right-long text-brand-cyan"></i>
                            <span class="text-brand-dark">Manali</span>
                            <i class="fa-solid fa-arrow-right-long text-brand-cyan"></i>
                            <span class="text-brand-dark">Sarchu</span>
                            <i class="fa-solid fa-arrow-right-long text-brand-cyan"></i>
                            <span class="text-brand-dark">Tso Moriri</span>
                        </div>
                        
                        <!-- Right U-Turn Connector -->
                        <div class="flex justify-end pr-6 -my-1 relative z-0">
                            <svg class="w-6 h-7 text-brand-cyan/40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                <path d="M2 4h12a4 4 0 0 1 4 4v10m0 0l-4-4m4 4l4-4" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        
                        <!-- Row 2 (Right to Left visually) -->
                        <div class="flex items-center justify-between bg-white border border-gray-100 shadow-sm px-3 py-2.5 rounded-2xl -mx-3 relative z-10">
                            <span class="text-brand-dark whitespace-nowrap">Nubra Valley</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-1.5"></i>
                            <span class="text-brand-dark">Pangong</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-1.5"></i>
                            <span class="text-brand-dark">Umling La</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-1.5"></i>
                            <span class="text-brand-dark">Hanle</span>
                        </div>
                        
                        <!-- Left U-Turn Connector -->
                        <div class="flex justify-start pl-6 -my-1 relative z-0">
                            <svg class="w-6 h-7 text-brand-yellow/40" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                                <path d="M22 4H10a4 4 0 0 0-4 4v10m0 0l4-4m-4 4l-4-4" stroke-linecap="round" stroke-linejoin="round"/>
                            </svg>
                        </div>
                        
                        <!-- Row 3 (Left to Right) -->
                        <div class="flex items-center justify-between w-[80%]">
                            <span class="text-brand-dark">Leh</span>
                            <i class="fa-solid fa-arrow-right-long text-brand-cyan"></i>
                            <span class="text-brand-dark">Kargil</span>
                            <i class="fa-solid fa-arrow-right-long text-brand-cyan"></i>
                            <span class="text-brand-dark">Srinagar</span>
                        </div>
                    </div>
                </div>
            </div>"""
            
new_block = """<!-- Route & Logistics -->
            <div class="bg-gray-50 border border-gray-100 rounded-3xl p-6 md:p-8 mb-12 flex flex-col md:flex-row gap-8 items-stretch">
                <div class="flex-[0.8] flex flex-col">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Logistics</div>
                    <div class="flex flex-col justify-between flex-grow pb-1">
                        <div class="flex items-center gap-3 font-semibold text-gray-800 text-sm">
                            <div class="w-6 h-6 rounded-full bg-brand-cyan/20 flex items-center justify-center text-brand-cyan text-xs"><i class="fa-solid fa-plane-arrival"></i></div>
                            <div><span class="text-gray-400 text-xs font-normal block">Pickup</span> Delhi</div>
                        </div>
                        <div class="w-px h-6 bg-gray-200 ml-3"></div>
                        <div class="flex items-center gap-3 font-semibold text-gray-800 text-sm">
                            <div class="w-6 h-6 rounded-full bg-brand-yellow/20 flex items-center justify-center text-brand-yellow text-xs"><i class="fa-solid fa-plane-departure"></i></div>
                            <div><span class="text-gray-400 text-xs font-normal block">Drop</span> Srinagar</div>
                        </div>
                    </div>
                </div>
                <div class="w-px bg-gray-200 hidden md:block"></div>
                <div class="flex-[2] flex flex-col">
                    <div class="text-[10px] font-bold text-gray-400 uppercase tracking-widest mb-3">Full Route</div>
                    <!-- Typographic Reverse S-Curve -->
                    <div class="flex flex-col justify-between flex-grow text-[11px] lg:text-[13px] font-bold text-gray-700 w-full mt-1">
                        
                        <!-- Row 1 (Left to Right) -->
                        <div class="flex items-center justify-between">
                            <span class="text-brand-dark">Delhi</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/30 mx-2 lg:mx-4"></div>
                            <span class="text-brand-dark">Manali</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/30 mx-2 lg:mx-4"></div>
                            <span class="text-brand-dark">Sarchu</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/30 mx-2 lg:mx-4"></div>
                            <span class="text-brand-dark">Tso Moriri</span>
                        </div>
                        
                        <!-- Right U-Turn Connector -->
                        <div class="flex justify-end pr-[30px] lg:pr-[40px] -my-1">
                            <div class="h-4 border-r-2 border-dashed border-brand-cyan/30"></div>
                        </div>
                        
                        <!-- Row 2 (Right to Left visually) -->
                        <div class="flex items-center justify-between bg-white border border-gray-100 shadow-sm px-4 py-2.5 rounded-2xl -mx-4 relative z-10">
                            <span class="text-brand-dark whitespace-nowrap">Nubra Valley</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-2 lg:mx-4"></i>
                            <span class="text-brand-dark">Pangong</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-2 lg:mx-4"></i>
                            <span class="text-brand-dark whitespace-nowrap">Umling La</span>
                            <i class="fa-solid fa-arrow-left-long text-brand-yellow shrink-0 mx-2 lg:mx-4"></i>
                            <span class="text-brand-dark">Hanle</span>
                        </div>
                        
                        <!-- Left U-Turn Connector -->
                        <div class="flex justify-start pl-[20px] lg:pl-[30px] -my-1">
                            <div class="h-4 border-l-2 border-dashed border-brand-yellow/50"></div>
                        </div>
                        
                        <!-- Row 3 (Left to Right) -->
                        <div class="flex items-center justify-between w-full">
                            <span class="text-brand-dark">Leh</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/30 mx-2 lg:mx-4"></div>
                            <span class="text-brand-dark">Kargil</span>
                            <div class="flex-1 border-t-2 border-dashed border-brand-cyan/30 mx-2 lg:mx-4"></div>
                            <span class="text-brand-dark">Srinagar</span>
                            <div class="flex-[0.5] lg:flex-1"></div>
                        </div>
                    </div>
                </div>
            </div>"""

if old_block in html:
    html = html.replace(old_block, new_block)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated Layout.")
else:
    print("Could not find the exact old block.")
