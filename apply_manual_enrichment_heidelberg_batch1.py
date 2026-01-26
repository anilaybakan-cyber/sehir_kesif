import json

# Manual enrichment data (Heidelberg - ALL 32 items)
updates = {
    "Carl Bosch Müzesi": {
        "description": "Nobel ödüllü kimyager Carl Bosch'un hayatına ve teknolojinin tarihine adanmış müze. Otomotiv ve kimya meraklıları için hazine.",
        "description_en": "Museum dedicated to life of Nobel laureate chemist Carl Bosch and history of technology. Treasure for automotive and chemistry enthusiasts."
    },
    "Chocolaterie Yilliy": {
        "description": "El yapımı çikolataları ve 'Öğrenci Öpücüğü' (Studentenkuss) tatlısı ile ünlü şirin dükkan. Eski şehirde tatlı bir mola.",
        "description_en": "Cute shop famous for handmade chocolates and 'Student's Kiss' (Studentenkuss) sweet. Great sweet break in Old Town."
    },
    "Neckarsteinach Dört Kale": {
        "description": "Neckar Nehri kıyısında, efsanelerle dolu dört ortaçağ kalesinin (Vorderburg, Mittelburg, Hinterburg, Schadeck) bulunduğu kasaba.",
        "description_en": "Town on Neckar River home to four medieval castles (Vorderburg, Mittelburg, Hinterburg, Schadeck) full of legends."
    },
    "Untere Straße (Bar Sokağı)": {
        "description": "Heidelberg gece hayatının kalbi, yan yana sıralanmış barlar ve publar. Öğrenci enerjisi, ucuz içecekler ve canlı müzik.",
        "description_en": "Heart of Heidelberg nightlife, lined with bars and pubs. Student energy, cheap drinks, and live music."
    },
    "Destille": {
        "description": "Untere Straße'nin en ikonik barlarından biri. Sanatsal dekor, 'Melon shot' ve yerel öğrencilerin vazgeçilmez buluşma noktası.",
        "description_en": "One of most iconic bars on Untere Straße. Artistic decor, 'Melon shot', and indispensable meeting point for local students."
    },
    "Havana Bar": {
        "description": "Küba temalı kokteyl barı, salsa müziği ve mojito. Heidelberg'in kalbinde Latin rüzgarları ve sıcak atmosfer.",
        "description_en": "Cuban-themed cocktail bar, salsa music, and mojito. Latin winds and warm atmosphere in heart of Heidelberg."
    },
    "Nachtschwärmer": {
        "description": "Gece kuşları için sabaha kadar açık olan klasik Alman pub'ı (Kneipe). Samimi ortam, futbol maçları ve bira kültürü.",
        "description_en": "Classic German pub (Kneipe) open until morning for night owls. Friendly atmosphere, football matches, and beer culture."
    },
    "Goldener Hecht": {
        "description": "Eski Köprü'nün hemen ayağında tarihi restoran. Goethe'nin de uğradığı mekan, geleneksel Alman mutfağı ve nehir manzarası.",
        "description_en": "Historic restaurant right at foot of Old Bridge. Place visited by Goethe, traditional German cuisine, and river views."
    },
    "Wirtshaus Zum Nepomuk": {
        "description": "Nehri gören terasıyla ünlü, rustik Alman hanı. Schnitzel, geyik eti ve yerel şaraplarla romantik bir akşam yemeği.",
        "description_en": "Rustic German inn famous for its terrace overlooking river. Romantic dinner with Schnitzel, venison, and local wines."
    },
    "Weinstube Schnitzelbank": {
        "description": "Turistlerden gizlenmiş, ahşap masalı otantik şarap evi. Duvarlarda eski yazılar, dev porsiyonlar ve samimi Alman misafirperverliği.",
        "description_en": "Authentic wine house with wooden tables hidden from tourists. Old writings on walls, huge portions, and friendly German hospitality."
    },
    "Sakura Sushi": {
        "description": "Bergheim bölgesinde taze ve kaliteli suşi sunan popüler Japon restoranı. Modern dekor, hızlı servis ve lezzetli rollar.",
        "description_en": "Popular Japanese restaurant serving fresh and quality sushi in Bergheim. Modern decor, fast service, and delicious rolls."
    },
    "Palmbrau Gasse": {
        "description": "Hauptstraße üzerinde tarihi bira salonu atmosferi. Kendi yapımları biralar, sosis tabağı ve ahşap fıçı dekorasyonu.",
        "description_en": "Historic beer hall atmosphere on Hauptstraße. Home-brewed beers, sausage platter, and wooden barrel decoration."
    },
    "Cafe Gundel": {
        "description": "Heidelberg'in en eski ve köklü pastanelerinden biri. Geleneksel Alman pastaları, kahve keyfi ve nostaljik iç mekan.",
        "description_en": "One of oldest and most established patisseries in Heidelberg. Traditional German cakes, coffee joy, and nostalgic interior."
    },
    "Gelato Go": {
        "description": "Bismarckplatz yakınında İtalyan usulü dondurmacı. Doğal malzemeler, yoğun lezzetler ve yürüyüş öncesi serinleme durağı.",
        "description_en": "Italian style ice cream shop near Bismarckplatz. Natural ingredients, intense flavors, and cooling stop before walking."
    },
    "Cafe Frisch": {
        "description": "Neuenheim pazar meydanında yerel halkın favorisi kafe. Güneşli teras, ev yapımı kahvaltılar ve rahat bir pazar sabahı.",
        "description_en": "Locals' favorite cafe at Neuenheim market square. Sunny terrace, homemade breakfasts, and relaxing Sunday morning."
    },
    "Tee Kontor": {
        "description": "Yüzlerce çeşit çayın satıldığı mistik kokulu dükkan. Çay seremonisi aksesuarları, hediyelikler ve uzman tavsiyeleri.",
        "description_en": "Mystic scented shop selling hundreds of tea varieties. Tea ceremony accessories, souvenirs, and expert advice."
    },
    "Providenzkirche": {
        "description": "Ana cadde üzerindeki Protestan kilisesi, 17. yüzyıl barok mimarisi. Şehrin en eski orgu ve huzurlu bir dua molası.",
        "description_en": "Protestant church on main street, 17th-century baroque architecture. City's oldest organ and peaceful prayer break."
    },
    "Jesuitenkirche": {
        "description": "Barok stilin şehirdeki en görkemli örneği, Cizvit Kilisesi. Beyaz içi mekan, altın detaylar ve Cizvit Koleji tarihi.",
        "description_en": "City's most magnificent example of Baroque style, Jesuit Church. White interior, gold details, and Jesuit College history."
    },
    "Marstall (Eski Ahır)": {
        "description": "Eskiden saray ahırları olan, şimdi üniversite yemekhanesi ve müzesi. Nehir kenarında tarihi bina, öğrenci yaşamının merkezi.",
        "description_en": "Former palace stables, now university cafeteria and museum. Historic building by river, center of student life."
    },
    "Hexenturm (Cadı Kulesi)": {
        "description": "Ortaçağ şehir surlarından kalan tek kule. Geçmişte hapishane olarak kullanılan, efsanelerle dolu gizemli yapı.",
        "description_en": "Only remaining tower from medieval city walls. Mysterious structure full of legends, used as prison in past."
    },
    "Botanik Bahçesi": {
        "description": "Almanya'nın en eski botanik bahçelerinden biri, üniversiteye ait. Nadir orkideler, seralar ve bilimsel bitki koleksiyonu.",
        "description_en": "One of Germany's oldest botanical gardens, belonging to university. Rare orchids, greenhouses, and scientific plant collection."
    },
    "Stadtwald (Şehir Ormanı)": {
        "description": "Heidelberg'i çevreleyen geniş ormanlık alan. Yürüyüş parkurları, temiz hava ve şehirden doğaya kaçış rotaları.",
        "description_en": "Vast forested area surrounding Heidelberg. Hiking trails, fresh air, and escape routes from city to nature."
    },
    "Handschuhsheim Bağları": {
        "description": "Şehrin kuzeyindeki üzüm bağları ve şarap yolu. Doğa yürüyüşü, panoramik manzara ve sonbaharda renk cümbüşü.",
        "description_en": "Vineyards and wine route in north of city. Nature hiking, panoramic views, and riot of colors in autumn."
    },
    "Iqbal Ufer": {
        "description": "Neckar Nehri kıyısında, şair Muhammed İkbal anısına isimlendirilmiş park ve yürüyüş yolu. Şiirsel manzara ve dinginlik.",
        "description_en": "Park and promenade on Neckar River named after poet Muhammad Iqbal. Poetic scenery and tranquility."
    },
    "Antiquariat Hatry": {
        "description": "Eski kitap kokusuyla dolu büyüleyici sahaf. Nadir baskılar, sanat kitapları ve kitap kurtları için hazine sandığı.",
        "description_en": "Charming second-hand bookstore filled with smell of old books. Rare editions, art books, and treasure chest for bookworms."
    },
    "Heidelberg Seramik": {
        "description": "Geleneksel Alman seramik sanatının sergilendiği dükkan. El boyaması kaseler, kupalar ve otantik hatıralar.",
        "description_en": "Shop exhibiting traditional German ceramic art. Hand-painted bowls, mugs, and authentic souvenirs."
    },
    "Galeria Kaufhof": {
        "description": "Bismarckplatz'da büyük departmanlı mağaza. Giyim, kozmetik, ev eşyası ve en üst katta manzara restoranı.",
        "description_en": "Large department store at Bismarckplatz. Clothing, cosmetics, home goods, and view restaurant on top floor."
    },
    "Wochenmarkt": {
        "description": "Marktplatz'da kurulan haftalık pazar. Taze yerel meyve, sebze, peynir ve çiçeklerle dolu renkli tezgahlar.",
        "description_en": "Weekly market set up at Marktplatz. Colorful stalls full of fresh local fruits, vegetables, cheese, and flowers."
    },
    "Kano Kiralama Neckar": {
        "description": "Nehirde kano yaparak şehri su seviyesinden keşfetme imkanı. Eski Köprü'nün altından kürek çekmek ve macera.",
        "description_en": "Opportunity to explore city from water level by canoeing on river. Paddling under Old Bridge and adventure."
    },
    "Segway Turu Heidelberg": {
        "description": "Filozoflar Yolu ve nehir kıyısında rehberli Segway gezisi. Eğlenceli, hızlı ve yorulmadan şehri gezme yolu.",
        "description_en": "Guided Segway tour on Philosophers' Way and river bank. Fun, fast way to tour city without getting tired."
    },
    "Fotoğraf Yürüyüşü": {
        "description": "Şehrin en fotostik noktalarını (Köprü, Kale, Dar Sokaklar) kapsayan rota. Işık, kompozisyon ve anı yakalama.",
        "description_en": "Route covering city's most photogenic spots (Bridge, Castle, Narrow Streets). Light, composition, and capturing memories."
    },
    "Şarap Tadımı Turu": {
        "description": "Bölgenin (Baden) riesling ve pinot noir şaraplarını keşfetme. Yerel şarap evlerinde tadım ve bağcılık kültürü.",
        "description_en": "Discovering region's (Baden) Riesling and Pinot Noir wines. Tasting in local wine houses and viticulture culture."
    }
}

filepath = 'assets/cities/heidelberg.json'
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

print(f"\n✅ Manually enriched {count} items (Heidelberg - COMPLETE).")
