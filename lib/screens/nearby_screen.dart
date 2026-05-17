// =============================================================================
// NEARBY SCREEN v5 - DARK THEME + AMBER + HAİTA TOGGLE + ANİMASYONLAR
// =============================================================================

import 'dart:convert';
import '../services/trip_update_service.dart';
import '../l10n/app_localizations.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:url_launcher/url_launcher.dart';
import '../utils/map_theme.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import 'detail_screen.dart';
import '../theme/wanderlust_colors.dart';
import 'package:geolocator/geolocator.dart';
import '../services/location_context_service.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../services/tutorial_service.dart';
import '../widgets/tutorial_overlay_widget.dart';
import '../services/premium_service.dart';
import '../services/plan_repository.dart';
import 'paywall_screen.dart';
import '../services/auto_slot_picker.dart';
import '../widgets/day_selection_dialog.dart';
import '../widgets/resilient_network_image.dart';
import 'dart:ui';
import '../services/image_prefetch_service.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../utils/image_utils.dart';

// Tema renkleri
const Color bgDark = WanderlustColors.bgDark;
const Color bgCard = WanderlustColors.bgCard;
const Color bgCardLight = WanderlustColors.bgCardLight;
const Color accent = WanderlustColors.accent; // Purple
const Color accentLight = WanderlustColors.accentLight; // Purple Light
const Color textPrimary = WanderlustColors.textWhite;
const Color textSecondary = WanderlustColors.textGrey;
const Color textWhite = WanderlustColors.textWhite;
const Color textGrey = WanderlustColors.textGrey;
const Color accentGreen = Color(0xFF4CAF50);
const Color borderColor = WanderlustColors.borderLight;

class NearbyScreen extends StatefulWidget {
  final bool isVisible;
  const NearbyScreen({super.key, this.isVisible = false});

  @override
  State<NearbyScreen> createState() => _NearbyScreenState();
}

class _NearbyScreenState extends State<NearbyScreen>
    with TickerProviderStateMixin {
  List<_NearbyPlace> _allPlaces = [];
  List<_NearbyPlace> _filteredPlaces = [];
  bool _loading = true;
  String _selectedCity = "berlin";

  static const String _allCategoryId = "Tümü";
  static const double _cityCenterSliderMaxDistanceValue = 20.0;
  static const double _liveLocationSliderMaxDistanceValue = 8.0;

  String _selectedCategory = _allCategoryId;
  String _selectedSort = AppLocalizations.instance.sortByDistance;
  double _maxDistance = 100.0;
  double _cityCenterSliderMaxDistance = _cityCenterSliderMaxDistanceValue;
  double _liveLocationSliderMaxDistance = _liveLocationSliderMaxDistanceValue;

  List<String> _routePlaces = [];
  List<String> _favorites = [];
  bool _showMap = false;
  String _searchQuery = '';
  final TextEditingController _searchController = TextEditingController();
  final GlobalKey _distanceFilterKey = GlobalKey();

  late AnimationController _animController;
  late AnimationController _listAnimController;
  late Animation<double> _fadeAnim;

  // Scroll Controller
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;

  int _lastPrefetchIndex = 15;

  void _onScroll() {
    final showButton = _scrollController.offset > 400;
    if (showButton != _showScrollToTop) {
      setState(() => _showScrollToTop = showButton);
    }

    // Katman 3: Scroll Listener Prefetch
    // Kullanıcı listeyi aşağı kaydırdıkça bir sonraki mekanları dinamik olarak prefetch et
    if (_filteredPlaces.isNotEmpty) {
      // Header, slider vs yaklaşık 400px, her kart ortalama 160px
      final estimatedIndex = ((_scrollController.offset - 400) / 160).floor();
      final targetIndex = estimatedIndex + 10; // Ekranda görünenden 10 adım sonrasını hazırla
      
      if (targetIndex > _lastPrefetchIndex) {
        final startIndex = _lastPrefetchIndex;
        final endIndex = targetIndex.clamp(0, _filteredPlaces.length);
        
        if (startIndex < endIndex) {
          for (int i = startIndex; i < endIndex; i++) {
            final p = _filteredPlaces[i];
            if (p.imageUrl != null && p.imageUrl!.isNotEmpty) {
              final safeUrl = firebaseCompatibleImageUrl(p.imageUrl!);
              if (safeUrl.isNotEmpty) {
                CachedNetworkImageProvider(safeUrl, cacheManager: AppImageCacheManager.instance).resolve(ImageConfiguration.empty);
              }
            }
          }
          _lastPrefetchIndex = endIndex;
        }
      }
    }
  }

  void _scrollToTop() {
    _scrollController.animateTo(
      0,
      duration: const Duration(milliseconds: 500),
      curve: Curves.easeInOut,
    );
  }

  // Harita değişkenleri
  GoogleMapController? _mapController;
  Set<Marker> _markers = {};
  String? _darkMapStyle;
  // Şehir merkezi koordinatları (cityData'dan alınacak)
  double _cityCenterLat = 41.3851;
  double _cityCenterLng = 2.1734;

  List<Map<String, dynamic>> get _categories => [
    {"id": _allCategoryId, "name": AppLocalizations.instance.allCategories, "icon": Icons.apps_rounded},
    {"id": "Restoran", "name": AppLocalizations.instance.translateCategory("Restoran"), "icon": Icons.restaurant_rounded},
    {"id": "Kafe", "name": AppLocalizations.instance.translateCategory("Kafe"), "icon": Icons.local_cafe_rounded},
    {"id": "Bar", "name": AppLocalizations.instance.translateCategory("Bar"), "icon": Icons.local_bar_rounded},
    {"id": "Müze", "name": AppLocalizations.instance.translateCategory("Müze"), "icon": Icons.museum_rounded},
    {"id": "Park", "name": AppLocalizations.instance.translateCategory("Park"), "icon": Icons.park_rounded},
    {"id": "Tarihi", "name": AppLocalizations.instance.translateCategory("Tarihi"), "icon": Icons.account_balance_rounded},
    {"id": "Manzara", "name": AppLocalizations.instance.translateCategory("Manzara"), "icon": Icons.landscape_rounded},
    {"id": "Deneyim", "name": AppLocalizations.instance.translateCategory("Deneyim"), "icon": Icons.explore_rounded},
    {"id": "Alışveriş", "name": AppLocalizations.instance.translateCategory("Alışveriş"), "icon": Icons.shopping_bag_rounded},
  ];

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    _setupAnimations();
    _loadMapStyle();
    _loadData(); // This now handles location context
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
    TripUpdateService().cityChanged.addListener(_onCityChanged);
    TripUpdateService().favoritesUpdated.addListener(_onFavoritesChanged);
    LocationContextService.instance.addListener(_onLocationModeChanged);
    LocationContextService.instance.setNearbyActive(widget.isVisible);
    
    WidgetsBinding.instance.addPostFrameCallback((_) {
       // Listen for tutorial triggers from MainScreen or Service
       TutorialService.instance.tutorialTrigger.listen((key) {
         if (key == TutorialService.KEY_TUTORIAL_NEARBY) {
           if (mounted) _showNearbyTutorial();
         }
       });
    });
  }

  void _onLocationModeChanged() {
    if (!mounted) return;
    setState(() {
      _syncMaxDistance();
    });
    _recalculateDistances();
  }

  LocationReferenceMode get _selectedReferenceMode {
    final referenceMode = LocationContextService.instance.referenceMode;
    if (referenceMode == LocationReferenceMode.liveLocation) {
      return LocationReferenceMode.liveLocation;
    }
    return LocationReferenceMode.cityCenter;
  }

  double get _sliderMaxDistance {
    if (_selectedReferenceMode == LocationReferenceMode.liveLocation) {
      return _liveLocationSliderMaxDistance;
    }
    return _cityCenterSliderMaxDistance;
  }

  double get _defaultMaxDistance {
    if (_selectedReferenceMode == LocationReferenceMode.liveLocation) {
      return (_sliderMaxDistance * 0.5).clamp(2.5, _sliderMaxDistance).toDouble();
    }
    return (_sliderMaxDistance * 0.45).clamp(4.0, _sliderMaxDistance).toDouble();
  }

  double get _effectiveMaxDistance => _normalizedDistanceValue(_maxDistance);

  void _syncMaxDistance({bool resetToDefault = false}) {
    _maxDistance = resetToDefault ? _defaultMaxDistance : _effectiveMaxDistance;
  }

  double _normalizedDistanceValue(double currentDistance) {
    if (currentDistance > _sliderMaxDistance) {
      return _defaultMaxDistance;
    }
    return currentDistance.clamp(0.5, _sliderMaxDistance).toDouble();
  }

  String _formatDistanceText(double distanceKm) {
    if (distanceKm < 1) {
      return "${(distanceKm * 1000).round()} m";
    }
    return "${distanceKm.toStringAsFixed(1)} km";
  }

  void _updateDistancePresets() {
    _cityCenterSliderMaxDistance = _cityCenterSliderMaxDistanceValue;
    _liveLocationSliderMaxDistance = _liveLocationSliderMaxDistanceValue;
  }

  String _referenceModeLabel(LocationReferenceMode mode) {
    final isEnglish = AppLocalizations.instance.isEnglish;
    switch (mode) {
      case LocationReferenceMode.auto:
        return isEnglish ? "Automatic" : "Otomatik";
      case LocationReferenceMode.cityCenter:
        return isEnglish ? "City Center" : "Şehir Merkezi";
      case LocationReferenceMode.liveLocation:
        return isEnglish ? "My Location" : "Konumum";
    }
  }

  Widget _referenceModeIcon(LocationReferenceMode mode, {Color? color}) {
    switch (mode) {
      case LocationReferenceMode.auto:
        return Icon(Icons.auto_awesome_rounded, size: 16, color: color);
      case LocationReferenceMode.cityCenter:
        return Image.asset('assets/icons/city.png', width: 18, height: 18);
      case LocationReferenceMode.liveLocation:
        return Image.asset('assets/icons/location.png', width: 18, height: 18);
    }
  }

  Future<void> _selectReferenceMode(LocationReferenceMode mode) async {
    HapticFeedback.selectionClick();
    final previousMode = _selectedReferenceMode;
    final success = await LocationContextService.instance.setReferenceMode(
      mode,
      requestPermissionIfNeeded: mode == LocationReferenceMode.liveLocation,
    );

    if (!mounted) return;

    final currentMode = _selectedReferenceMode;
    setState(() {
      _syncMaxDistance(resetToDefault: success && previousMode != currentMode);
    });

    if (!success && mode == LocationReferenceMode.liveLocation) {
      final reason = LocationContextService.instance.reason;
      final showSettingsAction =
          reason == LocationContextReason.permissionDenied ||
          reason == LocationContextReason.permissionDeniedForever ||
          reason == LocationContextReason.serviceDisabled;

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(LocationContextService.instance.statusDescription),
          behavior: SnackBarBehavior.floating,
          action: showSettingsAction
              ? SnackBarAction(
                  label: AppLocalizations.instance.settingsTitle,
                  onPressed: () async {
                    if (reason == LocationContextReason.serviceDisabled) {
                      await Geolocator.openLocationSettings();
                    } else {
                      await Geolocator.openAppSettings();
                    }
                  },
                )
              : null,
        ),
      );
    }
  }

  void _resetFilters() {
    setState(() {
      _selectedCategory = _allCategoryId;
      _selectedSort = AppLocalizations.instance.sortByDistance;
      _searchQuery = '';
      _searchController.clear();
      _syncMaxDistance(resetToDefault: true);
    });
    _applyFilters();
  }

  Future<void> _loadMapStyle() async {
    // Senkron yükleme (sabit değişken) - Gecikme yok
    setState(() => _darkMapStyle = darkMapStyle);
    if (_mapController != null) {
      _mapController!.setMapStyle(darkMapStyle);
    }
  }

  void _setupAnimations() {
    _animController = AnimationController(
      duration: const Duration(milliseconds: 500),
      vsync: this,
    );
    _listAnimController = AnimationController(
      duration: const Duration(milliseconds: 400),
      vsync: this,
    );
    _fadeAnim = CurvedAnimation(parent: _animController, curve: Curves.easeOut);
  }

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();
    final selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    final currentCity = selectedCity.toLowerCase();
    
    // Şehir bazlı bucket list yükle
    final bucketList = prefs.getStringList("trip_places_$currentCity") ?? [];
    final Set<String> allTripNames = Set.from(bucketList);

    // Rota / Schedule verilerini de kontrol et (Checkmark'ların doğru görünmesi için)
    final scheduleJson = prefs.getString("trip_schedule_$currentCity");
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

    if (mounted) {
      setState(() {
        _selectedCity = selectedCity;
        _routePlaces = allTripNames.toList();
        _favorites = prefs.getStringList("favorite_places") ?? [];
      });
    }
    
    // Gerçek şehir verisini yükle
    try {
      final cityData = await CityDataLoader.loadCity(_selectedCity);

      await LocationContextService.instance.updateContext(cityData);
      if (LocationContextService.instance.referenceMode ==
          LocationReferenceMode.auto) {
        await LocationContextService.instance.setReferenceMode(
          LocationReferenceMode.cityCenter,
        );
      }
      _updateDistancePresets();

      final places = cityData.highlights
          .map((h) {
             final distMeters = LocationContextService.instance.getDistance(h.lat, h.lng);
             final isEnglish = AppLocalizations.instance.isEnglish;
             return _NearbyPlace(
              name: h.getLocalizedName(isEnglish),
              category: h.category,
              distanceMeters: distMeters,
              rating: h.rating ?? 4.5,
              area: h.getLocalizedArea(isEnglish),
              imageUrl: h.imageUrl,
              blurHash: h.blurHash,
              description: h.getLocalizedDescription(isEnglish),
              price: h.price,
              highlight: h,
            );
          })
          .toList();

      places.sort((a, b) => a.distanceMeters.compareTo(b.distanceMeters));
      
      // Tüm fotoğraf URL'lerini topla (şehir değiştiğinde daha agresif yükle)
      final allUrlsToDownload = <String>[];
      for (final p in places.take(50)) { // 50 fotoğrafa çıkar
        if (p.imageUrl != null && p.imageUrl!.isNotEmpty) {
          final safeUrl = firebaseCompatibleImageUrl(p.imageUrl!);
          if (safeUrl.isNotEmpty && !allUrlsToDownload.contains(safeUrl)) {
            allUrlsToDownload.add(safeUrl);
          }
        }
      }

      if (mounted) {
        setState(() {
          _allPlaces = places;
          _filteredPlaces = List.from(places);
          _loading = false;
          _syncMaxDistance(resetToDefault: true);
          // Şehir merkezi koordinatlarını güncelle
          _cityCenterLat = cityData.centerLat;
          _cityCenterLng = cityData.centerLng;
        });
        
        _animController.forward();
        _applyFilters();
        
        // Harita açıksa kamerayı yeni şehre taşı
        _mapController?.animateCamera(
          CameraUpdate.newLatLngZoom(
            LatLng(_cityCenterLat, _cityCenterLng),
            13,
          ),
        );
      }

      // Arka planda fotoğrafları hemen yükle - öncelikli olarak ilk 20'yi yükle
      if (allUrlsToDownload.isNotEmpty) {
        final priorityUrls = allUrlsToDownload.take(20).toList();
        final remainingUrls = allUrlsToDownload.skip(20).toList();
        
        // Hemen başlat - öncelikli URL'leri paralel yükle
        for (final url in priorityUrls) {
          AppImageCacheManager.instance.downloadFile(url).catchError((_) {});
        }
        
        // Sonra kalan fotoğrafları yükle (düşük öncelik)
        for (final url in remainingUrls) {
          AppImageCacheManager.instance.downloadFile(url).catchError((_) {});
        }
      }
    } catch (e) {
      debugPrint("Yakınımda veri yükleme hatası: $e");
      if (mounted) {
        setState(() => _loading = false);
      }
    }
  }



  void _recalculateDistances() {
      if (_allPlaces.isEmpty) return;
      
      final updatedPlaces = _allPlaces.map((p) {
         final distMeters = LocationContextService.instance.getDistance(p.highlight.lat, p.highlight.lng);
         final isEnglish = AppLocalizations.instance.isEnglish;
         return _NearbyPlace(
            name: p.highlight.getLocalizedName(isEnglish),
            category: p.category,
            distanceMeters: distMeters,
            rating: p.rating,
            area: p.highlight.getLocalizedArea(isEnglish),
            imageUrl: p.imageUrl,
            blurHash: p.highlight.blurHash,
            description: p.highlight.getLocalizedDescription(isEnglish),
            price: p.price,
            highlight: p.highlight,
         );
      }).toList();

      setState(() {
          _allPlaces = updatedPlaces;
      });
      _applyFilters();
  }

  /// Birçok şehirde barlar JSON'da `Yeme-İçme`, `Kafe` veya `Deneyim` olarak işaretli;
  /// yalnızca `category == Bar` bakmak liste boş kalmasına yol açıyor.
  bool _matchesBarCategoryHeuristic(_NearbyPlace p) {
    const explicit = {
      'Bar',
      'Pub',
      'Wine Bar',
      'Enoteca',
      'Lounge',
      'American Bar',
    };
    if (explicit.contains(p.category)) return true;

    final h = p.highlight;
    final names = '${p.name} ${h.nameEn ?? ''}'.toLowerCase();

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
    if (_allPlaces.isEmpty) return;

    // Liste animasyonu
    _listAnimController.reset();
    final effectiveMaxDistance = _effectiveMaxDistance;

    List<_NearbyPlace> filtered = List.from(_allPlaces);

    if (_selectedCategory != _allCategoryId) {
      // Kategori eşleşmesini hem Türkçe hem İngilizce için kontrol et
      final categoryMappings = {
        'Kafe': ['Kafe', 'Cafe', 'Coffee'],
        'Müze': ['Müze', 'Museum'],
        'Restoran': ['Restoran', 'Restaurant', 'Yeme-İçme'],
        'Bar': ['Bar'],
        'Park': ['Park'],
        'Tarihi': ['Tarihi', 'Historical', 'Historic'],
        'Manzara': ['Manzara', 'View', 'Viewpoint'],
        'Deneyim': ['Deneyim', 'Experience'],
        'Alışveriş': ['Alışveriş', 'Shopping'],
      };

      if (_selectedCategory == 'Bar') {
        filtered = filtered.where(_matchesBarCategoryHeuristic).toList();
      } else {
        final validCategories =
            categoryMappings[_selectedCategory] ?? [_selectedCategory];
        filtered = filtered
            .where((p) => validCategories.contains(p.category))
            .toList();
        // Bar olarak tanınan mekanlar yalnızca Bar filtresinde (Keşfet ile uyum).
        if (_selectedCategory == 'Restoran' ||
            _selectedCategory == 'Deneyim') {
          filtered = filtered
              .where((p) => !_matchesBarCategoryHeuristic(p))
              .toList();
        }
      }
    }
    filtered = filtered.where((p) => p.distanceMeters <= effectiveMaxDistance * 1000).toList();

    // Search filter
    if (_searchQuery.isNotEmpty) {
      final query = _searchQuery.toLowerCase();
      filtered = filtered.where((p) => 
        p.name.toLowerCase().contains(query) ||
        p.area.toLowerCase().contains(query) ||
        (p.description?.toLowerCase().contains(query) ?? false)
      ).toList();
    }

    if (_selectedSort == AppLocalizations.instance.sortByDistance) {
      filtered.sort((a, b) => a.distanceMeters.compareTo(b.distanceMeters));
    } else if (_selectedSort == AppLocalizations.instance.sortByRating) {
      filtered.sort((a, b) => b.rating.compareTo(a.rating));
    } else if (_selectedSort == AppLocalizations.instance.sortByName) {
      filtered.sort((a, b) => a.name.compareTo(b.name));
    }

    setState(() => _filteredPlaces = filtered);
    _updateMarkers(); // Markerları güncelle
    _listAnimController.forward();

    // Filtre veya sıralama değiştiğinde scroll tracking sıfırlanmalı
    _lastPrefetchIndex = 15;

    // Katman 2: Progressive Prefetch for Nearby
    // Kullanıcının listeyi veya filtreyi değiştirdiği an ilk 15 mekanın fotoğrafını beklemeden RAM+Disk'e çek
    for (final p in filtered.take(15)) {
      if (p.imageUrl != null && p.imageUrl!.isNotEmpty) {
        final safeUrl = firebaseCompatibleImageUrl(p.imageUrl!);
        if (safeUrl.isNotEmpty) {
          CachedNetworkImageProvider(safeUrl, cacheManager: AppImageCacheManager.instance).resolve(ImageConfiguration.empty);
        }
      }
    }
  }

  Future<void> _toggleFavorite(String name) async {
    HapticFeedback.lightImpact();
    final prefs = await SharedPreferences.getInstance();
    
    // Favoriyi şehir:mekan formatında kaydet
    final favoriteKey = "$_selectedCity:$name";

    setState(() {
      if (_favorites.contains(favoriteKey)) {
        _favorites.remove(favoriteKey);
      } else {
        _favorites.add(favoriteKey);
      }
    });

    await prefs.setStringList("favorite_places", _favorites);
    TripUpdateService().notifyFavoritesChanged();
  }

  void _onFavoritesChanged() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _favorites = prefs.getStringList("favorite_places") ?? [];
    });
  }

  /// Mekanın favori olup olmadığını kontrol et (şehir:mekan formatı)
  bool _isFavorite(String name) {
    final key = "$_selectedCity:$name";
    return _favorites.contains(key);
  }

  Future<void> _toggleRoute(String name) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    final String currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
    // 1. Güncel verileri oku
    final List<String> tripPlaces = prefs.getStringList("trip_places_$currentCity") ?? [];
    final String? scheduleJson = prefs.getString("trip_schedule_$currentCity");
    
    // Schedule'ı parse et
    Map<String, dynamic> scheduleMap = {};
    if (scheduleJson != null) {
      try {
        scheduleMap = jsonDecode(scheduleJson);
      } catch (e) { print(e); }
    }
    
    final bool alreadyInRoute = _routePlaces.contains(name);

    if (alreadyInRoute) {
        // ÇIKARMA İŞLEMİ
        setState(() {
            _routePlaces.remove(name);
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
             content: Text(
               AppLocalizations.instance.removedFromRoute(name),
               style: TextStyle(color: textWhite, fontWeight: FontWeight.w500),
             ),
             backgroundColor: bgCardLight,
             behavior: SnackBarBehavior.floating,
             duration: const Duration(milliseconds: 1200),
          ));
        }
    } else {
        // EKLEME İŞLEMİ — kota: tek global sayaç (keşfet / detay / yakınımda toplamı)
        if (!PremiumService.instance.canAddToRoute()) {
          _showPaywall();
          return;
        }

        final int currentTotalDays = prefs.getInt("tripDays_$currentCity") ?? prefs.getInt("tripDays") ?? 3;
        final int? selectedDay = await _showDaySelectionDialogForNearby(currentTotalDays, name, scheduleMap);
        if (selectedDay == null) return; // İptal edildi

        // Kullanımı artır
        await PremiumService.instance.useRouteAdd();

        setState(() {
           _routePlaces.add(name);
        });

        if (selectedDay == 0) {
          // LISTEM'E EKLEME — sadece trip_places_ güncellenir
          if (!tripPlaces.contains(name)) {
            tripPlaces.add(name);
          }
          await prefs.setStringList("trip_places_$currentCity", tripPlaces);
          await PlanRepository.markPlanCreated(currentCity);
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
                       style: TextStyle(
                         color: textWhite,
                         fontWeight: FontWeight.w600,
                       ),
                     ),
                   ),
                 ],
               ),
               backgroundColor: bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 1500),
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 20),
            ));
          }
        } else {
          // GÜNE EKLEME — sadece schedule güncellenir, trip_places_ dokunulmaz
          final dayKey = selectedDay.toString();
          List<dynamic> targetList = scheduleMap[dayKey] ?? [];
          final placeEntry = {'name': name, 'city': currentCity};
          final alreadyExists = targetList.any((item) {
            if (item is Map<String, dynamic>) return item['name'] == name;
            if (item is String) return item == name;
            return false;
          });
          if (!alreadyExists) targetList.add(placeEntry);
          scheduleMap[dayKey] = targetList;

          // Yeni gün oluşturulduysa onboardingDays güncelle
          if (selectedDay > currentTotalDays) {
            await prefs.setInt("tripDays_$currentCity", selectedDay);
          }

          // Save ONLY schedule — trip_places_ dokunulmaz
          await prefs.setString("trip_schedule_$currentCity", jsonEncode(scheduleMap));
          await PlanRepository.markPlanCreated(currentCity);
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
                       style: TextStyle(
                         color: textWhite,
                         fontWeight: FontWeight.w600,
                       ),
                     ),
                   ),
                 ],
               ),
               backgroundColor: bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 1500),
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 20),
            ));
          }
        }
    }

    // Çıkarma durumunda schedule ve tripPlaces'i güncelle
    if (!_routePlaces.contains(name)) {
      tripPlaces.remove(name);
      await prefs.setStringList("trip_places_$currentCity", tripPlaces);
      await prefs.setString("trip_schedule_$currentCity", jsonEncode(scheduleMap));
      await PlanRepository.markPlanCreated(currentCity);
      TripUpdateService().notifyTripChanged();
    }
  }
  


  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }
  
  Future<int?> _showDaySelectionDialogForNearby(int totalDays, String placeName, Map<String, dynamic> scheduleMap) async {
    return showDaySelectionDialog(
      context,
      totalDays: totalDays,
      scheduleMap: scheduleMap,
      confirmMessage: AppLocalizations.instance.addToRouteConfirmDialog(placeName),
    );
  }



  @override
  void didUpdateWidget(NearbyScreen oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.isVisible != widget.isVisible) {
      LocationContextService.instance.setNearbyActive(widget.isVisible);
    }
  }

  @override
  void dispose() {
    _scrollController.dispose();
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    TripUpdateService().cityChanged.removeListener(_onCityChanged);
    TripUpdateService().favoritesUpdated.removeListener(_onFavoritesChanged);
    LocationContextService.instance.removeListener(_onLocationModeChanged);
    LocationContextService.instance.setNearbyActive(false);
    _animController.dispose();
    _listAnimController.dispose();
    _searchController.dispose();
    super.dispose();
  }
  
  void _onTripDataChanged() {
      _refreshRouteState();
  }
  
  void _onCityChanged() {
    if (_scrollController.hasClients) {
      _scrollController.jumpTo(0);
    }
    if (mounted) {
      setState(() {
        _showScrollToTop = false;
      });
    }
    _loadData();
  }
  
  Future<void> _refreshRouteState() async {
     final prefs = await SharedPreferences.getInstance();
     final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
     final newList = prefs.getStringList("trip_places_$currentCity") ?? [];
     if (mounted) {
       setState(() {
         _routePlaces = newList;
       });
     }
  }

  Color _getCategoryColor(String category) {
    switch (category) {
      case "Kafe":
        return const Color(0xFFFDAA5D);
      case "Restoran":
        return const Color(0xFFFF7675);
      case "Bar":
        return const Color(0xFFA29BFE);
      case "Müze":
        return const Color(0xFF74B9FF);
      case "Park":
        return const Color(0xFF00B894);
      case "Tarihi":
        return const Color(0xFFE17055);
      case "Manzara":
        return const Color(0xFF00CEC9);
      case "Deneyim":
        return const Color(0xFFD63031);
      case "Alışveriş":
        return const Color(0xFFFF6B9D);
      default:
        return accent;
    }
  }

  IconData _getCategoryIcon(String category) {
    switch (category) {
      case "Kafe":
        return Icons.local_cafe_rounded;
      case "Restoran":
        return Icons.restaurant_rounded;
      case "Bar":
        return Icons.local_bar_rounded;
      case "Müze":
        return Icons.museum_rounded;
      case "Park":
        return Icons.park_rounded;
      case "Tarihi":
        return Icons.account_balance_rounded;
      case "Manzara":
        return Icons.landscape_rounded;
      case "Deneyim":
        return Icons.explore_rounded;
      case "Alışveriş":
        return Icons.shopping_bag_rounded;
      default:
        return Icons.place_rounded;
    }
  }

  String _getCityDisplayName(String cityId) {
    final isEnglish = AppLocalizations.instance.isEnglish;
    final names = {
      'istanbul': isEnglish ? 'Istanbul' : 'İstanbul',
      'kapadokya': isEnglish ? 'Cappadocia' : 'Kapadokya',
      'cappadocia': isEnglish ? 'Cappadocia' : 'Kapadokya',
      'barcelona': 'Barcelona',
      'paris': 'Paris',
      'roma': isEnglish ? 'Rome' : 'Roma',
      'berlin': 'Berlin',
      'londra': isEnglish ? 'London' : 'Londra',
      'amsterdam': 'Amsterdam',
      'tokyo': 'Tokyo',
      'atina': isEnglish ? 'Athens' : 'Atina',
      'bangkok': 'Bangkok',
      'budapeste': isEnglish ? 'Budapest' : 'Budapeşte',
      'cenevre': isEnglish ? 'Geneva' : 'Cenevre',
      'dubai': 'Dubai',
      'dublin': 'Dublin',
      'floransa': isEnglish ? 'Florence' : 'Floransa',
      'hongkong': 'Hong Kong',
      'kopenhag': isEnglish ? 'Copenhagen' : 'Kopenhag',
      'lizbon': isEnglish ? 'Lisbon' : 'Lizbon',
      'lucerne': 'Lucerne',
      'lyon': 'Lyon',
      'madrid': 'Madrid',
      'marakes': isEnglish ? 'Marrakech' : 'Marakeş',
      'marsilya': isEnglish ? 'Marseille' : 'Marsilya',
      'milano': isEnglish ? 'Milan' : 'Milano',
      'napoli': isEnglish ? 'Naples' : 'Napoli',
      'newyork': 'New York',
      'nice': 'Nice',
      'porto': 'Porto',
      'prag': isEnglish ? 'Prague' : 'Prag',
      'seul': isEnglish ? 'Seoul' : 'Seul',
      'sevilla': isEnglish ? 'Seville' : 'Sevilla',
      'singapur': isEnglish ? 'Singapore' : 'Singapur',
      'stockholm': 'Stockholm',
      'venedik': isEnglish ? 'Venice' : 'Venedik',
      'viyana': isEnglish ? 'Vienna' : 'Viyana',
      'zurih': isEnglish ? 'Zurich' : 'Zürih',
      'antalya': 'Antalya',
      'belgrad': isEnglish ? 'Belgrade' : 'Belgrad',
      'edinburgh': 'Edinburgh',
      'hallstatt': 'Hallstatt',
      'strazburg': isEnglish ? 'Strasbourg' : 'Strazburg',
      'kahire': isEnglish ? 'Cairo' : 'Kahire',
      'fes': 'Fes',
      'brugge': isEnglish ? 'Bruges' : 'Brugge',
      'santorini': 'Santorini',
      'heidelberg': 'Heidelberg',
      'colmar': 'Colmar',
      'sintra': 'Sintra',
      'sansebastian': 'San Sebastian',
      'bologna': 'Bologna',
      'matera': 'Matera',
      'gaziantep': 'Gaziantep',
      'oslo': 'Oslo',
      'rovaniemi': 'Rovaniemi',
      'tromso': 'Tromso',
      'zermatt': 'Zermatt',
      'giethoorn': 'Giethoorn',
      'kotor': 'Kotor',

    };
    // Eğer bulunamazsa baş harfi büyük yap
    return names[cityId.toLowerCase()] ?? cityId[0].toUpperCase() + cityId.substring(1);
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
      backgroundColor: bgDark,
      body: _loading
          ? Center(
              child: CircularProgressIndicator(strokeWidth: 2, color: accent),
            )
          : FadeTransition(
              opacity: _fadeAnim,
              child: _showMap 
                ? Column(
                    children: [
                      _buildHeader(),
                      _buildLocationCard(),
                      _buildDistanceSlider(),
                      _buildSearchBar(),
                      _buildCategories(),
                      Expanded(child: _buildMapView()),
                    ],
                  )
                : Stack(
                    children: [
                      Column(
                        children: [
                          Expanded(
                            child: CustomScrollView(
                              controller: _scrollController,
                              cacheExtent: 1500,
                              physics: const BouncingScrollPhysics(),
                              slivers: [
                                SliverToBoxAdapter(child: _buildHeader()),
                                SliverToBoxAdapter(child: _buildLocationCard()),
                                SliverToBoxAdapter(child: _buildDistanceSlider()),
                                SliverToBoxAdapter(child: _buildSearchBar()),
                                SliverToBoxAdapter(child: _buildCategories()),
                                _buildPlacesSliverList(),
                              ],
                            ),
                          ),
                        ],
                      ),
                      if (_showScrollToTop)
                    Positioned(
                      right: 20,
                      bottom: 30,
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
            ),
    );
  }

  Widget _buildHeader() {
    return SafeArea(
      bottom: false,
      child: Padding(
        padding: const EdgeInsets.fromLTRB(20, 12, 20, 0),
        child: Row(
          children: [
            // Amber ikon
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
                'assets/icons/icon_nearby.png',
                width: 32,
                height: 32,
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    AppLocalizations.instance.navNearby,
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.w700,
                      color: textPrimary,
                      letterSpacing: -0.5,
                    ),
                  ),
                  Text(
                    _getCityDisplayName(_selectedCity),
                    style: const TextStyle(fontSize: 14, color: textSecondary),
                  ),
                ],
              ),
            ),
            // Harita toggle butonu
            GestureDetector(
              onTap: () {
                HapticFeedback.lightImpact();
                setState(() => _showMap = !_showMap);
              },
              child: Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: _showMap ? accent : bgCard,
                  borderRadius: BorderRadius.circular(14),
                  border: Border.all(
                    color: _showMap ? accent : Colors.white.withOpacity(0.1),
                  ),
                ),
                child: _showMap
                    ? const Icon(
                        Icons.list_rounded,
                        color: Colors.white,
                        size: 22,
                      )
                    : Image.asset(
                        'assets/icons/icon_map.png',
                        width: 22,
                        height: 22,
                      ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSearchBar() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 8, 20, 0),
      child: Container(
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: TextField(
          controller: _searchController,
          style: const TextStyle(color: textPrimary, fontSize: 15),
          decoration: InputDecoration(
            hintText: AppLocalizations.instance.searchPlaces,
            hintStyle: TextStyle(color: textSecondary.withOpacity(0.6)),
            prefixIcon: Icon(Icons.search_rounded, color: textSecondary, size: 22),
            suffixIcon: _searchQuery.isNotEmpty
                ? GestureDetector(
                    onTap: () {
                      _searchController.clear();
                      setState(() => _searchQuery = '');
                      _applyFilters();
                    },
                    child: Icon(Icons.close_rounded, color: textSecondary, size: 20),
                  )
                : null,
            border: InputBorder.none,
            contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          ),
          onChanged: (value) {
            setState(() => _searchQuery = value);
            _applyFilters();
          },
        ),
      ),
    );
  }

  Widget _buildLocationCard() {
    final locationContext = LocationContextService.instance;
    final sourceIsLocation = locationContext.isTravelMode;
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.white.withOpacity(0.05)),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: Colors.transparent,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Image.asset(
                    sourceIsLocation ? 'assets/icons/location.png' : 'assets/icons/city.png',
                    width: 22,
                    height: 22,
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        locationContext.statusTitle,
                        style: TextStyle(
                          fontSize: 15,
                          fontWeight: FontWeight.w600,
                          color: textPrimary,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 12),
            Text(
              locationContext.statusDescription,
              style: TextStyle(
                fontSize: 12,
                height: 1.35,
                color: textSecondary.withOpacity(0.85),
              ),
            ),
            const SizedBox(height: 14),
            Row(
              children: [
                Expanded(
                  child: _buildReferenceModeChip(
                    LocationReferenceMode.liveLocation,
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: _buildReferenceModeChip(
                    LocationReferenceMode.cityCenter,
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildReferenceModeChip(LocationReferenceMode mode) {
    final isSelected = _selectedReferenceMode == mode;
    return GestureDetector(
      onTap: () => _selectReferenceMode(mode),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 180),
        height: 42,
        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 8),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: bgCardLight,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: isSelected ? textPrimary.withOpacity(0.45) : borderColor.withOpacity(0.35),
            width: isSelected ? 1.5 : 1,
          ),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            SizedBox(
              width: 15,
              height: 15,
              child: _referenceModeIcon(mode, color: textPrimary),
            ),
            const SizedBox(width: 6),
            Flexible(
              child: Text(
                _referenceModeLabel(mode),
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w600,
                  color: textPrimary,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDistanceSlider() {
    final effectiveMaxDistance = _effectiveMaxDistance;
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 14, 20, 0),
      child: Column(
        key: _distanceFilterKey,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                AppLocalizations.instance.maxDistance,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: textSecondary,
                ),
              ),
              Text(
                _formatDistanceText(effectiveMaxDistance),
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w700,
                  color: accent,
                ),
              ),
            ],
          ),
          const SizedBox(height: 4),
          SliderTheme(
            data: SliderThemeData(
              activeTrackColor: accent,
              inactiveTrackColor: bgCardLight,
              thumbColor: accent,
              overlayColor: accent.withOpacity(0.2),
              trackHeight: 6,
              thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 8),
            ),
            child: Slider(
              value: effectiveMaxDistance,
              min: 0.5,
              max: _sliderMaxDistance,
              onChanged: (val) {
                setState(() => _maxDistance = val);
              },
              onChangeEnd: (val) {
                _applyFilters();
              },
            ),
          ),
          Text(
            _selectedReferenceMode == LocationReferenceMode.liveLocation
                ? (AppLocalizations.instance.isEnglish
                    ? "My Location mode searches within ${_formatDistanceText(_liveLocationSliderMaxDistance)} around you."
                    : "Konumum modunda arama çevrende en fazla ${_formatDistanceText(_liveLocationSliderMaxDistance)} içinde yapılır.")
                : (AppLocalizations.instance.isEnglish
                    ? "City Center mode scans up to ${_formatDistanceText(_cityCenterSliderMaxDistance)} from the center."
                    : "Şehir Merkezi modunda tarama merkezden en fazla ${_formatDistanceText(_cityCenterSliderMaxDistance)} uzaklığa kadar yapılır."),
            style: TextStyle(
              fontSize: 12,
              color: textSecondary.withOpacity(0.75),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCategories() {
    return Padding(
      padding: const EdgeInsets.only(top: 16),
      child: SizedBox(
        height: 44,
        child: ListView.builder(
          scrollDirection: Axis.horizontal,
          physics: const BouncingScrollPhysics(),
          padding: const EdgeInsets.symmetric(horizontal: 20),
          itemCount: _categories.length,
          itemBuilder: (context, index) {
            final cat = _categories[index];
            final isSelected = _selectedCategory == cat["id"];

            return GestureDetector(
              onTap: () {
                HapticFeedback.selectionClick();
                setState(() => _selectedCategory = cat["id"]);
                _applyFilters();
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                margin: const EdgeInsets.only(right: 10),
                padding: const EdgeInsets.symmetric(horizontal: 16),
                decoration: BoxDecoration(
                  color: isSelected ? accent : bgCard,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isSelected ? accent : Colors.white.withOpacity(0.08),
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      cat["icon"] as IconData,
                      size: 18,
                      color: isSelected ? Colors.white : textSecondary,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      cat["name"] as String,
                      style: TextStyle(
                        fontSize: 14,
                        fontWeight: FontWeight.w600,
                        color: isSelected ? Colors.white : textSecondary,
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
    );
  }

  Widget _buildMapView() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 20, 20, 20),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.white.withOpacity(0.05)),
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: GoogleMap(
          initialCameraPosition: CameraPosition(
            target: LatLng(_cityCenterLat, _cityCenterLng),
            zoom: 13,
          ),
          onMapCreated: (controller) {
            _mapController = controller;
            if (_darkMapStyle != null) {
              _mapController!.setMapStyle(_darkMapStyle);
            }
            if (_filteredPlaces.isNotEmpty) {
              _updateMarkers();
              _fitBounds();
            }
          },
          markers: _markers,
          myLocationEnabled: true,
          myLocationButtonEnabled: false,
          zoomControlsEnabled: false,
          mapToolbarEnabled: false,
          compassEnabled: false,
        ),
      ),
    );
  }

  void _updateMarkers() {
    final markers = _filteredPlaces.map((place) {
      return Marker(
        markerId: MarkerId(place.name),
        position: LatLng(place.highlight.lat, place.highlight.lng),
        infoWindow: InfoWindow(
          title: place.highlight.getLocalizedName(AppLocalizations.instance.isEnglish),
          snippet: place.category,
          onTap: () {
            // Navigation
            Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => DetailScreen(place: place.highlight)),
            );
          },
        ),
        icon: BitmapDescriptor.defaultMarkerWithHue(
          _getMarkerHue(place.category),
        ),
      );
    }).toSet();

    setState(() {
      _markers = markers;
    });
    
    if (_showMap && _filteredPlaces.isNotEmpty && _mapController != null) {
      _fitBounds();
    }
  }

  void _fitBounds() {
    if (_filteredPlaces.isEmpty || _mapController == null) return;

    double minLat = 90.0, maxLat = -90.0, minLng = 180.0, maxLng = -180.0;

    for (var place in _filteredPlaces) {
      final lat = place.highlight.lat;
      final lng = place.highlight.lng;
      if (lat == 0 && lng == 0) continue;

      if (lat < minLat) minLat = lat;
      if (lat > maxLat) maxLat = lat;
      if (lng < minLng) minLng = lng;
      if (lng > maxLng) maxLng = lng;
    }

    if (minLat == 90.0) return;

    _mapController!.animateCamera(
      CameraUpdate.newLatLngBounds(
        LatLngBounds(
          southwest: LatLng(minLat, minLng),
          northeast: LatLng(maxLat, maxLng),
        ),
        50,
      ),
    );
  }

  double _getMarkerHue(String category) {
    // Siyah-Gri-Amber paleti (Hue değerleri)
    // Amber/Gold: ~35-45, Koyu tonlar için düşük saturation ile çalışılabilir
    // Google Maps hue: 0=Red, 30=Orange, 45=Yellow/Amber, 270=Purple
    switch (category) {
      case "Park": return 45;           // Amber/Gold
      case "Restoran": return 35;       // Turuncu-Amber
      case "Kafe": return 40;           // Altın Sarısı
      case "Müze": return 30;           // Koyu Turuncu
      case "Tarihi": return 25;         // Bronz
      case "Bar": return 20;            // Bakır
      case "Deneyim": return 38;        // Amber
      case "Alışveriş": return 42;      // Sarı-Altın
      default: return 36;               // Varsayılan Amber
    }
  }

  void _showPlacePreview(_NearbyPlace place) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      builder: (ctx) => Container(
        padding: const EdgeInsets.all(24),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.2),
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 20),
            Row(
              children: [
                Container(
                  width: 60,
                  height: 60,
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.08),
                    borderRadius: BorderRadius.circular(14),
                    border: Border.all(color: Colors.white.withOpacity(0.12), width: 1),
                  ),
                  child: Icon(
                    _getCategoryIcon(place.category),
                    color: Colors.white,
                    size: 28,
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        place.highlight.getLocalizedName(AppLocalizations.instance.isEnglish),
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty 
                            ? place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish) 
                            : (place.highlight.city ?? ""),
                        style: const TextStyle(
                          fontSize: 14,
                          color: textSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
                Container(
                  padding: const EdgeInsets.symmetric(
                    horizontal: 10,
                    vertical: 6,
                  ),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: Colors.white.withOpacity(0.1), width: 0.5),
                  ),
                  child: Row(
                    children: [
                      const Icon(
                        Icons.star_rounded,
                        color: Color(0xFFFDCB6E),
                        size: 14,
                      ),
                      const SizedBox(width: 4),
                      Text(
                        place.rating.toString(),
                        style: const TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w700,
                          color: Colors.white,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Row(
              children: [
                Expanded(
                  child: GestureDetector(
                    onTap: () {
                      Navigator.pop(ctx);
                      _toggleRoute(place.highlight.name);
                    },
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      decoration: BoxDecoration(
                        color: _routePlaces.contains(place.name)
                            ? Colors.transparent
                            : accent,
                        borderRadius: BorderRadius.circular(12),
                        border: _routePlaces.contains(place.name)
                            ? Border.all(color: accent, width: 1.5)
                            : null,
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            _routePlaces.contains(place.name)
                                ? Icons.add_location_alt_outlined
                                : Icons.add_rounded,
                            color: _routePlaces.contains(place.name) ? accent : Colors.white,
                            size: 20,
                          ),
                          const SizedBox(width: 8),
                          Text(
                            _routePlaces.contains(place.name)
                                ? AppLocalizations.instance.addedToRoute
                                : AppLocalizations.instance.addToRoute,
                            style: TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w600,
                              color: _routePlaces.contains(place.name) ? accent : Colors.white,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ],
            ),
            SizedBox(height: MediaQuery.of(ctx).padding.bottom + 10),
          ],
        ),
      ),
    );
  }

  void _showPlaceDetail(_NearbyPlace place, Color color, IconData icon) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (ctx) => DraggableScrollableSheet(
        initialChildSize: 0.75,
        minChildSize: 0.5,
        maxChildSize: 0.95,
        builder: (_, scrollController) => Container(
          decoration: const BoxDecoration(
            color: bgCard,
            borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
          ),
          child: Column(
            children: [
              // Handle
              Padding(
                padding: const EdgeInsets.only(top: 12, bottom: 8),
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              // Content
              Expanded(
                child: ListView(
                  controller: scrollController,
                  padding: const EdgeInsets.all(20),
                  children: [
                    // Fotoğraf
                    ClipRRect(
                      borderRadius: BorderRadius.circular(16),
                      child: SizedBox(
                        height: 200,
                        child: ResilientNetworkImage(
                          imageUrl: place.imageUrl,
                          placeName: place.name,
                          city: place.area,
                          category: place.category,
                          blurHash: place.blurHash,
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                    const SizedBox(height: 20),

                    // Kategori ve Rating
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 12,
                            vertical: 6,
                          ),
                          decoration: BoxDecoration(
                            color: Colors.white.withOpacity(0.08),
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(color: Colors.white.withOpacity(0.12), width: 0.8),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(icon, size: 16, color: Colors.white.withOpacity(0.8)),
                              const SizedBox(width: 8),
                              Text(
                                AppLocalizations.instance.translateCategory(place.category),
                                style: TextStyle(
                                  fontSize: 13,
                                  fontWeight: FontWeight.w600,
                                  color: Colors.white.withOpacity(0.8),
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Spacer(),
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 10,
                            vertical: 6,
                          ),
                          decoration: BoxDecoration(
                            color: Colors.white.withOpacity(0.1),
                            borderRadius: BorderRadius.circular(8),
                            border: Border.all(color: Colors.white.withOpacity(0.1), width: 0.5),
                          ),
                          child: Row(
                            children: [
                              const Icon(
                                Icons.star_rounded,
                                color: Color(0xFFFDCB6E),
                                size: 14,
                              ),
                              const SizedBox(width: 4),
                              Text(
                                place.rating.toStringAsFixed(1),
                                style: const TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w700,
                                  color: Colors.white,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 16),

                    // İsim
                    FittedBox(
                      fit: BoxFit.scaleDown,
                      alignment: Alignment.centerLeft,
                      child: Text(
                        place.highlight.getLocalizedName(AppLocalizations.instance.isEnglish),
                        style: const TextStyle(
                          fontSize: 26,
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                          letterSpacing: -0.5,
                        ),
                      ),
                    ),
                    const SizedBox(height: 8),

                    // Konum
                    Row(
                      children: [
                        Icon(
                          Icons.location_on_rounded,
                          size: 18,
                          color: textSecondary,
                        ),
                        const SizedBox(width: 6),
                        Text(
                          place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty 
                              ? place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish) 
                              : (place.highlight.city ?? ""),
                          style: const TextStyle(
                            fontSize: 15,
                            color: textSecondary,
                          ),
                        ),
                        const SizedBox(width: 16),
                        Icon(
                          Icons.directions_walk_rounded,
                          size: 18,
                          color: accent,
                        ),
                        const SizedBox(width: 6),
                        Text(
                          "${place.distanceKm.toStringAsFixed(1)} km • ${(place.distanceKm * 12).round()} dk yürüme",
                          style: TextStyle(
                            fontSize: 14,
                            color: accent,
                            fontWeight: FontWeight.w500,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 24),

                    // Açıklama (eğer varsa)
                    if (place.description != null &&
                        place.description!.isNotEmpty) ...[
                      Text(
                        AppLocalizations.instance.about,
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        place.highlight.getLocalizedDescription(AppLocalizations.instance.isEnglish),
                        style: const TextStyle(
                          fontSize: 15,
                          color: textSecondary,
                          height: 1.5,
                        ),
                      ),
                      const SizedBox(height: 24),
                    ],

                    // Bilgi kartları
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: bgCardLight,
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: Column(
                        children: [
                          _buildInfoRow(
                            Icons.access_time_rounded,
                            "Tahmini süre",
                            "1-2 saat",
                          ),
                          const Divider(color: Colors.white10, height: 24),
                          _buildInfoRow(
                            Icons.payments_rounded,
                            "Fiyat aralığı",
                            place.price ?? "Orta",
                          ),
                          const Divider(color: Colors.white10, height: 24),
                          _buildInfoRow(
                            Icons.wb_sunny_rounded,
                            "En iyi zaman",
                            "Sabah / Öğleden sonra",
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 24),

                    // Aksiyon butonları
                    Row(
                      children: [
                        // Favori
                        Expanded(
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 16),
                            decoration: BoxDecoration(
                              color: bgCardLight,
                              borderRadius: BorderRadius.circular(14),
                            ),
                            child: const Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(
                                  Icons.favorite_border_rounded,
                                  color: textSecondary,
                                  size: 22,
                                ),
                                SizedBox(width: 8),
                                Text(
                                  "Favori",
                                  style: TextStyle(
                                    fontSize: 15,
                                    fontWeight: FontWeight.w600,
                                    color: textSecondary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                        const SizedBox(width: 12),
                        // Rotaya Ekle
                        Expanded(
                          flex: 2,
                          child: GestureDetector(
                            onTap: () {
                              Navigator.pop(ctx);
                              _toggleRoute(place.highlight.name);
                            },
                            child: Container(
                              padding: const EdgeInsets.symmetric(vertical: 16),
                              decoration: BoxDecoration(
                                gradient: _routePlaces.contains(place.name)
                                    ? null
                                    : LinearGradient(
                                        colors: [accent, accentLight],
                                        begin: Alignment.centerLeft,
                                        end: Alignment.centerRight,
                                      ),
                                color: _routePlaces.contains(place.name)
                                    ? accent // Filled accent when in route
                                    : null,
                                borderRadius: BorderRadius.circular(14),
                              ),
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Icon(
                                    _routePlaces.contains(place.name)
                                        ? Icons.check_rounded
                                        : Icons.add_rounded,
                                    color: Colors.white,
                                    size: 22,
                                  ),
                                  const SizedBox(width: 8),
                                  Text(
                                    _routePlaces.contains(place.name)
                                        ? "Rotada ✓"
                                        : AppLocalizations.instance.addToRoute,
                                    style: const TextStyle(
                                      fontSize: 15,
                                      fontWeight: FontWeight.w700,
                                      color: Colors.white,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: MediaQuery.of(ctx).padding.bottom + 20),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildPlaceholderImage(Color color, IconData icon) {
    return Container(
      height: 200,
      width: double.infinity,
      decoration: BoxDecoration(
        color: bgCardLight,
        borderRadius: BorderRadius.circular(16),
      ),
      child: Center(
        child: Icon(icon, size: 60, color: Colors.white.withOpacity(0.7)),
      ),
    );
  }

  Widget _buildInfoRow(IconData icon, String label, String value) {
    return Row(
      children: [
        Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: accent.withOpacity(0.1),
            borderRadius: BorderRadius.circular(10),
          ),
          child: Icon(icon, color: accent, size: 20),
        ),
        const SizedBox(width: 14),
        Expanded(
          child: Text(
            label,
            style: const TextStyle(fontSize: 14, color: textSecondary),
          ),
        ),
        Text(
          value,
          style: const TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.w600,
            color: textPrimary,
          ),
        ),
      ],
    );
  }

  Widget _buildPlacesList() {
    if (_filteredPlaces.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.search_off_rounded,
              size: 64,
              color: Colors.white.withOpacity(0.2),
            ),
            const SizedBox(height: 16),
            Text(
              AppLocalizations.instance.noPlacesFoundMatchingCriteria,
              style: TextStyle(fontSize: 16, color: textSecondary),
            ),
            const SizedBox(height: 12),
            GestureDetector(
              onTap: _resetFilters,
              child: Text(
                AppLocalizations.instance.clearFilters,
                style: TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w600,
                  color: accent,
                ),
              ),
            ),
          ],
        ),
      );
    }

    return ListView.builder(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 8, 20, 100),
      itemCount: _filteredPlaces.length,
      itemBuilder: (context, index) {
        final place = _filteredPlaces[index];
        final color = _getCategoryColor(place.category);
        final icon = _getCategoryIcon(place.category);

        final bool isLocked = index > 4 && !PremiumService.instance.isPremium;
        Widget card = _buildPlaceCard(place, color, icon);
        
        if (isLocked) {
          card = GestureDetector(
            onTap: _showPaywall,
            child: ClipRect(
              child: Stack(
                alignment: Alignment.center,
                children: [
                  ImageFiltered(
                    imageFilter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
                    child: IgnorePointer(child: card),
                  ),
                  if (index == 5)
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                      decoration: BoxDecoration(
                        color: WanderlustColors.accent,
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.black.withOpacity(0.3),
                            blurRadius: 8,
                            offset: const Offset(0, 2),
                          ),
                        ],
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.star, color: Colors.white, size: 16),
                          const SizedBox(width: 6),
                          Text(
                            AppLocalizations.instance.isEnglish ? "Unlock More" : "Daha Fazlasını Keşfet",
                            style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                          ),
                        ],
                      ),
                    ),
                ],
              ),
            ),
          );
        }
        
        return card;
      },
    );
  }

  // Sliver version of places list for CustomScrollView
  Widget _buildPlacesSliverList() {
    if (_filteredPlaces.isEmpty) {
      return SliverToBoxAdapter(
        child: Padding(
          padding: const EdgeInsets.all(40),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                Icons.search_off_rounded,
                size: 64,
                color: Colors.white.withOpacity(0.2),
              ),
              const SizedBox(height: 16),
              Text(
                AppLocalizations.instance.noPlacesFoundMatchingCriteria,
                style: const TextStyle(fontSize: 16, color: textSecondary),
              ),
              const SizedBox(height: 12),
              GestureDetector(
                onTap: _resetFilters,
                child: Text(
                  AppLocalizations.instance.clearFilters,
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                    color: accent,
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    }

    return SliverPadding(
      padding: const EdgeInsets.fromLTRB(20, 8, 20, 100),
      sliver: SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            final place = _filteredPlaces[index];
            final color = _getCategoryColor(place.category);
            final icon = _getCategoryIcon(place.category);
            final bool isLocked = index > 4 && !PremiumService.instance.isPremium;
            
            Widget card = _buildPlaceCard(place, color, icon);
            
            if (isLocked) {
              card = GestureDetector(
                onTap: _showPaywall,
                child: ClipRect(
                  child: Stack(
                    alignment: Alignment.center,
                    children: [
                      ImageFiltered(
                        imageFilter: ImageFilter.blur(sigmaX: 5, sigmaY: 5),
                        child: IgnorePointer(child: card),
                      ),
                      if (index == 5) // Only show the button/text on the first locked item to avoid clutter
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                          decoration: BoxDecoration(
                            color: WanderlustColors.accent,
                            borderRadius: BorderRadius.circular(20),
                            boxShadow: [
                              BoxShadow(
                                color: Colors.black.withOpacity(0.3),
                                blurRadius: 8,
                                offset: const Offset(0, 2),
                              ),
                            ],
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              const Icon(Icons.star, color: Colors.white, size: 16),
                              const SizedBox(width: 6),
                              Text(
                                AppLocalizations.instance.isEnglish ? "Unlock More" : "Daha Fazlasını Keşfet",
                                style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold),
                              ),
                            ],
                          ),
                        ),
                    ],
                  ),
                ),
              );
            }
            return RepaintBoundary(
              key: ValueKey("nearby_card_${place.name}"),
              child: card,
            );
          },
          childCount: _filteredPlaces.length,
          addAutomaticKeepAlives: true,
          addRepaintBoundaries: false,
        ),
      ),
    );
  }

  Widget _buildPlaceCard(_NearbyPlace place, Color color, IconData icon) {
    final isInRoute = _routePlaces.contains(place.name);

    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        // Navigation
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => DetailScreen(place: place.highlight),
          ),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 12), // Reduced margin
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16), // Slightly reduced radius
          border: Border.all(color: Colors.white.withOpacity(0.05)),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.2),
              blurRadius: 10,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: IntrinsicHeight( // Ensure row stretches
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Fotoğraf alanı
              Container(
                width: 100, // Reduced width slightly
                decoration: BoxDecoration(
                  borderRadius: const BorderRadius.only(
                    topLeft: Radius.circular(16),
                    bottomLeft: Radius.circular(16),
                  ),
                  image: place.imageUrl != null
                      ? DecorationImage(
                          image: CachedNetworkImageProvider(
                            firebaseCompatibleImageUrl(place.imageUrl!),
                            cacheManager: AppImageCacheManager.instance,
                          ),
                          fit: BoxFit.cover,
                        )
                      : null,
                ),
                child: place.imageUrl == null
                    ? Container(
                        decoration: BoxDecoration(
                          color: bgCardLight,
                          borderRadius: const BorderRadius.only(
                            topLeft: Radius.circular(16),
                            bottomLeft: Radius.circular(16),
                          ),
                        ),
                        child: Center(
                          child: Icon(
                            icon,
                            size: 32, // Reduced icon size
                            color: Colors.white.withOpacity(0.9),
                          ),
                        ),
                      )
                    : null,
              ),

              // İçerik
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.all(10), // Reduced padding
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.center, // Center vertically
                    children: [
                      // Top Row: Category & Rating
                        Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 8,
                              vertical: 4,
                            ),
                            decoration: BoxDecoration(
                              color: accent.withOpacity(0.1),
                              borderRadius: BorderRadius.circular(6),
                              border: Border.all(
                                  color: accent.withOpacity(0.3),
                                  width: 0.5),
                            ),
                            child: Text(
                              AppLocalizations.instance
                                  .translateCategory(place.category),
                              style: const TextStyle(
                                fontSize: 10,
                                fontWeight: FontWeight.w600,
                                color: accent,
                              ),
                            ),
                          ),
                          const Spacer(),
                          // Review score click -> Google Maps (PRO ONLY)
                          GestureDetector(
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

                              final query = Uri.encodeComponent('${place.name} ${_selectedCity}');
                              final url = 'https://www.google.com/maps/search/?api=1&query=$query';
                              if (await canLaunchUrl(Uri.parse(url))) {
                                await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
                              }
                            },
                            child: Row(
                              children: [
                                const Icon(Icons.star_rounded,
                                    size: 14, color: Color(0xFFFDCB6E)),
                                const SizedBox(width: 4),
                                Text(
                                  place.rating.toStringAsFixed(1),
                                  style: const TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w700,
                                    color: textPrimary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 6), // Reduced spacing
                      
                      // Name
                      Text(
                        place.highlight.getLocalizedName(AppLocalizations.instance.isEnglish),
                        style: const TextStyle(
                          fontSize: 15, // Reduced font size
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                          letterSpacing: -0.3,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 2), // Reduced spacing
                      
                      // Area
                      Text(
                        place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty
                            ? place.highlight.getLocalizedArea(AppLocalizations.instance.isEnglish)
                            : (place.highlight.city ?? ""),
                        style: const TextStyle(
                          fontSize: 12, // Reduced font size
                          color: textSecondary,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 10), // Reduced spacing

                      // Action Buttons Row
                      Row(
                        children: [
                          // Favori butonu
                          GestureDetector(
                            onTap: () => _toggleFavorite(place.name),
                            child: Container(
                              padding: const EdgeInsets.all(6), // Reduced padding
                              decoration: BoxDecoration(
                                color: _isFavorite(place.name)
                                    ? accent.withOpacity(0.2)
                                    : bgCardLight,
                                borderRadius: BorderRadius.circular(8),
                              ),
                              child: Icon(
                                _isFavorite(place.name)
                                    ? Icons.favorite_rounded
                                    : Icons.favorite_border_rounded,
                                size: 16, // Reduced size
                                color: _isFavorite(place.name)
                                    ? accent
                                    : textSecondary,
                              ),
                            ),
                          ),
                          const SizedBox(width: 8),
                          
                          // Rotaya ekle butonu - km button style
                          Expanded(
                            child: GestureDetector(
                              onTap: () => _toggleRoute(place.name),
                              child: Container(
                                height: 32,
                                padding: const EdgeInsets.symmetric(horizontal: 8),
                                decoration: BoxDecoration(
                                  color: isInRoute ? accent.withOpacity(0.15) : bgCardLight,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Icon(
                                      isInRoute
                                          ? Icons.check
                                          : Icons.add_location_alt_outlined,
                                      size: 14,
                                      color: isInRoute ? accent : accent,
                                    ),
                                    const SizedBox(width: 4),
                                    Text(
                                      isInRoute
                                          ? AppLocalizations.instance.addedToRoute
                                          : AppLocalizations.instance.addToRoute,
                                      style: TextStyle(
                                        fontSize: 11,
                                        fontWeight: FontWeight.w600,
                                        color: isInRoute ? accent : textPrimary,
                                      ),
                                      maxLines: 1,
                                      overflow: TextOverflow.ellipsis,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          ),
                          const SizedBox(width: 8),
                          
                          // Mesafe badge
                          AnimatedBuilder(
                            animation: LocationContextService.instance,
                            builder: (context, child) {
                              return Container(
                                height: 32, // Match button height
                                padding: const EdgeInsets.symmetric(
                                    horizontal: 8),
                                decoration: BoxDecoration(
                                  color: bgCardLight,
                                  borderRadius: BorderRadius.circular(8),
                                ),
                                child: Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Icon(
                                      Icons.directions_walk_rounded,
                                      size: 13,
                                      color: accent,
                                    ),
                                    const SizedBox(width: 2),
                                    Text(
                                      LocationContextService.instance.getDistanceLabel(place.highlight.lat, place.highlight.lng),
                                      style: const TextStyle(
                                        fontSize: 11,
                                        fontWeight: FontWeight.w600,
                                        color: textPrimary,
                                      ),
                                    ),
                                  ],
                                ),
                              );
                            },
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
  void _showNearbyTutorial() async {
    if (!mounted) return;
    
    final shouldShow = await TutorialService.instance.shouldShowTutorial(TutorialService.KEY_TUTORIAL_NEARBY);
    if (!shouldShow) return;

    // Wait for context to be ready (retry a few times)
    int retries = 0;
    while (_distanceFilterKey.currentContext == null && retries < 5) {
      await Future.delayed(const Duration(milliseconds: 500));
      retries++;
    }

    if (_distanceFilterKey.currentContext == null) {
      debugPrint("Nearby Tutorial Error: _distanceFilterKey context is null after retries");
      return;
    }

    // Scroll to top to ensure header is visible (although pinned)
    if (_scrollController.hasClients && _scrollController.offset > 0) {
       _scrollToTop();
       await Future.delayed(const Duration(milliseconds: 300));
    }

    late TutorialCoachMark tutorial;
    tutorial = TutorialCoachMark(
      targets: [
        TargetFocus(
          identify: "nearby_filter",
          keyTarget: _distanceFilterKey,
          color: Colors.black,
          contents: [
            TargetContent(
              align: ContentAlign.bottom,
              builder: (context, controller) {
                return TutorialOverlayWidget(
                  title: AppLocalizations.instance.isEnglish ? "Nearby & Filters" : "Mesafe ve Filtreleme",
                  description: AppLocalizations.instance.isEnglish 
                      ? "Filter according to what you want right now, whether specific distance or category." 
                      : "Sana yakın veya uzak, o an canın ne istiyorsa ona göre filtrele.",
                  currentStep: 1,
                  totalSteps: 1,
                  onSkip: () => controller.skip(),
                  onNext: () => controller.next(),
                  isArrowUp: true,
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
      onFinish: () {
         TutorialService.instance.markTutorialSeen(TutorialService.KEY_TUTORIAL_NEARBY);
      },
      onSkip: () {
         TutorialService.instance.skipAllTutorials();
         return true;
      },
      onClickTarget: (target) {
         tutorial.next();
      },
      onClickOverlay: (target) {
         tutorial.next();
      },
    )..show(context: context);
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
}

// Harita grid çizici
class _GridPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = Colors.white.withOpacity(0.03)
      ..strokeWidth = 1;

    const spacing = 40.0;

    // Yatay çizgiler
    for (double y = 0; y < size.height; y += spacing) {
      canvas.drawLine(Offset(0, y), Offset(size.width, y), paint);
    }

    // Dikey çizgiler
    for (double x = 0; x < size.width; x += spacing) {
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

class _NearbyPlace {
  final String name;
  final String category;
  final double distanceMeters;
  final double rating;
  final String area;
  final String? imageUrl;
  final String? blurHash;
  final String? description;
  final String? price;
  final Highlight highlight; // Original highlight for detail screen

  double get distanceKm => distanceMeters / 1000;

  _NearbyPlace({
    required this.name,
    required this.category,
    required this.distanceMeters,
    required this.rating,
    required this.area,
    this.imageUrl,
    this.blurHash,
    this.description,
    this.price,
    required this.highlight,
  });
}

// Sticky Header Delegate for pinned search bar and slider
class _StickyHeaderDelegate extends SliverPersistentHeaderDelegate {
  final Widget child;
  
  _StickyHeaderDelegate({required this.child});
  
  @override
  Widget build(BuildContext context, double shrinkOffset, bool overlapsContent) {
    return child;
  }
  
  @override
  double get maxExtent => 165; // height of search bar + slider
  
  @override
  double get minExtent => 165;
  
  @override
  bool shouldRebuild(covariant SliverPersistentHeaderDelegate oldDelegate) => true;
}
