import json

# Manual enrichment data (Hallstatt Batch 1: 35 items)
updates = {
    "Skywalk Hallstatt": {
        "description": "UNESCO Dünya Mirası listesindeki köyün ve turkuaz gölün 360 derece panoramik manzarasını sunan, uçurumun kenarına uzanan cam teras. Tuz mağaraları turuna dahil olan bu platform, fotoğrafçıların ve manzara meraklılarının birincil durağı.",
        "description_en": "A glass terrace extending to the edge of a cliff, offering a 360-degree panoramic view of the UNESCO World Heritage village and turquoise lake. Included in the salt mines tour, this platform is the primary stop for photographers and scenery enthusiasts."
    },
    "Salzwelten Hallstatt": {
        "description": "7.000 yıllık tarihe sahip dünyanın en eski tuz madeni, yeraltı kaydırakları ve tuz gölleriyle hem eğitici hem de heyecan verici bir deneyim sunuyor. Maden işçilerinin ahşap kaydırağından kayarak çalıştığı bu antik maden, tarih öncesi yaşama açılan bir kapı.",
        "description_en": "The world's oldest salt mine with 7,000 years of history offers both educational and exciting experience with underground slides and salt lakes. This ancient mine where miners worked sliding down wooden slides is a gateway to prehistoric life."
    },
    "Hallstatt Postcard Viewpoint": {
        "description": "Hallstatt'ın dünya çapında ünlü kartpostal fotoğrafının çekildiği, gölün kuzey kıyısındaki efsanevi manzara noktası. Ahşap evlerin suya yansıdığı bu ikonik görüntü, milyonlarca turisti buraya çeken büyülü bir an yakalamayı vaat ediyor.",
        "description_en": "The legendary viewpoint on the northern shore of the lake where Hallstatt's world-famous postcard photo is taken. This iconic image where wooden houses reflect on the water promises to capture a magical moment attracting millions of tourists."
    },
    "Marktplatz Hallstatt": {
        "description": "Çiçeklerle süslü ahşap evlerle çevrili, Hallstatt'ın tarihi kalbinin attığı renkli pazar meydanı. Kafeler, hediyelik eşya dükkanları ve tarihi binaların çerçevelediği bu alan, köy yaşamının ve alpçe atmosferin merkezi.",
        "description_en": "The colorful market square at the historic heart of Hallstatt, surrounded by wooden houses decorated with flowers. This area framed by cafes, souvenir shops, and historic buildings is the center of village life and alpine atmosphere."
    },
    "Beinhaus": {
        "description": "12. yüzyıldan kalma kemiklikte, 600'den fazla insan kafatasının boyalı olarak sergilendiği eşsiz ve biraz ürkütücü bir mekan. Yer sıkıntısı nedeniyle ortaya çıkan bu Avusturya geleneği, ölümle yüzleşmenin benzersiz bir kültürel ifadesi.",
        "description_en": "A unique and somewhat eerie place where more than 600 human skulls are painted and displayed in a 12th-century ossuary. This Austrian tradition arising from space constraints is a unique cultural expression of confronting death."
    },
    "5 Fingers": {
        "description": "Dachstein dağlarının zirvesinde, 400 metre boşluğa uzanan el şeklindeki beş ayrı platformdan oluşan nefes kesici panoramik seyir noktası. Her parmak farklı bir perspektif sunar, cam tabanlı platform ise adrenalin tutkunları için özel bir deneyim.",
        "description_en": "A breathtaking panoramic viewpoint consisting of five separate hand-shaped platforms extending 400 meters into the void at the summit of Dachstein mountains. Each finger offers a different perspective, and the glass-bottomed platform is a special experience for adrenaline enthusiasts."
    },
    "Dachstein Giant Ice Cave": {
        "description": "Dachstein dağının içindeki devasa buz kütleleri, donmuş şelaleler ve ışık gösterisiyle büyüleyen doğal bir harika. Binlerce yıl içinde oluşan bu buz mağarası, yazın bile dondurucu soğukluğu ve masalsı görüntüsüyle ziyaretçileri hayrete düşürüyor.",
        "description_en": "A natural wonder inside Dachstein mountain enchanting with giant ice masses, frozen waterfalls, and light show. This ice cave formed over thousands of years amazes visitors with its freezing cold and fairytale appearance even in summer."
    },
    "Waldbachstrub Waterfall": {
        "description": "Echern Vadisi'nin yemyeşil ormanları içinde gürül gürül akan, 90 metre yüksekliğindeki etkileyici şelale. Hallstatt'tan kolay bir yürüyüşle ulaşılan bu doğa harikası, sıcak yaz günlerinde serinlemek ve doğanın gücünü hissetmek için mükemmel.",
        "description_en": "An impressive 90-meter-high waterfall roaring through the lush green forests of Echern Valley. Accessible by an easy walk from Hallstatt, this natural wonder is perfect for cooling off on hot summer days and feeling the power of nature."
    },
    "Lake Hallstatt Boat Rental": {
        "description": "Elektrikli tekneler kiralayarak sessiz ve huzurlu bir göl turu yapabileceğiniz, Hallstatt limanındaki tekne kiralama servisi. Pedallı veya motorlu seçeneklerle, gölün kristal sularında kendi hızınızda keşif yapmanın tadını çıkarın.",
        "description_en": "A boat rental service at Hallstatt harbor where you can take a quiet and peaceful lake tour by renting electric boats. With pedal or motorized options, enjoy exploring at your own pace in the crystal waters of the lake."
    },
    "Seewirt Zauner": {
        "description": "Gölden taze tutulan 'Reinanke' alabalığıyla ünlü, göl manzaralı terasında Avusturya mutfağının en iyi örneklerini sunan geleneksel restoran. Nesiller boyu aile işletmesi olarak sürdürülen bu mekan, bölgenin gastronomik mirasını yaşatıyor.",
        "description_en": "A traditional restaurant famous for freshly caught 'Reinanke' trout from the lake, offering the best examples of Austrian cuisine on its lakeside terrace. Maintained as a family business for generations, this venue keeps the region's gastronomic heritage alive."
    },
    "Brauhaus": {
        "description": "Göl kenarında, asırlık kestane ağaçlarının gölgesinde kendi biralarını üreten otantik bira evi ve restoran. Yerel bira çeşitleri, Avusturya usulü sosis ve schnitzele eşlik eden cömert porsiyonlarla, huzurlu bir yemek deneyimi.",
        "description_en": "An authentic brewery and restaurant producing its own beers by the lake, in the shade of centuries-old chestnut trees. A peaceful dining experience with local beer varieties, generous portions accompanying Austrian-style sausages and schnitzel."
    },
    "Café Derbl": {
        "description": "Marktplatz meydanını izleyebileceğiniz konumuyla, ev yapımı apfelstrudel ve Avusturya kahveleriyle ünlü nostaljik kafe. Ahşap iç mekanı, sıcak atmosferi ve taze pastalarıyla, köy gezisine mola vermek için ideal.",
        "description_en": "A nostalgic cafe famous for homemade apfelstrudel and Austrian coffees with its position overlooking Marktplatz square. Ideal for taking a break from village touring with its wooden interior, warm atmosphere, and fresh pastries."
    },
    "Koppenwinkelsee": {
        "description": "Obertraun yakınlarında turistik kalabalıklardan uzak, turkuaz renkli kristal berraklığındaki suları ve çam ormanlarıyla çevrili saklı göl. Piknik yapmak, yüzmek ve doğanın sessizliğini dinlemek için Salzkammergut'un gizli cennetlerinden biri.",
        "description_en": "A hidden lake near Obertraun away from tourist crowds, with turquoise crystal-clear waters and surrounded by pine forests. One of Salzkammergut's hidden paradises for picnicking, swimming, and listening to nature's silence."
    },
    "Dachstein Krippenstein Seilbahn": {
        "description": "Dachstein zirvesine ve meşhur buz mağaralarına ulaştıran, muhteşem Alp manzaraları sunan modern teleferik hattı. 5 Fingers platformu, Giant Ice Cave ve Mammoth Cave'i tek bilette keşfetmenin başlangıç noktası.",
        "description_en": "A modern cable car line to Dachstein summit and famous ice caves, offering stunning Alpine views. The starting point for discovering 5 Fingers platform, Giant Ice Cave, and Mammoth Cave in a single ticket."
    },
    "Landbettler": {
        "description": "Obertraun'da sırtçantalı gezginlerin ve budget tourists'lerin buluştuğu, samimi ortamı ve uygun fiyatlarıyla popüler bar ve restoran. Yerel birar, basit ama doyurucu yemekler ve canlı sosyal atmosferiyle, bölgenin en rahat mekanlarından.",
        "description_en": "A popular bar and restaurant in Obertraun where backpackers and budget tourists meet, with its friendly atmosphere and affordable prices. One of the region's most relaxed venues with local beers, simple but satisfying food, and lively social atmosphere."
    },
    "Sarsteinalm": {
        "description": "Sarstein dağının yamaçlarında, panoramik göl ve dağ manzaralı geleneksel Alp kulübesi. Taze dağ peynirleri, ev yapımı çorbalar ve klasik Avusturya yemekleriyle, yürüyüşçülerin ödüllendirici mola noktası.",
        "description_en": "A traditional Alpine hut on the slopes of Sarstein mountain with panoramic lake and mountain views. A rewarding rest point for hikers with fresh mountain cheeses, homemade soups, and classic Austrian dishes."
    },
    "Predigstuhl Bad Goisern": {
        "description": "Hallstättersee gölünü kuzey ucundan görebileceğiniz, dramatik kayalık oluşumlarla çevrili muazzam panoramik manzara noktası. Zorlu ama ödüllendirici yürüyüş rotasının zirvesinde, nefes kesici bir Salzkammergut manzarası sizi bekliyor.",
        "description_en": "A magnificent panoramic viewpoint at the northern end overlooking Lake Hallstättersee, surrounded by dramatic rock formations. At the summit of a challenging but rewarding hiking route, a breathtaking Salzkammergut panorama awaits you."
    },
    "Chorinsky-Klause": {
        "description": "19. yüzyılda kereste taşımacılığı için inşa edilmiş, tarihi ahşap bent ve suyolu sistemi. Endüstriyel mirasın korunduğu bu alan, geçmişteki kereste dağıtım ağına ışık tutan açık hava müzesi niteliğinde.",
        "description_en": "A historic wooden dam and waterway system built for timber transportation in the 19th century. This area where industrial heritage is preserved is like an open-air museum shedding light on the timber distribution network of the past."
    },
    "Goiserer Hütte": {
        "description": "Kalmberg zirvesine yakın, yerel Avusturya lezzetleri sunan geleneksel dağ kulübesi. Schnitzel, Kaiserschmarrn ve taze peynir tabakları ile dağcıları ve doğa yürüyüşçülerini ağırlayan, samimi ve otantik bir mekan.",
        "description_en": "A traditional mountain hut near Kalmberg summit, offering local Austrian flavors. An intimate and authentic venue hosting mountaineers and hikers with schnitzel, Kaiserschmarrn, and fresh cheese platters."
    },
    "Hand.Werk.Haus Salzkammergut": {
        "description": "Salzkammergut bölgesinin zengin el sanatları geleneğini yaşatan, zanaatkarların çalışmalarını izleyebileceğiniz ve satın alabileceğiniz kültür merkezi. Ahşap oyma, seramik, tekstil ve geleneksel kostümlerle, yerel kültürün canlı vitrini.",
        "description_en": "A cultural center keeping Salzkammergut region's rich craftsmanship tradition alive, where you can watch artisans work and purchase their creations. A living showcase of local culture with wood carving, ceramics, textiles, and traditional costumes."
    },
    "Steegwirt": {
        "description": "Hallstättersee'nin kuzey ucunda, ödüllü mutfağı ve göl manzaralı terasıyla tanınan şık restoran. Yerel malzemelerden yaratıcı Avusturya lezzetleri, özenle seçilmiş şaraplar ve profesyonel servisle, özel bir yemek deneyimi.",
        "description_en": "An elegant restaurant at the northern end of Lake Hallstättersee, known for its award-winning cuisine and lakeside terrace. A special dining experience with creative Austrian flavors from local ingredients, carefully selected wines, and professional service."
    },
    "Halleralm": {
        "description": "Geleneksel Avusturya yayla atmosferini yaşatan, ineklerin otladığı çayırlara bakan nostaljik Alp kulübesi. Taze süt, ev yapımı peynirler ve rustik Alp yemekleriyle, şehir hayatından kaçış arayanların sığınağı.",
        "description_en": "A nostalgic Alpine hut overlooking meadows where cows graze, keeping traditional Austrian highland atmosphere alive. A refuge for those seeking escape from city life with fresh milk, homemade cheeses, and rustic Alpine dishes."
    },
    "Rathlucken Hütte": {
        "description": "Ewige Wand (Sonsuz Duvar) yürüyüş rotasının başlangıç noktasında, yüzyıllık gelenekleri sürdüren dağ kulübesi. Dağcıları karşılayan sıcak atmosferi, yerel yemekleri ve muazzam manzarasıyla, unutulmaz bir mola noktası.",
        "description_en": "A mountain hut at the starting point of Ewige Wand (Eternal Wall) hiking route, continuing century-old traditions. An unforgettable stop with its warm atmosphere welcoming mountaineers, local dishes, and magnificent views."
    },
    "Vorderer Gosausee": {
        "description": "Dachstein buzulunun dramatik manzarasıyla çerçevelenen, ulaşımı kolay ve yürüyüş pistli pitoresk dağ gölü. Turistlerin ilk durağı olan bu göl, yüzme, piknik ve fotoğraf çekimi için mükemmel bir alpin cennet.",
        "description_en": "A picturesque mountain lake framed by dramatic views of Dachstein glacier, easily accessible with walking trails. The first stop for tourists, this lake is a perfect alpine paradise for swimming, picnicking, and photography."
    },
    "Hinterer Gosausee": {
        "description": "Ön gölden yaklaşık 1 saatlik yürüyüşle ulaşılan, Dachstein buzulunun ayaklarına yaklaşan daha az bilinen gizemli göl. Turkuaz suları, yaban hayatı ve dramatik dağ manzarasıyla, maceraperestlerin ödüllendirici hedefi.",
        "description_en": "A lesser-known mysterious lake reached by about 1-hour walk from the front lake, approaching the feet of Dachstein glacier. A rewarding destination for adventurers with turquoise waters, wildlife, and dramatic mountain views."
    },
    "Gosaukammbahn": {
        "description": "Gosausee'den Zwieselalm bölgesine hızla yükselen, yaz yürüyüşleri ve kış kayağı için ideal modern teleferik. Dachstein manzarası eşliğinde konforlu yolculuk, zirvedeki restoran ve cafe ile mükemmel bir dağ deneyimi.",
        "description_en": "A modern cable car quickly ascending from Gosausee to Zwieselalm area, ideal for summer hikes and winter skiing. A perfect mountain experience with comfortable journey accompanied by Dachstein views, restaurant and cafe at the summit."
    },
    "Gablonzer Hütte": {
        "description": "Teleferik istasyonunun yakınında, Dachstein buzulunun ikonik manzarasına sahip efsanevi dağ kulübesi. Avusturya Alp mutfağının en iyi örnekleri, sıcak çorba ve sıcak içeceklerle, dağcıların vazgeçilmez uğrak noktası.",
        "description_en": "A legendary mountain hut near the cable car station with iconic views of Dachstein glacier. An indispensable stop for mountaineers with the best examples of Austrian Alpine cuisine, hot soup, and warm drinks."
    },
    "Breininghütte": {
        "description": "Zwieselalm bölgesinde, Gablonzer'e alternatif daha küçük ve samimi bir dağ kulübesi. Kalabalıktan uzak, ev yapımı Kaiserschmarrn ve yerel lezzetlerle, gerçek Alp atmosferini arayanların gizli hazinesi.",
        "description_en": "A smaller and more intimate mountain hut alternative to Gablonzer in the Zwieselalm area. Away from crowds, a hidden treasure for those seeking the real Alpine atmosphere with homemade Kaiserschmarrn and local flavors."
    },
    "Sonnenalm Gosau": {
        "description": "Geniş güneşlenme terası, panoramik manzarası ve kayak pistlerine yakın konumuyla, kayakçıların ve yürüyüşçülerin favori mola noktası. Şezlonglarda uzanarak güneşin ve dağların keyfini çıkarabileceğiniz rahat bir alm.",
        "description_en": "A favorite rest point for skiers and hikers with its wide sun terrace, panoramic views, and proximity to ski slopes. A relaxed alm where you can stretch out on loungers and enjoy the sun and mountains."
    },
    "Urzeitwald Gosau": {
        "description": "Çocuklar için tasarlanmış, dinozor temalı heykeller ve eğitici panolarla dolu doğa parkuru. Orman içinde macera dolu bir yürüyüş, tarih öncesi canlılar hakkında eğlenceli bilgiler ve aile dostu atmosferiyle ideal bir aktivite.",
        "description_en": "A nature trail designed for children, filled with dinosaur-themed sculptures and educational panels. An ideal activity with adventurous walk through the forest, fun facts about prehistoric creatures, and family-friendly atmosphere."
    },
    "Adamekhütte": {
        "description": "Dachstein'ın batı buzulunun eteğinde, deneyimli dağcılar için zorlu tırmanışın ödülü olan ücra dağ kulübesi. Minimalist konforu, muhteşem buzul manzarası ve samimi dağcı topluluğuyla, gerçek Alp macerası arayanların adresi.",
        "description_en": "A remote mountain hut at the foot of Dachstein's western glacier, a reward for challenging climb for experienced mountaineers. The address for those seeking real Alpine adventure with minimalist comfort, stunning glacier views, and friendly mountaineering community."
    },
    "Gasthof Gosauschmied": {
        "description": "Gosausee yolunda, özellikle taze alabalığı ve yöresel Avusturya yemekleriyle ünlü geleneksel han ve restoran. Rustik ahşap dekorasyonu, aile işletmesi sıcaklığı ve doyurucu porsiyonlarıyla, bölgenin sevilen klasiklerinden.",
        "description_en": "A traditional inn and restaurant on the Gosausee road, especially famous for fresh trout and regional Austrian dishes. One of the region's beloved classics with rustic wooden decor, family-run warmth, and satisfying portions."
    },
    "Seecafé Frundsberg": {
        "description": "Göl kenarında, kalabalıktan uzak sakin bir konumda hizmet veren butik kafe ve restoran. Kahve, pasta ve hafif yemekler eşliğinde, sessiz bir göl manzarası keyfi arayanların sığınağı.",
        "description_en": "A boutique cafe and restaurant serving in a quiet location by the lake, away from crowds. A refuge for those seeking quiet lake scenery enjoyment accompanied by coffee, pastries, and light meals."
    },
    "Gasthof Weisses Lamm": {
        "description": "16. yüzyıldan kalma tarihi binasında hizmet veren, Hallstatt'ın en köklü ve geleneksel hanlarından biri. Klasik Avusturya yemekleri, yerel biralar ve otantik atmosferiyle, yüzyılların misafirperverliğini yaşatan mekan.",
        "description_en": "One of Hallstatt's most established and traditional inns, serving in its historic 16th-century building. A venue keeping centuries of hospitality alive with classic Austrian dishes, local beers, and authentic atmosphere."
    },
    "Gasthof Bergfried": {
        "description": "Echern vadisi girişinde, Waldbachstrub şelalesine yakın konumuyla yürüyüşçülerin favori durağı. Huzurlu bahçesi, ev yapımı Avusturya lezzetleri ve samimi servisiyle, doğa gezisine mola vermek için ideal.",
        "description_en": "A favorite stop for hikers at the entrance of Echern valley, with its location near Waldbachstrub waterfall. Ideal for taking a break from nature touring with its peaceful garden, homemade Austrian flavors, and friendly service."
    }
}

filepath = 'assets/cities/hallstatt.json'
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

print(f"\n✅ Manually enriched {count} items (Hallstatt Batch 1).")
