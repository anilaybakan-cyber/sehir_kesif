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
    'zermatt',

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
    String normalizedName = _normalizeCityName(safeName);

    debugPrint("🌍 CityDataLoader: '$normalizedName' için en zengin veri aranıyor...");

    try {
      CityModel? assetCity;
      CityModel? localCity;

      // 1. Asset'i yüklemeyi dene
      try {
        final assetString = await rootBundle.loadString("assets/cities/$normalizedName.json");
        assetCity = CityModel.fromJson(json.decode(assetString));
      } catch (e) {
        debugPrint("⚠️ Asset yüklenemedi: $normalizedName");
      }

      // 2. Local Cache'i yüklemeyi dene
      try {
        final localFile = await ContentUpdateService.getLocalCityFile(normalizedName);
        if (localFile != null && await localFile.exists()) {
          final localString = await localFile.readAsString();
          localCity = CityModel.fromJson(json.decode(localString));
        }
      } catch (e) {
        debugPrint("⚠️ Local cache yüklenemedi: $normalizedName");
      }

      // 3. Karşılaştır ve en çok mekanı olanı seç
      if (assetCity != null && localCity != null) {
        final assetCount = assetCity.highlights.length;
        final localCount = localCity.highlights.length;

        if (localCount >= assetCount) {
          debugPrint("✅ LOCAL seçildi: $localCount mekan (Asset: $assetCount)");
          return localCity;
        } else {
          debugPrint("✅ ASSET seçildi: $assetCount mekan (Local: $localCount)");
          return assetCity;
        }
      }

      // 4. Sadece biri varsa onu dön
      if (localCity != null) return localCity;
      if (assetCity != null) return assetCity;

      throw Exception("Hiçbir veri kaynağı bulunamadı.");

    } catch (e) {
      debugPrint("❌ Şehir yükleme hatası ($normalizedName): $e");
      if (normalizedName != 'barcelona') {
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
    final safeName = _normalizeCityName(cityName.toLowerCase().trim());

    try {
      Map<String, dynamic>? assetData;
      Map<String, dynamic>? localData;

      // 1. Asset'i dene
      try {
        final assetString = await rootBundle.loadString("assets/cities/$safeName.json");
        assetData = json.decode(assetString) as Map<String, dynamic>;
      } catch (e) {
        debugPrint("⚠️ Asset preview hatası: $safeName");
      }

      // 2. Local'i dene
      try {
        final localFile = await ContentUpdateService.getLocalCityFile(safeName);
        if (localFile != null && await localFile.exists()) {
          final localString = await localFile.readAsString();
          localData = json.decode(localString) as Map<String, dynamic>;
        }
      } catch (e) {
        debugPrint("⚠️ Local preview hatası: $safeName");
      }

      // 3. Karşılaştır
      Map<String, dynamic>? selectedData;
      if (assetData != null && localData != null) {
        final assetCount = (assetData['highlights'] as List?)?.length ?? 0;
        final localCount = (localData['highlights'] as List?)?.length ?? 0;
        selectedData = (localCount >= assetCount) ? localData : assetData;
      } else {
        selectedData = localData ?? assetData;
      }

      if (selectedData == null) throw Exception("Veri bulunamadı");

      return {
        'city': selectedData['city'],
        'country': selectedData['country'],
        'description': selectedData['description'],
        'highlightCount': (selectedData['highlights'] as List?)?.length ?? 0,
        'coordinates': selectedData['coordinates'],
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
