import json

# Manual enrichment data (Colmar Batch 1: 40 items)
updates = {
    "Eguisheim": {
        "description": "Fransa'nın en güzel köylerinden biri, dairesel ortaçağ yerleşimi ve çiçekli evleriyle. Şarap mahzenleri, kale kalıntıları ve masalsı Alsace atmosferi.",
        "description_en": "One of France's most beautiful villages with circular medieval layout and flower-covered houses. Wine cellars, castle ruins, and fairy-tale Alsace atmosphere."
    },
    "Riquewihr": {
        "description": "Şarap rotasının incisi, 16. yüzyıldan kalma sur içi ortaçağ köyü. Riesling tadımları, yarı ahşap evler ve Disneyland ilham kaynağı.",
        "description_en": "Pearl of the wine route, walled medieval village from 16th century. Riesling tastings, half-timbered houses, and Disneyland inspiration."
    },
    "Kaysersberg": {
        "description": "Albert Schweitzer'ın doğduğu ortaçağ köyü, kale kalıntıları ve nehir kenarı manzarası. Şarap mahzenleri, müze ve Alsace zanaatları.",
        "description_en": "Medieval village where Albert Schweitzer was born, castle ruins and riverside views. Wine cellars, museum, and Alsace crafts."
    },
    "Ribeauvillé": {
        "description": "Üç kalenin gölgesindeki şarap köyü, ortaçağ festivalleriyle ünlü. Gewürztraminer, müzisyenler alayı ve yarı ahşap mimari.",
        "description_en": "Wine village in shadow of three castles, famous for medieval festivals. Gewürztraminer, minstrels' parade, and half-timbered architecture."
    },
    "Grand Rue": {
        "description": "Colmar'ın ana cadddesi, yarı ahşap evler, butikler ve restoranlarla dolu. Alışveriş, yeme-içme ve tarihi atmosfer.",
        "description_en": "Colmar's main street full of half-timbered houses, boutiques, and restaurants. Shopping, dining, and historic atmosphere."
    },
    "Parc du Champ de Mars": {
        "description": "Şehir merkezindeki büyük yeşil alan, çeşmeler, çocuk oyun alanları ve piknik. Aileler için huzurlu mola ve açık hava aktiviteleri.",
        "description_en": "Large green area in city center with fountains, playgrounds, and picnicking. Peaceful break and outdoor activities for families."
    },
    "Place des Dominicains": {
        "description": "Dominiken Kilisesi'nin önündeki meydan, Martin Schongauer'in Madonna'sıyla ünlü. Noel pazarı, açık hava kafeler ve gotik atmosfer.",
        "description_en": "Square in front of Dominican Church, famous for Martin Schongauer's Madonna. Christmas market, outdoor cafes, and Gothic atmosphere."
    },
    "Ancienne Douane (Koïfhus)": {
        "description": "15. yüzyıldan kalma eski gümrük binası, Colmar'ın en ikonik yapılarından. Renkli çini çatısı ve ortaçağ ticaret tarihi.",
        "description_en": "15th-century old customs building, one of Colmar's most iconic structures. Colorful tiled roof and medieval trade history."
    },
    "Sézanne": {
        "description": "Alsace mutfağı ve şarapları sunan geleneksel restoran. Choucroute, tarte flambée ve yöresel lezzetlerle Alsace deneyimi.",
        "description_en": "Traditional restaurant serving Alsace cuisine and wines. Alsace experience with choucroute, tarte flambée, and regional flavors."
    },
    "Fortwenger": {
        "description": "Alsace zencefilli kurabiyeleri ve geleneksel tatlıların satıldığı tarihi mağaza. Pain d'épices, bredele ve Noel lezzetleri.",
        "description_en": "Historic store selling Alsace gingerbread and traditional sweets. Pain d'épices, bredele, and Christmas flavors."
    },
    "Vins d'Alsace Robert Karcher": {
        "description": "Aile işletmesi şarap evi, Alsace şarap tadımları ve mahzen turu. Riesling, Gewürztraminer ve Pinot Gris.",
        "description_en": "Family-run winery with Alsace wine tastings and cellar tour. Riesling, Gewürztraminer, and Pinot Gris."
    },
    "Caveau Saint-Pierre": {
        "description": "Tarihi şarap mahzeninde tadım mekanı, Alsace şarapları ve yöresel atıştırmalıklar. Romantik atmosfer ve şarap eğitimi.",
        "description_en": "Tasting venue in historic wine cellar with Alsace wines and regional snacks. Romantic atmosphere and wine education."
    },
    "Jadis et Gourmande": {
        "description": "Nostaljik dekorasyonlu çikolata ve şekerleme dükkanı, el yapımı lezzetler. Alsace bisküvileri, pralin ve hediyelik kutular.",
        "description_en": "Chocolate and confectionery shop with nostalgic decor and handmade treats. Alsace biscuits, pralines, and gift boxes."
    },
    "Manneken Pis (Colmar)": {
        "description": "Brüksel'deki ünlü heykelin küçük replikası, Petite Venise'de bulunur. Fotoğraf noktası, şehir mizahı ve turistik merak.",
        "description_en": "Small replica of famous Brussels statue, located in Petite Venise. Photo point, city humor, and tourist curiosity."
    },
    "Maison Kern": {
        "description": "Geleneksel Alsace dondurması ve tatlıları sunan butik pastane. Fruit tart, kougelhopf ve ev yapımı lezzetler.",
        "description_en": "Boutique pastry shop serving traditional Alsace ice cream and desserts. Fruit tart, kougelhopf, and homemade treats."
    },
    "Boulangerie L'Enfariné": {
        "description": "Artisan ekmek ve hamur işleri sunan geleneksel fırın. Croissant, pain au chocolat ve Alsace ekmek çeşitleri.",
        "description_en": "Traditional bakery serving artisan bread and pastries. Croissant, pain au chocolat, and Alsace bread varieties."
    },
    "Parc de la Montagne Verte": {
        "description": "Şehrin batısındaki doğa parkı, yürüyüş yolları ve bisiklet rotaları. Piknik alanları, kuş gözlemi ve yeşil kaçış.",
        "description_en": "Nature park west of city with walking paths and bike routes. Picnic areas, bird watching, and green escape."
    },
    "Domaine Viticole de la Ville de Colmar": {
        "description": "Şehir belediyesine ait şarap üretim tesisi, organik Alsace şarapları. Tadım turları, mahzen ziyareti ve yerel üretim.",
        "description_en": "City municipality-owned wine production facility with organic Alsace wines. Tasting tours, cellar visit, and local production."
    },
    "Corps de Garde": {
        "description": "16. yüzyıldan kalma tarihi askeri yapı, şimdi kültürel etkinliklere ev sahipliği yapıyor. Rönesans mimarisi ve şehir tarihi.",
        "description_en": "16th-century historic military building, now hosting cultural events. Renaissance architecture and city history."
    },
    "Cinéma CGR Colmar": {
        "description": "Modern sinema kompleksi, uluslararası filmler ve Fransız yapımları. IMAX, 3D ve aile eğlencesi.",
        "description_en": "Modern cinema complex with international films and French productions. IMAX, 3D, and family entertainment."
    },
    "Bowling du Grillen": {
        "description": "Bowling salonu ve eğlence merkezi, aile aktiviteleri ve gece hayatı. Bilardo, dart ve parti organizasyonları.",
        "description_en": "Bowling alley and entertainment center for family activities and nightlife. Pool, darts, and party organizations."
    },
    "Jardin des Papillons (Butterfly Garden)": {
        "description": "Tropikal kelebeklerin uçuştuğu kapalı bahçe, egzotik türler ve eğitici deneyim. Aileler ve doğa severler için ideal.",
        "description_en": "Enclosed garden where tropical butterflies fly with exotic species and educational experience. Ideal for families and nature lovers."
    },
    "Base Nautique de Colmar Houssen": {
        "description": "Su sporları merkezi, kayak, kano ve yüzme aktiviteleri. Yaz eğlencesi, plaj alanı ve açık hava sporları.",
        "description_en": "Water sports center with kayaking, canoeing, and swimming activities. Summer fun, beach area, and outdoor sports."
    },
    "Musée Mémorial des Combats de la Poche de Colmar": {
        "description": "İkinci Dünya Savaşı'nın Colmar Cebi muharebesini anlatan anıt müze. Savaş eserleri, belgeler ve tarihi farkındalık.",
        "description_en": "Memorial museum telling the story of WWII Colmar Pocket battle. War artifacts, documents, and historical awareness."
    },
    "Église Saints-Pierre-et-Paul": {
        "description": "Romanesk ve gotik öğeleri harmanlayan, 12. yüzyıldan kalma tarihi kilise. Vitray pencereler ve dini mimari.",
        "description_en": "12th-century historic church blending Romanesque and Gothic elements. Stained glass windows and religious architecture."
    },
    "Le Grillen": {
        "description": "Alsace usulü ızgara et ve yerel lezzetler sunan popüler restoran. Choucroute, flammkuchen ve bölgesel şaraplar.",
        "description_en": "Popular restaurant serving Alsace-style grilled meats and local flavors. Choucroute, flammkuchen, and regional wines."
    },
    "Parc à Cigognes (Stork Park)": {
        "description": "Alsace'ın simgesi leyleklerin korunduğu ve izlenebildiği park. Kuş gözlemi, doğa eğitimi ve bölgesel sembol.",
        "description_en": "Park where storks, symbol of Alsace, are protected and can be observed. Bird watching, nature education, and regional symbol."
    },
    "Eglise Saint-Georges": {
        "description": "Riquewihr'deki tarihi kilise, köyün dini ve kültürel merkezlerinden. Ortaçağ mimarisi ve huzurlu atmosfer.",
        "description_en": "Historic church in Riquewihr, one of village's religious and cultural centers. Medieval architecture and peaceful atmosphere."
    },
    "Montagne des Singes": {
        "description": "Serbest dolaşan Barbary maymunlarının yaşadığı hayvan parkı. Aileler için eğlence, doğal habitat ve hayvan etkileşimi.",
        "description_en": "Animal park where free-roaming Barbary macaques live. Entertainment for families, natural habitat, and animal interaction."
    },
    "Route des Crêtes": {
        "description": "Vosges Dağları'nın zirvelerini takip eden manzaralı sürüş rotası. Panoramik görünümler, doğa fotoğrafçılığı ve açık hava.",
        "description_en": "Scenic driving route following peaks of Vosges Mountains. Panoramic views, nature photography, and outdoors."
    },
    "Munster": {
        "description": "Ünlü Munster peynirinin doğduğu şirin Vosges kasabası. Peynir tadımları, manastır kalıntıları ve dağ manzarası.",
        "description_en": "Charming Vosges town where famous Munster cheese originated. Cheese tastings, monastery ruins, and mountain views."
    },
    "Mont Sainte-Odile": {
        "description": "Alsace'ın en kutsal yerlerinden biri, manastır ve hac merkezi. Panoramik manzara, yürüyüş yolları ve spiritüel atmosfer.",
        "description_en": "One of Alsace's most sacred places, monastery and pilgrimage center. Panoramic views, hiking trails, and spiritual atmosphere."
    },
    "Obernai": {
        "description": "Alsace şarap rotasının en çekici kasabalarından biri, ortaçağ surları ve pazarı. Yarı ahşap evler ve Alsace ruhu.",
        "description_en": "One of most attractive towns on Alsace wine route with medieval walls and market. Half-timbered houses and Alsace spirit."
    },
    "Ligne Maginot - Fort de Schoenenbourg": {
        "description": "İkinci Dünya Savaşı öncesi Fransız savunma hattının ziyarete açık bölümü. Yeraltı tünelleri, askeri tarih ve savaş müzesi.",
        "description_en": "Visitable section of pre-WWII French defense line. Underground tunnels, military history, and war museum."
    },
    "Bistrot des Lavandières": {
        "description": "Petite Venise'de kanal kenarı restoran, geleneksel Alsace yemekleri. Romantik konum, şarap eşliğinde yemek.",
        "description_en": "Canalside restaurant in Petite Venise with traditional Alsace dishes. Romantic location, dining with wine."
    },
    "Pâtisserie Gilg": {
        "description": "Alsace'ın en ünlü pastanelerinden biri, kougelhopf ve meyveli turtalar. El yapımı çikolatalar ve Noel spesiyalleri.",
        "description_en": "One of Alsace's most famous pastry shops with kougelhopf and fruit tarts. Handmade chocolates and Christmas specials."
    },
    "L'Un des Sens": {
        "description": "Modern Fransız mutfağını Alsace malzemeleriyle yorumlayan fine-dining restoran. Yaratıcı menü, şarap eşleştirmeleri.",
        "description_en": "Fine-dining restaurant interpreting modern French cuisine with Alsace ingredients. Creative menu, wine pairings."
    },
    "Chocolaterie Jacques Bockel": {
        "description": "El yapımı çikolata ve pralin ustası, Alsace'ın ödüllü çikolatacısı. Fabrika turları, tadım ve hediyelik kutular.",
        "description_en": "Handmade chocolate and praline master, Alsace's award-winning chocolatier. Factory tours, tasting, and gift boxes."
    },
    "Marché de Noël Gourmand": {
        "description": "Colmar'ın gurme odaklı Noel pazarı, yerel lezzetler ve şaraplar. Foie gras, vin chaud ve Alsace tatları.",
        "description_en": "Colmar's gourmet-focused Christmas market with local delicacies and wines. Foie gras, mulled wine, and Alsace flavors."
    },
    "Café Dussourd": {
        "description": "1929'dan beri hizmet veren tarihi kafe, art deco dekorasyon. Alsace kahvaltısı, pastalar ve nostaljik atmosfer.",
        "description_en": "Historic cafe serving since 1929 with art deco decoration. Alsace breakfast, pastries, and nostalgic atmosphere."
    }
}

filepath = 'assets/cities/colmar.json'
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

print(f"\n✅ Manually enriched {count} items (Colmar Batch 1).")
