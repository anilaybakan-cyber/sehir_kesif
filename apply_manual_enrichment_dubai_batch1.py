import json

# Manual enrichment data (Dubai - ALL 35 items)
updates = {
    "Hatta Dam": {
        "description": "Dubai'nin dağlık bölgesinde turkuaz renkli baraj gölü. Kayak, kano yapma ve dağ manzaralı yürüyüş imkanı.",
        "description_en": "Turquoise dam lake in Dubai's mountainous region. Kayaking, canoeing, and hiking with mountain views."
    },
    "Tresind Studio": {
        "description": "Modern Hint mutfağının zirvesi, Michelin yıldızlı tadım menüsü. Yaratıcı sunumlar ve teatral yemek deneyimi.",
        "description_en": "Pinnacle of modern Indian cuisine, Michelin-starred tasting menu. Creative presentations and theatrical dining experience."
    },
    "SALT Kite Beach": {
        "description": "Kite Beach'te popüler gümüş renkli burger karavanı. Wagyu beef slider, Lotus shake ve plaj atmosferi.",
        "description_en": "Popular silver burger airstream at Kite Beach. Wagyu beef sliders, Lotus shake, and beach atmosphere."
    },
    "Ravi Restaurant": {
        "description": "Satwa'da efsanevi Pakistan lokantası, ucuz ve lezzetli. Anthony Bourdain'in favorisi, otantik sokak lezzeti.",
        "description_en": "Legendary Pakistani eatery in Satwa, cheap and delicious. Anthony Bourdain's favorite, authentic street flavor."
    },
    "At.mosphere": {
        "description": "Burj Khalifa'nın 122. katında dünyanın en yüksek restoranı. Lüks akşam yemeği ve bulutların üzerinde kokteyl.",
        "description_en": "World's highest restaurant on 122nd floor of Burj Khalifa. Luxury dinner and cocktails above the clouds."
    },
    "Zuma Dubai": {
        "description": "DIFC'de modern Japon mutfağı (Izakaya tarzı) ve şık bar. Pazar brunch'ı efsanevi, iş dünyasının buluşma noktası.",
        "description_en": "Modern Japanese cuisine (Izakaya style) and chic bar in DIFC. Legendary Sunday brunch, meeting point for business world."
    },
    "Nobu Dubai": {
        "description": "Atlantis The Palm'da dünyaca ünlü Japon-Peru füzyon restoranı. Black Cod Miso ve lüks dekorasyon.",
        "description_en": "World-famous Japanese-Peruvian fusion restaurant at Atlantis The Palm. Black Cod Miso and luxury decoration."
    },
    "Ossiano": {
        "description": "Atlantis'te dev akvaryumun içinde su altı yemek deneyimi. Michelin yıldızlı deniz ürünleri ve romantik atmosfer.",
        "description_en": "Underwater dining experience inside giant aquarium at Atlantis. Michelin-starred seafood and romantic atmosphere."
    },
    "Al Mallah": {
        "description": "Satwa'da Lübnan sokak lezzetleri, şavurma ve meyve kokteylleri. Gece geç saatlere kadar açık, yerel favori.",
        "description_en": "Lebanese street food, shawarma, and fruit cocktails in Satwa. Open late night, local favorite."
    },
    "Bu Qtair": {
        "description": "Jumeirah'da balıkçı kulübesinden restorana dönüşen salaş mekan. Taze kızarmış balık, karides ve köri sosu.",
        "description_en": "Shabby spot in Jumeirah turned from fisherman's shack to restaurant. Fresh fried fish, shrimp, and curry sauce."
    },
    "Jumeirah Mosque": {
        "description": "Geleneksel Fatımi tarzı mimari, gayrimüslimlerin ziyaretine açık. 'Açık kapılar, açık zihinler' programı.",
        "description_en": "Traditional Fatimid style architecture, open to non-Muslim visitors. 'Open doors, open minds' program."
    },
    "Dubai Butterfly Garden": {
        "description": "Miracle Garden yanında, 15.000 kelebeğe ev sahipliği yapan kapalı bahçe. Renkli kubbeler ve eğitim.",
        "description_en": "Indoor garden next to Miracle Garden, home to 15,000 butterflies. Colorful domes and education."
    },
    "Dubai Hills Mall": {
        "description": "Lüks markalar ve kapalı roller coaster (The Storm) bulunan yeni AVM. Şık restoranlar ve park manzarası.",
        "description_en": "New mall with luxury brands and indoor roller coaster (The Storm). Chic restaurants and park views."
    },
    "Mall of the Emirates": {
        "description": "İçinde kayak merkezi (Ski Dubai) olan dev alışveriş merkezi. Moda kubbesi, sinema ve aile eğlencesi.",
        "description_en": "Giant shopping mall containing ski resort (Ski Dubai). Fashion dome, cinema, and family entertainment."
    },
    "Meena Bazaar": {
        "description": "Bur Dubai'de 'Küçük Hindistan' olarak bilinen çarşı. Tekstil, mücevher, baharat ve otantik Hint yemekleri.",
        "description_en": "Bazaar known as 'Little India' in Bur Dubai. Textiles, jewelry, spices, and authentic Indian food."
    },
    "Ibn Battuta Mall": {
        "description": "Gezgin İbn Battuta'nın seyahatlerine göre temalandırılmış AVM. Çin, Hindistan, İran bölümleri ve dekorasyon.",
        "description_en": "Mall themed after travels of explorer Ibn Battuta. China, India, Persia courts and decoration."
    },
    "City Walk": {
        "description": "Açık hava alışveriş ve yaşam merkezi, Avrupa tarzı caddeler. Green Planet, duvar resimleri ve şık kafeler.",
        "description_en": "Outdoor shopping and lifestyle center, European style streets. Green Planet, wall murals, and chic cafes."
    },
    "The Beach at JBR": {
        "description": "Jumeirah Beach Residence sahilinde açık hava AVM ve plaj. Restoranlar, sinema, deniz ve gökdelen manzarası.",
        "description_en": "Outdoor mall and beach at Jumeirah Beach Residence waterfront. Restaurants, cinema, sea, and skyscraper views."
    },
    "Bollywood Parks Dubai": {
        "description": "Hint sineması Bollywood temalı dünyadaki ilk park. Dans şovları, renkli setler ve tematik ride'lar.",
        "description_en": "World's first Bollywood themed park. Dance shows, colorful sets, and thematic rides."
    },
    "Dubai Aquarium & Underwater Zoo": {
        "description": "Dubai Mall içindeki dev akvaryum tankı ve su altı tüneli. Köpekbalıkları, vatozlar ve Kral Timsah.",
        "description_en": "Giant aquarium tank and underwater tunnel inside Dubai Mall. Sharks, rays, and King Croc."
    },
    "XLine Dubai Marina Zipline": {
        "description": "Dünyanın en uzun şehir içi zipline hattı. Gökdelenlerin arasından marinaya süper kahraman gibi uçuş.",
        "description_en": "World's longest urban zipline. Flight like a superhero through skyscrapers to the marina."
    },
    "Dubai Ice Rink": {
        "description": "Dubai Mall içinde olimpik boyutlarda buz pateni pisti. Alışveriş molasında serinleme ve buz hokeyi.",
        "description_en": "Olympic-sized ice skating rink inside Dubai Mall. Cooling off during shopping break and ice hockey."
    },
    "VR Park Dubai Mall": {
        "description": "Dünyanın en büyük sanal gerçeklik (VR) ve artırılmış gerçeklik parkı. Burj Khalifa'dan düşme simülasyonu.",
        "description_en": "World's largest virtual reality (VR) and augmented reality park. Burj Khalifa drop simulation."
    },
    "Zabeel Park": {
        "description": "Dubai Frame'in bulunduğu teknolojik park. Barbekü alanları, teknoloji bahçesi ve Dubai Garden Glow.",
        "description_en": "Technological park where Dubai Frame is located. BBQ areas, technology garden, and Dubai Garden Glow."
    },
    "Safa Park": {
        "description": "Şehir merkezinde yeşil vaha, Dubai Kanalı manzaralı. Koşu parkuru, gölet ve aile piknikleri.",
        "description_en": "Green oasis in city center with Dubai Canal views. Jogging track, pond, and family picnics."
    },
    "Al Bastakiya Quarter": {
        "description": "Dubai'nin en eski yerleşim bölgesi, restore edilmiş rüzgar kuleli evler. Sanat galerileri, labirent sokaklar ve tarih.",
        "description_en": "Dubai's oldest residential area, restored wind-tower houses. Art galleries, labyrinth streets, and history."
    },
    "Dubai Museum (Al Fahidi Fort)": {
        "description": "1787 yapımı kalede Dubai'nin dönüşüm hikayesi. Bedevi yaşamı, inci dalgıçlığı ve yeraltı sergileri.",
        "description_en": "Dubai's transformation story in 1787 fort. Bedouin life, pearl diving, and underground exhibits."
    },
    "La Perle by Dragone": {
        "description": "Dubai'nin ilk kalıcı su gösterisi, Las Vegas tarzı akrobasi. Suyla dolu sahne, ışık efektleri ve sürükleyici şov.",
        "description_en": "Dubai's first permanent aqua show, Las Vegas style acrobatics. Water-filled stage, light effects, and immersive show."
    },
    "Dubai Water Canal": {
        "description": "Şehri boydan boya geçen yapay kanal. Şelale köprüsü (hareket sensörlü), yürüyüş yolu ve gece ışıkları.",
        "description_en": "Artificial canal crossing the city. Waterfall bridge (motion sensor), promenade, and night lights."
    },
    "The Lost Chambers Aquarium": {
        "description": "Atlantis efsanesi temalı labirent akvaryum. Antik kalıntılar arasında yüzbinlerce deniz canlısı ve dalış imkanı.",
        "description_en": "Atlantis legend themed labyrinth aquarium. Hundreds of thousands of marine life amidst ancient ruins and diving."
    },
    "Jumeirah Beach": {
        "description": "Burj Al Arab manzaralı halk plajı. Beyaz kum, turkuaz deniz ve gün batımı yürüyüşleri.",
        "description_en": "Public beach with Burj Al Arab views. White sand, turquoise sea, and sunset walks."
    },
    "Real Madrid World": {
        "description": "Dünyanın ilk futbol temalı parkı, Real Madrid deneyimi. Simülasyonlar, tarih müzesi ve interaktif oyunlar.",
        "description_en": "World's first football themed park, Real Madrid experience. Simulations, history museum, and interactive games."
    },
    "Souk Madinat Jumeirah": {
        "description": "Venedik kanalları tarzında modern 'geleneksel' çarşı. Abra turları, Burj Al Arab manzaralı restoranlar ve lüks.",
        "description_en": "Modern 'traditional' souk in Venice canals style. Abra tours, restaurants with Burj Al Arab views, and luxury."
    },
    "Love Lake": {
        "description": "Çölün ortasında birbirine geçmiş iki kalp şeklinde yapay göl. Romantik yürüyüş, kuş gözlemi ve kamp.",
        "description_en": "Intertwined two heart-shaped artificial lakes in middle of desert. Romantic walk, bird watching, and camping."
    },
    "Museum of Illusions": {
        "description": "Al Seef bölgesinde algı oyunları ve optik illüzyonlar müzesi. Vortex tüneli, yerçekimsiz oda ve eğlenceli fotoğraflar.",
        "description_en": "Perception games and optical illusions museum in Al Seef area. Vortex tunnel, anti-gravity room, and fun photos."
    }
}

filepath = 'assets/cities/dubai.json'
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

print(f"\n✅ Manually enriched {count} items (Dubai - COMPLETE).")
