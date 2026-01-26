import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import '../models/city_model.dart';
import 'content_update_service.dart';

class CityDataLoader {
  // Desteklenen şehirler - 30+ şehir
  static const List<String> supportedCities = [
    'istanbul',
    'barcelona',
    'madrid',
    'sevilla',
    'paris',
    'roma',
    'milano',
    'amsterdam',
    'londra',
    'berlin',
    'viyana',
    'prag',
    'lizbon',
    'tokyo',
    'seul',
    'singapur',
    'dubai',
    'newyork',
    'porto',
    'napoli',
    'floransa',
    'venedik',
    'atina',
    'dublin',
    'kopenhag',
    'stockholm',
    'budapeste',
    'bangkok',
    'hongkong',
    'kapadokya',
    'selanik',
    'edinburgh',
    'belgrad',
    'kotor',
    'tiran',
    'fes',
    'safsavan',
    'kahire',
    'saraybosna',
    'mostar',
    'strazburg',
    'midilli',
    'antalya',
    'matera',
    'colmar',
    'rovaniemi',
    'bologna',
    'giethoorn',
    'san_sebastian',
    'gaziantep',
    'brugge',
    'hallstatt',
    'sintra',
    'tromso',
    'lucerne',
    'marakes',
    'heidelberg',
    'santorini',
    'zurih',
    'marsilya',
  ];

  /// Şehir verisini yükler (Önce Asset, Cache fallback)
  static Future<CityModel> loadCity(String cityName) async {
    final safeName = cityName.toLowerCase().trim();
    // Şehir adını normalize et
    String normalizedName = _normalizeCityName(safeName);

    debugPrint("🌍 CityDataLoader: '$normalizedName' verisi isteniyor...");

    try {
      String jsonString;
      
      // 1. Önce Cache'i kontrol et (Güncel veri için)
      try {
        final File? localFile = await ContentUpdateService.getLocalCityFile(normalizedName);
        
        if (localFile != null && await localFile.exists()) {
          debugPrint("📂 CACHE: Yerel dosya bulundu, yükleniyor.");
          jsonString = await localFile.readAsString();
        } else {
          throw Exception("Cache file not found");
        }
      } catch (cacheError) {
        // 2. Cache yoksa Asset'i dene (Fallback)
        // debugPrint("⚠️ Cache yok, Asset deneniyor... ($cacheError)");
        try {
          jsonString = await rootBundle.loadString("assets/cities/$normalizedName.json");
          // debugPrint("📦 ASSET: Uygulama içinden yüklendi.");
        } catch (assetError) {
          debugPrint("❌ Hem Cache hem Asset bulunamadı!");
          rethrow;
        }
      }

      // 3. JSON Parse Et
      final jsonData = json.decode(jsonString) as Map<String, dynamic>;
      final city = CityModel.fromJson(jsonData);
      
      return city;

    } catch (e) {
      debugPrint("❌ Şehir yükleme hatası ($normalizedName): $e");

      // Fallback: Eğer aranan şehir yoksa veya hata varsa Barcelona'yı yükle (Crash olmasın diye)
      if (normalizedName != 'barcelona') {
        debugPrint("⚠️ Fallback: Barcelona yükleniyor...");
        return loadCity('barcelona');
      }
      rethrow;
    }
  }

  /// Şehir adını normalize eder
  static String _normalizeCityName(String name) {
    final Map<String, String> aliases = {
      // Türkçe
      'İstanbul': 'istanbul',
      'istanbul': 'istanbul',
      // İngilizce
      'Rome': 'roma',
      'rome': 'roma',
      'Roma': 'roma',
      'Paris': 'paris',
      'paris': 'paris',
      'Barcelona': 'barcelona',
      'barcelona': 'barcelona',
      'London': 'londra',
      'london': 'londra',
      'Vienna': 'viyana',
      'vienna': 'viyana',
      'Prague': 'prag',
      'prague': 'prag',
      'Lisbon': 'lizbon',
      'lisbon': 'lizbon',
      'Milan': 'milano',
      'milan': 'milano',
      'Seville': 'sevilla',
      'seville': 'sevilla',
      'Seoul': 'seul',
      'seoul': 'seul',
      'Singapore': 'singapur',
      'singapore': 'singapur',
      'New York': 'newyork',
      'new york': 'newyork',
      'Porto': 'porto',
      'porto': 'porto',
      'Naples': 'napoli',
      'naples': 'napoli',
      'Napoli': 'napoli',
      'Florence': 'floransa',
      'florence': 'floransa',
      'Floransa': 'floransa',
      'Venice': 'venedik',
      'venice': 'venedik',
      'Venedik': 'venedik',
      'Athens': 'atina',
      'athens': 'atina',
      'Atina': 'atina',
      'Dublin': 'dublin',
      'dublin': 'dublin',
      'Copenhagen': 'kopenhag',
      'copenhagen': 'kopenhag',
      'Kopenhag': 'kopenhag',
      'Stockholm': 'stockholm',
      'stockholm': 'stockholm',
      'Budapest': 'budapeste',
      'budapest': 'budapeste',
      'Budapeşte': 'budapeste',
      'Belgrade': 'belgrad',
      'belgrade': 'belgrad',
      'Bangkok': 'bangkok',
      'bangkok': 'bangkok',
      'Hong Kong': 'hongkong',
      'hong kong': 'hongkong',
      'hongkong': 'hongkong',
      'Cappadocia': 'kapadokya',
      'cappadocia': 'kapadokya',
      'Midilli': 'midilli',
      'Lesvos': 'midilli',
      'Mytilene': 'midilli',
      'Brüksel': 'bruksel',
      'brüksel': 'bruksel',
      'Brussels': 'bruksel',
      'brussels': 'bruksel',
      'Bruksel': 'bruksel',
      'Cenevre': 'cenevre',
      'Geneva': 'cenevre',
      'Zürih': 'zurih',
      'Zurich': 'zurih',
      'Strazburg': 'strazburg',
      'Strasbourg': 'strazburg',
      'Marakeş': 'marakes',
      'Marrakech': 'marakes',
    };

    return aliases[name] ?? name.toLowerCase();
  }

  static bool isSupported(String cityName) {
    final normalized = _normalizeCityName(cityName.toLowerCase());
    return supportedCities.contains(normalized);
  }

  static List<String> getSupportedCities() {
    return List.from(supportedCities);
  }

  /// Şehir önizleme bilgilerini yükler (Asset öncelikli)
  static Future<Map<String, dynamic>> loadCityPreview(String cityName) async {
    final safe = _normalizeCityName(cityName.toLowerCase().trim());

    try {
      String jsonString;
      
      // 1. Asset öncelikli
      try {
        jsonString = await rootBundle.loadString("assets/cities/$safe.json");
      } catch (_) {
        // 2. Fallback to Cache
        final File? localFile = await ContentUpdateService.getLocalCityFile(safe);
        if (localFile != null && await localFile.exists()) {
           jsonString = await localFile.readAsString();
        } else {
           throw Exception("Both Asset and Cache missing");
        }
      }
      
      final jsonData = json.decode(jsonString) as Map<String, dynamic>;

      return {
        'city': jsonData['city'],
        'country': jsonData['country'],
        'description': jsonData['description'],
        'highlightCount': (jsonData['highlights'] as List?)?.length ?? 0,
        'coordinates': jsonData['coordinates'],
      };
    } catch (e) {
      return {
        'city': cityName,
        'country': '',
        'description': '',
        'highlightCount': 0,
        'error': e.toString(),
      };
    }
  }
}
