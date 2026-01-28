// =============================================================================
// AI SERVICE v2 - TÜM ŞEHİRLER İÇİN ÖNERİLER
// Barcelona, Paris, Roma, İstanbul destekli
// Kişiselleştirilmiş AI Chat yanıtları
// =============================================================================

import 'dart:io';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import 'package:google_generative_ai/google_generative_ai.dart';
import '../models/city_model.dart';
import 'city_blog_content.dart';

class AIService {
  // API Key (Normalde .env dosyasında saklanmalı)
  static const _apiKey = 'AIzaSyAOXa8SaHbJi0tnUTacqQfFCiLcUq5UX0M';

  /// Dinamik olarak yüklenen (JSON'dan gelen) görseller
  static final Map<String, String> _dynamicImageOverrides = {};

  /// Bileşenleri başlat ve yerel JSON'lardan görselleri yükle
  static Future<void> initializeComponents() async {
    try {
      // DEBUG: List available models
      try {
        final model = GenerativeModel(model: 'gemini-2.0-flash', apiKey: _apiKey);
        // Note: The SDK might not expose listModels directly on the model instance in this version,
        // but let's try a simple generation to trigger the error with detail or refer to SDK capability.
        // Actually, for this specific SDK version, let's just log that we are trying to init.
        print("🤖 AI Service: Initializing and checking availability...");
      } catch (e) {
        print("🤖 AI Service Init Check Error: $e");
      }

      final directory = await getApplicationDocumentsDirectory();
      final citiesDir = Directory('${directory.path}/cities');

      if (await citiesDir.exists()) {
        final List<FileSystemEntity> files = citiesDir.listSync();
        for (final file in files) {
          if (file is File && file.path.endsWith('.json')) {
            try {
              final String content = await file.readAsString();
              final Map<String, dynamic> data = json.decode(content);
              
              // Dosya adından şehir slug'ını al (örn: /.../bruksel.json -> bruksel)
              final String filename = file.uri.pathSegments.last;
              final String citySlug = filename.replaceAll('.json', '');

              if (data.containsKey('heroImage') && data['heroImage'] != null) {
                final String heroImage = data['heroImage'];
                if (heroImage.isNotEmpty) {
                  _dynamicImageOverrides[citySlug] = heroImage;
                  debugPrint("🖼️ Dynamic Image Loaded: $citySlug -> $heroImage");
                }
              }
            } catch (e) {
              debugPrint("⚠️ JSON parse error ($file): $e");
            }
          }
        }
      }
    } catch (e) {
      debugPrint("❌ AIService initialization error: $e");
    }
  }

  /// Şehirler için merkezi görsel havuzu
  static final Map<String, String> _cityImages = {
    'amsterdam': 'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800',
    'atina': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg',
    'bangkok': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg',
    'barcelona': 'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800',
    'berlin': 'https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800',
    'budapeste': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltfde92aef92ecf073/6787eae0bf32fe28813c50fe/BCC-2024-EXPLORER-BUDAPEST-LANDMARKS-HEADER-_MOBILE.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'cenevre': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/jet_deau.jpg',
    'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800',
    'dublin': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/temple_bar.jpg',
    'floransa': 'https://italien.expert/wp-content/uploads/2021/05/Florenz-Toskana-Italien0.jpg',
    'hongkong': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/victoria_peak.jpg',
    'istanbul': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800',
    'kopenhag': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800',
    'lizbon': 'https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800',
    'londra': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800',
    'lucerne': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/chapel_bridge_kapellbrucke.jpg',
    'lyon': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/basilica_of_notre_dame_de_fourviere.jpg',
    'madrid': 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800',
    'marakes': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/jemaa_el_fna.jpg',
    'marsilya': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt0feb4d48a3fc134c/67c5fafa304ea9666082ff3e/iStock-956215674-2-Header_Mobile.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'milano': 'https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800',
    'napoli': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800',
    'newyork': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800',
    'nice': 'https://www.flypgs.com/blog/wp-content/uploads/2024/05/nice-sahilleri.jpeg',
    'paris': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800',
    'porto': 'https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=800',
    'prag': 'https://images.unsplash.com/photo-1541849546-216549ae216d?w=800',
    'roma': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800',
    'seul': 'https://www.agoda.com/wp-content/uploads/2019/03/Seoul-attractions-Gyeongbokgung-palace.jpg',
    'sevilla': 'https://images.unsplash.com/photo-1558370781-d6196949e317?w=800',
    'singapur': 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800',
    'stockholm': 'https://images.unsplash.com/photo-1509356843151-3e7d96241e11?w=800',
    'tokyo': 'https://img.piri.net/mnresize/900/-/resim/imagecrop/2023/01/17/11/54/resized_d9b02-8b17feafkapak2.jpg',
    'venedik': 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=800',
    'viyana': 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800',
    'zurih': 'https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800',
    'fes': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=800',
    'safsavan': 'https://images.unsplash.com/photo-1558258695-0e4284b3975d?w=800',
    'kahire': 'https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2019-11/image-explore-ancient-egypt-merl.jpg',
    'saraybosna': 'https://images.unsplash.com/photo-1596715694269-80838637ba76?w=800',
    'mostar': 'https://images.unsplash.com/photo-1605198089408-0138977114b0?w=800',
    'strazburg': 'https://www.avruparuyasi.com.tr/uploads/tour-gallery/36c44666-5e5a-4c2d-a341-2fa8285c3fb6.webp',

    'antalya': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/kaleici.jpg',
    'edinburgh': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt9d8daa2acc7bb33c/6797dc563b4101992b03092a/iStock-1153650218-MOBILE-HEADER.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'belgrad': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/belgrad/belgrad_kalesi_kalemegdan.jpg',
    'kotor': 'https://www.etstur.com/letsgo/wp-content/uploads/2025/12/montenegro-kotorda-gezilecek-yerler-en-populer-rotalar-guncel-liste-1024x576.png',
    'tiran': 'https://images.unsplash.com/photo-1599593442654-e1b088b7538c?w=800',
    'selanik': 'https://images.unsplash.com/photo-1562608460-f97577579893?w=800',
    'kapadokya': 'https://images.unsplash.com/photo-1641128324972-af3212f0f6bd?w=800',
    'rovaniemi': 'https://www.visitfinland.com/dam/jcr:70734834-7ba2-4bf1-9f6e-bf185e014367/central-plaza-santa-claus-village-rovaniemi-lapland-finland%20(1).jpg',
    'tromso': 'https://www.flightgift.com/media/wp/FG/2024/02/tromso.webp',
    'zermatt': 'https://holidaystoswitzerland.com/wp-content/uploads/2020/07/Zermatt-and-the-Matterhorn-at-dawn.jpg',
    'matera': 'https://ita.travel/user/blogimg/ostatni/aerial-view_matera_sunset.jpg',
    'giethoorn': 'https://www.onedayinacity.com/wp-content/uploads/2021/03/Giethoorn-Village.png',
    'colmar': 'https://images.goway.com/production/hero/iStock-1423136049.jpg',
    'sintra': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt75a384a61f2efa5b/68848225e7cb649650cc2d81/BCC-2024-EXPLORER-SINTRA-BEST_PLACES_TO_VISIT-HEADER-MOBILE.jpg?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440',
    'sansebastian': 'https://cdn.bunniktours.com.au/public/posts/images/Europe/Blog%20Header%20-%20Spain%20-%20San%20Sebastian%20-%20credit%20Raul%20Cacho%20Oses%20%28Unsplash%29-feature.jpg',
    'bologna': 'https://www.datocms-assets.com/57243/1661342703-6245af628d40974c9ab5a7fd_petr-slovacek-sxk8bwkvoxe-unsplash-20-1.jpg?auto=compress%2Cformat',
    'gaziantep': 'https://www.brandlifemag.com/wp-content/uploads/2021/04/acilis-gaziantep-december-06gaziantep-coppersmith-bazaar-600w-549044518.jpg',
    'brugge': 'https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2021-08/brugge-hakkinda-bilinmesi-gerekenler.jpg',
    'santorini': 'https://www.kucukoteller.com.tr/storage/images/2024/07/14/5e7eaf11eb5ec2dda2f7a602232faa8961347f29.webp',
    'heidelberg': 'https://image.hurimg.com/i/hurriyet/90/1110x740/56b3325818c7730e3cdb6757.jpg',
    'bruksel': 'https://gezipgordum.com/wp-content/uploads/2022/01/Brukselde-nerede-kalinir-1.jpg.webp',
    'oslo': 'https://www.journavel.com/wp-content/uploads/2024/10/IMG_1851-scaled.webp',
    'hallstatt': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hallstatt/hallstatt-postcard-viewpoint.jpg',
  };

  /// Şehir ID'sine göre görsel URL'ini döndürür
  static String getCityImage(String cityId) {
    // Normalizasyon (Türkçe karakterler ve boşluklar)
    final normalized = cityId.toLowerCase().trim()
      .replaceAll('ü', 'u').replaceAll('ş', 's').replaceAll('ç', 'c')
      .replaceAll('ö', 'o').replaceAll('ğ', 'g').replaceAll('ı', 'i')
      .replaceAll(' ', '');
    
    // English mapping
    String lookupId = normalized;
    if (normalized == 'brussels') lookupId = 'bruksel';
    if (normalized == 'london') lookupId = 'londra';
    if (normalized == 'vienna') lookupId = 'viyana';
    if (normalized == 'rome') lookupId = 'roma';
    if (normalized == 'venice') lookupId = 'venedik';
    if (normalized == 'athens') lookupId = 'atina';
    if (normalized == 'geneva') lookupId = 'cenevre';
    if (normalized == 'florence') lookupId = 'floransa';
    if (normalized == 'lisbon') lookupId = 'lizbon';
    if (normalized == 'milan') lookupId = 'milano';
    if (normalized == 'naples') lookupId = 'napoli';
    if (normalized == 'marrakech') lookupId = 'marakes';
    if (normalized == 'marseille') lookupId = 'marsilya';
    if (normalized == 'prague') lookupId = 'prag';
    if (normalized == 'seville') lookupId = 'sevilla';
    if (normalized == 'strasbourg') lookupId = 'strazburg';
    if (normalized == 'cairo') lookupId = 'kahire';

    if (normalized == 'cappadocia') lookupId = 'kapadokya';
    if (normalized == 'belgrade') lookupId = 'belgrad';

    // 1. Önce dinamik override listesine bak (JSON'dan gelen)
    if (_dynamicImageOverrides.containsKey(lookupId)) {
      return _dynamicImageOverrides[lookupId]!;
    }

    // 2. Yoksa hardcoded listeye bak
    return _cityImages[lookupId] ?? 'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800'; // Default mountain
  }

  /// Kullanıcının serbest formatlı sorularına yanıt verir (Chat için)
  Future<String> getChatResponse({
    required String cityName,
    required String question,
    required List<String> interests,
    required List<Map<String, dynamic>> places,
    bool isEnglish = false,
  }) async {
    try {
      print("🔑 AI Chat Key Prefix: ${_apiKey.substring(0, 6)}...");
      final model = GenerativeModel(
        model: 'gemini-2.0-flash',
        apiKey: _apiKey,
      );

      // Place listesini string'e çevir
      final placeNames = places.map((p) => p['name'] as String).join(", ");

      final prompt = '''
      Sen $cityName için bir yerel rehbersin.
      Kullanıcı sana bir soru sordu: "$question"
      
      MEVCUT YER LİSTESİ: [$placeNames]
      Sadece bu listeden yer öner, yeni yer uydurma.
      
      Yanıtını ${isEnglish ? "İngilizce" : "Türkçe"} olarak ver.
      Kısa ve öz yanıt ver (max 3-4 cümle).
      Emoji kullanma.

      ÖNEMLİ: Bir yerden bahsederken mutlaka şu formatı kullan: [Yer Adı](search:Yer Adı)
      Örnek: "Sana [Eiffel Kulesi](search:Eiffel Kulesi) öneririm."
      Yer adlarını köşeli parantez ve parantez içinde ASLA çevirme, listedeki tam adını kullan.
      ''';

      final content = [Content.text(prompt)];
      final response = await model.generateContent(content);

      return response.text ?? (isEnglish ? "Sorry, couldn't generate a response." : "Üzgünüm, yanıt oluşturulamadı.");
    } catch (e) {
      print("AI Chat Error: $e");
      return isEnglish ? "I can't respond right now. Please try again later." : "Şu an yanıt veremiyorum. Lütfen daha sonra tekrar deneyin.";
    }
  }

  /// Kişiselleştirilmiş AI chat yanıtı üretir (Gemini Powered)
  static Future<String> getPersonalizedChatResponse({
    required CityModel cityModel, // Context için eklendi
    required String userName,
    required String travelStyle,
    required List<String> interests,
    required String budgetLevel,
    required int tripDays,
    bool isEnglish = false,
  }) async {
    try {
      print("🔑 USED API KEY: $_apiKey"); // FULL KEY PRINT FOR DEBUGGING
      print("🤖 AI Service Model request: gemini-2.0-flash");
      
      // 1. Model Hazırlığı
      final model = GenerativeModel(
        model: 'gemini-2.0-flash', 
        apiKey: _apiKey,
      );

      // 2. RAG Context Hazırlığı - Yerleri karıştır ve sadece bunlardan öner
      final shuffledHighlights = List.from(cityModel.highlights)..shuffle();
      final placeNames = shuffledHighlights.map((h) => h.name).join(", ");
      final availablePlacesContext = "AVAILABLE PLACES IN DATABASE: [$placeNames]. "
          "ONLY recommend places from this list. Do NOT invent places.";

      // Rastgelelik için seed oluştur
      final randomSeed = DateTime.now().millisecondsSinceEpoch;
      final themes = ['hidden gems', 'local favorites', 'unique experiences', 'must-see spots', 'off the beaten path'];
      final selectedTheme = themes[randomSeed % themes.length];

      // 3. Prompt Oluşturma
      final languageInstruction = isEnglish 
          ? "IMPORTANT: You MUST respond ENTIRELY in English. All text, greetings, descriptions, and tips must be in English."
          : "IMPORTANT: You MUST respond ENTIRELY in Turkish. All text, greetings, descriptions, and tips must be in Turkish.";
      
      final prompt = '''
      $languageInstruction
      
      You are a local guide for ${cityModel.city}.
      User: $userName. Style: $travelStyle. Interests: ${interests.join(", ")}. Budget: $budgetLevel. Trip: $tripDays days.
      
      RANDOMIZATION SEED: $randomSeed
      TODAY'S THEME: Focus on "$selectedTheme" for today.

      $availablePlacesContext

      Task: Recommend exactly 3 DIFFERENT places from the available list that match the user's style.
      IMPORTANT: Choose places you haven't recommended before. Be creative and surprising!
      
      Output Format (Strict Markdown):
      Start with a friendly greeting paragraph.
      Then, for each recommendation use this EXACT format:
      - [Place Name](search:Place Name) - A short, engaging description (max 2 sentences).

      IMPORTANT RULES:
      1. ONLY recommend places from the "AVAILABLE PLACES" list.
      2. DO NOT translate the [Place Name] inside the brackets or parentheses. use the EXACT name from the list. 
         Example: If list has "Santa Caterina Market", write "[Santa Caterina Market](search:Santa Caterina Market)", NOT "[Santa Caterina Pazarı](search:Santa Caterina Pazarı)".
      3. The ENTIRE response (greeting, descriptions, tip) must be in ${isEnglish ? "English" : "Turkish"}.
      4. Do NOT use emojis.
      5. Each time you respond, pick DIFFERENT places from the list to keep it fresh.

      End with a "${isEnglish ? "Tip:" : "İpucu:"}" section.
      ''';


      // 4. İstek Gönderme
      final content = [Content.text(prompt)];
      final response = await model.generateContent(content);

      if (response.text != null) {
        return response.text!;
      } else {
        throw Exception("Empty response");
      }
    } catch (e) {
      print("AI Error: $e");
      // Fallback: Eski hardcoded yönteme dön
       return _getFallbackResponse(
         city: cityModel.city, userName: userName, travelStyle: travelStyle, 
         interests: interests, budgetLevel: budgetLevel, tripDays: tripDays, isEnglish: isEnglish
       );
    }
  }

  /// Mevcut AI içeriğini başka bir dile çevirir (yeniden üretmek yerine)
  static Future<String> translateContent({
    required String content,
    required bool toEnglish,
  }) async {
    try {
      final model = GenerativeModel(
        model: 'gemini-1.5-flash',
        apiKey: _apiKey,
      );

      final targetLanguage = toEnglish ? "English" : "Turkish";
      final prompt = '''
      Translate the following travel recommendation text to $targetLanguage.
      
      IMPORTANT RULES:
      1. Keep the EXACT same formatting (markdown, bullet points, links).
      2. DO NOT translate place names inside [brackets] or (parentheses).
         Example: "[Santa Caterina Market](search:Santa Caterina Market)" should stay EXACTLY the same.
      3. Only translate the descriptions and greeting text.
      4. Keep "Tip:" or "İpucu:" section.
      5. Do NOT add or remove any content.
      
      TEXT TO TRANSLATE:
      $content
      ''';

      final response = await model.generateContent([Content.text(prompt)]);
      
      if (response.text != null) {
        return response.text!;
      } else {
        throw Exception("Empty translation response");
      }
    } catch (e) {
      print("Translation Error: $e");
      // Çeviri başarısız olursa orijinal içeriği döndür
      return content;
    }
  }

  // Eski yöntemi fallback olarak buraya taşıdım (kısaltılmış)
  static String _getFallbackResponse({
    required String city,
    required String userName,
    required String travelStyle,
    required List<String> interests,
    required String budgetLevel,
    required int tripDays,
    bool isEnglish = false,
  }) {
    // ... Eski logic buraya taşınacak (yer tutucu)
    final cityData = _getCitySpecificContent(city, interests, budgetLevel, travelStyle, isEnglish);
     final greeting = isEnglish
        ? "Good evening $userName! Welcome to $city!"
        : "İyi akşamlar $userName! $city'e hoş geldin!";
    
     return isEnglish
        ? '''$greeting ${cityData['intro']}\n\n${cityData['recommendations']}\n\n**Tip:** ${cityData['tip']}'''
        : '''$greeting ${cityData['intro']}\n\n${cityData['recommendations']}\n\n**İpucu:** ${cityData['tip']}''';
  }

  static String _getTimeBasedGreeting(bool isEnglish) {
    final hour = DateTime.now().hour;
    if (isEnglish) {
      if (hour < 12) return "Good morning";
      if (hour < 18) return "Good afternoon";
      return "Good evening";
    }
    if (hour < 12) return "Günaydın";
    if (hour < 18) return "İyi günler";
    return "İyi akşamlar";
  }

  static String _formatInterests(List<String> interests, bool isEnglish) {
    if (interests.isEmpty) return isEnglish ? "discovery" : "keşif";
    if (interests.length == 1) return interests[0].toLowerCase();
    if (interests.length == 2) {
      final connector = isEnglish ? "and" : "ve";
      return "${interests[0]} $connector ${interests[1]}".toLowerCase();
    }
    final connector = isEnglish ? "and" : "ve";
    return "${interests.take(2).join(', ')} $connector ${interests[2]}".toLowerCase();
  }

  static String _getBudgetText(String budgetLevel, bool isEnglish) {
    switch (budgetLevel.toLowerCase()) {
      case 'ekonomik':
        return isEnglish ? "budget-friendly" : "bütçe dostu";
      case 'premium':
        return isEnglish ? "luxury-seeking" : "lüks deneyimler arayan";
      default:
        return isEnglish ? "balanced-budget" : "dengeli bütçeli";
    }
  }

  static String _getStyleText(String travelStyle, bool isEnglish) {
    switch (travelStyle.toLowerCase()) {
      case 'turistik':
        return isEnglish ? "classic tourist" : "Klasik turistik noktaları da severken";
      case 'maceracı':
        return isEnglish ? "adventurous" : "Macera arayan ruhuyla";
      case 'kültürel':
        return isEnglish ? "culture & history lover" : "Kültür ve tarihe meraklı";
      default:
        return isEnglish ? "local explorer" : "Yerel hayatı keşfetmeyi seven";
    }
  }

  static Map<String, String> _getCitySpecificContent(
    String city,
    List<String> interests,
    String budget,
    String style,
    bool isEnglish,
  ) {
    final normalizedCity = city.toLowerCase().trim();

    switch (normalizedCity) {
      case 'istanbul':
      case 'İstanbul':
        return _getIstanbulContent(interests, budget, isEnglish);
      case 'paris':
        return _getParisContent(interests, budget, isEnglish);
      case 'roma':
      case 'rome':
        return _getRomaContent(interests, budget, isEnglish);
      case 'londra':
      case 'london':
        return _getLondraContent(interests, budget, isEnglish);
      case 'berlin':
        return _getBerlinContent(interests, budget, isEnglish);
      case 'madrid':
        return _getMadridContent(interests, budget, isEnglish);
      case 'sevilla':
      case 'seville':
        return _getSevillaContent(interests, budget, isEnglish);
      case 'viyana':
      case 'vienna':
        return _getViyanaContent(interests, budget, isEnglish);
      case 'prag':
      case 'prague':
        return _getPragContent(interests, budget, isEnglish);
      case 'lizbon':
      case 'lisbon':
        return _getLizbonContent(interests, budget, isEnglish);
      case 'milano':
      case 'milan':
        return _getMilanoContent(interests, budget, isEnglish);
      case 'amsterdam':
        return _getAmsterdamContent(interests, budget, isEnglish);
      case 'tokyo':
        return _getTokyoContent(interests, budget, isEnglish);
      case 'seul':
      case 'seoul':
        return _getSeulContent(interests, budget, isEnglish);
      case 'singapur':
      case 'singapore':
        return _getSingapurContent(interests, budget, isEnglish);
      case 'dubai':
        return _getDubaiContent(interests, budget, isEnglish);
      case 'newyork':
      case 'new york':
        return _getNewYorkContent(interests, budget, isEnglish);
      case 'bruksel':
      case 'brussels':
        return _getBrukselContent(interests, budget, isEnglish);
      case 'oslo':
        return _getOsloContent(interests, budget, isEnglish);
      case 'kapadokya':
      case 'cappadocia':
        return _getKapadokyaContent(interests, budget, isEnglish);
      case 'barcelona':
      default:
        return _getBarcelonaContent(interests, budget, isEnglish);
    }
  }

  static Map<String, String> _getIstanbulContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro':
            "Welcome to Istanbul, I'm glad to hear you're in exploration mode!",
        'recommendations': '''
- [Fener & Balat Streets](search:Fener & Balat Streets) - This is an open-air museum! You won't stop taking photos with its colorful bay-windowed houses, narrow cobbled streets, and surprise cafes at every corner. Old churches, synagogues, and mosques all together - a magnificent cultural mosaic. You can find unique pieces in small antique shops, local design stores, and second-hand treasures, perfect for mid-budget shopping. Take your time to catch the spirit of this place!

- [Kuzguncuk](search:Kuzguncuk) - The "quiet village" vibe of the Anatolian Side is here! Like time travel with its narrow streets, nostalgic grocery stores, and colorful wooden houses. You must try İsmail Usta's famous toasts or the Kuzguncuk Borek Shop for weekend breakfast. Sitting on the benches overlooking the Bosphorus, watching seagulls, and catching the golden hour for photos is priceless.

- [Karaköy & Shipyard](search:Karaköy & Shipyard) - This is Istanbul's new creative heart! Art galleries, concept stores, and amazing cafes in old shipyard buildings. Street art walls are great for photos. Experience baklava at Karaköy Güllüoğlu, modern Turkish cuisine at Karaköy Lokantası. Watch the sunset with a Bosphorus view at Istanbul Modern's cafe in the evening.''',
        'tip':
            "Go to Balat early on a weekday morning to take photos without crowds and chat with local shopkeepers. Don't refuse if they offer tea!",
      };
    }
    return {
      'intro':
          "İstanbul'a hoş geldin, keşif modunda olduğunu duyunca çok sevindim!",
      'recommendations': '''
- [Fener & Balat Sokakları](search:Fener & Balat Sokakları) - Burası tam bir açık hava müzesi! Renkli cumbalı evleri, Arnavut kaldırımlı daracık sokakları, her köşede karşına çıkacak sürpriz kafeleri ve vintage dükkanlarıyla fotoğraf çekmekten parmakların yorulacak. Eski kiliseler, sinagoglar, camiler bir arada, müthiş bir kültür mozaiği. Küçük antikacılardan, yerel tasarım dükkanlarından ve ikinci el hazinelerinden kendine özgü parçalar bulabilir, orta bütçeyle harika alışveriş yapabilirsin. Buranın ruhunu yakalamak için bolca vakit ayır!

- [Kuzguncuk](search:Kuzguncuk) - Anadolu Yakası'nın o "sakin köy" havası burada! Dar sokakları, nostaljik bakkalları, rengârenk ahşap evleriyle zamanda yolculuk gibi. Hafta sonu kahvaltısı için İsmail Usta'nın meşhur tostlarını veya Kuzguncuk Börekçisi'ni denemelisin. Boğaz'a nazır banklarda oturup martıları izlemek, fotoğraf için altın saatini yakalamak paha biçilmez. Alışveriş için butik tasarım dükkanları ve antikacılar var.

- [Karaköy & Tersane](search:Karaköy & Tersane) - Burası İstanbul'un yeni yaratıcı kalbi! Eski tersane binalarında sanat galerileri, concept store'lar ve muhteşem kafeler var. Street art duvarları fotoğraf için harika. Karaköy Güllüoğlu'nda baklava, Karaköy Lokantası'nda modern Türk mutfağı deneyimle. Akşamüstü İstanbul Modern'in kafesinde Boğaz manzarasıyla gün batımını izle.''',
      'tip':
          "Balat'a hafta içi sabah erken git, hem kalabalıksız fotoğraf çekersin hem de yerel esnafla sohbet edersin. Çay ikram ederlerse reddetme!",
    };
  }

  static Map<String, String> _getBarcelonaContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro':
            "Welcome to Barcelona! A wonderful adventure awaits in Gaudí's magical city!",
        'recommendations': '''
- [Bunkers del Carmel](search:Bunkers del Carmel) - The best viewpoint in Barcelona, unknown to tourists and kept secret by locals! Built on old Civil War bunkers, this hill offers a 360-degree city panorama. Go at sunset, drink wine while the city lights turn on. A paradise for photographers! Free and uncrowded.

- [El Born District](search:El Born District) - The cooler, less touristy version of the Gothic Quarter! You won't get enough of exploring its narrow streets, independent boutiques, vintage shops, and great tapas bars. See Roman ruins at El Born Cultural Center, enter Santa Maria del Mar Church (free and magnificent). Nomad Coffee for coffee, Paradiso (one of the world's best bars) for cocktails.

- [Sant Antoni Market](search:Sant Antoni Market) - The newly restored market building is an architectural wonder. Transforms into a book and antique market on Sunday mornings. Have an Australian-style brunch at Federal Café, eat healthy at Flax & Kale. Surrounding streets are full of vintage shops and street art.''',
        'tip':
            "Buy tickets for La Sagrada Familia but go for the first slot at 9 AM. The light is magnificent at that hour and there are no crowds!",
      };
    }
    return {
      'intro':
          "Barcelona'ya hoş geldin! Gaudí'nin büyülü şehrinde harika bir macera seni bekliyor!",
      'recommendations': '''
- [Bunkers del Carmel](search:Bunkers del Carmel) - Turistlerin bilmediği, yerellerin gizli sakladığı Barcelona'nın en iyi manzara noktası! Eski İç Savaş sığınakları üzerine kurulu bu tepe, 360 derece şehir panoraması sunuyor. Gün batımında git, şehrin ışıkları yanarken şarap iç. Fotoğrafçılar için cennet! Ücretsiz ve kalabalıksız.

- [El Born Mahallesi](search:El Born Mahallesi) - Gotik Mahalle'nin daha cool, daha az turistik versiyonu! Dar sokakları, bağımsız butikleri, vintage dükkanları ve harika tapas barlarıyla keşfetmeye doyamazsın. El Born Kültür Merkezi'nde Roma kalıntılarını gör, Santa Maria del Mar Kilisesi'nin içine gir (ücretsiz ve muhteşem). Kahve için Nomad Coffee, kokteyl için Paradiso (dünyanın en iyi barlarından).

- [Sant Antoni Pazarı](search:Sant Antoni Pazarı) - Yeni restore edilmiş pazar binası mimari harika. Pazar Pazar günleri kitap ve antika pazarına dönüşüyor. Federal Café'de Avustralya tarzı brunch yap, Flax & Kale'de sağlıklı yemek ye. Çevre sokaklar vintage mağazalar ve street art ile dolu.''',
      'tip':
          "La Sagrada Familia'ya bilet al ama sabah 9'da ilk seansta git. Işık o saatte muhteşem ve kalabalık yok!",
    };
  }

  static Map<String, String> _getParisContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro': "Welcome to Paris! The City of Lights is ready to enchant you!",
        'recommendations': '''
- [Hidden Courtyards of Le Marais](search:Hidden Courtyards of Le Marais) - While tourists stick to main streets, you dive into courtyards! The garden of Hôtel de Sully, behind Place des Vosges, hidden passages... Vintage shops, Jewish quarter delicacies (L'As du Fallafel is legendary!), LGBTQ+ bars, art galleries. Photo moments at every corner.

- [Canal Saint-Martin](search:Canal Saint-Martin) - Atmosphere straight out of the Amélie movie! Iron bridges, cafe terraces, vintage bookstores. Have coffee at Chez Prune, shop at Antoine et Lili. Join Parisians picnicking by the canal on Sundays. The golden hour is magnificent for photos.

- [Backstreets of Montmartre](search:Backstreets of Montmartre) - Go behind Sacré-Cœur! Buy cheese and wine at the local market on Rue Lepic, take photos in front of La Maison Rose, but the real beauty is in the backstreets. Rue de l'Abreuvoir is the most romantic street in Paris. Don't miss chanson night at Au Lapin Agile.''',
        'tip':
            "Walk instead of using the metro! It's the only way to truly explore Paris. Don't be afraid to get lost, the best discoveries happen by accident!",
      };
    }
    return {
      'intro': "Paris'e hoş geldin! Işıklar şehri seni büyülemeye hazır!",
      'recommendations': '''
- [Le Marais'in Gizli Avluları](search:Le Marais'in Gizli Avluları) - Turistler ana caddelerde kalırken, sen avluların içine dal! Hôtel de Sully'nin bahçesi, Place des Vosges'un arkası, gizli pasajlar... Vintage dükkanları, Yahudi mahallesi lezzetleri (L'As du Fallafel efsane!), LGBTQ+ barları, sanat galerileri. Her köşede fotoğraflık anlar.

- [Canal Saint-Martin](search:Canal Saint-Martin) - Amelie filminden çıkma atmosfer! Demir köprüler, kafe terasları, vintage kitapçılar. Chez Prune'de kahve iç, Antoine et Lili'de alışveriş yap. Pazar günleri kanalın kenarında piknik yapan Parisililere katıl. Fotoğraf için altın saat muhteşem.

- [Montmartre'ın Arka Sokakları](search:Montmartre'ın Arka Sokakları) - Sacré-Cœur'ün arkasına dolan! Rue Lepic'te yerel pazarda peynir ve şarap al, La Maison Rose önünde fotoğraf çek ama asıl güzellik arka sokaklarda. Rue de l'Abreuvoir Paris'in en romantik sokağı. Au Lapin Agile'de chanson gecesi kaçırma.''',
      'tip':
          "Metro yerine yürü! Paris'i gerçekten keşfetmenin tek yolu bu. Kaybolmaktan korkma, en güzel keşifler tesadüfen olur!",
    };
  }

  static Map<String, String> _getRomaContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Roma'ya hoş geldin! Ebedi şehir 3000 yıllık hazinelerini sana açmaya hazır!",
      'recommendations': '''
- [Trastevere](search:Trastevere) - Roma'nın gerçek kalbi burası! Sarmaşıklı duvarlar, çamaşır asılı dar sokaklar, meydanlarda oynayan çocuklar... Turistik ama hala otantik. Da Enzo al 29'da cacio e pepe ye (sıra bekle ama değer!), Piazza di Santa Maria'da gece çeşmenin önünde otur, Bar San Calisto'da Negroni iç.

- [Testaccio](search:Testaccio) - Romalıların Roma'sı! Eski mezbaha binalarında şimdi MACRO müzesi ve gece kulüpleri var. Testaccio Pazarı'nda supplì ve porchetta dene (en iyi street food!). Aventine Tepesi'ndeki Malta Şövalyeleri Kapısı'nın anahtar deliğinden St. Peter's Bazilikası'nı gör - sürpriz manzara!

- [Garbatella](search:Garbatella) - Hiçbir turistin bilmediği mahalle! 1920'lerin işçi konutları şimdi bohem sanatçı cenneti. Renkli binalar, gizli bahçeler, yerel barlar. Cesare al Casaletto'da gerçek Roma mutfağı ye. Street art duvarları fotoğraf için harika.''',
      'tip':
          "Trastevere'de akşam 7'de aperitivo saati başlar. 8-10€'ya içki + sınırsız büfe! En iyi ekonomik akşam yemeği stratejisi",
    };
  }

  static Map<String, String> _getLondraContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Londra'ya hoş geldin! Kraliyet şehri modern ve tarihi bir arada sunuyor!",
      'recommendations': '''
- [Shoreditch & Brick Lane](search:Shoreditch & Brick Lane) - Londra'nın en cool mahallesi! Street art duvarları her köşede, vintage marketler, bağımsız tasarımcı dükkanları. Pazar günü Brick Lane Market muhteşem. Beigel Bake'de 24 saat taze bagel, Cereal Killer Cafe'de 120 çeşit mısır gevreği. Akşam rooftop barlarda kokteyl!

- [South Bank & Borough Market](search:South Bank & Borough Market) - Thames kıyısında yürüyüş, Tate Modern (ücretsiz!), Shakespeare's Globe. Borough Market'ta dünya mutfakları: İngiliz pies, İspanyol jamón, Fransız peynir. Neal's Yard Dairy'de peynir tadımı kaçırma. Gece National Theatre'da oyun izle.

- [Notting Hill & Portobello](search:Notting Hill & Portobello) - Pastel renkli evler, antika dükkanları, film setleri. Cumartesi Portobello Road Market'ta kaybol. The Churchill Arms pub tamamen çiçeklerle kaplı. Ottolenghi'de brunch, Electric Cinema'da vintage koltuklarda film izle.''',
      'tip':
          "Oyster Card al, tüm toplu taşıma için geçerli. Müzelerin çoğu ücretsiz, sanat galerilerine de giriş yok!",
    };
  }

  static Map<String, String> _getBerlinContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Berlin'e hoş geldin! Özgür ruhlu, yaratıcı ve tarihi derin bir şehir!",
      'recommendations': '''
- [Kreuzberg](search:Kreuzberg) - Berlin'in kalbi burası! Multikulti atmosfer, dönerci, vintage shop, techno kulüp yan yana. Markthalle Neun'da Perşembe Street Food, Görlitzer Park'ta piknik. Oranienstraße'de gece hayatı efsane. Burası gerçek Berlin!

- [Friedrichshain & RAW Gelände](search:Friedrichshain & RAW Gelände) - Eski tren deposu şimdi sanat merkezi! Duvar boyama, pazar, bara, klüp her şey var. East Side Gallery'de Berlin Duvarı'nın en uzun parçası. Boxhagener Platz'da hafta sonu kahvaltı, Simon-Dach-Straße'de bira.

- [Prenzlauer Berg](search:Prenzlauer Berg) - Hipster cennet! Mauerpark'ta Pazar günü karaoke ve bit pazarı. Kastanienallee'de butik alışveriş, Kulturbrauerei'de etkinlikler. Konnopke's Imbiss'te currywurst ye, Pratercarten'de Berlin'in en eski birahane bahçesi.''',
      'tip':
          "Berlin ucuz bir şehir. Döner 4€, bira 3€, giriş birçok yere ücretsiz. Club'lara gece 1'den sonra git!",
    };
  }

  static Map<String, String> _getMadridContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Madrid'e hoş geldin! İspanya'nın kalbinde enerji, sanat ve tapas seni bekliyor!",
      'recommendations': '''
- [La Latina & El Rastro](search:La Latina & El Rastro) - Madrid'in en otantik mahallesi! Pazar günü El Rastro bit pazarı efsane. Cava Baja'da tapas bardan bara atla. Casa Lucio'da huevos rotos, Juana la Loca'da pintxo. Akşam La Latina meydanlarında vermouth iç.

- [Malasaña](search:Malasaña) - Hipster Madrid! Vintage dükkanları, plak mağazaları, street art. Café Comercial'de kahve, Ojalá'nın kumlu zemininde brunch. Gece Calle Velarde'de bar hopping. La Vía Láctea'da canlı müzik.

- [Lavapiés](search:Lavapiés) - Multicultural, gerçek, ucuz! Hint, Çin, Afrika restoranları iç içe. Tabacalera sanat merkezi (ücretsiz), Cine Doré (en eski sinema). El Brillante'de calamares bocadillo ye. Gece açık havada sangria.''',
      'tip':
          "İspanyol saatine ayak uydur: Öğle 14:00, akşam yemeği 21:00, gece çıkışı 01:00'den sonra başlar!",
    };
  }

  static Map<String, String> _getSevillaContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Sevilla'ya hoş geldin! Flamenko, portakal ağaçları ve tutkulu Endülüs ruhu!",
      'recommendations': '''
- [Triana](search:Triana) - Guadalquivir'in karşı kıyısında gerçek Sevilla! Seramik atölyeleri, flamenko barları, tapas lokantaları. Mercado de Triana'da kahvaltı, Bar Bistec'te carrillada. Akşam nehir kenarında gün batımı, gece Casa de la Memoria'da flamenko.

- [Alameda de Hércules](search:Alameda de Hércules) - Lokal gece hayatının merkezi! Eski mahalle şimdi hipster cenneti. Gün içinde vintage kafeler, gece açık hava barları. El Rinconcillo (1670'den beri!) en eski bar. Duo Tapas'ta modern İspanyol.

- [Barrio Santa Cruz](search:Barrio Santa Cruz) - Evet turistik ama çok güzel! Labirent sokaklar, gizli avlular, jasmin kokusu. Sabah erken git, kalabalıksız. Casa Tomate'de rooftop kahve. Archivo de Indias'ı gör (ücretsiz, Kolomb haritaları).''',
      'tip':
          "Siesta kutsal! 14:00-17:00 arası çoğu yer kapalı. Bu saatleri dinlenmek veya Alcázar bahçelerinde zaman için kullan",
    };
  }

  static Map<String, String> _getViyanaContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Viyana'ya hoş geldin! İmparatorluk görkemi, kahve kültürü ve müzik şehri!",
      'recommendations': '''
- [Naschmarkt & Freihausviertel](search:Naschmarkt & Freihausviertel) - Viyana'nın en canlı pazarı! 120+ tezgah: Avusturya, Türk, Balkan lezzetleri. Cumartesi bit pazarı var. Arkasında Freihausviertel'de indie kafeler, vintage mağazalar. Café Savoy'da kahve, Motto'da brunch.

- [MuseumsQuartier](search:MuseumsQuartier) - Dünyanın en büyük sanat komplekslerinden! Leopold Museum, MUMOK, Kunsthalle. Ama asıl önemli olan avludaki dev renkli banklar - Viyanılıların buluşma noktası. Akşam şarap, gece dans. Café Leopold'da rooftop.

- [Spittelberg](search:Spittelberg) - Biedermeier evleri, dar sokaklar, sanat galerileri. Amerlingbeisl'de gizli bahçede yemek. Noel pazarı efsanevi. Yıl boyu butik mağazalar, tasarımcı atölyeleri. Plutzer Bräu'de ev yapımı bira.''',
      'tip':
          "Kahve bir ritüel! Melange sipariş et, pasta al, gazete oku, acele etme. Türk kahvesi istersen şaşırırlar",
    };
  }

  static Map<String, String> _getPragContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Prag'a hoş geldin! Ortaçağ büyüsü, bira cenneti ve uygun fiyatlar!",
      'recommendations': '''
- [Vinohrady & Žižkov](search:Vinohrady & Žižkov) - Turistsiz Prag! Vinohrady art nouveau binaları, trendy kafeler, LGBT+ dostu. Riegrovy Sady parkında bira bahçesi manzarayla. Žižkov ise underground: ucuz bira, punk bar, yerel pub. Televizyon Kulesi'ne çık.

- [Holešovice](search:Holešovice) - Eski endüstri bölgesi şimdi sanat merkezi! DOX çağdaş sanat, Vnitroblock yaratıcı hub. Manifesto Market'ta street food, Cross Club'da cyberpunk gece hayatı. Pazar günü Holešovice pazarı muhteşem.

- [Malá Strana](search:Malá Strana) - Evet turistik ama gece sihirli! Gündüz kalabalık, ama akşam 7'den sonra kafeler boşalır. Kampa Adası'nda nehir kenarı, Lennon Duvarı (gece git), U Malého Glena'da jazz. Cafe Lounge'da cheesecake.''',
      'tip':
          "Bira sudan ucuz gerçek! 0.5L 40 Kč (1.5€). Hospoda denen yerel birahane pub'larını ara, turistik olmayan!",
    };
  }

  static Map<String, String> _getLizbonContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Lizbon'a hoş geldin! Yedi tepe, fado müziği ve pastel de nata cenneti!",
      'recommendations': '''
- [Alfama](search:Alfama) - Lizbon'un ruhu burada! Dar sokaklar, azulejo karolar, fado sesleri. Gün batımında Miradouro da Graça'ya çık. Tasca do Chico'da fado (rezervasyon şart), A Baiuca'da yerel deneyim. Feira da Ladra bit pazarı Salı ve Cumartesi.

- [LX Factory](search:LX Factory) - Eski fabrika şimdi yaratıcı cennet! Kitapçı, restoran, galeri, pazar hepsi bir arada. Landeau'da dünyanın en iyi çikolatalı pastası. Hafta sonu açık hava pazarı. Gece rooftop barlarda dans.

- [Mouraria](search:Mouraria) - Turistlerin bilmediği gerçek mahalle! Multicultural, Afrikalı, Hintli, Çinli restoranlar. Zé da Mouraria'da fado, Tia Alice'de ev yemekleri. Street art turları muhteşem. Martim Moniz meydanında dünya mutfakları.''',
      'tip':
          "28 numaralı tramvay ikonik ama çok kalabalık. Sabah erken git ya da 12E tramvayını dene, aynı rota daha boş!",
    };
  }

  static Map<String, String> _getMilanoContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro': "Milano'ya hoş geldin! Moda, tasarım ve gizli avluların şehri!",
      'recommendations': '''
- [Navigli](search:Navigli) - Kanallar boyunca akşam hayatı! Aperitivo kültürü burada doğdu. Fonderie Milanesi'de kokteyl, Rita's'ta Spritz. Pazar günü antika pazarı. Gece clubları Tortona'da. Vintage mağazalar, street art, bohem ruh.

- [Brera](search:Brera) - Sanat ve tasarım merkezi! Pinacoteca di Brera muhteşem. Dar sokaklarda galeri, butik, tasarımcı mağazalar. Jamaica'da tarihi kafede aperitivo. Gece Bulgari Hotel'in bahçesinde kokteyl (pahalı ama havası var).

- [Isola](search:Isola) - Yükselen mahalle! Eski işçi semti şimdi hipster cenneti. Frida'da brunch, Blue Note'da jazz. Corso Como 10 tasarım mağazası. Gece Bosco Verticale'nin önünde fotoğraf, sonra Ceresio 7'de rooftop havuz kenarı.''',
      'tip':
          "Aperitivo 18:00-21:00 arası: 10€'ya içki + büfe! Navigli'de birkaç bar gez, en dolu büfeyi seç",
    };
  }

  static Map<String, String> _getAmsterdamContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Amsterdam'a hoş geldin! Kanallar, bisikletler ve özgür ruhun şehri!",
      'recommendations': '''
- [De Pijp](search:De Pijp) - Amsterdam'ın en canlı mahallesi! Albert Cuyp pazarı günlük, stroopwafel taze. Brouwerij 't IJ'de değirmende bira, CT Coffee'de kahve. Sarphatipark'ta piknik. Gece küçük barlarda canlı müzik.

- [Jordaan](search:Jordaan) - Kanal boyunca masal! 17. yy evleri, gizli avlular (hofjes), vintage dükkanları. Noordermarkt'ta Pazartesi bit pazarı, Cumartesi farmer's market. Café Papeneiland (1642'den beri!) elmalı turta. Gece bruin café'lerde bira.

- [NDSM Wharf](search:NDSM Wharf) - Eski tersane şimdi kültür merkezi! Street art, festival, plaj barı. Pllek'te nehir kenarında brunch. IJ-Hallen'de Avrupa'nın en büyük bit pazarı (ayda 2 kez). Ücretsiz feribot merkeze gidiyor.''',
      'tip':
          "Bisiklet kirala! 10€/gün, şehri gerçekten keşfetmenin tek yolu. Ama tramvay raylarına dikkat et!",
    };
  }

  static Map<String, String> _getTokyoContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "Tokyo'ya hoş geldin! Gelecek ve gelenek, kaos ve düzen bir arada!",
      'recommendations': '''
- [Shimokitazawa](search:Shimokitazawa) - Tokyo'nun en cool mahallesi! Vintage dükkanları, küçük kafeler, canlı müzik sahneleri. Trendy olmayan bir şekilde trendy. Shirohige's Cream Puff (Totoro şeklinde!) kaçırma. Gece küçük izakaya'larda sake.

- [Yanaka](search:Yanaka) - Eski Tokyo! Edo dönemi atmosferi, ahşap evler, kediler (!). Yanaka Ginza alışveriş sokağı, tapınak ve mezarlık gezisi. Kayaba Coffee tarihi kahve. Sakura zamanı en güzel yer burası.

- [Golden Gai](search:Golden Gai) - 200+ küçük bar sığmış 6 dar sokağa! Her biri 5-10 kişilik, her birinin farklı teması. İlk kez gidenler için ürkütücü ama kapı açık olanları dene. Gece 23:00'den sonra gitmen lazım. Efsanevi deneyim!''',
      'tip':
          "Suica kartı al, her yerde geçerli. Kombini'lerde (7-Eleven, Lawson) yemek kaliteli ve ucuz. Onigiri 150¥!",
    };
  }

  static Map<String, String> _getSeulContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro': "Seul'e hoş geldin! K-pop, BBQ ve 24 saat yaşayan megakent!",
      'recommendations': '''
- [Hongdae](search:Hongdae) - Gençlik enerjisi! Sokak performansları, indie müzik, gece hayatı 24 saat. Özgür park'ta cuma akşamı konser. Vintage mağazalar, K-beauty dükkanları. Thursday Party'de clubbing. Gece ayak masajı salonları!

- [Ikseon-dong Hanok](search:Ikseon-dong Hanok) - Eski-yeni karışımı! 100 yıllık hanok evler şimdi trendy kafe ve butik. Seoul Coffee'de kahve, Gyeongbokgung sarayına 5 dakika. Fotoğraf için altın. Gece yerel makgeolli barlarında.

- [Euljiro](search:Euljiro) - Hipster Seoul! Eski metal işleri dükkanları arasında gizli kafeler ve barlar. Café Onion eski ev fabrikasında. Euljiro 3-ga'da retro izakaya'lar. Cheonggyecheon deresi boyunca gece yürüyüşü romantik.''',
      'tip':
          "T-money kart al, metro ve otobüs için. Gece yarısı subway biter, o yüzden 24 saat barlar ve jimjilbang (sauna) var!",
    };
  }

  static Map<String, String> _getSingapurContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro': "Singapur'a hoş geldin! Gelecekten gelen şehir, yemek cenneti!",
      'recommendations': '''
- [Tiong Bahru](search:Tiong Bahru) - Singapur'un en eski HDB mahallesi şimdi en cool! Art deco binalar, bağımsız kafeler, kitapçılar. 40 Hands'de kahve, Tiong Bahru Bakery'de croissant. Wet market'ta yerel kahvaltı. Street art yürüyüşü.

- [Kampong Glam](search:Kampong Glam) - Arap Sokağı + hipster! Haji Lane dar sokakta graffiti, butik, vintage. Sultan Camii muhteşem. Zam Zam'da murtabak ye. Gece bar hopping, rooftop'lar. Arab Street'te nargile kafeleri.

- [Hawker Centres](search:Hawker Centres) - Singapur'un gerçek yemek kültürü! Maxwell Food Centre, Lau Pa Sat, Chinatown Complex. Michelin yıldızlı yemekler 5 SGD! Tian Tian Hainanese Chicken Rice efsane. Gece Clarke Quay'de riverside içki.''',
      'tip':
          "Hawker'larda yemek ye, restoranlara gitme. 5 SGD'ye Michelin kalitesi! Kopi (kahve) ve Teh (çay) dene",
    };
  }

  static Map<String, String> _getDubaiContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro': "Dubai'ye hoş geldin! Çöl mucizesi, lüks ve kontrast şehri!",
      'recommendations': '''
- [Al Fahidi Tarihi Bölgesi](search:Al Fahidi Tarihi Bölgesi) - Dubai'nin ruhu burada! Burj Khalifa'dan önce Dubai böyleydi. Rüzgar kuleleri, müzeler, sanat galerileri. Arabian Tea House'da kahvaltı, XVA Cafe'de öğle. Creek'te abra (1 AED!) ile karşıya geç.

- [Alserkal Avenue](search:Alserkal Avenue) - Dubai'nin sanat merkezi! Eski endüstri bölgesi şimdi 40+ galeri, tasarım stüdyosu. The Third Line, Carbon 12 önemli galeriler. Tom&Serg'de brunch. Cinema Akil'de bağımsız film.

- [Jumeirah Beach & Kite Beach](search:Jumeirah Beach & Kite Beach) - Şehrin plajı! Burj Al Arab manzarası. Kite Beach'te aktiviteler, Salt burger, Salt'bae değil gerçek Salt! Gece La Mer'de yürüyüş. Madinat Jumeirah'ta abra turu.''',
      'tip':
          "Cuma günü brunch kültürü var. 200-400 AED'ye sınırsız yiyecek ve içecek büfeleri. Rezervasyon şart!",
    };
  }

  static Map<String, String> _getNewYorkContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    return {
      'intro':
          "New York'a hoş geldin! Dünyanın başkenti, 24 saat uyumayan şehir!",
      'recommendations': '''
- [Lower East Side](search:Lower East Side) - Manhattan'ın en cool mahallesi! Göçmen tarihi + modern sanat. Katz's Deli (pastrami efsane!), Russ & Daughters (bagel). Essex Market'ta yemek turu. Gece rooftop barları, speakeasy'ler (Please Don't Tell!).

- [Williamsburg, Brooklyn](search:Williamsburg, Brooklyn) - Hipster başkenti! Bedford Ave butik mağazalar, vintage, plak. Smorgasburg (hafta sonu yemek pazarı) muhteşem. Domino Park'ta skyline. Gece Music Hall'da konser, Brooklyn Bowl'da bowling.

- [Bushwick, Brooklyn](search:Bushwick, Brooklyn) - Street art cenneti! Duvar boyamaları her yerde. Roberta's'ta pizza (bahçede), House of Yes'te queer party. Gece kulüpleri underground. Gündüz kafeler, gece rave. Brooklyn'in yükselen yıldızı.''',
      'tip':
          "Subway 24 saat açık! MetroCard değil OMNY (temassız) kullan. Dollar pizza hala 1\$ ve lezzetli",
    };
  }

  static Map<String, String> _getBrukselContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro':
            "Welcome to Brussels! The heart of Europe, where history meets comic art and chocolate!",
        'recommendations': '''
- [Grand Place & Beyond](search:Grand Place & Beyond) - One of the world's most beautiful squares! But don't just stay there. Dive into the Marolles district for vintage shops and the daily flea market at Place du Jeu de Balle. Visit the Atomium for a futuristic view.

- [Comic Strip Route](search:Comic Strip Route) - Walk the city and find Tintin, Smurfs, and more painted on walls! It's a fun, free open-air museum. Stop by the Comics Art Museum if you want more.

- [Sablon District](search:Sablon District) - For the chocolate lover! Wittamer, Pierre Marcolini... the best chocolatiers are here. Also great for antique hunting and cozy cafes.''',
        'tip':
            "Don't leave without trying mussels (moules-frites) and a warm waffle from a street vendor!",
      };
    }
    return {
      'intro':
          "Brüksel'e hoş geldin! Avrupa'nın kalbi, tarihin çizgi romanla ve çikolatayla buluştuğu yer!",
      'recommendations': '''
- [Grand Place ve Ötesi](search:Grand Place ve Ötesi) - Dünyanın en güzel meydanlarından biri! Ama sadece orada kalma. Marolles mahallesine dal, vintage dükkanları ve Place du Jeu de Balle'deki günlük bit pazarını keşfet. Fütüristik bir manzara için Atomium'a git.

- [Çizgi Roman Rotası](search:Çizgi Roman Rotası) - Şehri yürüyerek gez ve duvarlarda Tenten, Şirinler ve daha fazlasını bul! Eğlenceli, ücretsiz bir açık hava müzesi. Daha fazlasını istersen Çizgi Roman Müzesi'ne uğra.

- [Sablon Bölgesi](search:Sablon Bölgesi) - Çikolata aşıkları için cennet! Wittamer, Pierre Marcolini... en iyi çikolatacılar burada. Ayrıca antika avı ve şirin kafeler için harika.''',
      'tip':
          "Midye (moules-frites) ve sokak satıcısından sıcak bir waffle yemeden dönme!",
    };
  }

  static Map<String, String> _getOsloContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro':
            "Welcome to Oslo! Nature and modernity living in perfect harmony by the fjord!",
        'recommendations': '''
- [Oslo Opera House](search:Oslo Opera House) - Walk on the roof! This marble masterpiece rises from the fjord like an iceberg. Great for sunset views and photos. Nearby, explore the new Munch Museum.

- [Grünerløkka](search:Grünerløkka) - The hipster heart of Oslo! Street art, independent boutiques, vintage shops, and cool cafes along the Akerselva River. Sunday market at Birkelunden is a must.

- [Vigeland Park](search:Vigeland Park) - The world's largest sculpture park by a single artist. 200+ bronze and granite sculptures. Weird, wonderful, and free! Perfect for a picnic.''',
        'tip':
            "Oslo can be expensive. Buy an Oslo Pass for free transport and museum entries, or enjoy the many free parks and nature walks!",
      };
    }
    return {
      'intro':
          "Oslo'ya hoş geldin! Doğa ve modernliğin fiyort kenarında mükemmel uyumu!",
      'recommendations': '''
- [Oslo Opera Binası](search:Oslo Opera Binası) - Çatısında yürü! Bu mermer şaheser, fiyorttan bir buzdağı gibi yükseliyor. Gün batımı ve fotoğraf için harika. Yakınlardaki yeni Munch Müzesi'ni keşfet.

- [Grünerløkka](search:Grünerløkka) - Oslo'nun hipster kalbi! Akerselva Nehri boyunca sokak sanatı, bağımsız butikler, vintage dükkanlar ve havalı kafeler. Birkelunden'deki Pazar pazarı mutlaka görülmeli.

- [Vigeland Parkı](search:Vigeland Parkı) - Tek bir sanatçı tarafından yapılan dünyanın en büyük heykel parkı. 200'den fazla bronz ve granit heykel. Tuhaf, harika ve ücretsiz! Piknik için mükemmel.''',
      'tip':
          "Oslo pahalı olabilir. Ücretsiz ulaşım ve müze girişleri için Oslo Pass al veya birçok ücretsiz parkın ve doğa yürüyüşünün tadını çıkar!",
    };
  }

  static Map<String, String> _getKapadokyaContent(
    List<String> interests,
    String budget,
    bool isEnglish,
  ) {
    if (isEnglish) {
      return {
        'intro': "Welcome to Cappadocia! A fairytale land of fairy chimneys and balloons!",
        'recommendations': '''
- [Goreme Open Air Museum](search:Goreme Open Air Museum) - A UNESCO World Heritage site! Historic rock-cut churches, colorful frescoes, and monastic life. The Dark Church is a must-see (extra ticket but worth it). Visit early in the morning.

- [Uchisar Castle](search:Uchisar Castle) - The highest point of Cappadocia! Magnificent panoramic view. Watch the sunset here, seeing Mount Erciyes and all the valleys under your feet. The rooms carved into the rock inside the castle are fascinating.

- [Pasabag Valley (Monks Valley)](search:Pasabag Valley) - The best place to see fairy chimneys! Some are multi-headed. Legend has it monks used to live here in seclusion. Perfect for walking and taking photos. Admission is free.''',
        'tip':
            "A hot air balloon flight at sunrise is an unforgettable experience! If it exceeds your budget, get up early and watch the balloons from the panoramic hill in cafes.",
      };
    }
    return {
      'intro': "Kapadokya'ya hoş geldin! Peribacaları ve balonların masalsı diyarı!",
      'recommendations': '''
- [Göreme Açık Hava Müzesi](search:Göreme Açık Hava Müzesi) - UNESCO Dünya Mirası! Kayalara oyulmuş tarihi kiliseler, renkli freskler ve manastır hayatı. Karanlık Kilise'yi mutlaka gör (ekstra biletli ama değer). Sabah erken saatte gez.

- [Uçhisar Kalesi](search:Uçhisar Kalesi) - Kapadokya'nın zirvesi! Muhteşem panoramik manzara. Gün batımını buradan izle, Erciyes Dağı ve tüm vadiler ayaklarının altında. Kale içindeki kayaya oyulmuş odalar büyüleyici.

- [Paşabağları (Rahipler Vadisi)](search:Paşabağları) - Peribacalarını en net görebileceğin yer! Bazıları çok başlı. Efsaneye göre eskiden rahipler burada inzivaya çekilirmiş. Yürüyüş ve fotoğraf için harika. Giriş ücretsiz.''',
      'tip':
          "Gün doğumunda sıcak hava balonu turu unutulmaz bir deneyim! Bütçeni aşıyorsa, erken kalkıp kafelerden veya tepeden balonların havalanışını izle.",
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
  // =========================================================================
  // CITY GUIDE / BLOG FEATURE
  // =========================================================================

  /// Şehir rehberi konularını getirir
  /// Rehber için şehir listesini getirir - TÜM 36 ŞEHİR
  static List<Map<String, dynamic>> getAllCitiesForGuide(bool isEnglish) {
    return [
      // Popüler Şehirler
      {
        'city': isEnglish ? 'Istanbul' : 'İstanbul',
        'subtitle': isEnglish ? 'Where East meets West' : 'İki kıtanın buluşma noktası',
        'imageUrl': getCityImage('istanbul'),
      },
      {
        'city': 'Barcelona',
        'subtitle': isEnglish ? 'Gaudí\'s playground' : 'Gaudí\'nin başyapıtı',
        'imageUrl': getCityImage('barcelona'),
      },
      {
        'city': 'Paris',
        'subtitle': isEnglish ? 'City of lights & love' : 'Işıklar ve aşk şehri',
        'imageUrl': getCityImage('paris'),
      },
      {
        'city': isEnglish ? 'Rome' : 'Roma',
        'subtitle': isEnglish ? 'The eternal city' : 'Ebedi şehir',
        'imageUrl': getCityImage('roma'),
      },
      {
        'city': isEnglish ? 'London' : 'Londra',
        'subtitle': isEnglish ? 'Royal history, modern pulse' : 'Kraliyet mirası, modern enerji',
        'imageUrl': getCityImage('londra'),
      },
      // Avrupa
      {
        'city': 'Amsterdam',
        'subtitle': isEnglish ? 'Canals, bikes & culture' : 'Kanallar, bisikletler ve kültür',
        'imageUrl': getCityImage('amsterdam'),
      },
      {
        'city': isEnglish ? 'Athens' : 'Atina',
        'subtitle': isEnglish ? 'Cradle of civilization' : 'Medeniyetin beşiği',
        'imageUrl': getCityImage('atina'),
      },
      {
        'city': 'Berlin',
        'subtitle': isEnglish ? 'Art, history & freedom' : 'Sanat, tarih ve özgürlük',
        'imageUrl': getCityImage('berlin'),
      },
      {
        'city': isEnglish ? 'Budapest' : 'Budapeşte',
        'subtitle': isEnglish ? 'Pearl of the Danube' : 'Tuna\'nın incisi',
        'imageUrl': getCityImage('budapeste'),
      },
      {
        'city': isEnglish ? 'Copenhagen' : 'Kopenhag',
        'subtitle': isEnglish ? 'Hygge & design' : 'Hygge ve tasarım',
        'imageUrl': getCityImage('kopenhag'),
      },
      {
        'city': 'Dublin',
        'subtitle': isEnglish ? 'Pubs, poets & craic' : 'Publar, şairler ve eğlence',
        'imageUrl': getCityImage('dublin'),
      },
      {
        'city': isEnglish ? 'Florence' : 'Floransa',
        'subtitle': isEnglish ? 'Renaissance masterpiece' : 'Rönesans\'ın kalbi',
        'imageUrl': getCityImage('floransa'),
      },
      {
        'city': isEnglish ? 'Geneva' : 'Cenevre',
        'subtitle': isEnglish ? 'Luxury meets nature' : 'Lüks ve doğanın buluşması',
        'imageUrl': getCityImage('cenevre'),
      },
      {
        'city': isEnglish ? 'Lisbon' : 'Lizbon',
        'subtitle': isEnglish ? 'Hills, tiles & fado' : 'Tepeler, çiniler ve fado',
        'imageUrl': getCityImage('lizbon'),
      },
      {
        'city': 'Lucerne',
        'subtitle': isEnglish ? 'Alpine lake paradise' : 'Alp göllerinin cenneti',
        'imageUrl': getCityImage('lucerne'),
      },
      {
        'city': 'Lyon',
        'subtitle': isEnglish ? 'Gastronomy capital' : 'Gastronomi başkenti',
        'imageUrl': getCityImage('lyon'),
      },
      {
        'city': 'Madrid',
        'subtitle': isEnglish ? 'Art, tapas & nightlife' : 'Sanat, tapas ve gece hayatı',
        'imageUrl': getCityImage('madrid'),
      },
      {
        'city': isEnglish ? 'Marseille' : 'Marsilya',
        'subtitle': isEnglish ? 'Mediterranean soul' : 'Akdeniz\'in ruhu',
        'imageUrl': getCityImage('marsilya'),
      },
      {
        'city': isEnglish ? 'Milan' : 'Milano',
        'subtitle': isEnglish ? 'Fashion & design hub' : 'Moda ve tasarım merkezi',
        'imageUrl': getCityImage('milano'),
      },
      {
        'city': isEnglish ? 'Naples' : 'Napoli',
        'subtitle': isEnglish ? 'Pizza, passion & chaos' : 'Pizza, tutku ve kaos',
        'imageUrl': getCityImage('napoli'),
      },
      {
        'city': 'Nice',
        'subtitle': isEnglish ? 'Riviera glamour' : 'Fransız Rivierası\'nın incisi',
        'imageUrl': getCityImage('nice'),
      },
      {
        'city': 'Porto',
        'subtitle': isEnglish ? 'Wine & riverside charm' : 'Şarap ve nehir kenarı büyüsü',
        'imageUrl': getCityImage('porto'),
      },
      {
        'city': isEnglish ? 'Brussels' : 'Brüksel',
        'subtitle': isEnglish ? 'Heart of Europe' : 'Avrupa\'nın Kalbi',
        'imageUrl': getCityImage('bruksel'),
      },
      {
        'city': 'Oslo',
        'subtitle': isEnglish ? 'Fjords & Modernity' : 'Fiyortlar ve Modernizm',
        'imageUrl': getCityImage('oslo'),
      },
      {
        'city': isEnglish ? 'Prague' : 'Prag',
        'subtitle': isEnglish ? 'City of a hundred spires' : 'Yüz kuleli şehir',
        'imageUrl': getCityImage('prag'),
      },
      {
        'city': isEnglish ? 'Seville' : 'Sevilla',
        'subtitle': isEnglish ? 'Flamenco & orange trees' : 'Flamenko ve portakal ağaçları',
        'imageUrl': getCityImage('sevilla'),
      },
      {
        'city': 'Stockholm',
        'subtitle': isEnglish ? 'Nordic elegance' : 'İskandinav zarafeti',
        'imageUrl': getCityImage('stockholm'),
      },
      {
        'city': isEnglish ? 'Venice' : 'Venedik',
        'subtitle': isEnglish ? 'Floating romantic dream' : 'Suda yüzen romantizm',
        'imageUrl': getCityImage('venedik'),
      },
      {
        'city': isEnglish ? 'Vienna' : 'Viyana',
        'subtitle': isEnglish ? 'Imperial splendor & music' : 'İmparatorluk ihtişamı ve müzik',
        'imageUrl': getCityImage('viyana'),
      },
      {
        'city': isEnglish ? 'Zurich' : 'Zürih',
        'subtitle': isEnglish ? 'Swiss precision & lakes' : 'İsviçre kalitesi ve göller',
        'imageUrl': getCityImage('zurih'),
      },
      // Asya
      {
        'city': 'Bangkok',
        'subtitle': isEnglish ? 'Temples, street food & chaos' : 'Tapınaklar, sokak yemekleri ve kaos',
        'imageUrl': getCityImage('bangkok'),
      },
      {
        'city': 'Dubai',
        'subtitle': isEnglish ? 'Desert luxury & modernity' : 'Çöl lüksü ve modernlik',
        'imageUrl': getCityImage('dubai'),
      },
      {
        'city': 'Hong Kong',
        'subtitle': isEnglish ? 'Skyline & dim sum' : 'Gökdelenler ve dim sum',
        'imageUrl': getCityImage('hongkong'),
      },
      {
        'city': isEnglish ? 'Seoul' : 'Seul',
        'subtitle': isEnglish ? 'K-culture & traditions' : 'K-kültürü ve gelenekler',
        'imageUrl': getCityImage('seul'),
      },
      {
        'city': isEnglish ? 'Singapore' : 'Singapur',
        'subtitle': isEnglish ? 'Garden city of the future' : 'Geleceğin bahçe şehri',
        'imageUrl': getCityImage('singapur'),
      },
      {
        'city': 'Tokyo',
        'subtitle': isEnglish ? 'Neon lights & zen gardens' : 'Neon ışıklar ve zen bahçeleri',
        'imageUrl': getCityImage('tokyo'),
      },
      // Afrika
      {
        'city': isEnglish ? 'Marrakech' : 'Marakeş',
        'subtitle': isEnglish ? 'Medina magic & spices' : 'Medina büyüsü ve baharatlar',
        'imageUrl': getCityImage('marakes'),
      },
      // Amerika
      {
        'city': 'New York',
        'subtitle': isEnglish ? 'The city that never sleeps' : 'Hiç uyumayan şehir',
        'imageUrl': getCityImage('newyork'),
      },
      {
        'city': 'Rovaniemi',
        'subtitle': isEnglish ? 'Home of Santa Claus' : 'Noel Baba\'nın Evi',
        'imageUrl': getCityImage('rovaniemi'),
      },
      {
        'city': 'Tromso',
        'subtitle': isEnglish ? 'Arctic Gateway' : 'Kutup Kapısı',
        'imageUrl': getCityImage('tromso'),
      },
      {
        'city': 'Zermatt',
        'subtitle': isEnglish ? 'Matterhorn & Ski' : 'Matterhorn ve Kayak',
        'imageUrl': getCityImage('zermatt'),
      },
      {
        'city': 'Matera',
        'subtitle': isEnglish ? 'City of Stones' : 'Taşların Şehri',
        'imageUrl': getCityImage('matera'),
      },
      {
        'city': 'Giethoorn',
        'subtitle': isEnglish ? 'Venice of the North' : 'Kuzeyin Venedik\'i',
        'imageUrl': getCityImage('giethoorn'),
      },
      {
        'city': 'Kotor',
        'subtitle': isEnglish ? 'Medieval Fjord' : 'Ortaçağ Fiyortu',
        'imageUrl': getCityImage('kotor'),
      },
      {
        'city': 'Colmar',
        'subtitle': isEnglish ? 'Fairytale Town' : 'Masal Kasabası',
        'imageUrl': getCityImage('colmar'),
      },
      {
        'city': 'Sintra',
        'subtitle': isEnglish ? 'Mystic Palaces' : 'Mistik Saraylar',
        'imageUrl': getCityImage('sintra'),
      },
      {
        'city': 'San Sebastian',
        'subtitle': isEnglish ? 'Culinary Capital' : 'Lezzet Başkenti',
        'imageUrl': getCityImage('sansebastian'),
      },
      {
        'city': 'Bologna',
        'subtitle': isEnglish ? 'La Rossa' : 'Kızıl Şehir',
        'imageUrl': getCityImage('bologna'),
      },
      {
        'city': 'Gaziantep',
        'subtitle': isEnglish ? 'Taste of History' : 'Tarihin Tadı',
        'imageUrl': getCityImage('gaziantep'),
      },
      {
        'city': 'Brugge',
        'subtitle': isEnglish ? 'Canals & Waffles' : 'Kanallar ve Waffle',
        'imageUrl': getCityImage('brugge'),
      },
      {
        'city': 'Santorini',
        'subtitle': isEnglish ? 'Blue & White' : 'Mavi ve Beyaz',
        'imageUrl': getCityImage('santorini'),
      },
      {
        'city': 'Heidelberg',
        'subtitle': isEnglish ? 'Romantic Ruins' : 'Romantik Harabeler',
        'imageUrl': getCityImage('heidelberg'),
      },
      // Yeni Eklenenler
      {
        'city': 'Antalya',
        'subtitle': isEnglish ? 'Turquoise Coast' : 'Turkuaz Kıyılar',
        'imageUrl': getCityImage('antalya'),
      },
      {
        'city': isEnglish ? 'Cappadocia' : 'Kapadokya',
        'subtitle': isEnglish ? 'Fairy Chimneys' : 'Peri Bacaları',
        'imageUrl': getCityImage('kapadokya'),
      },
      {
        'city': isEnglish ? 'Belgrade' : 'Belgrad',
        'subtitle': isEnglish ? 'White City' : 'Beyaz Şehir',
        'imageUrl': getCityImage('belgrad'),
      },
      {
        'city': 'Edinburgh',
        'subtitle': isEnglish ? 'Gothic Charm' : 'Gotik Büyü',
        'imageUrl': getCityImage('edinburgh'),
      },
      {
        'city': 'Hallstatt',
        'subtitle': isEnglish ? 'Alpine Fairytale' : 'Alp Masalı',
        'imageUrl': getCityImage('hallstatt'),
      },
      {
        'city': isEnglish ? 'Strasbourg' : 'Strazburg',
        'subtitle': isEnglish ? 'Capital of Christmas' : 'Noel\'in Başkenti',
        'imageUrl': getCityImage('strazburg'),
      },
      {
        'city': isEnglish ? 'Cairo' : 'Kahire',
        'subtitle': isEnglish ? 'Pyramids & History' : 'Piramitler ve Tarih',
        'imageUrl': getCityImage('kahire'),
      },
      {
        'city': 'Fes',
        'subtitle': isEnglish ? 'Ancient Medina' : 'Antik Medina',
        'imageUrl': getCityImage('fes'),
      },
    ];
  }


  /// Detaylı blog içeriğini getirir (Markdown formatında)
  static Future<String> getCityBlogContent(String city, bool isEnglish) async {
    // Yapay bir bekleme süresi (AI simülasyonu)
    await Future.delayed(const Duration(milliseconds: 800));
    return CityBlogContent.getRemoteContent(city, isEnglish);
  }

  /// Özel makale içeriğini getirir
  static Future<String> getArticleContent(String articleId, bool isEnglish) async {
    await Future.delayed(const Duration(milliseconds: 600)); // Simülasyon
    return CityBlogContent.getArticleContent(articleId, isEnglish);
  }
}
