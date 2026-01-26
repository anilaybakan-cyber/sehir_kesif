import json

# Manual enrichment data (Matera Batch 1: 40 items)
updates = {
    "Convicinio di Sant'Antonio": {
        "description": "Dört kayaya oyulmuş kiliseden oluşan kompleks, Bizans freskleri ve dini miras. Sassi'nin en iyi korunmuş mağara kiliseleri.",
        "description_en": "Complex of four rock-cut churches with Byzantine frescoes and religious heritage. Best-preserved cave churches of Sassi."
    },
    "Ipogeo Materasum": {
        "description": "Yeraltı sarnıç sistemini ve antik su mühendisliğini anlatan müze. Labirent tüneller, ortaçağ toplama sistemi ve arkeoloji.",
        "description_en": "Museum explaining underground cistern system and ancient water engineering. Labyrinth tunnels, medieval collection system, and archaeology."
    },
    "Ponte Tibetano della Gravina": {
        "description": "Gravina kanyonu üzerindeki asma köprü, tırmanış ve macera deneyimi. Panoramik manzara, adrenalin ve doğa.",
        "description_en": "Suspension bridge over Gravina canyon for climbing and adventure experience. Panoramic views, adrenaline, and nature."
    },
    "MOOM Matera Olive Oil Museum": {
        "description": "Zeytinyağı üretiminin tarihini ve geleneğini anlatan müze. Antik presler, tadım ve Basilicata gastromisi.",
        "description_en": "Museum telling history and tradition of olive oil production. Antique presses, tasting, and Basilicata gastronomy."
    },
    "Ristorante Il Terrazzino": {
        "description": "Sassi manzaralı teras restoran, geleneksel Basilicata mutfağı. Romantik akşam yemekleri, yerel şaraplar ve panoramik konum.",
        "description_en": "Terrace restaurant with Sassi views serving traditional Basilicata cuisine. Romantic dinners, local wines, and panoramic location."
    },
    "Trattoria Stano": {
        "description": "Yerel halkın favori tratoriası, ev yapımı makarna ve bölgesel lezzetler. Otantik atmosfer, uygun fiyat ve doyurucu porsiyonlar.",
        "description_en": "Locals' favorite trattoria with homemade pasta and regional flavors. Authentic atmosphere, affordable prices, and satisfying portions."
    },
    "Dedalo - Sensi Sommersi": {
        "description": "Mağara içinde kurulan yaratıcı gastronomi restoranı, modern İtalyan mutfağı. Fine-dining, sanat ve yeraltı deneyimi.",
        "description_en": "Creative gastronomy restaurant in a cave with modern Italian cuisine. Fine-dining, art, and underground experience."
    },
    "Enoteca dai Tosi": {
        "description": "Basilicata şaraplarına odaklanan şarap barı, yerel tadım ve şarküteri. Aglianico, antipasti ve samimi ortam.",
        "description_en": "Wine bar focusing on Basilicata wines with local tasting and charcuterie. Aglianico, antipasti, and intimate setting."
    },
    "Birrificio 79": {
        "description": "Yerel craft bira üretim tesisi ve tadım mekanı. Matera aromalı biralar, pub yemekleri ve bira kültürü.",
        "description_en": "Local craft beer production facility and tasting venue. Matera-flavored beers, pub food, and beer culture."
    },
    "Quarry Lounge Terrace": {
        "description": "Taş ocağından dönüştürülmüş çatı bar, Sassi manzarası ve kokteyller. Gün batımı, aperitivo ve benzersiz konum.",
        "description_en": "Rooftop bar converted from quarry with Sassi views and cocktails. Sunset, aperitivo, and unique location."
    },
    "Dimora Ulmo": {
        "description": "Tarihi saray-otel, geleneksel mobilyalar ve lüks konaklama. Sassi mahallesi, bahçe ve aristokrat atmosfer.",
        "description_en": "Historic palace-hotel with traditional furniture and luxury accommodation. Sassi neighborhood, garden, and aristocratic atmosphere."
    },
    "Regia Corte": {
        "description": "Mağara odasında konaklama deneyimi, restore edilmiş Sassi evi. Otantik yaşam, modern konfor ve tarihi mekân.",
        "description_en": "Cave room accommodation experience in restored Sassi house. Authentic living, modern comfort, and historic venue."
    },
    "Panificio Paolucci": {
        "description": "Matera'nın ünlü ekmekçisi, geleneksel pane di Matera üretimi. Odun fırını, el yapımı ekmek ve sabah lezzetleri.",
        "description_en": "Matera's famous baker, traditional pane di Matera production. Wood oven, handmade bread, and morning treats."
    },
    "Gelateria I Vizi degli Angeli": {
        "description": "Artisan dondurma ve tatlılar sunan popüler dondurma dükkanı. Doğal malzemeler, yerel tatlar ve İtalyan gelato.",
        "description_en": "Popular ice cream shop serving artisan gelato and desserts. Natural ingredients, local flavors, and Italian gelato."
    },
    "Fontana Ferdinandea": {
        "description": "19. yüzyıldan kalma anıtsal çeşme, şehrin su kaynağı tarihi. Barok unsurlar, meydan ve tarihi merkez.",
        "description_en": "19th-century monumental fountain, city's water source history. Baroque elements, square, and historic center."
    },
    "Diga di San Giuliano": {
        "description": "Matera yakınındaki baraj gölü, kuş gözlemi ve doğa. Yürüyüş rotaları, piknik ve açık hava aktiviteleri.",
        "description_en": "Dam lake near Matera for bird watching and nature. Hiking trails, picnic, and outdoor activities."
    },
    "Villaggio Neolitico di Murgia Timone": {
        "description": "Neolitik dönem köy kalıntıları, prehistorik Matera yaşamı. Arkeolojik alan, kaya mezarları ve tarih öncesi.",
        "description_en": "Neolithic period village remains, prehistoric Matera life. Archaeological site, rock tombs, and prehistory."
    },
    "Parco Scultura La Palomba": {
        "description": "Doğa içinde açık hava heykel parkı, çağdaş sanat eserleri. Yürüyüş, sanat ve manzara.",
        "description_en": "Open-air sculpture park in nature with contemporary artworks. Walking, art, and scenery."
    },
    "Monastery of Saint Augustin": {
        "description": "Ortaçağ manastırı, dini sanat ve mimari miras. Avlu, fresk kalıntıları ve tarihi atmosfer.",
        "description_en": "Medieval monastery with religious art and architectural heritage. Courtyard, fresco remains, and historic atmosphere."
    },
    "Church of San Francesco d'Assisi": {
        "description": "Barok ve Romanesk öğeleri harmanlayan kilise, değerli sanat eserleri. Dini mimari, meydan ve şehir merkezi.",
        "description_en": "Church blending Baroque and Romanesque elements with valuable artworks. Religious architecture, square, and city center."
    },
    "San Nicola dei Greci": {
        "description": "Bizans döneminden kalma Yunan Ortodoks kilisesi, ikonalar ve freskler. Doğu Hristiyanlığı mirası ve dini sanat.",
        "description_en": "Greek Orthodox church from Byzantine period with icons and frescoes. Eastern Christian heritage and religious art."
    },
    "Grotta dei Pipistrelli": {
        "description": "Yarasa mağarası, doğal habitat ve ekolojik koruma alanı. Doğa gözlemi, jeoloji ve keşif.",
        "description_en": "Bat cave, natural habitat and ecological protection area. Nature observation, geology, and discovery."
    },
    "Panificio Cifarelli": {
        "description": "Geleneksel Matera ekmeği ve fırın ürünleri. IGP korumalı pane di Matera, focaccia ve sabah lezzetleri.",
        "description_en": "Traditional Matera bread and bakery products. IGP-protected pane di Matera, focaccia, and morning treats."
    },
    "Kapriol": {
        "description": "Lokal bitkiler ve bölgesel malzemelerle üretilen Matera cin markası. Damıtma turu, tadım ve yerel üretim.",
        "description_en": "Matera gin brand produced with local herbs and regional ingredients. Distillery tour, tasting, and local production."
    },
    "Laboratorio della Civiltà Contadina": {
        "description": "Güney İtalya köylü yaşamını sergileyen etnografik müze. Tarım aletleri, ev eşyaları ve kırsal miras.",
        "description_en": "Ethnographic museum exhibiting Southern Italian peasant life. Agricultural tools, household items, and rural heritage."
    },
    "Gravina Sotterranea": {
        "description": "Gravina di Puglia'daki yeraltı şehri turları. Mağaralar, kiliseler ve gizli geçitler.",
        "description_en": "Underground city tours in Gravina di Puglia. Caves, churches, and hidden passages."
    },
    "Chiesa di San Michele delle Grotte": {
        "description": "Kayaya oyulmuş ortaçağ kilisesi, Bizans freskleri ve mağara mimarisi. Dini miras ve arkeolojik değer.",
        "description_en": "Medieval church carved into rock with Byzantine frescoes and cave architecture. Religious heritage and archaeological value."
    },
    "Chiesa del Santo Spirito": {
        "description": "Romanesk dönem kilisesi, süslemeli portal ve sade iç mekân. Dini mimari ve ortaçağ sanatı.",
        "description_en": "Romanesque-period church with decorated portal and simple interior. Religious architecture and medieval art."
    },
    "Charlie's Speakeasy": {
        "description": "1920'ler Amerikan tarzı gizli kokteyl barı, speakeasy konseptiyle. Klasik kokteyller, jazz atmosferi ve gece hayatı.",
        "description_en": "1920s American-style hidden cocktail bar with speakeasy concept. Classic cocktails, jazz atmosphere, and nightlife."
    },
    "Il Forno di Gennaro": {
        "description": "Geleneksel odun fırınında pizza ve ekmek. Napoli usulü pizza, focaccia ve yerel lezzetler.",
        "description_en": "Pizza and bread in traditional wood oven. Neapolitan-style pizza, focaccia, and local flavors."
    },
    "Keiv Cafè": {
        "description": "Sassi'de modern kafe ve bar, espresso ve hafif öğle yemeği. Terrasa görünümü, brunch ve kahve kültürü.",
        "description_en": "Modern cafe and bar in Sassi with espresso and light lunch. Terrace views, brunch, and coffee culture."
    },
    "Hemingway Bistrot": {
        "description": "Edebiyat temalı dekorasyonlu bistro-bar, kokteyller ve hafif yemekler. Kitap rafları, rahat ortam ve akşam keyfi.",
        "description_en": "Literature-themed bistro-bar with cocktails and light meals. Bookshelves, comfortable setting, and evening enjoyment."
    },
    "Morgan Ristorante": {
        "description": "Modern İtalyan mutfağını geleneksel tariflerle harmanlayan şık restoran. Fine-dining, yerel malzemeler ve yaratıcı sunum.",
        "description_en": "Elegant restaurant blending modern Italian cuisine with traditional recipes. Fine-dining, local ingredients, and creative presentation."
    },
    "Geppetto": {
        "description": "Ahşap el sanatları ve oyuncak dükkanı, Pinocchio temalı ürünler. Hediyelik, İtalyan zanaatı ve nostaljik mağaza.",
        "description_en": "Wooden handicrafts and toy shop with Pinocchio-themed products. Souvenirs, Italian craftsmanship, and nostalgic store."
    },
    "Sassi in Miniatura": {
        "description": "Matera'nın Sassi mahallelerinin minyatür modellerini sergileyen atölye. Hediyelik, el yapımı ve detaylı çalışma.",
        "description_en": "Workshop exhibiting miniature models of Matera's Sassi neighborhoods. Souvenirs, handmade, and detailed work."
    },
    "Castello del Malconsiglio": {
        "description": "Miglionico'daki ortaçağ kalesi, Aragonese tarihi ve tırmanış. Panoramik manzara, savunma mimarisi ve gizem.",
        "description_en": "Medieval castle in Miglionico with Aragonese history and climbing. Panoramic views, defensive architecture, and mystery."
    },
    "Tavole Palatine": {
        "description": "Metaponto'daki antik Yunan Hera tapınağı kalıntıları. Dor sütunları, arkeolojik alan ve Magna Graecia mirası.",
        "description_en": "Ancient Greek Hera temple remains in Metaponto. Doric columns, archaeological site, and Magna Graecia heritage."
    },
    "La Talpa": {
        "description": "Mağara içinde kurulan otantik restoran, geleneksel Basilicata yemekleri. Yeraltı atmosferi, yerel tarifler ve şarap.",
        "description_en": "Authentic restaurant set up in a cave with traditional Basilicata dishes. Underground atmosphere, local recipes, and wine."
    },
    "Chiesa del Carmine": {
        "description": "Barok dönemi kilisesi, süslemeli iç mekân ve dini sanat. Şehir merkezinde mola noktası ve mimari.",
        "description_en": "Baroque-period church with decorated interior and religious art. Rest point in city center and architecture."
    },
    "Palazzo del Governo": {
        "description": "Valilik binası, 19. yüzyıl mimarisi ve resmi yapı. Piazza Vittorio Veneto'da konumlu, şehir yönetimi.",
        "description_en": "Government palace, 19th-century architecture and official building. Located in Piazza Vittorio Veneto, city administration."
    }
}

filepath = 'assets/cities/matera.json'
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

print(f"\n✅ Manually enriched {count} items (Matera Batch 1).")
