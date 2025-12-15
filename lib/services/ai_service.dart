// =============================================================================
// AI SERVICE v2 - TÜM ŞEHİRLER İÇİN ÖNERİLER
// Barcelona, Paris, Roma, İstanbul destekli
// Kişiselleştirilmiş AI Chat yanıtları
// =============================================================================

import 'dart:math';
import '../models/city_model.dart';

class AIService {
  /// Kişiselleştirilmiş AI chat yanıtı üretir
  static Future<String> getPersonalizedChatResponse({
    required String city,
    required String userName,
    required String travelStyle,
    required List<String> interests,
    required String budgetLevel,
    required int tripDays,
    required String transportMode,
  }) async {
    await Future.delayed(const Duration(milliseconds: 800));

    // İlgi alanlarını Türkçe formatlı stringe çevir
    String interestsText = _formatInterests(interests);

    // Bütçe seviyesi açıklaması
    String budgetText = _getBudgetText(budgetLevel);

    // Seyahat tarzı açıklaması
    String styleText = _getStyleText(travelStyle);

    // Şehre özel giriş ve öneriler
    final cityData = _getCitySpecificContent(
      city,
      interests,
      budgetLevel,
      travelStyle,
    );

    // Kişiselleştirilmiş mesaj oluştur
    String greeting = _getTimeBasedGreeting();

    String response =
        '''$greeting $userName! ${cityData['intro']}

Senin gibi $interestsText tutkunu, $budgetText bir gezgin için öyle yerler biliyorum ki, $tripDays günlük gezinde her anın tadını çıkaracaksın! $styleText seyahat tarzına uygun 3 "gizli cevher" öneriyorum, kimseye söyleme, aramızda kalsın! 😉

${cityData['recommendations']}

💡 **İpucu:** ${cityData['tip']}''';

    return response;
  }

  static String _getTimeBasedGreeting() {
    final hour = DateTime.now().hour;
    if (hour < 12) return "Günaydın";
    if (hour < 18) return "İyi günler";
    return "İyi akşamlar";
  }

  static String _formatInterests(List<String> interests) {
    if (interests.isEmpty) return "keşif";
    if (interests.length == 1) return interests[0].toLowerCase();
    if (interests.length == 2)
      return "${interests[0]} ve ${interests[1]}".toLowerCase();
    return "${interests.take(2).join(', ')} ve ${interests[2]}".toLowerCase();
  }

  static String _getBudgetText(String budgetLevel) {
    switch (budgetLevel.toLowerCase()) {
      case 'ekonomik':
        return "bütçe dostu";
      case 'premium':
        return "lüks deneyimler arayan";
      default:
        return "dengeli bütçeli";
    }
  }

  static String _getStyleText(String travelStyle) {
    switch (travelStyle.toLowerCase()) {
      case 'turistik':
        return "Klasik turistik noktaları da severken";
      case 'maceracı':
        return "Macera arayan ruhuyla";
      case 'kültürel':
        return "Kültür ve tarihe meraklı";
      default:
        return "Yerel hayatı keşfetmeyi seven";
    }
  }

  static Map<String, String> _getCitySpecificContent(
    String city,
    List<String> interests,
    String budget,
    String style,
  ) {
    final normalizedCity = city.toLowerCase().trim();

    switch (normalizedCity) {
      case 'istanbul':
      case 'İstanbul':
        return _getIstanbulContent(interests, budget);
      case 'paris':
        return _getParisContent(interests, budget);
      case 'roma':
      case 'rome':
        return _getRomaContent(interests, budget);
      case 'londra':
      case 'london':
        return _getLondraContent(interests, budget);
      case 'berlin':
        return _getBerlinContent(interests, budget);
      case 'madrid':
        return _getMadridContent(interests, budget);
      case 'sevilla':
      case 'seville':
        return _getSevillaContent(interests, budget);
      case 'viyana':
      case 'vienna':
        return _getViyanaContent(interests, budget);
      case 'prag':
      case 'prague':
        return _getPragContent(interests, budget);
      case 'lizbon':
      case 'lisbon':
        return _getLizbonContent(interests, budget);
      case 'milano':
      case 'milan':
        return _getMilanoContent(interests, budget);
      case 'amsterdam':
        return _getAmsterdamContent(interests, budget);
      case 'tokyo':
        return _getTokyoContent(interests, budget);
      case 'seul':
      case 'seoul':
        return _getSeulContent(interests, budget);
      case 'singapur':
      case 'singapore':
        return _getSingapurContent(interests, budget);
      case 'dubai':
        return _getDubaiContent(interests, budget);
      case 'newyork':
      case 'new york':
        return _getNewYorkContent(interests, budget);
      case 'barcelona':
      default:
        return _getBarcelonaContent(interests, budget);
    }
  }

  static Map<String, String> _getIstanbulContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "İstanbul'a hoş geldin, keşif modunda olduğunu duyunca çok sevindim!",
      'recommendations': '''
⭐ **Fener & Balat Sokakları** - Burası tam bir açık hava müzesi! Renkli cumbalı evleri, Arnavut kaldırımlı daracık sokakları, her köşede karşına çıkacak sürpriz kafeleri ve vintage dükkanlarıyla fotoğraf çekmekten parmakların yorulacak. Eski kiliseler, sinagoglar, camiler bir arada, müthiş bir kültür mozaiği. Küçük antikacılardan, yerel tasarım dükkanlarından ve ikinci el hazinelerinden kendine özgü parçalar bulabilir, orta bütçeyle harika alışveriş yapabilirsin. Buranın ruhunu yakalamak için bolca vakit ayır!

⭐ **Kuzguncuk** - Anadolu Yakası'nın o "sakin köy" havası burada! Dar sokakları, nostaljik bakkalları, rengârenk ahşap evleriyle zamanda yolculuk gibi. Hafta sonu kahvaltısı için İsmail Usta'nın meşhur tostlarını veya Kuzguncuk Börekçisi'ni denemelisin. Boğaz'a nazır banklarda oturup martıları izlemek, fotoğraf için altın saatini yakalamak paha biçilmez. Alışveriş için butik tasarım dükkanları ve antikacılar var.

⭐ **Karaköy & Tersane** - Burası İstanbul'un yeni yaratıcı kalbi! Eski tersane binalarında sanat galerileri, concept store'lar ve muhteşem kafeler var. Street art duvarları fotoğraf için harika. Karaköy Güllüoğlu'nda baklava, Karaköy Lokantası'nda modern Türk mutfağı deneyimle. Akşamüstü İstanbul Modern'in kafesinde Boğaz manzarasıyla gün batımını izle.''',
      'tip':
          "Balat'a hafta içi sabah erken git, hem kalabalıksız fotoğraf çekersin hem de yerel esnafla sohbet edersin. Çay ikram ederlerse reddetme! 🍵",
    };
  }

  static Map<String, String> _getBarcelonaContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Barcelona'ya hoş geldin! Gaudí'nin büyülü şehrinde harika bir macera seni bekliyor!",
      'recommendations': '''
⭐ **Bunkers del Carmel** - Turistlerin bilmediği, yerellerin gizli sakladığı Barcelona'nın en iyi manzara noktası! Eski İç Savaş sığınakları üzerine kurulu bu tepe, 360 derece şehir panoraması sunuyor. Gün batımında git, şehrin ışıkları yanarken şarap iç. Fotoğrafçılar için cennet! Ücretsiz ve kalabalıksız.

⭐ **El Born Mahallesi** - Gotik Mahalle'nin daha cool, daha az turistik versiyonu! Dar sokakları, bağımsız butikleri, vintage dükkanları ve harika tapas barlarıyla keşfetmeye doyamazsın. El Born Kültür Merkezi'nde Roma kalıntılarını gör, Santa Maria del Mar Kilisesi'nin içine gir (ücretsiz ve muhteşem). Kahve için Nomad Coffee, kokteyl için Paradiso (dünyanın en iyi barlarından).

⭐ **Sant Antoni Pazarı** - Yeni restore edilmiş pazar binası mimari harika. Pazar Pazar günleri kitap ve antika pazarına dönüşüyor. Federal Café'de Avustralya tarzı brunch yap, Flax & Kale'de sağlıklı yemek ye. Çevre sokaklar vintage mağazalar ve street art ile dolu.''',
      'tip':
          "La Sagrada Familia'ya bilet al ama sabah 9'da ilk seansta git. Işık o saatte muhteşem ve kalabalık yok! 🌅",
    };
  }

  static Map<String, String> _getParisContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro': "Paris'e hoş geldin! Işıklar şehri seni büyülemeye hazır!",
      'recommendations': '''
⭐ **Le Marais'in Gizli Avluları** - Turistler ana caddelerde kalırken, sen avluların içine dal! Hôtel de Sully'nin bahçesi, Place des Vosges'un arkası, gizli pasajlar... Vintage dükkanları, Yahudi mahallesi lezzetleri (L'As du Fallafel efsane!), LGBTQ+ barları, sanat galerileri. Her köşede fotoğraflık anlar.

⭐ **Canal Saint-Martin** - Amelie filminden çıkma atmosfer! Demir köprüler, kafe terasları, vintage kitapçılar. Chez Prune'de kahve iç, Antoine et Lili'de alışveriş yap. Pazar günleri kanalın kenarında piknik yapan Parisililere katıl. Fotoğraf için altın saat muhteşem.

⭐ **Montmartre'ın Arka Sokakları** - Sacré-Cœur'ün arkasına dolan! Rue Lepic'te yerel pazarda peynir ve şarap al, La Maison Rose önünde fotoğraf çek ama asıl güzellik arka sokaklarda. Rue de l'Abreuvoir Paris'in en romantik sokağı. Au Lapin Agile'de chanson gecesi kaçırma.''',
      'tip':
          "Metro yerine yürü! Paris'i gerçekten keşfetmenin tek yolu bu. Kaybolmaktan korkma, en güzel keşifler tesadüfen olur! 🚶‍♂️",
    };
  }

  static Map<String, String> _getRomaContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Roma'ya hoş geldin! Ebedi şehir 3000 yıllık hazinelerini sana açmaya hazır!",
      'recommendations': '''
⭐ **Trastevere** - Roma'nın gerçek kalbi burası! Sarmaşıklı duvarlar, çamaşır asılı dar sokaklar, meydanlarda oynayan çocuklar... Turistik ama hala otantik. Da Enzo al 29'da cacio e pepe ye (sıra bekle ama değer!), Piazza di Santa Maria'da gece çeşmenin önünde otur, Bar San Calisto'da Negroni iç.

⭐ **Testaccio** - Romalıların Roma'sı! Eski mezbaha binalarında şimdi MACRO müzesi ve gece kulüpleri var. Testaccio Pazarı'nda supplì ve porchetta dene (en iyi street food!). Aventine Tepesi'ndeki Malta Şövalyeleri Kapısı'nın anahtar deliğinden St. Peter's Bazilikası'nı gör - sürpriz manzara!

⭐ **Garbatella** - Hiçbir turistin bilmediği mahalle! 1920'lerin işçi konutları şimdi bohem sanatçı cenneti. Renkli binalar, gizli bahçeler, yerel barlar. Cesare al Casaletto'da gerçek Roma mutfağı ye. Street art duvarları fotoğraf için harika.''',
      'tip':
          "Trastevere'de akşam 7'de aperitivo saati başlar. 8-10€'ya içki + sınırsız büfe! En iyi ekonomik akşam yemeği stratejisi 🍷",
    };
  }

  static Map<String, String> _getLondraContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Londra'ya hoş geldin! Kraliyet şehri modern ve tarihi bir arada sunuyor!",
      'recommendations': '''
⭐ **Shoreditch & Brick Lane** - Londra'nın en cool mahallesi! Street art duvarları her köşede, vintage marketler, bağımsız tasarımcı dükkanları. Pazar günü Brick Lane Market muhteşem. Beigel Bake'de 24 saat taze bagel, Cereal Killer Cafe'de 120 çeşit mısır gevreği. Akşam rooftop barlarda kokteyl!

⭐ **South Bank & Borough Market** - Thames kıyısında yürüyüş, Tate Modern (ücretsiz!), Shakespeare's Globe. Borough Market'ta dünya mutfakları: İngiliz pies, İspanyol jamón, Fransız peynir. Neal's Yard Dairy'de peynir tadımı kaçırma. Gece National Theatre'da oyun izle.

⭐ **Notting Hill & Portobello** - Pastel renkli evler, antika dükkanları, film setleri. Cumartesi Portobello Road Market'ta kaybol. The Churchill Arms pub tamamen çiçeklerle kaplı. Ottolenghi'de brunch, Electric Cinema'da vintage koltuklarda film izle.''',
      'tip':
          "Oyster Card al, tüm toplu taşıma için geçerli. Müzelerin çoğu ücretsiz, sanat galerilerine de giriş yok! 🎨",
    };
  }

  static Map<String, String> _getBerlinContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Berlin'e hoş geldin! Özgür ruhlu, yaratıcı ve tarihi derin bir şehir!",
      'recommendations': '''
⭐ **Kreuzberg** - Berlin'in kalbi burası! Multikulti atmosfer, dönerci, vintage shop, techno kulüp yan yana. Markthalle Neun'da Perşembe Street Food, Görlitzer Park'ta piknik. Oranienstraße'de gece hayatı efsane. Burası gerçek Berlin!

⭐ **Friedrichshain & RAW Gelände** - Eski tren deposu şimdi sanat merkezi! Duvar boyama, pazar, bara, klüp her şey var. East Side Gallery'de Berlin Duvarı'nın en uzun parçası. Boxhagener Platz'da hafta sonu kahvaltı, Simon-Dach-Straße'de bira.

⭐ **Prenzlauer Berg** - Hipster cennet! Mauerpark'ta Pazar günü karaoke ve bit pazarı. Kastanienallee'de butik alışveriş, Kulturbrauerei'de etkinlikler. Konnopke's Imbiss'te currywurst ye, Pratercarten'de Berlin'in en eski birahane bahçesi.''',
      'tip':
          "Berlin ucuz bir şehir. Döner 4€, bira 3€, giriş birçok yere ücretsiz. Club'lara gece 1'den sonra git! 🍺",
    };
  }

  static Map<String, String> _getMadridContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Madrid'e hoş geldin! İspanya'nın kalbinde enerji, sanat ve tapas seni bekliyor!",
      'recommendations': '''
⭐ **La Latina & El Rastro** - Madrid'in en otantik mahallesi! Pazar günü El Rastro bit pazarı efsane. Cava Baja'da tapas bardan bara atla. Casa Lucio'da huevos rotos, Juana la Loca'da pintxo. Akşam La Latina meydanlarında vermouth iç.

⭐ **Malasaña** - Hipster Madrid! Vintage dükkanları, plak mağazaları, street art. Café Comercial'de kahve, Ojalá'nın kumlu zemininde brunch. Gece Calle Velarde'de bar hopping. La Vía Láctea'da canlı müzik.

⭐ **Lavapiés** - Multicultural, gerçek, ucuz! Hint, Çin, Afrika restoranları iç içe. Tabacalera sanat merkezi (ücretsiz), Cine Doré (en eski sinema). El Brillante'de calamares bocadillo ye. Gece açık havada sangria.''',
      'tip':
          "İspanyol saatine ayak uydur: Öğle 14:00, akşam yemeği 21:00, gece çıkışı 01:00'den sonra başlar! 🌙",
    };
  }

  static Map<String, String> _getSevillaContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Sevilla'ya hoş geldin! Flamenko, portakal ağaçları ve tutkulu Endülüs ruhu!",
      'recommendations': '''
⭐ **Triana** - Guadalquivir'in karşı kıyısında gerçek Sevilla! Seramik atölyeleri, flamenko barları, tapas lokantaları. Mercado de Triana'da kahvaltı, Bar Bistec'te carrillada. Akşam nehir kenarında gün batımı, gece Casa de la Memoria'da flamenko.

⭐ **Alameda de Hércules** - Lokal gece hayatının merkezi! Eski mahalle şimdi hipster cenneti. Gün içinde vintage kafeler, gece açık hava barları. El Rinconcillo (1670'den beri!) en eski bar. Duo Tapas'ta modern İspanyol.

⭐ **Barrio Santa Cruz** - Evet turistik ama çok güzel! Labirent sokaklar, gizli avlular, jasmin kokusu. Sabah erken git, kalabalıksız. Casa Tomate'de rooftop kahve. Archivo de Indias'ı gör (ücretsiz, Kolomb haritaları).''',
      'tip':
          "Siesta kutsal! 14:00-17:00 arası çoğu yer kapalı. Bu saatleri dinlenmek veya Alcázar bahçelerinde zaman için kullan 🍊",
    };
  }

  static Map<String, String> _getViyanaContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Viyana'ya hoş geldin! İmparatorluk görkemi, kahve kültürü ve müzik şehri!",
      'recommendations': '''
⭐ **Naschmarkt & Freihausviertel** - Viyana'nın en canlı pazarı! 120+ tezgah: Avusturya, Türk, Balkan lezzetleri. Cumartesi bit pazarı var. Arkasında Freihausviertel'de indie kafeler, vintage mağazalar. Café Savoy'da kahve, Motto'da brunch.

⭐ **MuseumsQuartier** - Dünyanın en büyük sanat komplekslerinden! Leopold Museum, MUMOK, Kunsthalle. Ama asıl önemli olan avludaki dev renkli banklar - Viyanılıların buluşma noktası. Akşam şarap, gece dans. Café Leopold'da rooftop.

⭐ **Spittelberg** - Biedermeier evleri, dar sokaklar, sanat galerileri. Amerlingbeisl'de gizli bahçede yemek. Noel pazarı efsanevi. Yıl boyu butik mağazalar, tasarımcı atölyeleri. Plutzer Bräu'de ev yapımı bira.''',
      'tip':
          "Kahve bir ritüel! Melange sipariş et, pasta al, gazete oku, acele etme. Türk kahvesi istersen şaşırırlar 😄 ☕",
    };
  }

  static Map<String, String> _getPragContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Prag'a hoş geldin! Ortaçağ büyüsü, bira cenneti ve uygun fiyatlar!",
      'recommendations': '''
⭐ **Vinohrady & Žižkov** - Turistsiz Prag! Vinohrady art nouveau binaları, trendy kafeler, LGBT+ dostu. Riegrovy Sady parkında bira bahçesi manzarayla. Žižkov ise underground: ucuz bira, punk bar, yerel pub. Televizyon Kulesi'ne çık.

⭐ **Holešovice** - Eski endüstri bölgesi şimdi sanat merkezi! DOX çağdaş sanat, Vnitroblock yaratıcı hub. Manifesto Market'ta street food, Cross Club'da cyberpunk gece hayatı. Pazar günü Holešovice pazarı muhteşem.

⭐ **Malá Strana** - Evet turistik ama gece sihirli! Gündüz kalabalık, ama akşam 7'den sonra kafeler boşalır. Kampa Adası'nda nehir kenarı, Lennon Duvarı (gece git), U Malého Glena'da jazz. Cafe Lounge'da cheesecake.''',
      'tip':
          "Bira sudan ucuz gerçek! 0.5L 40 Kč (1.5€). Hospoda denen yerel birahane pub'larını ara, turistik olmayan! 🍺",
    };
  }

  static Map<String, String> _getLizbonContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Lizbon'a hoş geldin! Yedi tepe, fado müziği ve pastel de nata cenneti!",
      'recommendations': '''
⭐ **Alfama** - Lizbon'un ruhu burada! Dar sokaklar, azulejo karolar, fado sesleri. Gün batımında Miradouro da Graça'ya çık. Tasca do Chico'da fado (rezervasyon şart), A Baiuca'da yerel deneyim. Feira da Ladra bit pazarı Salı ve Cumartesi.

⭐ **LX Factory** - Eski fabrika şimdi yaratıcı cennet! Kitapçı, restoran, galeri, pazar hepsi bir arada. Landeau'da dünyanın en iyi çikolatalı pastası. Hafta sonu açık hava pazarı. Gece rooftop barlarda dans.

⭐ **Mouraria** - Turistlerin bilmediği gerçek mahalle! Multicultural, Afrikalı, Hintli, Çinli restoranlar. Zé da Mouraria'da fado, Tia Alice'de ev yemekleri. Street art turları muhteşem. Martim Moniz meydanında dünya mutfakları.''',
      'tip':
          "28 numaralı tramvay ikonik ama çok kalabalık. Sabah erken git ya da 12E tramvayını dene, aynı rota daha boş! 🚋",
    };
  }

  static Map<String, String> _getMilanoContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro': "Milano'ya hoş geldin! Moda, tasarım ve gizli avluların şehri!",
      'recommendations': '''
⭐ **Navigli** - Kanallar boyunca akşam hayatı! Aperitivo kültürü burada doğdu. Fonderie Milanesi'de kokteyl, Rita's'ta Spritz. Pazar günü antika pazarı. Gece clubları Tortona'da. Vintage mağazalar, street art, bohem ruh.

⭐ **Brera** - Sanat ve tasarım merkezi! Pinacoteca di Brera muhteşem. Dar sokaklarda galeri, butik, tasarımcı mağazalar. Jamaica'da tarihi kafede aperitivo. Gece Bulgari Hotel'in bahçesinde kokteyl (pahalı ama havası var).

⭐ **Isola** - Yükselen mahalle! Eski işçi semti şimdi hipster cenneti. Frida'da brunch, Blue Note'da jazz. Corso Como 10 tasarım mağazası. Gece Bosco Verticale'nin önünde fotoğraf, sonra Ceresio 7'de rooftop havuz kenarı.''',
      'tip':
          "Aperitivo 18:00-21:00 arası: 10€'ya içki + büfe! Navigli'de birkaç bar gez, en dolu büfeyi seç 🍹",
    };
  }

  static Map<String, String> _getAmsterdamContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Amsterdam'a hoş geldin! Kanallar, bisikletler ve özgür ruhun şehri!",
      'recommendations': '''
⭐ **De Pijp** - Amsterdam'ın en canlı mahallesi! Albert Cuyp pazarı günlük, stroopwafel taze. Brouwerij 't IJ'de değirmende bira, CT Coffee'de kahve. Sarphatipark'ta piknik. Gece küçük barlarda canlı müzik.

⭐ **Jordaan** - Kanal boyunca masal! 17. yy evleri, gizli avlular (hofjes), vintage dükkanları. Noordermarkt'ta Pazartesi bit pazarı, Cumartesi farmer's market. Café Papeneiland (1642'den beri!) elmalı turta. Gece bruin café'lerde bira.

⭐ **NDSM Wharf** - Eski tersane şimdi kültür merkezi! Street art, festival, plaj barı. Pllek'te nehir kenarında brunch. IJ-Hallen'de Avrupa'nın en büyük bit pazarı (ayda 2 kez). Ücretsiz feribot merkeze gidiyor.''',
      'tip':
          "Bisiklet kirala! 10€/gün, şehri gerçekten keşfetmenin tek yolu. Ama tramvay raylarına dikkat et! 🚲",
    };
  }

  static Map<String, String> _getTokyoContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "Tokyo'ya hoş geldin! Gelecek ve gelenek, kaos ve düzen bir arada!",
      'recommendations': '''
⭐ **Shimokitazawa** - Tokyo'nun en cool mahallesi! Vintage dükkanları, küçük kafeler, canlı müzik sahneleri. Trendy olmayan bir şekilde trendy. Shirohige's Cream Puff (Totoro şeklinde!) kaçırma. Gece küçük izakaya'larda sake.

⭐ **Yanaka** - Eski Tokyo! Edo dönemi atmosferi, ahşap evler, kediler (!). Yanaka Ginza alışveriş sokağı, tapınak ve mezarlık gezisi. Kayaba Coffee tarihi kahve. Sakura zamanı en güzel yer burası.

⭐ **Golden Gai** - 200+ küçük bar sığmış 6 dar sokağa! Her biri 5-10 kişilik, her birinin farklı teması. İlk kez gidenler için ürkütücü ama kapı açık olanları dene. Gece 23:00'den sonra gitmen lazım. Efsanevi deneyim!''',
      'tip':
          "Suica kartı al, her yerde geçerli. Kombini'lerde (7-Eleven, Lawson) yemek kaliteli ve ucuz. Onigiri 150¥! 🍙",
    };
  }

  static Map<String, String> _getSeulContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro': "Seul'e hoş geldin! K-pop, BBQ ve 24 saat yaşayan megakent!",
      'recommendations': '''
⭐ **Hongdae** - Gençlik enerjisi! Sokak performansları, indie müzik, gece hayatı 24 saat. Özgür park'ta cuma akşamı konser. Vintage mağazalar, K-beauty dükkanları. Thursday Party'de clubbing. Gece ayak masajı salonları!

⭐ **Ikseon-dong Hanok** - Eski-yeni karışımı! 100 yıllık hanok evler şimdi trendy kafe ve butik. Seoul Coffee'de kahve, Gyeongbokgung sarayına 5 dakika. Fotoğraf için altın. Gece yerel makgeolli barlarında.

⭐ **Euljiro** - Hipster Seoul! Eski metal işleri dükkanları arasında gizli kafeler ve barlar. Café Onion eski ev fabrikasında. Euljiro 3-ga'da retro izakaya'lar. Cheonggyecheon deresi boyunca gece yürüyüşü romantik.''',
      'tip':
          "T-money kart al, metro ve otobüs için. Gece yarısı subway biter, o yüzden 24 saat barlar ve jimjilbang (sauna) var! 🌃",
    };
  }

  static Map<String, String> _getSingapurContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro': "Singapur'a hoş geldin! Gelecekten gelen şehir, yemek cenneti!",
      'recommendations': '''
⭐ **Tiong Bahru** - Singapur'un en eski HDB mahallesi şimdi en cool! Art deco binalar, bağımsız kafeler, kitapçılar. 40 Hands'de kahve, Tiong Bahru Bakery'de croissant. Wet market'ta yerel kahvaltı. Street art yürüyüşü.

⭐ **Kampong Glam** - Arap Sokağı + hipster! Haji Lane dar sokakta graffiti, butik, vintage. Sultan Camii muhteşem. Zam Zam'da murtabak ye. Gece bar hopping, rooftop'lar. Arab Street'te nargile kafeleri.

⭐ **Hawker Centres** - Singapur'un gerçek yemek kültürü! Maxwell Food Centre, Lau Pa Sat, Chinatown Complex. Michelin yıldızlı yemekler 5 SGD! Tian Tian Hainanese Chicken Rice efsane. Gece Clarke Quay'de riverside içki.''',
      'tip':
          "Hawker'larda yemek ye, restoranlara gitme. 5 SGD'ye Michelin kalitesi! Kopi (kahve) ve Teh (çay) dene ☕",
    };
  }

  static Map<String, String> _getDubaiContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro': "Dubai'ye hoş geldin! Çöl mucizesi, lüks ve kontrast şehri!",
      'recommendations': '''
⭐ **Al Fahidi Tarihi Bölgesi** - Dubai'nin ruhu burada! Burj Khalifa'dan önce Dubai böyleydi. Rüzgar kuleleri, müzeler, sanat galerileri. Arabian Tea House'da kahvaltı, XVA Cafe'de öğle. Creek'te abra (1 AED!) ile karşıya geç.

⭐ **Alserkal Avenue** - Dubai'nin sanat merkezi! Eski endüstri bölgesi şimdi 40+ galeri, tasarım stüdyosu. The Third Line, Carbon 12 önemli galeriler. Tom&Serg'de brunch. Cinema Akil'de bağımsız film.

⭐ **Jumeirah Beach & Kite Beach** - Şehrin plajı! Burj Al Arab manzarası. Kite Beach'te aktiviteler, Salt burger, Salt'bae değil gerçek Salt! Gece La Mer'de yürüyüş. Madinat Jumeirah'ta abra turu.''',
      'tip':
          "Cuma günü brunch kültürü var. 200-400 AED'ye sınırsız yiyecek ve içecek büfeleri. Rezervasyon şart! 🍾",
    };
  }

  static Map<String, String> _getNewYorkContent(
    List<String> interests,
    String budget,
  ) {
    return {
      'intro':
          "New York'a hoş geldin! Dünyanın başkenti, 24 saat uyumayan şehir!",
      'recommendations': '''
⭐ **Lower East Side** - Manhattan'ın en cool mahallesi! Göçmen tarihi + modern sanat. Katz's Deli (pastrami efsane!), Russ & Daughters (bagel). Essex Market'ta yemek turu. Gece rooftop barları, speakeasy'ler (Please Don't Tell!).

⭐ **Williamsburg, Brooklyn** - Hipster başkenti! Bedford Ave butik mağazalar, vintage, plak. Smorgasburg (hafta sonu yemek pazarı) muhteşem. Domino Park'ta skyline. Gece Music Hall'da konser, Brooklyn Bowl'da bowling.

⭐ **Bushwick, Brooklyn** - Street art cenneti! Duvar boyamaları her yerde. Roberta's'ta pizza (bahçede), House of Yes'te queer party. Gece kulüpleri underground. Gündüz kafeler, gece rave. Brooklyn'in yükselen yıldızı.''',
      'tip':
          "Subway 24 saat açık! MetroCard değil OMNY (temassız) kullan. Dollar pizza hala 1\$ ve lezzetli 🍕",
    };
  }

  /// Kullanıcı profiline göre "Sürpriz" ve "Lokal" öneriler üretir.
  static Future<List<Highlight>> getSerendipityRecommendations({
    required String city,
    required String travelStyle,
    required List<String> interests,
    required double moodLevel, // 0.0 (Sakin) - 1.0 (Popüler)
  }) async {
    await Future.delayed(const Duration(milliseconds: 600));

    // Şehre göre önerileri seç
    final normalizedCity = city.toLowerCase().trim();

    switch (normalizedCity) {
      case 'paris':
        return _getParisRecommendations(moodLevel);
      case 'roma':
      case 'rome':
        return _getRomaRecommendations(moodLevel);
      case 'istanbul':
      case 'İstanbul':
        return _getIstanbulRecommendations(moodLevel);
      case 'barcelona':
      default:
        return _getBarcelonaRecommendations(moodLevel);
    }
  }

  // =========================================================================
  // BARCELONA ÖNERİLERİ
  // =========================================================================
  static List<Highlight> _getBarcelonaRecommendations(double moodLevel) {
    if (moodLevel < 0.4) {
      // SAKİN
      return [
        Highlight(
          name: "Bunkers del Carmel",
          area: "Carmel",
          category: "Park",
          tags: ["manzara", "gün batımı", "sessiz"],
          distanceFromCenter: 3.8,
          lat: 41.4184,
          lng: 2.1565,
          price: "low",
          description:
              "360 derece şehir manzarası sunan gizli nokta. Gün batımı için mükemmel.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bunkers_del_Carmel_-_panoramio.jpg/800px-Bunkers_del_Carmel_-_panoramio.jpg",
        ),
        Highlight(
          name: "Federal Café",
          area: "Sant Antoni",
          category: "Kafe",
          tags: ["brunch", "kahve", "sakin"],
          distanceFromCenter: 1.1,
          lat: 41.3789,
          lng: 2.1623,
          price: "medium",
          description:
              "Avustralya tarzı brunch kültürü. Sakin bir ortamda flat white keyfi.",
          imageUrl:
              "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800",
        ),
        Highlight(
          name: "Montjuïc",
          area: "Montjuïc",
          category: "Park",
          tags: ["manzara", "park", "doğa"],
          distanceFromCenter: 2.5,
          lat: 41.3639,
          lng: 2.1586,
          price: "low",
          description:
              "Şehre hakim tepe. Botanik bahçeleri ve muhteşem manzara.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Castell_de_Montju%C3%AFc_-_panoramio_%281%29.jpg/800px-Castell_de_Montju%C3%AFc_-_panoramio_%281%29.jpg",
        ),
        Highlight(
          name: "Santa Maria del Mar",
          area: "El Born",
          category: "Tarihi",
          tags: ["kilise", "gotik", "huzur"],
          distanceFromCenter: 0.8,
          lat: 41.3838,
          lng: 2.1817,
          price: "low",
          description:
              "14. yüzyıl Katalan gotiğinin en güzel örneği. Huzurlu atmosfer.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Facade_-_Santa_Maria_del_Mar_-_Barcelona_2014_%28cropped%29.jpg/800px-Facade_-_Santa_Maria_del_Mar_-_Barcelona_2014_%28cropped%29.jpg",
        ),
      ];
    } else if (moodLevel < 0.8) {
      // KEŞİF
      return [
        Highlight(
          name: "Gothic Quarter",
          area: "Ciutat Vella",
          category: "Tarihi",
          tags: ["tarih", "keşif", "yürüyüş"],
          distanceFromCenter: 0.3,
          lat: 41.3833,
          lng: 2.1777,
          price: "low",
          description:
              "Ortaçağ'dan kalma dar sokaklar ve gizli meydanlar. Kaybolmaya hazır ol!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Barri_G%C3%B2tic_-_Barcelona_%28Catalonia%29.jpg/800px-Barri_G%C3%B2tic_-_Barcelona_%28Catalonia%29.jpg",
        ),
        Highlight(
          name: "Satan's Coffee Corner",
          area: "El Born",
          category: "Kafe",
          tags: ["kahve", "minimalist", "gizli"],
          distanceFromCenter: 0.8,
          lat: 41.3849,
          lng: 2.1821,
          price: "medium",
          description:
              "Şehrin en iyi gizli kahve noktası. Minimalist tasarım, mükemmel espresso.",
          imageUrl:
              "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
        ),
        Highlight(
          name: "Picasso Museum",
          area: "El Born",
          category: "Müze",
          tags: ["sanat", "picasso", "kültür"],
          distanceFromCenter: 0.9,
          lat: 41.3853,
          lng: 2.1810,
          price: "medium",
          description:
              "Picasso'nun erken dönem eserlerini keşfet. 4,000'den fazla eser.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Museu_Picasso_Barcelona_-_panoramio.jpg/800px-Museu_Picasso_Barcelona_-_panoramio.jpg",
        ),
        Highlight(
          name: "Paradiso",
          area: "El Born",
          category: "Bar",
          tags: ["kokteyl", "speakeasy", "gizli"],
          distanceFromCenter: 0.7,
          lat: 41.3845,
          lng: 2.1833,
          price: "high",
          description:
              "Pastrami dükkanının arkasındaki gizli speakeasy. Dünyanın en iyi barlarından!",
          imageUrl:
              "https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800",
        ),
      ];
    } else {
      // POPÜLER
      return [
        Highlight(
          name: "Sagrada Familia",
          area: "Eixample",
          category: "Tarihi",
          tags: ["mimari", "gaudí", "ikonik"],
          distanceFromCenter: 2.1,
          lat: 41.4036,
          lng: 2.1744,
          price: "high",
          description:
              "Gaudí'nin tamamlanmamış başyapıtı. Barcelona'nın simgesi!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Basilica_de_la_Sagrada_Familia_-_panoramio_%283%29.jpg/800px-Basilica_de_la_Sagrada_Familia_-_panoramio_%283%29.jpg",
        ),
        Highlight(
          name: "Park Güell",
          area: "Gracia",
          category: "Park",
          tags: ["gaudí", "mozaik", "manzara"],
          distanceFromCenter: 3.5,
          lat: 41.4145,
          lng: 2.1527,
          price: "medium",
          description:
              "Renkli mozaikler ve muhteşem şehir manzarası. Instagram favorisi!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Parc_G%C3%BCell_-_Entrada_Drac.JPG/800px-Parc_G%C3%BCell_-_Entrada_Drac.JPG",
        ),
        Highlight(
          name: "La Boqueria",
          area: "La Rambla",
          category: "Restoran",
          tags: ["pazar", "yemek", "popüler"],
          distanceFromCenter: 0.5,
          lat: 41.3816,
          lng: 2.1719,
          price: "medium",
          description:
              "Tarihi pazar. Taze meyve, deniz ürünleri ve yerel lezzetler.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Mercat_de_la_Boqueria_-_Barcelona%2C_Spain_-_panoramio.jpg/800px-Mercat_de_la_Boqueria_-_Barcelona%2C_Spain_-_panoramio.jpg",
        ),
        Highlight(
          name: "Casa Batlló",
          area: "Passeig de Gràcia",
          category: "Tarihi",
          tags: ["gaudí", "mimari", "trend"],
          distanceFromCenter: 1.2,
          lat: 41.3917,
          lng: 2.1650,
          price: "high",
          description:
              "Gaudí'nin deniz temalı modernist şaheseri. Mutlaka görülmeli!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Casa_Batll%C3%B3_%288623240352%29.jpg/800px-Casa_Batll%C3%B3_%288623240352%29.jpg",
        ),
      ];
    }
  }

  // =========================================================================
  // PARIS ÖNERİLERİ
  // =========================================================================
  static List<Highlight> _getParisRecommendations(double moodLevel) {
    if (moodLevel < 0.4) {
      // SAKİN
      return [
        Highlight(
          name: "Jardin du Luxembourg",
          area: "6ème",
          category: "Park",
          tags: ["park", "saray", "piknik", "romantik"],
          distanceFromCenter: 1.0,
          lat: 48.8462,
          lng: 2.3372,
          price: "low",
          description:
              "Paris'in en sevilen parkı. Yeşil sandalyelerde kitap oku, havuzda yelkenli izle.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Luxembourg_Garden.jpg/1280px-Luxembourg_Garden.jpg",
        ),
        Highlight(
          name: "Shakespeare and Company Café",
          area: "Latin Quarter",
          category: "Kafe",
          tags: ["kitap", "tarihi", "romantik", "kahve"],
          distanceFromCenter: 0.8,
          lat: 48.8526,
          lng: 2.3471,
          price: "medium",
          description:
              "Efsanevi kitapçının yanındaki kafe. Notre-Dame manzarası, kitap kokusu.",
          imageUrl:
              "https://images.unsplash.com/photo-1529158062015-cad636e205a0?w=800",
        ),
        Highlight(
          name: "Canal Saint-Martin",
          area: "10ème",
          category: "Manzara",
          tags: ["kanal", "yürüyüş", "yerel", "sakin"],
          distanceFromCenter: 2.5,
          lat: 48.8728,
          lng: 2.3653,
          price: "low",
          description:
              "Amélie filminden kanal. Demir köprüler, kestane ağaçları. Parisli'lerin piknik yeri.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/P1040157_Paris_X_canal_Saint-Martin_passerelle_Alibert_rwk.JPG/1280px-P1040157_Paris_X_canal_Saint-Martin_passerelle_Alibert_rwk.JPG",
        ),
        Highlight(
          name: "Musée Rodin",
          area: "7ème",
          category: "Müze",
          tags: ["heykel", "bahçe", "romantik"],
          distanceFromCenter: 1.8,
          lat: 48.8552,
          lng: 2.3161,
          price: "medium",
          description:
              "Rodin'in şaheserleri muhteşem bir bahçede. Düşünen Adam, gül bahçesi.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Mus%C3%A9e_Rodin_1.jpg/1280px-Mus%C3%A9e_Rodin_1.jpg",
        ),
      ];
    } else if (moodLevel < 0.8) {
      // KEŞİF
      return [
        Highlight(
          name: "Le Marais",
          area: "Le Marais",
          category: "Alışveriş",
          tags: ["moda", "vintage", "lgbtq", "keşif"],
          distanceFromCenter: 1.5,
          lat: 48.8598,
          lng: 2.3610,
          price: "medium",
          description:
              "Paris'in en trendy semti. Vintage dükkanlar, sanat galerileri, gizli avlular.",
          imageUrl:
              "https://images.unsplash.com/photo-1549144511-f099e773c147?w=800",
        ),
        Highlight(
          name: "Boot Café",
          area: "Le Marais",
          category: "Kafe",
          tags: ["specialty-coffee", "minimal", "instagram"],
          distanceFromCenter: 1.5,
          lat: 48.8637,
          lng: 2.3615,
          price: "medium",
          description:
              "Paris'in en küçük kafelerinden biri. Sadece 5m² ama muhteşem specialty coffee.",
          imageUrl:
              "https://images.unsplash.com/photo-1509042239860-f550ce710b93?w=800",
        ),
        Highlight(
          name: "Little Red Door",
          area: "Le Marais",
          category: "Bar",
          tags: ["speakeasy", "cocktail", "gizli"],
          distanceFromCenter: 1.8,
          lat: 48.8638,
          lng: 2.3625,
          price: "high",
          description:
              "Dünyanın en iyi 50 barı listesinde. Kırmızı kapının arkasında yaratıcı kokteyller.",
          imageUrl:
              "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=800",
        ),
        Highlight(
          name: "Centre Pompidou",
          area: "Le Marais",
          category: "Müze",
          tags: ["modern-sanat", "mimari", "manzara"],
          distanceFromCenter: 1.2,
          lat: 48.8607,
          lng: 2.3524,
          price: "medium",
          description:
              "Modern sanat müzesi. Renkli borularıyla ikonik mimari. Terastan Paris manzarası.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Centre_Georges-Pompidou_34.jpg/1280px-Centre_Georges-Pompidou_34.jpg",
        ),
      ];
    } else {
      // POPÜLER
      return [
        Highlight(
          name: "Eiffel Kulesi",
          area: "7ème",
          category: "Tarihi",
          tags: ["ikonik", "manzara", "romantik"],
          distanceFromCenter: 2.5,
          lat: 48.8584,
          lng: 2.2945,
          price: "medium",
          description:
              "Paris'in simgesi. 330 metre yüksekliğinde demir dantel. Gece ışık gösterisi!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/800px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg",
        ),
        Highlight(
          name: "Louvre Müzesi",
          area: "1er",
          category: "Müze",
          tags: ["sanat", "tarihi", "mona-lisa"],
          distanceFromCenter: 0.3,
          lat: 48.8606,
          lng: 2.3376,
          price: "medium",
          description:
              "Dünyanın en büyük müzesi. Mona Lisa, Venüs de Milo ve 35.000+ eser.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Louvre_Museum_Wikimedia_Commons.jpg/1280px-Louvre_Museum_Wikimedia_Commons.jpg",
        ),
        Highlight(
          name: "Sacré-Cœur",
          area: "Montmartre",
          category: "Tarihi",
          tags: ["bazilika", "manzara", "romantik"],
          distanceFromCenter: 4.0,
          lat: 48.8867,
          lng: 2.3431,
          price: "low",
          description:
              "Montmartre tepesinde beyaz bazilika. Paris'in en iyi manzara noktalarından.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Le_sacre_coeur.jpg/1280px-Le_sacre_coeur.jpg",
        ),
        Highlight(
          name: "Musée d'Orsay",
          area: "7ème",
          category: "Müze",
          tags: ["empresyonizm", "van-gogh", "monet"],
          distanceFromCenter: 1.0,
          lat: 48.8600,
          lng: 2.3266,
          price: "medium",
          description:
              "Empresyonist şaheserlerin evi. Van Gogh, Monet, Renoir. Eski tren istasyonu.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mus%C3%A9e_d%27Orsay%2C_North-West_view%2C_Paris_7e_140402.jpg/1280px-Mus%C3%A9e_d%27Orsay%2C_North-West_view%2C_Paris_7e_140402.jpg",
        ),
      ];
    }
  }

  // =========================================================================
  // ROMA ÖNERİLERİ
  // =========================================================================
  static List<Highlight> _getRomaRecommendations(double moodLevel) {
    if (moodLevel < 0.4) {
      // SAKİN
      return [
        Highlight(
          name: "Giardino degli Aranci",
          area: "Aventino",
          category: "Park",
          tags: ["manzara", "portakal", "romantik"],
          distanceFromCenter: 2.0,
          lat: 41.8836,
          lng: 12.4785,
          price: "low",
          description:
              "Portakal Bahçesi. St. Peter kubbesi manzarası. Roma'nın en romantik noktası.",
          imageUrl:
              "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800",
        ),
        Highlight(
          name: "Tazza d'Oro",
          area: "Centro Storico",
          category: "Kafe",
          tags: ["kahve", "granita", "klasik"],
          distanceFromCenter: 0.2,
          lat: 41.8987,
          lng: 12.4772,
          price: "low",
          description:
              "Pantheon'un yanında 1944'ten beri. Granita di caffè yaz aylarında şart.",
          imageUrl:
              "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=800",
        ),
        Highlight(
          name: "Villa Borghese",
          area: "Villa Borghese",
          category: "Park",
          tags: ["park", "göl", "bisiklet"],
          distanceFromCenter: 1.8,
          lat: 41.9137,
          lng: 12.4869,
          price: "low",
          description:
              "Roma'nın Central Park'ı. 80 hektar yeşillik, göl, Pincio tepesinden manzara.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Villa_Borghese_Park_in_Rome.jpg/1280px-Villa_Borghese_Park_in_Rome.jpg",
        ),
        Highlight(
          name: "Il Goccetto",
          area: "Centro Storico",
          category: "Bar",
          tags: ["şarap", "enoteca", "yerel"],
          distanceFromCenter: 0.7,
          lat: 41.8951,
          lng: 12.4686,
          price: "medium",
          description:
              "1980'lerden beri şarap barı. 800+ şarap, samimi atmosfer.",
          imageUrl:
              "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=800",
        ),
      ];
    } else if (moodLevel < 0.8) {
      // KEŞİF
      return [
        Highlight(
          name: "Trastevere",
          area: "Trastevere",
          category: "Tarihi",
          tags: ["semt", "dar-sokak", "yerel"],
          distanceFromCenter: 1.5,
          lat: 41.8869,
          lng: 12.4693,
          price: "low",
          description:
              "Roma'nın en atmosferik semti. Arnavut kaldırımlı sokaklar, sarmaşıklı duvarlar.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Trastevere_-_panoramio_%289%29.jpg/1280px-Trastevere_-_panoramio_%289%29.jpg",
        ),
        Highlight(
          name: "Da Enzo al 29",
          area: "Trastevere",
          category: "Restoran",
          tags: ["trattoria", "cacio-pepe", "otantik"],
          distanceFromCenter: 1.8,
          lat: 41.8863,
          lng: 12.4692,
          price: "medium",
          description:
              "Trastevere'nin en sevilen trattoriası. Cacio e pepe ve carbonara efsane.",
          imageUrl:
              "https://images.unsplash.com/photo-1546549032-9571cd6b27df?w=800",
        ),
        Highlight(
          name: "The Jerry Thomas Project",
          area: "Centro Storico",
          category: "Bar",
          tags: ["speakeasy", "cocktail", "gizli"],
          distanceFromCenter: 0.4,
          lat: 41.8961,
          lng: 12.4708,
          price: "high",
          description:
              "Roma'nın en iyi speakeasy'si. Şifre gerekli, pre-prohibition kokteyller.",
          imageUrl:
              "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=800",
        ),
        Highlight(
          name: "Mercato di Testaccio",
          area: "Testaccio",
          category: "Alışveriş",
          tags: ["pazar", "yerel", "yemek"],
          distanceFromCenter: 2.2,
          lat: 41.8767,
          lng: 12.4750,
          price: "low",
          description:
              "Romalıların gittiği gerçek pazar. Taze ürünler, street food, sıfır turist.",
          imageUrl:
              "https://images.unsplash.com/photo-1533900298318-6b8da08a523e?w=800",
        ),
      ];
    } else {
      // POPÜLER
      return [
        Highlight(
          name: "Colosseum",
          area: "Centro Storico",
          category: "Tarihi",
          tags: ["antik", "ikonik", "gladyatör"],
          distanceFromCenter: 1.0,
          lat: 41.8902,
          lng: 12.4922,
          price: "medium",
          description:
              "Roma İmparatorluğu'nun simgesi. 50.000 kişilik gladyatör arenası!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg",
        ),
        Highlight(
          name: "Vatikan Müzeleri",
          area: "Vatikan",
          category: "Müze",
          tags: ["sanat", "sistine", "michelangelo"],
          distanceFromCenter: 3.5,
          lat: 41.9065,
          lng: 12.4536,
          price: "medium",
          description:
              "Sistine Şapeli, Raphael Odaları, 7km galeri. Dünyanın en büyük koleksiyonu.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Sistine_Chapel_ceiling_photo_2.jpg/1280px-Sistine_Chapel_ceiling_photo_2.jpg",
        ),
        Highlight(
          name: "Trevi Çeşmesi",
          area: "Centro Storico",
          category: "Tarihi",
          tags: ["çeşme", "ikonik", "dilek"],
          distanceFromCenter: 0.5,
          lat: 41.9009,
          lng: 12.4833,
          price: "low",
          description:
              "Dünyanın en ünlü çeşmesi. Bozuk para at, Roma'ya dönersin!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/1280px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg",
        ),
        Highlight(
          name: "Pantheon",
          area: "Centro Storico",
          category: "Tarihi",
          tags: ["antik", "kubbe", "mimari"],
          distanceFromCenter: 0.2,
          lat: 41.8986,
          lng: 12.4769,
          price: "low",
          description:
              "2000 yıllık mükemmel kubbe. Dünyanın en iyi korunmuş antik binası.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Rome_Pantheon_front.jpg/1280px-Rome_Pantheon_front.jpg",
        ),
      ];
    }
  }

  // =========================================================================
  // İSTANBUL ÖNERİLERİ
  // =========================================================================
  static List<Highlight> _getIstanbulRecommendations(double moodLevel) {
    if (moodLevel < 0.4) {
      // SAKİN
      return [
        Highlight(
          name: "Pierre Loti Tepesi",
          area: "Eyüp",
          category: "Manzara",
          tags: ["tepe", "tarihi", "çay"],
          distanceFromCenter: 6.0,
          lat: 41.0531,
          lng: 28.9313,
          price: "low",
          description:
              "Fransız yazarın favori yeri. Haliç manzarası, tarihi çay bahçesi.",
          imageUrl:
              "https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?w=800",
        ),
        Highlight(
          name: "Mandabatmaz",
          area: "Beyoğlu",
          category: "Kafe",
          tags: ["türk-kahvesi", "tarihi", "efsane"],
          distanceFromCenter: 2.3,
          lat: 41.0326,
          lng: 28.9772,
          price: "low",
          description:
              "1967'den beri İstanbul'un en iyi Türk kahvesi. Minik mekan, muazzam köpük.",
          imageUrl:
              "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=800",
        ),
        Highlight(
          name: "Bebek Sahili",
          area: "Bebek",
          category: "Manzara",
          tags: ["sahil", "yürüyüş", "boğaz"],
          distanceFromCenter: 7.0,
          lat: 41.0770,
          lng: 29.0438,
          price: "low",
          description:
              "Boğaz'ın en şık sahili. Tarihi yalılar, lüks kafeler, koşu parkuru.",
          imageUrl:
              "https://images.unsplash.com/photo-1604580864964-0462f5d5b1a8?w=800",
        ),
        Highlight(
          name: "Yerebatan Sarnıcı",
          area: "Sultanahmet",
          category: "Tarihi",
          tags: ["bizans", "yeraltı", "mistik"],
          distanceFromCenter: 0.2,
          lat: 41.0084,
          lng: 28.9779,
          price: "medium",
          description:
              "Bizans'ın yeraltı su deposu. 336 sütun, Medusa başları, mistik atmosfer.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Basilica_Cistern_Yerebatan_Istanbul.jpg/1280px-Basilica_Cistern_Yerebatan_Istanbul.jpg",
        ),
      ];
    } else if (moodLevel < 0.8) {
      // KEŞİF
      return [
        Highlight(
          name: "Kadıköy Çarşı",
          area: "Kadıköy",
          category: "Alışveriş",
          tags: ["pazar", "yerel", "balık"],
          distanceFromCenter: 5.0,
          lat: 40.9912,
          lng: 29.0235,
          price: "medium",
          description:
              "İstanbul'un en canlı semti. Balık pazarı, antikacılar, sokak sanatı.",
          imageUrl:
              "https://images.unsplash.com/photo-1587129035511-d52a3dce8c67?w=800",
        ),
        Highlight(
          name: "Çiya Sofrası",
          area: "Kadıköy",
          category: "Restoran",
          tags: ["anadolu", "yerel", "ev-yemekleri"],
          distanceFromCenter: 5.5,
          lat: 40.9905,
          lng: 29.0258,
          price: "medium",
          description:
              "Anadolu mutfağının yaşayan müzesi. Anthony Bourdain'in favorisi.",
          imageUrl:
              "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=800",
        ),
        Highlight(
          name: "Münferit",
          area: "Asmalımescit",
          category: "Bar",
          tags: ["cocktail", "speakeasy", "gizli"],
          distanceFromCenter: 2.2,
          lat: 41.0305,
          lng: 28.9765,
          price: "medium",
          description:
              "İstanbul'un en iyi kokteyl barlarından. Dar, samimi, harika mixology.",
          imageUrl:
              "https://images.unsplash.com/photo-1572116469696-31de0f17cc34?w=800",
        ),
        Highlight(
          name: "İstanbul Modern",
          area: "Karaköy",
          category: "Müze",
          tags: ["modern-sanat", "çağdaş", "boğaz"],
          distanceFromCenter: 1.5,
          lat: 41.0263,
          lng: 28.9778,
          price: "medium",
          description:
              "Türkiye'nin ilk modern sanat müzesi. Renzo Piano binası, Boğaz manzaralı kafe.",
          imageUrl:
              "https://images.unsplash.com/photo-1594008317973-ffd4a5ac2f09?w=800",
        ),
      ];
    } else {
      // POPÜLER
      return [
        Highlight(
          name: "Ayasofya",
          area: "Sultanahmet",
          category: "Tarihi",
          tags: ["cami", "bizans", "kubbe", "ikonik"],
          distanceFromCenter: 0.2,
          lat: 41.0086,
          lng: 28.9802,
          price: "low",
          description:
              "1500 yıllık mimari mucize. Bizans bazilikası, Osmanlı camisi. Muazzam kubbe.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/1280px-Hagia_Sophia_Mars_2013.jpg",
        ),
        Highlight(
          name: "Topkapı Sarayı",
          area: "Sultanahmet",
          category: "Müze",
          tags: ["saray", "osmanlı", "harem"],
          distanceFromCenter: 0.5,
          lat: 41.0115,
          lng: 28.9833,
          price: "medium",
          description:
              "400 yıl Osmanlı'nın yönetim merkezi. Harem, Hazine, Kutsal Emanetler.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Topkap%C4%B1_-_01.jpg/1280px-Topkap%C4%B1_-_01.jpg",
        ),
        Highlight(
          name: "Kapalıçarşı",
          area: "Beyazıt",
          category: "Alışveriş",
          tags: ["çarşı", "tarihi", "halı"],
          distanceFromCenter: 0.8,
          lat: 41.0106,
          lng: 28.9682,
          price: "medium",
          description:
              "Dünyanın en eski ve büyük kapalı çarşısı. 4000+ dükkan, 61 sokak.",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Kapalicarsi-2023-11-DSC05497.jpg/1280px-Kapalicarsi-2023-11-DSC05497.jpg",
        ),
        Highlight(
          name: "Boğaz Turu",
          area: "Eminönü",
          category: "Manzara",
          tags: ["boğaz", "vapur", "manzara"],
          distanceFromCenter: 0.5,
          lat: 41.0170,
          lng: 28.9686,
          price: "low",
          description:
              "İki kıta arasında vapur yolculuğu. Yalılar, köprüler, kaleler. En güzel deneyim!",
          imageUrl:
              "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Bosphorus._Istanbul%2C_Turkey.jpg/1280px-Bosphorus._Istanbul%2C_Turkey.jpg",
        ),
      ];
    }
  }
}
