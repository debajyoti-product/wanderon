import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove budget divider + budget section from search bar
old_budget_block = """                    <div class="w-px bg-gray-100 my-1.5 hidden md:block"></div>

                    <!-- HOW MUCH -->
                    <div class="flex-1 px-5 py-2 hover:bg-gray-50 rounded-full transition cursor-pointer group relative" onclick="openHeroModal('budgetModal')">
                        <div class="text-[9px] font-bold text-gray-400 uppercase tracking-widest mb-0.5 group-hover:text-brand-cyan transition-colors">How much</div>
                        <div class="font-semibold text-gray-800 text-sm flex items-center gap-2" id="budget-value">
                            Any budget
                        </div>
                    </div>
                    
                    <button class="bg-brand-cyan text-white px-8 py-2 md:ml-2 rounded-full font-display font-bold text-sm hover:bg-brand-darkcyan hover:shadow-lg hover:shadow-cyan-500/30 transition-all flex items-center justify-center gap-2 active:scale-95 mt-2 md:mt-0">
                        Search <i class="fa-solid fa-arrow-right text-xs hidden lg:block"></i>
                    </button>"""

new_search_button = """                    <button onclick="performSearch()" class="bg-brand-cyan text-white px-8 py-2 md:ml-2 rounded-full font-display font-bold text-sm hover:bg-brand-darkcyan hover:shadow-lg hover:shadow-cyan-500/30 transition-all flex items-center justify-center gap-2 active:scale-95 mt-2 md:mt-0">
                        Search <i class="fa-solid fa-arrow-right text-xs hidden lg:block"></i>
                    </button>"""

if old_budget_block in html:
    html = html.replace(old_budget_block, new_search_button)
    print("1. Removed budget section from search bar")
else:
    print("1. FAILED to find budget block")

# 2. Remove budgetModal HTML
budget_modal_start = '                <!-- Budget Modal -->'
budget_modal_end = '                </div>\n\n\n                <!-- Rating & Review Count Pills -->'
idx_start = html.find(budget_modal_start)
idx_end = html.find('<!-- Rating & Review Count Pills -->')
if idx_start > 0 and idx_end > 0:
    html = html[:idx_start] + '\n                <!-- Rating & Review Count Pills -->' + html[idx_end + len('<!-- Rating & Review Count Pills -->'):] 
    print("2. Removed budgetModal HTML")
else:
    print(f"2. FAILED to find budget modal (start={idx_start}, end={idx_end})")

# 3. Remove selectBudget function and budgetModal from closeHeroModals
old_close = "const modals = ['whereModal', 'whenModal', 'budgetModal'];"
new_close = "const modals = ['whereModal', 'whenModal'];"
if old_close in html:
    html = html.replace(old_close, new_close)
    print("3. Removed budgetModal from closeHeroModals")
else:
    print("3. FAILED to find closeHeroModals")

# 4. Remove selectBudget function
old_select_budget = """function selectBudget(budgetText) {
            document.getElementById('budget-value').innerText = budgetText;
            closeHeroModals();
        }"""
if old_select_budget in html:
    html = html.replace(old_select_budget, "")
    print("4. Removed selectBudget function")
else:
    print("4. FAILED to find selectBudget function")

# 5. Add performSearch function before closing </script>
search_func = """
        function performSearch() {
            const where = document.getElementById('where-value').innerText.trim();
            const when = document.getElementById('when-value').innerText.trim();
            const params = new URLSearchParams();
            if (where && where !== 'Anywhere') params.set('where', where);
            if (when && when !== 'Any date') params.set('when', when);
            window.location.href = 'search.html' + (params.toString() ? '?' + params.toString() : '');
        }"""

# Find the last </script> before the body close
last_script_end = html.rfind('</script>')
if last_script_end > 0:
    # Find the position just before </script>
    insert_pos = last_script_end
    html = html[:insert_pos] + search_func + '\n    ' + html[insert_pos:]
    print("5. Added performSearch function")
else:
    print("5. FAILED to find </script>")

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nDone! Search bar updated.")
