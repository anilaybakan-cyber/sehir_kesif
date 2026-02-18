import json
import os

new_lyon_batch2 = [
    {
        "name": "Bouchon Lyonnais (Deneyim)",
        "name_en": "Bouchon Lyonnais Experience",
        "area": "Vieux Lyon",
        "category": "Deneyim",
        "tags": ["gastronomi", "geleneksel", "lokal", "yemek"],
        "distanceFromCenter": 0.4,
        "lat": 45.7605,
        "lng": 4.8280,
        "price": "medium",
        "rating": 4.9,
        "description": "Lyon'un kendine has geleneksel restoranları. Kırmızı pötikareli örtüleri ve samimi ortamında 'saucisson brioché' veya 'quenelle' tatmadan dönmeyin.",
        "description_en": "The quintessential Lyon dining experience. Traditional family-run restaurants serving hearty regional specialties in a warm, rustic atmosphere."
    },
    {
        "name": "Théâtre des Célestins",
        "name_en": "Celestins Theatre",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["tiyatro", "mimari", "italyan tarzı", "kültür"],
        "distanceFromCenter": 0.3,
        "lat": 45.7595,
        "lng": 4.8320,
        "price": "medium",
        "rating": 4.8,
        "description": "Muazzam bir İtalyan tarzı tiyatro binası. Kırmızı kadife koltukları ve altın varaklı süslemeleriyle Lyon'un en prestijli sanat mekanlarından biri.",
        "description_en": "A magnificent 19th-century Italian-style theater, one of the most beautiful in France, offering a world-class program of drama and comedy."
    },
    {
        "name": "Musée Gadagne",
        "name_en": "Gadagne Museum",
        "area": "Vieux Lyon",
        "category": "Müze",
        "tags": ["tarih", "kukla", "rönesans", "konak"],
        "distanceFromCenter": 0.6,
        "lat": 45.7644,
        "lng": 4.8277,
        "price": "medium",
        "rating": 4.7,
        "description": "Görkemli bir Rönesans konağında yer alan bu müze, hem Lyon'un tarihini hem de dünyanın dört bir yanından kukla sanatını keşfetmenizi sağlar.",
        "description_en": "Located in a stunning Renaissance mansion, this museum complex houses both the History of Lyon Museum and the World Puppet Museum."
    },
    {
        "name": "Jardin des Curiosités",
        "name_en": "Garden of Curiosities",
        "area": "Fourvière",
        "category": "Manzara",
        "tags": ["gizli", "manzara", "sandalye", "romantik"],
        "distanceFromCenter": 1.5,
        "lat": 45.7554,
        "lng": 4.8205,
        "price": "free",
        "rating": 4.9,
        "description": "Fourvière tepesinde saklı, turistlerin pek bilmediği bir park. Kenti izleyebileceğiniz demir sandalyeleri ve huzurlu ortamıyla gerçek bir keşif.",
        "description_en": "A hidden hilltop park offering unique vantage points of Lyon's skyline, gifted by Montreal and known for its whimsical chair sculptures."
    },
    {
        "name": "Gallo-Roman Museum (Lugdunum)",
        "name_en": "Lugdunum Museum",
        "area": "Fourvière",
        "category": "Müze",
        "tags": ["roma", "arkeoloji", "beton mimari", "tarih"],
        "distanceFromCenter": 1.1,
        "lat": 45.7604,
        "lng": 4.8199,
        "price": "medium",
        "rating": 4.8,
        "description": "Antik tiyatroların hemen yanında, toprağın altına gizlenmiş brütalist mimarisiyle Lyon'un Roma (Lugdunum) dönemini anlatan muazzam müze.",
        "description_en": "An underground archaeological museum integrated into the hillside, showcasing exceptional Roman excavations, mosaics, and everyday artifacts."
    },
    {
        "name": "Fresque des Lyonnais",
        "name_en": "Fresque des Lyonnais (Famous Folk Mural)",
        "area": "Presqu'île",
        "category": "Manzara",
        "tags": ["duvar resmi", "ünlüler", "sanat", "ikonik"],
        "distanceFromCenter": 0.8,
        "lat": 45.7681,
        "lng": 4.8290,
        "price": "free",
        "rating": 4.9,
        "description": "Saint-Exupéry'den Paul Bocuse'e kadar Lyon tarihine damga vurmuş 30 ünlü ismin pencerelerden size baktığı devasa bir duvar resmi.",
        "description_en": "A massive mural depicting 30 of Lyon's most famous historical figures looking out from the windows of a trompe-l'oeil building."
    },
    {
        "name": "Passerelle du Palais de Justice",
        "name_en": "Palais de Justice Footbridge",
        "area": "Vieux Lyon / Presqu'île",
        "category": "Manzara",
        "tags": ["köprü", "saone", "mimari", "modern"],
        "distanceFromCenter": 0.5,
        "lat": 45.7615,
        "lng": 4.8305,
        "price": "free",
        "rating": 4.7,
        "description": "Saône Nehri üzerinde uzanan koyu kırmızı renkli modern yaya köprüsü. Liman ve Fourvière manzarasını fotoğraflamak için en iyi noktalardan biri.",
        "description_en": "A striking modern pedestrian suspension bridge across the Saône, providing a perfect view of the neo-classical Law Courts and Fourvière hill."
    },
    {
        "name": "Hôtel-Dieu de Lyon (Gastronomi Merkezi)",
        "name_en": "Hotel-Dieu Cité Internationale de la Gastronomie",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["mimari", "gastronomi", "lüks", "tarih"],
        "distanceFromCenter": 0.6,
        "lat": 45.7583,
        "lng": 4.8364,
        "price": "free",
        "rating": 4.8,
        "description": "Eski bir hastanenin muazzam bir restorasyonla şık avlulara, butiklere ve yemek dünyasına dönüştürüldüğü kentin en görkemli yapılarından biri.",
        "description_en": "A magnificent former hospital on the banks of the Rhône, stunningly renovated into a high-end complex of shops, gardens, and food culture."
    },
    {
        "name": "Lyon Opera House (Opéra Nouvel)",
        "name_en": "Lyon Opera House",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["mimari", "modern", "opera", "kubbe"],
        "distanceFromCenter": 0.8,
        "lat": 45.7673,
        "lng": 4.8353,
        "price": "medium",
        "rating": 4.7,
        "description": "Jean Nouvel tarafından tasarlanan, tarihi bir cephenin üzerine eklenen devasa cam kubbesiyle modern ve klasiğin mükemmel birleşimi.",
        "description_en": "The national opera house, famous for its avant-garde design by Jean Nouvel featuring a massive glowing glass semi-cylindrical roof."
    },
    {
        "name": "Basilique Saint-Martin d'Ainay",
        "name_en": "Saint-Martin d'Ainay Abbey",
        "area": "Presqu'île",
        "category": "Tarihi",
        "tags": ["roman mimarisi", "manastır", "tarih", "sessiz"],
        "distanceFromCenter": 0.9,
        "lat": 45.7523,
        "lng": 4.8286,
        "price": "free",
        "rating": 4.6,
        "description": "Lyon'un kalbinde, Romanesk mimarinin nadide bir örneği olan 12. yüzyıl kilisesi. Sessizliği ve kadim taş duvarlarıyla çok huzurlu.",
        "description_en": "A rare and beautiful Romanesque abbey church from the 11th century, standing as a peaceful sanctuary in the busy Presqu'île district."
    },
    {
        "name": "Musée de l'Imprimerie et de la Communication Graphique",
        "name_en": "Printing and Graphic Communication Museum",
        "area": "Presqu'île",
        "category": "Müze",
        "tags": ["matbaa", "kitap", "grafik", "tarih"],
        "distanceFromCenter": 0.7,
        "lat": 45.7635,
        "lng": 4.8360,
        "price": "medium",
        "rating": 4.7,
        "description": "Avrupa'nın en önemli matbaacılık müzelerinden biri. Gutenberg'den modern grafik tasarıma kadar kitap ve baskının büyüleyici tarihini anlatır.",
        "description_en": "One of Europe's top museums of printing, tracing the evolution of books and visual communication in a beautiful 15th-century building."
    },
    {
        "name": "Quartier Confluence (Mimari Keşif)",
        "name_en": "Confluence District Architecture",
        "area": "Confluence",
        "category": "Manzara",
        "tags": ["modern mimari", "eko-mahalle", "tasarım", "renkli"],
        "distanceFromCenter": 3.0,
        "lat": 45.7450,
        "lng": 4.8180,
        "price": "free",
        "rating": 4.8,
        "description": "Eski bir sanayi bölgesinin, cesur tasarımlar ve 'Le Cube Orange' gibi ikonik renkli binalarla bir açık hava mimari müzesine dönüştüğü mahalle.",
        "description_en": "A leading-edge sustainable neighborhood where innovative architects have created a vibrant, colorful landscape of contemporary design."
    },
    {
        "name": "La Sucrière",
        "name_en": "La Sucriere (Art Center)",
        "area": "Confluence",
        "category": "Deneyim",
        "tags": ["çağdaş sanat", "sergi", "yineleme", "endüstriyel"],
        "distanceFromCenter": 3.7,
        "lat": 45.7385,
        "lng": 4.8140,
        "price": "medium",
        "rating": 4.7,
        "description": "Eski bir şeker fabrikasının devasa sergi salonlarına dönüştürüldüğü, Lyon Bienali gibi büyük sanat etkinliklerine ev sahipliği yapan mekan.",
        "description_en": "A former 1930s sugar factory transformed into a major international cultural hub for contemporary art and photography."
    },
    {
        "name": "Traboule de la Tour Rose",
        "name_en": "Pink Tower Traboule",
        "area": "Vieux Lyon",
        "category": "Tarihi",
        "tags": ["pembe kule", "traboule", "rönesans", "fotojenik"],
        "distanceFromCenter": 0.5,
        "lat": 45.7610,
        "lng": 4.8275,
        "price": "free",
        "rating": 4.9,
        "description": "Lyon'un en güzel 'pembe kulesine' ev sahipliği yapan bu Rönesans avlusu, gizli geçitlerin en romantik ve fotojenik durağıdır.",
        "description_en": "A famous hidden courtyard in Old Lyon featuring an elegant pink-washed Renaissance tower and a very atmospheric stairway."
    },
    {
        "name": "Escalier Mermet",
        "name_en": "Mermet Staircase (Painted)",
        "area": "Croix-Rousse",
        "category": "Manzara",
        "tags": ["merdiven", "sokak sanatı", "boyalı", "renkli"],
        "distanceFromCenter": 1.2,
        "lat": 45.7720,
        "lng": 4.8340,
        "price": "free",
        "rating": 4.8,
        "description": "Croix-Rousse yokuşunda yer alan, basamakları rengarenk geometrik desenlerle boyanmış şehrin en neşeli merdivenlerinden biri.",
        "description_en": "A colorful urban intervention where a steep set of stairs has been transformed into a vibrant geometric mural by local artists."
    },
    {
        "name": "Théâtre Antique (Odeon)",
        "name_en": "Roman Odeon",
        "area": "Fourvière",
        "category": "Tarihi",
        "tags": ["roma", "odeon", "müzik", "antik"],
        "distanceFromCenter": 1.1,
        "lat": 45.7570,
        "lng": 4.8210,
        "price": "free",
        "rating": 4.8,
        "description": "Büyük tiyatronun hemen yanındaki daha küçük ve samimi antik tiyatro. Zamanında şiir ve müzik dinletileri için kullanılırdı.",
        "description_en": "A smaller, more intimate Roman theater located next to the main Great Theater, once used for musical performances and speeches."
    },
    {
        "name": "Place des Jacobins",
        "name_en": "Place des Jacobins",
        "area": "Presqu'île",
        "category": "Manzara",
        "tags": ["meydan", "fıskiye", "heykel", "mimari"],
        "distanceFromCenter": 0.5,
        "lat": 45.7604,
        "lng": 4.8290,
        "price": "free",
        "rating": 4.9,
        "description": "Dört ünlü sanatçının heykeliyle süslü beyaz mermer fıskiyesi ve etrafındaki görkemli binalarıyla kentin en şık meydanı.",
        "description_en": "One of Lyon's most elegant squares, dominated by a magnificent fountain featuring statues of four famous local artists."
    },
    {
        "name": "Musée Lumière",
        "name_en": "Lumiere Museum",
        "area": "Monplaisir",
        "category": "Müze",
        "tags": ["sinema", "lumiere", "tarih", "icat"],
        "distanceFromCenter": 4.0,
        "lat": 45.7450,
        "lng": 4.8700,
        "price": "medium",
        "rating": 4.8,
        "description": "Sinemanın doğduğu yer! Lumière kardeşlerin eski konutunda, ilk film makinesinden ilk renkli fotoğraflara kadar sinema tarihini keşfedin.",
        "description_en": "The birthplace of cinema, located in the former villa of the Lumière brothers, where they invented the Cinematograph in 1895."
    },
    {
        "name": "Parc de la Tête d'Or (Gül Bahçesi)",
        "name_en": "Rose Garden of Parc Tete d'Or",
        "area": "Cité Internationale",
        "category": "Park",
        "tags": ["gül bahçesi", "romantik", "çiçek", "doğa"],
        "distanceFromCenter": 2.7,
        "lat": 45.7780,
        "lng": 4.8550,
        "price": "free",
        "rating": 4.9,
        "description": "Dünyanın en iyi gül bahçelerinden biri. Binlerce çeşit gülün yarattığı renk cümbüşü ve mis kokular arasında rüya gibi bir yürüyüş.",
        "description_en": "An internationally acclaimed international rose garden with over 15,000 rose bushes from hundreds of rare and classic species."
    },
    {
        "name": "Mur des Canuts (Modern Yaşam)",
        "name_en": "Canuts Mural (Modern Details)",
        "area": "Croix-Rousse",
        "category": "Manzara",
        "tags": ["duvar resmi", "detay", "grafiti", "modern"],
        "distanceFromCenter": 2.6,
        "lat": 45.7795,
        "lng": 4.8295,
        "price": "free",
        "rating": 4.8,
        "description": "Meşhur duvar resminin her birkaç yılda bir güncellendiğini biliyor muydunuz? Resimdeki detaylar, Lyon halkının yaşlanmasını ve değişen modasını takip eder.",
        "description_en": "This famous mural is periodically updated to reflect the aging of the characters and the changing style of the Croix-Rousse district."
    },
    {
        "name": "Marché Saint-Antoine",
        "name_en": "Saint-Antoine Market",
        "area": "Presqu'île",
        "category": "Alışveriş",
        "tags": ["pazar", "nehir kıyısı", "lokal lezzet", "ürün"],
        "distanceFromCenter": 0.4,
        "lat": 45.7610,
        "lng": 4.8315,
        "price": "medium",
        "rating": 4.8,
        "description": "Saône Nehri kıyısında kurulan kentin en sevilen açık hava pazarı. Yerel üreticilerin taze meyveleri, peynirleri ve Lyon sosislerini bulmak için ideal.",
        "description_en": "A beloved riverside open-air market where locals shop for farm-fresh produce, regional cheeses, and roasted chickens."
    },
    {
        "name": "Eglise Saint-Georges",
        "name_en": "Saint-Georges Church",
        "area": "Vieux Lyon",
        "category": "Tarihi",
        "tags": ["kilise", "saone", "mimari", "nehir"],
        "distanceFromCenter": 0.8,
        "lat": 45.7570,
        "lng": 4.8265,
        "price": "free",
        "rating": 4.7,
        "description": "Saône nehri kıyısında, suyun üzerindeki silüetiyle kentin en fotojenik ve zarif neo-gotik kiliselerinden biridir.",
        "description_en": "A beautiful neo-Gothic church whose spire creates one of the most iconic silhouettes on the right bank of the Saône river."
    },
    {
        "name": "Lyon Confluence (Yat Limanı)",
        "name_en": "Confluence Marina",
        "area": "Confluence",
        "category": "Manzara",
        "tags": ["marina", "modern", "deniz", "keyif"],
        "distanceFromCenter": 3.2,
        "lat": 45.7440,
        "lng": 4.8190,
        "price": "free",
        "rating": 4.6,
        "description": "Modern mahalle Confluence'ın kalbindeki küçük yat limanı. Nehir kenarındaki kafeleri ve tekneleriyle Akdeniz esintili bir atmosfer.",
        "description_en": "A modern leisure marina created as part of the Confluence project, surrounded by trendy bars, a mall, and innovative architecture."
    },
    {
        "name": "Musée Gallo-Romain (Teras Bahçeleri)",
        "name_en": "Gallo-Roman Museum Gardens",
        "area": "Fourvière",
        "category": "Park",
        "tags": ["roma", "bahçe", "manzara", "antik"],
        "distanceFromCenter": 1.2,
        "lat": 45.7600,
        "lng": 4.8205,
        "price": "free",
        "rating": 4.7,
        "description": "Müzenin çatısını oluşturan ve antik tiyatrolara basamaklar halinde inen, Roma dönemi bitkileriyle bezeli yeşil teraslar.",
        "description_en": "The terraced green roofs and surrounding slopes of the museum offer a peaceful walk with unique views of the Roman Ruins."
    },
    {
        "name": "Boulangerie du Palais (Praline)",
        "name_en": "Palais Bakery (Tarte aux Pralines)",
        "area": "Vieux Lyon",
        "category": "Kafe",
        "tags": ["fırın", "pralin", "tatlı", "lyon klasiği"],
        "distanceFromCenter": 0.5,
        "lat": 45.7620,
        "lng": 4.8285,
        "price": "low",
        "rating": 4.9,
        "description": "Lyon'un meşhur pembe şekerli 'Tarte aux Pralines'ini (pralinli turta) tadabileceğiniz, önünde her zaman kuyruk olan efsanevi fırın.",
        "description_en": "A legendary bakery in the heart of Old Lyon building, famous for its glowing pink sugar-coated praline tarts and brioches."
    }
]

def enrich_lyon_batch2():
    filepath = 'assets/cities/lyon.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_lyon_batch2:
        if new_h['name'].lower() not in existing_names:
            # Add missing fields
            new_h['imageUrl'] = "https://images.unsplash.com/photo-1549221165-276f7c181342?w=800"
            new_h['bestTime'] = "Gündüz"
            new_h['bestTime_en'] = "Daytime"
            new_h['tips'] = "Mutlaka görün."
            new_h['tips_en'] = "A must see."
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_lyon_batch2()
print(f"Lyon now has {count} highlights.")
