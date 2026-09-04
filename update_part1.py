import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Hero Gallery
hero_start = html.find('<!-- Image Gallery (Horizontal Scroll) -->')
main_content_start = html.find('<!-- Main Content -->')

if hero_start != -1 and main_content_start != -1:
    new_hero = """<!-- Image Gallery (Grid Collage) -->
    <section class="max-w-7xl mx-auto px-4 lg:px-8 mt-6">
        <div class="grid grid-cols-1 md:grid-cols-4 md:grid-rows-2 gap-2 h-[350px] md:h-[500px] rounded-3xl overflow-hidden cursor-pointer">
            <!-- Large Main Image -->
            <div class="col-span-1 md:col-span-2 md:row-span-2 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1596773256086-63044a30e797?q=80&w=1600&auto=format&fit=crop" onerror="this.src='https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?q=80&w=1600&auto=format&fit=crop'" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Ladakh Mountains">
            </div>
            <!-- Top Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1616091216791-a67b140ccbc9?q=80&w=800&auto=format&fit=crop" onerror="this.src='https://images.unsplash.com/photo-1595815771614-ade9d652a65d?q=80&w=800&auto=format&fit=crop'" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Lake">
            </div>
            <!-- Top Right 2 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1558317376-74fc21f822a1?q=80&w=800&auto=format&fit=crop" onerror="this.src='https://images.unsplash.com/photo-1518002171953-a080ee817e1f?q=80&w=800&auto=format&fit=crop'" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Road">
            </div>
            <!-- Bottom Right 1 -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1500366629938-1ee46067b57d?q=80&w=800&auto=format&fit=crop" onerror="this.src='https://images.unsplash.com/photo-1612438214708-f428a707dd4e?q=80&w=800&auto=format&fit=crop'" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="Monastery">
            </div>
            <!-- Bottom Right 2 (Overlay) -->
            <div class="hidden md:block col-span-1 row-span-1 overflow-hidden relative group">
                <img src="https://images.unsplash.com/photo-1459749411175-04bf5292ceea?q=80&w=800&auto=format&fit=crop" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" alt="More">
                <div class="absolute inset-0 bg-black/40 flex items-center justify-center transition-colors group-hover:bg-black/50">
                    <span class="text-white font-bold text-2xl tracking-wide">12+</span>
                </div>
            </div>
        </div>
    </section>

    """
    html = html[:hero_start] + new_hero + html[main_content_start:]


# 2. Update Header / Breadcrumbs (Add Download/Share)
bc_start = html.find('<!-- Breadcrumbs -->')
h1_end = html.find('</h1>', bc_start)

if bc_start != -1 and h1_end != -1:
    new_header = """<!-- Breadcrumbs & Actions -->
            <div class="flex flex-wrap items-center justify-between gap-4 mb-6">
                <div class="flex items-center gap-2 text-xs font-bold text-gray-400 uppercase tracking-widest">
                    <a href="#" class="hover:text-brand-cyan">India</a>
                    <span>/</span>
                    <a href="#" class="hover:text-brand-cyan">Ladakh</a>
                    <span>/</span>
                    <span class="text-brand-cyan">Umling La Circuit</span>
                </div>
                <div class="flex items-center gap-4 text-sm font-bold text-gray-500">
                    <button class="hover:text-brand-cyan transition-colors flex items-center gap-2"><i class="fa-solid fa-download"></i> Download Itinerary</button>
                    <button class="hover:text-brand-cyan transition-colors flex items-center gap-2"><i class="fa-solid fa-share-nodes"></i> Share</button>
                </div>
            </div>

            <h1 class="font-display font-extrabold text-4xl md:text-5xl text-brand-dark leading-tight mb-4 tracking-tight">
                Ladakh & Umling La Tour: Classic Value Circuit
            </h1>"""
    html = html[:bc_start] + new_header + html[h1_end+5:]

# 3. Update Travel Styles & Inclusions
# We will do string replacements for the specific targets

# Replace description
html = html.replace('Solo or dual riding on fully serviced Royal Enfield Himalayans.', 'Solo or dual riding on fully serviced bikes.')

# Remove "Selected" tags
selected_tag_suv = '<div x-show="style === \'suv\'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider">Selected</div>'
selected_tag_rented = '<div x-show="style === \'rented\'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider" style="display: none;">Selected</div>'
selected_tag_own = '<div x-show="style === \'own\'" class="absolute top-0 right-0 bg-brand-cyan text-white text-[9px] font-bold px-3 py-1 rounded-bl-xl uppercase tracking-wider" style="display: none;">Selected</div>'

html = html.replace(selected_tag_suv, '')
html = html.replace(selected_tag_rented, '')
html = html.replace(selected_tag_own, '')

# Remove specifics card header
card_header = """<div class="flex flex-col sm:flex-row sm:items-center gap-4 mb-8 pb-5 border-b border-gray-100 relative z-10">
                        <div class="w-12 h-12 rounded-2xl bg-brand-cyan/10 flex items-center justify-center text-brand-cyan shrink-0">
                            <i class="fa-solid fa-list-check text-xl"></i>
                        </div>
                        <div>
                            <h3 class="font-display font-bold text-xl text-brand-dark" x-text="style === 'suv' ? 'SUV / Tempo Inclusions' : (style === 'rented' ? 'Rented Bike Package Specifics' : 'Own Bike Package Specifics')"></h3>
                            <p class="text-sm text-gray-500 font-medium mt-1">Here is exactly what changes based on your selected travel style.</p>
                        </div>
                    </div>"""
html = html.replace(card_header, '')

# Change subheaders
old_sub1 = '<h4 class="text-[11px] font-bold uppercase tracking-widest text-gray-400 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500"></div> Standard Across All</h4>'
new_sub1 = '<h4 class="text-[13px] font-bold uppercase tracking-widest text-gray-500 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-green-500"></div> General Inclusions</h4>'
html = html.replace(old_sub1, new_sub1)

old_sub2 = '<h4 class="text-[11px] font-bold uppercase tracking-widest text-gray-400 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-brand-cyan"></div> Style Specifics</h4>'
new_sub2 = '<h4 class="text-[13px] font-bold uppercase tracking-widest text-gray-500 mb-5 flex items-center gap-2"><div class="w-1.5 h-1.5 rounded-full bg-brand-cyan"></div> Style Specific Inclusions</h4>'
html = html.replace(old_sub2, new_sub2)

# Remove general exclusions from dynamic list
gen_excl_start = html.find('<!-- General Exclusions -->')
if gen_excl_start != -1:
    gen_excl_end = html.find('</li>', gen_excl_start)
    if gen_excl_end != -1:
        # html = html[:gen_excl_start] + html[gen_excl_end+5:]
        pass
# Wait, my previous code didn't use `<!-- General Exclusions -->` as comment, it used:
# <!-- General Exclusions -->
# <li class="flex items-start gap-4" x-show="style === 'suv'">
target_excl = """<!-- General Exclusions -->
                                <li class="flex items-start gap-4" x-show="style === 'suv'">
                                    <div class="w-8 h-8 rounded-full bg-red-50 flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-xmark text-red-500 text-sm"></i></div>
                                    <div>
                                        <div class="text-sm font-bold text-gray-800">General Exclusions</div>
                                        <div class="text-xs text-gray-500 mt-1 leading-relaxed">Flights to Leh, Lunches, Personal Expenses, Medical Evacuation.</div>
                                    </div>
                                </li>"""
html = html.replace(target_excl, '')

# Inject separate general exclusions card below the styles wrapper
styles_wrapper_end = html.find('<!-- Things to Pack (Interactive category tabs) -->')
general_exclusions_card = """<!-- General Exclusions Card -->
            <div class="bg-red-50/50 border border-red-100 rounded-[2rem] p-6 md:p-8 mb-16 shadow-sm">
                <h3 class="font-display font-bold text-lg text-red-800 mb-6 flex items-center gap-2"><i class="fa-solid fa-circle-xmark text-red-500"></i> General Exclusions</h3>
                <ul class="grid grid-cols-1 md:grid-cols-2 gap-y-4 gap-x-8 text-sm text-gray-700 font-medium">
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Flights/Trains to and from Leh</li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Lunches during the entire trip</li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Personal expenses (laundry, snacks, bottled water)</li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Any medical emergency or evacuation costs</li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Any meals not explicitly mentioned in inclusions</li>
                    <li class="flex items-start gap-3"><i class="fa-solid fa-minus text-red-400 mt-1"></i> Any permit fees for foreign nationals</li>
                </ul>
            </div>
            
            """
html = html[:styles_wrapper_end] + general_exclusions_card + html[styles_wrapper_end:]

# 4. Booking Card CTA Update
# Look for <div class="grid grid-cols-2 gap-3 mb-6"> or similar in the right column
cta_start = html.find('<div class="flex gap-3 mb-4">')
if cta_start == -1: cta_start = html.find('<div class="flex flex-col gap-3">')
if cta_start == -1: cta_start = html.find('<div class="grid grid-cols-1 gap-3">')
if cta_start == -1: cta_start = html.find('<div class="flex gap-4 mt-6">')
if cta_start == -1:
    # Let's just find the first button in the Right Column
    right_col = html.find('<!-- Right Column: Sticky Booking Widget -->')
    btn_start = html.find('<button', right_col)
    
    # We will replace all buttons in that sticky widget area with the single CTA
    # The sticky widget typically ends before `<!-- Trust Corner -->` or `<!-- Social Proof / Reviews -->`
    # Let's write a targeted script to extract the right column and replace the buttons container.

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Hero, Header, Inclusions, Exclusions.")
