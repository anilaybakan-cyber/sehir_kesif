import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../services/tutorial_service.dart';

class PremiumTutorialScreen extends StatefulWidget {
  const PremiumTutorialScreen({super.key});

  @override
  State<PremiumTutorialScreen> createState() => _PremiumTutorialScreenState();
}

class _PremiumTutorialScreenState extends State<PremiumTutorialScreen>
    with SingleTickerProviderStateMixin {
  late PageController _pageController;
  int _currentPage = 0;
  late AnimationController _animationController;
  late Animation<double> _fadeAnimation;
  late Animation<Offset> _slideAnimation;

  @override
  void initState() {
    super.initState();
    _pageController = PageController();
    _animationController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 600),
    );
    _fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _animationController, curve: Curves.easeInOut),
    );
    _slideAnimation = Tween<Offset>(
      begin: const Offset(0, 0.3),
      end: Offset.zero,
    ).animate(
      CurvedAnimation(parent: _animationController, curve: Curves.easeOut),
    );
    _animationController.forward();
  }

  @override
  void dispose() {
    _pageController.dispose();
    _animationController.dispose();
    super.dispose();
  }

  void _onPageChanged(int page) {
    setState(() {
      _currentPage = page;
    });
    _animationController.reset();
    _animationController.forward();
  }

  void _nextPage() {
    HapticFeedback.mediumImpact();
    if (_currentPage < 4) {
      _pageController.nextPage(
        duration: const Duration(milliseconds: 600),
        curve: Curves.easeOutCubic,
      );
    } else {
      _skipTutorial();
    }
  }

  void _skipTutorial() async {
    HapticFeedback.lightImpact();
    await TutorialService.instance.markTutorialSeen(
      TutorialService.KEY_TUTORIAL_PREMIUM,
    );
    if (mounted) {
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: Stack(
        children: [
          // Background gradient
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  WanderlustColors.bgDark,
                  WanderlustColors.bgCard,
                  WanderlustColors.bgCardLight,
                ],
              ),
            ),
          ),
          // Main content
          SafeArea(
            child: Column(
              children: [
                // Skip button
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
                  child: Align(
                    alignment: Alignment.topRight,
                    child: TextButton(
                      onPressed: _skipTutorial,
                      child: Text(
                        isEnglish ? 'Skip' : 'Atla',
                        style: GoogleFonts.poppins(
                          color: WanderlustColors.textGrey,
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ),
                ),
                // PageView
                Expanded(
                  child: PageView(
                    controller: _pageController,
                    onPageChanged: _onPageChanged,
                    children: [
                      _buildNavigationScreen(),
                      _buildExploreScreen(),
                      _buildRoutesScreen(),
                      _buildNearbyScreen(),
                      _buildPremiumScreen(),
                    ],
                  ),
                ),
                // Progress indicator
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 24),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: List.generate(5, (index) {
                      return AnimatedContainer(
                        duration: const Duration(milliseconds: 300),
                        margin: const EdgeInsets.symmetric(horizontal: 4),
                        height: 8,
                        width: _currentPage == index ? 24 : 8,
                        decoration: BoxDecoration(
                          color: _currentPage == index
                              ? WanderlustColors.accent
                              : WanderlustColors.accent.withOpacity(0.3),
                          borderRadius: BorderRadius.circular(4),
                        ),
                      );
                    }),
                  ),
                ),
                // Bottom button
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
                  child: SizedBox(
                    width: double.infinity,
                    height: 56,
                    child: ElevatedButton(
                      onPressed: _nextPage,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: WanderlustColors.accent,
                        foregroundColor: Colors.white,
                        elevation: 0,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(16),
                        ),
                      ),
                      child: Text(
                        _currentPage == 4
                            ? (isEnglish ? 'Done' : 'Tamam')
                            : (isEnglish ? 'Next' : 'Sonraki'),
                        style: GoogleFonts.poppins(
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 20),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildNavigationScreen() {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Title
              Text(
                isEnglish ? 'Navigation' : 'Navigasyon',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: WanderlustColors.textWhite,
                ),
              ),
              const SizedBox(height: 16),
              // Subtitle
              Text(
                isEnglish
                    ? 'Use the bottom navigation to explore different features'
                    : 'Alt navigasyonu kullanarak farklı özellikleri keşfedin',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  color: WanderlustColors.textGrey,
                  height: 1.5,
                ),
              ),
              const SizedBox(height: 40),
              // Navigation mockup
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                decoration: BoxDecoration(
                  color: WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: WanderlustColors.border),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    _buildNavItem(Icons.explore, isEnglish ? 'Explore' : 'Keşfet', true),
                    _buildNavItem(Icons.route, isEnglish ? 'Routes' : 'Rotalar', false),
                    _buildNavItem(Icons.location_on, isEnglish ? 'Nearby' : 'Yakınımda', false),
                    _buildNavItem(Icons.menu_book, isEnglish ? 'Guide' : 'Rehber', false),
                    _buildNavItem(Icons.person, isEnglish ? 'Profile' : 'Profil', false),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              // Feature descriptions
              _buildFeatureDescription(
                icon: Icons.explore,
                title: isEnglish ? 'Explore' : 'Keşfet',
                description: isEnglish ? 'Discover cities and places' : 'Şehirleri ve mekanları keşfedin',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.route,
                title: isEnglish ? 'Routes' : 'Rotalar',
                description: isEnglish ? 'Create and manage your routes' : 'Rotalarınızı oluşturun ve yönetin',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.location_on,
                title: isEnglish ? 'Nearby' : 'Yakınımda',
                description: isEnglish ? 'Find places near you' : 'Yakınındaki mekanları bulun',
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildExploreScreen() {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Title
              Text(
                isEnglish ? 'Explore Screen' : 'Keşfet Ekranı',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: WanderlustColors.textWhite,
                ),
              ),
              const SizedBox(height: 16),
              // Subtitle
              Text(
                isEnglish
                    ? 'Discover cities and get AI-powered recommendations'
                    : 'Şehirleri keşfedin ve AI destekli öneriler alın',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  color: WanderlustColors.textGrey,
                  height: 1.5,
                ),
              ),
              const SizedBox(height: 40),
              // Explore mockup
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: WanderlustColors.border),
                ),
                child: Column(
                  children: [
                    // City selector
                    Container(
                      height: 50,
                      decoration: BoxDecoration(
                        color: WanderlustColors.accent.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: WanderlustColors.accent.withOpacity(0.3)),
                      ),
                      child: Row(
                        children: [
                          const SizedBox(width: 16),
                          Icon(Icons.location_city, color: WanderlustColors.accent, size: 20),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Text(
                              'Barcelona',
                              style: GoogleFonts.poppins(
                                color: WanderlustColors.textWhite,
                                fontSize: 16,
                              ),
                            ),
                          ),
                          const Icon(Icons.arrow_drop_down, color: WanderlustColors.textGrey),
                          const SizedBox(width: 12),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    // AI button
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [WanderlustColors.accent, WanderlustColors.accentLight],
                        ),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.psychology, color: Colors.white, size: 20),
                          const SizedBox(width: 8),
                          Text(
                            isEnglish ? 'AI Assistant' : 'AI Asistan',
                            style: GoogleFonts.poppins(
                              color: Colors.white,
                              fontSize: 14,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    // FAB
                    Align(
                      alignment: Alignment.centerRight,
                      child: Container(
                        width: 56,
                        height: 56,
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [WanderlustColors.accent, WanderlustColors.accentLight],
                          ),
                          borderRadius: BorderRadius.circular(16),
                          boxShadow: [
                            BoxShadow(
                              color: WanderlustColors.accent.withOpacity(0.3),
                              blurRadius: 12,
                              offset: const Offset(0, 4),
                            ),
                          ],
                        ),
                        child: const Icon(Icons.add, color: Colors.white, size: 28),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              // Feature descriptions
              _buildFeatureDescription(
                icon: Icons.location_city,
                title: isEnglish ? 'City Selection' : 'Şehir Seçimi',
                description: isEnglish ? 'Choose from 30+ cities worldwide' : 'Dünyadan 30+ şehir seçin',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.psychology,
                title: isEnglish ? 'AI Assistant' : 'AI Asistan',
                description: isEnglish ? 'Get personalized recommendations' : 'Kişiselleştirilmiş öneriler alın',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.add_circle,
                title: isEnglish ? 'Quick Actions' : 'Hızlı İşlemler',
                description: isEnglish ? 'Add places to your route instantly' : 'Mekanları rotanıza anında ekleyin',
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildRoutesScreen() {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Title
              Text(
                isEnglish ? 'Routes Screen' : 'Rotalar Ekranı',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: WanderlustColors.textWhite,
                ),
              ),
              const SizedBox(height: 16),
              // Subtitle
              Text(
                isEnglish
                    ? 'Create personalized travel routes'
                    : 'Kişiselleştirilmiş seyahat rotaları oluşturun',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  color: WanderlustColors.textGrey,
                  height: 1.5,
                ),
              ),
              const SizedBox(height: 40),
              // Routes mockup
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: WanderlustColors.border),
                ),
                child: Column(
                  children: [
                    // Route card
                    Container(
                      height: 80,
                      decoration: BoxDecoration(
                        color: WanderlustColors.bgCardLight,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Padding(
                        padding: const EdgeInsets.all(12),
                        child: Row(
                          children: [
                            Container(
                              width: 50,
                              height: 50,
                              decoration: BoxDecoration(
                                color: WanderlustColors.accent.withOpacity(0.2),
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: const Icon(Icons.map, color: WanderlustColors.accent),
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Container(
                                    height: 12,
                                    width: 100,
                                    decoration: BoxDecoration(
                                      color: WanderlustColors.textGrey.withOpacity(0.3),
                                      borderRadius: BorderRadius.circular(4),
                                    ),
                                  ),
                                  const SizedBox(height: 4),
                                  Container(
                                    height: 10,
                                    width: 60,
                                    decoration: BoxDecoration(
                                      color: WanderlustColors.textGrey.withOpacity(0.2),
                                      borderRadius: BorderRadius.circular(4),
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(height: 12),
                    // Create route button
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [WanderlustColors.accent, WanderlustColors.accentLight],
                        ),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          const Icon(Icons.add, color: Colors.white, size: 20),
                          const SizedBox(width: 8),
                          Text(
                            isEnglish ? 'Create Route' : 'Rota Oluştur',
                            style: GoogleFonts.poppins(
                              color: Colors.white,
                              fontSize: 14,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              // Feature descriptions
              _buildFeatureDescription(
                icon: Icons.add_circle,
                title: isEnglish ? 'Create Routes' : 'Rota Oluştur',
                description: isEnglish ? 'Build custom routes for any city' : 'Her şehir için özel rotalar oluşturun',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.favorite,
                title: isEnglish ? 'Save Favorites' : 'Favorileri Kaydet',
                description: isEnglish ? 'Keep your favorite routes handy' : 'Favori rotalarınızı elinizin altında tutun',
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNearbyScreen() {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Title
              Text(
                isEnglish ? 'Nearby Screen' : 'Yakınımda Ekranı',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: WanderlustColors.textWhite,
                ),
              ),
              const SizedBox(height: 16),
              // Subtitle
              Text(
                isEnglish
                    ? 'Discover places around your location'
                    : 'Konumunuz çevresindeki mekanları keşfedin',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  color: WanderlustColors.textGrey,
                  height: 1.5,
                ),
              ),
              const SizedBox(height: 40),
              // Nearby mockup
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: WanderlustColors.border),
                ),
                child: Column(
                  children: [
                    // Search bar
                    Container(
                      height: 45,
                      decoration: BoxDecoration(
                        color: WanderlustColors.bgCardLight,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        children: [
                          const SizedBox(width: 12),
                          const Icon(Icons.search, color: WanderlustColors.textGrey, size: 20),
                          const SizedBox(width: 8),
                          Text(
                            isEnglish ? 'Search places...' : 'Mekan ara...',
                            style: GoogleFonts.poppins(
                              color: WanderlustColors.textGrey,
                              fontSize: 14,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 12),
                    // Category chips
                    Wrap(
                      spacing: 8,
                      children: [
                        _buildCategoryChip(isEnglish ? 'All' : 'Tümü', true),
                        _buildCategoryChip(isEnglish ? 'Food' : 'Yemek', false),
                        _buildCategoryChip(isEnglish ? 'Culture' : 'Kültür', false),
                        _buildCategoryChip(isEnglish ? 'Nature' : 'Doğa', false),
                      ],
                    ),
                    const SizedBox(height: 12),
                    // Map/List toggle
                    Row(
                      children: [
                        Expanded(
                          child: Container(
                            height: 36,
                            decoration: BoxDecoration(
                              color: WanderlustColors.accent,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Center(
                              child: Icon(Icons.map, color: Colors.white, size: 20),
                            ),
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Container(
                            height: 36,
                            decoration: BoxDecoration(
                              color: WanderlustColors.bgCardLight,
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Center(
                              child: Icon(Icons.list, color: WanderlustColors.textGrey, size: 20),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              // Feature descriptions
              _buildFeatureDescription(
                icon: Icons.search,
                title: isEnglish ? 'Search' : 'Arama',
                description: isEnglish ? 'Find specific places by name or type' : 'İsim veya türe göre mekan bulun',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.filter_list,
                title: isEnglish ? 'Filter' : 'Filtre',
                description: isEnglish ? 'Filter by category and distance' : 'Kategori ve mesafeye göre filtrele',
              ),
              const SizedBox(height: 16),
              _buildFeatureDescription(
                icon: Icons.map,
                title: isEnglish ? 'Map View' : 'Harita Görünümü',
                description: isEnglish ? 'Switch between map and list views' : 'Harita ve liste görünümü arasında geçiş',
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildPremiumScreen() {
    final isEnglish = AppLocalizations.instance.isEnglish;

    return FadeTransition(
      opacity: _fadeAnimation,
      child: SlideTransition(
        position: _slideAnimation,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 32),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // Premium badge
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      WanderlustColors.accent,
                      WanderlustColors.accentLight,
                    ],
                  ),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Text(
                  'PREMIUM',
                  style: GoogleFonts.poppins(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                    letterSpacing: 2,
                  ),
                ),
              ),
              const SizedBox(height: 24),
              // Title
              Text(
                isEnglish ? 'Unlock Premium Features' : 'Premium Özellikleri Aç',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: WanderlustColors.textWhite,
                  height: 1.2,
                ),
              ),
              const SizedBox(height: 16),
              // Subtitle
              Text(
                isEnglish
                    ? 'Get unlimited access to all features'
                    : 'Tüm özelliklere sınırsız erişim alın',
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  fontSize: 16,
                  color: WanderlustColors.accent,
                  fontWeight: FontWeight.w600,
                ),
              ),
              const SizedBox(height: 32),
              // Feature cards
              _buildFeatureCard(
                icon: Icons.all_inclusive,
                title: isEnglish ? 'Unlimited Routes' : 'Sınırsız Rota',
                description: isEnglish
                    ? 'Create unlimited personalized routes'
                    : 'Sınırsız kişiselleştirilmiş rota oluşturun',
              ),
              const SizedBox(height: 12),
              _buildFeatureCard(
                icon: Icons.psychology,
                title: isEnglish ? 'AI Assistant' : 'AI Asistan',
                description: isEnglish
                    ? 'Get personalized recommendations'
                    : 'Kişiselleştirilmiş öneriler alın',
              ),
              const SizedBox(height: 12),
              _buildFeatureCard(
                icon: Icons.cloud_download,
                title: isEnglish ? 'Offline Mode' : 'Offline Mod',
                description: isEnglish
                    ? 'Download cities and use offline'
                    : 'Şehirleri indirin ve offline kullanın',
              ),
              const SizedBox(height: 12),
              _buildFeatureCard(
                icon: Icons.directions,
                title: isEnglish ? 'Directions' : 'Yol Tarifi',
                description: isEnglish
                    ? 'Get step-by-step directions'
                    : 'Adım adım yol tarifi alın',
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(IconData icon, String label, bool isActive) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Icon(
          icon,
          size: 24,
          color: isActive ? WanderlustColors.accent : WanderlustColors.textGrey,
        ),
        const SizedBox(height: 4),
        Text(
          label,
          style: GoogleFonts.poppins(
            fontSize: 10,
            color: isActive ? WanderlustColors.accent : WanderlustColors.textGrey,
          ),
        ),
      ],
    );
  }

  Widget _buildFeatureDescription({
    required IconData icon,
    required String title,
    required String description,
  }) {
    return Row(
      children: [
        Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: WanderlustColors.accent.withOpacity(0.1),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Icon(icon, color: WanderlustColors.accent, size: 20),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                title,
                style: GoogleFonts.poppins(
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: WanderlustColors.textWhite,
                ),
              ),
              const SizedBox(height: 2),
              Text(
                description,
                style: GoogleFonts.poppins(
                  fontSize: 12,
                  color: WanderlustColors.textGrey,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildFeatureCard({
    required IconData icon,
    required String title,
    required String description,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: WanderlustColors.border,
        ),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.1),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: WanderlustColors.accent, size: 24),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: GoogleFonts.poppins(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: WanderlustColors.textWhite,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  description,
                  style: GoogleFonts.poppins(
                    fontSize: 13,
                    color: WanderlustColors.textGrey,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCategoryChip(String label, bool isActive) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      decoration: BoxDecoration(
        color: isActive
            ? WanderlustColors.accent
            : WanderlustColors.accent.withOpacity(0.1),
        borderRadius: BorderRadius.circular(16),
      ),
      child: Text(
        label,
        style: GoogleFonts.poppins(
          fontSize: 12,
          color: isActive ? Colors.white : WanderlustColors.textGrey,
        ),
      ),
    );
  }
}
