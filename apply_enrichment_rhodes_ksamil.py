import json
import os

all_updates = {
    "Rhodes": {
        "Medieval City of Rhodes": {
            "description": "Rodos'un UNESCO listesindeki Ortaçağ kenti, Avrupa'nın hala içinde yaşam olan en büyük ve en iyi korunmuş kale-kentidir. Şövalyeler döneminden kalan taş sokakları, devasa surları ve her köşesinde fısıldayan Haçlı hikayeleriyle kentin en büyüleyici tarih laboratuvarıdır.",
            "description_en": "The UNESCO-listed Medieval City of Rhodes is the largest and best-preserved fortified city in Europe still inhabited today. With its stone streets from the era of the Knights, massive walls, and Crusader stories whispering at every corner, it is the city's most captivating historical laboratory.",
            "tips": "Şövalyeler Caddesi'nde gece yürüyüşü yapın, sokak lambalarının altında kendinizi 14. yüzyılda hissedeceksiniz; ara sokaklardaki küçük kafeleri keşfedin.",
            "tips_en": "Take a night walk on the Street of the Knights; under the street lamps, you'll feel like you're in the 14th century. Explore the small cafes in the back streets.",
            "category": "Tarihi"
        },
        "Lindos Acropolis": {
            "description": "Lindos köyünün üzerinde bir taç gibi yükselen bu antik akropol, Ege Denizi'nin turkuaz manzarasına bakan dor tarzı sütunlarıyla ünlüdür. Hem antik Yunan tapınaklarını hem de Ortaçağ kalesini barındıran bu katmanlı yapı, kentin en dramatik ve havadar gözlem noktasıdır.",
            "description_en": "Rising like a crown above Lindos village, this ancient acropolis is famous for its Doric columns overlooking the turquoise Aegean Sea. Housing both ancient Greek temples and a medieval fortress, this layered structure is the city's most dramatic and airy viewpoint.",
            "tips": "Akropol'e çıkış diktir, sabah erken saatleri veya gün batımı öncesini tercih edin; köyden eşeklerle çıkmak yerine yürüyerek manzaranın tadını çıkarın.",
            "tips_en": "The climb to the acropolis is steep, so prefer early morning or pre-sunset; instead of taking donkeys from the village, walk up to enjoy the view.",
            "category": "Tarihi"
        },
        "Kallithea Springs": {
            "description": "Art Deco mimarisiyle ünlü Kallithea Springs, antik çağlardan beri şifalı sularıyla bilinen kentsel bir huzur merkezidir. Beyaz mermerleri, mozaik zeminleri ve turkuaz bir koya açılan zarif rotasıyla kentin en estetik ve dinlendirici sahil noktalarından biridir.",
            "description_en": "Famous for its Art Deco architecture, Kallithea Springs is an urban center of peace known for its medicinal waters since antiquity. With its white marbles, mosaic floors, and elegant route opening to a turquoise bay, it is one of the city's most aesthetic and relaxing coastal spots.",
            "tips": "Buradaki plaj dalış için mükemmeldir; restoranda yerel 'Ouzo' eşliğinde deniz ürünleri tadımı yapın.",
            "tips_en": "The beach here is excellent for diving; try the seafood accompanied by local 'Ouzo' at the restaurant.",
            "category": "Deneyim"
        }
    },
    "Ksamil": {
        "Ksamil Islands": {
            "description": "Ksamil sahilinin hemen karşısında yer alan bu dört küçük ada, Arnavut Rivierası'nın 'Maldivler'i olarak bilinir. Sadece tekne veya kano ile ulaşılabilen bu adalar, kentin en el değmemiş kumsallarına ve en berrak sularına ev sahipliği yapar.",
            "description_en": "These four small islands right across from the Ksamil coast are known as the 'Maldives' of the Albanian Riviera. Accessible only by boat or kayak, these islands host the city's most pristine beaches and clearest waters.",
            "tips": "Adalardan birine kano kiralayarak kendiniz kürek çekin; kalabalıktan kaçmak için en uzak olan adayı (Twin Islands) tercih edin.",
            "tips_en": "Rent a kayak and paddle yourself to one of the islands; prefer the farthest one (Twin Islands) to escape the crowds.",
            "category": "Doğa"
        },
        "Mirror Beach": {
            "description": "Arnavutça adıyla 'Pasqyra', güneşin deniz üzerindeki yansımaları nedeniyle 'Ayna Plajı' olarak anılır. Sarp kayalıklar arasına gizlenmiş bu koy, kristal berraklığındaki suyu ve beyaz çakıl taşlarıyla kentin en saklı ve etkileyici doğa duraklarından biridir.",
            "description_en": "Known as 'Pasqyra' in Albanian, it is called 'Mirror Beach' because of the sun's reflections on the sea. Tucked between steep cliffs, this cove is one of the city's most hidden and impressive nature stops with its crystal clear water and white pebbles.",
            "tips": "Sabah 09:00'dan önce gidin, deniz gerçekten bir ayna gibi çarşaf gibidir; sahil yolunun son kısmı biraz engebelidir.",
            "tips_en": "Go before 09:00 AM when the sea is truly glass-calm like a mirror; the last part of the coastal road is a bit rough.",
            "category": "Doğa"
        },
        "The Blue Eye": {
            "description": "Ksamil'in biraz iç kısımlarında yer alan 'Syri i Kaltër', derinliği tam olarak bilinmeyen ve yüzeyi masmavi bir gözü andıran doğal bir su kaynağıdır. Buz gibi suyu ve yemyeşil orman dokusuyla kentin en mistik ve serinletici doğa harikasıdır.",
            "description_en": "Located slightly inland from Ksamil, 'Syri i Kaltër' is a natural water spring of unknown depth, resembling a deep blue eye from the surface. With its icy water and lush green forest surroundings, it is the city's most mystical and refreshing natural wonder.",
            "tips": "Su sıcaklığı yıl boyu 10 derecedir, yüzmek için cesaret ister; çevredeki ahşap platformda yürüyüş yapıp fotoğraflar çekin.",
            "tips_en": "The water temperature is 10 degrees year-round, swimming takes courage; walk on the wooden platforms nearby and take photos.",
            "category": "Doğa"
        }
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    highlights = []
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get('highlights', [])
        
    for h in highlights:
        name = h.get('name')
        if name in city_updates:
            upd = city_updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {city_file}")

# Apply updates
apply_updates('assets/cities/rhodes.json', all_updates['Rhodes'])
apply_updates('assets/cities/ksamil.json', all_updates['Ksamil'])
