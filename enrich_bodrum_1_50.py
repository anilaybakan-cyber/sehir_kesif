import json

def enrich_1_50():
    with open("assets/cities/bodrum.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    enrichments = {
        "ChIJYw5gNEJsvhQRcRzUhvXx1Cs": {
            "tr": "15. yüzyılda Saint Jean Şövalyeleri tarafından inşa edilen bu görkemli kale, dünyanın en önemli su altı arkeoloji müzelerinden birine ev sahipliği yapar. Antik batıklardan çıkan paha biçilemez eserleri görebilir ve kalenin burçlarından muazzam deniz manzarasını seyredebilirsiniz.",
            "en": "Built by the Knights of St. John in the 15th century, this iconic castle houses a world-class underwater archaeology museum. You can explore ancient shipwrecks and enjoy breathtaking Aegean views from its towers."
        },
        "ChIJlwmXEkdsvhQR0fktlJphpF4": {
            "tr": "Antik dünyanın yedi harikasından biri olan bu devasa anıt mezarın kalıntıları, Karya kralı Mausolus için inşa edilmiştir. Günümüze sadece temelleri kalmış olsa da, tarihin en büyük mimari eserlerinden birinin izlerini sürmek büyüleyici bir deneyimdir.",
            "en": "Once one of the Seven Wonders of the Ancient World, the remains of this grand tomb were built for King Mausolus. Although mostly in ruins today, it remains a site of immense historical and architectural significance."
        },
        "ChIJv9W_9UdsvhQR2r-WmkBy9K4": {
            "tr": "Klasik Helen döneminden günümüze ulaşan bu muazzam tiyatro, Bodrum'un en eski yapılarından biridir. Sadece tarihi dokusuyla değil, aynı zamanda yaz aylarında düzenlenen konserler ve Bodrum Kalesi'ne bakan panoramik manzarasıyla da mutlaka görülmelidir.",
            "en": "Dating back to the 4th century BC, this ancient theater is one of Bodrum's best-preserved historical sites. It offers panoramic harbor views and still hosts world-class concerts during summer nights."
        },
        "ChIJa74LinVtvhQRBjZuPM4x-bw": {
            "tr": "Halikarnassos Antik Kenti'nin giriş kapısı olan Myndos Kapısı, Büyük İskender'in şehri kuşattığı tarihi noktadır. Restorasyon çalışmalarının ardından ziyarete açılan kapı, antik kentin surlarıyla birlikte tarihin derinliklerini yansıtır.",
            "en": "The Myndos Gate was the main entrance to the ancient city of Halicarnassus and the site of Alexander the Great's famous siege. Today, its restored towers offer a glimpse into the city's heroic past."
        },
        "ChIJSxsWkUdtvhQREXRy5x1VJck": {
            "tr": "Bodrum Yarımadası'nın en rüzgarlı tepelerinden birinde yer alan bu tarihi yel değirmenleri, hem Bodrum hem de Gümbet koylarını kuşbakışı gören efsanevi bir manzaraya sahiptir. Özellikle gün doğumu ve gün batımında fotoğraf tutkunları için vazgeçilmezdir.",
            "en": "Perched on a windy hill overlooking both Bodrum and Gumbet bays, these historic windmills offer some of the best panoramic views on the peninsula. They are especially stunning during sunrise and sunset."
        },
        "ChIJ_1Ko1EFsvhQR3P9pZBJXqZ4": {
            "tr": "Eski bir belediye binasında yer alan bu butik müze, Bodrum'un süngercilik ve tekne yapım tarihini belgeler. Müzede sergilenen devasa deniz kabuğu koleksiyonu ve maket tekneler, kentin denizci ruhunu mükemmel bir şekilde yansıtır.",
            "en": "Housed in a charming old building, this boutique museum documents Bodrum's sponge diving and boat-building heritage. It features an impressive seashell collection and intricate scale models of traditional vessels."
        },
        "ChIJBQsjnm5svhQRJz_yDJJmtw0": {
            "tr": "Türkiye'nin sanat güneşi Zeki Müren'in Bodrum'da hayatının son yıllarını geçirdiği evi, şimdilerde bir müze olarak hizmet vermektedir. Müzede sanatçının sahne kostümleri, tabloları ve kişisel eşyaları sergilenerek onun anısı yaşatılmaktadır.",
            "en": "The final home of Turkey's legendary artist Zeki Müren has been converted into a museum dedicated to his life and career. Visitors can see his iconic stage costumes, paintings, and personal memorabilia."
        },
        "ChIJKSkfloRuvhQRo7OVs9aIrj8": {
            "tr": "Leleg uygarlığının başkenti olan Pedasa, zeytin ağaçları arasındaki patikalardan yürüyerek ulaşılan gizli bir antik kenttir. Doğa yürüyüşü ve tarih meraklıları için, sur duvarları ve kule kalıntıları arasında sessiz bir keşif imkanı sunar.",
            "en": "The capital of the Leleg civilization, Pedasa is a hidden ancient city accessible via scenic trails through olive groves. It is a perfect spot for hikers looking to explore silent ruins, city walls, and burial mounds."
        },
        "ChIJYeiNdDlyvhQRtOAzFXdvYgw": {
            "tr": "Geleneksel mimariyle modern sanatı birleştiren bu kültür ve sanat köyü, yıl boyu süren sergileri, atölyeleri ve restoranıyla çok şık bir komplekstir. Akşamları düzenlenen açık hava konserleri ve film gösterimleri buraya ayrı bir ruh katar.",
            "en": "Blending traditional architecture with modern art, this cultural village is an upscale complex featuring galleries, boutiques, and gourmet dining. Its open-air concerts and cinema nights are a summer highlight."
        },
        "ChIJS6IGGndtvhQRmh_4muCldt8": {
            "tr": "Mandalina bahçeleriyle çevrili Bitez Plajı, özellikle rüzgar sörfü tutkunları ve sığ deniziyle çocuklu aileler için ideal bir noktadır. Sahil boyunca uzanan kafe ve restoranlarda taze deniz mahsullerinin tadına bakabilirsiniz.",
            "en": "Famed for its mandarin groves and shallow waters, Bitez Beach is perfect for windsurfing and family outings. The beach is lined with cozy cafes and seafood restaurants that offer a relaxed Bodrum vibe."
        },
        "ChIJ47Rqu_p0vhQRei2H38xNHuI": {
            "tr": "Bohem atmosferi ve denizin içindeki masalarıyla ünlü Gümüşlük, Bodrum Yarımadası'nın en romantik köşesidir. Tavşan Adası'na sığ sudan yürüyerek geçebilir ve akşamları sahil kenarındaki balıkçılarda taze balık yiyebilirsiniz.",
            "en": "Known for its bohemian charm and seaside tables, Gümüşlük is the peninsula's most romantic corner. You can walk through shallow waters to Rabbit Island and enjoy world-class fish dinners at sunset."
        },
        "ChIJUQN2bBVyvhQROyp0NzOXui8": {
            "tr": "Ortakent'te yer alan Yahşi Plajı, kristal netliğindeki denizi ve geniş kum sahiliyle bilinir. 'Mavi Bayraklı' olan bu plaj, uzun yürüyüş yolu ve her bütçeye uygun mekan seçenekleriyle Bodrum'un en tercih edilen sahillerindendir.",
            "en": "Located in Ortakent, Yahşi Beach is famous for its crystal-clear Blue Flag waters and long sandy shore. It offers a great promenade and a wide variety of beach clubs and local eateries for all budgets."
        },
        "ChIJVVK9K_YMvhQRuLKlILDC-Uo": {
            "tr": "Akyarlar'da bulunan Karaincir, incecik altın sarısı kumu ve rüzgara kapalı, durgun deniziyle adeta bir havuzu andırır. Suyun serinliği ve sahilin sakinliği, huzurlu bir deniz günü arayanlar için Karaincir'i eşsiz kılar.",
            "en": "Karaincir Beach in Akyarlar feels like a natural swimming pool with its fine golden sand and calm, sheltered bay. Known for its cool waters, it is the perfect escape for those seeking peace and tranquility."
        },
        "ChIJt0Jtk25svhQR22ph3Szmf8I": {
            "tr": "Bodrum merkezin en popüler plajlarından biri olan Kumbahçe, tarihi kaleye karşı yüzme imkanı sunar. Akşamları sahil boyunca kurulan masalarda yemek yiyebilir ve kalenin ışıklandırması eşliğinde yürüyüş yapabilirsiniz.",
            "en": "One of central Bodrum's most popular beaches, Kumbahçe offers the chance to swim right across from the historic castle. In the evening, the beach transforms with waterside dining and illuminated views of the fortress."
        },
        "ChIJ_759OOxxvhQRXZc1KZwApPw": {
            "tr": "Dünyanın en lüks yat limanlarından biri olan Yalıkavak Marina, uluslararası tasarım ödülleriyle tescillenmiş bir komplekstir. Dünya çapında ünlü lüks markaların mağazaları ve Michelin yıldızlı kalitesinde restoranlarıyla Bodrum'un jet sosyete noktasıdır.",
            "en": "As one of the world's most luxurious marinas, Yalıkavak is an award-winning hub for mega-yachts and elite travelers. It hosts high-end designer boutiques and world-class dining destinations."
        },
        "ChIJHexKKERsvhQRCfysEWSpShM": {
            "tr": "Bodrum merkezdeki Milta Marina, modern tesisleri ve kentin kalbindeki konumuyla yatçıların favorisidir. Marina içindeki şık butikler ve gurme restoranlar, akşam yürüyüşleri için kentin en nezih atmosferini sunar.",
            "en": "Milta Marina in central Bodrum is a top choice for yachtsmen thanks to its modern facilities and heart-of-the-city location. Its upscale boutiques and gourmet restaurants provide a refined atmosphere for evening strolls."
        },
        "ChIJd9_mLEBsvhQR6pGYjxFgJ0o": {
            "tr": "Bodrum'un kalbi sayılan bu tarihi çarşı, beyaz badanalı sokakları ve Begonvillerle süslü dükkanlarıyla alışveriş meraklılarını ağırlar. El yapımı Bodrum sandaletlerinden takılara kadar yerel sanata dair her şeyi bulabilirsiniz.",
            "en": "Considered the heart of Bodrum, this historic marketplace features whitewashed alleys and shops adorned with bougainvillea. It is the best place to find local crafts, ranging from handmade sandals to unique jewelry."
        },
        "ChIJybTpQuxvvhQRvHMQvLA1YMk": {
            "tr": "Zeytinlikler arasında yer alan ve Bodrum'un 'lüks boho' tarzını dünyada temsil eden Maçakızı, ikonik iskelesi ve gurme mutfağıyla bir yaşam tarzıdır. Happy hour saatleri ve incelikli tasarımıyla yarımadanın en prestijli noktasıdır.",
            "en": "Set amidst olive groves, Maçakızı represents the pinnacle of Bodrum's 'boho-luxury' style. Its iconic deck and gourmet kitchen make it a prestigious lifestyle destination for the global jet set."
        },
        "ChIJeectHM9ovhQR4xsyVITINuw": {
            "tr": "Torba Koyu'nun turkuaz sularına hakim Nikki Beach, dünya çapında ünlü plaj kulübü konseptini Bodrum'a taşır. Canlı DJ performansları, yaratıcı kokteylleri ve şık havuz başı partileriyle eğlencenin merkezidir.",
            "en": "Overlooking the turquoise waters of Torba Bay, Nikki Beach brings its world-famous beach club concept to Bodrum. It is the center of daytime parties with live DJ sets, creative cocktails, and a chic poolside vibe."
        },
        "ChIJsc0ubABtvhQRyEfAZVpFoLA": {
            "tr": "Cennet Koyu'nun masmavi sularında yer alan Lucca Beach, İstanbul'un ikonik markasının sahil konseptidir. Rafine bir eğlence anlayışı, gurme atıştırmalıklar ve tasarım detaylarıyla lüks bir deniz günü vaat eder.",
            "en": "Located in the deep blue waters of Paradise Bay, Lucca Beach is the coastal concept of Istanbul's iconic brand. it promises a luxurious day at sea with refined entertainment, gourmet snacks, and designer style."
        },
        "ChIJJ2SLwVVxvhQRBW5Ezry6Dh0": {
            "tr": "Yalıkavak ve merkezde şubeleri bulunan Memedof, taze meze çeşitleri ve günlük deniz ürünleriyle kentin en prestijli balık restoranlarından biridir. Deniz kıyısındaki masalarıyla gerçek bir Bodrum klasiğidir.",
            "en": "With locations in Yalıkavak and the center, Memedof is one of Bodrum's most prestigious seafood restaurants. Known for its fresh daily catch and exquisite appetizers, it is a true local classic."
        },
        "ChIJm6aS3GlxvhQRFvn-6AKya34": {
            "tr": "Yalıkavak Marina'nın en ikonik duraklarından biri olan Sait, yıllardır değişmeyen kalitesiyle 'eski Bodrum' ruhunu lüksle birleştirir. Özellikle deniz mahsullü ara sıcakları ve taze balıklarıyla gurmelerin uğrak noktasıdır.",
            "en": "One of the most iconic spots in Yalıkavak Marina, Sait blends original Bodrum hospitality with high-end dining. It is a favorite among gourmets for its seafood appetizers and impeccable service."
        },
        "ChIJp2EErUdsvhQR4hhpautlFXQ": {
            "tr": "Bodrum Marina'nın tam karşısında yer alan Gemibaşı, samimi atmosferi ve 'ev yapımı' tadındaki mezeleriyle yerel halkın da favorisidir. Şehrin merkezinde gerçek bir Ege akşamı yaşamak isteyenler için idealdir.",
            "en": "Located right across from the Bodrum Marina, Gemibaşı is a local favorite known for its warm atmosphere and home-style appetizers. It is the perfect spot for an authentic Aegean evening in the heart of town."
        },
        "ChIJK8EeTELOvxQRvYZKtrHmCb8": {
            "tr": "Deniz mahsulleri konusunda yaratıcılığın zirvesi olan Orfoz, tadım menüleri ve egzotik deniz ürünleriyle klasik bir balıkçının çok ötesindedir. Gurmeler için kentin en özel gastronomi deneyimlerinden birini sunar.",
            "en": "A pinnacle of seafood creativity, Orfoz offers unique tasting menus that go far beyond standard fare. It is widely considered one of Bodrum's most exclusive and experimental culinary destinations."
        },
        "ChIJNcwJIKJ1vhQRx77eJ4VuNp8": {
            "tr": "Gümüşlük denilince akla gelen ilk yerlerden biri olan Limon, bir bahçenin içinde, gün batımına karşı kurulan masalarıyla efsanedir. Bohem şıklığı ve ev yapımı lezzetleriyle unutulmaz bir akşam yemeği noktasıdır.",
            "en": "Arguably the most legendary spot in Gümüşlük, Limon features a lush garden setting with tables facing the sunset. Its bohemian charm and rustic-chic delicacies make it an essential evening destination."
        },
        "ChIJV4CT2fhtvhQRmuYDm_i3S5M": {
            "tr": "Adını suyunun cam berraklığından alan Akvaryum Koyu, sadece tekne turlarıyla ulaşılabilen bakir bir doğa harikasıdır. Şnorkelle dalış yaparken balıkları çıplak gözle görebileceğiniz bu koy, Bodrum'un en özel rotalarındandır.",
            "en": "Named for its crystal-clear waters, Aquarium Bay is a pristine natural wonder reachable only by boat. It's a premier location for snorkeling, where you can swim alongside schools of fish in turquoise depths."
        },
        "ChIJcaKMBvlAvhQRgSBmQyMOxVM": {
            "tr": "Bodrum'un Maldivleri olarak bilinen Orak Adası, turkuazın en canlı tonlarına sahip deniziyle tekne turlarının favori durağıdır. Kristal suları ve bakir doğasıyla unutulmaz bir yüzme deneyimi sunar.",
            "en": "Known as the Maldives of Bodrum, Orak Island is the star of local boat tours thanks to its vibrant turquoise waters. Its crystal depths and untouched nature offer an unparalleled swimming experience."
        },
        "ChIJDz_6BuB4uxQR9iUno_n11tw": {
            "tr": "Alaçatı'nın kalbi olan Çarşı, Arnavut kaldırımlı sokakları, tarihi taş evleri ve Begonvillerle süslü butikleriyle büyüleyici bir atmosfere sahiptir. Akşam yürüyüşü ve akşam yemeği için kentin en popüler noktasıdır.",
            "en": "The heart of Alacati, this marketplace features cobblestone streets, historic stone houses, and bougainvillea-draped boutiques. It is the most popular spot for scenic evening strolls and gourmet dining."
        },
        "ChIJN2KX4aZ9uxQR5UV1UNY47h8": {
            "tr": "Adını denizindeki kumların pırıltısından alan Pırlanta Plajı, geniş kum alanı ve rüzgarlı yapısıyla sörf tutkunları için idealdir. Sığ ve temiz denizi, rüzgar sörfüne yeni başlayanlar için de harika bir ortam sunar.",
            "en": "Named after the sparkle of its sands, Pırlanta Beach is a haven for windsurfers thanks to its consistent winds. Its shallow and clean waters also provide a perfect environment for beginners and families."
        },
        "ChIJCRS37Mp7uxQRPRiXrVHW7TA": {
            "tr": "Lüks yatların ve şık restoranların buluşma noktası olan Çeşme Marina, kentin en modern ve nezih yüzünü temsil eder. Sahil boyunca uzanan mağazaları ve kafe-barlarıyla günün her saati canlı bir çekim merkezidir.",
            "en": "A premier destination for luxury yachts and fine dining, Cesme Marina represents the modern and upscale side of town. With its waterfront boutiques and chic bars, it's a vibrant hub at any time of day."
        }
    }
    
    # Apply to highlights
    for highlight in data.get("highlights", []):
        pid = highlight.get("id")
        if pid in enrichments:
            highlight["description"] = enrichments[pid]["tr"]
            highlight["description_en"] = enrichments[pid]["en"]
        elif highlight.get("description", "").startswith("Bodrum'un harika bir noktası"):
             # For those not explicitly in the enrichment list but still generic
             name = highlight.get("name", "Burası")
             highlight["description"] = f"{name}, Bodrum seyahatinizde keşfetmeniz gereken, kendine has dokusu ve atmosferiyle öne çıkan özel bir noktadır."
             highlight["description_en"] = f"{name} is a unique spot in Bodrum with a distinctive atmosphere that we highly recommend exploring during your visit."

    with open("assets/cities/bodrum.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("Enriched venues 1-50 for Bodrum.")

if __name__ == "__main__":
    enrich_1_50()
