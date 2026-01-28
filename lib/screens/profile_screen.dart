// =============================================================================
// PROFILE SCREEN – AIRBNB-INSPIRED WITH BADGE SYSTEM
// User profile with stats, badges, travel history, and settings
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:ui';
import 'dart:io';
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
import 'notifications_screen.dart';
import '../widgets/add_memory_sheet.dart';
import '../services/premium_service.dart';
import 'paywall_screen.dart';
import 'city_switcher_screen.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../widgets/tutorial_overlay_widget.dart';

class ProfileScreen extends StatefulWidget {
  final bool isVisible;
  const ProfileScreen({super.key, this.isVisible = false});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen>
    with SingleTickerProviderStateMixin {
  // ══════════════════════════════════════════════════════════════════════════
  // AMBER/GOLD THEME
  // ══════════════════════════════════════════════════════════════════════════

  static const Color bgDark = WanderlustColors.bgDark;
  static const Color bgCard = WanderlustColors.bgCard;
  static const Color bgCardLight = WanderlustColors.bgCardLight;
  static const Color accent = WanderlustColors.accent;
  static const Color accentLight = WanderlustColors.accentLight;
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [WanderlustColors.accent, WanderlustColors.accentLight],
  );

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  String _userName = "Gezgin";
  String _travelStyle = "Lokal";
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
  
  late TabController _tabController;
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
    _tabController = TabController(length: 3, vsync: this);
    _tabController.addListener(() {
      if (mounted) setState(() {});
    });
    
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
    TripUpdateService().favoritesUpdated.addListener(_loadData);
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
    // Tutorial triggering is controlled, not automatic
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _loadData();
  }

  @override
  void dispose() {
    TripUpdateService().visitUpdated.removeListener(_onVisitUpdated);
    TripUpdateService().tripUpdated.removeListener(_loadData);
    TripUpdateService().favoritesUpdated.removeListener(_loadData);
    _tabController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DATA LOADING
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();

    // Load user name - if not set, it will be empty and handled in build method
    _userName = prefs.getString("user_name") ?? "";
    _travelStyle = prefs.getString("travelStyle") ?? "Lokal";
    _interests = prefs.getStringList("interests") ?? [];
    _favorites = prefs.getStringList("favorite_places") ?? [];
    _visitedPlaces = prefs.getStringList("visited_places") ?? [];
    _tripPlaces = prefs.getStringList("trip_places") ?? [];
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

          // Tab Bar (Favorites/Visited)
          SliverToBoxAdapter(child: _buildTabBar()),

          // Tab Content (inline, scrolls with page)
          SliverToBoxAdapter(
            child: AnimatedSwitcher(
              duration: const Duration(milliseconds: 200),
              child: _tabController.index == 0 
                  ? _buildFavoritesContent() 
                  : _tabController.index == 1
                      ? _buildVisitedContent()
                      : _buildHistoryContent(),
            ),
          ),

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
                                    _userName.isNotEmpty 
                                        ? _userName[0].toUpperCase() 
                                        : (isEnglish ? "E" : "G"),
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
                              value: _favorites.length.toString(),
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
                      const Icon(Icons.photo_album_rounded, color: WanderlustColors.accent, size: 22),
                      const SizedBox(width: 10),
                      Text(
                        isEnglish ? "My Memories" : "Anılarım",
                        style: const TextStyle(
                          color: Colors.white,
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
                            child: const Icon(
                              Icons.add_a_photo_rounded,
                              color: WanderlustColors.accent,
                              size: 28,
                            ),
                          ),
                          const SizedBox(height: 8),
                          Text(
                            isEnglish ? "Add your first memory" : "İlk anını ekle",
                            style: const TextStyle(color: Colors.white70, fontSize: 13),
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

  void _addNewMemory(bool isPremium) async {
    HapticFeedback.mediumImpact();
    
    if (!isPremium) {
      // Show paywall
      showPaywall(
        context,
        onDismiss: () => Navigator.pop(context),
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
              icon: Icons.location_city_rounded,
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
              icon: Icons.tune_rounded,
              title: AppLocalizations.instance.t("Tercihler", "Preferences"),
              subtitle: AppLocalizations.instance.translateTravelStyle(_travelStyle),
              onTap: _showPreferencesBottomSheet,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildActionCard({
    required IconData icon,
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
              child: Icon(icon, color: accent, size: 20),
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
  // TAB BAR & LISTS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTabBar() {
    return Container(
      margin: const EdgeInsets.fromLTRB(24, 24, 24, 0),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
      ),
      child: TabBar(
        controller: _tabController,
        indicator: BoxDecoration(
          color: accent,
          borderRadius: BorderRadius.circular(12),
        ),
        indicatorSize: TabBarIndicatorSize.tab,
        indicatorPadding: const EdgeInsets.all(4),
        dividerColor: Colors.transparent,
        labelColor: Colors.white,
        unselectedLabelColor: textGrey,
        labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
        tabs: [
          Tab(text: "${AppLocalizations.instance.favorites} (${_favorites.length})"),
          Tab(text: "${AppLocalizations.instance.visited} (${_visitedPlaces.length})"),
          Tab(text: "${AppLocalizations.instance.isEnglish ? 'Routes' : 'Rotalar'} (${_completedRoutes.length})"),
        ],
      ),
    );
  }

  Widget _buildFavoritesContent() {
    if (_favoriteHighlights.isEmpty) {
      return _buildEmptyTab(
        icon: Icons.favorite_border,
        title: AppLocalizations.instance.t("Henüz favori yok", "No favorites yet"),
        subtitle: AppLocalizations.instance.t("Beğendiğin yerleri favorilere ekle", "Add places you like to favorites"),
      );
    }

    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
      child: Column(
        key: const ValueKey('favorites'),
        children: _favoriteHighlights.map((h) => _buildPlaceCard(h)).toList(),
      ),
    );
  }

  Widget _buildVisitedContent() {
    if (_visitedHighlights.isEmpty) {
      return _buildEmptyTab(
        icon: Icons.check_circle_outline,
        title: AppLocalizations.instance.t("Henüz ziyaret yok", "No visits yet"),
        subtitle: AppLocalizations.instance.t("Gittiğin yerleri işaretle", "Mark places you've visited"),
      );
    }

    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
      child: Column(
        key: const ValueKey('visited'),
        children: _visitedHighlights.map((h) => _buildPlaceCard(h, isVisited: true)).toList(),
      ),
    );
  }

  Widget _buildHistoryContent() {
    if (_completedRoutes.isEmpty) {
      return _buildEmptyTab(
        icon: Icons.history_rounded,
        title: AppLocalizations.instance.isEnglish ? "No route history" : "Henüz geçmiş rota yok",
        subtitle: AppLocalizations.instance.isEnglish ? "Complete a route to see it here" : "Burada görmek için bir rota tamamla",
      );
    }

    return Padding(
      padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
      child: Column(
        key: const ValueKey('history'),
        children: _completedRoutes.map((route) => _buildHistoryCard(route)).toList(),
      ),
    );
  }

  Widget _buildHistoryCard(CompletedRoute route) {
    return GestureDetector(
      onTap: () => _showHistoryDetails(route),
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: accent.withOpacity(0.15),
                borderRadius: BorderRadius.circular(12),
              ),
              child: const Icon(Icons.map_outlined, color: accent, size: 24),
            ),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    route.name,
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 15, // 16 -> 15 (sığması için)
                      fontWeight: FontWeight.w600,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Text(
                        "${route.cityName} • ${route.stopCount} ${AppLocalizations.instance.isEnglish ? 'stops' : 'durak'}",
                        style: TextStyle(color: textGrey.withOpacity(0.8), fontSize: 13),
                      ),
                    ],
                  ),
                  const SizedBox(height: 2),
                  Text(
                    "${route.date.day}.${route.date.month}.${route.date.year}",
                    style: TextStyle(color: textGrey.withOpacity(0.6), fontSize: 12),
                  ),
                ],
              ),
            ),
            const Icon(Icons.chevron_right, color: textGrey, size: 20),
          ],
        ),
      ),
    );
  }

  void _showHistoryDetails(CompletedRoute route) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => Container(
        height: MediaQuery.of(context).size.height * 0.7,
        decoration: const BoxDecoration(
          color: bgDark,
          borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Handle
            Center(
              child: Container(
                margin: const EdgeInsets.only(top: 12, bottom: 20),
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
            ),
            
            // Header
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              child: Row(
                children: [
                   Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: accent.withOpacity(0.15),
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: const Icon(Icons.check_circle, color: accent, size: 28),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          route.name,
                          style: const TextStyle(color: textWhite, fontSize: 20, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          "${route.cityName} • ${route.date.day}.${route.date.month}.${route.date.year}",
                          style: const TextStyle(color: textGrey, fontSize: 14),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
            
            const SizedBox(height: 24),
            const Padding(
              padding: EdgeInsets.symmetric(horizontal: 24),
              child: Divider(color: borderColor),
            ),
            const SizedBox(height: 16),
            
            // Stops List (with FutureBuilder for images)
            Expanded(
              child: FutureBuilder<CityModel>(
                future: CityDataLoader.loadCity(route.cityName),
                builder: (context, snapshot) {
                  if (snapshot.connectionState == ConnectionState.waiting) {
                    return const Center(child: CircularProgressIndicator(color: accent));
                  }
                  
                  final cityHighlights = snapshot.data?.highlights ?? [];
                  
                  return ListView.builder(
                    padding: const EdgeInsets.symmetric(horizontal: 24),
                    itemCount: route.placeNames.length,
                    itemBuilder: (context, index) {
                      final placeName = route.placeNames[index];
                      // Find highlight object if available
                      Highlight? place;
                      try {
                        place = cityHighlights.firstWhere((h) => h.name == placeName);
                      } catch (_) {
                        // Not found
                      }

                      return Padding(
                        padding: const EdgeInsets.only(bottom: 16),
                        child: place != null 
                          ? _buildHistoryPlaceCard(place, index) 
                          : _buildSimpleHistoryRow(placeName, index, isLast: index == route.placeNames.length - 1),
                      );
                    },
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHistoryPlaceCard(Highlight place, int index) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);
    
    return Container(
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Row(
        children: [
          // Resim + Badge
          Stack(
            clipBehavior: Clip.none,
            children: [
              ClipRRect(
                borderRadius: BorderRadius.circular(10),
                child: SizedBox(
                   width: 56,
                   height: 56,
                   child: hasImage
                       ? Image.network(
                           place.imageUrl!,
                           fit: BoxFit.cover,
                           errorBuilder: (_, __, ___) => Container(
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
              // Number Badge (-1, -1 offset so it hangs off the corner slightly)
              Positioned(
                top: -4,
                left: -4,
                child: Container(
                  width: 22,
                  height: 22,
                  decoration: BoxDecoration(
                    color: accent,
                    shape: BoxShape.circle,
                    border: Border.all(color: bgCard, width: 2),
                    boxShadow: [
                      BoxShadow(color: Colors.black.withOpacity(0.2), blurRadius: 4),
                    ],
                  ),
                  child: Center(
                    child: Text(
                      String.fromCharCode('A'.codeUnitAt(0) + index),
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ),
              ),
            ],
          ),
          
          const SizedBox(width: 12),
          
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  place.getLocalizedName(AppLocalizations.instance.isEnglish),
                  style: const TextStyle(
                    color: textWhite,
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                const SizedBox(height: 4),
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                      decoration: BoxDecoration(
                        color: bgCardLight,
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Text(
                        place.category,
                        style: TextStyle(
                          color: textGrey.withOpacity(0.9),
                          fontSize: 10,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    if (place.area.isNotEmpty)
                      Expanded(
                        child: Text(
                          place.area,
                          style: TextStyle(color: textGrey.withOpacity(0.7), fontSize: 11),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                  ],
                ),
              ],
            ),
          ),
          
          // Go to details
          GestureDetector(
             onTap: () => Navigator.push(
               context,
               MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
             ), 
             child: const Padding(
               padding: EdgeInsets.all(4.0),
               child: Icon(Icons.chevron_right, color: textGrey, size: 20),
             ),
          ),
        ],
      ),
    );
  }

  Widget _buildSimpleHistoryRow(String placeName, int index, {required bool isLast}) {
     return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Column(
          children: [
            Container(
              width: 24,
              height: 24,
              decoration: BoxDecoration(
                color: bgCardLight,
                shape: BoxShape.circle,
                border: Border.all(color: accent.withOpacity(0.5), width: 2),
              ),
              child: Center(
                child: Text(
                  String.fromCharCode('A'.codeUnitAt(0) + index),
                  style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.bold),
                ),
              ),
            ),
            if (!isLast)
              Container(
                width: 2,
                height: 30,
                color: borderColor,
                margin: const EdgeInsets.only(top: 4),
              ),
          ],
        ),
        const SizedBox(width: 16),
        Expanded(
          child: Text(
            placeName,
            style: const TextStyle(color: textWhite, fontSize: 16, fontWeight: FontWeight.w500),
          ),
        ),
      ],
    );
  }

  Widget _buildPlaceCard(Highlight place, {bool isVisited = false}) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);

    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
      ),
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(12),
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
                width: 56,
                height: 56,
                child: hasImage
                    ? Image.network(place.imageUrl!, fit: BoxFit.cover)
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
                  Text(place.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty ? place.getLocalizedArea(AppLocalizations.instance.isEnglish) : (place.city ?? ""), style: const TextStyle(color: textGrey, fontSize: 12)),
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

  Widget _buildEmptyTab({required IconData icon, required String title, required String subtitle}) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 48, color: textGrey.withOpacity(0.5)),
          const SizedBox(height: 16),
          Text(title, style: const TextStyle(color: textGrey, fontSize: 16, fontWeight: FontWeight.w600)),
          const SizedBox(height: 4),
          Text(subtitle, style: TextStyle(color: textGrey.withOpacity(0.7), fontSize: 13)),
        ],
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
                            'initialIndex': 4, // Profile Tab
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
                    final appLink = isEnglish 
                        ? "https://apps.apple.com/app/my-way-route-planner/id6741743515" 
                        : "https://apps.apple.com/app/my-way-rota-planlayici/id6741743515";
                    final message = isEnglish
                        ? "Hey! Check out My Way for smart city routes and personalized travel plans: $appLink"
                        : "Hey! Akıllı şehir rotaları ve kişiselleştirilmiş seyahat planları için My Way'i incele: $appLink";
                    Share.share(message);
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
                    final Uri url = Uri.parse("https://apps.apple.com/app/id6741743515?action=write-review");
                    if (await canLaunchUrl(url)) {
                      await launchUrl(url, mode: LaunchMode.externalApplication);
                    }
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
                    final Uri url = Uri.parse("https://mywaytravelapp.com/privacy.html");
                    if (await canLaunchUrl(url)) {
                      await launchUrl(url);
                    }
                  },
                  showDivider: true,
                ),

                // Manage Subscription (Visible if Premium)
                if (PremiumService.instance.hasFullAccess)
                  _buildSettingsItem(
                    icon: Icons.card_membership_rounded,
                    title: AppLocalizations.instance.manageSubscription,
                    trailing: const Icon(Icons.chevron_right, color: textGrey, size: 20),
                    onTap: () {
                      HapticFeedback.mediumImpact();
                      PremiumService.instance.manageSubscription();
                    },
                    showDivider: false,
                  ),
              ],
            ),
          ),
          
          const SizedBox(height: 16),
          
          // Version info
          Center(
            child: Text(
              "v1.0.0",
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
                  // Fallback for simulators or no email app
                  debugPrint("Could not launch email client");
                }
              },
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 16),
                decoration: BoxDecoration(
                  color: accent,
                  borderRadius: BorderRadius.circular(14),
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

  Map<String, dynamic> _getStyleInfo(String style) {
    switch (style) {
      case "Turist": return {'icon': Icons.camera_alt, 'color': const Color(0xFF2196F3)};
      case "Lokal": return {'icon': Icons.explore, 'color': const Color(0xFF4CAF50)};
      case "Macera": return {'icon': Icons.hiking, 'color': const Color(0xFFFF9800)};
      case "Lüks": return {'icon': Icons.diamond, 'color': const Color(0xFF9C27B0)};
      default: return {'icon': Icons.travel_explore, 'color': accentLight};
    }
  }

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

  double _getTabContentHeight() {
    int itemCount = 0;
    if (_tabController.index == 0) itemCount = _favoriteHighlights.length;
    else if (_tabController.index == 1) itemCount = _visitedHighlights.length;
    else itemCount = _completedRoutes.length;

    if (itemCount == 0) return 150;
    return (itemCount * 90.0 + 60); // Kart yüksekliği biraz daha fazla olabilir
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
      await prefs.setString("user_name", result);
      setState(() => _userName = result);
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
      tripDays = prefs.getInt("tripDays") ?? 3;
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
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          gradient: primaryGradient,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Icon(Icons.tune, color: Colors.white, size: 22),
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
                          icon: Icons.calendar_today,
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
                          icon: Icons.explore,
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
                          icon: Icons.favorite,
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
                          icon: Icons.account_balance_wallet,
                          title: AppLocalizations.instance.budgetPreference,
                          child: Row(
                            children: ["Ekonomik", "Dengeli", "Premium"].map((budget) {
                              final isSelected = budgetLevel == budget;
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
                                      child: Text(AppLocalizations.instance.translateBudgetLevel(budget), style: TextStyle(color: isSelected ? Colors.white : textGrey, fontWeight: FontWeight.w500, fontSize: 13)),
                                    ),
                                  ),
                                ),
                              );
                            }).toList(),
                          ),
                        ),

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
                      await prefs.setInt("tripDays", tripDays);
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
                            content: Text(AppLocalizations.instance.preferencesSavedMessage),
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
    required IconData icon,
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
              Icon(icon, color: accent, size: 20),
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
