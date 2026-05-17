import 'dart:async';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:ui';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../theme/wanderlust_colors.dart';
import '../l10n/app_localizations.dart';
import '../services/smart_itinerary_builder.dart';
import '../services/city_data_loader.dart';
import '../services/curated_routes_service.dart';
import '../services/plan_repository.dart';
import '../services/premium_service.dart';
import 'paywall_screen.dart';

class AnalysisLoadingScreen extends StatefulWidget {
  final String cityId;
  const AnalysisLoadingScreen({super.key, required this.cityId});

  @override
  State<AnalysisLoadingScreen> createState() => _AnalysisLoadingScreenState();
}

class _AnalysisLoadingScreenState extends State<AnalysisLoadingScreen>
    with TickerProviderStateMixin {
  late AnimationController _rotationController;
  late AnimationController _bgController;
  late Animation<double> _bgAnimation;

  // Button appear animation
  late AnimationController _btnController;
  late Animation<double> _btnFade;
  late Animation<Offset> _btnSlide;

  // Real plan data
  int _totalDays = 3;
  int _totalPlaces = 0;
  int _curatedRouteCount = 0;
  String _travelStyle = '';
  bool _allStepsDone = false;

  // Step reveal state
  int _revealedSteps = 0;
  final List<AnimationController> _stepControllers = [];
  final List<Animation<double>> _stepFades = [];
  final List<Animation<Offset>> _stepSlides = [];

  // Image carousel
  int _currentImageIndex = 0;
  Timer? _carouselTimer;

  final List<String> _cityImages = [
    'assets/images/loading/barcelona.png',
    'assets/images/loading/amsterdam.png',
    'assets/images/loading/paris.png',
    'assets/images/loading/rome.png',
    'assets/images/loading/nice.png',
    'assets/images/loading/madrid.png',
    'assets/images/loading/istanbul.png',
    'assets/images/loading/london.png',
    'assets/images/loading/venice.png',
    'assets/images/loading/lisbon.png',
  ];

  @override
  void initState() {
    super.initState();

    _rotationController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 2),
    )..repeat();

    _bgController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 600),
    );
    _bgAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(_bgController);
    _bgController.forward();

    // Button animation
    _btnController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 600),
    );
    _btnFade = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _btnController, curve: Curves.easeOut),
    );
    _btnSlide = Tween<Offset>(
      begin: const Offset(0, 0.4),
      end: Offset.zero,
    ).animate(CurvedAnimation(parent: _btnController, curve: Curves.easeOut));

    // Per-step animation controllers (4 steps)
    for (int i = 0; i < 4; i++) {
      final ctrl = AnimationController(
        vsync: this,
        duration: const Duration(milliseconds: 500),
      );
      _stepControllers.add(ctrl);
      _stepFades.add(Tween<double>(begin: 0.0, end: 1.0).animate(
        CurvedAnimation(parent: ctrl, curve: Curves.easeOut),
      ));
      _stepSlides.add(Tween<Offset>(
        begin: const Offset(0, 0.3),
        end: Offset.zero,
      ).animate(CurvedAnimation(parent: ctrl, curve: Curves.easeOut)));
    }

    _startCarousel();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _precacheImages();
      _runLoadingFlow();
    });
  }

  void _precacheImages() {
    for (var path in _cityImages) {
      precacheImage(AssetImage(path), context);
    }
  }

  void _startCarousel() {
    _carouselTimer = Timer.periodic(const Duration(milliseconds: 400), (t) {
      if (mounted) {
        setState(() {
          _currentImageIndex = (_currentImageIndex + 1) % _cityImages.length;
        });
      }
    });
  }

  Future<void> _runLoadingFlow() async {
    final prefs = await SharedPreferences.getInstance();
    _totalDays = prefs.getInt('tripDays_${widget.cityId.toLowerCase()}') ??
        prefs.getInt('tripDays') ?? 3;

    final rawStyle = prefs.getString('user_style') ??
        prefs.getString('travelStyle') ?? '';
    _travelStyle = _localizeStyle(rawStyle);

    // Step 1: show immediately
    await Future.delayed(const Duration(milliseconds: 400));
    _revealStep(0);

    // Generate in background
    final planFuture = SmartItineraryBuilder.generatePlan(
        widget.cityId, _totalDays);

    // Step 2: after plan finishes
    await Future.delayed(const Duration(milliseconds: 1400));
    final schedule = await planFuture;

    if (schedule != null) {
      int count = 0;
      schedule.forEach((_, list) {
        if (list is List) count += list.length;
      });
      if (mounted) setState(() => _totalPlaces = count);
      await SmartItineraryBuilder.savePlan(widget.cityId, schedule);
    }
    _revealStep(1);

    // Step 3: curated routes
    await Future.delayed(const Duration(milliseconds: 1200));
    try {
      final cityData = await CityDataLoader.loadCity(widget.cityId);
      final routes = await CuratedRoutesService.generateRoutes(
          cityData, AppLocalizations.instance.isEnglish);
      if (mounted) setState(() => _curatedRouteCount = routes.length);
    } catch (_) {
      if (mounted) setState(() => _curatedRouteCount = 0);
    }
    _revealStep(2);

    // Step 4: personalization
    await Future.delayed(const Duration(milliseconds: 1200));
    _revealStep(3);

    // Save trial count + flags
    await PlanRepository.incrementTrialCount(widget.cityId);
    await PlanRepository.markPlanCreated(widget.cityId, isAiPlan: true);

    // Show CTA button
    await Future.delayed(const Duration(milliseconds: 600));
    if (mounted) {
      setState(() => _allStepsDone = true);
      _btnController.forward();
      // Stop carousel, stop rotating logo
      _carouselTimer?.cancel();
      _rotationController.stop();
    }
  }

  void _revealStep(int index) {
    if (!mounted) return;
    setState(() => _revealedSteps = index + 1);
    _stepControllers[index].forward();
    HapticFeedback.lightImpact();
  }

  void _onCtaTapped() {
    HapticFeedback.mediumImpact();
    if (PremiumService.instance.isPremium) {
      _navigate();
      return;
    }
    // Ücretsiz: önce paywall; kapatınca (satın almasa bile) Rotam'a git — 1. gün görünür.
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (_) => const PaywallScreen(),
    ).then((_) {
      if (!mounted) return;
      _navigate();
    });
  }

  void _navigate() {
    Navigator.of(context).pushNamedAndRemoveUntil(
      '/main',
      (route) => false,
      arguments: {
        'checkPaywall': false,
        'initialIndex': 1,
        'initialRoutesTabIndex': 1,
      },
    );
  }

  String _localizeStyle(String raw) {
    final isEn = AppLocalizations.instance.isEnglish;
    final map = {
      'Lokal': isEn ? 'Local Explorer' : 'Lokal Kaşif',
      'Turist': isEn ? 'Tourist' : 'Turistik',
      'Tourist': isEn ? 'Tourist' : 'Turistik',
      'Doğa Sever': isEn ? 'Nature Lover' : 'Doğa Sever',
      'Kültür': isEn ? 'Culture Seeker' : 'Kültür Arayışçısı',
      'Denge': isEn ? 'Balanced' : 'Dengeli',
    };
    return map[raw] ?? (isEn ? 'Explorer' : 'Kaşif');
  }

  String _capitalize(String text) {
    if (text.isEmpty) return text;
    return text.split(' ').map((word) {
      if (word.isEmpty) return word;
      return word[0].toUpperCase() + word.substring(1).toLowerCase();
    }).join(' ');
  }

  @override
  void dispose() {
    _carouselTimer?.cancel();
    _rotationController.dispose();
    _bgController.dispose();
    _btnController.dispose();
    for (final c in _stepControllers) {
      c.dispose();
    }
    super.dispose();
  }

  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    final isEn = AppLocalizations.instance.isEnglish;

    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(
        children: [
          // Background carousel
          Positioned.fill(
            child: AnimatedSwitcher(
              duration: const Duration(milliseconds: 600),
              child: Container(
                key: ValueKey(_currentImageIndex),
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage(_cityImages[_currentImageIndex]),
                    fit: BoxFit.cover,
                  ),
                ),
              ),
            ),
          ),

          // Dark overlay
          Positioned.fill(
            child: Container(color: Colors.black.withOpacity(0.70)),
          ),

          // Accent gradient at bottom
          Positioned(
            left: 0, right: 0, bottom: 0,
            height: 220,
            child: Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    Colors.transparent,
                    WanderlustColors.accent.withOpacity(0.25),
                    WanderlustColors.accent.withOpacity(0.10),
                  ],
                ),
              ),
            ),
          ),

          // Main content
          SafeArea(
            child: Column(
              children: [
                const SizedBox(height: 80),

                // Spinning / static logo
                _allStepsDone
                    ? ColorFiltered(
                        colorFilter: const ColorFilter.mode(
                            Colors.white, BlendMode.srcIn),
                        child: Image.asset(
                          'assets/images/splash_logo.png',
                          width: 80,
                          height: 80,
                        ),
                      )
                    : RotationTransition(
                        turns: _rotationController,
                        child: ColorFiltered(
                          colorFilter: const ColorFilter.mode(
                              Colors.white, BlendMode.srcIn),
                          child: Image.asset(
                            'assets/images/splash_logo.png',
                            width: 80,
                            height: 80,
                          ),
                        ),
                      ),

                const SizedBox(height: 20),

                // Title
                FadeTransition(
                  opacity: _bgAnimation,
                  child: Text(
                    _allStepsDone
                        ? (isEn ? 'Your Plan is Ready!' : 'Planın Hazır!')
                        : (isEn ? 'Building Your Plan' : 'Planın Hazırlanıyor'),
                    style: GoogleFonts.poppins(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.5,
                    ),
                  ),
                ),

                const SizedBox(height: 6),

                FadeTransition(
                  opacity: _bgAnimation,
                  child: Text(
                    isEn
                        ? '${_capitalize(AppLocalizations.instance.translateCity(widget.cityId))} · $_totalDays ${_totalDays == 1 ? "day" : "days"}'
                        : '${_capitalize(AppLocalizations.instance.translateCity(widget.cityId))} · $_totalDays gün',
                    style: GoogleFonts.poppins(
                      color: Colors.white54,
                      fontSize: 13,
                    ),
                  ),
                ),

                const SizedBox(height: 36),

                // Step cards
                Expanded(
                  child: ListView(
                    padding: const EdgeInsets.symmetric(horizontal: 24),
                    children: [
                      _buildStep(
                        index: 0,
                        icon: Icons.access_time_rounded,
                        color: WanderlustColors.accent,
                        label: isEn
                            ? '$_totalDays-day itinerary built hour by hour'
                            : '$_totalDays günlük planın saat saat oluşturuldu',
                        subLabel: isEn
                            ? 'Morning to evening, optimized for each day'
                            : 'Sabahtan akşama, her gün için optimize edildi',
                      ),
                      _buildStep(
                        index: 1,
                        icon: Icons.add_location_alt_rounded,
                        color: const Color(0xFF00CEC9),
                        label: _totalPlaces > 0
                            ? (isEn
                                ? '$_totalPlaces places added to your route'
                                : '$_totalPlaces yer rotana eklendi')
                            : (isEn ? 'Adding places...' : 'Yerler ekleniyor...'),
                        subLabel: isEn
                            ? 'Cafés, landmarks, restaurants & viewpoints'
                            : 'Kafeler, tarihi yerler, restoranlar ve manzara noktaları',
                      ),
                      _buildStep(
                        index: 2,
                        icon: Icons.map_rounded,
                        color: const Color(0xFFFDAA5D),
                        label: _curatedRouteCount > 0
                            ? (isEn
                                ? '$_curatedRouteCount curated routes waiting for you'
                                : '$_curatedRouteCount hazır rota seni bekliyor')
                            : (isEn ? 'Loading routes...' : 'Rotalar yükleniyor...'),
                        subLabel: isEn
                            ? 'Expert-picked local experiences'
                            : 'Uzman seçimi yerel deneyimler',
                      ),
                      _buildStep(
                        index: 3,
                        icon: Icons.auto_awesome_rounded,
                        color: const Color(0xFFA29BFE),
                        label: isEn
                            ? 'My Way Assistant is ready to travel with you'
                            : 'My Way Asistan seninle seyahate hazır',
                        subLabel: isEn
                            ? 'Ask questions or generate instant tips on the go'
                            : 'Gezerken asistanına sor veya anlık yeni öneriler oluştur',
                        isLast: true,
                      ),
                    ],
                  ),
                ),

                // CTA Button (appears after all steps done)
                if (_allStepsDone)
                  FadeTransition(
                    opacity: _btnFade,
                    child: SlideTransition(
                      position: _btnSlide,
                      child: Padding(
                        padding: const EdgeInsets.fromLTRB(24, 0, 24, 24),
                        child: GestureDetector(
                          onTap: _onCtaTapped,
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(20),
                            child: BackdropFilter(
                              filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
                              child: Container(
                                width: double.infinity,
                                padding: const EdgeInsets.symmetric(vertical: 12),
                                decoration: BoxDecoration(
                                  color: WanderlustColors.accent.withValues(alpha: 0.35),
                                  borderRadius: BorderRadius.circular(20),
                                  border: Border.all(
                                    color: Colors.white.withValues(alpha: 0.4),
                                    width: 1,
                                  ),
                                ),
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Image.asset(
                                      'assets/icons/icon_travel.png',
                                      width: 28,
                                      height: 28,
                                      color: Colors.white,
                                    ),
                                    const SizedBox(width: 10),
                                    Text(
                                      isEn ? 'Start Exploring' : 'Keşfetmeye Başla',
                                      style: GoogleFonts.poppins(
                                        color: Colors.white,
                                        fontSize: 16,
                                        fontWeight: FontWeight.w700,
                                        letterSpacing: 0.3,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                      ),
                    ),
                  )
                else
                  // Placeholder to keep layout stable while loading
                  const SizedBox(height: 80),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStep({
    required int index,
    required IconData icon,
    required Color color,
    required String label,
    required String subLabel,
    bool isLast = false,
  }) {
    final revealed = _revealedSteps > index;
    if (!revealed) return const SizedBox.shrink();

    return AnimatedBuilder(
      animation: _stepControllers[index],
      builder: (context, child) {
        return FadeTransition(
          opacity: _stepFades[index],
          child: SlideTransition(
            position: _stepSlides[index],
            child: child,
          ),
        );
      },
      child: Padding(
        padding: EdgeInsets.only(bottom: isLast ? 0 : 12),
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            // Purple tick at start
            Container(
              width: 28,
              height: 28,
              decoration: BoxDecoration(
                color: WanderlustColors.accent,
                shape: BoxShape.circle,
              ),
              child: const Icon(Icons.check_rounded,
                  color: Colors.white, size: 16),
            ),
            const SizedBox(width: 12),
            // Glass card behind text
            Expanded(
              child: ClipRRect(
                borderRadius: BorderRadius.circular(14),
                child: Container(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 14, vertical: 12),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.08),
                    borderRadius: BorderRadius.circular(14),
                    border: Border.all(
                      color: Colors.white.withOpacity(0.12),
                      width: 1,
                    ),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        label,
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          height: 1.3,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        subLabel,
                        style: GoogleFonts.poppins(
                          color: Colors.white60,
                          fontSize: 12,
                          height: 1.4,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
