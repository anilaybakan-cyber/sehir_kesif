import json
import os

new_nice_batch1 = [
    {
        "name": "Castle Hill (Colline du Château)",
        "name_en": "Castle Hill",
        "area": "Vieux Nice",
        "category": "Manzara",
        "tags": ["şelale", "panoramik", "tarihi", "park"],
        "distanceFromCenter": 0.8,
        "lat": 43.6997,
        "lng": 7.2828,
        "price": "free",
        "rating": 4.9,
        "description": "Nice'in en ikonik manzara noktası. Devasa bir yapay şelale, liman ve kentin turkuaz kıyılarını tepeden gören muazzam bir park.",
        "description_en": "The best panoramic viewpoint in Nice. Featuring a dramatic artificial waterfall and stunning views overlooking Old Town and the Port."
    },
    {
        "name": "Musée Marc Chagall",
        "name_en": "Marc Chagall National Museum",
        "area": "Cimiez",
        "category": "Müze",
        "tags": ["chagall", "sanat", "modern", "bahçe"],
        "distanceFromCenter": 1.2,
        "lat": 43.7091,
        "lng": 7.2695,
        "price": "medium",
        "rating": 4.8,
        "description": "Ressam Marc Chagall'ın dini temalı en büyük eser koleksiyonuna ev sahipliği yapan, modern ve huzurlu bir müze.",
        "description_en": "A museum dedicated to the famous painter Marc Chagall, specifically showcasing his seventeen large biblical message canvases."
    },
    {
        "name": "Promenade du Paillon",
        "name_en": "Promenade du Paillon",
        "area": "Centro",
        "category": "Park",
        "tags": ["su aynası", "modern park", "çocuk dostu", "yeşil"],
        "distanceFromCenter": 0.3,
        "lat": 43.6974,
        "lng": 7.2714,
        "price": "free",
        "rating": 4.7,
        "description": "Place Masséna ile liman arasında uzanan, fıskiyeleri ve 'su aynası' ile ünlü kentin en modern ve keyifli şehir parkı.",
        "description_en": "A lush urban park connecting Place Masséna toward the port, famous for its giant reflecting pool and misty water jets."
    },
    {
        "name": "MAMAC (Modern Sanat Müzesi)",
        "name_en": "MAMAC Museum",
        "area": "Garibaldi",
        "category": "Müze",
        "tags": ["modern sanat", "yves klein", "niki de saint phalle", "teras"],
        "distanceFromCenter": 0.6,
        "lat": 43.7015,
        "lng": 7.2783,
        "price": "medium",
        "rating": 4.6,
        "description": "Yves Klein'ın ünlü mavisi ve Niki de Saint Phalle'in heykellerine ev sahipliği yapan, çatısındaki manzarayla büyüleyen modern sanat müzesi.",
        "description_en": "Nice's contemporary art museum, home to works by Yves Klein and Niki de Saint Phalle, with a roof terrace offering 360-degree city views."
    },
    {
        "name": "Fenocchio Gelato",
        "name_en": "Fenocchio Gelateria",
        "area": "Vieux Nice",
        "category": "Kafe",
        "tags": ["dondurma", "lavanta", "klasik", "meydan"],
        "distanceFromCenter": 0.5,
        "lat": 43.6971,
        "lng": 7.2759,
        "price": "medium",
        "rating": 4.8,
        "description": "Nice'in en meşhur dondurmacısı. Lavantalı ve domatesli gibi sıra dışı 100'den fazla aromasıyla Place Rossetti'nin kalbinde.",
        "description_en": "An institution in Old Nice since 1966, famous for its 100+ unconventional flavors like lavender, thyme, and tomato."
    },
    {
        "name": "Chez Pipo (Socca)",
        "name_en": "Chez Pipo",
        "area": "Port Lympia",
        "category": "Restoran",
        "tags": ["socca", "lokal lezzet", "tarihi", "ekonomik"],
        "distanceFromCenter": 1.0,
        "lat": 43.6961,
        "lng": 7.2820,
        "price": "low",
        "rating": 4.7,
        "description": "Nice'in geleneksel nohut unlu pizzası 'Socca'yı tatmak için gidilecek en iyi ve en tarihi yerlerden biri.",
        "description_en": "The legendary spot to try 'Socca,' Nice’s famous chickpea pancake. Expect a wait and a true local atmosphere."
    },
    {
        "name": "Le Plongeoir",
        "name_en": "Le Plongeoir Restaurant",
        "area": "Görsel Sahiller / Port",
        "category": "Restoran",
        "tags": ["manzara", "deniz üstü", "ikonik", "şık"],
        "distanceFromCenter": 1.5,
        "lat": 43.6896,
        "lng": 7.2882,
        "price": "high",
        "rating": 4.8,
        "description": "Eski bir atlama platformunun üzerine inşa edilmiş, tam anlamıyla denizin üzerinde yemek yiyebileceğiniz kentin en fotojenik restoranı.",
        "description_en": "Built on the iconic diving boards of the 19th-century beach, this restaurant offers spectacular views and fresh Mediterranean cuisine."
    },
    {
        "name": "Cimiez Monastery (Monastère de Cimiez)",
        "name_en": "Cimiez Monastery",
        "area": "Cimiez",
        "category": "Tarihi",
        "tags": ["manastır", "bahçe", "manzara", "sessiz"],
        "distanceFromCenter": 2.2,
        "lat": 43.7201,
        "lng": 7.2790,
        "price": "free",
        "rating": 4.7,
        "description": "Nice'in tepelerinde, muazzam İtalyan tarzı bahçeleri ve kenti tepeden gören manzarasıyla 9. yüzyıldan kalma huzurlu bir manastır.",
        "description_en": "A 9th-century Franciscan monastery featuring a tranquil rose garden and one of the finest viewpoints overlooking the city and the sea."
    }
]

def enrich_nice():
    filepath = 'assets/cities/nice.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update fillers in existing highlights
    fillers = {
        "Promenade des Anglais": {
            "description": "Akdeniz boyunca uzanan, Nice'in kalbi sayılan dünyaca ünlü sahil yolu. Yürüyüş, bisiklet ve efsanevi mavi sandalyeler için en doğru adres.",
            "description_en": "Nice's most famous landmark, a sweeping 7km boulevard along the Mediterranean, perfect for a sunset stroll or cycling."
        },
        "Old Town (Vieux Nice)": {
            "description": "Daracık sokakları, rengarenk binaları ve Cours Saleya pazarıyla İtalyan ve Fransız kültürünün en canlı harmanı.",
            "description_en": "The atmospheric old heart of Nice with narrow lanes, Baroque churches, and the vibrant flower market of Cours Saleya."
        },
        "Colline du Château": {
            "description": "Nice'in en yüksek noktası. Harika bir şelale, gölge dolu park alanları ve Melekler Körfezi'nin (Baie des Anges) en iyi manzarası buradadır.",
            "description_en": "A scenic hilltop park offering the most iconic panoramic views of the city, the port, and the turquoise waters below."
        },
        "Place Masséna": {
            "description": "Kentin ana meydanı. Kırmıza binaları, dama tahtası zeminini ve Jaume Plensa'nın modern heykelleriyle Nice'in simgesi.",
            "description_en": "The iconic main square of Nice, known for its checkerboard floor, red facades, and the 'Scribing Men' statues that glow at night."
        },
        "Nice Cathedral": {
            "description": "Vieux Nice'in merkezinde, Place Rossetti'de yer alan 17. yüzyıl Barok mimarisi ve muazzam renkli kubbesiyle büyüleyici bir yapı.",
            "description_en": "A stunning Baroque cathedral in the heart of the Old Town, dedicated to Sainte Réparate and featuring a tiled dome."
        },
        "Cours Saleya Market": {
            "description": "Hafta içi çiçek ve gıda pazarı, pazartesileri ise antikacılar çarşısı. Nice'in en taze ve renkli duraklarından biri.",
            "description_en": "The legendary open-air market in Old Nice, famous for its colorful flowers, local produce, and Provençal specialties."
        },
        "Musée Matisse": {
            "description": "Henri Matisse'in yaşamının büyük kısmını geçirdiği Nice'teki kişisel koleksiyonu ve eserlerini barındıran şık bir 17. yüzyıl villası.",
            "description_en": "A stunning 17th-century villa in the Cimiez hills housing one of the world's largest collections of Henri Matisse's works."
        },
        "Saint Nicholas Russian Orthodox Cathedral": {
            "description": "Rusya dışındaki en büyük Ortodoks katedrali. Renkli kubbeleri ve farklı mimarisiyle Nice'in en büyüleyici yapılarından biri.",
            "description_en": "The largest Eastern Orthodox cathedral in Western Europe, a colorful architectural marvel reflecting the city's Imperial Russian ties."
        }
    }

    for h in data.get('highlights', []):
        if h['name'] in fillers:
            h['description'] = fillers[h['name']]['description']
            h['description_en'] = fillers[h['name']]['description_en']

    # 2. Add new highlights
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_nice_batch1:
        if new_h['name'].lower() not in existing_names:
            # Add missing fields
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1533619239233-6280475a634a?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    # 3. Handle duplicates or near-duplicates (e.g., Castle Hill vs Colline du Château)
    # The cleanup script will do this better, but let's be careful.

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_nice()
print(f"Nice now has {count} highlights.")
