// =============================================================================
// EXPLORE SCREEN – WANDERLUST DARK THEME
// Dark background, purple/pink gradients, glassmorphism, hero city image
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:async'; // Added for Timer
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'dart:ui';
import 'package:cached_network_image/cached_network_image.dart';
import '../utils/image_utils.dart';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/ai_service.dart';
import '../services/analytics_service.dart'; // Added
import 'detail_screen.dart';
import 'dart:convert';
import '../services/trip_update_service.dart';
import 'city_switcher_screen.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../theme/wanderlust_design_system.dart';
import '../widgets/map_background.dart';
// For ImageFilter
import '../services/notification_service.dart';
import '../services/trending_service.dart';
import 'city_guide_detail_screen.dart';
import 'ai_chat_screen.dart';
import '../models/chat_message.dart';
import 'paywall_screen.dart';
import 'analysis_loading_screen.dart';
import '../services/premium_service.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../services/tutorial_service.dart';
import '../widgets/tutorial_overlay_widget.dart';
import '../services/location_context_service.dart';
import '../services/auto_slot_picker.dart';
import '../widgets/day_selection_dialog.dart';
import '../services/version_service.dart'; // Added
import '../widgets/resilient_network_image.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../utils/image_utils.dart';

class ExploreScreen extends StatefulWidget {
  final bool isVisible;
  const ExploreScreen({super.key, this.isVisible = false});

  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen>
    with TickerProviderStateMixin, AutomaticKeepAliveClientMixin {
  // Keep alive to preserve scroll position when navigating back
  @override
  bool get wantKeepAlive => true;
  // ══════════════════════════════════════════════════════════════════════════
  // RENK PALETİ - AMBER/GOLD THEME
  // ══════════════════════════════════════════════════════════════════════════

  static const Color bgDark = WanderlustColors.bgDark;
  
  // AI Chat History
  final List<ChatMessage> _savedChatMessages = [];
  static const Color bgCard = WanderlustColors.bgCard;
  static const Color bgCardLight = WanderlustColors.bgCardLight;
  static const Color accent = WanderlustColors.accent; // Purple
  static const Color accentLight = WanderlustColors.accentLight;
  static const Color textWhite = WanderlustColors.textWhite;
  static const Color textGrey = WanderlustColors.textGrey;
  static const Color borderColor = WanderlustColors.border;
  static const Color accentGreen = WanderlustColors.accentGreen;

  static const LinearGradient primaryGradient = WanderlustColors.primaryGradient;

  static const LinearGradient primaryGradientDark = WanderlustColors.primaryGradientVertical;

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  CityModel? _city;
  bool _loading = true;
  bool _aiLoading = false;
  String? _error;
  String _userName = "";
  String _currentCityId = ""; // Mevcut şehir ID'si
  bool _showScrollToTop = false; // Scroll-to-top butonu görünürlüğü

  List<Highlight> _allHighlights = [];
  List<Highlight> _filteredHighlights = [];
  List<Highlight> _aiRecommendations = [];
  String? _aiChatResponse; // Kişiselleştirilmiş AI yanıtı
  bool _aiCardExpanded = true; // AI kartı açık/kapalı

  // Şehir bazlı AI yanıt cache'i (eski içerik saklanır, dil değişince çevrilir)
  // Key: cityId, Value: { "content": String, "isEnglish": bool }
  static final Map<String, Map<String, dynamic>> _aiChatCache = {};

  List<String> _favorites = [];
  List<String> _tripPlaces = [];
  int _selectedMood = 1; // 0: Sakin, 1: Keşif, 2: Popüler
  String _selectedCategory = "Tümü";
  String _searchQuery = "";

  // Onboarding verileri
  String _travelStyle = "Lokal";
  List<String> _interests = [];
  String _budgetLevel = "Dengeli";
  int _tripDays = 3;
  String _transportMode = "Karışık";

  final TextEditingController _searchController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  Timer? _searchTimer; // Added for debouncing analytics
  bool get isEnglish => AppLocalizations.instance.isEnglish;

  // Keys for Tutorial
  // Keys for Tutorial
  final GlobalKey _citySelectKey = GlobalKey();
  final GlobalKey _askAiKey = GlobalKey();
  final GlobalKey _moodSelectionKey = GlobalKey();
  final GlobalKey _aiFabKey = GlobalKey(); // FAB Tutorial Key
  
  // Tutorial State
  bool _pendingCityTutorial = false;
  bool _isCityTutorialShowing = false;
  bool _isFabTutorialShown = false;
  bool _isMoodTutorialShown = false;
  bool _isAITutorialShown = false;


  // Şehir görselleri - Artık AIService üzerinden merkezi olarak yönetiliyor

  List<Map<String, dynamic>> get _categories => [
    {"id": "Tümü", "label": AppLocalizations.instance.allCategories},
    {"id": "Yeme-İçme", "label": AppLocalizations.instance.foodDrink},
    {"id": "Kafe", "label": AppLocalizations.instance.cafe},
    {"id": "Müze", "label": AppLocalizations.instance.museum},
    {"id": "Park", "label": AppLocalizations.instance.park},
    {"id": "Bar", "label": AppLocalizations.instance.bar},
    {"id": "Tarihi", "label": AppLocalizations.instance.historical},
    {"id": "Manzara", "label": AppLocalizations.instance.categoryViewpoint},
    {"id": "Deneyim", "label": AppLocalizations.instance.experience},
    {"id": "Alışveriş", "label": AppLocalizations.instance.shopping},
    {"id": "Plaj", "label": AppLocalizations.instance.beach},
  ];

  List<Map<String, dynamic>> get _moods => [
    {"id": 0, "label": AppLocalizations.instance.moodSakin},
    {"id": 1, "label": AppLocalizations.instance.moodKesif},
    {"id": 2, "label": AppLocalizations.instance.moodPopuler},
  ];

  // ══════════════════════════════════════════════════════════════════════════
  // LIFECYCLE
  // ══════════════════════════════════════════════════════════════════════════

  @override
  void initState() {
    super.initState();
    _loadData();
    TripUpdateService().tripUpdated.addListener(_refreshTripRelatedPrefsOnly);
    TripUpdateService().cityChanged.addListener(_loadData);
    TripUpdateService().nameUpdated.addListener(_onNameUpdated);
    TripUpdateService().favoritesUpdated.addListener(_refreshTripRelatedPrefsOnly);
    
    // Listen for tutorial triggers from MainScreen
    // Only subscribe, do NOT trigger automatically
    TutorialService.instance.tutorialTrigger.listen((key) {
      if (key == TutorialService.KEY_TUTORIAL_CITY_SELECTION) {
         if (_loading) {
            _pendingCityTutorial = true;
         } else {
            if (mounted) _showCityTutorial();
         }
      }
    });

    // Scroll listener for scroll-to-top button
    _scrollController.addListener(_onScroll);
    

  }

  void _onScroll() {
    final showButton = _scrollController.offset > 400;
    if (showButton != _showScrollToTop) {
      setState(() => _showScrollToTop = showButton);
    }
  }



  void _scrollToTop() {
    _scrollController.animateTo(
      0,
      duration: const Duration(milliseconds: 500),
      curve: Curves.easeOutCubic,
    );
  }

  @override
  void didUpdateWidget(ExploreScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    // Tutorial triggering is handled by MainScreen, not here
  }

  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_refreshTripRelatedPrefsOnly);
    TripUpdateService().cityChanged.removeListener(_loadData);
    TripUpdateService().nameUpdated.removeListener(_onNameUpdated);
    TripUpdateService().favoritesUpdated.removeListener(_refreshTripRelatedPrefsOnly);
    _searchController.dispose();
    _scrollController.dispose();
    _searchTimer?.cancel(); // Added
    super.dispose();
  }

  /// Rota / favori güncellemelerinde tüm şehir JSON'unu yeniden yüklemeyin —
  /// hero görseli ve liste sürekli yeniden kurulup yanıp sönüyordu.
  List<String> _tripPlaceNamesFromPrefs(
    SharedPreferences prefs,
    String normalizedCity,
  ) {
    final bucketList = prefs.getStringList("trip_places_$normalizedCity") ?? [];
    final Set<String> allTripNames = Set.from(bucketList);

    final scheduleJson = prefs.getString("trip_schedule_$normalizedCity");
    if (scheduleJson != null) {
      try {
        final Map<String, dynamic> scheduleMap = jsonDecode(scheduleJson);
        scheduleMap.forEach((day, list) {
          if (list is List) {
            for (var item in list) {
              if (item is Map) {
                final name = item['name']?.toString();
                if (name != null) allTripNames.add(name);
              } else if (item is String) {
                allTripNames.add(item);
              }
            }
          }
        });
      } catch (_) {}
    }

    return allTripNames.toList();
  }

  Future<void> _refreshTripRelatedPrefsOnly() async {
    if (_loading || !mounted) return;
    final prefs = await SharedPreferences.getInstance();
    _favorites = prefs.getStringList("favorite_places") ?? [];
    final normalizedCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    _tripPlaces = _tripPlaceNamesFromPrefs(prefs, normalizedCity);
    if (!mounted) return;
    setState(() {});
  }

  void _onNameUpdated() {
    _loadData(); // Re-load data to update name
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DATA LOADING
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _loadData() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      _favorites = prefs.getStringList("favorite_places") ?? [];
      
      final defaultName = AppLocalizations.instance.isEnglish ? "Explorer" : "Gezgin";
      final storedName = prefs.getString("userName");
      _userName = (storedName == null || storedName.isEmpty) ? defaultName : storedName;

      _travelStyle = prefs.getString("travelStyle") ?? "Lokal";
      _interests = prefs.getStringList("interests") ?? [];
      _budgetLevel = prefs.getString("budgetLevel") ?? "Dengeli";
      _tripDays = prefs.getInt("tripDays") ?? 3;
      _transportMode = prefs.getString("transportMode") ?? "Karışık";

      final selectedCity = prefs.getString("selectedCity") ?? "barcelona";
      final normalizedCity = selectedCity.toLowerCase();

      _tripPlaces = _tripPlaceNamesFromPrefs(prefs, normalizedCity);
      // Get localized city name from CitySwitcherScreen data
      final cityData = CitySwitcherScreen.allCities.firstWhere(
        (c) => c['id'] == normalizedCity,
        orElse: () => {'name': normalizedCity, 'name_en': normalizedCity},
      );
      
      final cityName = AppLocalizations.instance.isEnglish 
          ? (cityData['name_en'] ?? cityData['name']) 
          : cityData['name'];

      try {
        final city = await CityDataLoader.loadCity(normalizedCity);
        // Override city name with localized version
        city.city = cityName; // Update the CityModel instance

        // Şehir değişti mi kontrol et
        final cityChanged = _currentCityId != null && _currentCityId != normalizedCity;

        if (!mounted) return;

        final newAllHighlights = _removeDuplicates(city.highlights);
        final newFilteredHighlights = _calculateFilteredHighlights(newAllHighlights);

        if (mounted) {
          setState(() {
            _city = city;
            _currentCityId = normalizedCity;
            _allHighlights = newAllHighlights;
            _filteredHighlights = newFilteredHighlights;
            _loading = false;
            
            if (_pendingCityTutorial) {
              _pendingCityTutorial = false;
              _showCityTutorial();
            }

            if (cityChanged) {
              NotificationService().subscribeToCity(normalizedCity);
              _aiLoading = false;
              if (_aiChatCache.containsKey(normalizedCity)) {
                final cachedData = _aiChatCache[normalizedCity]!;
                _aiChatResponse = cachedData["content"];
                _aiCardExpanded = false;
              } else {
                _aiChatResponse = null;
                _aiCardExpanded = true;
              }
            }
          });

          if (cityChanged) {
            WidgetsBinding.instance.addPostFrameCallback((_) {
              if (!mounted) return;
              if (_scrollController.hasClients) {
                _scrollController.jumpTo(0);
              }
              setState(() => _showScrollToTop = false);
            });
          }
        }

        // Arka plan işlerine devam
        LocationContextService.instance.updateContext(city).timeout(
          const Duration(seconds: 8),
          onTimeout: () => debugPrint("ExploreScreen: updateContext timeout"),
        ).catchError((e) => debugPrint("ExploreScreen: updateContext error: $e"));

        NotificationService().logEvent('explore_city', parameters: {
          'city_id': normalizedCity,
          'city_name': city.city,
        });

        if (_aiChatResponse == null) {
          _fetchAIRecommendations();
        }

      } catch (e) {
        debugPrint("ExploreScreen: Error loading city data: $e");
        if (mounted) {
          setState(() => _loading = false);
        }
      }
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _error = e.toString();
        _loading = false;
      });
    }
  }

  /// İsim benzerliğine göre duplicate'leri temizle
  List<Highlight> _removeDuplicates(List<Highlight> items) {
    if (items.isEmpty) return [];

    final List<Highlight> uniqueItems = [];
    final Set<String> seenNames = {};

    for (final item in items) {
      // İsmi normalize et (küçük harf, trim)
      final name = item.name.toLowerCase().trim();
      
      // Kelimelere ayır
      final words = name.split(' ');
      
      // İlk 3 kelimeyi al (veya daha azsa hepsini)
      final prefixCount = words.length >= 3 ? 3 : words.length;
      final prefix = words.sublist(0, prefixCount).join(' ');

      // Eğer bu prefix daha önce görülmediyse ekle
      if (!seenNames.contains(prefix)) {
        seenNames.add(prefix);
        uniqueItems.add(item);
      }
    }
    
    return uniqueItems;
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
                          (AppLocalizations.instance.isEnglish && cityData['name_en'] != null 
                            ? cityData['name_en'] 
                            : cityData['name']),
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
                              (AppLocalizations.instance.isEnglish && cityData['country_en'] != null
                                  ? cityData['country_en']
                                  : AppLocalizations.instance.translateCountry(cityData['country'])),
                              style: const TextStyle(
                                color: Colors.white,
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
                      style: TextStyle(
                        color: textGrey,
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

  /// [NearbyScreen] ile aynı mantık: birçok şehirde barlar `Yeme-İçme`, `Kafe` veya
  /// `Deneyim` olarak işaretli; yalnızca kategori listesiyle eşleştirmek Keşfet listesini boş bırakıyor.
  bool _matchesBarCategoryHeuristicHighlight(Highlight h) {
    const explicit = {
      'Bar',
      'Pub',
      'Wine Bar',
      'Enoteca',
      'Lounge',
      'American Bar',
    };
    if (explicit.contains(h.category)) return true;

    final names = '${h.name} ${h.nameEn ?? ''}'.toLowerCase();

    if (RegExp(r'\bbar\b', caseSensitive: false).hasMatch(names)) {
      return true;
    }

    if (RegExp(
      r'enoteca|ristobar|lounge\s*bar|american\s*bar|cocktail\s*bar|\bpub\b|birreria|wine\s*bar',
      caseSensitive: false,
    ).hasMatch(names)) {
      return true;
    }

    for (final t in h.tags) {
      final s = t.toLowerCase().trim();
      if (s == 'bar' ||
          s == 'pub' ||
          s == 'enoteca' ||
          s == 'wine_bar' ||
          s.contains('cocktail')) {
        return true;
      }
    }

    final desc =
        '${h.description} ${h.descriptionEn ?? ''}'.toLowerCase();
    if (RegExp(
      r'\bbeachside bar\b|\bseafront bar\b|\blounge bar\b|\bamerican bar\b|\bcocktail bar\b|\bbar and cafe\b|\bcafe and bar\b|\bbar e caf|\bcaffè e bar\b',
      caseSensitive: false,
    ).hasMatch(desc)) {
      return true;
    }

    return false;
  }

  void _applyFilters() {
    setState(() => _filteredHighlights = _calculateFilteredHighlights(_allHighlights));
  }

  List<Highlight> _calculateFilteredHighlights(List<Highlight> sourceList) {
    // 0. Temel de-duplicate (Özellikle kategori geçişlerinde ve merge sonrası garantiye almak için)
    final List<Highlight> baseList = [];
    final Set<String> seenUniqueNames = {};
    for (final h in sourceList) {
      final slug = h.name.toLowerCase().trim().replaceAll(RegExp(r'\s+'), ' ');
      if (!seenUniqueNames.contains(slug)) {
        seenUniqueNames.add(slug);
        baseList.add(h);
      }
    }

    var filtered = List<Highlight>.from(baseList);

    // 1. Kategori filtresi (kesin filtre)
    // Comprehensive category mappings - maps orphan categories to filter buttons
    const categoryMappings = {
      // Kafe filtresi
      'Kafe': ['Kafe', 'Cafe', 'Kahve', 'Tatlı', 'Fırın', 'Dondurma', 'Atıştırmalık'],
      
      // Yeme-İçme filtresi (Restoran yerine)
      'Yeme-İçme': ['Yeme-İçme', 'Restoran', 'Yeme & İçme', 'Yeme İçme', 'Sokak Lezzeti', 'Yemek', 'Gastronomi'],
      
      // Müze filtresi
      'Müze': ['Müze', 'Sanat', 'Kültür', 'Bilim', 'Modern', 'Akvaryum'],
      
      // Park filtresi
      'Park': ['Park', 'Doğa', 'Göl', 'Hayvanat Bahçesi'],
      
      // Bar filtresi
      'Bar': ['Bar', 'Gece Hayatı', 'Gece Kulübü', 'Şarap', 'Müzik'],
      
      // Tarihi filtresi
      'Tarihi': ['Tarihi', 'Meydan', 'Mimari', 'Tarih', 'Simge', 'Landmark', 'Heykel', 'Mimar', 'Saray', 'Merkez'],

      // Manzara filtresi (YENİ) - Doğal güzellikler ve manzaralar
      'Manzara': ['Manzara', 'View', 'Teras', 'Seyir', 'Panaromik', 'Mağara'],
      
      // Deneyim filtresi
      'Deneyim': ['Deneyim', 'Aktivite', 'Eğlence', 'Yürüyüş', 'Spor', 'Gezi', 'Macera', 'Rahatlama', 
                  'Günlük Gezi', 'Etkinlik', 'Atölye', 'Mahalle', 'Sokak',
                  'Görülmesi Gereken Yerler', 'Köy', 'Kasaba', 'Şehir', 'Bölge', 'Liman', 'Otel'],
      
      // Alışveriş filtresi
      'Alışveriş': ['Alışveriş', 'Mağaza', 'Pazar', 'Pasaj', 'Ticaret', 'Kitapçı', 'Lüks', 'Kompleks'],
      
      // Plaj filtresi (yeni)
      'Plaj': ['Plaj', 'Beach', 'Sahil'],
    };
    
    // Filtre dışı kategoriler (Tümü'de de gösterilmeyecek)
    const excludedCategories = ['Konaklama', 'Otel', 'Ulaşım', 'Hizmet', 'Bilgi', 'İş', 'Sağlık', 'Eğitim'];
    
    // Önce filtre dışı kategorileri çıkar
    filtered = filtered.where((h) => !excludedCategories.contains(h.category)).toList();
    
    if (_selectedCategory != "Tümü") {
      if (_selectedCategory == 'Bar') {
        final barCategories = categoryMappings['Bar']!;
        filtered = filtered.where((h) {
          if (barCategories.contains(h.category)) return true;
          return _matchesBarCategoryHeuristicHighlight(h);
        }).toList();
      } else {
        final validCategories =
            categoryMappings[_selectedCategory] ?? [_selectedCategory];
        filtered = filtered
            .where((h) => validCategories.contains(h.category))
            .toList();
        // Bar olarak tanınan mekanlar yalnızca Bar filtresinde; Yeme-İçme / Deneyim'de tekrar gösterme.
        if (_selectedCategory == 'Yeme-İçme' ||
            _selectedCategory == 'Deneyim') {
          filtered = filtered
              .where((h) => !_matchesBarCategoryHeuristicHighlight(h))
              .toList();
        }
      }
    }

    // 2. Arama filtresi
    if (_searchQuery.isNotEmpty) {
      final query = _searchQuery.toLowerCase();
      filtered = filtered.where((h) {
        return h.name.toLowerCase().contains(query) ||
            (h.nameEn?.toLowerCase().contains(query) ?? false) ||
            h.area.toLowerCase().contains(query) ||
            (h.areaEn?.toLowerCase().contains(query) ?? false) ||
            h.category.toLowerCase().contains(query) ||
            (h.description.toLowerCase().contains(query)) ||
            (h.descriptionEn?.toLowerCase().contains(query) ?? false) ||
            h.tags.any((tag) => tag.toLowerCase().contains(query));
      }).toList();
    }

    // 3. Kişiselleştirilmiş sıralama (popülerlik + ilgi alanları serpiştirilmiş)
    if (_selectedCategory == "Tümü") {
      // Mood seçili değilse veya Keşif modundaysa kişiselleştirilmiş sıralama uygula
      filtered = _applyPersonalizedSorting(filtered);
      
      if (_selectedMood == 0) {
        // 🧘 Sakin: Önce kişiselleştir, sonra sakin kategorileri öne al
        filtered.sort((a, b) {
          int scoreA = _getCalmScore(a.category);
          int scoreB = _getCalmScore(b.category);
          if (scoreA != scoreB) return scoreA.compareTo(scoreB);
          // Eşit ise popülerliğe göre
          return _getPopularityScore(b).compareTo(_getPopularityScore(a));
        });
      } else if (_selectedMood == 2) {
        // 🎉 Canlı: Önce kişiselleştir, sonra canlı kategorileri öne al
        filtered.sort((a, b) {
          int scoreA = _getLivelyScore(a.category);
          int scoreB = _getLivelyScore(b.category);
          if (scoreA != scoreB) return scoreA.compareTo(scoreB);
          // Eşit ise popülerliğe göre
          return _getPopularityScore(b).compareTo(_getPopularityScore(a));
        });
      }
    } else {
        // KATEGORİ SEÇİLİ: Eleme yapma (PersonalizedSorting eleme yapar), sadece sırala!
        if (_selectedMood == 0) {
           filtered.sort((a, b) {
              int scoreA = _getCalmScore(a.category);
              int scoreB = _getCalmScore(b.category);
              if (scoreA != scoreB) return scoreA.compareTo(scoreB);
              return _getPopularityScore(b).compareTo(_getPopularityScore(a));
           });
        } else if (_selectedMood == 2) {
           filtered.sort((a, b) {
              int scoreA = _getLivelyScore(a.category);
              int scoreB = _getLivelyScore(b.category);
              if (scoreA != scoreB) return scoreA.compareTo(scoreB);
              return _getPopularityScore(b).compareTo(_getPopularityScore(a));
           });
        } else {
           // Keşif (Default)
           filtered.sort((a, b) => _getPopularityScore(b).compareTo(_getPopularityScore(a)));
        }
    }

    return filtered;
  }

  // Mood skor fonksiyonları (düşük = daha öncelikli)
  // _getInitialFilteredHighlights removed in favor of _calculateFilteredHighlights

  int _getCalmScore(String category) {
    switch (category) {
      case 'Park': return 0;
      case 'Manzara': return 0;
      case 'Kafe': return 1;
      case 'Müze': return 1;
      default: return 2;
    }
  }

  int _getExplorationScore(String category) {
    switch (category) {
      case 'Müze': return 0;
      case 'Tarihi': return 0;
      case 'Deneyim': return 1;
      case 'Manzara': return 1;
      case 'Sanat': return 1;
      default: return 2;
    }
  }

  int _getLivelyScore(String category) {
    switch (category) {
      case 'Bar': return 0;
      case 'Restoran': return 0;
      case 'Gece Hayatı': return 0;
      case 'Alışveriş': return 1;
      case 'Kafe': return 1;
      default: return 2;
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // PERSONALIZED SORTING HELPERS
  // ══════════════════════════════════════════════════════════════════════════

  /// İlgi alanı kategorilerine göre eşleştirme map'i
  static const Map<String, List<String>> _interestToCategoryMap = {
    'yemek': ['Restoran', 'Yeme & İçme', 'Yeme İçme', 'Yeme-İçme', 'Sokak Lezzeti'],
    'kahve': ['Kafe', 'Cafe', 'Kahve', 'Tatlı', 'Fırın'],
    'sanat': ['Müze', 'Sanat', 'Galeri', 'Modern'],
    'tarih': ['Tarihi', 'Mimari', 'Tarih', 'Simge', 'Landmark', 'Saray'],
    'doğa': ['Park', 'Doğa', 'Göl', 'Manzara', 'Bahçe'],
    'gece': ['Bar', 'Gece Hayatı', 'Gece Kulübü', 'Pub'],
    'alışveriş': ['Alışveriş', 'Mağaza', 'Pazar', 'Pasaj'],
    'fotoğraf': ['Manzara', 'Mimari', 'Tarihi', 'Deneyim'],
    'mimari': ['Mimari', 'Tarihi', 'Simge', 'Landmark'],
    'plaj': ['Plaj', 'Beach', 'Sahil'],
    'spor': ['Spor', 'Stadyum', 'Stadium', 'Arena'],
    'müze': ['Müze', 'Sanat', 'Bilim', 'Kültür'],
    'yerel lezzetler': ['Restoran', 'Sokak Lezzeti', 'Yeme & İçme', 'Yeme-İçme', 'Pazar'],
  };

  /// Popülerlik skoru hesapla (0-1 arası)
  double _getPopularityScore(Highlight h) {
    final rating = h.rating ?? 0;
    final reviewCount = h.reviewCount ?? 0;
    
    // Rating ağırlığı: %60, Review count ağırlığı: %30, Landmark bonus: %10
    final ratingScore = (rating / 5.0).clamp(0.0, 1.0);
    final reviewScore = (reviewCount / 5000.0).clamp(0.0, 1.0);
    
    // Tarihi/Simge/Müze kategorileri için bonus (Artırıldı: 0.1 -> 0.25)
    final isLandmark = ['Tarihi', 'Simge', 'Landmark', 'Mimari', 'Müze'].contains(h.category);
    final landmarkBonus = isLandmark ? 0.25 : 0.0;
    
    return (ratingScore * 0.6) + (reviewScore * 0.3) + landmarkBonus;
  }

  /// Kullanıcının ilgi alanlarına uyuyor mu?
  bool _matchesUserInterests(Highlight h) {
    if (_interests.isEmpty) return false;
    
    for (final interest in _interests) {
      final lowerInterest = interest.toLowerCase();
      final categories = _interestToCategoryMap[lowerInterest] ?? [];
      
      // Kategori eşleşmesi
      if (categories.contains(h.category)) return true;
      
      // Tag eşleşmesi
      if (h.tags.any((tag) => tag.toLowerCase().contains(lowerInterest))) return true;
      
      // İsim veya açıklama eşleşmesi (stadyum, müze gibi)
      if (h.name.toLowerCase().contains(lowerInterest)) return true;
    }
    
    return false;
  }

  /// Bütçe eşleşmesi skoru (0-1)
  double _getBudgetMatchScore(Highlight h) {
    final placePrice = h.price ?? 'medium';
    
    // Bütçe seviyeleri: Ekonomik, Dengeli, Premium
    final budgetMap = {
      'Ekonomik': {'low': 1.0, 'medium': 0.6, 'high': 0.3, 'luxury': 0.2},
      'Dengeli': {'low': 0.7, 'medium': 1.0, 'high': 0.7, 'luxury': 0.5},
      'Premium': {'low': 0.4, 'medium': 0.8, 'high': 1.0, 'luxury': 1.0},
    };
    
    final scores = budgetMap[_budgetLevel] ?? budgetMap['Dengeli']!;
    return scores[placePrice] ?? 0.7;
  }

  /// Kişiselleştirilmiş sıralama uygula (3 İkonik + 1 İlgi Alanı kuralı)
  List<Highlight> _applyPersonalizedSorting(List<Highlight> places) {
    if (places.isEmpty) return places;
    
    // Yeme-İçme ve alışveriş kategorilerini "İkonik" listesinden hariç tut.
    // ANCAK: Canlı modunda (2) barlar ve restoranlar ana içeriktir, filtreleme!
    List<String> nonIconicCategories;
    
    if (_selectedMood == 2) {
      // Canlı mod: Sadece alışverişi filtrele (veya hiçbir şeyi filtreleme)
      nonIconicCategories = ['Alışveriş', 'Mağaza', 'Pasaj'];
    } else {
      // Keşif/Sakin mod: Yeme-içme ve gece hayatını "İkonik" akışından çıkar 
      // (Sadece ilgi alanı olarak gelmeli)
      nonIconicCategories = [
        'Yeme-İçme', 'Restoran', 'Yeme & İçme', 'Yeme İçme', 'Sokak Lezzeti', 
        'Kafe', 'Cafe', 'Kahve', 'Tatlı', 'Fırın', 'Dondurma',
        'Bar', 'Gece Hayatı', 'Gece Kulübü', 'Pub',
        'Alışveriş', 'Mağaza', 'Pasaj'
      ];
    }

    // 1. İkonik ve Popüler yerleri ayır (Hepsini al, ama Mood'a uymayanları arkaya at)
    final iconicList = List<Highlight>.from(places);
    iconicList.sort((a, b) {
       // Önce Mood Puanına göre (Uymayanlar arkaya)
       bool isANonIconic = nonIconicCategories.contains(a.category);
       bool isBNonIconic = nonIconicCategories.contains(b.category);
       
       if (isANonIconic && !isBNonIconic) return 1; // A arkaya
       if (!isANonIconic && isBNonIconic) return -1; // B arkaya
       
       // Sonra Popülariteye göre
       return _getPopularityScore(b).compareTo(_getPopularityScore(a));
    });
    
    // 2. Kullanıcının ilgi alanlarına uyan (onboarding seçimleri) yerleri ayır
    // Burada yeme-içme olabilir, çünkü kullanıcı özellikle ilgiliyse gösterilmeli
    final interestList = places.where((h) => _matchesUserInterests(h)).toList();
    interestList.sort((a, b) {
      final scoreA = (_getPopularityScore(a) * 0.6) + (_getBudgetMatchScore(a) * 0.4);
      final scoreB = (_getPopularityScore(b) * 0.6) + (_getBudgetMatchScore(b) * 0.4);
      return scoreB.compareTo(scoreA);
    });
    
    // 3. Karıştırma (Interleaving): 3 İkonik + 1 İlgi Alanı
    final result = <Highlight>[];
    final usedNames = <String>{};
    int iconicIdx = 0;
    int interestIdx = 0;
    
    while (iconicIdx < iconicList.length || interestIdx < interestList.length) {
      // 3 tane ikonik/popüler yer ekle
      int addedIconicCount = 0;
      while (addedIconicCount < 3 && iconicIdx < iconicList.length) {
        final item = iconicList[iconicIdx++];
        if (!usedNames.contains(item.name)) {
          result.add(item);
          usedNames.add(item.name);
          addedIconicCount++;
        }
      }
      
      // 1 tane ilgi alanına dayalı yer ekle (eğer zaten eklenmemişse)
      if (interestIdx < interestList.length) {
        bool foundSpecificInterestMatch = false;
        while (interestIdx < interestList.length && !foundSpecificInterestMatch) {
          final item = interestList[interestIdx++];
          if (!usedNames.contains(item.name)) {
            result.add(item);
            usedNames.add(item.name);
            foundSpecificInterestMatch = true;
          }
        }
      }
    }
    
    // Eğer hala kullanılmamış ikonik yerler varsa ekle (ilgi alanı listesi bittiyse)
    while (iconicIdx < iconicList.length) {
       final item = iconicList[iconicIdx++];
       if (!usedNames.contains(item.name)) {
         result.add(item);
         usedNames.add(item.name);
       }
    }
    
    return result;
  }

  // Otomatik çağrılan - sadece mekan önerileri için, AI chat yanıtı ALMAZ
  Future<void> _fetchAIRecommendations() async {
    if (_city == null) return;

    // 🔒 Race-condition guard: isteği başlatırken hangi şehir için olduğunu yakala.
    // Await sırasında kullanıcı şehir değiştirirse, dönen sonucu yok say.
    final String requestedCityId = _currentCityId;

    try {
      final recs = await AIService.getSerendipityRecommendations(
        city: _city!.city,
        travelStyle: _travelStyle,
        interests: _interests,
        moodLevel: _selectedMood / 2.0,
        cityHighlights: _allHighlights,
      );

      if (!mounted) return;
      // Şehir değişmişse stale sonucu uygulama
      if (_currentCityId != requestedCityId) {
        debugPrint(
            "🚫 _fetchAIRecommendations: stale response dropped ($requestedCityId → $_currentCityId)");
        return;
      }
      setState(() {
        _aiRecommendations = recs;
      });
    } catch (e) {
      if (!mounted) return;
      if (_currentCityId != requestedCityId) return;
      setState(() {
        _aiRecommendations = _allHighlights.take(4).toList();
      });
    }
  }

  // Kullanıcı AppLocalizations.instance.askAI butonuna basınca çağrılır
  Future<void> _fetchAIChatResponse({int variation = 0}) async {
    if (_city == null) return;
    
    // Premium limit kontrolü
    if (!PremiumService.instance.canUseAISuggestion()) {
      _showPaywall();
      return;
    }

    // 🔒 Race-condition guard: isteği başlatırken hangi şehir için olduğunu yakala.
    // Await sırasında kullanıcı şehir değiştirirse, dönen sonucu uygulamayız ve
    // yeni şehrin cache'ine yazmayız. Premium kullanım sayacı da artırılmaz.
    final String requestedCityId = _currentCityId;
    final String requestedCityName = _city!.city;

    setState(() {
      _aiLoading = true;
    });

    try {
      // Kişiselleştirilmiş AI chat yanıtını al
      final chatResponse = await AIService.getPersonalizedChatResponse(
        cityModel: _city!, // CityModel parametresi
        userName: _userName,
        travelStyle: _travelStyle,
        interests: _interests,
        budgetLevel: _budgetLevel,
        tripDays: _tripDays,
        variation: variation, // Rastgelelik için
        isEnglish: AppLocalizations.instance.isEnglish, // Dil parametresi
      );

      if (!mounted) return;

      // Şehir await sırasında değiştiyse: stale yanıtı uygulama, cache'e yazma,
      // kullanım sayacını arttırma. Yeni şehir kendi isteğini kendi yapacak.
      // ⚠️ _aiLoading'a DOKUNMA: yeni şehir kendi spinner'ını yönetiyor olabilir,
      // burada sıfırlarsak canlı isteğin loader'ını yanlışlıkla kapatırız.
      if (_currentCityId != requestedCityId) {
        debugPrint(
            "🚫 _fetchAIChatResponse: stale response dropped ($requestedCityId/$requestedCityName → $_currentCityId)");
        return;
      }

      // Kullanımı artır (sadece kullanıcı hala aynı şehirdeyse)
      await PremiumService.instance.useAISuggestion();

      if (!mounted) return;
      // useAISuggestion da async; bir kez daha kontrol et
      if (_currentCityId != requestedCityId) return;

      setState(() {
        _aiChatResponse = chatResponse;
        _aiLoading = false;
        _aiCardExpanded = true;

      // Cache'e kaydet — istek başında yakaladığımız şehir id'sine yaz
        _aiChatCache[requestedCityId] = {
          "content": chatResponse,
          "isEnglish": AppLocalizations.instance.isEnglish
        };
      });
    } catch (e) {
      if (!mounted) return;
      // Stale hata: spinner'a dokunma (yeni şehrin canlı isteği olabilir), sadece çık.
      if (_currentCityId != requestedCityId) {
        return;
      }
      setState(() {
        _aiLoading = false;
      });
      
      // Hata mesajı göster
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            AppLocalizations.instance.isEnglish 
                ? "Couldn't generate recommendations. Please try again." 
                : "Öneriler oluşturulamadı. Lütfen tekrar deneyin.",
          ),
          backgroundColor: Colors.redAccent,
          behavior: SnackBarBehavior.floating,
        ),
      );
    }
  }

  /// Dil değiştiğinde mevcut AI içeriğini çevirir (yeniden üretmek yerine)
  void _checkAndTranslateContent() async {
    // Cache kontrolü
    if (!_aiChatCache.containsKey(_currentCityId)) return;
    
    final cachedData = _aiChatCache[_currentCityId]!;
    final cachedIsEnglish = cachedData["isEnglish"] as bool;
    final currentIsEnglish = AppLocalizations.instance.isEnglish;
    
    // Dil değişmemişse çık
    if (cachedIsEnglish == currentIsEnglish) {
      if (_aiChatResponse == null) {
         setState(() {
           _aiChatResponse = cachedData["content"];
         });
      }
      return;
    }
    
    // Dil değişmiş! Çeviri yap
    // Önce UI'da loading göster
    setState(() {
      _aiLoading = true;
      // Eğer ekranda bir şey yoksa en azından eskiyi gösterelim mi? 
      // Hayır, çeviri bekleniyor.
    });
    
    try {
      final contentToTranslate = cachedData["content"] as String;
      
      final translatedContent = await AIService.translateContent(
        content: contentToTranslate,
        toEnglish: currentIsEnglish,
      );
      
      if (!mounted) return;
      
      setState(() {
        _aiChatResponse = translatedContent;
        _aiLoading = false;
        
        // Cache'i de güncelle
        _aiChatCache[_currentCityId] = {
           "content": translatedContent,
           "isEnglish": currentIsEnglish
        };
      });
    } catch (e) {
      if (!mounted) return;
      setState(() => _aiLoading = false);
    }
  }  // ══════════════════════════════════════════════════════════════════════════
  // PAYWALL
  // ══════════════════════════════════════════════════════════════════════════
  
  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TUTORIAL
  // ══════════════════════════════════════════════════════════════════════════
  
  // ══════════════════════════════════════════════════════════════════════════
  // TUTORIAL (DECOUPLED)
  // ══════════════════════════════════════════════════════════════════════════

  // 0. Polling Loop for Tutorial
  void _startTutorialCheckLoop() async {
     for (int i = 0; i < 10; i++) { // Try for 10 seconds
        if (!mounted) return;
        
        // Wait 1 second
        await Future.delayed(const Duration(seconds: 1));
        
        if (!mounted) return;
        
        // Check if Paywall/Dialog is open (if open, isCurrent is false)
        final isCurrent = ModalRoute.of(context)?.isCurrent ?? false;
        final isVisible = widget.isVisible || isCurrent;
        
        if (isVisible && !_isCityTutorialShowing) {
           final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_CITY_SELECTION);
           if (shouldShow) {
              if (mounted) _showCityTutorial();
              break; // Success!
           } else {
              // Tutorial seen or not needed, stop loop
              break; 
           }
        }
     }
  }

  // 1. City Selection (Launch)  
  void _showCityTutorial() async {
      if (_isCityTutorialShowing) return;
      _isCityTutorialShowing = true;

      if (!mounted) {
        _isCityTutorialShowing = false;
        return;
      }

      final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_CITY_SELECTION);
      if (!shouldShow) {
        _isCityTutorialShowing = false;
        _showAITutorial(); 
        return;
      }

      // Ensure visible
      if (_citySelectKey.currentContext == null && _scrollController.hasClients) {
          _scrollController.jumpTo(0);
          // Wait for frame to render after jump
          await Future.delayed(const Duration(milliseconds: 200));
      }
      
      // Retry finding context
      if (_citySelectKey.currentContext == null) {
         // One last try after a slightly longer delay
         await Future.delayed(const Duration(milliseconds: 500));
         if (_citySelectKey.currentContext == null) {
             debugPrint("Tutorial Error: _citySelectKey context is null");
             _isCityTutorialShowing = false;
             return;
         }
      }

      late TutorialCoachMark tutorial;
      tutorial = TutorialCoachMark(
        targets: [
          TargetFocus(
            identify: "city_selection",
            keyTarget: _citySelectKey,
            color: Colors.black,
            contents: [
              TargetContent(
                align: ContentAlign.bottom,
                builder: (context, controller) {
                  return TutorialOverlayWidget(
                    title: AppLocalizations.instance.tutorialCitySelectTitle,
                    description: AppLocalizations.instance.tutorialCitySelectDesc,
                    currentStep: 1,
                    totalSteps: 4,
                    onSkip: () => controller.skip(),
                    onNext: () => controller.next(),
                    isArrowUp: true, // City selection is always at top
                  );
                },
              ),
            ],
            shape: ShapeLightFocus.RRect,
            radius: 20,
          ),
        ],
        colorShadow: Colors.black, 
        opacityShadow: 0.9, 
        textSkip: "",
        skipWidget: _buildSkipWidget(),
          onFinish: () async {
             _isCityTutorialShowing = false;
             TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_CITY_SELECTION);
             if (mounted) {
               await Future.delayed(const Duration(milliseconds: 500));
               _showAITutorial(); // Moved from 3rd to 2nd
             }
          },
          onClickTarget: (target) {
             tutorial.next();
          },
          onSkip: () {
             _isCityTutorialShowing = false;
             TutorialService.instance.skipAllTutorials();
             return true; 
          },
          onClickOverlay: (target) {
             tutorial.next();
          },
      );
      tutorial.show(context: context);
  }

  // 3. FAB Tutorial ("My Way Asistan")
  // Chain: City → AI → FAB → Mood
  void _showFabTutorial() async {
    if (!mounted) return;
    
    // Guard to prevent double-triggering
    if (_isFabTutorialShown) {
      _showMoodTutorial();
      return;
    }
    
    final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_FAB);
    if (!shouldShow) {
      _isFabTutorialShown = true;
      _showMoodTutorial();
      return;
    }
    
    _isFabTutorialShown = true;

    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        TargetFocus(
          identify: "ai_fab",
          keyTarget: _aiFabKey, // GlobalKey
          shape: ShapeLightFocus.Circle,
          radius: 28, // Adjust based on FAB size
          color: Colors.black,
          contents: [
            TargetContent(
              align: ContentAlign.top, // FAB is at bottom right
              builder: (context, controller) {
                return TutorialOverlayWidget(
                   title: "My Way Asistan",
                  description: AppLocalizations.instance.isEnglish 
                      ? "Ask instant questions about the city and get personalized answers."
                      : "Şehirle ilgili sorularını anlık sor, sana özel cevaplar al.",
                  currentStep: 3, // Moved from 2nd to 3rd
                  totalSteps: 4,
                  onSkip: () => controller.skip(),
                  onNext: () => controller.next(),
                  isArrowUp: false, 
                );
              },
            ),
          ],
        ),
      ],
      colorShadow: Colors.black,
      opacityShadow: 0.9,
      textSkip: "",
      skipWidget: _buildSkipWidget(),
      onFinish: () async {
         _isFabTutorialShown = true;
         TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_FAB);
         if (mounted) {
           await Future.delayed(const Duration(milliseconds: 500));
           _showMoodTutorial(); // Chain to mood
         }
      },
      onClickTarget: (target) {
         tutorial.next();
      },
      onSkip: () {
         _isFabTutorialShown = true;
         TutorialService.instance.skipAllTutorials();
         return true;
      },
      onClickOverlay: (target) {
         tutorial.next();
      },
    );
    tutorial.show(context: context);
  }

  // 2. AI Recommendation ("Öneri Oluştur" / "Bugün Yönün Neresi")
  // Chain: City → AI → FAB → Mood
  void _showAITutorial() async {
      if (!mounted) return;
      
      // Guard to prevent double-triggering
      if (_isAITutorialShown) {
        _showFabTutorial();
        return;
      }
      
      final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_AI_BUTTON);
      if (!shouldShow) {
        _isAITutorialShown = true;
        _showFabTutorial(); // AI is Step 2, go to 3
        return;
      }
      
      _isAITutorialShown = true;

      // Ensure visible? It is near top, usually visible.
      if (_askAiKey.currentContext == null) return;

      late TutorialCoachMark tutorial;
      tutorial = TutorialCoachMark(
        targets: [
          TargetFocus(
            identify: "ask_ai",
            keyTarget: _askAiKey,
            color: Colors.black,
            contents: [
              TargetContent(
                align: ContentAlign.bottom, 
                builder: (context, controller) {
                   return TutorialOverlayWidget(
                    title: AppLocalizations.instance.tutorialAiTitle,
                    description: AppLocalizations.instance.tutorialAiDesc,
                    currentStep: 2, // Moved from 3rd to 2nd
                    totalSteps: 4,
                    onSkip: () => controller.skip(),
                    onNext: () => controller.next(),
                    isArrowUp: true,
                    arrowHeight: 120,
                   );
                },
              ),
            ],
            shape: ShapeLightFocus.RRect, // Button shape
            radius: 20,
            paddingFocus: 0,
          ),
        ],
        colorShadow: Colors.black, 
        opacityShadow: 0.9, 
        textSkip: "",
        skipWidget: _buildSkipWidget(),
        onFinish: () async {
           TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_AI_BUTTON);
           if (mounted) {
             await Future.delayed(const Duration(milliseconds: 500));
             _showFabTutorial(); // Chain to FAB
           }
        },
        onClickTarget: (target) {
           tutorial.next();
        },
        onSkip: () {
           TutorialService.instance.skipAllTutorials();
           return true; 
        },
        onClickOverlay: (target) {
           tutorial.next();
        },
      );
      tutorial.show(context: context);
  }

  // 3. Mood Selection Tutorial
  void _showMoodTutorial() async {
    if (!mounted) return;

    final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_MODE_SELECTION);
    if (!shouldShow) return;
    
    // Local guard
    if (_isMoodTutorialShown) return;
    _isMoodTutorialShown = true;

    if (_moodSelectionKey.currentContext == null) return;
    
    // Calculate position
    final RenderBox? renderBox = _moodSelectionKey.currentContext?.findRenderObject() as RenderBox?;
    final offset = renderBox?.localToGlobal(Offset.zero);
    final screenHeight = MediaQuery.of(context).size.height;
    
    // If element is in top half, show text BELOW (bottom). If in bottom half, show ABOVE (top).
    final isTopHalf = (offset?.dy ?? 0) < (screenHeight / 2);
    final align = isTopHalf ? ContentAlign.bottom : ContentAlign.top;
    final isArrowUp = isTopHalf;

    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        TargetFocus(
          identify: "mood_selection",
          keyTarget: _moodSelectionKey,
          color: Colors.black,
          contents: [
            TargetContent(
              align: align,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: AppLocalizations.instance.isEnglish ? "Choose Your Vibe" : "Modunu Seç",
                  description: AppLocalizations.instance.isEnglish 
                      ? "Plan your day by your mood. A calm day, new discoveries or lively moments? Choice is yours." 
                      : "Gününü moduna göre planla. Sakin bir gün mü, yeni keşifler mi yoksa hareketli anlar mı? Seçim senin.",
                  currentStep: 4,
                  totalSteps: 4,
                  onSkip: () => controller.skip(),
                  onNext: () => controller.next(),
                  isArrowUp: isArrowUp, // Dynamic arrow direction
                  arrowHeight: 80, 
                );
              },
            ),
          ],
          shape: ShapeLightFocus.RRect,
          radius: 12,
        ),
      ],
      colorShadow: Colors.black.withOpacity(0.8),
      opacityShadow: 0.9,
      textSkip: AppLocalizations.instance.skip,
      skipWidget: _buildSkipWidget(),
      onFinish: () {
         TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_MODE_SELECTION);
      },
      onClickTarget: (target) {
         tutorial.next();
      },
      onSkip: () {
         TutorialService.instance.skipAllTutorials();
         return true;
      },
      onClickOverlay: (target) {
         tutorial.next();
      },
    );
    tutorial.show(context: context);
  }

  Widget _buildSkipWidget() {
    return SafeArea(
      child: Align(
        alignment: Alignment.topRight,
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Container(
             padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
             decoration: BoxDecoration(
               color: Colors.white24,
               borderRadius: BorderRadius.circular(20),
             ),
             child: const Text(
               "Atla", 
               style: TextStyle(
                 color: Colors.white,
                 fontWeight: FontWeight.w600,
               ),
             ),
          ),
        ),
      ),
    );
  }




  // ══════════════════════════════════════════════════════════════════════════
  // HELPER METHODS
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _toggleFavorite(String name) async {
    HapticFeedback.lightImpact();
    final prefs = await SharedPreferences.getInstance();
    final placeKey = "$_currentCityId:$name";

    setState(() {
      // Check both old format and new format
      final hasOldFormat = _favorites.contains(name);
      final hasNewFormat = _favorites.contains(placeKey);
      
      if (hasOldFormat || hasNewFormat) {
        // Remove both formats
        _favorites.remove(name);
        _favorites.remove(placeKey);
      } else {
        // Add new format only
        _favorites.add(placeKey);
      }
    });

    await prefs.setStringList("favorite_places", _favorites);
    TripUpdateService().notifyFavoritesChanged();
  }

  Future<void> _addToTrip(String name) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    final String currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
    // 1. Güncel verileri oku (Şehir bazlı)
    final List<String> bucketList = prefs.getStringList("trip_places_$currentCity") ?? [];
    final String? scheduleJson = prefs.getString("trip_schedule_$currentCity");
    
    // Schedule'ı parse et
    Map<String, dynamic> scheduleMap = {};
    if (scheduleJson != null) {
      try {
        scheduleMap = jsonDecode(scheduleJson);
      } catch (e) { print(e); }
    }

    final bool alreadyInTrip = _tripPlaces.contains(name);

    if (alreadyInTrip) {
        // ÇIKARMA İŞLEMİ
        setState(() {
          _tripPlaces.remove(name);
        });
        
        // Schedule'dan da sil (hem eski hem yeni format)
        scheduleMap.keys.forEach((day) {
             final List<dynamic> list = scheduleMap[day] ?? [];
             list.removeWhere((item) {
               if (item is String) return item == name;
               if (item is Map<String, dynamic>) return item['name'] == name;
               return false;
             });
             scheduleMap[day] = list;
        });

         if (mounted) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Text(AppLocalizations.instance.removedFromRoute(name), style: const TextStyle(color: WanderlustColors.textGrey)),
               backgroundColor: WanderlustColors.bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 1500),
            ));
         }

    } else {
         // Tek global rota-ekleme kotası (keşfet / detay / yakınımda toplamı)
         if (!PremiumService.instance.canAddToRoute()) {
           _showPaywall();
           return;
         }

         final int currentTotalDays = prefs.getInt("tripDays_$currentCity") ?? prefs.getInt("tripDays") ?? 3;
         final int? selectedDay = await _showDaySelectionDialogForExplore(currentTotalDays, name, scheduleMap);
         if (selectedDay == null) return; // İptal edildi

         await PremiumService.instance.useRouteAdd();

         setState(() {
            _tripPlaces.add(name);
         });

         if (selectedDay == 0) {
           // LISTEM'E EKLEME — sadece trip_places_ güncellenir
           if (!bucketList.contains(name)) {
             bucketList.add(name);
           }
           await prefs.setStringList("trip_places_$currentCity", bucketList);
           TripUpdateService().notifyTripChanged();

           if (mounted) {
             ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Row(
                 children: [
                   const Icon(Icons.check_circle_outline, color: WanderlustColors.accent, size: 20),
                   const SizedBox(width: 12),
                   Expanded(
                     child: Text(
                       AppLocalizations.instance.isEnglish
                           ? '$name added to My List'
                           : '$name Listem\'e eklendi',
                       style: const TextStyle(color: WanderlustColors.textGrey, fontWeight: FontWeight.w600),
                     ),
                   ),
                 ],
               ),
               backgroundColor: WanderlustColors.bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 2200),
             ));
           }
         } else {
           // GÜNE EKLEME — sadece schedule güncellenir, trip_places_ dokunulmaz
           final dayKey = selectedDay.toString();
           List<dynamic> targetList = scheduleMap[dayKey] ?? [];

           // Yeni format: {name, city} olarak ekle
           final placeEntry = {'name': name, 'city': currentCity};
           final alreadyExists = targetList.any((item) {
             if (item is Map<String, dynamic>) return item['name'] == name;
             if (item is String) return item == name;
             return false;
           });

           if (!alreadyExists) {
              targetList.add(placeEntry);
              // 🔥 Analytics Etkinliği: Rota eklendi
              NotificationService().logEvent('add_to_trip', parameters: {
                'place': name,
                'city': currentCity,
                'day': selectedDay,
              });
           }
           scheduleMap[dayKey] = targetList;

           // Yeni gün oluşturulduysa onboardingDays güncelle
           if (selectedDay > currentTotalDays) {
             await prefs.setInt("tripDays_$currentCity", selectedDay);
           }

           // Save ONLY schedule — trip_places_ dokunulmaz
           await prefs.setString("trip_schedule_$currentCity", jsonEncode(scheduleMap));
           TripUpdateService().notifyTripChanged();

           if (mounted) {
             ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Row(
                 children: [
                   const Icon(Icons.check_circle_outline, color: WanderlustColors.accent, size: 20),
                   const SizedBox(width: 12),
                   Expanded(
                     child: Text(
                       AppLocalizations.instance.addedToDay(name, selectedDay),
                       style: const TextStyle(color: WanderlustColors.textGrey, fontWeight: FontWeight.w600),
                     ),
                   ),
                 ],
               ),
               backgroundColor: WanderlustColors.bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 2200),
             ));
           }
         }
    }

    // Çıkarma durumunda schedule ve bucketList'i güncelle
    if (_tripPlaces.contains(name) == false) {
      // Çıkarma yapıldı — bucketList'ten de sil
      bucketList.remove(name);
      await prefs.setStringList("trip_places_$currentCity", bucketList);
      await prefs.setString("trip_schedule_$currentCity", jsonEncode(scheduleMap));
      TripUpdateService().notifyTripChanged();
    }
  }

  Future<int?> _showDaySelectionDialogForExplore(int totalDays, String placeName, Map<String, dynamic> scheduleMap) async {
    return showDaySelectionDialog(
      context,
      totalDays: totalDays,
      scheduleMap: scheduleMap,
      confirmMessage: AppLocalizations.instance.addToRouteConfirm(placeName),
    );
  }

  String _getGreeting() {
    final hour = DateTime.now().hour;
    final l10n = AppLocalizations.instance;
    if (hour < 12) return l10n.goodMorning;
    if (hour < 18) return l10n.goodAfternoon;
    return l10n.goodEvening;
  }

  String _getMoodText() {
    final l10n = AppLocalizations.instance;
    switch (_selectedMood) {
      case 0:
        return l10n.t("Bugün sakin bir gün geçireceksin.", "You'll have a calm day today.");
      case 1:
        return l10n.t("Bugün keşif modundasın.", "You're in discovery mode today.");
      case 2:
        return l10n.t("Bugün popüler yerleri keşfedeceksin.", "You'll explore popular places today.");
      default:
        return l10n.t("Bugün keşif modundasın.", "You're in discovery mode today.");
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    super.build(context); // Required for AutomaticKeepAliveClientMixin
    if (_loading) {
      return Scaffold(
        backgroundColor: bgDark,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(8), // Reduced padding
                decoration: BoxDecoration(
                  color: accent,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Image.asset(
                  'assets/images/splash_logo.png',
                  width: 40, // Increased size
                  height: 40, // Increased size
                  fit: BoxFit.contain,
                ),
              ),
              const SizedBox(height: 24),
              const CircularProgressIndicator(
                strokeWidth: 2,
                valueColor: AlwaysStoppedAnimation<Color>(accent),
              ),
            ],
          ),
        ),
      );
    }

    if (_error != null) {
      return Scaffold(
        backgroundColor: bgDark,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(Icons.error_outline, size: 48, color: textGrey),
              const SizedBox(height: 16),
              Text(AppLocalizations.instance.dataLoadError, style: TextStyle(color: textGrey)),
              const SizedBox(height: 16),
              _buildGradientButton(AppLocalizations.instance.tryAgain, () {
                setState(() => _loading = true);
                _loadData();
              }),
            ],
          ),
        ),
      );
    }

    return Scaffold(
      backgroundColor: Colors.transparent, // Transparent for map background
      body: MapBackground(
        child: Stack(
          children: [
            // Ana içerik - CustomScrollView
             NotificationListener<ScrollNotification>(
               onNotification: (notification) {
                 // Trigger Mood tutorial ONLY when scrolling stops
                 if (notification is ScrollEndNotification) {
                    final screenHeight = MediaQuery.of(context).size.height;

                    // 1. Check AI Card Tutorial
                    if (!_isAITutorialShown && _askAiKey.currentContext != null) {
                       final RenderBox? aiBox = _askAiKey.currentContext?.findRenderObject() as RenderBox?;
                       if (aiBox != null) {
                         final position = aiBox.localToGlobal(Offset.zero);
                         // Check if visible
                         if (position.dy > 100 && position.dy < screenHeight - 150) {
                            Scrollable.ensureVisible(
                              _askAiKey.currentContext!,
                              duration: const Duration(milliseconds: 300),
                              curve: Curves.easeInOut,
                              alignment: 0.5,
                            ).then((_) {
                               if (mounted) _showAITutorial();
                            });
                            return false; // Stop checking others
                         }
                       }
                    }

                    // 2. Check Mood Tutorial
                    if (!_isMoodTutorialShown && _moodSelectionKey.currentContext != null) {
                       final RenderBox? box = _moodSelectionKey.currentContext?.findRenderObject() as RenderBox?;
                       if (box != null) {
                         final position = box.localToGlobal(Offset.zero);
                         
                         // If element is visible strictly within screen bounds
                         if (position.dy > 150 && position.dy < screenHeight - 200) {
                            // Ensure it's fully visible and center it before showing
                            Scrollable.ensureVisible(
                              _moodSelectionKey.currentContext!,
                              duration: const Duration(milliseconds: 300),
                              curve: Curves.easeInOut,
                              alignment: 0.5,
                            ).then((_) {
                               if (mounted) _showMoodTutorial();
                            });
                         }
                       }
                    }
                 }
                 return false; 
               },
               child: CustomScrollView(
                key: const PageStorageKey('explore_scroll'),
                controller: _scrollController,
                cacheExtent: 2000,
              physics: const BouncingScrollPhysics(),
              slivers: [
              // Hero Section
              SliverToBoxAdapter(child: _buildHeroSection()),

              // AI Önerileri Kartı
              SliverToBoxAdapter(child: _buildAICard()),
          
              // 🔥 Trending Today
              SliverToBoxAdapter(child: _buildTrendingSection()),

              // 🗺️ Şehir Rehberi Banner'ı (YENİ YER)
              SliverToBoxAdapter(child: _buildCityGuideBanner()),

              // Mood Chips (Vibe Selector)
              SliverToBoxAdapter(child: _buildMoodChips()),

              // Arama
              SliverToBoxAdapter(child: _buildSearchBar()),

              // Kategori Chips
              SliverToBoxAdapter(child: _buildCategoryChips()),

              // Başlık
              SliverToBoxAdapter(child: _buildSectionTitle()),

              // Mekan Listesi
              SliverPadding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 100),
                sliver: SliverList(
                  delegate: SliverChildBuilderDelegate(
                    (context, index) {
                      final place = _filteredHighlights[index];
                      return RepaintBoundary(
                        key: ValueKey("explore_card_${place.name}"),
                        child: _buildPlaceCard(place, index),
                      );
                    },
                    childCount: _filteredHighlights.length,
                    addAutomaticKeepAlives: true,
                    addRepaintBoundaries: false, // Manuel olarak her karta ekledik
                  ),
                ),
              ),
              ],
            ),
          ),
 
          // Floating AI Button
          Positioned(
             right: 20, 
             bottom: 30, 
             child: Container(
               // key: _askAiKey, // Removed to avoid collision with AI Card button
               child: _buildFloatingAIButton(),
             )
          ),
          
          // Scroll-to-top Button
          if (_showScrollToTop)
            Positioned(
              right: 20,
              bottom: 90, // Adjusted to avoid overlap
              child: AnimatedOpacity(
                opacity: _showScrollToTop ? 1.0 : 0.0,
                duration: const Duration(milliseconds: 200),
                child: GestureDetector(
                  onTap: _scrollToTop,
                  child: Container(
                    width: 44,
                    height: 44,
                    decoration: BoxDecoration(
                      color: bgCard.withOpacity(0.8),
                      shape: BoxShape.circle,
                      border: Border.all(color: borderColor.withOpacity(0.5)),
                    ),
                    child: Icon(
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
    ),
  );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // CITY GUIDE BANNER (YENİ)
  // ══════════════════════════════════════════════════════════════════════════

  // ══════════════════════════════════════════════════════════════════════════
  // CITY GUIDE BANNER (YENİ - IMAGE BASED)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildCityGuideBanner() {
    if (_city == null) return const SizedBox.shrink();

    final isEnglish = AppLocalizations.instance.isEnglish;
    final cityName = _city!.getLocalizedCityName(isEnglish);
    // Şehir görselini bul (Artık AIService üzerinden merkezi olarak alınıyor)
    final imageUrl = AIService.getCityImage(_currentCityId);

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      child: GestureDetector(
        onTap: () {
          HapticFeedback.mediumImpact();
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (context) => CityGuideDetailScreen(
                city: cityName,
                imageUrl: imageUrl, 
              ),
            ),
          );
        },
        child: Container(
          height: 160, // Taşma olmaması için yükseklik artırıldı (140 -> 160)
          width: double.infinity,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.4),
                blurRadius: 12,
                offset: const Offset(0, 6),
              ),
            ],
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(20),
            child: Stack(
              fit: StackFit.expand,
              children: [
                Positioned.fill(
                  child: ResilientNetworkImage(
                    imageUrl: imageUrl,
                    placeName: cityName,
                    city: _currentCityId,
                    category: 'guide',
                    height: 160,
                    fit: BoxFit.cover,
                    placeholderBuilder: (_) => Container(color: bgCard),
                  ),
                ),

                Positioned.fill(
                  child: Container(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.centerLeft,
                        end: Alignment.centerRight,
                        colors: [
                          Colors.black.withOpacity(0.9),
                          Colors.black.withOpacity(0.4),
                          Colors.transparent,
                        ],
                        stops: const [0.0, 0.6, 1.0],
                      ),
                    ),
                  ),
                ),

                // 3. İçerik
                Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                              decoration: BoxDecoration(
                                color: accent.withOpacity(0.9),
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Text(
                                isEnglish ? "COMPLETE GUIDE" : "TAM REHBER",
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 10,
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 1.0,
                                ),
                              ),
                            ),
                            const SizedBox(height: 12),
                            Text(
                              isEnglish ? "$cityName Essentials" : "$cityName Hakkında\nHer Şey",
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 22,
                                fontWeight: FontWeight.bold,
                                height: 1.1,
                              ),
                            ),
                            const SizedBox(height: 6),
                            Text(
                              isEnglish ? "Transport, history, stay & all local tips" : "Ulaşım, tarih, konaklama ve tüm lokal ipuçları",
                              style: TextStyle(
                                color: Colors.white.withOpacity(0.8),
                                fontSize: 13,
                              ),
                            ),
                          ],
                        ),
                      ),
                      // Sağdaki ikon (Circular Action Button)
                      Container(
                        width: 50,
                        height: 50,
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.2),
                          shape: BoxShape.circle,
                          border: Border.all(color: Colors.white.withOpacity(0.3), width: 1.5),
                        ),
                        child: const Icon(
                          Icons.arrow_forward_rounded,
                          color: Colors.white,
                          size: 24,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // HERO SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildHeroSection() {
    // Şehir adını normalize et - Türkçe karakterleri de ele al
    String getCityKey(String? cityName) {
      if (cityName == null) return 'barcelona';

      final normalized = cityName
          .toLowerCase()
          .replaceAll('ı', 'i')
          .replaceAll('ü', 'u')
          .replaceAll('ö', 'o')
          .replaceAll('ş', 's')
          .replaceAll('ç', 'c')
          .replaceAll('ğ', 'g')
          .replaceAll('ı', 'i')
          .replaceAll('İ', 'i')
          .replaceAll('ø', 'o') // Fix for Tromsø
          .replaceAll('å', 'a')
          .replaceAll('æ', 'ae')
          .replaceAll(' ', '');

      // Özel eşleşmeler
      final aliases = {
        'istanbul': 'istanbul',
        'İstanbul': 'istanbul',
        'sevilla': 'sevilla',
        'Sevilla': 'sevilla',
        'new york': 'newyork',
        'seul': 'seul',
        'seoul': 'seul',
      };

      return aliases[cityName] ?? aliases[normalized] ?? normalized;
    }

    final cityKey = getCityKey(_city?.city);
    const String kHeroPoolFallback =
        'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800';
    final poolUrl = AIService.getCityImage(cityKey);
    final imageUrl = poolUrl != kHeroPoolFallback
        ? poolUrl
        : (_city?.heroImage ?? poolUrl);

    return Container(
      height: 320,
      margin: const EdgeInsets.fromLTRB(16, 0, 16, 0),
      child: Stack(
        children: [
          // Şehir Görseli
          ClipRRect(
            borderRadius: BorderRadius.circular(24),
            child: SizedBox(
              width: double.infinity,
              height: 320,
              child: ResilientNetworkImage(
                key: ValueKey<String>('explore_hero_${_currentCityId}_$imageUrl'),
                imageUrl: imageUrl,
                placeName: _city?.city ?? cityKey,
                city: cityKey,
                category: 'city',
                height: 320,
                fit: BoxFit.cover,
                fadeInDuration: Duration.zero,
                placeholderBuilder: (context) => Container(
                  decoration: BoxDecoration(color: accent),
                  child: const Center(
                    child: CircularProgressIndicator(
                      color: Colors.white,
                      strokeWidth: 2,
                    ),
                  ),
                ),
              ),
            ),
          ),

          // Gradient Overlay
          ClipRRect(
            borderRadius: BorderRadius.circular(24),
            child: Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [Colors.transparent, Colors.black.withOpacity(0.7)],
                ),
              ),
            ),
          ),

          // Şehir Seçici (Sol üst)
          Positioned(
            top: MediaQuery.of(context).padding.top + 12,
            left: 16,
            child: GestureDetector(
              key: _citySelectKey, // 🔥 KEY EKLENDİ
              onTap: () async {
                final result = await CitySwitcherScreen.showAsModal(context);
                if (result != null && mounted) {
                  // Eğer "Henüz Karar Vermedim" seçildiyse pop-up göster
                  _checkAndShowCitySuggestion();
                }
              },
              child: ClipRRect(
                borderRadius: BorderRadius.circular(20),
                child: BackdropFilter(
                  filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                  child: Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 14,
                      vertical: 8,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.15),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: Colors.white.withOpacity(0.2)),
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Image.asset(
                          'assets/icons/icon_sehirsec.png',
                          width: 28,
                          height: 28,
                        ),
                        const SizedBox(width: 8),
                        Text(
                          AppLocalizations.instance.translateCity(_city?.city ?? AppLocalizations.instance.city),
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 14,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                        const SizedBox(width: 4),
                        const Icon(
                          Icons.keyboard_arrow_down,
                          color: Colors.white,
                          size: 20,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),

          // PRO Button (Sağ üst)
          Positioned(
            top: MediaQuery.of(context).padding.top + 12,
            right: 16,
            child: ListenableBuilder(
              listenable: PremiumService.instance,
              builder: (context, child) {
                final isPremium = PremiumService.instance.isPremium;
                
                return GestureDetector(
                  onTap: () {
                    HapticFeedback.mediumImpact();
                    if (!isPremium) {
                      showPaywall(context);
                    }
                  },
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(20),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.15), 
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(color: Colors.white.withOpacity(0.2)),
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              isPremium ? Icons.verified_rounded : Icons.star_rounded, 
                              color: Colors.white, 
                              size: 18
                            ),
                            const SizedBox(width: 6),
                            Text(
                              isPremium ? 'PRO' : 'FREE',
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 14,
                                fontWeight: FontWeight.w800,
                                letterSpacing: 0.5,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
          ),



          // Premium Başlık (Alt kısım)
          Positioned(
            left: 20,
            bottom: 24,
            right: 20,
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.end,
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        AppLocalizations.instance.isEnglish ? "Discovering" : "Keşfediliyor",
                        style: TextStyle(
                          color: Colors.white.withOpacity(0.9),
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          letterSpacing: 1.2,
                          fontFamily: WanderlustTypography.accentFont,
                        ),
                      ),
                      const SizedBox(height: 2),
                      Text(
                        AppLocalizations.instance.translateCity(_city?.city ?? AppLocalizations.instance.city),
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 36,
                          fontWeight: FontWeight.w800,
                          letterSpacing: -1.0,
                          height: 1.1,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: [
                          Container(
                            width: 4,
                            height: 4,
                            decoration: const BoxDecoration(
                              color: WanderlustColors.accent,
                              shape: BoxShape.circle,
                            ),
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              AppLocalizations.instance.isEnglish ? "Curating your unique journey" : "Sana özel rota deneyimi",
                              style: TextStyle(
                                color: Colors.white.withOpacity(0.85),
                                fontSize: 15,
                                fontFamily: WanderlustTypography.bodyFont,
                                fontWeight: FontWeight.w400,
                              ),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 12),
                // Kaybolan Valiz ve Pasaport İkonu Geri Döndü!
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.15),
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.white.withOpacity(0.2), width: 1),
                  ),
                  child: Image.asset(
                    'assets/icons/gezgin.png',
                    height: 44,
                    width: 44,
                    color: Colors.white,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // AI CARD
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildAICard() {
    // İlgi alanlarını formatlı göster
    String interestsPreview = _interests.isEmpty
        ? AppLocalizations.instance.basedOnInterests
        : _interests.take(2).join(", ");

    // Eğer yanıt var ve kart kapalıysa küçük versiyon göster
    if (_aiChatResponse != null && !_aiCardExpanded) {
      return _buildCollapsedAICard(interestsPreview);
    }

    return AnimatedContainer(
      key: _askAiKey, // 🔥 KEY moved here for full card highlight
      duration: const Duration(milliseconds: 300),
      margin: const EdgeInsets.fromLTRB(16, 12, 16, 0),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(24),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 15, sigmaY: 15),
          child: Container(
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.45),
              borderRadius: BorderRadius.circular(24),
              border: Border.all(color: Colors.white.withOpacity(0.6), width: 1.2),
            ),
            child: Stack(
              children: [
                // Background Symbols
                _buildGlassSymbols(),
                
                // Content
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Header
                      Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(2), // Less padding to make the symbol larger
                            decoration: BoxDecoration(
                              color: accent,
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: Image.asset(
                              'assets/images/splash_logo.png',
                              width: 24, // Increased from 18
                              height: 24, // Increased from 18
                              fit: BoxFit.contain,
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  _aiChatResponse != null 
                                    ? "Keşfetmeye nereden başlayalım?" 
                                    : AppLocalizations.instance.aiRecommendations,
                                  style: const TextStyle(
                                    color: textWhite,
                                    fontSize: 16,
                                    fontWeight: FontWeight.w700,
                                    letterSpacing: -0.5,
                                  ),
                                ),
                                const SizedBox(height: 4),
                                Row(
                                  children: [
                                    Flexible(
                                      child: Text(
                                        _interests.isNotEmpty 
                                          ? AppLocalizations.instance.t("Senin tercihlerine göre öneriler", "Suggestions based on your interests")
                                          : AppLocalizations.instance.t("Kişiselleştirilmiş öneriler", "Personalized suggestions"),
                                        style: TextStyle(
                                          color: accent.withOpacity(0.9),
                                          fontSize: 11,
                                          fontWeight: FontWeight.w500,
                                        ),
                                        overflow: TextOverflow.ellipsis,
                                        maxLines: 1,
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                          // Yenile butonu — öneri ikonu (ilk CTA ile aynı)
                          if (_aiChatResponse != null && !_aiLoading)
                            GestureDetector(
                              onTap: () {
                                HapticFeedback.lightImpact();
                                // Cache'i temizle ve yeniden üret
                                _aiChatCache.remove(_currentCityId);
                                setState(() => _aiChatResponse = null);
                                _fetchAIChatResponse(variation: DateTime.now().millisecond);
                              },
                              child: Container(
                                padding: const EdgeInsets.all(8),
                                margin: const EdgeInsets.only(right: 8),
                                decoration: BoxDecoration(
                                  color: Colors.white.withOpacity(0.1),
                                  borderRadius: BorderRadius.circular(10),
                                ),
                                child: Image.asset(
                                  'assets/icons/icon_oneri.png',
                                  width: 20,
                                  height: 20,
                                  fit: BoxFit.contain,
                                ),
                              ),
                            ),
                          // Küçült butonu (sadece yanıt varsa göster)
                          if (_aiChatResponse != null)
                            GestureDetector(
                              onTap: () {
                                HapticFeedback.lightImpact();
                                setState(() => _aiCardExpanded = false);
                              },
                              child: Container(
                                padding: const EdgeInsets.all(8),
                                decoration: BoxDecoration(
                                  color: Colors.white.withOpacity(0.1),
                                  borderRadius: BorderRadius.circular(10),
                                ),
                                child: Icon(
                                  Icons.keyboard_arrow_up_rounded,
                                  color: textWhite.withOpacity(0.7),
                                  size: 22,
                                ),
                              ),
                            ),
                        ],
                      ),


                      const SizedBox(height: 12),

                      // AI Response veya Buton
                      if (_aiLoading)
                        _buildAILoadingState()
                      else if (_aiChatResponse != null)
                        _buildAIResponseState()
                      else
                        _buildAIInitialState(),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildGlassSymbols() {
    return Positioned.fill(
      child: Opacity(
        opacity: 0.25,
        child: Stack(
          children: [
            Positioned(
              right: -10,
              top: -10,
              child: Transform.rotate(
                angle: 0.2,
                child: const Icon(Icons.flight_takeoff_rounded, size: 64, color: WanderlustColors.accent),
              ),
            ),
            Positioned(
              left: -15,
              bottom: -10,
              child: Transform.rotate(
                angle: -0.1,
                child: const Icon(Icons.luggage_rounded, size: 54, color: WanderlustColors.accent),
              ),
            ),
            Positioned(
              right: 40,
              bottom: -20,
              child: const Icon(Icons.confirmation_number_rounded, size: 44, color: WanderlustColors.accent),
            ),
            Positioned(
              left: 30,
              top: 40,
              child: Transform.rotate(
                angle: 0.5,
                child: const Icon(Icons.train_rounded, size: 32, color: Colors.white10),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildCollapsedAICard(String interestsPreview) {
    return Container(
      margin: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 12, sigmaY: 12),
          child: GestureDetector(
            onTap: () {
              HapticFeedback.lightImpact();
              setState(() => _aiCardExpanded = true);
            },
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.08),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: Colors.white.withOpacity(0.12)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                        Container(
                          padding: const EdgeInsets.all(2),
                          decoration: BoxDecoration(
                            color: accent,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(10),
                            child: Image.asset(
                              'assets/images/splash_logo.png',
                              width: 24,
                              height: 24,
                              fit: BoxFit.cover,
                            ),
                          ),
                        ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              "Keşfetmeye nereden başlayalım?",
                              style: const TextStyle(
                                color: textWhite,
                                fontSize: 14,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                            Text(
                              "Şehrin ritmine uygun gizli hazineler bul veya takvimine tam uyan bir günlük plan hazırla",
                              style: TextStyle(
                                color: accent.withOpacity(0.9),
                                fontSize: 10,
                                fontWeight: FontWeight.w500,
                              ),
                            ),
                          ],
                        ),
                      ),
                      const Icon(
                        Icons.keyboard_arrow_down_rounded,
                        color: Colors.white60,
                        size: 22,
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Row(
                    children: [
                      // Yenile Butonu
                      Expanded(
                        child: GestureDetector(
                          onTap: () {
                            HapticFeedback.mediumImpact();
                            _aiChatCache.remove(_currentCityId);
                            setState(() => _aiChatResponse = null);
                            _fetchAIChatResponse(variation: DateTime.now().millisecond);
                          },
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 8),
                            decoration: BoxDecoration(
                              color: Colors.white.withOpacity(0.1),
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: accent.withOpacity(0.3)),
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/icons/icon_oneri.png',
                                  width: 16,
                                  height: 16,
                                  fit: BoxFit.contain,
                                ),
                                const SizedBox(width: 6),
                                const Text(
                                  "Yenile",
                                  style: TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 10),
                      // Günlük Plan Butonu
                      Expanded(
                        child: GestureDetector(
                          onTap: () {
                            HapticFeedback.mediumImpact();
                            _generateMagicPlan();
                          },
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 8),
                            decoration: BoxDecoration(
                              color: Colors.white.withOpacity(0.1),
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: accent.withOpacity(0.3)),
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Image.asset(
                                  'assets/icons/icon_gunluk.png',
                                  width: 16,
                                  height: 16,
                                  fit: BoxFit.contain,
                                ),
                                const SizedBox(width: 6),
                                Text(
                                  AppLocalizations.instance.buildSmartItinerary.split(' ')[0] + ' Planı',
                                  style: const TextStyle(color: textWhite, fontSize: 11, fontWeight: FontWeight.w600),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildAIInitialState() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          AppLocalizations.instance.preparingRecommendations(AppLocalizations.instance.translateCity(_city?.city ?? AppLocalizations.instance.city), _tripDays),
          style: const TextStyle(
            color: textGrey,
            fontSize: 14,
            height: 1.5,
          ),
        ),
        const SizedBox(height: 16),
        Row(
          children: [
            Expanded(
              child: GestureDetector(
                onTap: () {
                  HapticFeedback.mediumImpact();
                  // 📊 Analytics: Öneri butonu tıklama logu
                  NotificationService().logEvent('suggestion_button_clicked', parameters: {
                    'city_id': _currentCityId,
                  });
                  _fetchAIChatResponse(variation: DateTime.now().millisecond);
                },
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(12),
                  child: BackdropFilter(
                    filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: accent.withOpacity(0.4)),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Image.asset('assets/icons/icon_oneri.png', width: 24, height: 24),
                          const SizedBox(width: 6),
                          Flexible(
                            child: FittedBox(
                              fit: BoxFit.scaleDown,
                              alignment: Alignment.centerLeft,
                              child: Text(
                                AppLocalizations.instance.askAI,
                                maxLines: 1,
                                softWrap: false,
                                style: const TextStyle(
                                  color: textWhite,
                                  fontSize: 13,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 12),
            Expanded(
              child: GestureDetector(
                onTap: () {
                  HapticFeedback.mediumImpact();
                  _generateMagicPlan();
                },
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(12),
                  child: BackdropFilter(
                    filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                        border: Border.all(color: accent.withOpacity(0.4)),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Image.asset('assets/icons/icon_gunluk.png', width: 24, height: 24),
                          const SizedBox(width: 6),
                          Flexible(
                            child: FittedBox(
                              fit: BoxFit.scaleDown,
                              alignment: Alignment.centerLeft,
                              child: Text(
                                AppLocalizations.instance.buildSmartItinerary,
                                maxLines: 1,
                                softWrap: false,
                                style: const TextStyle(
                                  color: textWhite,
                                  fontSize: 13,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Future<void> _generateMagicPlan() async {
    final prefs = await SharedPreferences.getInstance();
    final cityId = prefs.getString("selectedCity") ?? _city?.city.toLowerCase() ?? "barcelona";

    // Free trial: 1 free use per city, then paywall for non-premium
    final trialCount = prefs.getInt("itinerary_trial_count_${cityId.toLowerCase()}") ?? 0;
    final hasUsedAiPlan = trialCount >= 1;

    if (hasUsedAiPlan && !PremiumService.instance.isPremium) {
      if (!mounted) return;
      showPaywall(context, onSubscribe: (planId) async {
        if (mounted) setState(() {});
      });
      return;
    }

    if (!mounted) return;
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => AnalysisLoadingScreen(cityId: cityId),
      ),
    );
  }

  Widget _buildAILoadingState() {
    return Column(
      children: [
        const SizedBox(height: 20),
        const Center(
          child: SizedBox(
            width: 28,
            height: 28,
            child: CircularProgressIndicator(
              color: accent,
              strokeWidth: 2.5,
            ),
          ),
        ),
        const SizedBox(height: 16),
        Text(
          AppLocalizations.instance.preparingForYou,
          style: TextStyle(color: textWhite.withOpacity(0.9), fontSize: 14),
        ),
        const SizedBox(height: 20),
      ],
    );
  }

  Widget _buildAIResponseState() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // AI Response - Markdown benzeri render
        _buildFormattedResponse(_aiChatResponse!),
      ],
    );
  }

  Widget _buildFormattedResponse(String response) {
    // 1. Ayrıştırma (Parsing)
    final parsedData = _parseAIResponse(response);
    final String intro = parsedData['intro'] as String;
    final String tip = parsedData['tip'] as String;
    final List<RecommendationItem> items = parsedData['items'] as List<RecommendationItem>;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Intro Text (Markdown olarak render et, belki bold vs vardır)
        if (intro.isNotEmpty)
          Padding(
            padding: const EdgeInsets.only(bottom: 16),
            child: MarkdownBody(
              data: intro,
              styleSheet: _getMarkdownStyle(),
              onTapLink: (text, href, title) {
                if (href != null && href.startsWith('search:')) {
                  _navigateToPlaceDetail(Uri.decodeComponent(href.substring(7)));
                } else if (href != null) {
                   launchUrl(Uri.parse(href));
                }
              },
            ),
          ),

        // Recommendation Cards (Görsel Kartlar)
        if (items.isNotEmpty)
          ...items.map((item) => _buildRecommendationCard(item)),

        // Tip Section (İpucu)
        if (tip.isNotEmpty)
          Container(
            margin: const EdgeInsets.only(top: 8),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.1),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: WanderlustColors.accent.withOpacity(0.2),
              ),
            ),
            child: MarkdownBody(
              data: tip, // **İpucu:** kısmı burada geliyor zaten
              styleSheet: _getMarkdownStyle(),
              onTapLink: (text, href, title) {
                if (href != null && href.startsWith('search:')) {
                  _navigateToPlaceDetail(Uri.decodeComponent(href.substring(7)));
                } else if (href != null) {
                   launchUrl(Uri.parse(href));
                }
              },
            ),
          ),
      ],
    );
  }

  // Markdown Stili (Ortak)
  MarkdownStyleSheet _getMarkdownStyle() {
    return MarkdownStyleSheet(
      p: TextStyle(
        color: textWhite.withOpacity(0.9),
        fontSize: 15,
        height: 1.6,
        letterSpacing: 0.2,
      ),
      strong: const TextStyle(
        color: WanderlustColors.accent,
        fontWeight: FontWeight.w700,
        fontSize: 15,
      ),
      blockSpacing: 12.0,
    );
  }

  // Tekil Öneri Kartı
  Widget _buildRecommendationCard(RecommendationItem item) {
    // 1. Resmi bulmaya çalış
    String? imageUrl;
    Highlight? place;
    
    if (_city != null) {
      try {
        place = _city!.highlights.firstWhere(
          (h) => h.name.toLowerCase().contains(item.query.toLowerCase()) || 
                 item.query.toLowerCase().contains(h.name.toLowerCase()),
        );
        imageUrl = place.imageUrl;
      } catch (_) {
        // Resim bulunamazsa null kalır
      }
    }

    // Yedek resim (Şehir resmi veya fallback)
    imageUrl ??= _city?.heroImage ?? 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1';

    return GestureDetector(
      onTap: () {
        if (place != null) {
          // Navigation

          Navigator.push(
            context,
            MaterialPageRoute(
               builder: (context) => DetailScreen(place: place!),
            ),
          );
        } else {
             // Bulunamadıysa toast göster
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                content: Text(AppLocalizations.instance.placeNotFound(item.name)),
                backgroundColor: Colors.redAccent,
              ),
            );
        }
      },
      child: ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(
            margin: const EdgeInsets.only(bottom: 20),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.6),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(
                color: Colors.white.withOpacity(0.8),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.06),
                  blurRadius: 15,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            clipBehavior: Clip.antiAlias,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Resim Alanı
            SizedBox(
              height: 150,
              width: double.infinity,
              child: Stack(
                fit: StackFit.expand,
                children: [
                  Positioned.fill(
                    child: ResilientNetworkImage(
                      imageUrl: imageUrl,
                      placeName: item.name,
                      city: _city?.city ?? _currentCityId,
                      category: place?.category ?? 'Genel',
                      blurHash: place?.blurHash,
                      height: 150,
                      fit: BoxFit.cover,
                      placeholderBuilder: (_) =>
                          Container(color: Colors.white.withOpacity(0.1)),
                    ),
                  ),
                  Positioned.fill(
                    child: Container(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.transparent,
                            Colors.black.withOpacity(0.4),
                          ],
                        ),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            
            // İçerik Alanı
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                   // Başlık + İkon
                   Row(
                     children: [
                       Expanded(
                         child: Text(
                           item.name,
                           style: const TextStyle(
                             color: WanderlustColors.accent,
                             fontSize: 17,
                             fontWeight: FontWeight.bold,
                           ),
                         ),
                       ),
                       const Icon(
                         Icons.arrow_forward_ios_rounded,
                         color: textGrey,
                         size: 14,
                       ),
                     ],
                   ),
                   const SizedBox(height: 8),
                   // Açıklama
                   Text(
                     item.description,
                     style: TextStyle(
                       color: textWhite.withOpacity(0.85),
                       fontSize: 14,
                       height: 1.5,
                     ),
                   ),
                 ],
               ),
             ),
           ],
         ),
       ),
     ),
   ),
);
  }

  // AI Yanıtını Ayrıştırıcı
  Map<String, dynamic> _parseAIResponse(String response) {
    String intro = "";
    String tip = "";
    List<RecommendationItem> items = [];

    // Pre-processing: AI bazen linklerin arasına gereksiz boşluk/satır sonu ekleyebiliyor
    String cleanedResponse = response.replaceAll(RegExp(r'\]\s*\n\s*\('), '](');
    // Bulletları normalize et (* veya • yerine - yap)
    cleanedResponse = cleanedResponse.replaceAll(RegExp(r'^[ \t]*[•*+]\s*', multiLine: true), '- ');

    // 1. İpucunu ayır (Tip veya İpucu)
    // AI Service formatı: ... \n\n**Tip:** Text
    final tipRegex = RegExp(r'\*\*(Tip|İpucu):\*\*\s*(.*)', dotAll: true);
    final tipMatch = tipRegex.firstMatch(cleanedResponse);
    
    String mainContent = cleanedResponse;
    if (tipMatch != null) {
      tip = "**${tipMatch.group(1)}:** ${tipMatch.group(2)?.trim()}";
      mainContent = cleanedResponse.substring(0, tipMatch.start).trim();
    }
    // Öneriler "- [Name](search:...) - " ile başlar
    // Bu patternin ilk görüldüğü yerden öncesi introdur.
    final listStartRegex = RegExp(r'-\s*\[');
    final firstListMatch = listStartRegex.firstMatch(mainContent);

    if (firstListMatch != null) {
      intro = mainContent.substring(0, firstListMatch.start).trim();
      final recommendationsSection = mainContent.substring(firstListMatch.start);

      // 3. Önerileri tek tek parse et
      // Regex: - [Display Name](search:Query) - Description
      // Not: Description multilne olabilir, bir sonraki "- [" gelene kadar almalıyız.
      final itemRegex = RegExp(r'-\s*\[(.*?)\]\s*\(search:(.*?)\)\s*-\s*(.*?)(?=\n-|$)', dotAll: true);
      
      final matches = itemRegex.allMatches(recommendationsSection);
      for (final match in matches) {
        if (match.groupCount >= 3) {
          items.add(RecommendationItem(
            name: match.group(1)?.trim() ?? "",
            query: match.group(2)?.trim() ?? "",
            description: match.group(3)?.trim() ?? "",
          ));
        }
      }

    } else {
      // Liste bulunamadıysa hepsi introdur
      intro = mainContent;
    }

    return {
      'intro': intro,
      'tip': tip,
      'items': items,
    };
  }

  void _navigateToPlaceDetail(String query) async {
    try {
      String? targetCity;
      String searchPlace = query;

      // 1. Önce mevcut şehri dene
      Highlight? foundPlace;
      if (_city != null) {
        try {
          foundPlace = _city!.highlights.firstWhere(
            (h) => h.name.toLowerCase().trim() == searchPlace.toLowerCase().trim() || 
                   searchPlace.toLowerCase().contains(h.name.toLowerCase().trim()) ||
                   h.name.toLowerCase().contains(searchPlace.toLowerCase().trim())
          );
        } catch (_) {}
      }

      // 2. Bulunamadıysa cross-city ara
      if (foundPlace == null) {
        // Query içinde şehir adı var mı kontrol et
        final allCities = CityDataLoader.supportedCities;
        for (var cityId in allCities) {
          if (query.toLowerCase().contains(cityId)) {
            targetCity = cityId;
            break;
          }
        }

        List<String> citiesToSearch = targetCity != null 
            ? [targetCity] 
            : ['roma', 'paris', 'barcelona', 'istanbul', 'londra', 'viyana', 'prag', 'lizbon', 'rovaniemi', 'matera', 'sintra', 'colmar'];
        
        for (var cityId in citiesToSearch) {
          if (_city != null && cityId == _currentCityId) continue;
          final cityModel = await CityDataLoader.loadCity(cityId);
          try {
            foundPlace = cityModel.highlights.firstWhere(
              (h) => h.name.toLowerCase().trim() == searchPlace.toLowerCase().trim() || 
                     searchPlace.toLowerCase().contains(h.name.toLowerCase().trim()) ||
                     h.name.toLowerCase().contains(searchPlace.toLowerCase().trim())
            );
            if (foundPlace != null) break;
          } catch (_) {}
        }
      }

      if (foundPlace != null && mounted) {
        // Navigation

        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: foundPlace!)),
        );
      } else {
         ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(AppLocalizations.instance.placeNotFound(query)),
            backgroundColor: Colors.redAccent,
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    } catch (e) {
      debugPrint('Place navigation error: $e');
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TRENDING TODAY SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildPlaceholderImage(String category) {
    final color = _getCategoryColor(category);
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [color.withOpacity(0.8), color.withOpacity(0.5)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
      ),
      child: Center(
        child: Icon(
          _getCategoryIcon(category),
          color: Colors.white.withOpacity(0.7),
          size: 32,
        ),
      ),
    );
  }

  Color _getCategoryColor(String category) {
    switch (category) {
      case 'Cafe': return const Color(0xFF8B4513);
      case 'Restoran': return const Color(0xFFE74C3C);
      case 'Bar': return const Color(0xFF9B59B6);
      case 'Müze': return const Color(0xFF3498DB);
      case 'Park': return const Color(0xFF27AE60);
      case 'Tarihi': return const Color(0xFFF39C12);
      case 'Manzara': return const Color(0xFF1ABC9C);
      case 'Deneyim': return const Color(0xFFE91E63);
      case 'Alışveriş': return const Color(0xFFFF9800);
      default: return accent;
    }
  }

  IconData _getCategoryIcon(String category) {
    switch (category) {
      case 'Cafe': return Icons.local_cafe_rounded;
      case 'Restoran': return Icons.restaurant_rounded;
      case 'Bar': return Icons.local_bar_rounded;
      case 'Müze': return Icons.museum_rounded;
      case 'Park': return Icons.park_rounded;
      case 'Tarihi': return Icons.account_balance_rounded;
      case 'Manzara': return Icons.landscape_rounded;
      case 'Deneyim': return Icons.explore_rounded;
      case 'Alışveriş': return Icons.shopping_bag_rounded;
      default: return Icons.place_rounded;
    }
  }

  Widget _buildTrendingSection() {
    final trendingPlaces = TrendingService.getTrendingPlaces(_allHighlights, limit: 8);
    if (trendingPlaces.isEmpty) return const SizedBox.shrink();

    final isEnglish = AppLocalizations.instance.isEnglish;
    final title = TrendingService.getTrendingTitle(isEnglish: isEnglish);
    final emoji = TrendingService.getDayPeriodEmoji();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Başlık
        Padding(
          padding: const EdgeInsets.fromLTRB(20, 24, 20, 12),
          child: Row(
            children: [
              Text(
                title,
                style: const TextStyle(
                  color: textWhite,
                  fontSize: 18,
                  fontWeight: FontWeight.w700,
                ),
              ),
              const Spacer(),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: accent.withOpacity(0.15),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Image.asset('assets/icons/icon_lively.png', width: 16, height: 16),
                    const SizedBox(width: 4),
                    Text(
                      isEnglish ? 'Live' : 'Canlı',
                      style: TextStyle(
                        color: accent,
                        fontSize: 12,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),

        // Horizontal scroll kartları
        // Horizontal liste önceki şehirdeki scroll offset'ini tutmasın.
        SizedBox(
          key: ValueKey<String>('explore_trending_h_${_currentCityId}'),
          height: 200,
          child: ListView.builder(
            scrollDirection: Axis.horizontal,
            physics: const BouncingScrollPhysics(),
            padding: const EdgeInsets.symmetric(horizontal: 16),
            itemCount: trendingPlaces.length,
            itemBuilder: (context, index) => _buildTrendingCard(trendingPlaces[index], index),
          ),
        ),
      ],
    );
  }

  Widget _buildTrendingCard(Highlight place, int index) {
    final placeKey = "$_currentCityId:${place.name}";
    final isFavorite = _favorites.contains(place.name) || _favorites.contains(placeKey);

    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        // 📊 Analytics: Mekan tıklama logu
        NotificationService().logEvent('place_card_clicked', parameters: {
          'place_name': place.name,
          'city_id': _currentCityId,
          'index': index,
        });
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
        );
      },
      child: Container(
        width: 160,
        margin: EdgeInsets.only(right: 12, left: index == 0 ? 4 : 0),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Stack(
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Görsel
                ClipRRect(
                  borderRadius: const BorderRadius.vertical(top: Radius.circular(16)),
                  child: SizedBox(
                    height: 100,
                    width: double.infinity,
                    child: place.imageUrl != null && place.imageUrl!.isNotEmpty
                        ? CachedNetworkImage(
                            imageUrl: place.imageUrl!,
                            fit: BoxFit.cover,
                            cacheManager: AppImageCacheManager.instance,
                            fadeInDuration: Duration.zero,
                            fadeOutDuration: Duration.zero,
                            placeholderFadeInDuration: Duration.zero,
                            placeholder: (_, __) => _buildPlaceholderImage(place.category),
                            errorWidget: (_, __, ___) => _buildPlaceholderImage(place.category),
                          )
                        : _buildPlaceholderImage(place.category),
                  ),
                ),

                // İçerik
                Padding(
                  padding: const EdgeInsets.all(10),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        place.getLocalizedName(isEnglish),
                        style: const TextStyle(
                          color: textWhite,
                          fontSize: 13,
                          fontWeight: FontWeight.w600,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 4),
                      Row(
                        children: [
                          Icon(Icons.location_on_outlined, color: textGrey, size: 12),
                          const SizedBox(width: 2),
                          Expanded(
                            child: Text(
                              place.getLocalizedArea(isEnglish).isNotEmpty ? place.getLocalizedArea(isEnglish) : (place.city ?? ""),
                              style: const TextStyle(color: textGrey, fontSize: 11),
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 6),
                      Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                            decoration: BoxDecoration(
                              color: Colors.black.withOpacity(0.3), // Glass style
                              borderRadius: BorderRadius.circular(6),
                              border: Border.all(color: Colors.white.withOpacity(0.2), width: 0.5),
                            ),
                            child: Text(
                              AppLocalizations.instance.translateCategory(place.category),
                              style: const TextStyle(
                                color: Colors.white, // White Text
                                fontSize: 10,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                          const Spacer(),
                          if (place.rating != null) ...[
                            const Icon(
                              Icons.star_rounded,
                              color: Color(0xFFFDCB6E), // Amber
                              size: 12,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              place.rating!.toStringAsFixed(1),
                              style: const TextStyle(
                                color: textWhite,
                                fontSize: 11,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ],
                      ),
                    ],
                  ),
                ),
              ],
            ),

            // Trend sırası badge
            Positioned(
              top: 8,
              left: 8,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                decoration: BoxDecoration(
                  color: Colors.black.withOpacity(0.7),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  '#${index + 1}',
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 10,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ),

            // Favori ikonu
            Positioned(
              top: 8,
              right: 8,
              child: GestureDetector(
                onTap: () => _toggleFavorite(place.name),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(20),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.3),
                          shape: BoxShape.circle,
                          border: Border.all(color: Colors.white.withOpacity(0.2), width: 0.5),
                        ),
                        child: Icon(
                          isFavorite ? Icons.favorite : Icons.favorite_border,
                          color: isFavorite ? accent : Colors.white,
                          size: 14,
                        ),
                      ),
                    ),
                  ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SEARCH BAR
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSearchBar() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 14, 20, 0),
      height: 50,
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: TextField(
        controller: _searchController,
        onChanged: (v) {
          setState(() => _searchQuery = v);
          _applyFilters();
          
          // --- ANALYTICS DEBOUNCE ---
          _searchTimer?.cancel();
          if (v.length >= 3) {
            _searchTimer = Timer(const Duration(seconds: 1), () {
              AnalyticsService.instance.logSearch(v);
            });
          }
        },
        style: const TextStyle(color: textWhite, fontSize: 15),
        decoration: InputDecoration(
          hintText: AppLocalizations.instance.searchInCity(AppLocalizations.instance.translateCity(_city?.city ?? AppLocalizations.instance.city)),
          hintStyle: TextStyle(color: textGrey.withOpacity(0.6)),
          prefixIcon: Icon(Icons.search, color: textGrey.withOpacity(0.6)),
          suffixIcon: _searchQuery.isNotEmpty
              ? IconButton(
                  icon: Icon(Icons.close, color: textGrey, size: 20),
                  onPressed: () {
                    _searchController.clear();
                    setState(() => _searchQuery = "");
                    _applyFilters();
                  },
                )
              : null,
          border: InputBorder.none,
          contentPadding: const EdgeInsets.symmetric(
            horizontal: 16,
            vertical: 16,
          ),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // MOOD CHIPS
  // ══════════════════════════════════════════════════════════════════════════

  String _getMoodDescription(int moodId) {
    switch (moodId) {
      case 0: return AppLocalizations.instance.isEnglish ? "Chaos is over, time to relax." : "Kaos bitti, şimdi kafa dinleme zamanı.";
      case 1: return AppLocalizations.instance.onboardingTagline;
      case 2: return AppLocalizations.instance.isEnglish ? "Energy is high! Ride the city rhythm." : "Enerji tavan! Şehrin ritmine kapıl.";
      default: return "";
    }
  }

  Widget _buildMoodChips() {
    final moods = [
      {"id": 0, "label": AppLocalizations.instance.moodCalm, "icon": "assets/icons/icon_sakin.png"},
      {"id": 1, "label": AppLocalizations.instance.moodDiscover, "icon": "assets/icons/icon_kesif.png"},
      {"id": 2, "label": AppLocalizations.instance.moodLively, "icon": "assets/icons/icon_canli.png"},
    ];

    return Column(
      key: _moodSelectionKey, // 🔥 KEY HERE
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.only(left: 20, top: 24, bottom: 12),
          child: AnimatedSwitcher(
            duration: const Duration(milliseconds: 300),
            child: Text(
              _getMoodDescription(_selectedMood).toUpperCase(),
              key: ValueKey<int>(_selectedMood),
              style: TextStyle(
                fontFamily: 'Ubuntu',
                color: textGrey.withOpacity(0.6),
                fontSize: 11,
                fontWeight: FontWeight.w700,
                letterSpacing: 1.5,
              ),
            ),
          ),
        ),

        Container(
          margin: const EdgeInsets.symmetric(horizontal: 20),
          height: 52,
          padding: const EdgeInsets.all(4),
          decoration: BoxDecoration(
            color: textGrey.withOpacity(0.08), // Soft, theme-adaptive background
            borderRadius: BorderRadius.circular(26),
          ),
          child: Stack(
            children: [
              // Premium Slide Pill
              AnimatedAlign(
                duration: const Duration(milliseconds: 350),
                curve: Curves.easeOutCirc,
                alignment: Alignment(
                  -1.0 + (_selectedMood * 1.0), 
                   0.0
                ),
                child: LayoutBuilder(
                  builder: (context, constraints) {
                    return Container(
                      width: constraints.maxWidth / 3,
                      height: double.infinity,
                      decoration: BoxDecoration(
                        color: WanderlustColors.bgCard, // Solid, theme-adaptive pill
                        borderRadius: BorderRadius.circular(22),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.06),
                            blurRadius: 8,
                            spreadRadius: 1,
                            offset: const Offset(0, 3),
                          ),
                          BoxShadow(
                            color: Colors.black.withOpacity(0.04),
                            blurRadius: 2,
                            offset: const Offset(0, 1),
                          ),
                        ],
                      ),
                    );
                  },
                ),
              ),

              // Buttons
              Row(
                children: moods.map((mood) {
                  final isSelected = _selectedMood == mood["id"];
                  return Expanded(
                    child: GestureDetector(
                      onTap: () {
                        HapticFeedback.lightImpact();
                        setState(() => _selectedMood = mood["id"] as int);
                        _applyFilters();
                        _fetchAIRecommendations();
                      },
                      behavior: HitTestBehavior.opaque,
                      child: Center(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            AnimatedContainer(
                              duration: const Duration(milliseconds: 350),
                              curve: Curves.easeOutCirc,
                              margin: const EdgeInsets.only(right: 6),
                              width: isSelected ? 24 : 18,
                              height: isSelected ? 24 : 18,
                              child: AnimatedOpacity(
                                duration: const Duration(milliseconds: 350),
                                opacity: isSelected ? 1.0 : 0.4,
                                child: Image.asset(
                                  mood["icon"] as String,
                                  fit: BoxFit.contain,
                                ),
                              ),
                            ),
                            AnimatedDefaultTextStyle(
                              duration: const Duration(milliseconds: 350),
                              curve: Curves.easeOutCirc,
                              style: TextStyle(
                                fontFamily: 'Ubuntu',
                                color: isSelected ? WanderlustColors.textWhite : WanderlustColors.textGrey.withOpacity(0.8),
                                fontSize: 14,
                                fontWeight: isSelected ? FontWeight.w700 : FontWeight.w600,
                                letterSpacing: 0.2,
                              ),
                              child: Text(
                                AppLocalizations.instance.translateCategory(mood["label"] as String),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  );
                }).toList(),
              ),
            ],
          ),
        ),
      ],
    );
  }



  // ══════════════════════════════════════════════════════════════════════════
  // CATEGORY CHIPS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildCategoryChips() {
    return Container(
      height: 42,
      margin: const EdgeInsets.only(top: 12),
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 20),
        itemCount: _categories.length,
        itemBuilder: (context, index) {
          final cat = _categories[index];
          final isSelected = _selectedCategory == cat["id"];

          return Padding(
            padding: const EdgeInsets.only(right: 10),
            child: GestureDetector(
              onTap: () {
                HapticFeedback.selectionClick();
                // 📊 Analytics: Kategori seçimi logu
                NotificationService().logEvent('category_selected', parameters: {
                  'category': cat["id"],
                  'city_id': _currentCityId,
                });
                setState(() => _selectedCategory = cat["id"]);
                _applyFilters();
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 16),
                decoration: BoxDecoration(
                  color: isSelected ? accent : Colors.transparent,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isSelected ? accent : borderColor,
                    width: 1.2,
                  ),
                ),
                child: Center(
                  child: Text(
                    AppLocalizations.instance.translateCategory(cat["label"]),
                    style: TextStyle(
                      color: isSelected ? Colors.white : textGrey,
                      fontSize: 13.5,
                      fontWeight: isSelected
                          ? FontWeight.w600
                          : FontWeight.w500,
                    ),
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SECTION TITLE
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSectionTitle() {
    String getBaseTitle() {
      switch (_selectedMood) {
        case 0: return AppLocalizations.instance.peacefulCorners;
        case 1: return AppLocalizations.instance.placesToExplore;
        case 2: return AppLocalizations.instance.cityRhythmFun;
        default: return AppLocalizations.instance.popularSpots;
      }
    }

    final title = _selectedCategory != "Tümü"
        ? "${AppLocalizations.instance.translateCategory(_selectedCategory)} (${_filteredHighlights.length})"
        : getBaseTitle();


    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 16),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(
            title,
            style: const TextStyle(
              color: textWhite,
              fontSize: 20,
              fontWeight: FontWeight.w700,
            ),
          ),
          if (_selectedCategory != "Tümü")
            GestureDetector(
              onTap: () {
                setState(() => _selectedCategory = "Tümü");
                _applyFilters();
              },
              child: Text(
                AppLocalizations.instance.clear,
                style: TextStyle(
                  color: accent,
                  fontSize: 14,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ),
        ],
      ),
    );
  }


  // ══════════════════════════════════════════════════════════════════════════
  // PLACE CARD
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildPlaceCard(Highlight place, int index) {
    final placeKey = "$_currentCityId:${place.name}";
    final isFavorite = _favorites.contains(placeKey) || _favorites.contains(place.name);
    final isInTrip = _tripPlaces.contains(place.name);

    return GestureDetector(
      onTap: () {
        // --- ANALYTICS: Landmark Selection ---
        AnalyticsService.instance.logSelectContent(
          contentType: 'landmark',
          itemId: place.name,
        );
        
        // Navigation
        
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(18),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Görsel
            Stack(
              children: [
                ClipRRect(
                  borderRadius: const BorderRadius.vertical(
                    top: Radius.circular(18),
                  ),
                  child: SizedBox(
                    height: 200,
                    width: double.infinity,
                    child: ResilientNetworkImage(
                      imageUrl: place.imageUrl,
                      placeName: place.name,
                      city: place.city ?? _city?.city ?? _currentCityId,
                      category: place.category,
                      blurHash: place.blurHash,
                      fit: BoxFit.cover,
                      placeholderBuilder: (_) => _buildPlaceholder(place.category),
                    ),
                  ),
                ),

                // Gradient overlay
                Container(
                  height: 200,
                  decoration: BoxDecoration(
                    borderRadius: const BorderRadius.vertical(
                      top: Radius.circular(18),
                    ),
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.transparent,
                        Colors.black.withOpacity(0.4),
                      ],
                    ),
                  ),
                ),

                // Favori butonu
                Positioned(
                  top: 12,
                  right: 12,
                  child: GestureDetector(
                    onTap: () => _toggleFavorite(place.name),
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(20),
                        child: BackdropFilter(
                          filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                          child: Container(
                            padding: const EdgeInsets.all(8),
                            decoration: BoxDecoration(
                              color: Colors.black.withOpacity(0.3),
                              shape: BoxShape.circle,
                              border: Border.all(color: Colors.white.withOpacity(0.2), width: 0.5),
                            ),
                            child: Icon(
                              isFavorite ? Icons.favorite : Icons.favorite_border,
                              color: isFavorite ? accent : Colors.white,
                              size: 20,
                            ),
                          ),
                        ),
                      ),
                  ),
                ),

                // Kategori chip
                Positioned(
                  top: 12,
                  left: 12,
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(8),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 10,
                          vertical: 5,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.2), // Neutral transparent background
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: Colors.white.withOpacity(0.6), width: 1), // White transparent border
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(
                              _getCategoryIcon(place.category),
                              color: Colors.white,
                              size: 12,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              AppLocalizations.instance.translateCategory(place.category),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 11,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                ),

                // Rating - tıklanabilir (Google Maps'e yönlendirir - PRO ONLY)
                if (place.rating != null)
                  Positioned(
                    bottom: 12,
                    left: 12,
                    child: GestureDetector(
                      onTap: () async {
                        HapticFeedback.lightImpact();
                        
                        // Premium kontrolü
                        if (!PremiumService.instance.isPremium) {
                          showModalBottomSheet(
                            context: context,
                            isScrollControlled: true,
                            backgroundColor: Colors.transparent,
                            builder: (context) => const PaywallScreen(),
                          );
                          return;
                        }

                        final query = Uri.encodeComponent('${place.name} ${_city?.city ?? ""}');
                        final url = 'https://www.google.com/maps/search/?api=1&query=$query';
                        if (await canLaunchUrl(Uri.parse(url))) {
                          await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
                        }
                      },
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 4,
                          ),
                          decoration: BoxDecoration(
                            color: Colors.black.withOpacity(0.6),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            children: [
                              const Icon(
                                Icons.star_rounded,
                                color: Color(0xFFFDCB6E),
                                size: 14,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                place.rating!.toStringAsFixed(1),
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 12,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ],
                          ),
                        ),
                    ),
                  ),
              // Mesafe — sağ alt köşe (rating gibi)
                Positioned(
                  bottom: 12,
                  right: 12,
                  child: AnimatedBuilder(
                    animation: LocationContextService.instance,
                    builder: (context, child) {
                      String distLabel = "";
                      if (place.lat == 0 && place.lng == 0) {
                        distLabel = "${place.distanceFromCenter.toStringAsFixed(1)} km";
                      } else {
                        distLabel = LocationContextService.instance.getDistanceLabel(place.lat, place.lng);
                      }
                      return Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.6),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          distLabel,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),

            // Bilgi kısmı
            Padding(
              padding: const EdgeInsets.all(14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // İsim
                  Text(
                    place.getLocalizedName(AppLocalizations.instance.isEnglish),
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 6),
                  // Konum + Rotaya Ekle (aynı satır)
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Row(
                        children: [
                          Icon(Icons.location_on_outlined, color: textGrey, size: 14),
                          const SizedBox(width: 4),
                          ConstrainedBox(
                            constraints: const BoxConstraints(maxWidth: 110),
                            child: Text(
                              place.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty
                                  ? place.getLocalizedArea(AppLocalizations.instance.isEnglish)
                                  : (place.city ?? ""),
                              style: TextStyle(color: textGrey, fontSize: 13),
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ],
                      ),
                      GestureDetector(
                        key: null,
                        onTap: () => _addToTrip(place.name),
                        child: Container(
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                          decoration: BoxDecoration(
                            color: isInTrip ? accent.withOpacity(0.15) : bgCardLight,
                            borderRadius: BorderRadius.circular(10),
                            border: Border.all(
                              color: isInTrip ? Colors.transparent : borderColor.withOpacity(0.5),
                              width: 1,
                            ),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                isInTrip ? Icons.check : Icons.add_location_alt_outlined,
                                color: isInTrip ? accent : textGrey,
                                size: 16,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                isInTrip ? AppLocalizations.instance.addedToRoute : AppLocalizations.instance.addToRoute,
                                style: TextStyle(
                                  color: isInTrip ? accent : textGrey,
                                  fontSize: 12,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ],
                          ),
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
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // FLOATING AI BUTTON
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildFloatingAIButton() {
    return GestureDetector(
      key: _aiFabKey,
      onTap: () {
        HapticFeedback.mediumImpact();
        _showAISheet();
      },
      child: Container(
        width: 48,
        height: 48,
        decoration: BoxDecoration(
          color: accent,
          shape: BoxShape.circle,
          boxShadow: [
            BoxShadow(
              color: accent.withOpacity(0.4),
              blurRadius: 16,
              offset: const Offset(0, 6),
            ),
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.all(6), // Reduced padding to make the symbol larger
          child: Image.asset(
            'assets/images/splash_logo.png',
            fit: BoxFit.contain,
          ),
        ),
      ),
    );
  }

  void _showAISheet() {
    // 🔒 PREMIUM CHECK: My Way Assistant
    if (!PremiumService.instance.isPremium) {
       showPaywall(
         context,
         onSubscribe: (planId) {
             // Paywall closes automatically on success, so we just proceed
             // Waiting for a small delay or check is handled by onSubscribe usually
         },
       );
       return;
    }

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (_) => AIChatScreen(
          city: _city,
          aiService: AIService(),
          allHighlights: _allHighlights,
          initialMessages: _savedChatMessages,
          onMessageAdded: (msg) {
            _savedChatMessages.add(msg);
          },
        ),
      ),
    );
  }


  // ══════════════════════════════════════════════════════════════════════════
  // HELPERS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildPlaceholder(String category) {
    return Container(
      color: _getCategoryColor(category).withOpacity(0.2),
      child: Center(
        child: Icon(
          _getCategoryIcon(category),
          size: 40,
          color: _getCategoryColor(category).withOpacity(0.5),
        ),
      ),
    );
  }

  Widget _buildGradientButton(String text, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
        decoration: BoxDecoration(
          color: accent,
          borderRadius: BorderRadius.circular(12),
        ),
        child: Text(
          text,
          style: const TextStyle(
            color: Colors.white,
            fontSize: 14,
            fontWeight: FontWeight.w600,
          ),
        ),
      ),
    );
  }
}

// Helper Class for AI Recommendations
class RecommendationItem {
  final String name;
  final String query;
  final String description;

  RecommendationItem({
    required this.name,
    required this.query,
    required this.description,
  });
}


