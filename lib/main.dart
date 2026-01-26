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

// Screens
import 'screens/onboarding_screen.dart';
import 'screens/explore_screen.dart'; // Import to ensure type safety if needed, though we use TutorialService
import 'services/tutorial_service.dart';
import 'dart:async';
import 'screens/detail_screen.dart';
import 'screens/routes_screen.dart';
import 'screens/nearby_screen.dart';
import 'screens/profile_screen.dart';
import 'screens/city_switcher_screen.dart';
import 'screens/city_guide_screen.dart'; // Yeni import
import 'models/city_model.dart';
import 'l10n/app_localizations.dart';
import 'theme/wanderlust_colors.dart';
import 'services/notification_service.dart';
import 'services/premium_service.dart';
import 'screens/paywall_screen.dart';
import 'services/premium_service.dart';
import 'screens/paywall_screen.dart';
import 'services/content_update_service.dart';
import 'services/remote_config_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  debugPrint('🚀 main() started');

  // 🔥 Initialize Firebase
  debugPrint('🔥 Firebase.initializeApp() starting...');
  await Firebase.initializeApp();
  debugPrint('🔥 Firebase.initializeApp() DONE');
  
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

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MyWay',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        fontFamily: 'Poppins',
        scaffoldBackgroundColor: WanderlustColors.bgDark,
        textTheme: GoogleFonts.poppinsTextTheme(
          ThemeData.dark().textTheme,
        ),
      ),
      home: const SplashScreen(),
      routes: {
        "/onboarding": (_) => const OnboardingScreen(),
        "/onboarding": (_) => const OnboardingScreen(),
        // "/main": (_) => const MainScreen(), // Moved to onGenerateRoute for arguments
        "/city-switch": (_) => const CitySwitcherScreen(),
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
          final checkPaywall = args?['checkPaywall'] as bool? ?? true;
          return MaterialPageRoute(
            builder: (_) => MainScreen(
              initialIndex: initialIndex,
              checkPaywall: checkPaywall,
            ),
          );
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
    // 🌍 Arka planda içerik güncellemelerini kontrol et (Kullanıcıyı bekletme)
    try {
      ContentUpdateService.checkForUpdates();
    } catch (e) {
      debugPrint("⚠️ Background update error: $e");
    }

    await Future.delayed(const Duration(milliseconds: 500)); // Kısa splash

    final prefs = await SharedPreferences.getInstance();
    final onboardingCompleted = prefs.getBool("onboardingCompleted") ?? false;
    
    // ⚠️ DEV_MODE: Her açılışta onboarding göster (TEST İÇİN)
    // Canlıya çıkarken bunu false yapın!
    // ⚠️ DEV_MODE: Her açılışta onboarding göster (TEST İÇİN)
    // Canlıya çıkarken bunu false yapın!
    const bool forceOnboarding = false;

    if (!mounted) return;

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
  final bool checkPaywall;

  const MainScreen({
    super.key,
    this.initialIndex = 0,
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
    
    if (widget.checkPaywall) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        _checkAndShowPaywall(onDone: () => _checkAndShowCitySuggestion(onDone: _scheduleTutorial));
      });
    } else {
       // Normal launch - still try to schedule tutorial (it will check if seen internally)
       // But maybe with less delay or immediately? User asked for 5-6s delay specifically for onboarding flow.
       // Let's keep it consistent or check if it's first run.
       _scheduleTutorial();
    }
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
          backgroundColor: WanderlustColors.bgDark, // Opaque dark
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Image Header with Overlay
              Stack(
                children: [
                  ClipRRect(
                    borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
                    child: Image.network(
                      cityData['networkImage'],
                      height: 200,
                      width: double.infinity,
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
                            WanderlustColors.bgDark, // Match dialog bg
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
                        color: Colors.white70,
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

  Future<void> _checkAndShowPaywall({VoidCallback? onDone}) async {
    final premium = PremiumService.instance;
    
    final args = ModalRoute.of(context)?.settings.arguments as Map?;
    final bool suppress = args?['suppressPaywall'] ?? false;

    if (!premium.isPremium && !_paywallShown && !suppress) {
      _paywallShown = true;
      await showPaywall(
        context,
        onSubscribe: (planId) async {

          // Paywall handles closing itself on success
        },
      );
      
      // Paywall kapandıktan sonra (her ne sebeple olursa olsun) devam et
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
          NearbyScreen(isVisible: _currentIndex == 1),
          RoutesScreen(isVisible: _currentIndex == 2),
          const CityGuideScreen(),
          ProfileScreen(isVisible: _currentIndex == 4),
        ]),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          HapticFeedback.selectionClick();
          setState(() => _currentIndex = index);
          
          // Trigger tutorial if switching to Nearby tab
          if (index == 1) {
             // Small delay to ensure UI settles if needed
             Future.delayed(const Duration(milliseconds: 300), () {
                TutorialService.instance.triggerTutorial(TutorialService.KEY_TUTORIAL_NEARBY);
             });
          }
        },
        backgroundColor: WanderlustColors.bgDark,
        selectedItemColor: WanderlustColors.accent,
        unselectedItemColor: Colors.white.withOpacity(0.5),
        type: BottomNavigationBarType.fixed,
        elevation: 0,
        items: [
          BottomNavigationBarItem(
            icon: const Icon(Icons.explore_outlined),
            activeIcon: const Icon(Icons.explore_rounded),
            label: AppLocalizations.instance.navExplore,
          ),
          BottomNavigationBarItem(
            icon: const Icon(Icons.near_me_outlined),
            activeIcon: const Icon(Icons.near_me_rounded),
            label: AppLocalizations.instance.navNearby,
          ),
          BottomNavigationBarItem(
            icon: const Icon(Icons.bookmark_border_rounded),
            activeIcon: const Icon(Icons.bookmark_rounded),
            label: AppLocalizations.instance.navRoutes,
          ),
          BottomNavigationBarItem(
            icon: const Icon(Icons.map_outlined),
            activeIcon: const Icon(Icons.map_rounded),
            label: AppLocalizations.instance.navGuide,
          ),
          BottomNavigationBarItem(
            icon: const Icon(Icons.person_outline_rounded),
            activeIcon: const Icon(Icons.person_rounded),
            label: AppLocalizations.instance.navProfile,
          ),
        ],
      ),
    ),
  );
  }
}
