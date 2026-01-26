import json

# Manual enrichment data (Hallstatt Batch 3: 35 items)
updates = {
    "Gasthof Hirlatz": {
        "description": "Köy merkezinden 15 dakika yürüme mesafesindeki, sakin konumu ve geleneksel Avusturya atmosferiyle dikkat çeken aile işletmesi pansiyon. Dağ manzaralı odaları, ev yapımı kahvaltısı ve samimi servisiyle, otantik bir konaklama deneyimi.",
        "description_en": "A family-run guesthouse notable for its quiet location and traditional Austrian atmosphere, 15 minutes walk from the village center. An authentic accommodation experience with mountain-view rooms, homemade breakfast, and friendly service."
    },
    "Pension Sarstein": {
        "description": "Hallstättersee gölünün kıyısında, neredeyse her odasından eşsiz göl manzarası sunan butik pansiyon. Sabah kahvaltınızı göle bakarak yapabileceğiniz terasıyla, romantik ve huzurlu bir konaklama alternatifi.",
        "description_en": "A boutique guesthouse on the shore of Lake Hallstättersee, offering unique lake views from almost every room. A romantic and peaceful accommodation alternative with its terrace where you can have breakfast overlooking the lake."
    },
    "Keramik Hallstatt": {
        "description": "Hallstatt'a özgü geleneksel motiflerle el boyaması yapılan, benzersiz seramik hediyelik eşyalar sunan atölye ve dükkan. Zanaatkarların çalışmasını izleyebilir, kişiselleştirilmiş ürünler sipariş edebilirsiniz.",
        "description_en": "A workshop and shop offering unique ceramic souvenirs hand-painted with traditional motifs specific to Hallstatt. You can watch artisans work and order personalized products."
    },
    "Schnaps & Holz": {
        "description": "Yerel meyve likörlerinden (Schnaps) el yapımı ahşap ürünlere kadar bölgenin en otantik hediyeliklerini sunan butik dükkan. Armut, erik ve elma likörlerini tadabilir, geleneksel ahşap oyuncakları keşfedebilirsiniz.",
        "description_en": "A boutique shop offering the region's most authentic souvenirs from local fruit schnapps to handmade wooden products. You can taste pear, plum, and apple liqueurs and discover traditional wooden toys."
    },
    "Seestrasse Hallstatt": {
        "description": "Köyün ana göl kıyısı caddesi, hediyelik eşya dükkanları, kafeler ve restoranlarla dolu pitoresk yürüyüş yolu. Ahşap evlerin gölün sularına yansıdığı bu rota, Hallstatt deneyiminin kalbidir.",
        "description_en": "The village's main lakeside street, a picturesque walking path filled with souvenir shops, cafes, and restaurants. This route where wooden houses reflect on the lake waters is the heart of the Hallstatt experience."
    },
    "Dr.-Friedrich-Morton-Weg": {
        "description": "Köyün üst kısmından geçen, turistik kalabalıktan uzak panoramik yürüyüş parkuru. Gölü ve köyü yukarıdan gören manzara noktaları, eski evler ve sakin atmosferiyle, gerçek Hallstatt'ı keşfetmek isteyenlerin rotası.",
        "description_en": "A panoramic walking trail through the upper part of the village, away from tourist crowds. The route for those wanting to discover the real Hallstatt with viewpoints overlooking the lake and village, old houses, and quiet atmosphere."
    },
    "Echerntal": {
        "description": "Hallstatt'ın arkasındaki dramatik buzul vadisi, şelaleler, tarihi değirmenler ve yoğun ormanlarıyla doğa yürüyüşçülerinin favorisi. Waldbachstrub şelalesine ve Gletschergarten'e ulaşan patikalarıyla, her seviyeye uygun rotalar sunuyor.",
        "description_en": "The dramatic glacial valley behind Hallstatt, a favorite of nature hikers with waterfalls, historic mills, and dense forests. Offering routes for every level with trails reaching Waldbachstrub waterfall and Gletschergarten."
    },
    "Gletschergarten Hallstatt": {
        "description": "Binlerce yıl önce buzulların kayaları oyarak oluşturduğu benzersiz jeolojik yapılar ve dev kazanlı formasyonlar. Echerntal vadisinde bulunan bu doğal müze, buz çağını canlı olarak anlatan büyüleyici bir alan.",
        "description_en": "Unique geological formations and giant cauldron formations created by glaciers carving rocks thousands of years ago. This natural museum in Echerntal valley is a fascinating area vividly explaining the ice age."
    },
    "Wiesberghaus": {
        "description": "Dachstein platosunda, doğa eğitim merkezi olarak da hizmet veren geleneksel dağ kulübesi. Çocuklar için eğitici aktiviteler, yetişkinler için huzurlu konaklama ve herkes için muhteşem Alp manzarası sunan eşsiz bir mekan.",
        "description_en": "A traditional mountain hut on Dachstein plateau also serving as a nature education center. A unique venue offering educational activities for children, peaceful accommodation for adults, and stunning Alpine views for everyone."
    },
    "Gjaid Alm": {
        "description": "Krippenstein teleferik istasyonuna yakın, ineklerin otladığı yeşil çayırlara bakan geleneksel yayla restoranı. Taze alpin peynirleri, ev yapımı çorbalar ve klasik Avusturya yemekleriyle, dağ yürüyüşlerinin ödüllendirici molası.",
        "description_en": "A traditional highland restaurant near Krippenstein cable car station, overlooking green meadows where cows graze. A rewarding break from mountain hikes with fresh alpine cheeses, homemade soups, and classic Austrian dishes."
    },
    "Parkbad Bad Goisern": {
        "description": "Kaydırakları, geniş havuzları ve çim alanlarıyla aileler için ideal açık hava yüzme kompleksi. Çocuk havuzları, güneşlenme terasları ve kafe servisiyle, sıcak yaz günlerinde serinlemek için mükemmel.",
        "description_en": "An outdoor swimming complex ideal for families with slides, large pools, and lawn areas. Perfect for cooling off on hot summer days with children's pools, sunbathing terraces, and cafe service."
    },
    "Jutel Obertraun": {
        "description": "Spor tesislerine yakın konumuyla, özellikle genç gruplar ve sırtçantalı gezginler için ideal ekonomik konaklama. Ortak mutfak, sosyal alanlar ve Dachstein aktivitelerine kolay erişimle, bütçe dostu Alp deneyimi.",
        "description_en": "Budget-friendly accommodation ideal especially for youth groups and backpackers with its location near sports facilities. A budget-friendly Alpine experience with shared kitchen, social areas, and easy access to Dachstein activities."
    },
    "EurothermenResort Bad Ischl": {
        "description": "İmparatorluk döneminden beri kullanılan tuzlu su kaynaklarıyla beslenen, modern termal kaplıca ve wellness kompleksi. Saunalar, masaj hizmetleri, tuz mağaraları ve göl manzaralı havuzlarıyla, beden ve ruh yenilemesi için ideal.",
        "description_en": "A modern thermal spa and wellness complex fed by salt water springs used since the imperial era. Ideal for body and soul renewal with saunas, massage services, salt caves, and pools with lake views."
    },
    "Lehár Villa": {
        "description": "Ünlü Avusturyalı besteci Franz Lehár'ın son yıllarını geçirdiği ve öldüğü tarihi ev, şimdi operete adanmış müze. Orijinal mobilyalar, kişisel eşyalar ve konser piyanosuyla, müzik tarihine yolculuk.",
        "description_en": "The historic house where famous Austrian composer Franz Lehár spent his final years and died, now a museum dedicated to operetta. A journey through music history with original furniture, personal belongings, and concert piano."
    },
    "Marmorschlössl": {
        "description": "Kaiservilla parkının içinde, İmparatoriçe Sisi'nin özel yaşamına ışık tutan küçük mermer köşk müze. Sisi'nin fotoğrafları, günlük yaşam eşyaları ve zarif dönem dekorasyonuyla, imparatorluk romantizmine dalış.",
        "description_en": "A small marble pavilion museum inside Kaiservilla park shedding light on Empress Sisi's private life. A dive into imperial romanticism with Sisi's photographs, everyday objects, and elegant period decoration."
    },
    "Rettenbachklamm": {
        "description": "Vahşi suların kayaları oyduğu, tehlikeli ama nefes kesici güzellikte dar kanyon ve yürüyüş parkuru. Köprüler, basamaklar ve korkuluklarla güvenli hale getirilmiş bu rotada, doğanın gücünü yakından hissedin.",
        "description_en": "A narrow canyon and hiking trail of breathtaking beauty where wild waters carve rocks. Feel the power of nature up close on this route made safe with bridges, steps, and railings."
    },
    "Stadtmuseum Bad Ischl": {
        "description": "Bad Ischl'in tuz madenciliği geçmişinden imparatorluk dönemine uzanan zengin tarihini sergileyen kapsamlı şehir müzesi. Franz Joseph, Sisi ve yerel kültürle ilgili tarihi eserler, fotoğraflar ve interaktif sergiler.",
        "description_en": "A comprehensive city museum exhibiting Bad Ischl's rich history from salt mining past to imperial era. Historical artifacts, photographs, and interactive exhibitions about Franz Joseph, Sisi, and local culture."
    },
    "Trinkhalle Bad Ischl": {
        "description": "Eskiden zengin aristokratların şifalı tuzlu suları içtiği, şimdi kafe ve sergi alanı olarak kullanılan tarihi içmece binası. Art Nouveau mimarisi ve nostaljik atmosferiyle, imparatorluk dönemi sosyal yaşamına açılan pencere.",
        "description_en": "A historic drinking hall where wealthy aristocrats once drank healing salt waters, now used as cafe and exhibition space. A window into imperial-era social life with Art Nouveau architecture and nostalgic atmosphere."
    },
    "Esplanade Bad Ischl": {
        "description": "Traun nehri boyunca uzanan, İmparatoriçe Sisi'nin de yürüdüğü tarihi ve romantik bulvar. Asırlık ağaçlar, nostaljik banklar ve nehir manzarasıyla, imparatorluk döneminin zarif yürüyüş kültürünü yaşatan yer.",
        "description_en": "A historic and romantic boulevard along the Traun River, where Empress Sisi also walked. Keeping the elegant walking culture of the imperial era alive with centuries-old trees, nostalgic benches, and river views."
    },
    "Gasthof Moserwirt": {
        "description": "Bad Goisern meydanında, yerel halkın düzenli olarak geldiği otantik Avusturya birahanesi ve restoranı. Schnitzelden biralı sosisne geniş menüsü, canlı atmosferi ve uygun fiyatlarıyla, gerçek yerel deneyim.",
        "description_en": "An authentic Austrian beer house and restaurant in Bad Goisern square, regularly frequented by locals. A real local experience with its wide menu from schnitzel to beer sausages, lively atmosphere, and affordable prices."
    },
    "Konditorei Maislinger Bad Goisern": {
        "description": "Bad Goisern'in en sevilen pastanesi, nesiller boyu sürdürülen tariflerle yapılan geleneksel Avusturya pastaları ve tatlıları. Sachertorte, Linzertorte ve bölgeye özgü tatlılarla, tatlı bir mola garantisi.",
        "description_en": "Bad Goisern's most beloved pastry shop with traditional Austrian pastries and desserts made with recipes passed down for generations. A guaranteed sweet break with Sachertorte, Linzertorte, and regional specialties."
    },
    "Kurpark Bad Ischl": {
        "description": "Şehrin kalbinde, bakımlı çiçek tarhları, havuzlar ve anıtlarla dolu tarihi kaplıca parkı. Konser kulübesi, gül bahçesi ve gölgeli yürüyüş yollarıyla, imparatorluk döneminin zarif park kültürünü yaşatan yeşil vaha.",
        "description_en": "A historic spa park in the heart of the city filled with well-maintained flower beds, ponds, and monuments. A green oasis keeping the elegant park culture of the imperial era alive with concert pavilion, rose garden, and shaded walking paths."
    },
    "Kongress & TheaterHaus Bad Ischl": {
        "description": "Her yaz düzenlenen ünlü Lehár Festivali'ne ev sahipliği yapan, kültür ve sanat hayatının merkezi tarihi tiyatro binası. Operetler, konserler ve tiyatro gösterileriyle, canlı bir kültürel takvim sunuyor.",
        "description_en": "A historic theater building at the center of cultural and artistic life, hosting the famous Lehár Festival every summer. Offering a lively cultural calendar with operettas, concerts, and theater performances."
    },
    "Nikolauskirche Bad Ischl": {
        "description": "Ünlü besteci Anton Bruckner'in org çaldığı tarihi kilise, muhteşem barok iç mekanı ve etkileyici orguyla dikkat çekiyor. Müzik tarihi, dini sanat ve mimari güzelliğin buluştuğu atmosferik mekan.",
        "description_en": "A historic church where famous composer Anton Bruckner played the organ, notable for its magnificent baroque interior and impressive organ. An atmospheric venue where music history, religious art, and architectural beauty meet."
    },
    "Hohenzoller Wasserfall": {
        "description": "Bad Ischl yakınlarında orman içinde gizlenmiş, kolay ulaşılabilir ve huzurlu atmosferiyle ailelere uygun şirin şelale. Nehir boyunca yapılan kısa yürüyüşün ödüllendirici hedefi, piknik ve fotoğraf için ideal.",
        "description_en": "A charming waterfall hidden in the forest near Bad Ischl, easily accessible and suitable for families with its peaceful atmosphere. An ideal spot for picnic and photography, a rewarding destination of a short walk along the river."
    },
    "Nussensee": {
        "description": "Turistlerin genellikle bilmediği, yerel halkın favorisi olan sakin ve pitoresk dağ gölü. Yüzmek, kano yapmak ve doğanın sessizliğini dinlemek için ideal, Salzkammergut'un gizli cennetlerinden biri.",
        "description_en": "A quiet and picturesque mountain lake usually unknown to tourists but a favorite of locals. One of Salzkammergut's hidden paradises, ideal for swimming, canoeing, and listening to nature's silence."
    },
    "Schwarzensee": {
        "description": "Adını çevreleyen ormanların yansımasından alan koyu renkli sularıyla gizemli ve büyüleyici dağ gölü. Flushing Meadows'a karşıblık olarak sakin atmosferi, berrak suları ve ender bulunur gizliliğiyle, doğal bir sığınak.",
        "description_en": "A mysterious and enchanting mountain lake with dark-colored waters named from reflections of surrounding forests. A natural refuge with its calm atmosphere, clear waters, and rare privacy."
    },
    "Wallfahrtskirche St. Wolfgang": {
        "description": "Michael Pacher'in 15. yüzyıldan kalma ünlü kanatlı sunağına ev sahipliği yapan, Avusturya Gotik sanatının en önemli örneklerinden hac kilisesi. Altın varaklı muazzam sunak ve tarihi atmosferiyle, sanat ve inanç meraklılarının durağı.",
        "description_en": "A pilgrimage church housing Michael Pacher's famous winged altar from the 15th century, one of the most important examples of Austrian Gothic art. A stop for art and faith enthusiasts with its magnificent gilded altar and historic atmosphere."
    },
    "Weisses Rössl": {
        "description": "Ünlü 'Im Weissen Rössl' operetine konu olmuş, Wolfgangsee gölü kenarında tarihi romantik otel ve restoran. Nostaljik dekorasyonu, göl manzaralı terasları ve zengin tarihiyle, Avusturya kültürünün ikonik simgelerinden.",
        "description_en": "A historic romantic hotel and restaurant on Lake Wolfgangsee, subject of the famous 'Im Weissen Rössl' operetta. One of the iconic symbols of Austrian culture with nostalgic decor, lake-view terraces, and rich history."
    },
    "Dorfplatz St. Wolfgang": {
        "description": "Geleneksel Avusturya mimarisinin en güzel örnekleriyle çevrili, St. Wolfgang'ın kalbi olan pitoresk köy meydanı. Kafeler, hediyelik eşya dükkanları ve tarihi binalarla, kasaba yaşamının canlı merkezi.",
        "description_en": "A picturesque village square at the heart of St. Wolfgang, surrounded by the finest examples of traditional Austrian architecture. The lively center of town life with cafes, souvenir shops, and historic buildings."
    },
    "Puppenmuseum St. Wolfgang": {
        "description": "19. ve 20. yüzyıllardan kalma yüzlerce tarihi bebeğin, oyuncağın ve minyatürün sergilendiği nostaljik müze. Koleksiyonun zenginliği ve sunumuyla, çocukluk anılarına yolculuk arayanların keyif alacağı yer.",
        "description_en": "A nostalgic museum exhibiting hundreds of historical dolls, toys, and miniatures from the 19th and 20th centuries. A place those seeking a journey into childhood memories will enjoy with the richness and presentation of the collection."
    },
    "Abarena": {
        "description": "Çocuklar için her türlü kapalı aktivitenin bulunduğu modern eğlence merkezi: tırmanma duvarları, trambolin parkı, kaydıraklar ve oyun alanları. Yağmurlu günlerde aileler için mükemmel bir alternatif.",
        "description_en": "A modern entertainment center with all kinds of indoor activities for children: climbing walls, trampoline park, slides, and play areas. A perfect alternative for families on rainy days."
    },
    "Falkensteinwand": {
        "description": "Wolfgangsee gölünün dik kayalık yamacında, efsanelere konu olmuş romantik şapel ve manzara noktası. Ziyaret için tırmanış gerektiren bu gizemli yer, göl manzarası ve mistik atmosferiyle büyüleyici.",
        "description_en": "A romantic chapel and viewpoint on the steep rocky slope of Lake Wolfgangsee, subject of legends. This mysterious place requiring a climb to visit is enchanting with lake views and mystical atmosphere."
    },
    "Dorfalm St. Wolfgang": {
        "description": "Canlı müzik geceleri, geleneksel Avusturya lezzetleri ve samimi köy atmosferiyle dikkat çeken popüler restoran ve bar. Yerel halk ve turistlerin kaynaştığı, après-ski tarzı eğlence merkezi.",
        "description_en": "A popular restaurant and bar notable for live music nights, traditional Austrian flavors, and friendly village atmosphere. An après-ski style entertainment center where locals and tourists mingle."
    },
    "Kaffeewerkstatt St. Wolfgang": {
        "description": "Kendi kavurdukları özel kahveleri sunan, vintage dekorasyonlu üçüncü dalga kahve dükkanı. El yapımı pastaları, latte art sunumları ve kahve tutkunlarına özel tarifle rile, modern bir kahve deneyimi.",
        "description_en": "A third-wave coffee shop with vintage decor serving specialty coffees roasted on-site. A modern coffee experience with homemade pastries, latte art presentations, and special recipes for coffee enthusiasts."
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

print(f"\n✅ Manually enriched {count} items (Hallstatt Batch 3).")
