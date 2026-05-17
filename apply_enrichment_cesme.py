import json
import os

all_updates = {
    "Cesme": {
        "Çeşme Kalesi": {
            "description": "1508 yılında II. Bayezid tarafından inşa edilen Çeşme Kalesi, kentin en görkemli tarihi anıtıdır. Üç tarafı hendeklerle çevrili olan ve bugün içerisinde Çeşme Arkeoloji Müzesi'ni barındıran bu yapı, Sakız Adası'na bakan muazzam bir manzara sunan kentin savunma kalbidir.",
            "description_en": "Built in 1508 by Bayezid II, Cesme Castle is the city's most magnificent historical monument. Surrounded by moats on three sides and now housing the Cesme Archaeology Museum, this structure is the defensive heart of the city, offering a magnificent view overlooking Chios Island.",
            "tips": "Kalenin burçlarına çıkarak liman ve deniz manzarasını fotoğraflayın; yaz aylarında düzenlenen konser ve festivaller için etkinlik takvimini kontrol edin.",
            "tips_en": "Climb the castle's bastions to photograph the harbor and sea views; check the event calendar for concerts and festivals held during the summer months.",
            "category": "Tarihi"
        },
        "Alaçatı Çarşı": {
            "description": "Alaçatı'nın Arnavut kaldırımlı dar sokaklarında yer alan Çarşı, kentin en popüler ve şık sosyal yaşam merkezidir. Tarihi taş evlerin altındaki butik dükkanları, sanat galerileri ve sardunyalarla süslü kafeleriyle, kentsel dokunun en estetik ve canlı halini sunar.",
            "description_en": "Located in the narrow cobblestone streets of Alacati, the Bazaar is the city's most popular and stylish social center. With its boutique shops under historical stone houses, art galleries, and cafes decorated with geraniums, it offers the most aesthetic and vibrant version of the urban fabric.",
            "tips": "Akşamüstü kalabalıklaşmadan önce gidin ve yerel dükkanlardan damla sakızlı ürünler almayı unutmayın; Hacımemiş bölgesine doğru yürüyerek daha sakin sokakları keşfedin.",
            "tips_en": "Go before it gets crowded in the late afternoon and don't forget to buy mastic products from local shops; walk towards the Hacimemis area to discover quieter streets.",
            "category": "Alışveriş"
        },
        "Alaçatı Yel Değirmenleri": {
            "description": "Alaçatı'nın girişinde bir tepede yer alan 150 yıllık bu taş yel değirmenleri, kentin en ikonik simgeleridir. Restore edilerek turizme kazandırılan bu yapılar, rüzgarın hiç eksik olmadığı bu bölgenin tarımsal geçmişine tanıklık eden kentsel birer anıttır.",
            "description_en": "Located on a hill at the entrance of Alacati, these 150-year-old stone windmills are the city's most iconic symbols. Restored and opened to tourism, these structures are urban monuments witnessing the agricultural past of this region where the wind never stops.",
            "tips": "Gün batımı saatlerinde yel değirmenlerinin arkasından batan güneşi izlemek büyüleyicidir; fotoğraf çekimi için en popüler duraktır.",
            "tips_en": "Watching the sun set behind the windmills at dusk is magical; it is the most popular stop for photography.",
            "category": "Tarihi"
        },
        "Çeşme Marina": {
            "description": "Ege'nin en modern marinalarından biri olan Çeşme Marina, kentin lüks ve sofistike yüzünü temsil eder. Şık restoranları, dünya markalarının bulunduğu mağazaları ve Adriyatik'ten gelen tekneleriyle kentsel koşturmacadan uzaklaşıp keyifli bir akşam yürüyüşü yapabileceğiniz rafine bir duraktır.",
            "description_en": "One of the most modern marinas in the Aegean, Cesme Marina represents the city's luxury and sophisticated side. With its chic restaurants, shops featuring global brands, and boats coming from the Adriatic, it is a refined stop where you can move away from urban hustle and enjoy a pleasant evening walk.",
            "tips": "Marinadaki kafelerde kahve molası verin; akşam yemekleri için önceden rezervasyon yaptırmanız önerilir.",
            "tips_en": "Take a coffee break at the cafes in the marina; pre-booking is recommended for dinners.",
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
apply_updates('assets/cities/cesme.json', all_updates['Cesme'])
