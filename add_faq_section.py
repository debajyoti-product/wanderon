import re

with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "r", encoding="utf-8") as f:
    html = f.read()

faq_section = """
    <!-- Creative FAQ Explorer Section -->
    <section class="py-20 md:py-32 bg-white relative overflow-hidden" x-data="{ faqCategory: 'getting_started' }">
        <!-- Ambient Backgrounds -->
        <div class="absolute top-0 right-0 w-[600px] h-[600px] bg-brand-cyan/5 rounded-full blur-3xl -translate-y-1/2 translate-x-1/3 pointer-events-none"></div>
        <div class="absolute bottom-0 left-0 w-[500px] h-[500px] bg-yellow-100/30 rounded-full blur-3xl translate-y-1/3 -translate-x-1/3 pointer-events-none"></div>

        <div class="max-w-7xl mx-auto px-4 lg:px-8 relative z-10">
            <div class="flex flex-col lg:flex-row gap-12 lg:gap-20 items-start">
                
                <!-- Left Column: Header, Tabs & CTA -->
                <div class="w-full lg:w-1/3 lg:sticky lg:top-32">
                    <h2 class="font-display font-bold text-4xl md:text-5xl text-brand-dark mb-5 leading-tight">Got questions?<br><span class="text-brand-cyan">We've got answers.</span></h2>
                    <p class="text-gray-500 font-medium mb-10 leading-relaxed text-lg">Everything you need to know about embarking on the journey of a lifetime with us.</p>
                    
                    <!-- Tabs -->
                    <div class="flex flex-row lg:flex-col gap-3 overflow-x-auto pb-4 lg:pb-0 scrollbar-hide mb-10 -mx-4 px-4 lg:mx-0 lg:px-0">
                        <button @click="faqCategory = 'getting_started'" 
                                :class="faqCategory === 'getting_started' ? 'bg-brand-dark text-white shadow-lg shadow-brand-dark/20 translate-x-0 lg:translate-x-2' : 'bg-gray-50 text-gray-600 hover:bg-gray-100'" 
                                class="px-6 py-4 rounded-2xl font-bold text-left transition-all duration-300 flex items-center gap-4 shrink-0 lg:shrink-0 whitespace-nowrap lg:whitespace-normal">
                            <div class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-colors" :class="faqCategory === 'getting_started' ? 'bg-white/20 text-brand-cyan' : 'bg-gray-200 text-gray-400'"><i class="fa-solid fa-rocket text-sm"></i></div>
                            Getting Started
                        </button>

                        <button @click="faqCategory = 'trips'" 
                                :class="faqCategory === 'trips' ? 'bg-brand-dark text-white shadow-lg shadow-brand-dark/20 translate-x-0 lg:translate-x-2' : 'bg-gray-50 text-gray-600 hover:bg-gray-100'" 
                                class="px-6 py-4 rounded-2xl font-bold text-left transition-all duration-300 flex items-center gap-4 shrink-0 lg:shrink-0 whitespace-nowrap lg:whitespace-normal">
                            <div class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-colors" :class="faqCategory === 'trips' ? 'bg-white/20 text-yellow-400' : 'bg-gray-200 text-gray-400'"><i class="fa-solid fa-map-location-dot text-sm"></i></div>
                            Trips & Itineraries
                        </button>

                        <button @click="faqCategory = 'payments'" 
                                :class="faqCategory === 'payments' ? 'bg-brand-dark text-white shadow-lg shadow-brand-dark/20 translate-x-0 lg:translate-x-2' : 'bg-gray-50 text-gray-600 hover:bg-gray-100'" 
                                class="px-6 py-4 rounded-2xl font-bold text-left transition-all duration-300 flex items-center gap-4 shrink-0 lg:shrink-0 whitespace-nowrap lg:whitespace-normal">
                            <div class="w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-colors" :class="faqCategory === 'payments' ? 'bg-white/20 text-green-400' : 'bg-gray-200 text-gray-400'"><i class="fa-solid fa-credit-card text-sm"></i></div>
                            Payments & Policies
                        </button>
                    </div>

                    <a href="#" class="inline-flex items-center justify-center gap-2 px-8 py-4 bg-white border-2 border-brand-cyan text-brand-cyan rounded-full font-bold hover:bg-brand-cyan hover:text-white transition-all shadow-sm group w-full lg:w-auto">
                        View all FAQs <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
                    </a>
                </div>

                <!-- Right Column: Q&A Grid -->
                <div class="w-full lg:w-2/3">
                    
                    <!-- Getting Started Content -->
                    <div x-show="faqCategory === 'getting_started'" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0" class="grid grid-cols-1 md:grid-cols-2 gap-6 pb-8 md:pb-0">
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-brand-cyan/10 rounded-full flex items-center justify-center text-brand-cyan text-lg mb-5"><i class="fa-solid fa-user-group"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Do I need to come with a group?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">Not at all! Over 60% of our community joins solo and leaves with a squad of lifelong friends.</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12">
                            <div class="w-10 h-10 bg-brand-cyan/10 rounded-full flex items-center justify-center text-brand-cyan text-lg mb-5"><i class="fa-regular fa-face-smile-wink"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Who usually travels with WanderOn?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">Our trips are curated for young travelers aged 18-35. Expect a high-energy, like-minded community!</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-brand-cyan/10 rounded-full flex items-center justify-center text-brand-cyan text-lg mb-5"><i class="fa-solid fa-users-viewfinder"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">What's the average group size?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">We keep it intimate and fun—usually between 12 to 20 travelers plus our seasoned trip captains.</p>
                        </div>
                        
                        <div class="bg-gradient-to-br from-brand-cyan to-brand-darkcyan text-white p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12 flex flex-col justify-center">
                            <h4 class="font-display font-bold text-xl mb-3">New to group travel?</h4>
                            <p class="text-white/80 leading-relaxed text-sm font-medium mb-6">Read our beginner's guide on what to expect, how to pack, and getting ready for the adventure.</p>
                            <a href="#" class="inline-flex items-center gap-2 text-sm font-bold bg-white text-brand-dark px-6 py-3 rounded-full w-fit hover:bg-gray-50 transition-colors">Read Guide <i class="fa-solid fa-arrow-right text-[10px]"></i></a>
                        </div>
                    </div>

                    <!-- Trips & Itineraries Content -->
                    <div x-show="faqCategory === 'trips'" style="display: none;" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0" class="grid grid-cols-1 md:grid-cols-2 gap-6 pb-8 md:pb-0">
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-500 text-lg mb-5"><i class="fa-solid fa-route"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Are the itineraries flexible?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">While we stick to a well-planned schedule to ensure you don't miss out, you always have free time to explore at your own pace.</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12">
                            <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-500 text-lg mb-5"><i class="fa-solid fa-mountain"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">How difficult are the treks?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">We have trips for all levels! Each itinerary clearly labels the physical requirement, from chill getaways to extreme adventures.</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-500 text-lg mb-5"><i class="fa-solid fa-pen-to-square"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Can I customize a trip?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">Absolutely! For private groups of 6 or more, we offer fully customized itineraries. Just hit us up!</p>
                        </div>

                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12">
                            <div class="w-10 h-10 bg-yellow-100 rounded-full flex items-center justify-center text-yellow-500 text-lg mb-5"><i class="fa-solid fa-bed"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">What about stays & food?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">We partner with top-rated hotels, boutique stays, and camps. Daily breakfast and dinner are always on us.</p>
                        </div>
                    </div>

                    <!-- Payments Content -->
                    <div x-show="faqCategory === 'payments'" style="display: none;" x-transition:enter="transition ease-out duration-300" x-transition:enter-start="opacity-0 translate-y-4" x-transition:enter-end="opacity-100 translate-y-0" class="grid grid-cols-1 md:grid-cols-2 gap-6 pb-8 md:pb-0">
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-green-500 text-lg mb-5"><i class="fa-solid fa-wallet"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Can I pay in EMIs?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">Yes! You can secure your slot by paying just 25% upfront and the rest in convenient installments closer to the trip date.</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm md:translate-y-12">
                            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-green-500 text-lg mb-5"><i class="fa-solid fa-rotate-left"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">What is the cancellation policy?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">We offer flexible cancellations. Cancel up to 15 days before departure for a hassle-free refund or free date change.</p>
                        </div>
                        
                        <div class="bg-white border border-gray-100 p-8 rounded-[2rem] hover:shadow-xl hover:-translate-y-1 transition-all duration-300 shadow-sm">
                            <div class="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center text-green-500 text-lg mb-5"><i class="fa-solid fa-magnifying-glass-dollar"></i></div>
                            <h4 class="font-display font-bold text-lg text-brand-dark mb-3">Are there any hidden charges?</h4>
                            <p class="text-gray-600 leading-relaxed text-sm font-medium">None. Our pricing is 100% transparent. Inclusions and exclusions are strictly detailed for every single itinerary.</p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </section>
"""

target = "<!-- Playful Footer (Clean & Modern) -->"
if target in html:
    html = html.replace(target, faq_section + "\n\n    " + target)
    with open("c:/Users/Debajyoti/.antigravity/wanderon/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Success")
else:
    print("Failed to find target")
