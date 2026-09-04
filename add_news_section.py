with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

news_section = """
    <!-- In the News Section -->
    <section class="py-16 md:py-24 bg-gray-50/50">
        <div class="max-w-7xl mx-auto px-4 lg:px-8">
            <div class="text-center max-w-2xl mx-auto mb-14">
                <h2 class="font-display font-bold text-3xl md:text-4xl text-brand-dark mb-4">In the News</h2>
                <p class="text-gray-500 font-medium leading-relaxed">See what top publications are saying about our community-driven trips and massive growth.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8 max-w-5xl mx-auto">
                <!-- Article 1 -->
                <a href="https://www.republicworld.com/initiatives/why-wanderon-is-becoming-a-leading-group-tour-company-for-young-indian-travellers-2026-06-19-129097" target="_blank" class="bg-white rounded-[2rem] p-8 md:p-10 border border-gray-100 shadow-sm hover:shadow-xl hover:border-brand-cyan/20 hover:-translate-y-1 transition-all duration-300 group flex flex-col">
                    <div class="mb-6 flex items-center justify-between">
                        <div class="font-display font-black text-xl tracking-tight text-red-600 flex items-center gap-2">
                            <i class="fa-regular fa-newspaper"></i> <span class="text-black font-bold text-lg">REPUBLIC</span>
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-xl md:text-2xl text-gray-800 leading-snug mb-8 group-hover:text-brand-cyan transition-colors">Why WanderOn is becoming a leading group tour company for young Indian travellers</h3>
                    <div class="mt-auto inline-flex items-center gap-2 text-sm font-bold text-brand-cyan uppercase tracking-wide">Read Article <i class="fa-solid fa-arrow-right text-[10px] transition-transform group-hover:translate-x-1"></i></div>
                </a>

                <!-- Article 2 -->
                <a href="https://www.moneycontrol.com/news/business/startup/wanderon-raises-rs-54-crore-in-series-a-fund-raise-led-by-dsg-consumer-partners-caaf-13782121.html" target="_blank" class="bg-white rounded-[2rem] p-8 md:p-10 border border-gray-100 shadow-sm hover:shadow-xl hover:border-brand-cyan/20 hover:-translate-y-1 transition-all duration-300 group flex flex-col">
                    <div class="mb-6 flex items-center justify-between">
                        <div class="font-display font-black text-xl tracking-tighter text-[#00a651] flex items-center gap-1.5">
                            <i class="fa-solid fa-chart-line"></i> moneycontrol
                        </div>
                        <div class="w-8 h-8 rounded-full bg-gray-50 flex items-center justify-center text-gray-400 group-hover:bg-brand-cyan group-hover:text-white transition-colors">
                            <i class="fa-solid fa-arrow-up-right-from-square text-xs"></i>
                        </div>
                    </div>
                    <h3 class="font-display font-bold text-xl md:text-2xl text-gray-800 leading-snug mb-8 group-hover:text-brand-cyan transition-colors">WanderOn raises Rs 54 crore in Series A fund raise led by DSG Consumer Partners, CAAF</h3>
                    <div class="mt-auto inline-flex items-center gap-2 text-sm font-bold text-brand-cyan uppercase tracking-wide">Read Article <i class="fa-solid fa-arrow-right text-[10px] transition-transform group-hover:translate-x-1"></i></div>
                </a>
            </div>
        </div>
    </section>
"""

# Insert right before footer
target = "<!-- Playful Footer (Clean & Modern) -->"
if target in html:
    html = html.replace(target, news_section + "\n\n    " + target)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Success")
else:
    print("Failed to find target")
