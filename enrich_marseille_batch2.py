import json
import os

new_marseille_batch2 = [
    {
        "name": "Les Calanques (En-Vau)",
        "name_en": "Calanque d'En-Vau",
        "area": "Parc National des Calanques",
        "category": "Manzara",
        "tags": ["fiyort", "yüzme", "tırmanış", "doğa"],
        "distanceFromCenter": 12.0,
        "lat": 43.2025,
        "lng": 5.5005,
        "price": "free",
        "rating": 5.0,
        "description": "Marseille'in en meşhur ve en güzel koyu. Bembeyaz dik kireçtaşı duvarları ve cam gibi turkuaz suyuyla ulaşması zor ama ödülü paha biçilemez bir cennet.",
        "description_en": "Commonly cited as the most beautiful of the Calanques, this dramatic inlet features towering white limestone cliffs and crystal-clear turquoise waters."
    },
    {
        "name": "Frioul Islands (Îles du Frioul)",
        "name_en": "Frioul Islands",
        "area": "Frioul",
        "category": "Manzara",
        "tags": ["ada", "deniz", "yürüyüş", "kale"],
        "distanceFromCenter": 4.0,
        "lat": 43.2786,
        "lng": 5.3078,
        "price": "low",
        "rating": 4.8,
        "description": "Limandan kalkan teknelerle ulaşılan, bembeyaz kayalıklar ve masmavi koylarla kaplı dört adadan oluşan takımada. Sakinlik ve doğa arayanlar için.",
        "description_en": "An archipelago consisting of four small islands off the coast, known for their unique flora, rare bird species, and excellent swimming spots."
    },
    {
        "name": "Stade Vélodrome (Orange Vélodrome)",
        "name_en": "Stade Velodrome",
        "area": "Sainte-Marguerite",
        "category": "Deneyim",
        "tags": ["futbol", "stadyum", "om", "mimari"],
        "distanceFromCenter": 3.5,
        "lat": 43.2696,
        "lng": 5.3956,
        "price": "medium",
        "rating": 4.9,
        "description": "Olympique de Marseille'in evi. Modern ve dalgalı çatısıyla mimari bir ikon olan bu stadın tutkulu atmosferi dünyaca ünlüdür.",
        "description_en": "The home ground of Olympique de Marseille, iconic for its unique undulating roof and the legendary atmosphere of its 67,000 passionate fans."
    },
    {
        "name": "L'Estaque",
        "name_en": "L'Estaque Village",
        "area": "Kuzey Marseille",
        "category": "Tarihi",
        "tags": ["sanat", "cezanne", "liman", "lokal lezzet"],
        "distanceFromCenter": 8.0,
        "lat": 43.3614,
        "lng": 5.3142,
        "price": "free",
        "rating": 4.7,
        "description": "Cézanne ve Braque gibi ressamlara ilham vermiş eski bir balıkçı köyü. Panisse ve Chichi Frégi gibi yerel lezzetleri tatmak için kentin en kuzey durağı.",
        "description_en": "A historic harbor district that inspired Impressionist and Cubist painters, still preserving its village charm and authentic culinary specialties."
    },
    {
        "name": "La Vieille Charité",
        "name_en": "Vieille Charite Cultural Center",
        "area": "Le Panier",
        "category": "Müze",
        "tags": ["mimari", "barok", "sergi", "avlu"],
        "distanceFromCenter": 1.0,
        "lat": 43.3003,
        "lng": 5.3678,
        "price": "medium",
        "rating": 4.8,
        "description": "Eski bir yetimhane ve hastane binası olan bu 17. yüzyıl barok başyapıtı, şimdi kentin en önemli sergi merkezlerinden biridir.",
        "description_en": "A former almshouse with a stunning domed chapel and a large internal courtyard, now housing museums and temporary art exhibitions."
    },
    {
        "name": "Grotte Cosquer (Cosquer Méditerranée)",
        "name_en": "Cosquer Cave Museum",
        "area": "Joliette",
        "category": "Müze",
        "tags": ["tarih öncesi", "mağara", "sergi", "deniz altı"],
        "distanceFromCenter": 1.0,
        "lat": 43.3000,
        "lng": 5.3600,
        "price": "medium",
        "rating": 4.7,
        "description": "Deniz altında saklı olan 30.000 yıllık Cosquer mağarasının birebir reprodüksiyonu. Tarih öncesi çizimleri keşfetmek için inanılmaz bir sanal deneyim.",
        "description_en": "A fascinating life-sized replica of an underwater prehistoric cave, showcasing magnificent Upper Paleolithic cave drawings and engravings."
    },
    {
        "name": "Musée d'Histoire de Marseille",
        "name_en": "Marseille History Museum",
        "area": "Belsunce",
        "category": "Müze",
        "tags": ["arkeoloji", "tarih", "liman", "antik"],
        "distanceFromCenter": 0.5,
        "lat": 43.2978,
        "lng": 5.3756,
        "price": "medium",
        "rating": 4.6,
        "description": "Avrupa'nın en büyük kent tarihi müzelerinden biri. Antik Yunan liman kalıntıları ve 2600 yıllık Marseille tarihini bir alışveriş merkezinin tam yanında keşfedin.",
        "description_en": "Built beside an archaeological site displaying remnants of the ancient Greek port, this museum beautifully details the city's 2,600-year history."
    },
    {
        "name": "Place aux Huiles",
        "name_en": "Place aux Huiles",
        "area": "Vieux-Port",
        "category": "Deneyim",
        "tags": ["meydan", "teras", "restoran", "sosyal"],
        "distanceFromCenter": 0.3,
        "lat": 43.2928,
        "lng": 5.3717,
        "price": "medium",
        "rating": 4.7,
        "description": "Vieux-Port'un hemen arkasında, kanal tarzı mimarisi ve teraslarıyla akşamları kentin en popüler buluşma ve yemek noktalarından biri.",
        "description_en": "A bustling urban square near the harbor, lined with terrace restaurants and bars, famous for its lively Mediterranean night scene."
    },
    {
        "name": "Les Terrasses du Port",
        "name_en": "Terrasses du Port Shopping Mall",
        "area": "Joliette",
        "category": "Alışveriş",
        "tags": ["modern", "manzara", "terast", "deniz"],
        "distanceFromCenter": 1.5,
        "lat": 43.3072,
        "lng": 5.3653,
        "price": "medium",
        "rating": 4.6,
        "description": "Marseille'in en şık alışveriş merkezidir. 260 metrelik devasa terası, Akdeniz'e tam anlamıyla hakim bir manzara sunar.",
        "description_en": "An upscale shopping center in the revitalized docks area, featuring a massive sea-facing terrace with panoramic views of the cruise ships."
    },
    {
        "name": "Musée Cantini",
        "name_en": "Cantini Museum",
        "area": "Centro",
        "category": "Müze",
        "tags": ["modern sanat", "resim", "konak", "sanat"],
        "distanceFromCenter": 0.5,
        "lat": 43.2922,
        "lng": 5.3781,
        "price": "medium",
        "rating": 4.5,
        "description": "Şık bir 17. yüzyıl konağında yer alan, 1900-1960 arası modern sanata ve sürrealizme odaklanan kentin en köklü sanat galerilerinden biridir.",
        "description_en": "Housed in an elegant private mansion, this museum specializes in modern art and is particularly noted for its surrealist collections."
    },
    {
        "name": "Vieux-Port (Ombrière)",
        "name_en": "Mirror Pavilion (L'Ombriere)",
        "area": "Vieux-Port",
        "category": "Manzara",
        "tags": ["modern", "ayna", "fotoğraf", "norman foster"],
        "distanceFromCenter": 0.1,
        "lat": 43.2952,
        "lng": 5.3745,
        "price": "free",
        "rating": 4.8,
        "description": "Norman Foster tarafından tasarlanan devasa aynalı tavan. Altında durup kendi yansımanızı ve limanın hareketini izlemek bir Marseille klasiği.",
        "description_en": "A massive polished steel canopy designed by Norman Foster, functioning as a giant mirror that creates incredible reflections of life on the harbor."
    },
    {
        "name": "Marché de Noailles",
        "name_en": "Noailles Market (Le Marché du Soleil)",
        "area": "Noailles",
        "category": "Alışveriş",
        "tags": ["baharat", "multikültürel", "egzotik", "pazar"],
        "distanceFromCenter": 0.6,
        "lat": 43.2970,
        "lng": 5.3795,
        "price": "low",
        "rating": 4.7,
        "description": "Marseille'in 'Doğu kapısı.' Baharat kokuları, egzotik meyveler ve her dilden seslerin yükseldiği en renkli ve kaotik gıda pazarı.",
        "description_en": "Often called 'The Belly of Marseille,' this bustling, multi-ethnic market is famous for its North African spices and vibrant atmosphere."
    },
    {
        "name": "Maison de l'Artisanat et des Métiers d'Art",
        "name_en": "House of Crafts and Applied Arts",
        "area": "Vieux-Port",
        "category": "Deneyim",
        "tags": ["el sanatları", "sergi", "yerel", "sanat"],
        "distanceFromCenter": 0.3,
        "lat": 43.2925,
        "lng": 5.3725,
        "price": "free",
        "rating": 4.5,
        "description": "Eski bir tersane binasında yer alan, yerel zanaatkarların el emeği ürünlerini ve tasarım eserlerini sergileyen ücretsiz bir galeri.",
        "description_en": "Housed in 18th-century former royal dock buildings, this space celebrates traditional and contemporary craftsmanship from the region."
    },
    {
        "name": "Le Panier (Grafiti ve Sanat)",
        "name_en": "Le Panier Art Walk",
        "area": "Le Panier",
        "category": "Deneyim",
        "tags": ["sokak sanatı", "grafiti", "keşif", "renkli"],
        "distanceFromCenter": 1.0,
        "lat": 43.2985,
        "lng": 5.3665,
        "price": "free",
        "rating": 4.9,
        "description": "Le Panier'nin her köşesinde karşınıza çıkan devasa grafitiler ve küçük sanat atölyeleri. Mahallenin labirentlerinde kaybolurken kenti okumak gibi.",
        "description_en": "The steep narrow streets of Le Panier are a living canvas, where world-class street art blends with small boutique galleries and ateliers."
    },
    {
        "name": "Plage des Catalans",
        "name_en": "Catalans Beach",
        "area": "Centro",
        "category": "Deneyim",
        "tags": ["plaj", "kum", "yüzme", "merkezi"],
        "distanceFromCenter": 1.8,
        "lat": 43.2905,
        "lng": 5.3535,
        "price": "free",
        "rating": 4.4,
        "description": "Kentin en merkezi kum plajı. Vieux-Port'tan yürüyerek ulaşılabilen, voleybol sahaları ve canlı atmosferiyle gençlerin favorisi.",
        "description_en": "The closest sandy beach to the city center, a very popular spot for beach volleyball and a quick dip in the Mediterranean."
    },
    {
        "name": "Unité d'Habitation (Le Corbusier)",
        "name_en": "The Corbusier Building (La Cité Radieuse)",
        "area": "Sainte-Anne",
        "category": "Tarihi",
        "tags": ["modern mimari", "le corbusier", "ikonik", "beton"],
        "distanceFromCenter": 4.2,
        "lat": 43.2614,
        "lng": 5.3964,
        "price": "low",
        "rating": 4.8,
        "description": "Modern mimarinin babası Le Corbusier tarafından tasarlanan 'Dikey Şehir'. Brütalist mimarinin dünyadaki en önemli örneği olan bir bina-mahalle.",
        "description_en": "An iconic piece of 20th-century architecture and a UNESCO World Heritage site, designed as a self-contained vertical village."
    },
    {
        "name": "Frioul (Fort de Ratonneau)",
        "name_en": "Ratonneau Fort",
        "area": "Frioul Islands",
        "category": "Tarihi",
        "tags": ["kale", "ada", "tarih", "manzara"],
        "distanceFromCenter": 4.5,
        "lat": 43.2805,
        "lng": 5.3045,
        "price": "free",
        "rating": 4.6,
        "description": "Frioul adalarından biri olan Ratonneau üzerindeki tarihi kalıntılar. Adanın en yüksek noktasında, Marseille kıyılarının en geniş açılı manzarasını sunar.",
        "description_en": "A historic fortress perched on the cliffs of Frioul Island, accessible by ferry and offering 360-degree maritime views."
    },
    {
        "name": "Vallon des Auffes (Deniz Havuzu)",
        "name_en": "Vallon des Auffes Swimming Pool",
        "area": "Endoume",
        "category": "Deneyim",
        "tags": ["yüzme", "deniz havuzu", "lokal", "eğlence"],
        "distanceFromCenter": 2.6,
        "lat": 43.2852,
        "lng": 5.3505,
        "price": "free",
        "rating": 4.8,
        "description": "Limanın hemen çıkışındaki kayalıkların arasında yer alan, denizden gelen taze suyla beslenen yerel bir 'havuz' alanı.",
        "description_en": "A natural enclave among the rocks where residents of the Vallon jump into the clear Mediterranean waters, a quintessential local summer spot."
    },
    {
        "name": "Musée de la Légion Étrangère",
        "name_en": "Foreign Legion Museum",
        "area": "Aubagne (Dış)",
        "category": "Müze",
        "tags": ["askeri tarih", "efsane", "tarih", "koleksiyon"],
        "distanceFromCenter": 15.0,
        "lat": 43.2925,
        "lng": 5.5535,
        "price": "free",
        "rating": 4.7,
        "description": "Dünyanın en gizemli askeri birliklerinden biri olan Fransız Yabancılar Lejyonu'nun tarihini ve kahramanlık öykülerini anlatan resmi müze.",
        "description_en": "Located just outside Marseille in Aubagne, this museum details the epic and mysterious history of the French Foreign Legion."
    },
    {
        "name": "Marché aux Puces de Marseille",
        "name_en": "Marseille Flea Market",
        "area": "Kuzey Marseille",
        "category": "Alışveriş",
        "tags": ["bit pazarı", "antika", "retro", "dev pazar"],
        "distanceFromCenter": 5.5,
        "lat": 43.3380,
        "lng": 5.3580,
        "price": "low",
        "rating": 4.5,
        "description": "Kentin kuzeyinde yer alan devasa bir alan. Antikalardan eski giysilere, yerel pazardan ikinci el eşyalara kadar her şeyin bulunduğu gerçek bir pazar.",
        "description_en": "One of the largest flea markets in southern France, a massive indoor and outdoor maze of antiques, vintage finds, and fresh local produce."
    },
    {
        "name": "Rue de la République (Mimari)",
        "name_en": "Republic Street Architecture",
        "area": "Centro / Joliette",
        "category": "Tarihi",
        "tags": ["cadde", "haussmann", "mimari", "yürüyüş"],
        "distanceFromCenter": 0.8,
        "lat": 43.2980,
        "lng": 5.3725,
        "price": "free",
        "rating": 4.6,
        "description": "Paris'teki caddeleri andıran 'Haussmann' tarzı binalarıyla Marseille'in en görkemli ve şık caddesi. Limanı modern Joliette bölgesine bağlar.",
        "description_en": "A grand 19th-century boulevard connecting the Old Port to the docks, famous for its elegant uniform neoclassical architecture."
    },
    {
        "name": "Anse de Maldormé",
        "name_en": "Maldorme Cove",
        "area": "Endoume",
        "category": "Manzara",
        "tags": ["koy", "gizli", "deniz", "sessiz"],
        "distanceFromCenter": 3.2,
        "lat": 43.2805,
        "lng": 5.3525,
        "price": "free",
        "rating": 4.9,
        "description": "Corniche üzerinde saklı kalmış, turkuaz suyu ve falezleriyle Marseille'in en romantik ve az bilinen küçük körfezlerinden biri.",
        "description_en": "A tiny, secluded rocky inlet tucked away behind the Corniche, offering a peaceful and scenic swimming spot with crystal-clear water."
    },
    {
        "name": "Stade Vélodrome (Müze & Tur)",
        "name_en": "OM Stadium Tour",
        "area": "Sainte-Marguerite",
        "category": "Deneyim",
        "tags": ["stadyum turu", "futbol", "OM", "spor"],
        "distanceFromCenter": 3.6,
        "lat": 43.2690,
        "lng": 5.3960,
        "price": "medium",
        "rating": 4.8,
        "description": "Marseille'in kalbinin attığı yer olan efsanevi Vélodrome stadyumunun soyunma odalarını, saha kenarını ve müzesini keşfedebileceğiniz özel tur.",
        "description_en": "A behind-the-scenes look at one of Europe’s most passionate stadiums, including the players' tunnel, dressing rooms, and the club museum."
    },
    {
        "name": "Prado Sahilleri (Plages du Prado)",
        "name_en": "Prado Beaches",
        "area": "Güney Marseille",
        "category": "Park",
        "tags": ["sahil", "yeşil alan", "yüzme", "spor"],
        "distanceFromCenter": 4.5,
        "lat": 43.2550,
        "lng": 5.3750,
        "price": "free",
        "rating": 4.5,
        "description": "Geniş çimenlik alanları ve deniziyle kentin güneyindeki ana rekreasyon bölgesi. Rüzgar sörfü yapanları ve güneşlenen Marseille yerlilerini görebilirsiniz.",
        "description_en": "A wide stretch of man-made seaside parks and pebble beaches, providing a massive space for outdoor activities and family leisure."
    },
    {
        "name": "L'Hôtel de Ville (Belediye Binası)",
        "name_en": "Marseille City Hall",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["mimari", "liman", "barok", "merkezi"],
        "distanceFromCenter": 0.4,
        "lat": 43.2965,
        "lng": 5.3698,
        "price": "free",
        "rating": 4.6,
        "description": "Vieux-Port'un hemen kuzey kıyısındaki bu şık 17. yüzyıl binası, Marseille'in barok mimarisinin en güzel örneklerinden biridir.",
        "description_en": "Overlooking the Old Port, this elegant 17th-century Baroque building is one of the few structures that survived the destruction of the port in 1943."
    }
]

def enrich_marseille_batch2():
    filepath = 'assets/cities/marsilya.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_marseille_batch2:
        if new_h['name'].lower() not in existing_names:
            # Add missing fields
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1549221165-276f7c181342?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    # We need to make sure we have at least 100
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_marseille_batch2()
print(f"Marseille now has {count} highlights.")
