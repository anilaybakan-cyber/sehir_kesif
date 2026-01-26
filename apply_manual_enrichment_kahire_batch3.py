import json

# Manual enrichment data (Kahire Batch 3 FINAL: 22 items)
updates = {
    "Tunis Village": {
        "description": "Fayum Vahası'ndaki sanat kolonisi, seramik atölyeleri ve yaratıcı topluluk. Köy hayatı, el sanatları ve çöl-vaha manzarası.",
        "description_en": "An art colony in Fayum Oasis with ceramic workshops and creative community. Village life, handicrafts, and desert-oasis scenery."
    },
    "Magic Lake": {
        "description": "Fayum'daki renk değiştiren tuz gölü, gün ışığına göre değişen tonlarıyla. Çöl safari, kamp ve benzersiz doğa deneyimi.",
        "description_en": "A color-changing salt lake in Fayum with tones that vary with daylight. Desert safari, camping, and unique nature experience."
    },
    "Point 90 Mall": {
        "description": "New Cairo'da modern alışveriş merkezi, markalar, sinema ve yeme-içme seçenekleri. Aile aktiviteleri ve hafta sonu eğlencesi.",
        "description_en": "A modern shopping mall in New Cairo with brands, cinema, and dining options. Family activities and weekend entertainment."
    },
    "Fish Garden": {
        "description": "Zamalek'te 1902'den kalma tarihi park, yapay mağaralar ve akvaryum kalıntıları. Gölgeli yürüyüş, çocuk oyun alanları ve nostaljik atmosfer.",
        "description_en": "A historic park from 1902 in Zamalek with artificial caves and aquarium remains. Shaded walks, children's playgrounds, and nostalgic atmosphere."
    },
    "Garden 8": {
        "description": "Maadi'de açık hava cafe ve etkinlik mekanı, canlı müzik ve film geceleri. Rahat ortam, yemek kamyonları ve topluluk atmosferi.",
        "description_en": "An outdoor cafe and event venue in Maadi with live music and movie nights. Relaxed setting, food trucks, and community atmosphere."
    },
    "Pyramid of Unas": {
        "description": "Saqqara'daki piramid, içinde dünyanın bilinen en eski dini metinleri olan 'Piramit Metinleri'. Antik cenaze ritüelleri ve hiyeroglif.",
        "description_en": "A pyramid in Saqqara containing the world's oldest known religious texts 'Pyramid Texts'. Ancient funeral rituals and hieroglyphics."
    },
    "Pompey's Pillar": {
        "description": "İskenderiye'deki devasa Roma dönemi sütunu, aslında Diocletian'a adanmış. Antik kalıntılar, arkeolojik alan ve tarih merakı.",
        "description_en": "A massive Roman-era column in Alexandria, actually dedicated to Diocletian. Ancient remains, archaeological site, and history curiosity."
    },
    "Petrified Forest": {
        "description": "Kahire yakınlarında milyonlarca yıllık taşlaşmış ağaçların bulunduğu koruma alanı. Jeolojik harika, çöl yürüyüşü ve prehistorik kalıntılar.",
        "description_en": "A protected area near Cairo with millions of years old petrified trees. Geological wonder, desert walking, and prehistoric remains."
    },
    "Andalus Garden": {
        "description": "Zamalek'te Nil kıyısında Endülüs tarzı park, çeşmeler ve süs havuzlarıyla. Romantik akşam yürüyüşleri, manzara ve huzur.",
        "description_en": "An Andalusian-style park on Nile bank in Zamalek with fountains and ornamental pools. Romantic evening walks, views, and peace."
    },
    "Roman Amphitheatre": {
        "description": "İskenderiye'deki Roma dönemi amfitiyatrı, antik gösterilerin yapıldığı yarım daire yapı. Mozaikler, mermer sütunlar ve arkeolojik önem.",
        "description_en": "A Roman-period amphitheater in Alexandria, a semicircular structure where ancient shows were held. Mosaics, marble columns, and archaeological importance."
    },
    "Family Park": {
        "description": "Yeni Kahire'de büyük aile eğlence parkı, oyun alanları ve piknik tesisleri. Çocuk aktiviteleri, yeşil alanlar ve hafta sonu kaçışı.",
        "description_en": "A large family entertainment park in New Cairo with playgrounds and picnic facilities. Children's activities, green areas, and weekend escape."
    },
    "Qanater Barrages": {
        "description": "Nil deltasının başlangıcındaki 19. yüzyıl baraj yapısı, parklar ve yeşil alanlarla. Piknik, tekne gezileri ve mühendislik mirası.",
        "description_en": "A 19th-century barrage structure at start of Nile delta with parks and green areas. Picnics, boat trips, and engineering heritage."
    },
    "Karanis": {
        "description": "Fayum'daki Yunan-Roma dönemi antik kasaba kalıntıları. Tapınaklar, evler ve günlük yaşam eserlerinin sergilendiği arkeolojik alan.",
        "description_en": "Greco-Roman period ancient town remains in Fayum. Archaeological site with temples, houses, and daily life artifacts on display."
    },
    "Lake View Plaza": {
        "description": "5. Yerleşim Bölgesi'nde göl kenarında açık hava alışveriş ve yeme-içme mekanı. Manzaralı kafeler, restoranlar ve akşam yürüyüşleri.",
        "description_en": "An open-air shopping and dining venue by the lake in 5th Settlement. Cafes with views, restaurants, and evening walks."
    },
    "Papyrus Institute": {
        "description": "Geleneksel papirüs yapım tekniklerini gösteren ve el yapımı papirüs satışı yapan merkez. Giza yakınında, turistik ama eğitici deneyim.",
        "description_en": "A center showing traditional papyrus making techniques and selling handmade papyrus. Near Giza, touristy but educational experience."
    },
    "Carpet Schools": {
        "description": "Kahire'nin geleneksel halı dokuma okulları, çocuklara ve zanaatkarlara beceri öğreten atölyeler. El dokuma, Mısır desenleri ve zanaat mirası.",
        "description_en": "Cairo's traditional carpet weaving schools, workshops teaching skills to children and artisans. Hand weaving, Egyptian patterns, and craft heritage."
    },
    "Japanese Garden": {
        "description": "Helwan'da Japon tarzı tasarlanmış park, köprüler, göletler ve Zen atmosferi. Sakin mola, fotoğraf ve doğa meditasyonu.",
        "description_en": "A Japanese-style designed park in Helwan with bridges, ponds, and Zen atmosphere. Peaceful break, photography, and nature meditation."
    },
    "Osana Family Wellness": {
        "description": "Aileler için spa ve wellness merkezi, çocuk aktiviteleri ve yetişkin rahatlama hizmetleri. Masaj, sauna ve aile dostu tesisler.",
        "description_en": "A spa and wellness center for families with children's activities and adult relaxation services. Massage, sauna, and family-friendly facilities."
    },
    "Nile City Boat": {
        "description": "Nile City Towers yanından kalkan yemekli nehir gezisi. Akşam yemeği, canlı müzik ve ışıltılı Kahire manzarası.",
        "description_en": "A dinner river cruise departing from Nile City Towers. Dinner, live music, and sparkling Cairo views."
    },
    "Colossus of Ramses": {
        "description": "Mit Rahina'daki devasa II. Ramses heykeli, antik Memphis kalıntıları arasında. 10 metre uzunluğunda yatan heykel, Mısır gücünün sembolü.",
        "description_en": "A colossal statue of Ramses II in Mit Rahina, among ancient Memphis remains. 10-meter lying statue, symbol of Egyptian power."
    },
    "Qasr Qarun": {
        "description": "Fayum'daki Ptolemy dönemi tapınağı, çöl manzarası ve iyi korunmuş yapısıyla. Uzak konum, arkeolojik keşif ve antik din.",
        "description_en": "A Ptolemaic-period temple in Fayum with desert scenery and well-preserved structure. Remote location, archaeological discovery, and ancient religion."
    },
    "Blue Nile Boat": {
        "description": "Nil'de akşam yemeği kruvazieryeri, Mısır ve uluslararası mutfak seçenekleri. Dans gösterileri, nehir manzarası ve özel geceler.",
        "description_en": "A dinner cruise on Nile with Egyptian and international cuisine options. Dance shows, river views, and special nights."
    }
}

filepath = 'assets/cities/kahire.json'
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

print(f"\n✅ Manually enriched {count} items (Kahire Batch 3 FINAL).")
