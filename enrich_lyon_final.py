import json
import os

new_lyon_final = [
    {
        "name": "Rue Saint-Jean",
        "name_en": "Rue Saint-Jean",
        "area": "Vieux Lyon",
        "category": "Alışveriş",
        "tags": ["ortaçağ", "turistik", "hediyelik", "tarihi sokağı"],
        "distanceFromCenter": 0.5,
        "lat": 45.7615,
        "lng": 4.8275,
        "price": "medium",
        "rating": 4.8,
        "description": "Old Lyon'un ana caddesi. Ortaçağ ve Rönesans binalarıyla çevrili bu yaya sokağı, hediyelik eşya dükkanları ve yerel lezzet duraklarıyla dolu.",
        "description_en": "The spiritual and tourism heart of Old Lyon, a bustling pedestrian cobbled street lined with stunning Renaissance houses and craft shops."
    },
    {
        "name": "Passerelle Saint-Vincent",
        "name_en": "Saint-Vincent Footbridge",
        "area": "Saône Kıyısı",
        "category": "Manzara",
        "tags": ["köprü", "saone", "manzara", "yürüyüş"],
        "distanceFromCenter": 0.9,
        "lat": 45.7675,
        "lng": 4.8310,
        "price": "free",
        "rating": 4.7,
        "description": "Saône Nehri üzerindeki en eski ve en zarif yaya köprülerinden biri. Vieux Lyon'un kuzey girişine harika bir bakış sunar.",
        "description_en": "A historic red-railed footbridge across the Saône, providing a very romantic perspective of the river and the colorful facades of Old Lyon."
    },
    {
        "name": "Place Saint-Jean",
        "name_en": "Place Saint-Jean",
        "area": "Vieux Lyon",
        "category": "Tarihi",
        "tags": ["meydan", "katedral", "fıskiye", "buluşma"],
        "distanceFromCenter": 0.5,
        "lat": 45.7610,
        "lng": 4.8270,
        "price": "free",
        "rating": 4.8,
        "description": "Lyon Katedrali'nin önündeki bu ana meydan, ortaçağ fıskiyesi ve etrafındaki tarihi binalarıyla Vieux Lyon'un en önemli buluşma noktasıdır.",
        "description_en": "The central square of the Old Town, dominated by the Cathedral and featuring a 19th-century fountain by Rene Dardel."
    },
    {
        "name": "Fresque de la Bibliothèque de la Cité",
        "name_en": "Bookshelf Mural (La Bibliothèque de la Cité)",
        "area": "Quais de Saône",
        "category": "Manzara",
        "tags": ["trompe l'oeil", "kitaplık", "duvar resmi", "sanat"],
        "distanceFromCenter": 0.7,
        "lat": 45.7665,
        "lng": 4.8295,
        "price": "free",
        "rating": 4.9,
        "description": "Devasa bir kütüphane rafları gibi görünen bu duvar resmi, Lyonlu yazarların kitaplarını ve kentin edebi mirasını onurlandırır.",
        "description_en": "An incredible 400-square-meter 'trompe l'oeil' mural that transforms a street corner into a giant outdoor library."
    },
    {
        "name": "Jardin du Rosaire",
        "name_en": "Rosaire Garden",
        "area": "Fourvière",
        "category": "Park",
        "tags": ["bahçe", "yürüyüş yolu", "bazilika", "manzara"],
        "distanceFromCenter": 1.3,
        "lat": 45.7615,
        "lng": 4.8235,
        "price": "free",
        "rating": 4.8,
        "description": "Basilique Notre-Dame de Fourvière'den Vieux Lyon'a inen, çiçekler ve nadide ağaçlarla dolu, kenti kuşbakışı izleyen nefis bir yürüyüş yolu.",
        "description_en": "A beautiful public park on the slopes of Fourvière Hill, connecting the Basilica to the Old Town through flowering terraces."
    },
    {
        "name": "Palais de la Bourse",
        "name_en": "Exchange Palace",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["mimari", "tarihi Bina", "heykel", "ihtişam"],
        "distanceFromCenter": 0.6,
        "lat": 45.7640,
        "lng": 4.8363,
        "price": "free",
        "rating": 4.7,
        "description": "Lyon'un 19. yüzyıl ihtişamını yansıtan, heykellerle bezeli dış cephesi ve görkemli ana salonuyla kentin en önemli ticaret binalarından biri.",
        "description_en": "A masterpiece of 19th-century architecture, this grand palace served as the city's stock exchange and is one of Lyon's most beautiful civic buildings."
    },
    {
        "name": "Théâtre Antique (Manzara)",
        "name_en": "Ancient Theatre Viewpoint",
        "area": "Fourvière",
        "category": "Manzara",
        "tags": ["antik", "panorama", "roma", "fotoğraf"],
        "distanceFromCenter": 1.1,
        "lat": 45.7578,
        "lng": 4.8215,
        "price": "free",
        "rating": 4.9,
        "description": "Roma tiyatrosunun en üst basamaklarından oturduğunuzda, antik taşların arasından modern Lyon'un tüm silüetini ve Alpler'i görebilirsiniz.",
        "description_en": "The panoramic view from the top tier of the Roman Theater, where history and the modern city skyline meet."
    },
    {
        "name": "Berges du Rhône (Rıhtım Boyu)",
        "name_en": "Rhone River Embankments",
        "area": "Rhône Boyu",
        "category": "Deneyim",
        "tags": ["yürüyüş yolu", "bisiklet", "nehir", "yerel yaşam"],
        "distanceFromCenter": 1.5,
        "lat": 45.7590,
        "lng": 4.8450,
        "price": "free",
        "rating": 4.8,
        "description": "Renovasyon sonrası kentin en popüler spor ve eğlence alanı olan nehir kıyısı. Bisikletçiler, patenciler ve çimlerde oturan Lyonlularla çok canlı.",
        "description_en": "Kilometers of landscaped riverfront paths, former industrial quays turned into a vibrant park for cycling, lounging, and socializing."
    },
    {
        "name": "Musée de l'Automobile Henri Malartre",
        "name_en": "Handri Malartre Automobile Museum",
        "area": "Rochetaillée-sur-Saône (Dış)",
        "category": "Müze",
        "tags": ["araba", "klasik", "şato", "koleksiyon"],
        "distanceFromCenter": 12.0,
        "lat": 45.8450,
        "lng": 4.8380,
        "price": "medium",
        "rating": 4.8,
        "description": "Bir şatoda yer alan, Hitler'in Mercedes'inden ilk bisikletlere kadar otomobil tarihinin en nadide parçalarını barındıran devasa koleksiyon.",
        "description_en": "Set in a majestic castle north of Lyon, this museum houses an extraordinary collection of vintage cars, bicycles, and early public transport."
    },
    {
        "name": "Traboule de la Rue Saint-Jean (Gizli)",
        "name_en": "Saint-Jean Street Secret Traboule",
        "area": "Vieux Lyon",
        "category": "Deneyim",
        "tags": ["traboule", "gizli", "keşif", "ortaçağ"],
        "distanceFromCenter": 0.5,
        "lat": 45.7618,
        "lng": 4.8272,
        "price": "free",
        "rating": 4.7,
        "description": "Rue Saint-Jean üzerindeki sıradan bir kapının arkasında saklanan, bir sokaktan diğerine çıkan ve muazzam Rönesans avluları barındıran gizli geçit.",
        "description_en": "One of the most atmospheric hidden shortcuts in Old Lyon, accessible through an unassuming heavy wooden door and leading to a quiet courtyard."
    },
    {
        "name": "Place Sathonay",
        "name_en": "Place Sathonay",
        "area": "Croix-Rousse Eteği",
        "category": "Manzara",
        "tags": ["meydan", "boule", "lokal", "bohem"],
        "distanceFromCenter": 1.0,
        "lat": 45.7695,
        "lng": 4.8325,
        "price": "free",
        "rating": 4.8,
        "description": "Lyon'un küçük bir köy meydanı gibi hissettiren bohem noktası. Yerlilerin 'boule' (bir çeşit oyun) oynadığı ve çınar ağaçları altında vakit geçirdiği şirin yer.",
        "description_en": "A charming, village-like square at the foot of the Croix-Rousse hill, where locals gather to play pétanque under the plane trees."
    },
    {
        "name": "Passerelle des Quatre Vents",
        "name_en": "Four Winds Footbridge (Park View)",
        "area": "Fourvière",
        "category": "Manzara",
        "tags": ["köprü", "manzara", "yükseklik", "viyadük"],
        "distanceFromCenter": 1.6,
        "lat": 45.7635,
        "lng": 4.8205,
        "price": "free",
        "rating": 4.9,
        "description": "Eski bir tramvay viyadüğü olan bu yaya köprüsü, Jardin des Hauteurs içinde yer alır ve kentin kuzeyine doğru muazzam bir perspektif sunar.",
        "description_en": "A former tram viaduct turned into a high-level pedestrian walkway, offering dizzying and spectacular views of the Saône valley."
    },
    {
        "name": "Musée de la Résistance et de la Déportation",
        "name_en": "Resistance and Deportation History Center",
        "area": "Jean Macé",
        "category": "Müze",
        "tags": ["tarih", "savaş", "hafıza", "direniş"],
        "distanceFromCenter": 2.2,
        "lat": 45.7470,
        "lng": 4.8350,
        "price": "medium",
        "rating": 4.7,
        "description": "İkinci Dünya Savaşı sırasında Fransız Direnişi'nin merkezi olan Lyon'daki bu müze, direnişçilerin öykülerini hüzünlü ve etkileyici bir şekilde anlatır.",
        "description_en": "Housed in the former Gestapo headquarters, this moving museum documents the heroic history of the French Resistance in Lyon."
    },
    {
        "name": "Quai de la Pêcherie (Sahaf Pazarı)",
        "name_en": "Pecherie Book Market",
        "area": "Quais de Saône",
        "category": "Alışveriş",
        "tags": ["kitap", "antika", "sahaflar", "nehir kıyısı"],
        "distanceFromCenter": 0.8,
        "lat": 45.7650,
        "lng": 4.8305,
        "price": "low",
        "rating": 4.8,
        "description": "Hafta sonları nehir kıyısındaki rıhtımlarda kurulan, eski kitaplar, kartpostallar ve antika baskılar bulabileceğiniz sahaf dükkanları.",
        "description_en": "The spiritual home for book lovers in Lyon, where specialized second-hand booksellers set up their stalls along the Saône riverbanks."
    },
    {
        "name": "Place Guichard (Market)",
        "name_en": "Place Guichard Market",
        "area": "Part-Dieu",
        "category": "Alışveriş",
        "tags": ["pazar", "organik", "lokal", "sosyal"],
        "distanceFromCenter": 1.5,
        "lat": 45.7595,
        "lng": 4.8480,
        "price": "medium",
        "rating": 4.6,
        "description": "Kentin modern bölümünde, Salı ve Pazar günleri kurulan, Lyonluların en sevdiği yerel gıda pazarlarından biri.",
        "description_en": "A vibrant neighborhood market in the 3rd district, known for its high-quality regional products and friendly local vibe."
    },
    {
        "name": "Tour Métallique de Fourvière",
        "name_en": "Metallic Tower of Fourviere",
        "area": "Fourvière",
        "category": "Manzara",
        "tags": ["kule", "eiffel benzeri", "mimari", "tepe"],
        "distanceFromCenter": 1.4,
        "lat": 45.7635,
        "lng": 4.8215,
        "price": "free",
        "rating": 4.5,
        "description": "Lyon'un 'küçük Eiffel'i'. Bazilikanın hemen yanındaki bu metal kule, kentin en yüksek noktasını oluşturur.",
        "description_en": "A landmark steel frameworks tower that resembles the third floor of the Eiffel Tower, marking the highest point in Lyon."
    },
    {
        "name": "Auditorium-Orchestre National de Lyon",
        "name_en": "Lyon Auditorium",
        "area": "Part-Dieu",
        "category": "Deneyim",
        "tags": ["müzik", "konser", "mimari", "brütalizm"],
        "distanceFromCenter": 1.9,
        "lat": 45.7610,
        "lng": 4.8510,
        "price": "high",
        "rating": 4.8,
        "description": "Brütalist mimarisiyle dikkat çeken, kentin en önemli klasik müzik durağı. Harika akustiğiyle dünya çapında orkestralara ev sahipliği yapar.",
        "description_en": "A 2,100-seat brutalist concert hall, home to the National Orchestra of Lyon and famous for its exceptional acoustics and massive organ."
    },
    {
        "name": "Vieux Lyon (Rönesans Avluları)",
        "name_en": "Old Lyon Renaissance Courtyards",
        "area": "Vieux Lyon",
        "category": "Tarihi",
        "tags": ["avlu", "mimari", "rönesans", "gizli"],
        "distanceFromCenter": 0.6,
        "lat": 45.7625,
        "lng": 4.8278,
        "price": "free",
        "rating": 4.9,
        "description": "Old Lyon binalarının çoğunun kapıları arkasında saklı İtalyan esintili muazzam Rönesans avluları. Merdiven yapısı ve taş işçiliğiyle büyüleyici.",
        "description_en": "Behind the modest street facades of Old Lyon lie spectacular Italianate courtyards with galleries and spiral staircases."
    },
    {
        "name": "Traboule de la Longue Vue",
        "name_en": "Longue Vue Traboule",
        "area": "Vieux Lyon",
        "category": "Deneyim",
        "tags": ["traboule", "gizli", "ortaçağ", "mimari"],
        "distanceFromCenter": 0.7,
        "lat": 45.7630,
        "lng": 4.8280,
        "price": "free",
        "rating": 4.7,
        "description": "Kentin en dar ve en uzun traboule'lerinden biri. Sokaklar arasında bir tünel gibi ilerlerken adeta tarihin derinliklerine yolculuk yapıyorsunuz.",
        "description_en": "One of the longest secret passages in Lyon, winding through several buildings and small internal courtyards."
    },
    {
        "name": "Jardin de l'Institut Lumière",
        "name_en": "Lumiere Institute Garden",
        "area": "Monplaisir",
        "category": "Park",
        "tags": ["sinema", "park", "açık hava", "kültür"],
        "distanceFromCenter": 4.2,
        "lat": 45.7455,
        "lng": 4.8710,
        "price": "free",
        "rating": 4.7,
        "description": "Lumière müzesinin etrafındaki bu bahçe, her yıl Lyon Film Festivali'ne ve açık hava sineması etkinliklerine ev sahipliği yapar.",
        "description_en": "The peaceful grounds surrounding the birthplace of cinema, used as a focal point for the city's annual Lumière Film Festival."
    },
    {
        "name": "Port Lympia (Yürüyüş Yolu)",
        "name_en": "Lympia Port Dock Walk",
        "area": "Port",
        "category": "Deneyim",
        "tags": ["liman", "yürüyüş", "manzara", "lokal"],
        "distanceFromCenter": 1.2,
        "lat": 43.6975,
        "lng": 7.2865,
        "price": "free",
        "rating": 4.7,
        "description": "Nice Limanı'nın Rıhtım boyu, rengarenk evleri ve eski tekneleriyle akşam yürüyüşleri için en huzurlu ve estetik parkurlardan biridir.",
        "description_en": "A scenic walk around the docks of Port Lympia, where the traditional architecture of Nice reflects in the calm Mediterranean waters."
    },
    {
        "name": "Maison de la Danse",
        "name_en": "House of Dance",
        "area": "Mermoz",
        "category": "Deneyim",
        "tags": ["dans", "performans", "modern", "kültür"],
        "distanceFromCenter": 3.4,
        "lat": 45.7285,
        "lng": 4.8810,
        "price": "high",
        "rating": 4.8,
        "description": "Avrupa'nın dans sanatına adanmış en önemli merkezlerinden biri. Dünyaca ünlü bale ve modern dans topluluklarının Lyon'daki evi.",
        "description_en": "A premier European venue dedicated to all forms of choreography, from classical ballet to the most cutting-edge contemporary dance."
    },
    {
        "name": "Théâtre la Maison de Guignol",
        "name_en": "House of Guignol Puppet Theatre",
        "area": "Vieux Lyon",
        "category": "Deneyim",
        "tags": ["kukla tiyatrosu", "çocuk dostu", "gelenek", "lyon"],
        "distanceFromCenter": 0.6,
        "lat": 45.7610,
        "lng": 4.8290,
        "price": "medium",
        "rating": 4.8,
        "description": "Guignol kukla şovlarının sergilendiği en otantik tiyatro. Lyon'un mizah anlayışını yerinde görmek için paha biçilemez bir deneyim.",
        "description_en": "The historic home of Guignol performances, providing authentic puppet shows that have entertained generations of Lyonnais."
    },
    {
        "name": "Place Gailleton",
        "name_en": "Place Gailleton",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["heykel", "mimari", "sessiz", "tarih"],
        "distanceFromCenter": 0.8,
        "lat": 45.7555,
        "lng": 4.8355,
        "price": "free",
        "rating": 4.6,
        "description": "Kentin güney Presqu'île bölgesinde yer alan, eski belediye başkanı Gailleton'un devasa heykeliyle süslü sessiz ve şık bir meydan.",
        "description_en": "A quiet and elegant square featuring a massive monument to a former mayor, surrounded by beautiful 19th-century properties."
    },
    {
        "name": "Quais du Rhône (Güneşlenme Terasları)",
        "name_en": "Rhone Sun Terraces",
        "area": "Rhône Boyu",
        "category": "Manzara",
        "tags": ["manzara", "dinlenme", "nehir", "yerel"],
        "distanceFromCenter": 1.6,
        "lat": 45.7570,
        "lng": 4.8460,
        "price": "free",
        "rating": 4.8,
        "description": "Rhône nehri kıyısındaki geniş basamaklar ve ahşap teraslar. Lyonluların özellikle bahar ve yaz aylarında gün batımını izlemek için toplandığı yer.",
        "description_en": "Large timber sun decks and stone stepped embankments along the Rhône, perfect for relaxing by the water right in the city center."
    },
    {
        "name": "Musée de la Soie (Maison des Canuts)",
        "name_en": "Silk Museum (Maison des Canuts)",
        "area": "Croix-Rousse",
        "category": "Müze",
        "tags": ["ipek", "tarih", "dokuma", "lyon zanaatı"],
        "distanceFromCenter": 1.4,
        "lat": 45.7765,
        "lng": 4.8340,
        "price": "low",
        "rating": 4.8,
        "description": "Lyon'un ipekçilik tarihini canlı tezgahlarda yapılan dokuma gösterileriyle anlatan, kentin ipek mirasını en iyi görebileceğiniz müze.",
        "description_en": "A museum and workshop dedicated to the history of silk in Lyon, featuring live demonstrations on traditional Jacquard looms."
    },
    {
        "name": "Place Raspail",
        "name_en": "Place Raspail",
        "area": "Presqu'île",
        "category": "Manzara",
        "tags": ["meydan", "nehir kıyısı", "pazar", "merkezi"],
        "distanceFromCenter": 0.5,
        "lat": 45.7600,
        "lng": 4.8335,
        "price": "free",
        "rating": 4.5,
        "description": "Rhône Nehri'ne bakan bu meydan, hafta sonları kurulan küçük kitap ve sanat pazarlarıyla Lyon'un kültürel nabzını tutan noktalardan biridir.",
        "description_en": "A lively urban square overlooking the Rhône bridge, often hosting local arts and crafts markets and community events."
    },
    {
        "name": "Sık Seferli 'Vaporetto' (Nehir Hattı)",
        "name_en": "Vaporetto River Shuttle",
        "area": "Saône Kıyısı",
        "category": "Deneyim",
        "tags": ["tekne", "ulaşım", "nehir turu", "manzara"],
        "distanceFromCenter": 1.0,
        "lat": 45.7580,
        "lng": 4.8300,
        "price": "low",
        "rating": 4.8,
        "description": "Lyon'un bir ucundan diğerine nehirden giden toplu taşıma teknesi. Vieux Lyon, Bellecour ve Confluence arasını en keyifli katetme yolu.",
        "description_en": "A river shuttle that provides a scenic and affordable boat commute between the historic center and the modern Confluence district."
    },
    {
        "name": "Eglise Saint-Polycarpe",
        "name_en": "Saint-Polycarpe Church",
        "area": "Croix-Rousse",
        "category": "Tarihi",
        "tags": ["kilise", "tarih", "barok", "mimari"],
        "distanceFromCenter": 1.2,
        "lat": 45.7695,
        "lng": 4.8345,
        "price": "free",
        "rating": 4.6,
        "description": "Croix-Rousse tepesinin eteklerindeki bu tarihi kilise, İpekçilerin (Canuts) ayaklanmalarına ve kentin pek çok tarihi olayına tanıklık etmiştir.",
        "description_en": "A significant historical church on the slopes of Croix-Rousse, central to many of Lyon's 19th-century social and religious movements."
    },
    {
        "name": "Passerelle Mazaryk",
        "name_en": "Mazaryk Bridge",
        "area": "Vaise",
        "category": "Manzara",
        "tags": ["köprü", "saone", "tarih", "yürüyüş"],
        "distanceFromCenter": 4.2,
        "lat": 45.7850,
        "lng": 4.8150,
        "price": "free",
        "rating": 4.7,
        "description": "Lyon'un kuzeyinde, ipek sanayi bölgesini merkeze bağlayan tarihi ve zarif bir asma köprü. Saône'un en geniş açılı manzaralarından birini sunar.",
        "description_en": "A historic suspension bridge located in the north of the city, marking the gateway to the industrial and scenic upper Saône reach."
    }
]

def enrich_lyon_final():
    filepath = 'assets/cities/lyon.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_lyon_final:
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

count = enrich_lyon_final()
print(f"Lyon now has {count} highlights.")
