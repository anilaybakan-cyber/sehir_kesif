import json
import os

# BATCH 4: Brugge, Santorini, Heidelberg, Viyana, Prag

enrichment_data = {
    "brugge": [
        # SQUARES & LANDMARKS
        {"name": "Grote Markt", "category": "Manzara", "tags": ["square", "belfry", "center"], "lat": 51.2085, "lng": 3.2240, "rating": 4.9, "description": "Renkli evler ve çan kulesiyle şehrin kalbi.", "description_en": "Heart of the city with colorful houses and belfry."},
        {"name": "Belfry of Bruges", "category": "Tarihi", "tags": ["tower", "climb", "view"], "lat": 51.2082, "lng": 3.2245, "rating": 4.7, "description": "366 basamakla tırmanılan ikonik çan kulesi.", "description_en": "Iconic bell tower climbed via 366 steps."},
        {"name": "Rozenhoedkaai", "category": "Manzara", "tags": ["photo spot", "canals", "iconic"], "lat": 51.2065, "lng": 3.2260, "rating": 4.9, "description": "Brugge'ün en çok fotoğraflanan kartpostallık köşesi.", "description_en": "Bruges' most photographed postcard corner."},
        {"name": "Burg Square", "category": "Manzara", "tags": ["square", "town hall", "historic"], "lat": 51.2080, "lng": 3.2265, "rating": 4.7, "description": "Belediye binası ve Kutsal Kan Bazilikası meydanı.", "description_en": "Town hall and Basilica of the Holy Blood square."},
        {"name": "Basilica of the Holy Blood", "category": "Tarihi", "tags": ["church", "relic", "romanesque"], "lat": 51.2080, "lng": 3.2266, "rating": 4.6, "description": "Kutsal kan kalıntısının saklandığı özel bazilika.", "description_en": "Special basilica holding relic of the Holy Blood."},
        {"name": "Church of Our Lady", "category": "Tarihi", "tags": ["church", "michelangelo", "madonna"], "lat": 51.2045, "lng": 3.2248, "rating": 4.6, "description": "Michelangelo'nun Madonna heykelinin bulunduğu kilise.", "description_en": "Church housing Michelangelo's Madonna sculpture."},
        {"name": "St Salvator's Cathedral", "category": "Tarihi", "tags": ["cathedral", "gothic", "art"], "lat": 51.2055, "lng": 3.2215, "rating": 4.5, "description": "Brugge'ün en eski kilisesi ve katedrali.", "description_en": "Bruges' oldest church and cathedral."},
        # PARKS & WATER
        {"name": "Lake of Love (Minnewater)", "category": "Park", "tags": ["lake", "swans", "romantic"], "lat": 51.1985, "lng": 3.2245, "rating": 4.8, "description": "Kuğuları ve sükunetiyle ünlü romantik park.", "description_en": "Romantic park famous for swans and tranquility."},
        {"name": "Begijnhof", "category": "Tarihi", "tags": ["beguinage", "peaceful", "unesco"], "lat": 51.2005, "lng": 3.2240, "rating": 4.8, "description": "UNESCO Mirası huzurlu ortaçağ manastır kompleksi.", "description_en": "UNESCO Heritage peaceful medieval monastery complex."},
        {"name": "Canal Boat Tour", "category": "Deneyim", "tags": ["boat", "canals", "tour"], "lat": 51.2065, "lng": 3.2255, "rating": 4.7, "description": "Kanal teknesiyle şehir turu.", "description_en": "City tour by canal boat."},
        {"name": "Windmills Park", "category": "Park", "tags": ["windmills", "walk", "views"], "lat": 51.2150, "lng": 3.2350, "rating": 4.5, "description": "Tarihi yel değirmenleri ve yürüyüş parkuru.", "description_en": "Historic windmills and walking path."},
        # MUSEUMS
        {"name": "Groeningemuseum", "category": "Müze", "tags": ["art", "flemish primitives", "paintings"], "lat": 51.2055, "lng": 3.2270, "rating": 4.6, "description": "Flaman ilkel ressamların başyapıtları.", "description_en": "Masterpieces of Flemish Primitives."},
        {"name": "Choco-Story", "category": "Müze", "tags": ["chocolate", "history", "tasting"], "lat": 51.2095, "lng": 3.2255, "rating": 4.5, "description": "Belçika çikolata tarihi ve tadım.", "description_en": "Belgian chocolate history and tasting."},
        {"name": "Frietmuseum", "category": "Müze", "tags": ["fries", "quirky", "belgian"], "lat": 51.2090, "lng": 3.2245, "rating": 4.4, "description": "Patates kızartmasının tarihini anlatan ilginç müze.", "description_en": "Quirky museum about the history of French fries."},
        {"name": "Diamond Museum", "category": "Müze", "tags": ["diamonds", "jewelry", "history"], "lat": 51.2040, "lng": 3.2235, "rating": 4.3, "description": "Brugge'ün elmas işçiliği mirası.", "description_en": "Bruges' diamond cutting heritage."},
        {"name": "Historium Bruges", "category": "Müze", "tags": ["interactive", "medieval", "experience"], "lat": 51.2088, "lng": 3.2242, "rating": 4.5, "description": "Ortaçağ Brugge'ünü interaktif keşif.", "description_en": "Interactive discovery of medieval Bruges."},
        # BEER & BREWERY
        {"name": "De Halve Maan Brewery", "category": "Deneyim", "tags": ["brewery", "tour", "beer"], "lat": 51.2025, "lng": 3.2240, "rating": 4.7, "description": "Tarihi aile bira fabrikası, popüler tur.", "description_en": "Historic family brewery, popular tour."},
        {"name": "2be Beer Wall", "category": "Alışveriş", "tags": ["beer", "shop", "canal view"], "lat": 51.2062, "lng": 3.2258, "rating": 4.6, "description": "Devasa bira duvarı ve kanal manzaralı bar.", "description_en": "Massive beer wall and bar with canal view."},
        # RESTAURANTS
        {"name": "Vlissinghe", "category": "Restoran", "tags": ["pub", "oldest", "historic"], "lat": 51.2120, "lng": 3.2295, "rating": 4.7, "description": "1515'ten beri açık olan Brugge'ün en eski barı.", "description_en": "Bruges' oldest bar, open since 1515."},
        {"name": "De Stove", "category": "Restoran", "tags": ["belgian", "cozy", "small"], "lat": 51.2070, "lng": 3.2230, "rating": 4.6, "description": "Samimi ortamda otantik Belçika yemekleri.", "description_en": "Authentic Belgian dishes in cozy setting."},
        {"name": "De Koetse", "category": "Restoran", "tags": ["traditional", "flemish", "stew"], "lat": 51.2075, "lng": 3.2238, "rating": 4.5, "description": "Geleneksel Flaman yahni (stoofvlees).", "description_en": "Traditional Flemish stew (stoofvlees)."},
        {"name": "Sans Cravate", "category": "Restoran", "tags": ["michelin", "fine dining", "creative"], "lat": 51.2058, "lng": 3.2255, "rating": 4.7, "description": "Michelin yıldızlı yaratıcı Belçika mutfağı.", "description_en": "Michelin starred creative Belgian cuisine."},
        {"name": "Chez Olivier", "category": "Restoran", "tags": ["mussels", "seafood", "terrace"], "lat": 51.2068, "lng": 3.2248, "rating": 4.5, "description": "Midye ve deniz ürünleri.", "description_en": "Mussels and seafood."},
        # CAFES & SWEETS
        {"name": "House of Waffles", "category": "Kafe", "tags": ["waffles", "dessert", "toppings"], "lat": 51.2075, "lng": 3.2235, "rating": 4.6, "description": "Çeşit çeşit Belçika waffle'ı.", "description_en": "Various Belgian waffles."},
        {"name": "The Old Chocolate House", "category": "Kafe", "tags": ["hot chocolate", "chocolate", "cozy"], "lat": 51.2072, "lng": 3.2242, "rating": 4.7, "description": "En iyi sıcak çikolata deneyimi.", "description_en": "Best hot chocolate experience."},
        {"name": "Dumon Chocolatier", "category": "Alışveriş", "tags": ["pralines", "artisan", "quality"], "lat": 51.2065, "lng": 3.2250, "rating": 4.8, "description": "El yapımı Belçika pralinleri.", "description_en": "Handmade Belgian pralines."},
        {"name": "That's Toast", "category": "Kafe", "tags": ["brunch", "coffee", "modern"], "lat": 51.2060, "lng": 3.2225, "rating": 4.5, "description": "Modern brunch ve kahve.", "description_en": "Modern brunch and coffee."},
        # SHOPPING
        {"name": "Lace Shops", "category": "Alışveriş", "tags": ["lace", "traditional", "handmade"], "lat": 51.2070, "lng": 3.2245, "rating": 4.4, "description": "Geleneksel el yapımı Brugge danteli.", "description_en": "Traditional handmade Bruges lace."},
        {"name": "Steenstraat", "category": "Alışveriş", "tags": ["shopping street", "brands", "walk"], "lat": 51.2065, "lng": 3.2220, "rating": 4.3, "description": "Ana alışveriş caddesi.", "description_en": "Main shopping street."},
    ],
    "santorini": [
        # ICONIC VIEWS
        {"name": "Oia Castle", "category": "Manzara", "tags": ["sunset", "famous", "crowd"], "lat": 36.4620, "lng": 25.3725, "rating": 4.9, "description": "Dünyanın en ünlü gün batımı noktası.", "description_en": "World's most famous sunset spot."},
        {"name": "Fira - Oia Hike", "category": "Park", "tags": ["hike", "caldera", "scenic"], "lat": 36.4400, "lng": 25.4100, "rating": 4.9, "description": "Kaldera kenarından 10 km yürüyüş rotası.", "description_en": "10 km hiking trail along caldera edge."},
        {"name": "Three Bells of Fira", "category": "Manzara", "tags": ["church", "blue dome", "photo"], "lat": 36.4230, "lng": 25.4290, "rating": 4.7, "description": "İkonik mavi kubbeli kilise manzarası.", "description_en": "Iconic blue-domed church view."},
        {"name": "Imerovigli Viewpoint", "category": "Manzara", "tags": ["village", "caldera", "quiet"], "lat": 36.4350, "lng": 25.4200, "rating": 4.8, "description": "Sakin köyden kaldera manzarası.", "description_en": "Caldera view from quiet village."},
        {"name": "Skaros Rock", "category": "Manzara", "tags": ["hike", "fortress", "panorama"], "lat": 36.4340, "lng": 25.4180, "rating": 4.7, "description": "Eski kale kalıntıları ve 360° manzara.", "description_en": "Old fortress ruins and 360° view."},
        # BEACHES
        {"name": "Red Beach", "category": "Park", "tags": ["beach", "red rocks", "unique"], "lat": 36.3485, "lng": 25.3945, "rating": 4.6, "description": "Kızıl volkanik kayalar arasında benzersiz plaj.", "description_en": "Unique beach among red volcanic rocks."},
        {"name": "Perissa Beach", "category": "Park", "tags": ["black sand", "long", "facilities"], "lat": 36.3550, "lng": 25.4770, "rating": 4.5, "description": "Siyah kum plajı ve olanaklar.", "description_en": "Black sand beach with facilities."},
        {"name": "Kamari Beach", "category": "Park", "tags": ["black sand", "organized", "bars"], "lat": 36.3700, "lng": 25.4850, "rating": 4.5, "description": "Organize siyah kum plajı.", "description_en": "Organized black sand beach."},
        {"name": "White Beach", "category": "Park", "tags": ["white cliffs", "boat access", "secluded"], "lat": 36.3460, "lng": 25.3970, "rating": 4.6, "description": "Beyaz kayalıklar arasında tekneyle ulaşılan plaj.", "description_en": "Beach accessible by boat among white cliffs."},
        # HISTORIC & CULTURE
        {"name": "Akrotiri Archaeological Site", "category": "Müze", "tags": ["ruins", "minoan", "pompeii"], "lat": 36.3515, "lng": 25.4035, "rating": 4.7, "description": "Yunan Pompeii'si, volkan külleri altındaki antik kent.", "description_en": "Greek Pompeii, ancient city under volcanic ash."},
        {"name": "Museum of Prehistoric Thera", "category": "Müze", "tags": ["museum", "artifacts", "frescoes"], "lat": 36.4165, "lng": 25.4315, "rating": 4.6, "description": "Akrotiri buluntuları ve freskler.", "description_en": "Akrotiri findings and frescoes."},
        {"name": "Ancient Thera", "category": "Tarihi", "tags": ["ruins", "hilltop", "history"], "lat": 36.3680, "lng": 25.4750, "rating": 4.5, "description": "Dağın tepesinde antik şehir kalıntıları.", "description_en": "Ancient city ruins on mountaintop."},
        {"name": "Pyrgos Village", "category": "Tarihi", "tags": ["village", "castle", "authentic"], "lat": 36.3880, "lng": 25.4420, "rating": 4.6, "description": "Otantik köy ve Venedik kalesi.", "description_en": "Authentic village and Venetian castle."},
        # WINE
        {"name": "Santo Wines", "category": "Deneyim", "tags": ["wine", "tasting", "view"], "lat": 36.3835, "lng": 25.4410, "rating": 4.8, "description": "Kaldera manzaralı şarap tadımı.", "description_en": "Wine tasting with caldera view."},
        {"name": "Venetsanos Winery", "category": "Deneyim", "tags": ["wine", "historic", "sunset"], "lat": 36.3830, "lng": 25.4400, "rating": 4.7, "description": "Tarihi şaraplıkta gün batımı eşliğinde tadım.", "description_en": "Tasting at sunset in historic winery."},
        {"name": "Gavalas Winery", "category": "Deneyim", "tags": ["wine", "family", "traditional"], "lat": 36.3875, "lng": 25.4415, "rating": 4.5, "description": "Aile işletmesi geleneksel şaraphane.", "description_en": "Family-run traditional winery."},
        # RESTAURANTS
        {"name": "Metaxi Mas", "category": "Restoran", "tags": ["tavern", "local", "hidden gem"], "lat": 36.3750, "lng": 25.4500, "rating": 4.9, "description": "Yerlilerin favorisi gizli taverna.", "description_en": "Locals' favorite hidden tavern."},
        {"name": "Melitini", "category": "Restoran", "tags": ["tapas", "greek", "oia"], "lat": 36.4625, "lng": 25.3745, "rating": 4.7, "description": "Oia'da lezzetli Yunan mezeleri.", "description_en": "Delicious Greek appetizers in Oia."},
        {"name": "Amoudi Bay Taverns", "category": "Restoran", "tags": ["seafood", "bay", "fresh"], "lat": 36.4600, "lng": 25.3710, "rating": 4.8, "description": "Oia'nın altındaki limanda taze deniz ürünleri.", "description_en": "Fresh seafood at harbor below Oia."},
        {"name": "Lucky's Souvlaki", "category": "Restoran", "tags": ["gyros", "cheap eats", "fira"], "lat": 36.4175, "lng": 25.4300, "rating": 4.5, "description": "Uygun fiyatlı gyros ve souvlaki.", "description_en": "Budget-friendly gyros and souvlaki."},
        {"name": "Selene", "category": "Restoran", "tags": ["fine dining", "greek", "creative"], "lat": 36.3885, "lng": 25.4425, "rating": 4.7, "description": "Yaratıcı Yunan gurme mutfağı.", "description_en": "Creative Greek gourmet cuisine."},
        # CAFES
        {"name": "PK Cocktail Bar", "category": "Kafe", "tags": ["sunset", "cocktails", "oia"], "lat": 36.4618, "lng": 25.3730, "rating": 4.6, "description": "Gün batımı eşliğinde kokteyl.", "description_en": "Cocktails at sunset."},
        {"name": "Galini Café", "category": "Kafe", "tags": ["coffee", "view", "breakfast"], "lat": 36.4345, "lng": 25.4195, "rating": 4.5, "description": "Kaldera manzaralı kahvaltı ve kahve.", "description_en": "Breakfast and coffee with caldera view."},
        # EXPERIENCES
        {"name": "Catamaran Cruise", "category": "Deneyim", "tags": ["boat", "caldera", "sunset"], "lat": 36.4000, "lng": 25.4200, "rating": 4.8, "description": "Kaldera turu ve gün batımı kruvaziyer.", "description_en": "Caldera tour and sunset cruise."},
        {"name": "Hot Springs", "category": "Deneyim", "tags": ["volcano", "swim", "thermal"], "lat": 36.4050, "lng": 25.3950, "rating": 4.5, "description": "Yanardağ kaldere sıcak suları.", "description_en": "Volcanic caldera hot springs."},
        {"name": "Volcano Hike", "category": "Deneyim", "tags": ["volcano", "walk", "active"], "lat": 36.4020, "lng": 25.3900, "rating": 4.6, "description": "Aktif yanardağ kraterin yürüyüşü.", "description_en": "Hike on active volcano crater."},
    ],
    "heidelberg": [
        # CASTLE & OLD TOWN
        {"name": "Heidelberg Castle", "category": "Tarihi", "tags": ["castle", "ruins", "romantic"], "lat": 49.4105, "lng": 8.7155, "rating": 4.8, "description": "Almanya'nın en romantik kale kalıntısı.", "description_en": "Germany's most romantic castle ruin."},
        {"name": "Old Bridge (Karl Theodor Bridge)", "category": "Manzara", "tags": ["bridge", "gate", "iconic"], "lat": 49.4135, "lng": 8.7100, "rating": 4.8, "description": "Neckar nehri üzerindeki ikonik köprü ve kapı.", "description_en": "Iconic bridge and gate over Neckar river."},
        {"name": "Marktplatz", "category": "Manzara", "tags": ["square", "fountain", "cafes"], "lat": 49.4122, "lng": 8.7105, "rating": 4.6, "description": "Kilise ve çeşmeli tarihi meydan.", "description_en": "Historic square with church and fountain."},
        {"name": "Hauptstrasse", "category": "Alışveriş", "tags": ["shopping", "pedestrian", "longest"], "lat": 49.4110, "lng": 8.7050, "rating": 4.5, "description": "Avrupa'nın en uzun yaya caddelerinden biri.", "description_en": "One of Europe's longest pedestrian streets."},
        {"name": "Church of the Holy Spirit", "category": "Tarihi", "tags": ["church", "gothic", "market"], "lat": 49.4118, "lng": 8.7105, "rating": 4.5, "description": "Gotik kilise ve pazar meydanı.", "description_en": "Gothic church and market square."},
        {"name": "Kornmarkt", "category": "Manzara", "tags": ["square", "castle view", "madonna"], "lat": 49.4108, "lng": 8.7115, "rating": 4.6, "description": "Kale manzaralı Madonna heykelinin olduğu meydan.", "description_en": "Square with Madonna statue and castle view."},
        # NATURE & VIEWS
        {"name": "Philosophers' Walk", "category": "Park", "tags": ["walk", "view", "famous"], "lat": 49.4160, "lng": 8.7110, "rating": 4.9, "description": "Filozofların düşünmek için yürüdüğü efsanevi yol.", "description_en": "Legendary path where philosophers walked to think."},
        {"name": "Heiligenberg", "category": "Park", "tags": ["hill", "ruins", "nature"], "lat": 49.4200, "lng": 8.7080, "rating": 4.6, "description": "Roma kalıntıları ve doğa yürüyüşü.", "description_en": "Roman ruins and nature walk."},
        {"name": "Neckarwiese", "category": "Park", "tags": ["river", "picnic", "relax"], "lat": 49.4150, "lng": 8.6950, "rating": 4.7, "description": "Nehir kenarında güneşlenmek için geniş çim alan.", "description_en": "Wide lawn for sunbathing by the river."},
        {"name": "Schlangenweg", "category": "Park", "tags": ["path", "steep", "views"], "lat": 49.4145, "lng": 8.7095, "rating": 4.5, "description": "Filosof Yolu'na tırmanan dik patika.", "description_en": "Steep path climbing to Philosophers' Walk."},
        # UNIVERSITY & MUSEUMS
        {"name": "Heidelberg University", "category": "Tarihi", "tags": ["university", "oldest", "historic"], "lat": 49.4125, "lng": 8.7065, "rating": 4.7, "description": "Almanya'nın en eski üniversitesi (1386).", "description_en": "Germany's oldest university (1386)."},
        {"name": "Studentenkarzer", "category": "Müze", "tags": ["prison", "graffiti", "unique"], "lat": 49.4120, "lng": 8.7060, "rating": 4.5, "description": "Duvarları çizimlerle dolu eski öğrenci hapishanesi.", "description_en": "Old student prison with graffiti-covered walls."},
        {"name": "Great Wine Barrel", "category": "Müze", "tags": ["barrel", "wine", "castle"], "lat": 49.4107, "lng": 8.7153, "rating": 4.4, "description": "Kalede bulunan dünyanın en büyük şarap fıçısı.", "description_en": "World's largest wine barrel in the castle."},
        {"name": "Pharmacy Museum", "category": "Müze", "tags": ["pharmacy", "apothecary", "historic"], "lat": 49.4106, "lng": 8.7154, "rating": 4.4, "description": "Kale içindeki tarihi eczane müzesi.", "description_en": "Historic pharmacy museum in the castle."},
        {"name": "Palatinate Museum", "category": "Müze", "tags": ["art", "archaeology", "regional"], "lat": 49.4118, "lng": 8.7100, "rating": 4.5, "description": "Bölgesel sanat ve arkeoloji.", "description_en": "Regional art and archaeology."},
        # RESTAURANTS
        {"name": "Kulturbrauerei", "category": "Restoran", "tags": ["brewery", "german", "beer"], "lat": 49.4130, "lng": 8.7130, "rating": 4.6, "description": "Kendi yapımı bira ve Alman yemekleri.", "description_en": "Own brewed beer and German dishes."},
        {"name": "Schnitzelbank", "category": "Restoran", "tags": ["schnitzel", "cozy", "barrel"], "lat": 49.4110, "lng": 8.7090, "rating": 4.7, "description": "Fıçı masalı rustik şnitzel restoranı.", "description_en": "Rustic schnitzel restaurant with barrel tables."},
        {"name": "Zum Roten Ochsen", "category": "Restoran", "tags": ["historic", "student", "traditional"], "lat": 49.4115, "lng": 8.7085, "rating": 4.5, "description": "1703'ten beri açık olan tarihi öğrenci lokantası.", "description_en": "Historic student tavern open since 1703."},
        {"name": "Hackteufel", "category": "Restoran", "tags": ["fine dining", "modern", "german"], "lat": 49.4105, "lng": 8.7080, "rating": 4.6, "description": "Modern Alman gurme mutfağı.", "description_en": "Modern German gourmet cuisine."},
        {"name": "Essighaus", "category": "Restoran", "tags": ["vinegar house", "german", "cozy"], "lat": 49.4112, "lng": 8.7095, "rating": 4.5, "description": "Tarihi sirke evinde Alman mutfağı.", "description_en": "German cuisine in historic vinegar house."},
        # CAFES
        {"name": "Café Knösel", "category": "Kafe", "tags": ["student kiss", "chocolate", "historic"], "lat": 49.4120, "lng": 8.7100, "rating": 4.5, "description": "'Öğrenci öpücüğü' çikolatalarıyla ünlü tarihi kafe.", "description_en": "Historic cafe famous for 'Student Kiss' chocolates."},
        {"name": "Café Burkardt", "category": "Kafe", "tags": ["pastry", "coffee", "elegant"], "lat": 49.4118, "lng": 8.7092, "rating": 4.4, "description": "Zarif atmosferde pasta ve kahve.", "description_en": "Pastry and coffee in elegant atmosphere."},
        {"name": "Yilliy", "category": "Kafe", "tags": ["specialty coffee", "modern", "brunch"], "lat": 49.4110, "lng": 8.7070, "rating": 4.6, "description": "Modern özel kahve deneyimi.", "description_en": "Modern specialty coffee experience."},
        # EXPERIENCES
        {"name": "Funicular to Castle", "category": "Deneyim", "tags": ["funicular", "castle", "historic"], "lat": 49.4100, "lng": 8.7125, "rating": 4.5, "description": "Tarihi kableyle kaleye çıkış.", "description_en": "Historic cable car ride to castle."},
        {"name": "River Cruise", "category": "Deneyim", "tags": ["boat", "neckar", "scenic"], "lat": 49.4135, "lng": 8.7095, "rating": 4.4, "description": "Neckar nehrinde tekne turu.", "description_en": "Boat tour on Neckar river."},
    ],
    "viyana": [
        # PALACES
        {"name": "Schönbrunn Palace", "category": "Tarihi", "tags": ["palace", "gardens", "habsburg"], "lat": 48.1848, "lng": 16.3122, "rating": 4.9, "description": "Habsburg hanedanının muazzam yazlık sarayı.", "description_en": "Magnificent summer palace of the Habsburgs."},
        {"name": "Belvedere Museum", "category": "Müze", "tags": ["klimt", "kiss", "baroque"], "lat": 48.1915, "lng": 16.3809, "rating": 4.7, "description": "Gustav Klimt'in 'Öpücük' tablosunun evi.", "description_en": "Home of Gustav Klimt's 'The Kiss'."},
        {"name": "Hofburg", "category": "Tarihi", "tags": ["imperial", "apartments", "museum"], "lat": 48.2065, "lng": 16.3634, "rating": 4.7, "description": "Avusturya imparatorlarının kışlık sarayı.", "description_en": "Winter palace of Austrian emperors."},
        {"name": "Kunsthistorisches Museum", "category": "Müze", "tags": ["art", "history", "world class"], "lat": 48.2038, "lng": 16.3616, "rating": 4.8, "description": "Dünya çapında sanat eserleri koleksiyonu.", "description_en": "World-class art collection."},
        {"name": "Albertina", "category": "Müze", "tags": ["graphics", "monet", "picasso"], "lat": 48.2048, "lng": 16.3685, "rating": 4.6, "description": "Dürer'den Picasso'ya grafik sanatları.", "description_en": "Graphic arts from Dürer to Picasso."},
        # CHURCHES & LANDMARKS
        {"name": "St. Stephen's Cathedral", "category": "Tarihi", "tags": ["cathedral", "gothic", "icon"], "lat": 48.2085, "lng": 16.3731, "rating": 4.8, "description": "Viyana'nın kalbindeki gotik şaheser.", "description_en": "Gothic masterpiece in the heart of Vienna."},
        {"name": "Karlskirche", "category": "Tarihi", "tags": ["church", "baroque", "dome"], "lat": 48.1982, "lng": 16.3718, "rating": 4.6, "description": "Etkileyici kubbesiyle barok kilise.", "description_en": "Baroque church with impressive dome."},
        {"name": "Hundertwasser House", "category": "Manzara", "tags": ["architecture", "colorful", "unique"], "lat": 48.2073, "lng": 16.3932, "rating": 4.5, "description": "Rengarenk ve asimetrik mimari harikası.", "description_en": "Colorful and asymmetric architectural wonder."},
        {"name": "Rathaus", "category": "Tarihi", "tags": ["city hall", "gothic", "events"], "lat": 48.2108, "lng": 16.3564, "rating": 4.5, "description": "Neo-Gotik belediye binası ve meydanı.", "description_en": "Neo-Gothic city hall and square."},
        # PARKS
        {"name": "Prater Park", "category": "Park", "tags": ["ferris wheel", "amusement", "green"], "lat": 48.2166, "lng": 16.3970, "rating": 4.6, "description": "İkonik dönme dolabı ve geniş yeşil alan.", "description_en": "Iconic Ferris wheel and large green space."},
        {"name": "Stadtpark", "category": "Park", "tags": ["park", "strauss statue", "central"], "lat": 48.2040, "lng": 16.3795, "rating": 4.5, "description": "Johann Strauss heykelinin bulunduğu şehir parkı.", "description_en": "City park with Johann Strauss statue."},
        {"name": "Volksgarten", "category": "Park", "tags": ["roses", "garden", "temple"], "lat": 48.2085, "lng": 16.3615, "rating": 4.6, "description": "Gül bahçeleri ve Theseus Tapınağı.", "description_en": "Rose gardens and Temple of Theseus."},
        # MUSIC & CULTURE
        {"name": "Vienna State Opera", "category": "Deneyim", "tags": ["opera", "music", "world class"], "lat": 48.2030, "lng": 16.3691, "rating": 4.9, "description": "Dünyanın en prestijli opera binası.", "description_en": "World's most prestigious opera house."},
        {"name": "Musikverein", "category": "Deneyim", "tags": ["concert", "classical", "new year"], "lat": 48.2005, "lng": 16.3725, "rating": 4.8, "description": "Yeni Yıl konserinin yapıldığı efsanevi salon.", "description_en": "Legendary hall of New Year's Concert."},
        {"name": "Mozarthaus Vienna", "category": "Müze", "tags": ["mozart", "museum", "apartment"], "lat": 48.2072, "lng": 16.3755, "rating": 4.5, "description": "Mozart'ın yaşadığı ve beste yaptığı ev.", "description_en": "House where Mozart lived and composed."},
        # COFFEE HOUSES
        {"name": "Cafe Central", "category": "Kafe", "tags": ["historic", "famous", "architecture"], "lat": 48.2104, "lng": 16.3653, "rating": 4.7, "description": "Freud ve Trotsky'nin müdavimi olduğu efsanevi kafe.", "description_en": "Legendary cafe frequented by Freud and Trotsky."},
        {"name": "Cafe Sacher", "category": "Kafe", "tags": ["sachertorte", "elegant", "famous"], "lat": 48.2038, "lng": 16.3695, "rating": 4.6, "description": "Orijinal Sachertorte'nin evi.", "description_en": "Home of the original Sachertorte."},
        {"name": "Cafe Sperl", "category": "Kafe", "tags": ["authentic", "billiards", "historic"], "lat": 48.1992, "lng": 16.3580, "rating": 4.6, "description": "1880'lerden kalma otantik kahve evi.", "description_en": "Authentic coffee house from the 1880s."},
        {"name": "Demel", "category": "Kafe", "tags": ["pastry", "imperial", "elegant"], "lat": 48.2095, "lng": 16.3670, "rating": 4.7, "description": "İmparatorluk döneminden kalma şık pastane.", "description_en": "Elegant pastry shop from imperial era."},
        # RESTAURANTS
        {"name": "Figlmüller", "category": "Restoran", "tags": ["schnitzel", "famous", "huge"], "lat": 48.2095, "lng": 16.3745, "rating": 4.6, "description": "Şehrin en ünlü dev şnitzeli.", "description_en": "City's most famous giant schnitzel."},
        {"name": "Plachutta", "category": "Restoran", "tags": ["tafelspitz", "traditional", "beef"], "lat": 48.2110, "lng": 16.3750, "rating": 4.5, "description": "Geleneksel Viyana bifteği (Tafelspitz).", "description_en": "Traditional Viennese beef (Tafelspitz)."},
        {"name": "Zum Schwarzen Kameel", "category": "Restoran", "tags": ["historic", "wine bar", "elegant"], "lat": 48.2105, "lng": 16.3685, "rating": 4.6, "description": "1618'den beri açık olan tarihi mekan.", "description_en": "Historic venue open since 1618."},
        {"name": "Steirereck", "category": "Restoran", "tags": ["michelin", "fine dining", "park"], "lat": 48.2050, "lng": 16.3810, "rating": 4.8, "description": "Park içinde 2 Michelin yıldızlı restoran.", "description_en": "2 Michelin star restaurant in the park."},
        # MARKETS & SHOPPING
        {"name": "Naschmarkt", "category": "Alışveriş", "tags": ["market", "food", "vibrant"], "lat": 48.1985, "lng": 16.3630, "rating": 4.6, "description": "Viyana'nın en büyük ve eski pazarı.", "description_en": "Vienna's largest and oldest market."},
        {"name": "Graben", "category": "Alışveriş", "tags": ["shopping", "pedestrian", "luxury"], "lat": 48.2085, "lng": 16.3700, "rating": 4.5, "description": "Lüks mağazaların bulunduğu yaya caddesi.", "description_en": "Pedestrian street with luxury shops."},
    ],
    "prag": [
        # OLD TOWN
        {"name": "Charles Bridge", "category": "Tarihi", "tags": ["bridge", "statues", "iconic"], "lat": 50.0865, "lng": 14.4114, "rating": 4.9, "description": "Heykellerle süslü efsanevi 14. yüzyıl köprüsü.", "description_en": "Legendary 14th century bridge with statues."},
        {"name": "Old Town Square", "category": "Manzara", "tags": ["square", "clock", "gothic"], "lat": 50.0875, "lng": 14.4211, "rating": 4.9, "description": "Astronomik Saat Kulesi'nin bulunduğu tarihi meydan.", "description_en": "Historic square with Astronomical Clock Tower."},
        {"name": "Astronomical Clock", "category": "Tarihi", "tags": ["clock", "medieval", "apostles"], "lat": 50.0871, "lng": 14.4212, "rating": 4.7, "description": "600 yıllık astronomik saat ve havari gösterisi.", "description_en": "600-year-old astronomical clock and apostle show."},
        {"name": "Tyn Church", "category": "Tarihi", "tags": ["church", "gothic", "towers"], "lat": 50.0878, "lng": 14.4225, "rating": 4.6, "description": "İkonik gotik kuleleriyle Eski Şehir kilisesi.", "description_en": "Old Town church with iconic Gothic towers."},
        {"name": "Jewish Quarter (Josefov)", "category": "Tarihi", "tags": ["jewish", "synagogues", "cemetery"], "lat": 50.0900, "lng": 14.4180, "rating": 4.7, "description": "Sinagoglar ve tarihi Yahudi mezarlığı.", "description_en": "Synagogues and historic Jewish cemetery."},
        # CASTLE COMPLEX
        {"name": "Prague Castle", "category": "Tarihi", "tags": ["castle", "largest", "complex"], "lat": 50.0909, "lng": 14.4005, "rating": 4.8, "description": "Dünyanın en büyük antik kale kompleksi.", "description_en": "World's largest ancient castle complex."},
        {"name": "St. Vitus Cathedral", "category": "Tarihi", "tags": ["cathedral", "gothic", "stained glass"], "lat": 50.0906, "lng": 14.4007, "rating": 4.8, "description": "Kale içindeki muazzam gotik katedral.", "description_en": "Magnificent Gothic cathedral within the castle."},
        {"name": "Golden Lane", "category": "Tarihi", "tags": ["lane", "colorful", "kafka"], "lat": 50.0912, "lng": 14.4020, "rating": 4.5, "description": "Renkli küçük evlerin olduğu tarihi sokak.", "description_en": "Historic street with colorful small houses."},
        {"name": "Old Royal Palace", "category": "Tarihi", "tags": ["palace", "halls", "history"], "lat": 50.0905, "lng": 14.4010, "rating": 4.5, "description": "Vladislav Hall ve Rönesans mimarisi.", "description_en": "Vladislav Hall and Renaissance architecture."},
        # VIEWS & BRIDGES
        {"name": "Petrin Hill", "category": "Park", "tags": ["park", "tower", "funicular"], "lat": 50.0833, "lng": 14.3950, "rating": 4.7, "description": "Minyatür Eiffel Kulesi ve bahçeler.", "description_en": "Mini Eiffel Tower and gardens."},
        {"name": "Lennon Wall", "category": "Manzara", "tags": ["graffiti", "beatles", "art"], "lat": 50.0862, "lng": 14.4068, "rating": 4.5, "description": "Beatles şarkıları ve graffitilerle dolu duvar.", "description_en": "Wall covered with Beatles lyrics and graffiti."},
        {"name": "Dancing House", "category": "Manzara", "tags": ["architecture", "modern", "gehry"], "lat": 50.0760, "lng": 14.4135, "rating": 4.4, "description": "Frank Gehry tasarımı post-modern bina.", "description_en": "Post-modern building designed by Frank Gehry."},
        {"name": "Vyšehrad", "category": "Tarihi", "tags": ["fortress", "views", "cemetery"], "lat": 50.0645, "lng": 14.4175, "rating": 4.6, "description": "Tarihi kale ve ünlüler mezarlığı.", "description_en": "Historic fortress and celebrity cemetery."},
        # MUSEUMS
        {"name": "National Gallery", "category": "Müze", "tags": ["art", "collections", "palaces"], "lat": 50.0905, "lng": 14.4010, "rating": 4.5, "description": "Birden fazla sarayda dağıtılan sanat koleksiyonları.", "description_en": "Art collections spread across multiple palaces."},
        {"name": "Museum of Communism", "category": "Müze", "tags": ["history", "soviet", "cold war"], "lat": 50.0850, "lng": 14.4280, "rating": 4.4, "description": "Komünist dönem tarihi ve günlük yaşam.", "description_en": "Communist era history and daily life."},
        {"name": "Franz Kafka Museum", "category": "Müze", "tags": ["kafka", "literature", "interactive"], "lat": 50.0880, "lng": 14.4095, "rating": 4.4, "description": "Kafkaesk atmosferde yazar müzesi.", "description_en": "Writer's museum in Kafkaesque atmosphere."},
        # RESTAURANTS
        {"name": "Lokál Dlouhááá", "category": "Restoran", "tags": ["beer", "czech food", "local"], "lat": 50.0908, "lng": 14.4228, "rating": 4.7, "description": "En taze Çek birası ve ev yemekleri.", "description_en": "Freshest Czech beer and home cooking."},
        {"name": "U Fleků", "category": "Restoran", "tags": ["brewery", "historic", "dark beer"], "lat": 50.0795, "lng": 14.4175, "rating": 4.5, "description": "1499'dan beri bira üreten tarihi birahane.", "description_en": "Historic brewery producing beer since 1499."},
        {"name": "Kantýna", "category": "Restoran", "tags": ["modern", "czech", "casual"], "lat": 50.0832, "lng": 14.4265, "rating": 4.5, "description": "Modern yorumda Çek mutfağı.", "description_en": "Czech cuisine with modern interpretation."},
        {"name": "Field", "category": "Restoran", "tags": ["michelin", "scandinavian", "creative"], "lat": 50.0875, "lng": 14.4230, "rating": 4.7, "description": "Michelin yıldızlı yaratıcı restoran.", "description_en": "Michelin starred creative restaurant."},
        {"name": "Havelska Koruna", "category": "Restoran", "tags": ["cafeteria", "cheap eats", "authentic"], "lat": 50.0850, "lng": 14.4200, "rating": 4.3, "description": "Uygun fiyatlı geleneksel Çek yemekleri.", "description_en": "Affordable traditional Czech dishes."},
        # CAFES
        {"name": "Cafe Louvre", "category": "Kafe", "tags": ["historic", "kafka", "elegant"], "lat": 50.0820, "lng": 14.4190, "rating": 4.6, "description": "Kafka ve Einstein'ın uğrak yeri.", "description_en": "Frequented by Kafka and Einstein."},
        {"name": "Cafe Savoy", "category": "Kafe", "tags": ["breakfast", "neo-renaissance", "pastry"], "lat": 50.0815, "lng": 14.4065, "rating": 4.5, "description": "Neo-Rönesans tavan altında kahvaltı.", "description_en": "Breakfast under neo-Renaissance ceiling."},
        {"name": "Kavárna Slavia", "category": "Kafe", "tags": ["river view", "historic", "artists"], "lat": 50.0815, "lng": 14.4140, "rating": 4.4, "description": "Nehir manzaralı sanatçıların kafesi.", "description_en": "Artists' cafe with river view."},
        # NIGHTLIFE
        {"name": "Hemingway Bar", "category": "Kafe", "tags": ["cocktails", "speakeasy", "intimate"], "lat": 50.0862, "lng": 14.4180, "rating": 4.7, "description": "Dünyanın en iyi kokteyl barlarından biri.", "description_en": "One of the world's best cocktail bars."},
    ],
}

def enrich_cities():
    base_dir = "assets/cities"
    
    for city_key, places in enrichment_data.items():
        filepath = os.path.join(base_dir, f"{city_key}.json")
        
        if not os.path.exists(filepath):
            print(f"⚠️ {filepath} bulunamadı, atlanıyor...")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        existing_names = set(h['name'].lower() for h in data.get('highlights', []))
        added = 0
        
        for place in places:
            if place['name'].lower() not in existing_names:
                place_entry = place.copy()
                place_entry["imageUrl"] = "https://images.unsplash.com/photo-1543783232-af412b852fc7?w=800"
                place_entry["price"] = "medium"
                place_entry["distanceFromCenter"] = 1.0
                place_entry["bestTime"] = "09:00 - 18:00"
                place_entry["bestTime_en"] = "09:00 - 18:00"
                place_entry["tips"] = "Erken gitmekte fayda var."
                place_entry["tips_en"] = "Better to go early."
                
                data['highlights'].append(place_entry)
                added += 1
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ {city_key}: {added} yeni yer eklendi (Toplam: {len(data['highlights'])})")

if __name__ == "__main__":
    enrich_cities()
