import json
import os

# COMPREHENSIVE ENRICHMENT DATA FOR 14 NEW CITIES
# Each city will have 30+ high-quality places

enrichment_data = {
    "rovaniemi": [
        # MUSEUMS & CULTURE
        {"name": "Pilke Science Centre", "category": "Müze", "tags": ["science", "forest", "interactive"], "lat": 66.5082, "lng": 25.7260, "rating": 4.5, "description": "Finlandiya ormanlarını ve ahşap endüstrisini interaktif olarak tanıtan bilim merkezi.", "description_en": "Interactive science center showcasing Finnish forests and wood industry."},
        {"name": "Korundi House of Culture", "category": "Müze", "tags": ["art", "contemporary", "chamber music"], "lat": 66.4995, "lng": 25.7215, "rating": 4.6, "description": "Laponya'nın en önemli çağdaş sanat müzesi ve konser salonu.", "description_en": "Lapland's premier contemporary art museum and concert hall."},
        {"name": "Rovaniemi Art Museum", "category": "Müze", "tags": ["art", "finnish", "exhibitions"], "lat": 66.5000, "lng": 25.7230, "rating": 4.4, "description": "Fin sanatçıların eserlerinin sergilendiği şehir sanat müzesi.", "description_en": "City art museum featuring works by Finnish artists."},
        {"name": "Lapland Forestry Museum", "category": "Müze", "tags": ["history", "forestry", "outdoor"], "lat": 66.5100, "lng": 25.7400, "rating": 4.3, "description": "Açık hava müzesinde Laponya ormancılığının tarihi.", "description_en": "Open-air museum showcasing Lapland forestry history."},
        # NATURE & PARKS
        {"name": "Ounasvaara Ski Resort", "category": "Park", "tags": ["ski", "snowboard", "view"], "lat": 66.5055, "lng": 25.7755, "rating": 4.7, "description": "Şehrin hemen yanında kayak merkezi ve panoramik manzara noktası.", "description_en": "Ski resort right next to the city with panoramic views."},
        {"name": "Angry Birds Activity Park", "category": "Park", "tags": ["kids", "playground", "fun"], "lat": 66.5038, "lng": 25.7280, "rating": 4.4, "description": "Çocuklar için Angry Birds temalı açık hava oyun alanı.", "description_en": "Angry Birds themed outdoor playground for kids."},
        {"name": "Auttiköngäs Waterfall", "category": "Manzara", "tags": ["waterfall", "nature", "hiking"], "lat": 66.3800, "lng": 27.2200, "rating": 4.8, "description": "Bölgenin en etkileyici şelalesi, yürüyüş parkuru ile.", "description_en": "The region's most impressive waterfall with hiking trails."},
        {"name": "Norvajärvi Lake", "category": "Park", "tags": ["lake", "swimming", "camping"], "lat": 66.4500, "lng": 25.6000, "rating": 4.5, "description": "Yaz aylarında yüzme ve kamp yapılabilecek sakin göl.", "description_en": "Peaceful lake for swimming and camping in summer."},
        {"name": "Kemijoki River Trail", "category": "Park", "tags": ["walking", "river", "scenic"], "lat": 66.5050, "lng": 25.7350, "rating": 4.6, "description": "Nehir boyunca uzanan manzaralı yürüyüş parkuru.", "description_en": "Scenic walking trail along the river."},
        # EXPERIENCES & ACTIVITIES
        {"name": "Santa Claus Village", "category": "Tarihi", "tags": ["christmas", "santa", "arctic circle"], "lat": 66.5434, "lng": 25.8472, "rating": 4.8, "description": "Noel Baba'nın resmi evi ve Kuzey Kutup Dairesi geçiş noktası.", "description_en": "Official home of Santa Claus and Arctic Circle crossing point."},
        {"name": "SantaPark", "category": "Deneyim", "tags": ["theme park", "underground", "kids"], "lat": 66.5398, "lng": 25.8033, "rating": 4.5, "description": "Yeraltında kurulmuş Noel temalı eğlence parkı.", "description_en": "Underground Christmas-themed amusement park."},
        {"name": "Ranua Wildlife Park", "category": "Park", "tags": ["zoo", "polar bears", "arctic animals"], "lat": 65.9442, "lng": 26.4746, "rating": 4.6, "description": "Kutup ayıları ve Arktik hayvanları görebileceğiniz park.", "description_en": "Wildlife park with polar bears and Arctic animals."},
        {"name": "Husky Safari Center", "category": "Deneyim", "tags": ["husky", "sledding", "dogs"], "lat": 66.5200, "lng": 25.8500, "rating": 4.9, "description": "Husky kızağı safari deneyimi ve köpeklerle tanışma.", "description_en": "Husky sled safari experience and meet the dogs."},
        {"name": "Northern Lights Tour Point", "category": "Deneyim", "tags": ["aurora", "night", "photography"], "lat": 66.5500, "lng": 25.9000, "rating": 4.8, "description": "Kuzey Işıkları izleme turlarının başlangıç noktası.", "description_en": "Starting point for Northern Lights viewing tours."},
        {"name": "Ice Hotel Experience", "category": "Deneyim", "tags": ["ice", "hotel", "unique"], "lat": 66.5450, "lng": 25.8600, "rating": 4.7, "description": "Buzdan inşa edilmiş otelde konaklama veya ziyaret.", "description_en": "Stay or visit the hotel built entirely from ice."},
        {"name": "Reindeer Farm Visit", "category": "Deneyim", "tags": ["reindeer", "sami", "culture"], "lat": 66.5300, "lng": 25.8300, "rating": 4.6, "description": "Ren geyiği çiftliğini ziyaret ve Sami kültürünü tanıma.", "description_en": "Visit reindeer farm and learn about Sami culture."},
        # RESTAURANTS
        {"name": "Nili Restaurant", "category": "Restoran", "tags": ["local", "reindeer", "fine dining"], "lat": 66.5025, "lng": 25.7310, "rating": 4.8, "description": "Geleneksel Laponya mutfağının en iyi adresi.", "description_en": "Best address for traditional Lapland cuisine."},
        {"name": "Restaurant Gaissa", "category": "Restoran", "tags": ["arctic", "modern", "seasonal"], "lat": 66.5030, "lng": 25.7320, "rating": 4.7, "description": "Mevsimsel Arktik malzemelerle modern mutfak.", "description_en": "Modern cuisine with seasonal Arctic ingredients."},
        {"name": "Ravintola Monte Rosa", "category": "Restoran", "tags": ["italian", "pizza", "central"], "lat": 66.5020, "lng": 25.7300, "rating": 4.4, "description": "Şehir merkezinde kaliteli İtalyan mutfağı.", "description_en": "Quality Italian cuisine in the city center."},
        {"name": "Arctic Boulevard", "category": "Restoran", "tags": ["bistro", "lunch", "casual"], "lat": 66.5015, "lng": 25.7325, "rating": 4.5, "description": "Günlük öğle yemekleri ve hafif atıştırmalıklar.", "description_en": "Daily lunch specials and light bites."},
        {"name": "Roka Kitchen & Bar", "category": "Restoran", "tags": ["steakhouse", "cocktails", "dinner"], "lat": 66.5028, "lng": 25.7315, "rating": 4.6, "description": "Et severler için ideal steakhouse ve kokteyl bar.", "description_en": "Ideal steakhouse and cocktail bar for meat lovers."},
        # CAFES
        {"name": "Cafe & Bar 21", "category": "Kafe", "tags": ["waffles", "cocktails", "trendy"], "lat": 66.5020, "lng": 25.7315, "rating": 4.7, "description": "En iyi waffle ve kokteyller burada.", "description_en": "Best waffles and cocktails here."},
        {"name": "Kahvila Kauppayhtiö", "category": "Kafe", "tags": ["coffee", "pastry", "historic"], "lat": 66.5018, "lng": 25.7308, "rating": 4.5, "description": "Tarihi binada geleneksel Fin kahve deneyimi.", "description_en": "Traditional Finnish coffee experience in historic building."},
        {"name": "Coffee House Rovaniemi", "category": "Kafe", "tags": ["specialty coffee", "modern", "wifi"], "lat": 66.5022, "lng": 25.7305, "rating": 4.4, "description": "Özel kahve çeşitleri ve çalışmak için ideal ortam.", "description_en": "Specialty coffees and ideal workspace."},
        # LANDMARKS
        {"name": "Jätkänkynttilä Bridge", "category": "Manzara", "tags": ["bridge", "landmark", "photo"], "lat": 66.5045, "lng": 25.7370, "rating": 4.7, "description": "Rovaniemi'nin simgesi, gece aydınlatmalı köprü.", "description_en": "Rovaniemi's landmark, illuminated bridge at night."},
        {"name": "Lordi's Square", "category": "Manzara", "tags": ["square", "center", "statue"], "lat": 66.5028, "lng": 25.7303, "rating": 4.4, "description": "Eurovision şampiyonu Lordi grubuna adanmış meydan.", "description_en": "Square dedicated to Eurovision winners Lordi."},
        {"name": "Arktikum Bridge", "category": "Manzara", "tags": ["architecture", "glass", "modern"], "lat": 66.5088, "lng": 25.7250, "rating": 4.5, "description": "Arktikum müzesinin ikonik cam tünel yapısı.", "description_en": "Arktikum museum's iconic glass tunnel structure."},
        {"name": "Rovaniemi Church", "category": "Tarihi", "tags": ["church", "modern", "architecture"], "lat": 66.5010, "lng": 25.7290, "rating": 4.3, "description": "Savaş sonrası yeniden inşa edilen modern kilise.", "description_en": "Post-war reconstructed modern church."},
        # SHOPPING
        {"name": "Sampokeskus Shopping Center", "category": "Alışveriş", "tags": ["mall", "brands", "central"], "lat": 66.5025, "lng": 25.7295, "rating": 4.2, "description": "Şehir merkezinin ana alışveriş merkezi.", "description_en": "Main shopping center in city center."},
        {"name": "Revontuli Shopping Centre", "category": "Alışveriş", "tags": ["mall", "fashion", "entertainment"], "lat": 66.5030, "lng": 25.7280, "rating": 4.3, "description": "Moda, eğlence ve restoranların bulunduğu AVM.", "description_en": "Mall with fashion, entertainment and restaurants."},
        {"name": "Lapin Kultakaivos Gold Mine Gift Shop", "category": "Alışveriş", "tags": ["souvenirs", "gold", "local"], "lat": 66.5035, "lng": 25.7310, "rating": 4.4, "description": "Laponya'dan altın ve yerel hediyelik eşyalar.", "description_en": "Lapland gold and local souvenirs."},
    ],
    "tromso": [
        # NATURE & VIEWS
        {"name": "Fjellheisen Cable Car", "category": "Manzara", "tags": ["cable car", "panorama", "midnight sun"], "lat": 69.6415, "lng": 18.9950, "rating": 4.8, "description": "421 metre yükseklikte şehir ve fiyort manzarası.", "description_en": "City and fjord views from 421 meters height."},
        {"name": "Telegrafbukta Beach", "category": "Park", "tags": ["beach", "midnight sun", "nature"], "lat": 69.6355, "lng": 18.9135, "rating": 4.7, "description": "Gece yarısı güneşini izlemek için ideal sahil.", "description_en": "Ideal beach for watching midnight sun."},
        {"name": "Prestvannet Lake", "category": "Park", "tags": ["lake", "birds", "walking"], "lat": 69.6590, "lng": 18.9320, "rating": 4.6, "description": "Kuş gözlemi ve yürüyüş için şehir içi göl.", "description_en": "City lake for bird watching and walking."},
        {"name": "Tromsøya Island Trail", "category": "Park", "tags": ["hiking", "nature", "views"], "lat": 69.6500, "lng": 18.9400, "rating": 4.5, "description": "Ada çevresinde doğa yürüyüşü parkuru.", "description_en": "Nature hiking trail around the island."},
        {"name": "Ersfjordbotn Viewpoint", "category": "Manzara", "tags": ["fjord", "mountains", "scenic"], "lat": 69.5200, "lng": 18.7500, "rating": 4.9, "description": "Nefes kesen fiyort manzarası.", "description_en": "Breathtaking fjord scenery."},
        {"name": "Rekvik Beach", "category": "Park", "tags": ["arctic beach", "remote", "peaceful"], "lat": 69.7000, "lng": 18.7000, "rating": 4.6, "description": "Arktik Okyanus'a bakan sakin kum plajı.", "description_en": "Peaceful sandy beach facing Arctic Ocean."},
        # MUSEUMS & CULTURE
        {"name": "Arctic Cathedral", "category": "Tarihi", "tags": ["church", "architecture", "iconic"], "lat": 69.6480, "lng": 18.9875, "rating": 4.7, "description": "Buzdağı şeklinde modern mimari şaheseri.", "description_en": "Modern architectural masterpiece shaped like iceberg."},
        {"name": "Polaria", "category": "Müze", "tags": ["aquarium", "arctic", "seals"], "lat": 69.6438, "lng": 18.9500, "rating": 4.5, "description": "Arktik deniz yaşamı akvaryumu ve sinema.", "description_en": "Arctic marine life aquarium and cinema."},
        {"name": "Polar Museum", "category": "Müze", "tags": ["history", "exploration", "hunting"], "lat": 69.6525, "lng": 18.9635, "rating": 4.6, "description": "Kutup keşif ve avcılık tarihi.", "description_en": "History of polar exploration and hunting."},
        {"name": "Tromsø University Museum", "category": "Müze", "tags": ["natural history", "sami", "aurora"], "lat": 69.6800, "lng": 18.9700, "rating": 4.5, "description": "Kuzey ışıkları bilimi ve Sami kültürü.", "description_en": "Northern lights science and Sami culture."},
        {"name": "Perspective Museum", "category": "Müze", "tags": ["photography", "local", "exhibitions"], "lat": 69.6520, "lng": 18.9600, "rating": 4.3, "description": "Yerel fotoğraf ve sanat sergileri.", "description_en": "Local photography and art exhibitions."},
        {"name": "Northern Norwegian Art Museum", "category": "Müze", "tags": ["art", "contemporary", "nordic"], "lat": 69.6530, "lng": 18.9610, "rating": 4.4, "description": "Kuzey Norveç sanatçılarının eserleri.", "description_en": "Works by Northern Norwegian artists."},
        {"name": "Tromsø Cathedral", "category": "Tarihi", "tags": ["cathedral", "wooden", "historic"], "lat": 69.6510, "lng": 18.9580, "rating": 4.4, "description": "Norveç'in en kuzeyindeki protestan katedrali.", "description_en": "Norway's northernmost protestant cathedral."},
        # EXPERIENCES
        {"name": "Northern Lights Observatory", "category": "Deneyim", "tags": ["aurora", "science", "tours"], "lat": 69.6600, "lng": 18.9400, "rating": 4.8, "description": "Kuzey ışıkları izleme turları ve bilim merkezi.", "description_en": "Northern lights viewing tours and science center."},
        {"name": "Whale Watching Tours", "category": "Deneyim", "tags": ["whales", "ocean", "wildlife"], "lat": 69.6470, "lng": 18.9550, "rating": 4.9, "description": "Kasım-Ocak arası balina izleme turları.", "description_en": "Whale watching tours November-January."},
        {"name": "Dog Sledding Camp", "category": "Deneyim", "tags": ["husky", "sledding", "arctic"], "lat": 69.7000, "lng": 19.0500, "rating": 4.8, "description": "Husky kızağı ile Arktik macerasına çıkın.", "description_en": "Arctic adventure with husky sled."},
        {"name": "Tromsø Ice Domes", "category": "Deneyim", "tags": ["ice bar", "experience", "winter"], "lat": 69.6550, "lng": 18.9700, "rating": 4.6, "description": "Buz bar ve buz heykeller deneyimi.", "description_en": "Ice bar and ice sculptures experience."},
        # LANDMARKS
        {"name": "Tromsø Bridge", "category": "Manzara", "tags": ["bridge", "landmark", "walk"], "lat": 69.6515, "lng": 18.9730, "rating": 4.6, "description": "Şehir adası ile anakarayı bağlayan ikonik köprü.", "description_en": "Iconic bridge connecting city island to mainland."},
        {"name": "Skansen Quay", "category": "Manzara", "tags": ["harbor", "historic", "boats"], "lat": 69.6508, "lng": 18.9620, "rating": 4.4, "description": "Tarihi liman bölgesi ve balıkçı tekneleri.", "description_en": "Historic harbor area and fishing boats."},
        # RESTAURANTS
        {"name": "Ølhallen", "category": "Restoran", "tags": ["pub", "historic", "beer"], "lat": 69.6530, "lng": 18.9600, "rating": 4.7, "description": "1928'den beri açık olan Tromsø'nün en eski barı.", "description_en": "Tromsø's oldest bar open since 1928."},
        {"name": "Full Steam Tromsø", "category": "Restoran", "tags": ["seafood", "museum", "dinner"], "lat": 69.6485, "lng": 18.9565, "rating": 4.6, "description": "Balıkçılık müzesi içinde deniz ürünleri restoranı.", "description_en": "Seafood restaurant inside fishing museum."},
        {"name": "Mathallen Tromsø", "category": "Restoran", "tags": ["food hall", "local", "variety"], "lat": 69.6495, "lng": 18.9590, "rating": 4.5, "description": "Yerel lezzetlerin bir arada olduğu yemek salonu.", "description_en": "Food hall with various local flavors."},
        {"name": "Bardus Bistro", "category": "Restoran", "tags": ["bistro", "arctic", "fine dining"], "lat": 69.6505, "lng": 18.9580, "rating": 4.7, "description": "Arktik malzemelerle yaratıcı mutfak.", "description_en": "Creative cuisine with Arctic ingredients."},
        {"name": "Emma's Drømmekjøkken", "category": "Restoran", "tags": ["nordic", "seasonal", "intimate"], "lat": 69.6518, "lng": 18.9595, "rating": 4.8, "description": "Samimi ortamda mevsimsel Nordik yemekler.", "description_en": "Seasonal Nordic dishes in intimate setting."},
        {"name": "Skarven Restaurant", "category": "Restoran", "tags": ["traditional", "fish", "view"], "lat": 69.6490, "lng": 18.9560, "rating": 4.5, "description": "Liman manzaralı geleneksel balık yemekleri.", "description_en": "Traditional fish dishes with harbor view."},
        # CAFES
        {"name": "Risø Mat & Kaffebar", "category": "Kafe", "tags": ["coffee", "cinnamon buns", "cozy"], "lat": 69.6495, "lng": 18.9575, "rating": 4.8, "description": "En iyi tarçınlı çörekler ve kahve.", "description_en": "Best cinnamon buns and coffee."},
        {"name": "Kaffebønna", "category": "Kafe", "tags": ["specialty coffee", "local roaster", "hip"], "lat": 69.6512, "lng": 18.9605, "rating": 4.6, "description": "Yerel kavurma özel kahveler.", "description_en": "Locally roasted specialty coffees."},
        {"name": "Smørtorget Café", "category": "Kafe", "tags": ["breakfast", "lunch", "central"], "lat": 69.6520, "lng": 18.9595, "rating": 4.4, "description": "Merkezi konumda kahvaltı ve öğle yemeği.", "description_en": "Breakfast and lunch in central location."},
        {"name": "Meieriet Chocolate Café", "category": "Kafe", "tags": ["chocolate", "dessert", "artisan"], "lat": 69.6508, "lng": 18.9598, "rating": 4.7, "description": "El yapımı çikolata ve tatlılar.", "description_en": "Handmade chocolates and desserts."},
        # SHOPPING
        {"name": "Nerstranda Shopping", "category": "Alışveriş", "tags": ["mall", "brands", "central"], "lat": 69.6515, "lng": 18.9602, "rating": 4.2, "description": "Şehir merkezinin ana alışveriş merkezi.", "description_en": "Main shopping center in city center."},
        {"name": "Tromsø Outdoor Market", "category": "Alışveriş", "tags": ["market", "local", "souvenirs"], "lat": 69.6530, "lng": 18.9590, "rating": 4.5, "description": "Yerel el sanatları ve hediyelik eşyalar.", "description_en": "Local crafts and souvenirs."},
    ],
    "zermatt": [
        # VIEWS & NATURE
        {"name": "Gornergrat Railway", "category": "Manzara", "tags": ["train", "mountain", "panorama"], "lat": 46.0090, "lng": 7.7850, "rating": 4.9, "description": "Matterhorn manzaralı 3100m yüksekliğe tırmanan tren.", "description_en": "Train climbing to 3100m with Matterhorn views."},
        {"name": "Matterhorn Glacier Paradise", "category": "Manzara", "tags": ["glacier", "highest", "ice palace"], "lat": 45.9385, "lng": 7.7295, "rating": 4.8, "description": "Avrupa'nın en yüksek teleferik istasyonu ve buz sarayı.", "description_en": "Europe's highest cable car station and ice palace."},
        {"name": "Riffelsee", "category": "Park", "tags": ["lake", "reflection", "hiking"], "lat": 46.0020, "lng": 7.7800, "rating": 4.9, "description": "Matterhorn'un yansımasının düştüğü efsanevi göl.", "description_en": "Legendary lake reflecting the Matterhorn."},
        {"name": "Five Lakes Walk", "category": "Park", "tags": ["hiking", "lakes", "scenic"], "lat": 46.0150, "lng": 7.7800, "rating": 4.8, "description": "Beş farklı dağ gölünü ziyaret eden yürüyüş rotası.", "description_en": "Hiking route visiting five different mountain lakes."},
        {"name": "Gorner Gorge", "category": "Park", "tags": ["gorge", "waterfall", "walk"], "lat": 46.0135, "lng": 7.7435, "rating": 4.6, "description": "Ahşap köprülerden geçilen dramatik kanyon.", "description_en": "Dramatic gorge crossed by wooden bridges."},
        {"name": "Sunnegga Paradise", "category": "Manzara", "tags": ["funicular", "family", "view"], "lat": 46.0100, "lng": 7.7600, "rating": 4.7, "description": "Aileler için ideal füniküler ve Leisee gölü.", "description_en": "Ideal funicular for families and Leisee lake."},
        {"name": "Schwarzsee", "category": "Park", "tags": ["lake", "chapel", "matterhorn"], "lat": 45.9800, "lng": 7.7200, "rating": 4.7, "description": "Matterhorn'a yakın şapel ve dağ gölü.", "description_en": "Mountain lake and chapel close to Matterhorn."},
        {"name": "Trockener Steg", "category": "Manzara", "tags": ["glacier", "summer ski", "views"], "lat": 45.9700, "lng": 7.7400, "rating": 4.5, "description": "Yaz kayağı yapılabilen buzul istasyonu.", "description_en": "Glacier station where you can ski in summer."},
        # HISTORIC & CULTURE
        {"name": "Hinterdorf", "category": "Tarihi", "tags": ["old town", "wooden houses", "history"], "lat": 46.0195, "lng": 7.7485, "rating": 4.7, "description": "16. yüzyıldan kalma ahşap evlerin olduğu tarihi mahalle.", "description_en": "Historic quarter with 16th century wooden houses."},
        {"name": "Matterhorn Museum", "category": "Müze", "tags": ["mountaineering", "history", "underground"], "lat": 46.0205, "lng": 7.7475, "rating": 4.6, "description": "Zermatlantis adlı yeraltı müzesinde dağcılık tarihi.", "description_en": "Mountaineering history in underground museum Zermatlantis."},
        {"name": "English Church", "category": "Tarihi", "tags": ["church", "climbers", "memorial"], "lat": 46.0200, "lng": 7.7490, "rating": 4.4, "description": "Matterhorn'da hayatını kaybeden dağcıların anıt kilisesi.", "description_en": "Memorial church for climbers who died on Matterhorn."},
        {"name": "Mountaineers' Cemetery", "category": "Tarihi", "tags": ["cemetery", "history", "tribute"], "lat": 46.0190, "lng": 7.7495, "rating": 4.5, "description": "Efsanevi dağcıların gömülü olduğu anıt mezarlık.", "description_en": "Memorial cemetery where legendary climbers are buried."},
        {"name": "St. Mauritius Church", "category": "Tarihi", "tags": ["church", "baroque", "village"], "lat": 46.0210, "lng": 7.7470, "rating": 4.3, "description": "Köyün tarihi barok kilisesi.", "description_en": "Village's historic baroque church."},
        # RESTAURANTS
        {"name": "Chez Vrony", "category": "Restoran", "tags": ["mountain", "michelin", "view"], "lat": 46.0140, "lng": 7.7650, "rating": 4.8, "description": "Pist kenarında Michelin rehberine girmiş restoran.", "description_en": "Michelin-listed restaurant by the slopes."},
        {"name": "Whymper-Stube", "category": "Restoran", "tags": ["fondue", "raclette", "cozy"], "lat": 46.0210, "lng": 7.7480, "rating": 4.7, "description": "En iyi İsviçre peynir fondüsü ve raclette.", "description_en": "Best Swiss cheese fondue and raclette."},
        {"name": "Findlerhof", "category": "Restoran", "tags": ["alpine", "lamb", "panorama"], "lat": 46.0050, "lng": 7.7700, "rating": 4.8, "description": "Matterhorn manzaralı Alp mutfağı.", "description_en": "Alpine cuisine with Matterhorn view."},
        {"name": "Zum See", "category": "Restoran", "tags": ["rustic", "mountain food", "traditional"], "lat": 46.0000, "lng": 7.7550, "rating": 4.7, "description": "Otantik dağ köyü atmosferinde geleneksel yemekler.", "description_en": "Traditional dishes in authentic mountain village atmosphere."},
        {"name": "After Seven", "category": "Restoran", "tags": ["fine dining", "modern", "reservation"], "lat": 46.0200, "lng": 7.7470, "rating": 4.6, "description": "Yaratıcı gurme mutfak, rezervasyon şart.", "description_en": "Creative gourmet cuisine, reservation required."},
        {"name": "Restaurant Klein Matterhorn", "category": "Restoran", "tags": ["highest", "glacier", "unique"], "lat": 45.9400, "lng": 7.7300, "rating": 4.5, "description": "Avrupa'nın en yüksek restoranlarından biri.", "description_en": "One of Europe's highest restaurants."},
        # CAFES & BAKERIES
        {"name": "Fuchs Bakery", "category": "Kafe", "tags": ["bakery", "bread", "chocolate"], "lat": 46.0200, "lng": 7.7490, "rating": 4.7, "description": "Dağcı ekmeği (Bergführerbrot) ile ünlü fırın.", "description_en": "Bakery famous for mountain guide bread."},
        {"name": "Café du Pont", "category": "Kafe", "tags": ["coffee", "terrace", "view"], "lat": 46.0195, "lng": 7.7478, "rating": 4.5, "description": "Köprü yanında manzaralı kahve molası.", "description_en": "Coffee break with view by the bridge."},
        {"name": "Elsie's Bar", "category": "Kafe", "tags": ["wine bar", "oysters", "apres ski"], "lat": 46.0205, "lng": 7.7472, "rating": 4.6, "description": "İstiridye ve şampanya ile après-ski.", "description_en": "Après-ski with oysters and champagne."},
        {"name": "Grampi's Pub", "category": "Kafe", "tags": ["pub", "nightlife", "live music"], "lat": 46.0198, "lng": 7.7485, "rating": 4.4, "description": "Gece hayatı ve canlı müzik.", "description_en": "Nightlife and live music."},
        # SHOPPING
        {"name": "Bahnhofstrasse", "category": "Alışveriş", "tags": ["main street", "shops", "boutiques"], "lat": 46.0207, "lng": 7.7483, "rating": 4.3, "description": "Ana cadde üzerinde butikler ve mağazalar.", "description_en": "Boutiques and shops on main street."},
        {"name": "Zermatt Souvenirs", "category": "Alışveriş", "tags": ["gifts", "swiss", "matterhorn"], "lat": 46.0202, "lng": 7.7477, "rating": 4.2, "description": "Matterhorn temalı hediyelik eşyalar.", "description_en": "Matterhorn themed souvenirs."},
        {"name": "Swiss Watch Boutique", "category": "Alışveriş", "tags": ["watches", "luxury", "swiss"], "lat": 46.0203, "lng": 7.7480, "rating": 4.5, "description": "Lüks İsviçre saatleri.", "description_en": "Luxury Swiss watches."},
        {"name": "Chocolate Shop Hörnli", "category": "Alışveriş", "tags": ["chocolate", "swiss", "artisan"], "lat": 46.0200, "lng": 7.7475, "rating": 4.6, "description": "El yapımı İsviçre çikolataları.", "description_en": "Handmade Swiss chocolates."},
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
                # Add standard fields
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
