// =============================================================================
// ONBOARDING SCREEN – SOLID AMBER EDITION ✨
// - Tek renk: #F5A623 (soft amber)
// - Gradient yok, flat design
// - Beyaz başlıklar
// - YENİ: Kaç gün kalacaksın sayfası
// - YENİ: Bitişte şehir seçimi
// =============================================================================

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../l10n/app_localizations.dart';
import '../services/notification_service.dart';
import 'package:google_fonts/google_fonts.dart';
import 'city_switcher_screen.dart';
import '../theme/wanderlust_colors.dart';
import 'paywall_screen.dart';
import '../services/premium_service.dart';
import '../services/tutorial_service.dart'; // YENİ: Tutorial servisi eklendi

class OnboardingScreen extends StatefulWidget {
  final int initialPage;
  
  const OnboardingScreen({super.key, this.initialPage = 0});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen>
    with SingleTickerProviderStateMixin {
  late PageController _pageController;
  int _currentPage = 0;

  late AnimationController _btnController;
  late Animation<double> _btnAnimation;

  // User preferences
  String _selectedStyle = "";
  String _transportMode = "";
  int _walkingLevel = 1;
  String _budgetLevel = "";
  List<String> _selectedInterests = [];
  String _userName = "";
  int _tripDays = 3; // YENİ: Kalınacak gün sayısı
  final _cityController = TextEditingController();

  // New variables from instruction
  double _budgetVal = 1.0; // 1: Eco, 2: Standard, 3: Luxury
  String _travelStyle = "Dengeli"; // This seems to be a duplicate of _selectedStyle, keeping for now as per instruction
  String _transportPref = "Toplu Taşıma"; // This seems to be a duplicate of _transportMode, keeping for now as per instruction
  String _budget = "Dengeli"; // New String variable for budget if needed, keeping sync with _budgetVal

  final _nameController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _currentPage = widget.initialPage;
    _pageController = PageController(initialPage: widget.initialPage);
    _btnController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1800),
    )..repeat(reverse: true);
    _btnAnimation = Tween<double>(
      begin: 0.0,
      end: 8.0,
    ).animate(CurvedAnimation(parent: _btnController, curve: Curves.easeInOut));
  }

  @override
  void dispose() {
    _pageController.dispose();
    _nameController.dispose();
    _btnController.dispose();
    super.dispose();
  }

  void _nextPage() {
    HapticFeedback.mediumImpact();
    if (_currentPage < 6) { // 7 pages total: 0-6
      _pageController.nextPage(
        duration: const Duration(milliseconds: 600),
        curve: Curves.easeOutCubic,
      );
    } else {
      _completeOnboarding();
    }
  }

  void _previousPage() {
    HapticFeedback.lightImpact();
    if (_currentPage > 0) {
      _pageController.previousPage(
        duration: const Duration(milliseconds: 600),
        curve: Curves.easeOutCubic,
      );
    }
  }

  Future<void> _completeOnboarding() async {
    HapticFeedback.heavyImpact();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString("userName", _userName.isEmpty ? "Gezgin" : _userName);
    await prefs.setString("travelStyle", _selectedStyle);
    await prefs.setString("transportMode", _transportMode);
    await prefs.setInt("walkingLevel", _walkingLevel);
    await prefs.setString("budgetLevel", _budgetLevel);
    await prefs.setStringList("interests", _selectedInterests.toList()); // Convert Set to List
    await prefs.setInt("tripDays", _tripDays);
    await prefs.setBool("onboardingCompleted", true);

    // 🔄 TEST MODU: Her yeni kurulumda tutorialları sıfırla ki kullanıcı görebilsin
    await TutorialService.instance.resetAllTutorials();

    if (!mounted) return;

    // Hoş geldin bildirimini tetikle
    // NotificationService().showWelcomeNotification();

    // Doğrudan Şehir Seçimine git (Paywall orada çıkacak)
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (context) => const CitySwitcherScreen(isOnboarding: true),
      ),
    );
  }

  bool get _canProceed {
    switch (_currentPage) {
      case 0:
        return true; // Splash (My Way)
      case 1:
        return true; // Welcome (Name optional)
      case 2:
        return _tripDays > 0;
      case 3:
        return _selectedStyle.isNotEmpty;
      case 4:
        return _transportMode.isNotEmpty;
      case 5:
        return _selectedInterests.isNotEmpty;
      case 6:
        return _budgetLevel.isNotEmpty;
    }
    return true;
  }

  // ✨ SOLID AMBER - Tek renk, gradient yok
  static const _accent = WanderlustColors.accent;

  // New method from instruction
  void _toggleInterest(String interest) {
    HapticFeedback.selectionClick();
    setState(() {
      if (_selectedInterests.contains(interest)) {
        _selectedInterests.remove(interest);
      } else {
        _selectedInterests.add(interest);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(
      const SystemUiOverlayStyle(
        statusBarColor: Colors.transparent,
        statusBarIconBrightness: Brightness.light,
      ),
    );

    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [
          // PAGE VIEW
          PageView(
            controller: _pageController,
            physics: const NeverScrollableScrollPhysics(),
            onPageChanged: (p) => setState(() => _currentPage = p),
            children: List.generate(7, (i) => _buildPage(i)), 
          ),

          // TOP BAR (Hidden on Splash Screen)
          if (_currentPage > 0)
            SafeArea(
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                child: Row(
                  children: [
                    // Back button
                    AnimatedOpacity(
                      opacity: _currentPage > 1 ? 1.0 : 0.0,
                      duration: const Duration(milliseconds: 200),
                      child: GestureDetector(
                        onTap: _currentPage > 1 ? _previousPage : null,
                        child: Container(
                          width: 40,
                          height: 40,
                          decoration: BoxDecoration(
                            color: Colors.white.withOpacity(0.1),
                            borderRadius: BorderRadius.circular(12),
                          ),
                          child: const Icon(
                            Icons.arrow_back_ios_new_rounded,
                            color: Colors.white70,
                            size: 18,
                          ),
                        ),
                      ),
                    ),

                    const Spacer(),

                    // Progress dots - 7 pages (Splash + 6 Steps)
                    // We can hide dots on Splash or show them starting from index 1.
                    // Let's hide dots on Splash.
                    if (_currentPage > 0)
                    ...List.generate(6, (i) {
                      final isActive = i == (_currentPage - 1);
                      final isPast = i < (_currentPage - 1);
                      return AnimatedContainer(
                        duration: const Duration(milliseconds: 300),
                        margin: const EdgeInsets.symmetric(horizontal: 3),
                        width: isActive ? 22 : 7,
                        height: 7,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(4),
                          color: (isActive || isPast)
                              ? _accent
                              : Colors.white.withOpacity(0.2),
                        ),
                      );
                    }),

                    const Spacer(),

                    // Skip button
                    GestureDetector(
                      onTap: _completeOnboarding,
                      child: Text(
                        AppLocalizations.instance.skip,
                        style: GoogleFonts.poppins(
                          color: Colors.white, // Daha görünür
                          fontSize: 14,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),

          // BOTTOM BUTTON
          Positioned(
            left: 20,
            right: 20,
            bottom: MediaQuery.of(context).padding.bottom + 20,
            child: AnimatedBuilder(
              animation: _btnAnimation,
              builder: (context, child) {
                return Transform.translate(
                  offset: Offset(
                    0,
                    _canProceed ? -_btnAnimation.value * 0.3 : 0,
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(100),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: GestureDetector(
                        onTap: _canProceed ? _nextPage : null,
                        child: AnimatedContainer(
                          duration: const Duration(milliseconds: 300),
                          height: 56,
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(100),
                              color: Colors.white.withOpacity(0.08), // Çok hafif, neredeyse görünmez dolgu
                              border: Border.all(
                                color: Colors.white.withOpacity(0.25), // İnce, buzlu cam çerçeve
                                width: 1.0,
                              ),
                            ),
                      child: Center(
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(
                              _currentPage == 6 
                                      ? AppLocalizations.instance.startExplore 
                                      : _currentPage == 0
                                          ? AppLocalizations.instance.t('Keşfetmeye Başla', 'Start Exploring')
                                          : AppLocalizations.instance.continueAction,
                              style: GoogleFonts.poppins(
                                color: _canProceed
                                    ? Colors.white
                                    : Colors.white30,
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                                letterSpacing: 0.3,
                              ),
                            ),
                            if (_canProceed) ...[
                              const SizedBox(width: 8),
                              Icon(
                                _currentPage == 6
                                    ? Icons.explore_rounded
                                    : Icons.arrow_forward_rounded,
                                color: Colors.white,
                                size: 20,
                              ),
                            ],
                          ],
                        ),
                      ),
                    ),
                  ),
                ),
              ),
            );
              },
            ),
          ),

          // LANGUAGE SELECTOR (Top Left - Only on First Page)
          if (_currentPage == 0)
            Positioned(
              top: MediaQuery.of(context).padding.top + 12,
              left: 16,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.black.withOpacity(0.1), // Daha şeffaf arka plan
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: Colors.white.withOpacity(0.15)),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    // Türkçe Bayrağı
                    GestureDetector(
                      onTap: () async {
                        await AppLocalizations.setLanguage(AppLanguage.tr);
                        setState(() {});
                      },
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: AppLocalizations.instance.isTurkish 
                              ? Colors.white.withOpacity(0.2) 
                              : Colors.transparent,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Text('🇹🇷', style: TextStyle(fontSize: 20)),
                      ),
                    ),
                    const SizedBox(width: 4),
                    // İngilizce Bayrağı
                    GestureDetector(
                      onTap: () async {
                        await AppLocalizations.setLanguage(AppLanguage.en);
                        setState(() {});
                      },
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: AppLocalizations.instance.isEnglish 
                              ? Colors.white.withOpacity(0.2) 
                              : Colors.transparent,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Text('🇬🇧', style: TextStyle(fontSize: 20)),
                      ),
                    ),
                  ],
                ),
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildPage(int index) {
    // Background images for 7 pages (0-6)
    // Page 0: My Way splash - uses onboarding1
    // Page 1: Welcome (name) - uses onboarding1  
    // Page 2: Trip days - uses onboarding6
    // Page 3-6: Style, Transport, Interests, Budget
    int imageIndex;
    if (index == 0) {
      imageIndex = 1; // My Way splash -> onboarding1
    } else if (index == 1) {
      imageIndex = 1; // Welcome -> onboarding1
    } else if (index == 2) {
      imageIndex = 6; // Trip days -> onboarding6
    } else if (index == 3) {
      imageIndex = 2; // Style -> onboarding2
    } else if (index == 4) {
      imageIndex = 3; // Transport -> onboarding3
    } else if (index == 5) {
      imageIndex = 4; // Interests -> onboarding4
    } else if (index == 6) {
      imageIndex = 5; // Budget -> onboarding5
    } else {
      imageIndex = 1;
    }

    final imagePath = "assets/onboarding/onboarding$imageIndex.png";

    // Page 0 (My Way splash): Sarı arka plan, logo ve buton
    if (index == 0) {
      return Container(
        color: _accent, // Sarı arka plan
        child: SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(24, 60, 24, 150),
            child: Column(
              children: [
                const Spacer(flex: 2),
                _buildContent(index),
                const Spacer(flex: 1),
              ],
            ),
          ),
        ),
      );
    }

    return Stack(
      fit: StackFit.expand,
      children: [
        // Background image
          Image.asset(
            imagePath,
            fit: BoxFit.cover,
            errorBuilder: (context, error, stackTrace) {
              return Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    colors: [_accent.withOpacity(0.3), Colors.black],
                  ),
                ),
              );
            },
          ),
        

        // Gradient overlay
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Colors.black.withOpacity(0.1),
                  Colors.black.withOpacity(0.4),
                  Colors.black.withOpacity(0.95),
                ],
                stops: const [0.0, 0.5, 0.85],
              ),
            ),
          ),

        SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(24, 60, 24, 150),
            child: Column(
                  children: [
                    const Spacer(flex: 3),
                    _buildContent(index),
                  ],
                ),
          ),
        ),
      ],
    );
  }

  Widget _buildContent(int index) {
    switch (index) {
      case 0:
        return _splashContent(); // My Way logo page
      case 1:
        return _welcomeContent();
      case 2:
        return _tripDaysContent();
      case 3:
        return _styleContent();
      case 4:
        return _transportContent();
      case 5:
        return _interestsContent();
      case 6:
        return _budgetContent();
      default:
        return const SizedBox();
    }
  }

  // ===========================================================================
  // PAGE 0: SPLASH SCREEN (New Design with Handwriting Animation)
  // ===========================================================================
  Widget _splashContent() {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        // Logo
        Center(
          child: Image.asset(
            'assets/images/splash_logo.png',
            width: 260,
            height: 260,
            fit: BoxFit.contain,
          ),
        ),
        const SizedBox(height: 10),
        
        // "MyWay" Title with Handwriting Animation
        Center(
          child: _HandwritingText(
            text: "My Way",
            style: GoogleFonts.pacifico(
              color: Colors.white,
              fontSize: 72,
            ),
            duration: const Duration(milliseconds: 3000),
          ),
        ),
        const SizedBox(height: 24),
        
        // Tagline - centered (with fade-in after text finishes)
        TweenAnimationBuilder<double>(
          tween: Tween(begin: 0.0, end: 1.0),
          // Total delay = 400ms (start) + 3000ms (duration) + 200ms (buffer)
          curve: const Interval(0.80, 1.0, curve: Curves.easeIn), 
          duration: const Duration(milliseconds: 4500),
          builder: (context, value, child) {
            return Opacity(
              opacity: value,
              child: Transform.translate(
                offset: Offset(0, 10 * (1 - value)),
                child: child,
              ),
            );
          },
          child: Center(
            child: Text(
              AppLocalizations.instance.onboardingTagline.toUpperCase(),
              style: GoogleFonts.poppins(
                color: Colors.white,
                fontSize: 12,
                fontWeight: FontWeight.w500,
                letterSpacing: 4.0,
              ),
            ),
          ),
        ),
      ],
    );
  }

  // ===========================================================================
  // PAGE 1: WELCOME (Original Form)
  // ===========================================================================
  Widget _welcomeContent() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title(AppLocalizations.instance.helloGreeting),
        const SizedBox(height: 8),
        _subtitle(AppLocalizations.instance.howToCallYou),
        const SizedBox(height: 24),
        _glassInput(
          controller: _nameController,
          hint: AppLocalizations.instance.nameHint,
          onChanged: (v) => setState(() => _userName = v),
        ),
        // Klavye ve buton arasında boşluk
        const SizedBox(height: 60),
      ],
    );
  }

  // ===========================================================================
  // PAGE 1: TRIP DAYS - Diğer sayfalara uygun zarif tasarım
  // ===========================================================================
  Widget _tripDaysContent() {
    // The original code had a duplicate _tripDaysContent() method.
    // I'm keeping the second, more complete one from the original document.
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        _title(AppLocalizations.instance.howManyDays),
        const SizedBox(height: 40),
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Expanded(child: _dayCard("1-2", AppLocalizations.instance.days, Icons.weekend_rounded, _tripDays <= 2, () => setState(() => _tripDays = 2))),
            const SizedBox(width: 12),
            Expanded(child: _dayCard("3-5", AppLocalizations.instance.days, Icons.calendar_today_rounded, _tripDays >= 3 && _tripDays <= 5, () => setState(() => _tripDays = 4))),
            const SizedBox(width: 12),
            Expanded(child: _dayCard("7+", AppLocalizations.instance.days, Icons.date_range_rounded, _tripDays > 5, () => setState(() => _tripDays = 7))),
          ],
        ),
        const SizedBox(height: 30),
        _daySlider(),
      ],
    );
  }

  Widget _dayCard(
    String days,
    String label,
    IconData icon,
    bool isSelected,
    VoidCallback onTap,
  ) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        curve: Curves.easeOutCubic,
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: isSelected ? _accent : Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected
                ? Colors.transparent
                : Colors.white.withOpacity(0.08),
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: _accent.withOpacity(0.3),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ]
              : null,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(
                  icon,
                  color: Colors.white.withOpacity(isSelected ? 1 : 0.6),
                  size: 20,
                ),
                if (isSelected)
                  Container(
                    padding: const EdgeInsets.all(3),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(
                      Icons.check_rounded,
                      color: Colors.white,
                      size: 10,
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 10),
            Text(
              "$days ${AppLocalizations.instance.days}",
              style: GoogleFonts.poppins(
                color: Colors.white.withOpacity(isSelected ? 1 : 0.85),
                fontSize: 15,
                fontWeight: FontWeight.w600,
              ),
            ),
            const SizedBox(height: 2),
            Text(
              label,
              style: GoogleFonts.poppins(
                color: Colors.white.withOpacity(isSelected ? 0.85 : 0.45),
                fontSize: 11,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _daySlider() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: Colors.white.withOpacity(0.08)),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                AppLocalizations.instance.exactlyHowManyDays,
                style: GoogleFonts.poppins(
                  color: Colors.white.withOpacity(0.6),
                  fontSize: 13,
                ),
              ),
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 10,
                  vertical: 3,
                ),
                decoration: BoxDecoration(
                  color: _accent,
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Text(
                  AppLocalizations.instance.nDays(_tripDays),
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontSize: 11,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          SliderTheme(
            data: SliderThemeData(
              activeTrackColor: _accent,
              inactiveTrackColor: Colors.white.withOpacity(0.1),
              thumbColor: Colors.white,
              thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 7),
              trackHeight: 3,
              overlayColor: _accent.withOpacity(0.2),
            ),
            child: Slider(
              value: _tripDays.toDouble(),
              min: 1,
              max: 14,
              divisions: 13,
              onChanged: (v) {
                HapticFeedback.selectionClick();
                setState(() => _tripDays = v.toInt());
              },
            ),
          ),
        ],
      ),
    );
  }

  // ===========================================================================
  // PAGE 2: STYLE
  // ===========================================================================
  Widget _styleContent() {
    final items = [
      (AppLocalizations.instance.styleTourist, Icons.photo_camera_rounded),
      (AppLocalizations.instance.styleLocal, Icons.store_rounded),
      (AppLocalizations.instance.styleAdventurer, Icons.terrain_rounded),
      (AppLocalizations.instance.styleCultural, Icons.museum_rounded),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title(AppLocalizations.instance.yourTravelStyle),
        const SizedBox(height: 8),
        _subtitle(AppLocalizations.instance.travelStyleSubtitle),
        const SizedBox(height: 24),
        Row(
          children: [
            Expanded(
              child: _selectCard(
                items[0].$1,
                items[0].$2,
                _selectedStyle == items[0].$1,
                () => setState(() => _selectedStyle = items[0].$1),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: _selectCard(
                items[1].$1,
                items[1].$2,
                _selectedStyle == items[1].$1,
                () => setState(() => _selectedStyle = items[1].$1),
              ),
            ),
          ],
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: _selectCard(
                items[2].$1,
                items[2].$2,
                _selectedStyle == items[2].$1,
                () => setState(() => _selectedStyle = items[2].$1),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: _selectCard(
                items[3].$1,
                items[3].$2,
                _selectedStyle == items[3].$1,
                () => setState(() => _selectedStyle = items[3].$1),
              ),
            ),
          ],
        ),
      ],
    );
  }

  // ===========================================================================
  // PAGE 3: TRANSPORT
  // ===========================================================================
  Widget _transportContent() {
    final items = [
      (AppLocalizations.instance.walking, Icons.directions_walk_rounded),
      (AppLocalizations.instance.publicTransport, Icons.directions_bus_rounded),
      (AppLocalizations.instance.byCar, Icons.directions_car_rounded),
      (AppLocalizations.instance.mixed, Icons.shuffle_rounded),
    ];

    final isSliderActive =
        _transportMode == AppLocalizations.instance.walking || _transportMode == AppLocalizations.instance.mixed;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title(AppLocalizations.instance.transportPreference),
        const SizedBox(height: 8),
        _subtitle(AppLocalizations.instance.transportSubtitle),
        const SizedBox(height: 24),
        Wrap(
          spacing: 10,
          runSpacing: 10,
          children: items.map((item) {
            final isSelected = _transportMode == item.$1;
            return _selectChip(
              item.$1,
              item.$2,
              isSelected,
              () => setState(() => _transportMode = item.$1),
            );
          }).toList(),
        ),
        const SizedBox(height: 20),
        _walkSlider(isActive: isSliderActive),
      ],
    );
  }

  Widget _walkSlider({required bool isActive}) {
    // final labels = ["Hafif", "Normal", "Aktif", "Sporcu"];

    return AnimatedOpacity(
      duration: const Duration(milliseconds: 300),
      opacity: isActive ? 1.0 : 0.4,
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.05),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.white.withOpacity(0.08)),
        ),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  AppLocalizations.instance.walkingCapacity,
                  style: GoogleFonts.poppins(
                    color: Colors.white.withOpacity(0.7),
                    fontSize: 14,
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 12,
                    vertical: 4,
                  ),
                  decoration: BoxDecoration(
                    color: isActive ? _accent : Colors.white.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Text(
                    AppLocalizations.instance.translateWalkingLevel(_walkingLevel),
                    style: GoogleFonts.poppins(
                      color: isActive ? Colors.white : Colors.white54,
                      fontSize: 12,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            AbsorbPointer(
              absorbing: !isActive,
              child: SliderTheme(
                data: SliderThemeData(
                  activeTrackColor: isActive ? _accent : Colors.white24,
                  inactiveTrackColor: Colors.white.withOpacity(0.1),
                  thumbColor: isActive ? Colors.white : Colors.white54,
                  thumbShape: const RoundSliderThumbShape(
                    enabledThumbRadius: 8,
                  ),
                  trackHeight: 4,
                  overlayColor: _accent.withOpacity(0.2),
                ),
                child: Slider(
                  value: _walkingLevel.toDouble(),
                  min: 0,
                  max: 3,
                  divisions: 3,
                  onChanged: isActive
                      ? (v) => setState(() => _walkingLevel = v.toInt())
                      : null,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ===========================================================================
  // PAGE 4: INTERESTS
  // ===========================================================================
  
  // İlgi alanlarının anahtarları
  final _allInterestKeys = const [
    "Tarih", "Yemek", "Sanat", "Doğa", 
    "Alışveriş", "Gece Hayatı", "Fotoğraf", 
    "Spor", "Mimari", "Müzik"
  ];

  Widget _interestsContent() {
    final areAllSelected = _selectedInterests.length == _allInterestKeys.length;

    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
             // Başlığı sola hizalayabilmek için Expanded veya esnek yapı
             Expanded(child: _title(AppLocalizations.instance.interests)),
             
             // TÜMÜNÜ SEÇ BUTONU
             GestureDetector(
               onTap: () {
                 HapticFeedback.mediumImpact();
                 setState(() {
                   if (areAllSelected) {
                     _selectedInterests.clear();
                   } else {
                     _selectedInterests = List.from(_allInterestKeys);
                   }
                 });
               },
               child: Container(
                 padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                 decoration: BoxDecoration(
                   color: Colors.white.withOpacity(0.1),
                   borderRadius: BorderRadius.circular(20),
                   border: Border.all(
                     color: areAllSelected ? _accent : Colors.white.withOpacity(0.2),
                   ),
                 ),
                 child: Text(
                   areAllSelected ? AppLocalizations.instance.clear : AppLocalizations.instance.selectAll,
                   style: GoogleFonts.poppins(
                     color: Colors.white, // Daha görünür
                     fontSize: 12,
                     fontWeight: FontWeight.w600,
                   ),
                 ),
               ),
             ),
          ],
        ),
        const SizedBox(height: 40),
        Wrap(
          spacing: 12,
          runSpacing: 12,
          alignment: WrapAlignment.center,
          children: [
            _selectChip(AppLocalizations.instance.interestHistory, Icons.account_balance_rounded, _selectedInterests.contains("Tarih"), () => _toggleInterest("Tarih")),
            _selectChip(AppLocalizations.instance.interestFood, Icons.restaurant_rounded, _selectedInterests.contains("Yemek"), () => _toggleInterest("Yemek")),
            _selectChip(AppLocalizations.instance.interestArt, Icons.palette_rounded, _selectedInterests.contains("Sanat"), () => _toggleInterest("Sanat")),
            _selectChip(AppLocalizations.instance.interestNature, Icons.park_rounded, _selectedInterests.contains("Doğa"), () => _toggleInterest("Doğa")),
            _selectChip(AppLocalizations.instance.interestShopping, Icons.shopping_bag_rounded, _selectedInterests.contains("Alışveriş"), () => _toggleInterest("Alışveriş")),
            _selectChip(AppLocalizations.instance.interestNightlife, Icons.nightlife_rounded, _selectedInterests.contains("Gece Hayatı"), () => _toggleInterest("Gece Hayatı")),
            
            // Çevirisi olmayanlar için translationCategory veya manuel
            _selectChip(AppLocalizations.instance.interestPhotography, Icons.camera_alt_rounded, _selectedInterests.contains("Fotoğraf"), () => _toggleInterest("Fotoğraf")),
            _selectChip(AppLocalizations.instance.interestSports, Icons.directions_bike_rounded, _selectedInterests.contains("Spor"), () => _toggleInterest("Spor")),
            _selectChip(AppLocalizations.instance.interestArchitecture, Icons.architecture_rounded, _selectedInterests.contains("Mimari"), () => _toggleInterest("Mimari")),
            _selectChip(AppLocalizations.instance.interestMusic, Icons.music_note_rounded, _selectedInterests.contains("Müzik"), () => _toggleInterest("Müzik")),
          ],
        ),
      ],
    );
  }

  // ===========================================================================
  // PAGE 5: BUDGET
  // ===========================================================================
  Widget _budgetContent() {
    final items = [
      (AppLocalizations.instance.budgetEconomy, Icons.savings_rounded, AppLocalizations.instance.budgetFriendly),
      (AppLocalizations.instance.budgetBalanced, Icons.account_balance_wallet_rounded, AppLocalizations.instance.pricePerformance),
      (AppLocalizations.instance.budgetPremium, Icons.diamond_rounded, AppLocalizations.instance.bestExperience),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title(AppLocalizations.instance.budgetPreference),
        const SizedBox(height: 8),
        _subtitle(AppLocalizations.instance.budgetSubtitle),
        const SizedBox(height: 24),
        ...items.map((item) {
          final isSelected = _budgetLevel == item.$1;
          return Padding(
            padding: const EdgeInsets.only(bottom: 12),
            child: _budgetTile(item.$1, item.$2, item.$3, isSelected, () {
              HapticFeedback.selectionClick();
              setState(() => _budgetLevel = item.$1);
            }),
          );
        }),
      ],
    );
  }

  // ===========================================================================
  // SHARED COMPONENTS
  // ===========================================================================

  Widget _title(String text) {
    return Text(
      text,
      style: GoogleFonts.poppins(
        fontSize: 32,
        fontWeight: FontWeight.w700,
        color: Colors.white,
        height: 1.2,
      ),
    );
  }

  Widget _subtitle(String text) {
    return Text(
      text,
      style: GoogleFonts.poppins(
        color: Colors.white.withOpacity(0.6),
        fontSize: 16,
      ),
    );
  }

  Widget _glassInput({
    required TextEditingController controller,
    required String hint,
    required ValueChanged<String> onChanged,
  }) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(16),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.08),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
          ),
          child: TextField(
            controller: controller,
            onChanged: onChanged,
            style: const TextStyle(color: Colors.white, fontSize: 16),
            decoration: InputDecoration(
              hintText: hint,
              hintStyle: TextStyle(color: Colors.white.withOpacity(0.3)),
              border: InputBorder.none,
              contentPadding: const EdgeInsets.symmetric(vertical: 18),
            ),
          ),
        ),
      ),
    );
  }

  Widget _selectCard(
    String label,
    IconData icon,
    bool isSelected,
    VoidCallback onTap,
  ) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        curve: Curves.easeOutCubic,
        padding: const EdgeInsets.all(20),
        decoration: BoxDecoration(
          color: isSelected ? _accent : Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isSelected
                ? Colors.transparent
                : Colors.white.withOpacity(0.08),
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: _accent.withOpacity(0.3),
                    blurRadius: 20,
                    offset: const Offset(0, 8),
                  ),
                ]
              : null,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Icon(
                  icon,
                  color: Colors.white.withOpacity(isSelected ? 1 : 0.7),
                  size: 28,
                ),
                if (isSelected)
                  Container(
                    padding: const EdgeInsets.all(4),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(
                      Icons.check_rounded,
                      color: Colors.white,
                      size: 14,
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 16),
            Text(
              label,
              style: GoogleFonts.poppins(
                color: Colors.white.withOpacity(isSelected ? 1 : 0.8),
                fontSize: 16,
                fontWeight: FontWeight.w600,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _selectChip(
    String label,
    IconData icon,
    bool isSelected,
    VoidCallback onTap,
  ) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        onTap();
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: isSelected ? _accent : Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isSelected
                ? Colors.transparent
                : Colors.white.withOpacity(0.1),
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: _accent.withOpacity(0.25),
                    blurRadius: 12,
                    offset: const Offset(0, 4),
                  ),
                ]
              : null,
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              color: Colors.white.withOpacity(isSelected ? 1 : 0.6),
              size: 18,
            ),
            const SizedBox(width: 8),
            Text(
              label,
              style: GoogleFonts.poppins(
                color: Colors.white.withOpacity(isSelected ? 1 : 0.7),
                fontSize: 14,
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _budgetTile(
    String label,
    IconData icon,
    String subtitle,
    bool isSelected,
    VoidCallback onTap,
  ) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        padding: const EdgeInsets.all(18),
        decoration: BoxDecoration(
          color: isSelected ? _accent : Colors.white.withOpacity(0.06),
          borderRadius: BorderRadius.circular(18),
          border: Border.all(
            color: isSelected
                ? Colors.transparent
                : Colors.white.withOpacity(0.08),
          ),
          boxShadow: isSelected
              ? [
                  BoxShadow(
                    color: _accent.withOpacity(0.3),
                    blurRadius: 16,
                    offset: const Offset(0, 6),
                  ),
                ]
              : null,
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(isSelected ? 0.2 : 0.08),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Icon(
                icon,
                color: Colors.white.withOpacity(isSelected ? 1 : 0.7),
                size: 22,
              ),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    label,
                    style: GoogleFonts.poppins(
                      color: Colors.white.withOpacity(isSelected ? 1 : 0.9),
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: GoogleFonts.poppins(
                      color: Colors.white.withOpacity(isSelected ? 0.8 : 0.5),
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),
            AnimatedContainer(
              duration: const Duration(milliseconds: 200),
              width: 24,
              height: 24,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: isSelected
                    ? Colors.white.withOpacity(0.2)
                    : Colors.transparent,
                border: Border.all(
                  color: Colors.white.withOpacity(isSelected ? 0 : 0.2),
                  width: 2,
                ),
              ),
              child: isSelected
                  ? const Icon(
                      Icons.check_rounded,
                      color: Colors.white,
                      size: 14,
                    )
                  : null,
            ),
          ],
        ),
      ),
    );
  }

  void _showLanguageSelector() {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) => Container(
        padding: const EdgeInsets.all(24),
        decoration: const BoxDecoration(
          color: WanderlustColors.bgCard, // bgCard color
          borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 40, height: 4,
              margin: const EdgeInsets.only(bottom: 24),
              decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)),
            ),
            Text(
              AppLocalizations.instance.languageLabel,
              style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 24),
            _buildLanguageOption(AppLanguage.tr, "Türkçe", "🇹🇷"),
            const SizedBox(height: 12),
            _buildLanguageOption(AppLanguage.en, "English", "🇺🇸"),
            const SizedBox(height: 20),
          ],
        ),
      ),
    );
  }

  Widget _buildLanguageOption(AppLanguage lang, String label, String flag) {
    // Current language from AppLocalizations
    final prefs = AppLocalizations.instance.language; 
    // We can't access instance field 'language' easily if it's not static or we don't know the current state.
    // However, AppLocalizations.instance returns the singleton which has 'language'.
    
    final isSelected = AppLocalizations.instance.language == lang;
    
    return GestureDetector(
      onTap: () async {
        await AppLocalizations.setLanguage(lang);
        if (mounted) {
             setState(() {}); // Trigger rebuild to update strings
             // Force AppLocalizations to refresh
        }
        Navigator.pop(context);
        
        // Restart app or navigate to update all screens?
        // Usually setState on the root widget is needed, but here we can just update this screen
        // ideally we should use a ValueListenable or similar for global language change.
        // For now, let's assume main.dart listens to language change or we just reload onboarding strings.
      },
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: isSelected ? WanderlustColors.accent : Colors.white.withOpacity(0.05),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: isSelected ? Colors.transparent : Colors.white10),
        ),
        child: Row(
          children: [
            Text(flag, style: const TextStyle(fontSize: 24)),
            const SizedBox(width: 16),
            Text(
              label,
              style: TextStyle(
                color: isSelected ? Colors.black : Colors.white,
                fontSize: 16,
                fontWeight: FontWeight.w600,
              ),
            ),
            if (isSelected) ...[
              const Spacer(),
              const Icon(Icons.check_circle_rounded, color: Colors.black),
            ],
          ],
        ),
      ),
    );
  }
}
// Custom Painter for the "MyWay" Dashed Loop Logo
class _MyWayLogoPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.white
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3.0
      ..strokeCap = StrokeCap.round;

    final path = Path();
    // Simplified loop shape roughly matching the reference
    // A figure-8 or loop that starts bottom left, loops top right, crosses, and ends bottom center-ish.
    
    final w = size.width;
    final h = size.height;
    
    path.moveTo(w * 0.3, h * 0.75);
    path.cubicTo(
      w * 0.1, h * 0.5,    // CP1
      w * 0.5, h * 0.2,    // CP2
      w * 0.8, h * 0.4,    // End
    );
    path.cubicTo(
      w * 1.0, h * 0.55,   // CP1
      w * 0.9, h * 0.8,    // CP2
      w * 0.6, h * 0.85,   // End
    );
    path.cubicTo(
      w * 0.4, h * 0.9,    // CP1
      w * 0.2, h * 0.7,    // CP2
      w * 0.5, h * 0.3,    // End
    );
    path.cubicTo(
      w * 0.7, h * 0.05,   // CP1
      w * 0.9, h * 0.2,    // CP2
      w * 0.85, h * 0.35,  // End
    );


    // Draw dashed path
    final dashPath = _dashPath(path, dashWidth: 8, dashSpace: 6);
    
    // Add Glow effect
    final glowPaint = Paint()
      ..color = Colors.white.withOpacity(0.5)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 6.0
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 8);
      
    canvas.drawPath(dashPath, glowPaint);
    canvas.drawPath(dashPath, paint);
  }
  
  Path _dashPath(Path source, {required double dashWidth, required double dashSpace}) {
    final Path dest = Path();
    for (final PathMetric metric in source.computeMetrics()) {
      double distance = 0;
      while (distance < metric.length) {
        dest.addPath(
          metric.extractPath(distance, distance + dashWidth),
          Offset.zero,
        );
        distance += dashWidth + dashSpace;
      }
    }
    return dest;
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

// Placeholder for missing glass input if referenced elsewhere (though I replaced its usage)
class _GlassInputPlaceholder extends StatelessWidget {
   const _GlassInputPlaceholder();
   @override
   Widget build(BuildContext context) => const SizedBox();
}

// HANDWRITING TEXT ANIMATION WIDGET - Apple Hello Style
// Draws text stroke by stroke as if a pen is tracing each letter
// =============================================================================
class _HandwritingText extends StatefulWidget {
  final String text;
  final TextStyle style;
  final Duration duration;

  const _HandwritingText({
    required this.text,
    required this.style,
    this.duration = const Duration(milliseconds: 2500),
  });

  @override
  State<_HandwritingText> createState() => _HandwritingTextState();
}

class _HandwritingTextState extends State<_HandwritingText>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: widget.duration,
    );
    // Start animation after a small delay
    Future.delayed(const Duration(milliseconds: 400), () {
      if (mounted) _controller.forward();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return CustomPaint(
          painter: _AppleHelloTextPainter(
            text: widget.text,
            progress: _controller.value,
            textStyle: widget.style,
          ),
          size: const Size(300, 100),
        );
      },
    );
  }
}

// Custom Painter that draws text path progressively like Apple's "Hello"
class _AppleHelloTextPainter extends CustomPainter {
  final String text;
  final double progress;
  final TextStyle textStyle;

  _AppleHelloTextPainter({
    required this.text,
    required this.progress,
    required this.textStyle,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // Create text painter to measure text
    final textPainter = TextPainter(
      text: TextSpan(text: text, style: textStyle),
      textDirection: TextDirection.ltr,
    );
    textPainter.layout();

    // Create path from text
    // Note: We'll simulate the path drawing effect using clip + gradient
    // True path extraction from font is complex and requires native code
    
    // Save the canvas state
    canvas.save();
    
    // Center the text
    final offset = Offset(
      (size.width - textPainter.width) / 2,
      (size.height - textPainter.height) / 2,
    );
    
    // Create a clip that reveals text progressively
    final revealWidth = textPainter.width * progress;
    
    // Draw revealed portion with gradient edge for smooth "writing" effect
    final rect = Rect.fromLTWH(
      offset.dx,
      offset.dy - 10,
      revealWidth + 20, // Extra for gradient fade
      textPainter.height + 20,
    );
    
    // Apply gradient clip for soft edge
    final gradient = LinearGradient(
      begin: Alignment.centerLeft,
      end: Alignment.centerRight,
      colors: [
        Colors.white,
        Colors.white,
        Colors.white.withOpacity(0.0),
      ],
      stops: [
        0.0,
        progress > 0.05 ? (progress - 0.02) : 0.0,
        progress,
      ],
    );
    
    // Draw background text (full, but will be masked)
    canvas.saveLayer(rect, Paint());
    textPainter.paint(canvas, offset);
    
    // Apply gradient mask
    final maskPaint = Paint()
      ..shader = gradient.createShader(
        Rect.fromLTWH(offset.dx, 0, textPainter.width, size.height),
      )
      ..blendMode = BlendMode.dstIn;
    
    canvas.drawRect(
      Rect.fromLTWH(0, 0, size.width, size.height),
      maskPaint,
    );
    
    canvas.restore();
    
    // Draw a subtle "pen tip" glow at the current writing position
    if (progress > 0.01 && progress < 0.99) {
      final penX = offset.dx + (textPainter.width * progress);
      final penY = offset.dy + textPainter.height * 0.6;
      
      final glowPaint = Paint()
        ..color = Colors.white.withOpacity(0.6)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 8);
      
      canvas.drawCircle(Offset(penX, penY), 4, glowPaint);
      
      // Small bright dot for pen tip
      final tipPaint = Paint()
        ..color = Colors.white
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 2);
      
      canvas.drawCircle(Offset(penX, penY), 2, tipPaint);
    }
    
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant _AppleHelloTextPainter oldDelegate) {
    return oldDelegate.progress != progress;
  }
}

// ===========================================================================
// ONBOARDING PAYWALL WRAPPER
// Onboarding sonrası paywall gösterip şehir seçimine yönlendirir
// ===========================================================================
class _OnboardingPaywallWrapper extends StatelessWidget {
  const _OnboardingPaywallWrapper();

  @override
  Widget build(BuildContext context) {
    return PaywallScreen(
      onDismiss: () => _goToCitySelection(context),
      onSubscribe: (planId) async {

        _goToCitySelection(context);
      },
    );
  }

  void _goToCitySelection(BuildContext context) {
    Navigator.pushReplacement(
      context,
      MaterialPageRoute(
        builder: (_) => const CitySwitcherScreen(isOnboarding: true),
      ),
    );
  }
}
