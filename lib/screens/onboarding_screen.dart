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
import 'package:google_fonts/google_fonts.dart';
import 'city_switcher_screen.dart';

class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen>
    with SingleTickerProviderStateMixin {
  final PageController _pageController = PageController();
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

  final _nameController = TextEditingController();

  @override
  void initState() {
    super.initState();
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
    if (_currentPage < 5) {
      // 6 sayfa oldu (0-5)
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
    await prefs.setStringList("interests", _selectedInterests);
    await prefs.setInt("tripDays", _tripDays);
    await prefs.setBool("onboardingCompleted", true);

    if (!mounted) return;

    // Şehir seçim modal'ını göster
    final selectedCity = await CitySwitcherScreen.showAsModal(context);

    // Şehir seçildiyse veya modal kapatıldıysa ana ekrana git
    if (mounted) {
      Navigator.pushReplacementNamed(context, "/main");
    }
  }

  bool get _canProceed {
    switch (_currentPage) {
      case 0:
        return true; // Welcome
      case 1:
        return _tripDays > 0; // Trip days
      case 2:
        return _selectedStyle.isNotEmpty; // Style
      case 3:
        return _transportMode.isNotEmpty; // Transport
      case 4:
        return _selectedInterests.isNotEmpty; // Interests
      case 5:
        return _budgetLevel.isNotEmpty; // Budget
    }
    return true;
  }

  // ✨ SOLID AMBER - Tek renk, gradient yok
  static const _accent = Color(0xFFF5A623);

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
            children: List.generate(6, (i) => _buildPage(i)), // 6 sayfa
          ),

          // TOP BAR
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
              child: Row(
                children: [
                  // Back button
                  AnimatedOpacity(
                    opacity: _currentPage > 0 ? 1.0 : 0.0,
                    duration: const Duration(milliseconds: 200),
                    child: GestureDetector(
                      onTap: _currentPage > 0 ? _previousPage : null,
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

                  // Progress dots - 6 sayfa
                  ...List.generate(6, (i) {
                    final isActive = i == _currentPage;
                    final isPast = i < _currentPage;
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
                      "Atla",
                      style: GoogleFonts.poppins(
                        color: Colors.white.withOpacity(0.5),
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
                  child: GestureDetector(
                    onTap: _canProceed ? _nextPage : null,
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 300),
                      height: 56,
                      decoration: BoxDecoration(
                        color: _canProceed
                            ? _accent
                            : Colors.white.withOpacity(0.08),
                        borderRadius: BorderRadius.circular(16),
                        boxShadow: _canProceed
                            ? [
                                BoxShadow(
                                  color: _accent.withOpacity(0.4),
                                  blurRadius: 24,
                                  offset: const Offset(0, 8),
                                ),
                              ]
                            : null,
                      ),
                      child: Center(
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(
                              _currentPage == 5 ? "Keşfetmeye Başla" : "Devam",
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
                                _currentPage == 5
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
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildPage(int index) {
    // Mevcut 5 onboarding resmini kullan (index 0-4 için)
    // Trip days sayfası (index 1) için onboarding2.png kullan
    // Diğerleri sırayla kayar
    int imageIndex;
    if (index == 0) {
      imageIndex = 1; // Welcome -> onboarding1
    } else if (index == 1) {
      imageIndex = 6; // Trip days -> onboarding2 (şehir manzarası)
    } else {
      imageIndex = index; // Diğerleri: 2->2, 3->3, 4->4, 5->5
    }

    final imagePath = "assets/onboarding/onboarding$imageIndex.png";

    return Stack(
      fit: StackFit.expand,
      children: [
        // Background image
        Image.asset(
          imagePath,
          fit: BoxFit.cover,
          errorBuilder: (context, error, stackTrace) {
            // Resim yoksa fallback - gradient arka plan
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

        // Content
        SafeArea(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(24, 70, 24, 90),
            child: Column(
              children: [const Spacer(flex: 3), _buildContent(index)],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildContent(int index) {
    switch (index) {
      case 0:
        return _welcomeContent();
      case 1:
        return _tripDaysContent(); // YENİ SAYFA
      case 2:
        return _styleContent();
      case 3:
        return _transportContent();
      case 4:
        return _interestsContent();
      case 5:
        return _budgetContent();
      default:
        return const SizedBox();
    }
  }

  // ===========================================================================
  // PAGE 0: WELCOME
  // ===========================================================================
  Widget _welcomeContent() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title("Merhaba! 👋"),
        const SizedBox(height: 8),
        _subtitle("Sana nasıl hitap edelim?"),
        const SizedBox(height: 24),
        _glassInput(
          controller: _nameController,
          hint: "İsmin",
          onChanged: (v) => setState(() => _userName = v),
        ),
      ],
    );
  }

  // ===========================================================================
  // PAGE 1: TRIP DAYS - Diğer sayfalara uygun zarif tasarım
  // ===========================================================================
  Widget _tripDaysContent() {
    final dayOptions = [
      ("1", "Günübirlik", Icons.bolt_rounded),
      ("2-3", "Kısa tatil", Icons.weekend_rounded),
      ("4-5", "Hafta ortası", Icons.explore_rounded),
      ("7+", "Uzun tatil", Icons.flight_takeoff_rounded),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title("Kaç gün kalacaksın?"),
        const SizedBox(height: 8),
        _subtitle("Rotanı buna göre planlayalım"),
        const SizedBox(height: 20),

        // Gün seçici kartları - 2x2 grid (daha kompakt)
        Row(
          children: [
            Expanded(
              child: _dayCard(
                dayOptions[0].$1,
                dayOptions[0].$2,
                dayOptions[0].$3,
                _tripDays == 1,
                () => setState(() => _tripDays = 1),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: _dayCard(
                dayOptions[1].$1,
                dayOptions[1].$2,
                dayOptions[1].$3,
                _tripDays >= 2 && _tripDays <= 3,
                () => setState(() => _tripDays = 3),
              ),
            ),
          ],
        ),
        const SizedBox(height: 10),
        Row(
          children: [
            Expanded(
              child: _dayCard(
                dayOptions[2].$1,
                dayOptions[2].$2,
                dayOptions[2].$3,
                _tripDays >= 4 && _tripDays <= 6,
                () => setState(() => _tripDays = 5),
              ),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: _dayCard(
                dayOptions[3].$1,
                dayOptions[3].$2,
                dayOptions[3].$3,
                _tripDays >= 7,
                () => setState(() => _tripDays = 7),
              ),
            ),
          ],
        ),

        const SizedBox(height: 16),

        // İnce ayar slider'ı
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
              "$days gün",
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
                "Tam olarak kaç gün?",
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
                  "$_tripDays gün",
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
      ("Turistik", Icons.photo_camera_rounded),
      ("Yerel", Icons.store_rounded),
      ("Maceracı", Icons.terrain_rounded),
      ("Kültürel", Icons.museum_rounded),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title("Seyahat tarzın"),
        const SizedBox(height: 8),
        _subtitle("Sana özel rotalar oluşturalım"),
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
      ("Yürüyerek", Icons.directions_walk_rounded),
      ("Toplu taşıma", Icons.directions_bus_rounded),
      ("Araçla", Icons.directions_car_rounded),
      ("Karışık", Icons.shuffle_rounded),
    ];

    final isSliderActive =
        _transportMode == "Yürüyerek" || _transportMode == "Karışık";

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title("Ulaşım tercihin"),
        const SizedBox(height: 8),
        _subtitle("Rotaları buna göre optimize edelim"),
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
    final labels = ["Hafif", "Normal", "Aktif", "Sporcu"];

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
                  "Yürüme kapasiten",
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
                    labels[_walkingLevel],
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
  Widget _interestsContent() {
    final items = [
      ("Yemek", Icons.restaurant_rounded),
      ("Kahve", Icons.local_cafe_rounded),
      ("Sanat", Icons.palette_rounded),
      ("Tarih", Icons.account_balance_rounded),
      ("Doğa", Icons.park_rounded),
      ("Gece", Icons.nightlife_rounded),
      ("Alışveriş", Icons.shopping_bag_rounded),
      ("Fotoğraf", Icons.camera_alt_rounded),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        Row(
          children: [
            Expanded(child: _title("İlgi alanların")),
            if (_selectedInterests.isNotEmpty)
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 10,
                  vertical: 4,
                ),
                decoration: BoxDecoration(
                  color: _accent.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  "${_selectedInterests.length} seçili",
                  style: GoogleFonts.poppins(
                    color: _accent,
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ),
          ],
        ),
        const SizedBox(height: 8),
        _subtitle("Birden fazla seçebilirsin"),
        const SizedBox(height: 24),
        Wrap(
          spacing: 10,
          runSpacing: 10,
          children: items.map((item) {
            final isSelected = _selectedInterests.contains(item.$1);
            return _selectChip(item.$1, item.$2, isSelected, () {
              HapticFeedback.selectionClick();
              setState(() {
                if (isSelected) {
                  _selectedInterests.remove(item.$1);
                } else {
                  _selectedInterests.add(item.$1);
                }
              });
            });
          }).toList(),
        ),
      ],
    );
  }

  // ===========================================================================
  // PAGE 5: BUDGET
  // ===========================================================================
  Widget _budgetContent() {
    final items = [
      ("Ekonomik", Icons.savings_rounded, "Bütçe dostu"),
      ("Dengeli", Icons.account_balance_wallet_rounded, "Fiyat/performans"),
      ("Premium", Icons.diamond_rounded, "En iyi deneyim"),
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      mainAxisSize: MainAxisSize.min,
      children: [
        _title("Bütçe tercihin"),
        const SizedBox(height: 8),
        _subtitle("Önerileri buna göre filtreleyeceğiz"),
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
}
