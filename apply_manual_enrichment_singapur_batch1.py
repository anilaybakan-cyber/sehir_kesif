import json

# Manual enrichment data (Singapore - ALL 51 items)
updates = {
    "Gardens by the Bay": {
        "description": "Marina Bay'deki futuristik botanik bahçeleri, Supertree Grove ve dome yapıları. Gece ışık gösterisi, bulut ormanı ve orkide bahçesi.",
        "description_en": "Futuristic botanical gardens in Marina Bay with Supertree Grove and dome structures. Night light show, cloud forest, and orchid garden."
    },
    "Marina Bay Sands": {
        "description": "Singapur'un ikonik gökdelen kompleksi, çatıdaki sonsuzluk havuzu. SkyPark, kumarhane, lüks alışveriş ve dünya çapında ünlü manzara.",
        "description_en": "Singapore's iconic skyscraper complex with rooftop infinity pool. SkyPark, casino, luxury shopping, and world-famous view."
    },
    "Cloud Forest": {
        "description": "Gardens by the Bay'deki yapay dağ ve şelale dome'u. Nadir bitkiler, 35 metre yükseklik ve tropikal mikroiklim.",
        "description_en": "Artificial mountain and waterfall dome at Gardens by the Bay. Rare plants, 35-meter height, and tropical microclimate."
    },
    "Singapore Botanic Gardens": {
        "description": "UNESCO korumasındaki 160 yıllık botanik bahçesi, orkide koleksiyonu dünyada en zengin. National Orchid Garden ve tropik yeşillik.",
        "description_en": "UNESCO-protected 160-year-old botanical garden with world's richest orchid collection. National Orchid Garden and tropical greenery."
    },
    "Sentosa Island": {
        "description": "Singapur'un eğlence ve tatil adası, plajlar, tema parkları ve resort. Golftan Universal Studios'a her şey bir arada.",
        "description_en": "Singapore's entertainment and resort island with beaches, theme parks, and resorts. Everything from golf to Universal Studios in one place."
    },
    "Universal Studios Singapore": {
        "description": "Güneydoğu Asya'nın tek Universal tema parkı, Hollywood filmleri temalı alanlar. Roller coaster, gösteri ve aileler için eğlence.",
        "description_en": "Southeast Asia's only Universal theme park with Hollywood movie-themed areas. Roller coasters, shows, and family entertainment."
    },
    "S.E.A. Aquarium": {
        "description": "Dünyanın en büyük akvaryumlarından biri, 100.000'den fazla deniz canlısı. Okyanus panorama penceresi, köpekbalıkları ve aileler için ideal.",
        "description_en": "One of world's largest aquariums with over 100,000 marine animals. Ocean panorama window, sharks, and ideal for families."
    },
    "Singapore Zoo": {
        "description": "Kafessiz konseptiyle ünlü tropikal hayvanat bahçesi. Kahvaltıda orangutan, gece safarisi ve doğal habitat.",
        "description_en": "Tropical zoo famous for cage-free concept. Breakfast with orangutans, night safari, and natural habitat."
    },
    "Night Safari": {
        "description": "Dünyanın ilk gece temalı yaban hayatı parkı, gece hayvanları ve tramvay turu. Benzersiz deneyim, yırtıcılar ve tropik gece.",
        "description_en": "World's first night-themed wildlife park with nocturnal animals and tram tour. Unique experience, predators, and tropical night."
    },
    "Chinatown": {
        "description": "Singapur'un renkli Çin mahallesi, tapınaklar, sokak yemekleri ve hediyelik dükkanlar. Buddha Tooth Relic Temple ve kültürel miras.",
        "description_en": "Singapore's colorful Chinatown with temples, street food, and souvenir shops. Buddha Tooth Relic Temple and cultural heritage."
    },
    "Little India": {
        "description": "Renkli Hint mahallesi, baharatlar, sari dükkanları ve Hindu tapınakları. Otantik Hint yemekleri, henna ve kültürel zenginlik.",
        "description_en": "Colorful Indian neighborhood with spices, sari shops, and Hindu temples. Authentic Indian food, henna, and cultural richness."
    },
    "Kampong Glam": {
        "description": "Tarihi Malay mahallesi, Sultan Camii ve sanat sokakları. Haji Lane butikleri, hipster kafeler ve Arap Caddesi.",
        "description_en": "Historic Malay neighborhood with Sultan Mosque and art streets. Haji Lane boutiques, hipster cafes, and Arab Street."
    },
    "Haji Lane": {
        "description": "Singapur'un en dar sokağı, vintage butikler ve sokak sanatı. Indie modası, özgün tasarımlar ve genç kültürü.",
        "description_en": "Singapore's narrowest street with vintage boutiques and street art. Indie fashion, unique designs, and youth culture."
    },
    "Merlion Park": {
        "description": "Singapur'un sembolü aslan balık heykeli, Marina Bay manzarası. Fotoğraf noktası, fıskiye ve şehrin ikonik simgesi.",
        "description_en": "Singapore's symbol lion-fish statue with Marina Bay views. Photo point, fountain, and city's iconic symbol."
    },
    "Singapore Flyer": {
        "description": "Asya'nın en büyük dönme dolabı, 165 metre yükseklikte şehir panoraması. Gün batımı, romantik deneyim ve skyline.",
        "description_en": "Asia's largest observation wheel with city panorama at 165 meters. Sunset, romantic experience, and skyline."
    },
    "ArtScience Museum": {
        "description": "Marina Bay Sands'teki lotus şekilli müze, sanat ve bilim sergileri. teamLab, interaktif sergiler ve çağdaş sanat.",
        "description_en": "Lotus-shaped museum at Marina Bay Sands with art and science exhibitions. teamLab, interactive exhibits, and contemporary art."
    },
    "National Museum of Singapore": {
        "description": "Singapur'un en eski müzesi, ülke tarihini ve kültürünü anlatıyor. Koloniyal dönem, bağımsızlık ve çok kültürlülük.",
        "description_en": "Singapore's oldest museum telling country's history and culture. Colonial period, independence, and multiculturalism."
    },
    "National Gallery Singapore": {
        "description": "Güneydoğu Asya sanatının en kapsamlı koleksiyonu, eski Yargıtay ve Belediye binalarında. Modern Asyalı ustalar.",
        "description_en": "Most comprehensive collection of Southeast Asian art in old Supreme Court and City Hall buildings. Modern Asian masters."
    },
    "Buddha Tooth Relic Temple": {
        "description": "Chinatown'daki muhteşem Çin Budist tapınağı, Buda'nın diş emiğini barındırıyor. Tang Hanedanlığı mimarisi ve dini sanat.",
        "description_en": "Magnificent Chinese Buddhist temple in Chinatown housing Buddha's tooth relic. Tang Dynasty architecture and religious art."
    },
    "Maxwell Food Centre": {
        "description": "Singapur'un en ünlü hawker merkezi, Michelin yıldızlı Tian Tian'ın evi. Hainanese chicken rice ve sokak yemekleri.",
        "description_en": "Singapore's most famous hawker center, home of Michelin-starred Tian Tian. Hainanese chicken rice and street food."
    },
    "Lau Pa Sat": {
        "description": "Victoria dönemi demir işi mimarisiyle tarihi hawker merkezi. Akşam satay sokağı, CBD'de öğle yemeği ve gece hayatı.",
        "description_en": "Historic hawker center with Victorian-era ironwork architecture. Evening satay street, CBD lunch, and nightlife."
    },
    "Newton Food Centre": {
        "description": "Crazy Rich Asians'ta görülen ünlü hawker merkezi. Istakoz, satay ve gece sokak yemekleri deneyimi.",
        "description_en": "Famous hawker center featured in Crazy Rich Asians. Lobster, satay, and night street food experience."
    },
    "Orchard Road": {
        "description": "Singapur'un ana alışveriş caddesi, dev alışveriş merkezleri ve lüks butikler. Moda, gastronomi ve gece ışıkları.",
        "description_en": "Singapore's main shopping street with giant malls and luxury boutiques. Fashion, gastronomy, and night lights."
    },
    "Clarke Quay": {
        "description": "Singapur Nehri kıyısında renkli gece hayatı ve yeme-içme bölgesi. Barlar, restoranlar ve nehir kruvazierleri.",
        "description_en": "Colorful nightlife and dining area along Singapore River. Bars, restaurants, and river cruises."
    },
    "Raffles Hotel": {
        "description": "1887'den beri hizmet veren efsanevi koloniyal otel, Singapore Sling'in doğum yeri. Tarihi lüks, Long Bar ve nostalji.",
        "description_en": "Legendary colonial hotel serving since 1887, birthplace of Singapore Sling. Historic luxury, Long Bar, and nostalgia."
    },
    "Long Bar": {
        "description": "Raffles Hotel'deki efsanevi bar, Singapore Sling'in orijinal evi. Fıstık kabukları yere atılır, koloniyal atmosfer.",
        "description_en": "Legendary bar at Raffles Hotel, original home of Singapore Sling. Peanut shells on floor, colonial atmosphere."
    },
    "Atlas Bar": {
        "description": "Art deco cennetinde dünyanın en büyük cin koleksiyonu. 1920'ler Gatsby atmosferi, kokteyller ve lüks.",
        "description_en": "World's largest gin collection in art deco paradise. 1920s Gatsby atmosphere, cocktails, and luxury."
    },
    "Tiong Bahru": {
        "description": "Singapur'un en hipster mahallesi, vintage dükkanlar ve specialty kahveciler. Art deco binalar, brunch ve sokak sanatı.",
        "description_en": "Singapore's hippest neighborhood with vintage shops and specialty coffee. Art deco buildings, brunch, and street art."
    },
    "Tiong Bahru Bakery": {
        "description": "Fransız tarzı brunch ve kahvaltı, croissant ve pastalar. Hipster kafe kültürü, kahve ve mahalle atmosferi.",
        "description_en": "French-style brunch and breakfast with croissants and pastries. Hipster cafe culture, coffee, and neighborhood atmosphere."
    },
    "PS.Cafe Harding": {
        "description": "Orman içinde gizli kafe-restoran, brunch ve tatlılar. Botanik bahçe yakını, hafta sonu kaçışı ve Instagram mekanı.",
        "description_en": "Hidden cafe-restaurant in forest for brunch and desserts. Near botanical garden, weekend escape, and Instagram spot."
    },
    "Jumbo Seafood": {
        "description": "Singapur'un en ünlü chilli crab restoranı, ikonik yengeç yemeği. Clarke Quay'de nehir manzarası, turistik ve lezzetli.",
        "description_en": "Singapore's most famous chilli crab restaurant with iconic crab dish. River views at Clarke Quay, touristy and delicious."
    },
    "Song Fa Bak Kut Teh": {
        "description": "Michelin Bib Gourmand ödüllü domuz kaburga çorbası. Yerel favorisi, baharatlı et ve geleneksel lezzet.",
        "description_en": "Michelin Bib Gourmand-awarded pork rib soup. Local favorite, spicy meat, and traditional flavor."
    },
    "Tian Tian Chicken Rice": {
        "description": "Michelin yıldızlı en ucuz yemek, Maxwell'deki Hainanese chicken rice efsanesi. Anthony Bourdain favorisi.",
        "description_en": "Cheapest Michelin-starred meal, Hainanese chicken rice legend at Maxwell. Anthony Bourdain's favorite."
    },
    "Haw Par Villa": {
        "description": "Çin mitolojisi temalı tuhaf tema parkı, cehennem dioramaları ve heykeller. Ücretsiz, garip ve benzersiz Singapur.",
        "description_en": "Strange theme park with Chinese mythology theme, hell dioramas, and statues. Free, weird, and unique Singapore."
    },
    "Jewel Changi Airport": {
        "description": "Dünyanın en iyi havalimanındaki iç mekan şelalesi ve alışveriş kompleksi. Rain Vortex, orman, ve transit turizmi.",
        "description_en": "Indoor waterfall and shopping complex at world's best airport. Rain Vortex, forest, and transit tourism."
    },
    "Pulau Ubin": {
        "description": "Singapur'un son kampung adası, bisiklet turları ve doğa. 1960'lar köy yaşamı, vahşi doğa ve şehirden kaçış.",
        "description_en": "Singapore's last kampung island for bike tours and nature. 1960s village life, wildlife, and escape from city."
    },
    "MacRitchie Reservoir": {
        "description": "Ormanda TreeTop Walk asma köprü ve doğa yürüyüşleri. Maymunlar, göl manzarası ve şehir içi orman.",
        "description_en": "TreeTop Walk suspension bridge and nature walks in forest. Monkeys, lake views, and urban forest."
    },
    "Fort Canning Park": {
        "description": "Tarihi tepe parkı, koloniyal kalıntılar ve düğün fotoğrafları. UNESCO kalıntıları, konserler ve yeşil vaha.",
        "description_en": "Historic hill park with colonial remains and wedding photos. UNESCO remains, concerts, and green oasis."
    },
    "Peranakan Museum": {
        "description": "Singapur'un Peranakan (Baba-Nyonya) kültürünü anlatan müze. Çin-Malay karışımı miras, kostümler ve mutfak.",
        "description_en": "Museum telling Singapore's Peranakan (Baba-Nyonya) culture. Chinese-Malay mixed heritage, costumes, and cuisine."
    },
    "Sultan Mosque": {
        "description": "Kampong Glam'deki tarihi cami, altın kubbe ve İslami mimari. Singapur Müslüman topluluğunun merkezi.",
        "description_en": "Historic mosque in Kampong Glam with golden dome and Islamic architecture. Center of Singapore's Muslim community."
    },
    "Sri Mariamman Temple": {
        "description": "Chinatown'daki en eski Hindu tapınağı, renkli gopuram ve Dravidian mimarisi. Dini törenler ve kültürel miras.",
        "description_en": "Oldest Hindu temple in Chinatown with colorful gopuram and Dravidian architecture. Religious ceremonies and cultural heritage."
    },
    "Level33": {
        "description": "Dünyanın en yüksek şehir içi birahanesinde craft bira ve Marina Bay manzarası. Gün batımı, kokteyller ve panorama.",
        "description_en": "Craft beer and Marina Bay views at world's highest urban brewery. Sunset, cocktails, and panorama."
    },
    "Ce La Vi": {
        "description": "Marina Bay Sands tepesindeki bar ve restoran, Singapur skyline'ı. Gece hayatı, kokteyller ve lüks atmosfer.",
        "description_en": "Bar and restaurant atop Marina Bay Sands with Singapore skyline. Nightlife, cocktails, and luxury atmosphere."
    },
    "Potato Head": {
        "description": "Chinatown'daki çok katlı bar ve restoran kompleksi, tiki kokteyller. Retro dekor, çatı terası ve dans.",
        "description_en": "Multi-story bar and restaurant complex in Chinatown with tiki cocktails. Retro decor, rooftop terrace, and dancing."
    },
    "Candlenut": {
        "description": "Michelin yıldızlı Peranakan mutfağı, geleneksel tarifler modern sunumla. Singapur'un yerel fine-dining'i.",
        "description_en": "Michelin-starred Peranakan cuisine with traditional recipes in modern presentation. Singapore's local fine-dining."
    },
    "Burnt Ends": {
        "description": "Asya'nın en iyi restoranları listesinde, Avustralya tarzı BBQ. Modern mangal, et olgunlaştırma ve gastronomi.",
        "description_en": "On Asia's best restaurants list, Australian-style BBQ. Modern grill, meat aging, and gastronomy."
    },
    "Odette": {
        "description": "Üç Michelin yıldızlı Fransız fine-dining, National Gallery'de konumlu. Singapur'un en prestijli restoranlarından.",
        "description_en": "Three Michelin-starred French fine-dining located in National Gallery. One of Singapore's most prestigious restaurants."
    },
    "Common Man Coffee": {
        "description": "Specialty kahve ve brunch zinciri, Avustralya tarzı kafe kültürü. Flat white, avokadolu tost ve genç kalabalık.",
        "description_en": "Specialty coffee and brunch chain with Australian-style cafe culture. Flat white, avocado toast, and young crowd."
    },
    "Nye Cafe": {
        "description": "Minimalist tasarımlı specialty kahve dükkanı, single origin ve pour-over. Third wave kahve ve modern atmosfer.",
        "description_en": "Minimalist design specialty coffee shop with single origin and pour-over. Third wave coffee and modern atmosphere."
    },
    "Mustafa Centre": {
        "description": "Little India'daki 24 saat açık dev alışveriş merkezi. Hint ürünleri, elektronik ve her şey bulunur.",
        "description_en": "24-hour giant shopping center in Little India. Indian products, electronics, and everything available."
    },
    "Province": {
        "description": "Kuzey Çin mutfağı ve el yapımı erişte uzmanı restoran. Lamian, mantı ve otantik Çin lezzetleri.",
        "description_en": "Restaurant specializing in Northern Chinese cuisine and handmade noodles. Lamian, dumplings, and authentic Chinese flavors."
    }
}

filepath = 'assets/cities/singapur.json'
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

print(f"\n✅ Manually enriched {count} items (Singapore - COMPLETE).")
