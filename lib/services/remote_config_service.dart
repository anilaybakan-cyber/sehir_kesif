import 'package:firebase_remote_config/firebase_remote_config.dart';
import 'package:flutter/foundation.dart';

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
}
