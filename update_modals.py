with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update Header Button
text = text.replace(
    '''<button onclick="document.getElementById('enquiry-modal').classList.remove('hidden')" class="bg-brand-dark text-white px-6 py-2.5 rounded-full shadow-lg hover:shadow-xl hover:bg-brand-cyan hover:-translate-y-0.5 transition-all">Submit Enquiry</button>''',
    '''<button onclick="openEnquiryModal('default')" class="bg-brand-dark text-white px-6 py-2.5 rounded-full shadow-lg hover:shadow-xl hover:bg-brand-cyan hover:-translate-y-0.5 transition-all">Submit Enquiry</button>'''
)

# 2. Update Solo Button
solo_btn_old = '''<h3 class="font-display font-bold text-[22px] text-brand-dark mb-3 leading-tight">Looking to travel solo?</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-8 flex-grow">
                        Don't worry, our community is here with you. Join thousands of solo travelers who found their tribe.
                    </p>
                    <button onclick="document.getElementById('enquiry-modal').classList.remove('hidden')" class="w-full bg-white border border-brand-cyan text-brand-dark hover:bg-brand-cyan hover:text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center mt-auto text-sm">'''
solo_btn_new = '''<h3 class="font-display font-bold text-[22px] text-brand-dark mb-3 leading-tight">Looking to travel solo?</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-8 flex-grow">
                        Don't worry, our community is here with you. Join thousands of solo travelers who found their tribe.
                    </p>
                    <button onclick="openEnquiryModal('solo')" class="w-full bg-white border border-brand-cyan text-brand-dark hover:bg-brand-cyan hover:text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center mt-auto text-sm">'''
text = text.replace(solo_btn_old, solo_btn_new)

# 3. Update Group Button
group_btn_old = '''<h3 class="font-display font-bold text-[22px] text-brand-dark mb-3 leading-tight">Want to book a group trip?</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-4">
                        Great, bring your own tribe & get discounts on every booking. The more, the merrier!
                    </p>
                    
                    <button onclick="document.getElementById('discount-modal').classList.remove('hidden')" class="text-brand-cyan font-bold text-sm hover:text-brand-dark transition-colors flex items-center gap-1.5 mb-8 text-left w-fit group/link">
                        <i class="fa-solid fa-tags"></i> View discount tiers
                    </button>
                    
                    <button onclick="document.getElementById('enquiry-modal').classList.remove('hidden')" class="w-full bg-white border border-brand-cyan text-brand-dark hover:bg-brand-cyan hover:text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center mt-auto text-sm">'''
group_btn_new = '''<h3 class="font-display font-bold text-[22px] text-brand-dark mb-3 leading-tight">Want to book a group trip?</h3>
                    <p class="text-gray-500 text-sm leading-relaxed mb-4">
                        Great, bring your own tribe & get discounts on every booking. The more, the merrier!
                    </p>
                    
                    <button onclick="document.getElementById('discount-modal').classList.remove('hidden')" class="text-brand-cyan font-bold text-sm hover:text-brand-dark transition-colors flex items-center gap-1.5 mb-8 text-left w-fit group/link">
                        <i class="fa-solid fa-tags"></i> View discount tiers
                    </button>
                    
                    <button onclick="openEnquiryModal('group')" class="w-full bg-white border border-brand-cyan text-brand-dark hover:bg-brand-cyan hover:text-white font-bold py-3 rounded-xl transition-all flex items-center justify-center mt-auto text-sm">'''
text = text.replace(group_btn_old, group_btn_new)

# 4. Add ID to travelers select
select_old = '''<select required class="w-full bg-gray-50 border border-gray-200 text-brand-dark text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-brand-cyan/50 focus:border-brand-cyan transition-all appearance-none cursor-pointer">
                                <option value="" disabled selected>Select</option>
                                <option value="1">1 (Solo)</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5+">5+</option>
                            </select>'''
select_new = '''<select id="travelers-select" required class="w-full bg-gray-50 border border-gray-200 text-brand-dark text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-brand-cyan/50 focus:border-brand-cyan transition-all appearance-none cursor-pointer">
                                <option value="" disabled selected>Select</option>
                                <option value="1">1 (Solo)</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                                <option value="4">4</option>
                                <option value="5+">5+</option>
                            </select>'''
text = text.replace(select_old, select_new)

# 5. Inject openEnquiryModal script before closing script tag
script_logic = """
        function openEnquiryModal(type) {
            const modal = document.getElementById('enquiry-modal');
            const select = document.getElementById('travelers-select');
            
            // Reset to default options
            select.innerHTML = `
                <option value="" disabled selected>Select</option>
                <option value="1">1 (Solo)</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5+">5+</option>
            `;
            select.disabled = false;
            select.value = "";
            
            if (type === 'solo') {
                select.value = "1";
                select.disabled = true; // disabled as per request
            } else if (type === 'group') {
                // Remove solo option
                select.innerHTML = `
                    <option value="" disabled selected>Select</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5+">5+</option>
                `;
                select.value = "";
            }
            
            modal.classList.remove('hidden');
        }

        // Soft navbar blur effect on scroll"""
text = text.replace("// Soft navbar blur effect on scroll", script_logic)

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates completed successfully.")
