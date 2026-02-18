// =============================================================================
// CACHE SERVICE - Offline Mod & Veri Önbellekleme
// - Şehir verilerini local'de sakla
// - Network durumu kontrolü
// - Otomatik sync
// =============================================================================

import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:connectivity_plus/connectivity_plus.dart';
import '../models/city_model.dart';

class CacheService {
  // Cache key'leri
  static const String _cityCachePrefix = 'city_cache_';
  static const String _lastSyncKey = 'last_sync_timestamp';
  static const String _offlineModeKey = 'offline_mode_enabled';

  // Cache süresi (30 gün)
  static const Duration _cacheDuration = Duration(days: 30);

  // Singleton
  static final CacheService _instance = CacheService._internal();
  factory CacheService() => _instance;
  CacheService._internal();

  // Network durumu
  bool _isOnline = true;
  bool get isOnline => _isOnline;

  // Connectivity stream
  final Connectivity _connectivity = Connectivity();

  /// Servisi başlat
  Future<void> init() async {
    // İlk network durumunu kontrol et
    final result = await _connectivity.checkConnectivity();
    _isOnline = result != ConnectivityResult.none;

    // Network değişikliklerini dinle
    _connectivity.onConnectivityChanged.listen((result) {
      _isOnline = result != ConnectivityResult.none;
      debugPrint('📶 Network durumu: ${_isOnline ? "Online" : "Offline"}');
    });
  }

  /// Şehir verisini cache'e kaydet
  Future<void> cacheCity(String cityName, CityModel city) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final key = '$_cityCachePrefix${cityName.toLowerCase()}';

      // CityModel'i JSON'a çevir
      final jsonData = _cityModelToJson(city);
      final cacheData = {
        'data': jsonData,
        'timestamp': DateTime.now().toIso8601String(),
        'version': '1.0',
      };

      await prefs.setString(key, json.encode(cacheData));
      debugPrint('💾 Cache kaydedildi: $cityName');
    } catch (e) {
      debugPrint('❌ Cache kayıt hatası: $e');
    }
  }

  /// Şehir verisini cache'den oku
  Future<CityModel?> getCachedCity(String cityName) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final key = '$_cityCachePrefix${cityName.toLowerCase()}';
      final cached = prefs.getString(key);

      if (cached == null) return null;

      final cacheData = json.decode(cached);
      final timestamp = DateTime.parse(cacheData['timestamp']);

      // Cache süresi dolmuş mu kontrol et (online ise)
      if (_isOnline && DateTime.now().difference(timestamp) > _cacheDuration) {
        debugPrint('⏰ Cache süresi dolmuş: $cityName');
        return null;
      }

      final cityJson = cacheData['data'] as Map<String, dynamic>;
      final city = CityModel.fromJson(cityJson);

      debugPrint(
        '📦 Cache\'den yüklendi: $cityName (${city.highlights.length} mekan)',
      );
      return city;
    } catch (e) {
      debugPrint('❌ Cache okuma hatası: $e');
      return null;
    }
  }

  /// Cache'de şehir var mı kontrol et
  Future<bool> isCityCached(String cityName) async {
    final prefs = await SharedPreferences.getInstance();
    final key = '$_cityCachePrefix${cityName.toLowerCase()}';
    return prefs.containsKey(key);
  }

  /// Tüm cache'lenmiş şehirleri listele
  Future<List<String>> getCachedCities() async {
    final prefs = await SharedPreferences.getInstance();
    final keys = prefs
        .getKeys()
        .where((k) => k.startsWith(_cityCachePrefix))
        .map((k) => k.replaceFirst(_cityCachePrefix, ''))
        .toList();
    return keys;
  }

  /// Belirli bir şehrin cache'ini sil
  Future<void> clearCityCache(String cityName) async {
    final prefs = await SharedPreferences.getInstance();
    final key = '$_cityCachePrefix${cityName.toLowerCase()}';
    await prefs.remove(key);
    debugPrint('🗑️ Cache silindi: $cityName');
  }

  /// Tüm cache'i temizle
  Future<void> clearAllCache() async {
    final prefs = await SharedPreferences.getInstance();
    final keys = prefs.getKeys().where((k) => k.startsWith(_cityCachePrefix));
    for (final key in keys) {
      await prefs.remove(key);
    }
    debugPrint('🗑️ Tüm cache temizlendi');
  }

  /// Cache boyutunu hesapla (yaklaşık)
  Future<int> getCacheSize() async {
    final prefs = await SharedPreferences.getInstance();
    int totalSize = 0;

    for (final key in prefs.getKeys()) {
      if (key.startsWith(_cityCachePrefix)) {
        final value = prefs.getString(key);
        if (value != null) {
          totalSize += value.length;
        }
      }
    }

    return totalSize;
  }

  /// Cache boyutunu formatla
  String formatCacheSize(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(1)} KB';
    return '${(bytes / (1024 * 1024)).toStringAsFixed(1)} MB';
  }

  /// Son sync zamanını kaydet
  Future<void> setLastSyncTime() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_lastSyncKey, DateTime.now().toIso8601String());
  }

  /// Son sync zamanını oku
  Future<DateTime?> getLastSyncTime() async {
    final prefs = await SharedPreferences.getInstance();
    final timestamp = prefs.getString(_lastSyncKey);
    if (timestamp == null) return null;
    return DateTime.tryParse(timestamp);
  }

  /// Offline mod ayarı
  Future<void> setOfflineMode(bool enabled) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_offlineModeKey, enabled);
  }

  Future<bool> isOfflineModeEnabled() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool(_offlineModeKey) ?? false;
  }

  /// CityModel'i JSON'a çevir (manuel - fromJson'ın tersi)
  Map<String, dynamic> _cityModelToJson(CityModel city) {
    return {
      'city': city.city,
      'country': city.country,
      'currency': city.currency,
      'language': city.language,
      'timezone': city.timezone,
      'emergency': city.emergency,
      'description': city.description,
      'coordinates': {'lat': city.centerLat, 'lng': city.centerLng},
      'highlights': city.highlights
          .map(
            (h) => <String, dynamic>{
              'name': h.name,
              'area': h.area,
              'category': h.category,
              'tags': h.tags,
              'distanceFromCenter': h.distanceFromCenter,
              'lat': h.lat,
              'lng': h.lng,
              'price': h.price,
              'description': h.description,
              'imageUrl': h.imageUrl,
              'tips': h.tips,
              'bestTime': h.bestTime,
              'duration': h.duration,
              'rating': h.rating,
              'reviewCount': h.reviewCount,
              'metro': h.metro,
              'priceRange': h.priceRange,
            },
          )
          .toList(),
      'regions': city.regions
          .map(
            (r) => <String, dynamic>{
              'name': r.name,
              'localName': r.localName,
              'description': r.description,
              'vibe': r.vibe,
              'bestFor': r.bestFor,
              'walkability': r.walkability,
              'safetyRating': r.safetyRating,
              'priceLevel': r.priceLevel,
            },
          )
          .toList(),
      'localTips': city.localTips,
    };
  }
}

/// Akıllı veri yükleyici - Cache + Network
class SmartDataLoader {
  static final CacheService _cache = CacheService();

  /// Şehir verisini akıllıca yükle
  /// 1. Önce cache'e bak
  /// 2. Online ise ve cache eski ise güncelle
  /// 3. Offline ise cache'den göster
  static Future<CityModel> loadCity(
    String cityName, {
    required Future<CityModel> Function(String) networkLoader,
  }) async {
    final normalizedName = cityName.toLowerCase().trim();

    // 1. Cache'e bak
    final cachedCity = await _cache.getCachedCity(normalizedName);

    // 2. Online mı kontrol et
    if (_cache.isOnline) {
      try {
        // Network'ten yükle
        final city = await networkLoader(normalizedName);

        // Cache'e kaydet
        await _cache.cacheCity(normalizedName, city);
        await _cache.setLastSyncTime();

        debugPrint('🌐 Network\'ten yüklendi: $normalizedName');
        return city;
      } catch (e) {
        debugPrint('⚠️ Network hatası, cache kullanılıyor: $e');

        // Network hatası, cache varsa onu kullan
        if (cachedCity != null) {
          return cachedCity;
        }
        rethrow;
      }
    } else {
      // Offline mod
      if (cachedCity != null) {
        debugPrint('📴 Offline mod, cache kullanılıyor: $normalizedName');
        return cachedCity;
      }

      throw Exception('Offline ve cache yok: $normalizedName');
    }
  }

  /// Tüm şehirleri ön yükle (background'da)
  static Future<void> preloadCities(List<String> cities) async {
    if (!_cache.isOnline) {
      debugPrint('📴 Offline, preload atlandı');
      return;
    }

    for (final city in cities) {
      final isCached = await _cache.isCityCached(city);
      if (!isCached) {
        debugPrint('📥 Preloading: $city');
        // Burada network loader çağrılabilir
      }
    }
  }
}
