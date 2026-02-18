import json
import os

new_marseille_batch1 = [
    {
        "name": "Vallon des Auffes",
        "name_en": "Vallon des Auffes",
        "area": "Endoume",
        "category": "Manzara",
        "tags": ["balıkçı limanı", "geleneksel", "yüzme", "fotojenik"],
        "distanceFromCenter": 2.5,
        "lat": 43.2854,
        "lng": 5.3509,
        "price": "free",
        "rating": 4.9,
        "description": "Marseille'in en gizli ve büyüleyici köşesi. Şehrin kalbinde, devasa bir viyadüğün altında saklanmış, geleneksel balıkçı tekneleri ve renkli evlerle dolu küçük bir liman.",
        "description_en": "A picturesque traditional fishing haven tucked away at the foot of a stunning viaduct, featuring small colorful boats and renowned seafood restaurants."
    },
    {
        "name": "Mucem (Avrupa ve Akdeniz Medeniyetleri Müzesi)",
        "name_en": "Mucem Museum",
        "area": "Vieux-Port",
        "category": "Müze",
        "tags": ["modern mimari", "akdeniz", "kültür", "panorama"],
        "distanceFromCenter": 0.8,
        "lat": 43.2953,
        "lng": 5.3619,
        "price": "medium",
        "rating": 4.8,
        "description": "Dantel gibi işlenmiş beton dış cephesiyle modern mimarinin başyapıtı. Akdeniz kültürüne adanmış bu müze, tarihi Fort Saint-Jean ile bir köprüyle birbirine bağlanır.",
        "description_en": "A stunning piece of contemporary architecture dedicated to Mediterranean cultures, linked by a high bridge to the historic Fort Saint-Jean."
    },
    {
        "name": "Fort Saint-Jean",
        "name_en": "Fort Saint-Jean",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["kale", "manzara", "bağlantı", "yürüyüş"],
        "distanceFromCenter": 0.8,
        "lat": 43.2953,
        "lng": 5.3619,
        "price": "free",
        "rating": 4.7,
        "description": "17. yüzyıldan kalma, limanı korumak için inşa edilmiş devasa kale. Şimdi ise muazzam bahçeleri ve Mucem'e uzanan asma köprüleriyle keyifli bir yürüyüş alanı.",
        "description_en": "A 17th-century fortification guarding the entrance to the Old Port, now a public space with Mediterranean gardens and spectacular harbor views."
    },
    {
        "name": "Cathédrale de la Major",
        "name_en": "Marseille Cathedral (La Major)",
        "area": "Joliette",
        "category": "Tarihi",
        "tags": ["katedral", "bizans", "görkemli", "mimari"],
        "distanceFromCenter": 1.2,
        "lat": 43.2997,
        "lng": 5.3650,
        "price": "free",
        "rating": 4.7,
        "description": "Çizgili kubbesi ve devasa yapısıyla Akdeniz'e yukarıdan bakan, Neo-Bizans tarzındaki bu katedral, Marseille'in en görkemli dini yapısıdır.",
        "description_en": "A monumental 19th-century cathedral overlooking the port, striking for its massive size and colorful Romanesque-Byzantine striped facade."
    },
    {
        "name": "Palais Longchamp",
        "name_en": "Palais Longchamp",
        "area": "Cinq-Avenues",
        "category": "Manzara",
        "tags": ["saray", "su", "anıt", "park"],
        "distanceFromCenter": 2.2,
        "lat": 43.3038,
        "lng": 5.3946,
        "price": "free",
        "rating": 4.9,
        "description": "Marseille'e suyun gelişini kutlamak için yapılmış muazzam bir anıt-saray. Görkemli fıskiyeleri, kolonatları ve arkasındaki geniş parkıyla kentin en güzel noktalarından biri.",
        "description_en": "A stunning 19th-century monument dedicated to water, featuring a grandiose fountain, majestic colonnades, and housing the city's Fine Arts museum."
    },
    {
        "name": "Vallon des Auffes (Viyadük)",
        "name_en": "Vallon des Auffes Viaduct",
        "area": "Endoume",
        "category": "Tarihi",
        "tags": ["mimari", "köprü", "manzara", "ikonik"],
        "distanceFromCenter": 2.5,
        "lat": 43.2858,
        "lng": 5.3510,
        "price": "free",
        "rating": 4.8,
        "description": "Limanın üzerinden geçen, kentin simgelerinden biridir. Altındaki balıkçı barınakları ve denizin turkuazıyla birleştiğinde muazzam bir kare sunar.",
        "description_en": "The monumental stone viaduct that frames the Vallon des Auffes, offering a dramatic backdrop to the traditional boats and seaside bars below."
    },
    {
        "name": "Corniche Kennedy",
        "name_en": "Corniche Kennedy",
        "area": "Sahil",
        "category": "Deneyim",
        "tags": ["manzara yolu", "koşu", "deniz", "bank"],
        "distanceFromCenter": 3.0,
        "lat": 43.2716,
        "lng": 5.3628,
        "price": "free",
        "rating": 4.8,
        "description": "Akdeniz boyunca uzanan, dünyanın en uzun bankına (3 km) ev sahipliği yapan sahil yolu. Gün batımı yürüyüşü ve spor için ideal.",
        "description_en": "A scenic coastal road stretching along the Mediterranean, home to 'the world's longest bench' and offering breathtaking views of the Frioul islands."
    },
    {
        "name": "Cours Julien (Grafiti Sokağı)",
        "name_en": "Cours Julien Graffiti District",
        "area": "Noailles",
        "category": "Deneyim",
        "tags": ["sokak sanatı", "bohem", "gece hayatı", "yaratıcı"],
        "distanceFromCenter": 0.8,
        "lat": 43.2943,
        "lng": 5.3830,
        "price": "free",
        "rating": 4.7,
        "description": "Marseille'in bohem ruhu. Rengarenk duvar resimleri, bağımsız kitapçıları, yerel tasarımcıları ve canlı barlarıyla kentin en yaratıcı mahallesidir.",
        "description_en": "A vibrant, bohemian hub of street art and creativity. Its pedestrian squares are filled with terraces, vintage shops, and incredible murals."
    },
    {
        "name": "Palais du Pharo",
        "name_en": "Pharo Palace",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["saray", "manzara", "bahçe", "liman giriş"],
        "distanceFromCenter": 1.2,
        "lat": 43.2943,
        "lng": 5.3582,
        "price": "free",
        "rating": 4.8,
        "description": "Napolyon III tarafından eşi için yaptırılan bu saray, limanın girişindeki bir tepede yer alır. Bahçesinden Vieux-Port ve Mucem'in kucaklaşmasını izlemek paha biçilemez.",
        "description_en": "Built by Napoleon III on a rocky promontory, this palace and its public gardens offer arguably the best overall view of the Old Port and the Joliette skyline."
    },
    {
        "name": "Abbaye Saint-Victor",
        "name_en": "Saint-Victor Abbey",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["manastır", "ortaçağ", "kript", "kutsal"],
        "distanceFromCenter": 0.7,
        "lat": 43.2903,
        "lng": 5.3655,
        "price": "low",
        "rating": 4.6,
        "description": "Marseille'in en eski dini merkezlerinden biri. Bir kale gibi görünen bu manastırın altındaki gizemli yeraltı mezarları (kriptler) binyıllık bir tarihe ışık tutar.",
        "description_en": "A former abbey with a church that looks like a fortress. Its 5th-century crypts are some of the oldest Christian sites in France."
    }
]

def enrich_marseille():
    filepath = 'assets/cities/marsilya.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update fillers in existing highlights
    fillers = {
        "Basilique Notre-Dame de la Garde": {
            "description": "Marseille'in 'İyi Annesi' (La Bonne Mère). Kentin en yüksek noktasında, altın heykeliyle şehri koruyan, eşsiz bir manzaraya sahip olan muazzam katedral.",
            "description_en": "The city's most famous landmark, a Neo-Byzantine basilica sitting atop the highest point in Marseille, topped with a golden statue of Mary."
        },
        "Old Port (Vieux-Port)": {
            "description": "2600 yıldır kentin kalbi. Balık pazarı, aynalı tavanı (L'Ombrière) ve yan yana dizilmiş balık lokantalarıyla Akdeniz'in en ikonik limanlarından biri.",
            "description_en": "The ancient heart of the city, now a pedestrianized harbor filled with yachts, fishing boats, and lively waterfront cafes."
        },
        "Le Panier district": {
            "description": "Marseille'in en eski mahallesi. Labirent gibi sokakları, asılı çamaşırları ve butik sanat galerileriyle tam bir Akdeniz klasiği.",
            "description_en": "The historic old quarter of Marseille, a steep and charming labyrinth of narrow streets filled with color, street art, and small artisan shops."
        },
        "Parc National des Calanques": {
            "description": "Turkuaz deniz ile bembeyaz kireçtaşının buluştuğu doğa harikası. Fiyortları andıran bu koylar, yürüyüş ve yüzme için eşsiz bir cennettir.",
            "description_en": "A spectacular national park of limestone sea cliffs and turquoise inlets, offering some of the best hiking and deep-sea swimming in Europe."
        },
        "Château d'If": {
            "description": "Monte Kristo Kontu romanına ilham veren tarihi ada hapishanesi. Vieux-Port'tan kısa bir tekne yolculuğuyla ulaşılabilen etkileyici bir yer.",
            "description_en": "The famous island fortress and former prison immortalized by Alexandre Dumas in 'The Count of Monte Cristo'."
        },
        "Palais de Longchamp": {
            "description": "Kente su getiren kanalın varış noktasında inşa edilmiş, İtalya'dan esintiler taşıyan muazzam bir anıt ve sanat merkezi.",
            "description_en": "A grandiose 19th-century palace built to celebrate the arrival of water into the city, housing several museums and a beautiful park."
        },
        "Vallon des Auffes": {
            "description": "Şehrin gürültüsünden uzak, viyadüğün altına gizlenmiş masalsı bir balıkçı köyü ve limanı. Marseille'in en romantik noktası.",
            "description_en": "A picturesque, secluded traditional fishing harbor nestled beneath a giant stone bridge, iconic for its authentic beauty."
        },
        "Corniche du Président-John-Fitzgerald-Kennedy": {
            "description": "Deniz kıyısı boyunca kıvrılan, muazzam kaleleri ve adaları izleyerek yürüyebileceğiniz kentin en uzun ve ferah sahil yolu.",
            "description_en": "A breathtaking coastal road stretching along the sea, featuring spectacular viewing points and some of the city's finest mansions."
        }
    }

    for h in data.get('highlights', []):
        if h['name'] in fillers:
            h['description'] = fillers[h['name']]['description']
            h['description_en'] = fillers[h['name']]['description_en']

    # 2. Add new highlights
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_marseille_batch1:
        if new_h['name'].lower() not in existing_names:
            # Add missing fields
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1549221165-276f7c181342?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    # 3. Handle duplicates or near-duplicates (e.g., Vallon des Auffes vs the existing one)
    # The cleanup script will do this better.

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_marseille()
print(f"Marseille now has {count} highlights.")
