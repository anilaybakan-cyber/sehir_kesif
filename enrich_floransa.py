import json
import os

new_floransa_batch1 = [
    {
        "name": "Basilica di Santo Spirito",
        "name_en": "Basilica di Santo Spirito",
        "area": "Oltrarno",
        "category": "Tarihi",
        "tags": ["brunelleschi", "rönesans", "kilise", "michelangelo"],
        "distanceFromCenter": 0.6,
        "lat": 43.7673,
        "lng": 11.2483,
        "price": "low",
        "rating": 4.6,
        "description": "Brunelleschi'nin son başyapıtı kabul edilen, sadeliğiyle büyüleyen Rönesans kilisesi. Michelangelo'nun gençken yaptığı ahşap haç burada saklanır.",
        "description_en": "Brunelleschi's last masterpiece, a Renaissance church known for its elegant simplicity. Houses a wooden crucifix carved by Michelangelo in his youth.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Kilisenin arkasındaki gizli avlular ve zangoç odası oldukça etkileyicidir.",
        "tips_en": "The hidden cloisters and the sacristy are well worth a visit."
    },
    {
        "name": "Mercato Centrale (Gourmet Hall)",
        "name_en": "Mercato Centrale",
        "area": "San Lorenzo",
        "category": "Restoran",
        "tags": ["yemek", "gurme", "yiyecek marketi", "yerel"],
        "distanceFromCenter": 0.3,
        "lat": 43.7764,
        "lng": 11.2529,
        "price": "medium",
        "rating": 4.7,
        "description": "19. yüzyıldan kalma dev demir yapının üst katında yer alan modern gastronomi marketi. En iyi yerel pizza, makarna ve şarapları burada bir arada bulabilirsiniz.",
        "description_en": "A modern gourmet hall on the top floor of a 19th-century iron building. Features a wide variety of high-quality local food stalls, from pasta to pizza.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Genellikle çok kalabalık olur; yemeklerinizi alıp ortak masalarda yer bulmak için hızlı olmalısınız.",
        "tips_en": "It gets very busy; act quickly to find a spot at the communal tables after ordering your food."
    },
    {
        "name": "Giotto's Bell Tower (Campanile)",
        "name_en": "Giotto's Bell Tower",
        "area": "Piazza del Duomo",
        "category": "Manzara",
        "tags": ["kule", "manzara", "duomo", "gotik"],
        "distanceFromCenter": 0.1,
        "lat": 43.7731,
        "lng": 11.2569,
        "price": "medium",
        "rating": 4.8,
        "description": "Floransa Katedrali'nin hemen yanında yükselen, Giotto tarafından tasarlanan muhteşem gotik çan kulesi. Tepesinden Duomo kubbesinin en iyi fotoğraflarını çekebilirsiniz.",
        "description_en": "Giotto's magnificent Gothic bell tower next to the Cathedral. Climbing the 414 steps offers the best possible view of Brunelleschi's Dome itself.",
        "imageUrl": "https://images.unsplash.com/photo-1476442368824-e9f3b9c7b0f6?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "414 basamağı tırmanmanız gerekecek; çıkarken farklı katlardaki pencerelerden mola verip manzarayı izleyebilirsiniz.",
        "tips_en": "There are 414 steps; use the different levels to take breaks and enjoy the intermediate views."
    },
    {
        "name": "Florence Baptistery (Battistero)",
        "name_en": "Florence Baptistery",
        "area": "Piazza del Duomo",
        "category": "Tarihi",
        "tags": ["tarih", "mozaik", "cennetin kapıları", "dante"],
        "distanceFromCenter": 0.0,
        "lat": 43.7731,
        "lng": 11.2550,
        "price": "medium",
        "rating": 4.7,
        "description": "Şehrin en eski binalarından biri. Michelangelo'nun 'Cennetin Kapıları' adını verdiği devasa bronz kapıları ve tavanındaki altın mozaikleriyle ünlüdür.",
        "description_en": "One of the oldest buildings in the city, famous for its magnificent gold-ground ceiling mosaics and the bronze 'Gates of Paradise' by Ghiberti.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Dışarıdaki kapıların orjinalleri Museo dell'Opera del Duomo'da saklanmaktadır, kapının üzerindeki figürleri yakından inceleyin.",
        "tips_en": "The original doors are kept in the nearby Duomo Museum; take a close look at the intricate panels of the copies outside."
    },
    {
        "name": "Museo dell'Opera del Duomo",
        "name_en": "Duomo Museum",
        "area": "Piazza del Duomo",
        "category": "Müze",
        "tags": ["heykel", "duomo", "michelangelo", "donatello"],
        "distanceFromCenter": 0.2,
        "lat": 43.7731,
        "lng": 11.2575,
        "price": "medium",
        "rating": 4.9,
        "description": "Katedral kompleksi için yapılmış orjinalleri barındıran muhteşem müze. Michelangelo'nun yaşlılık dönemi Pieta'sı ve Ghiberti'nin orjinal bronz kapıları buradadır.",
        "description_en": "A state-of-the-art museum housing the original masterpieces created for the Cathedral, including Michelangelo's 'The Deposition' and the original Gates of Paradise.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Sabah veya Geç öğleden sonra",
        "bestTime_en": "Morning or late afternoon",
        "tips": "Müzenin en üst katındaki terastan Duomo kubbesini çok yakından ve farklı bir açıdan görebilirsiniz.",
        "tips_en": "Go to the top floor terrace for a unique, close-up view of the Dome."
    },
    {
        "name": "Vivoli Gelato",
        "name_en": "Vivoli Gelato",
        "area": "Santa Croce",
        "category": "Kafe",
        "tags": ["dondurma", "tarihi", "aile işletmesi", "geleneksel"],
        "distanceFromCenter": 0.5,
        "lat": 43.7700,
        "lng": 11.2583,
        "price": "low",
        "rating": 4.6,
        "description": "1930'dan beri aynı aile tarafından işletilen, Floransa'nın en eski ve en saygın dondurmacılarından biri. Hiçbir katkı maddesi kullanmadan hazırlanan klasik lezzetler.",
        "description_en": "One of Florence's oldest and most prestigious gelaterias, run by the same family since 1930. Known for their additive-free, traditional recipes.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Burada dondurma sadece kapta servis edilir, kornet yoktur. 'Cremolata' çeşitlerini mutlaka deneyin.",
        "tips_en": "Gelato is served in cups only, no cones. Try their famous 'cremolata' fruit ice."
    },
    {
        "name": "Buca Lapi",
        "name_en": "Buca Lapi",
        "area": "Centro Storico",
        "category": "Restoran",
        "tags": ["bistecca", "tarihi", "fine dining", "prestijli"],
        "distanceFromCenter": 0.5,
        "lat": 43.7726,
        "lng": 11.2515,
        "price": "high",
        "rating": 4.7,
        "description": "Floransa'nın en eski restoranı (1880). Palazzo Antinori'nin altındaki eski bir şarap mahzeninde yer alan, Bistecca alla Fiorentina için en prestijli adres.",
        "description_en": "The oldest restaurant in Florence, located in a former wine cellar beneath Palazzo Antinori. The premier destination for a traditional Fiorentina steak.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Haftalar öncesinden rezervasyon şarttır. Etleri meşe kömüründe pişirirler, koku harikadır.",
        "tips_en": "Booking weeks in advance is essential. Their meat is grilled over oak charcoal, creating an incredible aroma."
    },
    {
        "name": "Osteria di Giovanni",
        "name_en": "Osteria di Giovanni",
        "area": "Santa Maria Novella",
        "category": "Restoran",
        "tags": ["toskana mutfağı", "lokal", "aile işletmesi", "popüler"],
        "distanceFromCenter": 0.6,
        "lat": 43.7714,
        "lng": 11.2486,
        "price": "medium",
        "rating": 4.6,
        "description": "Giovanni ve ailesi tarafından işletilen, sıcak bir atmosferde en iyi Toskana yemeklerini sunan çok popüler bir osteria.",
        "description_en": "A warmly run family establishment offering some of the best traditional Tuscan cooking in a cozy, authentic setting.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Masaya oturur oturmaz gelen taze Toskana zeytinyağı ve ekmeğiyle başlayın.",
        "tips_en": "Start with the fresh Tuscan olive oil and bread provided as soon as you sit down."
    },
    {
        "name": "Forte di Belvedere",
        "name_en": "Forte di Belvedere",
        "area": "Oltrarno",
        "category": "Tarihi",
        "tags": ["kale", "manzara", "sergi", "medici"],
        "distanceFromCenter": 1.2,
        "lat": 43.7631,
        "lng": 11.2537,
        "price": "medium",
        "rating": 4.5,
        "description": "Medici ailesi tarafından şehri ve kendilerini korumak için inşa ettirilmiş devasa kale. Günümüzde modern sanat sergilerine ve muhteşem manzaralara ev sahipliği yapar.",
        "description_en": "A massive fortress built by the Medici for defense. Today it hosts prestigious contemporary art exhibitions and offers some of the city's most breathtaking views.",
        "imageUrl": "https://images.unsplash.com/photo-1476442368824-e9f3b9c7b0f6?w=800",
        "bestTime": "Yaz gün batımı",
        "bestTime_en": "Summer sunset",
        "tips": "Genellikle sadece yaz aylarında sergiler için açık olur, gitmeden takvimi kontrol edin.",
        "tips_en": "Usually only open during the summer for exhibitions, check the schedule before heading up."
    },
    {
        "name": "Loggia dei Lanzi",
        "name_en": "Loggia dei Lanzi",
        "area": "Piazza della Signoria",
        "category": "Tarihi",
        "tags": ["heykel", "ücretsiz", "rönesans", "meydan"],
        "distanceFromCenter": 0.2,
        "lat": 43.7682,
        "lng": 11.2534,
        "price": "free",
        "rating": 4.8,
        "description": "Piazza della Signoria'nın bir köşesinde yer alan açık hava heykel galerisi. Cellini'nin 'Medusa Başlı Perseus'u gibi başyapıtları ücretsiz görebilirsiniz.",
        "description_en": "An open-air sculpture gallery on the main square. Features Renaissance masterpieces like Cellini's Perseus with the Head of Medusa, accessible for free.",
        "imageUrl": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800",
        "bestTime": "Gece",
        "bestTime_en": "Night",
        "tips": "Gece ışıklandırması altında heykeller çok daha dramatik ve etkileyici görünür.",
        "tips_en": "The statues look much more dramatic and impressive when illuminated at night."
    },
    {
        "name": "Salvatore Ferragamo Museum",
        "name_en": "Ferragamo Museum",
        "area": "Centro Storico",
        "category": "Müze",
        "tags": ["moda", "ayakkabı", "tasarım", "tarihi saray"],
        "distanceFromCenter": 0.4,
        "lat": 43.7691,
        "lng": 11.2523,
        "price": "medium",
        "rating": 4.5,
        "description": "Dünyaca ünlü ayakkabı tasarımcısı Salvatore Ferragamo'nun hayatına ve tasarımlarına adanmış, tarihi Palazzo Spini Feroni içindeki şık müze.",
        "description_en": "A museum dedicated to the life and work of the legendary shoe designer Salvatore Ferragamo, situated in the historic Palazzo Spini Feroni.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Hollywood yıldızları için yapılmış orjinal ayakkabı kalıplarını burada görebilirsiniz.",
        "tips_en": "You can see the original shoe lasts made for famous Hollywood stars here."
    },
    {
        "name": "Gucci Osteria da Massimo Bottura",
        "name_en": "Gucci Osteria",
        "area": "Piazza della Signoria",
        "category": "Restoran",
        "tags": ["fine dining", "moda", "massimo bottura", "lüks"],
        "distanceFromCenter": 0.2,
        "lat": 43.7697,
        "lng": 11.2566,
        "price": "high",
        "rating": 4.6,
        "description": "Ünlü şef Massimo Bottura ve moda evi Gucci'nin işbirliğiyle kurulan, rengarenk tasarımı ve ödüllü mutfağıyla eşsiz bir deneyim sunan restoran.",
        "description_en": "A Michelin-starred restaurant born from a partnership between chef Massimo Bottura and Gucci, offering creative cuisine in a stunningly designed space.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Gucci Garden binasının içinde yer alır; hem sanat hem de gastronomi severler için rüya gibi bir noktadır.",
        "tips_en": "Located inside the Gucci Garden; a dream destination for both art and gastronomy lovers."
    },
    {
        "name": "Sant'Ambrogio Market",
        "name_en": "Sant'Ambrogio Market",
        "area": "Santa Croce",
        "category": "Deneyim",
        "tags": ["pazar", "lokal", "taze", "kalabalıktan uzak"],
        "distanceFromCenter": 1.0,
        "lat": 43.7715,
        "lng": 11.2660,
        "price": "low",
        "rating": 4.6,
        "description": "Floransa yerlilerinin gerçek alışverişini yaptığı, Mercato Centrale'ye göre daha az turistik ve daha samimi bir yerel pazar.",
        "description_en": "The authentic local market where Florentines do their shopping. Less touristy and more down-to-earth than Mercato Centrale.",
        "imageUrl": "https://images.unsplash.com/photo-1503431128566-66abc0cf0464?w=800",
        "bestTime": "Sabah (08:00 - 12:00)",
        "bestTime_en": "Morning (08:00 - 12:00)",
        "tips": "Pazarın içindeki 'Da Rocco' tezgahında çok uygun fiyata gerçek yerel öğle yemeği yiyebilirsiniz.",
        "tips_en": "Try a cheap and authentic lunch at the 'Da Rocco' stall inside the market."
    },
    {
        "name": "Piazza Santo Spirito",
        "name_en": "Piazza Santo Spirito",
        "area": "Oltrarno",
        "category": "Manzara",
        "tags": ["meydan", "bohem", "gece hayatı", "yerel"],
        "distanceFromCenter": 0.6,
        "lat": 43.7673,
        "lng": 11.2483,
        "price": "free",
        "rating": 4.7,
        "description": "Oltrarno bölgesinin bohem kalbi. Akşamları kafelerin sokağa taşan masaları ve yerel gençlerin toplandığı, Floransa'nın en yaşayan meydanı.",
        "description_en": "The bohemian heart of the Oltrarno district. The liveliest square in Florence, where locals gather in the evenings to socialize on cafe terraces.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Hafta sonları sabahları kurulan organik pazarları veya antika sergilerini kaçırmayın.",
        "tips_en": "Don't miss the organic markets or antique fairs held here on weekend mornings."
    },
    {
        "name": "Galleria Palatina",
        "name_en": "Palatine Gallery",
        "area": "Pitti Palace",
        "category": "Müze",
        "tags": ["sanat", "saray", "rafael", "tiziano"],
        "distanceFromCenter": 0.5,
        "lat": 43.7656,
        "lng": 11.2505,
        "price": "high",
        "rating": 4.8,
        "description": "Pitti Sarayı'nın içindeki görkemli galeri. Tabloların kronolojik değil, dekoratif olarak asıldığı orjinal saray düzenini koruyan nadir müzelerdendir.",
        "description_en": "A magnificent gallery inside Pitti Palace, preserved as an 18th-century princely collection with works by Raphael and Titian.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Biletle aynı zamanda Gümüş Müzesi ve Kostüm Müzesi'ne de girebilirsiniz.",
        "tips_en": "Your ticket also covers the Treasury of the Grand Dukes and the Costume Museum."
    },
    {
        "name": "Porcellino Market (Mercato Nuovo)",
        "name_en": "Porcellino Market",
        "area": "Centro Storico",
        "category": "Alışveriş",
        "tags": ["deri", "hediyelik", "pazar", "tarihi"],
        "distanceFromCenter": 0.2,
        "lat": 43.7696,
        "lng": 11.2536,
        "price": "medium",
        "rating": 4.3,
        "description": "16. yüzyıldan kalma revakların altında kurulan, deri çantalar ve ipek eşarplar bulabileceğiniz tarihi pazar yeri.",
        "description_en": "A historic covered market dating back to the 16th century, famous for its leather goods and artisanal souvenirs.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Pazarın köşesindeki meşhur bronz domuz heykelinin burnunu okşamayı unutmayın.",
        "tips_en": "Don't forget to rub the snout of the famous bronze pig (Porcellino) for good luck."
    },
    {
        "name": "Ditta Artigianale (Via de' Neri)",
        "name_en": "Ditta Artigianale",
        "area": "Santa Croce",
        "category": "Kafe",
        "tags": ["kahve", "3. dalga", "brunch", "trendy"],
        "distanceFromCenter": 0.4,
        "lat": 43.7685,
        "lng": 11.2574,
        "price": "medium",
        "rating": 4.5,
        "description": "Floransa'ya modern kahve kültürünü getiren, şık dekorasyonu ve başarılı kahvaltısıyla ünlü 3. dalga kahve dükkanı.",
        "description_en": "A pioneer of specialty coffee in Florence, offering high-quality roasts and great brunch options in a stylish, modern setting.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Sabah veya brunch",
        "bestTime_en": "Morning or brunch",
        "tips": "Genellikle dijital göçebelerin çalıştığı bir yerdir; kendi kavurdukları kahve çekirdeklerinden alabilirsiniz.",
        "tips_en": "A favorite for digital nomads; you can buy their own roasted coffee beans to go."
    },
    {
        "name": "La Ménagère",
        "name_en": "La Ménagère",
        "area": "San Lorenzo",
        "category": "Restoran",
        "tags": ["konsept dükkan", "çiçekçi", "tasarım", "gurme"],
        "distanceFromCenter": 0.3,
        "lat": 43.7745,
        "lng": 11.2552,
        "price": "high",
        "rating": 4.7,
        "description": "İçinde çiçekçi, ev dekorasyon dükkanı ve müzik sahnesi barındıran devasa bir konsept restoran. Floransa'nın en fotojenik iç mekanlarından birine sahiptir.",
        "description_en": "A stunning multi-concept space combining a flower shop, home decor store, and high-end bistro in a beautifully restored palazzo.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Akşamüzeri kokteyli veya yemek",
        "bestTime_en": "Afternoon cocktail or dinner",
        "tips": "Hiçbir şey yemeseniz bile içeri girip iç tasarımını görmelisiniz; piyano katında bazen caz konserleri olur.",
        "tips_en": "Step inside just to see the incredible interior design; catch live jazz on the lower floor some evenings."
    },
    {
        "name": "Volume",
        "name_en": "Volume",
        "area": "Oltrarno",
        "category": "Bar",
        "tags": ["bohem", "canlı müzik", "kitapçı", "alternatif"],
        "distanceFromCenter": 0.6,
        "lat": 43.7672,
        "lng": 11.2481,
        "price": "medium",
        "rating": 4.6,
        "description": "Eski bir heykel atölyesinin içine kurulmuş; bar, kütüphane ve canlı müzik mekanını birleştiren aşırı karakteristik bir nokta.",
        "description_en": "A highly characteristic spot in a former sculpture workshop, combining a bar, bookshop, and cultural space with live music.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Duvarlardaki ahşap heykel kalıpları buranın eski ruhunu yansıtır, çok samimi bir ortamı vardır.",
        "tips_en": "Note the wooden sculpture molds on the walls, reminders of the building's creative history."
    },
    {
        "name": "Manifattura Tabacchi",
        "name_en": "Manifattura Tabacchi",
        "area": "Cascine Park Civarı",
        "category": "Deneyim",
        "tags": ["modern sanat", "endüstriyel", "tasarım", "alternatif"],
        "distanceFromCenter": 2.5,
        "lat": 43.7850,
        "lng": 11.2330,
        "price": "low",
        "rating": 4.7,
        "description": "Eski bir tütün fabrikasının kültür ve sanat merkezine dönüştürülmesiyle oluşan, Floransa'nın 'cool' yüzünü temsil eden devasa kompleks.",
        "description_en": "A former tobacco factory transformed into a vibrant cultural hub, representing the contemporary and alternative side of Florence.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Hafta sonu",
        "bestTime_en": "Weekend",
        "tips": "Burada pop-up mağazalar, sanat galerileri ve harika butik bira mekanları bulabilirsiniz.",
        "tips_en": "Home to pop-up shops, art galleries, and some of the city's coolest craft beer spots."
    }
]

def enrich_floransa_batch1():
    filepath = 'assets/cities/floransa.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Cleanup fillers in existing highlights
    for h in data.get('highlights', []):
        if "Özenle düzenlenmiş koleksiyonu" in h['description'] or "tarihinin en parlak dönemlerinden kalma" in h['description'] or "Yerel yaşamın en canlı hali" in h['description']:
             if h['name'] == "Uffizi Galerisi":
                 h['description'] = "Dünyanın en eski ve en ünlü sanat müzelerinden biri. Botticelli'nin 'Venüs'ün Doğuşu' ve Leonardo da Vinci'nin başyapıtları burada sergilenir."
                 h['description_en'] = "One of the world's most important art museums, housing the greatest collection of Italian Renaissance masterpieces."
             if h['name'] == "Ponte Vecchio":
                 h['description'] = "Arno Nehri üzerindeki en eski ve ikonik köprü. Üzerindeki mücevher dükkanları ve II. Dünya Savaşı'ndan sağ çıkan tek Floransa köprüsü olmasıyla bilinir."
                 h['description_en'] = "The oldest and most iconic bridge over the Arno, unique for the jewelry shops lining its sides. The only Florentine bridge to survive WWII."
             if h['name'] == "Accademia Galerisi":
                 h['description'] = "Michelangelo'nun efsanevi 'David' heykelinin evi. Rönesans heykel sanatının zirvesini burada görebilirsiniz."
                 h['description_en'] = "The home of Michelangelo's legendary statue of David. A must-visit to see the pinnacle of Renaissance sculpture."
             if h['name'] == "Palazzo Pitti":
                 h['description'] = "Medici ailesinin muazzam sarayı. İçinde Palatina Galerisi ve Kraliyet Daireleri gibi 4 ayrı müze ve arkasında Boboli Bahçeleri bulunur."
                 h['description_en'] = "The former residence of the Medici family, housing several important museums and the magnificent Boboli Gardens."
             if h['name'] == "Boboli Bahçeleri":
                 h['description'] = "Rönesans bahçe sanatının en görkemli örneği. Sarayın arkasında uzanan, heykeller ve mağaralarla dolu devasa bir açık hava müzesi gibidir."
                 h['description_en'] = "A masterpiece of Renaissance garden design, featuring ornate statues, fountains, and grottos behind the Pitti Palace."
             if h['name'] == "Piazzale Michelangelo":
                 h['description'] = "Şehrin en iyi panoramik manzara noktası. Tüm Floransa'yı, Duomo'yu ve Arno nehrini buradan kuş bakışı izleyebilirsiniz."
                 h['description_en'] = "The most famous panoramic viewpoint in Florence, offering a breathtaking bird's-eye view of the entire city and its monuments."
             if h['name'] == "San Lorenzo Pazarı":
                 h['description'] = "Floransa'nın deri ürünleriyle ünlü tarihi pazarı. İsa'nın çilesini anlatan Medici Şapelleri'nin hemen yanı başındadır."
                 h['description_en'] = "The city's historic leather market, surrounding the Basilica of San Lorenzo and the famous Medici Chapels."
             if h['name'] == "Santa Croce Bazilikası":
                 h['description'] = "İtalyanların 'Ulusal Gurur Tapınağı'. Michelangelo, Galileo ve Machiavelli gibi dehaların anıt mezarlarına ev sahipliği yapar."
                 h['description_en'] = "The final resting place of Italian greats like Michelangelo, Galileo, and Machiavelli. Known as the 'Temple of Italian Glories'."
             if h['name'] == "Santo Spirito":
                 h['description'] = "Oltrarno'nun en samimi mahallesi ve aynı adlı Brunelleschi tasarımı kilisesiyle ünlü, gerçek Floransa ruhunu yansıtan meydan."
                 h['description_en'] = "The heart of the local Oltrarno district, centered around Brunelleschi's church and a vibrant, authentic neighborhood square."
             if h['name'] == "Palazzo Vecchio":
                 h['description'] = "Floransa'nın belediye binası ve kalesi. 94 metrelik kulesi (Torre d'Arnolfo) şehrin siluetindeki en belirgin yapılardan biridir."
                 h['description_en'] = "The historic town hall of Florence, a fortress-palace that has been the symbol of local power since the 13th century."
             if h['name'] == "Cappelle Medicee":
                 h['description'] = "Medici ailesinin görkemli mezar şapelleri. Michelangelo'nun tasarladığı 'Yeni Sagristi' ve devasa kubbeli 'Prensler Şapeli' büyüleyicidir."
                 h['description_en'] = "The opulent burial place of the Medici family, featuring Michelangelo's New Sacristy and the vast Chapel of the Princes."
             if h['name'] == "Gucci Garden Florence":
                 h['description'] = "Massimo Bottura'nın restoranı, interaktif sergiler ve Gucci mağazasını birleştiren moda ve sanatın kalbi."
                 h['description_en'] = "A creative hub by Alessandro Michele, featuring a museum of iconic Gucci designs and a restaurant by Massimo Bottura."

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_floransa_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_floransa_batch1()
print(f"Floransa now has {count} highlights.")
