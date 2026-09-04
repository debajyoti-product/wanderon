import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# EXTRACT
india_match = re.search(r'(<!-- Discover Incredible India.*?)(?=<!-- Trust Corner)', html, re.DOTALL)
trust_match = re.search(r'(<!-- Trust Corner.*?)(?=<!-- Explore The World)', html, re.DOTALL)
intl_match = re.search(r'(<!-- Explore The World.*?</section>)', html, re.DOTALL)

if not india_match or not trust_match or not intl_match:
    print("Failed to find sections")
    exit(1)

india_html = india_match.group(1)
trust_html = trust_match.group(1)
intl_html = intl_match.group(1)

# Remove the original blocks from HTML
html = html.replace(india_html, '')
html = html.replace(trust_html, '')
html = html.replace(intl_html, '')

new_trips_hub = f"""
<!-- COMBINED TRIPS HUB (DOMESTIC & INTL) -->
<section id="trips-hub" class="flex flex-col lg:flex-row w-full h-[120vh] lg:h-[950px] overflow-hidden bg-gray-900 border-y border-gray-100 relative">
    
    <!-- DOMESTIC PANEL -->
    <div id="panel-domestic" class="relative group cursor-pointer overflow-hidden transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] flex-[4]" onclick="expandPanel('domestic')">
        <!-- Expanded View -->
        <div id="dom-exp" class="absolute inset-0 w-full h-full overflow-y-auto overflow-x-hidden transition-opacity duration-700 opacity-100 pointer-events-auto bg-[#faf9f6]">
            <div class="w-full lg:w-[80vw] min-h-full">
                {india_html}
            </div>
        </div>
        <!-- Collapsed View -->
        <div id="dom-col" class="absolute inset-0 w-full h-full overflow-hidden transition-opacity duration-700 opacity-0 pointer-events-none bg-black">
            <img src="india_map.jpg" class="w-full h-full object-cover opacity-40 group-hover:opacity-60 transition-opacity duration-500" alt="Domestic Background">
            <div class="absolute inset-0 bg-brand-yellow/30 mix-blend-multiply"></div>
            <div class="absolute inset-0 flex items-center justify-center p-4">
                <h2 class="text-white font-display font-bold text-3xl md:text-4xl lg:text-[40px] tracking-widest uppercase lg:[writing-mode:vertical-rl] lg:rotate-180 whitespace-nowrap drop-shadow-md">Domestic</h2>
            </div>
        </div>
    </div>
    
    <!-- INTL PANEL -->
    <div id="panel-intl" class="relative group cursor-pointer overflow-hidden transition-all duration-700 ease-[cubic-bezier(0.25,1,0.5,1)] flex-[1]" onclick="expandPanel('intl')">
        <!-- Expanded View -->
        <div id="intl-exp" class="absolute inset-0 w-full h-full overflow-y-auto overflow-x-hidden transition-opacity duration-700 opacity-0 pointer-events-none bg-[#f6f9fc]">
            <div class="w-full lg:w-[80vw] min-h-full">
                {intl_html}
            </div>
        </div>
        <!-- Collapsed View -->
        <div id="intl-col" class="absolute inset-0 w-full h-full overflow-hidden transition-opacity duration-700 opacity-100 pointer-events-auto bg-black">
            <img src="world_map.jpg" class="w-full h-full object-cover opacity-40 group-hover:opacity-60 transition-opacity duration-500" alt="Intl Background">
            <div class="absolute inset-0 bg-brand-cyan/30 mix-blend-multiply"></div>
            <div class="absolute inset-0 flex items-center justify-center p-4">
                <h2 class="text-white font-display font-bold text-3xl md:text-4xl lg:text-[40px] tracking-widest uppercase lg:[writing-mode:vertical-rl] lg:rotate-180 whitespace-nowrap drop-shadow-md">International</h2>
            </div>
        </div>
    </div>
</section>

<!-- Trust Corner (Testimonials) Relocated Below Hub -->
{trust_html}
"""

# Insert new structure precisely where the original block was (before Footer or Wanderon Across the World)
# Actually, the original sequence was: 
# ... -> Upcoming Community Trips -> India -> Trust -> Intl -> Stats ...
# But we removed them. Let's find where to insert.
# We can find "<!-- Upcoming Community Trips Section -->" and find the end of that section, then inject.
community_match = re.search(r'<!-- Upcoming Community Trips Section -->.*?</section>', html, re.DOTALL)
if community_match:
    end_pos = community_match.end()
    html = html[:end_pos] + '\n\n' + new_trips_hub + html[end_pos:]
else:
    print("Failed to find insertion point")
    exit(1)

# Add the JS toggle function before </body>
js_logic = """
    <!-- Custom Panel Toggle Logic -->
    <script>
    function expandPanel(panelId) {
        const pDom = document.getElementById('panel-domestic');
        const pIntl = document.getElementById('panel-intl');
        
        const domExp = document.getElementById('dom-exp');
        const domCol = document.getElementById('dom-col');
        const intlExp = document.getElementById('intl-exp');
        const intlCol = document.getElementById('intl-col');
        
        if (panelId === 'domestic') {
            pDom.classList.replace('flex-[1]', 'flex-[4]') || pDom.classList.add('flex-[4]');
            pDom.classList.remove('flex-[1]');
            pIntl.classList.replace('flex-[4]', 'flex-[1]') || pIntl.classList.add('flex-[1]');
            pIntl.classList.remove('flex-[4]');
            
            domExp.classList.replace('opacity-0', 'opacity-100');
            domExp.classList.replace('pointer-events-none', 'pointer-events-auto');
            domCol.classList.replace('opacity-100', 'opacity-0');
            domCol.classList.replace('pointer-events-auto', 'pointer-events-none');
            
            intlExp.classList.replace('opacity-100', 'opacity-0');
            intlExp.classList.replace('pointer-events-auto', 'pointer-events-none');
            intlCol.classList.replace('opacity-0', 'opacity-100');
            intlCol.classList.replace('pointer-events-none', 'pointer-events-auto');
            
        } else {
            pDom.classList.replace('flex-[4]', 'flex-[1]') || pDom.classList.add('flex-[1]');
            pDom.classList.remove('flex-[4]');
            pIntl.classList.replace('flex-[1]', 'flex-[4]') || pIntl.classList.add('flex-[4]');
            pIntl.classList.remove('flex-[1]');
            
            domExp.classList.replace('opacity-100', 'opacity-0');
            domExp.classList.replace('pointer-events-auto', 'pointer-events-none');
            domCol.classList.replace('opacity-0', 'opacity-100');
            domCol.classList.replace('pointer-events-none', 'pointer-events-auto');
            
            intlExp.classList.replace('opacity-0', 'opacity-100');
            intlExp.classList.replace('pointer-events-none', 'pointer-events-auto');
            intlCol.classList.replace('opacity-100', 'opacity-0');
            intlCol.classList.replace('pointer-events-auto', 'pointer-events-none');
        }
    }
    </script>
"""

html = html.replace('</body>', js_logic + '\n</body>')

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
    f.write(html)
    
print("Combined Hub created successfully.")
