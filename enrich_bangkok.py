import json
import os

new_bangkok_batch1 = [
    {
        "name": "MOCA (Museum of Contemporary Art)",
        "name_en": "MOCA Bangkok",
        "area": "Chatuchak",
        "category": "Müze",
        "tags": ["çağdaş sanat", "modern", "mimari", "tay sanatı"],
        "distanceFromCenter": 12.0,
        "lat": 13.8507,
        "lng": 100.563,
        "price": "medium",
        "rating": 4.8,
        "description": "Tayland'ın en büyük özel sanat müzesi. Benzersiz mimarisi ve muazzam Tay çağdaş sanat koleksiyonuyla görsel bir şölen sunar.",
        "description_en": "Thailand's largest private art museum. Known for its stunning modern architecture and a vast collection of contemporary Thai masterpieces.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Müze 5 kattan oluşuyor, en üst kattaki 'Evren' (Kingdom of Thailand) bölümünü kaçırmayın.",
        "tips_en": "The museum has 5 floors; don't miss the surreal 'Kingdom of Thailand' section on the top floor."
    },
    {
        "name": "Pak Khlong Talat (Çiçek Pazarı)",
        "name_en": "Pak Khlong Talat",
        "area": "Old City",
        "category": "Deneyim",
        "tags": ["çiçek", "pazar", "renkli", "gece"],
        "distanceFromCenter": 1.5,
        "lat": 13.7422,
        "lng": 100.4966,
        "price": "low",
        "rating": 4.6,
        "description": "Bangkok'un en büyük toptan çiçek pazarı. Gece yarısından sonra binlerce taze orkide, gül ve egzotik çiçeğin kokusu tüm sokağı sarar.",
        "description_en": "Bangkok's biggest wholesale flower market. After midnight, thousands of fresh orchids, roses, and exotic flowers create an incredible sensory experience.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Gece (01:00 - 04:00)",
        "bestTime_en": "Night (1:00 AM - 4:00 AM)",
        "tips": "Nehir teknesiyle Memorial Bridge terminalinde inerek kolayca ulaşabilirsiniz.",
        "tips_en": "Easily accessible by river boat, just hop off at the Memorial Bridge terminal."
    },
    {
        "name": "ICONSIAM (SookSiam)",
        "name_en": "SookSiam at ICONSIAM",
        "area": "Riverside",
        "category": "Alışveriş",
        "tags": ["yemek", "kültür", "lüks", "kapalı pazar"],
        "distanceFromCenter": 4.0,
        "lat": 13.7267,
        "lng": 100.5105,
        "price": "medium",
        "rating": 4.7,
        "description": "ICONSIAM'ın giriş katında yer alan, Tayland'ın 77 bölgesinden yerel yemek ve el sanatlarını bir araya getiren muazzam bir kapalı pazar alanı.",
        "description_en": "A massive indoor market area on the ground floor of ICONSIAM, bringing together food and crafts from all 77 provinces of Thailand.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Öğle veya Akşam yemeği",
        "bestTime_en": "Lunch or Dinner",
        "tips": "Dışarıdaki su şovu akşamları 18:30 ve 20:00 saatlerinde gerçekleşir, mutlaka izleyin.",
        "tips_en": "Watch the spectacular water show outside at 6:30 PM and 8:00 PM."
    },
    {
        "name": "BACC (Bangkok Art and Culture Centre)",
        "name_en": "BACC",
        "area": "Siam",
        "category": "Müze",
        "tags": ["sanat", "çağdaş", "ücretsiz", "tasarım"],
        "distanceFromCenter": 2.2,
        "lat": 13.7467,
        "lng": 100.5303,
        "price": "free",
        "rating": 4.5,
        "description": "Siam meydanının kalbinde, döner merdivenleri ve modern mimarisiyle dikkat çeken, sürekli değişen sergilere ev sahipliği yapan sanat merkezi.",
        "description_en": "A hub for contemporary art in the heart of Siam, featuring a spiral design and hosting ever-changing exhibitions from Thai and international artists.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Giriş ücretsizdir, içindeki butik kafeler ve sanat dükkanları çok kalitelidir.",
        "tips_en": "Entry is free; check out the small artisan shops and boutiques tucked within the floors."
    },
    {
        "name": "Wat Saket (Golden Mount)",
        "name_en": "Wat Saket",
        "area": "Old City",
        "category": "Tarihi",
        "tags": ["tapınak", "tepe", "manzara", "altın"],
        "distanceFromCenter": 2.0,
        "lat": 13.7539,
        "lng": 100.5083,
        "price": "low",
        "rating": 4.6,
        "description": "İnsan yapımı bir tepenin üzerinde yükselen, 300'den fazla basamakla çıkılan ve panoramik Bangkok manzarası sunan altın kubbeli tapınak.",
        "description_en": "An iconic gold chedi perched atop a man-made hill, offering panoramic views of old Bangkok after a climb of over 300 steps.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Merdivenleri çıkarken yol boyunca asılı olan onlarca çanı çalmak gelenektir.",
        "tips_en": "Ring the many bells along the stairway as you climb for good luck."
    },
    {
        "name": "Erawan Shrine (Phra Phrom)",
        "name_en": "Erawan Shrine",
        "area": "Siam",
        "category": "Tarihi",
        "tags": ["tapınak", "dua", "dans", "şehrin kalbi"],
        "distanceFromCenter": 2.5,
        "lat": 13.7444,
        "lng": 100.5404,
        "price": "free",
        "rating": 4.7,
        "description": "Lüks alışveriş merkezlerinin ortasında, modern hayatla geleneğin kesiştiği noktada yer alan, Tay dansçıların sürekli dua eşliğinde performans sergilediği kutsal alan.",
        "description_en": "A sacred Brahman shrine in the middle of a busy shopping district, famous for its traditional Thai dance performances and intense devotional energy.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Her zaman",
        "bestTime_en": "Anytime",
        "tips": "Dileği gerçekleşenlerin dansçılara sunduğu adakları izlemek ilginç bir deneyimdir.",
        "tips_en": "Watch the performance of traditional dancers commissioned by worshippers whose prayers have been answered."
    },
    {
        "name": "Taling Chan Floating Market",
        "name_en": "Taling Chan Market",
        "area": "Thonburi",
        "category": "Deneyim",
        "tags": ["yüzen pazar", "nehir yemeği", "lokal", "deniz ürünü"],
        "distanceFromCenter": 8.0,
        "lat": 13.7769,
        "lng": 100.4567,
        "price": "medium",
        "rating": 4.5,
        "description": "Şehir merkezine en yakın yüzen pazar. Nehir kenarında oturan yerlilerin teknelerde pişirdiği taze deniz ürünlerini yiyebileceğiniz samimi bir nokta.",
        "description_en": "The closest floating market to central Bangkok, offering a more local feel than the larger ones. Famous for fresh seafood cooked on boat-kitchens.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Hafta sonu öğle",
        "bestTime_en": "Weekend lunch",
        "tips": "Buradan kalkan küçük kanal turlarına (long-tail boat) katılarak yerel yaşamı su üzerinden görebilirsiniz.",
        "tips_en": "Take a long-tail boat tour from here to explore the peaceful surrounding canals (khlongs)."
    },
    {
        "name": "Jay Fai (Raan Jay Fai)",
        "name_en": "Jay Fai",
        "area": "Old City",
        "category": "Restoran",
        "tags": ["michelin", "street food", "yengeç omlet", "efsane"],
        "distanceFromCenter": 1.5,
        "lat": 13.7561,
        "lng": 100.5029,
        "price": "high",
        "rating": 4.6,
        "description": "Dünyanın en ünlü sokak yemeği şefi. Kayak gözlükleriyle dev wokların önünde yengeçli omlet yapan Jay Fai, Michelin yıldızlı bir efsanedir.",
        "description_en": "A Michelin-starred street food legend. Chef Jay Fai is world-famous for her crab omelets and her distinctive ski-goggles worn over open charcoal fires.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Rezervasyonsuz gitmek genellikle saatlerce beklemek demektir, önceden plan yapın.",
        "tips_en": "Table reservations are extremely limited; be prepared to wait for several hours if you go without one."
    },
    {
        "name": "Wattana Panich (Beef Broth)",
        "name_en": "Wattana Panich",
        "area": "Ekkamai",
        "category": "Restoran",
        "tags": ["çorba", "tarihi lezzet", "yerel", "beef stew"],
        "distanceFromCenter": 8.0,
        "lat": 13.7297,
        "lng": 100.5843,
        "price": "low",
        "rating": 4.7,
        "description": "40 yılı aşkın süredir aynı kazanda kaynamaya devam eden efsanevi sığır eti çorbası. Bangkok'un en özel gastronomi duraklarından biridir.",
        "description_en": "Famous for its massive copper pot containing a beef stew that has been simmering for over 40 years. A true cult destination for foodies.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Öğle yemeği",
        "bestTime_en": "Lunch",
        "tips": "Girişteki dev kazanı mutlaka görün, çorbanın derin lezzeti sizi şaşırtacak.",
        "tips_en": "Be sure to look at the massive pot at the entrance; the depth of flavor in the broth is unparalleled."
    },
    {
        "name": "Yaowarat Road (Gece Yemekleri)",
        "name_en": "Yaowarat Street Food",
        "area": "Chinatown",
        "category": "Deneyim",
        "tags": ["sokak yemeği", "neon", "gece", "chinatown"],
        "distanceFromCenter": 2.0,
        "lat": 13.7411,
        "lng": 100.5083,
        "price": "low",
        "rating": 4.8,
        "description": "Dünyanın en iyi sokak yemeği bölgelerinden biri. Hava karardığında neon ışıkları altında yüzlerce tezgah egzotik tatlar sunar.",
        "description_en": "One of the world's premier street food destinations. At night, the street transforms into a neon-lit open-air food hall with hundreds of vendors.",
        "imageUrl": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=800",
        "bestTime": "Gece (19:00 - 23:00)",
        "bestTime_en": "Night (7:00 PM - 11:00 PM)",
        "tips": "Firkonlu kızarmış çörekleri ve meşhur istiridye omletini tatmadan dönmeyin.",
        "tips_en": "Don't miss the legendary rolled noodles or the famous toasted buns with various fillings."
    },
    {
        "name": "Lumpini Park (Varano Gözlemi)",
        "name_en": "Lumpini Park",
        "area": "Silom",
        "category": "Park",
        "tags": ["doğa", "spor", "varan kertenkelesi", "yeşil alan"],
        "distanceFromCenter": 3.0,
        "lat": 13.7306,
        "lng": 100.5417,
        "price": "free",
        "rating": 4.6,
        "description": "Gökdelenlerin arasında bir vaha. Göl kenarında devasa varan kertenkelelerinin güneşlenişini izleyebileceğiniz huzurlu bir nokta.",
        "description_en": "A peaceful oasis amidst the skyscrapers. Famous for the large water monitor lizards that freely roam the park and sunbathe by the lake.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Sabah erken veya Akşamüzeri",
        "bestTime_en": "Early morning or Late afternoon",
        "tips": "Akşam saat 18:00'de milli marş çalındığında herkesin durup saygı duruşuna geçişini izlemek etkileyici bir kültürel andır.",
        "tips_en": "At 6:00 PM every day, the national anthem plays and the entire park comes to a complete standstill in collective respect."
    },
    {
        "name": "The Giant Swing (Sao Ching Cha)",
        "name_en": "The Giant Swing",
        "area": "Old City",
        "category": "Tarihi",
        "tags": ["ikon", "mimari", "törensellik", "tarihi"],
        "distanceFromCenter": 1.2,
        "lat": 13.7512,
        "lng": 100.5008,
        "price": "free",
        "rating": 4.4,
        "description": "Geçmişte dini törenler için kullanılan, 21 metre yüksekliğindeki devasa kırmızı tik ağacı yapı. Bangkok'un en ikonik sembollerinden biridir.",
        "description_en": "A 21-meter tall teak structure that was once used in religious ceremonies. It remains one of the most recognizable landmarks of the city.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Akşam (Işıklandırıldığında)",
        "bestTime_en": "Evening (When lit up)",
        "tips": "Hemen yanındaki Wat Suthat tapınağı, şehrin en büyük ve en güzel iç avlularından birine sahiptir.",
        "tips_en": "The adjacent Wat Suthat temple has one of the largest and most tranquil courtyards in the city."
    },
    {
        "name": "Manifattura (Jodd Fairs Rama 9)",
        "name_en": "Jodd Fairs",
        "area": "Rama 9",
        "category": "Deneyim",
        "tags": ["gece pazarı", "yemek", "vintage", "trendy"],
        "distanceFromCenter": 4.0,
        "lat": 13.7656,
        "lng": 100.5654,
        "price": "medium",
        "rating": 4.7,
        "description": "Bangkok'un en popüler yeni nesil gece pazarı. Beyaz çadırları, canlı müziği ve sonsuz sokak yemeği seçenekleriyle gerçek bir enerji patlaması.",
        "description_en": "Bangkok's trendiest new night market. Known for its white tents, vibrant live music, and an incredible array of creative street food stalls.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Akşam (20:00 - 23:00)",
        "bestTime_en": "Evening (8:00 PM - 11:00 PM)",
        "tips": "Meşhur 'Leng Zabb' (dağ gibi acılı sığır omurgası) yemeğini mutlaka deneyin, ama acısına hazırlıklı olun.",
        "tips_en": "Try the famous 'Leng Zabb' (spicy pork spine soup piled high like a mountain), but beware of the heat!"
    },
    {
        "name": "Mahanakhon Skywalk (Sky Beach)",
        "name_en": "Mahanakhon Skywalk",
        "area": "Sathorn",
        "category": "Manzara",
        "tags": ["gökdelen", "cam taban", "rooftop", "adrenalin"],
        "distanceFromCenter": 4.0,
        "lat": 13.7243,
        "lng": 100.5296,
        "price": "high",
        "rating": 4.5,
        "description": "Taylor'ın en yüksek binasında, 314 metre yükseklikte cam bir balkon üzerinde yürüme deneyimi. Şehri ayaklarınızın altında hissedin.",
        "description_en": "Located on top of Thailand's tallest building, this experience features a glass-bottomed observation deck at 314 meters above the ground.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gün batımı öncesi",
        "bestTime_en": "Just before sunset",
        "tips": "Ayakkabı kılıflarını giymeniz zorunludur ve camın üzerine telefon veya kamera sokamazsınız.",
        "tips_en": "You must wear shoe covers provided, and phones or cameras are not allowed directly onto the glass floor area."
    },
    {
        "name": "Wat Benchamabophit (Marble Temple)",
        "name_en": "The Marble Temple",
        "area": "Dusit",
        "category": "Tarihi",
        "tags": ["tapınak", "mermer", "saray civarı", "fotojenik"],
        "distanceFromCenter": 3.0,
        "lat": 13.7666,
        "lng": 100.5141,
        "price": "medium",
        "rating": 4.6,
        "description": "İtalyan mermerinden inşa edilen, simetrik yapısı ve görkemli duruşuyla Bangkok'un en estetik tapınaklarından biri.",
        "description_en": "Constructed from Italian Carrara marble, this temple is renowned for its symmetrical beauty and elegant, high-pitched roof design.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Sabah (08:00 - 10:00)",
        "bestTime_en": "Morning (8:00 AM - 10:00 AM)",
        "tips": "Ana salonun arkasındaki galeride 52 farklı Buda heykelini bir arada görebilirsiniz.",
        "tips_en": "The cloister in the back contains 52 different Buddha statues showing various historical styles."
    },
    {
        "name": "Octave Rooftop Bar (Marriott Thong Lo)",
        "name_en": "Octave Rooftop",
        "area": "Thong Lo",
        "category": "Bar",
        "tags": ["rooftop", "manzara", "kokteyl", "lüks"],
        "distanceFromCenter": 8.0,
        "lat": 13.7245,
        "lng": 100.5786,
        "price": "high",
        "rating": 4.7,
        "description": "360 derecelik kesintisiz şehir manzarası sunan, hiçbir cam engel olmadan yıldızların altında kokteyl içebileceğiniz en iyi rooftop'lardan biri.",
        "description_en": "A multi-level sky bar offering unobstructed 360-degree views of the city. One of the best places for sunset cocktails in Bangkok.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Akşam saatlerinde giderseniz 49. kattaki en üst terası tercih edin.",
        "tips_en": "Head to the absolute top floor (49th) for the best views and a dedicated DJ booth vibe."
    },
    {
        "name": "Thong Lo Neighborhood (Trendy Area)",
        "name_en": "Thong Lo Area",
        "area": "Sukhumvit",
        "category": "Deneyim",
        "tags": ["trendy", "gece hayatı", "kafe", "lüks"],
        "distanceFromCenter": 7.0,
        "lat": 13.7242,
        "lng": 100.5786,
        "price": "high",
        "rating": 4.6,
        "description": "Bangkok'un en 'cool' bölgesi. Tasarım cafeleri, gizli kokteyl barları ve şehrin en şık restoranlarının bulunduğu Sukhumvit'in kalbi.",
        "description_en": "The trendiest neighborhood in Bangkok, filled with concept cafes, hidden speakeasies, and the city's most fashionable dining spots.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Akşam veya Hafta sonu brunch",
        "bestTime_en": "Evening or weekend brunch",
        "tips": "Soi 55 boyunca yürüyerek ara sokaklardaki butikleri ve konsept mağazaları keşfedin.",
        "tips_en": "Wander down the small alleys (sois) off the main road to find the best hidden bars and cafe gems."
    },
    {
        "name": "Ari Neighborhood (Lo-fi Vibes)",
        "name_en": "Ari Neighborhood",
        "area": "Phaya Thai",
        "category": "Deneyim",
        "tags": ["bohem", "kafe kültürü", "sessiz", "lokal"],
        "distanceFromCenter": 5.0,
        "lat": 13.7797,
        "lng": 100.5446,
        "price": "medium",
        "rating": 4.7,
        "description": "Modern ama huzurlu. Eski villaların tasarım ofislerine ve butik kafelere dönüştüğü, gerçek Bangkok ruhunu taşıyan sakin mahalle.",
        "description_en": "A charming, laid-back neighborhood where old wooden villas sit alongside third-wave coffee shops and boutique bakeries.",
        "imageUrl": "https://images.unsplash.com/photo-1514525253361-bee1a2399222?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "BTS Ari durağından inip Soi 1-4 arasını yürüyerek gezmek en keyiflisidir.",
        "tips_en": "Wander the leafy sub-sois 1 through 4 to find the best quiet spots for coffee and local eats."
    },
    {
        "name": "Somtum Der (Michelin Bib Gourmand)",
        "name_en": "Somtum Der",
        "area": "Silom",
        "category": "Restoran",
        "tags": ["isen yemeği", "papaya salatası", "acılı", "yerel"],
        "distanceFromCenter": 3.0,
        "lat": 13.7329,
        "lng": 100.5395,
        "price": "medium",
        "rating": 4.5,
        "description": "Kuzeydoğu Tayland (Isan) mutfağının en iyi örneklerini sunan modern ve ödüllü bir restoran. Papaya salataları meşhurdur.",
        "description_en": "A vibrant restaurant specializing in authentic Isan (Northeastern Thai) cuisine. Famous for its incredible variety of papaya salads (somtum).",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Öğle veya Akşam",
        "bestTime_en": "Lunch or Dinner",
        "tips": "Acı seviyenizi sipariş verirken mutlaka belirtin, Isan mutfağı oldukça baharatlıdır.",
        "tips_en": "Specify your spice level; traditional Isan dishes can be extremely hot if you aren't careful."
    },
    {
        "name": "Tealicious Bangkok",
        "name_en": "Tealicious",
        "area": "Riverside",
        "category": "Restoran",
        "tags": ["geleneksel", "tay mutfağı", "samimi", "popüler"],
        "distanceFromCenter": 3.5,
        "lat": 13.7196,
        "lng": 100.5152,
        "price": "medium",
        "rating": 4.8,
        "description": "Nehir yakınında, her zaman taze malzemelerle hazırlanan klasik Tay yemeklerini ev sıcaklığında sunan çok sevilen bir adres.",
        "description_en": "A highly-rated gem near the river, known for its warm hospitality and perfectly executed Thai classics like Massaman curry.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Masaman körisi ve Pad Thai buranın en çok tercih edilen lezzetleridir.",
        "tips_en": "Their Massaman curry is often cited as one of the best in the city; booking is recommended for dinner."
    },
    {
        "name": "Gaggan Anand (Progressive Cuisine)",
        "name_en": "Gaggan Anand",
        "area": "Sukhumvit",
        "category": "Restoran",
        "tags": ["ince gastronomi", "dünya çapında", "deneyim", "lüks"],
        "distanceFromCenter": 5.0,
        "lat": 13.7346,
        "lng": 100.5402,
        "price": "high",
        "rating": 4.9,
        "description": "Defalarca Asya'nın en iyi restoranı seçilen, sadece yemek değil moleküler gastronomi şovu sunan dünyaca ünlü bir deneyim.",
        "description_en": "Regularly voted the best restaurant in Asia, Gaggan offers a progressive and theatrical multi-course emoji-menu dining experience.",
        "imageUrl": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "bestTime": "Özel akşam yemeği",
        "bestTime_en": "Special Dinner",
        "tips": "Aylar öncesinden rezervasyon gerektirir, hazırlıklı olun.",
        "tips_en": "Booking months in advance is mandatory; it's more of a culinary performance than just a meal."
    },
    {
        "name": "Pe Aor Tom Yum Kung",
        "name_en": "Pe Aor Tom Yum",
        "area": "Phaya Thai",
        "category": "Restoran",
        "tags": ["tom yum", "deniz ürünü", "yerel", "ödüllü"],
        "distanceFromCenter": 3.0,
        "lat": 13.7531,
        "lng": 100.5342,
        "price": "medium",
        "rating": 4.4,
        "description": "Bangkok'un en iyi Tom Yum çorbalarından birini yapan yer. İçinde dev karidelerin olduğu kremamsı ve yoğun lezzetli çorbasıyla tanınır.",
        "description_en": "Famous for serving what many consider the best Tom Yum Kung in the city, with a rich, creamy broth and giant king prawns.",
        "imageUrl": "https://images.unsplash.com/photo-1550966842-28df0503043d?w=800",
        "bestTime": "Öğle yemeği",
        "bestTime_en": "Lunch",
        "tips": "Dükkanın duvarları Jay Fai gibi ünlülerin ve ödüllerin fotoğraflarıyla doludur.",
        "tips_en": "Don't be put off by the unassuming entrance; their award-winning lobster Tom Yum is epic."
    },
    {
        "name": "Phra Sumen Fort",
        "name_en": "Phra Sumen Fort",
        "area": "Old City",
        "category": "Tarihi",
        "tags": ["kale", "park", "nehir", "tarihi yapılar"],
        "distanceFromCenter": 2.0,
        "lat": 13.7640,
        "lng": 100.4957,
        "price": "free",
        "rating": 4.5,
        "description": "18. yüzyıldan kalma, nehir kıyısındaki bembeyaz görkemli kale kalıntısı. Çevresindeki park yerlilerin dinlenme noktasıdır.",
        "description_en": "A beautiful white hexagonal fort built in 1783, standing in a small green park overlooking the river.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Akşamüzeri",
        "bestTime_en": "Late afternoon",
        "tips": "Hemen yanındaki Phra Athit Road, çok şık eski tarz kafelere ve butik otellere ev sahipliği yapar.",
        "tips_en": "The nearby Phra Athit Road is home to many cozy, atmospheric cafes and small guesthouses."
    }
]

def enrich_bangkok_batch1():
    filepath = 'assets/cities/bangkok.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Cleanup fillers in existing highlights
    for h in data.get('highlights', []):
        if "tarihinin en parlak dönemlerinden" in h['description'] or "zengin tarihine tanıklık eden" in h['description'] or "bir noktada yer almalı" in h['description'] or "ideal bir tercih" in h['description']:
             if h['name'] == "Grand Palace":
                 h['description'] = "Tayland'ın en kutsal saray kompleksi. 1782'den beri kraliyet ikametgahı olan bu muazzam yapı, Zümrüt Buda Tapınağı'na da ev sahipliği yapar."
                 h['description_en'] = "The spiritual heart of the Thai Kingdom. A spectacular complex of buildings that has been the official residence of the Kings of Siam since 1782."
             if h['name'] == "Wat Pho":
                 h['description'] = "46 metre uzunluğundaki devasa Yatan Buda heykeliyle ünlü. Aynı zamanda geleneksel Tay masajının doğum yeri kabul edilir."
                 h['description_en'] = "Home to the magnificent 46-meter long Reclining Buddha and the world-renowned school of traditional Thai massage."
             if h['name'] == "Wat Arun":
                 h['description'] = "Chao Phraya Nehri kıyısında yükselen, porselenlerle süslü görkemli kuleleriyle 'Şafak Tapınağı' olarak bilinen ikonik yapı."
                 h['description_en'] = "Known as the Temple of Dawn, its majestic prang (spire) decorated with colorful porcelain is one of Bangkok's most famous landmarks."
             if h['name'] == "Chatuchak Pazarı":
                 h['description'] = "Dünyanın en büyük hafta sonu pazarı. 15.000'den fazla tezgahta kıyafetten egzotik hayvanlara kadar her şeyi bulabilirsiniz."
                 h['description_en'] = "One of the world's largest weekend markets, featuring over 15,000 stalls selling everything from fashion to home decor."
             if h['name'] == "Khao San Road":
                 h['description'] = "Sırt çantalı gezginlerin dünya çapındaki merkezi. Canlı gece hayatı, ucuz sokak yemekleri ve kozmopolit atmosferiyle ünlüdür."
                 h['description_en'] = "The world-famous backpacker hub, known for its high-energy nightlife, street food stalls, and international vibe."
             if h['name'] == "Chinatown (Yaowarat)":
                 h['description'] = "Bangkok'un en renkli ve kaotik bölgesi. Gece çöktüğünde dünyanın en büyük açık hava restoranına dönüşen bir lezzet durağı."
                 h['description_en'] = "A sensory explosion of neon lights, gold shops, and endless street food stalls offering some of the best flavors in the city."
             if h['name'] == "Chao Phraya Nehri Teknesi":
                 h['description'] = "Şehri keşfetmenin en keyifli yolu. Yerel teknelerle nehir boyunca tapınakları ve otelleri izleyerek seyahat edebilirsiniz."
                 h['description_en'] = "The best way to navigate the city, offering a scenic journey past glowing temples and historic waterfront communities."
             if h['name'] == "Floating Market":
                 h['description'] = "Tayland'ın geleneksel su üzerindeki pazar kültürü. Kanallarda süzülen teknelerden meyve ve yerel yemekler alabilirsiniz."
                 h['description_en'] = "A traditional Thai market where vendors sell fresh produce and cooked food directly from their small wooden boats."
             if h['name'] == "Rooftop Barlar":
                 h['description'] = "Bangkok siluetini 360 derece izleyebileceğiniz, lüx kokteyller sunan gökyüzü barları şehrin imza deneyimlerinden biridir."
                 h['description_en'] = "Breathtaking sky bars offering panoramic views of the illuminated cityscape, perfect for a sophisticated evening cocktail."
             if h['name'] == "Thai Masaj":
                 h['description'] = "Yüzyıllık geleneksel şifa yöntemi. Vücudu esneten ve enerjiyi tazeleyen benzersiz bir terapi deneyimi."
                 h['description_en'] = "The ancient art of healing and relaxation, a unique therapy session that combines acupressure and yoga-like stretching."
             if h['name'] == "Jim Thompson House":
                 h['description'] = "Tay ipeğini dünyaya tanıtan Amerikalı iş adamının orjinal Tay evlerinden oluşan, tropikal bahçe içindeki muazzam müze evi."
                 h['description_en'] = "A stunning complex of historic Thai houses and art collections set in a lush garden, once the home of the 'Silk King'."
             if h['name'] == "Lumpini Park":
                 h['description'] = "Şehrin ortasındaki devasa yeşil alan. Gölü, yürüyüş yolları ve serbestçe dolaşan varan kertenkeleleriyle huzur noktası."
                 h['description_en'] = "Bangkok's green heart, offering a peaceful escape from the traffic with its large lake and friendly resident monitor lizards."
             if h['name'] == "MBK Center":
                 h['description'] = "Elektronikten hediyelik eşyaya kadar her şeyin bulunduğu, pazarlık kültürünün hala yaşadığı Bangkok'un en ikonik AVM'lerinden biri."
                 h['description_en'] = "A legendary shopping mall known for its incredible variety of electronics, mobile phones, and discount fashion."
             if h['name'] == "Asiatique The Riverfront":
                 h['description'] = "Nehir kıyısında eski bir rıhtımın açık hava pazar ve eğlence merkezine dönüştürülmüş hali. Dev dönme dolabıyla tanınır."
                 h['description_en'] = "A large open-air mall by the river combining shopping, dining, and entertainment, including a famous Ferris wheel."
             if h['name'] == "Wat Saket":
                 h['description'] = "Altın Dağ (Golden Mount) olarak bilinen, tepesinden Bangkok'un tüm eski yerleşimini görebileceğiniz panoramik tapınak."
                 h['description_en'] = "A shimmering gold chedi on a man-made hill that provides one of the best 360-degree viewpoints over old Bangkok."
             if h['name'] == "Soi Cowboy":
                 h['description'] = "Bangkok'un ünlü neon ışıklı gece hayatı sokağı. 'Hangover 2' filmiyle dünya çapında popülerlik kazanmıştır."
                 h['description_en'] = "A short but incredibly bright nightlife street famous for its neon-lit atmosphere and internationally recognized bars."
             if h['name'] == "Terminal 21 Asok":
                 h['description'] = "Her katı farklı bir dünya şehrini (İstanbul, Londra, Tokyo vb.) temsil eden benzersiz konseptli alışveriş merkezi."
                 h['description_en'] = "A unique travel-themed mall where each floor is designed after a famous world city like Rome, London, or Tokyo."
             if h['name'] == "ICONSIAM":
                 h['description'] = "Bangkok'un en lüks AVM'si. Sadece alışveriş değil, kapalı yüzen pazarı ve muhteşem su gösterileriyle tam bir deneyim merkezi."
                 h['description_en'] = "A mega-luxury destination on the riverside featuring high-end brands and the incredible SookSiam indoor heritage market."
             if h['name'] == "Wat Benchamabophit":
                 h['description'] = "İtalyan mermerinden yapılan, bembeyaz görkemli yapısıyla 'Mermer Tapınak' olarak bilinen Bangkok'un en güzel mimarilerinden biri."
                 h['description_en'] = "Known as the Marble Temple, its elegant symmetry and white Italian marble make it one of the most beautiful sights in the city."
             if h['name'] == "Pak Khlong Talat":
                 h['description'] = "Sadece geceleri tam kapasite çalışan, binlerce taze çiçek ve egzotik kokunun birleştiği dünyanın en büyük çiçek pazarlarından biri."
                 h['description_en'] = "Thailand's largest wholesale flower market, a vibrant 24-hour sensory explosion that is at its busiest after midnight."
             if h['name'] == "Ayutthaya Historical Park":
                 h['description'] = "Bangkok'a 1 saat mesafede, Siyam Krallığı'nın eski başkentinin görkemli tapınak kalıntılarını barındıran UNESCO dünya mirası."
                 h['description_en'] = "A UNESCO World Heritage site featuring the majestic ruins of the second capital of the Siamese Kingdom, just north of Bangkok."
             if h['name'] == "Mahanakhon SkyWalk":
                 h['description'] = "Şehrin en yüksek noktasında, cam tabanlı balkon üzerinde yürüme heyecanı yaşayabileceğiniz modern bir manzara platformu."
                 h['description_en'] = "Experience incredible views from Thailand's highest observation deck, featuring a thrilling glass tray floor high above the streets."
             if h['name'] == "Siam Paragon":
                 h['description'] = "Lüks markaların, devasa bir akvaryumun ve güneydoğu Asya'nın en büyük sinemalarından birinin bulunduğu prestijli AVM."
                 h['description_en'] = "A premier luxury shopping destination housing elite global brands and one of Southeast Asia's largest aquariums."
             if h['name'] == "Jodd Fairs":
                 h['description'] = "Bangkok'un en popüler yeni nesil gece pazarı. Beyaz çadırları ve yaratıcı sokak yemekleriyle modern bir enerji noktası."
                 h['description_en'] = "The trendiest new night market in the city, famous for its lively atmosphere, vintage finds, and innovative street food stalls."
             if h['name'] == "Maeklong Railway Market":
                 h['description'] = "Rayların tam üzerine kurulan, tren geçtiğinde saniyeler içinde toplanıp tekrar açılan dünyanın en ilginç pazarlarından biri."
                 h['description_en'] = "An incredible market built on active railway tracks, where vendors pull back their awnings just as the train passes through."
             if h['name'] == "Wat Traimit":
                 h['description'] = "5.5 ton ağırlığındaki dünyanın en büyük saf altın Buda heykeline ev sahipliği yapan görkemli tapınak."
                 h['description_en'] = "Home to the world's largest solid gold Buddha statue, weighing 5.5 tons and dating back to the Sukhothai period."
             if h['name'] == "Erawan Shrine":
                 h['description'] = "Gökdelenlerin arasında, Tay dansçıların performansı eşliğinde dua edilen şehrin en kutsal ve mistik noktalarından biri."
                 h['description_en'] = "A highly revered Brahman shrine famously host to daily traditional Thai dance performances offered by grateful worshippers."
             if h['name'] == "Rajadamnern Stadium":
                 h['description'] = "Muay Thai dövüş sanatının ruhanî evi. Gerçek boks maçlarını tarihin en eski stadyumunda izleme fırsatı sunar."
                 h['description_en'] = "The legendary home of Muay Thai. Watching a live fight here is an intense and authentic cultural experience like no other."
             if h['name'] == "Ancient City (Muang Boran)":
                 h['description'] = "Tayland'ın tüm tarihi yapılarını tek bir alanda görebileceğiniz dünyanın en büyük açık hava müzesi."
                 h['description_en'] = "The world's largest open-air museum, featuring replicas and original structures of Thailand's most famous historic sites."
             if h['name'] == "Erawan Museum":
                 h['description'] = "Üç başlı devasa fil heykeliyle tanınan, içindeki mistik sanat eserleri ve tavan süslemeleriyle büyüleyen benzersiz müze."
                 h['description_en'] = "An extraordinary museum housed inside a gargantuan three-headed copper elephant statue, filled with priceless religious artifacts."
             if h['name'] == "Wat Suthat & Giant Swing":
                 h['description'] = "Devasa kırmızı salıncağı ve duvar resimleriyle ünlü, Bangkok'un en büyük ve en önemli kraliyet tapınaklarından biri."
                 h['description_en'] = "One of the most important royal temples in the city, famous for its towering red Giant Swing located at the entrance."
             if h['name'] == "CentralWorld":
                 h['description'] = "Dünyanın en büyük alışveriş merkezlerinden biri. Yüzlerce mağaza, restoran ve buz pistiyle devasa bir yaşam alanı."
                 h['description_en'] = "One of the largest shopping complexes in the world, a massive destination for lifestyle, dining, and global brands."
             if h['name'] == "Bangkok Art and Culture Centre":
                 h['description'] = "Çağdaş sanatın merkezi. Devasa galerileri, sanat kitapçıları ve butik kafeleriyle yaratıcı bir mola noktası."
                 h['description_en'] = "A center for modern creativity, this museum features high-ceiling galleries and a community of independent art shops."
             if h['name'] == "Pratunam Market":
                 h['description'] = "Bangkok'un en büyük giyim pazarı. Ucuz alışverişin adresi olan bu pazar, gün boyu inanılmaz bir hareketliliğe sahiptir."
                 h['description_en'] = "Thailand's largest textile market, a chaotic and vibrant wholesale hub for incredibly affordable fashion and accessories."
             if h['name'] == "Platinum Fashion Mall":
                 h['description'] = "Modern ve klimalı toptan tekstil merkezi. Binlerce butik arasından en trend kıyafetleri uygun fiyata bulabilirsiniz."
                 h['description_en'] = "A massive and modern wholesale fashion mall, perfect for those scouting the latest trends at affordable bulk-prices."
             if h['name'] == "Talad Noi":
                 h['description'] = "Chinatown'un kıyısında, sokak sanatları ve eski motor parçalarıyla dolu labirent sokaklarında tarih kokan bir mahalle."
                 h['description_en'] = "A historic waterfront neighborhood filled with narrow alleys, hidden street art, and decades-old charm around every corner."
             if h['name'] == "MOCA Museum of Contemporary Art Bangkok":
                 h['description'] = "Tayland'ın en büyük özel sanat müzesi. Devasa tabloları ve gerçeküstü heykelleriyle modern bir tapınak gibidir."
                 h['description_en'] = "A world-class art museum dedicated to Thai contemporary masters, set within a breathtakingly designed modern building."

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_bangkok_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_bangkok_batch1()
print(f"Bangkok now has {count} highlights.")
