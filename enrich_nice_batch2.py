import json
import os

new_nice_batch2 = [
    {
        "name": "Port Lympia",
        "name_en": "Port Lympia",
        "area": "Port",
        "category": "Manzara",
        "tags": ["liman", "yat", "renkli evler", "yürüyüş"],
        "distanceFromCenter": 1.2,
        "lat": 43.6980,
        "lng": 7.2854,
        "price": "free",
        "rating": 4.7,
        "description": "Cenova tarzı rengarenk binaları, lüks yatları ve balıkçı tekneleriyle Nice'in en karakterli ve fotojenik bölgelerinden biri.",
        "description_en": "One of the most beautiful historic ports in France, lined with pastel-colored buildings and traditional 'pointu' fishing boats."
    },
    {
        "name": "Mont Boron (Parque)",
        "name_en": "Mont Boron Park",
        "area": "Doğu Nice",
        "category": "Park",
        "tags": ["doğa", "yürüyüş", "manzara", "kale"],
        "distanceFromCenter": 2.5,
        "lat": 43.6983,
        "lng": 7.2992,
        "price": "free",
        "rating": 4.8,
        "description": "Nice ile Villefranche-sur-Mer arasındaki tepede yer alan, her iki körfezi de görebileceğiniz muazzam bir ormanlık park alanı.",
        "description_en": "A vast Mediterranean forest park offering spectacular hiking trails and 360-degree views of the French Riviera coastline."
    },
    {
        "name": "Place Garibaldi",
        "name_en": "Place Garibaldi",
        "area": "Centro/Port",
        "category": "Tarihi",
        "tags": ["meydan", "mimari", "barok", "sosyal"],
        "distanceFromCenter": 0.7,
        "lat": 43.7008,
        "lng": 7.2808,
        "price": "free",
        "rating": 4.7,
        "description": "Sarı binaları ve simetrik yapısıyla Nice'in en eski ve en asil meydanlarından biri. Port Lympia ile kentin ana arterlerini bağlar.",
        "description_en": "A majestic neoclassical square known for its uniform yellow buildings, vibrant cafes, and the central statue of Giuseppe Garibaldi."
    },
    {
        "name": "Avenue Jean Médecin",
        "name_en": "Jean Medecin Avenue",
        "area": "Centro",
        "category": "Alışveriş",
        "tags": ["tramvay", "alışveriş", "cadde", "merkezi"],
        "distanceFromCenter": 0.5,
        "lat": 43.7021,
        "lng": 7.2671,
        "price": "medium",
        "rating": 4.6,
        "description": "Nice'in ana alışveriş caddesi. Boydan boya uzanan tramvay yolu, mağazaları ve hareketli atmosferiyle kentin ticari kalbi.",
        "description_en": "The bustling main shopping artery of Nice, lined with international department stores, boutiques, and historic architecture."
    },
    {
        "name": "Villa Masséna",
        "name_en": "Villa Massena Museum",
        "area": "Promenade",
        "category": "Müze",
        "tags": ["saray", "tarih", "riviera", "bahçe"],
        "distanceFromCenter": 0.9,
        "lat": 43.6953,
        "lng": 7.2589,
        "price": "medium",
        "rating": 4.7,
        "description": "Promenade des Anglais üzerinde yer alan, Nice'in Belle Époque dönemine ait tarihini ve ihtişamını sergileyen muazzam bir müze-saray.",
        "description_en": "An architectural jewel on the Promenade des Anglais, dedicated to the history of the Riviera and the art of the 19th and early 20th centuries."
    },
    {
        "name": "Nice Opera House (Opéra de Nice)",
        "name_en": "Nice Opera House",
        "area": "Vieux Nice",
        "category": "Tarihi",
        "tags": ["opera", "sanat", "mimari", "tiyatro"],
        "distanceFromCenter": 0.4,
        "lat": 43.6954,
        "lng": 7.2725,
        "price": "low",
        "rating": 4.6,
        "description": "19. yüzyıldan kalma bu tarihi bina, sadece sunduğu performanslarla değil, muazzam iç dekorasyonuyla da kentin sanatsal simgelerinden biridir.",
        "description_en": "A beautiful 19th-century Italianate opera house located near the sea, showcasing ballet, opera, and classical music performances."
    },
    {
        "name": "Phoenix Park (Parc Phoenix)",
        "name_en": "Phoenix Park",
        "area": "Batı Nice",
        "category": "Park",
        "tags": ["sera", "hayvanat bahçesi", "doğa", "aile dostu"],
        "distanceFromCenter": 4.5,
        "lat": 43.6669,
        "lng": 7.2028,
        "price": "low",
        "rating": 4.5,
        "description": "Havalimanı yakınında, dünyanın en büyük seralarından birine ev sahipliği yapan, tropikal bitkiler ve kuşlarla dolu devasa bir botanik park.",
        "description_en": "A large botanical garden and zoo featuring one of the world's largest greenhouses, spanning seven hectares near the airport."
    },
    {
        "name": "Hôtel Le Negresco",
        "name_en": "Hotel Le Negresco",
        "area": "Promenade",
        "category": "Tarihi",
        "tags": ["lüks", "ikonik", "otel", "mimari"],
        "distanceFromCenter": 1.0,
        "lat": 43.6900,
        "lng": 7.2545,
        "price": "high",
        "rating": 4.9,
        "description": "Dünyanın en meşhur otellerinden biri. Pembe kubbesi ve müze gibi iç tasarımıyla Nice'in ihtişamlı geçmişinin en canlı kanıtı.",
        "description_en": "An iconic symbol of the French Riviera, this historic luxury hotel is a work of art in itself, featuring an incredible private art collection."
    },
    {
        "name": "Villefranche-sur-Mer Viewpoint",
        "name_en": "Villefranche Viewpoint",
        "area": "Corniche",
        "category": "Manzara",
        "tags": ["körfez", "deniz", "manzara", "yol"],
        "distanceFromCenter": 3.5,
        "lat": 43.7076,
        "lng": 7.3160,
        "price": "free",
        "rating": 4.9,
        "description": "Nice'ten Monaco yönüne giderken, Villefranche körfezinin o meşhur turkuaz ve turuncu evlerle dolu manzarasını en iyi görebileceğiniz nokta.",
        "description_en": "A roadside viewpoint on the Boulevard Napoléon III offering the most famous postcard view of the Villefranche-sur-Mer bay."
    },
    {
        "name": "Confiserie Florian",
        "name_en": "Confiserie Florian",
        "area": "Port",
        "category": "Deneyim",
        "tags": ["tatlı", "reçel", "fabrika turu", "lokal"],
        "distanceFromCenter": 1.3,
        "lat": 43.6985,
        "lng": 7.2845,
        "price": "medium",
        "rating": 4.7,
        "description": "Nice'in ünlü çiçeklerinden ve meyvelerinden reçel, şekerleme ve çikolata üreten tarihi imalathane. Fabrika turu yapabilirsiniz.",
        "description_en": "A historic confectionery by the port where you can watch how crystallized flowers and artisanal jams are made using local ingredients."
    },
    {
        "name": "Marché aux Fleurs (Flower Market)",
        "name_en": "Flower Market",
        "area": "Vieux Nice",
        "category": "Alışveriş",
        "tags": ["pazar", "çiçek", "yerel", "fotojenik"],
        "distanceFromCenter": 0.5,
        "lat": 43.6958,
        "lng": 7.2730,
        "price": "low",
        "rating": 4.8,
        "description": "Cours Saleya üzerinde her sabah kurulan, Nice'in renklerini ve kokularını en iyi hissedebileceğiniz dünyaca ünlü çiçek pazarı.",
        "description_en": "The soul of Nice; a vibrant, daily open-air market dedicated to Mediterranean flowers, crafts, and Provençal delicacies."
    },
    {
        "name": "Palais Lascaris",
        "name_en": "Lascaris Palace",
        "area": "Vieux Nice",
        "category": "Müze",
        "tags": ["saray", "enstrüman", "barok", "mimari"],
        "distanceFromCenter": 0.6,
        "lat": 43.6975,
        "lng": 7.2763,
        "price": "medium",
        "rating": 4.6,
        "description": "17. yüzyıldan kalma aristokrat bir saray. İçindeki muazzam freskler ve dünyaca ünlü antika müzik aletleri koleksiyonuyla büyüleyici.",
        "description_en": "A magnificent 17th-century Baroque palace in the Old Town, housing an extraordinary collection of antique musical instruments."
    },
    {
        "name": "Place Rossetti",
        "name_en": "Place Rossetti",
        "area": "Vieux Nice",
        "category": "Manzara",
        "tags": ["meydan", "katedral", "dondurma", "sosyal"],
        "distanceFromCenter": 0.5,
        "lat": 43.6972,
        "lng": 7.2755,
        "price": "free",
        "rating": 4.8,
        "description": "Katedralin hemen önünde yer alan, Nice'in en canlı meydanı. Dondurmacıları, fıskiyesi ve teraslarıyla kentin gerçek ruhu burada.",
        "description_en": "The quintessential piazza of Old Nice, home to the Cathedral, local gelaterias, and a lively Mediterranean atmosphere."
    },
    {
        "name": "Villa Arson",
        "name_en": "Villa Arson",
        "area": "Castellane",
        "category": "Müze",
        "tags": ["sanat okulu", "modern", "bahçe", "brütalist"],
        "distanceFromCenter": 3.0,
        "lat": 43.7205,
        "lng": 7.2525,
        "price": "free",
        "rating": 4.5,
        "description": "Bir sanat okulu ve modern sanat merkezi. İlginç brütalist mimarisi ve sessiz bahçeleriyle Nice'in saklı kalmış bir cevheri.",
        "description_en": "A national center for contemporary art and a prestigious art school, set in a villa with unique brutalist gardens and galleries."
    },
    {
        "name": "Grotte du Lazaret",
        "name_en": "Lazaret Cave",
        "area": "Port / Mont Boron",
        "category": "Tarihi",
        "tags": ["mağara", "tarih öncesi", "arkeoloji", "deniz"],
        "distanceFromCenter": 2.0,
        "lat": 43.6895,
        "lng": 7.2915,
        "price": "low",
        "rating": 4.3,
        "description": "Limanın yakınında yer alan, 160.000 yıl öncesine dayanan insan izlerinin bulunduğu tarih öncesi bir mağara ve müze alanı.",
        "description_en": "An archaeological site and prehistoric cave dating back 160,000 years, offering a fascinating look at the early history of humans in Europe."
    },
    {
        "name": "Canal de l'Uve",
        "name_en": "Canal de l'Uve",
        "area": "Centro",
        "category": "Deneyim",
        "tags": ["su yolu", "gizli", "yürüyüş", "doğa"],
        "distanceFromCenter": 1.5,
        "lat": 43.7050,
        "lng": 7.2750,
        "price": "free",
        "rating": 4.4,
        "description": "Kentin içinden gizlice akan eski bir su kanalı boyunca uzanan yürüyüş yolu. Turistsiz, sakin bir rota arayanlar için.",
        "description_en": "A local's hidden secret; follow parts of this old irrigation canal for a quiet and shaded walk away from the tourist crowds."
    },
    {
        "name": "Marche Garibaldi (Antika)",
        "name_en": "Garibaldi Antique Market",
        "area": "Garibaldi",
        "category": "Alışveriş",
        "tags": ["bit pazarı", "antika", "retro", "yerel"],
        "distanceFromCenter": 0.7,
        "lat": 43.7010,
        "lng": 7.2810,
        "price": "low",
        "rating": 4.6,
        "description": "Her ayın belirli günlerinde Place Garibaldi'de kurulan, antikalardan eski kitaplara kadar pek çok hazinenin bulunduğu bit pazarı.",
        "description_en": "A monthly open-air vintage market in the heart of Garibaldi Square, perfect for finding unique Riviera memorabilia and antiques."
    },
    {
        "name": "Quai des États-Unis",
        "name_en": "Quai des Etats-Unis",
        "area": "Promenade / Port",
        "category": "Manzara",
        "tags": ["sahil", "yürüyüş", "balık lokantaları", "deniz"],
        "distanceFromCenter": 0.4,
        "lat": 43.6950,
        "lng": 7.2750,
        "price": "free",
        "rating": 4.7,
        "description": "Promenade des Anglais'nin bir uzantısı olan bu rıhtım, Vieux Nice'in tam kıyısında yer alır ve balık restoranlarıyla ünlüdür.",
        "description_en": "The continuation of the main promenade along the edge of the Old Town, lined with seafood restaurants and beach clubs."
    },
    {
        "name": "Rue Bonaparte (Hipster Sokağı)",
        "name_en": "Rue Bonaparte",
        "area": "Port / Garibaldi",
        "category": "Deneyim",
        "tags": ["hipster", "kafe", "bar", "gece hayatı"],
        "distanceFromCenter": 0.8,
        "lat": 43.7000,
        "lng": 7.2830,
        "price": "medium",
        "rating": 4.8,
        "description": "Nice'in en 'cool' sokağı. Tasarım dükkanları, şık kafeleri ve butik barlarıyla kentin modern yüzünün temsilcisi.",
        "description_en": "Nice’s version of a trendy Brooklyn street, filled with artisanal coffee shops, unique concept stores, and the best night bars."
    },
    {
        "name": "Eglise Sainte-Jeanne d'Arc",
        "name_en": "Sainte-Jeanne d'Arc Church",
        "area": "Liberation",
        "category": "Tarihi",
        "tags": ["modern kilise", "fütüristik", "mimari", "beyaz"],
        "distanceFromCenter": 1.7,
        "lat": 43.7135,
        "lng": 7.2625,
        "price": "free",
        "rating": 4.5,
        "description": "Bembeyaz fütüristik yapısı ve ilginç geometrik kubbeleriyle alışıldık kiliselerden çok farklı olan modern bir mimari başyapıt.",
        "description_en": "A unique, futurist Catholic church built in the 1920s, known for its striking white elliptical domes and avant-garde interior."
    },
    {
        "name": "Port Lympia (Sarı Binalar)",
        "name_en": "Port Lympia Architecture",
        "area": "Port",
        "category": "Tarihi",
        "tags": ["mimari", "renkli", "liman", "fotoğraf"],
        "distanceFromCenter": 1.2,
        "lat": 43.6990,
        "lng": 7.2860,
        "price": "free",
        "rating": 4.7,
        "description": "Limanın etrafındaki Cenova tarzı o meşhur sarı ve turuncu binaların oluşturduğu bütünlük, şehre İtalyan havası katan en önemli unsurdur.",
        "description_en": "The iconic yellow Genoese-style housing surrounding the port, a testament to Nice's historic and architectural ties to Italy."
    },
    {
        "name": "Rauba Capeu (Nice Yazısı)",
        "name_en": "I Love Nice Sign",
        "area": "Promenade / Port",
        "category": "Manzara",
        "tags": ["heykel", "fotoğraf noktası", "deniz", "manzara"],
        "distanceFromCenter": 0.9,
        "lat": 43.6942,
        "lng": 7.2805,
        "price": "free",
        "rating": 4.9,
        "description": "Deniz kıyısındaki kayalıkların üzerinde yer alan devasa 'I Love Nice' yazısı. Şehrin en popüler selfi ve manzara noktası.",
        "description_en": "The most famous photo spot in town, where the giant 'I Love Nice' letters stand against the backdrop of the turquoise Mediterranean."
    },
    {
        "name": "Museo de Paleontología Humana de Terra Amata",
        "name_en": "Terra Amata Museum",
        "area": "Port",
        "category": "Müze",
        "tags": ["arkeoloji", "tarih öncesi", "kazı", "insanlık"],
        "distanceFromCenter": 1.4,
        "lat": 43.6981,
        "lng": 7.2890,
        "price": "low",
        "rating": 4.4,
        "description": "400.000 yıl öncesine dayanan dünyanın bilinen en eski ateş izlerine ve insan yerleşim kalıntılarına ev sahipliği yapan müze.",
        "description_en": "A museum built directly over an archaeological site where some of the world's oldest hearths and human dwellings were discovered."
    },
    {
        "name": "Marché de la Libération",
        "name_en": "Liberation Market",
        "area": "Liberation",
        "category": "Alışveriş",
        "tags": ["market", "yerel", "sebze-meyve", "ucuza"],
        "distanceFromCenter": 1.8,
        "lat": 43.7115,
        "lng": 7.2645,
        "price": "low",
        "rating": 4.8,
        "description": "Turistlerin pek gelmediği, gerçek Nicelilerin alışveriş yaptığı kentin en büyük ve en taze açık hava gıda pazarı.",
        "description_en": "The largest fruit and vegetable market in Nice, where prices are lower than Cours Saleya and the atmosphere is 100% local."
    },
    {
        "name": "Galerie des Ponchettes",
        "name_en": "Galerie des Ponchettes",
        "area": "Promenade / Old Town",
        "category": "Müze",
        "tags": ["sanat galerisi", "modern", "belediye galerisi", "ücretsiz"],
        "distanceFromCenter": 0.4,
        "lat": 43.6948,
        "lng": 7.2740,
        "price": "free",
        "rating": 4.5,
        "description": "Quai des États-Unis üzerindeki bu şık beyaz bina, dönemsel modern sanat sergilerine ev sahipliği yapar ve girişi genellikle ücretsizdir.",
        "description_en": "A sleek seaside art gallery showcasing temporary contemporary exhibitions, conveniently located between the sea and the Old Town."
    }
]

def enrich_nice_batch2():
    filepath = 'assets/cities/nice.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_nice_batch2:
        if new_h['name'].lower() not in existing_names:
            # Add missing fields
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1533619239233-6280475a634a?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_nice_batch2()
print(f"Nice now has {count} highlights.")
