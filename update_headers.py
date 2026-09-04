import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inject Styles
style_block = """
    <!-- Dual Vibe Sections: Events & Romantic -->
    <style>
        @keyframes floatIcon {
            0% { transform: translateY(0) scale(0.8); opacity: 0; }
            20% { opacity: 0.8; }
            80% { opacity: 0.8; }
            100% { transform: translateY(-120px) scale(1.2); opacity: 0; }
        }
        .anim-float-1 { animation: floatIcon 6s infinite ease-in-out; }
        .anim-float-2 { animation: floatIcon 8s infinite ease-in-out 2s; }
        .anim-float-3 { animation: floatIcon 7s infinite ease-in-out 4s; }
        .anim-float-4 { animation: floatIcon 9s infinite ease-in-out 1s; }
    </style>"""
html = html.replace('<!-- Dual Vibe Sections: Events & Romantic -->', style_block)

# 2. Events Header & Animations
events_old_header = """<div class="relative z-10 mb-10 flex flex-col items-start">
                        <div class="inline-flex items-center gap-2 font-bold uppercase text-xs tracking-widest text-purple-400 mb-3 bg-white/5 backdrop-blur-md px-4 py-2 rounded-full border border-white/10">
                            <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
                            High Energy
                        </div>
                        <h2 class="font-display font-bold text-4xl lg:text-5xl text-white tracking-tight mb-4">
                            Most Hyped Events <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500">&amp; Festivals</span>
                        </h2>
                        <p class="text-gray-400 max-w-sm">From jungle techno to massive mainstages, experience the world's most electrifying parties.</p>
                    </div>"""

events_new_header = """<!-- Floating Animations -->
                    <div class="absolute top-0 left-0 w-full h-64 overflow-hidden pointer-events-none z-0">
                        <div class="absolute left-[15%] top-[60%] text-3xl text-purple-400/30 anim-float-1">🎵</div>
                        <div class="absolute left-[75%] top-[70%] text-4xl text-pink-500/20 anim-float-2">🎶</div>
                        <div class="absolute left-[40%] top-[50%] text-2xl text-purple-300/40 anim-float-3">🙌</div>
                        <div class="absolute left-[85%] top-[40%] text-3xl text-pink-400/30 anim-float-4">✨</div>
                    </div>
                    
                    <div class="relative z-10 mb-10 flex justify-between items-end w-full">
                        <div>
                            <h2 class="font-display font-bold text-[36px] lg:text-[43px] text-white tracking-tight mb-2">
                                Events &amp; Festivals
                            </h2>
                            <p class="text-gray-400 max-w-sm">From jungle techno to massive mainstages, experience the world's most electrifying parties.</p>
                        </div>
                        <a href="#" class="text-purple-400 hover:text-purple-300 font-bold text-sm whitespace-nowrap mb-1">View All &rarr;</a>
                    </div>"""

html = html.replace(events_old_header, events_new_header)

# 3. Romantic Header & Animations
romantic_old_header = """<div class="relative z-10 mb-10 flex flex-col items-start">
                        <div class="inline-flex items-center gap-2 font-bold uppercase text-xs tracking-widest text-rose-500 mb-3 bg-white/80 backdrop-blur-md px-4 py-2 rounded-full border border-rose-100 shadow-sm">
                            <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
                            Serene Escapes
                        </div>
                        <h2 class="font-display font-semibold text-4xl lg:text-5xl text-gray-800 tracking-tight mb-4">
                            Romantic <span class="italic font-light text-rose-500">Getaways</span>
                        </h2>
                        <p class="text-gray-500 max-w-sm">Beautiful, serene destinations designed for couples to relax, connect, and create memories.</p>
                    </div>"""

romantic_new_header = """<!-- Floating Animations -->
                    <div class="absolute top-0 left-0 w-full h-64 overflow-hidden pointer-events-none z-0">
                        <div class="absolute left-[15%] top-[60%] text-2xl text-rose-400/40 anim-float-1">🤍</div>
                        <div class="absolute left-[75%] top-[70%] text-4xl text-red-400/20 anim-float-2">👩‍❤️‍👨</div>
                        <div class="absolute left-[40%] top-[50%] text-2xl text-rose-300/50 anim-float-3">✨</div>
                        <div class="absolute left-[85%] top-[40%] text-3xl text-pink-400/30 anim-float-4">💕</div>
                    </div>
                    
                    <div class="relative z-10 mb-10 flex justify-between items-end w-full">
                        <div>
                            <h2 class="font-display font-semibold text-[36px] lg:text-[43px] text-gray-800 tracking-tight mb-2">
                                Romantic Escapes
                            </h2>
                            <p class="text-gray-500 max-w-sm">Beautiful, serene destinations designed for couples to relax, connect, and create memories.</p>
                        </div>
                        <a href="#" class="text-rose-500 hover:text-rose-400 font-bold text-sm whitespace-nowrap mb-1">View All &rarr;</a>
                    </div>"""

html = html.replace(romantic_old_header, romantic_new_header)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Replaced headers and added animations successfully!")
