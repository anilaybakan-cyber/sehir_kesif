// =============================================================================
// PROFILE SCREEN – AIRBNB-INSPIRED WITH BADGE SYSTEM
// User profile with stats, badges, travel history, and settings
// =============================================================================

// =============================================================================
// PROFILE SCREEN – AIRBNB-INSPIRED WITH BADGE SYSTEM
// User profile with stats, badges, travel history, and settings
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:convert';
import 'dart:io';
import 'package:google_fonts/google_fonts.dart';
import 'package:path_provider/path_provider.dart'; // Added
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:ui';
import 'package:url_launcher/url_launcher.dart';
import 'package:share_plus/share_plus.dart';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/trip_update_service.dart';
import '../services/badge_service.dart';
import '../services/memory_service.dart';
import '../models/travel_memory.dart';
import '../models/completed_route.dart';
import '../services/tutorial_service.dart';

import '../l10n/app_localizations.dart';
import 'detail_screen.dart';
import 'onboarding_screen.dart';
import 'memories_screen.dart';
import '../theme/wanderlust_colors.dart';
import '../constants/store_urls.dart';
import 'notifications_screen.dart';
import '../services/notification_service.dart';
import '../widgets/add_memory_sheet.dart';
import '../services/premium_service.dart';
import 'paywall_screen.dart';
import 'city_switcher_screen.dart';
import 'explore_screen.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../widgets/tutorial_overlay_widget.dart';
import '../widgets/feature_spotlight.dart';
import '../widgets/custom_toast.dart';
import '../widgets/resilient_network_image.dart';
import '../services/image_prefetch_service.dart';

class ProfileScreen extends StatefulWidget {
  final bool isVisible;

  /// Açılışta seçilecek alt tab: 0=Favoriler, 1=Ziyaret, 2=Rotalar (history)
  final int initialTabIndex;

  /// Mount sonrası tetiklenecek aksiyon. Desteklenen değerler:
  /// `'add-memory'`, `'preferences'`, `'memories'`.
  final String? initialAction;

  const ProfileScreen({
    super.key,
    this.isVisible = false,
    this.initialTabIndex = 0,
    this.initialAction,
  });

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  // ══════════════════════════════════════════════════════════════════════════
  // AMBER/GOLD THEME
  // ══════════════════════════════════════════════════════════════════════════

  static const Color bgDark = WanderlustColors.bgDark;
  static const Color bgCard = WanderlustColors.bgCard;
  static const Color bgCardLight = WanderlustColors.bgCardLight;
  static const Color accent = WanderlustColors.accent;
  static const Color accentLight = WanderlustColors.accentLight;
  static const Color textWhite = WanderlustColors.textWhite;
  static const Color textGrey = WanderlustColors.textGrey;
  static const Color borderColor = WanderlustColors.borderLight;

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [WanderlustColors.accent, WanderlustColors.accentLight],
  );

  static final Set<String> _citiesWithIcons = {
    'amalfi', 'amsterdam', 'antalya', 'atina', 'bangkok', 'barcelona', 'bari',
    'belgrad', 'berlin', 'bodrum', 'bologna', 'brugge', 'bruksel', 'budapeste',
    'budva', 'kahire', 'cannes', 'kapadokya', 'catania', 'colmar', 'kopenhag',
    'cesme', 'dubai', 'dublin', 'dubrovnik', 'edinburgh', 'fes', 'gaziantep',
    'cenevre', 'giethoorn', 'hallstatt', 'heidelberg', 'hongkong', 'ibiza',
    'istanbul', 'kotor', 'ksamil', 'lizbon', 'londra', 'lucerne', 'lyon',
    'mallorca', 'marakes', 'marsilya', 'midilli', 'milano', 'mykonos', 'napoli',
    'newyork', 'rhodes', 'roma', 'saraybosna', 'selanik', 'madrid', 'nice',
    'oslo', 'palermo', 'paris', 'porto', 'prag', 'rovaniemi', 'saint_tropez',
    'san_sebastian', 'santorini', 'sevilla', 'sintra', 'matera', 'seul', 'singapur',
    'floransa', 'stockholm', 'strazburg', 'tokyo', 'tromso', 'valencia', 'venedik',
    'viyana', 'zermatt', 'zurih', 'kas'
  };

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  String _userName = "Gezgin";
  String _travelStyle = "";
  String _budgetLevel = "";
  List<String> _interests = [];
  List<String> _favorites = [];
  List<String> _visitedPlaces = [];
  List<Highlight> _visitedHighlights = [];
  List<String> _tripPlaces = [];
  List<Highlight> _favoriteHighlights = [];
  String _currentCityName = "-";
  String _memberSince = "2024";
  int _completedRoutesCount = 0;
  List<CompletedRoute> _completedRoutes = [];
  List<Map<String, dynamic>> _savedPlans = [];
  // Planı olmayan ama favorisi/ziyareti olan mekanlar
  List<Highlight> _orphanFavorites = [];
  List<Highlight> _orphanVisited = [];
  final BadgeService _badgeService = BadgeService();
  final MemoryService _memoryService = MemoryService();
  
  // Scroll Controller
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;

  // Tutorial Key
  final GlobalKey _memoriesSectionKey = GlobalKey();

  @override
  void initState() {
    super.initState();
    // Tab controller no longer needed — city cards instead

    // Deeplinkten gelen aksiyon varsa ilk frame sonrası tetikle
    if (widget.initialAction != null && widget.initialAction!.isNotEmpty) {
      WidgetsBinding.instance.addPostFrameCallback((_) {
        if (!mounted) return;
        _handleDeepLinkAction(widget.initialAction!);
      });
    }

    // Listen for trip updates to refresh history count
    TripUpdateService().tripUpdated.addListener(_loadData);
    
    // Scroll Listener
    _scrollController.addListener(() {
      if (_scrollController.offset > 200) {
        if (!_showScrollToTop) setState(() => _showScrollToTop = true);
      } else {
        if (_showScrollToTop) setState(() => _showScrollToTop = false);
      }
    });

    _initializeBadges();
    _loadData();
    _memoryService.initialize();
    
    TripUpdateService().visitUpdated.addListener(_onVisitUpdated);
    TripUpdateService().favoritesUpdated.addListener(_loadData); // 🔥 Add this line
    _badgeService.badgesNotifier.addListener(_onBadgesUpdated);
    _memoryService.memoriesNotifier.addListener(_onMemoriesUpdated);
  }

  Future<void> _initializeBadges() async {
    await _badgeService.initialize();
    if (mounted) setState(() {});
  }

  void _onBadgesUpdated() => setState(() {});
  void _onMemoriesUpdated() => setState(() {});

  void _onVisitUpdated() => _loadData();

  @override
  void didUpdateWidget(ProfileScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    // Profil görünür olduğunda premium spotlight'ı dene (kurallar serviste)
    if (!oldWidget.isVisible && widget.isVisible) {
      Future.delayed(const Duration(milliseconds: 1200), () {
        if (mounted && widget.isVisible) {
          showFeatureSpotlight(
            context,
            spotlightId: 'memories',
            targetKey: _memoriesSectionKey,
          );
        }
      });
    }
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _loadData();
  }

  @override
  void dispose() {
    TripUpdateService().visitUpdated.removeListener(_onVisitUpdated);
    TripUpdateService().favoritesUpdated.removeListener(_loadData); // 🔥 Add this line
    TripUpdateService().tripUpdated.removeListener(_loadData);
    _scrollController.dispose();
    super.dispose();
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DATA LOADING
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();

    // Load user name - if not set, it will be empty and handled in build method
    _userName = prefs.getString("userName") ?? "";
    _travelStyle = prefs.getString("travelStyle") ?? "";
    _budgetLevel = prefs.getString("budgetLevel") ?? "";
    _interests = prefs.getStringList("interests") ?? [];
    _favorites = prefs.getStringList("favorite_places") ?? [];
    _visitedPlaces = prefs.getStringList("visited_places") ?? [];
    final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    _tripPlaces = prefs.getStringList("trip_places_$currentCity") ?? [];
    _completedRoutesCount = prefs.getInt("completed_routes_count") ?? 0;
    
    // Load history
    final historyJson = prefs.getStringList("completed_routes_history") ?? [];
    try {
      _completedRoutes = historyJson.map((e) => CompletedRoute.fromJson(e)).toList();
    } catch (e) {
      debugPrint("Error parsing history: $e");
    }
    
    // Get member since date
    final firstLaunch = prefs.getString("first_launch_date");
    if (firstLaunch != null) {
      final date = DateTime.tryParse(firstLaunch);
      if (date != null) {
        _memberSince = date.year.toString();
      }
    } else {
      await prefs.setString("first_launch_date", DateTime.now().toIso8601String());
    }

    final selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    debugPrint("📍 _loadData: _favorites = $_favorites");
    debugPrint("📍 _loadData: _visitedPlaces = $_visitedPlaces");
    try {
      // Tüm şehirlerdeki favorileri ve ziyaretleri yükle
      await _loadAllFavoritesAndVisits();
      
      // Aktif şehir adını al
      final city = await CityDataLoader.loadCity(selectedCity.toLowerCase());
      _currentCityName = city.city;
    } catch (e) {
      debugPrint("📍 Profil veri yükleme hatası: $e");
      _currentCityName = selectedCity.capitalize();
    }


    await _loadSavedPlans();

    if (!mounted) return;
    setState(() {});
    
    // Tutorial Check
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _checkMemoriesTutorial();
    });
  }

  void _checkMemoriesTutorial() {
    if (!widget.isVisible) return;
    
    TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_MEMORIES).then((shouldShow) {
      if (shouldShow) {
        Future.delayed(const Duration(milliseconds: 800), () {
          if (mounted && widget.isVisible) {
            _showMemoriesTutorial();
          }
        });
      }
    });
  }

  void _showMemoriesTutorial() {
    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        TargetFocus(
          identify: "memories_section",
          keyTarget: _memoriesSectionKey,
          shape: ShapeLightFocus.RRect,
          radius: 24,
          paddingFocus: 4,
          contents: [
            TargetContent(
              align: ContentAlign.top,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: "Anılarım",
                  description: "Seyahatlerinden en güzel anları burada sakla! Fotoğraf ekle, şehirlere göre kategorize et. Her gezi bir hikaye, her anı bir hazine!",
                  onNext: () {
                    controller.next();
                    TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_MEMORIES);
                  },
                  onSkip: () => controller.skip(),
                  currentStep: 1,
                  totalSteps: 1,
                  isArrowUp: false,
                );
              },
            ),
          ],
        ),
      ],
      colorShadow: Colors.black.withOpacity(0.8),
      textSkip: "Atla",
      paddingFocus: 0,
      opacityShadow: 0.9,
      onFinish: () {
         TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_MEMORIES);
      },
      onClickTarget: (target) {
         tutorial.next();
      },
      onClickOverlay: (target) {
         tutorial.next();
      },
      onSkip: () {
         TutorialService.instance.skipAllTutorials();
         return true;
      },
    );
    tutorial.show(context: context);
  }

  /// Tüm şehirlerdeki favorileri ve ziyaretleri yükle
  Future<void> _loadAllFavoritesAndVisits() async {
    // Clear existing lists to avoid duplicates on reload
    _favoriteHighlights.clear();
    _visitedHighlights.clear();

    final prefs = await SharedPreferences.getInstance();
    final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
    // Favori ve ziyaretlerden şehir isimlerini çıkar
    final Set<String> citiesToLoad = {};
    
    // Her zaman mevcut şehri yükle (eski format için)
    citiesToLoad.add(currentCity);
    
    // Eski format var mı kontrol et
    bool hasOldFormat = false;
    
    // Yeni format (city:isim) olan kayıtlardan şehirleri çıkar
    for (final fav in _favorites) {
      if (fav.contains(':')) {
        citiesToLoad.add(fav.split(':')[0].toLowerCase());
      } else {
        hasOldFormat = true;
      }
    }
    
    for (final visit in _visitedPlaces) {
      if (visit.contains(':')) {
        citiesToLoad.add(visit.split(':')[0].toLowerCase());
      } else {
        hasOldFormat = true;
      }
    }
    
    // Eski format varsa, yaygın şehirleri de yükle (geriye uyumluluk)
    if (hasOldFormat) {
      citiesToLoad.addAll(['barcelona', 'berlin', 'paris', 'londra', 'roma', 'amsterdam', 'prag', 'viyana', 'budapeste', 'dublin', 'atina', 'lizbon', 'porto', 'madrid', 'floransa', 'venedik', 'milano', 'istanbul', 'tokyo', 'seul']);
      debugPrint("📍 Eski format kayıt tespit edildi - yaygın şehirler ekleniyor");
    }
    
    debugPrint("📍 Profil: Yüklenecek şehirler = $citiesToLoad");
    debugPrint("📍 Profil: _favorites = $_favorites");
    debugPrint("📍 Profil: _visitedPlaces = $_visitedPlaces");
    
    // Her şehri yükle ve favorileri/ziyaretleri eşleştir
    for (final cityId in citiesToLoad) {
      try {
        final city = await CityDataLoader.loadCity(cityId);
        
        // Bu şehirdeki favorileri bul
        for (final h in city.highlights) {
          final newKey = "$cityId:${h.name}";
          final oldKey = h.name; // Eski format sadece isim
          
          // Hem yeni hem eski format kontrol et
          if (_favorites.contains(newKey) || _favorites.contains(oldKey)) {
            // Duplicate kontrolü
            if (!_favoriteHighlights.any((fh) => fh.name == h.name)) {
              _favoriteHighlights.add(h);
            }
          }
          if (_visitedPlaces.contains(newKey) || _visitedPlaces.contains(oldKey)) {
            // Duplicate kontrolü
            if (!_visitedHighlights.any((vh) => vh.name == h.name)) {
              _visitedHighlights.add(h);
            }
          }
        }
      } catch (e) {
        debugPrint("📍 Şehir yüklenemedi: $cityId - $e");
      }
    }
    
    debugPrint("📍 Toplam favori highlights: ${_favoriteHighlights.length}");
    debugPrint("📍 Toplam ziyaret highlights: ${_visitedHighlights.length}");
  }

  /// Tüm desteklenen şehirlerde kaydedilmiş plan var mı kontrol et
  /// + her şehirdeki favori/ziyaret sayılarını topla
  Future<void> _loadSavedPlans() async {
    final prefs = await SharedPreferences.getInstance();
    final plans = <Map<String, dynamic>>[];
    final plannedCityIds = <String>{};
    final orphanFavs = <Highlight>[];
    final orphanVis = <Highlight>[];

    for (final cityId in CityDataLoader.getSupportedCities()) {
      try {
        final scheduleJson = prefs.getString("trip_schedule_$cityId");
        int totalPlaces = 0;
        int totalDays = 0;
        
        final isPlanSaved = prefs.getBool("is_plan_saved_$cityId") ?? false;

        if (scheduleJson != null && scheduleJson.isNotEmpty && isPlanSaved) {
          try {
            final schedule = jsonDecode(scheduleJson) as Map<String, dynamic>;
            for (final entry in schedule.entries) {
              final dayPlaces = entry.value as List<dynamic>? ?? [];
              if (dayPlaces.isNotEmpty) {
                totalDays++;
                totalPlaces += dayPlaces.length;
              }
            }
          } catch (_) {}
        }

        final isAiPlan = prefs.getBool("is_ai_plan_$cityId") ?? false;

        String cityName = cityId;
        String? heroImage;
        final cityFavs = <Highlight>[];
        final cityVis = <Highlight>[];
        List<CompletedRoute> cityRoutes = [];

        try {
          final city = await CityDataLoader.loadCity(cityId);
          final isEn = AppLocalizations.currentLanguage == AppLanguage.en;
          cityName = (isEn ? city.cityEn : null) ?? city.city;

          try {
            final switcherCity = CitySwitcherScreen.allCities.firstWhere(
              (c) => c['id']?.toString().toLowerCase() == cityId.toLowerCase(),
            );
            heroImage = switcherCity['networkImage'] as String?;
          } catch (_) {}

          if (heroImage == null || heroImage!.isEmpty) {
            heroImage = city.heroImage;
          }
          heroImage = CityDataLoader.normalizeImageUrl(heroImage);

          for (final h in city.highlights) {
            final newKey = "$cityId:${h.name}";
            if (_favorites.contains(newKey) || _favorites.contains(h.name)) {
              cityFavs.add(h);
            }
            if (_visitedPlaces.contains(newKey) || _visitedPlaces.contains(h.name)) {
              cityVis.add(h);
            }
          }
        } catch (_) {
          cityName = cityId[0].toUpperCase() + cityId.substring(1);
        }

        cityRoutes = _completedRoutes
            .where((r) => r.cityName.toLowerCase() == cityId || r.cityName.toLowerCase() == cityName.toLowerCase())
            .toList();

        if (totalPlaces > 0 || cityFavs.isNotEmpty || cityVis.isNotEmpty || cityRoutes.isNotEmpty) {
          plannedCityIds.add(cityId);
          plans.add({
            'cityId': cityId,
            'cityName': cityName,
            'heroImage': heroImage,
            'totalDays': totalDays,
            'totalPlaces': totalPlaces,
            'isAiPlan': isAiPlan,
            'favCount': cityFavs.length,
            'visitCount': cityVis.length,
            'routeCount': cityRoutes.length,
            'scheduleJson': scheduleJson,
            'favorites': cityFavs,
            'visited': cityVis,
            'routes': cityRoutes,
          });
        }
      } catch (e) {
        debugPrint("📍 Plan parse hatası ($cityId): $e");
      }
    }

    // Planı olmayan ama favorisi/ziyareti olan mekanlar
    for (final h in _favoriteHighlights) {
      // Hangi şehirde olduğunu bul
      bool belongsToPlannedCity = false;
      for (final fav in _favorites) {
        if (fav.contains(':')) {
          final cId = fav.split(':')[0].toLowerCase();
          if (fav.split(':')[1] == h.name && plannedCityIds.contains(cId)) {
            belongsToPlannedCity = true;
            break;
          }
        }
      }
      if (!belongsToPlannedCity && !orphanFavs.any((o) => o.name == h.name)) {
        orphanFavs.add(h);
      }
    }
    for (final h in _visitedHighlights) {
      bool belongsToPlannedCity = false;
      for (final vis in _visitedPlaces) {
        if (vis.contains(':')) {
          final cId = vis.split(':')[0].toLowerCase();
          if (vis.split(':')[1] == h.name && plannedCityIds.contains(cId)) {
            belongsToPlannedCity = true;
            break;
          }
        }
      }
      if (!belongsToPlannedCity && !orphanVis.any((o) => o.name == h.name)) {
        orphanVis.add(h);
      }
    }

    _savedPlans = plans;
    _orphanFavorites = orphanFavs;
    _orphanVisited = orphanVis;
  }

  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    final isEnglish = AppLocalizations.currentLanguage == AppLanguage.en;
    
    return Scaffold(
      backgroundColor: bgDark,
      body: Stack(
        children: [
          // Landmark Icons Background (Low Opacity)
          Positioned.fill(
            child: Opacity(
              opacity: 0.15,
              child: Image.asset(
                'assets/images/landmarks.png',
                fit: BoxFit.cover,
                repeat: ImageRepeat.repeat,
              ),
            ),
          ),
          CustomScrollView(
            controller: _scrollController,
        physics: const BouncingScrollPhysics(),
        slivers: [
          // Airbnb-style Profile Header (includes stats)
          SliverToBoxAdapter(child: _buildAirbnbHeader(isEnglish)),

          // Interests Section (Airbnb-style)
          SliverToBoxAdapter(child: _buildInterestsSection(isEnglish)),

          // Memories Section (NEW)
          SliverToBoxAdapter(child: _buildMemoriesSection(isEnglish)),

          // Quick Actions
          SliverToBoxAdapter(child: _buildQuickActions()),

          // Seyahatlerim (City Trip Cards)
          SliverToBoxAdapter(child: _buildTripsSection(isEnglish)),

          // Planı olmayan favoriler/ziyaretler (varsa)
          if (_orphanFavorites.isNotEmpty || _orphanVisited.isNotEmpty)
            SliverToBoxAdapter(child: _buildOrphanSection(isEnglish)),

          // Settings & More
          SliverToBoxAdapter(child: _buildExpandedSettingsSection(isEnglish)),






          const SliverToBoxAdapter(child: SizedBox(height: 100)),
        ],
      ),
          // Scroll-to-top Button
          if (_showScrollToTop)
            Positioned(
              right: 20,
              bottom: 30,
              child: AnimatedOpacity(
                opacity: _showScrollToTop ? 1.0 : 0.0,
                duration: const Duration(milliseconds: 200),
                child: GestureDetector(
                  onTap: () {
                    HapticFeedback.lightImpact();
                    _scrollController.animateTo(
                      0,
                      duration: const Duration(milliseconds: 500),
                      curve: Curves.easeOutCubic,
                    );
                  },
                  child: Container(
                    width: 44,
                    height: 44,
                    decoration: BoxDecoration(
                      color: bgCard.withOpacity(0.8),
                      shape: BoxShape.circle,
                      border: Border.all(color: borderColor.withOpacity(0.5)),
                    ),
                    child: const Icon(
                      Icons.keyboard_arrow_up_rounded,
                      color: textGrey,
                      size: 28,
                    ),
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // AIRBNB-STYLE HEADER (Avatar+Name left, Stats right)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildAirbnbHeader(bool isEnglish) {
    // Stats removed, logic simplified
    // final stats = _badgeService.stats;
    
    return Container(
      padding: const EdgeInsets.fromLTRB(24, 60, 24, 24),
      child: Column(
        children: [
          // Top bar with back button
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              GestureDetector(
                onTap: _showPreferencesBottomSheet,
                child: Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: bgCard,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Icon(Icons.more_horiz, color: textGrey, size: 18),
                ),
              ),
            ],
          ),
          const SizedBox(height: 24),

          // Profile card (Airbnb-style: Avatar+Name left, Stats right)
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: bgCard,
              borderRadius: BorderRadius.circular(24),
              border: Border.all(color: borderColor.withOpacity(0.5)),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // LEFT SIDE: Avatar + Name
                Expanded(
                  flex: 1,
                  child: Column(
                    children: [
                      // Avatar
                      GestureDetector(
                        onTap: _editName,
                        child: Stack(
                          children: [
                            Container(
                              width: 80,
                              height: 80,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                color: bgCardLight,
                                border: Border.all(color: borderColor, width: 2),
                              ),
                              child: ClipRRect(
                                borderRadius: BorderRadius.circular(40),
                                child: Center(
                                  child: Text(
                                    _userName.isNotEmpty ? _userName[0].toUpperCase() : (isEnglish ? "E" : "G"),
                                    style: const TextStyle(
                                      color: textWhite,
                                      fontSize: 32,
                                      fontWeight: FontWeight.w700,
                                    ),
                                  ),
                                ),
                              ),
                            ),
                            Positioned(
                              bottom: 0,
                              right: 0,
                              child: PremiumService.instance.hasFullAccess 
                                ? Container(
                                    padding: const EdgeInsets.all(4),
                                    decoration: BoxDecoration(
                                      color: WanderlustColors.accent,
                                      shape: BoxShape.circle,
                                      border: Border.all(color: bgCard, width: 2),
                                    ),
                                    child: const Icon(Icons.check, color: Colors.white, size: 12),
                                  )
                                : const SizedBox.shrink(),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 12),
                      const SizedBox(height: 12),
                      // Name
                      GestureDetector(
                        onTap: _editName,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Text(
                              _userName.isNotEmpty 
                                  ? _userName 
                                  : (isEnglish ? "Explorer" : "Gezgin"),
                              style: const TextStyle(
                                color: textWhite,
                                fontSize: 18,
                                fontWeight: FontWeight.w700,
                              ),
                              textAlign: TextAlign.center,
                            ),
                            const SizedBox(width: 6),
                            const Icon(Icons.edit, color: textGrey, size: 14),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
                
                // Divider
                Container(
                  width: 1,
                  height: 120,
                  margin: const EdgeInsets.symmetric(horizontal: 16),
                  color: borderColor.withOpacity(0.5),
                ),
                
                // RIGHT SIDE: Stats (2x2 grid)
                Expanded(
                  flex: 1,
                  child: Column(
                    children: [
                      // Row 1
                      Row(
                        children: [
                          Expanded(
                            child: _buildMiniStat(
                              value: _visitedPlaces.length.toString(),
                              label: isEnglish ? "Visits" : "Ziyaret",
                            ),
                          ),
                          Expanded(
                            child: _buildMiniStat(
                              value: _favoriteHighlights.length.toString(),
                              label: isEnglish ? "Favorites" : "Favori",
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 14),
                      // Row 2
                      Row(
                        children: [
                          Expanded(
                            child: _buildMiniStat(
                              value: _completedRoutesCount.toString(),
                              label: isEnglish ? "Routes" : "Rota",
                            ),
                          ),
                          Expanded(
                            child: _buildMiniStat(
                              value: "${_badgeService.totalDistanceKm.toStringAsFixed(1)} km",
                              label: isEnglish ? "Walked" : "Yürüme",
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMiniStat({required String value, required String label}) {
    return Column(
      children: [
        Text(
          label,
          style: TextStyle(color: textGrey.withOpacity(0.7), fontSize: 13),
        ),
        const SizedBox(height: 4),
        Text(
          value,
          style: const TextStyle(
            color: textWhite,
            fontSize: 18,
            fontWeight: FontWeight.w700,
          ),
        ),
      ],
    );
  }

  // Stats bar is now removed - stats are in the header

  // ══════════════════════════════════════════════════════════════════════════
  // INTERESTS SECTION (Airbnb-style with icons)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildInterestsSection(bool isEnglish) {
    if (_interests.isEmpty) return const SizedBox.shrink();

    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 20, 24, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            isEnglish ? "Interests" : "İlgi Alanları",
            style: const TextStyle(
              color: textWhite,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 14),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _interests.map((interest) {
              final iconData = _getInterestIcon(interest);
              return Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                decoration: BoxDecoration(
                  color: bgCard,
                  borderRadius: BorderRadius.circular(24),
                  border: Border.all(color: borderColor.withOpacity(0.5)),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(iconData, color: textGrey, size: 18),
                    const SizedBox(width: 8),
                    Text(
                      AppLocalizations.instance.translateInterest(interest),
                      style: const TextStyle(
                        color: textWhite,
                        fontSize: 13,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  IconData _getInterestIcon(String interest) {
    switch (interest.toLowerCase()) {
      case 'yemek': return Icons.restaurant_rounded;
      case 'kahve': return Icons.coffee_rounded;
      case 'sanat': return Icons.palette_rounded;
      case 'tarih': return Icons.account_balance_rounded;
      case 'doğa': return Icons.park_rounded;
      case 'gece': return Icons.nightlife_rounded;
      case 'alışveriş': return Icons.shopping_bag_rounded;
      case 'fotoğraf': return Icons.camera_alt_rounded;
      case 'mimari': return Icons.architecture_rounded;
      case 'plaj': return Icons.beach_access_rounded;
      case 'spor': return Icons.sports_soccer_rounded;
      case 'müze': return Icons.museum_rounded;
      case 'müzik': return Icons.music_note_rounded;
      case 'yerel lezzetler': return Icons.local_dining_rounded;
      default: return Icons.interests_rounded;
    }
  }


  // ══════════════════════════════════════════════════════════════════════════
  // MEMORIES SECTION (Anılarım)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildMemoriesSection(bool isEnglish) {
    final memories = _memoryService.memories;
    final previewMemories = memories.take(4).toList();
    final isPremium = PremiumService.instance.hasFullAccess;

    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      child: Container(
        key: _memoriesSectionKey,
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(24),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 16, 12, 12),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      Image.asset('assets/icons/icon_memories.png', width: 24, height: 24),
                      const SizedBox(width: 10),
                      Text(
                        isEnglish ? "My Memories" : "Anılarım",
                        style: const TextStyle(
                          color: WanderlustColors.textWhite,
                          fontSize: 17,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      if (memories.isNotEmpty) ...[
                        const SizedBox(width: 8),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          decoration: BoxDecoration(
                            color: WanderlustColors.accent.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Text(
                            '${memories.length}',
                            style: const TextStyle(
                              color: WanderlustColors.accent,
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ],
                    ],
                  ),
                  if (memories.length > 4)
                    TextButton(
                      onPressed: () {
                        HapticFeedback.selectionClick();
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (_) => const MemoriesScreen()),
                        );
                      },
                      child: Text(
                        isEnglish ? "See All" : "Tümünü Gör",
                        style: const TextStyle(color: WanderlustColors.accent, fontSize: 13),
                      ),
                    ),
                ],
              ),
            ),

            // Content
            if (memories.isEmpty)
              // Empty state
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                child: GestureDetector(
                  onTap: () => _addNewMemory(isPremium),
                  child: Container(
                    height: 120,
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: WanderlustColors.accent.withOpacity(0.3)),
                    ),
                    child: Center(
                      child: Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Container(
                            padding: const EdgeInsets.all(12),
                            decoration: BoxDecoration(
                              color: WanderlustColors.accent.withOpacity(0.1),
                              shape: BoxShape.circle,
                            ),
                            child: Image.asset('assets/icons/icon_photo.png', width: 32, height: 32),
                          ),
                          const SizedBox(height: 8),
                          Text(
                            isEnglish ? "Add your first memory" : "İlk anını ekle",
                            style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              )
            else
              // Grid preview
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 16),
                child: Column(
                  children: [
                    SizedBox(
                      height: 160,
                      child: Row(
                        children: [
                          ...previewMemories.map((memory) => Expanded(
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 4),
                              child: _buildMemoryPreviewCard(memory),
                            ),
                          )),
                          // Add button if less than 4 memories
                          if (previewMemories.length < 4)
                            Expanded(
                              child: Padding(
                                padding: const EdgeInsets.symmetric(horizontal: 4),
                                child: GestureDetector(
                                  onTap: () => _addNewMemory(isPremium),
                                  child: Container(
                                    decoration: BoxDecoration(
                                      color: WanderlustColors.bgCard,
                                      borderRadius: BorderRadius.circular(12),
                                      border: Border.all(
                                        color: WanderlustColors.accent.withOpacity(0.3),
                                      ),
                                    ),
                                    child: const Center(
                                      child: Icon(
                                        Icons.add_rounded,
                                        color: WanderlustColors.accent,
                                        size: 32,
                                      ),
                                    ),
                                  ),
                                ),
                              ),
                            ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 12),
                    // View all button
                    GestureDetector(
                      onTap: () {
                        HapticFeedback.selectionClick();
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (_) => const MemoriesScreen()),
                        );
                      },
                      child: Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(vertical: 12),
                        decoration: BoxDecoration(
                          color: WanderlustColors.accent.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Center(
                          child: Text(
                            isEnglish ? "View All Memories" : "Tüm Anıları Gör",
                            style: const TextStyle(
                              color: WanderlustColors.accent,
                              fontWeight: FontWeight.w600,
                            ),
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
  }

  Widget _buildMemoryPreviewCard(TravelMemory memory) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => const MemoriesScreen()),
        );
      },
      child: ClipRRect(
        borderRadius: BorderRadius.circular(12),
        child: Stack(
          fit: StackFit.expand,
          children: [
            Image.file(
              File(memory.imagePath),
              fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Container(
                color: WanderlustColors.bgCard,
                child: const Icon(Icons.broken_image, color: Colors.white38),
              ),
            ),
            // Gradient
            Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    Colors.transparent,
                    Colors.black.withOpacity(0.6),
                  ],
                  stops: const [0.6, 1.0],
                ),
              ),
            ),
            // City name
            Positioned(
              left: 6,
              bottom: 6,
              right: 6,
              child: Builder(
                builder: (context) {
                  // Localize city name
                  String displayName = memory.cityName;
                  if (AppLocalizations.instance.isEnglish) {
                    final cityData = CitySwitcherScreen.allCities.firstWhere(
                      (c) => c['name'] == memory.cityName || c['id'] == memory.cityId,
                      orElse: () => {},
                    );
                    if (cityData.isNotEmpty && cityData['name_en'] != null) {
                      displayName = cityData['name_en'];
                    }
                  }
                  
                  return Text(
                    displayName,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 10,
                      fontWeight: FontWeight.w600,
                    ),
                  );
                }
              ),
            ),
          ],
        ),
      ),
    );
  }

  /// Deeplinkten gelen aksiyonları profil ekranı mount olduktan sonra çalıştırır.
  void _handleDeepLinkAction(String action) {
    final isPremium = PremiumService.instance.hasFullAccess;
    switch (action.toLowerCase()) {
      case 'add-memory':
      case 'addmemory':
      case 'memory-add':
        _addNewMemory(isPremium);
        break;
      case 'preferences':
      case 'settings':
      case 'tercihler':
        _showPreferencesBottomSheet();
        break;
      case 'memories':
      case 'all-memories':
      case 'anilar':
      case 'anılar':
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => const MemoriesScreen()),
        );
        break;
      default:
        debugPrint('🔗 Bilinmeyen profil aksiyonu: $action');
    }
  }

  void _addNewMemory(bool isPremium) async {
    HapticFeedback.mediumImpact();
    
    if (!isPremium) {
      // Show paywall. Paywall kendi rotasını kapatır; burada ek pop yapma,
      // aksi halde Profil ekranı da pop edilip siyah ekran kalıyor.
      showPaywall(
        context,
        source: 'profile_add_memory',
        onSubscribe: (planId) async {

        },
      );
      return;
    }

    await AddMemorySheet.show(context);
  }


  // ══════════════════════════════════════════════════════════════════════════
  // BADGES SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildBadgesSection() {
    final badges = _badgeService.badges;
    final unlockedCount = _badgeService.unlockedCount;
    final totalCount = _badgeService.totalCount;

    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      child: Container(
        decoration: BoxDecoration(
          color: const Color(0xFF1C1C2E),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white.withOpacity(0.05), width: 1),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Section header
            Padding(
              padding: const EdgeInsets.fromLTRB(20, 20, 20, 16),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text(
                    "Rozetlerim",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.w800,
                      letterSpacing: 0.3,
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: accent.withOpacity(0.15),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      "$unlockedCount / $totalCount",
                      style: const TextStyle(
                        color: accent,
                        fontSize: 13,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ],
              ),
            ),
            // Badges Grid (4 columns)
            Padding(
              padding: const EdgeInsets.fromLTRB(8, 0, 8, 20),
              child: GridView.builder(
                padding: EdgeInsets.zero,
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 4,
                  crossAxisSpacing: 8,
                  mainAxisSpacing: 16,
                  childAspectRatio: 0.75,
                ),
                itemCount: badges.length,
                itemBuilder: (context, index) {
                  return _BadgeItem(badge: badges[index]);
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // QUICK ACTIONS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildQuickActions() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 20, 24, 0),
      child: Row(
        children: [
          Expanded(
            child: _buildActionCard(
              iconAsset: 'assets/icons/city.png',
              title: AppLocalizations.instance.t("Aktif Şehir", "Active City"),
              subtitle: _currentCityName,
              onTap: () async {
                await Navigator.pushNamed(context, "/city-switch");
                _loadData();
              },
            ),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: _buildActionCard(
              iconAsset: 'assets/icons/icon_tercihler.png',
              title: AppLocalizations.instance.t("Tercihler", "Preferences"),
              subtitle: _travelStyle.isNotEmpty && _budgetLevel.isNotEmpty
                  ? "${AppLocalizations.instance.translateTravelStyle(_travelStyle)} • ${AppLocalizations.instance.translateBudgetLevel(_budgetLevel)}"
                  : AppLocalizations.instance.t("Henüz tercih yok", "No preferences yet"),
              onTap: _showPreferencesBottomSheet,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildActionCard({
    required String iconAsset,
    required String title,
    required String subtitle,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: bgCardLight,
                borderRadius: BorderRadius.circular(12),
              ),
              child: Image.asset(iconAsset, width: 24, height: 24),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(title, style: TextStyle(color: textGrey, fontSize: 12), maxLines: 1, overflow: TextOverflow.ellipsis),
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: const TextStyle(color: textWhite, fontSize: 14, fontWeight: FontWeight.w600),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ),
            ),
            const Icon(Icons.chevron_right, color: textGrey, size: 18),
          ],
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SEYAHATLERIM (AIRBNB-STYLE CITY TRIP CARDS)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTripsSection(bool isEnglish) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 12, 24, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Başlık
          Row(
            children: [
              Image.asset('assets/icons/icon_explore.png', width: 24, height: 24),
              const SizedBox(width: 8),
              Text(
                isEnglish ? "My Trips" : "Seyahatlerim",
                style: const TextStyle(
                  color: textWhite,
                  fontSize: 18,
                  fontWeight: FontWeight.w700,
                ),
              ),
              const Spacer(),
              if (_savedPlans.isNotEmpty)
                Text(
                  "${_savedPlans.length} ${isEnglish ? 'cities' : 'şehir'}",
                  style: TextStyle(
                    color: textGrey.withOpacity(0.7),
                    fontSize: 13,
                  ),
                ),
            ],
          ),
          const SizedBox(height: 10),
          if (_savedPlans.isEmpty)
            _buildEmptyTripsState(isEnglish)
          else
            GridView.builder(
              padding: EdgeInsets.zero,
              shrinkWrap: true,
              physics: const NeverScrollableScrollPhysics(),
              gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                crossAxisCount: 2,
                mainAxisSpacing: 14,
                crossAxisSpacing: 14,
                childAspectRatio: 0.95,
              ),
              itemCount: _savedPlans.length,
              itemBuilder: (context, index) => _buildSquareTripCard(_savedPlans[index]),
            ),
        ],
      ),
    );
  }

  Widget _buildEmptyTripsState(bool isEnglish) {
    return Container(
      padding: const EdgeInsets.all(32),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: borderColor.withOpacity(0.3)),
      ),
      child: Column(
        children: [
          Icon(Icons.map_outlined, color: textGrey.withOpacity(0.4), size: 48),
          const SizedBox(height: 16),
          Text(
            isEnglish ? "No trips yet" : "Henüz seyahat planın yok",
            style: const TextStyle(
              color: textWhite,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            isEnglish
                ? "Create a daily plan for any city to see it here"
                : "Bir şehir için günlük plan oluşturduğunda burada görünecek",
            textAlign: TextAlign.center,
            style: TextStyle(
              color: textGrey.withOpacity(0.7),
              fontSize: 13,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSquareTripCard(Map<String, dynamic> plan) {
    final cityName = plan['cityName'] as String;
    final cityId = plan['cityId'] as String;
    final totalDays = plan['totalDays'] as int;
    final totalPlaces = plan['totalPlaces'] as int;
    final heroImage = plan['heroImage'] as String?;
    final favCount = plan['favCount'] as int? ?? 0;
    final visitCount = plan['visitCount'] as int? ?? 0;
    final routeCount = plan['routeCount'] as int? ?? 0;
    final isEn = AppLocalizations.instance.isEnglish;

    return GestureDetector(
      onTap: () => _showCityTripDetails(plan),
      child: Container(
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: borderColor.withValues(alpha: 0.4)),
        ),
        clipBehavior: Clip.hardEdge,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Resim + Overlay (Üst kısım)
            Expanded(
              child: Stack(
                children: [
                  SizedBox(
                    width: double.infinity,
                    height: double.infinity,
                    child: _citiesWithIcons.contains(cityId)
                        ? Image.asset(
                            'assets/icons/${cityId}_icon.png',
                            width: double.infinity,
                            height: double.infinity,
                            fit: BoxFit.cover,
                          )
                        : (heroImage != null && heroImage.isNotEmpty
                            ? ResilientNetworkImage(
                                imageUrl: heroImage,
                                placeName: cityName,
                                city: cityId,
                                category: 'city',
                                width: double.infinity,
                                height: double.infinity,
                                fit: BoxFit.cover,
                              )
                            : Container(
                                color: bgCardLight,
                                child: const Center(
                                  child: Icon(Icons.location_city_rounded,
                                      color: textGrey, size: 36),
                                ),
                              )),
                  ),
                  // Gradient overlay
                  Positioned(
                    bottom: 0,
                    left: 0,
                    right: 0,
                    child: Container(
                      height: 50,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.transparent,
                            Colors.black.withValues(alpha: 0.75),
                          ],
                        ),
                      ),
                    ),
                  ),
                  // Şehir adı (bottom left)
                  Positioned(
                    bottom: 8,
                    left: 12,
                    right: 12,
                    child: Text(
                      cityName,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 17,
                        fontWeight: FontWeight.w800,
                        shadows: [Shadow(blurRadius: 6, color: Colors.black54)],
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                  ),
                ],
              ),
            ),
            // İstatistikler (Alt kısım)
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 10),
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                physics: const BouncingScrollPhysics(),
                child: Row(
                  children: [
                    const Icon(Icons.calendar_today_rounded, color: accent, size: 13),
                    const SizedBox(width: 4),
                    Text("$totalDays ${isEn ? 'days' : 'gün'}", style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600)),
                    const SizedBox(width: 8),
                    const Icon(Icons.place_outlined, color: accent, size: 13),
                    const SizedBox(width: 4),
                    Text("$totalPlaces ${isEn ? 'places' : 'mekan'}", style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600)),
                    if (favCount > 0) ...[
                      const SizedBox(width: 8),
                      const Icon(Icons.favorite_rounded, color: Colors.redAccent, size: 13),
                      const SizedBox(width: 3),
                      Text("$favCount", style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600)),
                    ],
                    if (visitCount > 0) ...[
                      const SizedBox(width: 8),
                      const Icon(Icons.check_circle_rounded, color: Colors.green, size: 13),
                      const SizedBox(width: 3),
                      Text("$visitCount", style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600)),
                    ],
                    if (routeCount > 0) ...[
                      const SizedBox(width: 8),
                      const Icon(Icons.route_rounded, color: accent, size: 13),
                      const SizedBox(width: 3),
                      Text("$routeCount", style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600)),
                    ],
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  /// Planı olmayan ama favori/ziyaret edilen mekanlar bölümü
  Widget _buildOrphanSection(bool isEnglish) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 20, 24, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            isEnglish ? "Other Places" : "Diğer Mekanlar",
            style: const TextStyle(
              color: textWhite,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 12),
          if (_orphanFavorites.isNotEmpty) ...[
            Text(
              "${isEnglish ? 'Favorites' : 'Favoriler'} (${_orphanFavorites.length})",
              style: TextStyle(color: textGrey, fontSize: 13),
            ),
            const SizedBox(height: 8),
            ..._orphanFavorites.map((h) => _buildPlaceCard(h)),
          ],
          if (_orphanVisited.isNotEmpty) ...[
            const SizedBox(height: 12),
            Text(
              "${isEnglish ? 'Visited' : 'Ziyaret'} (${_orphanVisited.length})",
              style: TextStyle(color: textGrey, fontSize: 13),
            ),
            const SizedBox(height: 8),
            ..._orphanVisited.map((h) => _buildPlaceCard(h, isVisited: true)),
          ],
        ],
      ),
    );
  }



  void _showCityTripDetails(Map<String, dynamic> trip) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => _CityTripDetailSheet(
        trip: trip,
        onNavigateToPlan: () => _navigateToPlan(trip['cityId']),
        buildPlaceCard: (h, {isVisited = false}) => _buildPlaceCard(h, isVisited: isVisited),
      ),
    );
  }

  Future<void> _navigateToPlan(String cityId) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    final currentCity = prefs.getString("selectedCity")?.toLowerCase();

    // Eğer farklı bir şehir ise, önce o şehre geçiş yap
    if (currentCity != cityId) {
      await prefs.setString("selectedCity", cityId);
      TripUpdateService().notifyTripChanged();
    }

    if (!mounted) return;

    // Ana sayfaya routes tab'ına (index 1) ve plan sekmesine (initialRoutesTabIndex: 1) yönlendir
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



  Widget _buildPlaceCard(Highlight place, {bool isVisited = false}) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);

    return GestureDetector(
      onTap: () {
        // Fotoğrafı prefetch et
        ImagePrefetchService.prefetchSinglePhoto(context, place.imageUrl, heroDecode: true);
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 8),
        padding: const EdgeInsets.all(10),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: SizedBox(
                width: 48,
                height: 48,
                child: hasImage
                    ? ResilientNetworkImage(
                        imageUrl: place.imageUrl,
                        placeName: place.getLocalizedName(AppLocalizations.instance.isEnglish),
                        city: place.city ?? place.area,
                        category: place.category,
                        blurHash: place.blurHash,
                        width: 48,
                        height: 48,
                        fit: BoxFit.cover,
                        placeholderBuilder: (_) => Container(
                          color: color.withOpacity(0.15),
                          child: Icon(Icons.place, color: color, size: 24),
                        ),
                      )
                    : Container(
                        color: color.withOpacity(0.15),
                        child: Icon(Icons.place, color: color, size: 24),
                      ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    place.getLocalizedName(AppLocalizations.instance.isEnglish),
                    style: const TextStyle(color: textWhite, fontSize: 14, fontWeight: FontWeight.w600),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),
                  Text(place.area.isNotEmpty ? place.area : (place.city ?? ""), style: const TextStyle(color: textGrey, fontSize: 12)),
                ],
              ),
            ),
            if (isVisited)
              const Icon(Icons.check_circle, color: Color(0xFF4CAF50), size: 20)
            else if (place.rating != null)
              Row(
                children: [
                  const Icon(Icons.star_rounded, color: Color(0xFFFDCB6E), size: 14),
                  const SizedBox(width: 4),
                  Text(
                    place.rating!.toStringAsFixed(1),
                    style: const TextStyle(color: textWhite, fontSize: 12, fontWeight: FontWeight.w600),
                  ),
                ],
              ),
          ],
        ),
      ),
    );
  }



  // ══════════════════════════════════════════════════════════════════════════
  // EXPANDED SETTINGS SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildExpandedSettingsSection(bool isEnglish) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 24, 24, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            isEnglish ? "Settings & Support" : "Ayarlar & Destek",
            style: const TextStyle(color: textWhite, fontSize: 16, fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 12),
          
          Container(
            decoration: BoxDecoration(
              color: bgCard,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: borderColor.withOpacity(0.5)),
            ),
            child: Column(
              children: [
                // Language switcher
                _buildSettingsItem(
                  icon: Icons.language_rounded,
                  title: AppLocalizations.instance.languageLabel,
                  trailing: GestureDetector(
                    onTap: () async {
                      HapticFeedback.mediumImpact();
                      final newLang = isEnglish ? AppLanguage.tr : AppLanguage.en;
                      await AppLocalizations.setLanguage(newLang);
                      if (mounted) {
                        // Restart app but keep state (skip paywall, open profile)
                        Navigator.pushNamedAndRemoveUntil(
                          context, 
                          '/main', 
                          (route) => false,
                          arguments: {
                            'initialIndex': 5, // Profile Tab
                            'checkPaywall': false // Don't show paywall again
                          }
                        );
                      }
                    },
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                      decoration: BoxDecoration(
                        color: accent.withOpacity(0.15),
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: Text(
                        isEnglish ? "🇬🇧 EN" : "🇹🇷 TR",
                        style: const TextStyle(color: accent, fontSize: 13, fontWeight: FontWeight.w600),
                      ),
                    ),
                  ),
                  showDivider: true,
                ),
                
                // Notifications
                _buildSettingsItem(
                  icon: Icons.notifications_rounded,
                  title: isEnglish ? "Notifications" : "Bildirimler",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () {
                    HapticFeedback.lightImpact();
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (_) => const NotificationsScreen()),
                    );
                  },
                  showDivider: true,
                ),
                
                // Share app
                _buildSettingsItem(
                  icon: Icons.share_rounded,
                  title: isEnglish ? "Share App" : "Uygulamayı Paylaş",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () {
                    HapticFeedback.lightImpact();
                    final appLink = Platform.isIOS
                        ? StoreUrls.iosStoreHttps.toString()
                        : StoreUrls.androidPlayHttps.toString();
                        
                    final message = isEnglish
                        ? "Hey! Check out My Way for smart city routes and personalized travel plans: $appLink"
                        : "Hey! Akıllı şehir rotaları ve kişiselleştirilmiş seyahat planları için My Way'i incele: $appLink";
                    
                    final RenderBox? box = context.findRenderObject() as RenderBox?;
                    SharePlus.instance.share(
                      ShareParams(
                        text: message,
                        sharePositionOrigin: box != null 
                            ? box.localToGlobal(Offset.zero) & box.size 
                            : null,
                      ),
                    );
                  },
                  showDivider: true,
                ),
                
                // Rate app
                _buildSettingsItem(
                  icon: Icons.star_rounded,
                  title: isEnglish ? "Rate Us" : "Bizi Değerlendir",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () async {
                    HapticFeedback.lightImpact();
                    await StoreUrls.launchReviewPage();
                  },
                  showDivider: true,
                ),
                
                // Contact us
                _buildSettingsItem(
                  icon: Icons.mail_rounded,
                  title: isEnglish ? "Contact Us" : "Bize Ulaşın",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () {
                    HapticFeedback.lightImpact();
                    _showContactBottomSheet(isEnglish);
                  },
                  showDivider: true,
                ),
                
                // Privacy policy
                _buildSettingsItem(
                  icon: Icons.privacy_tip_rounded,
                  title: isEnglish ? "Privacy Policy" : "Gizlilik Politikası",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () async {
                    HapticFeedback.lightImpact();
                    final Uri url = Uri.parse(isEnglish 
                        ? "https://mywaytravelapp.com/privacy.html" 
                        : "https://mywaytravelapp.com/privacy-tr.html");
                    if (await canLaunchUrl(url)) {
                      await launchUrl(url);
                    }
                  },
                  showDivider: true,
                ),

                 // Terms of Use (EULA)
                _buildSettingsItem(
                  icon: Icons.description_rounded,
                  title: isEnglish ? "Terms of Use (EULA)" : "Kullanım Koşulları",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () async {
                    HapticFeedback.lightImpact();
                    final Uri url = Uri.parse("https://www.apple.com/legal/internet-services/itunes/dev/stdeula/");
                    if (await canLaunchUrl(url)) {
                      await launchUrl(url, mode: LaunchMode.externalApplication);
                    }
                  },
                  showDivider: true,
                ),

                // Restore Purchases
                _buildSettingsItem(
                  icon: Icons.restore_rounded,
                  title: isEnglish ? "Restore Purchases" : "Satın Alımları Geri Yükle",
                   trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: _restorePurchases,
                  showDivider: true,
                ),

                // FCM Token (For Testing)
                _buildSettingsItem(
                  icon: Icons.vpn_key_rounded,
                  title: isEnglish ? "Copy Push Token" : "Push Token Kopyala",
                  trailing: const Icon(Icons.copy_rounded, color: textGrey, size: 18),
                  onTap: () {
                    HapticFeedback.lightImpact();
                    final token = NotificationService().fcmToken;
                    if (token != null) {
                      Clipboard.setData(ClipboardData(text: token));
                      CustomToast.show(context, isEnglish ? "Token copied to clipboard! 📋" : "Token panoya kopyalandı! 📋");
                    } else {
                      CustomToast.show(context, isEnglish ? "Token not available yet." : "Token henüz hazır değil.", isError: true);
                    }
                  },
                  showDivider: true,
                ),

                // Manage Subscription
                _buildSettingsItem(
                  icon: Icons.subscriptions_rounded,
                  title: isEnglish ? "Manage Subscription" : "Aboneliği Yönet",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: () async {
                    HapticFeedback.lightImpact();
                    final Uri url = Uri.parse(
                      Platform.isIOS
                          ? "https://apps.apple.com/account/subscriptions"
                          : "https://play.google.com/store/account/subscriptions"
                    );
                    if (await canLaunchUrl(url)) {
                      await launchUrl(url, mode: LaunchMode.externalApplication);
                    }
                  },
                  showDivider: true,
                ),

                // Delete Account
                _buildSettingsItem(
                  icon: Icons.delete_outline_rounded,
                  title: isEnglish ? "Delete My Data & Account" : "Verilerimi ve Hesabımı Sil",
                  trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                  onTap: _deleteAccount,
                  showDivider: false,
                ),
                const SizedBox(height: 12),
              ],
            ),
          ),
          
          const SizedBox(height: 16),
          
          // Version info
          Center(
            child: Text(
              "v1.0.3",
              style: TextStyle(color: textGrey.withOpacity(0.5), fontSize: 12),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSettingsItem({
    required IconData icon,
    required String title,
    required Widget trailing,
    VoidCallback? onTap,
    bool showDivider = true,
  }) {
    return Column(
      children: [
        GestureDetector(
          onTap: onTap,
          behavior: HitTestBehavior.opaque,
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            child: Row(
              children: [
                Icon(icon, color: textGrey, size: 22),
                const SizedBox(width: 14),
                Expanded(
                  child: Text(
                    title,
                    style: const TextStyle(color: textWhite, fontSize: 15, fontWeight: FontWeight.w500),
                  ),
                ),
                trailing,
              ],
            ),
          ),
        ),
        if (showDivider)
          Divider(
            color: borderColor.withOpacity(0.3),
            height: 1,
            indent: 52,
          ),
      ],
    );
  }

  void _showContactBottomSheet(bool isEnglish) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (context) => Container(
        padding: const EdgeInsets.all(24),
        decoration: const BoxDecoration(
          color: bgDark,
          borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.3),
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 24),
            const Icon(Icons.mail_rounded, color: accent, size: 48),
            const SizedBox(height: 16),
            Text(
              isEnglish ? "Contact Us" : "Bize Ulaşın",
              style: const TextStyle(color: textWhite, fontSize: 20, fontWeight: FontWeight.w700),
            ),
            const SizedBox(height: 8),
            Text(
              isEnglish 
                  ? "Have questions or feedback? We'd love to hear from you!"
                  : "Sorularınız veya önerileriniz mi var? Sizden haber almak isteriz!",
              style: const TextStyle(color: textGrey, fontSize: 14),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 24),
            // Email Address Display
            Container(
              padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 20),
              decoration: BoxDecoration(
                color: bgCard,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: accent.withOpacity(0.2)),
              ),
              child: Text(
                "info@mywaytravelapp.com",
                style: GoogleFonts.poppins(
                  color: accentLight,
                  fontSize: 15,
                  fontWeight: FontWeight.w500,
                  letterSpacing: 0.5,
                ),
              ),
            ),
            const SizedBox(height: 20),
            GestureDetector(
              onTap: () async {
                Navigator.pop(context);
                
                final Uri emailLaunchUri = Uri(
                  scheme: 'mailto',
                  path: 'info@mywaytravelapp.com',
                  query: isEnglish 
                      ? 'subject=MyWay Support'
                      : 'subject=MyWay Destek',
                );

                if (await canLaunchUrl(emailLaunchUri)) {
                  await launchUrl(emailLaunchUri);
                } else {
                  debugPrint("Could not launch email client");
                }
              },
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 16),
                decoration: BoxDecoration(
                  color: accent,
                  borderRadius: BorderRadius.circular(14),
                  boxShadow: [
                    BoxShadow(
                      color: accent.withOpacity(0.3),
                      blurRadius: 12,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Center(
                  child: Text(
                    isEnglish ? "Send Email" : "E-posta Gönder",
                    style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w700),
                  ),
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
    );
  }


  // ══════════════════════════════════════════════════════════════════════════
  // HELPERS
  // ══════════════════════════════════════════════════════════════════════════

  Color _getCategoryColor(String category) {
    final colors = {
      'Restoran': const Color(0xFFFF5252),
      'Bar': const Color(0xFF9C27B0),
      'Kafe': const Color(0xFFFF9800),
      'Müze': const Color(0xFF2196F3),
      'Tarihi': const Color(0xFF795548),
      'Park': const Color(0xFF4CAF50),
      'Manzara': const Color(0xFF00BCD4),
      'Alışveriş': const Color(0xFFE91E63),
      'Semt': const Color(0xFF673AB7),
    };
    return colors[category] ?? const Color(0xFF607D8B);
  }

  Future<void> _editName() async {
    final controller = TextEditingController(text: _userName);

    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: bgCard,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: Text(AppLocalizations.instance.editName, style: const TextStyle(color: textWhite)),
        content: TextField(
          controller: controller,
          style: const TextStyle(color: textWhite),
          decoration: InputDecoration(
            hintText: AppLocalizations.instance.nameHint,
            hintStyle: const TextStyle(color: textGrey),
            filled: true,
            fillColor: bgCardLight,
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(12),
              borderSide: BorderSide.none,
            ),
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(AppLocalizations.instance.cancel, style: const TextStyle(color: textGrey)),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, controller.text),
            child: Text(AppLocalizations.instance.save, style: const TextStyle(color: accent)),
          ),
        ],
      ),
    );

    if (result != null && result.isNotEmpty) {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString("userName", result);
      setState(() => _userName = result);
      // Notify other screens (ExploreScreen) about name change
      TripUpdateService().notifyNameUpdated(); 
    }
  }

  Future<void> _restorePurchases() async {
     HapticFeedback.mediumImpact();
     // Show loading indicator if desired, or just toast
     try {
       final success = await PremiumService.instance.restorePurchases();
       if (mounted) {
         ScaffoldMessenger.of(context).showSnackBar(
           SnackBar(
             content: Text(success 
               ? (AppLocalizations.instance.isEnglish ? "Purchases restored successfully" : "Satın alımlar geri yüklendi")
               : (AppLocalizations.instance.isEnglish ? "No active subscription found" : "Aktif abonelik bulunamadı")
             ),
             backgroundColor: bgCardLight,
             behavior: SnackBarBehavior.floating,
             duration: const Duration(seconds: 2),
             shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
           ),
         );
       }
     } catch (e) {
       debugPrint("Restore error: $e");
       if (mounted) {
         ScaffoldMessenger.of(context).showSnackBar(
           SnackBar(content: Text("Error: $e")),
         );
       }
     }
  }


  Future<void> _deleteAccount() async {
    final isEnglish = AppLocalizations.instance.isEnglish;
   
    // Confirmation Dialog
    final confirmed = await showDialog<bool>(
      context: context,
      barrierColor: Colors.black.withOpacity(0.8), // Darker background
      builder: (context) => AlertDialog(
        backgroundColor: bgCard, // Ensure opaque background
        elevation: 24, // Add shadow for depth
        title: Row(
          children: [
            const Icon(Icons.warning_amber_rounded, color: Colors.red, size: 28),
            const SizedBox(width: 12),
            Text(
              isEnglish ? "Delete Account" : "Hesabı Sil",
              style: const TextStyle(color: textWhite),
            ),
          ],
        ),
        content: Text(
          isEnglish 
            ? "Are you sure you want to delete all your data? This action cannot be undone. All your favorites, travel history, and photos will be permanently deleted."
            : "Tüm verilerinizi silmek istediğinize emin misiniz? Bu işlem geri alınamaz. Tüm favorileriniz, seyahat geçmişiniz ve fotoğraflarınız kalıcı olarak silinecektir.",
          style: const TextStyle(color: textGrey, fontSize: 14),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(
              isEnglish ? "Cancel" : "İptal",
              style: const TextStyle(color: textGrey),
            ),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(
              isEnglish ? "Delete Forever" : "Kalıcı Olarak Sil",
              style: const TextStyle(color: Colors.red, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );

    if (confirmed == true && mounted) {
      // Show loading
      showDialog(
        context: context,
        barrierDismissible: false,
        builder: (_) => const Center(child: CircularProgressIndicator(color: Colors.red)),
      );

      try {
        // 1. Clear SharedPreferences Selectively
        final prefs = await SharedPreferences.getInstance();
        final allKeys = prefs.getKeys();
        for (String key in allKeys) {
          // 🔥 KRİTİK: Kullanım haklarını (usage_), premium durumunu (purchases_) 
          // ve onboarding/plan durumunu KORU. Diğer her şeyi (favoriler, geçmiş, tercihler) sil.
          bool shouldKeep = key.startsWith('usage_') || 
                           key.startsWith('purchases_') ||
                           key == 'onboardingCompleted' || 
                           key == 'has_created_plan';
                           
          if (!shouldKeep) {
            await prefs.remove(key);
          }
        }

        // Tercih anahtarlarını boş bırak (yeniden seçim yaptır)
        await prefs.remove('travelStyle');
        await prefs.remove('budgetLevel');
        await prefs.remove('interests');

        // 2. Clear All Memories (Service handles Disk + Memory + Notifiers)
        await MemoryService().clearAllData();

        // 3. Clear Badge Data
        await BadgeService().reset();

        // 4. Clear in-memory static caches (AI önerileri, itinerary vb.)
        // ExploreScreen.clearCaches(); // removed: method no longer exists
        TripUpdateService().notifyTripChanged();
        
        // 3. Reset App State & Navigation
        if (mounted) {
           Navigator.of(context).pop(); // Close loading
           
           Navigator.pushNamedAndRemoveUntil(
             context,
             '/onboarding',
             (route) => false,
           );
        }
        
      } catch (e) {
        if (mounted) {
          Navigator.of(context).pop(); // Close loading
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text("Error: $e")),
          );
        }
      }
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // PREFERENCES BOTTOM SHEET

  // ══════════════════════════════════════════════════════════════════════════

  void _showPreferencesBottomSheet() {
    int tripDays = 3;
    String travelStyle = _travelStyle;
    String transportMode = "Karışık";
    int walkingLevel = 1;
    List<String> selectedInterests = List.from(_interests);
    String budgetLevel = "Dengeli";

    SharedPreferences.getInstance().then((prefs) {
      final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
      tripDays = prefs.getInt("tripDays_$currentCity") ?? prefs.getInt("tripDays") ?? 3;
      travelStyle = prefs.getString("travelStyle") ?? "Lokal";
      transportMode = prefs.getString("transportMode") ?? "Karışık";
      walkingLevel = prefs.getInt("walkingLevel") ?? 1;
      selectedInterests = prefs.getStringList("interests") ?? [];
      budgetLevel = prefs.getString("budgetLevel") ?? "Dengeli";
    });

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => StatefulBuilder(
        builder: (context, setSheetState) {
          return Container(
            height: MediaQuery.of(context).size.height * 0.85,
            decoration: const BoxDecoration(
              color: bgDark,
              borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
            ),
            child: Column(
              children: [
                Container(
                  margin: const EdgeInsets.only(top: 12),
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.3),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(20),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.18),
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: Colors.white.withOpacity(0.3), width: 1.2),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.white.withOpacity(0.08),
                              blurRadius: 12,
                              spreadRadius: 1,
                            ),
                          ],
                        ),
                        child: Image.asset('assets/icons/icon_tercihler.png', width: 32, height: 32),
                      ),
                      const SizedBox(width: 14),
                      Expanded(
                        child: Text(
                          AppLocalizations.instance.editPreferences,
                          style: const TextStyle(color: textWhite, fontSize: 20, fontWeight: FontWeight.w700),
                        ),
                      ),
                      GestureDetector(
                        onTap: () => Navigator.pop(context),
                        child: Container(
                          padding: const EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            color: bgCard,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: const Icon(Icons.close, color: textGrey, size: 20),
                        ),
                      ),
                    ],
                  ),
                ),
                Expanded(
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.symmetric(horizontal: 20),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        // Trip Days
                        _preferenceSection(
                          iconAsset: 'assets/icons/icon_calender.png',
                          title: AppLocalizations.instance.howManyDays,
                          child: Column(
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Text(AppLocalizations.instance.nDays(tripDays), 
                                       style: const TextStyle(color: accent, fontSize: 18, fontWeight: FontWeight.w600)),
                                ],
                              ),
                              const SizedBox(height: 8),
                              SliderTheme(
                                data: SliderThemeData(
                                  activeTrackColor: accent,
                                  inactiveTrackColor: bgCardLight,
                                  thumbColor: Colors.white,
                                  overlayColor: accent.withOpacity(0.2),
                                ),
                                child: Slider(
                                  value: tripDays.toDouble(),
                                  min: 1,
                                  max: 14,
                                  divisions: 13,
                                  onChanged: (v) => setSheetState(() => tripDays = v.toInt()),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const SizedBox(height: 16),

                        // Travel Style
                        _preferenceSection(
                          iconAsset: 'assets/icons/icon_Style.png',
                          title: AppLocalizations.instance.travelStyleTitle,
                          child: Wrap(
                            spacing: 10,
                            runSpacing: 10,
                            children: ["Turistik", "Yerel", "Maceracı", "Kültürel"].map((style) {
                              final isSelected = travelStyle == style;
                              return GestureDetector(
                                onTap: () => setSheetState(() => travelStyle = style),
                                child: Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                                  decoration: BoxDecoration(
                                    color: isSelected ? accent : bgCard,
                                    borderRadius: BorderRadius.circular(12),
                                    border: Border.all(color: isSelected ? accent : borderColor),
                                  ),
                                  child: Text(
                                    AppLocalizations.instance.translateTravelStyle(style),
                                    style: TextStyle(color: isSelected ? Colors.white : textGrey, fontWeight: FontWeight.w500),
                                  ),
                                ),
                              );
                            }).toList(),
                          ),
                        ),
                        const SizedBox(height: 16),

                        // Interests
                        _preferenceSection(
                          iconAsset: 'assets/icons/icon_interest.png',
                          title: AppLocalizations.instance.interestsTitle,
                          child: Wrap(
                            spacing: 8,
                            runSpacing: 8,
                            children: [
                              "Yemek", "Kahve", "Sanat", "Tarih", "Doğa", "Gece", 
                              "Alışveriş", "Fotoğraf", "Mimari", "Plaj", "Spor", "Müze", "Yerel Lezzetler"
                            ].map((interest) {
                              final isSelected = selectedInterests.contains(interest);
                              return GestureDetector(
                                onTap: () {
                                  setSheetState(() {
                                    if (isSelected) {
                                      selectedInterests.remove(interest);
                                    } else {
                                      selectedInterests.add(interest);
                                    }
                                  });
                                },
                                child: Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                                  decoration: BoxDecoration(
                                    color: isSelected ? accent : bgCard,
                                    borderRadius: BorderRadius.circular(20),
                                    border: Border.all(color: isSelected ? accent : borderColor),
                                  ),
                                  child: Text(
                                    AppLocalizations.instance.translateInterest(interest),
                                    style: TextStyle(color: isSelected ? Colors.white : textGrey, fontSize: 13),
                                  ),
                                ),
                              );
                            }).toList(),
                          ),
                        ),
                        const SizedBox(height: 16),

                        // Budget
                        _preferenceSection(
                          iconAsset: 'assets/icons/icon_wallet.png',
                          title: AppLocalizations.instance.budgetPreference,
                          child: Row(
                            children: ["Ekonomik", "Dengeli", "Premium"].map((budget) {
                              final isSelected = budgetLevel == budget;
                              
                              String displayText = budget;
                              if (budget == "Ekonomik") displayText = AppLocalizations.instance.budgetEconomy;
                              else if (budget == "Dengeli") displayText = AppLocalizations.instance.budgetBalanced;
                              else if (budget == "Premium") displayText = AppLocalizations.instance.budgetPremium;
                              
                              return Expanded(
                                child: GestureDetector(
                                  onTap: () => setSheetState(() => budgetLevel = budget),
                                  child: Container(
                                    margin: EdgeInsets.only(right: budget != "Premium" ? 10 : 0),
                                    padding: const EdgeInsets.symmetric(vertical: 14),
                                    decoration: BoxDecoration(
                                      color: isSelected ? accent : bgCard,
                                      borderRadius: BorderRadius.circular(12),
                                      border: Border.all(color: isSelected ? accent : borderColor),
                                    ),
                                    child: Center(
                                      child: Text(displayText, style: TextStyle(color: isSelected ? Colors.white : textGrey, fontWeight: FontWeight.w500, fontSize: 13)),
                                    ),
                                  ),
                                ),
                              );
                            }).toList(),
                          ),
                        ),
                        const SizedBox(height: 16),

                        const SizedBox(height: 30),
                      ],
                    ),
                  ),
                ),
                // Save button
                Container(
                  padding: const EdgeInsets.fromLTRB(20, 12, 20, 30),
                  decoration: BoxDecoration(
                    color: bgDark,
                    border: Border(top: BorderSide(color: borderColor.withOpacity(0.3))),
                  ),
                  child: GestureDetector(
                    onTap: () async {
                      final prefs = await SharedPreferences.getInstance();
                      await prefs.setBool("preferences_onboarding_shown", true);
                      final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
                      await prefs.setInt("tripDays_$currentCity", tripDays);
                      await prefs.setString("travelStyle", travelStyle);
                      await prefs.setString("transportMode", transportMode);
                      await prefs.setInt("walkingLevel", walkingLevel);
                      await prefs.setStringList("interests", selectedInterests);
                      await prefs.setString("budgetLevel", budgetLevel);
                      
                      if (mounted) {
                        Navigator.pop(context);
                        _loadData();
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(
                            content: Text(AppLocalizations.instance.preferencesSaved),
                            backgroundColor: bgCardLight,
                            behavior: SnackBarBehavior.floating,
                            duration: const Duration(milliseconds: 1200),
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10)),
                          ),
                        );
                      }
                    },
                    child: Container(
                      width: double.infinity,
                      padding: const EdgeInsets.symmetric(vertical: 16),
                      decoration: BoxDecoration(
                        gradient: primaryGradient,
                        borderRadius: BorderRadius.circular(14),
                        boxShadow: [
                          BoxShadow(
                            color: accent.withOpacity(0.4),
                            blurRadius: 16,
                            offset: const Offset(0, 6),
                          ),
                        ],
                      ),
                      child: Center(
                        child: Text(
                          AppLocalizations.instance.save,
                          style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.w700),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          );
        },
      ),
    );
  }





  Widget _preferenceSection({
    required String iconAsset,
    required String title,
    required Widget child,
  }) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Image.asset(iconAsset, width: 24, height: 24),
              const SizedBox(width: 10),
              Text(title, style: const TextStyle(color: textWhite, fontSize: 15, fontWeight: FontWeight.w600)),
            ],
          ),
          const SizedBox(height: 14),
          child,
        ],
      ),
    );
  }
}

extension StringExtension on String {
  String capitalize() {
    if (isEmpty) return this;
    return '${this[0].toUpperCase()}${substring(1)}';
  }
}

/// Badge item widget - displays a single city badge with icon
class _BadgeItem extends StatelessWidget {
  final CityBadge badge;

  const _BadgeItem({required this.badge});

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        // Badge Circle with Icon
        Stack(
          alignment: Alignment.topRight,
          children: [
            Container(
              width: 60,
              height: 60,
              decoration: BoxDecoration(
                color: badge.isUnlocked 
                    ? badge.color 
                    : badge.color.withOpacity(0.3),
                shape: BoxShape.circle,
                boxShadow: badge.isUnlocked
                    ? [
                        BoxShadow(
                          color: badge.color.withOpacity(0.4),
                          blurRadius: 8,
                          offset: const Offset(0, 3),
                        )
                      ]
                    : [],
              ),
              child: badge.hasImage
                  ? ClipOval(
                      child: Image.asset(
                        badge.imagePath!,
                        width: 60,
                        height: 60,
                        fit: BoxFit.cover,
                        color: badge.isUnlocked ? null : Colors.white.withOpacity(0.3),
                        colorBlendMode: badge.isUnlocked ? null : BlendMode.modulate,
                      ),
                    )
                  : Center(
                      child: Icon(
                        badge.icon,
                        color: badge.isUnlocked ? Colors.white : Colors.white38,
                        size: 26,
                      ),
                    ),

            ),
            // Gold dot for unlocked badges
            if (badge.isUnlocked)
              Positioned(
                top: 2,
                right: 2,
                child: Container(
                  width: 12,
                  height: 12,
                  decoration: BoxDecoration(
                    color: const Color(0xFFFFD700),
                    shape: BoxShape.circle,
                    border: Border.all(color: const Color(0xFF1C1C2E), width: 2),
                  ),
                ),
              ),
          ],
        ),
        const SizedBox(height: 8),
        // City Name
        Text(
          badge.name,
          style: TextStyle(
            fontWeight: badge.isUnlocked ? FontWeight.bold : FontWeight.normal,
            fontSize: 11,
            color: badge.isUnlocked ? Colors.white : Colors.white54,
          ),
          textAlign: TextAlign.center,
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
        ),
        const SizedBox(height: 2),
        // Subtitle
        Text(
          badge.subtitle,
          style: TextStyle(
            fontSize: 9,
            color: badge.isUnlocked 
                ? const Color(0xFF9CA3AF) 
                : const Color(0xFF9CA3AF).withOpacity(0.5),
          ),
          textAlign: TextAlign.center,
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
        ),
      ],
    );
  }
}

class _CityTripDetailSheet extends StatelessWidget {
  final Map<String, dynamic> trip;
  final VoidCallback onNavigateToPlan;
  final Widget Function(Highlight, {bool isVisited}) buildPlaceCard;

  const _CityTripDetailSheet({
    required this.trip,
    required this.onNavigateToPlan,
    required this.buildPlaceCard,
  });

  @override
  Widget build(BuildContext context) {
    final cityName = trip['cityName'] as String;
    final heroImage = trip['heroImage'] as String?;
    final totalDays = trip['totalDays'] as int;
    final totalPlaces = trip['totalPlaces'] as int;
    final favorites = trip['favorites'] as List<Highlight>? ?? [];
    final visited = trip['visited'] as List<Highlight>? ?? [];
    final routes = trip['routes'] as List<CompletedRoute>? ?? [];
    final scheduleJson = trip['scheduleJson'] as String?;
    final isAiPlan = trip['isAiPlan'] as bool? ?? false;
    final isEn = AppLocalizations.instance.isEnglish;

    return Container(
      height: MediaQuery.of(context).size.height * 0.88,
      decoration: const BoxDecoration(
        color: WanderlustColors.bgDark,
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: Column(
        children: [
          // Drag handle
          Center(
            child: Container(
              margin: const EdgeInsets.only(top: 12, bottom: 8),
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: WanderlustColors.textGrey.withValues(alpha: 0.3),
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
          
          // Header with City Hero Image
          Container(
            height: 140,
            width: double.infinity,
            margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(24),
              color: WanderlustColors.bgCardLight,
            ),
            clipBehavior: Clip.hardEdge,
            child: Stack(
              children: [
                _ProfileScreenState._citiesWithIcons.contains(trip['cityId'])
                    ? Image.asset(
                        'assets/icons/${trip['cityId']}_icon.png',
                        width: double.infinity,
                        height: 140,
                        fit: BoxFit.cover,
                      )
                    : (heroImage != null && heroImage.isNotEmpty
                        ? ResilientNetworkImage(
                            imageUrl: heroImage,
                            placeName: cityName,
                            city: trip['cityId'],
                            category: 'city',
                            width: double.infinity,
                            height: 140,
                            fit: BoxFit.cover,
                          )
                        : const SizedBox.shrink()),
                Container(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.transparent,
                        Colors.black.withValues(alpha: 0.8),
                      ],
                    ),
                  ),
                ),
                Positioned(
                  bottom: 16,
                  left: 20,
                  right: 20,
                  child: Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Text(
                              cityName,
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 28,
                                fontWeight: FontWeight.w900,
                              ),
                            ),
                            if (totalDays > 0)
                              Text(
                                isEn ? "$totalDays days • $totalPlaces places" : "$totalDays gün • $totalPlaces mekan",
                                style: TextStyle(color: Colors.white.withValues(alpha: 0.8), fontSize: 14),
                              ),
                          ],
                        ),
                      ),
                      // AI Plan badge removed
                    ],
                  ),
                ),
              ],
            ),
          ),

          // Body
          Expanded(
            child: ListView(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              children: [
                // 1. Günlük Planım
                _buildSectionHeader('assets/icons/icon_gunluk.png', isEn ? "My Daily Plan" : "Günlük Planım"),
                const SizedBox(height: 12),
                if (totalPlaces > 0 && scheduleJson != null) ...[
                  _buildSchedulePreview(context, scheduleJson, isEn, isAiPlan),
                  const SizedBox(height: 12),
                  InkWell(
                    onTap: () {
                      Navigator.pop(context);
                      onNavigateToPlan();
                    },
                    borderRadius: BorderRadius.circular(16),
                    child: Container(
                      width: double.infinity,
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      decoration: BoxDecoration(
                        color: WanderlustColors.bgCardLight,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(color: WanderlustColors.borderLight),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Image.asset(
                            'assets/icons/icon_map.png',
                            width: 22,
                            height: 22,
                          ),
                          const SizedBox(width: 8),
                          Text(
                            isEn ? "View / Edit in Route Builder" : "Rota Oluşturucuda Görüntüle / Düzenle",
                            style: const TextStyle(
                              color: WanderlustColors.textWhite,
                              fontWeight: FontWeight.w600,
                              fontSize: 14,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ] else ...[
                  Container(
                    padding: const EdgeInsets.all(24),
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard,
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: WanderlustColors.borderLight),
                    ),
                    child: Column(
                      children: [
                        Opacity(
                          opacity: 0.6,
                          child: Image.asset('assets/icons/icon_gunluk.png', width: 44, height: 44),
                        ),
                        const SizedBox(height: 12),
                        Text(
                          isEn ? "No daily plan created for this city yet." : "Bu şehir için henüz günlük gezi planı oluşturulmadı.",
                          textAlign: TextAlign.center,
                          style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 14),
                        ),
                        const SizedBox(height: 16),
                        ElevatedButton.icon(
                          onPressed: () {
                            Navigator.pop(context);
                            onNavigateToPlan();
                          },
                          style: ElevatedButton.styleFrom(
                            backgroundColor: WanderlustColors.accent,
                            foregroundColor: Colors.white,
                            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                          ),
                          icon: const Icon(Icons.add, size: 18),
                          label: Text(isEn ? "Create Plan" : "Plan Oluştur", style: const TextStyle(fontWeight: FontWeight.bold)),
                        ),
                      ],
                    ),
                  ),
                ],

                const SizedBox(height: 28),

                // 2. Favorilerim
                _buildSectionHeader('assets/icons/icon_interest.png', "${isEn ? 'My Favorites' : 'Favorilerim'} (${favorites.length})"),
                const SizedBox(height: 12),
                if (favorites.isNotEmpty) ...[
                  ...favorites.map((h) => buildPlaceCard(h)),
                ] else ...[
                  _buildEmptyState('assets/icons/icon_interest.png', isEn ? "No favorites in this city yet." : "Bu şehirde henüz favori mekanınız yok."),
                ],

                const SizedBox(height: 28),

                // 3. Ziyaret Ettiklerim
                _buildSectionHeader('assets/icons/icon_complete.png', "${isEn ? 'Visited Places' : 'Ziyaret Ettiklerim'} (${visited.length})"),
                const SizedBox(height: 12),
                if (visited.isNotEmpty) ...[
                  ...visited.map((h) => buildPlaceCard(h, isVisited: true)),
                ] else ...[
                  _buildEmptyState('assets/icons/icon_complete.png', isEn ? "No visited places in this city yet." : "Bu şehirde henüz ziyaret işaretlediğiniz mekan yok."),
                ],

                const SizedBox(height: 28),

                // 4. Tamamlanan Rotalarım
                _buildSectionHeader('assets/icons/icon_renkli_routes.png', "${isEn ? 'Completed Routes' : 'Tamamlanan Rotalar'} (${routes.length})"),
                const SizedBox(height: 12),
                if (routes.isNotEmpty) ...[
                  ...routes.map((r) => _buildRouteItem(context, r, isEn)),
                ] else ...[
                  _buildEmptyState('assets/icons/icon_renkli_routes.png', isEn ? "No completed routes in this city yet." : "Bu şehirde henüz tamamladığınız bir gezi rotası yok."),
                ],
                const SizedBox(height: 40),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSectionHeader(String iconAsset, String title) {
    return Row(
      children: [
        Image.asset(iconAsset, width: 26, height: 26),
        const SizedBox(width: 10),
        Expanded(
          child: Text(
            title,
            style: const TextStyle(color: WanderlustColors.textWhite, fontSize: 18, fontWeight: FontWeight.bold),
          ),
        ),
      ],
    );
  }

  Widget _buildEmptyState(String iconAsset, String message) {
    return Container(
      padding: const EdgeInsets.symmetric(vertical: 24, horizontal: 16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard.withValues(alpha: 0.5),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight.withValues(alpha: 0.5)),
      ),
      child: Center(
        child: Column(
          children: [
            Opacity(
              opacity: 0.6,
              child: Image.asset(iconAsset, width: 36, height: 36),
            ),
            const SizedBox(height: 10),
            Text(message, textAlign: TextAlign.center, style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13)),
          ],
        ),
      ),
    );
  }

  Widget _buildSchedulePreview(BuildContext context, String jsonStr, bool isEn, bool isAiPlan) {
    try {
      final schedule = jsonDecode(jsonStr) as Map<String, dynamic>;
      final days = schedule.entries.where((e) => e.key != "0" && (e.value as List).isNotEmpty).toList();
      days.sort((a, b) => int.parse(a.key).compareTo(int.parse(b.key)));

      return ListenableBuilder(
        listenable: PremiumService.instance,
        builder: (context, _) {
          final lockActive = !PremiumService.instance.isPremium && isAiPlan;

          final unlockedDays = <MapEntry<String, dynamic>>[];
          final lockedDays = <MapEntry<String, dynamic>>[];
          for (final day in days) {
            final dayInt = int.tryParse(day.key) ?? 1;
            if (lockActive && dayInt > 1) {
              lockedDays.add(day);
            } else {
              unlockedDays.add(day);
            }
          }

          return Column(
            children: [
              ...unlockedDays.map(
                (day) => _buildScheduleDayCard(day.key, day.value as List<dynamic>, isEn),
              ),
              if (lockedDays.isNotEmpty) _buildLockedDaysSection(context, lockedDays, isEn),
            ],
          );
        },
      );
    } catch (_) {
      return const SizedBox.shrink();
    }
  }

  Widget _buildScheduleDayCard(String dayNum, List<dynamic> places, bool isEn) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: WanderlustColors.accent.withValues(alpha: 0.2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  isEn ? "Day $dayNum" : "$dayNum. Gün",
                  style: const TextStyle(color: WanderlustColors.accent, fontWeight: FontWeight.bold, fontSize: 13),
                ),
              ),
              const Spacer(),
              Text("${places.length} ${isEn ? 'stops' : 'durak'}", style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 12)),
            ],
          ),
          const SizedBox(height: 12),
          ...places.map((p) {
            final name = p['name'] as String? ?? "";
            return Padding(
              padding: const EdgeInsets.only(bottom: 6),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.center,
                children: [
                  const Icon(Icons.circle, color: WanderlustColors.accent, size: 6),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(name, style: const TextStyle(color: WanderlustColors.textWhite, fontSize: 14)),
                  ),
                ],
              ),
            );
          }),
        ],
      ),
    );
  }

  /// PRO olmayan kullanıcılar için 2. gün ve sonrasını tek bir buzlu cam alanında
  /// kilitler. Routes ekranındaki "Plan Kilitli" overlay'i ile aynı stildedir.
  Widget _buildLockedDaysSection(BuildContext context, List<MapEntry<String, dynamic>> lockedDays, bool isEn) {
    return Stack(
      children: [
        // Teaser: kilitli günler arkada (etkileşimsiz)
        IgnorePointer(
          child: Column(
            children: lockedDays
                .map((day) => _buildScheduleDayCard(day.key, day.value as List<dynamic>, isEn))
                .toList(),
          ),
        ),
        // Buzlu cam katmanı
        Positioned.fill(
          child: ClipRRect(
            borderRadius: BorderRadius.circular(16),
            child: BackdropFilter(
              filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
              child: Container(color: Colors.white.withOpacity(0.15)),
            ),
          ),
        ),
        // Paywall içeriği
        Positioned.fill(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.lock_rounded, color: Colors.black.withOpacity(0.7), size: 48),
                  const SizedBox(height: 16),
                  Text(
                    isEn ? "Plan Locked" : "Plan Kilitli",
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 18,
                      color: Colors.black.withOpacity(0.85),
                      letterSpacing: 0.2,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    isEn
                        ? "Unlock your full personalized itinerary and smart recommendations."
                        : "Kişiselleştirilmiş rotanıza ve akıllı önerilere sınırsız erişin.",
                    style: const TextStyle(
                      color: WanderlustColors.textGrey,
                      fontSize: 14,
                      height: 1.5,
                      fontWeight: FontWeight.w500,
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 20),
                  GestureDetector(
                    onTap: () => showPaywall(context, source: 'profile_pro_badge', onSubscribe: (_) {}),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
                      decoration: BoxDecoration(
                        color: WanderlustColors.accent,
                        borderRadius: BorderRadius.circular(24),
                      ),
                      child: Text(
                        isEn ? "Try PRO" : "PRO'yu Dene",
                        style: const TextStyle(
                          fontWeight: FontWeight.w700,
                          fontSize: 14,
                          color: Colors.white,
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildRouteItem(BuildContext context, CompletedRoute route, bool isEn) {
    return GestureDetector(
      onTap: () => _showCompletedRouteDetails(context, route, isEn),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: WanderlustColors.bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: WanderlustColors.borderLight),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: WanderlustColors.accent.withValues(alpha: 0.15),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Image.asset('assets/icons/icon_renkli_routes.png', width: 28, height: 28),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    route.name,
                    style: const TextStyle(color: WanderlustColors.textWhite, fontSize: 16, fontWeight: FontWeight.bold),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    "${route.stopCount} ${isEn ? 'stops' : 'durak'} • ${route.date.day}.${route.date.month}.${route.date.year}",
                    style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                  ),
                ],
              ),
            ),
            const Icon(Icons.chevron_right_rounded, color: WanderlustColors.textGrey, size: 20),
          ],
        ),
      ),
    );
  }

  void _showCompletedRouteDetails(BuildContext context, CompletedRoute route, bool isEn) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: WanderlustColors.bgCard,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        title: Row(
          children: [
            Image.asset('assets/icons/icon_renkli_routes.png', width: 28, height: 28),
            const SizedBox(width: 10),
            Expanded(
              child: Text(route.name, style: const TextStyle(color: WanderlustColors.textWhite, fontWeight: FontWeight.bold, fontSize: 18)),
            ),
          ],
        ),
        content: SizedBox(
          width: double.maxFinite,
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                isEn ? "Route Stops:" : "Rota Durakları:",
                style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 14, fontWeight: FontWeight.w600),
              ),
              const SizedBox(height: 12),
              Flexible(
                child: ListView.builder(
                  shrinkWrap: true,
                  itemCount: route.placeNames.length,
                  itemBuilder: (context, idx) {
                    return Padding(
                      padding: const EdgeInsets.symmetric(vertical: 8),
                      child: Row(
                        children: [
                          Container(
                            width: 26,
                            height: 26,
                            decoration: BoxDecoration(
                              color: WanderlustColors.accent.withValues(alpha: 0.2),
                              shape: BoxShape.circle,
                              border: Border.all(color: WanderlustColors.accent),
                            ),
                            child: Center(
                              child: Text(
                                "${idx + 1}",
                                style: const TextStyle(color: WanderlustColors.accent, fontSize: 12, fontWeight: FontWeight.bold),
                              ),
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Text(
                              route.placeNames[idx],
                              style: const TextStyle(color: WanderlustColors.textWhite, fontSize: 15),
                            ),
                          ),
                        ],
                      ),
                    );
                  },
                ),
              ),
            ],
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text(isEn ? "Close" : "Kapat", style: const TextStyle(color: WanderlustColors.accent, fontWeight: FontWeight.bold)),
          ),
        ],
      ),
    );
  }
}
