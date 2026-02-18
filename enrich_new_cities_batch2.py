import json
import os

# BATCH 2: Matera, Giethoorn, Kotor, Colmar

enrichment_data = {
    "matera": [
        # HISTORIC SITES
        {"name": "Sassi di Matera", "category": "Tarihi", "tags": ["caves", "unesco", "ancient"], "lat": 40.6664, "lng": 16.6043, "rating": 4.9, "description": "9000 yıllık mağara evler bölgesi, UNESCO Mirası.", "description_en": "9000-year-old cave dwellings district, UNESCO Heritage."},
        {"name": "Matera Cathedral", "category": "Tarihi", "tags": ["cathedral", "romanesque", "hilltop"], "lat": 40.6668, "lng": 16.6112, "rating": 4.7, "description": "13. yüzyıl Romanesk katedrali, şehrin en yüksek noktası.", "description_en": "13th century Romanesque cathedral, city's highest point."},
        {"name": "Palombaro Lungo", "category": "Tarihi", "tags": ["cistern", "underground", "water"], "lat": 40.6660, "lng": 16.6075, "rating": 4.8, "description": "Piazza Vittorio Veneto altında devasa yeraltı su sarnıcı.", "description_en": "Massive underground water cistern beneath Piazza Vittorio Veneto."},
        {"name": "San Pietro Caveoso", "category": "Tarihi", "tags": ["church", "rock", "cave"], "lat": 40.6630, "lng": 16.6150, "rating": 4.6, "description": "Kayalara oyulmuş atmosferik mağara kilisesi.", "description_en": "Atmospheric rock-hewn cave church."},
        {"name": "Madonna de Idris", "category": "Tarihi", "tags": ["rock church", "frescoes", "views"], "lat": 40.6625, "lng": 16.6145, "rating": 4.7, "description": "Bizans freskleriyle süslü kaya kilisesi.", "description_en": "Rock church decorated with Byzantine frescoes."},
        {"name": "San Giovanni Battista", "category": "Tarihi", "tags": ["church", "norman", "medieval"], "lat": 40.6680, "lng": 16.6050, "rating": 4.4, "description": "12. yüzyıl Norman mimarisi kilisesi.", "description_en": "12th century Norman architecture church."},
        {"name": "Tramontano Castle", "category": "Tarihi", "tags": ["castle", "ruins", "history"], "lat": 40.6690, "lng": 16.6020, "rating": 4.3, "description": "Yarım kalmış ortaçağ kalesi kalıntıları.", "description_en": "Unfinished medieval castle ruins."},
        {"name": "Church of Santa Lucia alle Malve", "category": "Tarihi", "tags": ["convent", "frescoes", "benedictine"], "lat": 40.6640, "lng": 16.6140, "rating": 4.5, "description": "Benediktin rahibelerin mağara manastırı.", "description_en": "Benedictine nuns' cave convent."},
        # MUSEUMS
        {"name": "Casa Grotta nei Sassi", "category": "Müze", "tags": ["cave house", "life", "recreated"], "lat": 40.6630, "lng": 16.6130, "rating": 4.6, "description": "Mobilyalarıyla restore edilmiş otantik mağara evi.", "description_en": "Authentically furnished restored cave house."},
        {"name": "MUSMA", "category": "Müze", "tags": ["sculpture", "contemporary", "cave museum"], "lat": 40.6670, "lng": 16.6120, "rating": 4.7, "description": "Mağara içinde çağdaş heykel sanatı müzesi.", "description_en": "Contemporary sculpture museum inside caves."},
        {"name": "Museo Ridola", "category": "Müze", "tags": ["archaeology", "prehistory", "artifacts"], "lat": 40.6655, "lng": 16.6100, "rating": 4.5, "description": "Bölgenin tarih öncesi arkeolojik buluntuları.", "description_en": "Prehistoric archaeological finds of the region."},
        {"name": "Casa Noha", "category": "Müze", "tags": ["multimedia", "history", "storytelling"], "lat": 40.6645, "lng": 16.6095, "rating": 4.6, "description": "Matera tarihini anlatan multimedya deneyimi.", "description_en": "Multimedia experience telling Matera's history."},
        {"name": "Museo della Civiltà Contadina", "category": "Müze", "tags": ["rural life", "ethnography", "tools"], "lat": 40.6635, "lng": 16.6125, "rating": 4.3, "description": "Geleneksel köy yaşamı ve tarım aletleri.", "description_en": "Traditional rural life and farming tools."},
        # VIEWPOINTS
        {"name": "Belvedere di Murgia Timone", "category": "Manzara", "tags": ["viewpoint", "panorama", "hiking"], "lat": 40.6645, "lng": 16.6190, "rating": 4.9, "description": "Sassiler'e karşı tepenin en iyi manzara noktası.", "description_en": "Best viewpoint from opposite hill facing the Sassi."},
        {"name": "Piazzetta Pascoli", "category": "Manzara", "tags": ["terrace", "sunset", "photo spot"], "lat": 40.6650, "lng": 16.6080, "rating": 4.8, "description": "Gün batımı için mükemmel teras manzarası.", "description_en": "Perfect terrace view for sunset."},
        {"name": "Via Madonna delle Virtù", "category": "Manzara", "tags": ["street", "scenic", "walk"], "lat": 40.6655, "lng": 16.6110, "rating": 4.6, "description": "Tarihi sokakta yürüyüş ve fotoğraf noktaları.", "description_en": "Walk and photo spots on historic street."},
        # PARKS & NATURE
        {"name": "Parco della Murgia Materana", "category": "Park", "tags": ["national park", "rock churches", "nature"], "lat": 40.6650, "lng": 16.6200, "rating": 4.8, "description": "150+ kaya kilisesi barındıran doğa parkı.", "description_en": "Nature park home to 150+ rock churches."},
        {"name": "Gravina di Matera", "category": "Park", "tags": ["canyon", "gorge", "wildlife"], "lat": 40.6600, "lng": 16.6180, "rating": 4.7, "description": "Şehrin hemen yanındaki dramatik kanyon.", "description_en": "Dramatic canyon right next to the city."},
        # RESTAURANTS
        {"name": "Ristorante Francesca", "category": "Restoran", "tags": ["local", "orecchiette", "cave"], "lat": 40.6655, "lng": 16.6105, "rating": 4.7, "description": "Mağara içinde yöresel Orecchiette makarnası.", "description_en": "Local Orecchiette pasta inside a cave."},
        {"name": "Baccanti", "category": "Restoran", "tags": ["fine dining", "creative", "wine"], "lat": 40.6660, "lng": 16.6085, "rating": 4.8, "description": "Yaratıcı Güney İtalyan mutfağı ve şarap.", "description_en": "Creative Southern Italian cuisine and wine."},
        {"name": "Oi Marì", "category": "Restoran", "tags": ["trattoria", "homemade", "terrace"], "lat": 40.6650, "lng": 16.6095, "rating": 4.6, "description": "Ev yapımı makarna ve terastan manzara.", "description_en": "Homemade pasta and terrace views."},
        {"name": "Soul Kitchen", "category": "Restoran", "tags": ["modern", "tasting menu", "intimate"], "lat": 40.6645, "lng": 16.6088, "rating": 4.7, "description": "Tadım menüsü sunan modern Güney mutfağı.", "description_en": "Modern Southern cuisine with tasting menu."},
        {"name": "Trattoria Lucana", "category": "Restoran", "tags": ["traditional", "cheap eats", "local"], "lat": 40.6640, "lng": 16.6100, "rating": 4.5, "description": "Uygun fiyatlı geleneksel yöresel yemekler.", "description_en": "Affordable traditional local dishes."},
        {"name": "La Lopa", "category": "Restoran", "tags": ["focaccia", "street food", "budget"], "lat": 40.6655, "lng": 16.6070, "rating": 4.8, "description": "Ünlü Materan focacciası burada yenir.", "description_en": "Famous Materan focaccia is eaten here."},
        # CAFES & BARS
        {"name": "Area 8", "category": "Kafe", "tags": ["bar", "cocktails", "film set"], "lat": 40.6640, "lng": 16.6110, "rating": 4.6, "description": "Film seti gibi atmosferde kokteyl bar.", "description_en": "Cocktail bar with film set atmosphere."},
        {"name": "Zia Bruna", "category": "Kafe", "tags": ["panzerotti", "street food", "quick"], "lat": 40.6665, "lng": 16.6090, "rating": 4.8, "description": "Efsanevi panzerotti (kızarmış calzone).", "description_en": "Legendary panzerotti (fried calzone)."},
        {"name": "19a Buca Winery", "category": "Kafe", "tags": ["wine", "cellar", "local wines"], "lat": 40.6648, "lng": 16.6108, "rating": 4.7, "description": "Mağara şarap mahzeninde yerel şarap tadımı.", "description_en": "Local wine tasting in cave wine cellar."},
        {"name": "Caffè Tripoli", "category": "Kafe", "tags": ["coffee", "historic", "central"], "lat": 40.6658, "lng": 16.6082, "rating": 4.4, "description": "Merkezi meydanda tarihi kahve molası.", "description_en": "Historic coffee break in central square."},
        # EXPERIENCES
        {"name": "Cave Hotel Stay", "category": "Deneyim", "tags": ["unique stay", "sassi", "romantic"], "lat": 40.6635, "lng": 16.6135, "rating": 4.9, "description": "Otantik Sassi mağara otelinde konaklama.", "description_en": "Stay in authentic Sassi cave hotel."},
        {"name": "Cooking Class", "category": "Deneyim", "tags": ["cooking", "pasta", "local cuisine"], "lat": 40.6642, "lng": 16.6102, "rating": 4.7, "description": "Orecchiette yapımı öğrenin.", "description_en": "Learn to make Orecchiette."},
        {"name": "James Bond Set Tour", "category": "Deneyim", "tags": ["film", "007", "guided"], "lat": 40.6660, "lng": 16.6045, "rating": 4.5, "description": "No Time to Die film çekim lokasyonları turu.", "description_en": "No Time to Die filming locations tour."},
    ],
    "giethoorn": [
        # WATERWAYS & NATURE
        {"name": "Giethoorn Canals", "category": "Manzara", "tags": ["canals", "boat", "iconic"], "lat": 52.7400, "lng": 6.0800, "rating": 4.9, "description": "Köyün ana caddeleri olan huzurlu kanallar.", "description_en": "The village's main streets - peaceful canals."},
        {"name": "Bovenwijde Lake", "category": "Park", "tags": ["lake", "sailing", "nature"], "lat": 52.7350, "lng": 6.0900, "rating": 4.7, "description": "Yelken ve kano için geniş göl.", "description_en": "Large lake for sailing and canoeing."},
        {"name": "Weerribben-Wieden National Park", "category": "Park", "tags": ["national park", "wetlands", "birds"], "lat": 52.7500, "lng": 6.0500, "rating": 4.8, "description": "Kuzeybatı Avrupa'nın en büyük bataklık alanı.", "description_en": "Northwestern Europe's largest peat marsh area."},
        {"name": "Reed Islands", "category": "Park", "tags": ["islands", "nature", "peace"], "lat": 52.7420, "lng": 6.0820, "rating": 4.6, "description": "Kanallar arasında doğal saz adaları.", "description_en": "Natural reed islands among the canals."},
        {"name": "Boating Trail North", "category": "Manzara", "tags": ["boat route", "scenic", "quiet"], "lat": 52.7450, "lng": 6.0830, "rating": 4.7, "description": "Kuzey yönünde sakin tekne rotası.", "description_en": "Quiet boat route heading north."},
        {"name": "Boating Trail South", "category": "Manzara", "tags": ["boat route", "lake access", "popular"], "lat": 52.7380, "lng": 6.0850, "rating": 4.6, "description": "Göle çıkan güney tekne rotası.", "description_en": "Southern boat route leading to the lake."},
        {"name": "Sunset Viewing Spot", "category": "Manzara", "tags": ["sunset", "peaceful", "photography"], "lat": 52.7395, "lng": 6.0810, "rating": 4.8, "description": "Gün batımını izlemek için en iyi nokta.", "description_en": "Best spot for watching sunset."},
        # MUSEUMS & CULTURE
        {"name": "Museum Giethoorn 't Olde Maat Uus", "category": "Müze", "tags": ["history", "farm life", "local"], "lat": 52.7420, "lng": 6.0820, "rating": 4.6, "description": "Eski çiftlik yaşamını anlatan açık hava müzesi.", "description_en": "Open-air museum showing old farm life."},
        {"name": "De Oude Aarde", "category": "Müze", "tags": ["gemstones", "minerals", "rocks"], "lat": 52.7375, "lng": 6.0790, "rating": 4.5, "description": "Değerli taşlar ve mineraller koleksiyonu.", "description_en": "Collection of gemstones and minerals."},
        {"name": "Histomobil", "category": "Müze", "tags": ["cars", "vintage", "antique"], "lat": 52.7355, "lng": 6.0870, "rating": 4.4, "description": "Antika otomobil ve motorsiklet koleksiyonu.", "description_en": "Antique car and motorcycle collection."},
        {"name": "Gloria Maris Schelpengalerie", "category": "Müze", "tags": ["shells", "sea", "collection"], "lat": 52.7390, "lng": 6.0800, "rating": 4.4, "description": "Dünyanın dört bir yanından deniz kabukları.", "description_en": "Seashells from around the world."},
        {"name": "Kaasboerderij de Derde Mijl", "category": "Deneyim", "tags": ["cheese", "farm", "tasting"], "lat": 52.7430, "lng": 6.0750, "rating": 4.6, "description": "Peynir çiftliğinde tadım ve üretim izleme.", "description_en": "Cheese tasting and production viewing at farm."},
        # ACTIVITIES
        {"name": "Fietspad Bike Path", "category": "Manzara", "tags": ["cycling", "path", "scenic"], "lat": 52.7380, "lng": 6.0850, "rating": 4.7, "description": "Kanalların yanından giden ünlü bisiklet yolu.", "description_en": "Famous bike path along the canals."},
        {"name": "Whisper Boat Rental", "category": "Deneyim", "tags": ["boat rental", "electric", "quiet"], "lat": 52.7405, "lng": 6.0795, "rating": 4.8, "description": "Sessiz elektrikli tekne kiralama.", "description_en": "Quiet electric boat rental."},
        {"name": "Punter Boat Tour", "category": "Deneyim", "tags": ["guided tour", "traditional", "punter"], "lat": 52.7410, "lng": 6.0805, "rating": 4.7, "description": "Geleneksel kayıkla rehberli kanal turu.", "description_en": "Guided canal tour with traditional punter."},
        {"name": "Kayak & Canoe Rental", "category": "Deneyim", "tags": ["kayak", "canoe", "active"], "lat": 52.7395, "lng": 6.0815, "rating": 4.6, "description": "Kano ve kayak kiralama noktası.", "description_en": "Kayak and canoe rental point."},
        {"name": "Ice Skating", "category": "Deneyim", "tags": ["winter", "skating", "canal"], "lat": 52.7400, "lng": 6.0800, "rating": 4.8, "description": "Kış aylarında donan kanallarda buz pateni.", "description_en": "Ice skating on frozen canals in winter."},
        # RESTAURANTS
        {"name": "Smit's Paviljoen", "category": "Restoran", "tags": ["lake view", "traditional", "lunch"], "lat": 52.7340, "lng": 6.0880, "rating": 4.5, "description": "Göl kenarında harika manzaralı restoran.", "description_en": "Restaurant with great lake view."},
        {"name": "De Lindenhof", "category": "Restoran", "tags": ["michelin", "fine dining", "luxury"], "lat": 52.7450, "lng": 6.0750, "rating": 4.9, "description": "2 Michelin yıldızlı üst düzey gastronomi.", "description_en": "2 Michelin star high-end gastronomy."},
        {"name": "Restaurant Hollands Venetië", "category": "Restoran", "tags": ["dutch", "pancakes", "canal view"], "lat": 52.7398, "lng": 6.0802, "rating": 4.4, "description": "Hollanda yemekleri ve dev pannenkoeken.", "description_en": "Dutch dishes and giant pancakes."},
        {"name": "De Otters", "category": "Restoran", "tags": ["terrace", "casual", "snacks"], "lat": 52.7385, "lng": 6.0795, "rating": 4.3, "description": "Kanal kenarında rahat atıştırmalıklar.", "description_en": "Casual snacks by the canal."},
        {"name": "Restaurant't Achterhuus", "category": "Restoran", "tags": ["farm", "local", "cozy"], "lat": 52.7415, "lng": 6.0825, "rating": 4.5, "description": "Çiftlik atmosferinde yerel lezzetler.", "description_en": "Local flavors in farm atmosphere."},
        # CAFES
        {"name": "Grand Café Fanfare", "category": "Kafe", "tags": ["cafe", "famous", "movie set"], "lat": 52.7410, "lng": 6.0815, "rating": 4.6, "description": "Ünlü Hollanda filmine konu olmuş tarihi kafe.", "description_en": "Historic cafe featured in famous Dutch film."},
        {"name": "Gebroeders Pilsner", "category": "Kafe", "tags": ["beer", "terrace", "view"], "lat": 52.7392, "lng": 6.0808, "rating": 4.4, "description": "Kanal manzaralı bira bahçesi.", "description_en": "Beer garden with canal view."},
        {"name": "Ijssalon 't Olde Huis", "category": "Kafe", "tags": ["ice cream", "homemade", "treats"], "lat": 52.7388, "lng": 6.0792, "rating": 4.7, "description": "El yapımı dondurmalar ve tatlılar.", "description_en": "Homemade ice cream and treats."},
        # SHOPPING
        {"name": "Giethoorn Village Shops", "category": "Alışveriş", "tags": ["souvenirs", "local crafts", "gifts"], "lat": 52.7402, "lng": 6.0798, "rating": 4.3, "description": "Hediyelik eşya ve el sanatları dükkanları.", "description_en": "Souvenir and handicraft shops."},
        {"name": "Clogs Workshop", "category": "Deneyim", "tags": ["clogs", "demonstration", "dutch"], "lat": 52.7395, "lng": 6.0805, "rating": 4.5, "description": "Geleneksel tahta ayakkabı yapımı gösterisi.", "description_en": "Traditional wooden shoe making demonstration."},
    ],
    "kotor": [
        # HISTORIC SITES
        {"name": "Kotor Old Town", "category": "Tarihi", "tags": ["unesco", "medieval", "streets"], "lat": 42.4245, "lng": 18.7715, "rating": 4.8, "description": "UNESCO korumasındaki ortaçağ surlu şehri.", "description_en": "UNESCO protected medieval walled city."},
        {"name": "Castle of San Giovanni", "category": "Manzara", "tags": ["hike", "fortress", "panorama"], "lat": 42.4230, "lng": 18.7760, "rating": 4.9, "description": "1350 basamakla tırmanılan efsanevi kale ve manzara.", "description_en": "Legendary castle reached by climbing 1350 steps."},
        {"name": "Cathedral of Saint Tryphon", "category": "Tarihi", "tags": ["cathedral", "romanesque", "icon"], "lat": 42.4238, "lng": 18.7725, "rating": 4.7, "description": "12. yüzyıl Romanesk katedrali, şehrin simgesi.", "description_en": "12th century Romanesque cathedral, city's symbol."},
        {"name": "Maritime Museum", "category": "Müze", "tags": ["navy", "history", "palace"], "lat": 42.4248, "lng": 18.7720, "rating": 4.5, "description": "Grgurina Sarayı'nda denizcilik tarihi.", "description_en": "Maritime history in Grgurina Palace."},
        {"name": "Cats Museum", "category": "Müze", "tags": ["quirky", "cats", "art"], "lat": 42.4252, "lng": 18.7710, "rating": 4.4, "description": "Kotor'un meşhur kedilerine adanmış müze.", "description_en": "Museum dedicated to Kotor's famous cats."},
        {"name": "Church of St. Luke", "category": "Tarihi", "tags": ["church", "orthodox", "small"], "lat": 42.4242, "lng": 18.7712, "rating": 4.5, "description": "12. yüzyıldan kalma küçük Ortodoks kilisesi.", "description_en": "Small Orthodox church from 12th century."},
        {"name": "Church of St. Nicholas", "category": "Tarihi", "tags": ["orthodox", "20th century", "central"], "lat": 42.4250, "lng": 18.7718, "rating": 4.4, "description": "20. yüzyıl Sırp Ortodoks kilisesi.", "description_en": "20th century Serbian Orthodox church."},
        {"name": "Main Gate (Sea Gate)", "category": "Tarihi", "tags": ["gate", "entrance", "landmark"], "lat": 42.4260, "lng": 18.7700, "rating": 4.6, "description": "Surlu şehrin ana deniz kapısı.", "description_en": "Main sea gate of the walled city."},
        {"name": "River Gate (North Gate)", "category": "Tarihi", "tags": ["gate", "river", "medieval"], "lat": 42.4268, "lng": 18.7695, "rating": 4.4, "description": "Shkurda nehrinin yanındaki kuzey kapısı.", "description_en": "Northern gate by Shkurda river."},
        {"name": "Gurdic Gate (South Gate)", "category": "Tarihi", "tags": ["gate", "springs", "quiet"], "lat": 42.4220, "lng": 18.7720, "rating": 4.3, "description": "Güney kapısı ve doğal pınarlar.", "description_en": "Southern gate and natural springs."},
        {"name": "Kampana Tower", "category": "Tarihi", "tags": ["tower", "clock", "walls"], "lat": 42.4265, "lng": 18.7695, "rating": 4.6, "description": "Saat kulesi ve savunma burçları.", "description_en": "Clock tower and defense bastions."},
        {"name": "Plaza of Arms", "category": "Manzara", "tags": ["square", "central", "cafes"], "lat": 42.4255, "lng": 18.7712, "rating": 4.5, "description": "Ana meydan, kafeler ve buluşma noktası.", "description_en": "Main square, cafes and meeting point."},
        # VIEWPOINTS
        {"name": "San Giovanni Fortress View", "category": "Manzara", "tags": ["view", "bay", "mountains"], "lat": 42.4235, "lng": 18.7758, "rating": 4.9, "description": "Körfez ve dağların en iyi panoraması.", "description_en": "Best panorama of bay and mountains."},
        {"name": "Church of Our Lady of Remedy", "category": "Manzara", "tags": ["chapel", "halfway", "rest"], "lat": 42.4232, "lng": 18.7745, "rating": 4.6, "description": "Kaleye tırmanırken mola için şapel.", "description_en": "Chapel for resting while climbing to castle."},
        # RESTAURANTS
        {"name": "Galion", "category": "Restoran", "tags": ["seafood", "view", "upscale"], "lat": 42.4210, "lng": 18.7735, "rating": 4.8, "description": "Su kenarında, kale manzaralı şık balık restoranı.", "description_en": "Elegant fish restaurant by water with castle view."},
        {"name": "BBQ Tanjga", "category": "Restoran", "tags": ["meat", "grill", "budget"], "lat": 42.4205, "lng": 18.7705, "rating": 4.7, "description": "Bol porsiyonlu uygun fiyatlı ızgaracı.", "description_en": "Generous portions at budget-friendly grill."},
        {"name": "Konoba Scala Santa", "category": "Restoran", "tags": ["traditional", "local", "cozy"], "lat": 42.4240, "lng": 18.7710, "rating": 4.6, "description": "Karadağ geleneksel yemekleri.", "description_en": "Traditional Montenegrin dishes."},
        {"name": "Cesarica", "category": "Restoran", "tags": ["pizza", "pasta", "italian"], "lat": 42.4248, "lng": 18.7715, "rating": 4.5, "description": "Odun fırınında İtalyan pizzası.", "description_en": "Wood-fired Italian pizza."},
        {"name": "Bastion", "category": "Restoran", "tags": ["fine dining", "sea", "romantic"], "lat": 42.4235, "lng": 18.7730, "rating": 4.7, "description": "Romantik akşam yemeği için deniz kenarı.", "description_en": "Seaside for romantic dinner."},
        {"name": "Old Winery", "category": "Restoran", "tags": ["wine", "local wines", "balkan"], "lat": 42.4246, "lng": 18.7708, "rating": 4.5, "description": "Karadağ şarapları ve mezeler.", "description_en": "Montenegrin wines and appetizers."},
        # CAFES
        {"name": "Forza Cafe", "category": "Kafe", "tags": ["dessert", "coffee", "square"], "lat": 42.4242, "lng": 18.7712, "rating": 4.5, "description": "Şehrin en iyi Kotor pastası (Krempita).", "description_en": "City's best Kotor cake (Krempita)."},
        {"name": "Bandiera", "category": "Kafe", "tags": ["waterfront", "cocktails", "sunset"], "lat": 42.4258, "lng": 18.7700, "rating": 4.6, "description": "Gün batımı eşliğinde kokteyl.", "description_en": "Cocktails at sunset."},
        {"name": "Bokun Wine Bar", "category": "Kafe", "tags": ["wine bar", "local", "intimate"], "lat": 42.4244, "lng": 18.7718, "rating": 4.7, "description": "Yerel şarap tadımı için samimi mekan.", "description_en": "Intimate spot for local wine tasting."},
        # SHOPPING
        {"name": "Kotor Bazaar", "category": "Alışveriş", "tags": ["market", "souvenirs", "crafts"], "lat": 42.4255, "lng": 18.7730, "rating": 4.3, "description": "Hediyelik eşyalar ve el sanatları.", "description_en": "Souvenirs and handicrafts."},
        {"name": "Antique Shops", "category": "Alışveriş", "tags": ["antiques", "jewelry", "art"], "lat": 42.4250, "lng": 18.7722, "rating": 4.4, "description": "Antika takı ve sanat eserleri.", "description_en": "Antique jewelry and art pieces."},
        # EXPERIENCES
        {"name": "Bay of Kotor Boat Tour", "category": "Deneyim", "tags": ["boat", "bay", "scenic"], "lat": 42.4260, "lng": 18.7690, "rating": 4.8, "description": "Körfez turunda adalar ve köyler.", "description_en": "Islands and villages on bay tour."},
        {"name": "Cat Feeding Tour", "category": "Deneyim", "tags": ["cats", "unique", "local"], "lat": 42.4245, "lng": 18.7715, "rating": 4.6, "description": "Kotor'un ünlü kedileriyle tanışma.", "description_en": "Meet Kotor's famous cats."},
    ],
    "colmar": [
        # HISTORIC AREAS
        {"name": "La Petite Venise", "category": "Manzara", "tags": ["canals", "photogenic", "iconic"], "lat": 48.0745, "lng": 7.3590, "rating": 4.9, "description": "Renkli evlerin suya yansıdığı en fotojenik bölge.", "description_en": "Most photogenic area with colorful houses reflecting in water."},
        {"name": "Unterlinden Museum", "category": "Müze", "tags": ["art", "isenheim", "medieval"], "lat": 48.0798, "lng": 7.3555, "rating": 4.7, "description": "Ünlü Isenheim Sunağı'nı barındıran sanat müzesi.", "description_en": "Art museum housing the famous Isenheim Altarpiece."},
        {"name": "St Martin's Church", "category": "Tarihi", "tags": ["church", "gothic", "center"], "lat": 48.0775, "lng": 7.3582, "rating": 4.6, "description": "13. yüzyıl gotik kilisesi, şehrin kalbi.", "description_en": "13th century Gothic church, heart of the city."},
        {"name": "Pfister House", "category": "Tarihi", "tags": ["house", "painted", "iconic"], "lat": 48.0780, "lng": 7.3550, "rating": 4.5, "description": "1537 tarihli süslü boyalı ahşap ev.", "description_en": "Ornate painted timber house from 1537."},
        {"name": "Koïfhus", "category": "Tarihi", "tags": ["customs house", "medieval", "market"], "lat": 48.0755, "lng": 7.3585, "rating": 4.6, "description": "15. yüzyıl eski gümrük binası.", "description_en": "15th century old customs house."},
        {"name": "Maison des Têtes", "category": "Tarihi", "tags": ["facade", "heads", "renaissance"], "lat": 48.0790, "lng": 7.3560, "rating": 4.6, "description": "111 kafayla süslü Rönesans cephesi.", "description_en": "Renaissance facade decorated with 111 heads."},
        {"name": "Dominican Church", "category": "Tarihi", "tags": ["church", "virgin", "art"], "lat": 48.0785, "lng": 7.3575, "rating": 4.5, "description": "Schongauer'in Madonna tablosuna ev sahipliği yapar.", "description_en": "Houses Schongauer's Madonna painting."},
        {"name": "Tanners' Quarter", "category": "Manzara", "tags": ["historic", "timber", "walk"], "lat": 48.0750, "lng": 7.3580, "rating": 4.7, "description": "Eski tabakhanelerin bulunduğu tarihi sokak.", "description_en": "Historic street with old tanneries."},
        {"name": "Fishmonger's District", "category": "Manzara", "tags": ["quay", "river", "charm"], "lat": 48.0748, "lng": 7.3588, "rating": 4.6, "description": "Balıkçı evlerinin olduğu kanal kenarı.", "description_en": "Canalside with fishermen's houses."},
        # MUSEUMS
        {"name": "Bartholdi Museum", "category": "Müze", "tags": ["sculptor", "statue of liberty", "art"], "lat": 48.0772, "lng": 7.3565, "rating": 4.5, "description": "Özgürlük Heykeli'nin yaratıcısının doğduğu ev.", "description_en": "Birthplace of the Statue of Liberty creator."},
        {"name": "Toy Museum", "category": "Müze", "tags": ["toys", "kids", "vintage"], "lat": 48.0785, "lng": 7.3530, "rating": 4.5, "description": "Her yaştan çocuğa hitap eden oyuncak müzesi.", "description_en": "Toy museum appealing to all ages."},
        {"name": "Marché couvert", "category": "Alışveriş", "tags": ["market", "food", "local"], "lat": 48.0740, "lng": 7.3595, "rating": 4.4, "description": "Kapal çarşı ve yerel ürünler.", "description_en": "Covered market and local products."},
        {"name": "Natural History Museum", "category": "Müze", "tags": ["nature", "animals", "geology"], "lat": 48.0788, "lng": 7.3540, "rating": 4.3, "description": "Bölgenin doğal tarihi ve jeolojisi.", "description_en": "Natural history and geology of the region."},
        # RESTAURANTS
        {"name": "JY's", "category": "Restoran", "tags": ["michelin", "fine dining", "creative"], "lat": 48.0750, "lng": 7.3588, "rating": 4.8, "description": "2 Michelin yıldızlı yaratıcı mutfak.", "description_en": "2 Michelin star creative cuisine."},
        {"name": "Wistub Brenner", "category": "Restoran", "tags": ["alsatian", "choucroute", "cozy"], "lat": 48.0748, "lng": 7.3582, "rating": 4.6, "description": "Geleneksel Alsace yemekleri ve şarap.", "description_en": "Traditional Alsatian dishes and wine."},
        {"name": "Le Fer Rouge", "category": "Restoran", "tags": ["traditional", "tarte flambée", "wine"], "lat": 48.0770, "lng": 7.3575, "rating": 4.5, "description": "Flammekueche (Alsace pizzası) için ideal.", "description_en": "Ideal for Flammekueche (Alsatian pizza)."},
        {"name": "Aux Armes de Colmar", "category": "Restoran", "tags": ["historic", "foie gras", "elegant"], "lat": 48.0765, "lng": 7.3570, "rating": 4.6, "description": "Tarihi binada zarif Alsace mutfağı.", "description_en": "Elegant Alsatian cuisine in historic building."},
        {"name": "La Table du Brocanteur", "category": "Restoran", "tags": ["antique", "unique", "french"], "lat": 48.0758, "lng": 7.3565, "rating": 4.5, "description": "Antika dükkânı atmosferinde Fransız yemekleri.", "description_en": "French dishes in antique shop atmosphere."},
        {"name": "Schwendi Bier-und Weinstub", "category": "Restoran", "tags": ["beer hall", "local", "lively"], "lat": 48.0755, "lng": 7.3585, "rating": 4.4, "description": "Canlı atmosferde bira ve yöresel yemek.", "description_en": "Beer and local food in lively atmosphere."},
        # CAFES & BAKERIES
        {"name": "Au Croissant Doré", "category": "Kafe", "tags": ["bakery", "breakfast", "pastry"], "lat": 48.0760, "lng": 7.3570, "rating": 4.7, "description": "Eski tarz Fransız pastanesi.", "description_en": "Old-style French pastry shop."},
        {"name": "Gilg", "category": "Kafe", "tags": ["patisserie", "chocolate", "macarons"], "lat": 48.0768, "lng": 7.3568, "rating": 4.6, "description": "El yapımı çikolata ve makaronlar.", "description_en": "Handmade chocolates and macarons."},
        {"name": "Salon de Thé Un Moment à Colmar", "category": "Kafe", "tags": ["tea room", "cakes", "elegant"], "lat": 48.0762, "lng": 7.3572, "rating": 4.5, "description": "Zarif çay salonu ve pastalar.", "description_en": "Elegant tea room and pastries."},
        {"name": "Fénelon Café", "category": "Kafe", "tags": ["coffee", "terrace", "people watching"], "lat": 48.0755, "lng": 7.3582, "rating": 4.4, "description": "Meydanda kahve ve insanları izleme.", "description_en": "Coffee and people watching in the square."},
        # WINE & EXPERIENCES
        {"name": "Alsace Wine Route Start", "category": "Deneyim", "tags": ["wine", "route", "tour"], "lat": 48.0800, "lng": 7.3550, "rating": 4.8, "description": "Alsace Şarap Yolu'nun başlangıç noktası.", "description_en": "Starting point of Alsace Wine Route."},
        {"name": "Wine Tasting Cellars", "category": "Deneyim", "tags": ["wine", "tasting", "riesling"], "lat": 48.0775, "lng": 7.3560, "rating": 4.7, "description": "Yerel şarap mahzenlerinde tadım.", "description_en": "Tasting in local wine cellars."},
        {"name": "Christmas Market", "category": "Deneyim", "tags": ["seasonal", "christmas", "festive"], "lat": 48.0770, "lng": 7.3578, "rating": 4.9, "description": "Avrupa'nın en güzel Noel pazarlarından biri.", "description_en": "One of Europe's most beautiful Christmas markets."},
        {"name": "Boat Ride on Lauch", "category": "Deneyim", "tags": ["boat", "petit venise", "romantic"], "lat": 48.0742, "lng": 7.3592, "rating": 4.6, "description": "Petit Venise'de romantik tekne turu.", "description_en": "Romantic boat tour in Petit Venise."},
        # SHOPPING
        {"name": "Rue des Marchands", "category": "Alışveriş", "tags": ["shopping street", "boutiques", "souvenirs"], "lat": 48.0765, "lng": 7.3568, "rating": 4.5, "description": "Ana alışveriş caddesi ve butikler.", "description_en": "Main shopping street and boutiques."},
        {"name": "Hansi Boutique", "category": "Alışveriş", "tags": ["art", "postcards", "alsatian"], "lat": 48.0772, "lng": 7.3562, "rating": 4.4, "description": "Ünlü Alsace illüstratörü Hansi eserleri.", "description_en": "Works by famous Alsatian illustrator Hansi."},
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
