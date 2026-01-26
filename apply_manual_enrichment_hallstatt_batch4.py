import json

# Manual enrichment data (Hallstatt Batch 4 FINAL: 32 items)
updates = {
    "Zwieselalm": {
        "description": "Kışın muhteşem kayak pistleri, yazın çiçeklerle kaplı yürüyüş cenneti olan alpin yayla. Gosaukamm teleferik sistemiyle ulaşılan bu bölge, tüm sezondur macera ve manzara arayanların favorisi.",
        "description_en": "An alpine plateau with magnificent ski slopes in winter and hiking paradise covered with flowers in summer. This area reached by Gosaukamm cable car system is a favorite for adventure and scenery seekers in all seasons."
    },
    "Donnerkogel Klettersteig": {
        "description": "Meşhur 'Cennete Merdiven' (Sky Ladder) asma köprüsünün bulunduğu, Avusturya'nın en ikonik via ferrata rotalarından biri. Adrenalin tutkunları için 40 metre yükseklikte salınan köprü, unutulmaz bir deneyim vaat ediyor.",
        "description_en": "One of Austria's most iconic via ferrata routes featuring the famous 'Stairway to Heaven' (Sky Ladder) suspension bridge. The bridge swinging at 40 meters height promises an unforgettable experience for adrenaline enthusiasts."
    },
    "Löckernmoos": {
        "description": "Dağların tepesinde, özel bir ekosisteme sahip yüksek bataklık alanı. Nadir bitki türleri, ahşap patikalar ve doğal atmosferiyle, botanik ve ekoloji meraklıları için benzersiz bir keşif rotası.",
        "description_en": "A high moor area on top of mountains with a special ecosystem. A unique discovery route for botany and ecology enthusiasts with rare plant species, wooden paths, and natural atmosphere."
    },
    "Badestrand Obertraun": {
        "description": "Hallstättersee gölünün karşı kıyısında, yerel halkın tercih ettiği sakin ve sade halk plajı. Kalabalık Hallstatt'tan uzak, çim alanlar, sığ su girişi ve aileler için ideal ortamıyla huzurlu bir alternatif.",
        "description_en": "A calm and simple public beach on the opposite shore of Lake Hallstättersee, preferred by locals. A peaceful alternative far from crowded Hallstatt with lawn areas, shallow water entry, and ideal conditions for families."
    },
    "Heilbronner Kapelle": {
        "description": "Dachstein platosunda, trajik bir dağcılık kazasının anısına dikilen küçük anıt şapel. Sert hava koşullarına rağmen ayakta kalan bu yapı, dağcılık tarihine ve kaybedilen canlara saygı duruşu niteliğinde.",
        "description_en": "A small memorial chapel on Dachstein plateau erected in memory of a tragic mountaineering accident. This structure standing despite harsh weather conditions is a tribute to mountaineering history and lost lives."
    },
    "Rettenbachwildnis": {
        "description": "Kayalar ve nehir arasında, vahşi ve el değmemiş doğasıyla dikkat çeken korunan doğa alanı. Maceraperest yürüyüşçüler için zorlu ama ödüllendirici patikalar sunan, gerçek wilderness deneyimi arayanların adresi.",
        "description_en": "A protected natural area between rocks and river, notable for its wild and untouched nature. The address for those seeking real wilderness experience, offering challenging but rewarding trails for adventurous hikers."
    },
    "Konditorei Zauner": {
        "description": "1832'den beri hizmet veren, İmparator Franz Joseph'in de ziyaret ettiği Avusturya'nın en ünlü pastanelerinden biri. Tarihi reçetelere sadık Zaunerstollen, Sachertorte ve el yapımı çikolatalarıyla, tatlı tutkunlarının hac yeri.",
        "description_en": "One of Austria's most famous pastry shops serving since 1832, also visited by Emperor Franz Joseph. A pilgrimage site for sweet lovers with Zaunerstollen, Sachertorte, and handmade chocolates faithful to historic recipes."
    },
    "Gmundner Keramik Manufaktur": {
        "description": "Avusturya'nın meşhur yeşil çizgili (Grüngeflammte) seramiklerinin üretildiği tarihi manifaktür. 500 yıllık geleneğin devam ettiği atölyeyi ziyaret edebilir, orijinal ürünleri fabrika fiyatına satın alabilirsiniz.",
        "description_en": "A historic manufactory where Austria's famous green-striped (Grüngeflammte) ceramics are produced. You can visit the workshop where 500-year tradition continues and purchase original products at factory prices."
    },
    "Grünberg Seilbahn": {
        "description": "Gmunden şehrinden Grünberg dağının zirvesine çıkan, muhteşem Traunsee gölü manzarası sunan modern teleferik hattı. Yürüyüş rotalarına, Baumwipfelpfad'a ve panoramik restoranlara kolay erişim sağlıyor.",
        "description_en": "A modern cable car line from Gmunden city to the summit of Grünberg mountain, offering magnificent views of Lake Traunsee. Provides easy access to hiking trails, Baumwipfelpfad, and panoramic restaurants."
    },
    "Baumwipfelpfad Salzkammergut": {
        "description": "Ağaçların tepesinde yürüyüş yapabileceğiniz, 1.4 km uzunluğundaki eğitici ve panoramik ahşap platform yolu. 39 metre yükseklikteki gözetleme kulesinden Traunsee ve Alplerin 360 derece manzarası açılıyor.",
        "description_en": "A 1.4 km educational and panoramic wooden platform path where you can walk at treetop level. A 360-degree view of Traunsee and Alps opens from the 39-meter-high observation tower."
    },
    "Traunstein": {
        "description": "Traunsee gölünün ikonik koruyucusu olarak bilinen, piramit şekliyle dikkat çeken dramatik dağ. Zorlu tırmanış rotaları ve zirvedeki muhteşem manzarayla, deneyimli dağcıların gözdesi.",
        "description_en": "A dramatic mountain known as the iconic guardian of Lake Traunsee, notable for its pyramid shape. A favorite of experienced mountaineers with challenging climbing routes and magnificent summit views."
    },
    "Miesweg": {
        "description": "Traunstein dağlarının eteklerinde, göl kenarı boyunca uzanan romantik ve huzurlu yürüyüş parkuru. Turkuaz renkli göl, yükselen kayalıklar ve orman gölgeliğiyle, kolay ama çok güzel bir doğa yürüyüşü.",
        "description_en": "A romantic and peaceful walking trail at the foothills of Traunstein mountains, extending along the lakeside. An easy but beautiful nature walk with turquoise lake, rising cliffs, and forest shade."
    },
    "Toscanapark": {
        "description": "Ort kalesi yakınında, Traunsee gölü kenarında konumlanan egzotik bahçe ve park alanı. Tropikal bitkiler, palmiyeler ve Akdeniz atmosferiyle, Avusturya Alplerinde beklenmeyecek bir sürpriz.",
        "description_en": "An exotic garden and park area near Ort castle, positioned by Lake Traunsee. A surprise not expected in the Austrian Alps with tropical plants, palm trees, and Mediterranean atmosphere."
    },
    "Langbathseen": {
        "description": "Dağların arasında gizlenmiş, birbirine bağlı iki harika göl: Vorderer ve Hinterer Langbathsee. Yüzmek, yürüyüş yapmak ve doğanın sessizliğini dinlemek için mükemmel, Salzkammergut'un saklı mücevheri.",
        "description_en": "Two wonderful lakes connected to each other hidden among mountains: Vorderer and Hinterer Langbathsee. A hidden jewel of Salzkammergut, perfect for swimming, hiking, and listening to nature's silence."
    },
    "Feuerkogel Seilbahn": {
        "description": "Ebensee'den güneşli Feuerkogel platosuna hızla çıkan, kış kayağı ve yaz panoraması için ideal teleferik. Zirvedeki restoran, paragliding olanağı ve yürüyüş rotalarıyla, yıl boyu aktif bir dağ deneyimi.",
        "description_en": "A cable car quickly ascending from Ebensee to sunny Feuerkogel plateau, ideal for winter skiing and summer panoramas. An active mountain experience year-round with summit restaurant, paragliding opportunity, and hiking trails."
    },
    "Rindbach Wasserfall": {
        "description": "Ebensee yakınlarında orman içinde bulunan, kolay erişilebilir güzel şelale. Aileler ve günlük gezginler için ideal, nehir boyunca kısa ve keyifli bir yürüyüşün ödüllendirici hedefi.",
        "description_en": "A beautiful waterfall easily accessible in the forest near Ebensee. A rewarding destination of a short and pleasant walk along the river, ideal for families and day trippers."
    },
    "Offensee": {
        "description": "Tote Gebirge dağ silsilesinin eteğinde, kristal berraklığındaki suları ve dramatik dağ manzarasıyla büyüleyici göl. Yüzmek, piknik yapmak ve huzur içinde doğa fotoğrafı çekmek için ideal.",
        "description_en": "A captivating lake at the foot of Tote Gebirge mountain range with crystal-clear waters and dramatic mountain scenery. Ideal for swimming, picnicking, and taking nature photos in peace."
    },
    "KZ-Gedenkstätte Ebensee": {
        "description": "II. Dünya Savaşı döneminde burada yaşanan trajedilere tanıklık eden, Nazi toplama kampı anıt alanı ve müzesi. Tarihin karanlık sayfalarını unutmamak ve kurbanları onurlandırmak için önemli bir ziyaret noktası.",
        "description_en": "A Nazi concentration camp memorial site and museum witnessing the tragedies that occurred here during World War II. An important place to visit to not forget dark pages of history and honor the victims."
    },
    "Almsee": {
        "description": "Doğa koruma alanı içinde, kristal berraklığındaki yeşil suları ve dramatik dağ yansımalarıyla ünlü alpin göl. Çevreleyen ormanlar, şelaleler ve yaban hayatıyla, korunmuş doğanın en güzel örneklerinden.",
        "description_en": "An alpine lake within a nature reserve, famous for crystal-clear green waters and dramatic mountain reflections. One of the finest examples of preserved nature with surrounding forests, waterfalls, and wildlife."
    },
    "Cumberland Wildpark": {
        "description": "Yerel Avusturya vahşi yaşamını doğal ortamlarında gözlemleyebileceğiniz, aileler için ideal hayvan parkı. Geyikler, yaban domuzları, baykuşlar ve kurtlarla, eğitici ve eğlenceli bir doğa deneyimi.",
        "description_en": "An animal park ideal for families where you can observe local Austrian wildlife in natural habitats. An educational and entertaining nature experience with deer, wild boars, owls, and wolves."
    },
    "Laudachsee": {
        "description": "Grünberg teleferiğinden kısa bir yürüyüşle ulaşılan, sakin ve pitoresk dağ gölü. Yüzmek, güneşlenmek ve Avusturya Alplerinin huzurunu deneyimlemek için, kalabalıklardan uzak gizli bir cennet.",
        "description_en": "A calm and picturesque mountain lake reached by a short walk from Grünberg cable car. A hidden paradise away from crowds to swim, sunbathe, and experience the peace of Austrian Alps."
    },
    "Traunsee Schifffahrt": {
        "description": "Avusturya'nın en derin gölünde tarihi buharlı ve modern gemilerle yapılan panoramik göl turları. Ort kalesi, Traunkirchen ve Gmunden arasında seyrederek, gölün tüm güzelliklerini sudan keşfedin.",
        "description_en": "Panoramic lake tours on historic steamers and modern boats on Austria's deepest lake. Discover all the beauties of the lake from water sailing between Ort castle, Traunkirchen, and Gmunden."
    },
    "Kalvarienberg Bad Ischl": {
        "description": "14 duraklı çarmıh yolu istasyonları ve tepedeki şapelle ünlü, şehre hakim kutsal tepe. Hac yolu atmosferi, panoramik manzaralar ve huzurlu orman yürüyüşüyle, hem ruhani hem fiziksel bir keşif.",
        "description_en": "A sacred hill overlooking the city, famous for 14-station stations of the cross and the hilltop chapel. Both spiritual and physical discovery with pilgrimage atmosphere, panoramic views, and peaceful forest walk."
    },
    "Sophien Doppelblick": {
        "description": "İmparatoriçe Sisi'nin annesi Sophia'nın adını taşıyan, iki farklı vadiye bakış sunan panoramik manzara noktası. Kolay erişilebilir konumu ve dramatik görünümüyle, fotoğrafçıların favorisi.",
        "description_en": "A panoramic viewpoint named after Empress Sisi's mother Sophie, offering views of two different valleys. A photographer's favorite with its easily accessible location and dramatic views."
    },
    "Egelsee": {
        "description": "Ay şeklindeki ilginç formuyla bilinen, orman içinde gizlenmiş gizemli ve sakin göl. Yüzmek için soğuk ama pitoresk manzarası ve huzurlu atmosferiyle, keşfedilmeyi bekleyen bir sır.",
        "description_en": "A mysterious and quiet lake hidden in the forest, known for its interesting moon-shaped form. Cold for swimming but a secret waiting to be discovered with picturesque scenery and peaceful atmosphere."
    },
    "Sonnstein": {
        "description": "Traunsee gölünün muhteşem manzarasını sunan, zirvesine zorlu ama ödüllendirici tırmanışla ulaşılan popüler dağ. Gün doğumu ve batımı için ideal, fotoğrafçıların ve yürüyüşçülerin favorisi.",
        "description_en": "A popular mountain offering magnificent views of Lake Traunsee, reached by a challenging but rewarding climb to the summit. Ideal for sunrise and sunset, a favorite of photographers and hikers."
    },
    "Johannesbergkapelle": {
        "description": "Küçük bir tepe üzerindeki pitoresk şapel, çevre köy ve göl manzarasıyla romantik bir atmosfer yaratıyor. Kolay bir yürüyüşle ulaşılan bu nokta, sessiz bir anı paylaşmak isteyenler için ideal.",
        "description_en": "A picturesque chapel on a small hill creating a romantic atmosphere with surrounding village and lake views. This point reached by an easy walk is ideal for those wanting to share a quiet moment."
    },
    "Spitzvilla": {
        "description": "Traunsee gölü kenarında, tarihi bir art nouveau villada hizmet veren şık restoran ve kafe. Göl manzaralı terasında hafif yemekler ve içecekler keyfi, zarif bir mola deneyimi sunuyor.",
        "description_en": "A stylish restaurant and cafe serving in a historic art nouveau villa on Lake Traunsee shore. Offering an elegant break experience with light meals and drinks enjoyment on its lake-view terrace."
    },
    "Fischerkanzel": {
        "description": "Traunkirchen'deki barok kilisede bulunan, göl üzerinde balık tutan havari figürlerini betimleyen ünlü ahşap vaiz kürsüsü. Dini sanat ve detaylı zanaatkarlığın şaheseri olan tarihi eser.",
        "description_en": "A famous wooden pulpit in the baroque church in Traunkirchen depicting apostle figures fishing on the lake. A historic artifact that is a masterpiece of religious art and detailed craftsmanship."
    },
    "Stadtmuseum Bad Ischl": {
        "description": "İmparator Franz Joseph ve Sisi'nin aşkından tuz madenciliğine kadar Bad Ischl'in zengin tarihini anlatan kapsamlı yerel müze. İnteraktif sergiler, dönem kostümleri ve tarihi fotoğraflarla, geçmişe yolculuk.",
        "description_en": "A comprehensive local museum telling Bad Ischl's rich history from Emperor Franz Joseph and Sisi's love to salt mining. A journey into the past with interactive exhibitions, period costumes, and historic photos."
    },
    "EurothermenResort Bad Ischl": {
        "description": "İmparatorluk döneminden bu yana şifalı olduğuna inanılan tuzlu kaynaklarla beslenen lüks kaplıca ve wellness merkezi. Saunalar, tuz mağarası tedavileri, masaj hizmetleri ve dağ manzaralı havuzlarla tam bir rahatlama.",
        "description_en": "A luxury spa and wellness center fed by salt springs believed to be healing since the imperial era. Complete relaxation with saunas, salt cave treatments, massage services, and pools with mountain views."
    },
    "Esplanade Bad Ischl": {
        "description": "Traun nehri boyunca uzanan, imparatorluk döneminin zarif yürüyüş kültürünü yaşatan nostaljik bulvar. Sisi ve Franz Joseph'in de yürüdüğü bu tarihi yol, asırlık ağaçlar ve romantik banklarla çerçeveleniyor.",
        "description_en": "A nostalgic boulevard along the Traun River keeping the elegant walking culture of the imperial era alive. This historic path where Sisi and Franz Joseph also walked is framed by centuries-old trees and romantic benches."
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

print(f"\n✅ Manually enriched {count} items (Hallstatt Batch 4 FINAL).")
