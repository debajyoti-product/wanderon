import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Unify x-data for the main layout to share `style` state
# Find: <main class="max-w-7xl mx-auto px-4 lg:px-8 py-12 flex flex-col lg:flex-row gap-12 relative">
main_tag = '<main class="max-w-7xl mx-auto px-4 lg:px-8 py-12 flex flex-col lg:flex-row gap-12 relative">'
new_main_tag = '<main class="max-w-7xl mx-auto px-4 lg:px-8 py-12 flex flex-col lg:flex-row gap-12 relative" x-data="{ style: \'rented\' }">'
html = html.replace(main_tag, new_main_tag)

# Remove the old x-data="{ style: 'rented' }" from the Travel Styles wrapper
old_xdata = '<div x-data="{ style: \'rented\' }" class="mb-16">'
new_xdata = '<div class="mb-8">' # Also addressing Goal 1 (Move exclusions higher) by reducing mb-16 to mb-8
html = html.replace(old_xdata, new_xdata)

# Move general exclusions 15% higher -> We just reduced the bottom margin of the div above it.
# Let's also add negative margin to the exclusions card
old_excl_card = '<div class="bg-red-50/50 border border-red-100 rounded-[2rem] p-6 md:p-8 mb-16 shadow-sm">'
new_excl_card = '<div class="bg-red-50/50 border border-red-100 rounded-[2rem] p-6 md:p-8 mb-16 shadow-sm -mt-6">'
html = html.replace(old_excl_card, new_excl_card)

# 2. Fix Things to Pack auto-adjust height
old_pack_content = '<div class="bg-white border border-gray-100 rounded-3xl p-6 md:p-8 shadow-sm transition-all duration-300 min-h-[220px]">'
new_pack_content = '<div class="bg-white border border-gray-100 rounded-3xl p-6 md:p-8 shadow-sm transition-all duration-300">'
html = html.replace(old_pack_content, new_pack_content)

# 3 & 4. Right Column changes (Booking Card: inputs + dynamic tag)
# We need to find the specific select dropdown and replace it.
style_dropdown = """<div>
                        <label class="text-xs font-bold text-gray-500 uppercase tracking-wide mb-2 block">Travel Style</label>
                        <select class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-semibold text-gray-700 outline-none focus:border-brand-cyan transition">
                            <option>SUV / Tempo Traveller</option>
                            <option>Self-Ride (Rented Bike)</option>
                            <option>Self-Ride (Own Bike)</option>
                        </select>
                    </div>"""

inputs_and_tag = """<div class="mb-4">
                        <span class="text-[10px] font-bold text-gray-400 uppercase tracking-wide mr-2 block mb-2">Selected Package:</span>
                        <div class="inline-block bg-cyan-50 text-brand-cyan px-4 py-1.5 rounded-full text-xs font-bold border border-cyan-100" x-text="style === 'suv' ? 'SUV / Tempo Traveller' : (style === 'rented' ? 'Self-Ride (Rented Bike)' : 'Self-Ride (Own Bike)')">Self-Ride (Rented Bike)</div>
                    </div>
                    <div>
                        <input type="text" placeholder="Full Name" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-semibold text-gray-700 outline-none focus:border-brand-cyan transition mb-3">
                        <input type="tel" placeholder="Phone Number" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-semibold text-gray-700 outline-none focus:border-brand-cyan transition mb-3">
                        <input type="email" placeholder="Email Address" class="w-full bg-gray-50 border border-gray-200 rounded-xl px-4 py-3 text-sm font-semibold text-gray-700 outline-none focus:border-brand-cyan transition">
                    </div>"""
html = html.replace(style_dropdown, inputs_and_tag)

# 5. Route & Logistics Section above Itinerary
itin_header = '<h2 class="font-display font-bold text-2xl text-brand-dark mb-8">Daily Itinerary</h2>'
logistics_section = """<!-- Route & Logistics -->
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
                    <p class="text-sm text-gray-700 leading-relaxed font-semibold">
                        Delhi <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Manali <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Sarchu <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Tso Moriri <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Hanle <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Umling La <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Pangong <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Nubra Valley <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Leh <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Kargil <i class="fa-solid fa-arrow-right-long mx-1.5 text-brand-cyan"></i> Srinagar
                    </p>
                </div>
            </div>

            """
html = html.replace(itin_header, logistics_section + itin_header)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Part 1: State, Inputs, Fixes, Logistics completed.")
