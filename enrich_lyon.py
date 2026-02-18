import json
import os

new_lyon_batch1 = [
    {
        "name": "Basilique Notre-Dame de Fourvière",
        "name_en": "Basilica of Notre-Dame de Fourviere",
        "area": "Fourvière",
        "category": "Tarihi",
        "tags": ["bazilika", "manzara", "ikonik", "mozaik"],
        "distanceFromCenter": 1.2,
        "lat": 45.7621,
        "lng": 4.8225,
        "price": "free",
        "rating": 4.9,
        "description": "Lyon'un 'dua eden dağı' Fourvière'in tepesinde yer alan, muazzam mozaikleri ve kenti kuş bakışı gören manzarasıyla şehrin simgesi.",
        "description_en": "Lyon's iconic hilltop basilica, visible from across the city. Famous for its ornate mosaics, Byzantine architecture, and breathtaking panoramic views."
    },
    {
        "name": "Musée des Confluences",
        "name_en": "Confluences Museum",
        "area": "Confluence",
        "category": "Müze",
        "tags": ["modern mimari", "bilim", "antropoloji", "fütüristik"],
        "distanceFromCenter": 3.5,
        "lat": 45.7390,
        "lng": 4.8217,
        "price": "medium",
        "rating": 4.8,
        "description": "Rhône ve Saône nehirlerinin birleştiği noktada yükselen, fütüristik kristal ve bulut tasarımıyla bilim ve medeniyetler müzesi.",
        "description_en": "A strikingly futuristic museum of science and anthropology, located at the spectacular confluence of Lyon's two rivers."
    },
    {
        "name": "Les Halles de Lyon Paul Bocuse",
        "name_en": "Paul Bocuse Food Market",
        "area": "Part-Dieu",
        "category": "Deneyim",
        "tags": ["gastronomi", "gurme", "market", "peynir"],
        "distanceFromCenter": 1.8,
        "lat": 45.7629,
        "lng": 4.8524,
        "price": "medium",
        "rating": 4.9,
        "description": "Dünyaca ünlü şef Paul Bocuse'ün adını taşıyan, Lyon mutfağının en seçkin ürünlerini bulabileceğiniz efsanevi gurme kapalı pazar.",
        "description_en": "The spiritual home of French gastronomy. A high-end covered market featuring the region's finest cheeses, charcuterie, and artisanal specialties."
    },
    {
        "name": "Le Mur des Canuts",
        "name_en": "Mur des Canuts (Silkworkers Mural)",
        "area": "Croix-Rousse",
        "category": "Manzara",
        "tags": ["trompe l'oeil", "duvar resmi", "grafiti", "dev"],
        "distanceFromCenter": 2.5,
        "lat": 45.7797,
        "lng": 4.8299,
        "price": "free",
        "rating": 4.8,
        "description": "Avrupa'nın en büyük 'trompe l'oeil' (göz yanılması) duvar resmi. Bir mahallenin günlük yaşamını inanılmaz bir gerçeklikle tasvir eder.",
        "description_en": "Europe's largest mural, a 1,200-square-meter masterpiece that uses optical illusions to depict the daily life of the Croix-Rousse neighborhood."
    },
    {
        "name": "Théâtre Antique de Lyon",
        "name_en": "Ancient Theatre of Lyon",
        "area": "Fourvière",
        "category": "Tarihi",
        "tags": ["roma", "tiyatro", "antik", "UNESCO"],
        "distanceFromCenter": 1.1,
        "lat": 45.7576,
        "lng": 4.8218,
        "price": "free",
        "rating": 4.8,
        "description": "Roma İmparatorluğu döneminden kalma, hala yaz festivallerine ev sahipliği yapan ve kente hükmeden muazzam iki antik tiyatro.",
        "description_en": "A remarkably well-preserved Roman theater and odeon complex on Fourvière Hill, dating back to 15 BC and still used for live performances."
    },
    {
        "name": "Traboule de la Cour des Voraces",
        "name_en": "Cour des Voraces Traboule",
        "area": "Croix-Rousse",
        "category": "Tarihi",
        "tags": ["traboule", "ipekçiler", "mimari", "gizli geçit"],
        "distanceFromCenter": 1.5,
        "lat": 45.7725,
        "lng": 4.8365,
        "price": "free",
        "rating": 4.7,
        "description": "Croix-Rousse tepesindeki en meşhur traboule (gizli geçit). İnanılmaz açık merdiven yapısıyla ipek işçilerinin (Canuts) tarihini fısıldar.",
        "description_en": "The most famous 'traboule' in Croix-Rousse, featuring a stunning six-story monumental stone staircase used by 19th-century silk weavers."
    },
    {
        "name": "Musée Cinéma et Miniature",
        "name_en": "Cinema and Miniature Museum",
        "area": "Vieux Lyon",
        "category": "Müze",
        "tags": ["miniature", "sinema", "efekt", "ilgi çekici"],
        "distanceFromCenter": 0.5,
        "lat": 45.7603,
        "lng": 4.8286,
        "price": "medium",
        "rating": 4.9,
        "description": "Dünya çapındaki film setlerinden orijinal objeler ve inanılmaz gerçeklikteki minyatür sahneleri barındıran benzersiz bir müze.",
        "description_en": "A unique museum in a 16th-century building showcasing over 100 hyper-realistic miniature scenes and authentic movie props and special effects."
    },
    {
        "name": "Parc de la Tête d'Or (Botanik Bahçesi)",
        "name_en": "Tete d'Or Botanical Garden",
        "area": "Cité Internationale",
        "category": "Park",
        "tags": ["botanik", "sera", "doğa", "sessiz"],
        "distanceFromCenter": 2.5,
        "lat": 45.7756,
        "lng": 4.8505,
        "price": "free",
        "rating": 4.8,
        "description": "Fransa'nın en büyük belediye botanik bahçesi. 19. yüzyıl cam seraları ve binlerce bitki türüyle huzur dolu bir vaha.",
        "description_en": "One of Europe's premier botanical gardens, featuring historic greenhouses from the 1800s and a world-class collection of exotic plants."
    },
    {
        "name": "Île Barbe",
        "name_en": "Ile Barbe",
        "area": "Saône Kıyısı",
        "category": "Manzara",
        "tags": ["ada", "ortaçağ", "sessiz", "mistik"],
        "distanceFromCenter": 5.0,
        "lat": 45.7980,
        "lng": 4.8338,
        "price": "free",
        "rating": 4.7,
        "description": "Saône Nehri'nin ortasında, ortaçağ manastırı kalıntıları ve taş evleriyle zamanın durduğu mistik ve gizli bir ada.",
        "description_en": "A magical, island in the middle of the Saône river, home to 5th-century abbey ruins and a small, quiet village frozen in time."
    },
    {
        "name": "Le Petit Musée de Guignol",
        "name_en": "Guignol Puppet Museum",
        "area": "Vieux Lyon",
        "category": "Müze",
        "tags": ["kukla", "gelenek", "lyon kültürü", "tiyatro"],
        "distanceFromCenter": 0.6,
        "lat": 45.7615,
        "lng": 4.8295,
        "price": "low",
        "rating": 4.6,
        "description": "Lyon'un ünlü kukla karakteri Guignol'un dünyasına yolculuk. İpekçiler döneminden gelen bu kukla tiyatrosu şehrin ruhunu anlatır.",
        "description_en": "A charming museum dedicated to Lyon's famous puppet, Guignol, tracing its 19th-century history and the art of puppeteering."
    }
]

def enrich_lyon():
    filepath = 'assets/cities/lyon.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update fillers in existing highlights
    fillers = {
        "Basilique Notre-Dame de Fourvière": {
            "description": "Lyon'un 'dua eden dağı' Fourvière'in tepesinde yer alan, muazzam mozaikleri ve kenti kuş bakışı gören manzarasıyla şehrin simgesi.",
            "description_en": "Lyon's iconic hilltop basilica, visible from across the city. Famous for its ornate mosaics, Byzantine architecture, and breathtaking panoramic views."
        },
        "Vieux Lyon (Old Lyon)": {
            "description": "Avrupa'nın en geniş Rönesans bölgelerinden biri. Dar sokakları, 'Traboule' denen gizli geçitleri ve meşhur 'Bouchon' restoranlarıyla Lyon'un kalbi.",
            "description_en": "One of Europe's largest Renaissance neighborhoods, a labyrinth of cobbled alleys, secret 'traboule' passages, and authentic Lyon eateries."
        },
        "Place Bellecour": {
            "description": "Avrupa'nın en büyük yaya meydanlarından biri. Ortasındaki sadiheykeli ve kırmızımsı toprağıyla Lyon'un ana buluşma noktası.",
            "description_en": "One of the largest pedestrian squares in Europe, featuring a grand equestrian statue of Louis XIV and serving as the city's zero-kilometer marker."
        },
        "Parc de la Tête d'Or": {
            "description": "Şehrin ortasında devasa bir göl, hayvanat bahçesi ve gül bahçelerini barındıran, Lyon'un 'merkezi parkı'.",
            "description_en": "A massive 117-hectare urban park featuring a boating lake, a free zoo, and some of the world's most beautiful rose gardens."
        },
        "Musée des Beaux-Arts de Lyon": {
            "description": "Eski bir manastır binasında yer alan, Louvre'dan sonra Fransa'nın en zengin sanat koleksiyonuna sahip müzelerinden biri.",
            "description_en": "Housed in a former 17th-century abbey, this is one of France's premier art museums with an exceptional collection of European painting."
        },
        "Place des Terreaux": {
            "description": "Belediye binası (Hôtel de Ville) ve Bartholdi Çeşmesi'ne ev sahipliği yapan, Lyon'un en görkemli ve hareketli meydanı.",
            "description_en": "A majestic public square home to the City Hall, the Museum of Fine Arts, and the spectacular 19th-century Bartholdi Fountain."
        },
        "La Croix-Rousse district": {
            "description": "Lyon'un ipek işçilerinin (Canuts) yaşadığı tepe. Bohem atmosferi, dik yokuşları ve muazzam duvar resimleriyle kentin 'çalışan dağı'.",
            "description_en": "The historic silk-weaving district on a hill, known for its creative community, unique architectural features, and lively local markets."
        },
        "Lyon Cathedral (Cathédrale Saint-Jean-Baptiste)": {
            "description": "Rönesans mahallesinin kalbinde yer alan, 14. yüzyıldan kalma astronomik saati ve gotik mimarisiyle büyüleyen katedral.",
            "description_en": "The seat of the Archbishop of Lyon, featuring a rare 14th-century astronomical clock and stunning Romanesque and Gothic design."
        }
    }

    for h in data.get('highlights', []):
        if h['name'] in fillers:
            h['description'] = fillers[h['name']]['description']
            h['description_en'] = fillers[h['name']]['description_en']

    # 2. Add new highlights
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_lyon_batch1:
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

count = enrich_lyon()
print(f"Lyon now has {count} highlights.")
