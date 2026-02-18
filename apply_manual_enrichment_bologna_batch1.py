import json

# Manual enrichment data (Bologna Batch 1: 40 items)
updates = {
    "Basilica di San Petronio": {
        "description": "Dünyanın en büyük kiliseleri arasında yer alan, tamamlanmamış cephesiyle dikkat çeken gotik bazilika. İçindeki güneş saati ve Michelangelo'nun etkisi taşıyan şapellerle görülmeye değer.",
        "description_en": "A Gothic basilica among the world's largest churches, notable for its unfinished facade. Worth seeing with its interior sundial and chapels bearing Michelangelo's influence."
    },
    "Fontana del Nettuno": {
        "description": "Piazza del Nettuno'daki 16. yüzyıl Rönesans şaheseri, bronz Neptün heykeli ve deniz yaratıklarıyla. Giambologna'nın ustalığı, şehrin en ikonik simgelerinden.",
        "description_en": "A 16th-century Renaissance masterpiece in Piazza del Nettuno with bronze Neptune statue and sea creatures. Giambologna's mastery, one of the city's most iconic symbols."
    },
    "Le Due Torri (Asinelli & Garisenda)": {
        "description": "Bologna'nın simgesi ikiz kuleler, Asinelli 97 metre yüksekliğiyle tırmanılabilir. Ortaçağ güç gösterisi, 498 basamak ve muhteşem şehir panoraması.",
        "description_en": "Bologna's symbol twin towers, Asinelli climbable at 97 meters height. Medieval power display, 498 steps and magnificent city panorama."
    },
    "Basilica di Santo Stefano": {
        "description": "Yedi kiliseden oluşan benzersiz dini kompleks, erken Hıristiyanlık döneminden Roma mirasına. Iç içe geçen yapılar, avlular ve bin yıllık tarih yolculuğu.",
        "description_en": "A unique religious complex of seven churches, from early Christianity to Roman heritage. Interconnected structures, courtyards, and a thousand-year journey through history."
    },
    "Pinacoteca Nazionale": {
        "description": "Emilia-Romagna'nın en önemli sanat müzesi, Rönesans'tan Barok'a İtalyan ustalarının koleksiyonu. Raffaello, Carracci kardeşler ve Bologna okulu eserleri.",
        "description_en": "Emilia-Romagna's most important art museum, collection of Italian masters from Renaissance to Baroque. Works of Raphael, Carracci brothers, and Bologna school."
    },
    "Museo Civico Archeologico": {
        "description": "Etrüsk, Roma ve Mısır uygarlıklarından eserleri sergileyen arkeoloji müzesi. Antik mezar buluntuları, heykeller ve Emilia-Romagna'nın prehistorik geçmişi.",
        "description_en": "An archaeology museum exhibiting artifacts from Etruscan, Roman, and Egyptian civilizations. Ancient tomb finds, sculptures, and Emilia-Romagna's prehistoric past."
    },
    "Museo della Storia di Bologna": {
        "description": "Palazzo Pepoli'de Bologna'nın tarihini multimedya sergilerle anlatan modern müze. Şehrin evrimini interaktif olarak keşfedin ve yerel mirası öğrenin.",
        "description_en": "A modern museum in Palazzo Pepoli telling Bologna's history with multimedia exhibitions. Discover the city's evolution interactively and learn about local heritage."
    },
    "Finestrella (Venedik Penceresi)": {
        "description": "Via Piella'daki küçük pencereden görülen gizli kanal, Bologna'nın 'Küçük Venedik'i. Ortaçağ kanallarının kalıntısı, şaşırtıcı ve romantik manzara.",
        "description_en": "A hidden canal seen through a small window on Via Piella, Bologna's 'Little Venice'. Remnant of medieval canals, surprising and romantic scenery."
    },
    "Portico di San Luca": {
        "description": "Dünyanın en uzun portiko'su (3.8 km), 666 kemerle şehirden Santuario di San Luca'ya. Zorlu tırmanış, dini hac ve panoramik manzaralarla ödüllendirici.",
        "description_en": "World's longest portico (3.8 km), with 666 arches from city to Santuario di San Luca. Challenging climb, religious pilgrimage, rewarding with panoramic views."
    },
    "Giardini Margherita": {
        "description": "Bologna'nın en büyük ve sevilen şehir parkı, gölet, bahçeler ve açık hava aktiviteleriyle. Piknik, jogging ve aileler için yeşil kaçış.",
        "description_en": "Bologna's largest and most beloved city park with pond, gardens, and outdoor activities. Green escape for picnics, jogging, and families."
    },
    "Quadrilatero (Eski Pazar)": {
        "description": "Ortaçağ'dan beri aktif olan tarihi gıda pazarı bölgesi, dar sokaklar ve esnaf dükkanlarıyla. Taze makarna, peynir, şarküteri ve Bologna lezzetlerinin kalbi.",
        "description_en": "Historic food market area active since medieval times with narrow streets and artisan shops. Heart of Bologna flavors with fresh pasta, cheese, and charcuterie."
    },
    "Trattoria Anna Maria": {
        "description": "Ev yapımı tagliatelle al ragù ve tortellini'nin en otantik halini sunan efsane trattoria. Duvarlarında ünlülerin fotoğrafları, Bologna mutfağının tapınağı.",
        "description_en": "Legendary trattoria serving homemade tagliatelle al ragù and tortellini in most authentic form. Celebrity photos on walls, temple of Bologna cuisine."
    },
    "Mercato di Mezzo": {
        "description": "Quadrilatero'nun kalbindeki yenilenmiş pazar hali, sokak yemekleri ve yerel lezzetler. Crescentina, mortadella ve aperativo için trendy buluşma noktası.",
        "description_en": "Renovated market hall in heart of Quadrilatero with street food and local flavors. Trendy meeting point for crescentina, mortadella, and aperitivo."
    },
    "Cremeria Funivia": {
        "description": "El yapımı gelato ustası, doğal malzemeler ve yaratıcı tatlarla ünlü. Fıstıklı, stracciatella ve mevsimlik meyve sorbeleryle, şehrin en iyilerinden.",
        "description_en": "Handmade gelato master famous for natural ingredients and creative flavors. Among the city's best with pistachio, stracciatella, and seasonal fruit sorbets."
    },
    "Le Stanze": {
        "description": "Eski bir şapelde kurulan atmosferik kokteyl barı ve restoran. Fresk tavanlar, harika kokteyller ve benzersiz tarihi atmosferle, gece hayatının mücevheri.",
        "description_en": "An atmospheric cocktail bar and restaurant in an old chapel. Frescoed ceilings, amazing cocktails, and unique historic atmosphere, nightlife gem."
    },
    "Camera a Sud": {
        "description": "Güney İtalya lezzetlerini sunan, Napoli pizzası ve Sicilya yemekleriyle ünlü restoran. Sıcak atmosfer, otantik tarifler ve Akdeniz esintisi.",
        "description_en": "A restaurant serving Southern Italian flavors, famous for Neapolitan pizza and Sicilian dishes. Warm atmosphere, authentic recipes, and Mediterranean breeze."
    },
    "La Prosciutteria Bologna": {
        "description": "Parma jambonu ve İtalyan şarküteri tabaklarının tapınağı. Peynir seçkisi, yerel şaraplar ve aperitivo için mükemmel ortam.",
        "description_en": "Temple of Parma ham and Italian charcuterie platters. Cheese selection, local wines, and perfect setting for aperitivo."
    },
    "Forno Brisa": {
        "description": "El yapımı ekmek, focaccia ve geleneksel İtalyan fırın ürünleri sunan artisan fırın. Taze pişmiş lezzetler, kahvaltı ve hafif öğle yemeği için ideal.",
        "description_en": "Artisan bakery serving handmade bread, focaccia, and traditional Italian baked goods. Fresh-baked delights, ideal for breakfast and light lunch."
    },
    "Mozzarella e Basilico": {
        "description": "Taze mozzarella, burrata ve Campania süt ürünlerinin satıldığı ve tadıldığı butik dükkan. Caprese, bruschetta ve İtalyan light lunch deneyimi.",
        "description_en": "Boutique shop selling and tasting fresh mozzarella, burrata, and Campania dairy. Caprese, bruschetta, and Italian light lunch experience."
    },
    "Pizzeria Da Michele Bologna": {
        "description": "Ünlü Napoli pizzacısının Bologna şubesi, Margherita ve Marinara'nın otantik versiyonları. Uzun kuyruklar, ancak beklemeye değer lezzet.",
        "description_en": "Bologna branch of famous Neapolitan pizzeria, authentic versions of Margherita and Marinara. Long queues but flavor worth waiting for."
    },
    "Tigellino": {
        "description": "Emilia-Romagna'nın geleneksel tigelle ekmeğinin en iyi örneklerini sunan mekan. Şarküteri, peynir ve yerel dolgularla, bölgesel lezzet deneyimi.",
        "description_en": "A venue serving best examples of Emilia-Romagna's traditional tigelle bread. Regional flavor experience with charcuterie, cheese, and local fillings."
    },
    "Mortadella Shop": {
        "description": "Bologna'nın en ünlü yerel ürünü mortadella'nın ana üssü. Tadım, sandviç ve eve götürmek için paketleme, mortadella tutkunları için cennet.",
        "description_en": "Headquarters of mortadella, Bologna's most famous local product. Tasting, sandwiches, and packaging to take home, paradise for mortadella lovers."
    },
    "Lampadina Café": {
        "description": "Vintage dekorasyonu ve rahat atmosferiyle dikkat çeken, specialty coffee ve brunch sunan kafe. Kitap köşeleri, sabah kahvaltısı ve yaratıcı mekan.",
        "description_en": "A cafe notable for vintage decor and relaxed atmosphere, serving specialty coffee and brunch. Book corners, morning breakfast, and creative venue."
    },
    "Gamberini": {
        "description": "1907'den beri hizmet veren tarihi pastane, kruvasan ve İtalyan kahvaltısının adresi. Nostaljik atmosfer, taze pasta ve Bolognese kahve kültürü.",
        "description_en": "Historic pastry shop serving since 1907, address for croissants and Italian breakfast. Nostalgic atmosphere, fresh pastries, and Bolognese coffee culture."
    },
    "Sorbetteria Castiglione": {
        "description": "Artisan gelato ve sorbelerin en kaliteli halini sunan, doğal malzemelerle çalışan dondurma dükkanı. Organik süt, taze meyve ve İtalyan dondurma sanatı.",
        "description_en": "Ice cream shop serving highest quality artisan gelato and sorbets, working with natural ingredients. Organic milk, fresh fruit, and Italian ice cream art."
    },
    "Ristorante Donatello": {
        "description": "Klasik Bologna mutfağını geleneksel tariflerle sunan köklü restoran. Tortellini in brodo, lasagne ve tagliatelle al ragù'nun otantik versiyonları.",
        "description_en": "Established restaurant serving classic Bologna cuisine with traditional recipes. Authentic versions of tortellini in brodo, lasagne, and tagliatelle al ragù."
    },
    "Pasticceria Regina di Quadri": {
        "description": "Quadrilatero'daki tarihi pastane, Bologna'nın geleneksel tatlıları ve kahvesi. Torta di riso, certosino ve İtalyan pasta ustası.",
        "description_en": "Historic pastry shop in Quadrilatero with Bologna's traditional desserts and coffee. Torta di riso, certosino, and Italian pastry master."
    },
    "Zoo": {
        "description": "Aperitivo ve gece hayatının trendy adresi, DJ setleri ve canlı atmosferiyle. Kokteyller, sosyal sahne ve Bologna'nın genç kalabalığı.",
        "description_en": "Trendy address for aperitivo and nightlife with DJ sets and lively atmosphere. Cocktails, social scene, and Bologna's young crowd."
    },
    "Enoteca Italiana": {
        "description": "İtalyan şaraplarının geniş seçkisini sunan, tadım ve satış yapan şarap barı. Sommelier önerileri, yerel peynirler ve şarap eğitimi.",
        "description_en": "Wine bar offering wide selection of Italian wines with tasting and sales. Sommelier recommendations, local cheeses, and wine education."
    },
    "Il Veliero": {
        "description": "Deniz ürünleri ve Adriyatik balıklarının en taze halini sunan şık restoran. Risotto ai frutti di mare, ızgara balık ve Akdeniz lezzetleri.",
        "description_en": "Elegant restaurant serving freshest seafood and Adriatic fish. Risotto ai frutti di mare, grilled fish, and Mediterranean flavors."
    },
    "Vineria Favalli": {
        "description": "Emilia-Romagna şaraplarına odaklanan, samimi atmosferli şarap barı. Lambrusco, Sangiovese ve yerel şarküteri eşliğinde tadım.",
        "description_en": "Wine bar focusing on Emilia-Romagna wines with intimate atmosphere. Tasting with Lambrusco, Sangiovese, and local charcuterie."
    },
    "La Sorbetteria": {
        "description": "Doğal meyve sorbelerinin ve vegan dondurma seçeneklerinin adresi. Taze, sağlıklı ve lezzetli alternatif, yaz günlerinin favorisi.",
        "description_en": "Address for natural fruit sorbets and vegan ice cream options. Fresh, healthy, and delicious alternative, summer favorite."
    },
    "Biblioteca Salaborsa": {
        "description": "Tarihi Palazzo d'Accursio'da kurulan modern kütüphane, cam taban altında Roma kalıntıları. Okuma alanları, sergi ve kültürel etkinlikler.",
        "description_en": "Modern library in historic Palazzo d'Accursio with Roman remains under glass floor. Reading areas, exhibitions, and cultural events."
    },
    "San Colombano - Tagliavini Collection": {
        "description": "Tarihi müzik aletleri koleksiyonunu barındıran restore edilmiş kilise. Rönesans'tan 19. yüzyıla klavye enstrümanları ve konser salonu.",
        "description_en": "Restored church housing historic musical instruments collection. Keyboard instruments from Renaissance to 19th century and concert hall."
    },
    "Basilica di San Giacomo Maggiore": {
        "description": "13. yüzyıldan kalma gotik-Rönesans kilisesi, Bentivoglio şapeli freskleriyle ünlü. Lorenzo Costa ve Francesco Francia'nın şaheserleri.",
        "description_en": "13th-century Gothic-Renaissance church, famous for Bentivoglio chapel frescoes. Masterpieces of Lorenzo Costa and Francesco Francia."
    },
    "Palazzo Re Enzo": {
        "description": "13. yüzyılda Kral Enzo'nun hapsedildiği Ortaçağ sarayı, Piazza Maggiore'da. Gotik mimari, tarihi etkinlikler ve şehrin politik geçmişi.",
        "description_en": "Medieval palace where King Enzo was imprisoned in 13th century, in Piazza Maggiore. Gothic architecture, historic events, and city's political past."
    },
    "Torre degli Asinelli": {
        "description": "Bologna'nın tırmanılabilir kulesi, 498 basamak sonunda 360 derece şehir manzarası. İtalya'nın en yüksek eğik kulelerinden, meydan okuma ve ödül.",
        "description_en": "Bologna's climbable tower, 360-degree city view after 498 steps. Among Italy's tallest leaning towers, challenge and reward."
    },
    "Porta Galliera": {
        "description": "Ortaçağ surlarının kalıntısı tarihi şehir kapısı, restore edilmiş yapısıyla dikkat çekiyor. Bologna'nın eski savunma sisteminin örneği.",
        "description_en": "Historic city gate remnant of medieval walls, notable for restored structure. Example of Bologna's old defense system."
    },
    "Chiesa di Santa Maria dei Servi": {
        "description": "14. yüzyıldan kalma gotik kilise, etkileyici portiko ve Cimabue'nin Madonna'sıyla. Huzurlu atmosfer, sanat hazineleri ve dini miras.",
        "description_en": "14th-century Gothic church with impressive portico and Cimabue's Madonna. Peaceful atmosphere, art treasures, and religious heritage."
    },
    "Fontana Vecchia": {
        "description": "Quadrilatero'daki tarihi çeşme, ortaçağ pazarının su kaynağı kalıntısı. Şehrin eski su sisteminin hatırası, fotoğraf için şirin nokta.",
        "description_en": "Historic fountain in Quadrilatero, remnant of medieval market's water source. Memory of city's old water system, cute spot for photos."
    }
}

filepath = 'assets/cities/bologna.json'
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

print(f"\n✅ Manually enriched {count} items (Bologna Batch 1).")
