// =============================================================================
// MAIN.DART - WANDERLUST APP
// Onboarding kontrolü ile başlangıç akışı
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';

// Screens
import 'screens/onboarding_screen.dart';
import 'screens/explore_screen.dart';
import 'screens/detail_screen.dart';
import 'screens/routes_screen.dart';
import 'screens/nearby_screen.dart';
import 'screens/profile_screen.dart';
import 'screens/city_switcher_screen.dart';
import 'models/city_model.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

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
      title: 'Wanderlust',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        fontFamily: 'Poppins',
        scaffoldBackgroundColor: const Color(0xFF0D0D1A),
      ),
      home: const SplashScreen(),
      routes: {
        "/onboarding": (_) => const OnboardingScreen(),
        "/main": (_) => const MainScreen(),
        "/city-switch": (_) => const CitySwitcherScreen(),
      },
      onGenerateRoute: (settings) {
        // Detail screen için dynamic route
        if (settings.name == "/detail") {
          final place = settings.arguments as Highlight;
          return MaterialPageRoute(builder: (_) => DetailScreen(place: place));
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
    await Future.delayed(const Duration(milliseconds: 500)); // Kısa splash

    final prefs = await SharedPreferences.getInstance();
    final onboardingCompleted = prefs.getBool("onboardingCompleted") ?? false;

    if (!mounted) return;

    Navigator.pushReplacementNamed(context, "/onboarding");

    //if (onboardingCompleted) {
    // Onboarding tamamlanmış → Ana ekrana git
    //Navigator.pushReplacementNamed(context, "/main");
    //} else {
    // İlk açılış → Onboarding'e git
    Navigator.pushReplacementNamed(context, "/onboarding");
    //}
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF0D0D1A),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Logo/Icon
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: const Color(0xFFF5A623).withOpacity(0.15),
                borderRadius: BorderRadius.circular(24),
              ),
              child: const Icon(
                Icons.explore_rounded,
                color: Color(0xFFF5A623),
                size: 48,
              ),
            ),
            const SizedBox(height: 24),
            const Text(
              "Wanderlust",
              style: TextStyle(
                color: Colors.white,
                fontSize: 28,
                fontWeight: FontWeight.w700,
                letterSpacing: 1,
              ),
            ),
            const SizedBox(height: 32),
            const SizedBox(
              width: 24,
              height: 24,
              child: CircularProgressIndicator(
                color: Color(0xFFF5A623),
                strokeWidth: 2,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

// =============================================================================
// MAIN SCREEN - Bottom Navigation ile ana ekran
// =============================================================================

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int _currentIndex = 0;

  final List<Widget> _screens = [
    const ExploreScreen(),
    const NearbyScreen(),
    const RoutesScreen(),
    const ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(index: _currentIndex, children: _screens),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          color: const Color(0xFF1A1A2E),
          border: Border(
            top: BorderSide(color: Colors.white.withOpacity(0.1), width: 0.5),
          ),
        ),
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 8),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildNavItem(
                  0,
                  Icons.explore_outlined,
                  Icons.explore_rounded,
                  "Keşfet",
                ),
                _buildNavItem(
                  1,
                  Icons.near_me_outlined,
                  Icons.near_me_rounded,
                  "Yakınında",
                ),
                _buildNavItem(
                  2,
                  Icons.map_outlined,
                  Icons.map_rounded,
                  "Rotam",
                ),
                _buildNavItem(
                  3,
                  Icons.person_outline_rounded,
                  Icons.person_rounded,
                  "Profil",
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(
    int index,
    IconData icon,
    IconData activeIcon,
    String label,
  ) {
    final isActive = _currentIndex == index;
    const accent = Color(0xFFF5A623);

    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        setState(() => _currentIndex = index);
      },
      behavior: HitTestBehavior.opaque,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
        decoration: BoxDecoration(
          color: isActive ? accent.withOpacity(0.15) : Colors.transparent,
          borderRadius: BorderRadius.circular(12),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              isActive ? activeIcon : icon,
              color: isActive ? accent : Colors.white.withOpacity(0.5),
              size: 24,
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(
                color: isActive ? accent : Colors.white.withOpacity(0.5),
                fontSize: 11,
                fontWeight: isActive ? FontWeight.w600 : FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
