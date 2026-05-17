// =============================================================================
// ROUTES SCREEN v4 – WANDERLUST DARK THEME
// Real Google Maps preview + Named waypoints + Trip days from onboarding
// Compatible with city_model.dart v3
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:url_launcher/url_launcher.dart';
import 'dart:math' as math;
import 'dart:ui' as ui;
import 'dart:convert';
import '../services/trip_update_service.dart';
import '../services/badge_service.dart';
import '../l10n/app_localizations.dart';
import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/directions_service.dart'; // Import this if needed or generic logic
import '../utils/map_theme.dart';
import '../services/tutorial_service.dart';
import 'detail_screen.dart';
import '../services/curated_routes_service.dart';
import '../theme/wanderlust_colors.dart';
import '../widgets/map_background.dart';
import '../widgets/amber_background_symbols.dart';
import 'dart:ui'; // For ImageFilter
import '../models/completed_route.dart';
import '../services/premium_service.dart';
import '../services/image_prefetch_service.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../widgets/tutorial_overlay_widget.dart';
import 'paywall_screen.dart';
import '../secrets.dart';
import '../services/smart_itinerary_builder.dart';
import '../services/travel_time_estimator.dart';
import 'analysis_loading_screen.dart';
import '../services/location_context_service.dart';
import '../services/analytics_service.dart'; // Added
import '../widgets/resilient_network_image.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../utils/image_utils.dart';

// =============================================================================
// SUGGESTED ROUTE MODEL
// =============================================================================

class SuggestedRoute {
  final String id;
  final String name;
  final String description;
  final String duration;
  final String distance;
  final String difficulty;
  final String imageUrl;
  final List<String> tags;
  final List<String> placeNames;
  final List<String> interests;
  final Color accentColor;
  final IconData icon;

  const SuggestedRoute({
    required this.id,
    required this.name,
    required this.description,
    required this.duration,
    required this.distance,
    required this.difficulty,
    required this.imageUrl,
    required this.tags,
    required this.placeNames,
    required this.interests,
    required this.accentColor,
    required this.icon,
  });
}

// =============================================================================
// MAIN SCREEN
// =============================================================================

class RoutesScreen extends StatefulWidget {
  final bool isVisible;
  final int initialTabIndex;
  const RoutesScreen({
    super.key, 
    this.isVisible = false,
    this.initialTabIndex = 0,
  });

  @override
  State<RoutesScreen> createState() => _RoutesScreenState();
}

class _RoutesScreenState extends State<RoutesScreen>
    with TickerProviderStateMixin {
  // AMBER/GOLD THEME
  // Local constants removed as we use WanderlustColors globally
  static const Color accent = WanderlustColors.accent; // Purple
  static const Color accentLight = Color(0xFF9E7CFF); // Purple Light
  static const Color accentOrange = Color(0xFFFF9800);
  static const Color accentGreen = Color(0xFF4CAF50);
  static const Color iconColor = WanderlustColors.textWhite;
  static const Color bgCardLight = WanderlustColors.bgCardLight;

  // Tutorial Keys
  final GlobalKey _routesTabKey = GlobalKey();
  final GlobalKey _createRouteButtonKey = GlobalKey();
  final GlobalKey _myRouteStatsKey = GlobalKey();
  final GlobalKey _startRouteButtonKey = GlobalKey();
  
  bool get isEnglish => AppLocalizations.instance.isEnglish;


  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [WanderlustColors.accent, WanderlustColors.accent],
  );

  static const LinearGradient greenGradient = LinearGradient(
    colors: [Color(0xFF4CAF50), Color(0xFF4CAF50)],
  );


  // Google Maps API Key - Buraya kendi API key'inizi ekleyin
  // https://console.cloud.google.com/google/maps-apis/credentials
  static String get _googleMapsApiKey => Secrets.googleMapsApiKey;

  CityModel? _city;
  bool _loading = true;
  String _travelStyle = "Lokal";
  List<String> _interests = [];
  List<String> _tripPlaceNames = [];
  List<Highlight> _tripPlaces = [];
  Map<int, List<Highlight>> _dayPlans = {};
  Map<String, String> _placeCityMap = {}; // Yer adı -> şehir adı mapping
  int _totalDays = 1;
  int _tripDays = 3; // Onboarding'den gelen gün sayısı
  List<SuggestedRoute> _allSuggestedRoutes = [];
  List<SuggestedRoute> _filteredSuggestedRoutes = [];
  bool _showMapPreview = true;

  // Interactive Map State
  GoogleMapController? _routeMapController;
  Set<Marker> _routeMarkers = {};
  Set<Polyline> _routePolylines = {};
  final ScrollController _myRouteScrollController = ScrollController();
  
  bool _isAiPlan = false;

  late TabController _mainTabController;
  TabController? _dayTabController;
  int _selectedRouteFilter = 0; // 0: Tümü, 1: Bana Özel, 2: Popüler
  int _selectedTransportMode = 0; // 0 = walk, 1 = transit, 2 = car

  // Transit API Cache
  int? _transitTimeCache;
  bool _transitLoading = false;

  // Route Polyline Cache: "mode_day" -> route data
  Map<String, Map<String, dynamic>> _routeCache = {};
  bool _routeLoading = false;
  List<Map<String, dynamic>> _currentRouteSteps = []; // For displaying route breakdown
  /// Transit modunda API hatası veya yanıtta hiç toplu taşıma (TRANSIT) adımı yok.
  bool _transitLegsUnavailable = false;
  bool _isMapFullscreen = false; // Fullscreen map mode
  Map<String, String> _routeOrigins = {}; // Day -> RouteId mapping for zero-cost routes
  
  // Scroll Controller
  // Scroll Controllers
  final ScrollController _routesScrollController = ScrollController();
  final ScrollController _suggestionsScrollController = ScrollController();
  bool _showScrollToTop = false; // For My Route
  bool _showSuggestionsScrollToTop = false; // For Suggestions

  // Scroll Controller

  @override
  void initState() {
    super.initState();
    _mainTabController = TabController(
      length: 3, 
      vsync: this,
      initialIndex: widget.initialTabIndex,
    );
    _mainTabController.addListener(_onMainTabChanged);
    // Remove individual tab listeners if they cause issues, global controller usually enough
    // But day tabs need listener for index updates
    _loadData();
    
    // Global değişiklikleri dinle
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
    TripUpdateService().cityChanged.addListener(_onCityChanged);

    // Scroll Listeners
    _routesScrollController.addListener(() {
      if (_routesScrollController.offset > 200) {
        if (!_showScrollToTop) setState(() => _showScrollToTop = true);
      } else {
        if (_showScrollToTop) setState(() => _showScrollToTop = false);
      }
    });

    _suggestionsScrollController.addListener(() {
      if (_suggestionsScrollController.offset > 200) {
        if (!_showSuggestionsScrollToTop) setState(() => _showSuggestionsScrollToTop = true);
      } else {
        if (_showSuggestionsScrollToTop) setState(() => _showSuggestionsScrollToTop = false);
      }
    });
  }

  @override
  void didUpdateWidget(RoutesScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    // Tutorial triggering is controlled, not automatic
  }

  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    TripUpdateService().cityChanged.removeListener(_onCityChanged);
    _mainTabController.removeListener(_onMainTabChanged);
    _mainTabController.dispose();
    _dayTabController?.removeListener(_handleDayTabChange);
    _dayTabController?.dispose();
    // GoogleMap widget kendi controller yaşam döngüsünü yönetir; dispose() çağrısı
    // animateCamera gibi gecikmeli çağrıların "disposed map" hatasına yol açabiliyor.
    _routeMapController = null;
    _routesScrollController.dispose();
    _suggestionsScrollController.dispose();
    super.dispose();
  }

  void _onTripDataChanged() {
    _loadData();
  }

  void _onCityChanged() {
    _loadData();
  }

  void _handleDayTabChange() {
    if (_dayTabController == null || _dayTabController!.indexIsChanging) return;
    
    // Tab değiştiğinde (veya kaydırma bittiğinde) haritayı güncelle
    // +1 ekliyoruz çünkü _dayPlans içinde 1..N günler saklanıyor, controller ise 0..N-1
    final currentDay = _dayTabController!.index + 1;
    final places = _dayPlans[currentDay] ?? [];

    // Gün boşsa, önceki günden kalan rota detay/state'ini temizle.
    if (places.isEmpty) {
      if (mounted) {
        setState(() {
          _currentRouteSteps = [];
          _routePolylines = {};
          _transitTimeCache = null;
          _routeLoading = false;
          _transitLoading = false;
          _transitLegsUnavailable = false;
        });
      }
      return;
    }
    
    if (_showMapPreview) {
       _updateRouteMapMarkers(places);
    }

    // 🔥 UI Rebuild: Seçili sekmeki badge renginin güncellenmesi için
    if (mounted) setState(() {});
  }

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();
    
    // 1. Profil / İlgi Alanları
    final travelStyle = prefs.getString("user_style") ?? "Denge";
    final interests = prefs.getStringList("user_interests") ?? [];
    
    // 2. Rota Verisi - Şehir bazlı (per-city storage)
    final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
    // Migration: eski global anahtarları aktif şehre taşı
    final hasMigratedPerCity = prefs.getBool("has_migrated_to_per_city") ?? false;
    if (!hasMigratedPerCity) {
      final oldSchedule = prefs.getString("trip_schedule");
      final oldPlaces = prefs.getStringList("trip_places");
      final oldOrigins = prefs.getString("trip_route_origins");
      final oldDays = prefs.getInt("tripDays");
      if (oldSchedule != null) await prefs.setString("trip_schedule_$currentCity", oldSchedule);
      if (oldPlaces != null) await prefs.setStringList("trip_places_$currentCity", oldPlaces);
      if (oldOrigins != null) await prefs.setString("trip_route_origins_$currentCity", oldOrigins);
      if (oldDays != null) await prefs.setInt("tripDays_$currentCity", oldDays);
      // Eski anahtarları sil
      await prefs.remove("trip_schedule");
      await prefs.remove("trip_places");
      await prefs.remove("trip_route_origins");
      await prefs.remove("tripDays");
      await prefs.setBool("has_migrated_to_per_city", true);
    }
    
    final savedScheduleJson = prefs.getString("trip_schedule_$currentCity");
    final savedPlaces = prefs.getStringList("trip_places_$currentCity") ?? [];
    
    // Route Origins yükle (per-city)
    final savedOriginsJson = prefs.getString("trip_route_origins_$currentCity");
    Map<String, String> loadedOrigins = {};
    if (savedOriginsJson != null) {
      try {
        final decoded = jsonDecode(savedOriginsJson) as Map<String, dynamic>;
        decoded.forEach((key, value) {
          loadedOrigins[key] = value.toString();
        });
      } catch (_) {}
    }
    
    // Aktif şehir verisi yükle
    final cityData = await CityDataLoader.loadCity(currentCity);
    
    if (!mounted) return;
    if (cityData == null) return;

    final dayPlans = <int, List<Highlight>>{};
    int maxDay = 1;
    
    // Tüm yüklenen şehir dataları
    final Map<String, CityModel> loadedCities = {currentCity: cityData};
    
    // Benzersiz isimleri ve şehirlerini topla
    final Map<String, String> placeCityMapping = {};

    if (savedScheduleJson != null) {
      try {
        final Map<String, dynamic> scheduleMap = jsonDecode(savedScheduleJson);
        
        // Önce hangi şehirlerin gerektiğini bul
        final Set<String> neededCities = {currentCity};
        scheduleMap.forEach((dayStr, placeList) {
          final List<dynamic> places = placeList;
          for (var item in places) {
            if (item is Map<String, dynamic> && item['city'] != null) {
              neededCities.add(item['city'].toString().toLowerCase());
            }
          }
        });
        
        // Gerekli şehirleri yükle
        for (var cityName in neededCities) {
          if (!loadedCities.containsKey(cityName)) {
            final city = await CityDataLoader.loadCity(cityName);
            if (city != null) {
              loadedCities[cityName] = city;
            }
          }
        }
        
        // Şimdi planları oluştur
        scheduleMap.forEach((dayStr, placeList) {
          final day = int.tryParse(dayStr) ?? 1;
          if (day > maxDay) maxDay = day;
          
          final List<dynamic> items = placeList;
          final List<Highlight> places = [];
          
          for (var item in items) {
            String placeName;
            String placeCity;
            
            // Yeni format: {"name": "...", "city": "..."}
            if (item is Map<String, dynamic>) {
              placeName = item['name']?.toString() ?? '';
              placeCity = (item['city']?.toString() ?? currentCity).toLowerCase();
            } 
            // Eski format: sadece isim string
            else {
              placeName = item.toString();
              placeCity = currentCity;
            }
            
            if (placeName.isEmpty) continue;
            
            // İlgili şehirden bul
            final city = loadedCities[placeCity];
            if (city != null) {
              final exactMatches = city.highlights.where((h) => h.name == placeName);
              if (exactMatches.isNotEmpty) {
                final place = exactMatches.first;
                places.add(place);
                placeCityMapping[placeName] = placeCity;
              }
            }
          }
          dayPlans[day] = places;
        });
      } catch (e) {
        print("Schedule parse error: $e");
      }
    } 
    // Eski veri kurtarma (sadece trip_places varsa)
    else if (savedPlaces.isNotEmpty) {
      const int placesPerDay = 5;
      final total = savedPlaces.length;
      final daysNeeded = (total / placesPerDay).ceil();
      maxDay = daysNeeded > 0 ? daysNeeded : 1;
      
      for (int i = 0; i < maxDay; i++) {
        final start = i * placesPerDay;
        final end = math.min(start + placesPerDay, total);
        final subNames = savedPlaces.sublist(start, end);
        
        final List<Highlight> places = [];
        for (var name in subNames) {
          final exactMatches = cityData.highlights.where((h) => h.name == name);
          if (exactMatches.isNotEmpty) {
            final place = exactMatches.first;
            places.add(place);
            placeCityMapping[name] = currentCity;
          }
        }
        dayPlans[i + 1] = places;
      }
    }
    
    // Boş günleri de init et (en azından onboardingden gelen gün sayısı kadar)
    final onboardingDays = prefs.getInt("tripDays_$currentCity") ?? prefs.getInt("tripDays") ?? 3;
    if (maxDay < onboardingDays && dayPlans.isEmpty) maxDay = onboardingDays;
    
    if (dayPlans.isEmpty) {
         for (int i = 1; i <= maxDay; i++) {
             dayPlans[i] = [];
         }
    }
    
    // ══════════════════════════════════════════════════════════════════════════
    // MY BUCKET LIST (Index 0) - EXCLUSIVELY FROM USER SAVES (savedPlaces)
    // ══════════════════════════════════════════════════════════════════════════
    final List<Highlight> myListPlaces = [];
    final Set<String> myListNames = {};
    
    for (var name in savedPlaces) {
      final exactMatches = cityData.highlights.where((h) => h.name == name);
      if (exactMatches.isNotEmpty) {
        final place = exactMatches.first;
        if (!myListNames.contains(place.name)) {
          myListNames.add(place.name);
          myListPlaces.add(place);
          placeCityMapping[place.name] = currentCity;
        }
      }
    }
    dayPlans[0] = myListPlaces;

    // Trip Places Highlights listesini oluştur (tüm benzersiz mekanlar)
    // Trip Places Highlights listesini oluştur (SADECE Listem/Day 0'daki mekanlar)
    final Set<String> uniqueNames = Set.from(myListNames);
    final List<Highlight> tripHighlights = List.from(myListPlaces);

    // Generate automatic routes (Async)
    final curatedList = await CuratedRoutesService.generateRoutes(cityData, AppLocalizations.instance.isEnglish);
    final generatedSuggestions = curatedList.map((route) => SuggestedRoute(
      id: route.id,
      name: route.name,
      description: route.description,
      duration: route.duration,
      distance: route.distance,
      difficulty: route.difficulty,
      imageUrl: route.imageUrl,
      tags: route.tags,
      placeNames: route.placeNames,
      interests: route.interests,
      accentColor: route.accentColor,
      icon: route.icon,
    )).toList();

    final urlsToDownload = <String>[];
    for (final route in generatedSuggestions) {
      if (route.imageUrl.isNotEmpty) {
        final safeUrl = firebaseCompatibleImageUrl(route.imageUrl);
        if (safeUrl.isNotEmpty && !urlsToDownload.contains(safeUrl)) {
          urlsToDownload.add(safeUrl);
        }
      }
    }
    for (final place in tripHighlights.take(10)) {
      if (place.imageUrl != null && place.imageUrl!.isNotEmpty) {
        final safeUrl = firebaseCompatibleImageUrl(place.imageUrl!);
        if (safeUrl.isNotEmpty && !urlsToDownload.contains(safeUrl)) {
          urlsToDownload.add(safeUrl);
        }
      }
    }

    if (mounted) {
      setState(() {
        _city = cityData;
        _allSuggestedRoutes = generatedSuggestions;
        _filteredSuggestedRoutes = _allSuggestedRoutes;
        _travelStyle = travelStyle;
        _interests = interests;
        // Deduplicate day plans to fix potential "ghost" items
        dayPlans.forEach((day, places) {
          final seen = <String>{};
          final unique = <Highlight>[];
          for (var p in places) {
            if (!seen.contains(p.name)) {
              seen.add(p.name);
              unique.add(p);
            }
          }
          dayPlans[day] = unique;
        });

        _tripPlaceNames = uniqueNames.toList();
        _tripPlaces = tripHighlights;
        
        // Auto-optimize each day plan
        final optimizedDayPlans = <int, List<Highlight>>{};
        dayPlans.forEach((day, places) {
          optimizedDayPlans[day] = _getOptimizedSequence(places);
        });
        _dayPlans = optimizedDayPlans;

        _routeOrigins = loadedOrigins; // Restore static route origins
        _placeCityMap = placeCityMapping;
        _tripDays = onboardingDays; // Onboarding'den gelen gün sayısını sakla
        _totalDays = math.max(maxDay, onboardingDays); // En azından onboarding günleri kadar göster
        _loading = false;
        _isAiPlan = prefs.getBool("is_ai_plan_$currentCity") ?? false;
        
        // Preserve current tab index
        final previousIndex = _dayTabController?.index ?? 0;
        _dayTabController?.dispose();
        _dayTabController = TabController(length: _totalDays, vsync: this);
        _dayTabController?.addListener(_handleDayTabChange);
        
        // Restore tab index if still valid
        if (previousIndex < _totalDays) {
          _dayTabController?.index = previousIndex;
        }
      });
    }

    if (urlsToDownload.isNotEmpty) {
      Future.microtask(() async {
        try {
          await Future.wait(
            urlsToDownload.map((url) => AppImageCacheManager.instance.downloadFile(url).catchError((_) => null))
          );
        } catch (_) {}
        if (mounted) {
          for (final url in urlsToDownload) {
            CachedNetworkImageProvider(url, cacheManager: AppImageCacheManager.instance).resolve(ImageConfiguration.empty);
          }
        }
      });
    }

    // Tutorial Check
    WidgetsBinding.instance.addPostFrameCallback((_) { 
       _checkTutorial();
    });
  }

  void _checkTutorial() {
    if (!widget.isVisible) return;
    
    TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_ROUTES).then((shouldShow) {
      if (shouldShow) {
        Future.delayed(const Duration(milliseconds: 500), () {
          if (mounted && widget.isVisible) {
            _showRoutesTutorial();
          }
        });
      }
    });
  }

  void _onMainTabChanged() {
    if (_mainTabController.indexIsChanging) return;
    
    // --- ANALYTICS: Tab Switch ---
    final tabNames = ['Rotalarım', 'Öneriler', 'Tamamlananlar'];
    if (_mainTabController.index < tabNames.length) {
      AnalyticsService.instance.logButtonClick(
        'routes_main_tab_${_mainTabController.index}',
        buttonName: 'Tab: ${tabNames[_mainTabController.index]}',
      );
    }

    // Trigger My Route tutorial when switching to "Rotam" tab (index 1)
    if (_mainTabController.index == 1 && widget.isVisible) {
      _checkMyRouteTutorial();
    }
  }

  void _checkMyRouteTutorial() {
    if (!widget.isVisible) return;
    
    TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_MY_ROUTE).then((shouldShow) {
      if (shouldShow) {
         Future.delayed(const Duration(milliseconds: 800), () {
           if (mounted && widget.isVisible && _mainTabController.index == 1) {
          
              // Force render if key is missing (lazy sliver issue)
              if (_startRouteButtonKey.currentContext == null) {
                 if (_myRouteScrollController.hasClients) {
                     // Jump to bottom to build bottom widgets
                     _myRouteScrollController.jumpTo(_myRouteScrollController.position.maxScrollExtent);
                     
                     // Small delay then jump back to top
                     Future.delayed(const Duration(milliseconds: 100), () {
                        if (mounted && _myRouteScrollController.hasClients) {
                           _myRouteScrollController.jumpTo(0);
                           
                           // Now show tutorial
                           Future.delayed(const Duration(milliseconds: 300), () {
                               if (mounted) _showMyRouteTutorial();
                           });
                        }
                     });
                 }
              } else {
                 _showMyRouteTutorial();
              }
            } // if mounted
         }); // future delayed
      } // if shouldShow
    }); // service then
  }

  Future<void> _saveTripData() async {
     final prefs = await SharedPreferences.getInstance();
     final currentCity = prefs.getString("selectedCity")?.toLowerCase() ?? "barcelona";
     
     // 1. Liste olarak kaydet (per-city)
     await prefs.setStringList("trip_places_$currentCity", _tripPlaceNames);
     
     // 2. Schedule'ı DOĞRUDAN _dayPlans'den oluştur ve kaydet (per-city).
     final Map<String, List<Map<String, dynamic>>> finalSchedule = {};
     
     _dayPlans.forEach((day, places) {
       final dayKey = day.toString();
       final dayPlaces = places.map((p) => {
         'name': p.name,
         'city': _placeCityMap[p.name] ?? currentCity,
       }).toList();
       finalSchedule[dayKey] = dayPlaces;
     });
     
     await prefs.setString("trip_schedule_$currentCity", jsonEncode(finalSchedule));
      
      // Route Origins kaydet (per-city)
      await prefs.setString("trip_route_origins_$currentCity", jsonEncode(_routeOrigins));
      
      // Tutorial Check: Removed from here
  }

  Future<void> _toggleTripPlace(Highlight place) async {
    final name = place.name;
    setState(() {
      if (_tripPlaceNames.contains(name)) {
        _tripPlaceNames.remove(name);
        _tripPlaces.removeWhere((p) => p.name == name);
      } else {
        _tripPlaceNames.add(name);
        _tripPlaces.add(place);
        HapticFeedback.lightImpact();
      }
    });
    await _saveTripData();
    TripUpdateService().notifyTripChanged();
  }



  void _filterRoutes(int filterIndex) {
    setState(() {
      _selectedRouteFilter = filterIndex;
      if (filterIndex == 0) {
        _filteredSuggestedRoutes = _allSuggestedRoutes;
      } else if (filterIndex == 1) {
        // SANA ÖZEL (FOR YOU)
        _filteredSuggestedRoutes = _allSuggestedRoutes.where((route) {
          int matchScore = 0;

          // 1. İlgi Alanı Eşleşmesi
          for (var userInterest in _interests) {
             // Basit string içerir kontrolü (Case insensitive)
             if (route.interests.any((rInterest) => rInterest.toLowerCase().contains(userInterest.toLowerCase()))) {
               matchScore += 2;
             }
             if (route.tags.any((tag) => tag.toLowerCase().contains(userInterest.toLowerCase()))) {
               matchScore += 1;
             }
          }

          // 2. Seyahat Tarzı Eşleşmesi
          if (_travelStyle == "Lokal") {
             if (route.tags.any((t) => t.toLowerCase().contains("local") || t.toLowerCase().contains("lokal") || t.toLowerCase().contains("hidden"))) matchScore += 3;
          } else if (_travelStyle == "Turist" || _travelStyle == "Tourist") {
             if (route.tags.any((t) => t.toLowerCase().contains("iconic") || t.toLowerCase().contains("must-see") || t.toLowerCase().contains("top") || t.toLowerCase().contains("popular"))) matchScore += 3;
          } else if (_travelStyle == "Doğa Sever" || _travelStyle == "Nature") {
             if (route.tags.any((t) => t.toLowerCase().contains("nature") || t.toLowerCase().contains("park"))) matchScore += 3;
          }

          return matchScore > 0;
        }).toList();

        // Hiç eşleşme yoksa, en yeni/rasgele 2 taneyi göster (Boş kalmasın)
        if (_filteredSuggestedRoutes.isEmpty) {
          _filteredSuggestedRoutes = _allSuggestedRoutes.take(2).toList();
        }
      } else {
        // POPÜLER (POPULAR)
        _filteredSuggestedRoutes = _allSuggestedRoutes.where((route) {
           final lowerTags = route.tags.map((e) => e.toLowerCase()).toList();
           return lowerTags.contains("popular") || 
                  lowerTags.contains("popüler") || 
                  lowerTags.contains("must-see") ||
                  lowerTags.contains("iconic") ||
                  lowerTags.contains("top") ||
                  lowerTags.contains("best");
        }).toList();
        
        // Eşleşme yoksa ilk 3'ü al (Genelde en iyiler en üsttedir)
        if (_filteredSuggestedRoutes.isEmpty) {
          _filteredSuggestedRoutes = _allSuggestedRoutes.take(3).toList();
        }
      }
    });
  }

  Future<void> _assignPlaceToDayFromListem(String name) async {
    HapticFeedback.mediumImpact();
    // Use the existing dialog from Detail/Nearby screen but adapted. Need to access maxDay.
    int maxDay = _totalDays;
    final selectedDay = await _showDaySelectionDialog(name);
    if (selectedDay == null) return;
    
    // Add to specific day
    setState(() {
       // Expand totalDays if needed
       if (selectedDay > _totalDays) {
         _totalDays = selectedDay;
         _dayTabController?.dispose();
         _dayTabController = TabController(length: _totalDays, vsync: this);
       }
       
       final placeMatch = _tripPlaces.where((p) => p.name == name).firstOrNull ?? 
           _dayPlans[0]?.where((p) => p.name == name).firstOrNull;
           
       if (placeMatch != null) {
         _dayPlans[selectedDay] ??= [];
         if (!_dayPlans[selectedDay]!.any((p) => p.name == name)) {
            _dayPlans[selectedDay]!.add(placeMatch);
            _routeOrigins.remove(selectedDay.toString());
         }
       }
    });
    
    await _saveTripData();
    TripUpdateService().notifyTripChanged();
    
    if (mounted) {
       ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text(AppLocalizations.instance.addedToDay(name, selectedDay)),
          backgroundColor: const Color(0xFF1F1F1F),
          behavior: SnackBarBehavior.floating,
          duration: const Duration(milliseconds: 1500),
       ));
    }
  }

  Future<void> _removeFromDay(int day, String name) async {
    debugPrint("Removing item: $name from day: $day");
    HapticFeedback.mediumImpact();
    setState(() {
      // 1. İlgili günden mekanı sil
      final initialLen = _dayPlans[day]?.length ?? 0;
      _dayPlans[day]?.removeWhere((p) => p.name == name);
      if ((_dayPlans[day]?.length ?? 0) < initialLen) {
        _routeOrigins.remove(day.toString()); // Sadece bu günün rotasını iptal et
      }
      
      // 2. Eğer silinen gün "Listem" (0) ise, ana listelerden de sil
      if (day == 0) {
        _tripPlaceNames.removeWhere((n) => n == name);
        _tripPlaces.removeWhere((p) => p.name == name);
      }
    });

    await _saveTripData();
    TripUpdateService().notifyTripChanged();
  }

  void _reorderPlace(int day, int oldIndex, int newIndex) {
    HapticFeedback.selectionClick();
    if (oldIndex < newIndex) newIndex -= 1;
    setState(() {
      final item = _dayPlans[day]!.removeAt(oldIndex);
      _dayPlans[day]!.insert(newIndex, item);
      _routeOrigins.remove(day.toString()); // Sıralama değişirse statik rota bozulur
    });
    
    // Harita markerlarını ve polyline'ı güncelle (harfler yeni sıraya göre)
    final updatedPlaces = _dayPlans[day] ?? [];
    if (updatedPlaces.isNotEmpty && _showMapPreview) {
      _updateRouteMapMarkers(updatedPlaces);
      _fetchRouteForMode(_selectedTransportMode, day);
    }
  }

  String _getCategoryGroup(Highlight h) {
    final cat = h.category.toLowerCase();
    final name = h.name.toLowerCase();
    
    if (cat.contains("bar") || cat.contains("pub") || cat.contains("gece") || 
        cat.contains("night") || name.contains("bar") || name.contains("shot") || 
        name.contains("pub") || name.contains("club") || name.contains("meyhane")) return "SOCIAL";
    if (cat.contains("yeme") || cat.contains("food") || cat.contains("restoran") || cat.contains("dinner") || cat.contains("lunch")) return "FOOD";
    if (cat.contains("kafe") || cat.contains("cafe") || cat.contains("coffee")) return "COFFEE";
    if (cat.contains("park") || cat.contains("bahçe") || cat.contains("garden") || cat.contains("doğa")) return "NATURE";
    if (cat.contains("view") || cat.contains("manzara") || cat.contains("teras")) return "VIEW";
    if (cat.contains("meydan") || cat.contains("square")) return "SQUARE";
    return "CULTURE"; 
  }

  double _getCategoryPenalty(Highlight h, int slotIndex) {
    final group = _getCategoryGroup(h);
    double penalty = 0.0;

    // Slot saatleri tahmini: 
    // 0: 09:30, 1: 11:30, 2: 13:30, 3: 16:00, 4: 19:00, 5: 20:00, 6: 21:00+
    
    if (group == "CULTURE" || group == "SQUARE" || group == "NATURE" || group == "VIEW") {
      // Kültürel yerler, parklar ve manzara noktaları sabah/öğle iyidir.
      if (slotIndex == 0) penalty -= 1000.0; // İlk slot bonusu (Artırıldı)
      if (slotIndex == 1) penalty -= 600.0; 
      
      if (slotIndex >= 5) {
        penalty += (slotIndex - 2) * 500.0; // Akşam cezası (Artırıldı)
      }
    } else if (group == "SOCIAL") {
      // Barlar sabah/öğle ÇOK kötüdür (slot 0-3), akşam iyidir.
      if (slotIndex <= 3) penalty += 2000.0; // Sabah bar cezası (Maksimum)
      if (slotIndex >= 5) penalty -= 800.0; // Akşam bonusu
    } else if (group == "FOOD") {
      // Yemek öğle (slot 2) veya akşam (slot 4-5) iyidir.
      if (slotIndex == 0 || slotIndex == 1) penalty += 500.0; // Kahvaltı saati restoran istemeyiz
      if (slotIndex == 2 || slotIndex >= 4) penalty -= 100.0; // Yemek saati bonusu
    } else if (group == "COFFEE") {
      // Kahve molası sabah ve öğleden sonra iyidir.
      if (slotIndex == 1 || slotIndex == 3) penalty -= 100.0;
      if (slotIndex >= 5) penalty += 200.0; // Çok geç kahve istenmeyebilir
    }

    return penalty;
  }

  List<Highlight> _getOptimizedSequence(List<Highlight> places) {
    if (places.length < 2) return places;

    // V4.3: Day-trip yer varsa onu en başa pinle.
    // Day-trip günün büyük kısmını alır → sıralama tartışması yok.
    final dayTrips = places.where((p) => p.isDayTrip).toList();
    final regulars = places.where((p) => !p.isDayTrip).toList();

    if (dayTrips.isNotEmpty) {
      // Birden fazla day-trip aynı günde olmamalı; ama olduysa mesafeye göre sırala
      dayTrips.sort((a, b) => a.distanceFromCenter.compareTo(b.distanceFromCenter));
      // Day-trip + (varsa) akşam yerleri: regular'ları sona koy (akşam yemeği gibi)
      final List<Highlight> result = [...dayTrips];
      // Regular yerleri kendi içinde optimize et (rating yüksek FOOD önce gelsin akşam için)
      regulars.sort((a, b) {
        final aFood = _getCategoryGroup(a) == 'FOOD' ? 1 : 0;
        final bFood = _getCategoryGroup(b) == 'FOOD' ? 1 : 0;
        if (aFood != bFood) return bFood.compareTo(aFood);
        return (b.rating ?? 0).compareTo(a.rating ?? 0);
      });
      result.addAll(regulars);
      return result;
    }

    // Normal akış: weighted nearest-neighbor
    final optimized = <Highlight>[];
    final remaining = List<Highlight>.from(regulars);

    // İlk öğeyi seçerken de kategoriye bakalım (mümkünse sabah kültür olsun)
    Highlight? bestFirst;
    double bestFirstScore = double.infinity;

    for (var p in remaining) {
      double score = _getCategoryPenalty(p, 0); // Slot 0 için kategori puanı
      if (score < bestFirstScore) {
        bestFirstScore = score;
        bestFirst = p;
      }
    }

    if (bestFirst != null) {
      optimized.add(bestFirst);
      remaining.remove(bestFirst);
    } else {
      optimized.add(remaining.removeAt(0));
    }

    while (remaining.isNotEmpty) {
      final current = optimized.last;
      final slotIndex = optimized.length;
      Highlight? nextBest;
      double minCombinedScore = double.infinity;

      for (var p in remaining) {
        // Mesafe puanı (1km = 15 puan)
        final distKm = _haversine(current.lat, current.lng, p.lat, p.lng);
        final distScore = distKm * 15.0;

        // Kategori puanı
        final categoryPenalty = _getCategoryPenalty(p, slotIndex);

        final combinedScore = distScore + categoryPenalty;

        if (combinedScore < minCombinedScore) {
          minCombinedScore = combinedScore;
          nextBest = p;
        }
      }

      if (nextBest != null) {
        optimized.add(nextBest);
        remaining.remove(nextBest);
      } else {
        break;
      }
    }
    return optimized;
  }

  void _optimizeRoute() {
    HapticFeedback.heavyImpact();
    setState(() {
      for (int i = 1; i <= _totalDays; i++) {
        if (_dayPlans[i] != null && _dayPlans[i]!.isNotEmpty) {
          _dayPlans[i] = _getOptimizedSequence(_dayPlans[i]!);
        }
      }
    });
    
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final updatedPlaces = _dayPlans[currentDay] ?? [];
    if (updatedPlaces.isNotEmpty && _showMapPreview) {
      _updateRouteMapMarkers(updatedPlaces);
      _fetchRouteForMode(_selectedTransportMode, currentDay);
    }

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: WanderlustColors.accent, size: 20),
            const SizedBox(width: 12),
            Text(
              AppLocalizations.instance.isEnglish 
                ? "Route optimized! ✨" 
                : "Rota optimize edildi! ✨",
              style: const TextStyle(color: WanderlustColors.textWhite),
            ),
          ],
        ),
        backgroundColor: WanderlustColors.bgCardLight,
        behavior: SnackBarBehavior.floating,
        duration: const Duration(milliseconds: 1200),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }

  Duration _getEstimatedDuration(Highlight h, int totalPlaces) {
    // V4.4: Dinamik süre - Az mekan varsa süreleri artır (Günün dolu görünmesi için)
    double multiplier = 1.0;
    if (totalPlaces <= 4) multiplier = 1.5;
    else if (totalPlaces <= 6) multiplier = 1.2;

    if (h.isDayTrip) {
      return Duration(minutes: h.dayTripDurationMinutes);
    }
    final group = _getCategoryGroup(h);
    switch (group) {
      case "FOOD": return Duration(minutes: (90 * multiplier).round());
      case "COFFEE": return Duration(minutes: (45 * multiplier).round());
      case "SOCIAL": return Duration(minutes: (120 * multiplier).round());
      case "NATURE": return Duration(minutes: (60 * multiplier).round());
      case "VIEW": return Duration(minutes: (45 * multiplier).round());
      case "SQUARE": return Duration(minutes: (30 * multiplier).round());
      case "CULTURE": return Duration(minutes: (150 * multiplier).round()); // 120 -> 150 (MoMA gibi yerler için)
      default: return Duration(minutes: (60 * multiplier).round());
    }
  }

  List<String> _calculateScheduleForDay(List<Highlight> places, int mode, int dayIndex) {
    if (places.isEmpty) return [];

    final List<String> schedule = [];

    // Dinamik başlangıç saati: Her gün farklı
    final random = math.Random(dayIndex * 42);
    final startHour = 9 + random.nextInt(2); // 09:00 - 10:00 arası
    final startMinute = random.nextBool() ? 0 : 30; // :00 veya :30
    DateTime currentTime = DateTime(2024, 1, 1, startHour, startMinute);

    final modeString = _getModeString(mode);
    final cacheKey = "${modeString}_$dayIndex";

    final cachedData = _routeCache[cacheKey];
    final List<dynamic> legs = cachedData?['legs'] ?? [];

    // Günlük program limitleri (Kısaltma faktörü için)
    const int dayEndHour = 22;
    final int totalAvailableMinutes = (dayEndHour - startHour) * 60 - startMinute;
    int totalEstimatedMinutes = 0;
    for (int i = 0; i < places.length; i++) {
      totalEstimatedMinutes += _getEstimatedDuration(places[i], places.length).inMinutes;
      if (i < places.length - 1) totalEstimatedMinutes += 20;
    }

    double compressionFactor = 1.0;
    if (totalEstimatedMinutes > totalAvailableMinutes && places.length > 1) {
      compressionFactor = (totalAvailableMinutes / totalEstimatedMinutes).clamp(0.7, 1.0);
    }

    for (int i = 0; i < places.length; i++) {
      final place = places[i];
      final group = _getCategoryGroup(place);

      // 🔥 V4.5: AKŞAM ÇIPALAMA (Evening Anchoring)
      if ((group == "FOOD" || group == "SOCIAL") && i >= places.length - 2 && currentTime.hour < 18) {
         int targetHour = 18;
         int targetMin = 30 + (i * 15);
         if (targetMin >= 60) { targetHour++; targetMin -= 60; }
         currentTime = DateTime(2024, 1, 1, targetHour, targetMin);
      }

      // Gece yarısı ve açılış saati kontrolü
      if (currentTime.hour < 7) currentTime = DateTime(2024, 1, 1, 21, 0); 
      
      if (!place.isOpenAt(currentTime.hour, currentTime.minute)) {
        final typicalHours = place.getTypicalHours();
        if (typicalHours != null) {
          final openHour = typicalHours.openMinutes ~/ 60;
          final openMin = typicalHours.openMinutes % 60;
          if (openHour > currentTime.hour || (openHour == currentTime.hour && openMin > currentTime.minute)) {
            currentTime = DateTime(2024, 1, 1, openHour, openMin);
          }
        }
      }

      final hour = currentTime.hour.toString().padLeft(2, '0');
      final minute = currentTime.minute.toString().padLeft(2, '0');
      schedule.add("$hour:$minute");

      if (i < places.length - 1) {
        int durationMinutes = (_getEstimatedDuration(place, places.length).inMinutes * compressionFactor).round();
        durationMinutes = durationMinutes.clamp(30, 240);

        int travelSeconds;
        if (i < legs.length) {
          travelSeconds = (legs[i]['duration_seconds'] as num?)?.toInt() ?? 600;
        } else {
          final next = places[i + 1];
          final estMin = TravelTimeEstimator.estimateBetween(place, next, mode: TravelTimeEstimator.modeFromInt(mode));
          travelSeconds = estMin * 60;
        }

        // Travel time'ı da kısalt (sıkışık programda)
        int adjustedTravelSeconds = (travelSeconds * compressionFactor).round();
        adjustedTravelSeconds = adjustedTravelSeconds.clamp(180, 1800); // 3dk-30dk

        currentTime = currentTime.add(Duration(minutes: durationMinutes, seconds: adjustedTravelSeconds));

        // 5dk'luk yuvarlama
        int minutes = currentTime.minute;
        int remainder = minutes % 5;
        if (remainder != 0) {
          currentTime = currentTime.add(Duration(minutes: 5 - remainder));
        }
      }
    }
    return schedule;
  }

  bool _isPlaceClosed(Highlight h, String timeText) {
    // 🔥 Gerçek openHours verisini kullan
    if (h.openHours == null || h.openHours!.isEmpty) {
      // Fallback: Genel kurallar (eski davranış)
      if (timeText.isEmpty) return false;
      try {
        final parts = timeText.split(':');
        final currentHour = int.parse(parts[0]);
        final group = _getCategoryGroup(h);
        if ((group == "CULTURE" || group == "SQUARE" || group == "NATURE") && currentHour >= 19) {
          return true;
        }
        return false;
      } catch (e) {
        return false;
      }
    }

    // Gerçek açılış saatlerini kontrol et
    try {
      final parts = timeText.split(':');
      final currentHour = int.parse(parts[0]);
      final currentMin = int.parse(parts[1]);
      return !h.isOpenAt(currentHour, currentMin);
    } catch (e) {
      return false;
    }
  }

  Future<void> _clearDayPlaces(int day) async {
    final places = _dayPlans[day] ?? [];
    if (places.isEmpty) return;

    HapticFeedback.mediumImpact();
    
    // Show dialog with options: clear this day OR clear all days
    final result = await showModalBottomSheet<String>(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (ctx) {
        return Container(
          margin: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: WanderlustColors.bgCard,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: WanderlustColors.border),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const SizedBox(height: 20),
              Container(
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: WanderlustColors.textGrey.withOpacity(0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
              const SizedBox(height: 20),
              Text(
                AppLocalizations.instance.isEnglish ? "Clear Route" : "Rotayı Temizle",
                style: const TextStyle(
                  color: WanderlustColors.textWhite,
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              Text(
                AppLocalizations.instance.isEnglish
                    ? "Choose what to clear"
                    : "Neyi temizlemek istiyorsunuz?",
                style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
              ),
              const SizedBox(height: 20),
              // Option 1: Clear this day
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: GestureDetector(
                  onTap: () => Navigator.pop(ctx, "this_day"),
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 10,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(12),
                          decoration: BoxDecoration(
                            gradient: LinearGradient(
                              colors: [
                                accent.withOpacity(0.15),
                                accent.withOpacity(0.05),
                              ],
                              begin: Alignment.topLeft,
                              end: Alignment.bottomRight,
                            ),
                            borderRadius: BorderRadius.circular(14),
                          ),
                          child: const Icon(Icons.event_busy_rounded, color: accent, size: 22),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                AppLocalizations.instance.isEnglish
                                    ? "Clear Day $day"
                                    : "$day. Günü Temizle",
                                style: const TextStyle(
                                  color: WanderlustColors.textWhite,
                                  fontWeight: FontWeight.bold,
                                  fontSize: 16,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                AppLocalizations.instance.isEnglish
                                    ? "Remove all ${places.length} places from this day"
                                    : "Bu gündeki ${places.length} mekanı kaldır",
                                style: const TextStyle(
                                  color: WanderlustColors.textGrey,
                                  fontSize: 13,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Icon(Icons.arrow_forward_ios_rounded, color: WanderlustColors.textGrey.withOpacity(0.4), size: 16),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 12),
              // Option 2: Clear ALL days
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: GestureDetector(
                  onTap: () => Navigator.pop(ctx, "all_days"),
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.04),
                          blurRadius: 10,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(12),
                          decoration: BoxDecoration(
                            gradient: LinearGradient(
                              colors: [
                                Colors.grey.shade400.withOpacity(0.15),
                                Colors.grey.shade400.withOpacity(0.05),
                              ],
                              begin: Alignment.topLeft,
                              end: Alignment.bottomRight,
                            ),
                            borderRadius: BorderRadius.circular(14),
                          ),
                          child: Icon(Icons.layers_clear_rounded, color: Colors.grey.shade600, size: 22),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                AppLocalizations.instance.isEnglish
                                    ? "Clear All Days"
                                    : "Tüm Günleri Temizle",
                                style: const TextStyle(
                                  color: WanderlustColors.textWhite,
                                  fontWeight: FontWeight.bold,
                                  fontSize: 16,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                AppLocalizations.instance.isEnglish
                                    ? "Reset entire route plan"
                                    : "Tüm rota planını sıfırla",
                                style: const TextStyle(
                                  color: WanderlustColors.textGrey,
                                  fontSize: 13,
                                  fontWeight: FontWeight.w500,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Icon(Icons.arrow_forward_ios_rounded, color: WanderlustColors.textGrey.withOpacity(0.4), size: 16),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 24),
            ],
          ),
        );
      },
    );

    if (result == null) return; // User dismissed

    if (result == "all_days") {
      // Clear ALL days
      final prefs = await SharedPreferences.getInstance();
      final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
      
      await prefs.remove("trip_places_$currentCity");
      await prefs.remove("trip_schedule_$currentCity");
      await prefs.remove("trip_route_origins_$currentCity");
      await prefs.remove("has_migrated_to_listem_$currentCity");
      await prefs.remove("tripDays_$currentCity"); // Gün sayısını da temizle
      
      // Clear AI Caches
      await prefs.remove("ai_itinerary_cached_$currentCity");
      
      // Reset AI Plan flag so manual additions won't be blurred
      await prefs.setBool("is_ai_plan_$currentCity", false);
      
      setState(() {
        _tripPlaces = [];
        _tripPlaceNames = [];
        _dayPlans = {};
        _totalDays = 1;
        _routeOrigins = {};
        _routeCache = {};
        _routePolylines = {};
        _routeMarkers = {};
        _transitTimeCache = null;
        _currentRouteSteps = [];   // Rota Detayları sıfırla
        _transitLegsUnavailable = false;
        _routeLoading = false;
        
        _dayTabController?.dispose();
        _dayTabController = TabController(length: 1, vsync: this);
      });
      
      TripUpdateService().notifyTripChanged();
      await _loadData();
      TripUpdateService().notifyTripChanged();
      HapticFeedback.vibrate();
      
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Row(
            children: [
              Icon(Icons.layers_clear_rounded, color: Colors.grey.shade400, size: 20),
              const SizedBox(width: 12),
              Text(
                AppLocalizations.instance.isEnglish
                    ? "All days cleared"
                    : "Tüm günler temizlendi",
                style: const TextStyle(color: WanderlustColors.textWhite),
              ),
            ],
          ),
          backgroundColor: bgCardLight,
          behavior: SnackBarBehavior.floating,
          duration: const Duration(milliseconds: 1500),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      );
    } else {
      // Clear this day only
      setState(() {
        final namesToCheck = places.map((p) => p.name).toList();
        _dayPlans[day] = [];
        _routeOrigins.remove(day.toString());
        
        _routeCache.remove("walking_$day");
        _routeCache.remove("transit_$day");
        _routeCache.remove("driving_$day");
        _transitTimeCache = null;
        _routePolylines = {};
        _currentRouteSteps = [];   // Rota Detayları sıfırla
        _transitLegsUnavailable = false;
        _routeLoading = false;
        
        // Eğer silinen gün "Listem" (0) ise, ana listeleri de temizle
        if (day == 0) {
          _tripPlaceNames.clear();
          _tripPlaces.clear();
        }
      });

      await _saveTripData();
      TripUpdateService().notifyTripChanged();

      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Row(
            children: [
              const Icon(Icons.event_busy_rounded, color: accent, size: 20),
              const SizedBox(width: 12),
              Text(
                AppLocalizations.instance.isEnglish
                    ? "Day $day cleared"
                    : "${AppLocalizations.instance.day} $day temizlendi",
                style: const TextStyle(color: WanderlustColors.textWhite),
              ),
            ],
          ),
          backgroundColor: bgCardLight,
          behavior: SnackBarBehavior.floating,
          duration: const Duration(milliseconds: 1200),
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        ),
      );
    }
  }


  // ══════════════════════════════════════════════════════════════════════════
  // GOOGLE MAPS INTEGRATION - İSİMLİ DURAKLAR
  // ══════════════════════════════════════════════════════════════════════════

  /// Google Maps'te rotayı başlat - MEKAN İSİMLERİYLE
  Future<void> _startRouteInGoogleMaps(int day) async {
    // 🔥 Premium Check
    if (!PremiumService.instance.canGetDirections()) {
      _showPaywall();
      return;
    }

    final places = _dayPlans[day] ?? [];
    if (places.length < 2) return;

    HapticFeedback.heavyImpact();

    // Google Maps Parameterized URL
    // https://www.google.com/maps/dir/?api=1&origin=...&destination=...&waypoints=...
    
    // Yardımcı: İsim kodlama
    String encodePlace(Highlight p) => Uri.encodeComponent("${p.name}, ${_city?.city ?? ''}");

    final userOrigin = await _getUserOriginIfInCity();
    final origin = userOrigin != null
        ? "${userOrigin.latitude},${userOrigin.longitude}"
        : encodePlace(places.first);
    final destination = encodePlace(places.last);
    
    // Dynamic travel mode based on selected transport
    String travelMode;
    switch (_selectedTransportMode) {
      case 1: travelMode = 'transit'; break;
      case 2: travelMode = 'driving'; break;
      default: travelMode = 'walking';
    }

    // Transit mode doesn't support waypoints in Google Maps
    String waypoints = "";
    if (travelMode != 'transit' && places.length > 1) {
       final startIdx = userOrigin != null ? 0 : 1;
       final wpList = places.sublist(startIdx, places.length - 1).map(encodePlace).toList();
       waypoints = "&waypoints=${wpList.join('|')}";
    }

    final url = "https://www.google.com/maps/dir/?api=1&origin=$origin&destination=$destination$waypoints&travelmode=$travelMode";

    try {
      final uri = Uri.parse(url);
      // iOS 26+'da canLaunchUrl bazen false dönebiliyor, direkt deneyelim
      // --- ANALYTICS: Navigation Start ---
      AnalyticsService.instance.logButtonClick(
        'start_navigation_google_maps',
        buttonName: 'Start Navigation',
      );
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (e) {
      _openMapsWithCoordinates(day);
    }
  }

  /// Fallback - Koordinatlarla Google Maps aç
  Future<void> _openMapsWithCoordinates(int day) async {
    final places = _dayPlans[day] ?? [];
    if (places.isEmpty) return;

    try {
      // Waypoints ile directions API
      final userOrigin = await _getUserOriginIfInCity();
      final origin = userOrigin != null
          ? "${userOrigin.latitude},${userOrigin.longitude}"
          : "${places.first.lat},${places.first.lng}";
      final destination = "${places.last.lat},${places.last.lng}";

      // Dynamic travel mode
      String travelMode;
      switch (_selectedTransportMode) {
        case 1: travelMode = 'bicycling'; break;
        case 2: travelMode = 'transit'; break;
        case 3: travelMode = 'driving'; break;
        default: travelMode = 'walking';
      }

      String waypointsParam = "";
      if (travelMode != 'transit' && places.length > 1) {
        final startIdx = userOrigin != null ? 0 : 1;
        final middlePoints = places.sublist(startIdx, places.length - 1);
        waypointsParam =
            "&waypoints=${middlePoints.map((p) => "${p.lat},${p.lng}").join("|")}";
      }

      final url =
          "https://www.google.com/maps/dir/?api=1"
          "&origin=$origin"
          "&destination=$destination"
          "$waypointsParam"
          "&travelmode=$travelMode";

      if (await canLaunchUrl(Uri.parse(url))) {
        // --- ANALYTICS: Navigation Start ---
        AnalyticsService.instance.logButtonClick(
          'start_navigation_fallback',
          buttonName: 'Open Maps Fallback',
        );
        await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
      }
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text(
            "Harita açılamadı",
            style: TextStyle(color: WanderlustColors.textWhite),
          ),
          backgroundColor: bgCardLight,
          behavior: SnackBarBehavior.floating,
          duration: const Duration(milliseconds: 1200),
        ),
      );
    }
  }

  /// Google Maps Static API URL - Gerçek harita önizlemesi
  String _getStaticMapUrl(int day) {
    final places = _dayPlans[day] ?? [];
    if (places.isEmpty) return "";

    // Bounding box hesapla
    double minLat = places.map((p) => p.lat).reduce(math.min);
    double maxLat = places.map((p) => p.lat).reduce(math.max);
    double minLng = places.map((p) => p.lng).reduce(math.min);
    double maxLng = places.map((p) => p.lng).reduce(math.max);

    // Center hesapla
    double centerLat = (minLat + maxLat) / 2;
    double centerLng = (minLng + maxLng) / 2;

    // Zoom hesapla (basit yaklaşım)
    double latDiff = maxLat - minLat;
    double lngDiff = maxLng - minLng;
    double maxDiff = math.max(latDiff, lngDiff);
    int zoom = 14;
    if (maxDiff > 0.1) zoom = 12;
    if (maxDiff > 0.2) zoom = 11;
    if (maxDiff > 0.3) zoom = 10;

    // Markers - Her durak için özel marker
    final markers = <String>[];
    for (int i = 0; i < places.length; i++) {
      final p = places[i];
      // Custom marker: Amber/Orange renk (0xF5A623), numara label
      markers.add(
        "markers=color:0xF5A623%7Clabel:${i + 1}%7C${p.lat},${p.lng}",
      );
    }

    // Path - Rota çizgisi (Amber renk)
    final pathPoints = places.map((p) => "${p.lat},${p.lng}").join("|");
    final path = "path=color:0xF5A623FF%7Cweight:5%7C$pathPoints";

    // Dark mode style
    final style = [
      "style=element:geometry%7Ccolor:0x1A1A2E",
      "style=element:labels.text.fill%7Ccolor:0x9CA3AF",
      "style=element:labels.text.stroke%7Ccolor:0x0D0D1A",
      "style=feature:road%7Celement:geometry%7Ccolor:0x2D2D4A",
      "style=feature:water%7Celement:geometry%7Ccolor:0x0D0D1A",
      "style=feature:poi%7Cvisibility:off",
    ].join("&");

    // API key varsa kullan, yoksa sınırlı kullanım
    final apiKeyParam = _googleMapsApiKey != "YOUR_GOOGLE_MAPS_API_KEY"
        ? "&key=$_googleMapsApiKey"
        : "";

    return "https://maps.googleapis.com/maps/api/staticmap?"
        "center=$centerLat,$centerLng"
        "&zoom=$zoom"
        "&size=600x300"
        "&scale=2"
        "&maptype=roadmap"
        "&$style"

          "&$path"
          "&${markers.join("&")}"
          "$apiKeyParam";
  }

  Future<void> _applySuggestedRoute(SuggestedRoute route) async {
    // İlk rota her zaman ücretsiz (Pro olmadan)
    final bool isFirstRoute = _allSuggestedRoutes.isNotEmpty && _allSuggestedRoutes.first.id == route.id;
    
    // Premium kontrolü - free kullanıcılar sadece önizleyebilir
    if (!PremiumService.instance.isPremium && !isFirstRoute && !PremiumService.instance.canApplyCuratedRoute()) {
      _showPaywall();
      return;
    }
    
    // Önce kullanıcıya gün seçtir
    final selectedDay = await _showDaySelectionDialog(route.name);
    if (selectedDay == null) return; // İptal edildi

    HapticFeedback.mediumImpact();
    
    // Kullanımı artır
    await PremiumService.instance.useCuratedRoute();
    
    setState(() {
      _loading = true;
    });

    // Yapay gecikme (loader görünsün)
    await Future.delayed(const Duration(milliseconds: 600));

    // Rota mekanlarını bul ve ekle
    final List<Highlight> newPlaces = [];
    if (_city != null) {
      for (var name in route.placeNames) {
        final normalizedName = name.toLowerCase().trim();
        Highlight? p;
        // ID eşleşmesi
        p = _city!.highlights.where((h) => h.id != null && h.id == name).firstOrNull;
        // İsim eşleşmesi
        p ??= _city!.highlights.where((h) => h.name == name || h.nameEn == name).firstOrNull;
        // Case-insensitive eşleşme
        p ??= _city!.highlights.where((h) =>
            h.name.toLowerCase().trim() == normalizedName ||
            (h.nameEn?.toLowerCase().trim() == normalizedName)).firstOrNull;
        if (p != null && !newPlaces.contains(p)) {
          newPlaces.add(p);
          _placeCityMap[p.name] = _city!.city.toLowerCase();
        }
      }
    }

    if (newPlaces.isNotEmpty) {
      // V4.3: Hedef gün doluysa kullanıcıya sor — Üzerine ekle / Sil ve değiştir / İptal
      String mergeChoice = 'replace'; // varsayılan: yeni güne tamamen yerleştir
      final hasExistingPlaces = (_dayPlans[selectedDay]?.isNotEmpty ?? false);
      if (hasExistingPlaces) {
        setState(() => _loading = false);
        final choice = await _showMergeOrReplaceDialog(
          dayNumber: selectedDay,
          existingCount: _dayPlans[selectedDay]!.length,
          newRouteName: route.name,
          newRoutePlaceCount: newPlaces.length,
        );
        if (choice == null) {
          // İptal
          return;
        }
        mergeChoice = choice;
        setState(() => _loading = true);
        await Future.delayed(const Duration(milliseconds: 200));
      }

      setState(() {
        // Yeni gün kontrolü
        if (selectedDay > _totalDays) {
          _totalDays = selectedDay;
          _dayPlans[selectedDay] = [];

          // Tab controller'ı güncelle
          _dayTabController?.dispose();
          _dayTabController = TabController(length: _totalDays, vsync: this);
        }

        if (mergeChoice == 'append' && _dayPlans[selectedDay]?.isNotEmpty == true) {
          // Mevcut yerlerin üzerine ekle
          _dayPlans[selectedDay]!.addAll(newPlaces);
          _routeOrigins.remove(selectedDay.toString());
        } else {
          // Replace veya boş gün: yeni rota tüm günü doldursun
          _dayPlans[selectedDay] = newPlaces;
          _routeOrigins[selectedDay.toString()] = route.id;
        }

        // 🔥 OTOMATİK OPTİMİZASYON: Eklendikten sonra sırayı mesafeye göre optimize et
        _dayPlans[selectedDay] = _getOptimizedSequence(_dayPlans[selectedDay]!);
      });

      // 🔥 HARİTA SENKRONİZASYONU: Haritayı ve rotayı yeni sıraya göre anında güncelle
      if (selectedDay == (_dayTabController?.index != null ? _dayTabController!.index : 0)) {
        await _updateRouteMapMarkers(_dayPlans[selectedDay]!);
        await _fetchRouteForMode(_selectedTransportMode, selectedDay);
      }
      
      await _saveTripData();
      TripUpdateService().notifyTripChanged();
    }

    setState(() {
      _loading = false;
    });

    if (!mounted) return;

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: WanderlustColors.accent),
            const SizedBox(width: 12),
            Expanded(
              child: Text(
                AppLocalizations.instance.routeAddedToDay(route.name, selectedDay),
                style: const TextStyle(color: WanderlustColors.textWhite),
              ),
            ),
          ],
        ),
        backgroundColor: WanderlustColors.bgCardLight,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
    
    // Rotam sekmesine geç
    _mainTabController?.animateTo(1);
    
    // Seçilen güne geç (day tabs are 0-indexed)
    if (_dayTabController != null && _dayTabController!.length > 0) {
      final targetIndex = (selectedDay - 1).clamp(0, _dayTabController!.length - 1);
      _dayTabController!.animateTo(targetIndex);
    }
  }



  // SHOW PAYWALL
  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }

  Future<void> _generateAiPlanForExistingUser() async {
    final prefs = await SharedPreferences.getInstance();
    final cityId = prefs.getString("selectedCity") ?? "barcelona";
    
    // Check if user already used the free AI plan for this city
    final trialCount = prefs.getInt("itinerary_trial_count_$cityId") ?? 0;
    final hasUsedAiPlan = trialCount >= 1;
    
    if (hasUsedAiPlan && !PremiumService.instance.isPremium) {
      // Already used once and not premium → show paywall
      if (!mounted) return;
      showPaywall(
        context,
        onSubscribe: (planId) async {
          // After subscribing, allow them to generate
          setState(() {});
        },
      );
      return;
    }
    
    // Increment trial count (set BEFORE navigation so it persists even if user cancels midway)
    await prefs.setInt("itinerary_trial_count_$cityId", trialCount + 1);
    
    // Direkt Loading Ekranına git (Preview stepini atla, direkt entegre et)
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (context) => AnalysisLoadingScreen(cityId: cityId),
      ),
    );
  }

  void _showAiItineraryPreview(String cityId, Map<String, dynamic> schedule) {
    // Parse the schedule into a list of days for easier rendering
    final List<int> dayKeys = schedule.keys.map((k) => int.parse(k)).toList()..sort();
    
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => DraggableScrollableSheet(
        initialChildSize: 0.85,
        minChildSize: 0.5,
        maxChildSize: 0.95,
        builder: (context, scrollController) {
          return Container(
            decoration: const BoxDecoration(
              color: WanderlustColors.bgDark,
              borderRadius: BorderRadius.vertical(top: Radius.circular(32)),
            ),
            child: Column(
              children: [
                // Handle
                Container(
                  margin: const EdgeInsets.only(top: 12),
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                
                // Header
                Padding(
                  padding: const EdgeInsets.fromLTRB(24, 20, 24, 0),
                  child: Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            FittedBox(
                              fit: BoxFit.scaleDown,
                              alignment: Alignment.centerLeft,
                              child: Text(
                                isEnglish ? "Smart Preview" : "Akıllı Önizleme",
                                style: const TextStyle(
                                  color: WanderlustColors.textWhite,
                                  fontSize: 24,
                                  fontWeight: FontWeight.w800,
                                ),
                              ),
                            ),
                            const SizedBox(height: 4),
                            Text(
                              isEnglish 
                                ? "Here's your artificial intelligence powered plan." 
                                : "Yapay zeka senin için bu rotayı hazırladı.",
                              style: TextStyle(
                                color: WanderlustColors.textWhite.withOpacity(0.6),
                                fontSize: 13,
                              ),
                              maxLines: 2,
                              overflow: TextOverflow.ellipsis,
                            ),
                          ],
                        ),
                      ),
                      Container(
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          color: WanderlustColors.accent.withOpacity(0.15),
                          shape: BoxShape.circle,
                          border: Border.all(color: WanderlustColors.accent.withOpacity(0.3)),
                        ),
                        child: const Icon(Icons.auto_awesome, color: WanderlustColors.accent, size: 20),
                      ),
                    ],
                  ),
                ),
                
                const SizedBox(height: 20),
                
                // Plans List
                Expanded(
                  child: ListView.builder(
                    controller: scrollController,
                    padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 0),
                    itemCount: dayKeys.length,
                    itemBuilder: (context, index) {
                      final dayNum = dayKeys[index];
                      final List<dynamic> dayItems = schedule[dayNum.toString()] ?? [];
                      
                      return Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Padding(
                            padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 8),
                            child: Row(
                              children: [
                                Text(
                                  isEnglish ? "Day $dayNum" : "$dayNum. Gün",
                                  style: const TextStyle(
                                    color: WanderlustColors.accent,
                                    fontSize: 18,
                                    fontWeight: FontWeight.w800,
                                  ),
                                ),
                                const SizedBox(width: 8),
                                Expanded(child: Divider(color: WanderlustColors.accent.withOpacity(0.3), thickness: 1)),
                              ],
                            ),
                          ),
                          ...dayItems.map((item) {
                            final highlight = Highlight.fromJson(item, city: cityId);
                            final idx = dayItems.indexOf(item);
                            return _buildPreviewStopCard(highlight, idx, dayItems.length);
                          }).toList(),
                        ],
                      );
                    },
                  ),
                ),
                
                // Bottom Actions
                Container(
                  padding: const EdgeInsets.all(24),
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard,
                    border: Border(top: BorderSide(color: Colors.white.withOpacity(0.05))),
                  ),
                  child: SafeArea(
                    child: Row(
                      children: [
                        Expanded(
                          child: TextButton(
                            onPressed: () => Navigator.pop(context),
                            child: Text(
                              isEnglish ? "Cancel" : "İptal",
                              style: TextStyle(color: WanderlustColors.textWhite.withOpacity(0.5), fontWeight: FontWeight.w600),
                            ),
                          ),
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          flex: 2,
                          child: GestureDetector(
                            onTap: () async {
                              Navigator.pop(context); // Close preview
                              
                              // Show saving loader
                              showDialog(
                                context: context,
                                barrierDismissible: false,
                                builder: (context) => const Center(child: CircularProgressIndicator(color: WanderlustColors.accent)),
                              );
                              
                              await SmartItineraryBuilder.savePlan(cityId, schedule);
                              
                              if (mounted) {
                                Navigator.pop(context); // Close saving loader
                                _loadData(); // Reload UI
                                HapticFeedback.heavyImpact();
                              }
                            },
                            child: Container(
                              padding: const EdgeInsets.symmetric(vertical: 16),
                              decoration: BoxDecoration(
                                gradient: WanderlustColors.accentGradient,
                                borderRadius: BorderRadius.circular(16),
                                boxShadow: [
                                  BoxShadow(
                                    color: WanderlustColors.accent.withOpacity(0.3),
                                    blurRadius: 12,
                                    offset: const Offset(0, 4),
                                  ),
                                ],
                              ),
                              child: Center(
                                child: Text(
                                  isEnglish ? "Apply This Plan" : "Planı Uygula",
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 16,
                                    fontWeight: FontWeight.w800,
                                  ),
                                ),
                              ),
                            ),
                          ),
                        ),
                      ],
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

  Widget _buildPreviewStopCard(Highlight place, int index, int total) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.03),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.05)),
      ),
      child: Row(
        children: [
          // Index dot/line aesthetic
          Column(
            children: [
              Container(
                width: 24,
                height: 24,
                decoration: BoxDecoration(
                  color: WanderlustColors.accent.withOpacity(0.2),
                  shape: BoxShape.circle,
                ),
                child: Center(
                  child: Text(
                    (index + 1).toString(),
                    style: const TextStyle(color: WanderlustColors.accent, fontSize: 12, fontWeight: FontWeight.bold),
                  ),
                ),
              ),
              if (index < total - 1)
                Container(
                  width: 2,
                  height: 20,
                  color: WanderlustColors.accent.withOpacity(0.2),
                ),
            ],
          ),
          const SizedBox(width: 12),
          
          // Place Info
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  place.getLocalizedName(isEnglish),
                  style: const TextStyle(
                    color: WanderlustColors.textWhite,
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                  ),
                  maxLines: 1,
                  overflow: TextOverflow.ellipsis,
                ),
                const SizedBox(height: 2),
                Text(
                  AppLocalizations.instance.translateCategory(place.category),
                  style: TextStyle(
                    color: WanderlustColors.textGrey,
                    fontSize: 12,
                  ),
                ),
              ],
            ),
          ),
          
          const Icon(Icons.arrow_forward_ios_rounded, color: WanderlustColors.textGrey, size: 12),
        ],
      ),
    );
  }
  
  // TUTORIAL
  void _showRoutesTutorial() {
    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        // Step 1: Tabs
        TargetFocus(
          identify: "routes_tab",
          keyTarget: _routesTabKey,
          shape: ShapeLightFocus.RRect,
          radius: 14,
          paddingFocus: 0,
          contents: [
            TargetContent(
              align: ContentAlign.bottom,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: "Rotanı Seç!",
                  description: "Şehrin en iyi hazır rotalarını buradan keşfedebilir veya kendi oluşturduğun rotayı 'Rotam' sekmesinden yönetebilirsin.",
                  onNext: () => controller.next(),
                  onSkip: () => controller.skip(),
                  currentStep: 1,
                  totalSteps: 2,
                  isArrowUp: true,
                );
              },
            ),
          ],
        ),
        // Step 2: Create Route Button
        TargetFocus(
          identify: "create_route_button",
          keyTarget: _createRouteButtonKey,
          shape: ShapeLightFocus.RRect,
          radius: 12,
          paddingFocus: 4,
          contents: [
            TargetContent(
              align: ContentAlign.top,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: "Rotayı Ekle",
                  description: "Beğendiğin bir hazır rotayı tek tıkla kendi seyahat planına ekleyebilirsin. Tüm duraklar otomatik olarak 'Rotam' sekmesine eklenir.",
                  onNext: () {
                    controller.next();
                    TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_ROUTES);
                  },
                  onSkip: () => controller.skip(),
                  currentStep: 2,
                  totalSteps: 2,
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
        TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_ROUTES);
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

  // TUTORIAL - My Route Tab
  void _showMyRouteTutorial() {
    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        // Step 1: Stats + Transport Modes
        TargetFocus(
          identify: "my_route_stats",
          keyTarget: _myRouteStatsKey,
          shape: ShapeLightFocus.RRect,
          radius: 16,
          paddingFocus: 4,
          contents: [
            TargetContent(
              align: ContentAlign.bottom,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: "Rota Özeti",
                  description: "Rotandaki toplam durak sayısını, mesafeyi ve farklı ulaşım modlarına göre süreyi buradan görebilirsin. Yürüyüş, bisiklet, toplu taşıma veya araç seçeneklerinden birini seç.",
                  onNext: () => controller.next(),
                  onSkip: () => controller.skip(),
                  currentStep: 1,
                  totalSteps: 2,
                  isArrowUp: true,
                );
              },
            ),
          ],
        ),
        // Step 2: Start Route Button
        TargetFocus(
          identify: "start_route_button",
          keyTarget: _startRouteButtonKey,
          shape: ShapeLightFocus.RRect,
          radius: 14,
          paddingFocus: 4,
          contents: [
            TargetContent(
              align: ContentAlign.top,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: AppLocalizations.instance.startRoute,
                  description: "Planladığın rotayı tek tıkla başlat, adım adım keşfetmeye başla.",
                  onNext: () {
                    controller.next();
                    TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_MY_ROUTE);
                  },
                  onSkip: () => controller.skip(),
                  currentStep: 2,
                  totalSteps: 2,
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
         TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_MY_ROUTE);
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

  /// V4.3: Hazır rota uygulanırken hedef gün doluysa kullanıcıya sor.
  /// Döner: 'append' (mevcut yerlere ekle), 'replace' (mevcut yerleri sil),
  /// veya null (iptal).
  Future<String?> _showMergeOrReplaceDialog({
    required int dayNumber,
    required int existingCount,
    required String newRouteName,
    required int newRoutePlaceCount,
  }) async {
    final isEn = AppLocalizations.instance.isEnglish;
    return showModalBottomSheet<String>(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (ctx) {
        return Container(
          margin: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            color: WanderlustColors.bgCard,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: WanderlustColors.border),
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              const SizedBox(height: 20),
              Container(
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: WanderlustColors.textGrey.withOpacity(0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
              const SizedBox(height: 20),
              // Başlık
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                child: Text(
                  isEn ? "Day $dayNumber is full" : "$dayNumber. Gün dolu",
                  style: const TextStyle(
                    color: WanderlustColors.textWhite,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              const SizedBox(height: 6),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                child: Text(
                  isEn
                      ? "$existingCount places already planned. Adding \"$newRouteName\" ($newRoutePlaceCount places). What would you like to do?"
                      : "Bu günde zaten $existingCount yer var. \"$newRouteName\" ($newRoutePlaceCount yer) ekleniyor. Ne yapmak istersin?",
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                    color: WanderlustColors.textGrey,
                    fontSize: 13,
                    height: 1.4,
                  ),
                ),
              ),
              const SizedBox(height: 20),
              // Option 1: Append
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: GestureDetector(
                  onTap: () => Navigator.pop(ctx, 'append'),
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgDark,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: WanderlustColors.border),
                    ),
                    child: Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(10),
                          decoration: BoxDecoration(
                            color: accent.withOpacity(0.15),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: const Icon(Icons.playlist_add_rounded, color: accent, size: 22),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                isEn ? "Add on top" : "Üzerine ekle",
                                style: const TextStyle(
                                  color: WanderlustColors.textWhite,
                                  fontWeight: FontWeight.w600,
                                  fontSize: 15,
                                ),
                              ),
                              const SizedBox(height: 2),
                              Text(
                                isEn
                                    ? "Keep existing places + add new route"
                                    : "Mevcut yerleri koru + yeni rotayı ekle",
                                style: const TextStyle(
                                  color: WanderlustColors.textGrey,
                                  fontSize: 12,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Icon(Icons.chevron_right, color: WanderlustColors.textGrey),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 10),
              // Option 2: Replace
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: GestureDetector(
                  onTap: () => Navigator.pop(ctx, 'replace'),
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgDark,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: const Color(0xFFFF9800).withOpacity(0.4)),
                    ),
                    child: Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.all(10),
                          decoration: BoxDecoration(
                            color: const Color(0xFFFF9800).withOpacity(0.15),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: const Icon(Icons.refresh_rounded, color: Color(0xFFFF9800), size: 22),
                        ),
                        const SizedBox(width: 14),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                isEn ? "Replace day" : "Günü değiştir",
                                style: const TextStyle(
                                  color: WanderlustColors.textWhite,
                                  fontWeight: FontWeight.w600,
                                  fontSize: 15,
                                ),
                              ),
                              const SizedBox(height: 2),
                              Text(
                                isEn
                                    ? "Clear existing places + apply new route"
                                    : "Mevcut yerleri sil + yeni rotayı uygula",
                                style: const TextStyle(
                                  color: WanderlustColors.textGrey,
                                  fontSize: 12,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Icon(Icons.chevron_right, color: WanderlustColors.textGrey),
                      ],
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 10),
              // Option 3: Cancel
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: TextButton(
                  onPressed: () => Navigator.pop(ctx, null),
                  child: Text(
                    isEn ? "Cancel" : "İptal",
                    style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 14),
                  ),
                ),
              ),
              const SizedBox(height: 20),
            ],
          ),
        );
      },
    );
  }

  Future<int?> _showDaySelectionDialog(String routeName) async {
    return showDialog<int>(
      context: context,
      builder: (context) {
        return Dialog(
          backgroundColor: WanderlustColors.bgCard,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  AppLocalizations.instance.whichDay,
                  style: const TextStyle(
                      color: WanderlustColors.textWhite, fontSize: 18, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),
                Text(
                  AppLocalizations.instance.whichDayPlan(routeName),
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 14),
                ),
                const SizedBox(height: 20),
                ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 300),
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                         ...List.generate(_totalDays, (index) {
                             final day = index + 1;
                             final count = _dayPlans[day]?.length ?? 0;
                             return ListTile(
                               title: Text(AppLocalizations.instance.dayN(day), style: const TextStyle(color: WanderlustColors.textWhite)),
                               subtitle: Text(AppLocalizations.instance.nPlaces(count), style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 12)),
                               trailing: const Icon(Icons.arrow_forward_ios, color: accent, size: 16),
                               onTap: () => Navigator.pop(context, day),
                               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                               tileColor: Colors.transparent,
                               hoverColor: WanderlustColors.bgCardLight,
                             );
                         }),
                         const Divider(color: WanderlustColors.border),
                         ListTile(
                             title: Text(AppLocalizations.instance.createNewDay, style: TextStyle(color: WanderlustColors.textWhite, fontWeight: FontWeight.bold)),
                             subtitle: Text(AppLocalizations.instance.dayN(_totalDays + 1), style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 12)),
                             leading: const Icon(Icons.add_circle, color: accentGreen),
                             onTap: () => Navigator.pop(context, _totalDays + 1),
                         ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  void _reorganizeDays() {
    const placesPerDay = 5;
    final totalDays = _tripPlaces.isEmpty
        ? _tripDays
        : math
              .max(_tripDays, (_tripPlaces.length / placesPerDay).ceil())
              .clamp(1, 10);

    final dayPlans = <int, List<Highlight>>{};
    for (int i = 0; i < totalDays; i++) {
      final start = i * placesPerDay;
      final end = math.min(start + placesPerDay, _tripPlaces.length);
      if (start < _tripPlaces.length) {
        dayPlans[i + 1] = _tripPlaces.sublist(start, end);
      } else {
        dayPlans[i + 1] = [];
      }
    }

    setState(() {
      _dayPlans = dayPlans;
      _totalDays = totalDays;
      _dayTabController?.dispose();
      _dayTabController = TabController(length: totalDays, vsync: this);
    });
  }

  double _calculateTotalDistance(int day, {double detourFactor = 1.0}) {
    final places = _dayPlans[day] ?? [];
    double total = 0;
    for (int i = 0; i < places.length - 1; i++) {
      total += _haversine(
        places[i].lat,
        places[i].lng,
        places[i + 1].lat,
        places[i + 1].lng,
      );
    }
    return total * detourFactor;
  }

  double _haversine(double lat1, double lon1, double lat2, double lon2) {
    const R = 6371.0;
    final dLat = (lat2 - lat1) * math.pi / 180;
    final dLon = (lon2 - lon1) * math.pi / 180;
    final a =
        math.sin(dLat / 2) * math.sin(dLat / 2) +
        math.cos(lat1 * math.pi / 180) *
            math.cos(lat2 * math.pi / 180) *
            math.sin(dLon / 2) *
            math.sin(dLon / 2);
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a));
  }

  int _estimateWalkingTime(int day) =>
      (_calculateTotalDistance(day, detourFactor: 1.25) / 5 * 60).round(); // 5 km/h + 25% curve

  int _estimateDrivingTime(int day) =>
      (_calculateTotalDistance(day, detourFactor: 1.2) / 25 * 60).round(); // 25 km/h + 20% curve

  int _estimateTransitFallback(int day) =>
      (_calculateTotalDistance(day, detourFactor: 1.2) / 20 * 60).round(); // ~20 km/h avg for transit

  int _getCurrentTransportTime(int day) {
    switch (_selectedTransportMode) {
      case 0: return _estimateWalkingTime(day);
      case 1: return _transitTimeCache ?? _estimateTransitFallback(day); // Transit
      case 2: return _estimateDrivingTime(day);
      default: return _estimateWalkingTime(day);
    }
  }

  /// Fetch route for selected transport mode with caching
  Future<void> _fetchRouteForMode(int mode, int day) async {
    final places = _dayPlans[day] ?? [];
    if (places.length < 2) return;

    final modeString = _getModeString(mode);
    final cacheKey = "${modeString}_$day";

    // Check cache first
    if (_routeCache.containsKey(cacheKey)) {
      _applyRouteFromCache(cacheKey, mode);
      return;
    }

    setState(() {
      _routeLoading = true;
      if (mode == 1) {
        _transitLoading = true;
        _currentRouteSteps = [];
        _transitLegsUnavailable = false;
      }
      _routePolylines = {}; // Yeni rota yüklenirken eskiyi temizle
    });

    try {
      Map<String, dynamic>? result;
      final userOrigin = await _getUserOriginIfInCity();

      // Toplu taşıma için waypoint segmentasyon mantığı (Stitching)
      // Google Directions API transit modunda waypoint desteklemez, bu yüzden noktaları tek tek birleştiriyoruz.
      if (modeString == 'transit' && (places.length > 2 || userOrigin != null)) {
        final allSteps = <Map<String, dynamic>>[];
        double totalSeconds = 0;
        final allOverviewPoints = <LatLng>[];

        if (userOrigin != null) {
          final toPlace = places.first.name;
          final segmentResult = await DirectionsService().getDirections(
            origin: userOrigin,
            destination: LatLng(places.first.lat, places.first.lng),
            mode: modeString,
          );
          if (segmentResult != null) {
            final segmentSteps = List<Map<String, dynamic>>.from(segmentResult['steps'] ?? []);
            if (segmentSteps.isNotEmpty) {
              segmentSteps.first['context_from'] =
                  AppLocalizations.instance.isEnglish ? "Your Location" : "Konumun";
              segmentSteps.first['context_to'] = toPlace;
            }
            allSteps.addAll(segmentSteps);
            totalSeconds += (segmentResult['duration_seconds'] as double? ?? 0);
            allOverviewPoints.addAll(List<LatLng>.from(segmentResult['polyline_points'] ?? []));
          }
        }

        for (int i = 0; i < places.length - 1; i++) {
          final fromPlace = places[i].name;
          final toPlace = places[i + 1].name;
          
          final segmentResult = await DirectionsService().getDirections(
            origin: LatLng(places[i].lat, places[i].lng),
            destination: LatLng(places[i + 1].lat, places[i + 1].lng),
            mode: modeString,
          );
          if (segmentResult != null) {
            final segmentSteps = List<Map<String, dynamic>>.from(segmentResult['steps'] ?? []);
            // Inject context into the first and last step of this segment
            if (segmentSteps.isNotEmpty) {
              segmentSteps.first['context_from'] = fromPlace;
              segmentSteps.first['context_to'] = toPlace;
            }
            
            allSteps.addAll(segmentSteps);
            totalSeconds += (segmentResult['duration_seconds'] as double? ?? 0);
            allOverviewPoints.addAll(List<LatLng>.from(segmentResult['polyline_points'] ?? []));
          }
        }

        if (allSteps.isNotEmpty) {
          result = {
            'steps': allSteps,
            'duration_seconds': totalSeconds,
            'polyline_points': allOverviewPoints,
          };
        }
      } else {
        // Normal modlar için tek API isteği (Google Maps Optimize desteği ile)
        final routeOrigin = userOrigin ?? LatLng(places.first.lat, places.first.lng);
        final waypointStartIndex = userOrigin != null ? 0 : 1;
        result = await DirectionsService().getDirections(
          origin: routeOrigin,
          destination: LatLng(places.last.lat, places.last.lng),
          waypoints: places.length > 2
              ? places.sublist(waypointStartIndex, places.length - 1)
                  .map((p) => LatLng(p.lat, p.lng)).toList()
              : null,
          mode: modeString,
          optimizeWaypoints: false, // Don't optimize automatically, respect user sequence
        );
      }

      if (result != null && mounted) {
        final res = result;
        // Cache the result
        _routeCache[cacheKey] = res;

        // Parse duration for transit
        if (mode == 1) {
          final seconds = res['duration_seconds'] as double? ?? 0;
          _transitTimeCache = (seconds / 60).round();
        }

        // Update polylines with multi-modal visualization
        _updatePolylinesFromRoute(res, mode);

        setState(() {
          _routeLoading = false;
          _transitLoading = false;
          final steps =
              List<Map<String, dynamic>>.from(res['steps'] ?? []);
          _currentRouteSteps = steps;
          if (mode == 1) {
            // Önceki mantık: adımlarda TRANSIT yoksa uyarı — Google bazen transit
            // modunda yalnızca yürüyüş önerir veya yanıt MIXED olur; yine de adımlar geçerlidir.
            _transitLegsUnavailable = steps.isEmpty;
          } else {
            _transitLegsUnavailable = false;
          }
        });
      } else {
        await _applyFallbackRoutePolyline(places, mode);
        setState(() {
          _routeLoading = false;
          _transitLoading = false;
          if (mode == 1) {
            _currentRouteSteps = [];
            _transitLegsUnavailable = true;
            _transitTimeCache = null;
          }
        });
      }
    } catch (e) {
      print("Route API Error: $e");
      await _applyFallbackRoutePolyline(places, mode);
      if (mounted) {
        setState(() {
          _routeLoading = false;
          _transitLoading = false;
          if (mode == 1) {
            _currentRouteSteps = [];
            _transitLegsUnavailable = true;
            _transitTimeCache = null;
          }
        });
      }
    }
  }

  Future<void> _applyFallbackRoutePolyline(List<Highlight> places, int mode) async {
    if (!mounted || places.length < 2) return;

    final points = <LatLng>[];
    final userOrigin = await _getUserOriginIfInCity();
    if (userOrigin != null) {
      points.add(userOrigin);
    }
    points.addAll(places.map((p) => LatLng(p.lat, p.lng)));
    if (points.length < 2) return;

    final fallbackPolyline = Polyline(
      polylineId: PolylineId('route_fallback_${DateTime.now().millisecondsSinceEpoch}'),
      points: points,
      color: _getColorForMode(mode, null),
      width: 5,
      patterns: mode == 0 ? [PatternItem.dash(15), PatternItem.gap(10)] : [],
      jointType: JointType.round,
      startCap: Cap.roundCap,
      endCap: Cap.roundCap,
    );

    if (!mounted) return;
    setState(() {
      _routePolylines = {fallbackPolyline};
    });
  }

  String _getModeString(int mode) {
    switch (mode) {
      case 0: return 'walking';
      case 1: return 'transit';
      case 2: return 'driving';
      default: return 'walking';
    }
  }

  void _applyRouteFromCache(String cacheKey, int mode) {
    final cached = _routeCache[cacheKey];
    if (cached == null) return;

    // Apply transit time if transit mode
    if (mode == 1) {
      final seconds = cached['duration_seconds'] as double? ?? 0;
      _transitTimeCache = (seconds / 60).round();
    }

    _updatePolylinesFromRoute(cached, mode);
    setState(() {
      final steps =
          List<Map<String, dynamic>>.from(cached['steps'] ?? []);
      _currentRouteSteps = steps;
      if (mode == 1) {
        _transitLegsUnavailable = steps.isEmpty;
      } else {
        _transitLegsUnavailable = false;
      }
    });
  }

  void _updatePolylinesFromRoute(Map<String, dynamic> routeData, int mode) {
    final steps = routeData['steps'] as List<dynamic>? ?? [];
    final polylines = <Polyline>{};
    final String modeString = _getModeString(mode);
    final String timestamp = DateTime.now().millisecondsSinceEpoch.toString();

    // WALKING ve DRIVING modunda adım bazlı çizim yerine
    // bütünleşik overview polyline kullanarak kesintisiz rota çiz.
    if (mode == 0 || mode == 2 || steps.isEmpty) {
      final points = routeData['polyline_points'] as List<LatLng>? ?? [];
      if (points.isNotEmpty) {
        polylines.add(Polyline(
          polylineId: PolylineId('route_${modeString}_$timestamp'),
          points: points,
          color: _getColorForMode(mode, null),
          width: 5,
          patterns: mode == 0 ? [PatternItem.dash(15), PatternItem.gap(10)] : [],
          jointType: JointType.round,
          startCap: Cap.roundCap,
          endCap: Cap.roundCap,
        ));
      }
    } else {
      // TRANSIT/DRIVING modları için çoklu (multi-modal) gösterim
      int stepIndex = 0;
      for (var step in steps) {
        final travelMode = step['travel_mode'] as String? ?? 'WALKING';
        final points = step['polyline_points'] as List<LatLng>? ?? [];
        
        if (points.isEmpty) continue;

        Color lineColor;
        int lineWidth;
        List<PatternItem> patterns = [];

        if (travelMode == 'WALKING') {
          lineColor = accent;
          lineWidth = 4;
          patterns = [PatternItem.dash(12), PatternItem.gap(8)];
        } else if (travelMode == 'TRANSIT') {
          final transitDetails = step['transit_details'] as Map<String, dynamic>?;
          final vehicleType = transitDetails?['vehicle_type'] as String? ?? 'BUS';
          final colorHex = transitDetails?['color'] as String? ?? '#2196F3';
          
          if (vehicleType == 'SUBWAY' || vehicleType == 'METRO') {
            lineColor = _parseHexColor(colorHex) ?? const Color(0xFF2196F3);
          } else if (vehicleType == 'TRAM') {
            lineColor = _parseHexColor(colorHex) ?? const Color(0xFF9C27B0);
          } else {
            lineColor = _parseHexColor(colorHex) ?? const Color(0xFF4CAF50);
          }
          lineWidth = 6;
        } else {
          lineColor = const Color(0xFF9C27B0);
          lineWidth = 5;
        }

        polylines.add(Polyline(
          polylineId: PolylineId('step_${modeString}_${stepIndex}_$timestamp'),
          points: points,
          color: lineColor,
          width: lineWidth,
          patterns: patterns,
          jointType: JointType.round,
          startCap: Cap.roundCap,
          endCap: Cap.roundCap,
        ));
        stepIndex++;
      }

      // Transit modunda segment polyline'lar arasında görsel kopma olursa,
      // alttan tek parça bir overview çizgisi ile bağlantıyı güçlendir.
      if (mode == 1) {
        final basePoints = routeData['polyline_points'] as List<LatLng>? ?? [];
        if (basePoints.isNotEmpty) {
          polylines.add(Polyline(
            polylineId: PolylineId('route_base_${modeString}_$timestamp'),
            points: basePoints,
            color: const Color(0x552196F3),
            width: 5,
            jointType: JointType.round,
            startCap: Cap.roundCap,
            endCap: Cap.roundCap,
          ));
        }
      }
    }

    if (!mounted) return;
    setState(() => _routePolylines = polylines);
  }

  Color? _parseHexColor(String hex) {
    try {
      hex = hex.replaceFirst('#', '');
      if (hex.length == 6) {
        return Color(int.parse('FF$hex', radix: 16));
      }
    } catch (_) {}
    return null;
  }

  Color _getColorForMode(int mode, Map<String, dynamic>? transitDetails) {
    switch (mode) {
      case 0: return accent; // Walking - Amber
      case 1: return const Color(0xFF2196F3); // Transit - Blue
      case 2: return const Color(0xFF9C27B0); // Driving - Purple
      default: return accent;
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


  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    if (_loading) {
      return Scaffold(
        backgroundColor: WanderlustColors.bgDark,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: accent,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: const Icon(
                  Icons.map_outlined,
                  color: Colors.white,
                  size: 32,
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

    // Show fullscreen map if enabled
    if (_isMapFullscreen) {
      return _buildFullscreenMap();
    }

    return Scaffold(
      backgroundColor: Colors.transparent, // Transparent for map background
      body: MapBackground(
        child: SafeArea(
          child: Column(
            children: [
              _buildHeader(),
              _buildMainTabs(),
              Expanded(
                child: TabBarView(
                  controller: _mainTabController,
                  children: [
                    _buildSuggestedRoutesTab(), // Index 0: Suggested
                    _buildMyRouteTab(),        // Index 1: Plan/Itinerary
                    _buildMyListTab(),         // Index 2: Bucket List (Saved)
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
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
            child: Image.asset(
              'assets/icons/icon_renkli_routes.png',
              width: 32,
              height: 32,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                FittedBox(
                  fit: BoxFit.scaleDown,
                  alignment: Alignment.centerLeft,
                  child: Text(
                    AppLocalizations.instance.cityRoutes(_city?.getLocalizedCityName(AppLocalizations.instance.isEnglish) ?? ''),
                    style: const TextStyle(
                      color: WanderlustColors.textWhite,
                      fontSize: 24,
                      fontWeight: FontWeight.w700,
                      letterSpacing: -0.5,
                    ),
                  ),
                ),
                FittedBox(
                  fit: BoxFit.scaleDown,
                  alignment: Alignment.centerLeft,
                  child: Text(
                    "${_allSuggestedRoutes.length} ${AppLocalizations.instance.readyRoutes} • ${_tripPlaces.length} ${AppLocalizations.instance.selectedSpotsLabel} • ${AppLocalizations.instance.nDays(_tripDays)}",
                    style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMainTabs() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      height: 50,
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(14),
      ),
      child: Container(
        key: _routesTabKey,
        child: TabBar(
          controller: _mainTabController,
          onTap: (index) {
            // --- ANALYTICS: Log tab change ---
            AnalyticsService.instance.logTabChange(tabName: index == 0 ? 'suggested' : index == 1 ? 'my_route' : 'my_list');
          },
          indicator: BoxDecoration(
            color: accent,
            borderRadius: BorderRadius.circular(12),
          ),
          indicatorSize: TabBarIndicatorSize.tab,
          indicatorPadding: const EdgeInsets.all(4),
          dividerColor: Colors.transparent,
          labelColor: Colors.white,
          unselectedLabelColor: WanderlustColors.textGrey,
          labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
          tabs: [
            Tab(
              child: FittedBox(
                fit: BoxFit.scaleDown,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset('assets/icons/icon_readyroute.png', width: 18, height: 18),
                    const SizedBox(width: 8),
                    Text(AppLocalizations.instance.suggestedRoutes),
                  ],
                ),
              ),
            ),
            Tab(
              child: FittedBox(
                fit: BoxFit.scaleDown,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset('assets/icons/icon_myroute.png', width: 18, height: 18),
                    const SizedBox(width: 8),
                    Text(AppLocalizations.instance.myRoute),
                  ],
                ),
              ),
            ),
            Tab(
              child: FittedBox(
                fit: BoxFit.scaleDown,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.asset('assets/icons/icon_mylist.png', width: 18, height: 18),
                    const SizedBox(width: 8),
                    Text(AppLocalizations.instance.myList),
                    if (_dayPlans[0]?.isNotEmpty == true) ...[
                      const SizedBox(width: 6),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                        decoration: BoxDecoration(
                          color: accent,
                          borderRadius: BorderRadius.circular(10),
                        ),
                        child: Text(
                          _dayPlans[0]!.length.toString(),
                          style: const TextStyle(fontSize: 10, fontWeight: FontWeight.w700, color: Colors.white),
                        ),
                      ),
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

  // ══════════════════════════════════════════════════════════════════════════
  // MY ROUTE TAB - GERÇEK HARİTA ÖNİZLEMESİ
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildMyRouteTab() {
    // Veri yüklenirken boş ekranı gösterme (flicker'ı önle)
    if (_loading) {
      return const Center(
        child: CircularProgressIndicator(strokeWidth: 2, color: accent),
      );
    }
    return Stack(
      children: [
        NestedScrollView(
          controller: _myRouteScrollController,
          physics: const ClampingScrollPhysics(),
          headerSliverBuilder: (context, innerBoxIsScrolled) {
            return [
              if (_dayTabController != null && _totalDays > 0) // Changed from _totalDays > 1 to _totalDays > 0
                SliverPersistentHeader(
                  delegate: _SliverAppBarDelegate(_buildDayTabs()),
                  pinned: true,
                ),
              SliverToBoxAdapter(
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const SizedBox(height: 8),
                    _buildRealMapPreview(),
                    _buildTransportModeSelector(),
                    _buildTransitStepsInfo(),
                    _buildCombinedActionButtons(),
                    if (_totalDays <= 1 || _dayTabController == null)
                      const SizedBox(height: 16),
                  ],
                ),
              ),
            ];
          },
          body: _dayTabController != null && _totalDays > 0 // Changed from _totalDays > 1 to _totalDays > 0
              ? TabBarView(
                  controller: _dayTabController,
                  children: List.generate(
                    _totalDays, // Changed from _totalDays + 1 to _totalDays
                    (i) => _buildDayContent(i + 1), // Changed from (i) => _buildDayContent(i) to (i) => _buildDayContent(i + 1)
                  ),
                )
              : _buildDayContent(1), // Changed from _buildDayContent(0) to _buildDayContent(1)
        ),
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
                  _routesScrollController.animateTo(
                    0,
                    duration: const Duration(milliseconds: 500),
                    curve: Curves.easeOutCubic,
                  );
                },
                child: Container(
                  width: 44,
                  height: 44,
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard.withOpacity(0.8),
                    shape: BoxShape.circle,
                    border: Border.all(color: WanderlustColors.border.withOpacity(0.5)),
                  ),
                  child: const Icon(
                    Icons.keyboard_arrow_up_rounded,
                    color: WanderlustColors.textGrey,
                    size: 28,
                  ),
                ),
              ),
            ),
          ),
      ],
    );
  }


  Widget _buildStatsBar() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final distance = _calculateTotalDistance(currentDay);
    final transportTime = _getCurrentTransportTime(currentDay);
    final placesCount = _dayPlans[currentDay]?.length ?? 0;

    // Dynamic icon and label based on transport mode
    IconData transportIcon;
    String transportLabel;
    switch (_selectedTransportMode) {
      case 1:
        transportIcon = Icons.directions_transit;
        transportLabel = AppLocalizations.instance.isEnglish ? "Transit" : "Toplu T.";
        break;
      case 2:
        transportIcon = Icons.directions_car;
        transportLabel = AppLocalizations.instance.car;
        break;
      default:
        transportIcon = Icons.directions_walk;
        transportLabel = AppLocalizations.instance.walk;
    }

    // --- REAL DATA OVERRIDE ---
    // If we have real route data in cache, use it for stats
    final modeString = _getModeString(_selectedTransportMode);
    final cacheKey = "${modeString}_$currentDay";
    String? realDistanceText;
    int? realDurationMin;

    if (_routeCache.containsKey(cacheKey)) {
      final cached = _routeCache[cacheKey];
      realDistanceText = cached?['distance_text'];
      final double? seconds = cached?['duration_seconds'];
      if (seconds != null) {
        realDurationMin = (seconds / 60).round();
      }
    }
    // -------------------------

    // Use corrected estimates if no real data
    final detourFactor = _selectedTransportMode == 0 ? 1.25 : 1.15; // 0=walking, others slightly less
    final correctedDistance = _calculateTotalDistance(currentDay, detourFactor: detourFactor);
    final distanceLabel = realDistanceText ?? "${correctedDistance.toStringAsFixed(1)} km";
    final timeLabel = realDurationMin ?? transportTime;

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard.withOpacity(0.8),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 8,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _buildStatItem(Icons.place, "$placesCount", AppLocalizations.instance.spots),
          Container(width: 1, height: 40, color: WanderlustColors.border),
          _buildStatItem(
            Icons.straighten,
            distanceLabel,
            AppLocalizations.instance.distance,
          ),
          Container(width: 1, height: 40, color: WanderlustColors.border),
          _buildStatItem(transportIcon, "$timeLabel ${AppLocalizations.instance.min}", transportLabel),
        ],
      ),
    );
  }

  Widget _buildStatItem(IconData icon, String value, String label) {
    return Column(
      children: [
        Icon(icon, color: accent, size: 22),
        const SizedBox(height: 6),
        Text(
          value,
          style: const TextStyle(
            color: WanderlustColors.textWhite,
            fontSize: 16,
            fontWeight: FontWeight.w700,
          ),
        ),
        Text(label, style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 11)),
      ],
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TRANSPORT MODE SELECTOR (VibeMaps-Inspired)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTransportModeSelector() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    
    final places = _dayPlans[currentDay] ?? [];
    
    int walkTime = _estimateWalkingTime(currentDay);
    if (_routeCache.containsKey("walking_$currentDay")) {
      final seconds = _routeCache["walking_$currentDay"]?['duration_seconds'];
      if (seconds != null) walkTime = (seconds / 60).round();
    }

    int transitTime = _transitTimeCache ?? _estimateTransitFallback(currentDay);
    if (_routeCache.containsKey("transit_$currentDay")) {
      final seconds = _routeCache["transit_$currentDay"]?['duration_seconds'];
      if (seconds != null) transitTime = (seconds / 60).round();
    }

    int driveTime = _estimateDrivingTime(currentDay);
    if (_routeCache.containsKey("driving_$currentDay")) {
      final seconds = _routeCache["driving_$currentDay"]?['duration_seconds'];
      if (seconds != null) driveTime = (seconds / 60).round();
    }

    if (places.isEmpty) {
      walkTime = 0;
      transitTime = 0;
      driveTime = 0;
    }

    final modes = [
      {"icon": "assets/icons/icon_walking.png", "time": walkTime, "label": AppLocalizations.instance.min, "name": AppLocalizations.instance.walk},
      {"icon": "assets/icons/icon_subway.png", "time": transitTime, "label": AppLocalizations.instance.min, "name": AppLocalizations.instance.publicTransportShort},
      {"icon": "assets/icons/icon_Car.png", "time": driveTime, "label": AppLocalizations.instance.min, "name": AppLocalizations.instance.car},
    ];

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 12, 20, 12),
      padding: const EdgeInsets.all(4),
      height: 52, // Slightly more compact
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05), // Glassmorphic style
        borderRadius: BorderRadius.circular(20), 
        border: Border.all(color: Colors.white.withOpacity(0.1)),
      ),
      child: Stack(
        children: [
          // Animated Pill Indicator
          AnimatedAlign(
            duration: const Duration(milliseconds: 300),
            curve: Curves.easeInOutCubic,
            alignment: Alignment(
              -1.0 + (_selectedTransportMode * 1.0),
              0.0,
            ),
            child: FractionallySizedBox(
              widthFactor: 1 / 3,
              child: Container(
                height: 44, 
                decoration: BoxDecoration(
                  color: accent.withOpacity(0.9), 
                  borderRadius: BorderRadius.circular(22),
                  boxShadow: [
                    BoxShadow(
                      color: accent.withOpacity(0.3),
                      blurRadius: 12,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
              ),
            ),
          ),

          // Mode Buttons
          Row(
            children: List.generate(3, (index) {
              final mode = modes[index];
              final isSelected = _selectedTransportMode == index;
              final isTransit = index == 1;

              return Expanded(
                child: GestureDetector(
                  onTap: () {
                    HapticFeedback.selectionClick();
                    setState(() => _selectedTransportMode = index);
                    _fetchRouteForMode(index, currentDay);
                  },
                  behavior: HitTestBehavior.opaque,
                  child: Center(
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.min, // Center tightly
                      children: [
                        if (isTransit && _transitLoading)
                          SizedBox(
                            width: 16,
                            height: 16,
                            child: CircularProgressIndicator(
                              strokeWidth: 2,
                              valueColor: AlwaysStoppedAnimation<Color>(
                                isSelected ? Colors.white : Colors.white.withOpacity(0.6),
                              ),
                            ),
                          )
                        else
                          Image.asset(
                            mode["icon"] as String,
                            width: 22,
                            height: 22,
                          ),
                        const SizedBox(width: 6),
                        Text(
                          "${mode["time"]} ${mode["label"]}",
                          style: TextStyle(
                            color: isSelected ? Colors.white : WanderlustColors.textWhite,
                            fontSize: 13,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              );
            }),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // INTERACTIVE GOOGLE MAP
  // ══════════════════════════════════════════════════════════════════════════
  
  /// Harf/Sayı içeren custom marker oluşturur (A, B, C...)
  Future<BitmapDescriptor> _createCustomMarkerBitmap(String text) async {
    final pictureRecorder = ui.PictureRecorder();
    final canvas = Canvas(pictureRecorder);
    final paint = Paint()..color = accent;
    const radius = 24.0; // Marker büyüklüğü

    // Dış çember (gölge efekti için)
    canvas.drawCircle(
      const Offset(radius, radius),
      radius,
      Paint()..color = Colors.black.withOpacity(0.2)..maskFilter = const MaskFilter.blur(BlurStyle.normal, 4),
    );

    // Ana daire
    canvas.drawCircle(const Offset(radius, radius), radius - 2, paint);
    
    // Beyaz stroke
    canvas.drawCircle(
      const Offset(radius, radius), 
      radius - 2, 
      Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 2
    );

    // Text çizimi
    final textPainter = TextPainter(
      textDirection: TextDirection.ltr,
    );
    
    textPainter.text = TextSpan(
      text: text,
      style: const TextStyle(
        fontSize: 20.0,
        fontWeight: FontWeight.bold,
        color: Colors.white,
      ),
    );
    
    textPainter.layout();
    textPainter.paint(
      canvas,
      Offset(
        radius - textPainter.width / 2,
        radius - textPainter.height / 2,
      ),
    );

    final picture = pictureRecorder.endRecording();
    final img = await picture.toImage((radius * 2).toInt(), (radius * 2).toInt());
    final byteData = await img.toByteData(format: ui.ImageByteFormat.png);

    return BitmapDescriptor.fromBytes(byteData!.buffer.asUint8List());
  }

  Future<void> _updateRouteMapMarkers(List<Highlight> places) async {
    if (places.isEmpty) return;
    
    final markers = <Marker>{};
    final points = <LatLng>[];
    final userOrigin = await _getUserOriginIfInCity();
    if (userOrigin != null) {
      points.add(userOrigin);
      markers.add(
        Marker(
          markerId: const MarkerId("user_origin"),
          position: userOrigin,
          infoWindow: InfoWindow(
            title: AppLocalizations.instance.isEnglish ? "Your Location" : "Konumun",
          ),
          icon: BitmapDescriptor.defaultMarkerWithHue(BitmapDescriptor.hueAzure),
        ),
      );
    }

    for (int i = 0; i < places.length; i++) {
        final p = places[i];
        final latLng = LatLng(p.lat, p.lng);
        points.add(latLng);

        // A, B, C... şeklinde harflendirme (veya 1, 2, 3)
        // A = 65
        final markerText = String.fromCharCode(65 + i); // Alfabeye göre
        // final markerText = "${i + 1}"; // Sayıya göre

        final icon = await _createCustomMarkerBitmap(markerText);

        markers.add(
            Marker(
                markerId: MarkerId(p.name),
                position: latLng,
                infoWindow: InfoWindow(title: "$markerText. ${p.name}", snippet: p.category),
                icon: icon,
            ),
        );
    }
    
    // Polyline
    final polylines = <Polyline>{};
    if (points.length > 1) {
        polylines.add(
            Polyline(
                polylineId: const PolylineId("route_line"),
                points: points,
                color: accent,
                width: 5,
                jointType: JointType.round,
            ),
        );
    }

    if (!mounted) return;

    setState(() {
        _routeMarkers = markers;
        _routePolylines = polylines;
    });
    
    if (_routeMapController != null) {
      Future.delayed(const Duration(milliseconds: 500), () {
        if (!mounted) return;
        _fitRouteBounds();
      });
    }
  }

  Future<LatLng?> _getUserOriginIfInCity() async {
    if (_city == null) return null;
    await LocationContextService.instance.updateContext(_city!);
    if (!LocationContextService.instance.isTravelMode) return null;
    final coord = LocationContextService.instance.currentUserCoordinate;
    if (coord == null) return null;
    return LatLng(coord.lat, coord.lng);
  }

  void _fitRouteBounds() {
    if (!mounted) return;
    if (_routeMarkers.isEmpty) return;
    final c = _routeMapController;
    if (c == null) return;

    double minLat = 90.0, maxLat = -90.0, minLng = 180.0, maxLng = -180.0;

    for (var m in _routeMarkers) {
      final lat = m.position.latitude;
      final lng = m.position.longitude;
      if (lat < minLat) minLat = lat;
      if (lat > maxLat) maxLat = lat;
      if (lng < minLng) minLng = lng;
      if (lng > maxLng) maxLng = lng;
    }

    if (minLat == 90.0) return;

    try {
      c.animateCamera(
        CameraUpdate.newLatLngBounds(
          LatLngBounds(
            southwest: LatLng(minLat, minLng),
            northeast: LatLng(maxLat, maxLng),
          ),
          50,
        ),
      );
    } catch (_) {
      // Harita widget'ı dispose edildiyse veya platform kanalı kapandıysa yut
    }
  }

  Widget _buildRealMapPreview() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final places = _dayPlans[currentDay] ?? [];

    if (places.isEmpty) return const SizedBox.shrink();
    
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        // Header & Toggle
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                AppLocalizations.instance.dailyRouteMap,
                style: TextStyle(
                    color: WanderlustColors.textWhite, 
                    fontWeight: FontWeight.bold, 
                    fontSize: 16
                ),
              ),
              InkWell(
                onTap: () {
                   setState(() {
                      _showMapPreview = !_showMapPreview;
                   });
                   if (_showMapPreview) {
                       // Harita açılınca update et
                       Future.delayed(const Duration(milliseconds: 100), () {
                           if (!mounted) return;
                           _updateRouteMapMarkers(places);
                           _fetchRouteForMode(_selectedTransportMode, currentDay);
                       });
                   }
                },
                borderRadius: BorderRadius.circular(8),
                child: Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCardLight,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: WanderlustColors.border),
                  ),
                  child: Row(
                    children: [
                       Text(
                         _showMapPreview ? AppLocalizations.instance.hide : AppLocalizations.instance.show, 
                         style: const TextStyle(color: accent, fontSize: 12, fontWeight: FontWeight.bold),
                       ),
                       const SizedBox(width: 6),
                       Icon(
                         _showMapPreview ? Icons.visibility_off : Icons.visibility, 
                         color: accent, 
                         size: 16
                       ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),

        // Harita Alanı
        if (_showMapPreview)
           Builder(
             builder: (context) {
               final bool isMapLocked = currentDay > 1 && !PremiumService.instance.isPremium && _isAiPlan;
               
               return Container(
                height: 240,
                margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: WanderlustColors.border),
                  boxShadow: [
                      BoxShadow(color: Colors.black.withOpacity(0.2), blurRadius: 10, offset: const Offset(0,4)),
                  ],
                ),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(16),
                  child: Stack(
                    fit: StackFit.expand,
                    children: [
                      // Map Layer (Blurred if locked)
                      if (isMapLocked)
                        ImageFiltered(
                          imageFilter: ui.ImageFilter.blur(sigmaX: 5.0, sigmaY: 5.0),
                          child: GoogleMap(
                            initialCameraPosition: CameraPosition(
                              target: LatLng(_city?.centerLat ?? 41.3851, _city?.centerLng ?? 2.1734),
                              zoom: 12,
                            ),
                            markers: const {},
                            polylines: const {},
                            scrollGesturesEnabled: false,
                            zoomGesturesEnabled: false,
                            myLocationButtonEnabled: false,
                            zoomControlsEnabled: false,
                            mapToolbarEnabled: false,
                            compassEnabled: false,
                            onMapCreated: (controller) {
                              controller.setMapStyle(darkMapStyle);
                            },
                          ),
                        )
                      else
                        GoogleMap(
                          initialCameraPosition: CameraPosition(
                            target: LatLng(_city?.centerLat ?? 41.3851, _city?.centerLng ?? 2.1734),
                            zoom: 12,
                          ),
                          onMapCreated: (controller) {
                              _routeMapController = controller;
                              controller.setMapStyle(darkMapStyle);
                              _updateRouteMapMarkers(places);
                              _fetchRouteForMode(_selectedTransportMode, currentDay);
                          },
                          markers: _routeMarkers,
                          polylines: _routePolylines,
                          scrollGesturesEnabled: true,
                          zoomGesturesEnabled: true,
                          myLocationButtonEnabled: false,
                          zoomControlsEnabled: false,
                          mapToolbarEnabled: false,
                          compassEnabled: false,
                        ),

                      if (!isMapLocked) ...[
                        // Custom Zoom Controls
                        Positioned(
                          right: 12,
                          bottom: 12,
                          child: Column(
                            children: [
                              _buildZoomButton(Icons.add, () {
                                _routeMapController?.animateCamera(CameraUpdate.zoomIn());
                              }),
                              const SizedBox(height: 8),
                              _buildZoomButton(Icons.remove, () {
                                _routeMapController?.animateCamera(CameraUpdate.zoomOut());
                              }),
                            ],
                          ),
                        ),
                        // Fullscreen Button
                        Positioned(
                          right: 12,
                          top: 12,
                          child: _buildZoomButton(Icons.fullscreen, () {
                            setState(() => _isMapFullscreen = true);
                          }),
                        ),
                      ],

                      if (isMapLocked)
                        ClipRect(
                          child: BackdropFilter(
                            filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
                            child: Container(
                              color: Colors.white.withOpacity(0.15),
                              alignment: Alignment.center,
                              child: Column(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Icon(Icons.lock_rounded, color: Colors.black.withOpacity(0.7), size: 40),
                                  const SizedBox(height: 12),
                                  Text(
                                    AppLocalizations.instance.isEnglish ? "Plan Locked" : "Plan Kilitli",
                                    style: TextStyle(
                                      color: Colors.black.withOpacity(0.85),
                                      fontWeight: FontWeight.bold,
                                      fontSize: 16,
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
            },
          )
        else
          // Kapalıyken gösterilecek alternatif (boşluk veya çizgi)
          const SizedBox(height: 0),
      ],
    );
  }

  Widget _buildZoomButton(IconData icon, VoidCallback onTap) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.selectionClick();
        onTap();
      },
      child: Container(
        width: 36,
        height: 36,
        decoration: BoxDecoration(
          color: WanderlustColors.bgCard.withOpacity(0.9),
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: WanderlustColors.border),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.2),
              blurRadius: 6,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Icon(icon, color: accent, size: 20),
      ),
    );
  }

  /// Fullscreen map overlay with draggable route list
  Widget _buildFullscreenMap() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final places = _dayPlans[currentDay] ?? [];
    
    if (places.isEmpty) return const SizedBox.shrink();

    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: SafeArea(
        child: Stack(
          children: [
            // Main content column
            Column(
              children: [
                // Header with close button
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  child: Row(
                    children: [
                      GestureDetector(
                        onTap: () {
                          HapticFeedback.selectionClick();
                          setState(() => _isMapFullscreen = false);
                        },
                        child: Container(
                          padding: const EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            color: WanderlustColors.bgCard,
                            borderRadius: BorderRadius.circular(10),
                            border: Border.all(color: WanderlustColors.border),
                          ),
                          child: Icon(Icons.arrow_back, color: accent, size: 22),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Text(
                        AppLocalizations.instance.routeMap,
                        style: TextStyle(
                          color: WanderlustColors.textWhite,
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const Spacer(),
                      // Day indicator if multi-day
                      if (_totalDays > 0) // Changed from _totalDays > 1 to _totalDays > 0
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                          decoration: BoxDecoration(
                            color: accent.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(20),
                          ),
                          child: Text(
                            "${AppLocalizations.instance.day} $currentDay",
                            style: TextStyle(color: accent, fontWeight: FontWeight.w600, fontSize: 13),
                          ),
                        ),
                    ],
                  ),
                ),
                
                // Transport mode selector
                _buildTransportModeSelector(),
                
                // Map (takes remaining space)
                Expanded(
                  child: Container(
                    margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: WanderlustColors.border),
                    ),
                    child: ClipRRect(
                      borderRadius: BorderRadius.circular(16),
                      child: Stack(
                        children: [
                          GoogleMap(
                            initialCameraPosition: CameraPosition(
                              target: LatLng(places.first.lat, places.first.lng),
                              zoom: 13,
                            ),
                            onMapCreated: (controller) {
                              _routeMapController = controller;
                              controller.setMapStyle(darkMapStyle);
                              _updateRouteMapMarkers(places);
                              _fetchRouteForMode(_selectedTransportMode, currentDay);
                            },
                            markers: _routeMarkers,
                            polylines: _routePolylines,
                            scrollGesturesEnabled: true,
                            zoomGesturesEnabled: true,
                            myLocationButtonEnabled: false,
                            zoomControlsEnabled: false,
                            mapToolbarEnabled: false,
                            compassEnabled: true,
                            trafficEnabled: false,
                          ),
                          // Zoom controls
                          Positioned(
                            right: 12,
                            bottom: 12,
                            child: Column(
                              children: [
                                _buildZoomButton(Icons.add, () {
                                  _routeMapController?.animateCamera(CameraUpdate.zoomIn());
                                }),
                                const SizedBox(height: 8),
                                _buildZoomButton(Icons.remove, () {
                                  _routeMapController?.animateCamera(CameraUpdate.zoomOut());
                                }),
                              ],
                            ),
                          ),
                          // Exit fullscreen button
                          Positioned(
                            right: 12,
                            top: 12,
                            child: _buildZoomButton(Icons.fullscreen_exit, () {
                              setState(() => _isMapFullscreen = false);
                            }),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
            
            // Draggable scrollable sheet for route stops
            DraggableScrollableSheet(
              initialChildSize: 0.25,
              minChildSize: 0.12,
              maxChildSize: 0.7,
              builder: (context, scrollController) {
                // 🔥 SYNC SCHEDULE: Calculate dynamic arrival times for fullscreen view
                final schedule = _calculateScheduleForDay(places, _selectedTransportMode, currentDay);

                return Container(
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard,
                    borderRadius: const BorderRadius.vertical(top: Radius.circular(20)),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.3),
                        blurRadius: 20,
                        offset: const Offset(0, -5),
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      // Handle bar
                      Container(
                        margin: const EdgeInsets.only(top: 12, bottom: 8),
                        width: 40,
                        height: 4,
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.3),
                          borderRadius: BorderRadius.circular(2),
                        ),
                      ),
                      
                      // Header with start button
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 16),
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              AppLocalizations.instance.stops,
                              style: const TextStyle(
                                color: WanderlustColors.textWhite,
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                            Text(
                              "${places.length} ${AppLocalizations.instance.spots.toLowerCase()}",
                              style: const TextStyle(
                                color: WanderlustColors.textGrey,
                                fontSize: 13,
                              ),
                            ),
                          ],
                        ),
                      ),
                      
                      const SizedBox(height: 8),
                      
                      // Scrollable stops list
                      Expanded(
                        child: ListView.builder(
                          controller: scrollController,
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          itemCount: places.length + 1, // +1 for the start button at end
                          itemBuilder: (context, index) {
                            if (index == places.length) {
                              // Start route button at the end
                              return Padding(
                                padding: const EdgeInsets.symmetric(vertical: 16),
                                child: GestureDetector(
                                  onTap: () => _startRouteInGoogleMaps(currentDay),
                                  child: Container(
                                    padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 20),
                                    decoration: BoxDecoration(
                                      color: Colors.white.withOpacity(0.95),
                                      borderRadius: BorderRadius.circular(14),
                                      boxShadow: [
                                        BoxShadow(
                                          color: Colors.black.withOpacity(0.12),
                                          blurRadius: 10,
                                          offset: const Offset(0, 4),
                                        ),
                                      ],
                                    ),
                                    child: Row(
                                      mainAxisAlignment: MainAxisAlignment.center,
                                      children: [
                                        const Icon(Icons.navigation_rounded, color: Color(0xFF1A1A2E), size: 20),
                                        const SizedBox(width: 10),
                                        Text(
                                          AppLocalizations.instance.startRoute,
                                          style: const TextStyle(
                                            color: Color(0xFF1A1A2E),
                                            fontSize: 15,
                                            fontWeight: FontWeight.w700,
                                          ),
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                              );
                            }
                            
                            final place = places[index];
                            final timeText = index < schedule.length ? schedule[index] : "";
                            
                            return Padding(
                              padding: const EdgeInsets.only(bottom: 12),
                              child: _buildHorizontalPlaceCard(
                                currentDay, 
                                place, 
                                index, 
                                timeText: timeText, // 🔥 Pass the dynamic time
                                isReadOnly: true,
                                isLast: index == places.length - 1,
                              ),
                            );
                          },
                        ),
                      ),
                    ],
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMyListTab() {
     return Column(
       children: [
         Padding(
           padding: const EdgeInsets.fromLTRB(20, 20, 20, 10),
           child: Row(
             children: [
               Icon(Icons.bookmark, color: accent, size: 20),
               SizedBox(width: 8),
               Text(
                 AppLocalizations.instance.isEnglish ? "My Bucket List" : "Şehir Listem",
                 style: const TextStyle(color: WanderlustColors.textWhite, fontSize: 18, fontWeight: FontWeight.bold),
               ),
               Spacer(),
               Text(
                 "${_dayPlans[0]?.length ?? 0} ${AppLocalizations.instance.selectedSpotsLabel}",
                 style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
               ),
             ],
           ),
         ),
         Expanded(child: _buildDayContent(0)),
       ],
     );
  }

  Widget _buildCombinedActionButtons() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final placesCount = _dayPlans[currentDay]?.length ?? 0;
    final bool isLocked = !PremiumService.instance.isPremium && _isAiPlan && currentDay > 1;
    
    // Distance calculation logic
    final modeString = _getModeString(_selectedTransportMode);
    final cacheKey = "${modeString}_$currentDay";
    String? realDistanceText;
    if (_routeCache.containsKey(cacheKey)) {
      realDistanceText = _routeCache[cacheKey]?['distance_text'];
    }
    final detourFactor = _selectedTransportMode == 0 ? 1.25 : 1.15;
    final correctedDistance = placesCount == 0 ? 0.0 : _calculateTotalDistance(currentDay, detourFactor: detourFactor);
    final distanceLabel = placesCount == 0 ? "0 km" : (realDistanceText ?? "${correctedDistance.toStringAsFixed(1)} km");
    final subtitle = "$placesCount ${AppLocalizations.instance.isEnglish ? 'stops' : 'durak'} • $distanceLabel";

    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
      padding: const EdgeInsets.symmetric(vertical: 4),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight, width: 1),
      ),
      child: Row(
        children: [
          // Start Route Action
          Expanded(
            flex: 1,
            child: GestureDetector(
              onTap: isLocked ? _showPaywall : () => _startRouteInGoogleMaps(currentDay),
              behavior: HitTestBehavior.opaque,
              child: Opacity(
                opacity: isLocked ? 0.3 : 1.0,
                child: Container(
                  height: 64,
                  margin: const EdgeInsets.symmetric(vertical: 4),
                  padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: accent, width: 0.5),
                  ),
                  child: Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Image.asset('assets/icons/icon_start.png', width: 20, height: 20),
                            const SizedBox(width: 6),
                            Flexible(
                              child: Text(
                                AppLocalizations.instance.startRoute,
                                style: TextStyle(
                                  color: accent,
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                ),
                                maxLines: 1,
                                overflow: TextOverflow.ellipsis,
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 2),
                        Text(
                          subtitle,
                          style: TextStyle(
                            color: WanderlustColors.textGrey,
                            fontSize: 11,
                            fontWeight: FontWeight.w500,
                          ),
                          textAlign: TextAlign.center,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
          ),
          
          const SizedBox(width: 10),
          
          // Complete Route Action
          Expanded(
            flex: 1,
            child: GestureDetector(
              onTap: isLocked ? _showPaywall : _completeRoute,
              behavior: HitTestBehavior.opaque,
              child: Opacity(
                opacity: isLocked ? 0.3 : 1.0,
                child: Container(
                  height: 64,
                  margin: const EdgeInsets.symmetric(vertical: 4),
                  padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(color: accent, width: 0.5),
                  ),
                  child: Center(
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Image.asset('assets/icons/icon_complete.png', width: 20, height: 20),
                        const SizedBox(width: 6),
                        Flexible(
                          child: Text(
                            AppLocalizations.instance.isEnglish ? "Complete Route" : "Rotayı Tamamla",
                            style: TextStyle(
                              color: accent,
                              fontSize: 14,
                              fontWeight: FontWeight.w600,
                            ),
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
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
    );
  }

  Future<void> _completeRoute() async {
    HapticFeedback.mediumImpact();

    // Show confirmation dialog
    final confirmed = await showDialog<bool>(
      barrierColor: Colors.black.withOpacity(0.8),
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: WanderlustColors.bgCard.withOpacity(0.95),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
        title: Text(
          AppLocalizations.instance.isEnglish ? "Complete Trip?" : "Rotayı Tamamla?",
          style: const TextStyle(color: WanderlustColors.textWhite),
        ),
        content: Text(
          AppLocalizations.instance.isEnglish 
              ? "This will clear your current route and add it to your completed routes history."
              : "Mevcut rotanız silinecek ve tamamlanan rotalar geçmişine eklenecek.",
          style: const TextStyle(color: WanderlustColors.textGrey),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(
              AppLocalizations.instance.cancel,
              style: const TextStyle(color: WanderlustColors.textGrey),
            ),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(
              AppLocalizations.instance.confirm,
              style: const TextStyle(color: accent, fontWeight: FontWeight.bold),
            ),
          ),
        ],
      ),
    );

    if (confirmed != true) return;

    // 1. Rota detaylarını hazırla ve geçmişe kaydet
    try {
      final prefs = await SharedPreferences.getInstance();
      
      // Aktif günü ve yerleri al
      final activeDayIndex = _dayTabController?.index ?? 0;
      final currentDayPlaces = _dayPlans[activeDayIndex] ?? [];
      final currentDayPlaceNames = currentDayPlaces.map((p) => p.name).toList();

      if (currentDayPlaces.isEmpty) {
         if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(
              content: Text(
                AppLocalizations.instance.isEnglish ? "No places to complete for this day." : "Bu gün için tamamlanacak mekan yok.",
                style: const TextStyle(color: WanderlustColors.textWhite),
              ),
              backgroundColor: WanderlustColors.bgCardLight,
              behavior: SnackBarBehavior.floating,
            ),
          );
         }
        return;
      }
      
      // Rota ismini belirle
      String routeName = AppLocalizations.instance.isEnglish ? "My Trip" : "Gezim";
      if (_city != null) {
        routeName = "${_city!.city} ${AppLocalizations.instance.isEnglish ? 'Trip' : 'Gezisi'}";
      }
      
      // Curated route kontrolü (Sadece bu gün için)
      bool isCurated = false;
      if (_routeOrigins.containsKey(activeDayIndex.toString())) {
        final routeId = _routeOrigins[activeDayIndex.toString()];
        try {
          final match = _allSuggestedRoutes.firstWhere((r) => r.id == routeId);
          routeName = match.name;
          isCurated = true;
        } catch (_) {}
      }

      // Eğer custom rota ise kullanıcıya isim sor
      if (!isCurated) {
        final customName = await showDialog<String>(
          context: context,
          barrierDismissible: false,
          builder: (context) {
            String tempName = routeName;
            return AlertDialog(
              backgroundColor: WanderlustColors.bgCard.withOpacity(0.95),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
              title: Text(
                 AppLocalizations.instance.isEnglish ? "Name Your Trip" : "Gezinize İsim Verin",
                 style: const TextStyle(color: WanderlustColors.textWhite),
              ),
              content: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    AppLocalizations.instance.isEnglish 
                      ? "Give your custom route a memorable name."
                      : "Oluşturduğunuz bu rotaya hatırlanabilir bir isim verin.",
                    style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                  ),
                  const SizedBox(height: 16),
                  TextField(
                    autofocus: true,
                    style: const TextStyle(color: WanderlustColors.textWhite),
                    decoration: InputDecoration(
                      filled: true,
                      fillColor: WanderlustColors.bgDark,
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(12),
                        borderSide: const BorderSide(color: WanderlustColors.border),
                      ),
                      focusedBorder: OutlineInputBorder(
                         borderRadius: BorderRadius.circular(12),
                         borderSide: const BorderSide(color: accent),
                      ),
                      hintText: routeName,
                      hintStyle: TextStyle(color: WanderlustColors.textGrey.withOpacity(0.5)),
                    ),
                    controller: TextEditingController(text: routeName),
                    onChanged: (val) => tempName = val,
                  ),
                ],
              ),
              actions: [
                 TextButton(
                  onPressed: () => Navigator.pop(context, null), // Cancel
                  child: Text(
                    AppLocalizations.instance.cancel,
                    style: const TextStyle(color: WanderlustColors.textGrey),
                  ),
                ),
                TextButton(
                  onPressed: () => Navigator.pop(context, tempName.isEmpty ? routeName : tempName),
                  child: Text(
                    AppLocalizations.instance.save,
                    style: const TextStyle(color: accent, fontWeight: FontWeight.bold),
                  ),
                ),
              ],
            );
          },
        );

        if (customName == null) return; // Kullanıcı iptal etti
        routeName = customName;
      }

      // CompletedRoute objesi oluştur
      final completedRoute = CompletedRoute(
        id: DateTime.now().millisecondsSinceEpoch.toString(),
        name: routeName,
        cityName: _city?.getLocalizedCityName(AppLocalizations.instance.isEnglish) ?? "Unknown",
        date: DateTime.now(),
        stopCount: currentDayPlaceNames.length,
        placeNames: List<String>.from(currentDayPlaceNames),
      );

      // Mevcut geçmişi yükle
      final historyJson = prefs.getStringList("completed_routes_history") ?? [];
      
      // Yeni rotayı başa ekle
      historyJson.insert(0, completedRoute.toJson());
      
      // Kaydet
      await prefs.setStringList("completed_routes_history", historyJson);

      // 2. İstatistikleri güncelle
      final currentCount = prefs.getInt("completed_routes_count") ?? 0;
      await prefs.setInt("completed_routes_count", currentCount + 1);

      // Rota mesafesini hesapla ve ekle
      final routeDistance = _calculateTotalDistance(activeDayIndex);
      if (routeDistance > 0) {
        await BadgeService().addDistance(routeDistance);
        debugPrint("📍 Rota tamamlandı: $routeDistance km eklendi.");
      }

      // 3. SADECE Tamamlanan Günü Temizle ve State'i Güncelle
      setState(() {
        // İlgili günün planını temizle
        _dayPlans.remove(activeDayIndex);
        _routeOrigins.remove(activeDayIndex.toString());

        // Trip listelerini yeniden oluştur — SADECE Listem (day 0) kaynak
        // Day 1..N planlarından gelen yerler trip_places_'e eklenmemeli
        _tripPlaces.clear();
        _tripPlaceNames.clear();
        
        final myListPlaces = _dayPlans[0] ?? [];
        _tripPlaces.addAll(myListPlaces);
        _tripPlaceNames.addAll(myListPlaces.map((e) => e.name));
      });

      // Yeni durumu kaydet (Diğer günler korunur)
      await _saveTripData();
      
      // Notify updates
      TripUpdateService().notifyTripChanged();
      
    } catch (e) {
      debugPrint("Error saving route history: $e");
    }

    if (!mounted) return;

    // Show success & switch to Explore or stay
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: WanderlustColors.accent),
            const SizedBox(width: 12),
            Text(
              AppLocalizations.instance.isEnglish ? "Route Completed!" : "Rota Tamamlandı!",
              style: const TextStyle(
                color: WanderlustColors.textWhite,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        backgroundColor: WanderlustColors.bgCardLight,
        behavior: SnackBarBehavior.floating,
      ),
    );
  }


  /// Build transit route breakdown display
  Widget _buildTransitStepsInfo() {
    if (_selectedTransportMode != 1) {
      return const SizedBox.shrink();
    }

    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final bool isLocked =
        !PremiumService.instance.isPremium && _isAiPlan && currentDay > 1;

    if (_transitLoading) {
      return const SizedBox.shrink();
    }

    final l10n = AppLocalizations.instance;

    Widget headerRow() {
      return Row(
        children: [
          Icon(Icons.directions_transit, color: accent, size: 18),
          const SizedBox(width: 8),
          Text(
            l10n.isEnglish ? "Route Details" : "Rota Detayları",
            style: const TextStyle(
              color: WanderlustColors.textWhite,
              fontSize: 14,
              fontWeight: FontWeight.w600,
            ),
          ),
          if (isLocked) ...[
            const Spacer(),
            Icon(Icons.lock_outline, color: accent.withOpacity(0.5), size: 14),
          ],
        ],
      );
    }

    if (_transitLegsUnavailable) {
      return Container(
        margin: const EdgeInsets.fromLTRB(20, 8, 20, 0),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.05),
          borderRadius: BorderRadius.circular(22),
          border: Border.all(color: Colors.white.withOpacity(0.08)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            headerRow(),
            const SizedBox(height: 10),
            if (isLocked)
              Padding(
                padding: const EdgeInsets.symmetric(vertical: 8),
                child: Text(
                  l10n.isEnglish
                      ? "Upgrade to Premium to see detailed transit instructions."
                      : "Detaylı ulaşım tarifelerini görmek için Premium'a geç.",
                  style:
                      TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                ),
              )
            else
              Text(
                l10n.t(
                  'Bu güzergâh için toplu taşıma bağlantısı bulunamadı. Tahmini süre genel bir özet olabilir; yürüme veya araç seçeneklerine göz atabilirsin.',
                  'No public transit connection was found for this route. The time shown may be an estimate — try walking or driving for a clearer route.',
                ),
                style: TextStyle(
                  color: WanderlustColors.textGrey,
                  fontSize: 13,
                  height: 1.35,
                ),
              ),
          ],
        ),
      );
    }

    if (_currentRouteSteps.isEmpty) {
      return const SizedBox.shrink();
    }

    // Filter only WALKING and TRANSIT steps (Google bazen farklı casing döner)
    final relevantSteps = _currentRouteSteps.where((step) {
      final mode = (step['travel_mode'] as String? ?? '').toUpperCase();
      return mode == 'WALKING' || mode == 'TRANSIT';
    }).toList();

    if (relevantSteps.isEmpty) return const SizedBox.shrink();

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 8, 20, 0),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(color: Colors.white.withOpacity(0.08)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          headerRow(),
          const SizedBox(height: 10),
          if (isLocked)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 8),
              child: Text(
                AppLocalizations.instance.isEnglish 
                  ? "Upgrade to Premium to see detailed transit instructions." 
                  : "Detaylı ulaşım tarifelerini görmek için Premium'a geç.",
                style: TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
              ),
            )
          else
            Container(
              constraints: BoxConstraints(
                maxHeight: MediaQuery.of(context).size.height * 0.4,
              ),
              child: SingleChildScrollView(
              physics: const BouncingScrollPhysics(),
              child: Column(
                children: () {
                  // Segment bazlı gruplama: A'dan B'ye giden tüm adımları tek bir satırda özetle
                  List<Widget> segmentWidgets = [];
                  
                  // context_from / context_to yalnızca çok duraklı transit birleştirmede enjekte edilir.
                  // İki mekan arasında tek bacakta API ham adımlarında bu alanlar yok — günün ilk/son durağını kullan.
                  String? currentFrom;
                  String? currentTo;
                  List<String> currentVehicles = [];
                  int totalWalkMins = 0;
                  int totalTransitMins = 0;

                  final hasStepContext =
                      relevantSteps.any((s) => s['context_from'] != null);
                  if (!hasStepContext) {
                    final dayPlaces = _dayPlans[currentDay] ?? [];
                    if (dayPlaces.length >= 2) {
                      currentFrom = dayPlaces.first.name;
                      currentTo = dayPlaces.last.name;
                    }
                  }
                  
                  for (final step in relevantSteps) {
                    final from = step['context_from'] as String?;
                    final to = step['context_to'] as String?;
                    
                    // Yeni bir segmente başladık (örneğin A'dan B'ye)
                    if (from != null && to != null) {
                      // Eğer önceki bir segment birikmişse onu UI'a dök
                      if (currentFrom != null && currentTo != null) {
                        segmentWidgets.add(_buildCollapsedSegmentRow(
                          from: currentFrom!,
                          to: currentTo!,
                          vehicles: currentVehicles,
                          walkMins: totalWalkMins,
                          transitMins: totalTransitMins,
                        ));
                      }
                      
                      // Yeni segment için değişkenleri sıfırla/ayarla
                      currentFrom = from;
                      currentTo = to;
                      currentVehicles = [];
                      totalWalkMins = 0;
                      totalTransitMins = 0;
                    }
                    
                    // Mevcut segmentin istatistiklerini topla
                    if (currentFrom != null) {
                      final mode =
                          (step['travel_mode'] as String? ?? 'WALKING').toUpperCase();
                      final durationVal = step['duration_seconds'];
                      final durationSecs = durationVal is num ? durationVal.toDouble() : 0.0;
                      final mins = (durationSecs / 60).round();
                      
                      if (mode == 'WALKING') {
                        totalWalkMins += mins;
                      } else if (mode == 'TRANSIT') {
                        totalTransitMins += mins;
                        final transitDetails = step['transit_details'] as Map<String, dynamic>?;
                        final lineName = transitDetails?['line_name'] as String? ?? '';
                        final vehicleType = transitDetails?['vehicle_type'] as String? ?? '';
                        
                        String trType = "Otobüs";
                        if (vehicleType == 'SUBWAY' || vehicleType == 'METRO') trType = "Metro";
                        else if (vehicleType == 'TRAM') trType = "Tramvay";
                        else if (vehicleType == 'RAIL' || vehicleType == 'TRAIN') trType = "Tren";
                        
                        if (lineName.isNotEmpty) {
                           currentVehicles.add("$trType $lineName");
                        } else {
                           currentVehicles.add(trType);
                        }
                      }
                    }
                  }
                  
                  // Son kalan segmenti de ekle
                  if (currentFrom != null && currentTo != null) {
                    segmentWidgets.add(_buildCollapsedSegmentRow(
                      from: currentFrom!,
                      to: currentTo!,
                      vehicles: currentVehicles,
                      walkMins: totalWalkMins,
                      transitMins: totalTransitMins,
                    ));
                  }
                  
                  return segmentWidgets;
                }(),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCollapsedSegmentRow({
    required String from,
    required String to,
    required List<String> vehicles,
    required int walkMins,
    required int transitMins,
  }) {
    String subtitle = "";
    final isEn = AppLocalizations.instance.isEnglish;
    if (walkMins > 0 && transitMins > 0) {
       subtitle = isEn 
           ? "Walk $walkMins min, take ${vehicles.join(' → ')} ($transitMins min)"
           : "$walkMins dk yürü, ${vehicles.join(' → ')} kullan ($transitMins dk)";
    } else if (transitMins > 0) {
       subtitle = isEn
           ? "Take ${vehicles.join(' → ')} ($transitMins min)"
           : "${vehicles.join(' → ')} kullan ($transitMins dk)";
    } else if (walkMins > 0) {
       subtitle = isEn
           ? "Walk only ($walkMins min)"
           : "Sadece yürü ($walkMins dk)";
    } else {
       subtitle = isEn ? "Arrival" : "Varış";
    }

    // Seçilecek ikon
    IconData icon = Icons.directions_transit;
    Color iconColor = const Color(0xFF2196F3);
    
    if (vehicles.isEmpty && walkMins > 0) {
      icon = Icons.directions_walk;
      iconColor = accent;
    } else if (vehicles.isNotEmpty) {
      if (vehicles.first.contains("Metro")) icon = Icons.subway;
      else if (vehicles.first.contains("Tramvay")) { icon = Icons.tram; iconColor = const Color(0xFF9C27B0); }
      else if (vehicles.first.contains("Tren")) { icon = Icons.train; iconColor = const Color(0xFF607D8B); }
      else { icon = Icons.directions_bus; iconColor = const Color(0xFF4CAF50); }
    }

    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 32,
            height: 32,
            margin: const EdgeInsets.only(top: 2),
            decoration: BoxDecoration(
              color: iconColor.withOpacity(0.2),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Icon(icon, color: iconColor, size: 18),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "$from → $to",
                  style: TextStyle(
                    color: WanderlustColors.textWhite,
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subtitle,
                  style: TextStyle(
                    color: WanderlustColors.textGrey,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          Text(
            "${walkMins + transitMins} dk",
            style: TextStyle(
              color: WanderlustColors.textGrey,
              fontSize: 13,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTransitStepRow(IconData icon, Color color, String title, String duration, {String? subtitle}) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Container(
            width: 28,
            height: 28,
            decoration: BoxDecoration(
              color: color.withOpacity(0.2),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Icon(icon, color: color, size: 16),
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    color: WanderlustColors.textWhite,
                    fontSize: 14,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                if (subtitle != null) ...[
                  const SizedBox(height: 2),
                  Text(
                    subtitle,
                    style: TextStyle(
                      color: WanderlustColors.textGrey,
                      fontSize: 12,
                    ),
                  ),
                ],
              ],
            ),
          ),
          Text(
            duration,
            style: TextStyle(
              color: WanderlustColors.textGrey,
              fontSize: 12,
            ),
          ),
        ],
      ),
    );
  }

  /// API key yoksa custom çizim
  Widget _buildCustomMapFallback(List<Highlight> places) {
    return CustomPaint(
      painter: RouteMapPainter(
        places: places,
        accentColor: accent,
        bgColor: WanderlustColors.bgCardLight,
      ),
      size: const Size(double.infinity, 160),
    );
  }

  /// Harita üzerindeki marker'lar
  List<Widget> _buildMapMarkers(List<Highlight> places) {
    if (places.isEmpty) return [];

    // Koordinatları normalize et
    double minLat = places.map((p) => p.lat).reduce(math.min);
    double maxLat = places.map((p) => p.lat).reduce(math.max);
    double minLng = places.map((p) => p.lng).reduce(math.min);
    double maxLng = places.map((p) => p.lng).reduce(math.max);

    // Padding ekle
    final latPadding = (maxLat - minLat) * 0.15;
    final lngPadding = (maxLng - minLng) * 0.15;
    minLat -= latPadding;
    maxLat += latPadding;
    minLng -= lngPadding;
    maxLng += lngPadding;

    return List.generate(places.length, (index) {
      final place = places[index];
      // Normalize edilmiş pozisyon
      final xRatio = (place.lng - minLng) / (maxLng - minLng);
      final yRatio = 1 - (place.lat - minLat) / (maxLat - minLat); // Y ters

      // Widget pozisyonu (padding ile)
      final xPos = 30 + xRatio * 280; // 30-310 arası
      final yPos = 20 + yRatio * 80; // 20-100 arası

      return Positioned(
        left: xPos,
        top: yPos,
        child: Container(
          width: 26,
          height: 26,
          decoration: BoxDecoration(
            color: accent,
            shape: BoxShape.circle,
            border: Border.all(color: Colors.white, width: 2),
            boxShadow: [
              BoxShadow(
                color: accent.withOpacity(0.5),
                blurRadius: 8,
                offset: const Offset(0, 2),
              ),
            ],
          ),
          child: Center(
            child: Text(
              "${index + 1}",
              style: const TextStyle(
                color: Colors.white,
                fontSize: 11,
                fontWeight: FontWeight.w700,
              ),
            ),
          ),
        ),
      );
    });
  }



  Widget _buildDayTabs() {
    return Container(
      margin: const EdgeInsets.only(top: 16),
      height: 44,
      child: TabBar(
        controller: _dayTabController,
        isScrollable: true,
        padding: const EdgeInsets.symmetric(horizontal: 16),
        labelPadding: const EdgeInsets.symmetric(horizontal: 6),
        indicator: BoxDecoration(
          color: accent,
          borderRadius: BorderRadius.circular(12),
        ),
        indicatorSize: TabBarIndicatorSize.tab,
        dividerColor: Colors.transparent,
        labelColor: Colors.white,
        unselectedLabelColor: WanderlustColors.textWhite,
        labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
        unselectedLabelStyle: const TextStyle(
          fontWeight: FontWeight.w500,
          fontSize: 14,
        ),
        onTap: (_) => setState(() {}),
        tabs: List.generate(_totalDays, (index) {
          final dayNum = index + 1;
          final count = _dayPlans[dayNum]?.length ?? 0;
          return Tab(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 14),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(AppLocalizations.instance.isEnglish ? "Day $dayNum" : "$dayNum. Gün"),
                  if (count > 0) ...[
                    const SizedBox(width: 6),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 6,
                        vertical: 2,
                      ),
                      decoration: BoxDecoration(
                        // Seçili sekmeyse şeffaf beyaz, değilse hafif mor arka plan
                        color: _dayTabController?.index == index 
                            ? Colors.white.withOpacity(0.2) 
                            : accent.withOpacity(0.12),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        "$count",
                        style: TextStyle(
                          fontSize: 10, 
                          color: _dayTabController?.index == index 
                              ? Colors.white 
                              : accent,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                  ],
                ],
              ),
            ),
          );
        }),
      ),
    );
  }

  Widget _buildDayContent(int day) {
    final places = _dayPlans[day] ?? [];
    final schedule = _calculateScheduleForDay(places, _selectedTransportMode, day);

    if (places.isEmpty) {
      return SingleChildScrollView(
        physics: const AlwaysScrollableScrollPhysics(),
        child: Center(
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 60),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.wb_sunny_outlined,
                  size: 48,
                  color: WanderlustColors.textGrey.withOpacity(0.5),
                ),
                const SizedBox(height: 16),
                Text(
                  day == 0 
                      ? (AppLocalizations.instance.isEnglish ? "Your bucket list is empty" : "Şehir listeniz henüz boş")
                      : AppLocalizations.instance.dayEmpty(day),
                  style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 16),
                ),
                const SizedBox(height: 8),
                Text(
                  day == 0 
                      ? (AppLocalizations.instance.isEnglish ? "Add places from the Discover tab" : "Keşfet ekleyerek buraları doldurabilirsin")
                      : AppLocalizations.instance.startAddingPlaces,
                  style: TextStyle(color: WanderlustColors.textGrey.withOpacity(0.7), fontSize: 13),
                ),
                if (day >= 1) ...[
                   const SizedBox(height: 32),
                   OutlinedButton.icon(
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                        backgroundColor: Colors.white,
                        foregroundColor: accent,
                        surfaceTintColor: Colors.transparent,
                        side: BorderSide(color: accent.withOpacity(0.3)),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                      onPressed: _generateAiPlanForExistingUser,
                      icon: Image.asset(
                        'assets/icons/icon_gunluk.png',
                        width: 22,
                        height: 22,
                        fit: BoxFit.contain,
                      ),
                      label: Text(
                        AppLocalizations.instance.buildSmartItinerary,
                        style: TextStyle(color: accent, fontWeight: FontWeight.w600),
                      ),
                   ),
                ],
              ],
            ),
          ),
        ),
      );
    }

    final bool isLocked = !PremiumService.instance.isPremium && _isAiPlan && day > 1;
    
    Widget listView;
    if (isLocked) {
      // Locked teaser: shrinkWrap = içerik kadar yükseklik; alt boşluk Stack + SliverFillRemaining ile doldurulur
      listView = ListView.builder(
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 20),
        itemCount: places.length, 
        itemBuilder: (context, index) {
          final place = places[index];
          final timeText = index < schedule.length ? schedule[index] : "";
          return _buildMyRouteCard(
            day: day,
            key: ValueKey("day_${day}_${place.name}_${index}"),
            place: place,
            index: index,
            timeText: timeText,
            isLast: index == places.length - 1,
          );
        },
      );
    } else {
      // Unlocked: Regular Reorderable ListView
      listView = ReorderableListView.builder(
        buildDefaultDragHandles: false,
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 80),
        itemCount: places.length,
        onReorder: (oldIndex, newIndex) => _reorderPlace(day, oldIndex, newIndex),
        proxyDecorator: (child, index, animation) {
          return AnimatedBuilder(
            animation: animation,
            builder: (context, child) {
              final scale = Tween<double>(begin: 1, end: 1.03).animate(animation);
              return Transform.scale(scale: scale.value, child: child);
            },
            child: child,
          );
        },
        itemBuilder: (context, index) {
          final place = places[index];
          final timeText = index < schedule.length ? schedule[index] : "";
          return _buildMyRouteCard(
            day: day,
            key: ValueKey("day_${day}_${place.name}_${index}"),
            place: place,
            index: index,
            timeText: timeText,
            isLast: index == places.length - 1,
          );
        },
      );
    }

    if (isLocked) {
      listView = Stack(
        fit: StackFit.expand,
        children: [
          IgnorePointer(
            child: ImageFiltered(
              imageFilter: ui.ImageFilter.blur(sigmaX: 3.0, sigmaY: 3.0),
              child: listView,
            ),
          ),
          // Aynı ton: hazır rota detayı — hafif buzlu cam + koyu gri metin
          Positioned.fill(
            child: ClipRect(
              child: BackdropFilter(
                filter: ui.ImageFilter.blur(sigmaX: 5, sigmaY: 5),
                child: Container(
                  color: Colors.white.withOpacity(0.15),
                ),
              ),
            ),
          ),
          // Üst kenar: birleşik aksiyon butonları (bgCard) ile blur alanı arasındaki keskin geçişi yumuşatır
          Positioned(
            top: 0,
            left: 0,
            right: 0,
            height: 88,
            child: IgnorePointer(
              child: DecoratedBox(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      WanderlustColors.bgCard,
                      WanderlustColors.bgCard.withOpacity(0.55),
                      WanderlustColors.bgCard.withOpacity(0),
                    ],
                    stops: const [0.0, 0.5, 1.0],
                  ),
                ),
              ),
            ),
          ),
          // Paywall: üstte az yer kalınca (harita + butonlar açık) Center+Column ~89px'ta taşar.
          // Dikey scroll + minHeight ile hem ortalanır hem taşma olmaz.
          Positioned.fill(
            child: LayoutBuilder(
              builder: (context, constraints) {
                final h = constraints.maxHeight;
                final paywallColumn = Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(Icons.lock_rounded, color: Colors.black.withOpacity(0.7), size: 48),
                    const SizedBox(height: 16),
                    Text(
                      AppLocalizations.instance.isEnglish ? "Plan Locked" : "Plan Kilitli",
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
                      AppLocalizations.instance.isEnglish
                          ? "Unlock your full personalized itinerary and smart recommendations."
                          : "Kişiselleştirilmiş rotanıza ve akıllı önerilere sınırsız erişin.",
                      style: TextStyle(
                        color: WanderlustColors.textGrey,
                        fontSize: 14,
                        height: 1.5,
                        fontWeight: FontWeight.w500,
                      ),
                      textAlign: TextAlign.center,
                    ),
                    const SizedBox(height: 20),
                    GestureDetector(
                      onTap: () {
                        showPaywall(
                          context,
                          onSubscribe: (planId) async {
                            setState(() {});
                          },
                        );
                      },
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 14),
                        decoration: BoxDecoration(
                          color: WanderlustColors.accent,
                          borderRadius: BorderRadius.circular(32),
                        ),
                        child: Text(
                          AppLocalizations.instance.isEnglish ? "Try PRO" : "PRO'yu Dene",
                          style: const TextStyle(
                            fontWeight: FontWeight.w700,
                            fontSize: 16,
                            color: Colors.white,
                          ),
                        ),
                      ),
                    ),
                  ],
                );

                return SingleChildScrollView(
                  physics: const ClampingScrollPhysics(),
                  padding: const EdgeInsets.symmetric(horizontal: 48, vertical: 16),
                  child: h.isFinite && h > 0
                      ? ConstrainedBox(
                          constraints: BoxConstraints(minHeight: h),
                          child: paywallColumn,
                        )
                      : paywallColumn,
                );
              },
            ),
          ),
        ],
      );
    }

    final mainStack = Stack(
      fit: isLocked && places.isNotEmpty ? StackFit.expand : StackFit.loose,
      children: [
        listView,
        if (places.isNotEmpty && !isLocked) ...[
          // Optimize Et button (right side)
          Positioned(
            right: 20,
            bottom: 16,
            child: GestureDetector(
              onTap: _optimizeRoute,
              child: ClipRRect(
                borderRadius: BorderRadius.circular(18),
                child: BackdropFilter(
                  filter: ui.ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.5),
                      borderRadius: BorderRadius.circular(18),
                      border: Border.all(color: Colors.white.withOpacity(0.2)),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.05),
                          blurRadius: 10,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Text(
                      AppLocalizations.instance.optimize,
                      style: const TextStyle(
                        color: Colors.black,
                        fontSize: 13,
                        fontWeight: FontWeight.w700,
                        letterSpacing: 0.3,
                      ),
                    ),
                  ),
                ),
              ),
            ),
          ),
          // Clear All button (left side)
          Positioned(
            left: 20,
            bottom: 16,
            child: GestureDetector(
              onTap: () => _clearDayPlaces(day),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(18),
                child: BackdropFilter(
                  filter: ui.ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.5),
                      borderRadius: BorderRadius.circular(18),
                      border: Border.all(color: Colors.white.withOpacity(0.2)),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.05),
                          blurRadius: 10,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.delete_outline_rounded, color: Colors.black.withOpacity(0.7), size: 18),
                        const SizedBox(width: 8),
                        Text(
                          AppLocalizations.instance.clear,
                          style: const TextStyle(
                            color: Colors.black,
                            fontSize: 13,
                            fontWeight: FontWeight.w700,
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
      ],
    );

    // Kilitli + az durak: gövdeyi en az TabBarView yüksekliği kadar tut (alt boş şerit).
    // CustomScrollView kullanma — NestedScrollView ile ikincil scroll çakışması null/assert hatalarına yol açıyor.
    if (isLocked && places.isNotEmpty) {
      return LayoutBuilder(
        builder: (context, constraints) {
          final h = constraints.maxHeight;
          if (!h.isFinite || h <= 0) return mainStack;
          return ConstrainedBox(
            constraints: BoxConstraints(minHeight: h),
            child: mainStack,
          );
        },
      );
    }

    return mainStack;
  }

  Widget _buildMyRouteCard({
    required int day,
    required Key key,
    required Highlight place,
    required int index,
    required bool isLast,
    required String timeText,
  }) {
    return Container(
      key: key,
      margin: const EdgeInsets.only(bottom: 4),
      child: Stack(
        children: [
          _buildHorizontalPlaceCard(day, place, index, timeText: timeText, isLast: isLast),
          
          // Drag Handle (Sağ taraf) - Yalnızca Gün planlarında
          if (day > 0)
          Positioned(
            right: 0,
            top: 0,
            bottom: 0,
            child: Center(
              child: ReorderableDragStartListener(
                index: index,
                child: Container(
                  width: 40,
                  height: 60,
                  color: Colors.transparent,
                  child: const Icon(
                    Icons.drag_indicator,
                    color: WanderlustColors.textGrey,
                    size: 20,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  /// Yeni yatay kart tasarımı (Profil ekranındaki favoriler gibi)
  Widget _buildHorizontalPlaceCard(int day, Highlight place, int index, {String? timeText, bool isReadOnly = false, bool isLast = false}) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);
    final letter = String.fromCharCode(65 + index); // A, B, C...
    final bool isMyList = day == 0;

    String actualTimeText = timeText ?? "";
    if (actualTimeText.isEmpty && day > 0) {
       actualTimeText = "${9 + index}:30";
    }

    // Compact dimensions for My List
    final double imageSize = isMyList ? 36 : 48;
    final double cardPadding = isMyList ? 8 : 10;
    final double titleFontSize = isMyList ? 14 : 16;
    final double timelineSideWidth = isMyList ? 28 : 40;

    return IntrinsicHeight(
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Timeline Sol Sütun
          SizedBox(
            width: timelineSideWidth,
            child: Stack(
              alignment: Alignment.topCenter,
              clipBehavior: Clip.none,
              children: [
                if (!isLast && day > 0)
                  Positioned(
                    top: 36, // Pin'in ortasından başlar
                    bottom: -32, // Bir sonraki pin'in arkasına kadar uzanır
                    child: Container(
                      width: 3,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            accent.withOpacity(0.8),
                            accent.withOpacity(0.1),
                          ],
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                        ),
                        borderRadius: BorderRadius.circular(2),
                      ),
                    ),
                  ),
                Center(
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 4), // Kartın bottom margin'ine (4) uyum sağlaması için
                    child: Container(
                      width: day == 0 ? 10 : 32,
                      height: day == 0 ? 10 : 32,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            accent.withOpacity(0.8),
                            accent,
                          ],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        shape: BoxShape.circle,
                        boxShadow: [
                          if (day > 0)
                            BoxShadow(
                              color: accent.withOpacity(0.4),
                              blurRadius: 8,
                              offset: const Offset(0, 3),
                            ),
                        ],
                        border: Border.all(color: Colors.white, width: day == 0 ? 0 : 2),
                      ),
                      child: Center(
                        child: day == 0 ? const SizedBox() : Text(
                          letter,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 14,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          SizedBox(width: isMyList ? 8 : 12),
          
          Expanded(
            child: GestureDetector(
               onTap: () {
                 // --- ANALYTICS: Landmark Selection ---
                 AnalyticsService.instance.logSelectContent(
                   contentType: 'landmark_in_route',
                   itemId: place.name,
                 );
                 // Fotoğrafı prefetch et
                 ImagePrefetchService.prefetchSinglePhoto(context, place.imageUrl, heroDecode: true);
                 Navigator.push(context, MaterialPageRoute(builder: (_) => DetailScreen(place: place)));
               },
               child: Container(
                 padding: EdgeInsets.all(cardPadding),
                 margin: const EdgeInsets.only(bottom: 4), 
                 decoration: BoxDecoration(
                   color: WanderlustColors.bgCard,
                   borderRadius: BorderRadius.circular(16),
                 ),
                 child: Row(
                   children: [
                     if (hasImage) 
                       Padding(
                         padding: EdgeInsets.only(right: isMyList ? 8 : 12),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(isMyList ? 6 : 8),
                          child: ResilientNetworkImage(
                            imageUrl: place.imageUrl,
                            placeName: place.name,
                            city: place.city ?? _city?.city ?? '',
                            category: place.category,
                            blurHash: place.blurHash,
                            width: imageSize,
                            height: imageSize,
                            fit: BoxFit.cover,
                            placeholderBuilder: (_) => Container(
                              width: imageSize,
                              height: imageSize,
                              color: WanderlustColors.bgCardLight,
                              child: Icon(Icons.image_not_supported, size: isMyList ? 16 : 20, color: Colors.white.withOpacity(0.5)),
                            ),
                          ),
                        ),
                       ),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                             if (actualTimeText.isNotEmpty)
                               Padding(
                                 padding: const EdgeInsets.only(bottom: 2),
                                 child: Row(
                                   children: [
                                     const Icon(Icons.access_time, size: 12, color: WanderlustColors.accent),
                                     const SizedBox(width: 4),
                                     Text(actualTimeText, style: const TextStyle(color: WanderlustColors.accent, fontSize: 12, fontWeight: FontWeight.bold)),
                                   ],
                                 ),
                               ),
                             Text(place.getLocalizedName(AppLocalizations.instance.isEnglish), maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(fontWeight: FontWeight.bold, fontSize: titleFontSize, color: WanderlustColors.textWhite)),
                             const SizedBox(height: 2),
                             Text("${AppLocalizations.instance.translateCategory(place.category.trim())} • ${place.getLocalizedArea(AppLocalizations.instance.isEnglish)}", maxLines: 1, overflow: TextOverflow.ellipsis, style: TextStyle(color: Colors.grey, fontSize: isMyList ? 11 : 12)),
                             
                             // Listem sekmesinde, bu mekanın hangi günlere atandığını göster (inline, kompakt)
                             if (day == 0)
                               Builder(
                                 builder: (context) {
                                   List<int> assignedDays = [];
                                   for (int i = 1; i <= _totalDays; i++) {
                                     if (_dayPlans[i]?.any((p) => p.name == place.name) == true) {
                                       assignedDays.add(i);
                                     }
                                   }
                                   if (assignedDays.isEmpty) return const SizedBox.shrink();
                                   
                                   final dayLabel = assignedDays.map((d) => AppLocalizations.instance.isEnglish ? "D$d" : "$d.G").join(', ');
                                   return Text(dayLabel, style: TextStyle(color: accent.withOpacity(0.6), fontSize: 10, fontWeight: FontWeight.w600));
                                 }
                               ),
                          ],
                        ),
                      ),
                      
                      // Güne ata butonu (Sadece Listem sekmesinde)
                      if (!isReadOnly && isMyList)
                        Material(
                           color: Colors.transparent,
                           child: InkWell(
                             onTap: () => _assignPlaceToDayFromListem(place.name),
                             borderRadius: BorderRadius.circular(20),
                             child: Padding(
                               padding: const EdgeInsets.all(4),
                               child: Icon(Icons.calendar_month_outlined, color: Colors.white.withOpacity(0.35), size: 16),
                             ),
                           ),
                        ),
                       
                      // Delete button (Sadece düzenlenebilir modda)
                      if (!isReadOnly)
                        Padding(
                          padding: const EdgeInsets.only(left: 2),
                          child: Material(
                             color: Colors.transparent,
                             child: InkWell(
                               onTap: () => _removeFromDay(day, place.name),
                               borderRadius: BorderRadius.circular(20),
                               child: Padding(
                                 padding: const EdgeInsets.all(4),
                                 child: Icon(Icons.close, color: WanderlustColors.textGrey.withOpacity(0.8), size: 16),
                               ),
                             ),
                          ),
                        ),
                        
                      // ReadOnly ise ok
                      if (isReadOnly)
                        const Icon(Icons.chevron_right, color: WanderlustColors.textGrey, size: 20),
                        
                      // Drag Handle için boşluk (Eğer düzenlenebilir ise ve gün 1+ ise drag handle dışarıda)
                      if (!isReadOnly && day > 0)
                         const SizedBox(width: 24),
                   ],
                 ),
               ),
            ),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SUGGESTED ROUTES TAB
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSuggestedRoutesTab() {
    return Stack(
      children: [
        Column(
          children: [
            Expanded(
              child: ListView.builder(
                controller: _suggestionsScrollController,
                padding: const EdgeInsets.fromLTRB(20, 8, 20, 80),
                itemCount: _filteredSuggestedRoutes.length,
                itemBuilder: (context, index) =>
                    _buildSuggestedRouteCard(_filteredSuggestedRoutes[index], isFirstCard: index == 0),
              ),
            ),
          ],
        ),
        if (_showSuggestionsScrollToTop)
          Positioned(
            right: 20,
            bottom: 30,
            child: AnimatedOpacity(
              opacity: _showSuggestionsScrollToTop ? 1.0 : 0.0,
              duration: const Duration(milliseconds: 200),
              child: GestureDetector(
                onTap: () {
                  HapticFeedback.lightImpact();
                  _suggestionsScrollController.animateTo(
                    0,
                    duration: const Duration(milliseconds: 500),
                    curve: Curves.easeOutCubic,
                  );
                },
                child: Container(
                  width: 44,
                  height: 44,
                  decoration: BoxDecoration(
                    color: WanderlustColors.bgCard.withOpacity(0.8),
                    shape: BoxShape.circle,
                    border: Border.all(color: WanderlustColors.border.withOpacity(0.5)),
                  ),
                  child: const Icon(
                    Icons.keyboard_arrow_up_rounded,
                    color: WanderlustColors.textGrey,
                    size: 28,
                  ),
                ),
              ),
            ),
          ),
      ],
    );
  }

  Widget _buildRouteFilters({Key? key}) {
    final List<Map<String, dynamic>> tabs = [
      {"label": AppLocalizations.instance.tabAll, "icon": Icons.grid_view_rounded},
      {"label": AppLocalizations.instance.tabForYou, "icon": Icons.recommend_outlined},
      {"label": AppLocalizations.instance.tabPopular, "icon": Icons.trending_up},
    ];
    return Container(
      key: key,
      height: 44,
      margin: const EdgeInsets.only(top: 16),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: tabs.asMap().entries.map((entry) {
          final index = entry.key;
          final filter = entry.value;
          final isSelected = _selectedRouteFilter == index;
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 5),
            child: GestureDetector(
              onTap: () => _filterRoutes(index),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 16),
                decoration: BoxDecoration(
                  color: isSelected ? accent : WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Row(
                  children: [
                    Icon(
                      filter["icon"] as IconData,
                      size: 18,
                      color: isSelected ? Colors.white : WanderlustColors.textGrey,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      filter["label"] as String,
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w600,
                        color: isSelected ? Colors.white : WanderlustColors.textGrey,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        }).toList(),
      ),
    );
  }

  Widget _buildSuggestedRouteCard(SuggestedRoute route, {Key? key, bool isFirstCard = false}) {
    // 🔥 placeNames artık CuratedRoutesService.generateRoutes'da validate ediliyor.
    // Yine de güvence için: sadece city.highlights'ta gerçekten var olan mekanları say.
    int actualStopCount = route.placeNames.length;
    if (_city != null) {
      int foundCount = 0;
      final seen = <String>{};
      for (var name in route.placeNames) {
        final normalizedTarget = name.toLowerCase().trim();
        final found = _city!.highlights.any((h) =>
          h.name.toLowerCase().trim() == normalizedTarget ||
          (h.nameEn?.toLowerCase().trim() == normalizedTarget) ||
          (h.id != null && h.id == name)
        );
        if (found && !seen.contains(normalizedTarget)) {
          seen.add(normalizedTarget);
          foundCount++;
        }
      }
      actualStopCount = foundCount;
    }

    return GestureDetector(
      key: key,
      onTap: () {
        // --- ANALYTICS: Suggested Route Selection ---
        AnalyticsService.instance.logSelectContent(
          contentType: 'suggested_route',
          itemId: route.name,
        );
        _showRouteDetail(route);
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        decoration: BoxDecoration(
          color: WanderlustColors.bgCard,
          borderRadius: BorderRadius.circular(20),
        ),
        child: Stack(
          children: [
            Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Stack(
              children: [
                ClipRRect(
                  borderRadius: const BorderRadius.vertical(
                    top: Radius.circular(20),
                  ),
                  child: SizedBox(
                    height: 140,
                    width: double.infinity,
                    child: ResilientNetworkImage(
                      imageUrl: route.imageUrl,
                      placeName: route.name,
                      city: _city?.city ?? '',
                      category: 'route',
                      fit: BoxFit.cover,
                      placeholderBuilder: (_) => Container(
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [
                              WanderlustColors.bgCardLight,
                              WanderlustColors.bgCard,
                            ],
                          ),
                        ),
                        child: Icon(
                          route.icon,
                          size: 48,
                          color: Colors.white.withOpacity(0.5),
                        ),
                      ),
                    ),
                  ),
                ),
                Container(
                  height: 140,
                  decoration: BoxDecoration(
                    borderRadius: const BorderRadius.vertical(
                      top: Radius.circular(20),
                    ),
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        Colors.transparent,
                        Colors.black.withOpacity(0.7),
                      ],
                    ),
                  ),
                ),
                Positioned(
                  top: 12,
                  left: 12,
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(12),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: Container(
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          color: Colors.white.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: Colors.white.withOpacity(0.2)),
                        ),
                        child: Icon(route.icon, color: Colors.white, size: 20),
                      ),
                    ),
                  ),
                ),
                Positioned(
                  top: 12,
                  right: 12,
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
                          color: Colors.black.withOpacity(0.3),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: Colors.white.withOpacity(0.1)),
                        ),
                        child: Text(
                          _getLocalizedDifficulty(route.difficulty),
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
                Positioned(
                  bottom: 12,
                  left: 12,
                  child: Row(
                    children: [
                      _buildStatChip(Icons.schedule, route.duration),
                      const SizedBox(width: 8),
                      _buildStatChip(Icons.straighten, route.distance),
                      const SizedBox(width: 8),
                      _buildStatChip(
                        Icons.place,
                        AppLocalizations.instance.nStops(actualStopCount),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    route.name,
                    style: const TextStyle(
                      color: WanderlustColors.textWhite,
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    route.description,
                    style: const TextStyle(
                      color: WanderlustColors.textGrey,
                      fontSize: 13,
                      height: 1.4,
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 12),
                  Wrap(
                    spacing: 8,
                    children: route.tags
                        .map(
                          (tag) => Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 10,
                              vertical: 5,
                            ),
                            decoration: BoxDecoration(
                              color: WanderlustColors.bgCardLight,
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: WanderlustColors.border.withOpacity(0.3)),
                            ),
                            child: Text(
                              tag,
                              style: const TextStyle(
                                color: WanderlustColors.textGrey,
                                fontSize: 11,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                        )
                        .toList(),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    children: [
                      Expanded(
                        child: GestureDetector(
                          onTap: () => _showRouteDetail(route),
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 12),
                            decoration: BoxDecoration(
                              color: WanderlustColors.bgCardLight,
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(
                                  Icons.visibility,
                                  color: WanderlustColors.textGrey,
                                  size: 18,
                                ),
                                SizedBox(width: 8),
                                Text(
                                  AppLocalizations.instance.details,
                                  style: TextStyle(
                                    color: WanderlustColors.textGrey,
                                    fontSize: 13,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: Builder(
                          builder: (context) {
                            // Check if active (all places in trip)
                            // Isimler farkli dilde olabilir, bu yuzden highlight uzerinden kontrol ediyoruz
                            final bool isApplied = route.placeNames.every((routeName) {
                              if (_city == null) return false;
                              try {
                                final place = _city!.highlights.firstWhere(
                                  (h) => h.name == routeName || h.nameEn == routeName,
                                );
                                return _tripPlaceNames.contains(place.name);
                              } catch (_) {
                                return false;
                              }
                            });
                            
                            // Kullanıcının istediği sarı renk (WanderlustColors.accent)
                            const activeColor = WanderlustColors.accent; 

                            if (isApplied) {
                              // Non-clickable when applied
                              return Container(
                                padding: const EdgeInsets.symmetric(vertical: 11),
                                decoration: BoxDecoration(
                                  color: activeColor,
                                  borderRadius: BorderRadius.circular(12),
                                  border: Border.all(
                                    color: activeColor,
                                    width: 1.5,
                                  ),
                                ),
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Icon(
                                      Icons.check, // Checkmark icon
                                      color: Colors.white,
                                      size: 18,
                                    ),
                                    const SizedBox(width: 8),
                                    Text(
                                      AppLocalizations.instance.onRoute, // "Rotada"
                                      style: TextStyle(
                                        color: Colors.white,
                                        fontSize: 13,
                                        fontWeight: FontWeight.w700,
                                      ),
                                    ),
                                  ],
                                ),
                              );
                            }

                            return GestureDetector(
                              key: isFirstCard ? _createRouteButtonKey : null,
                              onTap: () => _applySuggestedRoute(route),
                              child: Container(
                                padding: const EdgeInsets.symmetric(vertical: 12),
                                decoration: BoxDecoration(
                                  color: WanderlustColors.bgCardLight,
                                  borderRadius: BorderRadius.circular(12),
                                ),
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Icon(
                                      Icons.add,
                                      color: WanderlustColors.textGrey,
                                      size: 18,
                                    ),
                                    SizedBox(width: 8),
                                    Text(
                                      AppLocalizations.instance.applyRoute, // "Uygula"
                                      style: TextStyle(
                                        color: WanderlustColors.textGrey,
                                        fontSize: 13,
                                        fontWeight: FontWeight.w600,
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            );
                          }
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
          ],
        ),
      ),
    );
  }

  String _getLocalizedDifficulty(String difficulty) {
    final d = difficulty.toLowerCase().trim();
    if (d.contains('easy') || d.contains('kolay')) {
      return AppLocalizations.instance.difficultyEasy;
    } else if (d.contains('medium') || d.contains('orta')) {
      return AppLocalizations.instance.difficultyMedium;
    } else if (d.contains('hard') || d.contains('zor') || d.contains('difficult')) {
      return AppLocalizations.instance.difficultyHard;
    }
    return difficulty;
  }

  Widget _buildStatChip(IconData icon, String text) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: Colors.black.withOpacity(0.5),
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, color: Colors.white, size: 12),
          const SizedBox(width: 4),
          Text(
            text,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 11,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // ROUTE DETAIL MODAL
  // ══════════════════════════════════════════════════════════════════════════

  void _showRouteDetail(SuggestedRoute route) {
    // Paywall trigger moved to inside the detail sheet as a visual teaser

    // Track this route view (increments usage only for new routes)
    PremiumService.instance.trackRouteView(route.id);

    final places = <Highlight>[];
    for (var name in route.placeNames) {
      final normalizedTarget = name.toLowerCase().trim();
      
      // Strategy 0: Place ID match
      var place = _city?.highlights
          .where((h) => h.id != null && h.id == name)
          .firstOrNull;

      // Strategy 1: Exact Match
      place ??= _city?.highlights
          .where((h) => h.name == name || h.nameEn == name)
          .firstOrNull;
          
      // Strategy 2: Case Insensitive
      place ??= _city?.highlights
          .where((h) => 
              h.name.toLowerCase().trim() == normalizedTarget || 
              (h.nameEn?.toLowerCase().trim() == normalizedTarget))
          .firstOrNull;

      // Strategy 3: Fuzzy / Substring
      place ??= _city?.highlights
          .where((h) => 
              h.name.toLowerCase().contains(normalizedTarget) || 
              normalizedTarget.contains(h.name.toLowerCase()))
          .firstOrNull;

      if (place != null) {
        // Avoid duplicates
        if (!places.any((p) => p.name == place!.name)) {
          places.add(place);
        }
      } else {
        debugPrint("⚠️ Route stop NOT FOUND: $name");
      }
    }

    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) {
          // İlk rota her zaman ücretsiz (Pro olmadan)
          final bool isFirstRoute = _allSuggestedRoutes.isNotEmpty && _allSuggestedRoutes.first.id == route.id;
          final bool isLocked = !PremiumService.instance.isPremium && !isFirstRoute;
          final media = MediaQuery.of(context);
          final maxSheetH = media.size.height * 0.92;

          return Padding(
            padding: EdgeInsets.only(
              top: media.padding.top + 8,
              bottom: media.viewInsets.bottom,
            ),
            child: Align(
              alignment: Alignment.bottomCenter,
              child: Container(
                constraints: BoxConstraints(maxHeight: maxSheetH),
                decoration: const BoxDecoration(
                  color: WanderlustColors.bgDark,
                  borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
                ),
                child: ClipRRect(
                  borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
                  child: SafeArea(
                    top: false,
                    child: SingleChildScrollView(
                      physics: const ClampingScrollPhysics(),
                      child: Column(
                        mainAxisSize: MainAxisSize.min,
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          Center(
                            child: Container(
                              margin: const EdgeInsets.only(top: 12),
                              width: 40,
                              height: 4,
                              decoration: BoxDecoration(
                                color: WanderlustColors.border,
                                borderRadius: BorderRadius.circular(2),
                              ),
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.all(20),
                            child: Row(
                              children: [
                                Container(
                                  padding: const EdgeInsets.all(12),
                                  decoration: BoxDecoration(
                                    color: WanderlustColors.accent,
                                    borderRadius: BorderRadius.circular(14),
                                  ),
                                  child: Icon(route.icon, color: Colors.white, size: 24),
                                ),
                                const SizedBox(width: 14),
                                Expanded(
                                  child: Column(
                                    crossAxisAlignment: CrossAxisAlignment.start,
                                    children: [
                                      Text(
                                        route.name,
                                        style: const TextStyle(
                                          color: WanderlustColors.textWhite,
                                          fontSize: 20,
                                          fontWeight: FontWeight.w700,
                                        ),
                                      ),
                                      const SizedBox(height: 4),
                                      Row(
                                        children: [
                                          const Icon(
                                            Icons.schedule,
                                            color: WanderlustColors.textGrey,
                                            size: 14,
                                          ),
                                          const SizedBox(width: 4),
                                          Text(
                                            route.duration,
                                            style: const TextStyle(
                                              color: WanderlustColors.textGrey,
                                              fontSize: 13,
                                            ),
                                          ),
                                          const SizedBox(width: 12),
                                          const Icon(
                                            Icons.straighten,
                                            color: WanderlustColors.textGrey,
                                            size: 14,
                                          ),
                                          const SizedBox(width: 4),
                                          Text(
                                            route.distance,
                                            style: const TextStyle(
                                              color: WanderlustColors.textGrey,
                                              fontSize: 13,
                                            ),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),
                                GestureDetector(
                                  onTap: () => Navigator.pop(context),
                                  child: Container(
                                    padding: const EdgeInsets.all(8),
                                    decoration: const BoxDecoration(
                                      color: WanderlustColors.bgCard,
                                      shape: BoxShape.circle,
                                    ),
                                    child: const Icon(
                                      Icons.close,
                                      color: WanderlustColors.textGrey,
                                      size: 20,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 20),
                            child: Text(
                              route.description,
                              style: const TextStyle(
                                color: WanderlustColors.textGrey,
                                fontSize: 14,
                                height: 1.5,
                              ),
                            ),
                          ),
                          const SizedBox(height: 16),
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 20),
                            child: Row(
                              children: [
                                Text(
                                  AppLocalizations.instance.stops,
                                  style: const TextStyle(
                                    color: WanderlustColors.textWhite,
                                    fontSize: 16,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                                const Spacer(),
                                Text(
                                  "${places.length} ${AppLocalizations.instance.spots.toLowerCase()}",
                                  style: const TextStyle(color: WanderlustColors.textGrey, fontSize: 13),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(height: 10),
                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 20),
                            child: Stack(
                              clipBehavior: Clip.hardEdge,
                              children: [
                                Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    for (int index = 0; index < places.length; index++)
                                      _buildStopCard(
                                        places[index],
                                        index,
                                        places.length,
                                        route.accentColor,
                                      ),
                                  ],
                                ),
                                if (isLocked)
                                  Positioned.fill(
                                    child: ClipRect(
                                      child: BackdropFilter(
                                        filter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
                                        child: Container(
                                          color: Colors.white.withOpacity(0.15),
                                          alignment: Alignment.center,
                                          child: Padding(
                                            padding: const EdgeInsets.symmetric(horizontal: 40),
                                            child: Column(
                                              mainAxisSize: MainAxisSize.min,
                                              children: [
                                                Icon(Icons.lock_rounded, color: Colors.black.withOpacity(0.7), size: 48),
                                                const SizedBox(height: 16),
                                                Text(
                                                  AppLocalizations.instance.isEnglish ? "Unlock to see all stops" : "Tüm durakları görmek için kilidi açın",
                                                  textAlign: TextAlign.center,
                                                  style: TextStyle(
                                                    color: Colors.black.withOpacity(0.85),
                                                    fontSize: 18,
                                                    fontWeight: FontWeight.bold,
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
                          ),
                          Container(
                            color: WanderlustColors.bgCard,
                            padding: const EdgeInsets.fromLTRB(20, 16, 20, 40), // Daha aşağıda olması için alt boşluk eklendi
                            child: Builder(
                              builder: (context) {
                                if (isLocked) {
                                  return GestureDetector(
                                    onTap: () {
                                      Navigator.pop(context); // close sheet
                                      _showPaywall();
                                    },
                                    child: Container(
                                      width: double.infinity,
                                      padding: const EdgeInsets.symmetric(vertical: 16),
                                      decoration: BoxDecoration(
                                        color: WanderlustColors.accent,
                                        borderRadius: BorderRadius.circular(32),
                                      ),
                                      child: Text(
                                        AppLocalizations.instance.isEnglish ? "Start your route with PRO" : "PRO ile hemen rotanı başlat",
                                        textAlign: TextAlign.center,
                                        style: const TextStyle(
                                          color: Colors.white,
                                          fontSize: 16,
                                          fontWeight: FontWeight.w800,
                                        ),
                                      ),
                                    ),
                                  );
                                }

                                // Check if route is already applied
                                final bool isApplied = route.placeNames.every((routeName) {
                                  if (_city == null) return false;
                                  try {
                                    final place = _city!.highlights.firstWhere(
                                      (h) => h.name == routeName || h.nameEn == routeName,
                                    );
                                    return _tripPlaceNames.contains(place.name);
                                  } catch (_) {
                                    return false;
                                  }
                                });

                                const activeColor = WanderlustColors.accent;

                                if (isApplied) {
                                  // Route already applied
                                  return Container(
                                    width: double.infinity,
                                    padding: const EdgeInsets.symmetric(vertical: 14),
                                    decoration: BoxDecoration(
                                      color: activeColor.withOpacity(0.8),
                                      borderRadius: BorderRadius.circular(20),
                                    ),
                                    child: Row(
                                      mainAxisAlignment: MainAxisAlignment.center,
                                      children: [
                                        const Icon(
                                          Icons.check,
                                          color: Colors.white,
                                          size: 20,
                                        ),
                                        const SizedBox(width: 8),
                                        Text(
                                          AppLocalizations.instance.routeApplied,
                                          style: const TextStyle(
                                            color: Colors.white,
                                            fontSize: 15,
                                            fontWeight: FontWeight.w700,
                                          ),
                                        ),
                                      ],
                                    ),
                                  );
                                }

                                return Column(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    GestureDetector(
                                      onTap: () {
                                        _startDirectRouteInGoogleMaps(places);
                                      },
                                      child: Container(
                                        width: double.infinity,
                                        padding: const EdgeInsets.symmetric(vertical: 8),
                                        decoration: BoxDecoration(
                                          color: Colors.white,
                                          borderRadius: BorderRadius.circular(32),
                                          border: Border.all(color: WanderlustColors.borderLight, width: 1),
                                        ),
                                        child: Row(
                                          mainAxisAlignment: MainAxisAlignment.center,
                                          children: [
                                            Container(
                                              padding: const EdgeInsets.all(8),
                                              decoration: BoxDecoration(
                                                color: WanderlustColors.accent.withOpacity(0.08),
                                                shape: BoxShape.circle,
                                              ),
                                              child: Image.asset(
                                                'assets/icons/icon_start.png',
                                                width: 28,
                                                height: 28,
                                              ),
                                            ),
                                            const SizedBox(width: 12),
                                            Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              children: [
                                                Text(
                                                  AppLocalizations.instance.startRoute,
                                                  style: const TextStyle(
                                                    color: Colors.black,
                                                    fontSize: 16,
                                                    fontWeight: FontWeight.w800,
                                                  ),
                                                ),
                                                const SizedBox(height: 2),
                                                Text(
                                                  AppLocalizations.instance.isEnglish ? "${places.length} stops · Google Maps" : "${places.length} durak · Google Maps",
                                                  style: const TextStyle(
                                                    color: WanderlustColors.textGrey,
                                                    fontSize: 12,
                                                    fontWeight: FontWeight.w600,
                                                  ),
                                                ),
                                              ],
                                            ),
                                          ],
                                        ),
                                      ),
                                    ),
                                  ],
                                );
                              },
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),
          );
        },
    );
  }

  /// Google Maps'te hazır rotayı direkt başlat 
  Future<void> _startDirectRouteInGoogleMaps(List<Highlight> places) async {
    // 🔥 Premium Check
    if (!PremiumService.instance.canGetDirections()) {
      _showPaywall();
      return;
    }

    if (places.length < 2) return;

    HapticFeedback.heavyImpact();

    // Yardımcı: İsim kodlama
    String encodePlace(Highlight p) => Uri.encodeComponent("${p.name}, ${_city?.city ?? ''}");

    final userOrigin = await _getUserOriginIfInCity();
    final origin = userOrigin != null
        ? "${userOrigin.latitude},${userOrigin.longitude}"
        : encodePlace(places.first);
    final destination = encodePlace(places.last);
    
    // Dynamic travel mode (default walking for suggested routes)
    String travelMode = 'walking';

    String waypoints = "";
    if (places.length > 1) {
       final startIdx = userOrigin != null ? 0 : 1;
       final wpList = places.sublist(startIdx, places.length - 1).map(encodePlace).toList();
       waypoints = "&waypoints=${wpList.join('|')}";
    }

    final url = "https://www.google.com/maps/dir/?api=1&origin=$origin&destination=$destination$waypoints&travelmode=$travelMode";

    try {
      final uri = Uri.parse(url);
      await launchUrl(uri, mode: LaunchMode.externalApplication);
    } catch (e) {
      debugPrint('Google Maps açılamadı: $e');
    }
  }

  Widget _buildStopCard(
    Highlight place,
    int index,
    int total,
    Color accentColor,
  ) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final isLast = index == total - 1;

    return IntrinsicHeight(
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Sol Taraf: Dinamik Harita Pini ve Yol Çizgisi
          SizedBox(
            width: 48,
            child: Stack(
              alignment: Alignment.topCenter,
              clipBehavior: Clip.none,
              children: [
                if (!isLast)
                  Positioned(
                    top: 40, // Pin'in ortalarından başlar
                    bottom: -50, // Bir sonraki pin'in arkasına kadar uzanır
                    child: Container(
                      width: 3,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            WanderlustColors.accent.withOpacity(0.8),
                            WanderlustColors.accent.withOpacity(0.1),
                          ],
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                        ),
                        borderRadius: BorderRadius.circular(2),
                      ),
                    ),
                  ),
                Center(
                  child: Padding(
                    padding: const EdgeInsets.only(bottom: 16), // Sağdaki kartın alt boşluğu (16) ile tam hizalamak için
                    child: Container(
                      width: 32,
                      height: 32,
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            WanderlustColors.accent.withOpacity(0.8),
                            WanderlustColors.accent,
                          ],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        shape: BoxShape.circle,
                        boxShadow: [
                          BoxShadow(
                            color: WanderlustColors.accent.withOpacity(0.4),
                            blurRadius: 8,
                            offset: const Offset(0, 3),
                          ),
                        ],
                        border: Border.all(color: Colors.white, width: 2),
                      ),
                      child: Center(
                        child: Text(
                          String.fromCharCode(65 + index), // A, B, C...
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 14,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ),
          
          // Sağ Taraf: Havalı İçerik Kartı
          Expanded(
            child: Padding(
              padding: const EdgeInsets.only(bottom: 16),
              child: GestureDetector(
              onTap: () {
                Navigator.pop(context);
                // Fotoğrafı prefetch et
                ImagePrefetchService.prefetchSinglePhoto(context, place.imageUrl, heroDecode: true);
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
                );
              },
              child: Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(20),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.04),
                      blurRadius: 10,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Row(
                  children: [
                    ClipRRect(
                      borderRadius: BorderRadius.circular(14),
                      child: SizedBox(
                        width: 60,
                        height: 60,
                        child: hasImage
                            ? ResilientNetworkImage(
                                imageUrl: place.imageUrl,
                                placeName: place.name,
                                city: place.city ?? _city?.city ?? '',
                                category: place.category,
                                blurHash: place.blurHash,
                                fit: BoxFit.cover,
                                placeholderBuilder: (_) => Container(
                                  color: WanderlustColors.bgCardLight,
                                  child: const Icon(
                                    Icons.place,
                                    color: WanderlustColors.textGrey,
                                    size: 24,
                                  ),
                                ),
                              )
                            : Container(
                                color: WanderlustColors.bgCardLight,
                                child: const Icon(
                                  Icons.place,
                                  color: WanderlustColors.textGrey,
                                  size: 24,
                                ),
                              ),
                      ),
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            place.getLocalizedName(AppLocalizations.instance.isEnglish),
                            style: const TextStyle(
                              color: Colors.black87,
                              fontSize: 16,
                              fontWeight: FontWeight.bold,
                            ),
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                          ),
                          const SizedBox(height: 6),
                          Row(
                            children: [
                              Container(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 8,
                                  vertical: 4,
                                ),
                                decoration: BoxDecoration(
                                  color: Colors.grey.shade100,
                                  borderRadius: BorderRadius.circular(6),
                                ),
                                child: Text(
                                  AppLocalizations.instance.translateCategory(place.category.trim()),
                                  style: TextStyle(
                                    color: Colors.grey.shade700,
                                    fontSize: 10,
                                    fontWeight: FontWeight.bold,
                                  ),
                                ),
                              ),
                              const SizedBox(width: 8),
                              Expanded(
                                child: Text(
                                  place.area.isNotEmpty ? place.area : (place.city ?? ""),
                                  style: TextStyle(
                                    color: Colors.grey.shade500,
                                    fontSize: 12,
                                    fontWeight: FontWeight.w500,
                                  ),
                                  overflow: TextOverflow.ellipsis,
                                ),
                              ),
                            ],
                          ),
                        ],
                      ),
                    ),
                    Icon(Icons.arrow_forward_ios_rounded, color: Colors.grey.shade300, size: 16),
                  ],
                ),
              ),
            ),
          ),
        ),
      ],
    ),
  );
}
}

// ══════════════════════════════════════════════════════════════════════════
// CUSTOM PAINTER - ROUTE MAP (API key yokken fallback)
// ══════════════════════════════════════════════════════════════════════════

class RouteMapPainter extends CustomPainter {
  final List<Highlight> places;
  final Color accentColor;
  final Color bgColor;

  RouteMapPainter({
    required this.places,
    required this.accentColor,
    required this.bgColor,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final bgPaint = Paint()..color = bgColor;
    canvas.drawRect(Rect.fromLTWH(0, 0, size.width, size.height), bgPaint);

    if (places.isEmpty) return;

    // Grid çizgileri
    final gridPaint = Paint()
      ..color = accentColor.withOpacity(0.08)
      ..strokeWidth = 1;
    for (int i = 0; i < 12; i++) {
      final y = size.height * i / 12;
      canvas.drawLine(Offset(0, y), Offset(size.width, y), gridPaint);
    }
    for (int i = 0; i < 20; i++) {
      final x = size.width * i / 20;
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), gridPaint);
    }

    // Koordinatları normalize et
    double minLat = places.map((p) => p.lat).reduce((a, b) => a < b ? a : b);
    double maxLat = places.map((p) => p.lat).reduce((a, b) => a > b ? a : b);
    double minLng = places.map((p) => p.lng).reduce((a, b) => a < b ? a : b);
    double maxLng = places.map((p) => p.lng).reduce((a, b) => a > b ? a : b);

    final latPadding = (maxLat - minLat) * 0.2;
    final lngPadding = (maxLng - minLng) * 0.2;
    minLat -= latPadding;
    maxLat += latPadding;
    minLng -= lngPadding;
    maxLng += lngPadding;

    // Noktaları hesapla
    final points = places.map((p) {
      final x =
          (p.lng - minLng) / (maxLng - minLng) * size.width * 0.85 +
          size.width * 0.075;
      final y =
          size.height -
          ((p.lat - minLat) / (maxLat - minLat) * size.height * 0.65 +
              size.height * 0.175);
      return Offset(x, y);
    }).toList();

    // Rota çizgisi
    if (points.length > 1) {
      final pathPaint = Paint()
        ..color = accentColor.withOpacity(0.7)
        ..strokeWidth = 3
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round;

      final path = Path();
      path.moveTo(points.first.dx, points.first.dy);
      for (int i = 1; i < points.length; i++) {
        path.lineTo(points[i].dx, points[i].dy);
      }
      canvas.drawPath(path, pathPaint);

      // Glow efekti
      final glowPaint = Paint()
        ..color = accentColor.withOpacity(0.25)
        ..strokeWidth = 10
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 6);
      canvas.drawPath(path, glowPaint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}

// ══════════════════════════════════════════════════════════════════════════
// ANIMATED BUILDER HELPER
// ══════════════════════════════════════════════════════════════════════════

class AnimatedBuilder extends AnimatedWidget {
  final Widget Function(BuildContext, Widget?) builder;
  final Widget? child;

  const AnimatedBuilder({
    super.key,
    required Animation<double> animation,
    required this.builder,
    this.child,
  }) : super(listenable: animation);

  @override
  Widget build(BuildContext context) => builder(context, child);
}

class _SliverAppBarDelegate extends SliverPersistentHeaderDelegate {
  final Widget child;

  _SliverAppBarDelegate(this.child);

  @override
  double get minExtent => 50.0; // TabBar height

  @override
  double get maxExtent => 50.0;

  @override
  Widget build(
      BuildContext context, double shrinkOffset, bool overlapsContent) {
    return Container(
      color: WanderlustColors.bgDark, // WanderlustColors.bgDark
      child: child,
    );
  }

  @override
  bool shouldRebuild(_SliverAppBarDelegate oldDelegate) {
    return true;
  }
}
