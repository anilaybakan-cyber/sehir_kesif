import json
import os

# BATCH 3: Sintra, San Sebastian, Bologna, Gaziantep

enrichment_data = {
    "sintra": [
        # PALACES & CASTLES
        {"name": "Pena Palace", "category": "Tarihi", "tags": ["palace", "colorful", "hilltop"], "lat": 38.7876, "lng": -9.3906, "rating": 4.8, "description": "Sarı-kırmızı renkli masalsı Romantik saray.", "description_en": "Yellow-red colored fairytale Romantic palace."},
        {"name": "Quinta da Regaleira", "category": "Park", "tags": ["gardens", "mystic", "well"], "lat": 38.7963, "lng": -9.3960, "rating": 4.9, "description": "Gizemli kuyusu ve labirent bahçeleriyle ünlü.", "description_en": "Famous for its mysterious well and labyrinth gardens."},
        {"name": "Moorish Castle", "category": "Tarihi", "tags": ["castle", "walls", "views"], "lat": 38.7926, "lng": -9.3920, "rating": 4.7, "description": "8. yüzyıl Mağribi kalesi surları ve manzarası.", "description_en": "8th century Moorish castle walls and views."},
        {"name": "Sintra National Palace", "category": "Tarihi", "tags": ["palace", "chimneys", "royal"], "lat": 38.7977, "lng": -9.3907, "rating": 4.6, "description": "İkonik devasa mutfak bacalarıyla şehir sarayı.", "description_en": "Town palace with iconic massive kitchen chimneys."},
        {"name": "Monserrate Palace", "category": "Park", "tags": ["exotic", "romantic", "gardens"], "lat": 38.7940, "lng": -9.4180, "rating": 4.8, "description": "Egzotik botanik bahçeler içinde Arap mimarisi.", "description_en": "Arab architecture within exotic botanical gardens."},
        {"name": "Seteais Palace", "category": "Tarihi", "tags": ["hotel", "luxury", "neoclassical"], "lat": 38.7960, "lng": -9.3980, "rating": 4.6, "description": "Lüks otele dönüştürülmüş neoklasik saray.", "description_en": "Neoclassical palace converted to luxury hotel."},
        {"name": "Pena Park", "category": "Park", "tags": ["forest", "trails", "exotic plants"], "lat": 38.7880, "lng": -9.3920, "rating": 4.7, "description": "Pena Sarayı çevresinde 200 hektar orman parkı.", "description_en": "200 hectare forest park around Pena Palace."},
        {"name": "Chalet of Countess d'Edla", "category": "Tarihi", "tags": ["chalet", "alpine", "romantic"], "lat": 38.7895, "lng": -9.3890, "rating": 4.5, "description": "Alp tarzı romantik şale ve bahçesi.", "description_en": "Alpine style romantic chalet and garden."},
        {"name": "Cruz Alta", "category": "Manzara", "tags": ["viewpoint", "highest point", "cross"], "lat": 38.7890, "lng": -9.3880, "rating": 4.6, "description": "Sintra dağlarının en yüksek noktası.", "description_en": "Highest point of Sintra mountains."},
        # NATURE & BEACHES
        {"name": "Cabo da Roca", "category": "Manzara", "tags": ["coast", "westernmost", "cliffs"], "lat": 38.7803, "lng": -9.5005, "rating": 4.7, "description": "Avrupa kıtasının en batı ucu.", "description_en": "Westernmost point of continental Europe."},
        {"name": "Praia das Maçãs", "category": "Park", "tags": ["beach", "family", "tram"], "lat": 38.8240, "lng": -9.4700, "rating": 4.5, "description": "Nostaljik tramvayla ulaşılan aile plajı.", "description_en": "Family beach reachable by nostalgic tram."},
        {"name": "Praia Grande", "category": "Park", "tags": ["beach", "surfing", "big"], "lat": 38.8150, "lng": -9.4750, "rating": 4.6, "description": "Sörf severler için büyük okyanus plajı.", "description_en": "Large ocean beach for surf lovers."},
        {"name": "Azenhas do Mar", "category": "Manzara", "tags": ["cliff village", "swimming pool", "scenic"], "lat": 38.8400, "lng": -9.4600, "rating": 4.8, "description": "Uçuruma tutunmuş köy ve doğal havuz.", "description_en": "Village clinging to cliff and natural pool."},
        {"name": "Capuchos Convent", "category": "Tarihi", "tags": ["convent", "cork", "nature"], "lat": 38.7815, "lng": -9.4300, "rating": 4.5, "description": "Mantar kaplı minyatür keşiş manastırı.", "description_en": "Cork-lined miniature monk monastery."},
        {"name": "Peninha Sanctuary", "category": "Manzara", "tags": ["chapel", "coast views", "remote"], "lat": 38.7750, "lng": -9.4620, "rating": 4.7, "description": "Denize bakan uzak tepe şapeli.", "description_en": "Remote hilltop chapel overlooking the sea."},
        # RESTAURANTS
        {"name": "Incomum", "category": "Restoran", "tags": ["modern", "portuguese", "chef"], "lat": 38.8000, "lng": -9.3890, "rating": 4.7, "description": "Şef Luis Santos'tan yaratıcı Portekiz mutfağı.", "description_en": "Creative Portuguese cuisine by Chef Luis Santos."},
        {"name": "Tascantiga", "category": "Restoran", "tags": ["tapas", "cozy", "wine"], "lat": 38.7970, "lng": -9.3910, "rating": 4.5, "description": "Yerel mezeler ve Portekiz şarapları.", "description_en": "Local appetizers and Portuguese wines."},
        {"name": "Cantinho de São Pedro", "category": "Restoran", "tags": ["seafood", "local", "historic"], "lat": 38.7952, "lng": -9.3945, "rating": 4.6, "description": "Deniz ürünleri ve geleneksel Portekiz yemekleri.", "description_en": "Seafood and traditional Portuguese dishes."},
        {"name": "Nau Palatina", "category": "Restoran", "tags": ["medieval", "themed", "experience"], "lat": 38.7980, "lng": -9.3905, "rating": 4.4, "description": "Ortaçağ temalı yemek deneyimi.", "description_en": "Medieval themed dining experience."},
        {"name": "Dom Pipas", "category": "Restoran", "tags": ["grilled", "meat", "rustic"], "lat": 38.7985, "lng": -9.3915, "rating": 4.5, "description": "Izgara et ve rustik atmosfer.", "description_en": "Grilled meat and rustic atmosphere."},
        # CAFES & SWEETS
        {"name": "Casa Piriquita", "category": "Kafe", "tags": ["pastry", "travesseiros", "famous"], "lat": 38.7965, "lng": -9.3905, "rating": 4.8, "description": "Meşhur 'Travesseiros' tatlısının doğduğu yer.", "description_en": "Birthplace of famous 'Travesseiros' pastry."},
        {"name": "Queijadas da Sapa", "category": "Kafe", "tags": ["cheesecakes", "traditional", "local"], "lat": 38.7958, "lng": -9.3912, "rating": 4.6, "description": "Sintra'nın ünlü peynirli tatlısı Queijadas.", "description_en": "Sintra's famous cheese pastry Queijadas."},
        {"name": "Café Paris", "category": "Kafe", "tags": ["terrace", "central", "people watching"], "lat": 38.7975, "lng": -9.3900, "rating": 4.4, "description": "Saray meydanında teraslı kafe.", "description_en": "Terrace cafe in palace square."},
        {"name": "Fábrica das Verdadeiras Queijadas", "category": "Kafe", "tags": ["historic", "queijadas", "since 1756"], "lat": 38.7968, "lng": -9.3908, "rating": 4.7, "description": "1756'dan beri queijada üreten tarihi dükkan.", "description_en": "Historic shop producing queijadas since 1756."},
        # EXPERIENCES
        {"name": "Sintra Tram", "category": "Deneyim", "tags": ["tram", "historic", "beach"], "lat": 38.7995, "lng": -9.3895, "rating": 4.5, "description": "1904'ten kalma nostaljik tramvayla sahile.", "description_en": "To the beach by nostalgic 1904 tram."},
        {"name": "Horse Carriage Ride", "category": "Deneyim", "tags": ["carriage", "romantic", "tour"], "lat": 38.7978, "lng": -9.3908, "rating": 4.4, "description": "Şehir merkezinde at arabası turu.", "description_en": "Horse carriage tour in town center."},
        {"name": "Wine Tasting in Colares", "category": "Deneyim", "tags": ["wine", "tasting", "local"], "lat": 38.8000, "lng": -9.4500, "rating": 4.6, "description": "Yakın Colares bölgesinde şarap tadımı.", "description_en": "Wine tasting in nearby Colares region."},
        # SHOPPING
        {"name": "Rua das Padarias", "category": "Alışveriş", "tags": ["bakeries", "crafts", "souvenirs"], "lat": 38.7972, "lng": -9.3902, "rating": 4.3, "description": "Fırınlar ve hediyelik eşya dükkanları.", "description_en": "Bakeries and souvenir shops."},
        {"name": "Sintra Artisan Market", "category": "Alışveriş", "tags": ["market", "handmade", "local"], "lat": 38.7980, "lng": -9.3895, "rating": 4.4, "description": "El yapımı sanat ve zanaat ürünleri.", "description_en": "Handmade art and craft products."},
    ],
    "san_sebastian": [
        # BEACHES
        {"name": "La Concha Beach", "category": "Park", "tags": ["beach", "iconic", "promenade"], "lat": 43.3155, "lng": -1.9860, "rating": 4.9, "description": "Avrupa'nın en güzel şehir plajlarından biri.", "description_en": "One of Europe's most beautiful city beaches."},
        {"name": "Zurriola Beach", "category": "Park", "tags": ["surf", "youth", "waves"], "lat": 43.3255, "lng": -1.9750, "rating": 4.6, "description": "Sörfçülerin tercih ettiği dalgalı plaj.", "description_en": "Surfers' preferred wavy beach."},
        {"name": "Ondarreta Beach", "category": "Park", "tags": ["family", "calm", "west"], "lat": 43.3120, "lng": -1.9990, "rating": 4.5, "description": "Aileler için daha sakin batı plajı.", "description_en": "Calmer western beach for families."},
        {"name": "Isla Santa Clara", "category": "Park", "tags": ["island", "boat", "summer"], "lat": 43.3160, "lng": -1.9900, "rating": 4.6, "description": "Yazın tekneyle ulaşılabilen küçük ada.", "description_en": "Small island reachable by boat in summer."},
        # VIEWPOINTS
        {"name": "Monte Igueldo", "category": "Manzara", "tags": ["funicular", "park", "panorama"], "lat": 43.3220, "lng": -2.0050, "rating": 4.7, "description": "Fünikülerle çıkılan körfez panoraması.", "description_en": "Bay panorama reached by funicular."},
        {"name": "Monte Urgull", "category": "Park", "tags": ["castle", "hike", "free"], "lat": 43.3270, "lng": -1.9880, "rating": 4.7, "description": "Şehir merkezinden yürüyerek çıkılabilen tepe.", "description_en": "Hill reachable on foot from city center."},
        {"name": "Peine del Viento", "category": "Manzara", "tags": ["sculpture", "sea", "chillida"], "lat": 43.3225, "lng": -2.0070, "rating": 4.8, "description": "Chillida'nın dalgalarla bütünleşen heykelleri.", "description_en": "Chillida's sculptures integrated with waves."},
        {"name": "Miramar Palace Gardens", "category": "Park", "tags": ["palace", "gardens", "royal"], "lat": 43.3140, "lng": -1.9960, "rating": 4.6, "description": "Kraliyet yazlık sarayının İngiliz bahçeleri.", "description_en": "English gardens of the royal summer palace."},
        # OLD TOWN & CULTURE
        {"name": "Parte Vieja (Old Town)", "category": "Tarihi", "tags": ["pintxos", "bars", "historic"], "lat": 43.3230, "lng": -1.9850, "rating": 4.8, "description": "Pintxos barlarının en yoğun olduğu tarihi bölge.", "description_en": "Historic area densest with pintxos bars."},
        {"name": "San Telmo Museum", "category": "Müze", "tags": ["basque", "history", "art"], "lat": 43.3245, "lng": -1.9840, "rating": 4.6, "description": "Bask kültürü ve tarihi müzesi.", "description_en": "Basque culture and history museum."},
        {"name": "Basilica of Santa Maria", "category": "Tarihi", "tags": ["church", "baroque", "old town"], "lat": 43.3235, "lng": -1.9838, "rating": 4.5, "description": "18. yüzyıl barok kilisesi.", "description_en": "18th century baroque church."},
        {"name": "Aquarium", "category": "Müze", "tags": ["aquarium", "ocean", "family"], "lat": 43.3262, "lng": -1.9825, "rating": 4.5, "description": "Bask Körfezi deniz yaşamı.", "description_en": "Bay of Biscay marine life."},
        {"name": "Kursaal Congress Centre", "category": "Manzara", "tags": ["architecture", "modern", "events"], "lat": 43.3260, "lng": -1.9770, "rating": 4.4, "description": "Rafael Moneo tasarımı modern kongre merkezi.", "description_en": "Modern congress center designed by Rafael Moneo."},
        # PINTXOS & RESTAURANTS
        {"name": "Arzak", "category": "Restoran", "tags": ["3 michelin", "innovative", "world's best"], "lat": 43.3190, "lng": -1.9600, "rating": 4.9, "description": "Dünyanın en iyi restoranlarından, 3 Michelin yıldız.", "description_en": "One of world's best restaurants, 3 Michelin stars."},
        {"name": "Bar Nestor", "category": "Restoran", "tags": ["tortilla", "steak", "legendary"], "lat": 43.3235, "lng": -1.9835, "rating": 4.7, "description": "Efsanevi tortilla ve biftek.", "description_en": "Legendary tortilla and steak."},
        {"name": "La Viña", "category": "Restoran", "tags": ["cheesecake", "pintxos", "original"], "lat": 43.3240, "lng": -1.9845, "rating": 4.9, "description": "San Sebastian Cheesecake'in doğduğu yer.", "description_en": "Birthplace of San Sebastian Cheesecake."},
        {"name": "Gandarias", "category": "Restoran", "tags": ["pintxos", "meat", "quality"], "lat": 43.3232, "lng": -1.9852, "rating": 4.6, "description": "Kaliteli et pintxosları.", "description_en": "Quality meat pintxos."},
        {"name": "Ganbara", "category": "Restoran", "tags": ["mushrooms", "seasonal", "pintxos"], "lat": 43.3228, "lng": -1.9848, "rating": 4.8, "description": "Mevsimsel mantar pintxoslarıyla ünlü.", "description_en": "Famous for seasonal mushroom pintxos."},
        {"name": "Mugaritz", "category": "Restoran", "tags": ["2 michelin", "avant-garde", "experience"], "lat": 43.2800, "lng": -2.0200, "rating": 4.7, "description": "2 Michelin yıldızlı avangard mutfak.", "description_en": "2 Michelin star avant-garde cuisine."},
        {"name": "Txepetxa", "category": "Restoran", "tags": ["anchovies", "pintxos", "specialist"], "lat": 43.3238, "lng": -1.9843, "rating": 4.7, "description": "Hamsi pintxoslarında uzman.", "description_en": "Specialist in anchovy pintxos."},
        {"name": "Bodegón Alejandro", "category": "Restoran", "tags": ["traditional", "basque", "family"], "lat": 43.3248, "lng": -1.9830, "rating": 4.5, "description": "Geleneksel Bask aile restoranı.", "description_en": "Traditional Basque family restaurant."},
        # CAFES & BARS
        {"name": "Café de la Concha", "category": "Kafe", "tags": ["promenade", "views", "elegant"], "lat": 43.3158, "lng": -1.9855, "rating": 4.5, "description": "Sahil kenarında zarif kafe.", "description_en": "Elegant cafe by the promenade."},
        {"name": "La Cepa", "category": "Kafe", "tags": ["wine bar", "ham", "pintxos"], "lat": 43.3230, "lng": -1.9850, "rating": 4.6, "description": "Şarap ve İberiko jamón.", "description_en": "Wine and Iberian ham."},
        {"name": "Atari Gastroteka", "category": "Kafe", "tags": ["modern", "coffee", "brunch"], "lat": 43.3222, "lng": -1.9858, "rating": 4.5, "description": "Modern kafe ve brunch.", "description_en": "Modern cafe and brunch."},
        # EXPERIENCES
        {"name": "Pintxo Tour", "category": "Deneyim", "tags": ["food tour", "guided", "local"], "lat": 43.3235, "lng": -1.9845, "rating": 4.8, "description": "Rehberli pintxo turu.", "description_en": "Guided pintxo tour."},
        {"name": "Surfing Lesson", "category": "Deneyim", "tags": ["surf", "lesson", "zurriola"], "lat": 43.3250, "lng": -1.9755, "rating": 4.6, "description": "Zurriola'da sörf dersi.", "description_en": "Surfing lesson at Zurriola."},
        {"name": "Txakoli Winery Visit", "category": "Deneyim", "tags": ["wine", "local", "txakoli"], "lat": 43.2900, "lng": -2.0100, "rating": 4.7, "description": "Yerel Txakoli şaraphanesi ziyareti.", "description_en": "Visit to local Txakoli winery."},
    ],
    "bologna": [
        # SQUARES & STREETS
        {"name": "Piazza Maggiore", "category": "Manzara", "tags": ["square", "central", "lively"], "lat": 44.4938, "lng": 11.3432, "rating": 4.9, "description": "Bologna'nın kalbi, devasa ve canlı ana meydan.", "description_en": "Heart of Bologna, massive and lively main square."},
        {"name": "Via dell'Indipendenza", "category": "Alışveriş", "tags": ["shopping", "boulevard", "cafes"], "lat": 44.5000, "lng": 11.3440, "rating": 4.5, "description": "Ana alışveriş bulvarı ve kafeler.", "description_en": "Main shopping boulevard and cafes."},
        {"name": "Via Piella", "category": "Manzara", "tags": ["secret window", "canal", "hidden"], "lat": 44.4980, "lng": 11.3470, "rating": 4.7, "description": "Gizli pencereden görülen kanal manzarası.", "description_en": "Canal view from secret window."},
        {"name": "Porticoes of Bologna", "category": "Manzara", "tags": ["unesco", "arcades", "walking"], "lat": 44.4945, "lng": 11.3430, "rating": 4.8, "description": "UNESCO Mirası 40 km'lik revaklar.", "description_en": "UNESCO Heritage 40 km of arcades."},
        # TOWERS & HISTORIC
        {"name": "Two Towers (Due Torri)", "category": "Tarihi", "tags": ["towers", "leaning", "icon"], "lat": 44.4945, "lng": 11.3465, "rating": 4.7, "description": "Şehrin sembolü eğik ikiz kuleler.", "description_en": "City's symbol twin leaning towers."},
        {"name": "San Petronio Basilica", "category": "Tarihi", "tags": ["church", "massive", "gothic"], "lat": 44.4935, "lng": 11.3435, "rating": 4.6, "description": "Dünyanın en büyük kiliselerinden biri.", "description_en": "One of the world's largest churches."},
        {"name": "Archiginnasio", "category": "Müze", "tags": ["library", "anatomy", "university"], "lat": 44.4920, "lng": 11.3430, "rating": 4.8, "description": "Tarihi anatomi salonu ve kütüphane.", "description_en": "Historic anatomy theater and library."},
        {"name": "Santuario di San Luca", "category": "Manzara", "tags": ["church", "portico", "hike"], "lat": 44.4795, "lng": 11.2980, "rating": 4.8, "description": "Dünyanın en uzun revaklı yoluyla çıkılan kilise.", "description_en": "Church reached by world's longest portico."},
        {"name": "Santo Stefano", "category": "Tarihi", "tags": ["seven churches", "complex", "medieval"], "lat": 44.4915, "lng": 11.3485, "rating": 4.8, "description": "İç içe geçmiş 'Yedi Kilise' kompleksi.", "description_en": "Interconnected 'Seven Churches' complex."},
        {"name": "Palazzo dell'Archiginnasio", "category": "Müze", "tags": ["palace", "historic", "coats of arms"], "lat": 44.4918, "lng": 11.3428, "rating": 4.6, "description": "Binlerce arma ile süslü tarihi bina.", "description_en": "Historic building decorated with thousands of coats of arms."},
        # MUSEUMS
        {"name": "MAMbo", "category": "Müze", "tags": ["modern art", "contemporary", "exhibitions"], "lat": 44.5020, "lng": 11.3380, "rating": 4.5, "description": "Bologna Modern Sanat Müzesi.", "description_en": "Bologna Museum of Modern Art."},
        {"name": "National Picture Gallery", "category": "Müze", "tags": ["paintings", "renaissance", "art"], "lat": 44.4960, "lng": 11.3550, "rating": 4.6, "description": "Rönesans tabloları koleksiyonu.", "description_en": "Collection of Renaissance paintings."},
        {"name": "Archaeological Museum", "category": "Müze", "tags": ["archaeology", "etruscan", "roman"], "lat": 44.4930, "lng": 11.3465, "rating": 4.5, "description": "Etrüsk ve Roma eserleri.", "description_en": "Etruscan and Roman artifacts."},
        # FOOD MARKETS
        {"name": "Quadrilatero", "category": "Alışveriş", "tags": ["food market", "deli", "medieval"], "lat": 44.4935, "lng": 11.3445, "rating": 4.7, "description": "Ortaçağ sokaklarında lüks şarküteriler.", "description_en": "Luxury delis in medieval streets."},
        {"name": "Mercato delle Erbe", "category": "Alışveriş", "tags": ["market", "food hall", "fresh"], "lat": 44.4985, "lng": 11.3420, "rating": 4.5, "description": "Kapalı pazar ve yemek salonu.", "description_en": "Covered market and food hall."},
        {"name": "FICO Eataly World", "category": "Deneyim", "tags": ["food park", "italian food", "large"], "lat": 44.5150, "lng": 11.4250, "rating": 4.4, "description": "Dünyanın en büyük yemek tema parkı.", "description_en": "World's largest food theme park."},
        # RESTAURANTS
        {"name": "Osteria dell'Orsa", "category": "Restoran", "tags": ["student", "tagliatelle", "budget"], "lat": 44.4975, "lng": 11.3470, "rating": 4.6, "description": "Öğrencilerin favorisi uygun fiyatlı klasik.", "description_en": "Students' favorite budget classic."},
        {"name": "Trattoria di Via Serra", "category": "Restoran", "tags": ["local", "authentic", "slow food"], "lat": 44.5050, "lng": 11.3450, "rating": 4.8, "description": "Otantik Bolonez yemekleri.", "description_en": "Authentic Bolognese dishes."},
        {"name": "Drogheria della Rosa", "category": "Restoran", "tags": ["elegant", "pasta", "wine"], "lat": 44.4925, "lng": 11.3485, "rating": 4.7, "description": "Şık ortamda mükemmel makarna.", "description_en": "Perfect pasta in elegant setting."},
        {"name": "Sfoglia Rina", "category": "Restoran", "tags": ["fresh pasta", "tortellini", "take away"], "lat": 44.4942, "lng": 11.3428, "rating": 4.6, "description": "Taze el yapımı makarna.", "description_en": "Fresh handmade pasta."},
        {"name": "Oltre", "category": "Restoran", "tags": ["michelin", "modern", "creative"], "lat": 44.4930, "lng": 11.3440, "rating": 4.7, "description": "Michelin yıldızlı yaratıcı mutfak.", "description_en": "Michelin starred creative cuisine."},
        {"name": "All'Osteria Bottega", "category": "Restoran", "tags": ["traditional", "mortadella", "ragu"], "lat": 44.4948, "lng": 11.3455, "rating": 4.6, "description": "Bolognese ragù ve mortadella.", "description_en": "Bolognese ragù and mortadella."},
        # GELATO & CAFES
        {"name": "Cremeria Santo Stefano", "category": "Kafe", "tags": ["gelato", "artisan", "best"], "lat": 44.4895, "lng": 11.3530, "rating": 4.9, "description": "Şehrin en iyi dondurması.", "description_en": "City's best ice cream."},
        {"name": "Gelateria Gianni", "category": "Kafe", "tags": ["gelato", "creamy", "local favorite"], "lat": 44.4952, "lng": 11.3468, "rating": 4.7, "description": "Yerlilerin favorisi kremamsı dondurma.", "description_en": "Locals' favorite creamy ice cream."},
        {"name": "Caffè Terzi", "category": "Kafe", "tags": ["espresso", "specialty coffee", "roaster"], "lat": 44.4945, "lng": 11.3438, "rating": 4.6, "description": "Özel kavurma espresso.", "description_en": "Specialty roasted espresso."},
        {"name": "Caffè Zanarini", "category": "Kafe", "tags": ["historic", "elegant", "pastries"], "lat": 44.4940, "lng": 11.3445, "rating": 4.5, "description": "Tarihi elegant pastane.", "description_en": "Historic elegant pastry shop."},
        # EXPERIENCES
        {"name": "Pasta Making Class", "category": "Deneyim", "tags": ["cooking", "tortellini", "tagliatelle"], "lat": 44.4950, "lng": 11.3450, "rating": 4.8, "description": "Tortellini ve tagliatelle yapımı öğrenin.", "description_en": "Learn to make tortellini and tagliatelle."},
        {"name": "San Luca Portico Walk", "category": "Deneyim", "tags": ["walk", "pilgrimage", "666 arches"], "lat": 44.4850, "lng": 11.3100, "rating": 4.7, "description": "666 kemerli dünya rekoru portico yürüyüşü.", "description_en": "World record 666 arch portico walk."},
    ],
    "gaziantep": [
        # HISTORIC SITES
        {"name": "Zeugma Mozaik Müzesi", "category": "Müze", "tags": ["mosaic", "world class", "roman"], "lat": 37.0755, "lng": 37.3855, "rating": 4.9, "description": "Çingene Kızı mozaiğinin evi, dünyanın en büyük mozaik müzesi.", "description_en": "Home of Gypsy Girl mosaic, world's largest mosaic museum."},
        {"name": "Gaziantep Kalesi", "category": "Tarihi", "tags": ["castle", "panorama", "defense"], "lat": 37.0645, "lng": 37.3835, "rating": 4.6, "description": "Şehre hakim heybetli tarihi kale.", "description_en": "Majestic historic castle overlooking the city."},
        {"name": "Bakırcılar Çarşısı", "category": "Alışveriş", "tags": ["bazaar", "copper", "crafts"], "lat": 37.0635, "lng": 37.3820, "rating": 4.8, "description": "Yüzyıllardır çekiç seslerinin yankılandığı bakır işi çarşısı.", "description_en": "Coppersmith bazaar echoing with hammer sounds for centuries."},
        {"name": "Zincirli Bedesten", "category": "Alışveriş", "tags": ["market", "spices", "souvenirs"], "lat": 37.0630, "lng": 37.3825, "rating": 4.7, "description": "Baharat ve hediyelik eşya bulabileceğiniz tarihi kapalı çarşı.", "description_en": "Historic covered bazaar where you can find spices and souvenirs."},
        {"name": "Hasan Süzer Etnografya Müzesi", "category": "Müze", "tags": ["ethnography", "mansion", "life"], "lat": 37.0648, "lng": 37.3830, "rating": 4.5, "description": "Antep yaşamını gösteren restore edilmiş konak.", "description_en": "Restored mansion showing Antep life."},
        {"name": "Kurtuluş Camileri", "category": "Tarihi", "tags": ["mosque", "historic", "center"], "lat": 37.0660, "lng": 37.3838, "rating": 4.4, "description": "Şehir merkezindeki tarihi cami kompleksi.", "description_en": "Historic mosque complex in city center."},
        {"name": "Gaziantep Savunma ve Kahramanlık Panoramik Müzesi", "category": "Müze", "tags": ["war", "panorama", "history"], "lat": 37.0640, "lng": 37.3840, "rating": 4.6, "description": "Kurtuluş Savaşı'nı anlatan panoramik müze.", "description_en": "Panoramic museum telling the War of Independence."},
        {"name": "Antep Evleri", "category": "Tarihi", "tags": ["houses", "architecture", "old town"], "lat": 37.0625, "lng": 37.3815, "rating": 4.5, "description": "Restore edilmiş geleneksel Antep evleri bölgesi.", "description_en": "Restored traditional Antep houses area."},
        # FOOD & GASTRONOMY
        {"name": "Mutfak Sanatları Merkezi", "category": "Müze", "tags": ["gastronomy", "unesco", "culture"], "lat": 37.0650, "lng": 37.3840, "rating": 4.7, "description": "UNESCO Gastronomi şehrinin mutfak müzesi.", "description_en": "Cuisine museum of UNESCO Gastronomy city."},
        {"name": "Tahmis Kahvesi", "category": "Kafe", "tags": ["coffee", "historic", "menengiç"], "lat": 37.0620, "lng": 37.3810, "rating": 4.8, "description": "1635'ten beri hizmet veren menengiç kahvesiyle ünlü mekan.", "description_en": "Famous for menengiç coffee, serving since 1635."},
        {"name": "İmam Çağdaş", "category": "Restoran", "tags": ["baklava", "kebab", "legend"], "lat": 37.0625, "lng": 37.3815, "rating": 4.6, "description": "Şehrin en ikonik kebap ve baklava restoranı.", "description_en": "City's most iconic kebab and baklava restaurant."},
        {"name": "Koçak Baklava", "category": "Kafe", "tags": ["baklava", "famous", "pistachio"], "lat": 37.0730, "lng": 37.3750, "rating": 4.9, "description": "Fıstıklı baklava ustası.", "description_en": "Master of pistachio baklava."},
        {"name": "Metanet Lokantası", "category": "Restoran", "tags": ["beyran", "breakfast", "soup"], "lat": 37.0615, "lng": 37.3830, "rating": 4.8, "description": "Meşhur Beyran çorbasının en iyi adresi.", "description_en": "Best address for famous Beyran soup."},
        {"name": "Kebapçı Halil Usta", "category": "Restoran", "tags": ["küşleme", "kebab", "local"], "lat": 37.0760, "lng": 37.3860, "rating": 4.9, "description": "Efsanevi küşleme (lokum et) için gelmeniz gereken yer.", "description_en": "The place to come for legendary küşleme (melt meat)."},
        {"name": "Orkide Pastanesi", "category": "Kafe", "tags": ["katmer", "bakery", "traditional"], "lat": 37.0618, "lng": 37.3825, "rating": 4.7, "description": "Sabah katmeri için en popüler adres.", "description_en": "Most popular address for morning katmer."},
        {"name": "Çulcuoğlu Baklava", "category": "Kafe", "tags": ["baklava", "historic", "quality"], "lat": 37.0622, "lng": 37.3818, "rating": 4.7, "description": "100 yılı aşkın baklava geleneği.", "description_en": "Over 100 years of baklava tradition."},
        {"name": "Uçar Lahmacun", "category": "Restoran", "tags": ["lahmacun", "fast food", "crispy"], "lat": 37.0655, "lng": 37.3820, "rating": 4.6, "description": "Çıtır çıtır lahmacun.", "description_en": "Crispy lahmacun."},
        {"name": "Yüzevler Kebapçısı", "category": "Restoran", "tags": ["kebab", "variety", "popular"], "lat": 37.0665, "lng": 37.3845, "rating": 4.5, "description": "Çeşitli kebap türleri.", "description_en": "Various types of kebab."},
        # SHOPPING
        {"name": "Elmacı Pazarı", "category": "Alışveriş", "tags": ["antiques", "old bazaar", "treasures"], "lat": 37.0633, "lng": 37.3823, "rating": 4.4, "description": "Antika ve eski eşya pazarı.", "description_en": "Antiques and old items market."},
        {"name": "Hanlar Bölgesi", "category": "Alışveriş", "tags": ["hans", "historic", "trade"], "lat": 37.0628, "lng": 37.3822, "rating": 4.5, "description": "Tarihi hanların bulunduğu ticaret bölgesi.", "description_en": "Trade area with historic hans."},
        {"name": "Fıstık Pazarı", "category": "Alışveriş", "tags": ["pistachio", "nuts", "local"], "lat": 37.0638, "lng": 37.3828, "rating": 4.6, "description": "Antep fıstığı ve kuruyemiş.", "description_en": "Antep pistachios and nuts."},
        # EXPERIENCES
        {"name": "Baklava Yapım Kursu", "category": "Deneyim", "tags": ["cooking", "baklava", "class"], "lat": 37.0645, "lng": 37.3835, "rating": 4.8, "description": "Baklava yapımını ustalardan öğrenin.", "description_en": "Learn baklava making from masters."},
        {"name": "Bakırcı Atölyesi Ziyareti", "category": "Deneyim", "tags": ["workshop", "copper", "craft"], "lat": 37.0632, "lng": 37.3818, "rating": 4.6, "description": "Geleneksel bakır işçiliğini izleyin.", "description_en": "Watch traditional coppersmithing."},
        {"name": "Zeugma Antik Kenti", "category": "Tarihi", "tags": ["ruins", "roman", "day trip"], "lat": 37.0500, "lng": 37.8700, "rating": 4.5, "description": "Mozaiklerin bulunduğu antik kent kalıntıları.", "description_en": "Ancient city ruins where mosaics were found."},
        # NATURE
        {"name": "Dülük Antik Kenti", "category": "Park", "tags": ["ancient", "nature", "walk"], "lat": 37.1100, "lng": 37.3200, "rating": 4.4, "description": "Doğa yürüyüşü ve antik kalıntılar.", "description_en": "Nature walk and ancient ruins."},
        {"name": "Rumkale", "category": "Manzara", "tags": ["castle", "river", "scenic"], "lat": 37.2700, "lng": 37.8300, "rating": 4.6, "description": "Fırat Nehri kıyısında etkileyici kale.", "description_en": "Impressive castle on Euphrates River bank."},
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
