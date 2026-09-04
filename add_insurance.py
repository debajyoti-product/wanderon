with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

insurance_card = """<!-- Medical Insurance Card -->
            <div class="bg-brand-cyan/10 border border-brand-cyan/20 rounded-[1.5rem] p-5 md:p-6 mb-6 flex flex-col md:flex-row items-start md:items-center justify-between gap-4 shadow-sm relative z-20">
                <div class="flex items-start gap-4">
                    <div class="w-10 h-10 rounded-full bg-brand-cyan text-white flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-file-medical text-lg"></i></div>
                    <div>
                        <h4 class="font-display font-bold text-base text-brand-dark mb-1">Medical insurance coverage</h4>
                        <p class="text-xs md:text-sm text-gray-600 leading-relaxed max-w-2xl font-medium">Valid strictly from base to base. Does not include any travel before arrival at the starting point or after departure from the ending point.</p>
                    </div>
                </div>
                <a href="#" class="text-sm font-bold text-brand-cyan hover:text-brand-darkcyan whitespace-nowrap md:self-center shrink-0 transition-colors flex items-center gap-1 group">View details <i class="fa-solid fa-chevron-right text-[10px] transition-transform group-hover:translate-x-0.5"></i></a>
            </div>

            <!-- General Exclusions Card -->
            <div class="bg-red-50/50 border border-red-100 rounded-[2rem] p-6 md:p-8 mb-16 shadow-sm">"""

old_target = """<!-- General Exclusions Card -->
            <div class="bg-red-50/50 border border-red-100 rounded-[2rem] p-6 md:p-8 mb-16 shadow-sm -mt-6">"""

if old_target in html:
    html = html.replace(old_target, insurance_card)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully added medical insurance card.")
else:
    print("Target not found. Please review the old target string.")
