import json

# Manual enrichment data (Venice - ALL 49 items)
updates = {
    "St Mark's Basilica": {
        "description": "Altın mozaikleri ve Bizans mimarisiyle ünlü katedral. Venedik'in zenginliğinin ve gücünün sembolü, San Marco Meydanı'nın kalbi.",
        "description_en": "Cathedral famous for golden mosaics and Byzantine architecture. Symbol of Venice's wealth and power, heart of St Mark's Square."
    },
    "Doge's Palace": {
        "description": "Venedik Cumhuriyeti'nin yönetim merkezi, gotik şaheser. Altın Merdiven, hapishaneler ve Casanova'nın kaçtığı yer.",
        "description_en": "Administrative center of Venetian Republic, Gothic masterpiece. Golden Staircase, prisons, and place where Casanova escaped."
    },
    "Rialto Bridge": {
        "description": "Büyük Kanal üzerindeki en eski ve ikonik taş köprü. Dükkânlarla dolu, Venedik'in en ünlü fotoğraf noktası ve gün batımı.",
        "description_en": "Oldest and iconic stone bridge over Grand Canal. Filled with shops, Venice's most famous photo spot and sunset."
    },
    "Grand Canal": {
        "description": "Venedik'in ana su yolu, 'S' şeklinde şehri böler. Vaporetto turu, sarayların geçit töreni ve romantik gondol gezisi.",
        "description_en": "Venice's main waterway, dividing city in 'S' shape. Vaporetto tour, parade of palaces, and romantic gondola ride."
    },
    "Bridge of Sighs": {
        "description": "Dükler Sarayı'nı hapishaneye bağlayan kapalı köprü. Mahkumların Venedik'e son bakışı ve romantik efsaneler.",
        "description_en": "Enclosed bridge connecting Doge's Palace to prison. Prisoners' last look at Venice and romantic legends."
    },
    "Burano": {
        "description": "Rengarenk boyalı balıkçı evleriyle ünlü ada. Dantel yapımı geleneği, fotoğrafçılık cenneti ve huzurlu atmosfer.",
        "description_en": "Island famous for colorful painted fishermen's houses. Lace making tradition, photography paradise, and peaceful atmosphere."
    },
    "Murano": {
        "description": "Dünyaca ünlü cam üfleme sanatının merkezi ada. Cam atölyeleri, gösteriler ve Cam Müzesi. Venedik'ten tekneyle ulaşım.",
        "description_en": "Island center of world-famous glass blowing art. Glass workshops, demonstrations, and Glass Museum. Boat access from Venice."
    },
    "Peggy Guggenheim Collection": {
        "description": "Büyük Kanal üzerindeki sarayda modern sanat müzesi. Picasso, Dali, Pollock eserleri ve heykel bahçesi.",
        "description_en": "Modern art museum in palace on Grand Canal. Works by Picasso, Dali, Pollock, and sculpture garden."
    },
    "Teatro La Fenice": {
        "description": "Küllerinden defalarca doğan efsanevi opera binası. Verdi'nin prömiyerleri, altın varaklı iç mekan ve Yeni Yıl konseri.",
        "description_en": "Legendary opera house repeatedly born from ashes. Verdi's premieres, gold leaf interior, and New Year concert."
    },
    "Gallerie dell'Accademia": {
        "description": "Venedik Rönesans sanatının en büyük koleksiyonu. Titian, Tintoretto ve Veronese başyapıtları. Leonardo'nun Vitruvius Adamı.",
        "description_en": "Largest collection of Venetian Renaissance art. Masterpieces by Titian, Tintoretto, and Veronese. Leonardo's Vitruvian Man."
    },
    "Ca' Rezzonico": {
        "description": "18. yüzyıl Venedik yaşamını sergileyen müze saray. Balo salonu, freskler ve kanal manzarası. Barok ihtişam.",
        "description_en": "Museum palace exhibiting 18th-century Venetian life. Ballroom, frescoes, and canal views. Baroque splendor."
    },
    "Santa Maria della Salute": {
        "description": "Veba salgınının bitişine şükran olarak yapılan barok kilise. Büyük Kanal'ın girişinde ikonik kubbe ve beyaz taş.",
        "description_en": "Baroque church built in gratitude for end of plague. Iconic dome and white stone at Grand Canal entrance."
    },
    "Scuola Grande di San Rocco": {
        "description": "Tintoretto'nun başyapıt freskleriyle dolu 'Venedik'in Sistine Şapeli'. Sanat tarihi, dini lonca binası ve görkem.",
        "description_en": "'Sistine Chapel of Venice' filled with Tintoretto's masterpiece frescoes. Art history, religious guild building, and splendor."
    },
    "Libreria Acqua Alta": {
        "description": "Kanal sularının bastığı kitapçı, gondol içinde kitaplar. 'Dünyanın en güzel kitapçısı', kediler ve kitap merdiveni.",
        "description_en": "Bookstore flooded by channel waters, books in gondola. 'Most beautiful bookstore in world', cats, and book staircase."
    },
    "Campanile di San Marco": {
        "description": "San Marco Meydanı'ndaki 98 metrelik çan kulesi. Asansörle çıkış, lagün ve şehir panoraması. Galileo'nun gözlemevi.",
        "description_en": "98-meter bell tower in St Mark's Square. Elevator access, lagoon and city panorama. Galileo's observatory."
    },
    "Rialto Market": {
        "description": "Yüzyıllardır süren taze balık ve sebze pazarı. Sabah erken saatlerde canlılık, yerel ürünler ve kanal kenarı.",
        "description_en": "Centuries-old fresh fish and vegetable market. Liveliness in early morning, local produce, and canalside."
    },
    "Torcello": {
        "description": "Venedik lagününün en eski yerleşimi, sakin ada. Bizans mozaikli bazilika, Attila'nın Tahtı ve sessizlik.",
        "description_en": "Oldest settlement of Venice lagoon, quiet island. Basilica with Byzantine mosaics, Attila's Throne, and silence."
    },
    "Lido di Venezia": {
        "description": "Venedik Film Festivali'ne ev sahipliği yapan plaj adası. Art nouveau oteller, kumsallar ve bisiklet turları.",
        "description_en": "Beach island hosting Venice Film Festival. Art nouveau hotels, sandy beaches, and bike tours."
    },
    "San Giorgio Maggiore": {
        "description": "San Marco'nun karşısındaki ada, Palladio tasarımı kilise. Çan kulesinden en iyi Venedik manzarası (sıra beklemeden).",
        "description_en": "Island opposite St Mark's, Palladio-designed church. Best Venice view from bell tower (without waiting in line)."
    },
    "Palazzo Contarini del Bovolo": {
        "description": "Gizli mücevher, salyangoz şeklindeki dış merdiven kulesi. Gotik-Rönesans karışımı, çatı manzarası ve mimari harika.",
        "description_en": "Hidden gem, snail-shaped external staircase tower. Gothic-Renaissance mix, rooftop views, and architectural marvel."
    },
    "Harry's Bar": {
        "description": "Bellini kokteyli ve Carpaccio'nun icat edildiği efsanevi bar. Hemingway'in uğrak yeri, klasik servis ve tarih.",
        "description_en": "Legendary bar where Bellini cocktail and Carpaccio were invented. Hemingway's haunt, classic service, and history."
    },
    "Caffe Florian": {
        "description": "1720'den beri San Marco Meydanı'nda, dünyanın en eski kafesi. Orkestra müziği, lüks dekor ve pahalı (ama değer) kahve.",
        "description_en": "Since 1720 in St Mark's Square, world's oldest cafe. Orchestra music, luxury decor, and expensive (but worth it) coffee."
    },
    "Caffe Quadri": {
        "description": "Meydanın diğer tarafındaki tarihi rakip, Avusturya askerlerinin favorisiydi. Michelin yıldızlı restoran ve zarif kafe.",
        "description_en": "Historic rival on other side of square, was favorite of Austrian soldiers. Michelin-starred restaurant and elegant cafe."
    },
    "Cantina Do Mori": {
        "description": "1462'den beri açık Venedik'in en eski bacaro'su. Bakır tencere dekoru, cicchetti (tapas) ve yerel şarap.",
        "description_en": "Venice's oldest bacaro open since 1462. Copper pot decor, cicchetti (tapas), and local wine."
    },
    "All'Arco": {
        "description": "Rialto Pazarı yakınında küçük ve kalabalık bacaro. Taze deniz ürünlü cicchetti, prosecco ve ayakta atıştırma.",
        "description_en": "Small and crowded bacaro near Rialto Market. Fresh seafood cicchetti, prosecco, and standing snack."
    },
    "Osteria alle Testiere": {
        "description": "Sadece 9 masalı küçük deniz ürünleri restoranı. Günlük taze menü, samimi ortam ve rezervasyon şart.",
        "description_en": "Small seafood restaurant with only 9 tables. Daily fresh menu, intimate setting, and reservation required."
    },
    "Antiche Carampane": {
        "description": "Turist tuzağı olmayan, yerel halkın favori balık restoranı. Kızarmış deniz ürünleri, taze makarna ve gizli konum.",
        "description_en": "Locals' favorite fish restaurant, not a tourist trap. Fried seafood, fresh pasta, and hidden location."
    },
    "Paradiso Perduto": {
        "description": "Cannaregio'da canlı müzik ve bol yemek sunan osteria. Genç atmosfer, kanal kenarı masalar ve gece hayatı.",
        "description_en": "Osteria offering live music and abundant food in Cannaregio. Young atmosphere, canalside tables, and nightlife."
    },
    "Vino Vero": {
        "description": "Modern şarap barı, doğal şaraplar ve gurme cicchetti. Kanal kenarında ayakta sohbet, yerel kalabalık.",
        "description_en": "Modern wine bar, natural wines, and gourmet cicchetti. Standing chat by canal, local crowd."
    },
    "Fondaco dei Tedeschi": {
        "description": "Eski Alman tüccar evi, şimdi lüks alışveriş merkezi. Ücretsiz çatı terası (rezervasyonlu), Büyük Kanal manzarası.",
        "description_en": "Old German merchant house, now luxury shopping mall. Free rooftop terrace (booked), Grand Canal views."
    },
    "Jewish Ghetto": {
        "description": "Dünyanın ilk gettosu, tarihi sinagoglar ve müze. Shakespeare'in Venedik Taciri mekanı, koşer fırınlar.",
        "description_en": "World's first ghetto, historic synagogues, and museum. Venue of Shakespeare's Merchant of Venice, kosher bakeries."
    },
    "Arsenal": {
        "description": "Venedik donanmasının tarihi tersanesi, deniz gücünün merkezi. Bienal mekanı, aslanlı kapı ve denizcilik müzesi.",
        "description_en": "Historic shipyard of Venetian navy, center of naval power. Biennale venue, lion gate, and naval museum."
    },
    "Giardini della Biennale": {
        "description": "Venedik Sanat ve Mimarlık Bienali'nin bahçeleri ve pavyonları. Kamusal park, heykeller ve sanat yürüyüşü.",
        "description_en": "Gardens and pavilions of Venice Art and Architecture Biennale. Public park, sculptures, and art walk."
    },
    "Ca' d'Oro": {
        "description": "'Altın Ev', Büyük Kanal'ın en güzel gotik cephelerinden biri. Şimdi Franchetti Galerisi, sanat ve mozaik zeminler.",
        "description_en": "'House of Gold', one of Grand Canal's most beautiful Gothic facades. Now Franchetti Gallery, art, and mosaic floors."
    },
    "Museo Correr": {
        "description": "San Marco Meydanı'nda Venedik tarihi ve sanatı müzesi. İmparatorluk odaları, haritalar ve Canova heykelleri.",
        "description_en": "Venice history and art museum in St Mark's Square. Imperial rooms, maps, and Canova sculptures."
    },
    "Squero di San Trovaso": {
        "description": "Venedik'in son çalışan gondol yapım atölyelerinden biri. Karşı kıyıdan izlenebilir, ahşap işçiliği ve gelenek.",
        "description_en": "One of Venice's last working gondola boatyards. Viewable from opposite bank, woodcraft, and tradition."
    },
    "Zattere": {
        "description": "Giudecca Kanalı boyunca uzun ve güneşli yürüyüş yolu. Gelato molası, gün batımı ve daha sakin Venedik.",
        "description_en": "Long and sunny promenade along Giudecca Canal. Gelato break, sunset, and calmer Venice."
    },
    "Gelateria Nico": {
        "description": "Zattere'de meşhur 'Gianduiotto' (çikolata ve krema) dondurması. Su kenarı teras, gün batımı klasiği.",
        "description_en": "Famous 'Gianduiotto' (chocolate and cream) ice cream at Zattere. Waterside terrace, sunset classic."
    },
    "Rosa Salva": {
        "description": "Venedik'in en sevilen tarihi pastanelerinden biri. Tramezzini (üçgen sandviç), kahve ve ayakta kahvaltı.",
        "description_en": "One of Venice's most beloved historic pastry shops. Tramezzini (triangle sandwich), coffee, and standing breakfast."
    },
    "Farini": {
        "description": "Hızlı, ucuz ve lezzetli pizza dilimleri ve makarna. Modern fırın, turistler ve öğrencilerin favorisi.",
        "description_en": "Quick, cheap, and delicious pizza slices and pasta. Modern bakery, favorite of tourists and students."
    },
    "Bacareto da Lele": {
        "description": "Üniversite bölgesinde efsanevi küçük şarap evi. 1 Euro şarap, mini sandviçler ve kanal kenarı basamaklar.",
        "description_en": "Legendary small wine house in university area. 1 Euro wine, mini sandwiches, and canalside steps."
    },
    "Campo Santa Margherita": {
        "description": "Dorsoduro'da gençlerin ve öğrencilerin buluşma meydanı. Barlar, teraslar, spritz saati ve gece hayatı.",
        "description_en": "Meeting square for youth and students in Dorsoduro. Bars, terraces, spritz hour, and nightlife."
    },
    "Skyline Rooftop Bar": {
        "description": "Hilton Molino Stucky'nin terasında panoramik bar. Venedik'in en iyi çatı manzarası, kokteyller ve lüks.",
        "description_en": "Panoramic bar on Hilton Molino Stucky terrace. Venice's best rooftop view, cocktails, and luxury."
    },
    "Al Covo": {
        "description": "Gizli meydanda aile işletmesi, yerel malzemelere odaklı restoran. Michelin tavsiyeli, zarif ve otantik.",
        "description_en": "Family business in hidden square, restaurant focused on local ingredients. Michelin recommended, elegant, and authentic."
    },
    "La Zucca": {
        "description": "Sebze ağırlıklı menüsüyle ünlü osteria (vejetaryen dostu). Kabak flan, kanal kenarı masa ve rezervasyon şart.",
        "description_en": "Osteria famous for vegetable-heavy menu (vegetarian friendly). Pumpkin flan, canalside table, and booking essential."
    },
    "Pasticceria Tonolo": {
        "description": "Venedik'in en iyi pastanelerinden, karnaval tatlıları (frittelle) meşhur. Taze krema, espresso ve yoğunluk.",
        "description_en": "One of Venice's best pastry shops, famous for carnival sweets (frittelle). Fresh cream, espresso, and crowded."
    },
    "Torrefazione Cannaregio": {
        "description": "Kendi kahvesini kavuran tarihi kahve dükkanı. Ayakta espresso, taze çekirdek kokusu ve yerel yaşam.",
        "description_en": "Historic coffee shop roasting its own coffee. Standing espresso, fresh bean smell, and local life."
    },
    "Venissa": {
        "description": "Mazzorbo adasında surlarla çevrili şarap bağı ve restoran. Michelin yıldızlı, lagün lezzetleri ve huzur.",
        "description_en": "Walled vineyard and restaurant on Mazzorbo island. Michelin-starred, lagoon flavors, and peace."
    },
    "San Michele": {
        "description": "Venedik'in mezarlık adası, yüksek duvarlar ve selvi ağaçları. Stravinsky ve Ezra Pound'un mezarları, sessizlik.",
        "description_en": "Venice's cemetery island, high walls, and cypress trees. Graves of Stravinsky and Ezra Pound, silence."
    }
}

filepath = 'assets/cities/venedik.json'
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

print(f"\n✅ Manually enriched {count} items (Venice - COMPLETE).")
