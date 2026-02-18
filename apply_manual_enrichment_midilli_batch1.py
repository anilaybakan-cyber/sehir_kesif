import json

# Manual enrichment data (Lesvos - ALL 15 items)
updates = {
    "Parasol Beach Bar": {
        "description": "Skala Eressos'ta denize sıfır popüler plaj barı. Harika kokteyller, gün batımı partileri ve rahat şezlonglar.",
        "description_en": "Popular beach bar right by sea in Skala Eressos. Great cocktails, sunset parties, and comfortable sunbeds."
    },
    "Reef Bar": {
        "description": "Molyvos limanında kayaların üzerindeki teras bar. Ege denizi manzarası, romantik akşamlar ve chill müzik.",
        "description_en": "Terrace bar on rocks at Molyvos harbor. Aegean sea views, romantic evenings, and chill music."
    },
    "Kremasti Köprüsü": {
        "description": "Agia Paraskevi yakınlarında, Cenevizlilerden kalma tarihi taş köprü. Ortaçağ mimarisi ve fotoğrafçılık.",
        "description_en": "Historic stone bridge from Genoese era near Agia Paraskevi. Medieval architecture and photography."
    },
    "Mesa Manastırı": {
        "description": "Kalloni körfezi yakınında sakin bir ibadethane. Tavus kuşları, zeytinlikler ve huzurlu avlu atmosferi.",
        "description_en": "Quiet sanctuary near Kalloni bay. Peacocks, olive groves, and peaceful courtyard atmosphere."
    },
    "Palaiochori": {
        "description": "Plomari'nin dağlık kesiminde, geleneksel kahvehaneleriyle ünlü şirin köy. Zamanın durduğu, otantik Yunan yaşamı.",
        "description_en": "Cute village famous for traditional coffee houses in mountainous Plomari. Authentic Greek life where time stands still."
    },
    "Kapi": {
        "description": "Kuzeyde yer alan, taş evleri ve dar sokaklarıyla tipik bir dağ köyü. Yerel bal, seramik ve misafirperverlik.",
        "description_en": "Typical mountain village in north with stone houses and narrow streets. Local honey, ceramics, and hospitality."
    },
    "Rani Plajı": {
        "description": "Adanın kuzeyinde sakin ve temiz bir koy. Kalabalıktan uzak yüzmek isteyenler için gizli cennet.",
        "description_en": "Quiet and clean cove in north of island. Hidden paradise for those wanting to swim away from crowds."
    },
    "Ligona Vadisi": {
        "description": "Petra yakınlarında su değirmenleri ve doğa yürüyüşü rotası. Yemyeşil bitki örtüsü, şelaleler ve kuş sesleri.",
        "description_en": "Water mills and hiking route near Petra. Lush vegetation, waterfalls, and bird sounds."
    },
    "Little Lakka": {
        "description": "Mytilene merkezde, gençlerin popüler buluşma noktası olan kafe-bar. Canlı müzik, uygun fiyatlar ve samimi ortam.",
        "description_en": "Popular meeting point cafe-bar for youth in Mytilene center. Live music, affordable prices, and friendly atmosphere."
    },
    "Pammegistoi Taxiarches (Mantamados)": {
        "description": "Başmelek Mikail'e adanmış ünlü hac kilisesi. Mucizevi sayılan rölyef ikon, siyah kanatlı melek ve askeri gelenek.",
        "description_en": "Famous pilgrimage church dedicated to Archangel Michael. Miraculous relief icon, black-winged angel, and military tradition."
    },
    "Lighthouse of Mytilene": {
        "description": "Liman girişindeki tarihi deniz feneri. Şehri ve Ege'yi selamlayan sembol yapı, özellikle gece ışıklandırmasıyla güzel.",
        "description_en": "Historic lighthouse at harbor entrance. Symbol structure greeting city and Aegean, especially beautiful with night lighting."
    },
    "Xirokastrou": {
        "description": "Antik dönemden kalma sur kalıntıları. Tarih meraklıları için kısa bir keşif noktası, manzara ve arkeoloji.",
        "description_en": "Remains of walls from ancient period. Short discovery spot for history buffs, view, and archeology."
    },
    "Paleokipos": {
        "description": "Gera Körfezi manzaralı, zeytinyağı üretimiyle bilinen köy. Geleneksel tavernalar ve Ege mimarisi.",
        "description_en": "Village known for olive oil production with Gera Bay views. Traditional tavernas and Aegean architecture."
    },
    "Museum of the Industrial Olive-Oil Production of Lesvos": {
        "description": "Agia Paraskevi'de, eski bir fabrikada kurulu modern zeytinyağı müzesi. Üretim makineleri, tarihçe ve tadım.",
        "description_en": "Modern olive oil museum in an old factory in Agia Paraskevi. Production machines, history, and tasting."
    },
    "Vatera Beach Bar": {
        "description": "Adanın en uzun plajı Vatera'da, tüm gün hizmet veren mekan. Kristal berraklığında deniz, soğuk kahve ve deniz ürünleri.",
        "description_en": "All-day venue on island's longest beach Vatera. Crystal clear sea, cold coffee, and seafood."
    }
}

filepath = 'assets/cities/midilli.json'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for place in data['highlights']:
    name = place.get('name')
    if name in updates:
        place['description'] = updates[name]['description']
        place['description_en'] = updates[name]['description_en']
        print(f"Enriched: {name}")
        count += 1

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Manually enriched {count} items (Lesvos - COMPLETE).")
