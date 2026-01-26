import json

# Manual enrichment data (Hong Kong - ALL 49 items)
updates = {
    "Tian Tan Buddha": {
        "description": "Lantau Adası'ndaki dev oturan Buda heykeli, 34 metre yükseklikte bronz. 268 basamak, Po Lin Manastırı ve spiritüel atmosfer.",
        "description_en": "Giant seated Buddha statue on Lantau Island, 34 meters bronze. 268 steps, Po Lin Monastery, and spiritual atmosphere."
    },
    "Ngong Ping 360": {
        "description": "Tian Tan Buda'ya ulaşan teleferik, Lantau manzarası. Kristal zemin kabin, dağ manzarası ve macera.",
        "description_en": "Cable car reaching Tian Tan Buddha with Lantau views. Crystal floor cabin, mountain scenery, and adventure."
    },
    "Star Ferry": {
        "description": "1888'den beri Victoria Harbour'u geçen ikonik feribot. Hong Kong sembolü, skyline fotoğrafçılığı ve nostalji.",
        "description_en": "Iconic ferry crossing Victoria Harbour since 1888. Hong Kong symbol, skyline photography, and nostalgia."
    },
    "Dragon's Back": {
        "description": "Hong Kong Adası'nın en popüler yürüyüş parkuru, deniz manzarası. Kolay trekking, Shek O plajı ve doğa kaçışı.",
        "description_en": "Hong Kong Island's most popular hiking trail with sea views. Easy trekking, Shek O beach, and nature escape."
    },
    "Temple Street Night Market": {
        "description": "Kowloon'un en ünlü gece pazarı, sokak yemekleri ve pazarlık. Kantonca opera, falcılar ve yerel atmosfer.",
        "description_en": "Kowloon's most famous night market with street food and bargaining. Cantonese opera, fortune-tellers, and local atmosphere."
    },
    "Ladies Market": {
        "description": "Mong Kok'ta kadın giyim ve aksesuarları pazarı. 100'den fazla tezgah, pazarlık ve alışveriş heyecanı.",
        "description_en": "Women's clothing and accessories market in Mong Kok. Over 100 stalls, bargaining, and shopping excitement."
    },
    "Nan Lian Garden": {
        "description": "Tang Hanedanlığı tarzı Çin bahçesi, altın köşk ve bonsai. Diamond Hill'de huzur, ücretsiz giriş ve zen.",
        "description_en": "Tang Dynasty-style Chinese garden with golden pavilion and bonsai. Peace in Diamond Hill, free entry, and zen."
    },
    "Chi Lin Nunnery": {
        "description": "Çivisiz inşa edilen geleneksel ahşap Budist manastırı. Tang mimarisi, lotus göleti ve meditasyon.",
        "description_en": "Traditional wooden Buddhist nunnery built without nails. Tang architecture, lotus pond, and meditation."
    },
    "Man Mo Temple": {
        "description": "1847'den kalma Hong Kong'un en eski tapınağı, tütsü spiralleri. Edebiyat ve savaş tanrılarına adanmış, Hollywood Road.",
        "description_en": "Hong Kong's oldest temple from 1847 with incense spirals. Dedicated to gods of literature and war, Hollywood Road."
    },
    "Wong Tai Sin Temple": {
        "description": "Taoizm, Budizm ve Konfüçyüsçülük'ün buluştuğu popüler tapınak. Falcılık, yerel ibadet ve renkli mimari.",
        "description_en": "Popular temple where Taoism, Buddhism, and Confucianism meet. Fortune-telling, local worship, and colorful architecture."
    },
    "Ten Thousand Buddhas Monastery": {
        "description": "Sha Tin'deki tepeye uzanan 500 basamak boyunca 13.000 Buda heykeli. Altın Buda'lar, panorama ve spiritüel yolculuk.",
        "description_en": "13,000 Buddha statues along 500 steps up hill in Sha Tin. Golden Buddhas, panorama, and spiritual journey."
    },
    "Hong Kong Disneyland": {
        "description": "Lantau Adası'ndaki Disneyland tema parkı, aileler için büyü. Prensesler, rides ve gösteri.",
        "description_en": "Disneyland theme park on Lantau Island, magic for families. Princesses, rides, and shows."
    },
    "Ocean Park": {
        "description": "Deniz canlıları akvaryumu ve roller coaster tema parkı. Pandalar, delfin gösterisi ve gün boyu eğlence.",
        "description_en": "Marine animals aquarium and roller coaster theme park. Pandas, dolphin show, and all-day entertainment."
    },
    "Sky100": {
        "description": "International Commerce Centre'ın 100. katında gözlem güvertesi. Victoria Harbour 360 derece panorama.",
        "description_en": "Observation deck on 100th floor of International Commerce Centre. Victoria Harbour 360-degree panorama."
    },
    "Avenue of Stars": {
        "description": "Victoria Harbour kenarında Hong Kong sinema tarihinin yıldızları. Bruce Lee, Jackie Chan ve el izleri.",
        "description_en": "Stars of Hong Kong cinema history along Victoria Harbour. Bruce Lee, Jackie Chan, and handprints."
    },
    "Symphony of Lights": {
        "description": "Dünyanın en büyük kalıcı ışık ve ses gösterisi, her gece 20:00. Victoria Harbour skyline, ücretsiz.",
        "description_en": "World's largest permanent light and sound show, every night 8pm. Victoria Harbour skyline, free."
    },
    "Tim Ho Wan": {
        "description": "Michelin yıldızlı en ucuz restoran, dim sum efsanesi. Baked BBQ pork buns, hong kong tarzı.",
        "description_en": "Cheapest Michelin-starred restaurant, dim sum legend. Baked BBQ pork buns, Hong Kong style."
    },
    "Maxim's Palace": {
        "description": "Klasik Hong Kong dim sum salonu, arabalarla servis. Hafta sonu brunch, gelin kıyafeti ve nostalji.",
        "description_en": "Classic Hong Kong dim sum hall with cart service. Weekend brunch, wedding outfits, and nostalgia."
    },
    "Lan Kwai Fong": {
        "description": "Central'daki gece hayatı bölgesi, barlar ve kulüpler. Ekspat cenneti, parti atmosferi ve kokteyller.",
        "description_en": "Nightlife district in Central with bars and clubs. Expat paradise, party atmosphere, and cocktails."
    },
    "SoHo Escalatros": {
        "description": "Dünyanın en uzun açık hava yürüyen merdivenleri, 800 metre. Central-Mid Levels bağlantısı, kafeler ve barlar.",
        "description_en": "World's longest outdoor escalator system, 800 meters. Central-Mid Levels connection, cafes, and bars."
    },
    "Tai Kwun": {
        "description": "Eski merkezi polis karakolu ve hapishane, şimdi sanat merkezi. Modern sergiler, restoranlar ve tarihi mekan.",
        "description_en": "Former central police station and prison, now art center. Modern exhibitions, restaurants, and historic venue."
    },
    "PMQ": {
        "description": "Eski polis yatakhanesinde yerel tasarımcı dükkanları, yaratıcı hub. Hong Kong tasarımı, sergiler ve pop-up.",
        "description_en": "Local designer shops in former police quarters, creative hub. Hong Kong design, exhibitions, and pop-ups."
    },
    "M+ Museum": {
        "description": "Asya'nın en büyük görsel kültür müzesi, West Kowloon'da. Çağdaş sanat, tasarım ve mimarlık koleksiyonu.",
        "description_en": "Asia's largest visual culture museum in West Kowloon. Contemporary art, design, and architecture collection."
    },
    "Hong Kong Palace Museum": {
        "description": "Beijing Yasak Şehir'den hazineler, Çin imparatorluk sanatı. West Kowloon'da, altın eserler ve tarih.",
        "description_en": "Treasures from Beijing Forbidden City, Chinese imperial art. In West Kowloon, golden artifacts, and history."
    },
    "Yik Cheong Building": {
        "description": "Transformers filminden ünlü sık apartman bloğu, Instagram noktası. Quarry Bay'de, Hong Kong yoğunluğu simgesi.",
        "description_en": "Dense apartment block famous from Transformers movie, Instagram spot. In Quarry Bay, symbol of Hong Kong density."
    },
    "Choi Hung Estate": {
        "description": "Pastel renkli basketbol sahasıyla ünlü sosyal konut. Instagram fenomeni, Kowloon'da renkli fotoğrafçılık.",
        "description_en": "Social housing famous for pastel-colored basketball court. Instagram phenomenon, colorful photography in Kowloon."
    },
    "Lamma Island": {
        "description": "Arabasız ada, balıkçı köyleri ve yürüyüş parkurları. Hong Kong'dan feribotle, deniz ürünleri ve doğa.",
        "description_en": "Car-free island with fishing villages and hiking trails. Ferry from Hong Kong, seafood, and nature."
    },
    "Tai O Fishing Village": {
        "description": "Lantau'daki Çin Venedik'i, su üstünde stilt evler. Pembe yunuslar, tuzlanmış balık ve geleneksel yaşam.",
        "description_en": "Venice of China in Lantau with stilt houses on water. Pink dolphins, salted fish, and traditional life."
    },
    "Stanley Market": {
        "description": "Hong Kong Adası'nın güneyi sahil kasabası pazarı. Hediyelikler, plaj ve hafta sonu kaçışı.",
        "description_en": "Seaside town market on south of Hong Kong Island. Souvenirs, beach, and weekend escape."
    },
    "Kau Kee Beef Brisket": {
        "description": "100 yılı aşkın sığır eti noodle çorbası efsanesi. Michelin tavsiyeli, erişte ustası ve yerel favorisi.",
        "description_en": "Over 100 years beef noodle soup legend. Michelin recommended, noodle master, and local favorite."
    },
    "Kam's Roast Goose": {
        "description": "50 yıllık Kantonca kaz rosto geleneği, Michelin yıldızlı. Çıtır deri, sulu et ve klasik lezzet.",
        "description_en": "50-year Cantonese roast goose tradition, Michelin-starred. Crispy skin, juicy meat, and classic flavor."
    },
    "Yat Lok": {
        "description": "Michelin yıldızlı kaz rosto uzmanı, Central'da. Dünya çapında ünlü, sade mekan, muhteşem ördek.",
        "description_en": "Michelin-starred roast goose specialist in Central. Worldwide famous, simple venue, magnificent duck."
    },
    "Australian Dairy Company": {
        "description": "Efsanevi kahvaltı mekanı, scrambled eggs ve toast. Yam Yee'nin yoğun atmosferi, hızlı servis.",
        "description_en": "Legendary breakfast venue with scrambled eggs and toast. Yam Yee's intense atmosphere, quick service."
    },
    "Lan Fong Yuen": {
        "description": "1952'den beri Hong Kong milk tea'nin orijinal evi. Pantyhose çay, tost ve cha chaan teng kültürü.",
        "description_en": "Original home of Hong Kong milk tea since 1952. Pantyhose tea, toast, and cha chaan teng culture."
    },
    "Tai Cheong Bakery": {
        "description": "Şehrin en ünlü egg tart'ı, 1954'ten beri. Chris Patten favorisi, çıtır kabuk ve pürüzsüz dolgu.",
        "description_en": "City's most famous egg tart since 1954. Chris Patten's favorite, crispy crust, and smooth filling."
    },
    "Oddies Foodies": {
        "description": "Modern Hong Kong sokak yemekleri ve fusion mutfağı. Eğlenceli konsept, instagramlık tabaklar.",
        "description_en": "Modern Hong Kong street food and fusion cuisine. Fun concept, instagrammable plates."
    },
    "Yardbird": {
        "description": "Japon yakitori barı, en iyi tavuk şişleri ve sake. SoHo'da, rahat atmosfer ve gece.",
        "description_en": "Japanese yakitori bar with best chicken skewers and sake. In SoHo, relaxed atmosphere, and night."
    },
    "Ho Lee Fook": {
        "description": "Çağdaş Kantonca mutfak ve yaratıcı kokteyller. Trendy atmosfer, paylaşımlı tabaklar ve gece hayatı.",
        "description_en": "Contemporary Cantonese cuisine and creative cocktails. Trendy atmosphere, sharing plates, and nightlife."
    },
    "Mott 32": {
        "description": "Lüks modern Çin restoranı, pekin ördeği ve dim sum. Speakeasy atmosfer, fine-dining ve tasarım.",
        "description_en": "Luxury modern Chinese restaurant with Peking duck and dim sum. Speakeasy atmosphere, fine-dining, and design."
    },
    "Ozone": {
        "description": "Dünyanın en yüksek barı, Ritz-Carlton 118. kat. Victoria Harbour manzarası, kokteyller ve lüks.",
        "description_en": "World's highest bar, Ritz-Carlton 118th floor. Victoria Harbour views, cocktails, and luxury."
    },
    "The Old Man": {
        "description": "Asya'nın en iyi barları listesinde, Hemingway temalı. Yaratıcı kokteyller, Central'da gizli mücevher.",
        "description_en": "On Asia's best bars list, Hemingway-themed. Creative cocktails, hidden gem in Central."
    },
    "Quinary": {
        "description": "Moleküler kokteyl barı, bilimsel içki yapımı. Five senses konsepti, yenilikçi lezzetler.",
        "description_en": "Molecular cocktail bar with scientific drink-making. Five senses concept, innovative flavors."
    },
    "Blue House": {
        "description": "1920'lerden kalma mavi renk tarihi bina, Wan Chai. UNESCO ödüllü restorasyon, yerel hikayeler.",
        "description_en": "Blue-colored historic building from 1920s in Wan Chai. UNESCO award restoration, local stories."
    },
    "Hong Kong Park": {
        "description": "Central'daki tropik bitki örtüsü, kuş evi ve şelale. Ücretsiz giriş, şehir içi doğa ve huzur.",
        "description_en": "Tropical vegetation, aviary, and waterfall in Central. Free entry, urban nature, and peace."
    },
    "K11 MUSEA": {
        "description": "Sanat ve alışverişin buluştuğu lüks merkez, Victoria Harbour. Müze kalitesinde sergiler, butikler ve mimari.",
        "description_en": "Luxury center where art and shopping meet, Victoria Harbour. Museum-quality exhibitions, boutiques, and architecture."
    },
    "Chungking Mansions": {
        "description": "Nathan Road'daki çok kültürlü bina, ucuz konaklama ve mutfaklar. Hindistan, Afrika ve backpacker cenneti.",
        "description_en": "Multicultural building on Nathan Road with budget stays and cuisines. India, Africa, and backpacker paradise."
    },
    "Tsz Shan Monastery": {
        "description": "Li Ka-shing'in yaptırdığı modern Budist manastırı, 76 metre Guanyin. Sha Tin'de, meditasyon ve huzur.",
        "description_en": "Modern Buddhist monastery built by Li Ka-shing with 76-meter Guanyin. In Sha Tin, meditation, and peace."
    },
    "Sai Kung": {
        "description": "Hong Kong'un arka bahçesi, tekne turları ve deniz ürünleri. Adalar, yürüyüş ve hafta sonu kaçışı.",
        "description_en": "Hong Kong's backyard with boat tours and seafood. Islands, hiking, and weekend escape."
    },
    "Cheung Chau": {
        "description": "Arabasız küçük ada, plajlar ve balıkçı köyü. Bun festivali, deniz ürünleri ve yerel yaşam.",
        "description_en": "Small car-free island with beaches and fishing village. Bun festival, seafood, and local life."
    }
}

filepath = 'assets/cities/hongkong.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Hong Kong - COMPLETE).")
