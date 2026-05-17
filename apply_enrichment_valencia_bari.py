import json
import os

all_updates = {
    "Valencia": {
        "Ciudad de las Artes y las Ciencias": {
            "description": "Valencia'nın fütüristik sembolü olan Sanat ve Bilim Şehri, mimar Santiago Calatrava tarafından tasarlanmış bir modernizm şaheseridir. Dev bir gözü andıran planetaryumdan, yelkenliyi andıran operaya kadar uzanan bu yapılar kompleksi, kentin geleceğe bakan yüzünü temsil eder.",
            "description_en": "Valencia's futuristic symbol, the City of Arts and Sciences, is a masterpiece of modernism designed by architect Santiago Calatrava. This complex of buildings, ranging from a planetarium resembling a giant eye to an opera house resembling a sailboat, represents the city's forward-looking face.",
            "tips": "Binaların etrafındaki turkuaz havuzlarda kano kiralayabilirsiniz; özellikle akşam ışıklandırmasıyla fotoğraf çekmek için kentin en etkileyici noktasıdır.",
            "tips_en": "You can rent kayaks in the turquoise pools around the buildings; it's the city's most impressive spot for photography, especially with the evening lighting.",
            "category": "Kültür"
        },
        "Central Market of Valencia": {
            "description": "Avrupa'nın en eski ve en büyük taze ürün pazarlarından biri olan Mercado Central, devasa metal kubbesi ve rengarenk vitraylarıyla bir gastronomi tapınağıdır. Valensiya'nın yerel mutfak kültürünü, taze deniz ürünlerini ve dünyaca ünlü portakallarını keşfetmek için kentin en canlı merkezidir.",
            "description_en": "One of Europe's oldest and largest fresh produce markets, Mercado Central is a gastronomic temple with its massive metal dome and colorful stained glass. It is the city's most vibrant center to discover Valencia's local culinary culture, fresh seafood, and world-famous oranges.",
            "tips": "Pazara aç gitmenizi öneririm; oradaki 'Central Bar'da Michelin yıldızlı şef Ricard Camarena'nın tapaslarını mutlaka deneyin.",
            "tips_en": "I suggest going to the market hungry; be sure to try the tapas by Michelin-starred chef Ricard Camarena at 'Central Bar' inside.",
            "category": "Alışveriş"
        },
        "Valencia Cathedral": {
            "description": "Gotik, Barok ve Romanesk tarzların harmanlandığı Valencia Katedrali, içerisinde kutsal kase (Holy Grail) olduğuna inanılan kadehi barındıran muazzam bir tarihi yapıdır. Miguelete kulesiyle kentin silüetine karakter katan bu yapı, Valensiya'nın dini ve tarihi mirasının kalbidir.",
            "description_en": "A blend of Gothic, Baroque, and Romanesque styles, Valencia Cathedral is a magnificent historical structure housing the chalice believed to be the Holy Grail. Adding character to the city's skyline with its Miguelete tower, it is the heart of Valencia's religious and historical heritage.",
            "tips": "Miguelete kulesine 207 basamakla tırmanarak kentin 360 derecelik panaromik manzarasını seyredin; Kutsal Kase şapelini mutlaka ziyaret edin.",
            "tips_en": "Climb the 207 steps of the Miguelete tower for a 360-degree panoramic view of the city; be sure to visit the Holy Grail chapel.",
            "category": "Tarihi"
        }
    },
    "Bari": {
        "Bari Vecchia": {
            "description": "Bari'nin 'Eski Şehir' bölgesi, çamaşırların asılı olduğu daracık sokakları ve kapı önlerinde makarna yapan teyzeleriyle kentin en otantik ve samimi ruhudur. Adriyatik'in taze havası ve fırınlardan yükselen taze focaccia kokusuyla kentsel yaşamın en saf halini sunar.",
            "description_en": "Bari's 'Old Town' area is the city's most authentic and sincere soul, with narrow streets where laundry hangs and grandmothers make pasta outside their doors. It offers the purest form of urban life with the fresh Adriatic air and the smell of fresh focaccia rising from bakeries.",
            "tips": "'Arco Basso' sokağında (Makarna Sokağı) Orecchiette makarnasının elle nasıl yapıldığını izleyin ve bir paket taze makarna satın alın.",
            "tips_en": "Watch how Orecchiette pasta is handmade in 'Arco Basso' street (Pasta Street) and buy a bag of fresh pasta.",
            "category": "Tarihi"
        },
        "Basilica of Saint Nicholas": {
            "description": "Noel Baba olarak bilinen Aziz Nikolaos'un kemiklerine ev sahipliği yapan bu bazilika, hem Katolik hem de Ortodoks dünyası için kentin en önemli hac merkezidir. 11. yüzyıldan kalma görkemli yapısı ve içerisinde barındırdığı sanat eserleriyle kentsel maneviyatın en güçlü kalesidir.",
            "description_en": "Housing the bones of Saint Nicholas, known as Santa Claus, this basilica is the city's most important pilgrimage center for both Catholic and Orthodox worlds. Its magnificent 11th-century structure and the artworks it contains make it the strongest fortress of urban spirituality.",
            "tips": "Alt kattaki kriptayı (mezar odası) ziyaret etmeyi unutmayın; kilisenin tavanındaki muazzam altın varaklı süslemelere mutlaka bakın.",
            "tips_en": "Don't forget to visit the crypt (burial chamber) downstairs; be sure to look at the magnificent gold-leaf decorations on the church ceiling.",
            "category": "Tarihi"
        },
        "Lungomare di Bari": {
            "description": "İtalya'nın en uzun ve en güzel sahil yollarından biri olan Lungomare, Bari'nin Adriyatik ile kucaklaştığı yerdir. Tarihi lambaları, masmavi denizi ve kıyı boyunca uzanan görkemli binalarıyla kentin en popüler yürüyüş ve sosyal yaşam alanıdır.",
            "description_en": "One of Italy's longest and most beautiful coastal roads, Lungomare is where Bari embraces the Adriatic. With its historical street lamps, deep blue sea, and magnificent buildings along the coast, it is the city's most popular walking and social area.",
            "tips": "Sabah erken saatlerde yerel balıkçıların taze deniz ürünlerini satmasını izlemek için N'derre la Lanze bölgesine gidin.",
            "tips_en": "Go to the N'derre la Lanze area in the early morning to watch local fishermen sell their fresh seafood.",
            "category": "Sosyal"
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
apply_updates('assets/cities/valencia.json', all_updates['Valencia'])
apply_updates('assets/cities/bari.json', all_updates['Bari'])
