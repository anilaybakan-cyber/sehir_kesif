// =============================================================================
// MAIN.DART - WANDERLUST APP
// Onboarding kontrolü ile başlangıç akışı
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:ui'; // For PathMetric, MaskFilter
import 'package:shared_preferences/shared_preferences.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_analytics/firebase_analytics.dart';

// Screens
import 'screens/onboarding_screen.dart' show OnboardingScreen;
import 'screens/explore_screen.dart' show ExploreScreen;
import 'services/tutorial_service.dart';
import 'dart:async';
import 'screens/detail_screen.dart' show DetailScreen;
import 'screens/routes_screen.dart' show RoutesScreen;
import 'screens/nearby_screen.dart' show NearbyScreen;
import 'screens/profile_screen.dart' show ProfileScreen;
import 'screens/city_switcher_screen.dart' show CitySwitcherScreen;
import 'screens/city_guide_screen.dart' show CityGuideScreen;
import 'screens/city_guide_detail_screen.dart' show CityGuideDetailScreen;
import 'models/city_model.dart';
import 'services/city_data_loader.dart';
import 'l10n/app_localizations.dart';
import 'theme/wanderlust_colors.dart';
import 'widgets/resilient_network_image.dart';
import 'services/notification_service.dart';
import 'services/premium_service.dart';
import 'screens/paywall_screen.dart';
import 'services/content_update_service.dart';
import 'services/remote_config_service.dart';
import 'services/city_blog_content.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'screens/force_update_screen.dart';
import 'services/version_service.dart';
import 'app_navigator.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'utils/image_utils.dart';
import 'services/curated_routes_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  debugPrint('🚀 main() started');

  // 🖼️ Performans: Görsel belleğini 100MB -> 250MB'a çıkar.
  // Fotoğraf yoğunluklu bir uygulama için akıcılığı sağlar.
  PaintingBinding.instance.imageCache.maximumSizeBytes = 250 * 1024 * 1024;
  PaintingBinding.instance.imageCache.maximumSize = 300; // Maksimum 300 görsel bellekte kalsın

  // 🔥 Initialize Firebase
  debugPrint('🔥 Firebase.initializeApp() starting...');
  await Firebase.initializeApp();
  debugPrint('🔥 Firebase.initializeApp() DONE');
  
  // 🔑 Load Environment Variables
  debugPrint('🔑 Loading .env...');
  try {
    await dotenv.load(fileName: ".env");
    debugPrint('🔑 .env loaded successfully');
  } catch (e) {
    debugPrint('❌ Failed to load .env: $e');
  }
  
  // 🔔 Initialize Push Notifications
  debugPrint('🔔 NotificationService initialization starting...');
  try {
    await NotificationService().initialize();
    debugPrint('🔔 NotificationService initialization DONE');
  } catch (e, stackTrace) {
    debugPrint('🔔 Notification initialization FAILED: $e');
    debugPrint('🔔 Stack trace: $stackTrace');
  }

  // Kaydedilmiş dil tercihini yükle
  await AppLocalizations.loadSavedLanguage();
  
  // 💎 Premium Service başlat
  debugPrint('💎 PremiumService initialization starting...');
  await PremiumService.instance.init();
  debugPrint('💎 PremiumService initialized. Premium: ${PremiumService.instance.isPremium}');

  // 🌍 Remote Config initialization
  debugPrint('🌍 RemoteConfigService initialization starting...');
  await RemoteConfigService.instance.init();
  debugPrint('🌍 RemoteConfigService initialized');

  // 🏙️ OTA şehir listesini yükle (varsa)
  await CitySwitcherScreen.loadRemoteCities();

  // Sardinya geçici olarak listeden kaldırıldı; kayıtlı seçim varsa Catania’ya taşı.
  try {
    final prefs = await SharedPreferences.getInstance();
    final sel = (prefs.getString('selectedCity') ?? '').toLowerCase();
    if (sel == 'sardinya' || sel == 'sardinia') {
      await prefs.setString('selectedCity', 'catania');
    }
  } catch (_) {}

  // Status bar stilini ayarla
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.light,
    ),
  );

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  static final FirebaseAnalytics analytics = FirebaseAnalytics.instance;

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MyWay',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        fontFamily: 'Poppins',
        scaffoldBackgroundColor: WanderlustColors.bgDark,
        colorScheme: const ColorScheme.light(
          primary: WanderlustColors.accent,
          secondary: WanderlustColors.accentLight,
          surface: WanderlustColors.bgCard,
          onSurface: WanderlustColors.textWhite,
          onPrimary: Colors.white,
        ),
        textTheme: GoogleFonts.poppinsTextTheme(
          ThemeData.light().textTheme,
        ).apply(
          bodyColor: WanderlustColors.textWhite,
          displayColor: WanderlustColors.textWhite,
        ),
      ),
      navigatorKey: navigatorKey,
      navigatorObservers: [
        FirebaseAnalyticsObserver(analytics: MyApp.analytics),
      ],
      home: const SplashScreen(),
      routes: {
        "/onboarding": (_) => const OnboardingScreen(),
        "/city-switch": (_) => const CitySwitcherScreen(),
      },
      onGenerateRoute: (settings) {
        if (settings.name == "/detail") {
          final place = settings.arguments as Highlight;
          return MaterialPageRoute(builder: (_) => DetailScreen(place: place));
        }
        if (settings.name == "/main") {
          final args = settings.arguments as Map<String, dynamic>?;
          final initialIndex = args?['initialIndex'] as int? ?? 0;
          final initialRoutesTabIndex = args?['initialRoutesTabIndex'] as int? ?? 0;
          final initialProfileTabIndex = args?['initialProfileTabIndex'] as int? ?? 0;
          final initialProfileAction = args?['initialProfileAction']?.toString();
          final checkPaywall = args?['checkPaywall'] as bool? ?? true;
          return MaterialPageRoute(
            builder: (_) => MainScreen(
              initialIndex: initialIndex,
              initialRoutesTabIndex: initialRoutesTabIndex,
              initialProfileTabIndex: initialProfileTabIndex,
              initialProfileAction: initialProfileAction,
              checkPaywall: checkPaywall,
            ),
          );
        }
        // Deep link: Paywall
        if (settings.name == "/paywall") {
          // PRO kullanıcı için sessizce ana ekrana yönlendir.
          if (PremiumService.instance.isPremium) {
            return MaterialPageRoute(
              builder: (_) => const MainScreen(initialIndex: 0),
            );
          }
          return MaterialPageRoute(
            builder: (ctx) {
              WidgetsBinding.instance.addPostFrameCallback((_) {
                showPaywall(ctx, onSubscribe: (_) {});
              });
              return const SizedBox.shrink();
            },
          );
        }
        // Deep link: Şehir Rehberi Detay
        if (settings.name == "/guide") {
          final args = settings.arguments as Map<String, dynamic>?;
          final cityId = args?['cityId']?.toString().toLowerCase() ?? '';
          if (cityId.isNotEmpty) {
            // Find city data safely
            Map<String, dynamic>? cityData;
            try {
              cityData = CitySwitcherScreen.allCities.firstWhere(
                (c) => c['id'].toString().toLowerCase() == cityId,
              );
            } catch (_) {
              // Fallback: If list is not loaded yet or city not found
              cityData = null;
            }

            return MaterialPageRoute(
              builder: (_) => CityGuideDetailScreen(
                city: cityId,
                imageUrl: cityData?['networkImage'] ?? '',
              ),
            );
          }
        }
        // Deep link: Mekan Detay (cityId + placeName ile)
        if (settings.name == "/detail-by-id") {
          final args = settings.arguments as Map<String, dynamic>?;
          final cityId = args?['cityId'] as String? ?? '';
          final placeName = args?['placeName'] as String? ?? '';
          if (cityId.isNotEmpty && placeName.isNotEmpty) {
            return MaterialPageRoute(
              builder: (_) => FutureBuilder<CityModel>(
                future: CityDataLoader.loadCity(cityId),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const Scaffold(
                      backgroundColor: WanderlustColors.bgDark,
                      body: Center(child: CircularProgressIndicator(color: WanderlustColors.accent)),
                    );
                  }
                  if (snapshot.hasData) {
                    final city = snapshot.data!;
                    final place = city.highlights.cast<Highlight?>().firstWhere(
                      (h) => h!.name.toLowerCase() == placeName.toLowerCase() ||
                             (h.nameEn?.toLowerCase() ?? '') == placeName.toLowerCase(),
                      orElse: () => null,
                    );
                    if (place != null) {
                      return DetailScreen(place: place);
                    }
                  }
                  return Scaffold(
                    backgroundColor: WanderlustColors.bgDark,
                    body: Center(
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.place_outlined, color: WanderlustColors.textGrey, size: 48),
                          const SizedBox(height: 12),
                          Text('Mekan bulunamadı', style: TextStyle(color: WanderlustColors.textGrey)),
                          const SizedBox(height: 16),
                          TextButton(
                            onPressed: () => Navigator.pop(context),
                            child: const Text('Geri Dön'),
                          ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            );
          }
        }
        return null;
      },
    );
  }
}

// =============================================================================
// SPLASH SCREEN - Onboarding kontrolü
// =============================================================================

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen> {
  @override
  void initState() {
    super.initState();
    _checkOnboarding();
  }

  Future<void> _checkOnboarding() async {
    // 🌍 İçerik güncellemelerini ve blog preload'u GERÇEKTEN arka planda yap.
    // (Eskiden 'await' edildiği için splash görseli ağ koşullarına göre uzayabiliyordu.)
    unawaited(() async {
      try {
        await ContentUpdateService.checkForUpdates();
      } catch (e) {
        debugPrint("⚠️ Background update error: $e");
      }

      try {
        await CityBlogContent.preloadOtaBlogs('saint_tropez');
        await CityBlogContent.preloadOtaBlogs('midilli');
        await CityBlogContent.preloadOtaBlogs('saraybosna');
        await CityBlogContent.preloadOtaBlogs('san_sebastian');
        debugPrint("✅ New city blogs preloaded");
      } catch (e) {
        debugPrint("⚠️ Blog preload error: $e");
      }
    }());

    await Future.delayed(const Duration(milliseconds: 500)); // Kısa splash

    final prefs = await SharedPreferences.getInstance();
    
    final onboardingCompleted = prefs.getBool("onboardingCompleted") ?? false;
    
    // ⚠️ DEV_MODE: Her açılışta onboarding göster (KAPALI)
    final bool forceOnboarding = false;

    if (!mounted) return;

    // Force Update — hard block on SplashScreen
    try {
      final bool updateRequired = await VersionService.instance.isUpdateRequired();
      if (updateRequired) {
        debugPrint("🚀 [SplashScreen] Force update required. Navigating to ForceUpdateScreen.");
        if (!mounted) return;
        Navigator.pushReplacement(context, MaterialPageRoute(builder: (_) => const ForceUpdateScreen()));
        return; // Halt further routing
      }
    } catch (e) {
      debugPrint("⚠️ Failed to check version update: $e");
    }

    if (onboardingCompleted && !forceOnboarding) {
      debugPrint("🚀 [SplashScreen] Navigating to /main");
      Navigator.pushReplacementNamed(context, "/main");
    } else {
      debugPrint("🚀 [SplashScreen] Navigating to /onboarding");
      Navigator.pushReplacementNamed(context, "/onboarding");
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: WanderlustColors.accent,
      body: Center(
        child: Image.asset(
          'assets/images/splash_logo.png',
          width: 150,
          height: 150,
        ),
      ),
    );
  }
}

// =============================================================================
// MAIN SCREEN - Bottom Navigation ile ana ekran
// =============================================================================

// =============================================================================
// MAIN SCREEN - Bottom Navigation ile ana ekran
// =============================================================================

class MainScreen extends StatefulWidget {
  final int initialIndex;
  final int initialRoutesTabIndex;
  final int initialProfileTabIndex;
  final String? initialProfileAction;
  final bool checkPaywall;

  const MainScreen({
    super.key,
    this.initialIndex = 0,
    this.initialRoutesTabIndex = 0,
    this.initialProfileTabIndex = 0,
    this.initialProfileAction,
    this.checkPaywall = true,
  });

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  late int _currentIndex;
  bool _paywallShown = false;


  @override
  void initState() {
    super.initState();
    _currentIndex = widget.initialIndex;
    
    WidgetsBinding.instance.addPostFrameCallback((_) {
      // If user tapped a push notification while the app was terminated,
      // the NotificationService queued the deep link. Deliver it now that
      // MainScreen is mounted so the navigator stack is stable.
      NotificationService().consumePendingDeepLink();

      _checkAndShowCitySuggestion(onDone: () {
        _checkPeriodicPaywall(onDone: _scheduleTutorial);
      });
    });
  }

  void _scheduleTutorial() {
      // 1.5s delay to ensure Paywall close animation finishes and UI is ready
      Future.delayed(const Duration(milliseconds: 1500), () {
          if (!mounted) return;
          
          if (_currentIndex == 0) {
             TutorialService.instance.triggerTutorial(TutorialService.KEY_TUTORIAL_CITY_SELECTION);
          } else if (_currentIndex == 1) {
             TutorialService.instance.triggerTutorial(TutorialService.KEY_TUTORIAL_NEARBY);
          }
      });
  }

  Future<void> _checkAndShowCitySuggestion({VoidCallback? onDone}) async {
    final prefs = await SharedPreferences.getInstance();
    if (prefs.getBool("suggest_city_popup") == true) {
      await prefs.setBool("suggest_city_popup", false);
      
      final cityId = prefs.getString("selectedCity") ?? "barcelona";
      final cityData = CitySwitcherScreen.allCities.firstWhere(
        (c) => c['id'] == cityId,
        orElse: () => CitySwitcherScreen.allCities.first,
      );

      if (!mounted) return;

      showDialog(
        context: context,
        barrierDismissible: false,
        builder: (context) => Dialog(
          backgroundColor: WanderlustColors.bgCard,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Image Header with Overlay
              Stack(
                children: [
                  ClipRRect(
                    borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
                    child: ResilientNetworkImage(
                      imageUrl: cityData['networkImage'] as String?,
                      placeName: (cityData['name'] ?? cityData['id']).toString(),
                      city: cityData['id'].toString(),
                      category: 'city',
                      height: 200,
                      fit: BoxFit.cover,
                    ),
                  ),
                  Positioned.fill(
                    child: Container(
                      decoration: BoxDecoration(
                        borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
                        gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.transparent,
                            WanderlustColors.bgCard,
                          ],
                        ),
                      ),
                    ),
                  ),
                  Positioned(
                    bottom: 16,
                    left: 20,
                    right: 20,
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: WanderlustColors.accent,
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Text(
                            AppLocalizations.instance.ourSuggestion,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 12,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                        const SizedBox(height: 8),
                        Text(
                          cityData['name'],
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 28,
                            fontWeight: FontWeight.bold,
                            letterSpacing: -0.5,
                          ),
                        ),
                        Row(
                          children: [
                            Text(
                              cityData['flag'],
                              style: const TextStyle(fontSize: 16),
                            ),
                            const SizedBox(width: 6),
                            Text(
                              AppLocalizations.instance.translateCountry(cityData['country']),
                              style: const TextStyle(
                                color: Colors.white70,
                                fontSize: 14,
                                fontWeight: FontWeight.w500,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ],
              ),
              
              // Content Body
              Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  children: [
                    Text(
                      AppLocalizations.instance.undecidedSuggestionDesc,
                      textAlign: TextAlign.center,
                      style: const TextStyle(
                        color: WanderlustColors.textGrey,
                        fontSize: 15,
                        height: 1.5,
                      ),
                    ),
                    const SizedBox(height: 24),
                    SizedBox(
                      width: double.infinity,
                      child: ElevatedButton(
                        onPressed: () {
                          Navigator.pop(context);
                          onDone?.call();
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: WanderlustColors.accent,
                          foregroundColor: Colors.white,
                          elevation: 0,
                          padding: const EdgeInsets.symmetric(vertical: 16),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(16),
                          ),
                        ),
                        child: Text(
                          AppLocalizations.instance.discoverNow,
                          style: const TextStyle(
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      );
    } else {
      onDone?.call();
    }
  }

  Future<void> _checkPeriodicPaywall({VoidCallback? onDone}) async {
    final premium = PremiumService.instance;
    if (premium.isPremium) {
      onDone?.call();
      return;
    }

    final prefs = await SharedPreferences.getInstance();
    final openCount = (prefs.getInt('app_open_count') ?? 0) + 1;
    await prefs.setInt('app_open_count', openCount);

    if (openCount % 3 == 0 && !_paywallShown) {
      _paywallShown = true;
      await showPaywall(
        context,
        onSubscribe: (planId) async {},
      );
      onDone?.call();
    } else {
      onDone?.call();
    }
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, result) {
        if (_currentIndex != 0) {
          // If not on home tab, go to home tab
          setState(() => _currentIndex = 0);
        } else {
          // If on home tab, minimize app (go to home screen)
          SystemNavigator.pop();
        }
      },
      child: Scaffold(
        body: IndexedStack(index: _currentIndex, children: [
          ExploreScreen(isVisible: _currentIndex == 0),
          RoutesScreen(
            isVisible: _currentIndex == 1,
            initialTabIndex: widget.initialRoutesTabIndex,
          ),
          NearbyScreen(isVisible: _currentIndex == 2),
          const CityGuideScreen(),
          ProfileScreen(
            isVisible: _currentIndex == 4,
            initialTabIndex: widget.initialProfileTabIndex,
            initialAction: widget.initialProfileAction,
          ),
        ]),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          HapticFeedback.selectionClick();
          setState(() => _currentIndex = index);
          
          // Trigger tutorial if switching to Nearby tab
          if (index == 2) {
             // Small delay to ensure UI settles if needed
             Future.delayed(const Duration(milliseconds: 300), () {
                TutorialService.instance.triggerTutorial(TutorialService.KEY_TUTORIAL_NEARBY);
             });
          }
        },
        backgroundColor: WanderlustColors.bgCard,
        selectedItemColor: WanderlustColors.accent,
        unselectedItemColor: WanderlustColors.textGrey,
        type: BottomNavigationBarType.fixed,
        elevation: 0,
        items: [
          BottomNavigationBarItem(
            icon: Image.asset('assets/icons/icon_explore.png', width: 24, height: 24),
            activeIcon: Image.asset('assets/icons/icon_explore.png', width: 26, height: 26),
            label: AppLocalizations.instance.navExplore,
          ),
          BottomNavigationBarItem(
            icon: Image.asset('assets/icons/icon_renkli_routes.png', width: 24, height: 24),
            activeIcon: Image.asset('assets/icons/icon_renkli_routes.png', width: 26, height: 26),
            label: AppLocalizations.instance.navRoutes,
          ),
          BottomNavigationBarItem(
            icon: Image.asset('assets/icons/icon_nearby.png', width: 24, height: 24),
            activeIcon: Image.asset('assets/icons/icon_nearby.png', width: 26, height: 26),
            label: AppLocalizations.instance.navNearby,
          ),
          BottomNavigationBarItem(
            icon: Image.asset('assets/icons/icon_guide.png', width: 24, height: 24),
            activeIcon: Image.asset('assets/icons/icon_guide.png', width: 26, height: 26),
            label: AppLocalizations.instance.navGuide,
          ),
          BottomNavigationBarItem(
            icon: Image.asset('assets/icons/icon_profile.png', width: 24, height: 24),
            activeIcon: Image.asset('assets/icons/icon_profile.png', width: 26, height: 26),
            label: AppLocalizations.instance.navProfile,
          ),
        ],
      ),
    ),
  );
  }
}
