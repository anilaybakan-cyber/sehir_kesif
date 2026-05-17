import 'package:firebase_remote_config/firebase_remote_config.dart';
import 'package:flutter/foundation.dart';
import 'dart:convert';

class RemoteConfigService {
  static final RemoteConfigService instance = RemoteConfigService._();
  final FirebaseRemoteConfig _remoteConfig = FirebaseRemoteConfig.instance;

  RemoteConfigService._();

  Future<void> init() async {
    try {
      await _remoteConfig.setConfigSettings(RemoteConfigSettings(
        fetchTimeout: const Duration(minutes: 1),
        minimumFetchInterval: const Duration(hours: 1),
      ));

      await _remoteConfig.setDefaults({
        // Paywall Defaults
        'paywall_title_tr': 'Pro\'ya Yükselt',
        'paywall_title_en': 'Upgrade to Pro',
        'paywall_subtitle_tr': 'Sınırsız özelliklerin kilidini aç',
        'paywall_subtitle_en': 'Unlock unlimited features',
        // Feature Flags
        'enable_new_ui': false,
        'show_promo_banner': true,
        'enable_dynamic_routes': true, // 🔥 EKLENDİ - Dinamik rotaları aç/kapat
        'target_route_count': 12,      // 🔥 EKLENDİ - Hedef rota sayısı (30'dan düşürüldü)
        // Force Update
        'min_app_version': '1.0.3',
        'store_url_ios': 'https://apps.apple.com/app/id6757671492',
        'store_url_android':
            'https://play.google.com/store/apps/details?id=com.anilaybakan.sehirkesif',
        // Featured Articles (JSON)
        'featured_cards': '',  // Boşsa hardcoded fallback kullanılır
      });

      await _remoteConfig.fetchAndActivate();
      debugPrint('✅ RemoteConfigService initialized');
    } catch (e) {
      debugPrint('❌ RemoteConfigService init error: $e');
    }
  }

  // --- Getters ---

  String get paywallTitle => _getString(
        keyTr: 'paywall_title_tr',
        keyEn: 'paywall_title_en',
      );

  String get paywallSubtitle => _getString(
        keyTr: 'paywall_subtitle_tr',
        keyEn: 'paywall_subtitle_en',
      );
  
  bool get showPromoBanner => _remoteConfig.getBool('show_promo_banner');

  String get minAppVersion => _remoteConfig.getString('min_app_version');
  String get storeUrlIOS => _remoteConfig.getString('store_url_ios');
  String get storeUrlAndroid => _remoteConfig.getString('store_url_android');
  
  // Dynamic Route Controls
  bool get enableDynamicRoutes => _remoteConfig.getBool('enable_dynamic_routes');
  int get targetRouteCount => _remoteConfig.getInt('target_route_count');
  // Helper to fetch localized string based on system locale (basic check)
  // In a real app, you might pass the locale to this service or check AppLocalizations
  String _getString({required String keyTr, required String keyEn}) {
    // Basic detection via PlatformDispatcher or just assume EN if not TR
    // For simplicity, we can rely on how the app sets language. 
    // Ideally this service should be aware of the current app language.
    // For now, let's return the key directly from remote config, 
    // and let the UI decide which key to ask for? 
    // Or better: UI asks for specific key dependent on its state.
    
    // Let's allow direct key access
    return _remoteConfig.getString(keyEn); // Default fallback
  }

  String getString(String key) => _remoteConfig.getString(key);
  bool getBool(String key) => _remoteConfig.getBool(key);
  int getInt(String key) => _remoteConfig.getInt(key);
  double getDouble(String key) => _remoteConfig.getDouble(key);

  // ===== FEATURED ARTICLES =====

  /// Featured kartları Remote Config'den oku
  /// Boşsa boş liste döner (hardcoded fallback kullanılır)
  List<Map<String, dynamic>> get featuredCards {
    final json = _remoteConfig.getString('featured_cards');
    if (json.isEmpty) return [];
    try {
      final list = jsonDecode(json);
      if (list is List) {
        return list.cast<Map<String, dynamic>>();
      }
      return [];
    } catch (e) {
      debugPrint('❌ Error parsing featured_cards: $e');
      return [];
    }
  }

  /// Makale içeriğini Remote Config'den oku
  /// Key formatı: article_[id]_[tr/en]
  /// Boşsa boş string döner (hardcoded fallback kullanılır)
  String getArticleContent(String articleId, String lang) {
    final key = 'article_${articleId}_$lang';
    try {
      return _remoteConfig.getString(key);
    } catch (e) {
      return '';
    }
  }
}
