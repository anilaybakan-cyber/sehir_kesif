import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:path_provider/path_provider.dart';
import '../models/city_model.dart';
import 'content_update_service.dart';
import '../screens/city_switcher_screen.dart';

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
    'bodrum',
    'cesme',
    'mykonos',
    'dubrovnik',
    'amalfi',
    'ibiza',
    'mallorca',
    'valencia',
    'kas',
    'palermo',
    'catania',
    'bari',
    'budva',
    'ksamil',
    'selanik',
    'rhodes',
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
    'cannes',
    'saint_tropez',
  ];


  /// Bellek cache'i — aynı şehir tekrar istendiğinde disk I/O + JSON parse atlanır.
  static final Map<String, CityModel> _memoryCache = {};

  /// Cache'i temizler (şehir değiştiğinde veya OTA güncelleme sonrası çağrılır).
  static void invalidateCache([String? cityName]) {
    if (cityName != null) {
      _memoryCache.remove(cityName.toLowerCase().trim());
    } else {
      _memoryCache.clear();
    }
  }

  /// Şehir verisini yükler (Önce Memory Cache, sonra Asset/Disk)
  static Future<CityModel> loadCity(String cityName) async {
    final safeName = cityName.toLowerCase().trim();
    // Sardinya şu an uygulama listesinde yok; eski seçim/cache için Sicilya kıyısı kullan.
    if (safeName == 'sardinya' || safeName == 'sardinia') {
      return loadCity('catania');
    }
    String normalizedName = _normalizeCityName(safeName);

    // ⚡ Memory cache — tekrar disk okuması yapma
    if (_memoryCache.containsKey(normalizedName)) {
      debugPrint("⚡ CityDataLoader: '$normalizedName' memory cache'ten döndü");
      return _memoryCache[normalizedName]!;
    }

    // 🧹 CACHE CLEANUP: Eğer eski bozuk URL'ler cache'e girmişse temizle (Bir kez çalışır)
    try {
      final docDir = await getApplicationDocumentsDirectory();
      final citiesDir = Directory('${docDir.path}/cities');
      if (await citiesDir.exists()) {
        // Barcelona dosyasına bak, eğer eski URL formatı varsa tüm klasörü temizle
        final testFile = File('${citiesDir.path}/barcelona.json');
        if (await testFile.exists()) {
          final content = await testFile.readAsString();
          if (content.contains('storage.googleapis.com')) {
            debugPrint("🧹 Bozuk URL cache'i tespit edildi, temizleniyor...");
            await citiesDir.delete(recursive: true);
          }
        }
      }
    } catch (e) {
      debugPrint("⚠️ Cache temizleme hatası: $e");
    }

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

      // 3. ULTIMATE MERGE: Her iki kaynaktaki mekanları birleştir (ID bazlı tekilleştirme)
      if (assetCity != null || localCity != null) {
        final Map<String, Highlight> mergedHighlights = {};
        
        String normalizeKey(String name) {
          // Slugify name for consistent matching (lowercase, alphanumeric only)
          return name.toLowerCase().trim().replaceAll(RegExp(r'[^a-z0-9]'), '');
        }

        // Önce OTA (İnternetten gelenler) verisini ekle
        if (localCity != null) {
          for (var item in localCity.highlights) {
            final key = normalizeKey(item.name);
            if (key.isNotEmpty) mergedHighlights[key] = _withNormalizedImageUrl(item);
          }
        }
        
        // Sonra Asset (Yerel dosya) verisini ekle (Aynı isim varsa üzerine yazar/günceller)
        if (assetCity != null) {
          for (var item in assetCity.highlights) {
            final key = normalizeKey(item.name);
            if (key.isNotEmpty) {
              final normalizedAsset = _withNormalizedImageUrl(item);
              final existing = mergedHighlights[key];
              if (existing != null) {
                // Asset metadata'sını kullan, ancak asset görseli zayıf/boşsa local görseli koru.
                final keepExistingImage =
                    !_hasUsableImage(normalizedAsset.imageUrl) &&
                    _hasUsableImage(existing.imageUrl);
                if (keepExistingImage) {
                  mergedHighlights[key] = _copyHighlightWithImage(
                    normalizedAsset,
                    existing.imageUrl,
                  );
                } else {
                  mergedHighlights[key] = normalizedAsset;
                }
              } else {
                mergedHighlights[key] = normalizedAsset;
              }
            }
          }
        }

        // Ana modeli oluştur (AssetCity temel alınır ama mekanlar birleştirilmiştir)
        final baseCity = assetCity ?? localCity!;
        final finalCity = CityModel(
          city: baseCity.city,
          cityEn: baseCity.cityEn,
          country: baseCity.country,
          countryEn: baseCity.countryEn,
          description: baseCity.description,
          descriptionEn: baseCity.descriptionEn,
          heroImage: baseCity.heroImage,
          highlights: mergedHighlights.values.toList(),
          centerLat: baseCity.centerLat,
          centerLng: baseCity.centerLng,
          curatedRoutes: baseCity.curatedRoutes,
        );

        debugPrint("💎 MERGE TAMAMLANDI: Toplam ${finalCity.highlights.length} eşsiz mekan gösteriliyor.");
        _memoryCache[normalizedName] = finalCity;
        return finalCity;
      }

      throw Exception("Hiçbir veri kaynağı bulunamadı.");

    } catch (e) {
      debugPrint("❌ Şehir yükleme hatası ($normalizedName): $e");
      if (normalizedName != 'barcelona') {
        return loadCity('barcelona');
      }
      rethrow;
    }
  }

  static bool _hasUsableImage(String? imageUrl) {
    if (imageUrl == null || imageUrl.trim().isEmpty) return false;
    final normalized = _normalizeImageUrl(imageUrl);
    if (normalized == null || normalized.isEmpty) return false;
    return normalized.startsWith('http://') || normalized.startsWith('https://');
  }

  static Highlight _withNormalizedImageUrl(Highlight source) {
    return _copyHighlightWithImage(source, _normalizeImageUrl(source.imageUrl));
  }

  static String? _normalizeImageUrl(String? rawUrl) {
    if (rawUrl == null) return null;
    final trimmed = rawUrl.trim();
    if (trimmed.isEmpty) return null;

    final uri = Uri.tryParse(trimmed);
    if (uri == null) return trimmed;

    // Direct GCS URL → Firebase Storage REST URL (Firebase Rules tarafından
    // yetkilendirilen public URL formatı). Bucket public olmadığı için direct
    // GCS host'u 403/timeout verir; REST endpoint Storage Rules'ı kullanır.
    // https://storage.googleapis.com/<bucket>/<objectPath>
    //   →
    // https://firebasestorage.googleapis.com/v0/b/<bucket>/o/<encodedObjectPath>?alt=media
    if (uri.host == 'storage.googleapis.com' && uri.pathSegments.length >= 2) {
      final bucket = uri.pathSegments.first;
      final objectPath = uri.pathSegments.sublist(1).join('/');
      if (bucket.isNotEmpty && objectPath.isNotEmpty) {
        final encoded = Uri.encodeComponent(objectPath);
        return 'https://firebasestorage.googleapis.com/v0/b/$bucket/o/$encoded?alt=media';
      }
    }

    return trimmed;
  }

  static Highlight _copyHighlightWithImage(Highlight source, String? imageUrl) {
    return Highlight(
      id: source.id,
      name: source.name,
      area: source.area,
      category: source.category,
      city: source.city,
      tags: source.tags,
      distanceFromCenter: source.distanceFromCenter,
      lat: source.lat,
      lng: source.lng,
      price: source.price,
      description: source.description,
      imageUrl: imageUrl,
      tips: source.tips,
      descriptionEn: source.descriptionEn,
      nameEn: source.nameEn,
      areaEn: source.areaEn,
      tipsEn: source.tipsEn,
      bestTime: source.bestTime,
      bestTimeEn: source.bestTimeEn,
      duration: source.duration,
      rating: source.rating,
      reviewCount: source.reviewCount,
      metro: source.metro,
      priceRange: source.priceRange,
      website: source.website,
      phone: source.phone,
      instagram: source.instagram,
      parking: source.parking,
      reservation: source.reservation,
      openHours: source.openHours,
      features: source.features,
    );
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
      'sarajevo': 'saraybosna',
      'saraybosna': 'saraybosna',
      'san sebastian': 'san_sebastian',
      'sansebastian': 'san_sebastian',
      'saint tropez': 'saint_tropez',
      'saint-tropez': 'saint_tropez',
      'saint_tropez': 'saint_tropez',
      'lesbos': 'midilli',
      'lesvos': 'midilli',
    };

    return aliases[name] ?? name.toLowerCase();
  }

  static bool isSupported(String cityName) {
    final normalized = _normalizeCityName(cityName.toLowerCase());
    // Hem hardcoded hem OTA şehirleri kontrol et
    if (supportedCities.contains(normalized)) return true;
    return CitySwitcherScreen.allCities.any((c) => c['id'] == normalized);
  }

  static List<String> getSupportedCities() {
    // Hardcoded + OTA şehirleri birleştir
    final ids = <String>{...supportedCities};
    for (final c in CitySwitcherScreen.allCities) {
      if (c['id'] != null) ids.add(c['id'] as String);
    }
    return ids.toList();
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

      // 3. Karşılaştır - OTA (Local) varsa o her zaman önceliklidir
      Map<String, dynamic>? selectedData;
      if (localData != null) {
        selectedData = localData;
      } else {
        selectedData = assetData;
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
