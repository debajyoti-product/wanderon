with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix 1: Header & Subheader
old_header = """<h2 class="font-display font-bold text-4xl md:text-5xl text-brand-dark mb-5 leading-tight">Got questions?<br><span class="text-brand-cyan">We've got answers.</span></h2>
                    <p class="text-gray-500 font-medium mb-10 leading-relaxed text-lg">Everything you need to know about embarking on the journey of a lifetime with us.</p>"""
new_header = """<h2 class="font-display font-bold text-4xl md:text-5xl text-brand-dark mb-10 leading-tight">Frequently Asked Questions</h2>"""
if old_header in html:
    html = html.replace(old_header, new_header)
else:
    print("Failed to find header block")

# Fix 2: 4th Card
old_card = """<div class="bg-gradient-to-br from-brand-cyan to-brand-darkcyan text-white p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12 flex flex-col justify-center">
                            <h4 class="font-display font-bold text-xl mb-3">New to group travel?</h4>
                            <p class="text-white/80 leading-relaxed text-sm font-medium mb-6">Read our beginner's guide on what to expect, how to pack, and getting ready for the adventure.</p>
                            <a href="#" class="inline-flex items-center gap-2 text-sm font-bold bg-white text-brand-dark px-6 py-3 rounded-full w-fit hover:bg-gray-50 transition-colors">Read Guide <i class="fa-solid fa-arrow-right text-[10px]"></i></a>
                        </div>"""
new_card = """<div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12">
                            <div class="w-10 h-10 bg-brand-cyan/10 rounded-full flex items-center justify-center text-brand-cyan text-lg mb-5"><i class="fa-regular fa-circle-question"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">New to group travel?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">Don't worry! Read our beginner's guide on what to expect, how to pack, and getting ready for the adventure.</p>
                        </div>"""
if old_card in html:
    html = html.replace(old_card, new_card)
else:
    print("Failed to find 4th card block")

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated successfully")
