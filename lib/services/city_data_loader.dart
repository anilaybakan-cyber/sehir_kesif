// =============================================================================
// CITY DATA LOADER v2
// - 18 şehri destekler
// - Hata yakalama
// - Debug bilgisi
// =============================================================================

import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import '../models/city_model.dart';

class CityDataLoader {
  // Desteklenen şehirler - 18 şehir
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
  ];

  /// Şehir verisini yükler
  /// [cityName] - Şehir adı (küçük harf, örn: "paris", "roma")
  static Future<CityModel> loadCity(String cityName) async {
    final safe = cityName.toLowerCase().trim();

    debugPrint("🌍 CityDataLoader: '$safe' şehri yükleniyor...");

    // Şehir adını normalize et
    String normalizedName = _normalizeCityName(safe);

    try {
      final path = "assets/cities/$normalizedName.json";
      debugPrint("📂 JSON path: $path");

      final data = await rootBundle.loadString(path);
      debugPrint("✅ JSON yüklendi: ${data.length} karakter");

      final jsonData = json.decode(data) as Map<String, dynamic>;
      debugPrint(
        "✅ JSON parse edildi: ${jsonData['city']} - ${jsonData['highlights']?.length ?? 0} mekan",
      );

      final city = CityModel.fromJson(jsonData);
      debugPrint(
        "✅ CityModel oluşturuldu: ${city.city} (${city.highlights.length} highlight)",
      );

      return city;
    } catch (e, stackTrace) {
      debugPrint("❌ Şehir yükleme hatası: $e");
      debugPrint("📍 Stack trace: $stackTrace");

      // Fallback: Barcelona'yı yükle
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
    };

    return aliases[name] ?? name.toLowerCase();
  }

  /// Şehrin desteklenip desteklenmediğini kontrol eder
  static bool isSupported(String cityName) {
    final normalized = _normalizeCityName(cityName.toLowerCase());
    return supportedCities.contains(normalized);
  }

  /// Desteklenen şehir listesini döndürür
  static List<String> getSupportedCities() {
    return List.from(supportedCities);
  }

  /// Şehir önizleme bilgilerini yükler (hafif versiyon)
  static Future<Map<String, dynamic>> loadCityPreview(String cityName) async {
    final safe = _normalizeCityName(cityName.toLowerCase().trim());

    try {
      final data = await rootBundle.loadString("assets/cities/$safe.json");
      final jsonData = json.decode(data) as Map<String, dynamic>;

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
