import json

# Manual enrichment data (Kotor Batch 2: 20 items)
updates = {
    "Dalış (Diving)": {
        "description": "Kotor Körfezi'nin berrak sularında, batık gemileri, su altı mağaralarını ve zengin deniz yaşamını keşfedin. Hem yeni başlayanlar için sertifikalı dersler hem de deneyimli dalgıçlar için ileri düzey dalış noktaları sunan profesyonel dalış merkezleri mevcut.",
        "description_en": "Explore sunken ships, underwater caves, and rich marine life in the crystal-clear waters of the Bay of Kotor. Professional diving centers offering certified lessons for beginners and advanced diving sites for experienced divers are available."
    },
    "Paragliding": {
        "description": "Kotor'un çevresindeki dağlardan atlayarak, Adriyatik kıyılarının ve körfezin üzerinde yamaç paraşütüyle süzülün. Deneyimli pilotlar eşliğinde tandem uçuşlar, adrenalin tutkunlarına kuşbakışı bir Karadağ manzarası ve unutulmaz bir macera sunuyor.",
        "description_en": "Jump from the mountains surrounding Kotor and glide over the Adriatic coastline and bay by paraglider. Tandem flights with experienced pilots offer adrenaline enthusiasts a bird's-eye view of Montenegro and an unforgettable adventure."
    },
    "Bisiklet Turu": {
        "description": "Kotor Körfezi'ni çevreleyen pitoresk sahil yolunda bisikletle keşfe çıkın. Perast'tan Herceg Novi'ye uzanan rota boyunca tarihi köyler, deniz kenarı kafeleri ve nefes kesici manzaralarla dolu bir gün geçirebilirsiniz.",
        "description_en": "Set out to explore by bicycle on the picturesque coastal road surrounding the Bay of Kotor. You can spend a day full of historic villages, seaside cafes, and breathtaking views along the route from Perast to Herceg Novi."
    },
    "Jeep Safari": {
        "description": "4x4 araçlarla Karadağ'ın zorlu dağ yollarına tırmanın ve turist güzergahlarından uzak otantik köyleri keşfedin. Lovcen dağından körfez manzaraları, geleneksel yaşam ve yerel gastronomi deneyimiyle dolu bir macera günü.",
        "description_en": "Climb Montenegro's challenging mountain roads with 4x4 vehicles and discover authentic villages away from tourist routes. An adventure day full of bay views from Mount Lovćen, traditional life, and local gastronomy experiences."
    },
    "Kotor Serpantine Viewpoint": {
        "description": "Lovcen Milli Parkı'na çıkan ünlü serpantin yolunun 25 virajından birinde, Kotor şehrini ve körfezin tamamını kuşbakışı görebileceğiniz nefes kesici manzara noktası. Fotoğrafçıların favorisi olan bu nokta, özellikle gün doğumu ve batımında büyüleyici.",
        "description_en": "A breathtaking viewpoint at one of the 25 turns of the famous serpentine road ascending to Lovćen National Park, offering a bird's-eye view of Kotor city and the entire bay. A favorite of photographers, this spot is especially enchanting at sunrise and sunset."
    },
    "Krstac Viewpoint": {
        "description": "Lovcen'e çıkan yolda, Kotor Körfezi'nin muhteşem panoramasını sunan popüler durak noktası. Körfezin mavi suları, çevredeki dağlar ve aşağıdaki kasabalar tek bir karede birleşen bu manzara, Karadağ'ın en ikonik görüntülerinden birini sunuyor.",
        "description_en": "A popular stop on the road up to Lovćen, offering a magnificent panorama of the Bay of Kotor. This view where the bay's blue waters, surrounding mountains, and towns below merge in a single frame offers one of Montenegro's most iconic images."
    },
    "Dobrota Promenade": {
        "description": "Kotor'un hemen kuzeyinde, deniz kenarında uzanan sakin ve romantik sahil yürüyüş yolu. Palmiye ağaçlarıyla gölgelenen bu kaldırımda, tarihi taş evler, küçük kiliseler ve denize bakan kafelerin yanından geçerek huzurlu bir yürüyüş yapabilirsiniz.",
        "description_en": "A quiet and romantic seaside promenade extending just north of Kotor by the sea. On this sidewalk shaded by palm trees, you can take a peaceful walk passing historic stone houses, small churches, and seaside cafes."
    },
    "Square of Arms": {
        "description": "Kotor Eski Şehir'in kalbi, 17. yüzyıldan kalma Saat Kulesi ve üç cepheli Venedik Sarayı'na ev sahipliği yapan tarihi ana meydan. Kafeler, sanat galerileri ve hareketli atmosferiyle, şehri keşfetmeye başlamak için mükemmel bir merkez.",
        "description_en": "The heart of Kotor Old Town, a historic main square hosting the 17th-century Clock Tower and three-faced Venetian Palace. A perfect center to start exploring the city with its cafes, art galleries, and lively atmosphere."
    },
    "Church of St. Michael": {
        "description": "Kotor'un ortaçağ kiliselerinden biri, günümüzde şehrin taş eserler koleksiyonuna ev sahipliği yapan Lapidarium müzesi olarak işlev görüyor. Antik dönemden Venedik çağına uzanan lahitler, yazıtlar ve mimari parçalar sergileniyor.",
        "description_en": "One of Kotor's medieval churches, now functioning as the Lapidarium museum housing the city's stone artifacts collection. Sarcophagi, inscriptions, and architectural pieces from ancient to Venetian times are exhibited."
    },
    "Buca Palace": {
        "description": "Kotor'un en eski ve köklü soylu ailelerinden birine ait, gotik ve rönesans öğelerini harmanlayan tarihi saray. Cephesindeki zarif pencere süslemeleri ve balkonlarıyla, şehrin aristokratik mirasının en güzel örneklerinden biri.",
        "description_en": "A historic palace belonging to one of Kotor's oldest and most distinguished noble families, blending Gothic and Renaissance elements. One of the finest examples of the city's aristocratic heritage with its elegant window decorations and balconies on its facade."
    },
    "Sea Fortress (Kampana Kulesi)": {
        "description": "Kotor limanının girişini koruyan, şehir surlarının en stratejik noktalarından biri olan deniz kalesi. Venedik döneminde inşa edilen bu kule, bir zamanlar çan sesiyle gemi hareketlerini duyuran ve şehri denizden gelen tehlikelere karşı uyaran önemli bir savunma noktasıydı.",
        "description_en": "A sea fortress protecting the entrance to Kotor harbor, one of the most strategic points of the city walls. Built in the Venetian period, this tower was an important defense point that once announced ship movements with bell sounds and warned the city against dangers from the sea."
    },
    "Trg od Brasna": {
        "description": "Kotor Eski Şehir'in tarihi un meydanı, bir zamanlar buğday ve un ticaretinin yapıldığı canlı pazar yeri. Günümüzde küçük dükkanlar, kafeler ve hediyelik eşya satıcılarıyla, gezginlerin mola verdiği atmosferik bir köşe.",
        "description_en": "The historic flour square of Kotor Old Town, once a lively marketplace where wheat and flour were traded. Today an atmospheric corner where travelers take breaks with small shops, cafes, and souvenir sellers."
    },
    "Palazzo Bizanti": {
        "description": "16. yüzyıldan kalma, Kotor'un en etkileyici Rönesans saraylarından biri. Şimdi bir kültür merkezine dönüştürülmüş yapı, geçici sergiler, kültürel etkinlikler ve tarihi mimariyi bir arada sunuyor.",
        "description_en": "One of Kotor's most impressive Renaissance palaces from the 16th century. Now converted into a cultural center, the structure offers temporary exhibitions, cultural events, and historic architecture together."
    },
    "St. Luke's Church": {
        "description": "1195 yılında inşa edilen, Kotor'un en eski ve en iyi korunmuş kiliselerinden biri. Romanın mimarisi, iki sunağı (biri Katolik, biri Ortodoks) ve binlerce yıllık fresklerinde hâlâ görülebilen izlerle, şehrin dini çeşitliliğine tanıklık ediyor.",
        "description_en": "One of Kotor's oldest and best-preserved churches, built in 1195. With its Romanesque architecture, two altars (one Catholic, one Orthodox), and traces still visible in its millennia-old frescoes, it witnesses the city's religious diversity."
    },
    "St. Nicholas Church": {
        "description": "20. yüzyıl başında inşa edilen, Sırp Ortodoks cemaatinin ana ibadethanesi olan görkemli kilise. İç mekanındaki ikonostaz, duvar resimleri ve altın varaklı süslemeler, Ortodoks sanatının ve imanının canlı bir temsili.",
        "description_en": "A magnificent church built in the early 20th century, the main place of worship for the Serbian Orthodox community. The iconostasis, wall paintings, and gilded decorations inside are a living representation of Orthodox art and faith."
    },
    "Museo Marittimo": {
        "description": "Kotor'un zengin denizcilik tarihini anlatan, antik haritalar, gemi modelleri, silahlar ve denizci objelerinin sergilendiği kapsamlı müze. Venedik döneminden günümüze şehrin denizle olan bağını keşfetmek isteyenler için ideal bir durak.",
        "description_en": "A comprehensive museum telling Kotor's rich maritime history, exhibiting antique maps, ship models, weapons, and sailor objects. An ideal stop for those wanting to discover the city's connection with the sea from the Venetian period to the present."
    },
    "Cats of Kotor": {
        "description": "Kotor'un resmi olmayan sembolleri olan kediler, şehrin her köşesinden çıkarak ziyaretçileri karşılıyor. Eski surların, kafe teraslarının ve dar sokakların hakimleri olan bu sevimli sakinler, şehrin karakterini belirleyen özel bir detay.",
        "description_en": "Cats, the unofficial symbols of Kotor, emerge from every corner of the city to greet visitors. These adorable residents, rulers of old walls, cafe terraces, and narrow streets, are a special detail that defines the city's character."
    },
    "Cats Museum": {
        "description": "Kotor'un efsanevi kedi nüfusuna adanmış küçük, tutkulu ve benzersiz müze. Kedi temalı sanat eserleri, tarihi fotoğraflar, heykeller ve her türden kedi memorabiliası, kedi severler için eğlenceli ve keyifli bir ziyaret.",
        "description_en": "A small, passionate, and unique museum dedicated to Kotor's legendary cat population. Cat-themed artworks, historic photos, sculptures, and all kinds of cat memorabilia, a fun and enjoyable visit for cat lovers."
    },
    "Kotor City Walls": {
        "description": "4.5 kilometre uzunluğunda, 9. yüzyıldan itibaren inşa edilen ve şehri çevreleyen muhteşem savunma duvarları. 1.350 basamakla San Giovanni Kalesi'ne tırmanan parkur, zorlu ama hem manzara hem de tarihi keşif için ödüllendirici bir deneyim.",
        "description_en": "Magnificent defensive walls surrounding the city, built from the 9th century onwards, 4.5 kilometers long. The trail climbing to San Giovanni Fortress with 1,350 steps is a challenging but rewarding experience for both views and historic discovery."
    },
    "Lovcen Ulusal Parkı Girişi": {
        "description": "Kotor'dan Lovcen Milli Parkı'na açılan ana kapı, serüvenin başladığı nokta. Buradan itibaren serpantin yollar, muazzam manzaralar ve Njegos Mozolesi gibi tarihi alanlar keşfetmenizi bekliyor.",
        "description_en": "The main gate opening from Kotor to Lovćen National Park, the point where the adventure begins. From here, serpentine roads, tremendous views, and historic sites like the Njegos Mausoleum await your exploration."
    }
}

filepath = 'assets/cities/kotor.json'
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

print(f"\n✅ Manually enriched {count} items (Kotor Batch 2).")
