import json
import os

new_cenevre_batch1 = [
    {
        "name": "Île Rousseau",
        "name_en": "Rousseau Island",
        "area": "Göl / Limmat",
        "category": "Park",
        "tags": ["ada", "heykel", "huzur", "manzara"],
        "distanceFromCenter": 0.2,
        "lat": 46.2057,
        "lng": 6.1465,
        "price": "free",
        "rating": 4.5,
        "description": "Limmat nehrinin göle birleştiği noktada yer alan, ünlü filozof Jean-Jacques Rousseau'nun heykeline ev sahipliği yapan huzurlu küçük bir ada.",
        "description_en": "A peaceful small island at the confluence of the lake and the Rhône river, named after and featuring a bronze statue of the philosopher Jean-Jacques Rousseau.",
        "imageUrl": "https://images.unsplash.com/photo-1595995204423-66286756854e?w=800",
        "bestTime": "Günün her saati",
        "bestTime_en": "Anytime",
        "tips": "Adadaki restoranda göl manzarasına karşı bir şeyler içmek oldukça keyiflidir.",
        "tips_en": "The island's terrace restaurant is a perfect spot for a quiet drink with a unique view of the Jet d'Eau."
    },
    {
        "name": "Bordier-Brunnen",
        "name_en": "Bordier Fountain",
        "area": "Vieille Ville",
        "category": "Tarihi",
        "tags": ["çeşme", "heykel", "gizli", "ortaçağ"],
        "distanceFromCenter": 0.1,
        "lat": 46.2012,
        "lng": 6.1481,
        "price": "free",
        "rating": 4.4,
        "description": "Eski şehrin dar sokaklarında gizlenmiş, 18. yüzyıldan kalma çok şık ve detaylı bir tarihi çeşme.",
        "description_en": "A beautifully detailed 18th-century fountain tucked away in the narrow alleys of Geneva's Old Town, representing the city's rich history.",
        "imageUrl": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Bu çeşmenin suyu içilebilir; eski şehir yürüyüşünde şişenizi doldurmak için idealdir.",
        "tips_en": "The water here is fresh and drinkable; it's a great spot to refill your bottle while exploring the cobblestone streets."
    },
    {
        "name": "Passage des Degrés-de-Poules",
        "name_en": "Passage des Degres-de-Poules",
        "area": "Vieille Ville",
        "category": "Tarihi",
        "tags": ["merdiven", "dar sokak", "nostalji", "gizli geçit"],
        "distanceFromCenter": 0.1,
        "lat": 46.2014,
        "lng": 6.1478,
        "price": "free",
        "rating": 4.6,
        "description": "Katedrale çıkan, gizli görünümlü ve oldukça dik, çok dar bir tarihi merdivenli geçit.",
        "description_en": "A narrow, steep, and atmospheric covered staircase leading up to Saint-Pierre Cathedral, feeling like a secret passage from the Middle Ages.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Yukarı çıkarken her basamakta şehrin ortaçağ havasını daha çok hissedeceksiniz, dikkatli tırmanın.",
        "tips_en": "The climb is steep but very photogenic; it's one of the most authentic medieval shortcuts in the city."
    },
    {
        "name": "Musée Ariana (Dış Cephe)",
        "name_en": "Ariana Museum Architecture",
        "area": "Nations",
        "category": "Tarihi",
        "tags": ["mimari", "saray", "kubbe", "park"],
        "distanceFromCenter": 2.6,
        "lat": 46.2255,
        "lng": 6.1385,
        "price": "free",
        "rating": 4.7,
        "description": "İçindeki seramikler kadar dış mimarisi ve tavan süslemeleriyle de büyüleyen, saray görünümlü muazzam bir müze binası.",
        "description_en": "An architectural masterpiece resembling a palace, known for its grand dome and ornate ceilings, housing an extensive ceramics collection.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Müzeye girmeseniz bile parkın içinde yer alan bu binanın etrafında dolaşmak ve mimari detayları incelemek serbesttir.",
        "tips_en": "Even if you don't visit the exhibits, the building itself and its surrounding park are free to explore and very impressive."
    },
    {
        "name": "Brunswick Monument",
        "name_en": "Brunswick Monument",
        "area": "Pâquis",
        "category": "Tarihi",
        "tags": ["anıt", "gotik", "revitalization", "manzara"],
        "distanceFromCenter": 0.4,
        "lat": 46.2085,
        "lng": 6.1495,
        "price": "free",
        "rating": 4.5,
        "description": "Brunswick Dükü Charles II onuruna 1873'te inşa edilen, Gotik tarzda inşa edilmiş görkemli bir mozole.",
        "description_en": "A striking neo-Gothic mausoleum built in 1873 to honor Charles II, Duke of Brunswick, who bequeathed his fortune to the city.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz / Akşam ışıklandırması",
        "bestTime_en": "Daytime / Evening lighting",
        "tips": "Hemen yanındaki parkta oturup anıtın detaylarını incelerken göl manzarasının tadını çıkarabilirsiniz.",
        "tips_en": "The surrounding terrace is a lovely spot to rest and appreciate the intricate stonework of the monument."
    },
    {
        "name": "L'Ancien Arsenal",
        "name_en": "The Old Arsenal",
        "area": "Vieille Ville",
        "category": "Tarihi",
        "tags": ["toplar", "müze", "açık hava", "ücretsiz"],
        "distanceFromCenter": 0.1,
        "lat": 46.2010,
        "lng": 6.1475,
        "price": "free",
        "rating": 4.5,
        "description": "Eski Cenevre cephaneliği. Bugün mozaiklerle süslü duvarlarının altında tarihi topların sergilendiği bir açık hava galerisi.",
        "description_en": "The former city armory, featuring a row of historic cannons sheltered by an arcade decorated with beautiful mosaics depicting Geneva's history.",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Duvarlardaki mozaikler şehre dair üç önemli tarihi anı tasvir eder, incelemeyi unutmayın.",
        "tips_en": "Take a moment to look at the three large mosaics on the back wall; they represent key eras of Geneva's history."
    },
    {
        "name": "Promenade des Bastions (Dev Satranç)",
        "name_en": "Giant Chess at Bastions Park",
        "area": "Plainpalais",
        "category": "Deneyim",
        "tags": ["satranç", "eğlence", "lokal", "açık hava"],
        "distanceFromCenter": 0.5,
        "lat": 46.2005,
        "lng": 6.1445,
        "price": "free",
        "rating": 4.6,
        "description": "Parkın girişinde yer alan, yerlilerin her gün tutkuyla oynadığı devasa yer satranç takımları.",
        "description_en": "Located at the entrance of Bastions Park, these giant floor-sized chess sets are a beloved local tradition where people play and watch intense matches.",
        "imageUrl": "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Oynamak için sıra beklemeniz gerekebilir ama izlemek de en az oynamak kadar keyiflidir.",
        "tips_en": "Even if you don't play, watching the locals strategize over the giant pieces is a quintessential Geneva experience."
    },
    {
        "name": "Buvette des Bains",
        "name_en": "Buvette des Bains",
        "area": "Pâquis",
        "category": "Deneyim",
        "tags": ["fondü", "ekonomik", "göl kenarı", "samimi"],
        "distanceFromCenter": 0.8,
        "lat": 46.2105,
        "lng": 6.1575,
        "price": "low",
        "rating": 4.7,
        "description": "Cenevre'nin en popüler ve ekonomik fondü noktası. Gölün ortasında, salaş ve çok samimi bir atmosfer.",
        "description_en": "One of the most authentic and affordable fondue spots in the city, located right on the jetty in the middle of Lake Geneva.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Kış akşamları (fondü için)",
        "bestTime_en": "Winter evenings (for fondue)",
        "tips": "Kışın fondü için mutlaka önceden rezervasyon yaptırın, çok kalabalık olur.",
        "tips_en": "In winter, be sure to book your table in advance for the famous fondue; it's extremely popular with locals."
    },
    {
        "name": "Quai du Mont-Blanc",
        "name_en": "Quai du Mont-Blanc",
        "area": "Pâquis / Göl",
        "category": "Manzara",
        "tags": ["yürüyüş", "göl", "mont blanc", "panoramik"],
        "distanceFromCenter": 0.4,
        "lat": 46.2090,
        "lng": 6.1500,
        "price": "free",
        "rating": 4.8,
        "description": "Havanın berrak olduğu günlerde Avrupa'nın en yüksek zirvesi Mont Blanc'ın muazzam göründüğü sahil şeridi.",
        "description_en": "A beautiful lakeside promenade offering panoramic views of the lake, the Jet d'Eau, and on clear days, the snowy peak of Mont Blanc.",
        "imageUrl": "https://images.unsplash.com/photo-1473951574080-01fe45ec8643?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Yürüyüş yaparken Sissi (Avusturya İmparatoriçesi Elisabeth) anıtını da görebilirsiniz.",
        "tips_en": "Look out for the statue of Empress Sissi, who was tragically assassinated near this spot in 1898."
    },
    {
        "name": "MAMCO (Modern Sanat Müzesi)",
        "name_en": "MAMCO Geneva",
        "area": "Plainpalais",
        "category": "Müze",
        "tags": ["modern sanat", "enstalasyon", "endüstriyel", "çağdaş"],
        "distanceFromCenter": 1.1,
        "lat": 46.1985,
        "lng": 6.1380,
        "price": "medium",
        "rating": 4.4,
        "description": "Eski bir fabrikada yer alan, İsviçre'nin en büyük ve en önemli çağdaş sanat müzesi.",
        "description_en": "Switzerland's largest and most influential contemporary art museum, housed in a spacious former industrial laboratory.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Her ayın ilk Pazar günü giriş ücretsizdir.",
        "tips_en": "Entry is free on the first Sunday of every month; check their website for experimental performance schedules."
    },
    {
        "name": "Pavillon de la Danse",
        "name_en": "Pavillon de la Danse",
        "area": "Plainpalais",
        "category": "Tarihi",
        "tags": ["mimari", "dans", "modern", "tasarım"],
        "distanceFromCenter": 0.8,
        "lat": 46.1995,
        "lng": 6.1420,
        "price": "medium",
        "rating": 4.3,
        "description": "Tamamen ahşaptan inşa edilmiş, modern ve şık tasarımıyla dikkat çeken geçici ama ikonik bir dans tiyatrosu.",
        "description_en": "A striking contemporary wooden architectural pavilion dedicated to modern dance performances, located in the heart of Plainpalais.",
        "imageUrl": "https://images.unsplash.com/photo-1506764483492-1813517e5735?w=800",
        "bestTime": "Akşam (Gösteri varken)",
        "bestTime_en": "Evening (During shows)",
        "tips": "Binanın mimarisi gece ışıklandığında çok daha etkileyici görünür.",
        "tips_en": "The building's unique wooden structure is beautifully illuminated at night, making it very photogenic even if you don't stay for a show."
    }
]

def enrich_cenevre():
    filepath = 'assets/cities/cenevre.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Update fillers in existing highlights
    fillers = {
         "Jet d'Eau": {
            "description": "Zürih gölü üzerindeki bu devasa su fıskiyesi şehrin simgesi. 140 metre yüksekliğe fırlatılan su, güneşli günlerde gökkuşakları oluşturarak görsel bir şölen sunar.",
            "description_en": "The iconic 140-meter tall water fountain on Lake Geneva. On sunny days, the spray creates beautiful rainbows, making it the city's most recognizable landmark."
        },
        "Old Town (Vieille Ville)": {
            "description": "Cenevre'nin kalbinde yer alan, taş döşeli sokakları, tarihi binaları ve gizli geçitleriyle kentin ortaçağ ruhunu yaşatan büyüleyici bölge.",
            "description_en": "The historic heart of Geneva, featuring steep cobblestone streets, charming squares, and medieval architecture filled with hidden passages."
        },
        "CERN (Globe of Science)": {
            "description": "Bilimin sınırlarının zorlandığı yer. Dev ahşap küre, evrenin oluşumu ve parçacık fiziği üzerine büyüleyici sergileriyle ziyaretçilerini bekliyor.",
            "description_en": "The gateway to the world's largest particle physics lab. The iconic wooden Globe houses fascinating exhibits about the origins of the universe."
        },
        "St. Pierre Cathedral": {
            "description": "Protestan Reformu'nun lideri John Calvin'in kilisesi. Şehrin en yüksek noktasında yer alır ve kulesinden 360 derece şehir ve Alpler manzarası sunar.",
            "description_en": "A historic landmark associated with the Reformation. Climb its towers for the most spectacular panoramic views of Geneva and the Alps."
        },
        "Jardin Anglais": {
            "description": "Göl kıyısında yer alan, ünlü Çiçek Saati'ne ev sahipliği yapan ve rengarenk peyzajıyla bilinen şehrin en sevilen parkı.",
            "description_en": "A beautiful English-style park on the lakefront, home to the famous L'Horloge Fleurie (Flower Clock) and a favorite spot for shaded strolls."
        },
        "Patek Philippe Museum": {
            "description": "Beş yüz yıllık saatçilik tarihine bir yolculuk. Dünyanın en nadide ve değerli saat koleksiyonlarından birini burada görebilirsiniz.",
            "description_en": "A temple dedicated to horology, showcasing 500 years of watchmaking history through an incredible collection of rare timepieces."
        },
        "Bains des Pâquis": {
            "description": "Cenevre'nin yerel yaşamının merkezi. Yazın yüzmek, kışın sauna ve meşhur fondü için göl ortasındaki bu iskeleye mutlaka uğrayın.",
            "description_en": "The social soul of the city where locals swim in summer and enjoy saunas and world-class fondue in winter right on the lake."
        },
        "Parc des Bastions": {
            "description": "Reform Duvarı'na ev sahipliği yapan, dev satranç takımları ve huzurlu ağaçlı yollarıyla kentin en önemli tarihi parkı.",
            "description_en": "Home to the Reformation Wall and giant outdoor chess boards, this lush park is a perfect blend of history and student-filled energy."
        },
        "Mont Salève (Günübirlik)": {
            "description": "Teknik olarak Fransa'da olsa da Cenevre'nin ev dağı sayılır. Teleferikle çıkıp kentin, gölün ve karlı zirvelerin tadını çıkarın.",
            "description_en": "Known as the 'Balcony of Geneva.' A short trip to France where a cable car takes you to stunning views of the city and Mont Blanc."
        },
        "Broken Chair": {
            "description": "BM Ofisi'nin karşısında duran bu 12 metrelik dev heykel, kara mayınlarına karşı bir duruşu simgeleyen güçlü bir sanat eseridir.",
            "description_en": "A powerful 12-meter tall sculpture of a chair with a broken leg, symbolizing opposition to landmines and cluster bombs across the globe."
        },
        "Red Cross Museum": {
            "description": "İnsani yardım tarihine duygusal ve etkileyici bir bakış. Yardımseverliğin ve dayanışmanın öykülerini modern sergilerle keşfedin.",
            "description_en": "A moving and thought-provoking museum documenting the history of humanitarian aid and the impact of conflict through immersive exhibits."
        },
        "Lake Geneva Cruise": {
            "description": "Cenevre'yi göl üzerinden keşfedin. Alpler ve şehrin silüeti suya yansırken yapacağınız bu tekne turu unutulmaz olacaktır.",
            "description_en": "The best way to experience the scale of the city and the lake. Enjoy a relaxing boat tour with the Alps reflecting on the crystal clear water."
        },
        "Carouge": {
            "description": "Cenevre'nin içinde bir 'Küçük İtalya.' Akdeniz mimarisi, sanatçı atölyeleri ve butik kafeleriyle kentin en bohem köşesi.",
            "description_en": "Often called Geneva's 'Greenwich Village,' this Mediterranean-style district is famous for its artisanal workshops and bohemian cafes."
        },
        "Maison Tavel": {
            "description": "Cenevre'nin ayakta kalan en eski evi. Şehrin ortaçağdan günümüze hikayesini anlatan ücretsiz bir tarih müzesi.",
            "description_en": "The oldest private house in the city, now a free museum that tells the fascinating story of daily life in Geneva from the Middle Ages."
        },
        "Parc de la Grange": {
            "description": "Şehrin en güzel gül bahçelerine ve tarihi bir malikaneye ev sahipliği yapan, göle nazır geniş ve huzurlu yeşil alan.",
            "description_en": "Geneva's largest park, famous for its magnificent rose gardens, ancient trees, and open-air summer theater overlooking the lake."
        },
        "Musée d'Art et d'Histoire": {
            "description": "Arkeolojiden güzel sanatlara kadar uzanan devasa koleksiyonuyla İsviçre'nin en önemli müzelerinden biri.",
            "description_en": "Switzerland's leading encyclopedic museum with vast collections ranging from Egyptian archaeology to major European fine art masterpieces."
        },
        "Place du Bourg-de-Four": {
            "description": "Eski şehrin en eski meydanı. Roma döneminden beri kentin merkezi olan bu meydan, bugün şık kafelerle doludur.",
            "description_en": "The oldest city square in Geneva, dating back to Roman times. Today it's the perfect spot to enjoy coffee amidst historic facades."
        },
        "Conservatoire et Jardin botaniques": {
            "description": "Dünyanın her yerinden binlerce bitki türünü ve egzotik kuşları görebileceğiniz, göl kıyısında devasa bir açık hava müzesi.",
            "description_en": "A massive botanical sanctuary home to thousands of plant species, exotic bird aviaries, and a world-class seed bank."
        },
        "Perle du Lac": {
            "description": "Gölün incisi. Mont Blanc'ın en iyi göründüğü nokta olan bu parkta Bilim Tarihi Müzesi de yer almaktadır.",
            "description_en": "The 'Pearl of the Lake.' A stunning lakeside park offering the best views of Mont Blanc and housing the charming History of Science Museum."
        },
        "Rue du Rhône": {
            "description": "Dünyanın en prestijli saat ve moda markalarının sıralandığı, Cenevre'nin lüks alışveriş caddesi.",
            "description_en": "One of the world's most exclusive shopping streets, featuring flagship stores of luxury watchmakers and high-end fashion houses."
        },
        "Yvoire (Günübirlik)": {
            "description": "Gölün karşı kıyısında yer alan, Fransa'nın en güzel köylerinden biri seçilen, çiçeklerle bezenmiş bir ortaçağ kasabası.",
            "description_en": "A stunning medieval lakeside village in France. Famous for its flower-covered stone houses and the enchanting Garden of the Five Senses."
        },
        "Annecy (Günübirlik)": {
            "description": "Kanalları ve çiçekli köprüleriyle 'Alpler'in Venedik'i' olarak bilinir. Cenevre'den çok kolay ulaşılan romantik bir kaçamak noktası.",
            "description_en": "Known as the 'Venice of the Alps,' this French lakeside town is famous for its crystal clear canals and fairytale-like cobblestone streets."
        },
        "Chamonix-Mont-Blanc (Günübirlik)": {
            "description": "Alplerin zirvesinde, karlı tepeler ve buzullar arasında bir macera. Dünyanın en ünlü dağ kasabalarından biri.",
            "description_en": "Located at the foot of Mont Blanc, Chamonix is a world-renowned destination for breathtaking cable car rides and glacial scenery."
        },
        "Château de Gruyères": {
            "description": "Masalsı bir şato ve dünyaca ünlü peynirin ana vatanı. Peynir fabrikasını ve sürrealist Giger Müzesi'ni mutlaka görün.",
            "description_en": "A medieval fortress in a picturesque village, world-famous for its namesake cheese and the surreal H.R. Giger Museum."
        },
        "Montreux (Günübirlik)": {
            "description": "Caz festivali ve Freddie Mercury ile özdeşleşmiş, göl kıyısındaki Chillon Kalesi ile büyüleyen çok şık bir sayfiye kasabası.",
            "description_en": "An elegant lakeside town famous for its jazz festival, Chillon Castle, and its enduring connection to legendary singer Freddie Mercury."
        },
        "Café du Soleil": {
            "description": "Cenevre'nin en iyi fondü adreslerinden biri. 400 yıllık bir binada geleneksel lezzetlerin tadını çıkarın.",
            "description_en": "Widely considered the best place for authentic Swiss fondue in Geneva, serving traditional recipes in a building dating back 400 years."
        },
        "Les Armures": {
            "description": "Eski şehrin kalbinde, tarihin ve lezzetin buluştuğu nokta. Geleneksel İsviçre mutfağının en seçkin örneklerini sunar.",
            "description_en": "A historic culinary institution in the Old Town, famous for its grand atmosphere and impeccable traditional Swiss specialties like raclette."
        },
        "Manor Geneva (Department Store)": {
            "description": "Cenevre'nin en büyük çok katlı mağazası. En üst katındaki restoran, uygun fiyatlı ve lezzetli yemekler için harikadır.",
            "description_en": "The city's premier department store. Don't miss the top-floor cafeteria for high-quality, affordably priced fresh Swiss meals and views."
        },
        "Lausanne Cathedral": {
            "description": "İsviçre'nin en etkileyici Gotik yapılarından biri. Olimpiyat başkenti Lozan'ın dik yokuşlu sokaklarını ve göl manzarasını keşfedin.",
            "description_en": "One of Switzerland's most beautiful Gothic cathedrals. Explore Lausanne's vibrant streets and its prestigious Olympic legacy."
        },
        "Musée Patek Philippe": {
            "description": "İsviçre saatçiliğinin zirvesi. 16. yüzyıldan günümüze binlerce nadide saatin sergilendiği dünyanın en önemli saat müzesi.",
            "description_en": "The final authority on the history of timekeeping, housing thousands of unique and complex watches from the 16th century to today."
        },
        "Plainpalais Flea Market": {
            "description": "Cenevre'nin en büyük ve renkli bit pazarı. Antikalardan ilginç nesnelere kadar her şeyi bulabileceğiniz bir hazine avı alanı.",
            "description_en": "Geneva's largest flea market, where locals hunt for antiques, vintage books, and unique treasures in a vibrant, open-air setting."
        },
        "Saleve Cable Car": {
            "description": "Cenevre'yi kuş bakışı görmek için en iyi yol. Teleferikle çıkılan zirvede yürüyüş parkurları ve eşsiz bir manzara sizi bekler.",
            "description_en": "The easiest way to reach the clouds. The cable car whisks you to the ridge for hiking and unparalleled panoramic views over Lake Geneva."
        },
        "Ariana Museum": {
            "description": "Seramik ve cam sanatına adanmış muazzam bir müze. Binanın kendisi bile başlı başına bir sanat eseri sayılır.",
            "description_en": "Dedicated to ceramics and glass, this museum houses an extraordinary collection in one of Geneva's most stunning architectural landmarks."
        },
        "International Museum of the Reformation": {
            "description": "Cenevre'nin neden 'Protestan Roma'sı' dendiğini anlamak için bu modern ve interaktif müzeyi mutlaka ziyaret edin.",
            "description_en": "Discover why Geneva is called the 'Protestant Rome' through engaging and modern exhibits about the history of the Reformation."
        },
        "L'Horloge Fleurie (Flower Clock)": {
            "description": "Cenevre'nin saatçilik mirasına ve doğaya olan sevgisinin sembolü. 6500'den fazla çiçekle yapılan devasa işleyen bir saat.",
            "description_en": "A symbol of the city's watchmaking excellence and love for nature, featuring over 6,500 seasonal flowers in a working clock."
        },
        "Cottage Café": {
            "description": "Brunswick Parkı'nın içinde, bir peri masalından çıkmış masalsı küçük bir evde hizmet veren çok şirin ve popüler bir kafe.",
            "description_en": "A fairytale-like cottage tucked away in a park, serving creative global cuisine and excellent coffee in a cozy, hidden setting."
        }
    }

    for h in data.get('highlights', []):
        if h['name'] in fillers:
            h['description'] = fillers[h['name']]['description']
            h['description_en'] = fillers[h['name']]['description_en']

    # 2. Add new highlights
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_cenevre_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_cenevre()
print(f"Geneva now has {count} highlights.")
