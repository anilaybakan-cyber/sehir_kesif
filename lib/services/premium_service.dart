import 'dart:io';
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:purchases_flutter/purchases_flutter.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Premium subscription service - Subscription management via RevenueCat
class PremiumService extends ChangeNotifier {
  static const String _entitlementId = 'My Way Pro'; // RevenueCat entitlement ID

  // RevenueCat API Keys
  static const _apiKeyIOS = 'appl_ZferbHQlSkQXzoGYBmiDwTlJDCP'; // Replace with actual key if different
  static const _apiKeyAndroid = 'goog_imkNKhMhKOeejVclGkaVSkAfCte'; // Added Android support

  // Usage tracking keys (kept locally for free tier limits)
  static const String _keyUsageAISuggestion = 'usage_ai_suggestion';
  /// Tüm “rotaya ekle” girişleri (keşfet, mekan detayı, yakınımda) bu sayacı paylaşır.
  static const String _keyUsageRouteAdd = 'usage_route_add';
  static const String _keyUsageMyWay = 'usage_myway';
  static const String _keyUsageMemories = 'usage_memories';
  static const String _keyUsageDirections = 'usage_directions';
  static const String _keyUsageCuratedRoute = 'usage_curated_route';
  static const String _keyUsageItinerary = 'usage_itinerary_generation';
  static const String _keyViewedRoutes = 'viewed_curated_routes'; // Track unique route IDs
  
  // Free user limits (TOTAL, not daily)
  static const int limitAISuggestion = 1;
  static const int limitRouteAdd = 5; // Daha önce 999'a çıkarılmıştı, Sunk Cost revizesiyle 5 yapıldı.
  static const int limitMyWay = 1;
  static const int limitMemories = 1; // Daha önce 4'tü, 1'e düşürüldü
  static const int limitDirections = 1; // Daha önce 3'tü, 1'e düşürüldü
  static const int limitCuratedRoute = 0; // Bedava hazır rota detay görünümü sıfırlandı
  static const int limitItinerary = 1; // Ücretsiz günlük plan oluşturma hakkı
  
  static PremiumService? _instance;
  static PremiumService get instance => _instance ??= PremiumService._();
  
  PremiumService._();
  
  SharedPreferences? _prefs;
  CustomerInfo? _customerInfo;

  /// Yerelde geçici Pro testi için `true` yapılabilir; **yayına false ile çıkın.**
  /// Pro olmayan kullanıcılar için `isPremium` her zaman RevenueCat sonucuna bağlı kalır.
  static const bool _debugPremiumOverride = true;
  
  bool? _lastSyncedPremium;

  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    
    await _initRevenueCat();
    await _syncPremiumTargeting();
    debugPrint('✅ PremiumService initialized');
  }

  /// Firebase Messaging topic ve Analytics user property'sini premium
  /// durumuna göre senkronize eder. Böylece Firebase Console'dan Pro/Free
  /// hedefli push gönderebiliriz.
  Future<void> _syncPremiumTargeting() async {
    final premium = isPremium;
    if (_lastSyncedPremium == premium) return;
    _lastSyncedPremium = premium;

    try {
      final messaging = FirebaseMessaging.instance;
      if (premium) {
        await messaging.subscribeToTopic('premium_users');
        await messaging.unsubscribeFromTopic('free_users');
      } else {
        await messaging.subscribeToTopic('free_users');
        await messaging.unsubscribeFromTopic('premium_users');
      }
      debugPrint('🔔 Premium targeting topics synced (premium=$premium)');
    } catch (e) {
      debugPrint('❌ Premium topic sync error: $e');
    }

    try {
      await FirebaseAnalytics.instance.setUserProperty(
        name: 'is_premium',
        value: premium ? 'true' : 'false',
      );
    } catch (e) {
      debugPrint('❌ Premium user property error: $e');
    }
  }

  Future<void> _initRevenueCat() async {
    try {
      if (Platform.isIOS) {
        await Purchases.setLogLevel(kReleaseMode ? LogLevel.warn : LogLevel.debug);
        await Purchases.configure(PurchasesConfiguration(_apiKeyIOS));
      } else if (Platform.isAndroid) {
        await Purchases.configure(PurchasesConfiguration(_apiKeyAndroid));
      }

      // Check current subscription status
      _customerInfo = await Purchases.getCustomerInfo();
      debugPrint("🔍 RC Init Info: Entitlements: ${_customerInfo?.entitlements.all}");
      
      // Update listener on changes
      Purchases.addCustomerInfoUpdateListener((info) {
        _customerInfo = info;
        debugPrint("🔄 RC Update: Entitlements: ${info.entitlements.all}");
        notifyListeners();
        _syncPremiumTargeting();
      });
    } catch (e) {
      debugPrint('❌ RevenueCat init error: $e');
    }
  }
  
  /// Premium kullanıcı mı? (Checked via RevenueCat)
  bool get isPremium {
    if (_debugPremiumOverride) return true;
    return _customerInfo?.entitlements.active.containsKey(_entitlementId) ?? false;
  }
  
  /// Full erişim var mı?
  bool get hasFullAccess => isPremium;

  /// Get available offerings (products)
  Future<Offerings?> getOfferings() async {
    try {
      return await Purchases.getOfferings();
    } on PlatformException catch (e) {
      debugPrint('❌ RevenueCat getOfferings error: $e');
      return null;
    }
  }

  /// Check if user is eligible for trial/introductory price
  Future<bool> isTrialEligible() async {
    try {
      final offerings = await getOfferings();
      if (offerings == null || offerings.current == null) return true;
      
      final productIds = offerings.current!.availablePackages
          .map((package) => package.storeProduct.identifier)
          .toList();
      
      if (productIds.isEmpty) return true;

      final eligibilityMap = await Purchases.checkTrialOrIntroductoryPriceEligibility(productIds);
      
      // If any of the current offerings allow trial for this user, return true
      for (var productId in productIds) {
        if (eligibilityMap[productId]?.status == IntroEligibilityStatus.introEligibilityStatusEligible) {
          return true;
        }
      }
      return false;
    } catch (e) {
      debugPrint('❌ RevenueCat isTrialEligible error: $e');
      return true; // Default to true on error to not block potential trials
    }
  }
  
  // ══════════════════════════════════════════════════════════════════════════
  // FREE USER USAGE LIMITS (Local tracking)
  // ══════════════════════════════════════════════════════════════════════════
  
  /// Kullanım sayısını getir
  int _getUsage(String key) => _prefs?.getInt(key) ?? 0;
  
  /// Kullanım sayısını artır
  Future<void> _incrementUsage(String key) async {
    final current = _getUsage(key);
    await _prefs?.setInt(key, current + 1);
  }
  
  /// AI Önerisi kullanabilir mi?
  bool canUseAISuggestion() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageAISuggestion) < limitAISuggestion;
  }
  
  /// AI Önerisi kullanımını artır
  Future<void> useAISuggestion() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageAISuggestion);
  }
  
  /// Ücretsiz planda rotaya manuel ekleme hakkı var mı? (Tüm kaynakların toplamı.)
  bool canAddToRoute() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageRouteAdd) < limitRouteAdd;
  }
  
  /// Her başarılı manuel rotaya eklemede çağrılır; kaynak fark etmez.
  Future<void> useRouteAdd() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageRouteAdd);
  }
  
  /// Mevcut rota ekleme sayısı
  int get routeAddCount => _getUsage(_keyUsageRouteAdd);
  
  /// My Way Asistan kullanabilir mi?
  bool canUseMyWay() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageMyWay) < limitMyWay;
  }
  
  /// My Way kullanımını artır
  Future<void> useMyWay() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageMyWay);
  }
  
  /// Anı kaydedebilir mi?
  bool canSaveMemory() {
    return hasFullAccess;
  }
  
  /// Anı kaydetme kullanımını artır
  Future<void> useSaveMemory() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageMemories);
  }
  
  /// Mevcut anı sayısı
  int get memoriesCount => _getUsage(_keyUsageMemories);
  
  /// Yol tarifi alabilir mi?
  bool canGetDirections() {
    return hasFullAccess;
  }
  
  /// Yol tarifi kullanımını artır
  Future<void> useDirections() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageDirections);
  }

  /// Günlük plan oluşturabilir mi? (Magic Plan)
  bool canGenerateItinerary() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageItinerary) < limitItinerary;
  }

  /// Günlük plan oluşturma kullanımını artır
  Future<void> useItinerary() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageItinerary);
  }
  
  /// Hazır rotaları uygulayabilir mi?
  bool canApplyCuratedRoute() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageCuratedRoute) < limitCuratedRoute;
  }

  /// Spesifik bir rotaya bakabilir mi? (Zaten baktıysa bakabilir, bakmadıysa hakkı varsa bakabilir)
  bool canViewCuratedRoute(String routeId) {
    if (hasFullAccess) return true;
    
    final viewedRoutes = _prefs?.getStringList(_keyViewedRoutes) ?? [];
    if (viewedRoutes.contains(routeId)) return true;
    
    return _getUsage(_keyUsageCuratedRoute) < limitCuratedRoute;
  }

  /// Hazır rota izlendiğinde kaydet
  Future<void> trackRouteView(String routeId) async {
    if (hasFullAccess) return;
    
    final viewedRoutes = _prefs?.getStringList(_keyViewedRoutes) ?? [];
    if (!viewedRoutes.contains(routeId)) {
      viewedRoutes.add(routeId);
      await _prefs?.setStringList(_keyViewedRoutes, viewedRoutes);
      await _incrementUsage(_keyUsageCuratedRoute);
    }
  }

  /// Hazır rota kullanımını artır (Manual use if needed)
  Future<void> useCuratedRoute() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageCuratedRoute);
  }
  
  /// Kalan kullanım hakkı
  Map<String, int> get remainingUsage => {
    'aiSuggestion': limitAISuggestion - _getUsage(_keyUsageAISuggestion),
    'routeAdd': limitRouteAdd - _getUsage(_keyUsageRouteAdd),
    'myWay': limitMyWay - _getUsage(_keyUsageMyWay),
    'memories': limitMemories - _getUsage(_keyUsageMemories),
    'directions': limitDirections - _getUsage(_keyUsageDirections),
    'curatedRoute': limitCuratedRoute - _getUsage(_keyUsageCuratedRoute),
    'itinerary': limitItinerary - _getUsage(_keyUsageItinerary),
  };
  
  // ══════════════════════════════════════════════════════════════════════════
  // SUBSCRIPTION ACTIONS
  // ══════════════════════════════════════════════════════════════════════════
  
  /// Abonelik satın al
  Future<bool> purchasePackage(Package package) async {
    try {
      _customerInfo = await Purchases.purchasePackage(package);
      notifyListeners();
      return isPremium;
    } on PlatformException catch (e) {
      var errorCode = PurchasesErrorHelper.getErrorCode(e);
      if (errorCode != PurchasesErrorCode.purchaseCancelledError) {
        debugPrint('❌ Purchase Error: $e');
      }
      return false;
    }
  }
  
  /// Abonelik satın al (StoreProduct ile)
  Future<bool> purchaseStoreProduct(StoreProduct product) async {
    try {
      _customerInfo = await Purchases.purchaseStoreProduct(product);
      notifyListeners();
      return isPremium;
    } on PlatformException catch (e) {
      var errorCode = PurchasesErrorHelper.getErrorCode(e);
      if (errorCode != PurchasesErrorCode.purchaseCancelledError) {
        debugPrint('❌ Purchase Error: $e');
      }
      return false;
    }
  }

  /// Önceki satın almaları geri yükle
  Future<bool> restorePurchases() async {
    try {
      _customerInfo = await Purchases.restorePurchases();
      notifyListeners();
      return isPremium;
    } on PlatformException catch (e) {
      debugPrint('❌ Restore Error: $e');
      return false;
    }
  }
  
  /// Test için: Tüm kullanımları sıfırla
  Future<void> resetUsage() async {
    await _prefs?.setInt(_keyUsageAISuggestion, 0);
    await _prefs?.setInt(_keyUsageRouteAdd, 0);
    await _prefs?.setInt(_keyUsageMyWay, 0);
    await _prefs?.setInt(_keyUsageMemories, 0);
    await _prefs?.setInt(_keyUsageDirections, 0);
    await _prefs?.setInt(_keyUsageCuratedRoute, 0);
    await _prefs?.setStringList(_keyViewedRoutes, []);
    notifyListeners();
  }
}
