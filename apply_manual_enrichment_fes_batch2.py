import json

# Manual enrichment data (Fes Batch 2 FINAL: 36 items)
updates = {
    "Crafts of Fez": {
        "description": "Fes el sanatlarının çeşitli dallarını sergileyen ve satan genel zanaat dükkanı. Seramik, deri, ahşap ve tekstil bir arada.",
        "description_en": "General craft shop exhibiting and selling various branches of Fes handicrafts. Ceramics, leather, wood, and textiles together."
    },
    "Palais De Fes Dar Tazi": {
        "description": "Tarihi sarayda lüks konaklama ve restoran, geleneksel Fas mimarisi. Avlu, çeşme ve kraliyet atmosferi.",
        "description_en": "Luxury accommodation and restaurant in historic palace with traditional Moroccan architecture. Courtyard, fountain, and royal atmosphere."
    },
    "Cafe La Noria": {
        "description": "Medina manzaralı teras kafe, nane çayı ve Fas kahvaltısı. Gün batımı izleme, huzurlu mola ve yerel atmosfer.",
        "description_en": "Terrace cafe with medina views, mint tea and Moroccan breakfast. Sunset viewing, peaceful break, and local atmosphere."
    },
    "Thami's": {
        "description": "Vejetaryen ve vegan seçeneklerle modern Fas mutfağı sunan restoran. Sağlıklı lezzetler, yaratıcı menü ve çağdaş yaklaşım.",
        "description_en": "Restaurant serving modern Moroccan cuisine with vegetarian and vegan options. Healthy flavors, creative menu, and contemporary approach."
    },
    "Riad Rcif": {
        "description": "Rcif Meydanı yakınında restore edilmiş geleneksel riad konaklama. Zellige süslemeler, avlu bahçe ve otantik deneyim.",
        "description_en": "Restored traditional riad accommodation near Rcif Square. Zellige decorations, courtyard garden, and authentic experience."
    },
    "Les Jardins de Sheherazade": {
        "description": "Güllü bahçeler içinde romantik riad-otel, sakin konum ve lüks hizmet. Spa, havuz ve Bin Bir Gece atmosferi.",
        "description_en": "Romantic riad-hotel in rose gardens with quiet location and luxury service. Spa, pool, and Arabian Nights atmosphere."
    },
    "Veggie-pause": {
        "description": "Fes'in vejetaryen dostu kafesi, sağlıklı öğle yemeği ve taze meyve suları. Organik malzemeler ve diyet dostu menü.",
        "description_en": "Fes's vegetarian-friendly cafe with healthy lunch and fresh juices. Organic ingredients and diet-friendly menu."
    },
    "L'Amandier Palais Faraj": {
        "description": "Palais Faraj'ın panoramik restoranı, şehir manzarası ve fine-dining Fas mutfağı. Romantik akşam yemekleri ve özel anlar.",
        "description_en": "Panoramic restaurant of Palais Faraj with city views and fine-dining Moroccan cuisine. Romantic dinners and special moments."
    },
    "Cremerie La Place": {
        "description": "Meydanın kenarında dondurma ve hafif tatlılar sunan kafe. Yerel halkın mola noktası, uygun fiyat ve taze lezzetler.",
        "description_en": "Cafe serving ice cream and light desserts at the edge of square. Rest stop for locals, affordable prices, and fresh flavors."
    },
    "Jawharat Fes": {
        "description": "Geleneksel Fas düğün yemeklerini sunan büyük restoran, grup etkinlikleri için ideal. Fassi mutfak, canlı müzik ve şölen.",
        "description_en": "Large restaurant serving traditional Moroccan wedding dishes, ideal for group events. Fassi cuisine, live music, and feast."
    },
    "Cafe Restaurant Al Oud": {
        "description": "Geleneksel Fas yemekleri ve canlı oud müziği sunan atmosferik mekan. Romantik akşamlar, nane çayı ve kültürel deneyim.",
        "description_en": "Atmospheric venue serving traditional Moroccan dishes and live oud music. Romantic evenings, mint tea, and cultural experience."
    },
    "Culture Box": {
        "description": "Çağdaş sanat ve kültür merkezi, sergiler, atölyeler ve yaratıcı etkinlikler. Genç Fas sanatı ve kültürel diyalog.",
        "description_en": "Contemporary art and culture center with exhibitions, workshops, and creative events. Young Moroccan art and cultural dialogue."
    },
    "Restaurant Ouliya": {
        "description": "Medinada yüksek çatı teraslı restoran, panoramik şehir manzarası ve Fas yemekleri. Gün batımı yemeği ve romantik atmosfer.",
        "description_en": "Restaurant with high rooftop terrace in medina, panoramic city views, and Moroccan food. Sunset dining and romantic atmosphere."
    },
    "Bab Mansour Laleuj": {
        "description": "Meknes'teki Fas'ın en görkemli kapısı, 18. yüzyıl mimari şaheseri. Mermer sütunlar, zellige mozaikler ve ihtişam.",
        "description_en": "Morocco's most magnificent gate in Meknes, 18th-century architectural masterpiece. Marble columns, zellige mosaics, and grandeur."
    },
    "Hammam Moulay Yacoub": {
        "description": "Fes yakınındaki termal kaplıca kasabası, şifalı sular ve hammam deneyimi. Cilt hastalıkları, wellness ve rahatlatıcı tatil.",
        "description_en": "Thermal spa town near Fes with healing waters and hammam experience. Skin conditions, wellness, and relaxing vacation."
    },
    "Sidi Harazem Oasis": {
        "description": "Fes'e yakın sıcak su kaynakları ve piknik alanı, yerel halkın hafta sonu kaçışı. Termal havuzlar ve doğa.",
        "description_en": "Hot springs and picnic area near Fes, locals' weekend escape. Thermal pools and nature."
    },
    "Azrou Cedar Forest": {
        "description": "Orta Atlas'taki devasa sedir ormanı, Barbary maymunlarının yaşam alanı. Doğa yürüyüşü, yaban hayatı ve dağ havası.",
        "description_en": "Giant cedar forest in Middle Atlas, habitat of Barbary macaques. Nature hiking, wildlife, and mountain air."
    },
    "Ain Vittel": {
        "description": "Fes yakınındaki tatlı su kaynağı, yerel halkın piknik ve dinlenme alanı. Doğal pınar, açık hava ve hafta sonu.",
        "description_en": "Freshwater spring near Fes, locals' picnic and rest area. Natural spring, outdoors, and weekends."
    },
    "Meknes Medina": {
        "description": "UNESCO korumasındaki Meknes tarihi merkezi, Fes'ten günübirlik gezi. İmparatorluk şehri, pazarlar ve anıtlar.",
        "description_en": "UNESCO-protected historic center of Meknes, day trip from Fes. Imperial city, markets, and monuments."
    },
    "Heri es-Souani": {
        "description": "Meknes'teki Moulay Ismail'in devasa tahıl ambarları ve ahırları. Osmanlı-Fas mühendisliği, tarihi yapı ve fotoğrafçılık.",
        "description_en": "Moulay Ismail's massive granaries and stables in Meknes. Ottoman-Moroccan engineering, historic structure, and photography."
    },
    "Hammam de la Poste": {
        "description": "Ville Nouvelle'deki modern hammam ve spa, geleneksel kese ve masaj. Lüks hizmet, temizlik ve rahatlama.",
        "description_en": "Modern hammam and spa in Ville Nouvelle with traditional scrub and massage. Luxury service, cleanliness, and relaxation."
    },
    "Spa Laaroussa": {
        "description": "Riad içinde butik spa, argan yağı masajı ve geleneksel Fas bakımları. Wellness, aromaterapi ve sakin atmosfer.",
        "description_en": "Boutique spa in riad with argan oil massage and traditional Moroccan treatments. Wellness, aromatherapy, and calm atmosphere."
    },
    "Mount Zalagh": {
        "description": "Fes'i çevreleyen tepelerden biri, trekking ve şehir panoraması. Gün doğumu, fotoğrafçılık ve doğa yürüyüşü.",
        "description_en": "One of the hills surrounding Fes for trekking and city panorama. Sunrise, photography, and nature walking."
    },
    "Fes Country Club": {
        "description": "Golf sahası, tenis kortları ve sosyal tesis. Spor aktiviteleri, aile günleri ve yeşil alanlar.",
        "description_en": "Golf course, tennis courts, and social facility. Sports activities, family days, and green areas."
    },
    "Gaudy Palace (Palais El Glaoui - Meknes)": {
        "description": "Meknes'teki El Glaoui ailesinin gösterişli sarayı (Pacha'nın sarayı olarak da bilinir). Süslü iç mekanlar, tarihi dram ve mimari.",
        "description_en": "El Glaoui family's ostentatious palace in Meknes (also known as Pasha's Palace). Ornate interiors, historical drama, and architecture."
    },
    "Fes Saiss Airport": {
        "description": "Fes'in uluslararası havalimanı, Avrupa ve Fas içi bağlantılar. Araç kiralama, transfer ve seyahat bilgisi.",
        "description_en": "Fes's international airport with European and domestic Morocco connections. Car rental, transfer, and travel information."
    },
    "Gare de Fes": {
        "description": "Fes merkez tren istasyonu, Kazablanka, Marakeş ve Tanca bağlantıları. ONCF trenleri, bilet satışı ve ulaşım bilgisi.",
        "description_en": "Fes central train station with Casablanca, Marrakech, and Tangier connections. ONCF trains, ticket sales, and transport information."
    },
    "Place El-Hedim": {
        "description": "Meknes'in ana meydanı, Bab Mansour karşısında buluşma noktası. Sokak sanatçıları, kafeler ve şehir yaşamı.",
        "description_en": "Meknes's main square, meeting point opposite Bab Mansour. Street performers, cafes, and city life."
    },
    "Dar Jamai Museum": {
        "description": "Meknes'teki 19. yüzyıl vezir konağında Fas sanat ve zanaat müzesi. Ahşap oyma, seramik ve tekstil koleksiyonu.",
        "description_en": "Moroccan art and craft museum in 19th-century vizier's mansion in Meknes. Wood carving, ceramics, and textile collection."
    },
    "Sidi Mguild": {
        "description": "Orta Atlas'ta kayak merkezi, kış sporları için Fas'ın alternatifi. Kar, dağ manzarası ve outdoor aktiviteler.",
        "description_en": "Ski resort in Middle Atlas, Morocco's alternative for winter sports. Snow, mountain views, and outdoor activities."
    },
    "Imouzzer Kandar": {
        "description": "Fes yakınındaki dağ kasabası, yaz serinliği ve doğa kaçışı. Elma bahçeleri, yeşillik ve sakin atmosfer.",
        "description_en": "Mountain town near Fes for summer coolness and nature escape. Apple orchards, greenery, and peaceful atmosphere."
    },
    "Bhalil": {
        "description": "Fes yakınındaki troglodyte köyü, kayalara oyulmuş geleneksel evler. Berber kültürü, otantik yaşam ve keşif.",
        "description_en": "Troglodyte village near Fes with traditional houses carved into rocks. Berber culture, authentic life, and exploration."
    },
    "Sefrou Falls": {
        "description": "Sefrou kasabasındaki şelaleler, doğa yürüyüşü ve piknik alanı. Serinlik, yeşillik ve hafta sonu kaçışı.",
        "description_en": "Waterfalls in Sefrou town for nature walking and picnic area. Coolness, greenery, and weekend escape."
    },
    "Sahara Tours from Fes": {
        "description": "Fes'ten Sahra Çölü'ne çok günlük turlar, Merzouga kum tepeleri ve çöl kampı. Deve safarisi, yıldızlar ve macera.",
        "description_en": "Multi-day tours from Fes to Sahara Desert, Merzouga sand dunes, and desert camp. Camel safari, stars, and adventure."
    },
    "Atlas Film Studios (Ouarzazate)": {
        "description": "Dünyanın en büyük film stüdyosu, Hollywood ve uluslararası yapımların çekildiği yer. Gladiator, Game of Thrones ve sinema turu.",
        "description_en": "World's largest film studio where Hollywood and international productions are shot. Gladiator, Game of Thrones, and cinema tour."
    },
    "Hammam Cinq Mondes": {
        "description": "Lüks spa ve hammam merkezi, Fas ritüelleri ve uluslararası masaj teknikleri. Premium hizmet, aromaterapiteti ve rahatlama.",
        "description_en": "Luxury spa and hammam center with Moroccan rituals and international massage techniques. Premium service, aromatherapy, and relaxation."
    }
}

filepath = 'assets/cities/fes.json'
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

print(f"\n✅ Manually enriched {count} items (Fes Batch 2 FINAL).")
