from enrich_venues import enrich_venues

# BATCH 3: IBIZA, MALLORCA, VALENCIA, PALERMO, CATANIA - PART 1

# IBIZA UPDATES
ibiza_updates = {
    "Ushuaïa Ibiza Beach Hotel": {
        "desc_tr": "Playa d'en Bossa'nın kalbindeki bu açık hava sahnesi, dünyanın en ünlü DJ'lerine ve devasa prodüksiyonlara ev sahipliği yapar. Gündüz plaj partilerinden gece yarısı festivallerine uzanan enerjisiyle, modern Ibiza kulüp kültürünün mabedidir.",
        "desc_en": "This legendary open-air stage in Playa d'en Bossa hosts the world's top DJs and massive productions. With a seamless transition from poolside day parties to midnight spectacles, it is the undisputed temple of modern Ibizan club culture."
    },
    "Amnesia Ibiza": {
        "desc_tr": "Dünyanın en iyi gece kulüplerinden biri kabul edilen Amnesia, ikonik 'buz makineleri' ve gün ışığının vurduğu terasıyla ünlüdür. Adanın spiritüel hippie köklerinden global EDM merkezine dönüşümünü simgeleyen efsanevi bir duraktır.",
        "desc_en": "Consistently ranked among the best clubs in the world, Amnesia is famous for its iconic nitrogen ice cannons and its sun-drenched terrace. It remains a legendary institution, bridging Ibiza's spiritual hippie roots with top-tier global EDM."
    },
    "Cala Salada": {
        "desc_tr": "Çam ormanlarıyla çevrili bu bakir koy, turkuazın en canlı tonlarına sahiptir. Ibiza'daki en doğal ve korunmuş plajlardan biri olan Cala Salada, kristal netliğindeki suyu ve kayaların üzerine kurulmuş geleneksel balıkçı kulübeleriyle büyüleyicidir.",
        "desc_en": "Enclosed by lush pine forests, this pristine cove boasts the most vibrant shades of turquoise. As one of Ibiza's most natural and protected beaches, it offers crystal-clear waters and charming traditional boathouses perched on the rocks."
    },
    "Lío": {
        "desc_tr": "Ibiza Marina'da yer alan bu sofistike mekan, kabare, fine-dining ve gece kulübünün eşsiz bir sentezidir. Eski kente (Dalt Vila) bakan manzarası eşliğinde sunulan dünyaca ünlü gösterileriyle adanın en lüks ve seçkin akşam yemeği deneyimidir.",
        "desc_en": "Located in Ibiza Marina, this world-renowned cabaret and club is a masterclass in 'show-dinner' elegance. With breathtaking views of Dalt Vila and high-octane performances, it is the most exclusive and glamorous dining ticket on the island."
    }
}

# MALLORCA UPDATES
mallorca_updates = {
    "Port d'Andratx": {
        "desc_tr": "Adanın güneybatısındaki bu şık liman kasabası, lüks yatları ve sahil boyunca sıralanan gurme restoranlarıyla tanınır. Balıkçı teknesi geleneğini modern lüksle birleştiren Port d'Andratx, Mallorca'nın en prestijli yerleşim birimlerinden biridir.",
        "desc_en": "This stylish harbor town in the southwest is famed for its luxury yachts and upscale waterfront dining. Seamlessly blending its traditional fishing heritage with modern high-end living, it is one of Mallorca's most prestigious coastal retreats."
    },
    "Es Trenc": {
        "desc_tr": "Karayipler'i andıran bembeyaz kumu ve sığ, tertemiz sularıyla Mallorca'nın en saf plajıdır. Bir doğa koruma alanı olan Es Trenc, kalabalık tatil köylerinden uzakta, kum tepeleri ve turkuaz denizin buluştuğu vahşi bir cennettir.",
        "desc_en": "With its brilliant white sands and shallow, crystalline waters, Es Trenc is Mallorca's most famous 'Caribbean-style' beach. Tucked away in a nature reserve, its wild dunes offer a serene alternative to the island's more developed resorts."
    },
    "Sóller": {
        "desc_tr": "Tramuntana Dağları ile çevrili bereketli bir vadide yer alan Sóller, portakal bahçeleri ve modernist mimarisiyle ünlüdür. Antik ahşap trenle ulaşılan bu kasaba, dar sokakları ve art nouveau tarzı binalarıyla zamanın durduğu bir his verir.",
        "desc_en": "Nestled in a lush 'valley of oranges' surrounded by the Tramuntana Mountains, Sóller is a gem of modernist architecture. Reached via a historic wooden train, its narrow streets and art nouveau facades offer a timeless, nostalgic charm."
    },
    "Deià": {
        "desc_tr": "Kayalıkların üzerine kurulu bal ayvazı rengindeki evleriyle Deià, on yıllardır sanatçılara ve ünlü isimlere ilham veren bir köydür. Tramuntana Dağları'nın arasına gizlenmiş bu bohem cennet, adanın en rafine ve doğal güzelliğini temsil eder.",
        "desc_en": "Perched on a hillside with honey-colored stone houses, Deià has long been a sanctuary for famous artists and writers. This bohemian haven, tucked between the Mediterranean and the mountains, captures Mallorca's most refined and poetic essence."
    }
}

# VALENCIA UPDATES
valencia_updates = {
    "Oceanogràfic València": {
        "desc_tr": "Avrupa'nın en büyük akvaryumu olan Oceanogràfic, dünyanın ana deniz ekosistemlerini temsil eden 10 farklı alana sahiptir. Köpekbalığı tünelleri ve binlerce deniz canlısıyla hem mimari hem de biyolojik bir harikadır.",
        "desc_en": "As Europe's largest aquarium, Oceanogràfic features 10 distinct areas representing the world's main marine ecosystems. With its underwater tunnels and thousands of species, it is a masterpiece of both architecture and biodiversity."
    },
    "Bioparc Valencia": {
        "desc_tr": "Geleneksel bir hayvanat bahçesinden öte, hayvanların engelsiz yaşadığı bir 'zoo-immersion' alanıdır. Afrika savanı, Madagaskar ve Ekvator ormanlarını aslına uygun şekilde canlandıran parkta kendinizi doğanın içinde hissedeceksiniz.",
        "desc_en": "More than a traditional zoo, Bioparc is a 'zoo-immersion' experience where barriers are invisible. It masterfully recreates habitats like the African Savannah and Madagascar, placing visitors directly into the heart of the wild."
    },
    "Valencia Cathedral": {
        "desc_tr": "Roma, Gotik ve Barok tarzların iç içe geçtiği bu katedral, kutsal kadeh (Holy Grail) efsanesinin kalbidir. Miguelete Kulesi'ne tırmanarak kentin tarihi dokusunu kuşbakışı izleyebilir ve yüzyıllara tanıklık eden bu yapının ihtişamını görebilirsiniz.",
        "desc_en": "A fascinating mix of Romanesque, Gothic, and Baroque styles, this cathedral is famously home to what is claimed to be the Holy Grail. Climbing the Miguelete Tower offers panoramic views of Valencia's terracotta-roofed historic center."
    }
}

# PALERMO UPDATES
palermo_updates = {
    "Palermo Cathedral": {
        "desc_tr": "Arap-Norman mimarisinin en görkemli örneklerinden biri olan bu yapı, asırlar boyunca cami, kilise ve katedral olarak kullanılmıştır. İçindeki kraliyet mezarları ve panoramik çatı katı manzarasıyla kentin çok kültürlü geçmişinin en güçlü sembolüdür.",
        "desc_en": "A grand tapestry of Arab-Norman architecture, this complex has been a mosque, a church, and a royal tomb over the centuries. Its stunning mosaics and panoramic rooftop offer a unique vantage point over Palermo's multicultural soul."
    },
    "Teatro Massimo di Palermo": {
        "desc_tr": "İtalya'nın en büyük, Avrupa'nın ise üçüncü büyük opera binası olan Teatro Massimo, görkemli neoklasik tasarımı ve kusursuz akustiğiyle bilinir. 'Baba 3' filminin final sahnesine ev sahipliği yapan bu bina, Palermo'nun sanat ve ihtişam merkezidir.",
        "desc_en": "As Italy's largest opera house, Teatro Massimo is a neoclassical jewel renowned for its perfect acoustics. Famous globally as the backdrop for the finale of 'The Godfather Part III,' it remains the cultural heart of Sicilian high art."
    },
    "Mercato Ballarò": {
        "desc_tr": "Bin yılı aşkın süredir kentin en hareketli noktası olan Ballarò, Arap tarzı pazar geleneğini sürdürür. 'Panelle' ve 'Sfingi' gibi sokak lezzetleriyle dolu bu yer, Palermo'nun gerçek ruhunu ve gürültülü neşesini en iyi yansıtan noktadır.",
        "desc_en": "A thousand-year-old tradition, Ballarò is Palermo’s oldest and most vibrant street market. Bursting with the shouts of vendors and the aroma of 'panelle' and 'arancini,' it offers an unfiltered sensory journey into the heart of Sicilian life."
    }
}

# CATANIA UPDATES
catania_updates = {
    "Mount Etna": {
        "desc_tr": "Avrupa'nın en yüksek ve en aktif yanardağı olan Etna, Catania'nın silüetine hükmeden yaşayan bir devdir. Ay yüzeyini andıran manzaraları, krater turları ve lav akıntılarıyla Sicilya'nın en efsanevi doğa macerasını sunar.",
        "desc_en": "Europe's tallest and most active volcano, Mt. Etna is a living giant dominating Catania’s horizon. Its lunar landscapes, smoldering craters, and ancient lava flows provide the most legendary natural spectacle in the Mediterranean."
    },
    "Monastero dei Benedettini di San Nicolò l'Arena": {
        "desc_tr": "Avrupa'nın en büyük Benedictine manastırlarından biri olan bu devasa yapı, UNESCO Dünya Mirası listesindedir. Lav taşları üzerine inşa edilen manastır, Barok bahçeleri ve görkemli kütüphanesiyle kentin entelektüel ve tarihi gururudur.",
        "desc_en": "One of Europe's largest Benedictine monasteries, this UNESCO-listed complex is a Baroque marvel built over layers of volcanic lava. Its sprawling cloisters, gardens, and library represent Catania's rich intellectual and spiritual history."
    },
    "Greek - Roman theatre": {
        "desc_tr": "Catania'nın modern binaları arasına gizlenmiş bu antik tiyatro, kentin lavlarla kaplı temelleri üzerinde yükselir. Mavi gökyüzü altında korunan taş basamakları ve orkestra çukuruyla kentin binlerce yıllık asaletini gözler önüne serer.",
        "desc_en": "Hidden among Catania’s modern apartment buildings, this ancient amphitheater sits directly on the city's volcanic foundations. Its well-preserved stone seating and orchestra area provide a hauntingly beautiful bridge to the city's Roman past."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Batch 3 Enrichment: Ibiza, Mallorca, Valencia, Palermo, Catania...")
enrich_venues("ibiza", ibiza_updates)
enrich_venues("mallorca", mallorca_updates)
enrich_venues("valencia", valencia_updates)
enrich_venues("palermo", palermo_updates)
enrich_venues("catania", catania_updates)
print("✨ Batch 3 Enrichment - Part 1 Complete.")
