import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:purchases_flutter/purchases_flutter.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Premium subscription service - Subscription management via RevenueCat
class PremiumService extends ChangeNotifier {
  static const String _entitlementId = 'My Way Pro'; // RevenueCat entitlement ID

  // RevenueCat API Keys
  static const _apiKeyIOS = 'appl_ZferbHQlSkQXzoGYBmiDwTlJDCP'; // Replace with actual key if different
  static const _apiKeyAndroid = 'goog_...'; // Add if Android support is needed

  // Usage tracking keys (kept locally for free tier limits)
  static const String _keyUsageAISuggestion = 'usage_ai_suggestion';
  static const String _keyUsageRouteAdd = 'usage_route_add';
  static const String _keyUsageMyWay = 'usage_myway';
  static const String _keyUsageMemories = 'usage_memories';
  static const String _keyUsageDirections = 'usage_directions';
  
  // Free user limits (TOTAL, not daily)
  static const int limitAISuggestion = 1;
  static const int limitRouteAdd = 3;
  static const int limitMyWay = 1;
  static const int limitMemories = 4;
  static const int limitDirections = 3;
  
  static PremiumService? _instance;
  static PremiumService get instance => _instance ??= PremiumService._();
  
  PremiumService._();
  
  SharedPreferences? _prefs;
  CustomerInfo? _customerInfo;
  
  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    
    await _initRevenueCat();
    debugPrint('✅ PremiumService initialized');
  }

  Future<void> _initRevenueCat() async {
    try {
      if (Platform.isIOS) {
        await Purchases.setLogLevel(LogLevel.debug); // Enable debug logs
        await Purchases.configure(PurchasesConfiguration(_apiKeyIOS));
      } else if (Platform.isAndroid) {
        // await Purchases.configure(PurchasesConfiguration(_apiKeyAndroid));
      }

      // Check current subscription status
      _customerInfo = await Purchases.getCustomerInfo();
      debugPrint("🔍 RC Init Info: Entitlements: ${_customerInfo?.entitlements.all}");
      
      // Update listener on changes
      Purchases.addCustomerInfoUpdateListener((info) {
        _customerInfo = info;
        debugPrint("🔄 RC Update: Entitlements: ${info.entitlements.all}");
        notifyListeners();
      });
    } catch (e) {
      debugPrint('❌ RevenueCat init error: $e');
    }
  }
  
  /// Premium kullanıcı mı? (Checked via RevenueCat)
  bool get isPremium {

    if (_customerInfo == null) return false;
    
    // Check if user has active entitlement
    final entitlement = _customerInfo?.entitlements.all[_entitlementId];
    if (entitlement != null && entitlement.isActive) {
      debugPrint("✅ User IS Premium. Active Entitlement: $_entitlementId");
      return true;
    } else {
      debugPrint("🔒 User NOT Premium. Entitlements found: ${_customerInfo?.entitlements.all.keys}");
      return false;
    }
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
    return hasFullAccess;
  }
  
  /// AI Önerisi kullanımını artır
  Future<void> useAISuggestion() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageAISuggestion);
  }
  
  /// Rotaya yer ekleyebilir mi? (Limitli: 3)
  bool canAddToRoute() {
    if (hasFullAccess) return true;
    return _getUsage(_keyUsageRouteAdd) < limitRouteAdd;
  }
  
  /// Rotaya ekleme kullanımını artır
  Future<void> useRouteAdd() async {
    if (!hasFullAccess) await _incrementUsage(_keyUsageRouteAdd);
  }
  
  /// Mevcut rota ekleme sayısı
  int get routeAddCount => _getUsage(_keyUsageRouteAdd);
  
  /// My Way Asistan kullanabilir mi?
  bool canUseMyWay() {
    return hasFullAccess;
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
  
  /// Hazır rotaları uygulayabilir mi?
  bool canApplyCuratedRoute() {
    return hasFullAccess;
  }
  
  /// Kalan kullanım hakkı
  Map<String, int> get remainingUsage => {
    'aiSuggestion': limitAISuggestion - _getUsage(_keyUsageAISuggestion),
    'routeAdd': limitRouteAdd - _getUsage(_keyUsageRouteAdd),
    'myWay': limitMyWay - _getUsage(_keyUsageMyWay),
    'memories': limitMemories - _getUsage(_keyUsageMemories),
    'directions': limitDirections - _getUsage(_keyUsageDirections),
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
    notifyListeners();
  }
}
