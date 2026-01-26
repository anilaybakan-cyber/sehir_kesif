import json

# Manual enrichment data (Brugge Batch 2: 45 items)
updates = {
    "Sanseveria Bagelsalon": {
        "description": "Vintage dekorasyonu, ev yapımı bagelleri ve sıcak atmosferiyle dikkat çeken butik kahvaltı mekanı. Brunch severler için gizli bir hazine, Amerikan tarzı bageller ve güçlü kahvelerle enerjik bir güne başlangıç.",
        "description_en": "A boutique breakfast venue notable for vintage decor, homemade bagels, and warm atmosphere. A hidden treasure for brunch lovers, starting an energetic day with American-style bagels and strong coffees."
    },
    "Li O Lait": {
        "description": "Ressamlar sokağında konumlanan, güzel kahve ve ev yapımı keklerle ünlü samimi kafe. Sakin atmosferi, vintage mobilyaları ve kaliteli içecekleriyle, turistik kalabalıktan kaçış arayanların gizli durağı.",
        "description_en": "An intimate cafe located on painters' street, famous for great coffee and homemade cakes. A hidden stop for those seeking escape from tourist crowds with calm atmosphere, vintage furniture, and quality drinks."
    },
    "Blackbird": {
        "description": "Jan van Eyck meydanında, şık sunumları ve modern Belçika mutfağıyla öne çıkan trendy kafe-restoran. Brunch menüsü, sağlıklı seçenekler ve Instagram'a yakışır tabak sunumlarıyla genç kitlenin favorisi.",
        "description_en": "A trendy cafe-restaurant in Jan van Eyck square, standing out with stylish presentations and modern Belgian cuisine. A favorite of young crowds with brunch menu, healthy options, and Instagram-worthy dish presentations."
    },
    "St. James's Church": {
        "description": "Zengin sanat koleksiyonu ve bağışçı ailelerinin anıtsal mezarlarıyla dikkat çeken tarihi kilise. Gotik mimarisi, Flaman resim şaheserleri ve yakındaki sanat galerisiyle, sanat tarihi tutkunlarının durağı.",
        "description_en": "A historic church notable for its rich art collection and monumental tombs of donor families. A stop for art history enthusiasts with Gothic architecture, Flemish painting masterpieces, and nearby art gallery."
    },
    "Guild of Archers St. Sebastian": {
        "description": "600 yılı aşkın süredir faaliyet gösteren, hala aktif okçuluk loncası ve müzesi. Tarihi silahlar, madalyalar ve geleneksel kıyafetlerle, Brugge'ün ortaçağ lonca kültürünü yaşatan benzersiz mekan.",
        "description_en": "An active archery guild and museum operating for over 600 years. A unique venue keeping Bruges' medieval guild culture alive with historic weapons, medals, and traditional costumes."
    },
    "Sashuis": {
        "description": "Minnewater (Aşk Gölü) üzerindeki su seviyesini düzenleyen, 16. yüzyıldan kalma tarihi savak evi. Gotik mimarisi ve romantik konumuyla, Brugge'ün hidrolojik mühendislik tarihine tanıklık eden yapı.",
        "description_en": "A 16th-century historic lock house regulating water levels on Minnewater (Lake of Love). A structure witnessing Bruges' hydraulic engineering history with Gothic architecture and romantic location."
    },
    "Hof De Jonghe": {
        "description": "İçinde koyunların otladığı, turistlerden uzak saklı bir bahçe ve tarihi avlu. Şehrin en az bilinen köşelerinden biri olarak, ortaçağ Brugge'ünün kırsal yaşamını hissettiren huzurlu bir kaçış.",
        "description_en": "A hidden garden and historic courtyard where sheep graze, away from tourists. A peaceful escape as one of the city's least known corners, feeling the rural life of medieval Bruges."
    },
    "Gouden Handrei": {
        "description": "Brugge'ün en sessiz ve huzurlu kanallarından biri, altın el anlamına gelen adıyla tarihi ticaret rotası. Söğüt ağaçları, taş köprüler ve tarihi evlerle çevrili romantik yürüyüş güzergahı.",
        "description_en": "One of Bruges' quietest and most peaceful canals, a historic trade route with its name meaning golden hand. A romantic walking route surrounded by willow trees, stone bridges, and historic houses."
    },
    "Augustijnenrei": {
        "description": "Augustinian köprüsünün altından geçen, yeşillikler ve tarihi binalarla çevrili pitoresk kanal. Şehrin daha az bilinen güzel köşelerinden biri, fotoğraf meraklıları için gizli bir mücevher.",
        "description_en": "A picturesque canal passing under Augustinian bridge, surrounded by greenery and historic buildings. One of the city's lesser-known beautiful corners, a hidden gem for photography enthusiasts."
    },
    "Speelmansrei": {
        "description": "Şehrin kuzeybatısında, yeşillikler içinde sakin bir kanal manzarası sunan romantik köşe. Müzisyenler kanalı anlamına gelen adıyla, ortaçağda gezici müzisyenlerin yaşadığı bölge.",
        "description_en": "A romantic corner in the city's northwest offering a calm canal view among greenery. With its name meaning musicians' canal, the area where traveling musicians lived in medieval times."
    },
    "'t Apostelientje": {
        "description": "Gerçek el yapımı ve antika Brugge dantelleri satan otantik dükkan. Makinede üretilen Çin mallarından farklı, nesiller boyu sürdürülen geleneksel zanaatın canlı temsilcisi.",
        "description_en": "An authentic shop selling genuine handmade and antique Bruges lace. A living representative of traditional craftsmanship continued for generations, different from machine-made Chinese products."
    },
    "Rococo Lace": {
        "description": "Çin malı olmayan, kaliteli Belçika danteli ve geleneksel el işlerini sunan güvenilir butik. Dantel tarihini öğrenmek ve orijinal hediyelik almak isteyenler için ideal adres.",
        "description_en": "A trustworthy boutique offering quality Belgian lace and traditional handicrafts that are not Chinese-made. An ideal address for those wanting to learn lace history and buy original souvenirs."
    },
    "Bauhaus": {
        "description": "Sırtçantalı gezginlerin buluşma noktası, canlı barı ve sosyal atmosferiyle popüler hostel. Bütçe dostu fiyatları, parti havası ve merkezi konumuyla genç turistlerin favorisi.",
        "description_en": "A meeting point for backpackers, a popular hostel with lively bar and social atmosphere. A favorite of young tourists with budget-friendly prices, party vibe, and central location."
    },
    "Snuffel Hostel Bar": {
        "description": "Sık sık canlı müzik etkinliklerine ev sahipliği yapan, samimi ve rahat hostel barı. Yerel ve uluslararası gezginlerin kaynaştığı, bütçe dostu içkiler ve dostane atmosfer.",
        "description_en": "An intimate and comfortable hostel bar frequently hosting live music events. A budget-friendly drink and friendly atmosphere where local and international travelers mingle."
    },
    "Charlie Rockets": {
        "description": "Eski bir sinemadan dönüştürülmüş, büyük ekranda filmler izlenebilen hostel ve bar. Retro atmosferi, canlı müzik geceleri ve sosyal etkinlikleriyle, alternatif bir konaklama deneyimi.",
        "description_en": "A hostel and bar converted from an old cinema where you can watch movies on the big screen. An alternative accommodation experience with retro atmosphere, live music nights, and social events."
    },
    "Gran Kaffe De Passage": {
        "description": "Art Deco tarzı zarif bir pasajın içinde konumlanan, nostaljik dekorasyonuyla büyüleyici kafe. Vintage ortamı, lezzetli pastaları ve klasik Avrupa kafe atmosferiyle, zamanda yolculuk deneyimi.",
        "description_en": "An enchanting cafe located inside an elegant Art Deco-style passage with nostalgic decor. A time travel experience with vintage setting, delicious pastries, and classic European cafe atmosphere."
    },
    "De Stoepa": {
        "description": "Minnewater (Aşk Gölü) yakınında, güzel bahçe terasıyla dikkat çeken vejetaryen ve vegan dostu kafe. Sağlıklı yemekler, organik içecekler ve huzurlu atmosferiyle, alternatif yaşam tarzı arayanların durağı.",
        "description_en": "A vegetarian and vegan-friendly cafe near Minnewater (Lake of Love), notable for its beautiful garden terrace. A stop for those seeking alternative lifestyles with healthy food, organic drinks, and peaceful atmosphere."
    },
    "Joey's Cafe": {
        "description": "Blues ve rock müzik çalan, harika kokteylleri ve samimi ortamıyla öne çıkan gece barı. Canlı müzik performansları, yerel sanatçılar ve otantik bar atmosferiyle, müzik severler için gizli cennet.",
        "description_en": "A night bar playing blues and rock music, standing out with great cocktails and friendly atmosphere. A hidden paradise for music lovers with live music performances, local artists, and authentic bar atmosphere."
    },
    "De Windmolen": {
        "description": "Yel değirmenlerinin hemen karşısında, muhteşem gün batımı manzarasıyla bilinen geleneksel bira bahçesi. Belçika biraları, hafif atıştırmalıklar ve panoramik görünümle, şehrin en romantik mola noktalarından.",
        "description_en": "A traditional beer garden right across from the windmills, known for magnificent sunset views. One of the city's most romantic rest stops with Belgian beers, light snacks, and panoramic views."
    },
    "Estaminet": {
        "description": "Koningin Astridpark'a bakan, makarna ve hafif yemekleriyle ünlü rahat bistro. Parkın yeşilliklerine karşı yemek yiyebileceğiniz terasıyla, yerel halkın favori öğle yemeği durağı.",
        "description_en": "A comfortable bistro overlooking Koningin Astridpark, famous for pasta and light meals. A favorite lunch stop for locals with its terrace where you can dine facing the park's greenery."
    },
    "De Republiek": {
        "description": "Kültür merkezi bünyesinde, geniş iç mekanı ve çeşitli etkinlikleriyle dikkat çeken çok amaçlı mekan. Konserler, sergiler, kahve ve yemek bir arada, şehrin alternatif kültür merkezi.",
        "description_en": "A multi-purpose venue within a cultural center, notable for spacious interior and various events. The city's alternative cultural center with concerts, exhibitions, coffee, and food together."
    },
    "Books & Brunch": {
        "description": "Kitaplarla çevrili, sakin ve sağlıklı kahvaltı seçenekleri sunan kütüphane-kafe konsepti. Okuma tutkunları ve brunch severler için mükemmel, huzurlu ve entelektüel bir atmosfer.",
        "description_en": "A library-cafe concept surrounded by books, offering calm and healthy breakfast options. A perfect, peaceful, and intellectual atmosphere for reading enthusiasts and brunch lovers."
    },
    "Cafe Rose Red": {
        "description": "Tavandan sarkan kurutulmuş kırmızı güllerle dekore edilmiş, romantik ve gotik atmosferiyle benzersiz bar. Özel bira seçkisi, mumlu aydınlatma ve vintage mobilyalarla, unutulmaz bir akşam deneyimi.",
        "description_en": "A unique bar decorated with dried red roses hanging from the ceiling, with romantic and gothic atmosphere. An unforgettable evening experience with special beer selection, candlelit lighting, and vintage furniture."
    },
    "Bar Des Amis": {
        "description": "Grote Markt'a çok yakın, gece geç saatlere kadar açık popüler bar. Canlı atmosferi, geniş bira menüsü ve merkezi konumuyla, turistlerin ve yerel halkın buluşma noktası.",
        "description_en": "A popular bar very close to Grote Markt, open until late at night. A meeting point for tourists and locals with lively atmosphere, extensive beer menu, and central location."
    },
    "Groot Vlaenderen": {
        "description": "Şık ve sofistike atmosferiyle öne çıkan üst sınıf bira evi. Nadir bulunan Belçika biraları, lezzetli yemekler ve zarif servis anlayışıyla, kaliteli bir Brugge akşamı arayanların adresi.",
        "description_en": "An upscale beer house standing out with stylish and sophisticated atmosphere. The address for those seeking a quality Bruges evening with rare Belgian beers, delicious food, and elegant service."
    },
    "The Monk": {
        "description": "Geniş bira menüsü, bilardo masaları ve rahat ortamıyla ünlü geleneksel Belçika barı. Yerel halk arasında popüler, turistik olmayan otantik bar deneyimi arayanlar için ideal.",
        "description_en": "A traditional Belgian bar famous for extensive beer menu, pool tables, and comfortable atmosphere. Ideal for those seeking an authentic non-touristy bar experience, popular among locals."
    },
    "Comptoir des Arts": {
        "description": "Canlı caz ve blues performanslarını izleyebileceğiniz, sanat ve müziğin buluştuğu atmosferik bar. Vintage dekorasyonu, kaliteli kokteylleri ve kültürel etkinlikleriyle, şehrin sanat sahnesinin kalbi.",
        "description_en": "An atmospheric bar where you can watch live jazz and blues performances, where art and music meet. The heart of the city's art scene with vintage decor, quality cocktails, and cultural events."
    },
    "Cherry's": {
        "description": "Renkli dekorasyonu, dev milkshake'leri ve Amerikan tarzı menüsüyle eğlenceli aile restoranı. Çocuklarla gelen aileler için ideal, nostaljik 50'ler Amerika'sını anımsatan retro mekan.",
        "description_en": "A fun family restaurant with colorful decor, giant milkshakes, and American-style menu. Ideal for families with children, a retro venue reminiscent of nostalgic 1950s America."
    },
    "Yesterday's World": {
        "description": "Eski oyuncaklar, nostaljik eşyalar ve 20. yüzyıl yaşam tarzını sergileyen vintage müze-mağaza. Çocukluk anılarına yolculuk ve benzersiz hediyelik eşyalar için keyifli bir durak.",
        "description_en": "A vintage museum-store exhibiting old toys, nostalgic items, and 20th-century lifestyle. An enjoyable stop for a journey into childhood memories and unique souvenirs."
    },
    "L'Estaminet": {
        "description": "Rahat atmosferi, lezzetli tapasları ve geniş bira seçkisiyle öne çıkan samimi mahalle barı. Yerel halkın severek gittiği, turistik olmayan otantik Brugge deneyimi.",
        "description_en": "An intimate neighborhood bar standing out with comfortable atmosphere, delicious tapas, and wide beer selection. An authentic Bruges experience locals love, non-touristy."
    },
    "Da Vinci": {
        "description": "Brugge'deki en iyi İtalyan usulü dondurma (gelato) sunan, el yapımı ve taze malzemelerle çalışan dondurmacı. Geleneksel İtalyan tariflerle hazırlanan onlarca çeşidi ile tatlı molası için mükemmel.",
        "description_en": "An ice cream shop offering the best Italian-style gelato in Bruges, made with handmade and fresh ingredients. Perfect for a sweet break with dozens of flavors prepared with traditional Italian recipes."
    },
    "Uilenspiegel Museum": {
        "description": "Efsanevi Flaman halk kahramanı Tijl Uilenspiegel'e adanmış küçük ama büyüleyici müze. Folklor, yerel efsaneler ve mizah tarihine ışık tutan koleksiyonuyla, bölge kültürüne dalış.",
        "description_en": "A small but enchanting museum dedicated to legendary Flemish folk hero Tijl Uilenspiegel. A dive into regional culture with its collection shedding light on folklore, local legends, and history of humor."
    },
    "Schellemolen": {
        "description": "Damme kanalının kenarında pitoresk manzarasıyla dikkat çeken tarihi yel değirmeni. Bisiklet rotası üzerinde mola vermek ve fotoğraf çekmek için ideal, Brugge kırsalının simgesi.",
        "description_en": "A historic windmill notable for its picturesque scenery by Damme canal. Ideal for taking a break on the bicycle route and photography, a symbol of Bruges countryside."
    },
    "Ter Doest Abbey": {
        "description": "13. yüzyıldan kalma devasa tuğla tahıl ambarıyla ünlü eski Cistercian manastırı. Gotik tarım mimarisi harikası, yanındaki gurme restoran ve huzurlu atmosferiyle kırsal kaçamak.",
        "description_en": "A former Cistercian abbey famous for its massive 13th-century brick barn. A rural getaway with Gothic agricultural architecture wonder, adjacent gourmet restaurant, and peaceful atmosphere."
    },
    "Zeebrugge Beach": {
        "description": "Brugge'ün Kuzey Denizi kıyısındaki liman kasabası, geniş kumsalı ve deniz havasıyla günübirlik ziyaret için ideal. Balık restoranları, gezinti iskelesi ve deniz müzesiyle, şehir hayatından kaçış.",
        "description_en": "Bruges' port town on the North Sea coast, ideal for day visits with wide beach and sea air. An escape from city life with fish restaurants, promenade pier, and maritime museum."
    },
    "Boudewijn Seapark": {
        "description": "Yunus gösterileri, denizaslanı performansları ve lunapark oyuncaklarıyla aileler için eğlence parkı. Su parkı, roller coaster ve hayvan showlarıyla, çocuklu aileler için tam gün eğlence.",
        "description_en": "An amusement park for families with dolphin shows, sea lion performances, and carnival rides. Full-day entertainment for families with children with water park, roller coaster, and animal shows."
    },
    "Kasteel van Loppem": {
        "description": "Neo-Gotik mimarisi, iç dekorasyonu ve labirent bahçesiyle mükemmel korunan 19. yüzyıl şatosu. Antik mobilyalar, sanat eserleri ve dönem atmosferiyle, aristokrat yaşamına göz atma fırsatı.",
        "description_en": "A 19th-century castle perfectly preserved with Neo-Gothic architecture, interior decoration, and maze garden. An opportunity to glimpse aristocratic life with antique furniture, artworks, and period atmosphere."
    },
    "Maze of Loppem": {
        "description": "1873 yılında tasarlanmış, Belçika'nın en eski ve büyük çit labirentlerinden biri. Loppem Şatosu'nun bahçesinde, çocuklar ve yetişkinler için eğlenceli macera deneyimi.",
        "description_en": "One of Belgium's oldest and largest hedge mazes, designed in 1873. A fun adventure experience for children and adults in the garden of Loppem Castle."
    },
    "Bulskampveld": {
        "description": "Geniş ormanlık alanı, kalesi ve göletleriyle Brugge çevresinin en büyük doğa parklarından biri. Yürüyüş, bisiklet ve piknik için mükemmel, şehir hayatından tam bir kopuş.",
        "description_en": "One of the largest nature parks around Bruges with extensive woodland area, castle, and ponds. Perfect for hiking, cycling, and picnicking, a complete escape from city life."
    },
    "Ryckevelde": {
        "description": "Büyülü Ryckeveldebos ormanının yanında, şato, park ve hayvan çiftliğiyle aile dostu rekreasyon alanı. Yürüyüş parkurları, çocuk oyun alanları ve kafesiyle, hafta sonu gezisi için ideal.",
        "description_en": "A family-friendly recreation area by the magical Ryckeveldebos forest, with castle, park, and animal farm. Ideal for weekend trips with hiking trails, children's playgrounds, and cafe."
    },
    "Tillegembos": {
        "description": "Bir şato ve geniş ormanla çevrili, Brugge'ün hemen dışındaki popüler rekreasyon bölgesi. Yürüyüş yolları, göletler ve doğa gözlem kuleleriyle, doğa severler için yakın bir kaçış noktası.",
        "description_en": "A popular recreation area just outside Bruges, surrounded by a castle and extensive forest. A nearby escape point for nature lovers with walking paths, ponds, and nature observation towers."
    },
    "Provincial Domain Tudor": {
        "description": "Tudor tarzı şato, geniş bahçeler ve çeşitli etkinliklere ev sahipliği yapan eyalet alanı. Piknik alanları, oyun alanları ve mevsimlik festivalleriyle, aileler için çok amaçlı yeşil alan.",
        "description_en": "A provincial domain with Tudor-style castle, extensive gardens, and hosting various events. A multi-purpose green area for families with picnic areas, playgrounds, and seasonal festivals."
    },
    "Damme": {
        "description": "Brugge'den bisikletle ulaşılabilecek mesafede, pittoresk mimarisi ve eski kitapçı geleneğiyle ünlü tarihi kasaba. Ortaçağ kanalı boyunca romantik yürüyüş ve antika kitap keşfi için ideal.",
        "description_en": "A historic town within cycling distance from Bruges, famous for picturesque architecture and old bookshop tradition. Ideal for romantic walks along medieval canal and discovering antique books."
    },
    "Damse Vaart": {
        "description": "Brugge'den Damme'a uzanan, ağaç sıralı popüler bisiklet ve yürüyüş rotası. Dümdüz kanal boyunca pitoresk manzaralar, yel değirmenleri ve kırsal Flaman atmosferi.",
        "description_en": "A tree-lined popular cycling and walking route from Bruges to Damme. Picturesque views along a straight canal, windmills, and rural Flemish atmosphere."
    }
}

filepath = 'assets/cities/brugge.json'
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

print(f"\n✅ Manually enriched {count} items (Brugge Batch 2).")
