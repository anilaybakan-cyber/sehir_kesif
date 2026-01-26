import json
import os

new_madrid_batch1 = [
    {
        "name": "Templo de Debod",
        "name_en": "Temple of Debod",
        "area": "Moncloa",
        "category": "Tarihi",
        "tags": ["mısır", "gün batımı", "antik", "park"],
        "distanceFromCenter": 1.2,
        "lat": 40.4240,
        "lng": -3.7177,
        "price": "free",
        "rating": 4.8,
        "description": "Mısır'dan Madrid'e getirilmiş, kentin en güzel gün batımı manzarasına sahip antik bir Mısır tapınağı.",
        "description_en": "An ancient Egyptian temple donated to Spain, now standing in a park near the Royal Palace. It's the most iconic spot in Madrid to watch the sunset.",
        "imageUrl": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Tapınağın suya yansıması fotoğraf çekmek için muazzamdır, gün batımından en az yarım saat önce gidin.",
        "tips_en": "The reflection of the temple in the surrounding pool is stunning; arrive at least 30 minutes before sunset to secure a good spot."
    },
    {
        "name": "Palacio de Cibeles",
        "name_en": "Cibeles Palace",
        "area": "Retiro / Centro",
        "category": "Tarihi",
        "tags": ["belediye", "mimari", "seyir terası", "ikonik"],
        "distanceFromCenter": 0.8,
        "lat": 40.4193,
        "lng": -3.6931,
        "price": "low",
        "rating": 4.7,
        "description": "Madrid'in simgelerinden biri olan, muazzam bir mimariye sahip eski posta binası ve şimdiki belediye sarayı.",
        "description_en": "One of Madrid's most iconic landmarks, this former communications palace now serves as the City Hall and a major cultural center.",
        "imageUrl": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        "bestTime": "Akşam ışıklandırması",
        "bestTime_en": "Evening lighting",
        "tips": "Binanın üst katındaki seyir terasından (Mirador) Madrid'i 360 derece izleyebilirsiniz.",
        "tips_en": "Take the elevator to the 'Mirador' observation deck for one of the best 360-degree panoramic views over central Madrid."
    },
    {
        "name": "Chocolatería San Ginés",
        "name_en": "Chocolateria San Gines",
        "area": "Centro",
        "category": "Kafe",
        "tags": ["churros", "tarihi", "tatlı", "lokal"],
        "distanceFromCenter": 0.2,
        "lat": 40.4170,
        "lng": -3.7068,
        "price": "medium",
        "rating": 4.6,
        "description": "1894'ten beri hizmet veren, Madrid'in en meşhur churro ve sıcak çikolata durağı.",
        "description_en": "Founded in 1894, this is Madrid's most famous spot for 'churros con chocolate.' A timeless institution that never sleeps.",
        "imageUrl": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        "bestTime": "Günün her saati (24 saat açık)",
        "bestTime_en": "Anytime (Open 24/7)",
        "tips": "Her zaman kuyruk olabilir ama çok hızlı akar. Gece yarısı veya sabahın ilk ışıklarında gitmek bir Madrid geleneğidir.",
        "tips_en": "It's open 24 hours a day; visiting for a late-night snack or very early breakfast is a quintessential Madrid experience."
    },
    {
        "name": "Matadero Madrid",
        "name_en": "Matadero Madrid",
        "area": "Arganzuela",
        "category": "Deneyim",
        "tags": ["kültür", "modern sanat", "etkinlik", "endüstriyel"],
        "distanceFromCenter": 2.5,
        "lat": 40.3919,
        "lng": -3.6985,
        "price": "low",
        "rating": 4.8,
        "description": "Eski bir mezbahanın devasa bir sanat ve kültür kompleksine dönüştürüldüğü, kentin en 'cool' yaratıcı merkezi.",
        "description_en": "A former slaughterhouse converted into a massive artistic community and cultural center, hosting exhibitions, cinemas, and music festivals.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Hafta sonu",
        "bestTime_en": "Weekend",
        "tips": "İçindeki 'Cineteca' film arşivi ve tasarım pazarını (Mercado de Motores) mutlaka görün.",
        "tips_en": "Check the programming for Cineteca or the monthly Mercado de Motores flea market which often takes place nearby."
    },
    {
        "name": "Círculo de Bellas Artes (Azotea)",
        "name_en": "Circulo de Bellas Artes Rooftop",
        "area": "Centro",
        "category": "Manzara",
        "tags": ["rooftop", "manzara", "kokteyl", "gran via"],
        "distanceFromCenter": 0.5,
        "lat": 40.4183,
        "lng": -3.6966,
        "price": "medium",
        "rating": 4.9,
        "description": "Madrid'in en iyi manzarasını sunan teras. Gran Vía ve Metropolis binasını tepeden izlemek için en doğru yer.",
        "description_en": "Arguably the best rooftop view in Madrid, offering a stunning perspective looking down over Gran Vía and the iconic Metropolis building.",
        "imageUrl": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Teras girişi ücretlidir ancak manzara kesinlikle buna değer. Bir içki eşliğinde Madrid silüetinin tadını çıkarın.",
        "tips_en": "There is a small entry fee for the roof-only ticket, but the 360-degree views make it worth every cent, especially at dusk."
    },
    {
        "name": "Salmon Guru",
        "name_en": "Salmon Guru",
        "area": "Huertas",
        "category": "Bar",
        "tags": ["kokteyl", "yaratıcı", "gece hayatı", "şık"],
        "distanceFromCenter": 0.6,
        "lat": 40.4135,
        "lng": -3.6988,
        "price": "high",
        "rating": 4.8,
        "description": "Dünyanın en iyi barlarından biri kabul edilen, çılgın sunumları ve retro dekorasyonuyla ünlü kokteyl barı.",
        "description_en": "Consistently ranked among the World's 50 Best Bars, known for its wildly imaginative cocktails served in unique, custom-made glassware.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Akşam geç saatler",
        "bestTime_en": "Late evening",
        "tips": "Kuyruk olabilir, erken gitmek veya hafta içi tercih etmek yer bulmanıza yardımcı olur.",
        "tips_en": "No reservations accepted; arrive early or on a weeknight to snag a spot in this neon-lit, high-energy cocktail temple."
    }
]

def enrich_madrid():
    filepath = 'assets/cities/madrid.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update fillers in existing highlights
    fillers = {
        "Royal Palace of Madrid": {
            "description": "Batı Avrupa'nın en büyük kraliyet sarayı. 3000'den fazla odası, Stradivarius enstrüman koleksiyonu ve muazzam bahçeleriyle İspanyol monarşisinin kalbi.",
            "description_en": "The largest royal palace in Western Europe. A marvel of grandiose architecture housing priceless art, armor, and the Royal Pharmacy."
        },
        "Plaza Mayor": {
            "description": "Her tarafı asırlık binalarla çevrili, Madrid'in en görkemli tarihi meydanı. 17. yüzyıldan beri kentin ana buluşma noktası.",
            "description_en": "Madrid's grand central square, surrounded by 400-year-old red buildings and frescoes. The pulse of the city's historic center."
        },
        "Prado Museum": {
            "description": "Dünyanın en zengin sanat galerilerinden biri. Velázquez, Goya ve El Greco gibi ustaların eserlerini barındıran İspanyol sanatının zirvesi.",
            "description_en": "One of the premier art museums in the world, home to the finest collections of Spanish art including Velázquez's 'Las Meninas'."
        },
        "Retiro Park": {
            "description": "Madrid'in 'akciğerleri.' İçinde muazzam bir gölet, Kristal Saray (Palacio de Cristal) ve gül bahçeleri barındıran devasa, huzurlu bir park.",
            "description_en": "A vast, historic city park featuring a rowing lake, the stunning glass-and-iron Crystal Palace, and lush, shaded promenades."
        },
        "Mercado de San Miguel": {
            "description": "100 yıllık tarihi bir demir ve cam yapı içinde yer alan gurme tapas pazarı. İspanyol lezzetlerini tatmak için kentin en canlı noktası.",
            "description_en": "A gourmet food hall housed in a beautiful 20th-century iron structure, perfect for tasting high-quality Spanish tapas and wines."
        },
        "Puerta del Sol": {
            "description": "Madrid'in ve tüm İspanya'nın merkezi (Kilometre 0). Ünlü 'Ayı ve Kocayemiş Ağacı' heykeline ev sahipliği yapan hareketli meydan.",
            "description_en": "The geographic center of Spain and the site of the city's famous 'Bear and Strawberry Tree' statue, always buzzing with energy."
        },
        "Gran Vía": {
            "description": "Madrid'in asla uyumayan ana caddesi. Tiyatroları, devasa binaları ve alışveriş olanaklarıyla şehrin Broadway'i sayılır.",
            "description_en": "The city's grandest boulevard, famous for its 20th-century architecture, theaters, shopping, and neon-lit 'Broadway' feel."
        },
        "Santiago Bernabéu Stadium": {
            "description": "Futbolun tapınaklarından biri. Real Madrid'in evi olan bu dev stat, müzesi ve efsanevi kupalarıyla her sporsever için bir zorunluluktur.",
            "description_en": "The legendary home of Real Madrid. A must-visit for football fans to see the museum showcasing the club's record-breaking trophies."
        },
        "Reina Sofía Museum": {
            "description": "İspanya'nın modern sanat galerisi. Picasso'nun ölümsüz eseri Guernica'ya ve Salvador Dalí'nin gerçeküstü tablolarına ev sahipliği yapar.",
            "description_en": "Spain's national museum of 20th-century art, famously housing Picasso's massive anti-war masterpiece, 'Guernica'."
        },
        "Almudena Cathedral": {
            "description": "Kraliyet Sarayı'nın hemen karşısında yer alan, modern ve renkli iç dekorasyonuyla kentin en önemli dini simgesi.",
            "description_en": "A grand neo-Gothic cathedral facing the Royal Palace, known for its strikingly colorful modern ceiling and beautiful crypt."
        },
        "El Rastro Flea Market": {
            "description": "Pazar günleri kurulan, yüzlerce tezgahta antikalardan giysilere kadar her şeyi bulabileceğiniz kentin en eski ve en büyük bit pazarı.",
            "description_en": "The most famous open-air market in Spain, held every Sunday in the La Latina neighborhood, and a true local tradition for over 400 years."
        },
        "Plaza de Cibeles": {
            "description": "Milano'dan esintiler taşıyan heybetli saray binası ve ortasındaki ünlü çeşme ile kentin en güzel ve görkemli meydanlarından biri.",
            "description_en": "A majestic plaza featuring the iconic Cibeles Fountain and the stunning City Hall palace; a prime spot for celebratory gatherings."
        }
    }

    for h in data.get('highlights', []):
        if h['name'] in fillers:
            h['description'] = fillers[h['name']]['description']
            h['description_en'] = fillers[h['name']]['description_en']

    # 2. Add new highlights
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_madrid_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_madrid()
print(f"Madrid now has {count} highlights.")
