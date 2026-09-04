with open("c:/Users/Debajyoti/.antigravity/wanderon/search.html", "r", encoding="utf-8") as f:
    text = f.read()

# We need to insert the Budget UI inside the Mobile Filter Bottom Sheet.
# The mobile filter sheet has a <div class="space-y-6"> followed by <!-- Duration (Added 1-3 Days) -->

search_str = """            <div class="space-y-6">
                <!-- Duration (Added 1-3 Days) -->
                <div>"""

replace_str = """            <div class="space-y-6">
                <!-- Budget -->
                <div>
                    <h3 class="font-display font-bold text-sm text-brand-dark mb-3 tracking-wide">Budget</h3>
                    <div class="mb-4 mt-2 px-1 relative">
                        <div class="range-slider">
                            <div class="range-slider-track" :style="`left: ${(minBudget/50000)*100}%; right: ${100 - (maxBudget/50000)*100}%`"></div>
                            <input type="range" min="0" max="50000" step="500" x-model.number="minBudget" @input="minBudget = Math.min(minBudget, maxBudget - 500)" class="z-20">
                            <input type="range" min="0" max="50000" step="500" x-model.number="maxBudget" @input="maxBudget = Math.max(maxBudget, minBudget + 500)" class="z-20">
                        </div>
                    </div>
                    <div class="flex items-center gap-2">
                        <div class="relative flex-1">
                            <span class="absolute left-2.5 top-1/2 -translate-y-1/2 text-gray-400 text-xs font-semibold">₹</span>
                            <input type="number" x-model.number="minBudget" class="w-full bg-gray-50 border border-gray-200 rounded-xl py-1.5 pl-6 pr-2 text-xs font-bold text-gray-700 focus:outline-none focus:border-brand-cyan transition-colors" @change="minBudget = Math.min(Math.max(0, minBudget), maxBudget - 500)">
                        </div>
                        <span class="text-gray-400 text-xs">-</span>
                        <div class="relative flex-1">
                            <span class="absolute left-2.5 top-1/2 -translate-y-1/2 text-gray-400 text-xs font-semibold">₹</span>
                            <input type="number" x-model.number="maxBudget" class="w-full bg-gray-50 border border-gray-200 rounded-xl py-1.5 pl-6 pr-2 text-xs font-bold text-gray-700 focus:outline-none focus:border-brand-cyan transition-colors" @change="maxBudget = Math.max(Math.min(50000, maxBudget), minBudget + 500)">
                        </div>
                    </div>
                </div>

                <!-- Duration (Added 1-3 Days) -->
                <div>"""

if search_str in text:
    text = text.replace(search_str, replace_str)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/search.html", "w", encoding="utf-8") as f:
        f.write(text)
    print("Updated mobile filter successfully!")
else:
    print("Could not find the mobile filter injection point!")
