import json
import os

new_marseille_final = [
    {
        "name": "Rue de Rome",
        "name_en": "Rue de Rome",
        "area": "Centro",
        "category": "Alışveriş",
        "tags": ["tramvay", "alışveriş", "cadde", "tarihi"],
        "distanceFromCenter": 0.4,
        "lat": 43.2925,
        "lng": 5.3785,
        "price": "medium",
        "rating": 4.5,
        "description": "Marseille'in en uzun ve en eski alışveriş caddelerinden biri. Boydan boya uzanan tramvayı ve tarihi binalarıyla kentin ana damarlarından.",
        "description_en": "One of Marseille's longest shopping boulevards, featuring grand 19th-century architecture and the city's main tram line."
    },
    {
        "name": "Église de la Trinité",
        "name_en": "Trinity Church",
        "area": "Noailles / La Plaine",
        "category": "Tarihi",
        "tags": ["kilise", "tarih", "mimari", "merkezi"],
        "distanceFromCenter": 0.8,
        "lat": 43.2955,
        "lng": 5.3855,
        "price": "free",
        "rating": 4.6,
        "description": "La Plaine yakınındaki bu tarihi kilise, özellikle pazar günleri kurulan pazarın hemen yanında kentin sosyal ve dini hayatını birleştirir.",
        "description_en": "An important local church near La Plaine, standing at a crossroads of the city's multicultural and historic districts."
    },
    {
        "name": "Parc Borély (Gül Bahçesi)",
        "name_en": "Borely Park Rose Garden",
        "area": "Güney Marseille",
        "category": "Park",
        "tags": ["gül bahçesi", "botanik", "romantik", "park"],
        "distanceFromCenter": 4.6,
        "lat": 43.2595,
        "lng": 5.3810,
        "price": "free",
        "rating": 4.8,
        "description": "Parc Borély içindeki bu muazzam gül bahçesi, yüzlerce çeşit gül ve heykelleriyle kentin en romantik saklanma noktalarından biridir.",
        "description_en": "The stunning botanical rose garden located within Parc Borély, featuring rare varieties and perfectly manicured paths."
    },
    {
        "name": "Vieux-Port (Balık Pazarı)",
        "name_en": "Old Port Fish Market",
        "area": "Vieux-Port",
        "category": "Deneyim",
        "tags": ["balık pazarı", "lokal", "taze", "kültür"],
        "distanceFromCenter": 0.1,
        "lat": 43.2955,
        "lng": 5.3750,
        "price": "medium",
        "rating": 4.8,
        "description": "Her sabah kıyıya yanaşan teknelerden taze balık alabileceğiniz, Marseille'in 2600 yıllık balıkçılık geleneğinin hala yaşadığı en canlı nokta.",
        "description_en": "A daily Marseille institution where fishermen sell their morning catch directly from their boats on the quays of the Old Port."
    },
    {
        "name": "Musée des Beaux-Arts",
        "name_en": "Museum of Fine Arts",
        "area": "Cinq-Avenues",
        "category": "Müze",
        "tags": ["sanat", "resim", "saray", "klasik"],
        "distanceFromCenter": 2.2,
        "lat": 43.3040,
        "lng": 5.3940,
        "price": "medium",
        "rating": 4.7,
        "description": "Palais Longchamp'ın sol kanadında yer alan, 16. yüzyıldan 19. yüzyıla kadar olan Avrupa resim ve heykel sanatının seçkin örneklerini barındıran müze.",
        "description_en": "The oldest museum in Marseille, located in the Palais Longchamp, featuring masters of Italian, French, and Flemish painting."
    },
    {
        "name": "Musée d'Archéologie Méditerranéenne",
        "name_en": "Mediterranean Archaeology Museum",
        "area": "Le Panier",
        "category": "Müze",
        "tags": ["arkeoloji", "mısır", "antik", "tarih"],
        "distanceFromCenter": 1.0,
        "lat": 43.3005,
        "lng": 5.3680,
        "price": "medium",
        "rating": 4.7,
        "description": "La Vieille Charité içinde bulunan, özellikle Mısır koleksiyonu ve antik Akdeniz uygarlıklarına ait eserleriyle ünlü müze.",
        "description_en": "A significant museum focused on Egypt and regional archaeology, housed in the magnificent Vieille Charité complex."
    },
    {
        "name": "Phare de Sainte-Marie",
        "name_en": "Sainte-Marie Lighthouse",
        "area": "Joliette",
        "category": "Manzara",
        "tags": ["deniz feneri", "liman", "mimari", "manzara"],
        "distanceFromCenter": 2.5,
        "lat": 43.3100,
        "lng": 5.3550,
        "price": "free",
        "rating": 4.5,
        "description": "Marseille liman bölgesinin kuzeyinde yer alan, bembeyaz kireçtaşından yapılmış tarihi ve şık bir deniz feneri.",
        "description_en": "A beautiful 19th-century lighthouse built from local white limestone, marking the northern end of Marseille's industrial docks."
    },
    {
        "name": "Parc Pastré",
        "name_en": "Pastre Park",
        "area": "Güney Marseille",
        "category": "Park",
        "tags": ["doğa", "yürüyüş", "saray", "göl"],
        "distanceFromCenter": 6.0,
        "lat": 43.2380,
        "lng": 5.3720,
        "price": "free",
        "rating": 4.9,
        "description": "Calanques milli parkının kapısı sayılan, içinde üç farklı şato ve devasa göletler barındıran Marseille'in en geniş sahil parkı.",
        "description_en": "A vast coastal park spanning 120 hectares, serving as a gateway to the Calanques and featuring castles, canals, and woodlands."
    },
    {
        "name": "Le Panier (Eski Fırın sokağı)",
        "name_en": "Le Panier Bakery Alleys",
        "area": "Le Panier",
        "category": "Deneyim",
        "tags": ["fırın", "yerel lezzet", "navettes", "tarihi"],
        "distanceFromCenter": 1.1,
        "lat": 43.2980,
        "lng": 5.3670,
        "price": "low",
        "rating": 4.8,
        "description": "Marseille'in meşhur 'Navettes' bisküvilerinin kokusunun sokaklara taştığı, kentin en eski ve en otantik fırınlarının bulunduğu bölge.",
        "description_en": "The heart of Old Marseille's culinary heritage, where traditional bakeries slow-bake the famous boat-shaped 'Navettes' biscuits."
    },
    {
        "name": "Docks de la Joliette",
        "name_en": "The Joliette Docks",
        "area": "Joliette",
        "category": "Deneyim",
        "tags": ["modern mimari", "alışveriş", "ofis", "restoran"],
        "distanceFromCenter": 1.8,
        "lat": 43.3055,
        "lng": 5.3675,
        "price": "medium",
        "rating": 4.7,
        "description": "Eski liman depolarının muazzam bir mimari projeyle şık avlulara, butiklere ve restoranlara dönüştürüldüğü modern yaşam merkezi.",
        "description_en": "A brilliant adaptive reuse project of historic port warehouses, now filled with trendy courtyards, workshops, and eateries."
    },
    {
        "name": "Jardin de la Magalone",
        "name_en": "Magalone Garden",
        "area": "Güney Marseille",
        "category": "Park",
        "tags": ["bahçe", "saray", "heykel", "sessiz"],
        "distanceFromCenter": 5.0,
        "lat": 43.2570,
        "lng": 5.3980,
        "price": "free",
        "rating": 4.6,
        "description": "18. yüzyıldan kalma bir konutun etrafındaki klasik Fransız bahçesi. Heykelleri ve düzenli yapısıyla huzur verici bir durak.",
        "description_en": "A beautiful classical French garden centered around a historic bastide, featuring ornate statues and quiet paths."
    },
    {
        "name": "Place Jean Jaurès (La Plaine)",
        "name_en": "La Plaine Square",
        "area": "Noailles / La Plaine",
        "category": "Manzara",
        "tags": ["meydan", "sosyal", "market", "lokal"],
        "distanceFromCenter": 1.0,
        "lat": 43.2950,
        "lng": 5.3850,
        "price": "free",
        "rating": 4.5,
        "description": "Marseille yerlilerinin en sevdiği meydan. Her hafta kurulan devasa pazarı ve etrafındaki bohem barlarıyla kentin gerçek ruhunu yansıtır.",
        "description_en": "Commonly known as 'La Plaine,' this large square is the cultural hub for Marseille's youth and home to its most popular weekly market."
    },
    {
        "name": "Musée des Arts Décoratifs, de la Faïence et de la Mode",
        "name_en": "Decorative Arts and Fashion Museum",
        "area": "Güney Marseille",
        "category": "Müze",
        "tags": ["moda", "sanat", "saray", "seramik"],
        "distanceFromCenter": 6.2,
        "lat": 43.2385,
        "lng": 5.3725,
        "price": "medium",
        "rating": 4.8,
        "description": "Château Borély içinde yer alan, nadide seramik koleksiyonlarından tarihi moda parçalarına kadar çok zengin bir sergi alanı.",
        "description_en": "Located inside the Borely Castle, this museum showcases exquisite ceramics, 18th-century furniture, and a rich fashion collection."
    },
    {
        "name": "Frioul (Hôpital Caroline)",
        "name_en": "Caroline Hospital",
        "area": "Frioul Islands",
        "category": "Tarihi",
        "tags": ["karantina", "tarih", "mimari", "ada"],
        "distanceFromCenter": 4.8,
        "lat": 43.2825,
        "lng": 5.3025,
        "price": "free",
        "rating": 4.7,
        "description": "19. yüzyılda gemilerle gelen salgın hastalıkları önlemek için inşa edilmiş tarihi karantina hastanesi. Restorasyonuyla adanın en ilginç yapısıdır.",
        "description_en": "A former 19th-century quarantine site on Frioul Island, now used for cultural events and offering a hauntedly beautiful architectural landscape."
    },
    {
        "name": "Cannebière (Giriş)",
        "name_en": "La Canebiere Gateway",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["cadde", "liman", "tarih", "merkezi"],
        "distanceFromCenter": 0.1,
        "lat": 43.2960,
        "lng": 5.3760,
        "price": "free",
        "rating": 4.6,
        "description": "Marseille'in Şanzelize'si sayılan caddenin limanla buluştuğu nokta. Şehrin tüm ihtişamını ve karmaşasını bir arada görebilirsiniz.",
        "description_en": "The starting point of Marseille's historic main boulevard, once world-famous for its luxury stores and grand hotels."
    },
    {
        "name": "Vallon des Auffes (Teraslar)",
        "name_en": "Vallon des Auffes Terraces",
        "area": "Endoume",
        "category": "Manzara",
        "tags": ["manzara", "akşam", "deniz hızı", "romantik"],
        "distanceFromCenter": 2.7,
        "lat": 43.2855,
        "lng": 5.3495,
        "price": "medium",
        "rating": 4.9,
        "description": "Limanın etrafındaki kayalıklara kurulmuş teraslarda oturup gün batımında bir içki eşliğinde ufuk çizgisini izlemek paha biçilemez.",
        "description_en": "The rocky terraces surrounding the Vallon des Auffes are the best spots for a sunset drink with panoramic Mediterranean views."
    },
    {
        "name": "Mémorial des Déportations",
        "name_en": "Deportation Memorial",
        "area": "Vieux-Port",
        "category": "Müze",
        "tags": ["tarih", "hafıza", "savaş", "kale"],
        "distanceFromCenter": 0.9,
        "lat": 43.2940,
        "lng": 5.3615,
        "price": "free",
        "rating": 4.7,
        "description": "Fort Saint-Jean'ın bir parçası olan bu anıt-müze, İkinci Dünya Savaşı sırasında Marseille'den sürgün edilenlerin anısına adanmış hüzünlü ve etkileyici bir yerdir.",
        "description_en": "A sober and touching memorial museum located in a historic fortress tower, dedicated to the victims of the WW2 deportations."
    },
    {
        "name": "Place Castellane",
        "name_en": "Place Castellane",
        "area": "Castellane",
        "category": "Manzara",
        "tags": ["meydan", "fıskiye", "merkezi", "buluşma"],
        "distanceFromCenter": 1.2,
        "lat": 43.2850,
        "lng": 5.3850,
        "price": "free",
        "rating": 4.4,
        "description": "Marseille'in ulaşım ağının merkezindeki bu büyük meydan, ortasındaki devasa 'Fontaine Cantini' fıskiyesiyle ünlüdür.",
        "description_en": "A major roundabout and hub of city life, dominated by the spectacular 1911 white marble Cantini Fountain."
    },
    {
        "name": "Jardin de la Colline de Saint-Nicolas",
        "name_en": "Saint-Nicolas Hill Garden",
        "area": "Vieux-Port",
        "category": "Park",
        "tags": ["gizli", "manzara", "sessiz", "liman"],
        "distanceFromCenter": 0.8,
        "lat": 43.2865,
        "lng": 5.3625,
        "price": "free",
        "rating": 4.7,
        "description": "Abbbaye Saint-Victor yakınında saklı, turistlerin pek bilmediği bu küçük park, limana ve karşı kıyıya çok farklı ve sakin bir bakış açısı sunar.",
        "description_en": "A hidden gem of a garden on the south side of the harbor, offering a quiet bench with perfect views of Fort Saint-Jean."
    },
    {
        "name": "Théâtre de la Criée",
        "name_en": "La Criee Theatre",
        "area": "Vieux-Port",
        "category": "Deneyim",
        "tags": ["tiyatro", "sanat", "tarihi Bina", "liman"],
        "distanceFromCenter": 0.5,
        "lat": 43.2925,
        "lng": 5.3690,
        "price": "medium",
        "rating": 4.7,
        "description": "Eski bir balık hali binasının içine kurulmuş, Marseille'in en önemli ulusal tiyatro sahnelerinden biri.",
        "description_en": "Housed in the former fish auction house on the quays, this is Marseille's premier national theater and a hub for performing arts."
    },
    {
        "name": "Place aux Huiles (Sabun dükkanları)",
        "name_en": "Soap Shops of Marseille",
        "area": "Vieux-Port",
        "category": "Alışveriş",
        "tags": ["sabun", "savon de marseille", "lokal", "hediyelik"],
        "distanceFromCenter": 0.3,
        "lat": 43.2930,
        "lng": 5.3720,
        "price": "medium",
        "rating": 4.8,
        "description": "Marseille'in dünyaca ünlü zeytinyağlı sabunlarının (Savon de Marseille) en taze ve otantik örneklerini bulabileceğiniz tarihi dükkanların kümelendiği meydan.",
        "description_en": "The best area to buy authentic 'Savon de Marseille,' with several historic workshops selling the traditional olive oil soap nearby."
    },
    {
        "name": "Fort Saint-Nicolas",
        "name_en": "Fort Saint-Nicolas",
        "area": "Vieux-Port",
        "category": "Tarihi",
        "tags": ["kale", "manzara", "liman", "mimari"],
        "distanceFromCenter": 1.0,
        "lat": 43.2925,
        "lng": 5.3615,
        "price": "free",
        "rating": 4.6,
        "description": "Limanın güney girişini koruyan, 17. yüzyıldan kalma devasa bir yapı. Şimdi kısmen halka açık olan teraslarından denizi izleyebilirsiniz.",
        "description_en": "Facing Fort Saint-Jean, this massive star-shaped fortress was built by Louis XIV to keep an eye on the rebellious city."
    },
    {
        "name": "Bibliothèque de l'Alcazar",
        "name_en": "Alcazar Library",
        "area": "Belsunce",
        "category": "Tarihi",
        "tags": ["kütüphane", "modern", "sanat", "tarihi Bina"],
        "distanceFromCenter": 0.6,
        "lat": 43.2990,
        "lng": 5.3785,
        "price": "free",
        "rating": 4.7,
        "description": "Eski ve ünlü bir tiyatro binasının (Alcazar) içine kurulmuş modern bir kütüphane. Mimari ve kültürel açıdan kentin en dinamik noktalarından.",
        "description_en": "A massive and modern central library housed behind the historic facade of a world-famous 19th-century music hall."
    },
    {
        "name": "Le Panier (Eski Merdivenli Sokaklar)",
        "name_en": "Staircase Streets of Le Panier",
        "area": "Le Panier",
        "category": "Manzara",
        "tags": ["merdiven", "dar sokak", "fotoğraf", "renkli"],
        "distanceFromCenter": 1.1,
        "lat": 43.2990,
        "lng": 5.3675,
        "price": "free",
        "rating": 4.8,
        "description": "Le Panier mahallesinin kalbindeki dik ve rengarenk merdivenli sokaklar. Marseille'in en iyi fotoğraf kareleri bu basamaklarda gizlidir.",
        "description_en": "The iconic steep staircases of Old Marseille, lined with overflowing flower pots, laundry, and unique local street art."
    },
    {
        "name": "Musée de la Moto",
        "name_en": "Motorcycle Museum",
        "area": "Kuzey Marseille",
        "category": "Müze",
        "tags": ["motosiklet", "teknoloji", "koleksiyon", "tarih"],
        "distanceFromCenter": 6.8,
        "lat": 43.3425,
        "lng": 5.4125,
        "price": "medium",
        "rating": 4.8,
        "description": "Eski bir değirmenin içine kurulmuş, 250'den fazla nadide motosiklete ev sahipliği yapan Avrupa'nın en önemli motosiklet müzelerinden biri.",
        "description_en": "A hidden gem for motor enthusiasts, housing one of Europe's largest collections of motorcycles from 1885 to the present day."
    },
    {
        "name": "Calanque de Callelongue",
        "name_en": "Calanque de Callelongue",
        "area": "Les Goudes",
        "category": "Manzara",
        "tags": ["fiyort", "deniz", "yürüyüş", "dünyanın sonu"],
        "distanceFromCenter": 10.0,
        "lat": 43.2125,
        "lng": 5.3525,
        "price": "free",
        "rating": 4.9,
        "description": "Marseille'in 'dünyanın bittiği yer' dendiği noktası. Calanques milli parkının başladığı yerdeki bu küçük koy, balıkçı barınakları ve bembeyaz kayalıklarıyla büyüleyicidir.",
        "description_en": "Known as 'The End of the World,' this is the first calanque accessible by road, surrounded by dramatic cliffs and tiny fishing shacks."
    },
    {
        "name": "L'Ombrière (Gün Batımı)",
        "name_en": "Sunset at the Mirror Pavilion",
        "area": "Vieux-Port",
        "category": "Manzara",
        "tags": ["ayna", "gün batımı", "liman", "yansıma"],
        "distanceFromCenter": 0.1,
        "lat": 43.2952,
        "lng": 5.3745,
        "price": "free",
        "rating": 4.8,
        "description": "Güneş batan limanın renklerinin aynalı tavandaki yansıması, Marseille'deki en etkileyici görsel şölenlerden biridir.",
        "description_en": "The golden hour reflection under the mirror pavilion at the Old Port provides a unique and kaleidoscopic view of the city at dusk."
    },
    {
        "name": "Port-Miou (Viewpoint)",
        "name_en": "Port-Miou Viewback",
        "area": "Cassis / Calanques",
        "category": "Manzara",
        "tags": ["liman", "deniz", "manzara", "yelkenli"],
        "distanceFromCenter": 15.0,
        "lat": 43.2115,
        "lng": 5.5115,
        "price": "free",
        "rating": 4.9,
        "description": "Yüzlerce yelkenli teknenin sığındığı, upuzun ve dar bir doğa harikası koy. Marseille ile Cassis arasındaki en fotojenik duraklardan biri.",
        "description_en": "The longest calanque, used as a natural marina for hundreds of sailboats, offering a stunning perspective of white cliffs and deep blue water."
    },
    {
        "name": "Cathédrale de la Major (Teraslar)",
        "name_en": "Major Cathedral Terraces",
        "area": "Joliette",
        "category": "Manzara",
        "tags": ["manzara", "teras", "deniz hızı", "mimari"],
        "distanceFromCenter": 1.3,
        "lat": 43.2995,
        "lng": 5.3645,
        "price": "free",
        "rating": 4.8,
        "description": "Katedralin hemen önündeki teraslar, Mucem ve liman bölgesindeki modern dönüşümü izlemek için en iyi seyir yeridir.",
        "description_en": "The wide stone esplanades surrounding the cathedral offer perfect views of the modern port docks and the setting sun."
    },
    {
        "name": "Phare du Planier (View)",
        "name_en": "Planier Lighthouse View",
        "area": "Offshore",
        "category": "Manzara",
        "tags": ["deniz feneri", "ada", "uzak", "manzara"],
        "distanceFromCenter": 12.0,
        "lat": 43.1985,
        "lng": 5.2305,
        "price": "free",
        "rating": 4.7,
        "description": "Marseille açıklarındaki ıssız bir adada yer alan, kentin en yüksek ve en uzak deniz feneri. Sahil kıyısından ufk bakınca görülen o meşhur silüet.",
        "description_en": "The tallest and most distant lighthouse in the region, standing on a rocky island out at sea and visible from almost any point on the coast."
    }
]

def enrich_marseille_final():
    filepath = 'assets/cities/marsilya.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_marseille_final:
        if new_h['name'].lower() not in existing_names:
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1543783232-af412b852fc7?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_marseille_final()
print(f"Marseille now has {count} highlights.")
