import 'dart:io';
import 'dart:convert';
import 'package:path_provider/path_provider.dart';
import 'package:flutter/foundation.dart';

/// City Blog Content - Detailed guide content for all cities
class CityBlogContent {
  
  static Future<String> getRemoteContent(String city, bool isEnglish) async {
    try {
      final normalizedCity = city.toLowerCase().trim()
          .replaceAll(' ', '')
          .replaceAll('İstanbul', 'istanbul')
          .replaceAll('i̇stanbul', 'istanbul')
          .replaceAll('stokholm', 'stockholm')
          .replaceAll('zürih', 'zurih')
          .replaceAll('budapeşte', 'budapeste')
          .replaceAll('strazburg', 'strasbourg');
          
      final directory = await getApplicationDocumentsDirectory();
      final file = File('${directory.path}/guides/$normalizedCity.json');

      if (await file.exists()) {
        final String content = await file.readAsString();
        final Map<String, dynamic> jsonData = json.decode(content);
        return jsonData[isEnglish ? 'en' : 'tr']?.toString() ?? '';
      }
    } catch (e) {
      debugPrint("⚠️ CityBlogContent: Uzak rehber yüklenemedi: $e");
    }
    return getContent(city, isEnglish); // Fallback to hardcoded
  }

  static String getContent(String city, bool isEnglish) {
    final c = city.toLowerCase().trim();
    
    switch (c) {
      case 'roma':
      case 'rome':
        return isEnglish ? _romaEN : _romaTR;
      case 'londra':
      case 'london':
        return isEnglish ? _londraEN : _londraTR;
      case 'berlin':
        return isEnglish ? _berlinEN : _berlinTR;
      case 'amsterdam':
        return isEnglish ? _amsterdamEN : _amsterdamTR;
      case 'tokyo':
        return isEnglish ? _tokyoEN : _tokyoTR;
      case 'new york':
        return isEnglish ? _newyorkEN : _newyorkTR;
      case 'atina':
      case 'athens':
        return isEnglish ? _atinaEN : _atinaTR;
      case 'prag':
      case 'prague':
        return isEnglish ? _pragEN : _pragTR;
      case 'viyana':
      case 'vienna':
        return isEnglish ? _viyanaEN : _viyanaTR;
      case 'lizbon':
      case 'lisbon':
        return isEnglish ? _lizbonEN : _lizbonTR;
      case 'porto':
        return isEnglish ? _portoEN : _portoTR;
      case 'floransa':
      case 'florence':
        return isEnglish ? _floransaEN : _floransaTR;
      case 'venedik':
      case 'venice':
        return isEnglish ? _venedikEN : _venedikTR;
      case 'madrid':
        return isEnglish ? _madridEN : _madridTR;
      case 'sevilla':
      case 'seville':
        return isEnglish ? _sevillaEN : _sevillaTR;
      case 'dubai':
        return isEnglish ? _dubaiEN : _dubaiTR;
      case 'singapur':
      case 'singapore':
        return isEnglish ? _singapurEN : _singapurTR;
      case 'bangkok':
        return isEnglish ? _bangkokEN : _bangkokTR;
      case 'seul':
      case 'seoul':
        return isEnglish ? _seulEN : _seulTR;
      case 'istanbul':
      case 'İstanbul':
      case 'i̇stanbul':
        return isEnglish ? _istanbulEN : _istanbulTR;
      case 'paris':
        return isEnglish ? _parisEN : _parisTR;
      case 'marakes':
      case 'marakeş':
      case 'marrakech':
        return isEnglish ? _marakesEN : _marakesTR;
      case 'milano':
      case 'milan':
        return isEnglish ? _milanoEN : _milanoTR;
      case 'napoli':
      case 'naples':
        return isEnglish ? _napoliEN : _napoliTR;
      case 'budapeste':
      case 'budapeşte':
      case 'budapest':
        return isEnglish ? _budapesteEN : _budapesteTR;
      case 'stokholm':
      case 'stockholm':
        return isEnglish ? _stokholmEN : _stokholmTR;
      case 'zurih':
      case 'zürih':
      case 'zurich':
        return isEnglish ? _zurihEN : _zurihTR;
      case 'cenevre':
      case 'geneva':
        return isEnglish ? _cenevreEN : _cenevreTR;
      case 'lucerne':
      case 'luzern':
        return isEnglish ? _lucerneEN : _lucerneTR;
      case 'lyon':
        return isEnglish ? _lyonEN : _lyonTR;
      case 'marsilya':
      case 'marseille':
        return isEnglish ? _marsilyaEN : _marsilyaTR;
      case 'nice':
        return isEnglish ? _niceEN : _niceTR;
      case 'hongkong':
      case 'hong kong':
        return isEnglish ? _hongKongEN : _hongKongTR;
      case 'dublin':
        return isEnglish ? _dublinEN : _dublinTR;
      case 'kopenhag':
      case 'copenhagen':
        return isEnglish ? _kopenhagEN : _kopenhagTR;
      case 'barcelona':
        return isEnglish ? _barcelonaEN : _barcelonaTR;
      case 'newyork':
      case 'new york':
        return isEnglish ? _newyorkEN : _newyorkTR;
      case 'antalya':
        return isEnglish ? _antalyaEN : _antalyaTR;
      case 'cappadocia':
      case 'kapadokya':
        return isEnglish ? _kapadokyaEN : _kapadokyaTR;
      case 'gaziantep':
        return isEnglish ? _gaziantepEN : _gaziantepTR;

      case 'belgrad':
      case 'belgrade':
        return isEnglish ? _belgradEN : _belgradTR;
      case 'saraybosna':
      case 'sarajevo':
        return isEnglish ? _saraybosnaEN : _saraybosnaTR;
      case 'kotor':
        return isEnglish ? _kotorEN : _kotorTR;
      case 'oslo':
        return isEnglish ? _osloEN : _osloTR;
      case 'rovaniemi':
        return isEnglish ? _rovaniemiEN : _rovaniemiTR;
      case 'tromso':
      case 'tromsø':
        return isEnglish ? _tromsoEN : _tromsoTR;
      case 'edinburgh':
        return isEnglish ? _edinburghEN : _edinburghTR;
      case 'bruksel':
      case 'brussels':
        return isEnglish ? _brukselEN : _brukselTR;
      case 'brugge':
      case 'bruges':
        return isEnglish ? _bruggeEN : _bruggeTR;
      case 'strazburg':
      case 'strasbourg':
        return isEnglish ? _strazburgEN : _strazburgTR;
      case 'heidelberg':
        return isEnglish ? _heidelbergEN : _heidelbergTR;
      case 'colmar':
        return isEnglish ? _colmarEN : _colmarTR;
      case 'giethoorn':
        return isEnglish ? _giethoornEN : _giethoornTR;
      case 'sintra':
        return isEnglish ? _sintraEN : _sintraTR;
      case 'san_sebastian':
      case 'san sebastian':
        return isEnglish ? _sanSebastianEN : _sanSebastianTR;
      case 'bologna':
        return isEnglish ? _bolognaEN : _bolognaTR;
      case 'matera':
        return isEnglish ? _materaEN : _materaTR;
      case 'santorini':
        return isEnglish ? _santoriniEN : _santoriniTR;
      case 'kahire':
      case 'cairo':
        return isEnglish ? _kahireEN : _kahireTR;
      case 'fes':
      case 'fez':
        return isEnglish ? _fesEN : _fesTR;
      case 'zermatt':
        return isEnglish ? _zermattEN : _zermattTR;
      case 'hallstatt':
        return isEnglish ? _hallstattEN : _hallstattTR;
      default:
        return '';
    }
  }

  // ROMA
  static const _romaTR = '''# Roma Rehberi: Ebedi Şehir 🇮🇹

Roma sadece bir şehir değil, açık hava müzesidir. Her köşesinde binlerce yıllık tarih fısıldar. İşte kaotik ama büyüleyici Roma'yı bir yerli gibi yaşamanın yolları.

## 📅 Ne Zaman Gidilir?
- **Bahar (Nisan-Haziran):** Hava ılıktır, çiçekler açar. Yürüyerek keşfetmek için en ideal zaman.
- **Sonbahar (Eylül-Ekim):** Yaz sıcağı biter, "Ottobrata Romana" (Roma'nın Ekim güneşi) şehre altın rengi bir hava katar.
- **İpucu:** Ağustos ayından kaçının; hem çok sıcaktır hem de birçok yerli dükkanını kapatıp tatile çıkar.

## 🏘️ Konaklama Rehberi
- **Trastevere:** Şehrin kalbi burada atar. Arnavut kaldırımlı sokaklar, sarmaşıklı binalar ve en iyi gece hayatı.
- **Monti:** Kolezyum'un hemen yanında ama turistik kalabalıktan uzak. Vintage dükkanlar ve şık kafeler.
- **Prati:** Vatikan'a yakın, daha modern ve düzenli. Alışveriş ve yerel restoranlar için harika.

## 🍽️ Ne Yenir ve İçilir?
- **Dört Klasik:** Roma mutfağı dört temel makarna üzerine kuruludur: *Carbonara* (krema asla olmaz!), *Cacio e Pepe*, *Amatriciana* ve *Gricia*.
- **Kahve Kuralları:** Sabahları *Cappuccino* içilir, ancak öğleden sonra sadece *Espresso* (un caffè) istenir. Kahveyi barda ayakta içmek daha ucuzdur; masaya oturursanız fiyat artar.
- **Su Sebilleri (Nasoni):** Şehrin her yerindeki dökme demir çeşmelerden su içilebilir. Bedava, buz gibi ve tertemizdir.
- **Yemek Saatleri:** Akşam yemeği 20:30'dan önce pek başlamaz. Acele etmeyin, Roma'nın tadını çıkarın.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Roma'yı keşfetmenin tek gerçek yolu yürümektir. Şehir merkezi yürünebilir mesafededir.
- **Roma Pass:** 48 veya 72 saatlik kartlar; toplu taşıma ve ilk 1-2 müze için avantajlıdır.
- **Termini Uyarısı:** Ana tren istasyonu geceleri biraz tekinsiz olabilir, eşyalarınıza dikkat edin.

## 💎 Lokal Sırlar & İpuçları
- [Gizli Anahtar Deliği](search:Piazza dei Cavalieri di Malta): Aventine Tepesi'ndeki *Piazza dei Cavalieri di Malta*'da bulunan meşhur delikten bakınca, Aziz Petrus Bazilikası'nı harika bir perspektifle görebilirsiniz.
- **Ücretsiz Manzara:** [Gianicolo Tepesi](search:Gianicolo Tepesi) veya [Pincio Terrazza](search:Pincio Terrazza), gün batımında şehri izlemek için en romantik noktalardır.
- **Güvenlik:** Trevi Çeşmesi ve Kolezyum gibi çok kalabalık yerlerde yankesicilere karşı tetikte olun. Çantanız hep önünüzde olsun.''';

  static const _romaEN = '''# Rome Guide: The Eternal City 🇮🇹

Rome isn't just a destination; it's an open-air museum. Every corner whispers thousands of years of history. Here is how to experience this chaotic yet mesmerizing city like a local.

## 📅 Best Time to Visit
- **Spring (April-June):** Mild weather and blooming flowers. Perfect for exploring the city by foot.
- **Autumn (Sept-Oct):** The summer heat fades, and the "Ottobrata Romana" (Roman October sun) gives the city a golden glow.
- **Tip:** Avoid August if you can; it's incredibly hot, and many locals close their shops for vacation.

## 🏘️ Neighborhood Guide
- **Trastevere:** The heartbeat of the city. Cobblestone streets, ivy-covered buildings, and the best nightlife.
- **Monti:** Right next to the Colosseum but away from the tourist swarms. Think vintage shops and chic cafes.
- **Prati:** Close to the Vatican, more modern and upscale. Great for shopping and authentic restaurants.

## 🍝 Food & Dining Etiquette
- **The Four Classics:** Roman cuisine is built on four core pastas: *Carbonara* (never with cream!), *Cacio e Pepe*, *Amatriciana*, and *Gricia*.
- **Coffee Rules:** *Cappuccino* is for mornings only. After midday, order *Espresso* (un caffè). Drinking coffee standing at the bar is cheaper; sitting down costs more.
- **Nasoni (Water Fountains):** You'll see iron fountains everywhere. The water is free, ice-cold, and perfectly safe to drink.
- **Meal Times:** Dinner rarely starts before 8:30 PM. Don't rush; Rome is meant to be savored slowly.

## 🚇 Transportation Tips
- **Walking:** The only real way to feel Rome is to walk. The historic center is mostly manageable on foot.
- **Roma Pass:** 48 or 72-hour cards; includes public transport and your first 1-2 museum entries.
- **Termini Safety:** The main station can be sketchy at night; keep a close eye on your belongings.

## 💎 Local Secrets & Insights
- [The Secret Keyhole](search:Piazza dei Cavalieri di Malta): Head to the [Piazza dei Cavalieri di Malta](search:Piazza dei Cavalieri di Malta) on Aventine Hill. Look through the famous keyhole for a perfectly framed view of St. Peter's Basilica.
- **Free Views:** [Gianicolo Hill](search:Gianicolo Hill) or [Pincio Terrazza](search:Pincio Terrazza) are the most romantic spots to watch the sunset over the city silhouette.
- **Safety Specifics:** Be extremely vigilant about pickpockets in crowded areas like the Trevi Fountain and the Colosseum. Keep your bags in front of you at all times.''';

  // LONDRA
  static const _londraTR = '''# Londra Rehberi: Kraliyet Mirası ve Modern Enerji 🇬🇧

Londra; tarihin, modanın ve finansın baş döndürücü bir karışımıdır. Yağmurlu klişelerin ötesinde, her mahallesinde farklı bir dünya saklar.

## 📅 Ne Zaman Gidilir?
- **Yaz (Haziran-Ağustos):** Parkların en canlı olduğu, açık hava festivallerinin tavan yaptığı dönem. Hava genellikle şaşırtıcı derecede güzeldir.
- **Aralık:** Şehir ışıl ışıldır. Noel pazarları ve Regent Street neonları için en büyüleyici zaman.
- **İpucu:** Londra her mevsim yağmurlu olabilir; çantanızda her zaman küçük bir şemsiye bulundurun.

## 🏘️ Konaklama Rehberi
- **Shoreditch/Hoxton:** Hipster kültürü, sokak sanatı ve harika gece hayatı. Şehrin en dinamik bölgesi.
- **South Kensington:** Müzeler bölgesi. Daha şık, sakin ve lüks bir atmosfer isteyenler için ideal.
- **Marylebone:** Şehrin göbeğinde bir İngiliz köyü gibi. Butik dükkanlar ve meşhur kitapçılar burada.

## 🍽️ Ne Yenir ve İçilir?
- **Sunday Roast:** Bir Pazar geleneğidir. İyi bir pub bulun ve fırınlanmış et, Yorkshire pudding ve sebze tabağının tadını çıkarın.
- **Afternoon Tea:** Turistik oteller pahalı olabilir; daha lokal ve şık kafelerde de bu çay seremonisini yaşayabilirsiniz.
- **Pub Kültürü:** Pub'larda masaya servis olmaz. İçeceğinizi barın önünde sipariş edin ve ödemenizi hemen yapın.
- **Borough Market:** Gurme lezzetler için mutlaka uğrayın. Dünyanın her yerinden taze yemekler bulabilirsiniz.

## 🚇 Ulaşım İpuçları
- **Oyster & Contactless:** Kağıt biletlerle uğraşmayın. Temassız kredi kartınız veya Oyster kartınızla tüm ağda (Metro ve Otobüs) seyahat edin.
- **The Tube:** Şehrin damarlarıdır. "Mind the Gap" anonsuna alışın.
- **Çift Katlı Otobüsler:** En üst katın en ön koltuğu, şehri gezmek için en ucuz ve en keyifli "tur otobüsüdür".

## 💎 Lokal Sırlar & İpuçları
- **Ücretsiz Manzaralar:** [The Shard](search:The Shard) için çok para ödemek yerine, [Sky Garden](search:Sky Garden) veya [The Lookout](search:The Lookout) için ücretsiz rezervasyon yapın (haftalar önceden yapılmalı). Manzara aynı ve bedava!
- **Müze Akşamları:** Birçok büyük müze (British Museum, V&A) Cuma akşamları geç saate kadar açıktır ve daha az kalabalıktır.
- **Görgü Kuralları:** Yürüyen merdivenlerde mutlaka sağda durun, soldan yürüyenlerin yolunu kapatmayın. Bu Londra'nın en temel kuralıdır.''';

  static const _londraEN = '''# London Guide: Royal Heritage & Modern Energy 🇬🇧

London is a dizzying blend of history, fashion, and finance. Beyond the rainy clichés, it hides a different world in every neighborhood.

## 📅 Best Time to Visit
- **Summer (June-August):** When parks are at their liveliest and outdoor festivals are at their peak. The weather is often surprisingly pleasant.
- **December:** The city is glowing. The most magical time for Christmas markets and the neon lights of Regent Street.
- **Tip:** London can be rainy in any season; always keep a small umbrella in your bag.

## 🏘️ Neighborhood Guide
- **Shoreditch/Hoxton:** Hipster culture, street art, and fantastic nightlife. The most dynamic part of the city.
- **South Kensington:** The museum district. Ideal for those who want a more elegant, quiet, and upscale atmosphere.
- **Marylebone:** Feels like a classic British village in the heart of the city. High-end boutiques and famous bookstores are here.

## 🍽️ Food & Dining Etiquette
- **Sunday Roast:** A Sunday tradition. Find a good pub and enjoy roasted meat, Yorkshire pudding, and gravy.
- **Afternoon Tea:** High-end hotel teas can be pricey; you can experience this ceremony in more local and chic cafes too.
- **Pub Etiquette:** There is rarely table service in pubs. Order your drink at the bar and pay immediately.
- **Borough Market:** A must-visit for foodies. You can find fresh food and gourmet treats from all over the world.

## 🚇 Transportation Tips
- **Oyster & Contactless:** Don't bother with paper tickets. Use your contactless card or Oyster card to travel across the entire network (Tube and Bus).
- **The Tube:** The veins of the city. Get used to the "Mind the Gap" announcement.
- **Double-Decker Buses:** The front seat on the top deck is the cheapest and most enjoyable "tour bus" in town.

## 💎 Local Secrets & Insights
- **Free Views:** Instead of paying for [The Shard](search:The Shard), book a free ticket for the [Sky Garden](search:Sky Garden) or [The Lookout](search:The Lookout) (must be done weeks in advance). The view is the same and free!
- **Museum Lates:** Many major museums (British Museum, V&A) are open late on Friday evenings and are usually less crowded.
- **Etiquette:** Always stand on the right on escalators, leaving the left free for those who wish to walk. This is London's most fundamental unwritten law.''';

  // BERLIN
  static const _berlinTR = '''# Berlin Rehberi: Tarih, Sanat ve Özgür Ruh 🇩🇪

Berlin; sadece Almanya'nın başkenti değil, aynı zamanda Avrupa'nın yaratıcı enerji deposudur. Yıkılan duvarların arasından doğan, her köşesinde tarihi barındıran ama yüzü tamamen geleceğe dönük bir şehir.

## 📅 Ne Zaman Gidilir?
- **Yaz (Haziran-Ağustos):** Şehir tam anlamıyla sokağa dökülür. Kanalların kenarında piknikler, açık hava sinemaları ve bitmek bilmeyen festivaller.
- **Aralık:** Berlin, Avrupa'nın en iyi Noel pazarlarına ev sahipliği yapar. Soğuktur ama atmosfer büyüleyicidir.
- **İpucu:** Pazar günleri Berlin'de vites düşer. Mauerpark'taki devasa bit pazarı ve karaoke etkinliği bir Berlin klasiğidir.

## 🏘️ Semt Rehberi
- **Mitte:** Şehrin tarihi kalbi. Müzeler Adası, Brandenburg Kapısı ve ana turistik noktalar burada.
- **Kreuzberg:** Berlin'in alternatif ve çok kültürlü yüzü. Sanat galerileri, meşhur gece hayatı ve harika Türk mutfağı.
- **Prenzlauer Berg:** Daha nezih, aile dostu ve "hipster" bir bölge. Şık kafeler ve butik dükkanlarla dolu.
- **Friedrichshain:** Gece hayatının ve sokak sanatının merkezi. East Side Gallery (Duvarın kalıntıları) burada yer alır.

## 🍽️ Ne Yenir ve İçilir?
- **Döner Kebab:** Berlin stili döner bir dünya markasıdır. *Mustafa's Gemüse Kebap* gibi popüler yerlerin önündeki uzun kuyruklara hazırlıklı olun.
- **Currywurst:** Üzerine köri serpilmiş sosis. Berlin'in ikonik sokak lezzetidir.
- **Biergarten Kültürü:** Hava güzelse bir "Biergarten"a (Bira bahçesi) gidip yerlilerle uzun masalarda oturmak bir zorunluluktur.
- **Nakit Paradoks:** Berlin gibi modern bir şehirde bile birçok küçük dükkan ve kafe hala "Nur Cash" (Sadece Nakit) çalışır. Yanınızda mutlaka Euro bulundurun.

## 🚇 Ulaşım İpuçları
- **S-Bahn ve U-Bahn:** Şehir inanılmaz bir raylı sistem ağına sahiptir. Google Maps veya BVG uygulamasıyla her yere kolayca gidersiniz.
- **Bisiklet:** Berlin düz bir şehirdir ve harika bisiklet yolları vardır. Şehri keşfetmenin en özgür yolu bisiklet kiralamaktır.
- **Bilet Onayı:** Biletinizi makineye okutmayı (validate) sakın unutmayın; kontrolörler çok katıdır.

## 💎 Lokal Sırlar & İpuçları
- [Tempelhofer Feld](search:Tempelhof Park): Kapatılan devasa bir havalimanının uçak pistlerinde yürümek, paten kaymak veya mangal yapmak sadece Berlin'de yaşayacağınız bir deneyimdir.
- [Thai Park](search:Thai Park): Hafta sonları Preußenpark'ta kurulan, Taylandlı kadınların ev yapımı yemekler sattığı bu açık hava pazarı gerçek bir gizli cevherdir.
- [Teufelsberg](search:Teufelsberg): Soğuk Savaş döneminden kalma terk edilmiş dinleme istasyonu. Hem tarihi bir gizem hem de muhteşem bir şehir manzarası sunar.''';

  static const _berlinEN = '''# Berlin Guide: History, Art & The Free Spirit 🇩🇪

Berlin is more than just Germany's capital; it’s the creative pulse of Europe. A city born from the shadows of a fallen wall, it holds history in every corner while keeping its eyes fixed firmly on the future.

## 📅 Best Time to Visit
- **Summer (June-August):** The city literally moves outdoors. Picnics by the canals, open-air cinemas, and non-stop street festivals.
- **December:** Berlin hosts some of the best Christmas markets in the world. It’s cold, but the magical atmosphere is worth it.
- **Tip:** Sundays are slow in Berlin. Spending the day at Mauerpark for the massive flea market and outdoor karaoke is a local rite of passage.

## 🏘️ Neighborhood Guide
- **Mitte:** The historic heart. Home to Museum Island, Brandenburg Gate, and the major tourist landmarks.
- **Kreuzberg:** The alternative, multicultural soul of Berlin. Known for its art galleries, legendary nightlife, and incredible Turkish food.
- **Prenzlauer Berg:** More upscale, family-friendly, and hipster-chic. Filled with stylish cafes and independent boutiques.
- **Friedrichshain:** The hub of nightlife and street art. This is where you'll find the East Side Gallery (remnants of the Wall).

## 🍽️ Food & Dining Etiquette
- **Döner Kebab:** Berlin-style döner is a global icon. Be prepared for long waits at famous spots like *Mustafa's Gemüse Kebap*.
- **Currywurst:** Sliced sausage with curry-spiced ketchup. It’s the quintessential Berlin street snack.
- **Biergarten Culture:** When the weather is fine, sitting at long communal tables in a Biergarten is a mandatory social experience.
- **The Cash Paradox:** Despite being a modern tech hub, many small shops and cafes in Berlin remain "Nur Cash" (Cash Only). Always carry Euros.

## 🚇 Transportation Tips
- **S-Bahn & U-Bahn:** The rail network is extensive and efficient. Use the BVG app to navigate seamlessly everywhere.
- **Cycling:** Berlin is flat and extremely bike-friendly. Renting a bike is the most liberating way to explore the different districts.
- **Validation:** Always validate your paper ticket at the yellow or red machines on the platform; inspectors are strict and fines are high.

## 💎 Local Secrets & Insights
- [Tempelhofer Feld](search:Tempelhof Park): Walking, skating, or BBQing on the runways of a massive former airport is an experience you can only find in Berlin.
- [Thai Park](search:Thai Park): An open-air weekend market in Preußenpark where local Thai grandmas sell incredible home-cooked food. A true hidden gem.
- [Teufelsberg](search:Teufelsberg): An abandoned Cold War listening station. It offers a mix of historical mystery, street art, and one of the highest viewpoints in the city.''';

  // AMSTERDAM
  static const _amsterdamTR = '''# Amsterdam Rehberi: Kanallar, Bisikletler ve Özgürlük 🇳🇱

Amsterdam sadece kanallardan ibaret değildir; o, her köşesinde yaratıcılığın ve hoşgörünün hissedildiği yaşayan bir sanat eseridir.

## 📅 Ne Zaman Gidilir?
- **Lale Mevsimi (Nisan):** Şehir ve yakındaki *Keukenhof* bahçeleri renk cümbüşüne döner. Kral Günü (27 Nisan) ise tüm şehrin turuncuya boyandığı dev bir partidir.
- **Yaz (Temmuz-Ağustos):** Tekneler kanallarla dolar, parklarda piknik yapan yerlilerle sosyalleşmek için en iyi zamandır.
- **İpucu:** Kış ayları çok rüzgarlı ve yağmurlu olabilir; ancak kanallar donarsa üzerinde buz pateni yapmak unutulmaz bir deneyimdir.

## 🏘️ Konaklama Rehberi
- **Jordaan:** Şehrin en karakteristik ve romantik mahallesi. Dar sokaklar, çiçekli pencereler ve butik kafeler.
- **De Pijp:** Bohem ve kozmopolit. Ünlü *Albert Cuyp* pazarı burada yer alır. Gece hayatı ve gurme duraklar için bir numara.
- **Oud-West:** Daha lokal ve sakin bir hava isteyenler için. *Foodhallen* (eski bir tramvay deposu) burada mutlaka görülmeli.

## 🍽️ Ne Yenir ve İçilir?
- **Bitterballen:** Pub'larda biranın yanında gelen meşhur kızarmış et topları. Sıcaklığına dikkat edin!
- **Stroopwafel:** İki ince gofret arası karamel. Taze yapılmış sıcak bir stroopwafel hayatınızı değiştirebilir.
- **Bisiklet Yoluna Dikkat:** Asla bisiklet yolları üzerinde durmayın veya yürümeyin. Amsterdamlılar bisiklet sürerken çok ciddidir ve çarpabilirler!
- **Yemek Saatleri:** Akşam yemeği genellikle erkendir (18:00 - 19:30). Restoran mutfakları geç saatlerde kapanabilir.

## 🚇 Ulaşım İpuçları
- **Yürüyüş ve Tramvay:** Şehri yürüyerek veya meşhur mavi-beyaz tramvaylarla keşfetmek en kolay yoldur.
- **Ücretsiz Feribotlar:** Merkez istasyonun arkasından kalkan feribotlarla Amsterdam'ın "Kuzey" (Noord) kısmına ücretsiz geçebilir ve daha modern bir yüzle karşılaşabilirsiniz.
- **Bisiklet Kiralama:** Eğer kendinize güveniyorsanız kiralayın, ancak trafiğin hızına ayak uydurmak ilk başta zorlayıcı olabilir.

## 💎 Lokal Sırlar & İpuçları
- [Gizli Avlu (Begijnhof)](search:Begijnhof): Kalabalık alışveriş caddesinin ortasındaki gizli bir kapıdan girilen bu 14. yüzyıl avlusu, şehrin en sessiz ve huzurlu noktasıdır.
- [NDSM Wharf](search:NDSM Wharf): Eski bir tersane bölgesidir; feribotla geçilen bu alan sokak sanatı, sanatçılar ve endüstriyel kafelerle doludur.
- **Saygı:** Red Light District'te fotoğraf çekmek yasaktır ve büyük bir saygısızlıktır. Lütfen kurallara uyun.''';

  static const _amsterdamEN = '''# Amsterdam Guide: Canals, Bikes & Freedom 🇳🇱

Amsterdam is more than just canals; it's a living work of art where creativity and tolerance are felt at every corner.

## 📅 Best Time to Visit
- **Tulip Season (April):** The city and nearby *Keukenhof* gardens turn into a riot of color. King's Day (April 27) is a giant party where the whole city turns orange.
- **Summer (July-August):** Boats fill the canals, and it's the best time to socialize with locals picnicking in the parks.
- **Tip:** Winter months can be very windy and rainy; but if the canals freeze, ice skating on them is an unforgettable experience.

## 🏘️ Neighborhood Guide
- **Jordaan:** The city's most characteristic and romantic area. Think narrow streets, flowery windows, and boutique cafes.
- **De Pijp:** Bohemian and cosmopolitan. The famous *Albert Cuyp* market is located here. Number one for nightlife and gourmet stops.
- **Oud-West:** For those who want a more local and quiet vibe. *Foodhallen* (an old tram depot) is a must-see here.

## 🍽️ Food & Dining Etiquette
- **Bitterballen:** The famous fried meat balls served alongside beer in pubs. Be careful, the inside is lava hot!
- **Stroopwafel:** Caramel between two thin waffles. A freshly made hot stroopwafel can change your life.
- **Watch the Bike Lanes:** Never stand or walk on the bike paths. Amsterdammers are serious about cycling and will ring their bells (or worse) if you're in the way!
- **Meal Times:** Dinner is usually early (6:00 PM - 7:30 PM). Restaurant kitchens may close surprisingly early on weekdays.

## 🚇 Transportation Tips
- **Walking & Trams:** Exploring the city by foot or on the famous blue-and-white trams is the easiest way.
- **Free Ferries:** Take the ferries from behind the Central Station to the "North" (Noord) part of Amsterdam for free. It shows a more modern and edgy face of the city.
- **Bike Rental:** Rent one if you feel confident, but keeping up with the speed and rules of the local traffic can be challenging at first.

## 💎 Local Secrets & Insights
- [Hidden Courtyard (Begijnhof)](search:Begijnhof): Entered through a discrete door in the middle of the busy shopping street, this 14th-century courtyard is the quietest spot in town.
- [NDSM Wharf](search:NDSM Wharf): An old shipyard area accessible by ferry; this space is filled with street art, artist studios, and industrial-style cafes.
- **Respect:** Taking photos in the Red Light District is forbidden and disrespectful. Please follow the local rules.''';

  // TOKYO
  static const _tokyoTR = '''# Tokyo Rehberi: Geleceğe Yolculuk 🇯🇵

Tokyo sadece bir şehir değil, farklı evrenlerin bir araya geldiği devasa bir ekosistemdir. Neon ışıklı gökdelenlerin arasında 400 yıllık tapınakları bulacağınız, her köşesinde sizi şaşırtacak bir detay saklayan bir rüya.

## 📅 Ne Zaman Gidilir?
- **Kiraz Çiçeği Mevsimi (Mart Sonu-Nisan):** Şehri pembe bir bulut kaplar. *Hanami* (çiçek izleme) ritüeli için en büyüleyici zaman.
- **Sonbahar (Kasım):** Akçaağaç yapraklarının kırmızısı şehri doğal bir tabloya dönüştürür.
- **İpucu:** Yaz ayları (Temmuz-Ağustos) aşırı nemli ve sıcak olabilir, gezmeyi zorlaştırabilir.

## 🏘️ Konaklama Rehberi
- **Shinjuku:** Şehrin kalbi. Gece hayatı, neonlar ve dev istasyonun etrafındaki hareketlilik.
- **Shibuya:** Modanın ve gençlik enerjisinin merkezi. Meşhur yaya geçidi ve alışveriş için ideal.
- **Shimokitazawa:** "Tokyo'nun Brooklyn'i". Vintage dükkanlar, plakçılar ve bohem kafeler.

## 🍽️ Ne Yenir ve İçilir?
- **Ramen Kültürü:** Ramen içerken hüpürdetmek ayıp değil, bir iltifattır! Yemeği ne kadar sevdiğinizi gösterir.
- **Sushi Görgüsü:** Tsukiji veya Toyosu pazarı çevresindeki yerlerde sushi yiyin. Wasabi genellikle sushinin içinde gelir, ekstra eklemeden önce tadına bakın.
- **Bahşiş Yok:** Japonya'da bahşiş bırakmak kaba bir davranış sayılabilir. En iyi hizmeti zaten fiyata dahil alırsınız.
- **Sessizlik:** Toplu taşımada telefonda konuşmak yasaktır. Şehir ne kadar kalabalık olursa olsun, sessizliğe saygı esastır.

## 🚇 Ulaşım İpuçları
- **Suica veya Pasmo:** Bu kartlar sadece ulaşım için değil, otomatlardan ve marketlerden alışveriş yapmak için de kullanılır. Telefonunuza da ekleyebilirsiniz.
- **JR Yamanote Hattı:** Şehrin tüm ana noktalarını dairesel bir hatla birbirine bağlar. Turistlerin can simididir.
- **Yürüyüş:** Tokyo devasadır ama her mahalle kendi içinde yürünerek keşfedilecek binlerce detay sunar.

## 💎 Lokal Sırlar & İpuçları
- [Golden Gai](search:Golden Gai): Shinjuku'da sadece 5-6 kişinin sığabildiği minicik barların olduğu labirent sokaklar. Gerçek Tokyo ruhu burada.
- [Nakano Broadway](search:Nakano Broadway): Akihabara çok popülerdir ama gerçek koleksiyonerler ve anime aşıkları Nakano'yu tercih eder.
- **Görgü Kuralları:** Yürürken yemek yemek hoş karşılanmaz. Aldığınız şeyi aldığınız yerin önünde veya oturarak yiyin.''';

  static const _tokyoEN = '''# Tokyo Guide: Journey to the Future 🇯🇵

Tokyo isn't just a city; it's a massive ecosystem where different universes collide. It's a dream where you'll find 400-year-old temples tucked between neon-lit skyscrapers.

## 📅 Best Time to Visit
- **Cherry Blossom Season (Late March-April):** The city is covered in a pink cloud of blossoms. The most magical time for the *Hanami* (flower viewing) ritual.
- **Autumn (November):** The fiery red of the maple leaves turns the city into a natural masterpiece.
- **Tip:** Summer months (July-August) can be extremely humid and hot, making long walks quite draining.

## 🏘️ Neighborhood Guide
- **Shinjuku:** The heart of the city. Nightlife, neon lights, and the non-stop energy surrounding the world's busiest station.
- **Shibuya:** The center of fashion and youth energy. Perfect for the famous scramble crossing and endless shopping.
- **Shimokitazawa:** "The Brooklyn of Tokyo." Think vintage shops, record stores, and bohemian cafes.

## 🍜 Food & Dining Etiquette
- **Ramen Culture:** Slurping your noodles is not rude; it's a compliment! It shows how much you are enjoying the dish.
- **Sushi Manners:** Try sushi near the Tsukiji or Toyosu markets. Wasabi is already inside the sushi; taste it before adding more.
- **No Tipping:** Tipping in Japan is not customary and can even be considered rude. You get the best service included in the price.
- **Silence:** Speaking on the phone in public transport is prohibited. No matter how crowded, respect for collective silence is key.

## 🚇 Transportation Tips
- **Suica or Pasmo:** These cards aren't just for transport; you can use them at vending machines and convenience stores. You can also add them to your smartphone.
- **JR Yamanote Line:** A circular line connecting all the major hubs of the city. A lifesaver for tourists.
- **Walking:** Tokyo is massive, but each neighborhood offers thousands of details that are best discovered by wandering on foot.

## 💎 Local Secrets & Insights
- [Golden Gai](search:Golden Gai): A maze of tiny alleys in Shinjuku with bars that fit only 5 or 6 people. This is the real soul of Tokyo.
- [Nakano Broadway](search:Nakano Broadway): While Akihabara is famous, true collectors and anime lovers prefer the hidden treasures of Nakano.
- **Etiquette:** Eating while walking is generally looked down upon. Eat what you buy in front of the shop or find a place to sit.''';

  // NEW YORK
  static const _newyorkTR = '''# New York Rehberi: Hiç Uyumayan Şehir 🇺🇸

New York; bitmek bilmeyen enerjisi, gökyüzüne uzanan binaları ve her köşesinde duyulan siren sesleriyle bir film setini andırır. Burası sadece bir şehir değil, bir hırs ve hayaller meydanıdır.

## 📅 Ne Zaman Gidilir?
- **Bahar ve Güz:** Mayıs-Haziran veya Eylül-Ekim dönemleri havanın en dengeli olduğu zamanlardır. Central Park'ta yürümek için idealdir.
- **Aralık:** Noel ağaçları, buz pateni pistleri ve 5. Cadde vitrinleri ile New York kışın bambaşka bir büyüye bürünür.
- **İpucu:** Yazın New York çok sıcak ve bazen metroda bunaltıcı olabilir, kışın ise dondurucu rüzgarlara hazırlıklı olun.

## 🏘️ Konaklama Rehberi
- **West Village:** Şehrin en karakteristik, alçak binalı ve ağaçlı yolları. Meşhur kafeler ve "Friends" apartmanı burada.
- **Williamsburg (Brooklyn):** Hipster kültürünün başkenti. Harika Manhattan manzarası, butikler ve yerel bir hava.
- **Upper West Side:** Daha sakin, aile dostu ve Central Park'a çok yakın. Gerçek New Yorklu gibi hissetmek için birebir.

## 🍽️ Ne Yenir ve İçilir?
- **Pizza Slice:** 1-2 dolarlık dilim pizzalar New York'un yakıtıdır. Joe's Pizza gibi klasikleri deneyin.
- **Bagel Kahvaltısı:** Gerçek bir New Yorklu gibi "cream cheese" ve "lox" (somon füme) ile dolu bir bagel yiyin.
- **Bahşiş Kuralı:** Amerika'da bahşiş isteğe bağlı değildir. Restoranlarda en az %18-%22 arası bahşiş bırakmak standarttır.
- **Yürüyüş Temposu:** Kaldırımlarda hızlı yürüyün ve aniden durmayın. New Yorkluların acelesi vardır!

## 🚇 Ulaşım İpuçları
- **OMNY:** Metro kartıyla uğraşmanıza gerek yok. Kredi kartınızı veya telefonunuzu turnikeye okutarak (tap) kolayca geçebilirsiniz.
- **Subway:** 7/24 çalışır ama biraz karmaşık ve kirli olabilir. "Express" ve "Local" tren ayrımına dikkat edin.
- **Ayağınıza Güvenin:** New York çok yürünecek bir yer. Rahat bir ayakkabı hayat kurtarır.

## 💎 Lokal Sırlar & İpuçları
- [High Line](search:High Line): Eski bir tren hattından park haline getirilen bu yolda gün batımında yürüyün. Şehre çok farklı bir perspektiften bakarsınız.
- [Roosevelt Island Tramway](search:Roosevelt Island Tramway): Sadece bir metro biletine Manhattan manzarasını teleferikle havadan izleyebilirsiniz.
- [Chelsea Market](search:Chelsea Market): Bir öğle yemeğinizi buradaki farklı dünya lezzetlerine ayırın.''';

  static const _newyorkEN = '''# New York Guide: The City That Never Sleeps 🇺🇸

New York feels like a permanent movie set with its endless energy, sky-scraping buildings, and the persistent sound of sirens. It’s more than a city; it’s an arena of ambition and dreams.

## 📅 Best Time to Visit
- **Spring and Autumn:** May-June or September-October are when the weather is most balanced. Ideal for exploring Central Park.
- **December:** With Christmas trees, ice skating rinks, and the window displays of 5th Avenue, New York takes on a different kind of magic in winter.
- **Tip:** NYC can be stiflingly hot in the summer and the subways can feel humid; in winter, be prepared for freezing winds.

## 🏘️ Neighborhood Guide
- **West Village:** The most characteristic area with low-rise buildings and tree-lined streets. Famous cafes and the "Friends" apartment are here.
- **Williamsburg (Brooklyn):** The capital of hipster culture. Offers great Manhattan views, boutiques, and a local vibe.
- **Upper West Side:** Quieter, family-friendly, and right next to Central Park. Perfect to feel like a true New Yorker.

## 🍕 Food & Dining Etiquette
- **The Pizza Slice:** 1-2 dollar slices are the fuel of New York. Try the classics like Joe's Pizza.
- **Bagel Breakfast:** Eat like a local with an "everything bagel" with cream cheese and lox (smoked salmon).
- **Tipping Rule:** In the US, tipping is not optional. Leaving at least 18%-22% at restaurants is the standard expectation.
- **Pavement Etiquette:** Walk fast and don't stop suddenly on the sidewalks. New Yorkers are always in a rush!

## 🚇 Transportation Tips
- **OMNY:** No need for a physical MetroCard. Just tap your credit card or phone at the turnstiles for easy access.
- **The Subway:** It runs 24/7 but can be gritty and confusing. Pay close attention to the difference between "Express" and "Local" trains.
- **Trust Your Feet:** New York is a city meant for walking. A comfortable pair of sneakers is an absolute lifesaver.

## 💎 Local Secrets & Insights
- [The High Line](search:High Line): Walk this elevated park built on a historic freight rail line at sunset. It offers a unique perspective of the city's architecture.
- [Roosevelt Island Tramway](search:Roosevelt Island Tramway): Use a standard metro fare to get an aerial view of the Manhattan skyline from a cable car.
- [Chelsea Market](search:Chelsea Market): Dedicate a lunch to exploring the diverse global flavors inside this historic food hall.''';

  // BANGKOK
  static const _bangkokTR = '''# Bangkok Rehberi: Kaotik ve Büyüleyici 🇹🇭

Bangkok; altın varaklı tapınakların, tüten sokak yemeği tezgahlarının ve lüks gökdelenlerin birbirine geçtiği bir duyu patlamasıdır. Kaosu sevmeyi öğreneceğiniz bir şehir.

## 📅 Ne Zaman Gidilir?
- **Serin Mevsim (Kasım-Şubat):** Havanın en az nemli ve gezilebilir olduğu zaman. Akşamları hafif bir serinlik olabilir.
- **Songkran (Nisan):** Tayland Yeni Yılı. Tüm şehrin dev bir su savaşına döndüğü, eğlencenin dorukta olduğu zaman.
- **İpucu:** Yağmur sezonu (Mayıs-Ekim) ani ve şiddetli yağışlar getirir ancak oteller çok daha ucuzdur.

## 🏘️ Konaklama Rehberi
- **Sukhumvit:** Modern Bangkok. En iyi oteller, alışveriş merkezleri ve gece hayatı burada yoğunlaşır.
- **Ari:** Şehrin yükselen yıldızı. Daha sakin, hipster kafeler ve yerel bir atmosfer isteyenler için.
- **Old City (Rattanakosin):** Tapınaklara ve büyük saraya yürüyerek ulaşmak isteyen tarih tutkunları için ideal.

## 🍽️ Ne Yenir ve İçilir?
- **Sokak Yemekleri:** Dünyanın en iyi sokak yemeği sahnesi. Pad Thai, Mango Sticky Rice ve Som Tum (papaya salatası) mutlaka denenmeli.
- **Tapınak Saygısı:** Tapınaklara girerken omuzlar ve dizler kapalı olmalıdır. Ayakkabılarınızı kapıda bırakmayı unutmayın.
- **Kraliyet Saygısı:** Tayland halkı için Kraliyet ailesi kutsaldır. Onlar hakkında olumsuz konuşmak yasaktır ve büyük saygısızlık kabul edilir.
- **Pazarlık:** Gece pazarlarında ve tuk-tuklarda nazikçe pazarlık yapmak normaldir, ancak AVM'lerde ve marketlerde sabit fiyat geçerlidir.

## 🚇 Ulaşım İpuçları
- **BTS ve MRT:** Gök treni ve Metro. Trafikten kaçmanın en hızlı ve klimalı yolu.
- **Nehir Tekneleri:** Chao Phraya nehrinde ulaşım hem ucuz hem de manzaralıdır.
- **Tuk-tuk Deneyimi:** Turistik bir klişe olsa da en az bir kere deneyin. Binmeden önce mutlaka fiyat üzerinde anlaşın.

## 💎 Lokal Sırlar & İpuçları
- [Khlong Lat Mayom](search:Khlong Lat Mayom): Turistik yüzen pazarlar yerine yerlilerin gittiği bu pazarı tercih edin. Gerçek yemek deneyimi burada.
- [Chatuchak Hafta Sonu Pazarı](search:Chatuchak Market): Devasa bir labirent. Aradığınız her şeyi (evet, her şeyi) burada bulabilirsiniz.
- **Çatı Barları:** Sahra otellerin çatı barları yerine daha az bilinen terasları keşfedin; manzara aynı, fiyatlar daha makul.''';

  static const _bangkokEN = '''# Bangkok Guide: Chaotic & Mesmerizing 🇹🇭

Bangkok is a sensory explosion where gold-leafed temples, steaming street food stalls, and luxury skyscrapers intertwine. It’s a city where you’ll learn to love the chaos.

## 📅 Best Time to Visit
- **Cool Season (November-February):** When humidity is at its lowest and the weather is manageable. Evenings can be slightly cool.
- **Songkran (April):** The Thai New Year. A time when the entire city turns into a giant water fight—pure, unadulterated fun.
- **Tip:** The rainy season (May-October) brings sudden, heavy downpours but this is when hotels are at their cheapest.

## 🏘️ Neighborhood Guide
- **Sukhumvit:** Modern Bangkok. Home to the best hotels, malls, and the heart of the city's nightlife.
- **Ari:** The rising star. Ideal for those seeking a quieter, hipster vibe with local cafes and a relaxed atmosphere.
- **Old City (Rattanakosin):** Perfect for history buffs who want to be within walking distance of the temples and the Grand Palace.

## 🍜 Food & Dining Etiquette
- **Street Food is King:** Bangkok has one of the world's best street food scenes. Pad Thai, Mango Sticky Rice, and Som Tum (papaya salad) are non-negotiable.
- **Temple Respect:** When entering temples, shoulders and knees must be covered. Don’t forget to remove your shoes at the entrance.
- **Royal Respect:** The Royal Family is highly revered in Thailand. Harmless jokes or criticism are not tolerated and can lead to legal issues.
- **Bargaining:** It’s normal to politely bargain at night markets and with tuk-tuk drivers, but malls and convenience stores use fixed prices.

## 🚇 Transportation Tips
- **BTS & MRT:** The Skytrain and Underground Metro. The fastest and most air-conditioned way to bypass the legendary Bangkok traffic.
- **River Boats:** Commuting on the Chao Phraya river is cheap, scenic, and surprisingly efficient.
- **Tuk-tuk Experience:** A total tourist cliché, but you must try it at least once. Always agree on the price before you hop in.

## 💎 Local Secrets & Insights
- [Khlong Lat Mayom](search:Khlong Lat Mayom): Skip the overly touristy floating markets for this local favorite. The food here is authentic and much cheaper.
- [Chatuchak Weekend Market](search:Chatuchak Market): A massive labyrinth. You can find everything (literally everything) here. Wear comfortable shoes.
- **Rooftop Bars:** Instead of the mega-famous ones, look for smaller boutique rooftops for similar views without the dress codes and high prices.''';

  // SINGAPUR
  static const _singapurTR = '''# Singapur Rehberi: Geleceğin Bahçe Şehri 🇸🇬

Singapur; kusursuz düzeni, devasa yapay ağaçları ve çok kültürlü mutfağıyla 21. yüzyılın en modern şehir devletidir. Doğanın ve teknolojinin mükemmel uyumu.

## 📅 Ne Zaman Gidilir?
- **Şubat-Nisan:** Yağışın en az olduğu dönem. Dışarıdaki aktiviteler için en uygun zaman.
- **F1 Sezonu (Eylül):** Gece yarışı heyecanı tüm şehri sarar; sokaklar konserler ve etkinliklerle dolar.
- **İpucu:** Singapur her zaman nemlidir. Gün içinde aniden bir yağmur başlayıp 15 dakika sonra güneş çıkabilir.

## 🏘️ Konaklama Rehberi
- **Marina Bay:** Şehrin ikonik silüeti. Lüks oteller ve görsel bir şölen isteyenler için.
- **Tiong Bahru:** Art Deco binalar, niş kitapçılar ve en iyi fırınlar. Daha karakteristik bir bölge.
- **Kampong Glam:** Müslüman mahallesi; renkli sokaklar, Arap mimarisi ve çok havalı kafeler.

## 🍽️ Ne Yenir ve İçilir?
- **Hawker Centers:** Michelin yıldızlı tavuklu pilavdan (Hainanese Chicken Rice) en lezzetli Laksa'ya kadar her şeyi burada ucuza yiyebilirsiniz.
- **"Chope" Kültürü:** Masanızda sahipsiz bir paket kağıt mendil görürseniz dokunmayın; birisi orayı rezerve etmiş demektir!
- **Temizlik ve Yasaklar:** Sakız çiğnemek, yere çöp atmak ve kapalı alanlarda sigara içmek ciddi cezalara tabidir. Kurallara uymak burada bir yaşam tarzıdır.
- **Bahşiş:** Genellikle fiyata %10 servis ücreti eklenir, ekstra bahşiş beklentisi yoktur.

## 🚇 Ulaşım İpuçları
- **MRT:** Dünyanın en temiz ve düzenli metrosu. Her yere ulaşır.
- **EZ-Link:** Bu kartla hem tüm toplu taşımayı kullanabilir hem de bazı marketlerde ödeme yapabilirsiniz.
- **Yürüyüş:** Şehir inanılmaz yeşildir ama yoğun nem nedeniyle uzun yürüyüşler yorucu olabilir; AVM'lerin klimaları arasında geçiş yapın!

## 💎 Lokal Sırlar & İpuçları
- [Henderson Waves](search:Henderson Waves): Gün batımında bu dalga şeklindeki köprüde yürüyün. Şehir manzarası ve doğa bir arada.
- [Haji Lane](search:Haji Lane): Gece modası ve canlı müzik için bu dar ve renkli sokağa uğrayın.
- [Havalimanı (Jewel Changi)](search:Jewel Changi): Sırf o dev şelaleyi görmek için bile havalimanına birkaç saat erken gidin.''';

  static const _singapurEN = '''# Singapore Guide: The Garden City of the Future 🇸🇬

Singapore is the most modern city-state of the 21st century, with its perfect order, massive artificial trees, and multicultural cuisine. A perfect harmony of nature and technology.

## 📅 Best Time to Visit
- **February-April:** The period with the least rainfall. The most suitable time for outdoor activities.
- **F1 Season (September):** The excitement of the night race takes over the city; streets are filled with concerts and events.
- **Tip:** Singapore is always humid. An sudden rain can start during the day and the sun can come out 15 minutes later.

## 🏘️ Neighborhood Guide
- **Marina Bay:** The iconic silhouette of the city. For those who want luxury hotels and a visual feast.
- **Tiong Bahru:** Art Deco buildings, niche bookstores, and the best bakeries. A more characteristic area.
- **Kampong Glam:** The Malay district; colorful streets, Arab architecture, and very cool cafes.

## 🍽️ Food & Dining Etiquette
- **Hawker Centers:** You can eat everything from Michelin-starred chicken rice (Hainanese Chicken Rice) to the tastiest Laksa cheaply here.
- **"Chope" Culture:** If you see an unattended pack of tissues on a table, don't touch it; it means someone has reserved that spot!
- **Cleanliness and Prohibitions:** Chewing gum, littering, and smoking in closed areas are subject to serious fines. Following the rules is a way of life here.
- **Tipping:** Usually, a 10% service charge is added to the price, there is no expectation of extra tipping.

## 🚇 Transportation Tips
- **MRT:** The cleanest and most organized metro in the world. It reaches everywhere.
- **EZ-Link:** With this card, you can use all public transport and pay at some convenience stores.
- **Walking:** The city is incredibly green, but long walks can be tiring due to the intense humidity; switch between the air-conditioners of the malls!

## 💎 Local Secrets & Insights
- [Henderson Waves](search:Henderson Waves): Walk on this wave-shaped bridge at sunset. City views and nature combined.
- [Haji Lane](search:Haji Lane): Swing by this narrow and colorful street for nightlife fashion and live music.
- [The Airport (Jewel Changi)](search:Jewel Changi): Go to the airport a few hours early just to see that massive indoor waterfall.''';

  // SEUL
  static const _seulTR = '''# Seul Rehberi: Gelenek ve K-Pop Arasında 🇰🇷

Seul; 500 yıllık sarayların devasa dijital ekranlarla yan yana durduğu, günün 24 saati uyanık ve dinamik bir şehirdir. Geleceği bugün yaşayan bir başkent.

## 📅 Ne Zaman Gidilir?
- **Bahar (Nisan):** Kiraz çiçeklerinin açtığı ve festivallerin başladığı en güzel zaman.
- **Sonbahar (Ekim-Kasım):** Akçaağaçların şehri turuncuya boyadığı, havanın taze olduğu dönem.
- **İpucu:** Kış ayları (Aralık-Şubat) Sibirya soğuklarını aratmayacak kadar sert geçebilir, sıkı giyinin!

## 🏘️ Konaklama Rehberi
- **Hongdae:** Üniversite enerjisi, sokak performansları ve bağımsız moda. Genç ve eğlenceli.
- **Bukchon Hanok Village:** Geleneksel Kore evleri arasında konaklamak isteyenler için tarihi bir deneyim.
- **Seongsu-dong:** "Seul'ün Brooklyn'i". Eski fabrikaların sanatsal kafelere ve butiklere dönüştüğü en trend semt.

## 🍽️ Ne Yenir ve İçilir?
- **Korean BBQ:** Yemek burada sosyal bir olaydır. Masadaki ızgarada etinizi kendiniz pişirin ve sayısız "Banchan" (küçük yan yemekler) ile tadını çıkarın.
- **İçecek Saygısı:** Birisi size içecek ikram ederken bardağınızı iki elinizle tutun. Bu, büyük bir saygı göstergesidir.
- **Sokak Lezzetleri:** Myeongdong sokağı bir açık hava büfesi gibidir. Tteokbokki ve Kore usulü kızarmış tavuğu denemeden dönmeyin.
- **Bahşiş Yok:** Güney Kore'de bahşiş beklentisi yoktur; nezaket ve "teşekkür ederim" demek yeterlidir.

## 🚇 Ulaşım İpuçları
- **T-Money:** Tüm ulaşım araçlarında ve marketlerde geçen hayat kurtarıcı kart.
- **Subway:** Çok geniş ve dakik bir ağ. İngilizce tabelalar sayesinde kaybolmak zordur.
- **Naver Maps / Kakao Maps:** Google Maps Kore'de çok iyi çalışmayabilir; bu yerel uygulamalar hayat kurtarır.

## 💎 Lokal Sırlar & İpuçları
- [Han Nehrinde Ramen](search:Han River Park): Yerliler gibi yapın; nehir kenarındaki marketlerden otomatik makinede pişen hazır ramenlerden alın ve piknik yapın.
- [Gece Pazarları](search:Dongdaemun Market): Dongdaemun pazarı sabaha karşı saat 4'e kadar canlıdır. Alışverişun saati yoktur!
- **Sessiz Vagonlar:** Metroda sessizliğe dikkat edin; yüksek sesle konuşmak hoş karşılanmaz.''';

  static const _seulEN = '''# Seoul Guide: Between Tradition & K-Pop 🇰🇷

Seoul is a dynamic city where 500-year-old palaces stand alongside massive digital screens, staying awake and active 24 hours a day. A capital living in the future today.

## 📅 Best Time to Visit
- **Spring (April):** The most beautiful time when cherry blossoms bloom and festivals begin.
- **Autumn (October-November):** When maple trees paint the city orange and the air is fresh and crisp.
- **Tip:** Winter months (December-February) can be as harsh as Siberian cold; make sure to pack heavy layers!

## 🏘️ Neighborhood Guide
- **Hongdae:** University energy, street performances, and indie fashion. Young and incredibly fun.
- **Bukchon Hanok Village:** A historical experience for those who want to stay among traditional Korean houses.
- **Seongsu-dong:** "The Brooklyn of Seoul." The trendiest neighborhood where old factories have been turned into artistic cafes and boutiques.

## 🍜 Food & Dining Etiquette
- **Korean BBQ:** Dining here is a social event. Grill your meat at the table and enjoy it with countless "Banchan" (small side dishes).
- **Drinking Respect:** When someone offers you a drink, hold your glass with both hands. This is a sign of immense respect.
- **Street Food:** Myeongdong street is like an open-air buffet. Don't leave without trying Tteokbokki and Korean Fried Chicken.
- **No Tipping:** There is no expectation of tipping in South Korea; politeness and a "Kamsahamnida" (Thank you) are enough.

## 🚇 Transportation Tips
- **T-Money:** A lifesaver card that works in all transport vehicles and convenience stores.
- **Subway:** A very extensive and punctual network. It's hard to get lost thanks to the English signs.
- **Naver Maps / Kakao Maps:** Google Maps might not work well in Korea; these local apps are essential for navigation.

## 💎 Local Secrets & Insights
- [Han River Ramen](search:Han River Park): Do as the locals do; buy instant ramen from a convenience store by the river, cook it in the automatic machines, and have a picnic.
- [Night Markets](search:Dongdaemun Market): Dongdaemun market is alive until 4 AM. There's no time limit for shopping in this city!
- **Quiet Carriages:** Pay attention to the volume of your voice in the subway; loud conversations are frowned upon.''';



  // LIZBON
  static const _lizbonTR = '''# Lizbon Rehberi: Yedi Tepeli Işığın Şehri 🇵🇹

Lizbon; sarı tramvayları, melankolik Fado müziği ve Atlas Okyanusu'ndan gelen taze esintisiyle Avrupa'nın en karakteristik başkentlerinden biridir. Tarih ve modernliğin altın sarısı bir ışık altında buluştuğu yer.

## 📅 Ne Zaman Gidilir?
- **Festivaller Ayı (Haziran):** Şehir hayatının en renkli olduğu zaman. *Santo António* festivalleriyle sokaklar ızgara sardalya kokusu ve müzikle dolar.
- **Bahar ve Güz:** Mayıs ve Eylül-Ekim ayları havanın en güzel, ışığın en yumuşak olduğu dönemlerdir.
- **İpucu:** Yazın çok kalabalık olabilir ama Okyanus etkisi sayesinde hava hiçbir zaman Madrid kadar boğucu olmaz.

## 🏘️ Konaklama Rehberi
- **Alfama:** Şehrin en eski, labirent sokaklı mahallesi. Fado sesleri arasında uyanmak isteyenler için büyüleyici.
- **Principe Real:** En trend mahalle. Şık butikler, tasarım otelleri ve harika manzaralı parklar.
- **Baixa:** Şehrin düz ayak merkezi. Ulaşım kolaylığı ve her yere yakınlık isteyenler için ideal.

## 🍽️ Ne Yenir ve İçilir?
- **Pastel de Nata:** Bu efsanevi kremalı tartı yerinde, Belem'de yiyin. Üzerine tarçın ve pudra şekeri serpmeyi unutmayın.
- **Bacalhau:** Portekizliler morina balığını (Bacalhau) pişirmenin 1000 yolu olduğunu söyler. Her birini denemeye değer!
- **Ginja:** Küçük bir çikolata kadehte servis edilen vişne likörü. Gün arası harika bir enerji kaynağıdır.
- **Yemek Saatleri:** İspanya kadar geç olmasa da akşam yemeği genellikle 20:00'den sonra yenir.

## 🚇 Ulaşım İpuçları
- **Tramvay 28:** Şehrin sembolüdür ama turistler nedeniyle çok kalabalıktır. Sabah çok erken binerseniz keyfini çıkarabilirsiniz.
- **Elevadores:** Şehir çok tepeli olduğu için tarihi asansörler ve fünikülerler (Gloria, Bica gibi) hayat kurtarır.
- **Yürüyüş:** Lizbon'un meşhur kalsada (kaldırım taşları) kaygandır; mutlaka iyi yol tutan bir ayakkabı giyin.

## 💎 Lokal Sırlar & İpuçları
- [Miradouros](search:Miradouro da Senhora do Monte): Şehrin her yerindeki teraslar (seyir noktaları). Gün batımında *Miradouro da Senhora do Monte* en geniş ve en güzel manzarayı sunar.
- [LX Factory](search:LX Factory): Eski bir fabrika alanının sanat galerileri, restoranlar ve meşhur kitapçılarla dolu bir yaşam alanına dönüşmüş hali.
- **Yankesicilik:** Tramvaylarda ve kalabalık meydanlarda eşyalarınıza dikkat edin; Lizbon genel olarak güvenli olsa da bu bir klasik sorundur.''';

  static const _lizbonEN = '''# Lisbon Guide: The City of Seven Hills and Golden Light 🇵🇹

Lisbon is one of Europe's most atmospheric capitals, with its iconic yellow trams, melancholic Fado music, and the fresh breeze from the Atlantic. It's where history meets modernity under a unique golden glow.

## 📅 Best Time to Visit
- **Month of Festivals (June):** The liveliest time in the city. Streets are filled with the scent of grilled sardines and music during the *Santo António* celebrations.
- **Spring and Autumn:** May and September-October offer the best weather and the softest, most photogenic light.
- **Tip:** While summer can be crowded, the Atlantic influence keeps it from being as stifling as Madrid.

## 🏘️ Neighborhood Guide
- **Alfama:** The oldest, most labyrinthine part of town. Enchanting for those who want to wake up to the sounds of Fado.
- **Principe Real:** The trendiest neighborhood. Home to chic boutiques, design hotels, and parks with stunning vistas.
- **Baixa:** The flat center of the city. Ideal for accessibility and being close to all major transport links.

## 🍽️ Food & Dining Etiquette
- **Pastel de Nata:** Eat this legendary custard tart at its source in Belem. Don't forget to sprinkle it with cinnamon and icing sugar.
- **Bacalhau:** The Portuguese say there are 1000 ways to cook salt cod (Bacalhau). Every single one is worth trying!
- **Ginja:** A cherry liqueur often served in a small chocolate cup. A perfect mid-day pick-me-up.
- **Meal Times:** While not as late as Spain, dinner is typically served after 8:00 PM.

## 🚇 Transportation Tips
- **Tram 28:** An icon of the city, but often packed with tourists. Ride it very early in the morning to truly enjoy the experience.
- **Elevadores:** Since the city is built on hills, historic elevators and funiculars (like Gloria and Bica) are lifesavers.
- **Walking:** Lisbon's famous cobblestones (calcada) are slippery; always wear shoes with good grip.

## 💎 Local Secrets & Insights
- [Miradouros](search:Miradouro da Senhora do Monte): These are the viewpoints scattered across the city. *Miradouro da Senhora do Monte* offers the widest and arguably most beautiful sunset view.
- [LX Factory](search:LX Factory): An old industrial site transformed into a hub of art galleries, restaurants, and one of the world's coolest bookstores.
- **Pickpockets:** Be vigilant with your belongings on the trams and in crowded squares; it's a common issue in an otherwise very safe city.''';

  // PORTO
  static const _portoTR = '''# Porto Rehberi: Nehir ve Granitin Büyüsü 🇵🇹

Porto; Douro Nehri kıyısına dizilmiş rengarenk evleri, heybetli köprüleri ve dünyaca ünlü şaraplarıyla Lizbon'un o meşhur melankolisini daha samimi bir havada sunar.

## 📅 Ne Zaman Gidilir?
- **São João Festivali (23 Haziran):** Şehrin en büyük gecesi. Herkes sokağa dökülür, havai fişekler atılır ve geleneksel olarak birbirlerinin kafasına plastik çekiçlerle vururlar!
- **Yaz Sonu (Eylül):** Douro Vadisi'nde bağ bozumu zamanıdır. Şehir cıvıl cıvıl ve hava mükemmeldir.

## 🏘️ Konaklama Rehberi
- **Ribeira:** Nehir kıyısı. Turistik ama manzarası paha biçilemez.
- **Cedofeita:** Porto'nun sanat mahallesi. Yerel galeriler, butikler ve modern kafeler için en iyi yer.
- **Vila Nova de Gaia:** Teknik olarak karşı kıyı ama şarap mahzenlerine en yakın ve Porto manzarasını en iyi gören bölge.

## 🍽️ Ne Yenir ve İçilir?
- **Francesinha:** Porto'nun efsanevi sandviçi. İçinde farklı etler, üzerinde erimiş peynir ve özel bir sosla servis edilir. Oldukça doyurucudur!
- **Porto Şarabı:** Gaia tarafındaki mahzenlerde tadım yapmadan dönmeyin.
- **Yemek Görgüsü:** Porsiyonlar Portekiz'de genellikle büyüktür, sipariş vermeden önce porsiyonun büyüklüğünü kontrol edin.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Porto tepelidir ama yürüyerek gezmeye çok uygundur. Dom Luis I köprüsünden yürüyerek geçmek bir klasiktir.
- **Metro:** Havaalanından şehre ulaşım için en pratik yoldur.

## 💎 Lokal Sırlar & İpuçları
- [Jardim do Morro](search:Jardim do Morro): Karşı kıyıda (Gaia), gün batımında yerlilerin toplanıp müzik yaptığı ve Porto manzarasını izlediği en popüler nokta.
- [Sao Bento İstasyonu](search:Sao Bento Station): Dünyanın en güzel tren istasyonlarından biri. İçerideki "azulejo" (mavi-beyaz seramik) panolarını incelemek için mutlaka uğrayın.''';

  static const _portoEN = '''# Porto Guide: Magic of River and Granite 🇵🇹

Porto offers a more intimate version of Portugal's famous melancholy, with its colorful houses lined along the Douro River, imposing bridges, and world-renowned port wine cells.

## 📅 Best Time to Visit
- **Festa de São João (June 23):** The city's biggest night. Everyone pours into the streets, fireworks go off, and people traditionally hit each other on the head with soft plastic hammers!
- **Late Summer (September):** Harvest time in the Douro Valley. The city is vibrant and the weather is perfect.

## 🏘️ Neighborhood Guide
- **Ribeira:** The riverbank. Touristy, but the views and atmosphere are priceless.
- **Cedofeita:** Porto's artsy district. The best place for local galleries, boutiques, and independent cafes.
- **Vila Nova de Gaia:** Technically the opposite bank, but it's where the port wine cellars are and offers the iconic view of the Porto skyline.

## 🍽️ Food & Dining Etiquette
- **Francesinha:** Porto's legendary sandwich. Layers of meat, covered in melted cheese, and served in a signature spice sauce. It's an absolute beast of a meal!
- **Port Wine:** Don't leave without doing a tasting at the cellars on the Gaia side.
- **Dining Portion:** Portions in Portugal are generally very generous; check the size before you order too much.

## 🚇 Transportation Tips
- **Walking:** Porto is hilly but very walkable. Walking across the Dom Luis I bridge is a quintessential Porto experience.
- **Metro:** The most practical way to get from the airport to the city center.

## 💎 Local Secrets & Insights
- [Jardim do Morro](search:Jardim do Morro): Located on the Gaia side, this is the most popular spot for locals to gather at sunset, play music, and watch the city light up.
- [Sao Bento Station](search:Sao Bento Station): One of the most beautiful train stations in the world. Stop by to admire the stunning "azulejo" (blue and white ceramic) panels.''';

  // MADRID
  static const _madridTR = '''# Madrid Rehberi: İspanya'nın Sosyal Ruhu 🇪🇸

Madrid; geniş caddeleri, görkemli müzeleri ve bitmek bilmeyen sosyal hayatıyla İspanya'nın atan kalbidir. Burası binaları görmekten ziyade, sokaktaki enerjiyi yaşama şehridir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Mayıs):** Hava mükemmeldir ve şehir *San Isidro* festivalleriyle canlanır.
- **Sonbahar (Ekim):** Yazın yakıcı sıcağı geçmiş, parklar altın rengine bürünmüştür.
- **İpucu:** Temmuz ve Ağustos aylarında Madrid aşırı sıcak olabilir; yerlilerin çoğu tatile gider.

## 🏘️ Konaklama Rehberi
- **Malasaña:** Madrid'in en "cool" mahallesi. Vintage dükkanlar, gece hayatı ve yaratıcı bir enerji.
- **La Latina:** Geleneksel Madrid. Tapas barları ve her Pazar kurulan *El Rastro* pazarı ile meşhur.
- **Salamanca:** Şık, lüks ve düzenli. Alışveriş tutkunlarının tercihi.

## 🍽️ Ne Yenir ve İçilir?
- **Tapiar (Tapas Turu):** Madrid'de akşam yemeği tek bir yerde yenmez. Bir bar-dan diğerine geçip her yerde bir içki ve bir meze (tapa) almak bir hayat tarzıdır.
- **Bocadillo de Calamares:** Kalamar sandviç. Madrid'in en meşhur sokak lezzetidir, özellikle Mayor Meydanı çevresinde deneyin.
- **Yemek Saatleri:** Madrid çok geç yaşar. Öğle yemeği 14:00, akşam yemeği ise 21:30'dan önce pek başlamaz.

## 🚇 Ulaşım İpuçları
- **Metro:** Avrupa'nın en iyi metro ağlarından biridir. Çok temiz, hızlı ve her yere ulaşır.
- **Yürüyüş:** Şehir merkezi geniştir ama yürüyerek keşfetmek çok keyiflidir.

## 💎 Lokal Sırlar & İpuçları
- [Templo de Debod](search:Templo de Debod): Mısır'dan getirilmiş gerçek bir tapınak. Gün batımında Madrid'in en büyülü manzarası buradadır.
- [Retiro Parkı](search:Retiro Park): Sadece bir park değil, Madrid'in akciğeridir. İçindeki [Palacio de Cristal](search:Palacio de Cristal)'i (Kristal Saray) mutlaka görün.
- [El Rastro](search:El Rastro): Pazar sabahı kalabalığına karışın ama eşyalarınıza dikkat edin.''';

  static const _madridEN = '''# Madrid Guide: The Social Soul of Spain 🇪🇸

Madrid is the beating heart of Spain, with its grand boulevards, majestic museums, and an irrepressible social life. It's a city less about looking at buildings and more about feeling the energy in the streets.

## 📅 Best Time to Visit
- **Spring (May):** The weather is perfect and the city comes alive with the *San Isidro* festivals.
- **Autumn (October):** The scorching summer heat has passed, and the parks are dressed in autumn colors.
- **Tip:** Avoid July and August if you can; it's intensely hot and many locals head to the coast for vacation.

## 🏘️ Neighborhood Guide
- **Malasaña:** The coolest neighborhood in Madrid. Think vintage shops, rock-and-roll nightlife, and a creative energy.
- **La Latina:** Traditional Madrid at its best. Famous for its tapas bars and the massive *El Rastro* market held every Sunday.
- **Salamanca:** Elegant, upscale, and pristine. The place for high-end shopping and refined dining.

## 🍽️ Food & Dining Etiquette
- **Tapiar (Tapas Crawl):** In Madrid, you don't typically just go to one restaurant for dinner. Moving from one bar to another, having a drink and a tapa at each, is a way of life.
- **Bocadillo de Calamares:** Squid sandwich. It's the most iconic street food in Madrid—try it in the plazas around Plaza Mayor.
- **Meal Times:** Madrid lives late. Lunch starts at 2 PM, and dinner rarely begins before 9:30 PM.

## 🚇 Transportation Tips
- **The Metro:** One of the best subway systems in Europe. It's clean, fast, and reaches every corner of the city.
- **Walking:** The city center is sprawling but very rewarding to explore on foot.

## 💎 Local Secrets & Insights
- [Templo de Debod](search:Templo de Debod): An authentic ancient Egyptian temple gifted to Spain. It's the most magical spot in Madrid during sunset.
- [Retiro Park](search:Retiro Park): It’s the lungs of Madrid. Make sure to visit the [Palacio de Cristal](search:Palacio de Cristal) (Crystal Palace) inside for some stunning photos.
- [El Rastro](search:El Rastro): Immerse yourself in the Sunday morning market crowd, but keep a cautious eye on your belongings.''';

  // SEVILLA
  static const _sevillaTR = '''# Sevilla Rehberi: Endülüs'ün Ruhunu Keşfedin 🇪🇸

Sevilla; portakal çiçeği kokulu sokakları, tutkulu Flamenco müziği ve dünyanın en büyük Gotik katedraliyle Endülüs ruhunun en canlı yaşandığı şehirdir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Mart-Nisan):** En sevilen zaman. *Semana Santa* (Kutsal Hafta) ve *Feria de Abril* (Nisan Panayırı) ile şehir adeta büyülenir. Portakal çiçekleri her yeri sarar.
- **Uyarı:** Yaz aylarında (Temmuz-Ağustos) Sevilla "Avrupa'nın tavası" gibidir. Sıcaklık 45 dereceyi aşabilir, bu aylardan kaçının!

## 🏘️ Konaklama Rehberi
- **Santa Cruz:** Eski Yahudi mahallesi. Daracık, begonvilli labirent sokaklar ve tarihi Sevilla ruhu.
- **Triana:** Nehrin karşı kıyısı. Flamenco'nun, seramiğin ve gerçek yerel hayatın merkezi.
- **Alameda:** Şehrin bohem ve alternatif yüzü. Yerel halkın takıldığı barlar ve kafeler için ideal.

## 🍽️ Ne Yenir ve İçilir?
- **Tapas Kültürü:** Sevilla, tapasın doğduğu yerlerden biridir. "Montadito" (küçük sandviçler) ve deniz ürünleri meşhurdur.
- **Siesta:** Sevilla'da öğle uykusu (siesta) hala çok ciddiye alınır. 14:00-17:30 arası dükkanların çoğu kapalıdır, siz de dinlenin!
- **Flamenco:** Turistik şovlar yerine Triana'daki daha küçük, samimi barlarda (Peña) gerçek flamenkoyu arayın.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Şehir merkezi düzdür ve keşfetmenin en iyi yolu yürümektir.
- **Bisiklet (Sevici):** Şehir genelinde çok iyi bir bisiklet yolu ağı vardır.

## 💎 Lokal Sırlar & İpuçları
- [Plaza de España](search:Plaza de España): Sabah erken gidin; henüz kalabalık yokken o görkemi ve seramiklerin (azulejos) detaylarını tek başınıza görün.
- [Metropol Parasol (Setas)](search:Metropol Parasol): Dünyanın en büyük ahşap yapısı. Gün batımında çatısına çıkıp Sevilla'nın damlarını izlemek harikadır.''';

  static const _sevillaEN = '''# Seville Guide: Discover the Soul of Andalusia 🇪🇸

Seville is the vibrant capital of Andalusia, where the air smells of orange blossoms, the passion of Flamenco is felt in every bar, and the world's largest Gothic cathedral dominates the skyline.

## 📅 Best Time to Visit
- **Spring (March-April):** The most beloved time. The city mesmerizes with *Semana Santa* (Holy Week) and the *Feria de Abril* (April Fair). The scent of orange blossoms is everywhere.
- **Warning:** During summer (July-August), Seville is often called the "Frying Pan of Europe." Temperatures can soar above 45°C—avoid these months at all costs!

## 🏘️ Neighborhood Guide
- **Santa Cruz:** The former Jewish quarter. Think narrow, bougainvillea-filled labyrinthine streets and the historic soul of Seville.
- **Triana:** Across the river. The true center of Flamenco, ceramic pottery, and authentic local life.
- **Alameda:** The bohemian and alternative side of the city. Ideal for bars and cafes frequented by the locals.

## 🍽️ Food & Dining Etiquette
- **Tapas Culture:** Seville is one of the birthplaces of tapas. "Montaditos" (small sandwiches) and fresh seafood are legendary here.
- **The Siesta:** In Seville, the midday nap (siesta) is still very much alive. Most shops close between 2:00 PM and 5:30 PM—do as the locals do and rest!
- **Flamenco:** Instead of flashy tourist shows, seek out "Peñas" (social clubs) or small bars in Triana for a more raw and authentic Flamenco experience.

## 🚇 Transportation Tips
- **Walking:** The historical center is flat and very compact, making walking the most enjoyable way to explore.
- **Bikes (Sevici):** Seville has an excellent bike-sharing system and many dedicated cycle lanes across the city.

## 💎 Local Secrets & Insights
- [Plaza de España](search:Plaza de España): Visit early in the morning. Witness the grandeur and the intricate ceramic details (azulejos) before the crowds arrive.
- [Metropol Parasol (The Mushrooms)](search:Metropol Parasol): The largest wooden structure in the world. Head to the top at sunset to walk the winding pathways above the rooftops of Seville.''';


  // ISTANBUL
  static const _istanbulTR = '''# İstanbul'u Yaşama Sanatı: Kapsamlı Rehber 🇹🇷

İstanbul sadece gezilecek bir yer değil, hissedilecek bir şehirdir. Kaotik, büyüleyici ve çok katmanlı. İşte bu şehri gerçek bir lokal gibi deneyimlemenin harmanlanmış rehberi.

## 📅 Ne Zaman Gidilir?
- **Erguvan Mevsimi (Nisan-Mayıs):** Şehir mora boyanır, hava yürüyüş için idealdir. Boğaz hattı bu dönemde bir başka güzel olur.
- **Sonbahar (Eylül-Kasım):** Şehrin en romantik zamanı. Turist kalabalığı azalır, İstanbul'un o tatlı hüznü çöker.
- **İpucu:** Temmuz-Ağustos sıcaklarından kaçınmaya çalışın; nemli hava yokuşları tırmanmayı zorlaştırabilir.

## 🏘️ Semt Rehberi
- **Karaköy & Galata:** Modern sanat, graffitiler ve tasarım dükkanlarıyla dolu. Sokaklarında kaybolmak için en iyi bölge.
- **Moda (Kadıköy):** Şehrin nefes alanı. Sahilde çimlere yayılmak, vintage dükkanları gezmek ve sakinliği hissetmek için birebir.
- **Cihangir & Çukurcuma:** Antikacılar, kediler ve entelektüel bir hava. Merdivenli sokaklarında harika fotoğraf kareleri yakalarsınız.

## 🍽️ Ne Yenir ve İçilir?
- **Kahvaltı Ritüeli:** Otel kahvaltısını boşverin. *Beşiktaş Kahvaltıcılar Sokağı*'nda veya Cihangir/Moda ara sokaklarında "serpme kahvaltı" kültürünü yaşayın. Pişi ve Menemen olmazsa olmaz.
- **Sokak Lezzetleri:**
  - **Midye Dolma:** Tabakta değil, tezgah başında yenir. Limonu sıkın, tadını çıkarın.
  - **Balık Ekmek:** Eminönü'ndeki turistik tekneler yerine, Karaköy hırdavatçılar çarşısının oradaki daha salaş tezgahları keşfedin.
- **Meyhane Kültürü:** Akşam yemeği için *Asmalımescit* yerine, daha lokal kalan *Yeniköy* veya *Kadıköy Güneşli Bahçe Sokak* taraflarını deneyin.

## 🚇 Ulaşım & Pratik Bilgiler
- **İstanbulKart:** Şehrin anahtarı. Vapur, metro, otobüs her yerde geçer.
- **Vapur Terapisi:** Sadece bir ulaşım aracı değil, dünyanın en güzel manzaralı yolculuğudur. Bir çay söyleyin, simidinizi martılarla paylaşın.
- **Metro ve Trafik:** Trafik saatlerinde taksi bulmak imkansızlaşabilir. Metro (M2) ve Tramvay (T1) ağını kullanmak her zaman en hızlı çözümdür.

## 💎 Lokal Sırlar & İpuçları
- **Alternatif Gün Batımı:** [Galata Kulesi](search:Galata Kulesi) önündeki kuyrukta saatler harcamayın. Çevredeki teraslı kafeler veya Üsküdar *[Salacak](search:Salacak)* sahili, tarihi yarımada silüetini izlemek için çok daha keyiflidir.
- **Şehrin Gerçek Sahipleri:** Kediler her yerde. Onlara saygılı davranın; onlar İstanbul'un ruhudur.
- **Müze Kart:** Uzun bilet kuyruklarından kurtulmak için mutlaka bir müze kart edinin veya biletinizi online alın.''';

  static const _istanbulEN = '''# The Art of Experiencing Istanbul 🇹🇷

Istanbul is not just a destination; it's a feeling. It's chaotic, mesmerizing, and deeply historical all at once. Here is a curated guide to navigating this multi-layered city like a pro.

## 📅 Best Time to Visit
- **Spring (April-May):** The city turns pink with Juda trees (Erguvan). The weather is crisp, perfect for long Bosphorus walks.
- **Autumn (Sept-Nov):** Locals' favorite season. The melancholy of the Bosphorus is best enjoyed with a light jacket.
- **Tip:** Avoid mid-summer if you can; the humidity can be overwhelming for exploring on foot.

## 🏘️ Neighborhood Guide
- **Karaköy & Galata:** The heart of the modern vibe. Full of street art, hidden courtyards, and design shops. Great for getting lost.
- **Moda (Asian Side):** A laid-back, residential haven. Think seaside promenades, tea gardens, and a very "local" feel.
- **Cihangir & Çukurcuma:** Famous for antique shops and bohemian cafes. You might spot a few writers or actors here.

## 🥯 Gastronomy Route
- **Breakfast Ritual:** Skip the hotel buffet. Authenticity lies in *Beşiktaş Kahvaltıcılar Sokağı* (Breakfast Street) or the backstreets of Cihangir and Moda.
- **Street Eats:**
  - **Midye Dolma (Stuffed Mussels):** A night-out tradition. Eat them standing at the stall, squeeze lemon, repeat.
  - **Balık Ekmek (Fish Sandwich):** Instead of the rocky boats in Eminönü, try the local grillers in the backstreets of Karaköy fish market.
- **Coffee Culture:** While Turkish coffee is a must, the third-wave coffee scene is exploding in areas like Topağacı and Moda.

## 🚇 Transportation & Logistics
- **Istanbulkart:** Essential. Buy one at any metro station; it works on ferries, buses, and trams.
- **The Ferry Experience:** The best way to commute. Taking a ferry from Europe to Asia at sunset is cheaper and better than any paid tour.
- **Metro vs Taxi:** Traffic is unpredictable. Rely on the Metro (M2) and Tram (T1) networks to bypass the gridlock.

## 💎 Local Secrets & Insights
- **Sunset Views:** Skip the long queue at [Galata Tower](search:Galata Tower). Instead, head to a rooftop terrace nearby or cross to the Asian side to *[Salacak](search:Salacak)* to watch the silhouette of the old city.
- **Cat Capital:** Istanbul belongs to its cats. You'll see them everywhere; they are community-cared and highly respected.
- **Museum Pass:** Highly recommended to save time in ticket lines for major attractions like Topkapi Palace.''';

  // PARIS
  static const _parisTR = '''# Paris'in Gerçek Yüzü: Klişelerden Uzak 🇫🇷

Filmlerdeki o kusursuz sahneleri bir kenara bırakın. Gerçek Paris daha karmaşık, daha "cool" ve kesinlikle çok daha lezzetli. İşte Işıklar Şehri'nde bir turist gibi değil, bir Parizyen gibi gezmenin yolları.

## 📅 Mevsimsel Ritim
- **Piknik Mevsimi (Mayıs-Haziran):** Havalar ısınınca Seine kenarı ve Canal Saint-Martin, şarabını ve peynirini kapan yerlilerle dolar. Aralarına karışın, gerçek sosyal hayat burada.
- **Kış Büyüsü:** Gri ve soğuk olabilir ama kafelerin sıcaklığı ve o meşhur yılbaşı ışıklandırmaları şehre başka bir hava katar.
- **İpucu:** Paris'i yürüyerek gezmek için en güzel zaman Sonbahar'ın başlarıdır (Eylül-Ekim).

## 🏘️ Bölge (Arrondissement) Seçimi
- **Le Marais (3. & 4. Bölge):** Tarihi doku, modern moda ve canlı sokaklar. En iyi falafeller ve sanat galerileri burada.
- **Saint-Germain-des-Prés:** Entelektüel Paris. Meşhur edebiyatçıların uğrak noktası olan kafeler ve zarif butikler.
- **Canal Saint-Martin (10. Bölge):** Daha genç, "hipster" ve dinamik. En iyi yeni nesil kahveciler ve brunch mekanları bu bölgede.

## 🥐 Gurme Emirleri
- **"Bonjour" Kuralı:** Bir dükkana girdiğinizde "Bonjour" demek isteğe bağlı değil, zorunludur. Bu basit nezaket, alacağınız hizmetin kalitesini doğrudan etkiler.
- **Kruvasan Testi:** Üstünüz başınız pul pul dökülen hamur parçalarıyla dolmuyorsa, o kruvasan olmamıştır. Fırınlardan (Boulangerie) sabah taze taze alın.
- **Formule Midi:** Öğle yemeği için restoranların sunduğu set menüleri tercih edin. Akşamın yarı fiyatına harika bir gurme deneyimi yaşarsınız.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Paris aslında küçük bir şehirdir. En iyi detaylar sokak aralarında yürürken keşfedilir.
- **Navigo Easy:** Kağıt biletler yerine bu temassız kartı alın ve doldurun. Metro kullanımı çok daha pratik olur.
- **Velib:** Şehrin her yerindeki bisiklet sistemi. Özellikle nehir kenarında sürmek çok keyiflidir.

## 💎 Lokal Sırlar & İpuçları
- **Eyfel Manzarası:** Kuleye çıkmak yerine [Zafer Takı (Arc de Triomphe)](search:Arc de Triomphe) tepesine çıkın. Hem şehri hem de bizzat Eyfel'i görebilirsiniz.
- [Orsay Müzesi](search:Musée d'Orsay): Louvre çok devasadır ve yorucudur. Daha insancıl bir ölçekte sanat deneyimi için Eski bir tren garı olan Orsay'ı tercih edin.
- [Passage des Panoramas](search:Passage des Panoramas): Paris'in tarihi pasajlarını keşfedin. Antikacılar ve küçük restonranlarla dolu bu pasajlar sizi zamanda yolculuğa çıkarır.''';

  static const _parisEN = '''# The Real Paris: Beyond the Clichés 🇫🇷

Forget the flawless movie scenes. Real Paris is more complex, cooler, and definitely much tastier. Here is how to navigate the City of Lights like a Parisian, not a tourist.

## 📅 Seasonal Rhythm
- **Picnic Season (May-June):** As the weather warms up, the banks of the Seine and Canal Saint-Martin fill with locals armed with wine and cheese.
- **Winter Magic:** It can be grey and cold, but the warmth of the cafes and the famous Christmas lights give the city a special atmosphere.
- **Tip:** The best time for walking tours is early Autumn (September-October) with its crisp air and golden leaves.

## 🏘️ District (Arrondissement) Guide
- **Le Marais (3rd & 4th):** Historic architecture, cutting-edge fashion, and vibrant streets. Find the best falafel and art galleries here.
- **Saint-Germain-des-Prés:** Intellectual Paris. Home to iconic literary cafes and elegant boutiques.
- **Canal Saint-Martin (10th):** Younger, "hipster," and dynamic. The best third-wave coffee shops and brunch spots are in this area.

## 🥐 Food & Dining Etiquette
- **The "Bonjour" Rule:** Saying "Bonjour" when entering a shop is not optional—it's mandatory. This simple courtesy is the key to good service.
- **The Croissant Test:** If your clothes aren't covered in flaky crumbs while eating it, it's not a real croissant. Get them fresh from a *Boulangerie* in the morning.
- **Formule Midi:** For lunch, look for set menus. You can experience a high-end gourmet meal for a fraction of the dinner price.

## 🚇 Transportation Tips
- **Walking:** Paris is surprisingly compact. The best details are discovered while wandering through the side streets.
- **Navigo Easy:** Skip the paper tickets and get this contactless card. It makes using the Metro much more seamless.
- **Velib:** The city-wide bike-sharing system. Cycling along the river is a quintessential Parisian experience.

## 💎 Local Secrets & Insights
- **The Best Eiffel View:** Instead of climbing the Tower, go to the top of the [Arc de Triomphe](search:Arc de Triomphe). You get the whole city view, including the Eiffel Tower itself!
- [Orsay over Louvre](search:Musée d'Orsay): The Louvre is massive and exhausting. For a more digestible art experience, visit the *Musée d'Orsay*, housed in a stunning former train station.
- [Passage des Panoramas](search:Passage des Panoramas): Discover the historic covered passages. Filled with stamp collectors and tiny bistros, they feel like stepping back in time.''';

  // BARCELONA

  // FLORANSA
  static const _floransaTR = '''# Floransa Rehberi: Rönesans'ın Beşiği 🇮🇹

Floransa bir şehir değil, devasa bir sanat galerisidir. Michelangelo ve Da Vinci'nin ayak izlerini takip edeceğiniz, her adımda tarihin derinliklerini hissedeceğiniz büyüleyici bir yer.

## 📅 Ne Zaman Gidilir?
- **Bahar (Nisan-Mayıs):** Toskana güneşinin en yumuşak olduğu, bahçelerin çiçek açtığı zaman.
- **Sonbahar (Eylül-Ekim):** Bağ bozumu dönemi; hava taze ve şehir daha sakin.
- **İpucu:** Yaz aylarında (Temmuz-Ağustos) Floransa çok sıcak ve nemli olabilir, ayrıca inanılmaz bir turist kalabalığı vardır.

## 🏘️ Konaklama Rehberi
- **Santo Spirito:** Nehrin karşı kıyısı (Oltrarno). Yerel zanaatkarların, antikacıların ve en samimi Floransa hayatının merkezi.
- **San Marco:** Dünyanın en iyi sanat müzelerine ev sahipliği yapar. Tarihi ve daha sakin bir atmosfer isteyenler için.
- **Duomo Çevresi:** Şehrin tam kalbi. Her yere yürüyebilmek isteyenler için ama her zaman kalabalıktır.

## 🍽️ Ne Yenir ve İçilir?
- **Bistecca alla Fiorentina:** Dünyanın en iyi bifteklerinden biridir. Az pişmiş (rare) servis edilir, "iyi pişmiş" isterseniz şefle aranızı bozabilirsiniz!
- **Gelato:** Dondurma burada icat edildi! *Vivoli* veya *Perché No!* gibi köklü yerlerde gerçek İtalyan dondurmasını deneyin.
- **Lampredotto:** Floransa'nın gerçek sokak lezzeti. İşkembe sandviçi; denemek için cesur olun, yerliler buna bayılır!
- **Chianti:** Toskana'da olduğunuzu unutmayın; bölgenin meşhur kırmızı şaraplarının tadını çıkarın.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Floransa'nın tarihi merkezi araç trafiğine kapalıdır ve tamamen yürüyerek gezilecek kadar küçüktür.
- **Bisiklet:** Şehir merkezinde bisiklet sürmek hem keyifli hem de pratiktir.

## 💎 Lokal Sırlar & İpuçları
- [Piazzale Michelangelo](search:Piazzale Michelangelo): Gün batımında mutlaka burada olun. Floransa'nın o meşhur turuncu damlı manzarasını en iyi buradan izlersiniz.
- [Derici Pazarı (San Lorenzo)](search:San Lorenzo Pazarı): Kaliteli deri ürünler bulabilirsiniz ama pazarlık yapmayı unutmayın!
- **Rezervasyon:** [Uffizi](search:Uffizi Galerisi) ve [Academia](search:Accademia Galerisi) müzeleri için biletlerinizi haftalar öncesinden online alın, aksi takdirde gününüz kuyruklarda geçebilir.''';

  static const _floransaEN = '''# Florence Guide: Cradle of the Renaissance 🇮🇹

Florence isn't just a city; it's a massive art gallery. It's an enchanting place where you can follow in the footsteps of Michelangelo and Da Vinci, feeling the depths of history with every step.

## 📅 Best Time to Visit
- **Spring (April-May):** When the Tuscan sun is softest and the gardens are in full bloom.
- **Autumn (September-October):** The harvest season; the air is fresh, and the city feels slightly more tranquil.
- **Tip:** In July and August, Florence can be intensely hot and humid, and the tourist crowds are at their peak.

## 🏘️ Neighborhood Guide
- **Santo Spirito:** Across the river (Oltrarno). The hub of local artisans, antique shops, and the most authentic Florentine life.
- **San Marco:** Home to some of the world's most famous art museums. Ideal for those seeking a historical and quieter atmosphere.
- **Duomo Area:** The very heart of the city. Best for those who want to walk everywhere, though it's always bustling with people.

## 🍽️ Food & Dining Etiquette
- **Bistecca alla Fiorentina:** One of the best steaks in the world. It's traditionally served rare—asking for it "well done" is often considered a faux pas!
- **Gelato:** Ice cream was invented here! Try authentic Italian gelato at established spots like *Vivoli* or *Perché No!*.
- **Lampredotto:** The true street food of Florence. It's a tripe sandwich; be brave and give it a try—locals absolutely love it!
- **Chianti:** Remember you're in Tuscany; don't miss out on tasting the region's world-famous red wines.

## 🚇 Transportation Tips
- **Walking:** The historical center of Florence is largely pedestrianized and small enough to explore entirely on foot.
- **Biking:** Cycling through the center is both enjoyable and practical, though watch out for the cobblestones.

## 💎 Local Secrets & Insights
- [Piazzale Michelangelo](search:Piazzale Michelangelo): Make sure to be here at sunset. It offers the most iconic panoramic view of Florence's terracotta rooftops.
- [Leather Market (San Lorenzo)](search:San Lorenzo Pazarı): You can find high-quality leather goods here, but remember to bargain for the best price.
- **Bookings:** Get your tickets for the [Uffizi](search:Uffizi Galerisi) and [Academia](search:Accademia Galerisi) galleries weeks in advance online, otherwise you'll spend your day in endless queues.''';

  // VENEDIK
  static const _venedikTR = '''# Venedik Rehberi: Su Üstündeki Rüya 🇮🇹

Venedik; suyun üzerine inşa edilmiş mermer sarayları, sessizce süzülen gondolları ve zamanın durduğu hissini veren daracık sokaklarıyla dünyanın en benzersiz şehridir.

## 📅 Ne Zaman Gidilir?
- **Bahar ve Güz:** Nisan-Mayıs ve Eylül-Ekim dönemleri havanın en dengeli olduğu, yürüyüşün keyifli olduğu zamanlardır.
- **Karnaval Zamanı (Şubat):** Şehir maskeler ve kostümlerle dolduğunda büyülü ama çok kalabalık ve pahalı olur.
- **İpucu:** Yazın (Temmuz-Ağustos) kanallarda koku olabilir ve nem oldukça yüksektir.

## 🏘️ Konaklama Rehberi
- **Cannaregio:** Venedik'in gerçek yerel yüzü. Daha az turistik, daha çok kanal kenarı barı ve mahalle havası.
- **Dorsoduro:** Sanat ve öğrenci mahallesi. Harika müzeler ve daha canlı, genç bir gece hayatı.
- **Castello:** Şehrin en yeşil ve sessiz bölgesi. Venediklilerin hala yaşadığı, "çamaşırların sokaklara asıldığı" o klasik görüntüyü burada bulursunuz.

## 🍽️ Ne Yenir ve İçilir?
- **Cicchetti Deneyimi:** Venedik usulü tapas. Küçük ekmek üstü lezzetleri bir kadeh şarap (ombra) eşliğinde ayakta atıştırmak buranın en büyük geleneğidir.
- **Spritz Veneziano:** Bu meşhur içkinin anavatanındasınız. Akşamüstü kanala karşı yudumlamadan dönmeyin.
- **Gondol Fiyatları:** Gondol fiyatları resmi olarak sabittir ama binmeden önce mutlaka süreyi ve rotayı teyit edin.
- **Ekmek Ücreti (Coperto):** İtalya'da masaya oturduğunuzda otomatik olarak eklenen servis ücretine (coperto) hazırlıklı olun.

## 🚇 Ulaşım İpuçları
- **Vaporetto:** Venedik'in otobüsleridir. Kanallar arasında seyahat etmenin tek ana yoludur. Günlük bilet almak çok daha ekonomiktir.
- **Yürüyüş:** Venedik'te kaybolmak kaçınılmazdır ve aslında bu, şehri keşfetmenin en iyi yoludur.
- **Traghetto:** Büyük kanalı geçmek için kullanılan daha ucuz, basitleştirilmiş gondollardır. Sadece birkaç Euro'ya gondol deneyimini yaşarsınız.

## 💎 Lokal Sırlar & İpuçları
- [Libreria Acqua Alta](search:Libreria Acqua Alta): Dünyanın en güzel kitapçılarından biri. Kitapların botlar ve gondollar içinde durduğu, su baskınlarına karşı korunmuş bu büyüleyici mekana mutlaka uğrayın.
- [Burano Adası](search:Burano): Venedik'ten feribotla geçilen, rengarenk evleriyle meşhur bu ada, fotoğraf tutkunları için bir cennettir.
- **Acqua Alta (Yüksek Su):** Kış aylarında şehirde su seviyesi yükselebilir. Bu bir felaket değil, Venedik hayatının bir parçasıdır.''';

  static const _venedikEN = '''# Venice Guide: A Dream Floating on Water 🇮🇹

Venice is the world's most unique city, with its marble palaces built over the lagoons, gondolas gliding silently, and narrow alleys that feel as though time has still stood here.

## 📅 Best Time to Visit
- **Spring and Autumn:** April-May and September-October offer the most balanced weather, perfect for endless explorations.
- **Carnival Season (February):** When the city is filled with masks and costumes—it's truly magical but also very crowded and expensive.
- **Tip:** In mid-summer (July-August), the canals can have an odor and the humidity is incredibly high.

## 🏘️ Neighborhood Guide
- **Cannaregio:** The true local face of Venice. Less touristy, with many waterfront bars and a genuine neighborhood feel.
- **Dorsoduro:** The artistic and student hub. Home to great museums and a more vibrant, younger nightlife scene.
- **Castello:** The greenest and quietest part of the city. This is where you'll find the classic Venice with laundry hanging over the narrow streets.

## 🍽️ Food & Dining Etiquette
- **Cicchetti Experience:** Venetian-style tapas. Spending an evening moving from one bar to another, having a glass of wine (ombra) and small bites, is a beloved local tradition.
- **Spritz Veneziano:** You are in the birthplace of this world-famous drink. Don't leave without sipping one by the canal.
- **Gondola Rates:** Official prices are fixed, but always confirm the duration and route with the gondolier before setting off.
- **Coperto:** Be prepared for the standard cover charge (coperto) added to your bill when you sit down for a meal.

## 🚇 Transportation Tips
- **Vaporetto:** The water buses of Venice. They are the main way to travel between the islands and through the canals. A day pass is much more economical.
- **Walking:** Getting lost in Venice is inevitable, and frankly, it's the best way to discover the city's hidden charms.
- **Traghetto:** These are simplified gondolas used to cross the Grand Canal for just a few Euros—a great way to get a gondola experience on a budget.

## 💎 Local Secrets & Insights
- [Libreria Acqua Alta](search:Libreria Acqua Alta): One of the world's most beautiful bookstores. Books are stored in boats and bathtubs to protect them from high tides—don't miss the staircase made of old books!
- [Burano Island](search:Burano): A short ferry ride from Venice, this island is famous for its brightly colored houses. A photographer's paradise.
- **Acqua Alta (High Water):** During winter, the water level can rise. It's not a disaster; it's a unique part of Venetian life.''';

  // MILANO
  static const _milanoTR = '''# Milano Rehberi: Moda, Tasarım ve Estetik 🇮🇹

Milano; İtalya'nın modern yüzü, moda dünyasının kalbi ve tasarımın başkentidir. Gökdelenlerle Gotik katedrallerin, lüks butiklerle tarihi kanalların kusursuz uyumu.

## 📅 Ne Zaman Gidilir?
- **Moda Haftaları (Eylül ve Şubat):** Şehir en havalı ve en kalabalık zamanını yaşar. Otel fiyatları artar ama sokak modası görülmeye değerdir.
- **Bahar ve Güz:** Gezmek için en ideal havalar bu dönemdedir.

## 🏘️ Konaklama Rehberi
- **Brera:** Şehrin en şık ve aristokrat mahallesi. Sanat galerileri, antikacılar ve lüks kafeler.
- **Navigli:** Kanallar bölgesi. Gece hayatı ve akşamüstü içecekleri (aperitivo) için en popüler yer.
- **Isola:** Eskiden işçi mahallesi olan bu bölge, şimdi dikey bahçeli gökdelenleri ve modern mekanlarıyla çok trend.

## 🍽️ Ne Yenir ve İçilir?
- **Risotto alla Milanese:** Safranlı bu sarı pilav, Milano mutfağının baş tacıdır.
- **Cotoletta alla Milanese:** Panelendirilmiş çıtır çıtır dana pirzola.
- **Aperitivo Ritüeli:** Milano'da akşam sefası saat 18:30'da başlar. Bir içki istersiniz ve yanında açık büfe atıştırmalıklar ücretsiz gelir.
- **Kıyafet Kodu:** Milanolular şıklığa çok önem verir. Akşam yemeğine giderken biraz özenli giyinmek hoş karşılanır.

## 🚇 Ulaşım İpuçları
- **Metro:** Çok gelişmiş ve kullanımı kolaydır.
- **Eski Tramvaylar:** 1920'lerden kalma ahşap koltuklu tramvaylarla (örneğin 1 numara) bir şehir turu yapın.

## 💎 Lokal Sırlar & İpuçları
- [Duomo'nun Çatısı](search:Duomo di Milano): Katedralin içine girmek yetmez, asansörle çatısına çıkın. Gotik kulelerin arasından Alpler'e kadar uzanan bir manzara sizi bekliyor.
- [10 Corso Como](search:10 Corso Como): Bir sanat galerisi, kitapçı, butik ve kafe; tasarım dünyasına kısa bir yolculuk.
- **İndirim Zamanı:** Büyük indirim sezonları Ocak başında ve Temmuz başında başlar.''';

  static const _milanoEN = '''# Milan Guide: Fashion, Design & Aesthetics 🇮🇹

Milan is the modern face of Italy, the heart of the global fashion world, and the capital of design. It’s where skyscrapers meet Gothic cathedrals and luxury boutiques harmonize with historic canals.

## 📅 Best Time to Visit
- **Fashion Weeks (September & February):** The city is at its trendiest and busiest. Hotel prices spike, but the street style is a spectacle in itself.
- **Spring & Autumn:** These seasons offer the best weather for exploring the city comfortably.

## 🏘️ Neighborhood Guide
- **Brera:** The most elegant and aristocratic area. Think art galleries, antique shops, and refined cafes.
- **Navigli:** The canal district. This is the place to be for nightlife and the iconic Milanese *aperitivo*.
- **Isola:** Once a working-class neighborhood, it's now a trendsetting hub with vertical gardens and ultra-modern spaces.

## 🍽️ Food & Dining Etiquette
- **Risotto alla Milanese:** This saffron-infused yellow risotto is the crown jewel of Milanese cuisine.
- **Cotoletta alla Milanese:** A delicious, breaded veal cutlet fried to perfection.
- **Aperitivo Ritual:** In Milan, "happy hour" starts at 6:30 PM. Buy a drink, and enjoy a spread of free snacks—it's a sacred local tradition.
- **Dress Code:** Milanesi take appearance seriously. Dressing up a little for dinner is highly recommended and well-received.

## 🚇 Transportation Tips
- **The Metro:** Extensive, clean, and very easy to navigate.
- **Vintage Trams:** Take a ride on the 1920s wooden trams (line 1 is great) for a nostalgic city tour at the cost of a standard ticket.

## 💎 Local Secrets & Insights
- [The Duomo Rooftop](search:Duomo di Milano): Don't just go inside the cathedral; take the lift to the terrace. Walking among the Gothic spires with a view of the Alps is unforgettable.
- [10 Corso Como](search:10 Corso Como): A unique mix of a gallery, bookstore, boutique, and cafe—a must-visit for design lovers.
- **Sale Season:** Major sales start in early January and early July.''';

  // NAPOLI
  static const _napoliTR = '''# Napoli Rehberi: Akdeniz'in Vahşi Ruhu 🇮🇹

Napoli; kaotik, gürültülü ama bir o kadar da içten ve lezzetli bir şehirdir. İtalya'nın en "gerçek" halini görmek istiyorsanız Napoli tam size göre.

## 📅 Ne Zaman Gidilir?
- **Bahar (Nisan-Haziran):** Hava ılıktır ve Vezüv Yanardağı'nın manzarası tertemizdir.
- **Noel Zamanı (Aralık):** Meşhur "Presepe" (İsa'nın doğuş sahnesi) figürleriyle ünlü San Gregorio Armeno sokağı bu dönemde bir masal diyarı gibidir.

## 🏘️ Konaklama Rehberi
- **Centro Storico:** Şehrin UNESCO korumalı tarihi kalbi. Daracık sokaklar, çamaşır asılı balkonlar ve kaosun en tatlı hali.
- **Vomero:** Tepede, nezih ve modern bir mahalle. Fünikülerle çıkılır ve harika şehir manzaraları sunar.
- **Chiaia:** Deniz kenarında, şık butikler ve kaliteli restoranlarla dolu daha üst orta sınıf bölge.

## 🍽️ Ne Yenir ve İçilir?
- **Gerçek Pizza:** Pizzanın anavatanındasınız. *Margherita* ve *Marinara* dışında pek bir şeye ihtiyacınız yok. *Pizzeria Da Michele* gibi klasikleri deneyin.
- **Sfogliatella:** Kat kat çıtır hamurlu meşhur Napoli tatlısı. Sıcak yemeniz önerilir.
- **Espresso Kültürü:** Napoli'de kahve bir sanattır. Ayakta, hızlıca ve çok sıcak içilir.
- **Caffè Sospeso:** İhtiyacı olanlar için "askıda kahve" bırakma geleneği burada doğmuştur. Bir tane kendinize alın, bir tane de başkası için ödeyin.

## 🚇 Ulaşım İpuçları
- **Dikkatli Olun:** Trafik kuralı burada pek işlemez, özellikle scooterlara karşı yaya olarak çok dikkatli olun.
- **Füniküler:** Sahil ile yukarıdaki Vomero mahallesini birbirine bağlayan tarih ve keyif dolu bir ulaşım yolu.
- **Sanat Metrosu:** Linea 1 (1. Hat) istasyonları birer sanat galerisidir (özellikle Toledo istasyonu).

## 💎 Lokal Sırlar & İpuçları
- [Castel Sant'Elmo](search:Castel Sant'Elmo): Şehri, Vezüv Yanardağı'nı ve denizi 360 derece izlemek için en iyi seyir noktası.
- [Yeraltı Napolisi (Napoli Sotterranea)](search:Napoli Sotterranea): Şehrin altına inip antik Roma tiyatrolarını ve II. Dünya Savaşı sığınaklarını keşfedin.
- **Günübirlik Gezi:** Procida adası, Capri'ye göre daha az turistik ve çok daha renklidir.''';

  static const _napoliEN = '''# Naples Guide: The Wild Heart of the Mediterranean 🇮🇹

Naples is chaotic, noisy, and raw, but it's also incredibly sincere and delicious. If you want to see Italy's most authentic self, Naples is exactly where you belong.

## 📅 Best Time to Visit
- **Spring (April-June):** The weather is mild, and the views of Mount Vesuvius are crystal clear.
- **Christmas (December):** San Gregorio Armeno street, famous for its "Presepe" (Nativity scene) figurines, transforms into a magical wonderland.

## 🏘️ Neighborhood Guide
- **Centro Storico:** The UNESCO-protected heart of the city. Narrow alleys, laundry hanging from balconies, and the sweetest form of chaos.
- **Vomero:** An upscale, hilltop neighborhood accessed by funicular, offering fresh air and stunning panoramic views.
- **Chiaia:** A chic, seaside district filled with high-end boutiques and some of the city's finest dining.

## 🍽️ Food & Dining Etiquette
- **Real Pizza:** You are in the birthplace of pizza. Stick to the classics: *Margherita* or *Marinara*. Try local legends like *Pizzeria Da Michele*.
- **Sfogliatella:** A crisp, multi-layered pastry that is a staple of Neapolitan snacking. Best enjoyed warm.
- **Coffee Culture:** Coffee in Naples is an art form. It's served very hot, very short, and drunk standing up quickly.
- **Caffè Sospeso:** The tradition of "suspended coffee"—paying for an extra cup for someone in need—originated here. Buy one, leave one.

## 🚇 Transportation Tips
- **Be Vigilant:** Traffic rules are more suggestions than laws here. Be extremely careful of scooters when crossing the streets.
- **The Funiculars:** These are not just transport; they're historical rides that connect the coast to the Vomero neighborhood.
- **Metro Art Stations:** Line 1 stations are underground art galleries—Toledo station is widely considered one of the most beautiful in Europe.

## 💎 Local Secrets & Insights
- [Castel Sant'Elmo](search:Castel Sant'Elmo): The best vantage point for a 360-degree view of the city, the Bay of Naples, and Mount Vesuvius.
- [Napoli Sotterranea (Underground Naples)](search:Napoli Sotterranea): Descend below the streets to explore ancient Roman theaters and WWII air-raid shelters.
- **Day Trip:** The island of Procida is less touristy than Capri and significantly more colorful and authentic.''';

  // ATINA
  static const _atinaTR = '''# Atina Rehberi: Antik Miras ve Modern Kaos 🇬🇷

Atina; sadece Akropolis değil, tarihle modern sokak sanatının, kadim felsefeyle canlı gece hayatının iç içe geçtiği çok enerjik bir şehirdir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Nisan-Haziran):** Gezmek için en ideal sıcaklıklar. Tepeler hala yeşildir.
- **Erişilebilir Kış:** Atina kışın da nispeten ılıktır ve antik alanları kalabalıksız gezmek için harikadır.
- **İpucu:** Temmuz ve Ağustos aylarında Atina'da sıcaklık gölgede bile 40 dereceye çıkabilir. Akropolis'e çıkmak bu aylarda zordur.

## 🏘️ Semt Rehberi
- **Plaka:** Akropolis'in eteklerinde, bembeyaz evleri ve çiçekli sokaklarıyla en ikonik mahalle. Turistiktir ama her zaman büyüleyicidir.
- **Koukaki:** Son yılların en popüler bölgesi. Birçok gurme restoran, butik kafe ve yerel bir atmosfer.
- **Anafiotika:** Plaka'nın üst kısmında, Cyclades adalarını andıran küçük beyaz evler bölgesi. Şehrin ortasında bir Ege adası gibi.

## 🍽️ Ne Yenir ve İçilir?
- **Meze Kültürü:** Akşam yemeği uzun sürer. Masayı çeşitli mezelerle donatıp yavaş yavaş yemek bir gelenektir.
- **Freddo Espresso:** Atinalıların milli içeceğidir. Soğuk ve köpüklü bu kahveyi günün her saati ellerinde görebilirsiniz.
- **Souvlaki ve Gyros:** Hızlı, ucuz ve inanılmaz lezzetli sokak yemekleri.
- **Hesap Ödeme:** Yunanistan'da hesabı "Alman usulü" ödemek pek yaygın değildir; genellikle biri ısmarlar veya toplam hesap bölünür.

## 🚇 Ulaşım İpuçları
- **Metro:** Atina metrosu kazılırken birçok antik eser bulunmuştur; istasyonların bazıları küçük birer müze gibidir.
- **Yürüyüş:** Tarihi merkez (Plaka, Monastiraki, Thissio) tamamen yürünebilir bir ring hattı üzerindedir.

## 💎 Lokal Sırlar & İpuçları
- [Lycabettus Tepesi](search:Lycabettus Hill): Şehrin en yüksek noktası. Gün batımında veya gece Atina'nın sonsuz ışıklarını izlemek için buraya çıkın.
- **Laiki (Semt Pazarları):** Mahallelerde kurulan taze meyve ve sebze pazarları gerçek yerel hayatı gözlemlemek için harikadır.
- **Bedava Müzeler:** Ayın belirli Pazar günleri antik alanlara girişler ücretsiz olabilir, gitmeden önce kontrol edin.''';

  static const _atinaEN = '''# Athens Guide: Ancient Heritage & Modern Edge 🇬🇷

Athens is more than just the Acropolis; it's an energetic city where ancient history meets modern street art, and legendary philosophy blends with vibrant nightlife.

## 📅 Best Time to Visit
- **Spring (April-June):** Ideal temperatures for exploring. The surrounding hills are still lush and green.
- **Accessible Winter:** Athens remains relatively mild in winter—a great time to visit ancient sites without the massive crowds.
- **Tip:** In July and August, the city is a furnace. Climbing the Acropolis in 40°C heat can be dangerous; stay hydrated!

## 🏘️ Neighborhood Guide
- **Plaka:** Nestled under the Acropolis, this is the most iconic neighborhood with its whitewashed houses and flowering alleys.
- **Koukaki:** The trendiest spot in recent years. Fill with gourmet tavernas, boutique cafes, and a genuine residential feel.
- **Anafiotika:** Located at the top of Plaka, this area looks exactly like a Cycladic island. A tiny piece of the Aegean in the heart of the city.

## 🍽️ Food & Dining Etiquette
- **Meze Culture:** Dinner is a marathon, not a sprint. The tradition is to fill the table with various appetizers (meze) and share them slowly over wine or ouzo.
- **Freddo Espresso:** The "national drug" of modern Greeks. You’ll see everyone carrying these cold, frothy coffees at all hours.
- **Souvlaki & Gyros:** The ultimate fast, cheap, and delicious street food.
- **Splitting the Bill:** In Greece, splitting the bill down to the last cent is rare; usually, one person hosts or the total is roughly divided.

## 🚇 Transportation Tips
- **The Metro:** While digging the tunnels, many ancient artifacts were uncovered—some stations (like Syntagma) look like mini-museums.
- **Walking:** The historical heart (Plaka, Monastiraki, Thissio) is connected by a pedestrian ring that makes walking the best way to see the sights.

## 💎 Local Secrets & Insights
- [Lycabettus Hill](search:Lycabettus Hill): The highest point in the city center. Head up here at night to see the sprawling lights of Athens stretch all the way to the sea.
- **Laiki Markets:** These local farmers' markets are held weekly in different neighborhoods—the best place to see authentic local life.
- **Free Entry:** Many archaeological sites are free to the public on the first Sunday of the month during the winter season.''';

  static const _barcelonaTR = '''# Barcelona'nın Kodları: Gaudi'den Ötesi 🇪🇸

Barcelona canlı, sanatsal ve gürültülü. Gaudi şehrin yıldızı olsa da, asıl büyü Katalanların günlük yaşam tarzında saklı.

## 📅 Ne Zaman Gidilir?
- **Geç Bahar (Mayıs-Haziran):** Plaj sezonu açılır, festivaller başlar, şehir cıvıl cıvıldır.
- **Eylül:** Şehir *La Mercè* festivalini kutlar. Dev kuklalar ve "Correfoc" (ateş koşusu) etkinlikleri şehri alevler içinde bırakır. İnanılmaz bir deneyimdir.

## 🏘️ Konaklama Rehberi
- **Gracia:** Eskiden ayrı bir köymüş, hala o havasını koruyor. Trafiğe kapalı meydanları, butik dükkanları ile "turist değilim" diyenlerin tercihi.
- **El Born:** Ortaçağ sokakları gece hayatıyla buluşuyor. Daracık labirent sokaklar, en iyi barlar ve galeriler burada.
- **Eixample:** Geniş caddeler ve mimari tutkunları için. Güvenli, merkezi ve şık.
- **Uyarı:** *La Rambla* üzerinde kalmaktan kaçının. Çok gürültülü ve tam bir turist tuzağıdır.

## 🍽️ Ne Yenir ve İçilir?
- **Peçete Kuralı:** Geleneksel tapas barlarında yerde ne kadar çok peçete varsa, orası o kadar iyidir! Lezzetin ve kalabalığın işaretidir.
- **Pintxos Deneyimi:** *Carrer de Blai* sokağına gidin. Yan yana onlarca bar, tezgahlarında "pintxos" (ekmek üstü atıştırmalıklar) sunar. Bar bar gezmek buranın adeti.
- **Paella Uyarısı:** İyi bir paella pişmesi en az 20 dakika sürer. Önünüze 5 dakikada geliyorsa bilin ki donmuş üründür. Ayrıca yerliler paellayı öğlen yer, akşam değil.
- **Ne İçilir:** Sangria genellikle turistlere satılır. Yerliler gibi "Tinto de Verano" (Limonlu gazozlu şarap) veya "Cava" (Katalan şampanyası) tercih edin.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Eixample bölgesinin mimarisini görmenin tek yolu yürümektir. Kafanızı yukarı kaldırın ve binaların detaylarına bakın.
- **Hola Barcelona Kart:** Çok fazla metro kullanacaksanız ekonomik bir seçenek.
- **Havalimanı:** *Aerobus*, sizi hızlı ve konforlu bir şekilde doğrudan Plaça Catalunya'ya getirir.

## 💎 Şehir Dedikoduları & Sırlar
- [Sagrada Familia](search:Sagrada Familia): Biletinizi haftalar önceden alın. İkindi vaktini tercih edin; güneş vitraylara vurduğunda içeride oluşan renk cümbüşü büyüleyicidir.
- [Park Güell](search:Park Güell): Anıtsal bölge paralıdır ama etrafındaki ormanlık park alanı ücretsizdir ve manzara hemen hemen aynıdır.
- **Güvenlik Uyarısı:** Yankesicilik konusunda dikkatli olun. Çantanızı asla sandalyenin arkasına asmayın, masanın üstünde telefon bırakmayın. Kucağınızda tutun.
- **Yemek Saatleri:** Öğle yemeği 14:00, akşam yemeği 21:00'den sonra başlar. Midenizi buna göre ayarlayın!''';

  static const _barcelonaEN = '''# Barcelona Unlocked: Beyond the Guidebooks 🇪🇸

Barcelona is vibrant, artistic, and loud. While Gaudi is the star, the real charm lies in the daily lifestyle of the Catalans.

## 📅 Timing Your Visit
- **Late Spring (May-June):** Beach clubs open, festivals begin, and the mood is ecstatic.
- **September:** The city celebrates *La Mercè* festival with giant puppets and fire runs (*Correfoc*). A must-see cultural explosion.

## 🏘️ Where to Stay?
- **Gracia:** Once a separate village, now the bohemian heart. Pedestrian squares, independent boutiques, and a very strong local community feel.
- **El Born:** Medieval charm meets nightlife. Narrow maze-like streets filled with cocktail bars and galleries.
- **Eixample:** If you love architecture and broad avenues. Safe, central, and elegant.
- **Note:** Avoid staying right on *La Rambla*. It's noisy and overpriced.

## 🥘 Tapas & Dining Etiquette
- **The "Napkin Rule":** In traditional tapas bars, dirty napkins on the floor are a good sign—it means the food is delicious and the place is busy!
- **Pintxos Experience:** Head to *Carrer de Blai*. It's a street full of bars serving "pintxos" (bite-sized snacks on bread). Hop from one bar to another.
- **Paella Tip:** Good paella takes time (20+ mins). If it arrives in 5 minutes, it's frozen. Also, locals eat it for lunch, rarely for dinner.
- **Must Drink:** Forget Sangria (mostly for tourists). Try "Tinto de Verano" (summer red wine with lemon soda) or "Cava" (local sparkling wine).

## 🚇 Getting Around
- **Walking:** The best way to appreciate the "Modernista" facades in Eixample. Look up!
- **Hola Barcelona Card:** Great value if you plan to use the metro extensively.
- **From Airport:** The *Aerobus* is fast, frequent, and comfortable, taking you directly to Plaça Catalunya.

## 💎 Local Insights
- [Sagrada Familia](search:Sagrada Familia): Book weeks in advance. Visit in the late afternoon when the sun hits the stained glass—the light show inside is spiritual.
- [Park Güell](search:Park Güell): The monumental zone requires a ticket, but the surrounding forest area is free and offers similar views with fewer crowds.
- **Safety Specifics:** Pickpocketing is real. Never hang your bag on the back of your chair at a cafe. Keep belongings on your lap or in front of you.
- **Meal Times:** Lunch is around 2 PM, dinner starts after 9 PM. Adjust your stomach clock!''';

  // PRAG
  static const _pragTR = '''# Prag Rehberi: Yüz Kuleli Şehir 🇨🇿

Prag; Arnavut kaldırımlı sokakları, Ortaçağ'dan kalma astronomik saati ve heybetli kalesiyle adeta bir masal kitabından fırlamış gibidir. Vltava Nehri'nin iki yakasına yayılmış bu şehir, Avrupa'nın en iyi korunmuş tarihi merkezlerinden biridir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Mayıs):** Şehir pembe ve beyaz çiçeklerle dolar, hava gezmek için mükemmeldir.
- **Noel Zamanı (Aralık):** Prag'ın meydanları dünyanın en romantik Noel pazarlarından birine dönüşür. Sıcak şarap kokusu her yeri sarar.
- **İpucu:** Temmuz ve Ağustos hem çok sıcak hem de aşırı kalabalık olur; tadını çıkarmak zordur.

## 🏘️ Konaklama Rehberi
- **Mala Strana (Küçük Mahalle):** Kalenin hemen altında, Barok binalar ve sessiz sokaklar. En romantik bölge.
- **Vinohrady:** Yerlilerin favorisi. Harika parklar, kaliteli restoranlar ve turistik kaostan uzak bir yaşam.
- **Stare Mesto (Eski Şehir):** Her şeyin merkezinde olmak isteyenler için. Tarih kapınızın önündedir.

## 🍽️ Ne Yenir ve İçilir?
- **Bira (Pivo):** Çek Cumhuriyeti dünyada kişi başı bira tüketiminde liderdir. *Pilsner Urquell* mutlaka denenmeli. Biraya "su" muamelesi yapılır!
- **Svíčková:** Kremsi sebze soslu sığır eti; yanındaki ekmek toplarıyla (knedlíky) tam bir lezzet şöleni.
- **Trdelník:** Turistlerin bayıldığı, dumanı üstünde şekerli rulo tatlı. Her köşede bulabilirsiniz.
- **Bahşiş (Tip):** Hesap geldiğinde tutarı yukarı yuvarlamak veya %10 civarında bir bahşiş bırakmak gelenektir.

## 🚇 Ulaşım İpuçları
- **Tramvay:** Prag'ın tramvay ağı harikadır. Özellikle 22 numaralı hat, adeta bir şehir turu yaptırır.
- **Yürüyüş:** Prag bir "yürüyüş şehri"dir. Eski şehir ile kaleyi birbirine bağlayan Charles Köprüsü'nü gün doğumunda yürüyerek geçmek büyüleyicidir.

## 💎 Lokal Sırlar & İpuçları
- **Döviz Bozdurma:** Sokaktaki döviz bürolarına çok dikkat edin. "0% Komisyon" yazanların çoğu gizli ücretler alır. *Honest Guide* videolarına göz atmadan para bozdurmayın!
- [Letná Park](search:Letná Park): Şehrin en iyi bira bahçesi ve Vltava üzerindeki köprülerin en güzel fotoğraf karesi buradadır.
- **Kütüphane Büyüsü:** *[Strahov Manastırı](search:Strahov Monastery)* kütüphanesini görün; kendinizi Harry Potter filminde hissedeceksiniz.''';

  static const _pragEN = '''# Prague Guide: The City of a Hundred Spires 🇨🇿

Prague feels like a page out of a fairytale, with its cobblestone streets, medieval astronomical clock, and the majestic castle overlooking the Vltava River. It remains one of Europe's best-preserved historic gems.

## 📅 Best Time to Visit
- **Spring (May):** The city blooms in pink and white, and the weather is perfect for long walks.
- **Christmas (December):** Prague transforms into one of the world's most romantic settings with its iconic Christmas markets and the scent of mulled wine.
- **Tip:** Avoid July and August if possible; the heat and the density of the crowds can make exploring feel like a chore.

## 🏘️ Neighborhood Guide
- **Mala Strana (Lesser Town):** Tucked right under the castle. Baroque architecture, hidden gardens, and quiet alleys—the most romantic area.
- **Vinohrady:** A local favorite. Residential yet chic, with great parks, elegant dining, and a peaceful escape from the tourist center.
- **Stare Mesto (Old Town):** For those who want to be in the thick of it all. History is literally on your doorstep.

## 🍽️ Food & Dining Etiquette
- **Beer (Pivo):** The Czech Republic leads the world in beer consumption per capita. Trying *Pilsner Urquell* is a must. Here, beer is often cheaper than water!
- **Svíčková:** Beef in a creamy vegetable sauce, served with traditional bread dumplings (knedlíky)—it's the ultimate comfort food.
- **Trdelník:** The famous cinnamon-sugar rolled pastry you'll see everywhere. Best enjoyed hot from the grill.
- **Tipping:** Standard practice is to round up the bill or leave about 10% if the service was good.

## 🚇 Transportation Tips
- **The Trams:** Prague has an excellent tram network. Line 22 is legendary as it travels past many of the major sights for the cost of a standard ticket.
- **Walking:** Prague is made for walking. Crossing the Charles Bridge at sunrise is a spiritual experience you’ll never forget.

## 💎 Local Secrets & Insights
- **Currency Exchange:** Be very cautious with street bureaux de change. Some advertise "0% commission" but use horrible rates. Use reputable places recommended by locals.
- [Letná Park](search:Letná Park): Home to the city's best beer garden and the iconic viewpoint overlooking the bridges of the Vltava.
- **Strahov Library:** Visit the library at [Strahov Monastery](search:Strahov Monastery); it's one of the most breathtaking libraries in the world and feels like stepping into a movie set.''';

  // VIYANA
  static const _viyanaTR = '''# Viyana Rehberi: İmparatorluk Zarafeti ve Kahve Kültürü 🇦🇹

Viyana; geniş caddeleri, heybetli sarayları ve dünyaca ünlü klasik müzik mirasıyla Avrupa'nın en asil şehirlerinden biridir. Disiplin ve sanatın iç içe geçtiği bir başkent.

## 📅 Ne Zaman Gidilir?
- **Noel Pazarları (Kasım Sonu-Aralık):** Viyana bu dönemde bir ışık şöleni yaşar. Belediye binası (Rathaus) önündeki pazar büyüleyicidir.
- **Baharda (Mayıs-Haziran):** Saray bahçelerindeki binlerce gül açtığında şehir tam bir imparatorluk atmosferine bürünür.

## 🏘️ Semt Rehberi
- **Innere Stadt (1. Bölge):** Şehrin tam merkezi. Şık mağazalar, tarihi kafeler ve ana katedraller burada.
- **Neubau (7. Bölge):** Sanatçıların, tasarımcıların ve butik kahvecilerin bölgesi. Modern Viyana hayatını burada gözlemlersiniz.
- **Leopoldstadt (2. Bölge):** Prater parkının olduğu, nehir kenarına yakın ve daha dinamik, çok kültürlü bölge.

## 🍽️ Ne Yenir ve İçilir?
- **Wiener Schnitzel:** Gerçek bir Viyana şinitzeli dana etinden (Kalb) yapılır ve tabağın dışına taşacak kadar büyüktür. *Figlmüller* bu konuda efsanedir.
- **Kaffeehaus Kültürü:** Kahve içmek Viyana'da bir sosyal aktivitedir. Bir fincan kahve isteyip saatlerce gazete okuyabilirsiniz; kimse sizi rahatsız etmez.
- **Sachertorte:** Dünyanın en meşhur çikolatalı pastası. Yoğun ve lezzetli; yanında şekersiz çırpılmış krema (Schlagobers) ile servis edilir.

## 🚇 Ulaşım İpuçları
- **U-Bahn:** Metro sistemi çok temiz, dakik ve güvenlidir.
- **Ringstrasse Tramvayı:** 1 ve 2 numaralı tramvaylarla şehrin etrafındaki o meşhur dairesel bulvarda tur atıp en görkemli binaları görebilirsiniz.

## 💎 Lokal Sırlar & İpuçları
- [Devlet Operası (Staatsoper)](search:Vienna State Opera): Pahalı koltuklar yerine, oyun başlamadan 80 dakika önce satılan çok ucuz "ayakta bilet"lerden (standing tickets) alıp o görkemi yaşayabilirsiniz.
- [Hundertwasserhaus](search:Hundertwasserhaus): Klasik mimariden sıkıldıysanız, bu renkli ve eğimli binayı mutlaka görün; doğayla mimarinin barışmış hali.
- **Musluk Suyu:** Viyana'nın musluk suyu doğrudan Alpler'den gelir ve dünyanın en temiz sularından biridir; boşuna para vermeyin!''';

  static const _viyanaEN = '''# Vienna Guide: Imperial Elegance & Coffee Tradition 🇦🇹

Vienna is one of Europe's most noble cities, with its grand boulevards, majestic palaces, and a world-class classical music heritage. It’s a capital where discipline meets fine art in every alleyway.

## 📅 Best Time to Visit
- **Christmas Markets (Late Nov-Dec):** Vienna is stunning during the holidays. The market in front of the City Hall (Rathaus) is like a fairy tale captured in lights.
- **Spring (May-June):** When the palace gardens bloom with thousands of roses, the city truly feels like an imperial residence.

## 🏘️ Neighborhood Guide
- **Innere Stadt (District 1):** The historic center. This is where you’ll find the luxury boutiques, the state opera, and the grand St. Stephen’s Cathedral.
- **Neubau (District 7):** The artsy soul of Vienna. Filled with independent designers, trendy coffee shops, and a cool, modern vibe.
- **Leopoldstadt (District 2):** Home to the famous Prater amusement park. A vibrant area between the city center and the Danube.

## 🍽️ Food & Dining Etiquette
- **Wiener Schnitzel:** An authentic Viennese schnitzel is made from veal (Kalb) and should be larger than the plate it's served on. *Figlmüller* is the local legend for this dish.
- **Kaffeehaus Culture:** Drinking coffee in Vienna is a serious social occupation. You can order one coffee and spend hours reading newspapers; the waitstaff will never rush you.
- **Sachertorte:** The world's most famous chocolate cake. Rich and dense, it's traditionally served with a side of unsweetened whipped cream (*Schlagobers*).

## 🚇 Transportation Tips
- **U-Bahn:** The subway system is exceptionally clean, punctual, and safe.
- **Ringstrasse Trams:** Take trams 1 or 2 for a full loop around the famous circular boulevard to see the city's most monumental architecture.

## 💎 Local Secrets & Insights
- [State Opera (Staatsoper)](search:Vienna State Opera): Instead of expensive seats, you can buy very cheap standing tickets sold about 80 minutes before each performance.
- [Hundertwasserhaus](search:Hundertwasserhaus): If you get tired of classical symmetry, visit this colorful, curvy apartment block—an artistic vision of building in harmony with nature.
- **Tap Water:** Vienna’s tap water comes directly from the Alps and is some of the cleanest in the world; don't bother buying bottled water!''';

  // BUDAPESTE
  static const _budapesteTR = '''# Budapeşte Rehberi: Tuna'nın İncisi 🇭🇺

Budapeşte; Buda'nın tarihi sükuneti ile Pest'in hareketli gece hayatının, termal hamamların ve büyüleyici Tuna manzarasının muhteşem bir birleşimidir. Avrupa'nın "ikiz" ruhlu en güzel başkentlerinden biri.

## 📅 Ne Zaman Gidilir?
- **Mayıs ve Eylül:** En keyifli sıcaklıklar, yürüyüş ve nehir turları için ideal.
- **Ağustos Başı (Sziget Festivali):** Dünyanın en büyük müzik festivallerinden biri için şehir gençlerle dolar.
- **İpucu:** Kışın çok soğuk olabilir ama termal hamamların buharı altında kar izlemek paha biçilemez bir deneyimdir.

## 🏘️ Semt Rehberi
- **I. Bölge (Kale Bölgesi):** Tarihi Buda. Balıkçı Tabyası, kalesi ve taş sokaklarıyla görkemli bir manzara sunar.
- **VII. Bölge (Yahudi Mahallesi):** Pest'in kalbi. Sokak sanatları, tasarım dükkanları ve meşhur "Yıkıntı Barlar" (Ruin Bars) burada.
- **V. Bölge (Belváros):** Parlamentonun, şık mağazaların ve lüks otellerin merkezi.

## 🍽️ Ne Yenir ve İçilir?
- **Gulaş (Gulyás):** Macar mutfağının baş tacı. Çorba kıvamında, bol paprikalı ve doyurucu.
- **Ruin Bars (Yıkıntı Barlar):** Terk edilmiş eski binaların içine kurulan, her köşesinden farklı bir objenin fırladığı bu barlar Budapeşte'nin imzasıdır. *Szimpla Kert* en meşhurudur.
- **Lángos:** Üzerine sarımsak, peynir ve krema sürülen kızarmış hamur. En sevilen sokak lezzetidir.
- **Hamam Adabı:** Széchenyi veya Gellért hamamlarına giderken yanınızda terlik ve havlu götürmeyi unutmayın; orada kiralamak oldukça pahalıdır.

## 🚇 Ulaşım İpuçları
- **Metro 1 (Sarı Hat):** Kıta Avrupası'nın en eski metrosudur; istasyonları çok nostaljik ve şıktır.
- **Tramvay 2:** Tuna Nehri kıyısı boyunca gider ve dünyanın en güzel panoramik hatlarından biri kabul edilir.
- **Yürüyüş:** Buda'dan Pest'e yürüyerek geçmek, özellikle ışıklandırılmış Zincir Köprü üzerinden, şehrin ruhunu hissettirir.

## 💎 Lokal Sırlar & İpuçları
- [Balıkçı Tabyası (Halászbástya)](search:Fisherman's Bastion): Gün doğumu veya gece gidin; manzara o kadar masalsıdır ki kendinizi bir film setinde sanabilirsiniz.
- [Margaret Adası](search:Margaret Island): Şehrin gürültüsünden kaçmak için Tuna'nın ortasındaki bu yeşil adaya sığının.
- **Market Hall:** Taze paprika, Macar salamı ve hediyelik eşya almak için büyük pazar alanına uğrayın (üst katta yerel yemekler tadılabilir).''';

  static const _budapesteEN = '''# Budapest Guide: The Pearl of the Danube 🇭🇺

Budapest is a stunning blend of the historic tranquility of Buda and the vibrant, edgy energy of Pest, famous for its grand thermal baths and the majestic Danube views. 

## 📅 Best Time to Visit
- **May and September:** The most pleasant temperatures, ideal for walking and Danube cruises.
- **Early August (Sziget Festival):** The city fills with music lovers for one of the largest and most famous festivals in the world.
- **Tip:** Winter can be bitterly cold, but watching the snow while soaking in an outdoor thermal bath is a bucket-list experience.

## 🏘️ Neighborhood Guide
- **District I (Castle District):** Historic Buda. Home to Fisherman's Bastion, the Royal Palace, and cobblestone lanes offering medieval charm.
- **District VII (Jewish Quarter):** The heart of Pest’s nightlife. A hub of street art, designer boutiques, and the world-famous "Ruin Bars."
- **District V (Belváros):** The elegant center of the city, housing the Parliament building, luxury hotels, and high-end shopping.

## 🍽️ Food & Dining Etiquette
- **Goulash (Gulyás):** The king of Hungarian cuisine. A hearty soup-stew rich in paprika and local flavors.
- **Ruin Bars:** Set in abandoned buildings and decorated with an eclectic mix of flea-market junk, these bars are iconic. *Szimpla Kert* is the original and most famous.
- **Lángos:** Fried dough topped with garlic, sour cream, and cheese—the ultimate Hungarian street food.
- **Thermal Bath Etiquette:** When visiting Széchenyi or Gellért, bring your own flip-flops and towel to avoid expensive rental fees.

## 🚇 Transportation Tips
- **Metro 1 (Yellow Line):** The oldest underground line in continental Europe. Its stations are beautifully preserved and feel like a trip back in time.
- **Tram 2:** Runs along the Pest side of the Danube and is widely considered one of the most scenic tram routes in the world.
- **Walking:** Walking from Buda to Pest across the Chain Bridge at night, when the city is fully illuminated, is an unforgettable experience.

## 💎 Local Secrets & Insights
- **Fisherman's Bastion:** Visit at sunrise or late at night. The panoramic views are so magical they feel staged for a movie.
- **Margaret Island:** A peaceful green sanctuary in the middle of the Danube, perfect for escaping the city's hustle and bustle.
- **Central Market Hall:** Head here for authentic paprika, Hungarian salami, and local crafts—check out the upstairs stalls for a quick, traditional lunch.''';

  // KOPENHAG
  static const _kopenhagTR = '''# Kopenhag Rehberi: Tasarım ve Mutluluk Başkenti 🇩🇰

Kopenhag; "Hygge" felsefesiyle ısınan evleri, dünyaca ünlü tasarım anlayışı ve bisikletli yerlileriyle dünyanın en yaşanılabilir ve huzurlu şehirlerinden biridir.

## 📅 Ne Zaman Gidilir?
- **Yaz (Haziran-Ağustos):** Günlerin neredeyse hiç batmadığı, kanalların yüzmek ve tekne turları için ideal olduğu en canlı dönem.
- **Aralık:** Tivoli Bahçeleri bir peri masalına dönüşür; Kopenhag Noel ruhunu en iyi yansıtan şehirlerden biridir.
- **İpucu:** Kopenhag pahalı bir şehirdir, bütçenizi buna göre ayarlayın!

## 🏘️ Semt Rehberi
- **Nyhavn:** Rengarenk evleriyle Kopenhag'ın kartpostallık yüzü. Turistiktir ama bir akşamüstü içeceği için vazgeçilmezdir.
- **Vesterbro:** Eskiden "kırmızı fener" bölgesi olan bu mahalle, şimdi şehrin en trend, tasarım dükkanları ve iyi restoranlarla dolu bölgesi.
- **Nørrebro:** Çok kültürlü, dinamik ve genç. Dünyanın en iyi pizzacıları ve antikacıları bu mahallededir.

## 🍽️ Ne Yenir ve İçilir?
- **Smørrebrød:** Geleneksel açık yüzlü sandviçler. Çavdar ekmeği üzerine balık, et veya sebze kombinasyonlarıyla bir sanat eseridir.
- **Pastry (Danish):** Gerçekten burada yemeniz gereken tereyağlı çıtır çörekler.
- **Bisiklet Adabı:** Bisikletliler için kurallara uymak çok ciddidir. Bisiklet yolunda durmayın ve dönerken mutlaka el işareti verin.
- **Hygge:** Arkadaşlarla mum ışığında, samimi bir ortamda vakit geçirme sanatı. Siz de bu ritme ayak uydurun.

## 🚇 Ulaşım İpuçları
- **Bisiklet Kiralamak:** Kopenhag'da otomobil bir azınlıktır. Şehri gerçek bir Kopenhaglı gibi gezmenin tek yolu iki tekerlek üstündedir.
- **Kopenhag Kart:** Müzeler ve ulaşım için oldukça karlı olabilir.

## 💎 Lokal Sırlar & İpuçları
- [Reffen](search:Reffen): Eski bir endüstriyel alanda kurulan devasa sokak yemeği pazarı. Yaz akşamlarının vazgeçilmezidir.
- [Christiania (Özgür Şehir)](search:Freetown Christiania): Kendi kuralları olan bu özerk bölgeyi ziyaret edin; graffitileri ve alternatif yaşam tarzı ile benzersizdir (fotoğraf çekme kurallarına dikkat edin!).
- **Kanalda Yüzmek:** Şehrin ortasındaki kanalların suyu tertemizdir. Yazın yerlilerle birlikte bu "havuzlara" atlayın.''';

  static const _kopenhagEN = '''# Copenhagen Guide: Capital of Design & Happiness 🇩🇰

Copenhagen is one of the most liveable cities in the world, defined by the "Hygge" philosophy, world-class design, and a sea of bicycles. It’s a place where aesthetic beauty meets effortless functionality.

## 📅 Best Time to Visit
- **Summer (June-August):** Long days where the sun barely sets, making the canals perfect for swimming and boat tours.
- **December:** Tivoli Gardens transforms into a sparkling winter wonderland; Copenhagen captures the Christmas spirit like no other.
- **Tip:** Copenhagen is expensive—be prepared for higher prices on dining and accommodation.

## 🏘️ Neighborhood Guide
- **Nyhavn:** The quintessential postcard view of Copenhagen with its colorful 17th-century townhouses. 
- **Vesterbro:** Once the red-light district, now a trendy hub filled with independent boutiques, galleries, and the city’s best nightlife.
- **Nørrebro:** Multicultural, vibrant, and young. It’s the place to find eclectic antique shops and world-class pizza.

## 🍽️ Food & Dining Etiquette
- **Smørrebrød:** Traditional open-faced sandwiches. Built on dense rye bread, these topping-loaded masterpieces are a Danish staple.
- **Danish Pastry:** You haven't truly experienced a pastry until you've had a fresh, buttery "Wienerbrød" in its homeland.
- **Cycling Etiquette:** Biking is a serious business here. Do not walk on bike lanes, keep to the right, and always signal with your hands before stopping or turning.
- **Hygge:** The Danish art of creating intimacy and coziness. Embrace the slower pace and enjoy a candlelit meal.

## 🚇 Transportation Tips
- **Rent a Bike:** In Copenhagen, cars are secondary. To explore the city like a local, you must do it on two wheels.
- **Copenhagen Card:** Offers great value if you plan to visit multiple museums and use public transport within the wider metropolitan area.

## 💎 Local Secrets & Insights
- [Reffen](search:Reffen): A massive outdoor street food market on a former industrial site. It’s the ultimate place for summer evening vibes.
- [Freetown Christiania](search:Freetown Christiania): Visit this self-governing autonomous district for its unique street art and alternative lifestyle (be sure to follow their internal rules regarding photography).
- **Canal Swimming:** The water in Copenhagen's canals is exceptionally clean. Join the locals at Harbor Bath Islands Brygge for a refreshing summer dip.''';

  // STOKHOLM
  static const _stokholmTR = '''# Stokholm Rehberi: Suyun Üstündeki Zarafet 🇸🇪

Stokholm; 14 ada üzerine yayılmış, 50'den fazla köprüyle birbirine bağlanmış, kuzeyin modernliğini ortaçağ dokusuyla harmanlayan büyüleyici bir şehirdir.

## 📅 Ne Zaman Gidilir?
- **Midsommar (Haziran Sonu):** Günlerin neredeyse hiç batmadığı, şehrin çiçeklerle dolduğu en sihirli zaman.
- **Kış (Aralık):** Karlar altındaki Gamla Stan (Eski Şehir) sokaklarında zencefilli kurabiye kokuları eşliğinde Noel pazarlarını gezmek paha biçilemez.
- **İpucu:** Kışın güneş çok erken batar (öğleden sonra 3 gibi), bu yüzden gün ışığını iyi değerlendirin.

## 🏘️ Semt Rehberi
- **Gamla Stan:** Şehrin kalbi. Renkli binaları ve dar sokaklarıyla Avrupa'nın en iyi korunmuş ortaçağ merkezlerinden biri.
- **Södermalm:** Stokholm'ün "hipster" ruhu. Tasarım dükkanları, vintage mağazalar ve şehrin en iyi manzaralarına sahip kafeler burada.
- **Östermalm:** Şık, zarif ve lüks. Geniş bulvarlar ve kaliteli restoranların merkezi.
- **Djurgården:** Müzeler adası. ABBA müzesi, Vasa müzesi ve dünyanın en eski açık hava müzesi Skansen burada yer alır.

## 🍽️ Ne Yenir ve İçilir?
- **Fika Ritüeli:** İsveç'in kahve ve mola kültürü. Sadece bir kahve molası değil, hayata kısa bir ara verme sanatıdır. Yanında mutlaka "Kanelbulle" (tarçınlı çörek) deneyin.
- **Köttbullar:** Meşhur İsveç köftesi; yanında patates püresi, yaban mersini sosu (lingonberry) ve turşu ile servis edilir.
- **Gravlax:** Dereotuyla marine edilmiş çiğ somon. Kuzey mutfağının en taze lezzetlerinden biri.
- **Kıyafet:** İsveçliler sade ama çok şık giyinir. "Lagom" (ne eksik ne fazla) felsefesi giyim tarzlarına da yansır.

## 🚇 Ulaşım İpuçları
- **Dünyanın En Uzun Sanat Galerisi:** Stokholm metrosu (Tunnelbana) istasyonları devasa sanat eserlerine ev sahipliği yapar. Mavi hat istasyonlarını mutlaka görün.
- **Feribotlar:** Toplu taşıma kartınız feribotlarda da geçerlidir. Adalar arasında deniz yoluyla seyahat etmek hem ucuz hem de manzaralıdır.

## 💎 Lokal Sırlar & İpuçları
- [Monteliusvägen](search:Monteliusvägen): Södermalm'da bulunan bu yürüyüş yolu, Gamla Stan ve belediye binasının en güzel manzarasını sunar; özellikle gün batımında unutulmazdır.
- [Rosendals Trädgård](search:Rosendals Trädgård): Djurgården'ın derinliklerinde saklı bir bahçe kafe. Kendi yetiştirdikleri ürünlerle yaptıkları yemekler ve sera atmosferi büyüleyicidir.
- **Nakit:** İsveç neredeyse tamamen nakitsiz bir toplumdur. Birçok yer "Card Only" çalışır; nakit paraya ihtiyacınız olmayacaktır.''';

  static const _stokholmEN = '''# Stockholm Guide: Elegance on the Water 🇸🇪

Stockholm is spread across 14 islands connected by over 50 bridges, seamlessly blending North European modernity with medieval charm—a city where water and forest meet urban design.

## 📅 Best Time to Visit
- **Midsommar (Late June):** The most magical time when the sun barely sets, and the city is filled with wildflowers and festivities.
- **Winter (December):** Exploring the snow-covered alleys of Gamla Stan (Old Town) with the scent of gingerbread in the air is priceless.
- **Tip:** In mid-winter, the sun sets around 3 PM. Plan your sightseeing early to make the most of the short daylight hours.

## 🏘️ Neighborhood Guide
- **Gamla Stan:** The historic heart. One of Europe's best-preserved medieval centers with colorful buildings and narrow cobblestone streets.
- **Södermalm:** The hipster soul of Stockholm. Home to creative design studios, vintage stores, and hilltop cafes with amazing views.
- **Östermalm:** Elegant, chic, and high-end. Known for its grand boulevards and some of the city's finest dining establishments.
- **Djurgården:** The museum island. Here you'll find the ABBA Museum, the 17th-century Vasa ship, and Skansen open-air museum.

## 🍽️ Food & Dining Etiquette
- **Fika Ritual:** More than just a coffee break, Fika is the Swedish art of slowing down with coffee and a treat. Pair it with a "Kanelbulle" (cinnamon bun).
- **Köttbullar:** Authentic Swedish meatballs served with creamy mashed potatoes, lingonberry jam, and pickled cucumber.
- **Gravlax:** Dill-cured Atlantic salmon—a fresh and essential staple of Nordic cuisine.
- **Dress Code:** Swedes dress simply but very stylishly. The philosophy of "Lagom" (just the right amount) is reflected in their fashion.

## 🚇 Transportation Tips
- **The World's Longest Art Gallery:** The Stockholm metro (Tunnelbana) stations are massive art installations. Don't miss the blue line stations for incredible visuals.
- **Ferries:** Your public transport card is valid on many ferries. Crossing between islands by water is both economical and offers the best perspectives of the city.

## 💎 Local Secrets & Insights
- [Monteliusvägen](search:Monteliusvägen): This walking path on Södermalm offers the single best panoramic view of Gamla Stan and the City Hall, especially stunning at sunset.
- [Rosendals Trädgård](search:Rosendals Trädgård): A hidden garden cafe in the middle of Djurgården island, where food is prepared with ingredients grown on-site in a greenhouse setting.
- **Cashless Society:** Sweden is almost entirely cashless. Most places are "Card Only," so don't worry about carrying physical currency.''';

  // ZURIH
  static const _zurihTR = '''# Zürih Rehberi: Alp Zirveleri ve Göl Kıyısında Lüks 🇨🇭

Zürih; dünyanın finans başkentlerinden biri olmasının yanı sıra, tertemiz gölü, nehir kenarı kafeleri ve arkasındaki Alp manzarasıyla hayat kalitesinin zirvesidir.

## 📅 Ne Zaman Gidilir?
- **Yaz (Temmuz-Ağustos):** Göl kıyısındaki "Badi"lerin (açık hava havuzları) dolduğu, nehirde yüzüldüğü ve havanın en güzel olduğu dönem.
- **Kış:** Alpler'e kayak turu yapmak için en iyi başlangıç noktası; ayrıca şehrin Noel ışıkları dünyaca meşhurdur.

## 🏘️ Semt Rehberi
- **Altstadt (Eski Şehir):** Nehrin iki yakasına yayılmış, Arnavut kaldırımlı sokaklar ve tarihi Lonca (Guild) binaları.
- **Zürih West:** Eskiden sanayi bölgesi olan bu mahalle, şimdi sanat galerileri, tasarım mağazaları ve dikey bahçeleriyle şehrin en modern yüzü.
- **Enge:** Göl kenarında, daha sakin ve lüks konutların olduğu yeşil bir bölge.

## 🍽️ Ne Yenir ve İçilir?
- **Fondü:** Peynir tutkunları için bir zorunluluk. Genelde ekmekle bandırılarak yenir.
- **Zürcher Geschnetzeltes:** Krema ve mantar soslu ince dilimlenmiş dana eti; yanında çıtır "Rösti" (patates mücveri) ile servis edilir.
- **Çikolata:** *Sprüngli* veya *Läderach* gibi dükkanlarda el yapımı İsviçre çikolatalarının tadına bakın.
- **Dakiklik:** İsviçre'de 5 dakika gecikmek bile kaba bir hareket kabul edilebilir. Randevularınıza tam zamanında gidin.

## 🚇 Ulaşım İpuçları
- **Tramvaylar:** Şehrin her köşesine ulaşan, sessiz ve inanılmaz dakik tramvay ağı.
- **Zürih Kart:** Müzeler ve tüm ulaşım için büyük kolaylık sağlar.
- **Tekne turları:** Gölde kısa bir tur yapmak şehrin siluetini görmek için en iyi yoldur.

## 💎 Lokal Sırlar & İpuçları
- [Lindenhof](search:Lindenhof): Eski şehirde, nehir ve katedrallere karşı oturup dinlenmek için en huzurlu tepe noktası.
- [Thermalbad & Spa Zurich](search:Thermalbad & Spa Zurich): Eski bir bira fabrikasının içinde yer alan bu spa, özellikle çatısındaki açık havuzuyla şehre tepeden bakarken dinlenme imkanı sunar.
- **Musluk Suyu:** Şehrin her yerindeki fıskiyelerden akan su içilebilir ve Alp tazeliğindedir.''';

  static const _zurihEN = '''# Zurich Guide: Alpine Peaks & Lakeside Luxury 🇨🇭

Zurich is not just a global financial hub; it's a city of pristine waters, riverside cafes, and incredible mountain views, consistently ranking as one of the best places to live.

## 📅 Best Time to Visit
- **Summer (July-August):** When the "Badis" (open-air pools) by the lake are full, people are swimming in the Limmat river, and the weather is at its peak.
- **Winter:** The perfect gateway for ski trips to the Alps, accompanied by world-famous Christmas illuminations throughout the city center.

## 🏘️ Neighborhood Guide
- **Altstadt (Old Town):** Spread across both sides of the river, featuring medieval houses, cobbled streets, and historic Guild halls.
- **Zurich West:** Once industrial, now a trendsetting district with art galleries, designer labels, and industrial spaces turned into bars and gardens.
- **Enge:** A peaceful, green lakeside district with elegant architecture and beautiful parks.

## 🍽️ Food & Dining Etiquette
- **Cheese Fondue:** An absolute ritual for cheese lovers. Traditionally eaten by dipping bread into a communal pot.
- **Zürcher Geschnetzeltes:** Sliced veal in a creamy mushroom sauce, served with a crispy "Rösti" (Swiss potato pancake).
- **Chocolate:** Don't miss artisanal Swiss chocolates at legendary shops like *Sprüngli* or *Läderach*.
- **Punctuality:** In Switzerland, being even 5 minutes late is often considered rude. Always aim to be exactly on time.

## 🚇 Transportation Tips
- **The Trams:** Silent, incredibly punctual, and cover every corner of the city.
- **Zurich Card:** Highly recommended for unlimited travel and free or discounted museum entries.
- **Lake Boats:** A short cruise on Lake Zurich is the best way to see the city's skyline against the mountains.

## 💎 Local Secrets & Insights
- [Lindenhof](search:Lindenhof): A quiet hilltop in the old town providing a beautiful panorama of the river and the iconic twin towers of Grossmünster.
- [Thermalbad & Spa Zurich](search:Thermalbad & Spa Zurich): Built inside an old brewery, its rooftop pool offers a unique opportunity to soak in thermal waters with a view over the city.
- **Free Water:** The fountains scattered across the city flow with drinkable, cold Alpine water—bring a reusable bottle!''';

  // CENEVRE
  static const _cenevreTR = '''# Cenevre Rehberi: Diplomasi, Saatler ve Alp Esintisi 🇨🇭

Cenevre; Alpler'in ortasında, devasa bir gölün kenarında yer alan, çok dilli ve son derece kozmopolit bir Diplomasi merkezidir. Zarafetin ve düzenin başkentidir.

## 📅 Ne Zaman Gidilir?
- **Yaz:** Göl kenarında yürüyüşler ve açık hava festivalleri için ideal. "Bains des Pâquis"te göle girmek bir Cenevre geleneğidir.
- **Kış:** Yakındaki kayak merkezlerine gitmek için harika bir üs.

## 🏘️ Semt Rehberi
- **Vieille Ville (Eski Şehir):** Şehrin en yüksek noktasında, antikacılar ve taş binalarla dolu tarihi merkez.
- **Pâquis:** Kozmopolit, hareketli ve çok çeşitli restoran alternatifleri sunar.
- **Carouge:** Cenevre'nin içinde bir "Akdeniz" kasabası gibi; daha bohem ve sanatçı dolu bir mahalle.

## 🍽️ Ne Yenir ve İçilir?
- **Fondü:** Peynirin en iyi halini burada tadın.
- **Filets de Perche:** Cenevre Gölü'nden taze tutulan tatlı su balığı; yanındaki tereyağlı sosuyla meşhurdur.
- **Saat Kültürü:** Burası mekanik saatçiliğin kalbi. Dünyanın en iyi markalarının mağazalarını "Rue du Rhône"da görebilirsiniz.

## 🚇 Ulaşım İpuçları
- **Ücretsiz Ulaşım:** Cenevre'de bir otelde kalıyorsanız, size tüm toplu taşımada kullanabileceğiniz ücretsiz bir "Geneva Transport Card" verilecektir.
- **Mouettes:** Gölün iki yakası arasında ulaşım sağlayan küçük sarı tekneler; hem keyifli hem de hızlıdır.

## 💎 Lokal Sırlar & İpuçları
- [Jet d'Eau](search:Jet d'Eau): Şehrin sembolü olan bu dev fıskıye rüzgarlı havalarda kapatılır. Akşamları ışıklandırıldığında çok daha etkileyicidir.
- [CERN](search:CERN (Globe of Science)): Bilim meraklıları için dünyanın en büyük parçacık fiziği laboratuvarı şehir merkezine tramvayla sadece 20 dakika uzaklıktadır; turlar için aylar öncesinden rezervasyon yapın.''';

  static const _cenevreEN = '''# Geneva Guide: Diplomacy, Watches & Alpine Charm 🇨🇭

Geneva is a multilingual, highly cosmopolitan hub of diplomacy situated on the shores of one of Europe's largest lakes, framed by the breathtaking peaks of the Alps.

## 📅 Best Time to Visit
- **Summer:** Perfect for lakeside strolls and outdoor festivals. Joining locals for a swim at "Bains des Pâquis" is a summer essential.
- **Winter:** Serving as a refined gateway to some of the world's most famous ski resorts.

## 🏘️ Neighborhood Guide
- **Vieille Ville (Old Town):** Perched on a hill, it’s filled with antique shops, cozy cafes, and cobblestone lanes leading to the cathedral.
- **Pâquis:** A diverse, bustling district known for its international vibe and great value-for-money dining options.
- **Carouge:** Often called the "Greenwich Village" of Geneva; a bohemian area with Mediterranean-style architecture and artisanal workshops.

## 🍽️ Food & Dining Etiquette
- **Cheese Fondue:** An unmissable local staple, best enjoyed in the rustic setting of an old town bistro.
- **Filets de Perche:** Freshly caught lake perch, typically served with a delicate lemon butter sauce and crispy fries.
- **Horology:** The city is the spiritual heart of watchmaking. High-end boutiques of the world's most prestigious brands line the "Rue du Rhône."

## 🚇 Transportation Tips
- **Free Transport:** If you are staying in a hotel, hostel, or campsite, you are entitled to a free "Geneva Transport Card" for unlimited public transit.
- **Mouettes:** These small yellow water taxis are the most charming way to cross the lake and are included in the local transport network.

## 💎 Local Secrets & Insights
- [Jet d'Eau](search:Jet d'Eau): The city's 140-meter-high water fountain. Note that it's turned off in high winds and is most beautiful when illuminated at night.
- [CERN](search:CERN (Globe of Science)): Science enthusiasts shouldn't miss the world's largest particle physics lab, just a 20-minute tram ride from the center. (Book tours well in advance!).''';

  // LUCERNE
  static const _lucerneTR = '''# Lucerne Rehberi: Kartpostallık Bir İsviçre Masalı 🇨🇭

Lucerne (Luzern); karlarla örtülü Alpler'in ve masmavi bir gölün kıyısında yer alan, tarihi ahşap köprüleriyle ünlü, İsviçre'nin kalbi sayılan bir şehirdir.

## 📅 Ne Zaman Gidilir?
- **Bahar ve Yaz:** Göl turları ve dağ tırmanışları için en uygun zaman.
- **Kış:** Şehrin etrafındaki kayak merkezleri ve ışıl ışıl Noel atmosferi için tercih edilir.

## 🏘️ Semt Rehberi
- **Old Town (Altstadt):** Duvarları resimli tarihi binalar, dar sokaklar ve butik dükkanlar.
- **Lakeside:** Şık otellerin ve göl manzarasının tadını çıkaracağınız sahil şeridi.

## 🍽️ Ne Yenir ve İçilir?
- **Luzerner Chügelipastete:** Lucerne'e özgü, içi etli ve kremalı soslu milföy böreği.
- **Çikolata Tadımı:** *Max Felchlin* veya *Bachmann* gibi yerel markaları deneyin.
- **Sessizlik:** Pazar günleri çoğu dükkan kapalıdır ve şehirde genel bir sessizlik hakimdir; bu tempoya ayak uydurun.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Şehir merkezi küçüktür ve tamamen yürüyerek keşfedilebilir.
- **Göl Feribotları:** Lucerne Gölü'nde (Vierwaldstättersee) eski tip buharlı gemilerle bir tur yapmadan dönmeyin.

## 💎 Lokal Sırlar & İpuçları
- [Kapellbrücke (Şapel Köprüsü)](search:Chapel Bridge): Dünyanın en eski ahşap köprülerinden biridir. Sabah çok erken giderseniz turist kalabalığı olmadan fotoğraflayabilirsiniz.
- [Mt. Pilatus](search:Mount Pilatus): Dünyanın en dik dişli treniyle dağın zirvesine çıkın; manzara sizi büyüleyecektir.
- [Lion Monument](search:Lion Monument): Mark Twain'in "dünyanın en hüzünlü ve etkileyici taş parçası" olarak tanımladığı bu anıtı mutlaka görün.''';

  static const _lucerneEN = '''# Lucerne Guide: A Postcard-Perfect Swiss Fairytale 🇨🇭

Lucerne (Luzern) is the literal heart of Switzerland, famous for its historic covered wooden bridges and its stunning location beside a crystal-clear lake surrounded by Alpine peaks.

## 📅 Best Time to Visit
- **Spring & Summer:** The ideal time for scenic lake cruises and excursions to the surrounding mountains like Rigi or Pilatus.
- **Winter:** Great for combining a city visit with nearby skiing, and for experiencing the traditional Swiss Christmas markets.

## 🏘️ Neighborhood Guide
- **Old Town (Altstadt):** A pedestrian-only zone filled with medieval houses painted with colorful frescoes and charming boutiques.
- **Lakeside Promenade:** Lined with grand hotels and offering unparalleled views across the water to the mountains.

## 🍽️ Food & Dining Etiquette
- **Luzerner Chügelipastete:** A traditional local specialty—a puff pastry shell filled with a rich, creamy veal and mushroom sauce.
- **Chocolate & Pastry:** Visit local favorites like *Bachmann* or seek out artisanal Swiss chocolate workshops near the center.
- **Sunday Rest:** Most shops are closed on Sundays, and the city takes on a peaceful, slow-paced atmosphere.

## 🚇 Transportation Tips
- **Walking:** The city center is compact and best explored on foot.
- **Steamers:** A boat trip on Lake Lucerne (Vierwaldstättersee) using the historic paddlewheel steamers is an essential Lucerne experience.

## 💎 Local Secrets & Insights
- [Kapellbrücke (Chapel Bridge)](search:Chapel Bridge): One of the world's oldest covered bridges. Arrive early at dawn for the best photos without the tourist crowds.
- [Mt. Pilatus](search:Mount Pilatus): Take the world's steepest cogwheel railway to the summit for a 360-degree view that will leave you speechless.
- [Lion Monument](search:Lion Monument): Described by Mark Twain as "the most mournful and moving piece of stone in the world"—visit it early to appreciate the quiet solemnity.''';

  // LYON
  static const _lyonTR = '''# Lyon Rehberi: Lezzet ve Işığın Başkenti 🇫🇷

Lyon; Fransa'nın gastronomi kalbi, iki nehrin buluştuğu nokta ve gizli geçitleriyle (traboules) ünlü, tarih ve moderni harmanlayan zarif bir şehirdir.

## 📅 Ne Zaman Gidilir?
- **Fête des Lumières (Aralık Başı):** Şehrin devasa bir ışık gösterisine dönüştüğü, dünyaca ünlü Işık Festivali dönemi.
- **Bahar ve Güz:** Nehir kenarlarında yürüyüş yapmak ve dışarıda yemek yemek için en güzel havalar.

## 🏘️ Semt Rehberi
- **Vieux Lyon:** Rönesans döneminden kalma binaları ve dar sokaklarıyla UNESCO korumasındaki eski şehir.
- **Presqu'île:** Mağazaların, operanın ve belediye binasının olduğu şehrin hareketli ticari merkezi.
- **Croix-Rousse:** Eski ipek işçilerinin mahallesi; şimdi sokak sanatçıları ve bohem bir atmosferin merkezi.

## 🍽️ Ne Yenir ve İçilir?
- **Bouchons:** Lyon'a özgü geleneksel restoranlar. Yerel lezzetleri tatmak için "Bouchon Lyonnais" sertifikalı olanları seçin.
- **Quenelles:** Balık veya etle yapılan, kremsi soslu Lyon usulü köfteler.
- **Praline Tart:** Pembe şekerli bademlerle yapılan bu meşhur tatlıyı mutlaka deneyin.

## 🚇 Ulaşım İpuçları
- **Velo'v:** Lyon'un harika bisiklet paylaşım sistemiyle nehir kenarında tur atın.
- **Füniküler:** "Ficelle" denilen fünikülerle Fourvière Tepesi'ne kolayca çıkabilirsiniz.

## 💎 Lokal Sırlar & İpuçları
- [Traboules](search:Vieux Lyon): Binaların içinden geçen bu gizli geçitleri keşfedin (özellikle Vieux Lyon ve Croix-Rousse'da). İpek işçilerinin kumaşları yağmurdan korumak için kullandığı yollardır.
- [Les Halles de Lyon Paul Bocuse](search:Les Halles de Lyon Paul Bocuse): Şehrin dev kapalı gurme pazarı. Dünyanın en iyi peynirlerini ve şaraplarını burada tadabilirsiniz.''';

  static const _lyonEN = '''# Lyon Guide: The Capital of Flavors & Light 🇫🇷

Lyon is the gastronomic heart of France, famously situated at the confluence of two rivers and known for its "traboules" (hidden passages) that connect its historic streets.

## 📅 Best Time to Visit
- **Fête des Lumières (Early December):** The world-renowned Festival of Lights, when the entire city becomes a canvas for spectacular light installations.
- **Spring & Autumn:** The best seasons for strolling along the riverbanks and enjoying outdoor dining in a traditional bouchon.

## 🏘️ Neighborhood Guide
- **Vieux Lyon:** One of the world's largest Renaissance neighborhoods, filled with secret inner courtyards and atmospheric stairs.
- **Presqu'île:** The city’s vibrant shopping and cultural core, located on the peninsula between the Rhône and Saône rivers.
- **Croix-Rousse:** Known as "the hill that works," this historic silk-weaving district is now a bohemian hub for artists and creative studios.

## 🍽️ Food & Dining Etiquette
- **Bouchons:** Traditional Lyonnais bistros with a warm, lively atmosphere. Look for the "Bouchon Lyonnais" seal to ensure authenticity.
- **Quenelles:** A local specialty made of cream and poached fish or meat, typically served with a rich Nantua sauce.
- **Tarte aux Pralines:** Don't leave without trying this bright pink almond tart, a signature dessert of the city.

## 🚇 Transportation Tips
- **Velo'v:** Use Lyon's extensive and easy-to-use bike-share system to cruise along the modern promenades of the Rhône river.
- **The Funicular:** Known by locals as "La Ficelle," it takes you up to Fourvière hill for the best panoramic views.

## 💎 Local Secrets & Insights
- [The Traboules](search:Vieux Lyon): These secret passages allowed silk workers to transport fabrics without exposing them to rain. Many are open to the public during the day.
- [Les Halles de Lyon Paul Bocuse](search:Les Halles de Lyon Paul Bocuse): A massive indoor food market named after the legendary chef. It's a paradise for cheese, wine, and gourmet deli lovers.''';

  // MARSILYA
  static const _marsilyaTR = '''# Marsilya Rehberi: Akdeniz'in Vahşi ve Renkli Yüzü 🇫🇷

Marsilya; kaotik, güneşe boğulmuş, çok kültürlü ve son derece samimi bir liman şehridir. Fransa'nın en eski şehri, her sokağında farklı bir hikaye barındırır.

## 📅 Ne Zaman Gidilir?
- **Bahar ve Güz:** Hava ılıktır, rüzgar (Mistral) daha azdır ve gezmek keyiflidir.
- **Yaz:** Plajlar için harika ama şehir merkezi çok sıcak olabilir.

## 🏘️ Semt Rehberi
- **Le Panier:** Rengarenk duvarları, balkonlarından sarkan çamaşırları ve sanat galerileriyle Marsilya'nın en eski ve fotojenik mahallesi.
- **Vieux-Port:** Şehrin kalbi; balık pazarı, dev aynalı tavanı ve liman atmosferiyle her zaman canlı.
- **Vallon des Auffes:** Şehrin ortasında gizli kalmış, küçük balıkçı tekneleriyle dolu bir liman köyü hissi veren koy.

## 🍽️ Ne Yenir ve İçilir?
- **Bouillabaisse:** Marsilya'nın dünyaca ünlü balık çorbası. Gerçeği pahalıdır ve özel bir seremoniyle servis edilir.
- **Pastis:** Akdeniz güneşinin altında, bir kadeh anasonlu "Pastis" içmeden Marsilya deneyimi tamamlanmış sayılmaz.
- **Sabun (Savon de Marseille):** El yapımı geleneksel Marsilya sabunlarından almayı unutmayın.

## 🚇 Ulaşım İpuçları
- **Metro ve Tramvay:** Şehri gezmek için pratik bir yol.
- **Feribot:** Vieux-Port'tan karşı kıyıya veya Frioul adalarına giden feribotlar harika manzaralar sunar.

## 💎 Lokal Sırlar & İpuçları
- [Les Calanques](search:Calanques National Park): Şehir merkezinden kısa bir otobüs veya tekne yolculuğuyla ulaşılan bu masmavi fiyortlarda yüzmek unutulmaz bir deneyimdir.
- [Cours Julien](search:Cours Julien): Alternatif bir ruh arıyorsanız, grafiti dolu sokakları ve canlı gece hayatıyla bu bölge tam size göre.
- **Güvenlik:** Her büyük liman şehri gibi Marsilya'da da özellikle kalabalık yerlerde eşyalarınıza dikkat edin ve ıssız sokaklardan kaçının.''';

  static const _marsilyaEN = '''# Marseille Guide: The Wild & Colorful Heart of the Med 🇫🇷

Marseille is a sun-drenched, multicultural, and raw port city. As France's oldest city, it offers a gritty yet sincere atmosphere where history meets a vibrant, modern edge.

## 📅 Best Time to Visit
- **Spring & Autumn:** The weather is mild, the strong Mistral winds are less frequent, and its perfect for exploring the streets.
- **Summer:** Great for boat trips and swimming, though the city center can get intensely hot.

## Neighborhood Guide
- **Le Panier:** The oldest district, filled with narrow steep streets, colorful wall art, and cozy artisan workshops.
- **Vieux-Port:** The bustling heart of the city—visit the morning fish market or walk under the giant mirrored "Ombrière."
- **Vallon des Auffes:** A hidden gem of a fishing harbor nestled under the corniche, feeling like a tiny village inside the city.

## 🍽️ Food & Dining Etiquette
- **Bouillabaisse:** Marseille's world-famous fish stew. The authentic version involves a specific ritual and multiple types of fish—expect to pay a premium for the real deal.
- **Pastis:** No Marseille experience is complete without sipping a glass of this anise-flavored liqueur as the sun goes down.
- **Savon de Marseille:** Don't forget to buy some traditional, handmade soaps from one of the historic soap makers in the center.

## 🚇 Transportation Tips
- **Metro & Trams:** Reliable and the best way to move between the center and the trendy hills.
- **Ferry Boats:** Take the small ferry across the Old Port or catch a larger boat to the historic Frioul Islands and the Château d'If.

## 💎 Local Secrets & Insights
- [The Calanques](search:Calanques National Park): These stunning limestone sea inlets with turquoise water are just a bus or boat ride away. Ideal for hiking and swimming.
- [Cours Julien](search:Cours Julien): If you’re looking for an alternative vibe, this is the center of Marseille’s street art scene, filled with bars and indie bookstores.
- **Safety Specifics:** Like any major port city, stay aware of your surroundings in crowded tourist areas and keep an eye on your belongings.''';

  // NICE
  static const _niceTR = '''# Nice Rehberi: Fransız Rivierası'nın Işıl Işıl Başkenti 🇫🇷

Nice; Côte d'Azur'un kalbinde, çakıllı plajları, masmavi denizi ve İtalyan esintili sokaklarıyla zarafetin ve güneşin şehridir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Mayıs-Haziran):** Hava mükemmeldir, çiçekler açmıştır ve henüz devasa yaz kalabalığı gelmemiştir.
- **Şubat (Nice Karnavalı):** Avrupa'nın en eski ve en büyük karnavallarından biriyle şehir rengarenk olur.
- **İpucu:** Yazın (Temmuz-Ağustos) plajlar ve oteller çok pahalı ve aşırı dolu olabilir.

## 🏘️ Semt Rehberi
- **Vieux Nice (Eski Şehir):** Daracık sokaklar, sarı binalar ve meşhur pazar yeri Cours Saleya burada yer alır.
- **Promenade des Anglais:** Şehrin sembolü olan devasa sahil şeridi. Yürüyüş veya paten için ideal.
- **Cimiez:** Roma kalıntıları, Marc Chagall ve Matisse müzelerinin olduğu daha tepede ve elit bir bölge.
- **Port Lympia:** Şık yatların ve popüler barların olduğu, yerel halkın sosyalleşmeyi sevdiği liman bölgesi.

## 🍽️ Ne Yenir ve İçilir?
- **Socca:** Nohut unundan yapılan, Nice'e özgü fırınlanmış bir çeşit krep. Sıcak ve karabiberli yenir.
- **Salade Niçoise:** Dünya markası olan bu salata burada en taze haliyle servis edilir.
- **Pissaladière:** Soğanlı ve ançüezli Nice usulü bir tart/pizza.
- **Rosé Şarap:** Provence bölgesinin meşhur roze şarapları öğle yemeklerinin olmazsa olmazıdır.

## 🚇 Ulaşım İpuçları
- **Tramvay Line 2:** Havaalanından şehir merkezine ulaşım için en hızlı ve ekonomik yoldur.
- **Trenler (TER):** Nice, Riviera'daki diğer şehirleri gezmek için mükemmel bir merkezdir. Sadece 20-30 dakikada Monaco veya Cannes'a gidebilirsiniz.

## 💎 Lokal Sırlar & İpuçları
- [Colline du Château (Kale Tepesi)](search:Castle Hill Nice): Şehrin ve denizin o meşhur manzarasını görmek için buraya mutlaka çıkın (Asansör ücretsizdir).
- [Cours Saleya](search:Cours Saleya): Gündüz çiçek pazarı, akşam ise dev açık hava restoranına dönüşen bu meydanın atmosferi büyüleyicidir.
- [Villefranche-sur-Mer](search:Villefranche-sur-Mer): Sadece bir durak ötedeki bu küçük koy, çok daha sakin bir plaj ve büyüleyici bir balıkçı kasabası atmosferi sunar.''';

  static const _niceEN = '''# Nice Guide: The Radiant Capital of the French Riviera 🇫🇷

Nice is the heart of the Côte d'Azur, a city of pebbles and blue shutters, where French elegance meets Italian soul under a relentless Mediterranean sun.

## 📅 Best Time to Visit
- **Spring (May-June):** Perfect temperatures, blooming flowers, and the absence of the overwhelming summer peaks.
- **February (Nice Carnival):** One of the world's oldest and major carnival events transforms the city into a theater of flowers and lights.
- **Tip:** July and August are peak season; expect high prices and very crowded beaches.

## 🏘️ Neighborhood Guide
- **Vieux Nice (Old Town):** A maze of narrow alleys, pastel-colored buildings, and traditional markets like Cours Saleya.
- **Promenade des Anglais:** The iconic 7km seafront walkway—the perfect spot for a sunrise stroll or a bicycle ride.
- **Cimiez:** A hilly district home to Roman ruins, the Matisse Museum, and peaceful olive groves.
- **Port Lympia:** The trendy harbor area where historic fishing boats dock next to luxury yachts, surrounded by great bars.

## 🍽️ Food & Dining Etiquette
- **Socca:** A chickpea flour pancake that is the soul of Nice's street food. Best enjoyed hot from the wood-fire oven.
- **Salade Niçoise:** The local legend. Ensure you try an authentic version with fresh local produce.
- **Pissaladière:** A thick, savory tart topped with caramelized onions, anchovies, and olives.
- **Rosé Wine:** Crisp, cold Provence Rosé is the drink of choice for almost any meal on the Riviera.

## 🚇 Transportation Tips
- **Tramway Line 2:** The fastest and most efficient way to get from the airport to the city center for just a few Euros.
- **Regional Trains (TER):** Nice is a brilliant hub. Monaco, Cannes, and Antibes are all within a 30-minute train ride along the coast.

## 💎 Local Secrets & Insights
- [Castle Hill (Colline du Château)](search:Castle Hill Nice): Climb up (or take the free elevator) for the most famous panorama of the Bay of Angels.
- [Cours Saleya](search:Cours Saleya): A vibrant flower and produce market by day that turns into a massive outdoor dining space at night.
- [Villefranche-sur-Mer](search:Villefranche-sur-Mer): Just one train stop away, this bay offers a sandier beach and a much more peaceful, picturesque fishing village vibe.''';

  // MARAKES
  static const _marakesTR = '''# Marakeş Rehberi: Baharat, Saraylar ve Çöl Ruhu 🇲🇦

Marakeş; kırmızı duvarları, labirent gibi çarşıları ve bitmek bilmeyen enerjisiyle duyuları uyandıran, "Kızıl Şehir" olarak anılan büyüleyici bir vaha şehridir.

## 📅 Ne Zaman Gidilir?
- **Bahar (Mart-Mayıs) ve Güz (Ekim-Kasım):** Sıcaklıklar gezmek için en ideal düzeydedir.
- **Yaz:** Temmuz ve Ağustos aylarında sıcaklık 45 dereceyi aşabilir, bu dönemden kaçınmakta fayda var.
- **İpucu:** Ramazan ayı boyunca yaşam ritmi değişir; akşamları çok canlıdır ama gündüzleri birçok yer kapalı olabilir.

## 🏘️ Semt Rehberi
- **Medina (Eski Şehir):** Şehrin kalbi; pazarlar (souks), tarihi yapılar ve geleneksel avlulu evler (Riad) burada bulunur.
- **Gueliz:** Marakeş'in modern yüzü. Şık galeriler, Fransız tarzı kafeler ve markalarla dolu bir bölge.
- **Hivernage:** Lüks otellerin ve en iyi gece hayatı mekanlarının bulunduğu modern semt.

## 🍽️ Ne Yenir ve İçilir?
- **Tagine:** Koni şeklindeki toprak kaplarda yavaş pişen, et ve sebze yemeği.
- **Nane Çayı (Berber Whiskey):** Fas misafirperverliğinin sembolü. Bol şekerli ve yüksekten doldurularak servis edilir.
- **Pazarlık:** Pazarlarda fiyat sormak bir oyunun başlangıcıdır. İlk söylenen fiyatın yarısını teklif etmek normal karşılanır.
- **Kıyafet:** Saygılı olun; çok açık kıyafetlerden kaçınmak, özellikle dini alanlarda önemlidir.

## 🚇 Ulaşım İpuçları
- **Yürüyüş:** Medina sadece yürüyerek keşfedilebilir ama kaybolmaya hazır olun!
- **Petit Taxi:** Şehir içi kısa mesafeler için ekonomik ve pratik olan bu küçük arabaları kullanın (mutlaka taksimetre açtırın).

## 💎 Lokal Sırlar & İpuçları
- [Majorelle Bahçesi](search:Jardin Majorelle): Yves Saint Laurent'ın şehre mirası olan bu masmavi bahçeyi mutlaka sabah erken saatlerde ziyaret edin.
- [Bahia Sarayı](search:Bahia Palace): Fas mimarisinin ve çini sanatının en güzel örneklerini burada görebilirsiniz.
- [Jemaa el-Fna](search:Jemaa el-Fna): Güneş battığında bu meydan dev bir açık hava mutfağına ve gösteri alanına dönüşür; bir teras kafesinden izlemek harikadır.''';

  static const _marakesEN = '''# Marrakech Guide: Spices, Palaces & Desert Soul 🇲🇦

Marrakech, known as the "Red City," is a sensory feast of intricate architecture, bustling souks, and vibrant colors—a true oasis that stays in the heart forever.

## 📅 Best Time to Visit
- **Spring (March-May) & Autumn (October-November):** The most pleasant temperatures for exploring the city and the nearby desert.
- **Summer:** Be warned, July and August can see temperatures soaring above 45°C (113°F).
- **Tip:** Visiting during Ramadan offers a unique spiritual atmosphere, but be aware that daytime schedules for shops and cafes may change.

## 🏘️ Neighborhood Guide
- **Medina (Old City):** The historic core. A labyrinth of markets (souks), stunning palaces, and traditional courtyard houses (Riads).
- **Gueliz:** The modern French-inspired district filled with contemporary art galleries, chic cafes, and high-street shopping.
- **Hivernage:** The upscale modern quarter, home to luxury international hotels and the city's best nightlife.

## 🍽️ Food & Dining Etiquette
- **Tagine:** Slow-cooked stews named after the conical clay pot they are cooked in. An absolute staple of Moroccan cuisine.
- **Mint Tea (Berber Whiskey):** The symbol of Moroccan hospitality, served hot, sweet, and poured from a height to create foam.
- **Bargaining:** In the souks, haggling is expected and considered a social interaction. Aim to start at about half the initial asking price.
- **Dress Code:** To show respect for local customs, it's recommended to dress modestly, especially when away from the modern hotel pool areas.

## 🚇 Transportation Tips
- **Walking:** The only way to navigate the deep Medina alleys. Use offline maps as signal can be spotty.
- **Petit Taxis:** Small brown cars for city transfers. They are inexpensive, but always insist on using the meter (the "compteur").

## 💎 Local Secrets & Insights
- [Jardin Majorelle](search:Jardin Majorelle): The famous cobalt-blue garden owned by Yves Saint Laurent. Buy tickets online in advance to avoid long queues.
- [Bahia Palace](search:Bahia Palace): A 19th-century masterpiece showing the very best of Islamic architecture and Moroccan mosaics (zellij).
- **[Jemaa el-Fna](search:Jemaa el-Fna) at Night:** As dusk falls, the main square transforms into a massive open-air grill. Watch the chaos from a safe distance at a rooftop cafe.''';

  // DUBAI
  static const _dubaiTR = '''# Dubai Rehberi: Çölün Ortasında Bir Gelecek Vizyonu 🇦🇪

Dubai; imkansızın mümkün kılındığı, dünyanın en yüksek binalarının, lüksün ve sınırsız eğlencenin çöl kumlarıyla buluştuğu bir modern çağ mucizesidir.

## 📅 Ne Zaman Gidilir?
- **Kış (Altın Sezon - Kasım'dan Mart'a):** Hava mükemmeldir. Plaj, safari ve açık hava etkinlikleri için en iyi zaman.
- **Yaz:** Sıcaklık 50 dereceye yaklaşabilir. Sadece kapalı alanlar ve dev alışveriş merkezleri için uygundur.

## 🏘️ Semt Rehberi
- **Downtown Dubai:** Burj Khalifa ve Dubai Mall'un olduğu, şehrin kalbi ve gösterişin merkezi.
- **Dubai Marina:** Gökdelenler arasında yürüyüş yolları, şık yatlar ve plaj keyfi için en iyi bölge.
- **Old Dubai (Deira & Bur Dubai):** Şehrin kökleri. Altın ve Baharat çarşılarının olduğu, geleneksel hayatın sürdüğü bölge.
- **Palm Jumeirah:** Dünyanın en büyük yapay adası; lüks oteller ve tatil köyü atmosferi.

## 🍽️ Ne Yenir ve İçilir?
- **Uluslararası Mutfak:** Dubai'de dünyanın her yerinden en iyi şeflerin restoranlarını bulabilirsiniz.
- **Geleneksel Tatlar:** Humus, Manousheh ve Luqaimat (şerbetli tatlı) mutlaka denenmeli.
- **Adab-ı Muaşeret:** Halka açık yerlerde sevgi gösterilerinde aşırıya kaçmamak ve yerel kültüre saygılı giyinmek önemlidir. Alkol sadece lisanslı mekanlarda (oteller, barlar) tüketilebilir.

## 🚇 Ulaşım İpuçları
- **Dubai Metrosu:** Sürücüsüz, son derece modern ve temiz. "Gold Class" vagonuyla en önden şehir manzarasını izleyebilirsiniz.
- **Taksiler ve Careem:** Taksiler nispeten ucuzdur. Careem (yerel Uber) ulaşım için çok yaygındır.

## 💎 Lokal Sırlar & İpuçları
- **Abra Yolculuğu:** [Dubai Creek](search:Dubai Creek)'te karşıdan karşıya geçmek için kullanılan geleneksel tekneler sadece 1-2 Dirhem'dir; en ucuz ve keyifli deneyimdir.
- [Al Qudra Gölleri](search:Al Qudra Lakes): Şehir merkezinden uzakta, çölde yıldızları izlemek ve gün batımı pikniği yapmak için yerlilerin tercihidir.
- **[Burj Khalifa](search:Burj Khalifa) İpucu:** Manzara için biletinizi haftalar öncesinden online alın; gün batımı saatleri en popüler olanlardır.''';

  static const _dubaiEN = '''# Dubai Guide: A Vision of the Future in the Desert 🇦🇪

Dubai is a modern marvel where the impossible becomes possible—a city of record-breaking skyscrapers, unparalleled luxury, and boundless entertainment where desert sands meet the sea.

## 📅 Best Time to Visit
- **Winter (The Golden Season - Nov to March):** The pleasant weather makes it ideal for the beach, desert safaris, and outdoor festivals.
- **Summer:** Extreme heat (often 45°C+) means life moves entirely indoors to the massive, air-conditioned malls and attractions.

## 🏘️ Neighborhood Guide
- **Downtown Dubai:** The heart of the city, home to the Burj Khalifa, the Dubai Fountain, and the world's largest mall.
- **Dubai Marina:** A futuristic shoreline featuring high-rise apartments, the Marina Walk, and great beach access.
- **Old Dubai (Deira & Bur Dubai):** The roots of the city. Visit the traditional Gold and Spice souks across the Creek.
- **Palm Jumeirah:** The world's largest man-made island, known for its luxury resorts like Atlantis and upscale beach clubs.

## 🍽️ Food & Dining Etiquette
- **Global Gastronomy:** With 200+ nationalities, you can find every world cuisine from Michelin-starred dining to authentic street food.
- **Local Flavors:** Try Middle Eastern staples like Hummus, Manakish, and the sweet, fried dumplings called Luqaimat.
- **Etiquette:** Dress respectfully in public areas (shoulders and knees covered in malls). Public displays of affection should be kept modest. Alcohol is served in licensed hotels and bars.

## 🚇 Transportation Tips
- **Dubai Metro:** A clean, driverless, and futuristic rail system. For a few extra Dirhams, the "Gold Class" cabin offers the best views from the front.
- **Taxis & Careem:** Government taxis are plentiful and fair. Careem is the local ride-hailing app, essential for getting around quickly.

## 💎 Local Secrets & Insights
- **The Abra Ride:** Crossing the [Dubai Creek](search:Dubai Creek) in a traditional wooden boat costs only 1 Dirham—the most authentic and affordable experience in town.
- [Al Qudra Lakes](search:Al Qudra Lakes): A man-made desert oasis perfect for a sunset picnic or stargazing, far from the city's neon lights.
- **[Burj Khalifa](search:Burj Khalifa) View:** Book your "At The Top" tickets online weeks in advance; choosing a slot just before sunset gives you the best of both day and night views.''';

  // HONG KONG
  static const _hongKongTR = '''# Hong Kong Rehberi: Gökyüzü ve Denizin Buluştuğu Dev Metropol 🇭🇰

Hong Kong; sislere bürünmüş yeşil tepelerin, devasa gökdelenlerin ve hareketli limanların oluşturduğu benzersiz bir siluete sahip, Doğu ile Batı'nın en dinamik karışımıdır.

## 📅 Ne Zaman Gidilir?
- **Sonbahar (Ekim-Aralık):** Nem azdır, hava güneşli ve serindir; gezmek için en mükemmel dönemdir.
- **Bahar (Mart-Nisan):** Keyifli olabilir ama sisli günlere hazırlıklı olun.

## 🏘️ Semt Rehberi
- **Central:** İş dünyasının kalbi, lüks mağazalar ve ünlü gece hayatı bölgesi Lan Kwai Fong burada yer alır.
- **Tsim Sha Tsui (TST):** Victoria Limanı'nın en güzel manzarası, müzeler ve alışveriş merkezlerinin olduğu bölge.
- **Mong Kok:** Dünyanın en yoğun bölgelerinden biri; sokak pazarları ve gerçek bir Hong Kong kaosu için gidilmeli.
- **Causeway Bay:** Alışverişin başkenti; hiç sönmeyen ışıklar ve dev mağazalar.

## 🍽️ Ne Yenir ve İçilir?
- **Dim Sum:** Hong Kong mutfağının kalbidir. *Tim Ho Wan* gibi yerlerde dünyanın en ucuz Michelin yıldızlı yemeğini yiyebilirsiniz.
- **Roast Goose:** Çıtır derili fırın kaz eti buranın bir diğer spesiyalidir.
- **Yemek Adabı:** Masada paylaşımlı oturmak (daap toi) çok yaygındır; tanımadığınız biriyle aynı masada yemek yemeye hazır olun.
- **Çay:** Restoranlarda oturduğunuzda ilk gelen çay genellikle bardakları temizlemek içindir, hemen içmeyin!

## 🚇 Ulaşım İpuçları
- **Octopus Card:** Sadece ulaşımda değil, marketlerde ve kafelerde de geçen bu kart Hong Kong'da hayatta kalma kitidir.
- **Star Ferry:** Hong Kong Adası ile Kowloon arasında sadece birkaç dakikada geçen bu tarihi feribot, dünyanın en keyifli ulaşım yollarından biridir.
- **MTR:** Dünyanın en verimli metro sistemlerinden biri; her yere ulaşır.

## 💎 Lokal Sırlar & İpuçları
- [Victoria Peak](search:Victoria Peak): Tepeye çıkmak için meşhur füniküler (Peak Tram) yerine 15 numaralı otobüsü kullanın; yolculuk daha uzun sürer ama manzara harikadır.
- [Dragon's Back](search:Dragon's Back): Şehir merkezinden sadece 30 dakikada ulaşabileceğiniz bu yürüyüş rotası, gökdelenlerin ardındaki muhteşem doğayı gösterir.
- [Lamma Adası](search:Lamma Island): Araba trafiğinin olmadığı bu adaya gidip taze deniz mahsulleri yiyerek şehirden tamamen uzaklaşabilirsiniz.''';

  static const _hongKongEN = '''# Hong Kong Guide: Where Skyscrapers Meet the Sea 🇭🇰

Hong Kong is a vertical marvel—a city of mist-covered green peaks, endless skyscrapers, and a bustling harbor that serves as the world's most dynamic crossroads between East and West.

## 📅 Best Time to Visit
- **Autumn (October-December):** Low humidity, clear skies, and mild temperatures make this the absolute best time for sightseeing.
- **Spring (March-April):** Pleasant weather, though be prepared for occasional fog and humidity.

## 🏘️ Neighborhood Guide
- **Central:** The financial heart, home to world-class dining, upscale malls, and the famous nightlife of Lan Kwai Fong.
- **Tsim Sha Tsui (TST):** Offers the quintessential skyline view of Hong Kong Island, along with the Cultural Centre and luxury hotels.
- **Mong Kok:** One of the most densely populated spots on Earth—visit for street markets, neon signs, and authentic local energy.
- **Causeway Bay:** A neon-lit shopping paradise where department stores and boutiques stay open late into the night.

## 🍽️ Food & Dining Etiquette
- **Dim Sum:** The soul of Hong Kong dining. Experience Michelin-starred excellence at affordable prices at spots like *Tim Ho Wan*.
- **Roast Goose:** Known for its crispy skin and tender meat, it's a gourmet local favorite.
- **Dining Etiquette:** Table sharing ("daap toi") is very common in busy restaurants; don't be surprised if you're seated next to strangers.
- **Tea Ritual:** The first pot of tea served in traditional spots is often intended for rinsing your chopsticks and bowl—watch the locals before you sip!

## 🚇 Transportation Tips
- **Octopus Card:** A must-have rechargeable card used for all public transport, convenience stores, and many cafes.
- **Star Ferry:** Crossing between Kowloon and Hong Kong Island on this historic ferry is arguably the world’s most scenic (and cheapest) commute.
- **MTR:** Exceptionally clean, fast, and punctual—the MTR covers almost every corner of the metropolitan area.

## 💎 Local Secrets & Insights
- [Victoria Peak](search:Victoria Peak): Instead of the crowded Peak Tram, take Bus 15 from Central. It’s cheaper and offers stunning winding views of the island's lush hills.
- [Dragon's Back Hike](search:Dragon's Back): A stunning ridge-top walk just 30 minutes from the city center, offering breathtaking views of the coastline and beaches.
- [Lamma Island](search:Lamma Island): A car-free sanctuary just a ferry ride away. Go for the fresh seafood restaurants and the peaceful, bohemian vibe.''';

  // DUBLIN
  static const _dublinTR = '''# Dublin Rehberi: Edebiyat, Publar ve Samimi Bir Ruh 🇮🇪

Dublin; Georgian tarzı sokakları, bin yıllık tarihi, meşhur bira kültürü ve dünyanın en sıcakkanlı insanlarıyla bilinen samimi bir başkenttir.

## 📅 Ne Zaman Gidilir?
- **St. Patrick's Day (17 Mart):** Şehrin tamamen yeşile büründüğü ve dünyanın en büyük partisine dönüştüğü dönem.
- **Yaz (Haziran-Ağustos):** Günlerin çok uzun olduğu ve parkların keyfinin en iyi çıkarıldığı zaman.
- **İpucu:** Dublin'de hava her an değişebilir; "dört mevsimi bir günde yaşama" hazırlıklı olun ve yanınızda mutlaka hafif bir yağmurluk bulundurun.

## 🏘️ Semt Rehberi
- **Temple Bar:** Renkli publar ve sokak sanatçılarıyla şehrin turistik kalbi. Akşamları çok canlıdır.
- **Grafton Street & Around:** Şık alışveriş caddeleri, St. Stephen’s Green parkı ve Trinity College'ın olduğu nezih bölge.
- **Smithfield:** Eskiden endüstriyel olan, şimdi modern müzeler (Jameson Distillery gibi) ve trend kafelerle dolu hipster mahallesi.

## 🍽️ Ne Yenir ve İçilir?
- **Irish Stew:** Kuzu eti, patates ve havuçla yapılan geleneksel ve iç ısıtan bir tencere yemeği.
- **Guinness:** İrlanda'nın simgesi olan siyah bira. St. James's Gate'deki fabrikasında (Guinness Storehouse) tadına bakmak bir Dublin klasiğidir.
- **Pub Kültürü:** İrlanda'da publar sadece içki içilen yerler değil, toplumsallaşmanın kalbidir. Genelde canlı İrlanda müziği eşlik eder.
- **Tur:** Birine bir içki ısmarlamak ("Buying a round") arkadaşlık kurmanın en hızlı yoludur.

## 🚇 Ulaşım İpuçları
- **Luas:** Şehir içi ulaşımı sağlayan modern ve hızlı tramvay hattı.
- **DART:** Sahil şeridi boyunca giden tren. Dublin'den uzaklaşıp deniz havası almak için idealdir.
- **Yürüyüş:** Dublin merkezi oldukça kompakttır; çoğu yer birbirine yürüme mesafesindedir.

## 💎 Lokal Sırlar & İpuçları
- [Trinity College Kütüphanesi](search:Trinity College): Dünyanın en güzel kütüphanelerinden biridir ve bin yıllık "Book of Kells" el yazmasına ev sahipliği yapar.
- [Phoenix Park](search:Phoenix Park): Avrupa'nın en büyük şehir parklarından biri. İçinde serbestçe dolaşan geyikleri görebilirsiniz.
- [Howth Cliff Walk](search:Howth Cliff Walk): Şehir merkezinden DART ile 25 dakikada ulaşabileceğiniz bu falez yürüyüşü, muhteşem bir okyanus manzarası sunar.''';

  static const _dublinEN = '''# Dublin Guide: Literature, Pubs & A Warm Soul 🇮🇪

Dublin is a city of stories—from its Viking roots and Georgian architecture to its legendary pub culture and world-famous literary heritage. It’s a capital that feels like a friendly village.

## 📅 Best Time to Visit
- **St. Patrick's Day (March 17):** When the entire city turns green for a week-long celebration. It’s crowded but an unforgettable experience.
- **Summer (June-August):** Offers the longest days and the best chance of dry weather for exploring the coastal outskirts.
- **Tip:** Dublin weather is famously fickle. You will often experience "four seasons in one day"—always carry a light waterproof jacket.

## 🏘️ Neighborhood Guide
- **Temple Bar:** The cultural quarter known for its cobblestone streets, vibrant pubs, and street performers. Touristy but essential.
- **Trinity & Grafton St:** The elegant heart of the city, featuring upscale shopping, historic colleges, and the beautiful St. Stephen's Green park.
- **Smithfield:** A trendy district home to the Jameson Distillery, independent cinemas, and great brunch spots.

## 🍽️ Food & Dining Etiquette
- **Irish Stew:** A hearty, traditional stew made with lamb, potatoes, and root vegetables.
- **Guinness:** More than just a beer, it’s a national symbol. The freshest pints are pulled right here in Dublin (visit the Guinness Storehouse for the full story).
- **Pub Etiquette:** In Ireland, a pub is the living room of the community. "Bought rounds" are common—if someone buys you a drink, you are expected to buy the next one for the group.
- **Live Music:** Look for pubs hosting "Trad Sessions"—impromptu gatherings of traditional Irish musicians.

## 🚇 Transportation Tips
- **The Luas:** Dublin's efficient tram system with two main lines (Green and Red) connecting the suburbs to the center.
- **DART:** The coastal train—perfect for a day trip to the seaside villages of Howth or Dalkey.
- **Leap Card:** A prepaid card that saves money on all city buses, trams, and trains.

## 💎 Local Secrets & Insights
- [The Long Room (Trinity College)](search:Trinity College): One of the most beautiful libraries in the world, home to the ancient Book of Kells.
- [Phoenix Park](search:Phoenix Park): One of the largest walled city parks in Europe. Keep an eye out for the herds of wild fallow deer that roam freely.
- [Howth Cliff Walk](search:Howth Cliff Walk): Just 25 minutes from the center via DART, this rugged coastal path offers stunning views of the Irish Sea and fresh seafood at the harbor.''';
  // ===================================
  // FEATURED ARTICLES
  // ===================================
  static String getArticleContent(String articleId, bool isEnglish) {
    switch (articleId) {
      case 'winter_routes':
        return isEnglish ? _winterRoutesEN : _winterRoutesTR;
      case 'hidden_gems':
        return isEnglish ? _hiddenGemsEN : _hiddenGemsTR;
      case 'gastronomy':
        return isEnglish ? _gastronomyEN : _gastronomyTR;
      case 'romantic':
        return isEnglish ? _romanticEN : _romanticTR;
      default:
        return isEnglish ? "# Coming Soon\n\nThis article is being written!" : "# Çok Yakında\n\nBu makale hazırlanıyor!";
    }
  }

  static const _winterRoutesTR = '''# Kış Tatili İçin En İyi 5 Rota

Kışın Avrupa bir başka güzel. Karlı çatılar, sıcak şarap kokusu ve peri masalı gibi sokaklar... İşte soğuğu sevdirecek 5 harika rota.

## 1. Rovaniemi, Finlandiya
[Noel Baba'nın resmi evi](search:Santa Claus Village)! Kuzey ışıklarını (Aurora Borealis) izlemek, husky kızağına binmek ve buz otelde kalmak için dünyadaki en iyi yer.
> **İpucu:** Termal içliklerinizi unutmayın, hava -20 dereceyi görebilir!

## 2. Viyana, Avusturya
Şehir bir balo salonu gibi. [Rathausplatz](search:Rathausplatz Vienna)'daki devasa buz pisti ve her köşedeki zarif kafeler. [Cafe Central](search:Cafe Central Vienna)'de sıcak çikolata ve Sachertorte bir ritüeldir.

## 3. Prag, Çekya
[Karl köprüsü](search:Charles Bridge) karlar altındayken adeta bir Game of Thrones sahnesi. [Eski Şehir Meydanı](search:Old Town Square Prague)'ndaki gotik kuleler sisler arasında büyüleyici görünür. Trdelník (tarçınlı tatlı) yiyerek ısının.

## 4. Tromsø, Norveç
Kutup dairesinin kalbi. Balina izleme turları ve gece yarısı güneşinin tersi "polar gece" deneyimi. Şehir hayatı ve vahşi doğa iç içe.

## 5. Zermatt, İsviçre
[Matterhorn](search:Matterhorn Glacier Paradise) dağının gölgesinde, araç trafiğine kapalı bir masal kasabası. Dünyanın en iyi kayak pistleri ve fondü restoranları burada.
''';

  static const _winterRoutesEN = '''# Top 5 Winter Holiday Routes

Europe is uniquely beautiful in winter. Snowy rooftops, the scent of mulled wine, and fairytale streets... Here are 5 routes that will make you love the cold.

## 1. Rovaniemi, Finland
 The [official hometown of Santa Claus](search:Santa Claus Village)! The best place on earth to watch the Northern Lights (Aurora Borealis), ride husky sleds, and sleep in an ice hotel.
> **Tip:** Don't forget your thermal layers; temperatures can drop to -20°C!

## 2. Vienna, Austria
The city looks like a ballroom. The massive ice rink at [Rathausplatz](search:Rathausplatz Vienna) and elegant cafes on every corner. Hot chocolate and Sachertorte at [Cafe Central](search:Cafe Central Vienna) is a ritual.

## 3. Prague, Czechia
[Charles Bridge](search:Charles Bridge) under snow looks like a scene from Game of Thrones. The gothic towers of [Old Town Square](search:Old Town Square Prague) look mesmerizing in the mist. Warm up with a Trdelník (cinnamon pastry).

## 4. Tromsø, Norway
The heart of the Arctic Circle. Whale watching tours and the "polar night" experience. City life and wild nature intertwined.

## 5. Zermatt, Switzerland
A car-free fairytale village in the shadow of the [Matterhorn](search:Matterhorn Glacier Paradise). Home to the world's best ski slopes and fondue restaurants.
''';

  static const _hiddenGemsTR = '''# Avrupa'nın Gizli Hazineleri

Herkes Paris ve Roma'ya giderken, siz kalabalıktan uzak bu büyüleyici kasabaları keşfedin.

## 1. Matera, İtalya
Taş devrinden kalma mağara evlerin olduğu bu şehir, sanki başka bir gezegen. James Bond filminin çekildiği o mistik sokaklar.
> **İpucu:** [Sassi di Matera](search:Sassi di Matera) bölgesindeki bir mağara otelde konaklayın.

## 2. Giethoorn, Hollanda
"Kuzeyin Venedik'i" ama motor sesi yok. Sadece elektrikli sessiz tekneler, saz çatılı evler ve kanallar. Tam bir huzur cenneti.

## 3. Kotor, Karadağ
Fiyortların arasında saklanmış ortaçağ şehri. Kedileriyle meşhur! [Kale surlarına](search:Castle of San Giovanni) tırmanıp o muhteşem manzarayı izlemek paha biçilemez.

## 4. Colmar, Fransa
Alsace şarap yolunun başkenti. Yarı ahşap renkli evleriyle Disney filmi (Güzel ve Çirkin) setinden fırlamış gibi.

## 5. Sintra, Portekiz
Lizbon'a sadece 40 dakika ama bambaşka bir dünya. [Pena Sarayı](search:Pena Palace)'nın sarı-kırmızı renkleri ve sisli ormanlar. Mistik ve romantik.
''';

  static const _hiddenGemsEN = '''# Europe's Hidden Gems

While everyone goes to Paris and Rome, distinct yourself by exploring these enchanting towns away from the crowds.

## 1. Matera, Italy
A city of cave dwellings dating back to the Stone Age; it feels like another planet. The mystical streets where James Bond was filmed.
> **Tip:** Stay in a cave hotel in the [Sassi di Matera](search:Sassi di Matera) district.

## 2. Giethoorn, Netherlands
"Venice of the North" but without engine noise. Only silent electric boats, thatched-roof houses, and canals. A total haven of peace.

## 3. Kotor, Montenegro
A medieval city hidden among fjords. Famous for its cats! Climbing the [fortress walls](search:Castle of San Giovanni) to see that magnificent view is priceless.

## 4. Colmar, France
Capital of the Alsace wine route. With its half-timbered colorful houses, it looks straight out of a Disney movie (Beauty and the Beast).

## 5. Sintra, Portugal
Only 40 minutes from Lisbon but a different world. The yellow-red colors of [Pena Palace](search:Pena Palace) and misty forests. Mystical and romantic.
''';

  static const _gastronomyTR = '''# Gastronomi Tutkunları İçin

Midenizin bayram edeceği, diyeti bozduracak 5 lezzet başkenti.

## 1. San Sebastian, İspanya
Dünyada metrekareye en çok Michelin yıldızı düşen şehir! Ama asıl olay barlardaki "Pintxos"lar. Tezgahın üzerindeki her şeyden bir tane alın.

## 2. Lyon, Fransa
Paris değil, Fransa'nın gerçek yemek başkenti Lyon'dur. "Bouchon" adı verilen geleneksel lokantalarda soğan çorbası ve ördek konfit yiyin.

## 3. Bologna, İtalya
Lakabı "La Grassa" (Şişman). Çünkü yemekler o kadar güzel! Gerçek Bolonez sos (Ragù) burada yenir ama spagettiyle değil, Tagliatelle ile!

## 4. Gaziantep, Türkiye
UNESCO Gastronomi şehri. Sabah beyran, öğlen küşleme, tatlı olarak katmer. Dünyanın en iyi mutfaklarından biri.

## 5. Kopenhag, Danimarka
"Yeni İskandinav Mutfağı"nın evi. [Noma](search:Noma Copenhagen) gibi efsaneler burada. Sadece fine-dining değil, Smørrebrød (açık sandviç) kültürü de harika.
''';

  static const _gastronomyEN = '''# For Gastronomy Lovers

5 delicious capitals where your stomach will celebrate and diets will be broken.

## 1. San Sebastian, Spain
The city with the most Michelin stars per square meter in the world! But the real deal involves "Pintxos" in bars. Grab one of everything on the counter.

## 2. Lyon, France
Not Paris, but Lyon is the true food capital of France. Eat onion soup and duck confit in traditional restaurants called "Bouchon".

## 3. Bologna, Italy
Nicknamed "La Grassa" (The Fat One). Because the food is that good! Real Bolognese sauce (Ragù) is eaten here, but with Tagliatelle, not spaghetti!

## 4. Gaziantep, Turkey
UNESCO City of Gastronomy. Beyran for breakfast, Küşleme for lunch, Katmer for dessert. One of the best cuisines on earth.

## 5. Copenhagen, Denmark
Home of "New Nordic Cuisine". Legends like [Noma](search:Noma Copenhagen) are here. Not just fine dining, but the Smørrebrød (open sandwich) culture is also amazing.
''';

  static const _romanticEN = '''# Romantic Weekend Getaways

Perfect routes for a weekend trip with your loved one.

## 1. Venice, Italy
Yes, it's cliché, but getting lost in the canals at night is unbeatable. Suggestion: Go to the [Dorsoduro](search:Dorsoduro) district, calmer and more local.

## 2. Bruges, Belgium
Like a chocolate box. Medieval buildings, swans in canals, and the smell of waffles everywhere. Rent a bike and cycle to the windmills.

## 3. Santorini, Greece
Watching the sunset in [Oia](search:Oia Santorini) is a bucket list item. White houses with blue domes and the vast Aegean Sea.
> **Tip:** Stay in [Imerovigli](search:Imerovigli) instead of Oia for better views and fewer crowds.

## 4. Heidelberg, Germany
Germany's most romantic city. An old castle on the hill, the Neckar river below, and the philosophical walking path ([Philosophenweg](search:Philosophenweg)).

## 5. Seville, Spain
Passion, flamenco, and orange trees. Taking a carriage ride in [Plaza de España](search:Plaza de España Seville) and getting lost in the [Santa Cruz](search:Barrio Santa Cruz) neighborhood.
''';

  static const _romanticTR = '''# Romantik Haftasonu Kaçamakları

Sevdiğinizle baş başa bir haftasonu için mükemmel rotalar.

## 1. Venedik, İtalya
Evet klişe ama gece kanallarda kaybolmanın yerini hiçbir şey tutamaz. Öneri: [Dorsoduro](search:Dorsoduro) bölgesine gidin, daha sakin ve lokal.

## 2. Brugge, Belçika
Bir çikolata kutusu gibi. Ortaçağ binaları, kanallarda kuğular ve her yerde waffle kokusu. Bisiklet kiralayıp yel değirmenlerine sürün.

## 3. Santorini, Yunanistan
[Oia](search:Oia Santorini)'da gün batımını izlemek ölmeden önce yapılacaklar listesinde. Mavi kubbeli beyaz evler ve sonsuz Ege denizi.
> **İpucu:** Daha iyi manzara ve daha az kalabalık için Oia yerine [Imerovigli](search:Imerovigli)'de kalın.

## 4. Heidelberg, Almanya
Almanya'nın en romantik şehri. Tepede eski bir kale, aşağıda Neckar nehri ve filozoflar yolu ([Philosophenweg](search:Philosophenweg)).

## 5. Sevilla, İspanya
Tutku, flamenko ve portakal ağaçları. [Plaza de España](search:Plaza de España Sevilla)'da fayton turu yapmak ve [Santa Cruz](search:Barrio Santa Cruz) mahallesinde kaybolmak.
''';

  // ANTALYA
  static const _antalyaTR = '''# Antalya Rehberi: Akdeniz'in Mavi İncisi 🇹🇷

Antalya sadece otellerden ibaret değildir; antik kentleri, şelaleleri ve yaşayan tarihiyle Akdeniz'in en güzel liman şehirlerinden biridir.

## 📅 Ne Zaman Gidilir?
- **İlkbahar ve Sonbahar:** Nisan-Mayıs ve Eylül-Ekim ayları hem gezmek hem de denize girmek için en ideal sıcaklıkları sunar.
- **Yaz:** Çok sıcak olabilir ama gece hayatı ve plajlar en canlı dönemini yaşar.
- **İpucu:** Ekim ayında deniz suyu hala sıcacıktır ve kalabalıklar azalmıştır.

## 🏘️ Semt Rehberi
- **Kaleiçi:** Şehrin kalbi. Tarihi Osmanlı evleri, Hadrian Kapısı ve daracık sokaklarıyla görsel bir şölen.
- **Lara:** Daha modern, lüks kafeler ve restoranların olduğu, sahil şeridi boyunca uzanan bölge.
- **Konyaaltı:** Şehrin diğer ucu; uzun plajı ve arkasındaki heybetli dağ manzarasıyla ünlüdür.

## 🍽️ Ne Yenir ve İçilir?
- **Piyaz:** Antalya usulü piyaz tahinli olur! Köftenin yanında mutlaka isteyin. *Piyazcı Sami* bir klasiktir.
- **Yanık Dondurma:** Keçi sütünden yapılan ve hafif yanık tadı olan bu dondurma şehre özgüdür.
- **Serpme Börek:** Sabah kahvaltısında incecik açılmış, kıymalı veya peynirli serpme börek yemeden dönmeyin.

## 🚇 Ulaşım İpuçları
- **Antray:** Havalimanından şehir merkezine ve otogara ulaşım için modern tramvay hattını kullanın.
- **Nostaljik Tramvay:** Kaleiçi'nin üst tarafında sahil boyunca giden bu tramvay harika manzaralar sunar.

## 💎 Lokal Sırlar & İpuçları
- [Düden Şelalesi](search:Duden Waterfalls): Şelalenin denize döküldüğü noktayı görmek için Lara tarafındaki parka gidin; manzara büyüleyicidir.
- [Falezler](search:Falezler): Konyaaltı Varyant'tan inerek falezlerin altındaki plajları keşfedin; su burada kristal berraklığındadır.
- [Likya Yolu](search:Lycian Way): Dünyanın en iyi yürüyüş rotalarından biri buradan başlar; en azından kısa bir parkurunu yürüyün.''';

  static const _antalyaEN = '''# Antalya Guide: The Blue Pearl of the Mediterranean 🇹🇷

Antalya is far more than just resorts; it's a vibrant port city filled with ancient ruins, cascading waterfalls, and living history.

## 📅 Best Time to Visit
- **Spring & Autumn:** April-May and September-October offer perfect temperatures for both sightseeing and swimming.
- **Summer:** Can be intensely hot, but the beaches and nightlife are at their peak.
- **Tip:** In October, the sea water is still warm, and the summer crowds have dispersed.

## 🏘️ Neighborhood Guide
- **Kaleiçi (Old Town):** The historic heart. A visual feast of Ottoman houses, Hadrian's Gate, and narrow cobbled streets.
- **Lara:** The modern side, stretching along the cliffs with upscale cafes, restaurants, and parks.
- **Konyaaltı:** Famous for its long pebble beach backed by majestic mountains.

## 🍽️ Food & Dining Etiquette
- **Piyaz:** Antalya-style bean salad is unique because it's made with tahini! A must-have side dish with meatballs.
- **Burnt Ice Cream (Yanık Dondurma):** Made from goat's milk with a distinct smoky flavor—a local specialty you won't find elsewhere.
- **Serpme Börek:** Don't miss this flaky, hand-tossed pastry filled with cheese or meat for breakfast.

## 🚇 Transportation Tips
- **Antray:** Use the modern tram line to travel easily between the airport, city center, and bus terminal.
- **Nostalgic Tram:** Runs along the coast above Kaleiçi, offering stunning panoramic views.

## 💎 Local Secrets & Insights
- [Lower Düden Waterfall](search:Duden Waterfalls): Visit the park in Lara to see the massive waterfall plunging directly into the sea—it's a spectacular sight.
- [The Cliffs](search:Antalya Cliffs): Explore the beach clubs tucked under the massive cliffs near Variant for crystal-clear water.
- [Lycian Way](search:Lycian Way): One of the world's best hiking trails starts nearby; try walking a short section for breathtaking views.''';

  // KAPADOKYA
  static const _kapadokyaTR = '''# Kapadokya Rehberi: Masal Diyarında Yolculuk 🇹🇷

Kapadokya, doğanın ve tarihin el ele vererek yarattığı, dünyada eşi benzeri olmayan bir coğrafyadır. Peri bacaları, yeraltı şehirleri ve mağara otelleriyle sizi başka bir gezegende hissettirir.

## 📅 Ne Zaman Gidilir?
- **Bahar:** Doğa uyanırken vadilerde yürüyüş yapmak için en güzel zaman.
- **Kış:** Karlar altındaki peri bacaları manzarası nefes kesicidir; şömine başında ısınmak çok keyiflidir.
- **İpucu:** Balonlar sadece rüzgar uygunsa uçar; garantilemek için en az 2-3 gün kalmalısınız.

## 🏘️ Bölge Rehberi
- **Göreme:** Her şeyin merkezi. Açık hava müzesi ve en ikonik manzaralar burada.
- **Ürgüp:** Daha soylu konaklar, şaraphaneler ve gece hayatı için tercih edilebilir.
- **Uçhisar:** Bölgenin en yüksek noktası. Kalesi ve lüks butik otelleriyle meşhurdur.
- **Avanos:** Kızılırmak kenarında, çömlekçiliğin ve sanatın merkezi.

## 🍽️ Ne Yenir ve İçilir?
- **Testi Kebabı:** Yemeğiniz masada kırılarak servis edilir. Hem lezzetli hem de izlemesi keyifli bir ritüeldir.
- **Şarap:** Bölge binlerce yıldır bağcılık merkezidir. Yerel üzümlerden yapılan şarapları mutlaka tadın.
- **Mantı (Nevşehir Mantısı):** İnce hamuru ve özel sosuyla Kayseri ve Nevşehir bölgesinin en meşhur yemeğidir.

## 💎 Lokal Sırlar & İpuçları
- [Gün Doğumu](search:Göreme Sunset Point): Balona binmeseniz bile sabah 05:30'da kalkın ve balonların kalkışını izleyin. Göreme'deki "Aşıklar Tepesi" (Sunset Point) en iyi noktadır.
- [Yeraltı Şehirleri](search:Derinkuyu Underground City): Derinkuyu veya Kaymaklı'ya gidin. 8 kat aşağı inmek klostrofobik olabilir ama mühendislik karşısında büyüleneceksiniz.
- [ATV Turu](search:Love Valley): Gün batımında tozlu yollarda ATV turu yapmak, vadileri keşfetmenin en eğlenceli yoludur.''';

  static const _kapadokyaEN = '''# Cappadocia Guide: A Journey to Fairyland 🇹🇷

Cappadocia is a unique landscape created by nature and history hand in hand. With its fairy chimneys, underground cities, and cave hotels, it feels like another planet.

## 📅 Best Time to Visit
- **Spring:** The best time for hiking in the valleys as nature wakes up.
- **Winter:** The sight of fairy chimneys under snow is breathtaking; warming up by a fireplace is pure cozy bliss.
- **Tip:** Hot air balloons only fly if the wind permits; stay at least 2-3 days to maximize your chances.

## 🏘️ Area Guide
- **Göreme:** The center of it all. Home to the Open Air Museum and the most iconic views.
- **Ürgüp:** Known for its noble stone mansions, wineries, and evening entertainment.
- **Uçhisar:** The highest point in the region. Famous for its castle and luxury boutique cave hotels.
- **Avanos:** Located by the Red River, this is the hub of pottery and local arts.

## 🍽️ Food & Drink
- **Pottery Kebab (Testi Kebabı):** A meat stew cooked in a sealed clay pot which is broken open at your table. A delicious ritual.
- **Local Wine:** This region has been a winemaking center for millennia. Be sure to taste wines made from local grapes.
- **Manti (Turkish Ravioli):** Tiny dumplings served with garlic yogurt and spiced butter. A staple of the region.

## 💎 Local Secrets & Insights
- [Sunrise Spectacle](search:Göreme Sunset Point): Even if you don't fly, wake up at 5:30 AM to watch the balloons launch. "Sunset Point" in Göreme offers the best panoramic view.
- [Underground Cities](search:Derinkuyu Underground City): Visit Derinkuyu or Kaymaklı. Going 8 levels deep might challenge claustrophobia, but the engineering is mind-blowing.
- **ATV Tour:** An ATV safari at sunset is the most fun way to explore the dusty trails and hidden valleys.''';

  // GAZIANTEP
  static const _gaziantepTR = '''# Gaziantep Rehberi: Dünyanın En Lezzetli Şehri 🇹🇷

UNESCO tarafından tescillenmiş bir gastronomi şehri olan Gaziantep, sadece yemekleriyle değil; müzeleri, hanları ve çarşılarıyla da bir kültür başkentidir.

## 📅 Ne Zaman Gidilir?
- **İlkbahar ve Sonbahar:** Yürüyüş ve yemek turları için hava en uygundur.
- **İpucu:** Yazın (Temmuz-Ağustos) sıcaklıklar 40 dereceyi aşabilir, bu aylardan kaçının.

## 🍽️ Ne Yenir ve İçilir?
- **Kahvaltı:** Burada güne "Beyran" çorbası ile başlanır. *Metanet Lokantası* en meşhurudur. Yanına ciğer kebabı da ekleyebilirsiniz.
- **Öğle Yemeği:** *İmam Çağdaş* veya *Halil Usta*'da Lahmacun ve Küşleme (koyunun en yumuşak yeri) yiyin.
- **Tatlı:** Baklavanın anavatanındasınız. *Koçak* veya *Zeki İnal*'da fıstıklı baklava veya sıcak "Katmer" yiyerek zirveye çıkın.
- **Menengiç Kahvesi:** Yabani fıstıktan yapılan bu sütlü kahveyi *Tahmis Kahvesi*'nin tarihi atmosferinde için.

## 🏘️ Gezilecek Yerler
- **Zeugma Mozaik Müzesi:** Dünyanın en büyük mozaik müzelerinden biri. Meşhur "Çingene Kızı" mozaiği burada sergileniyor.
- **Bakırcılar Çarşısı:** Çekiç sesleri arasında kaybolun. El yapımı bakır eşyalar harika birer hatıradır.
- **Zincirli Bedesten:** Geleneksel kumaşlar (kutnu) ve baharatlar için uğrayın.

## 💎 Lokal Sırlar & İpuçları
- **Baharat Alışverişi:** Eve dönerken mutlaka pul biber, kuru patlıcan ve Antep fıstığı alın. [Almacı Pazarı](search:Almaci Pazari) bu işin merkezidir.
- **Mide Kapasitesi:** Buraya gelmeden önce diyet yapın, çünkü burada durmak imkansızdır!''';

  static const _gaziantepEN = '''# Gaziantep Guide: The World's Most Delicious City 🇹🇷

A UNESCO Creative City of Gastronomy, Gaziantep is not just about food; it's a cultural capital with its world-class museums, historic inns, and bustling bazaars.

## 📅 Best Time to Visit
- **Spring & Autumn:** The weather is perfect for walking tours and endless food tasting.
- **Tip:** Avoid July and August when temperatures can soar above 40°C.

## 🍽️ Gastronomy Route (Food First!)
- **Breakfast:** Start the day with "Beyran" soup, a spicy lamb and rice soup. *Metanet* is the legendary spot. Having liver kebab for breakfast is also a local tradition.
- **Lunch:** Try Lahmacun and Küşleme (the tenderest cut of lamb) at iconic spots like *İmam Çağdaş* or *Halil Usta*.
- **Dessert:** You are in the homeland of Baklava. Visit *Koçak* or *Zeki İnal* for pistachio baklava or warm "Katmer" to reach dessert heaven.
- **Menengiç Coffee:** Drink this milky wild pistachio coffee in the historic atmosphere of *Tahmis Kahvesi*.

## 🏘️ Places to Visit
- **Zeugma Mosaic Museum:** One of the largest mosaic museums in the world. The famous "Gypsy Girl" mosaic is displayed here.
- **Coppersmith Bazaar (Bakırcılar Çarşısı):** Get lost in the rhythmic sounds of hammers. Handmade copperware makes for a beautiful souvenir.
- **Zincirli Bedesten:** Visit this covered market for traditional fabrics (kutnu) and spices.

## 💎 Local Secrets & Insights
- **Spice Shopping:** Don't leave without buying red pepper flakes, dried eggplants, and Antep pistachios. [Almacı Market](search:Almaci Pazari) is the place to go.
- **Stomach Capacity:** Go on a diet before you come, because stopping eating here is impossible!''';




  // BELGRAD
  static const _belgradTR = '''# Belgrad Rehberi: Balkanların Hiç Uyumayan Şehri 🇷🇸

Belgrad, Tuna ve Sava nehirlerinin buluştuğu noktada, fırtınalı tarihini müthiş bir enerji ve gece hayatıyla harmanlayan beyaz şehirdir (Beo-grad).

## 📅 Ne Zaman Gidilir?
- **İlkbahar:** Parkların yeşillendiği ve nehir kenarının canlandığı en güzel zaman.
- **Yaz:** "Splavovi" denen nehir kulüpleri açılır ve şehir tam anlamıyla sabaha kadar parti moduna girer.

## 🏘️ Semt Rehberi
- **Stari Grad (Eski Şehir):** Knez Mihailova caddesi ve çevresi. Alışveriş, kafeler ve şehrin kalbi.
- **Dorćol:** Eski Türk mahallesi. Şimdi şehrin en havalı kafelerinin ve barlarının olduğu hipster bölgesi.
- **Vračar:** Aziz Sava Katedrali'nin bulunduğu, geniş caddeli ve şık bir bölge.
- **Zemun:** Eskiden Avusturya-Macaristan toprağı olan bu nehir kenarı kasabası, balık restoranları ve Arnavut kaldırımlı sokaklarıyla çok farklı bir hava sunar.

## 🍽️ Ne Yenir ve İçilir?
- **Cevapi (Cevapcici):** Balkan köftesi. *Walter* gibi zincirlerde veya yerel restoranlarda, yanında "kajmak" (kaymak) ve soğanla yiyin.
- **Burek:** Bizim böreğimiz ama daha yağlı ve doyurucu. Kahvaltının vazgeçilmezidir.
- **Rakija:** Erik, ayva veya kayısıdan yapılan sert meyve rakısı. Yemeğin üstüne "şifa niyetine" ikram edilir.

## 💎 Lokal Sırlar & İpuçları
- [Kalemegdan](search:Belgrade Fortress): Gün batımında kaleye çıkın ve iki nehrin (Sava ve Tuna) birleştiği noktayı izleyin. "Victor" heykeli buranın sembolüdür.
- [Skadarlija](search:Skadarlija): Belgrad'ın Montmartre'ı. Canlı müzik, çiçekli restoranlar ve eski bohem hava. Turistik ama görülmeye değer.
- [Nikola Tesla Müzesi](search:Nikola Tesla Museum): Dünyanın en büyük mucitlerinden birine adanmış bu küçük müzede, elektrik deneyimlerini bizzat yaşayabilirsiniz.''';

  static const _belgradEN = '''# Belgrade Guide: The City That Never Sleeps 🇷🇸

Situated at the confluence of the Danube and Sava rivers, Belgrade ("White City") blends its turbulent history with an incredible energy and world-famous nightlife.

## 📅 Best Time to Visit
- **Spring:** The best time for walking tours as parks turn green and the riverside wakes up.
- **Summer:** The "Splavovi" (river clubs) open their doors, and the city enters full party mode until sunrise.

## 🏘️ Neighborhood Guide
- **Stari Grad (Old Town):** Centered around Knez Mihailova Street. Shopping, cafes, and the historic heart.
- **Dorćol:** The historic Ottoman quarter, now the coolest hipster district filled with coffee shops and bars.
- **Vračar:** An upscale area with wide boulevards, home to the massive Saint Sava Temple.
- **Zemun:** Formerly an Austro-Hungarian town, this riverside neighborhood offers seafood restaurants and cobblestone streets with a distinct Central European vibe.

## 🍽️ Food & Drink
- **Cevapi:** Balkan meatballs. Try them at spots like *Walter*, served with "kajmak" (clotted cream) and onions.
- **Burek:** A flaky pastry filled with meat or cheese. A greasy but delicious breakfast staple.
- **Rakija:** A strong fruit brandy (usually plum, quince, or apricot). Often offered after meals as a digestive.

## 💎 Local Secrets & Insights
- [Kalemegdan Fortress](search:Belgrade Fortress): Visit at sunset to watch the confluence of the Sava and Danube rivers. The "Victor" monument stands guard here.
- [Skadarlija](search:Skadarlija): Belgrade's Bohemian quarter. Live folk music, flower-adorned restaurants, and a vintage atmosphere. Touristy but charming.
- [Nikola Tesla Museum](search:Nikola Tesla Museum): A small but interactive museum dedicated to one of the greatest inventors of all time. You can participate in live electrical demonstrations.''';

  // SARAYBOSNA
  static const _saraybosnaTR = '''# Saraybosna Rehberi: Avrupa'nın Kudüs'ü 🇧🇦

Doğu ile Batı'nın, cami ile kilisenin, hüzün ile umudun iç içe geçtiği Saraybosna; ruhu olan, derin ve duygu dolu bir şehirdir.

## 📅 Ne Zaman Gidilir?
- **İlkbahar ve Yaz:** Şehir en canlı halini alır. Film festivali zamanı (Ağustos) çok hareketlidir.
- **Kış:** Çevredeki olimpik dağlarda (Bjelasnica, Jahorina) kayak yapmak için idealdir.

## 🏘️ Gezilecek Yerler
- **Başçarşı (Baščaršija):** Osmanlı kalbi. Sebil, bakırcılar, ahşap dükkanlar ve güvercinli meydan.
- **Latin Köprüsü:** I. Dünya Savaşı'nın başladığı yer (Arşidük Ferdinand'ın vurulduğu nokta).
- **Umut Tüneli (Tunel Spasa):** Savaş sırasında şehri hayata bağlayan tünel. İnsanın tüylerini diken diken eden bir deneyim.

## 🍽️ Ne Yenir ve İçilir?
- **Boşnak Böreği:** Kıymalı olana "Burek", peynirli olana "Sirnica", ıspanaklıya "Zeljanica" denir. Saçta pişer, yoğurtla yenir.
- **Cevapi:** Saraybosna köftesi *Željo* veya *Hodžić* gibi yerlerde yenir. Somun ekmeği içinde gelir.
- **Boşnak Kahvesi:** Türk kahvesine benzer ama sunumu farklıdır; cezve (džezva) ile gelir, yanında lokumla ikram edilir.

## 💎 Lokal Sırlar & İpuçları
- [Sarı Tabya (Žuta Tabija)](search:Yellow Bastion): Gün batımında şehri tepeden izlemek için en iyi nokta. Ramazan'da iftar topu buradan atılır.
- [Vrelo Bosne](search:Vrelo Bosne): Faytonla gidilebilen, Bosna nehrinin kaynağının olduğu yemyeşil bir park. Şehrin gürültüsünden kaçış noktası.
- [Doğu-Batı Çizgisi](search:Sarajevo Meeting of Cultures): Ferhadija caddesinde yere bakın; "Sarajevo Meeting of Cultures" yazısını göreceksiniz. Bir taraf Osmanlı, diğer taraf Avusturya mimarisidir.''';

  static const _saraybosnaEN = '''# Sarajevo Guide: The Jerusalem of Europe 🇧🇦

Where East meets West, mosque meets church, and sorrow meets hope. Sarajevo is a city with a deep soul that touches everyone who visits.

## 📅 Best Time to Visit
- **Spring & Summer:** The city is vibrant. The Sarajevo Film Festival in August brings an extra buzz.
- **Winter:** An affordable destination for skiing in the nearby Olympic mountains (Bjelasnica, Jahorina).

## 🏘️ Places to Visit
- **Baščaršija:** The Ottoman heart. The wooden fountain (Sebilj), coppersmith alley, and the pigeon-filled square.
- **Latin Bridge:** The site of the assassination of Archduke Franz Ferdinand, which triggered World War I.
- **Tunnel of Hope (Tunel Spasa):** The tunnel that kept the city alive during the siege. A moving and humbling experience.

## 🍽️ Food & Drink
- **Bosnian Pie (Pita):** Meat pie is "Burek", cheese is "Sirnica", spinach is "Zeljanica". Crispy, flaky, and eaten with yogurt.
- **Cevapi:** Sarajevo's trademark kebabs. Eat them at legends like *Željo* inside a fluffy somun bread.
- **Bosnian Coffee:** Similar to Turkish coffee but served in a copper pot (džezva) with a Turkish delight on the side.

## 💎 Local Secrets & Insights
- [Yellow Bastion (Žuta Tabija)](search:Yellow Bastion): The best sunset spot overlooking the valley. During Ramadan, the cannon signaling iftar is fired from here.
- [Vrelo Bosne](search:Vrelo Bosne): A lush park at the spring of the Bosna River. You can take a horse carriage ride down the long, tree-lined avenue to get there.
- [East-West Line](search:Sarajevo Meeting of Cultures): Look down on Ferhadija street for the "Sarajevo Meeting of Cultures" marker. Face one way to see Ottoman architecture; turn around to see Austro-Hungarian styles.''';

  // KOTOR
  static const _kotorTR = '''# Kotor Rehberi: Fiyortların Gizli Hazinesi 🇲🇪

Kotor Körfezi'nin derinliklerinde, sarp dağların gölgesinde saklanan bu ortaçağ şehri, dar sokakları ve her köşede karşınıza çıkan kedileriyle ünlüdür.

## 📅 Ne Zaman Gidilir?
- **Mayıs-Haziran:** Hava mükemmeldir ve dev cruise gemileri henüz şehri istila etmemiştir.
- **Eylül:** Deniz suyu en sıcak seviyesindedir.

## 🏘️ Gezilecek Yerler
- **Stari Grad (Eski Şehir):** Surlar içinde, Venedik mimarisiyle dolu bir labirent. Kaybolmak serbest!
- **San Giovanni Kalesi:** 1350 basamak tırmanmayı göze alırsanız, tepeden göreceğiniz körfez manzarası tüm yorgunluğunuza değecektir.
- **Perast:** Kotor'a 15 dakika uzaklıkta, barok saraylarla süslü sessiz bir sahil kasabası.

## 🍽️ Ne Yenir ve İçilir?
- **Deniz Ürünleri:** Karadağ mutfağı İtalyan etkisindedir. Siyah risotto ve taze ızgara balıklar harikadır.
- **Krempita:** Bölgenin meşhur kremalı tatlısı. Hafif ve çok lezzetlidir.
- **Şarap:** Karadağ'ın yerel "Vranac" kırmızı şarabını deneyin.

## 💎 Lokal Sırlar & İpuçları
- [Kayaların Leydisi (Our Lady of the Rocks)](search:Our Lady of the Rocks): Perast'tan tekneyle bu yapay adaya gidin. Efsaneye göre denizcilerin attığı taşlarla oluşturulmuştur.
- [Kedi Müzesi](search:Cats Museum Kotor): Kotor kedileriyle meşhurdur. Geliri sokak kedilerine giden bu küçük müzeyi ziyaret edebilirsiniz.
- **Pazar:** Kapı önünde kurulan pazardan yerel tütsülenmiş proşutto (Njeguski prsut) ve peynir almayı unutmayın.''';

  static const _kotorEN = '''# Kotor Guide: Hidden Gem of the Fjords 🇲🇪

Tucked deep within the Bay of Kotor under the shadow of dramatic limestone cliffs, this medieval walled city is famous for its winding alleys and resident cats.

## 📅 Best Time to Visit
- **May-June:** Weather is perfect, and the massive cruise ship crowds haven't fully arrived yet.
- **September:** The sea temperature is at its warmest.

## 🏘️ Places to Visit
- **Stari Grad (Old Town):** A maze of Venetian architecture inside the city walls. Getting lost here is part of the charm!
- **San Giovanni Fortress:** If you dare to climb the 1350 steps, the view of the bay from the top is absolutely world-class.
- **Perast:** A quiet, baroque waterfront town just 15 minutes from Kotor.

## 🍽️ Food & Drink
- **Seafood:** Montenegrin cuisine is heavily influenced by Italy. Try the black risotto and fresh grilled fish.
- **Krempita:** The local cream slice cake. Light, fluffy, and delicious.
- **Wine:** Try "Vranac," the robust local red wine of Montenegro.

## 💎 Local Secrets & Insights
- [Our Lady of the Rocks](search:Our Lady of the Rocks): Take a boat from Perast to this artificial island. Legend says it was built by sailors throwing rocks into the sea over centuries.
- [Cat Museum](search:Cats Museum Kotor): Kotor is obsessive about its cats. Visit this quirky museum where proceeds go to feeding the strays.
- **Farmers Market:** Just outside the city walls, buy some "Njeguski prsut" (smoked ham) and local cheese from the morning market.''';

  // OSLO
  static const _osloTR = '''# Oslo Rehberi: Doğayla İç İçe Modern Yaşam 🇳🇴

Oslo; fiyortların kıyısında, modern mimarinin ve ormanların buluştuğu sakin ama etkileyici bir başkenttir. Şehir hayatından kopmadan doğaya kaçmak burada mümkündür.

## 📅 Ne Zaman Gidilir?
- **Yaz:** Günlerin hiç bitmediği, insanların parklara ve fiyortlara akın ettiği en canlı dönem.
- **Kış:** Müzeler ve kış sporları için ideal, ancak günler çok kısadır.

## 🏘️ Semt Rehberi
- **Grünerløkka:** Şehrin hipster bölgesi. Sokak sanatı, vintage dükkanlar, kahveciler ve barlar burada.
- **Bjørvika:** Opera Binası ve Munch Müzesi'nin olduğu ultra modern sahil şeridi.
- **Aker Brygge:** Lüks restoranlar ve alışveriş merkezleriyle dolu eski tersane bölgesi.

## 🍽️ Ne Yenir ve İçilir?
- **Somon:** Norveç somonu dünyaca ünlüdür. Taze veya füme, her öğünde yiyebilirsiniz.
- **Brunost (Kahverengi Peynir):** Karamelimsi tadı olan bu keçi peyniri Norveç kahvaltılarının olmazsa olmazıdır. Waffle ile deneyin.
- **Kahve:** Oslo, dünyanın en iyi kahve kavurucularından bazılarına (Tim Wendelboe gibi) ev sahipliği yapar.

## 💎 Lokal Sırlar & İpuçları
- [Opera Binasının Çatısı](search:Oslo Opera House): Mermer çatısında yürümek serbesttir. Şehrin ve fiyordun en güzel manzarası buradadır.
- **Sauna Kültürü:** Fiyort kenarındaki yüzer saunalardan (KOK veya SALT) birine gidin, terleyip buz gibi denize atlayın. Tam bir Viking deneyimi!
- [Vigeland Parkı](search:Vigeland Park): Dünyanın en büyük heykel parklarından biri. Gustav Vigeland'ın insan doğasını anlatan 200'den fazla heykeli buradadır.''';

  static const _osloEN = '''# Oslo Guide: Modern Life Embracing Nature 🇳🇴

Oslo is a calm yet striking capital where modern architecture meets deep forests on the edge of the fjords. It's the perfect place to combine city life with outdoor escape.

## 📅 Best Time to Visit
- **Summer:** The most vibrant time when days are endless, and locals flock to parks and the fjord islands.
- **Winter:** Ideal for museums and winter sports, though be prepared for very short daylight hours.

## 🏘️ Neighborhood Guide
- **Grünerløkka:** The hipster district. Full of street art, vintage shops, artisan coffee, and lively bars.
- **Bjørvika:** The ultra-modern waterfront home to the Opera House and the new Munch Museum.
- **Aker Brygge:** A former shipyard turned into a hub of high-end dining and shopping along the boardwalk.

## 🍽️ Food & Drink
- **Salmon:** Norwegian salmon is world-famous. Enjoy it fresh, smoked, or cured at any meal.
- **Brunost (Brown Cheese):** A goat cheese with a caramel-like sweet taste. Essential on waffles.
- **Coffee:** Oslo is home to some of the world's best coffee roasters (like Tim Wendelboe). A must for caffeine lovers.

## 💎 Local Secrets & Insights
- [Opera House Roof](search:Oslo Opera House): Walking on the marble roof is allowed and encouraged. It offers the best panoramic views of the city and fjord.
- **Sauna Culture:** Visit one of the floating saunas (like KOK or SALT) on the fjord. Sweat it out, then jump into the icy water—a true Viking experience!
- [Vigeland Park](search:Vigeland Park): The world's largest sculpture park by a single artist, featuring over 200 sculptures depicting the cycle of human life.''';

  // ROVANIEMI
  static const _rovaniemiTR = '''# Rovaniemi Rehberi: Noel Baba'nın Resmi Evi 🇫🇮

Kutup Dairesi'nin (Arctic Circle) tam üzerinde yer alan Rovaniemi, çocukluk hayallerinin gerçeğe dönüştüğü büyülü bir kış cennetidir.

## 📅 Ne Zaman Gidilir?
- **Aralık-Mart:** Kar garantidir, Noel Baba köyü en süslü halindedir ve Kuzey Işıklarını görme şansı yüksektir.
- **Yaz:** "Gece Yarısı Güneşi"ni yaşamak için Haziran-Temmuz aylarında gidin; güneş hiç batmaz.

## 🏘️ Gezilecek Yerler
- **Santa Claus Village:** Noel Baba ile tanışabileceğiniz, geyikleri besleyebileceğiniz ve "Kutup Dairesini Geçtim" sertifikası alabileceğiniz köy.
- **Arktikum Müzesi:** Kuzey kutbu yaşamını ve tarihini anlatan, mimarisiyle büyüleyen cam tünelli müze.
- **Ranua Hayvanat Bahçesi:** Kutup ayılarını ve diğer arktik hayvanları doğal ortamlarında görebileceğiniz vahşi yaşam parkı.

## 🍽️ Ne Yenir ve İçilir?
- **Geyik Eti (Poronkäristys):** Laponya mutfağının temelidir. Patates püresi ve yaban mersini reçeli ile sote olarak servis edilir.
- **Leipäjuusto:** "Gıcırtılı peynir" olarak da bilinir. Fırınlanmış bu peynir, sıcakken bulutberry (cloudberry) reçeli ile yenir.

## 💎 Lokal Sırlar & İpuçları
- **Kuzey Işıkları (Aurora):** Şehir ışıklarından uzaklaşın. Donmuş nehir yatağı veya [Ounasvaara](search:Ounasvaara) tepesi izlemek için güzel noktalardır.
- **Husky Safari:** Karlı ormanlarda husky köpeklerinin çektiği kızaklarla gezmek, hayatınızda yapacağınız en heyecanlı aktivitelerden biri olacak.
- **Soğuk:** Termal içlik, yün kazak ve kar tulumu zorunludur. Hava -30 dereceleri görebilir!''';

  static const _rovaniemiEN = '''# Rovaniemi Guide: The Official Hometown of Santa Claus 🇫🇮

Located right on the Arctic Circle, Rovaniemi is a magical winter wonderland where childhood dreams come true.

## 📅 Best Time to Visit
- **December-March:** Snow is guaranteed, Santa Claus Village is at its festive peak, and chances of seeing Northern Lights are high.
- **Summer:** Visit in June-July to experience the "Midnight Sun"—the sun never sets!

## 🏘️ Places to Visit
- **Santa Claus Village:** Meet Santa himself, feed the reindeer, and get your certificate for crossing the Arctic Circle.
- **Arktikum Museum:** A stunning museum with a glass tunnel, dedicated to the history and life of the Arctic region.
- **Ranua Wildlife Park:** See polar bears and other arctic animals in a natural forest setting.

## 🍽️ Food & Drink
- **Reindeer Meat (Poronkäristys):** A staple of Lapland cuisine. Sautéed reindeer served with mashed potatoes and lingonberry jam.
- **Leipäjuusto:** Known as "squeaky cheese." This baked cheese is best eaten warm with cloudberry jam.

## 💎 Local Secrets & Insights
- **Northern Lights (Aurora):** Get away from city lights. The frozen riverbed or [Ounasvaara](search:Ounasvaara) hill are great viewing spots.
- **Husky Safari:** Sledding through snowy forests pulled by a team of huskies is an adrenaline rush you won't forget.
- **The Cold:** Thermal layers, wool sweaters, and snowsuits are mandatory. Temperatures can drop to -30°C!''';

  // TROMSO
  static const _tromsoTR = '''# Tromsø Rehberi: Kuzeyin Paris'i 🇳🇴

Kutup dairesinin 350 km kuzeyinde yer alan Tromsø, canlı şehir hayatını vahşi arktik doğa ile birleştiren kozmopolit bir merkezdir.

## 📅 Ne Zaman Gidilir?
- **Eylül-Mart:** Kuzey Işıkları avı için en iyi sezon.
- **Ocak:** Uluslararası Film Festivali ve caz festivalleriyle şehir karanlığına rağmen çok canlıdır.

## 🏘️ Gezilecek Yerler
- **Arktik Katedral:** Şehrin simgesi olan bu modern kilise, buzdağlarından esinlenerek tasarlanmıştır.
- **Fjellheisen Teleferiği:** Storsteinen dağına çıkın. Şehrin adalar üzerindeki konumu ve gece manzarası büyüleyicidir.
- **Polaria:** Kutup yaşamını interaktif şekilde anlatan akvaryum ve müze.

## 🍽️ Ne Yenir ve İçilir?
- **Deniz Mahsulleri:** Kral Yengeç ve karides burada yiyebileceğiniz en taze halindedir.
- **Møsbrømlefse:** Tatlı kahverengi peynir, ekşi krema ve tereyağı ile doldurulan geleneksel bir hamur işi.

## 💎 Lokal Sırlar & İpuçları
- **Balina Safarisi:** Kasım-Ocak arası fiyortlara gelen kambur balinaları ve orkaları görmek için turlara katılın.
- **Gece Hayatı:** Tromsø, kişi başına düşen pub sayısıyla ünlüdür. *Ølhallen*, şehrin en eski pubıdır ve 70'ten fazla bira çeşidi sunar.
- **Polar Gece:** Kasım sonundan Ocak ortasına kadar güneş hiç doğmaz; ancak "mavi saatler" (alacakaranlık) şehre mistik bir hava katar.''';

  static const _tromsoEN = '''# Tromsø Guide: The Paris of the North 🇳🇴

Located 350 km north of the Arctic Circle, Tromsø is a cosmopolitan hub that blends vibrant city life with wild arctic nature.

## 📅 Best Time to Visit
- **September-March:** The prime season for Northern Lights hunting.
- **January:** Despite the darkness, the city is alive with the International Film Festival and jazz festivals.

## 🏘️ Places to Visit
- **Arctic Cathedral:** The city's landmark. A modern church inspired by icebergs and winter landscapes.
- **Fjellheisen Cable Car:** Take a ride up Mt. Storsteinen. The view of the city glowing on the islands below is mesmerizing.
- **Polaria:** An interactive aquarium and museum dedicated to arctic life.

## 🍽️ Food & Drink
- **Seafood:** King Crab and Arctic prawns are fresher here than anywhere else.
- **Møsbrømlefse:** A traditional flatbread filled with sweet brown cheese, sour cream, and butter.

## 💎 Local Secrets & Insights
- **Whale Safari:** Join a boat tour between November and January to see humpback whales and orcas in the fjords.
- **Nightlife:** Tromsø is famous for having more pubs per capita than any other Norwegian city. *Ølhallen* is the oldest pub, serving 70+ types of beer.
- **Polar Night:** From late November to mid-January, the sun never rises. However, the "blue hour" twilight casts a mystical glow over the city.''';

  // EDINBURGH
  static const _edinburghTR = '''# Edinburgh Rehberi: Gotik, Gizemli ve Büyüleyici 🏴󠁧󠁢󠁳󠁣󠁴󠁿

Edinburgh, sönmüş bir yanardağın üzerine kurulu kalesi, yeraltı şehirleri ve gayda sesleriyle dünyada eşi benzeri olmayan bir atmosfere sahiptir.

## 📅 Ne Zaman Gidilir?
- **Ağustos (Fringe Festivali):** Dünyanın en büyük sanat festivali. Şehir tiyatro, komedi ve müzikle dolup taşar ama konaklama bulmak çok zordur.
- **Yılbaşı (Hogmanay):** Dünyanın en büyük yılbaşı partilerinden biri burada yapılır.

## 🏘️ Semt Rehberi
- **Old Town (Eski Şehir):** Kraliyet Yolu (Royal Mile), kale ve daracık geçitler (Close). Harry Potter'a ilham veren sokaklar buradadır.
- **New Town (Yeni Şehir):** Gürcü mimarisi, geniş caddeler ve lüks mağazalar. "Yeni" dendiğine bakmayın, 250 yıllıktır!
- **Leith:** Liman bölgesi. Şimdi Michelin yıldızlı restoranlar ve havalı barlarla dolu.

## 🍽️ Ne Yenir ve İçilir?
- **Haggis:** İskoçyanın milli yemeği. Sakatat, yulaf ve baharatlarla yapılır. Önyargılı olmayın, tadı çok baharatlı bir kıymaya benzer!
- **Viski:** Bir "Scotch" tatmadan dönmek olmaz. *The Scotch Whisky Experience* müzesi iyi bir başlangıçtır.
- **Shortbread:** Tereyağlı İskoç kurabiyesi. Çay veya kahve yanına mükemmel gider.

## 💎 Lokal Sırlar & İpuçları
- [Arthur’s Seat](search:Arthur’s Seat): Şehrin ortasındaki bu sönmüş yanardağa tırmanın. 45 dakikalık yürüyüşle tüm şehri ayaklarınızın altında göreceksiniz.
- **Hayalet Turları:** Edinburgh dünyanın en "perili" şehirlerinden biridir. *[Mary King's Close](search:Mary King's Close)* gibi yeraltı turlarına katılın.
- [Victoria Street](search:Victoria Street): Renkli dükkanlarıyla meşhur bu kıvrımlı sokak, Harry Potter'daki *Diagon Yolu*nun gerçek hayattaki karşılığıdır.''';

  static const _edinburghEN = '''# Edinburgh Guide: Gothic, Mysterious & Enchanting 🏴󠁧󠁢󠁳󠁣󠁴󠁿

Dominated by a castle atop an extinct volcano, filled with underground vaults and the sound of bagpipes, Edinburgh has an atmosphere unlike anywhere else.

## 📅 Best Time to Visit
- **August (Fringe Festival):** The world's largest arts festival. Every street corner becomes a stage, but accommodation is scarce.
- **New Year (Hogmanay):** One of the biggest and most famous New Year's Eve street parties in the world.

## 🏘️ Neighborhood Guide
- **Old Town:** The Royal Mile, the Castle, and narrow alleyways ("Closes"). These streets inspired Harry Potter.
- **New Town:** Georgian architecture, wide squares, and upscale shopping. Don't let the name fool you; it's 250 years old!
- **Leith:** The harbor district. Once gritty, now a hub for Michelin-starred dining and cool bars.

## 🍽️ Food & Drink
- **Haggis:** The national dish of Scotland. Made with sheep's pluck, oats, and spices. Don't be biased; it tastes like a savory, spicy mince!
- **Whisky:** You can't leave without tasting a "Scotch." *The Scotch Whisky Experience* is a great place to start.
- **Shortbread:** Rich, buttery Scottish biscuits. Perfect with afternoon tea.

## 💎 Local Secrets & Insights
- [Arthur’s Seat](search:Arthur’s Seat): Hike up this extinct volcano right in the city center. A 45-minute walk rewards you with panoramic views of the entire city and sea.
- **Ghost Tours:** Edinburgh is one of the most haunted cities in the world. Join a tour of the underground vaults like *[Mary King's Close](search:Mary King's Close)*.
- [Victoria Street](search:Victoria Street): With its colorful shopfronts and curved cobblestones, this street is the real-life inspiration for *Diagon Alley*.''';

  // BRUKSEL
  static const _brukselTR = '''# Brüksel Rehberi: Avrupa'nın Çikolata Başkenti 🇧🇪

Avrupa Birliği'nin başkenti Brüksel, ciddi siyasi yüzünün altında eğlenceli, çikolata kokulu ve çizgi roman dolu bir dünya saklar.

## 📅 Ne Zaman Gidilir?
- **Yaz:** Parklarda piknik yapmak ve festivaller için en iyi zaman.
- **Aralık:** Grand Place'deki ışık şovları ve Noel pazarı büyüleyicidir.

## 🏘️ Gezilecek Yerler
- **Grand Place:** Dünyanın en güzel meydanlarından biri. Altın yaldızlı lonca binalarına hayran kalacaksınız.
- **Atomium:** Brüksel'in "Eyfel Kulesi". Fütüristik, dev metal küreler ve harika bir manzara.
- **Sablon:** Antikacılar ve en lüks çikolatacıların bulunduğu nezih mahalle.

## 🍽️ Ne Yenir ve İçilir?
- **Midye Patates (Moules-Frites):** Tencerede şaraplı veya kremalı pişmiş midye. Yanında mutlaka patates kızartması ve bira ile.
- **Waffle:** Sokaklarda satılan "Gaufre" kokusuna direnmek imkansızdır.
- **Çikolata:** *Pierre Marcolini*, *Neuhaus* veya *Leonidas*. Dünyanın en iyi pralinleri burada.

## 💎 Lokal Sırlar & İpuçları
- **Çizgi Roman Rotası:** Tenten, Şirinler gibi karakterlerin duvar resimlerini takip ederek şehri gezmek çok eğlencelidir.
- [Delirium Café](search:Delirium Café): 2000'den fazla bira çeşidiyle Guinness rekorlar kitabına giren bu bara mutlaka uğrayın.
- **İşeyen Heykeller:** Sadece meşhur işeyen çocuk ([Manneken Pis](search:Manneken Pis)) değil, bir de işeyen kız (Jeanneke Pis) ve işeyen köpek (Zinneke Pis) heykeli vardır; hepsini bulun!''';

  static const _brukselEN = '''# Brussels Guide: The Chocolate Capital of Europe 🇧🇪

The capital of the EU hides a playful, chocolate-scented, and comic-book-loving soul beneath its serious political exterior.

## 📅 Best Time to Visit
- **Summer:** Great for picnics in the parks and outdoor music festivals.
- **December:** The light show at the Grand Place and the Christmas markets are magical.

## 🏘️ Places to Visit
- **Grand Place:** One of the most beautiful squares in the world, surrounded by opulent guildhalls.
- **Atomium:** Brussels' answer to the Eiffel Tower. Futuristic giant spheres offering panoramic views.
- **Sablon:** An elegant neighborhood known for antique shops and luxury chocolatiers.

## 🍽️ Food & Drink
- **Moules-Frites:** Mussels cooked in wine or cream, served with fries and a local beer. The national dish.
- **Waffles:** The smell of fresh waffles ("Gaufre") on the street is irresistible.
- **Chocolate:** *Pierre Marcolini*, *Neuhaus*, or *Leonidas*. The best pralines in the world are here.

## 💎 Local Secrets & Insights
- **Comic Strip Route:** Walking the city by following murals of Tintin, The Smurfs, and other characters is a fun way to explore.
- [Delirium Café](search:Delirium Café): Visit this bar holding the Guinness World Record for offering over 2,000 types of beer.
- **Pissing Statues:** Don't just see the famous [Manneken Pis](search:Manneken Pis); try to find his sister (Jeanneke Pis) and their dog (Zinneke Pis) too!''';

  // BRUGGE
  static const _bruggeTR = '''# Brugge Rehberi: Ortaçağ Masalı 🇧🇪

Kendinizi bir zaman makinesinde hissedeceğiniz Brugge, kanalları, kuğuları ve bozulmamış ortaçağ mimarisiyle tam bir romantizm şehridir.

## 📅 Ne Zaman Gidilir?
- **İlkbahar:** Nergislerin açtığı ve Beguinage bahçesinin en güzel olduğu zaman.
- **Kış:** Sisli kanallar ve sıcak çikolata şehre mistik bir hava katar.

## 🏘️ Gezilecek Yerler
- **Belfry Kulesi:** "In Bruges" filminin yıldızı. 366 basamak çıkın ve çanların yanından şehri izleyin.
- **Rozenhoedkaai:** Brugge'un en çok fotoğrafı çekilen, kartpostallık köşesi.
- **Beguinage:** Beyaz badanalı evleri ve sessizlik kuralıyla rahibelerin yaşadığı huzur dolu bir bölge.

## 🍽️ Ne Yenir ve İçilir?
- **Flemish Stew (Carbonade flamande):** Siyah bira ile pişmiş, yumuşacık dana eti yahnisi.
- **Sıcak Çikolata:** *The Old Chocolate House* gibi yerlerde koca bir kase içinde gelen sıcak çikolataları deneyin.

## 💎 Lokal Sırlar & İpuçları
- **Kanal Turu:** Çok turistiktir ama Brugge'da kanal turu yapmak zorunludur. Şehri su seviyesinden görmek bambaşkadır.
- [Yel Değirmenleri](search:Sint-Janshuismolen): Şehir merkezinin biraz dışına yürüyerek tarihi yel değirmenlerinin olduğu parka gidin.
- **Dantel:** Brugge danteli meşhurdur ama gerçek el yapımı olanları pahalıdır; ucuz olanlar fabrikasyondur, dikkat edin.''';

  static const _bruggeEN = '''# Bruges Guide: A Medieval Fairytale 🇧🇪

Bruges feels like a time machine. With its canals, swans, and untouched medieval architecture, it is the ultimate romantic destination.

## 📅 Best Time to Visit
- **Spring:** When daffodils bloom, and the Beguinage garden is at its most beautiful.
- **Winter:** Misty canals and hot chocolate give the city a mystical vibe.

## 🏘️ Places to Visit
- **Belfry Tower:** The star of the movie "In Bruges." Climb 366 steps to see the city from above the bells.
- **Rozenhoedkaai:** The most photographed, postcard-perfect corner of Bruges.
- **Beguinage:** A peaceful, enclosed community of white houses and silence, formerly home to Beguines.

## 🍽️ Food & Drink
- **Flemish Stew (Carbonade flamande):** A rich beef stew cooked in dark beer, melt-in-the-mouth delicious.
- **Hot Chocolate:** Try the massive bowls of hot chocolate at spots like *The Old Chocolate House*.

## 💎 Local Secrets & Insights
- **Canal Boat Tour:** It's touristy, but mandatory. Seeing the medieval facades from the water is a unique perspective.
- [Windmills](search:Sint-Janshuismolen): Walk to the edge of the city center to find a row of historic windmills set in a grassy park.
- **Lace:** Bruges lace is famous. Be aware that real handmade lace is expensive; cheap versions are machine-made.''';

  // STRAZBURG
  static const _strazburgTR = '''# Strazburg Rehberi: Fransız ve Alman Aşkı 🇫🇷

Fransa ile Almanya sınırında, her iki kültürün en güzel özelliklerini almış masalsı bir şehir. Noel'in başkenti!

## 📅 Ne Zaman Gidilir?
- **Aralık:** Tartışmasız en iyi zaman. Strazburg Noel Pazarı, Avrupa'nın en eskisi ve en güzelidir.
- **Bahar:** Ren nehrinin kolları boyunca çiçekler açtığında şehir çok romantiktir.

## 🏘️ Gezilecek Yerler
- **Petite France:** Kanalların, yarı ahşap evlerin ve değirmenlerin olduğu eski tabakhaneler bölgesi.
- **Strazburg Katedrali:** Victor Hugo'nun "dev ve narin bir harika" dediği, tek kuleli gotik şaheser.
- **Avrupa Parlamentosu:** Modern yüzü. Tekne turları buradan da geçer.

## 🍽️ Ne Yenir ve İçilir?
- **Choucroute:** Lahana turşusu ve sosis çeşitleriyle yapılan Alsas klasiği.
- **Tarte Flambée (Flammekueche):** İncecik hamur üzerine krema, soğan ve pastırma. Pizza gibi ama daha hafif.
- **Kugelhopf:** Kuru üzümlü ve bademli, kalıpta pişen geleneksel kek.

## 💎 Lokal Sırlar & İpuçları
- [Astronomik Saat](search:Strasbourg Cathedral): Katedralin içindeki saat her gün 12:30'da (biletli) figürlerini hareket ettirerek bir şov yapar.
- [Vauban Barajı (Barrage Vauban)](search:Barrage Vauban): Ücretsiz olarak çatısına çıkın ve Petite France'ın en güzel panoramik fotoğrafını çekin.
- **Bisiklet:** Strazburg Fransa'nın en bisiklet dostu şehridir; bir bisiklet kiralayıp kanalları takip edin.''';

  static const _strazburgEN = '''# Strasbourg Guide: A French-German Romance 🇫🇷

Sitting on the border of France and Germany, Strasbourg takes the best of both cultures. It is arguably the Capital of Christmas.

## 📅 Best Time to Visit
- **December:** Undisputedly the best time. The Strasbourg Christmas Market is the oldest and most beautiful in Europe.
- **Spring:** When flowers bloom along the Rhine tributaries, the city is incredibly romantic.

## 🏘️ Places to Visit
- **Petite France:** The picturesque district of tanners with canals, half-timbered houses, and covered bridges.
- **Strasbourg Cathedral:** Called a "gigantic and delicate marvel" by Victor Hugo, this single-towered Gothic masterpiece is stunning.
- **European Parliament:** The modern face of the city, visible from river boat tours.

## 🍽️ Food & Drink
- **Choucroute:** The Alsatian classic of sauerkraut served with various sausages and meats.
- **Tarte Flambée (Flammekueche):** Thin dough topped with crème fraîche, onions, and bacon. Like pizza, but lighter.
- **Kugelhopf:** A traditional bundt cake with raisins and almonds.

## 💎 Local Secrets & Insights
- [Astronomical Clock](search:Strasbourg Cathedral): Inside the cathedral, the clock puts on a mechanical show with moving figures every day at 12:30 PM (ticket required).
- [Vauban Dam (Barrage Vauban)](search:Barrage Vauban): Climb to the roof terrace (free) for the best panoramic photo of Petite France and the covered bridges.
- **Cycling:** Strasbourg is France's most bike-friendly city; rent a bike and follow the canal paths.''';

  // HEIDELBERG
  static const _heidelbergTR = '''# Heidelberg Rehberi: Romantizmin Başkenti 🇩🇪

Neckar nehri kıyısında, tepedeki kızıl kalesi ve dünyanın en eski üniversitelerinden biriyle Heidelberg, Alman romantizminin simgesidir.

## 📅 Ne Zaman Gidilir?
- **Sonbahar:** Ormanların kızıla döndüğü ve sisli nehir manzarasının en etkileyici olduğu dönem.
- **Yaz:** Kale festivalleri ve havai fişek gösterileri (şato aydınlatması) zamanı.

## 🏘️ Gezilecek Yerler
- **Heidelberg Kalesi:** Şehre tepeden bakan bu devasa harabe, dünyanın en büyük şarap fıçısına ev sahipliği yapar.
- **Eski Köprü (Alte Brücke):** Kale manzaralı ikonik taş köprü. Kapısındaki maymun heykeline dokunmak şans getirir!
- **Filozoflar Yolu (Philosophenweg):** Nehrin karşı kıyısında, şairlerin ve profesörlerin yürüdüğü, en iyi şehir manzarasına sahip yol.

## 🍽️ Ne Yenir ve İçilir?
- **Öğrenci Barları:** Untere Strasse bölgesi, uygun fiyatlı bira ve canlı ortam sunan tarihi barlarla doludur.
- **Schneeballen:** "Kar topu" tatlısı. Kırarak yenen sert hamurlu bir kurabiye.

## 💎 Lokal Sırlar & İpuçları
- [Hapishane (Studentenkarzer)](search:Studentenkarzer): Üniversitenin yaramaz öğrencileri eskiden buraya hapsedilirmiş. Duvarlardaki yüzyıllık graffitiler çok ilginçtir.
- [Thingstätte](search:Thingstätte): Tepedeki ormanın içinde, Nazi döneminden kalma devasa bir açık hava amfitiyatrosu. Biraz ürkütücü ama etkileyici.''';

  static const _heidelbergEN = '''# Heidelberg Guide: Capital of Romance 🇩🇪

With its red sandstone castle perched above the Neckar River and one of the world's oldest universities, Heidelberg is the symbol of German Romanticism.

## 📅 Best Time to Visit
- **Autumn:** When the forests turn red and gold, and the misty river views are most atmospheric.
- **Summer:** The time for castle festivals and the famous "Castle Illumination" fireworks.

## 🏘️ Places to Visit
- **Heidelberg Castle:** This massive ruin overlooking the city houses the world's largest wine barrel.
- **Old Bridge (Alte Brücke):** The iconic stone bridge. Touching the bronze monkey by the gate is said to bring good luck!
- **Philosophers' Walk (Philosophenweg):** A scenic path on the opposite side of the river where poets and professors walked, offering the best skyline views.

## 🍽️ Food & Drink
- **Student Pubs:** The Untere Strasse area is full of historic pubs offering cheap beer and a lively atmosphere.
- **Schneeballen:** "Snowball" pastry. A hard shortcrust pastry that you smash to eat.

## 💎 Local Secrets & Insights
- [Student Prison (Studentenkarzer)](search:Studentenkarzer): Naughty university students were once locked up here. The century-old graffiti on the walls is fascinating.
- [Thingstätte](search:Thingstätte): Hidden in the forest on the hill, this massive open-air amphitheater from the Nazi era is eerie but impressive.''';

  // COLMAR
  static const _colmarTR = '''# Colmar Rehberi: Masal Kitabından Bir Sayfa 🇫🇷

Alsas Şarap Yolu'nun başkenti Colmar, kanalları ve çiçekli pencereleriyle "Küçük Venedik" olarak anılır. Burası gerçek olamayacak kadar güzeldir.

## 📅 Ne Zaman Gidilir?
- **Noel:** Colmar'ın 6 farklı Noel pazarı şehri bir ışık şölenine çevirir.
- **Bağ Bozumu (Eylül-Ekim):** Şarap severler için en iyi zamandır.

## 🏘️ Gezilecek Yerler
- [La Petite Venise](search:Little Venice Colmar) (Küçük Venedik): Lauch nehri kenarındaki rengarenk evler. Sandalla gezinti yapabilirsiniz.
- [Pfister Evi](search:Maison Pfister): "Howl'un Yürüyen Şatosu" animesine ilham veren, ahşap işlemeli tarihi bina.
- [Unterlinden Müzesi](search:Unterlinden Museum): Eski bir manastırda yer alan önemli bir sanat müzesi.

## 🍽️ Ne Yenir ve İçilir?
- **Alsas Şarapları:** Riesling ve Gewürztraminer şaraplarını yerel mahzenlerde tadın.
- **Pretzel (Bretzel):** Burada her köşe başında devasa, sıcak ve tuzlu pretzeller bulabilirsiniz.

## 💎 Lokal Sırlar & İpuçları
- [Özgürlük Heykeli](search:Statue of Liberty Colmar): New York'taki heykelin heykeltıraşı Bartholdi Colmarlıdır. Şehrin girişindeki 12 metrelik replikayı görünce şaşırmayın.
- **Işıklandırma:** Cuma ve Cumartesi akşamları şehir özel bir sistemle aydınlatılır, gece yürüyüşü yapmayı ihmal etmeyin.''';

  static const _colmarEN = '''# Colmar Guide: A Page from a Fairytale 🇫🇷

The capital of the Alsace Wine Route, Colmar is known as "Little Venice" for its canals and flower-decked windows. It is almost too beautiful to be real.

## 📅 Best Time to Visit
- **Christmas:** Colmar's 6 Christmas markets turn the town into a festival of lights.
- **Harvest (Sept-Oct):** The absolute best time for wine lovers.

## 🏘️ Places to Visit
- [La Petite Venise](search:Little Venice Colmar): Colorful houses lining the Lauch river. You can take a flat-bottomed boat tour here.
- [Maison Pfister](search:Maison Pfister): An ornate wooden house that inspired the anime "Howl's Moving Castle."
- [Unterlinden Museum](search:Unterlinden Museum): An important art museum housed in a former medieval convent.

## 🍽️ Food & Drink
- **Alsace Wines:** Taste Riesling and Gewürztraminer in local cellars ("Caveau").
- **Pretzel (Bretzel):** Giant, warm, salty soft pretzels are available on every corner.

## 💎 Local Secrets & Insights
- [Statue of Liberty](search:Statue of Liberty Colmar): Bartholdi, the sculptor of the Statue of Liberty, was born in Colmar. Don't be surprised to see a 12-meter replica at the town entrance.
- **Illumination:** On Friday and Saturday nights, the city is lit up by a special light design—perfect for a night walk.''';

  // GIETHOORN
  static const _giethoornTR = '''# Giethoorn Rehberi: Sessizliğin Sesi 🇳🇱

"Kuzeyin Venedik'i" denilen Giethoorn'da yol yoktur, araba yoktur. Sadece kanallar, köprüler ve sessiz elektrikli tekneler vardır.

## 📅 Ne Zaman Gidilir?
- **İlkbahar ve Yaz:** En yeşil ve en güzel zamanıdır ama gündüzleri kalabalık olabilir.
- **İpucu:** Kalabalıktan kaçmak için saat 11:00'den önce veya 17:00'den sonra tekne kiralayın.

## 🏘️ Ne Yapılır?
- **Tekne Kiralama (Whisper Boat):** Sessiz motorlu küçük botlardan kiralayıp kendiniz kullanın. Kanallarda kaybolmak çok keyiflidir.
- **Yürüyüş:** "Binnenpad" yolu boyunca yürüyerek saz çatılı çiftlik evlerini ve çiçekli bahçeleri inceleyin.

## 🍽️ Ne Yenir ve İçilir?
- **Kanal Kenarı Restoranları:** *Smit's Paviljoen* gibi su kenarındaki restoranlarda öğle yemeği yiyin.
- **Peynir:** Hollanda peynirlerinin tadına bakabileceğiniz küçük dükkanlar vardır.

## 💎 Lokal Sırlar & İpuçları
- [Müze Çiftlik](search:Museum 't Olde Maat Uus) (Museum 't Olde Maat Uus): 100 yıl önce burada hayatın nasıl olduğunu gösteren, oyuncuların olduğu canlı bir müze.
- **Sessizlik:** Yerel halkın huzuruna saygı gösterin; bahçelerine girmeyin veya yüksek sesle konuşmayın.''';

  static const _giethoornEN = '''# Giethoorn Guide: The Sound of Silence 🇳🇱

Known as the "Venice of the North," Giethoorn has no roads and no cars. Only canals, bridges, and silent electric boats.

## 📅 Best Time to Visit
- **Spring & Summer:** The greenest and most beautiful time, though it can get crowded midday.
- **Tip:** Rent a boat before 11:00 AM or after 5:00 PM to avoid the "boat traffic jams."

## 🏘️ What to Do?
- **Rent a Whisper Boat:** Rent a small electric boat and drive it yourself. Getting lost in the canals is pure joy.
- **Walking:** Stroll along the "Binnenpad" path to admire the thatched-roof farmhouses and flower gardens close up.

## 🍽️ Food & Drink
- **Canalside Dining:** Have lunch at water-edge restaurants like *Smit's Paviljoen*.
- **Cheese:** Visit the small local shops to taste authentic Dutch cheeses.

## 💎 Local Secrets & Insights
- [Museum Farm](search:Museum 't Olde Maat Uus) ('t Olde Maat Uus): A living museum with actors showing what life in Giethoorn was like a century ago.
- **Respect:** Remember people live here. Respect their privacy, stay off private bridges, and keep noise levels down.''';

  // SINTRA
  static const _sintraTR = '''# Sintra Rehberi: Masalsı Bir Kaçış 🇵🇹

Lizbon'un hemen yanı başında, sisli dağların üzerine kurulu sarayları ve egzotik bahçeleriyle Sintra, UNESCO Dünya Mirası listesimdedir. Lord Byron burayı "Muhteşem Cennet" olarak tanımlamıştır.

## 📅 Ne Zaman Gidilir?
- **İlkbahar:** Bahçelerin en renkli olduğu, havanın yürüyüşe uygun olduğu zaman.
- **Sonbahar:** Sisler içindeki Pena Sarayı daha da mistik görünür.
- **İpucu:** Yazın çok kalabalıktır, erken gitmeye çalışın.

## 🏘️ Gezilecek Yerler
- [Pena Sarayı](search:Pena Palace) (Palácio da Pena): Sarı ve kırmızı renkli, Disney şatolarını andıran zirvedeki saray.
- [Quinta da Regaleira](search:Quinta da Regaleira): Gotik mimarisi, gizli geçitleri ve meşhur "Başlangıç Kuyusu" (Initiation Well) ile burası bir labirenttir.
- [Mağribi Kalesi](search:Castelo dos Mouros) (Castelo dos Mouros): Tepelere yayılan surlarda yürüyerek okyanusu ve sarayları izleyin.

## 🍽️ Ne Yenir ve İçilir?
- **Travesseiro:** "Yastık" anlamına gelen, badem kremalı milföy tatlısı. *Piriquita* pastanesinde yiyin.
- **Queijada:** Peynir, yumurta, süt ve şekerle yapılan küçük tart.

## 💎 Lokal Sırlar & İpuçları
- [Monserrate Sarayı](search:Monserrate Palace): Kalabalıktan kaçmak için buraya gidin. Arap ve Gotik mimari karışımı sarayı ve botanik bahçesi çok huzurludur.
- **Ulaşım:** Sintra'da araba park etmek kabustur. Lizbon'dan trenle gelin ve içeride otobüs (434 hattı) kullanın.''';

  static const _sintraEN = '''# Sintra Guide: A Fairytale Escape 🇵🇹

Just outside Lisbon, with its palaces perched on misty peaks and exotic gardens, Sintra is a UNESCO World Heritage site described by Lord Byron as a "Glorious Eden."

## 📅 Best Time to Visit
- **Spring:** When gardens bloom and the weather is perfect for hiking.
- **Autumn:** The misty atmosphere makes Pena Palace look even more mystical.
- **Tip:** It gets very crowded in summer; try to arrive early.

## 🏘️ Places to Visit
- [Pena Palace](search:Pena Palace): The yellow and red romanticist castle on the peak that looks like it's straight out of Disney.
- [Quinta da Regaleira](search:Quinta da Regaleira): A gothic estate filled with secret tunnels, grottoes, and the famous "Initiation Well."
- [Moorish Castle](search:Castle of the Moors): Walk along the ancient walls for breathtaking views of the ocean and palaces.

## 🍽️ Food & Drink
- **Travesseiro:** Meaning "pillow," this puff pastry filled with almond cream is a local legend. Try it at *Piriquita*.
- **Queijada:** A delicious small tart made with fresh cheese, eggs, milk, and sugar.

## 💎 Local Secrets & Insights
- [Monserrate Palace](search:Monserrate Palace): Escape the crowds here. The blend of Arabic and Gothic architecture surrounded by botanical gardens is incredibly peaceful.
- **Transport:** Parking is a nightmare. Take the train from Lisbon and use the bus (line 434) to get around.''';

  // SAN SEBASTIAN
  static const _sanSebastianTR = '''# San Sebastian Rehberi: Lezzet Başkenti 🇪🇸

Bask bölgesinin incisi Donostia (San Sebastian), dünyada metrekareye en çok Michelin yıldızı düşen şehirlerden biridir ve Avrupa'nın en güzel şehir plajına sahiptir.

## 📅 Ne Zaman Gidilir?
- **Yaz:** Plajların keyfini çıkarmak için idealdir.
- **Eylül:** Film Festivali zamanı şehir yıldızlarla dolar.

## 🏘️ Gezilecek Yerler
- [La Concha](search:La Concha Beach): İspanya'nın, hatta Avrupa'nın en güzel şehir plajı. Yarım ay şeklindeki kumsalda yürüyüş yapın.
- **Parte Vieja (Eski Şehir):** Dar sokaklar, kiliseler ve sayısız Pintxos barı burada.
- [Monte Igueldo](search:Monte Igueldo): Fünikülerle tepeye çıkın ve o meşhur koy manzarasını fotoğraflayın.

## 🍽️ Ne Yenir ve İçilir?
- **Pintxos (Pinçoz):** Bask usulü tapas. Barların tezgahlarındaki yüzlerce çeşit arasından seçin. Kürdanları atmayın, hesap kürdan sayısına göre ödenir!
- **Txuleta:** Izgara dana pirzola. Sadece deniz tuzu ile pişirilir, lezzeti etin kalitesindedir.
- **Txakoli:** Bölgeye özgü, hafif gazlı ve asitli beyaz şarap. Yüksekten dökülerek servis edilir.

## 💎 Lokal Sırlar & İpuçları
- **Gastronomi Kulüpleri:** Üye olmadan girilemeyen "Txoko"lar meşhurdur. Bir yerli arkadaş bulup girmeyi deneyin.
- **Sörf:** [Zurriola](search:Zurriola Beach) plajı sörfçülerin mekanıdır; ders alabilir veya izleyebilirsiniz.
- **Cheesecake:** Dünyaca ünlü "San Sebastian Cheesecake"in doğduğu yer *[La Viña](search:La Viña San Sebastian)* restoranıdır. Kuyruk beklemeye değer!''';

  static const _sanSebastianEN = '''# San Sebastian Guide: The Culinary Capital 🇪🇸

Donostia (San Sebastian), the pearl of the Basque Country, holds one of the highest concentrations of Michelin stars per capita in the world and boasts Europe's finest city beach.

## 📅 Best Time to Visit
- **Summer:** Perfect for enjoying the magnificent beaches.
- **September:** The city fills with stars during the International Film Festival.

## 🏘️ Places to Visit
- [La Concha](search:La Concha Beach): Arguably the most beautiful city beach in Europe. Take a stroll along the crescent-shaped bay.
- **Parte Vieja (Old Town):** Narrow streets packed with churches and endless Pintxos bars.
- [Monte Igueldo](search:Monte Igueldo): Take the funicular to the top for the iconic panoramic photo of the bay.

## 🍽️ Food & Drink
- **Pintxos:** Basque tapas. Pick from hundreds of options displayed on bar counters. Keep your toothpicks; the bill is calculated by counting them!
- **Txuleta:** Grilled rib steak. Seasoned simply with sea salt, the flavor comes from the quality of the meat.
- **Txakoli:** A slightly sparkling, acidic white wine poured from a height to aerate it.

## 💎 Local Secrets & Insights
- **Gastronomic Societies:** "Txokos" are private dining clubs. Try to befriend a local to get invited inside.
- **Surf:** [Zurriola](search:Zurriola Beach) beach is the surfer's spot; take a lesson or watch the pros.
- **Cheesecake:** The birthplace of the world-famous "San Sebastian Cheesecake" is *[La Viña](search:La Viña San Sebastian)*. It's worth waiting in line!''';

  // BOLOGNA
  static const _bolognaTR = '''# Bologna Rehberi: Kızıl, Bilge ve Şişman 🇮🇹

İtalya'nın yemek başkenti. "Kızıl" (tuğla binaları ve solcu geleneği), "Bilge" (en eski üniversite) ve "Şişman" (zengin mutfağı) lakaplarıyla bilinir.

## 📅 Ne Zaman Gidilir?
- **İlkbahar ve Sonbahar:** Yürüyerek keşfetmek için ideal sıcaklıklar.
- **Yaz:** Çok sıcak ve nemli olabilir.

## 🏘️ Gezilecek Yerler
- [Piazza Maggiore](search:Piazza Maggiore): Şehrin kalbi. San Petronio Bazilikası ve Neptün Çeşmesi buradadır.
- [İki Kule](search:Two Towers Bologna) (Due Torri): Şehrin sembolü olan bu eğik kulelerden Asinelli'ye (498 basamak) çıkıp manzarayı izleyin.
- **Portikolar:** UNESCO listesindeki 40 km'lik revaklar (kemerli yollar) sayesinde yağmurda bile ıslanmadan tüm şehri gezebilirsiniz.

## 🍽️ Ne Yenir ve İçilir?
- **Tagliatelle al Ragù:** Bizim "Bolonez soslu makarna" dediğimiz şeyin aslı. Spagetti ile değil, yumurtalı taze tagliatelle ile yenir.
- **Mortadella:** Bologna'nın meşhur büyük sosis/salamı. Sandviç içinde harikadır.
- **Tortellini in Brodo:** Et suyunda servis edilen minik, dolgulu makarnalar.

## 💎 Lokal Sırlar & İpuçları
- [San Luca](search:Sanctuary of the Madonna di San Luca): Şehir merkezinden başlayıp tepeye kadar uzanan dünyanın en uzun portikosunu (3.8 km) yürüyün.
- [Venedik Penceresi](search:Finestrella): Via Piella'daki küçük pencereden bakınca, binaların arasındaki gizli kanalı görüp kendinizi Venedik'te zannedersiniz.
- [Eski Üniversite](search:Archiginnasio of Bologna): Archiginnasio sarayındaki eski anatomi tiyatrosunu (tamamen ahşap) mutlaka görün.''';

  static const _bolognaEN = '''# Bologna Guide: The Red, The Learned, The Fat 🇮🇹

Italy's food capital. Nicknamed "The Red" (brick buildings), "The Learned" (oldest university), and "The Fat" (rich cuisine).

## 📅 Best Time to Visit
- **Spring & Autumn:** Ideal temperatures for walking around.
- **Summer:** Can be very hot and humid.

## 🏘️ Places to Visit
- [Piazza Maggiore](search:Piazza Maggiore): The heart of the city, flanked by San Petronio Basilica and the Fountain of Neptune.
- [Two Towers](search:Two Towers Bologna) (Due Torri): Climb the Asinelli Tower (498 steps) for a stunning view. These leaning towers are the city's symbol.
- **Porticoes:** Thanks to 40 km of UNESCO-listed arcades, you can walk the entire city without getting wet in the rain.

## 🍽️ Food & Drink
- **Tagliatelle al Ragù:** The original "Bolognese." Never eaten with spaghetti, but with fresh egg tagliatelle.
- **Mortadella:** Bologna's famous giant cured sausage. Delicious in a sandwich.
- **Tortellini in Brodo:** Tiny stuffed pasta served in a rich meat broth.

## 💎 Local Secrets & Insights
- [San Luca](search:Sanctuary of the Madonna di San Luca): Walk the world's longest portico (3.8 km) from the city center up to the Sanctuary on the hill.
- [Venice Window](search:Finestrella): Look through the small window on Via Piella to see a hidden canal flowing between buildings—a glimpse of Venice.
- [Old University](search:Archiginnasio of Bologna): Visit the Archiginnasio and see the stunning wooden Anatomical Theatre.''';

  // MATERA
  static const _materaTR = '''# Matera Rehberi: Taşların Şehri 🇮🇹

Tarih öncesi çağlardan beri yerleşim olan Matera, kayalara oyulmuş evleri (Sassi) ile benzersizdir. Bir zamanlar İtalya'nın "utancı" iken, şimdi gururu olmuştur.

## 📅 Ne Zaman Gidilir?
- **İlkbahar:** Kır çiçekleri ve yumuşak hava.
- **Kış:** Noel zamanı burası canlı bir "doğuş sahnesi"ne (Nativity Scene) dönüşür.

## 🏘️ Gezilecek Yerler
- [Sassi di Matera](search:Sassi di Matera): Sasso Caveoso ve Sasso Barisano bölgelerinde kaybolun. Mağara kiliseleri ve evleri inceleyin.
- [Kaya Kiliseleri](search:Rupestrian Churches Matera): Santa Maria de Idris gibi kayanın içine oyulmuş ve fresklerle süslü kiliseler büyüleyicidir.
- [Palombaro Lungo](search:Palombaro Lungo): Şehrin altındaki devasa tarihi su sarnıcı. Bir film setini andırır.

## 🍽️ Ne Yenir ve İçilir?
- **Pane di Matera:** İtalya'nın en iyi ekmeklerinden biri. Sert kabuklu, içi yumuşacık durum buğdayı ekmeği.
- **Peperoni Cruschi:** Kurutulup kızartılmış, cips gibi yenen tatlı kırmızı biberler.

## 💎 Lokal Sırlar & İpuçları
- [Belvedere](search:Belvedere Murgia Timone): Şehri karşıdan, Murgia Parkı tarafından gün batımında izleyin. Işıklar yanınca şehir büyülü görünür.
- **Konaklama:** Mutlaka bir "mağara otel"de kalın. İçi lüks ama duvarları binlerce yıllık taş olan odalar unutulmazdır.
- **Film Seti:** James Bond "No Time to Die" ve Mel Gibson'ın "Passion of the Christ" filmleri burada çekilmiştir.''';

  static const _materaEN = '''# Matera Guide: City of Stone 🇮🇹

Inhabited since prehistoric times, Matera is unique for its cave dwellings (Sassi). Once Italy's "shame," it is now its pride.

## 📅 Best Time to Visit
- **Spring:** Wildflowers and mild weather.
- **Winter:** At Christmas, the city transforms into a living Nativity Scene.

## 🏘️ Places to Visit
- [Sassi di Matera](search:Sassi di Matera): Get lost in Sasso Caveoso and Sasso Barisano. Explore the cave houses and ancient dwellings.
- [Rupestrian Churches](search:Rupestrian Churches Matera): Rock-hewn churches like Santa Maria de Idris, decorated with ancient frescoes.
- [Palombaro Lungo](search:Palombaro Lungo): A massive historic water cistern under the city that looks like a cathedral.

## 🍽️ Food & Drink
- **Pane di Matera:** One of Italy's best breads. Crunchy crust, soft inside, made from durum wheat.
- **Peperoni Cruschi:** Dried and fried sweet red peppers, eaten like chips.

## 💎 Local Secrets & Insights
- [Belvedere](search:Belvedere Murgia Timone): View the city from the Murgia Park side at sunset. When the lights come on, it's magical.
- **Accommodation:** You must stay in a "cave hotel." Sleeping in a room carved into rock but with modern luxury is unforgettable.
- **Film Set:** Films like James Bond's "No Time to Die" and Mel Gibson's "Passion of the Christ" were shot here.''';

  // SANTORINI
  static const _santoriniTR = '''# Santorini Rehberi: Gün Batımı Rüyası 🇬🇷

Volkanik bir patlama sonucu oluşan hilal şeklindeki ada; beyaz badanalı evleri, mavi kubbeleri ve sonsuz Ege mavisiyle dünyanın en romantik yerlerinden biridir.

## 📅 Ne Zaman Gidilir?
- **Mayıs-Haziran ve Eylül:** Hava güzeldir, kalabalıklar Temmuz-Ağustos kadar boğucu değildir.
- **İpucu:** Kışın birçok otel ve restoran kapalı olabilir.

## 🏘️ Köy Rehberi
- [Oia](search:Oia Santorini): O meşhur gün batımı ve mavi kubbelerin olduğu lüks köy.
- [Fira](search:Fira Santorini): Adanın başkenti. Alışveriş, gece hayatı ve teleferik burada.
- [Pyrgos](search:Pyrgos Santorini): Adanın en yüksek ve daha az turistik, geleneksel köyü.

## 🍽️ Ne Yenir ve İçilir?
- **Fava:** Santorini'ye özgü sarı mercimekten yapılan meze.
- **Domatokeftedes:** Adanın susuz tarımla yetişen küçük domateslerinden yapılan mücver.
- **Vinsanto:** Volkanik topraktaki üzümlerden yapılan tatlı şarap.

## 💎 Lokal Sırlar & İpuçları
- **Yürüyüş Rotası:** Fira'dan Oia'ya kraterin kenarından (Caldera) yapılan 10 km'lik yürüyüş, dünyanın en güzel manzaralı rotalarından biridir.
- [Ammoudi Körfezi](search:Ammoudi Bay): Oia'nın altındaki bu küçük limana 300 basamak inin; taze balık yiyin ve kayalardan denize girin.
- [Kızıl Plaj (Red Beach)](search:Red Beach Santorini): Kırmızı volkanik kayalarla çevrili plajı görmeden dönmeyin.''';

  static const _santoriniEN = '''# Santorini Guide: A Sunset Dream 🇬🇷

Formed by a volcanic eruption, this crescent-shaped island with its whitewashed houses and blue domes is one of the most romantic places on earth.

## 📅 Best Time to Visit
- **May-June & September:** Weather is great, and crowds are manageable compared to peak summer.
- **Tip:** Many hotels and restaurants close during winter.

## 🏘️ Village Guide
- [Oia](search:Oia Santorini): The famous village with the sunset views and blue domes.
- [Fira](search:Fira Santorini): The capital. Hub for shopping, nightlife, and the cable car.
- [Pyrgos](search:Pyrgos Santorini): The highest village, more traditional and less touristy.

## 🍽️ Food & Drink
- **Fava:** A creamy puree made from yellow split peas native to the island.
- **Tomatokeftedes:** Tomato fritters made from the island's unique cherry tomatoes.
- **Vinsanto:** A sweet dessert wine made from grapes grown in volcanic soil.

## 💎 Local Secrets & Insights
- **Hiking:** The 10km hike from Fira to Oia along the caldera edge offers the most spectacular views imaginable.
- [Ammoudi Bay](search:Ammoudi Bay): Walk down 300 steps from Oia to this tiny port for fresh seafood and swimming off the rocks.
- [Red Beach](search:Red Beach Santorini): Don't miss the unique beach surrounded by towering red volcanic cliffs.''';

  // KAHIRE
  static const _kahireTR = '''# Kahire Rehberi: Kaosun ve Tarihin Şehri 🇪🇬

Piramitlerin gölgesinde, İslami mimari, korna sesleri, baharat kokuları ve Nil nehrinin sakinliği... Kahire tüm duyularınıza aynı anda saldırır.

## 📅 Ne Zaman Gidilir?
- **Ekim-Nisan:** Hava gezmek için idealdir. Yazın sıcaklık dayanılmaz olabilir.

## 🏘️ Gezilecek Yerler
- [Giza Piramitleri ve Sfenks](search:Giza Necropolis): Dünyanın yedi harikasından ayakta kalan tek yapı. Şehrin hemen kıyısındadır.
- [Mısır Müzesi](search:Egyptian Museum): Tutankamon'un hazineleri ve mumyalar burada. (Yeni Büyük Mısır Müzesi'ni de kontrol edin).
- [Han el-Halili](search:Khan el-Khalili): Ortaçağdan kalma devasa çarşı. Baharat, lamba ve hediyelik eşya cenneti.

## 🍽️ Ne Yenir ve İçilir?
- **Koshary:** Mısır'ın milli yemeği. Pirinç, makarna, mercimek, nohut ve kızarmış soğanın domates sosuyla karışımı. Karbonhidrat bombası!
- **Falafel (Ta'meya):** Mısır'da bakla ile yapılır ve kahvaltıda yenir.
- **Türk Kahvesi:** Burada da çok popülerdir, genellikle kakuleli yapılır.

## 💎 Lokal Sırlar & İpuçları
- **Nil Gezisi:** Akşam saatlerinde bir "Felucca" (yelkenli) kiralayıp Nil üzerinde gün batımını izleyin; şehrin gürültüsünden uzaklaşın.
- **Uber:** Taksilerle pazarlık yapmak zor olabilir, Uber kullanmak hayat kurtarır.
- **Bahşiş (Baksheesh):** Mısır'da her hizmet için bahşiş beklenir, cebinizde bozuk para bulundurun.''';

  static const _kahireEN = '''# Cairo Guide: City of Chaos and History 🇪🇬

In the shadow of the Pyramids, Cairo assaults all your senses with Islamic architecture, car horns, spice scents, and the calmness of the Nile.

## 📅 Best Time to Visit
- **October-April:** The weather is pleasant. Summer heat can be unbearable.

## 🏘️ Places to Visit
- [Pyramids of Giza & Sphinx](search:Giza Necropolis): The only surviving wonder of the ancient world. Located right on the edge of the city.
- [Egyptian Museum](search:Egyptian Museum): Home to Tutankhamun's treasures. (Check if the new Grand Egyptian Museum is open).
- [Khan el-Khalili](search:Khan el-Khalili): A massive medieval bazaar. Heaven for spices, lamps, and souvenirs.

## 🍽️ Food & Drink
- **Koshary:** Egypt's national dish. A mix of rice, pasta, lentils, chickpeas, and fried onions topped with tomato sauce. A carb bomb!
- **Falafel (Ta'meya):** Made with fava beans in Egypt and often eaten for breakfast.
- **Turkish Coffee:** Very popular here, usually brewed with cardamom.

## 💎 Local Secrets & Insights
- **Nile Cruise:** Rent a "Felucca" (sailboat) at sunset. Sailing on the Nile is the best way to escape the city noise.
- **Uber:** Haggling with taxis can be exhausting; using Uber is a lifesaver.
- **Tipping (Baksheesh):** Tipping is expected for almost everything. Keep small change handy.''';

  // FES
  static const _fesTR = '''# Fes Rehberi: Ortaçağ Labirenti 🇲🇦

Dünyanın en büyük trafiğe kapalı şehirsel alanı olan Fes el-Bali (Eski Fes), zamanda yolculuk gibidir. 9000'den fazla dar sokakta kaybolmaya hazır olun.

## 📅 Ne Zaman Gidilir?
- **İlkbahar:** En ideal zamandır.
- **İpucu:** Fes Müzik Festivali zamanı şehir çok canlıdır.

## 🏘️ Gezilecek Yerler
- [Tabakhaneler](search:Chouara Tannery) (Chouara Tannery): Yüzyıllardır aynı ilkel yöntemlerle deri boyanan dev kuyular. Kokuya hazırlıklı olun (nane yaprağı koklayın)!
- [Al Quaraouiyine](search:Al Quaraouiyine): Dünyanın en eski üniversitesi kabul edilir. Cami ve kütüphanesi muazzamdır.
- [Bou Inania Medresesi](search:Bou Inania Madrasa): İslami mimarinin, ahşap oymacılığının ve çini sanatının zirvesi.

## 🍽️ Ne Yenir ve İçilir?
- **Tagine:** Kuskus ve etin o meşhur konik kaplarda ağır ağır pişmesi.
- **Pastilla:** Yufka içinde güvercin veya tavuk eti, badem ve şekerin garip ama lezzetli uyumu.
- **Nane Çayı:** "Fas Viskisi". Her yerde, her zaman bol şekerli ikram edilir.

## 💎 Lokal Sırlar & İpuçları
- **Rehber:** Medine (eski şehir) bir labirenttir. İlk gün lisanslı bir rehber tutmak, kaybolmadan önemli yerleri görmek için mantıklıdır.
- **Ryad:** Mutlaka eski bir konaktan dönüştürülmüş "Ryad" otellerde kalın. Dışarıdan yıkık dökük görünen kapıların arkasında saray yavrusu avlular vardır.
- **Balak!:** Sokakta "Balak!" (Dikkat!) diye bağıran birini duyarsanız kenara çekilin; yüklü bir eşek veya el arabası geliyor demektir.''';

  static const _fesEN = '''# Fes Guide: The Medieval Labyrinth 🇲🇦

Fes el-Bali is the world's largest car-free urban area. It's a time capsule. Get ready to get lost in over 9,000 narrow alleyways.

## 📅 Best Time to Visit
- **Spring:** The most pleasant weather.
- **Tip:** The city comes alive during the Sacred Music Festival.

## 🏘️ Places to Visit
- [Chouara Tannery](search:Chouara Tannery): Giant vats where leather has been dyed manually for centuries. Be prepared for the smell (hold fresh mint to your nose)!
- [Al Quaraouiyine](search:Al Quaraouiyine): Considered the oldest existing university in the world. Its mosque and library are stunning.
- [Bou Inania Madrasa](search:Bou Inania Madrasa): A masterpiece of Islamic architecture, wood carving, and tile work.

## 🍽️ Food & Drink
- **Tagine:** Slow-cooked meat and couscous in the famous conical clay pots.
- **Pastilla:** A unique pie mixing savory chicken/pigeon with almonds and sugar. Strange but delicious.
- **Mint Tea:** "Moroccan Whiskey." Served everywhere, always hot and very sweet.

## 💎 Local Secrets & Insights
- **Guide:** The Medina is a maze. Hiring a licensed guide for your first day is a smart move to navigate without stress.
- **Riad:** Stay in a "Riad" (traditional courtyard house). Behind humble doors lie magnificent tiled courtyards with fountains.
- **Balak!:** If you hear someone shouting "Balak!" (Watch out!), jump to the side; a loaded donkey or cart is coming through.''';

  // ZERMATT
  static const _zermattTR = '''# Zermatt Rehberi: Matterhorn'un Gölgesinde 🇨🇭

İsviçre Alplerinin kalbinde, motorlu taşıtların girmediği, dünyanın en ünlü dağı Matterhorn'un eteklerinde lüks ve doğanın buluşma noktası.

## 📅 Ne Zaman Gidilir?
- **Kış (Aralık-Mart):** Dünyanın en iyi kayak pistleri için.
- **Yaz (Temmuz-Ağustos):** Yemyeşil vadilerde yürüyüş (hiking) yapmak için.

## 🏘️ Gezilecek Yerler
- [Gornergrat](search:Gornergrat): Trenle 3089 metreye çıkın. Matterhorn ve buzulların manzarası nefes kesicidir.
- [Matterhorn Glacier Paradise](search:Matterhorn Glacier Paradise): Avrupa'nın teleferikle çıkılan en yüksek noktası (3883m). Yazın bile kar vardır.
- [Hinterdorf](search:Hinterdorf Zermatt): Zermatt'ın en eski bölgesi. 16. yüzyıldan kalma ahşap ambarları görün.

## 🍽️ Ne Yenir ve İçilir?
- **Peynir Fondü:** İsviçre klasiği. Dağ manzarasına karşı erimiş peynire ekmek batırmak bir ritüeldir.
- **Rösti:** Kızarmış patates rendesi, üzerine yumurta veya peynirle servis edilir.

## 💎 Lokal Sırlar & İpuçları
- **Toblerone:** O meşhur çikolatanın üzerindeki dağ işte buradaki Matterhorn'dur. Bir paket alıp dağa karşı fotoğraf çekilin.
- **Elektrikli Taksiler:** Kasabada benzinli araba yasaktır. Tren istasyonundan otelinize bu sessiz, kutu gibi taksilerle gidersiniz.
- [5 Göller Yolu](search:5 Lakes Walk Zermatt): Yazın gidiyorsanız bu yürüyüş rotasında Matterhorn'un göllere yansıyan silüetini yakalayabilirsiniz.''';

  static const _zermattEN = '''# Zermatt Guide: In the Shadow of the Matterhorn 🇨🇭

In the heart of the Swiss Alps, a car-free village where luxury meets nature at the foot of the world's most famous mountain, the Matterhorn.

## 📅 Best Time to Visit
- **Winter (Dec-Mar):** For some of the world's best skiing.
- **Summer (Jul-Aug):** For hiking in lush green valleys.

## 🏘️ Places to Visit
- [Gornergrat](search:Gornergrat): Take the cogwheel train up to 3089m. The view of the Matterhorn and glaciers is breathtaking.
- [Matterhorn Glacier Paradise](search:Matterhorn Glacier Paradise): The highest cable car station in Europe (3883m). There is snow even in summer.
- [Hinterdorf](search:Hinterdorf Zermatt): The oldest part of Zermatt. See the wooden barns dating back to the 16th century.

## 🍽️ Food & Drink
- **Cheese Fondue:** The Swiss classic. Dipping bread into melted cheese with a mountain view is a ritual.
- **Rösti:** Fried grated potatoes, often served with a fried egg or melted cheese.

## 💎 Local Secrets & Insights
- **Toblerone:** The mountain on the famous chocolate bar is the Matterhorn right here. Buy a bar and take a photo matching it to the peak!
- **Electric Taxis:** Gas cars are banned. You travel from the station to your hotel in these quiet, boxy electric taxis.
- [5 Lakes Walk](search:5 Lakes Walk Zermatt): If visiting in summer, hike this trail to see the Matterhorn's reflection in crystal clear alpine lakes.''';
  static const _hallstattTR = '''# Hallstatt Rehberi: Masalsı Alp Köyü 🇦🇹

Hallstatt, Avusturya Alpleri'nin eteğinde, göl kenarına kurulmuş, dünyanın en fotojenik köylerinden biridir. O kadar güzeldir ki Çin'de bir kopyası bile yapılmıştır.

## 📅 Ne Zaman Gidilir?
- **Kış (Aralık-Ocak):** Karlar altındaki köy tam bir masal diyarına döner. Noel pazarı küçüktür ama atmosferi büyülüdür.
- **Yaz (Haziran-Ağustos):** Göl kenarında yürümek ve tekneye binmek için idealdir ancak turist kalabalığı çok fazladır.
- **İpucu:** Günübirlik turlar öğlen gelir; köyün tadını çıkarmak için mutlaka bir gece kalın ve sabahın sessizliğini yaşayın.

## 🏘️ Konaklama Rehberi
- **Göl Kenarı:** Manzaralı oteller pahalıdır ancak sabah uyanıp pencereden gölü izlemek buna değer.
- **Obertraun:** Gölün hemen karşısındaki kasaba. Konaklama çok daha uygundur ve Hallstatt'a tren/tekne ile ulaşım çok kolaydır.

## 🍽️ Ne Yenir ve İçilir?
- **Göl Balığı (Reinanke):** Hallstatt gölünden tutulan taze balıkları mutlaka deneyin.
- **Schaumrolle:** Avusturya'ya özgü, içi krema dolu rulo tatlılar. Köy meydanındaki fırınlarda tazesini bulabilirsiniz.
- **Sessizlik:** Burası yaşayan bir köydür. Yerlilerin evlerinin içine bakmak veya gürültü yapmak kesinlikle hoş karşılanmaz.

## 🚇 Ulaşım İpuçları
- **Tren ve Feribot:** Tren istasyonu gölün diğer tarafındadır. Trenden inince "Stefanie" adlı tekneyle köye geçersiniz; bu yolculuk bile tek başına bir deneyimdir.
- **Yürüyüş:** Köy araç trafiğine kapalıdır (sadece yerliler girebilir). Her yere yürüyerek gideceksiniz.

## 💎 Lokal Sırlar & İpuçları
- [Skywalk](search:Hallstatt Skywalk): Köyün hemen üzerindeki bu seyir terası, o meşhur "Dünya Mirası" manzarasını tepeden görmenizi sağlar. Fünikülerle çıkabilirsiniz.
- [Tuz Madenleri](search:Hallstatt Salt Mines): Dünyanın en eski tuz madenleri buradadır. İçindeki yer altı kaydırağı çok eğlencelidir!
- [Mezarlık (Beinhaus)](search:Hallstatt Charnel House): Yer kısıtlı olduğu için eski kemiklerin boyanıp saklandığı "Kemik Evi" ilginç ve biraz ürkütücü bir duraktır.''';

  static const _hallstattEN = '''# Hallstatt Guide: Fairytale Alpine Village 🇦🇹

Hallstatt is one of the most photogenic villages in the world, nestled at the foot of the Austrian Alps by the lake. It is so beautiful that a replica of it has been built in China.

## 📅 Best Time to Visit
- **Winter (December-January):** Under the snow, the village turns into a complete fairytale land. The Christmas market is small but the atmosphere is magical.
- **Summer (June-August):** Ideal for walking by the lake and boating, but the tourist crowds are overwhelming.
- **Tip:** Day trips arrive at noon; to truly enjoy the village, you must stay one night and experience the silence of the morning.

## 🏘️ Accommodation Guide
- **Lakeside:** Hotels with views are expensive, but waking up to see the lake from your window is worth every penny.
- **Obertraun:** The town just across the lake. Accommodation is much cheaper and access to Hallstatt by train/boat is very easy.

## 🍽️ Food & Dining Etiquette
- **Lake Fish (Reinanke):** Definitely try the fresh fish caught from Lake Hallstatt.
- **Schaumrolle:** An Austrian specialty, cream-filled pastry rolls. You can find fresh ones at the bakeries in the village square.
- **Silence:** This is a living village. Peeking into locals' homes or making noise is strictly frowned upon.

## 🚇 Transportation Tips
- **Train and Ferry:** The train station is on the other side of the lake. When you get off the train, you cross to the village with a boat named "Stefanie"; this journey is an experience in itself.
- **Walking:** The village is closed to car traffic (only locals can enter). You will be walking everywhere.

## 💎 Local Secrets & Insights
- [Skywalk](search:Hallstatt Skywalk): This viewing platform just above the village allows you to see that famous "World Heritage" view from above. You can go up by funicular.
- [Salt Mines](search:Hallstatt Salt Mines): The world's oldest salt mines are here. The underground slide inside is widely fun!
- [Cemetery (Beinhaus)](search:Hallstatt Charnel House): Because space is limited, the "Bone House" where old painted skulls are stored is an interesting and slightly spooky stop.''';
}
