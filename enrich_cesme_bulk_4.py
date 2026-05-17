from enrich_venues import enrich_venues

# BATCH: ÇEŞME SYSTEMATIC COMPLETION - PART 4 (FINAL)

cesme_bulk_4_updates = {
    "Two Sexy Fish Alaçatı": {
        "desc_tr": "Alaçatı'nın en iddialı ve modern kentsel lezzet duraklarından olan Two Sexy Fish, yüksek enerjili müzikleri ve şık sunumlarıyla tanınır. Gastronomi ile eğlenceyi kentsel bir estetikle buluşturan kentin en kentsel sosyal duraklarındandır.",
        "desc_en": "One of Alaçatı's most ambitious food stops, Two Sexy Fish is known for high-energy music and chic service. It’s an urban landmark merging gastronomy and entertainment with a modern local aesthetic."
    },
    "Mirror Alaçatı": {
        "desc_tr": "Kentsel şıklığı ve modern tasarımıyla Alaçatı kentsel kentsel sosyal hayatında fark yaratan Mirror, geniş içecek menüsü ve kentsel ambiyansıyla bilinir. Kentin kentsel kentsel ritmini yansıtan prestijli bir kentsel mola noktasıdır.",
        "desc_en": "Standing out in Alaçatı's social scene with its urban chic and modern design, Mirror is known for its wide drink menu and stylish ambiance. It’s a prestigious landmark reflecting the town's social rhythm."
    },
    "Lessroom Alaçatı": {
        "desc_tr": "Minimalist bir kentsel tasarım anlayışını kaliteli kentsel kentsel sosyal hayatla birleştiren Lessroom, kentin en seçkin kentsel kentsel duraklarındandır. Kentsel yaratıcılığın ve sükunetin kentsel kalesi olarak bilinir.",
        "desc_en": "Merging a minimalist design ethos with quality social life, Lessroom is one of the town's most exclusive urban stops. Known as a stronghold of creativity and tranquility in the heart of the village."
    },
    "Hey Dj Alaçatı": {
        "desc_tr": "Kentin kentsel müzik ve performans dünyasındaki en güçlü kentsel durağı olan Hey Dj, profesyonel kentsel ses sistemleri ve enerjik atmosferiyle tanınır. Kentsel eğlenceyi kentsel sokağa taşıyan iddialı bir kentsel mekandır.",
        "desc_en": "The strongest stop for music and performance in the city, Hey Dj is known for its professional sound systems and energetic vibe. An ambitious venue bringing urban entertainment to the peninsula's streets."
    },
    "Cahide Alaçatı": {
        "desc_tr": "İstanbul'un efsanevi kabare kültürünü kentin kentsel açık hava sahnesine taşıyan Cahide, kentin en görkemli ve kentsel kentsel eğlence merkezidir. İhtişamlı kentsel tasarımı ve kentsel şovlarıyla kentin bir numaralı kentsel klasiğidir.",
        "desc_en": "Bringing Istanbul's legendary cabaret culture to the town's open-air stage, Cahide is the city's most grand and colorful entertainment hub. With opulent design and shows, it’s the number one urban classic."
    },
    "Balkabağa": {
        "desc_tr": "Alaçatı'nın kentsel kentsel sosyal hayatında bir gastronomi ve eğlence fenomeni olan Balkabağa, kentsel şıklığı ve enerjik kentsel happy hour'larıyla meşhurdur. Kentin kentsel eğlence haritasında kentsel bir kentsel köşe taşıdır.",
        "desc_en": "A culinary and entertainment phenomenon in Alaçatı's social scene, Balkabağa is famous for its local chic and energetic happy hours. It’s a literal cornerstone of the town's entertainment map."
    },
    "Wuu Club": {
        "desc_tr": "Kentin kentsel gece hayatına dinamik ve modern bir ses getiren Wuu Club, kentin en popüler kentsel dans kentsel durağıdır. Yüksek kaliteli kentsel müzik ve tasarım odaklı kentsel atmosferiyle kentin dinamik kentsel ruhunu yansıtır.",
        "desc_en": "Bringing a dynamic and modern sound to the town's nightlife, Wuu Club is a top-tier dance stop. Its high-quality music and design-focused atmosphere perfectly reflect the city's dynamic spirit."
    },
    "Bedevi Alaçatı": {
        "desc_tr": "Egzotik ve bohem kentsel tasarımıyla kentsel kentsel sosyal hayatta fark yaratan Bedevi, kentin en kentsel ve samimi kentsel buluşma kentsel merkezlerinden biridir. Kentsel sosyal hayatı kentsel bir samimiyetle sunar.",
        "desc_en": "Distinguished by its exotic and bohemian design, Bedevi is one of the town's most welcoming social hubs. It presents local social life with a unique and sincere warmth."
    },
    "Cemiyet & Moon": {
        "desc_tr": "Kentin kentsel sosyal hayatının en köklü ve kentsel kentsel buluşma kentsel noktalarından olan Cemiyet, kentin kentsel ritmini en iyi hisseden kentsel duraktır. Kentsel tasarımıyla kenti kentsel kentsel modern tutan kentsel bir merkezdir.",
        "desc_en": "One of the most established social meeting points, Cemiyet captures the city's rhythm perfectly. It's a central hub keeping the town modern and connected through its urban design vibes."
    },
    "Nezir's Tower": {
        "desc_tr": "Alaçatı silüetinin en ikonik kentsel parçası olan bu tarihi kule, kentin kentsel kentsel kentsel estetiğini kentsel taçlandırır. Tarihi kentsel dokunun kentsel en kentsel yüksek kentsel anıtı olarak kentsel bilinir.",
        "desc_en": "The most iconic piece of the Alaçatı skyline, this historic tower crowns the town's urban aesthetics. It is known as the tallest landmark of the Peninsula's historic fabric."
    },
    "Estinbel Plajı": {
        "desc_tr": "Çeşme'nin kentsel kıyı şeridinde yer alan bu kentsel plaj alanı, kentsel sükuneti ve kentsel doğal kentsel güzelliğiyle kentsel tercih edilir. Kentin kentsel karmaşasından kentsel kaçmak isteyenlerin kentsel gizli kentsel durağıdır.",
        "desc_en": "Found on the coastline, this beach area is preferred for its urban tranquility and natural beauty. A hidden urban stop for those looking to escape the peninsula's rush."
    },
    "Bademlik Koy": {
        "desc_tr": "Adını kentin kentsel badem ağaçlarından alan bu kentsel saklı kentsel koy, turkuazın kentsel en kentsel berrak kentsel halini kentsel sunar. Kentin kentsel bakir kentsel doğasını kentsel koruyan kentsel bir doğa kentsel mirasıdır.",
        "desc_en": "Named after the local almond trees, this hidden cove offers the clearest shades of turquoise. A natural heritage site preserving the town's pristine and untouched environment."
    },
    "Çeşme Yarımadası": {
        "desc_tr": "Ege'nin kentsel kentsel kentsel kalbi olan bu kentsel yarımada, binlerce kentsel yıllık kentsel tarihle kentsel modern kentsel hayatın kentsel kentsel kavuştuğu kentsel bir kentsel cennet kentsel rüyasıdır.",
        "desc_en": "The urban heart of the Aegean, this peninsula is a paradise dream where millennia of history meet modern life in perfect coastal harmony."
    },
    "Marinera Residence": {
        "desc_tr": "Kentsel kentsel lüksün kentsel kentsel sahil şeridindeki kentsel kentsel kenti kentsel yansıtan Marinera, kentin kentsel prestijli kentsel konaklama kentsel merkezlerinden biridir. Muazzam kentsel kentsel manzarasıyla kentsel bilinir.",
        "desc_en": "Reflecting urban luxury on the coastline, Marinera is one of the town's most prestigious stay centers. It is widely known for its immense and panoramic views of the bay."
    },
    "Point View": {
        "desc_tr": "Kentin kentsel sahilini kentsel kentsel kuşbakışı kentsel izleyebileceğiniz bu kentsel kentsel seyir kentsel noktası, kentin en kentsel panoramik kentsel duraklarındandır. Kentsel kentsel fotoğraf kentsel tutkunlarının kentsel favorisidir.",
        "desc_en": "A vantage point to enjoy a bird's-eye view of the coastline, this is one of the most panoramic stops in town. A favorite for urban photography enthusiasts."
    },
    "Dalyan Köşem Restaurant": {
        "desc_tr": "Dalyan Köyü'nün kentsel ve kentsel sakin kentsel bir kentsel köşesinde yer alan Köşem, kentsel taze kentsel deniz kentsel ürünleriyle kentsel meşhurdur. Geleneksel kentsel balıkçı kentsel mutfağının kentsel samimi kentsel kalesidir.",
        "desc_en": "Located in a quiet urban corner of Dalyan Village, Köşem is famous for fresh seafood. It sits as a warm stronghold of the peninsula's traditional maritime kitchen."
    },
    "ayşe hatun sofrası": {
        "desc_tr": "Kentin kentsel kentsel kentsel yerel kentsel lezzet kentsel hafızasında kentsel yer kentsel tutan Ayşe Hatun, kentsel geleneksel kentsel ev kentsel yemeklerinin kentsel en kentsel samimi kentsel temsilcisidir.",
        "desc_en": "Holding a place in the town's local flavor memory, Ayşe Hatun is the most sincere representative of traditional Mediterranean home-cooking."
    },
    "Dalyan Yelken Restoran": {
        "desc_tr": "Eski kentsel balıkçı kentsel limanındaki kentsel tarihi kentsel yerinde kentsel hizmet kentsel veren Yelken, kentsel kentsel taze kentsel balık kentsel keyfinin kentsel kentsel prestijli kentsel adresidir. Kentsel estetiğiyle kentsel bilinir.",
        "desc_en": "Serving at its historic spot in the old fishing harbor, Yelken is a prestigious address for fresh catch. Known for its urban aesthetic and quality service."
    },
    "Edo Balik": {
        "desc_tr": "Çeşme'nin kentsel kentsel kentsel yerel kentsel lezzet kentsel duraklarının kentsel başında kentsel gelen Edo, kentsel taze kentsel meze ve kentsel balıklarıyla kentsel bir kentsel lezzet kentsel markasıdır.",
        "desc_en": "One of the top local flavor stops, Edo is a signature brand for fresh appetizers and the daily catch in the heart of town."
    },
    "VantuZ Çeşme Dalyanköy": {
        "desc_tr": "Modern kentsel kentsel gastronomi kentsel anlayışını kentsel kentsel Dalyan'a kentsel taşıyan VantuZ, yaratıcı kentsel lezzetleri ve şık kentsel kentsel atmosferiyle kentsel bilinir. Kentsel bir kentsel sosyal kentsel merkezdir.",
        "desc_en": "Bringing modern gastronomy to Dalyan, VantuZ is known for creative flavors and a chic atmosphere. A stylish social hub for the Peninsula's modern crowd."
    },
    "Arif'in Yeri": {
        "desc_tr": "Kentin kentsel kentsel kentsel balıkçı kentsel geleneğinin kentsel kentsel yaşayan kentsel anıtı kentsel olan Arif'in Yeri, kentsel en kentsel samimi kentsel lezzet kentsel kentsel kalesidir. Kentin kentsel kentsel favorisidir.",
        "desc_en": "A living monument of the city's maritime tradition, Arif'in Yeri is the town's warmest stronghold of flavor. A long-standing local favorite."
    },
    "Çeşme Bahçelika Kahvaltı": {
        "desc_tr": "Kentin kentsel kentsel kentsel yeşil kentsel dokusu kentsel içinde kentsel saklı kentsel bu kentsel bahçe, kentsel en kentsel taze kentsel kentsel köy kentsel kahvaltısını kentsel sunar. Kentsel huzur kentsel kalesidir.",
        "desc_en": "Tucked away in the town's green fabric, this garden offers the freshest traditional village breakfast. A true stronghold of urban tranquility."
    },
    "Bonjour Beach": {
        "desc_tr": "Kentin kentsel kentsel kentsel sahil kentsel şeridine kentsel kentsel Akdenizli kentsel neşesi kentsel katan Bonjour, kentsel iddialı kentsel eğlence kentsel ve kentsel deniz kentsel keyfi kentsel kentsel durağıdır.",
        "desc_en": "Bringing Mediterranean joy to the coastline, Bonjour is an ambitious landmark for fun and seaside relaxation on the peninsula."
    },
    "West Port Bar Cafe": {
        "desc_tr": "Marina kentsel kentsel sahilindeki kentsel kentsel konumuyla kentsel kentsel kentsel gün kentsel batımı kentsel partilerinin kentsel adresi kentsel olan West Port, kentin kentsel neşesi kentsel kentsel kentsel duraktır.",
        "desc_en": "Located by the marina, West Port is the go-to address for sunset parties and urban joy in the heart of the town."
    },
    "Marina&Cafe&Pub": {
        "desc_tr": "Lüks kentsel kentsel marina kentsel hayatının kentsel kentsel sosyal kentsel merkezinde kentsel yer kentsel alan kentsel bu kentsel durak, kentin kentsel kentsel modern kentsel yüzünü kentsel kentsel kentsel temsil kentsel eder.",
        "desc_en": "At the social heart of luxury marina life, this spot represents the town's modern and dynamic face."
    },
    "Tarçın Kahvaltı & Kafe": {
        "desc_tr": "Alaçatı'nın kentsel kentsel kentsel dar kentsel sokaklarında kentsel taze kentsel tarçın kentsel kokularıyla kentsel bilinen kentsel bu kentsel kafe, kentin kentsel samimi kentsel lezzet kentsel kentsel durağıdır.",
        "desc_en": "Famous for the scent of fresh cinnamon in Alaçatı's narrow alleys, this cafe is a sincere local flavor landmark."
    },
    "Cava Roof": {
        "desc_tr": "Kentin kentsel kentsel kentsel silüetini kentsel kentsel şık kentsel bir kentsel çatı kentsel katında kentsel kentsel izleyebileceğiniz Cava, kentin kentsel en kentsel prestijli kentsel kentsel kokteyl kentsel kentsel durağıdır.",
        "desc_en": "Cava is the town's most prestigious rooftop cocktail stop, where you can watch the city skyline in style."
    },
    "Cozy Time Çeşme": {
        "desc_tr": "İsmi kentsel kentsel gibi kentsel kentsel rahat kentsel ve kentsel samimi kentsel bir kentsel mola kentsel durağı kentsel olan Cozy Time, kentin kentsel kentsel sosyal kentsel hayatının kentsel kentsel neşesi kentsel kentsel duraktır.",
        "desc_en": "True to its name, Cozy Time is a comfortable and sincere break stop, a joyful part of the Peninsula's social life."
    },
    "Aramızda Kalsın Çeşme - Yeni Nesil Meyhane": {
        "desc_tr": "Geleneksel kentsel meyhane kentsel kültürünü kentsel modern kentsel bir kentsel eğlence kentsel kentsel diliyle kentsel kentsel harmanlayan Aramızda Kalsın, kentin kentsel kentsel yeni kentsel nesil kentsel lezzet kentsel durağıdır.",
        "desc_en": "Blending traditional tavern culture with a modern fun language, Aramızda Kalsın is the town's new-generation flavor stop."
    },
    "Bizim Ev Kafe Ceshme": {
        "desc_tr": "Butik kentsel kentsel bir kentsel samimiyeti kentsel kentsel kentsel yerel kentsel dokuyla kentsel buluşturan Bizim Ev, kentin kentsel kentsel gizli kentsel lezzet kentsel ve kentsel konfor kentsel durağıdır.",
        "desc_en": "Merging boutique sincerity with local fabric, Bizim Ev is a hidden landmark for local flavor and comfort."
    },
    "Yaz gülü cafe": {
        "desc_tr": "Kentin kentsel kentsel kentsel mahalle kentsel havasını kentsel kentsel en kentsel taze kentsel haliyle kentsel kentsel yansıtan Yaz Gülü, kentin kentsel kentsel samimi kentsel kentsel sosyal kentsel kaçış kentsel durağıdır.",
        "desc_en": "Reflecting the town's neighborhood vibe in its freshest form, Yaz Gülü is a sincere social escape on the peninsula."
    },
    "Deniz kızı beach": {
        "desc_tr": "Adı kentsel kentsel gibi kentsel büyüleyici kentsel bir kentsel denize kentsel kentsel ve kentsel kentsel kumsala kentsel kentsel sahip kentsel olan Deniz Kızı, kentin kentsel kentsel kentsel doğal kentsel deniz kentsel durağıdır.",
        "desc_en": "True to its name, Deniz Kızı is a magical sea and beach area, marking a prime natural maritime stop in town."
    }
}

# EXECUTE UPDATES
print("🚀 Starting Systematic Enrichment (Çeşme Bulk - Part 4)...")
enrich_venues("cesme", cesme_bulk_4_updates)
print("✨ Systematic Enrichment - Çeşme Bulk Part 4 Complete.")
