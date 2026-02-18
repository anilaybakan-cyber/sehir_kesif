import json

# Manual enrichment data (Hallstatt Batch 2: 35 items)
updates = {
    "Strandbad St. Wolfgang": {
        "description": "Wolfgangsee'nin berrak turkuaz sularında yüzme, güneşlenme ve su sporları için ideal halk plajı. Çim alanlar, tramplen, çocuk havuzu ve sahil kafesiyle, aile dostu bir yaz günü geçirmek için mükemmel.",
        "description_en": "An ideal public beach for swimming, sunbathing, and water sports in the crystal-clear turquoise waters of Wolfgangsee. Perfect for spending a family-friendly summer day with lawn areas, diving board, children's pool, and beach cafe."
    },
    "Europakloster Gut Aich": {
        "description": "Şifalı bitkiler, otlar ve likörlerle ünlü Benediktin manastırı. Manastır bahçesinde yetiştirilen otlardan üretilen doğal ürünleri satın alabilir, huzurlu atmosferde ruhani bir mola verebilirsiniz.",
        "description_en": "A Benedictine monastery famous for healing herbs, plants, and liqueurs. You can purchase natural products made from herbs grown in the monastery garden and take a spiritual break in the peaceful atmosphere."
    },
    "Cafe Nannerl": {
        "description": "Mozart'ın kız kardeşi Nannerl'in adını taşıyan, St. Wolfgang'ın tarihi meydanında yer alan nostaljik kafe. Ev yapımı Avusturya pastaları, Mozartkugel ve zengin kahve çeşitleriyle, kültürel bir mola deneyimi.",
        "description_en": "A nostalgic cafe named after Mozart's sister Nannerl, located in St. Wolfgang's historic square. A cultural break experience with homemade Austrian pastries, Mozartkugel, and rich coffee varieties."
    },
    "Sausteigalm": {
        "description": "Zwölferhorn dağına giden yol üzerinde, muhteşem göl ve Alp manzarasına karşı yemek yiyebileceğiniz geleneksel yayla kulübesi. Taze peynir, ev yapımı çorba ve rustik Alp atmosferiyle, yürüyüşçülerin ödüllendirici molası.",
        "description_en": "A traditional highland hut on the way to Zwölferhorn mountain where you can dine against magnificent lake and Alpine views. A rewarding break for hikers with fresh cheese, homemade soup, and rustic Alpine atmosphere."
    },
    "Altaussee Lake": {
        "description": "James Bond Spectre filminin çekildiği, kristal berraklığındaki suları ve dramatik dağ manzarasıyla efsanevi göl. II. Dünya Savaşı sırasında Nazi'lerin sanat eserlerini sakladığı tuz madenlerine yakınlığıyla tarih meraklılarını da cezbediyor.",
        "description_en": "A legendary lake where the James Bond Spectre movie was filmed, with crystal-clear waters and dramatic mountain scenery. Also attracts history enthusiasts with its proximity to salt mines where Nazis hid artworks during World War II."
    },
    "Loser Panoramastraße": {
        "description": "Arabayla 1.600 metreye kadar çıkabileceğiniz, her virajda nefes kesici manzaralar sunan panoramik dağ yolu. Zirvedeki restoran, yürüyüş parkurları ve paragliding olanağıyla, hem sürüş hem macera tutkunları için ideal.",
        "description_en": "A panoramic mountain road where you can drive up to 1,600 meters, offering breathtaking views at every turn. Ideal for both driving and adventure enthusiasts with a summit restaurant, hiking trails, and paragliding opportunities."
    },
    "Toplitzsee": {
        "description": "Nazi altınlarının ve II. Dünya Savaşı belgelerinin sularında saklandığı efsanesiyle ünlü, gizemli ve koyu renkli orman gölü. Tekne turuyla ulaşılan bu izole göl, hem tarih meraklıları hem doğa severler için büyüleyici.",
        "description_en": "A mysterious and dark forest lake famous for legends of Nazi gold and World War II documents hidden in its waters. This isolated lake accessible by boat tour is fascinating for both history buffs and nature lovers."
    },
    "Grundlsee": {
        "description": "Steiermark eyaletinin en büyük gölü, yüzmek, kürek çekmek ve tekne gezisi için ideal berrak sularıyla biliniyor. Çevre dağlar, sahil restoranları ve huzurlu atmosferiyle, Salzkammergut'un gizli cennetlerinden biri.",
        "description_en": "The largest lake in Styria, known for its crystal-clear waters ideal for swimming, rowing, and boat trips. One of Salzkammergut's hidden paradises with surrounding mountains, lakeside restaurants, and peaceful atmosphere."
    },
    "3-Seen-Tour": {
        "description": "Grundlsee, Toplitzsee ve gizli Kammersee'yi birbirine bağlayan, tekne ve yürüyüş kombinasyonuyla yapılan unutulmaz günlük tur. Her göl farklı bir karakter sunar, son göl ise sadece doğa yürüyüşüyle ulaşılabilen gizemli bir cennet.",
        "description_en": "An unforgettable day tour connecting Grundlsee, Toplitzsee, and hidden Kammersee by combination of boat and hiking. Each lake offers a different character, and the last lake is a mysterious paradise accessible only by nature walk."
    },
    "Narzissenbad Aussee": {
        "description": "Tuzlu su mağarası tedavileri, wellness uygulamaları ve muazzam dağ manzaralı havuzlarıyla ünlü modern kaplıca kompleksi. Solunum yolları rahatsızlıkları için önerilen tuz terapi oturumları, bölgenin en benzersiz deneyimlerinden.",
        "description_en": "A modern spa complex famous for salt water cave treatments, wellness applications, and pools with tremendous mountain views. Salt therapy sessions recommended for respiratory conditions are among the region's most unique experiences."
    },
    "Kammerhofmuseum Bad Aussee": {
        "description": "Salzkammergut bölgesinin tarihini, geleneksel kıyafetlerini (Tracht) ve tuz madenciliği geçmişini sergileyen kapsamlı yerel müze. İnteraktif sergiler, tarihi fotoğraflar ve yerel zanaat örnekleriyle, bölge kültürüne derinlemesine dalış.",
        "description_en": "A comprehensive local museum exhibiting Salzkammergut region's history, traditional costumes (Tracht), and salt mining past. A deep dive into regional culture with interactive exhibitions, historic photos, and local craft examples."
    },
    "Blaa Alm": {
        "description": "İlkbaharda binlerce sarı nergis çiçeğiyle kaplanan, Avusturya'nın en güzel çayırlarından biri olan alpin yayla. Fotoğrafçıların favorisi olan bu doğal gösterilerin yanı sıra, geleneksel Alp kulübesi yemekleri sunan huzurlu bir mola noktası.",
        "description_en": "An alpine plateau covered with thousands of yellow daffodils in spring, one of Austria's most beautiful meadows. A peaceful rest point offering traditional Alpine hut meals alongside this natural spectacle that is a photographer's favorite."
    },
    "Loserhütte": {
        "description": "Loser panoramik yolunun sonunda, 360 derece dağ manzarası sunan teraslı dağ restoranı. Taze Alp yemekleri, soğuk biralar ve nefes kesici görünümle, uzun bir sürüşün veya yürüyüşün ödüllendirici finali.",
        "description_en": "A terraced mountain restaurant at the end of Loser panoramic road, offering 360-degree mountain views. A rewarding finale to a long drive or hike with fresh Alpine dishes, cold beers, and breathtaking views."
    },
    "Fischerhütte Toplitzsee": {
        "description": "Toplitzsee'den taze tutulan balıkların odun ateşinde pişirildiği, gölün kenarında samimi balıkçı kulübesi. Dumanın, doğanın ve tarih kokusunun karıştığı bu benzersiz mekanda, en otantik Avusturya deneyimlerinden biri.",
        "description_en": "An intimate fisherman's hut by the lake where fresh-caught fish from Toplitzsee are cooked over wood fire. One of the most authentic Austrian experiences in this unique place where smoke, nature, and the scent of history blend."
    },
    "Seewiese Altaussee": {
        "description": "Altaussee gölünün kuzey ucunda, gölün durgun sularına yansıyan dağ manzarasını izleyebileceğiniz huzurlu çayırlık piknik alanı. Yüzmek, güneşlenmek ve doğanın sessizliğini dinlemek için mükemmel bir kaçış noktası.",
        "description_en": "A peaceful meadow picnic area at the northern end of Lake Altaussee where you can watch mountain views reflected in the lake's calm waters. A perfect escape point for swimming, sunbathing, and listening to nature's silence."
    },
    "Literaturmuseum Altaussee": {
        "description": "19. ve 20. yüzyıllarda Altaussee'de yaşayan birçok ünlü Avusturyalı yazarın anısına kurulmuş edebiyat müzesi. El yazmaları, mektuplar, fotoğraflar ve kişisel eşyalarla, bölgenin edebi mirasına ışık tutuyor.",
        "description_en": "A literature museum established in memory of many famous Austrian writers who lived in Altaussee in the 19th and 20th centuries. Sheds light on the region's literary heritage with manuscripts, letters, photos, and personal belongings."
    },
    "Kurpark Bad Aussee": {
        "description": "Avusturya'nın coğrafi merkezi sayılan noktanın bulunduğu, tarihi kaplıca parkı ve yeşil alan. Botanik bahçeleri, yürüyüş yolları ve tarihi anıtlarıyla, şehir gezisine huzurlu bir mola vermek için ideal.",
        "description_en": "A historic spa park and green area containing the point considered the geographical center of Austria. Ideal for taking a peaceful break from city touring with botanical gardens, walking paths, and historic monuments."
    },
    "Mercedes-Brücke": {
        "description": "Mercedes-Benz yıldız logosunu andıran benzersiz Y şeklindeki ilginç ahşap yaya köprüsü. Bad Aussee ve Altaussee arasındaki yürüyüş rotasında, fotoğraf çekimi için popüler ve mimari olarak dikkat çekici bir durak.",
        "description_en": "A unique Y-shaped interesting wooden pedestrian bridge resembling the Mercedes-Benz star logo. An architecturally striking and popular photography stop on the walking route between Bad Aussee and Altaussee."
    },
    "Vitalhotel Wasnerin": {
        "description": "Yoga, meditasyon ve wellness odaklı, doğa içinde lüks konaklama sunan butik sağlık oteli. Organik mutfak, spa hizmetleri ve dağ manzaralı odalarıyla, zihin ve beden yenilemesi arayanların adresi.",
        "description_en": "A boutique health hotel offering luxury accommodation in nature focused on yoga, meditation, and wellness. The address for those seeking mind and body renewal with organic cuisine, spa services, and rooms with mountain views."
    },
    "Villa Seilern": {
        "description": "19. yüzyıldan kalma tarihi bir villada hizmet veren, göl manzaralı şık butik otel. Avusturya aristokrasisinin izlerini taşıyan zarif dekorasyonu, mükemmel mutfağı ve huzurlu bahçesiyle romantik bir konaklama deneyimi.",
        "description_en": "A stylish boutique hotel with lake views, serving in a 19th-century historic villa. A romantic accommodation experience with elegant decor bearing traces of Austrian aristocracy, excellent cuisine, and peaceful garden."
    },
    "Bad Aussee Center": {
        "description": "Salzkammergut'un geleneksel 'Tracht' (Avusturya halk kıyafetleri) modasının başkenti sayılan kasabanın tarihi merkezi. Butikler, Dirndl ve Lederhosen dükkanları, kafeler ve yerel zanaatkarlarla dolu canlı meydan.",
        "description_en": "The historic center of the town considered the capital of traditional 'Tracht' (Austrian folk costumes) fashion in Salzkammergut. A lively square filled with boutiques, Dirndl and Lederhosen shops, cafes, and local artisans."
    },
    "Pötschenpass": {
        "description": "Salzkammergut bölgesine giriş kapısı niteliğindeki, muhteşem manzaralar sunan tarihi dağ geçidi. Her virajda yeni bir panorama açılan bu yolculuk, sürüş keyfi ve fotoğraf duraklarıyla dolu.",
        "description_en": "A historic mountain pass serving as the gateway to the Salzkammergut region, offering magnificent views. A journey with new panoramas unfolding at every turn, full of driving pleasure and photography stops."
    },
    "Rossmoosalm": {
        "description": "Turistik güzergahlardan uzak, sessiz ve sakin bir atmosferde hizmet veren otantik yayla kulübesi. Yerel çiftçilerin ürettiği taze peynir, süt ürünleri ve geleneksel yemeklerle, gerçek Alp yaşamını deneyimleyin.",
        "description_en": "An authentic plateau hut serving in a quiet and peaceful atmosphere away from tourist routes. Experience real Alpine life with fresh cheese, dairy products, and traditional dishes produced by local farmers."
    },
    "Hütteneckalm": {
        "description": "Dachstein buzulunun muhteşem manzarasına karşı yemek yiyebileceğiniz, geleneksel Avusturya Alp kulübesi. Sıcak çorba, Kaiserschmarrn ve bölgenin en iyi peynir tabakları ile dağcıların favori uğrak noktası.",
        "description_en": "A traditional Austrian Alpine hut where you can dine against magnificent views of Dachstein glacier. A favorite stop for mountaineers with hot soup, Kaiserschmarrn, and the region's best cheese platters."
    },
    "Lambacher Hütte": {
        "description": "Sandling dağında, kendi halinde işleyen küçük ve samimi dağ kulübesi. Aile işletmesi sıcaklığı, ev yapımı yemekler ve kalabalıktan uzak atmosferiyle, gerçek dağcılık deneyimi arayanların sığınağı.",
        "description_en": "A small and intimate mountain hut operating independently on Sandling mountain. A refuge for those seeking real mountaineering experience with family-run warmth, homemade dishes, and atmosphere away from crowds."
    },
    "Sandling": {
        "description": "Altaussee'nin ikonik tuz madenlerinin bulunduğu, tarihi ve doğal güzellikleriyle öne çıkan dağ. Zirveye çıkan yürüyüş rotaları, panoramik manzaralar ve yeraltı dünyasıyla, macera ve tarih tutkunlarının adresi.",
        "description_en": "A mountain where Altaussee's iconic salt mines are located, standing out with its historical and natural beauties. The address for adventure and history enthusiasts with hiking trails to the summit, panoramic views, and underground world."
    },
    "Zwerchwand": {
        "description": "Kaya tırmanışçıları ve deneyimli dağcılar için zorlu rotalar sunan, dramatik kaya duvarlarıyla ünlü dik yamaç. Spor tırmanışçılığı için popüler alan, eşsiz Salzkammergut manzarasıyla ödüllendiriyor.",
        "description_en": "A steep slope famous for dramatic rock walls offering challenging routes for rock climbers and experienced mountaineers. A popular area for sport climbing, rewarding with unique Salzkammergut views."
    },
    "Ruine Wildenstein": {
        "description": "Ormanın içinde gizlenmiş, ortaçağ atmosferini yaşatan eski kale kalıntıları. Tarihi duvarlar, yıkık kuleler ve gizemli atmosferiyle, macera ve tarih meraklıları için romantik bir keşif noktası.",
        "description_en": "Old castle ruins hidden in the forest, keeping medieval atmosphere alive. A romantic discovery point for adventure and history enthusiasts with historic walls, ruined towers, and mysterious atmosphere."
    },
    "Jainzenberg": {
        "description": "Bad Ischl'in güneşli yamacında, ailelere uygun kolay yürüyüş rotaları ve panoramik manzara noktaları sunan popüler dağ. Çayırlıklar, orman patikları ve geleneksel alm restoranlartıyla, günlük kaçamak için ideal.",
        "description_en": "A popular mountain on Bad Ischl's sunny slope, offering family-friendly easy hiking trails and panoramic viewpoints. Ideal for a day getaway with meadows, forest paths, and traditional alm restaurants."
    },
    "Sisis Park": {
        "description": "İmparatoriçe Sisi'ye adanmış, çocuklar için oyun alanları, yürüyüş yolları ve piknik noktaları bulunan modern park. Aileler için keyifli, tarihi bağlamıyla eğitici, doğa içinde huzurlu bir gün için mükemmel.",
        "description_en": "A modern park dedicated to Empress Sisi with playgrounds for children, walking paths, and picnic spots. Perfect for a pleasant day for families, educational with historical context, and peaceful in nature."
    },
    "Ochsenkreuz": {
        "description": "Hallstättersee gölünün ortasındaki küçük adacık üzerinde yükselen tarihi haç. Efsaneye göre bir öküzün boğulduğu yere dikilen bu anıt, tekne turlarında görülebilen romantik ve gizemli bir simge.",
        "description_en": "A historic cross rising on a small island in the middle of Lake Hallstättersee. According to legend, this monument erected where an ox drowned is a romantic and mysterious symbol visible during boat tours."
    },
    "Basilika St. Michael Mondsee": {
        "description": "Sound of Music filmindeki ikonik düğün sahnesinin çekildiği, 15. yüzyıldan kalma barok bazilika. Muhteşem süslemeli iç mekanı, altın varaklı sunakları ve müzikallere ilham veren tarihiyle, film fanlarının hac yeri.",
        "description_en": "A baroque basilica from the 15th century where the iconic wedding scene from the Sound of Music film was shot. A pilgrimage site for film fans with its magnificently decorated interior, gilded altars, and history inspiring musicals."
    },
    "Schloss Fuschl": {
        "description": "Fuschlsee gölünün kıyısında, masalsı bir yarımadada konumlanan lüks kale-otel. 15. yüzyıldan kalma tarihi yapı, spa, golf sahası ve göl manzaralı restoranlartıyla, Avusturya'nın en prestijli konaklama adreslerinden.",
        "description_en": "A luxury castle-hotel located on a fairytale peninsula on the shore of Fuschlsee lake. One of Austria's most prestigious accommodation addresses with a 15th-century historic building, spa, golf course, and lake-view restaurants."
    },
    "Fuschlsee Bad": {
        "description": "Turkuaz renkli berrak sularıyla ünlü Fuschlsee gölünde yüzmek, güneşlenmek ve su sporları yapmak için modern plaj tesisi. Çim alanlar, şezlonglar, kafe ve yüzen platformlarla, kaliteli bir göl günü deneyimi.",
        "description_en": "A modern beach facility for swimming, sunbathing, and water sports in Lake Fuschlsee, famous for its turquoise clear waters. A quality lake day experience with lawn areas, sunbeds, cafe, and floating platforms."
    },
    "Red Bull Headquarters": {
        "description": "Ünlü enerji içeceği markasının Fuschl'daki fütüristik tasarımlı uluslararası genel merkezi. Devasa boğa heykelleri, modern mimari ve göl manzarasıyla, marka hayranları ve mimari meraklıları için dikkat çekici bir durak.",
        "description_en": "The futuristically designed international headquarters of the famous energy drink brand in Fuschl. An eye-catching stop for brand fans and architecture enthusiasts with giant bull statues, modern architecture, and lake views."
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

print(f"\n✅ Manually enriched {count} items (Hallstatt Batch 2).")
