import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "r", encoding="utf-8") as f:
    html = f.read()

right_col_start = html.find('<!-- Right Column: Sticky Booking Widget -->')
right_col_end = html.find('</main>', right_col_start)

# Replace the buttons
old_buttons = """<button class="w-full bg-brand-cyan text-white py-4 rounded-xl font-display font-bold text-lg shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 mb-4">
                    Book This Trip
                </button>
                
                <button class="w-full bg-green-50 text-green-600 border border-green-200 py-3 rounded-xl font-bold text-sm hover:bg-green-100 transition flex items-center justify-center gap-2">
                    <i class="fa-brands fa-whatsapp text-lg"></i> Chat on WhatsApp
                </button>"""

new_button = """<button class="w-full bg-brand-cyan text-white py-4 rounded-full font-display font-bold text-lg shadow-lg shadow-cyan-500/30 hover:bg-brand-darkcyan transition hover:-translate-y-0.5 active:translate-y-0 flex items-center justify-center gap-2">
                    <i class="fa-solid fa-phone-volume text-xl"></i> Get a Call Back
                </button>"""

html = html.replace(old_buttons, new_button)

with open("c:/Users/Debajyoti/.antigravity/wanderon/ladakh.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated CTA button.")
