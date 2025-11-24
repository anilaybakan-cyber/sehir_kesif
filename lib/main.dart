import 'package:flutter/material.dart';
import 'package:flutter/cupertino.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'screens/explore_screen.dart';
import 'screens/routes_screen.dart';
import 'screens/nearby_screen.dart';
import 'screens/onboarding_screen.dart';
import 'screens/profile_screen.dart';
import 'screens/city_switcher_screen.dart';
import 'utils/platform_utils.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  final prefs = await SharedPreferences.getInstance();

  // Şimdilik onboarding'i hep gösteriyoruz
  bool showOnboarding = true;
  // Eğer ileride gerçek kontrol istersek:
  // bool showOnboarding =
  //     !(prefs.getBool("onboarding_completed") ?? false);

  runApp(MyApp(showOnboarding: showOnboarding));
}

class MyApp extends StatelessWidget {
  final bool showOnboarding;

  const MyApp({super.key, required this.showOnboarding});

  @override
  Widget build(BuildContext context) {
    final isIOS = PlatformUtils.isIOS;

    return MaterialApp(
      debugShowCheckedModeBanner: false,

      routes: {
        "/main": (_) => MainNavigation(),
        "/city-switch": (_) => CitySwitcherScreen(),
      },

      home: showOnboarding ? const OnboardingScreen() : MainNavigation(),

      theme: ThemeData(
        brightness: Brightness.light,
        scaffoldBackgroundColor: const Color(0xFFF5F5F7),
        primaryColor: Colors.teal,
        fontFamily: isIOS ? '.SF Pro Text' : null,
        platform: isIOS ? TargetPlatform.iOS : TargetPlatform.android,
        appBarTheme: const AppBarTheme(
          backgroundColor: Colors.white,
          elevation: 0,
          foregroundColor: Colors.black87,
        ),
        bottomNavigationBarTheme: const BottomNavigationBarThemeData(
          backgroundColor: Colors.white,
          selectedItemColor: Colors.teal,
          unselectedItemColor: Colors.black38,
          elevation: 8,
        ),
        pageTransitionsTheme: PageTransitionsTheme(
          builders: {
            TargetPlatform.android: const FadeUpwardsPageTransitionsBuilder(),
            TargetPlatform.iOS: const CupertinoPageTransitionsBuilder(),
            TargetPlatform.macOS: const CupertinoPageTransitionsBuilder(),
          },
        ),
      ),
    );
  }
}

class MainNavigation extends StatefulWidget {
  @override
  _MainNavigationState createState() => _MainNavigationState();
}

class _MainNavigationState extends State<MainNavigation> {
  int _selectedIndex = 0;

  final List<Widget> _screens = [
    ExploreScreen(),
    RoutesScreen(),
    NearbyScreen(),
    ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_selectedIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _selectedIndex,
        onTap: (i) => setState(() => _selectedIndex = i),
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.explore), label: "Keşfet"),
          BottomNavigationBarItem(icon: Icon(Icons.map), label: "Rotalar"),
          BottomNavigationBarItem(
            icon: Icon(Icons.location_on),
            label: "Yakında",
          ),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: "Profil"),
        ],
      ),
    );
  }
}
