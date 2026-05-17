import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/foundation.dart';

class AnalyticsService {
  static final AnalyticsService instance = AnalyticsService._internal();
  AnalyticsService._internal();

  final FirebaseAnalytics _analytics = FirebaseAnalytics.instance;

  Future<void> logEvent(String name, {Map<String, Object>? parameters}) async {
    try {
      await _analytics.logEvent(name: name, parameters: parameters);
      debugPrint('📊 [Analytics] Event: $name, Params: $parameters');
    } catch (e) {
      debugPrint('❌ [Analytics] Error logging event $name: $e');
    }
  }

  Future<void> setUserProperty(String name, String value) async {
    try {
      await _analytics.setUserProperty(name: name, value: value);
      debugPrint('📊 [Analytics] UserProperty: $name = $value');
    } catch (e) {
      debugPrint('❌ [Analytics] Error setting user property $name: $e');
    }
  }

  // Helper methods for specific events
  Future<void> logOnboardingCompleted() async {
    await logEvent('onboarding_completed');
  }

  Future<void> logPreferencesSaved(String cityId) async {
    await logEvent('preferences_saved', parameters: {'city_id': cityId});
  }

  Future<void> logPlanGenerated(String cityId) async {
    await logEvent('plan_generated', parameters: {'city_id': cityId});
  }
  
  Future<void> logPlanApplied(String cityId) async {
    await logEvent('plan_applied', parameters: {'city_id': cityId});
  }

  // --- NEW TRACKING METHODS ---

  /// Takip: Kullanıcı arama çubuğuna ne yazdı?
  Future<void> logSearch(String query) async {
    await logEvent('search', parameters: {'search_term': query});
  }

  /// Takip: Kullanıcı hangi mekan/rehber kartına tıkladı?
  Future<void> logSelectContent({
    required String contentType, // 'landmark', 'guide', 'city'
    required String itemId,
  }) async {
    await logEvent('select_content', parameters: {
      'content_type': contentType,
      'item_id': itemId,
    });
  }

  /// Takip: Kritik butonlara basılma durumları
  Future<void> logButtonClick(String buttonId, {String? buttonName}) async {
    await logEvent('button_click', parameters: {
      'button_id': buttonId,
      if (buttonName != null) 'button_name': buttonName,
    });
  }

  /// Takip: Tab geçişleri
  Future<void> logTabChange({required String tabName}) async {
    await logEvent('tab_change', parameters: {'tab_name': tabName});
  }


  /// Takip: Uygulama içi hata durumları
  Future<void> logAppError(String errorMsg) async {
    await logEvent('app_error', parameters: {'message': errorMsg});
  }
}
