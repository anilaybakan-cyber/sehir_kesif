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
import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/directions_service.dart'; // Import this if needed or generic logic
import '../utils/map_theme.dart';
import 'detail_screen.dart';

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
    required this.accentColor,
    required this.icon,
  });
}

// =============================================================================
// MAIN SCREEN
// =============================================================================

class RoutesScreen extends StatefulWidget {
  const RoutesScreen({super.key});

  @override
  State<RoutesScreen> createState() => _RoutesScreenState();
}

class _RoutesScreenState extends State<RoutesScreen>
    with TickerProviderStateMixin {
  // AMBER/GOLD THEME
  static const Color bgDark = Color(0xFF0D0D1A);
  static const Color bgCard = Color(0xFF1A1A2E);
  static const Color bgCardLight = Color(0xFF252542);
  static const Color accent = Color(0xFFF5A623); // Amber
  static const Color accentLight = Color(0xFFFFB800); // Gold
  static const Color accentBlue = Color(0xFF4ECDC4);
  static const Color accentOrange = Color(0xFFFF9800);
  static const Color accentGreen = Color(0xFF4CAF50);
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFF5A623), Color(0xFFFFB800)],
  );

  static const LinearGradient greenGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFF4CAF50), Color(0xFF2E7D32)],
  );

  // Google Maps API Key - Buraya kendi API key'inizi ekleyin
  // https://console.cloud.google.com/google/maps-apis/credentials
  static const String _googleMapsApiKey = "AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0";

  CityModel? _city;
  bool _loading = true;
  String _travelStyle = "Lokal";
  List<String> _interests = [];
  List<String> _tripPlaceNames = [];
  List<Highlight> _tripPlaces = [];
  Map<int, List<Highlight>> _dayPlans = {};
  int _totalDays = 1;
  int _tripDays = 3; // Onboarding'den gelen gün sayısı
  List<SuggestedRoute> _allSuggestedRoutes = [];
  List<SuggestedRoute> _filteredSuggestedRoutes = [];
  bool _showMapPreview = true;

  // Interactive Map State
  GoogleMapController? _routeMapController;
  Set<Marker> _routeMarkers = {};
  Set<Polyline> _routePolylines = {};

  late TabController _mainTabController;
  TabController? _dayTabController;
  int _selectedRouteFilter = 0; // 0: Tümü, 1: Bana Özel, 2: Popüler

  @override
  void initState() {
    super.initState();
    _mainTabController = TabController(length: 2, vsync: this);
    _loadData();
    // Global değişiklikleri dinle
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
  }

  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    _mainTabController.dispose();
    _dayTabController?.removeListener(_handleDayTabChange);
    _dayTabController?.dispose();
    _routeMapController?.dispose();
    super.dispose();
  }

  void _onTripDataChanged() {
    _loadData();
  }

  void _handleDayTabChange() {
    if (_dayTabController == null || _dayTabController!.indexIsChanging) return;
    
    // Tab değiştiğinde (veya kaydırma bittiğinde) haritayı güncelle
    final currentDay = _dayTabController!.index + 1;
    final places = _dayPlans[currentDay] ?? [];
    
    // Eğer harita açıksa güncelle
    if (_showMapPreview) {
       _updateRouteMapMarkers(places);
    }
  }

  Future<void> _loadData() async {
    final cityData = await CityDataLoader.loadCity("barcelona");
    if (cityData == null) return;

    if (!mounted) return;

    final prefs = await SharedPreferences.getInstance();
    
    // 1. Profil / İlgi Alanları
    final travelStyle = prefs.getString("user_style") ?? "Denge";
    final interests = prefs.getStringList("user_interests") ?? [];
    
    // 2. Rota Verisi
    final savedPlaces = prefs.getStringList("trip_places") ?? [];
    final savedScheduleJson = prefs.getString("trip_schedule");

    final dayPlans = <int, List<Highlight>>{};
    int maxDay = 1;
    bool scheduleLoaded = false;

    if (savedScheduleJson != null) {
      // Kayıtlı program varsa onu yükle
      try {
        final Map<String, dynamic> scheduleMap = jsonDecode(savedScheduleJson);
        scheduleMap.forEach((dayStr, placeNamesList) {
           final day = int.tryParse(dayStr) ?? 1;
           if (day > maxDay) maxDay = day;
           
           final List<dynamic> names = placeNamesList;
           final List<Highlight> places = [];
           
           for (var name in names) {
              final place = cityData.highlights.firstWhere(
                  (h) => h.name == name,
                  orElse: () => cityData.highlights.first
              );
              // İsim eşleşmezse eklemede dikkat et (fallback yüzünden duplicate olmasın)
              if (place.name == name) places.add(place);
           }
           dayPlans[day] = places;
        });
        scheduleLoaded = true;
      } catch (e) {
        print("Schedule parse error: $e");
      }
    } 
    
    // Eğer schedule yoksa veya boşsa ama trip_places varsa (Eski veriyi kurtarma)
    if (!scheduleLoaded && savedPlaces.isNotEmpty) {
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
              final place = cityData.highlights.firstWhere((h) => h.name == name, orElse: () => cityData.highlights.first);
              if (place.name == name) places.add(place);
           }
           dayPlans[i + 1] = places;
       }
    }
    
    // Boş günleri de init et (en azından onboardingden gelen gün sayısı kadar)
    final onboardingDays = prefs.getInt("tripDays") ?? 3;
    if (maxDay < onboardingDays && dayPlans.isEmpty) maxDay = onboardingDays;
    
    if (dayPlans.isEmpty) {
         for (int i = 1; i <= maxDay; i++) {
             dayPlans[i] = [];
         }
    }

    // Trip Places Highlights listesini oluştur (tüm benzersiz mekanlar)
    final Set<String> uniqueNames = {};
    final List<Highlight> tripHighlights = [];
    
    // user_interests veya savedPlaces'den değil, dayPlans'deki her şeyden oluştur
    dayPlans.forEach((_, list) {
        for (var p in list) {
             if (!uniqueNames.contains(p.name)) {
                 uniqueNames.add(p.name);
                 tripHighlights.add(p);
             }
        }
    });

    setState(() {
      _city = cityData;
      _allSuggestedRoutes = _generateSuggestedRoutes(cityData);
      _filteredSuggestedRoutes = _allSuggestedRoutes.take(3).toList();
      _travelStyle = travelStyle;
      _interests = interests;
      _tripPlaceNames = uniqueNames.toList();
      _tripPlaces = tripHighlights;
      _dayPlans = dayPlans;
      _totalDays = maxDay;
      _loading = false;
      
      _dayTabController?.dispose();
      _dayTabController = TabController(length: _totalDays, vsync: this);
      _dayTabController?.addListener(_handleDayTabChange);
    });
  }

  Future<void> _saveTripData() async {
     final prefs = await SharedPreferences.getInstance();
     
     // 1. Liste olarak kaydet
     await prefs.setStringList("trip_places", _tripPlaceNames);
     
     // 2. Schedule olarak kaydet (Gün gün)
     // Map<int, List<Highlight>> -> Map<String, List<String>>
     final Map<String, List<String>> scheduleMap = {};
     
     _dayPlans.forEach((day, places) {
        scheduleMap[day.toString()] = places.map((p) => p.name).toList();
     });
     
     await prefs.setString("trip_schedule", jsonEncode(scheduleMap));
  }

  List<SuggestedRoute> _generateSuggestedRoutes(CityModel city) {
    final cityName = city.city;

    // YARDIMCI: Belirli bir bölgeden ve kategorilerden mekan seçici
    // Bu fonksiyon, belirtilen bölgedeki (veya bölgelerdeki) mekanları tarar
    // ve istenen kategorilerden çeşitlilik sağlayacak şekilde seçim yapar.
    List<String> pickMixedPlaces({
      required List<String> areas, 
      required List<String> categories, 
      int count = 5
    }) {
      final candidates = city.highlights.where((h) {
        final areaMatch = areas.any((a) => h.area.toLowerCase().contains(a.toLowerCase()));
        return areaMatch;
      }).toList();

      final selected = <String>{};
      
      // Önce her kategoriden en az 1 tane bulmaya çalış
      for (final cat in categories) {
        if (selected.length >= count) break;
        final match = candidates.firstWhere(
          (h) => !selected.contains(h.name) && (h.category.contains(cat) || h.tags.contains(cat)),
          orElse: () => candidates.isEmpty ? city.highlights.first : candidates.first, 
        );
        // firstWhere orElse workaround: eğer match yoksa dummy dönüyor, kontrol et
        if (candidates.contains(match) && !selected.contains(match.name)) {
             if (match.category.contains(cat) || match.tags.contains(cat)) {
                selected.add(match.name);
             }
        }
      }

      // Kalanı popüler olanlardan doldur (çeşitlilik katarak)
      for (final h in candidates) {
        if (selected.length >= count) break;
        if (!selected.contains(h.name)) {
          selected.add(h.name);
        }
      }
      
      // Eğer hala sayı yetmediyse genel listeden tamamla (fallback)
      if (selected.length < count) {
         for (final h in city.highlights) {
            if (selected.length >= count) break;
            if (!selected.contains(h.name)) selected.add(h.name);
         }
      }

      return selected.toList();
    }

    return [
      SuggestedRoute(
        id: "classic_tour",
        name: "Klasik $cityName Turu",
        description:
            "Şehrin en ikonik noktalarını keşfedin. İlk kez gelenler için ideal.",
        duration: "4-5 saat",
        distance: "3.2 km",
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800",
        tags: ["Klasik", "Turistik", "Fotoğraf"],
        placeNames: city.highlights
            .where((h) => h.category == "Tarihi" || h.category == "Manzara")
            .take(5)
            .map((h) => h.name)
            .toList(),
        accentColor: accentLight,
        icon: Icons.account_balance,
      ),
      SuggestedRoute(
        id: "gothic_mix",
        name: "Gotik & Gizem",
        description: "Dar sokaklar, tarihi katedraller ve arada gizli kahve molaları.",
        duration: "4-5 saat",
        distance: "3.5 km",
        difficulty: "Kolay",
        imageUrl: "https://images.unsplash.com/photo-1544415918-ad9d65116749?w=800",
        tags: ["Tarih", "Mistik", "Yürüyüş"],
        placeNames: pickMixedPlaces(
          areas: ["Gothic", "Ciutat Vella", "Gotik"],
          categories: ["Tarihi", "Kafe", "Meydan", "Restoran"],
        ),
        accentColor: const Color(0xFFE67E22), // Bronze
        icon: Icons.history_edu,
      ),
      SuggestedRoute(
        id: "born_art",
        name: "Sanat & Lezzet (El Born)",
        description: "Müzelerle dolu bir sabahın ardından parkta dinlenme ve tapas keyfi.",
        duration: "5 saat",
        distance: "4.0 km",
        difficulty: "Kolay",
        imageUrl: "https://images.unsplash.com/photo-1545620864-70950a41be74?w=800",
        tags: ["Sanat", "Tapas", "Park"],
        placeNames: pickMixedPlaces(
          areas: ["Born", "Ribera"],
          categories: ["Müze", "Park", "Bar", "Restoran", "Alışveriş"],
        ),
        accentColor: const Color(0xFFE91E63), // Pink
        icon: Icons.palette,
      ),
      SuggestedRoute(
        id: "gaudi_modern",
        name: "Gaudí ve Modernizm",
        description: "Eixample'ın şık caddelerinde mimari bir şölen ve lüks mağazalar.",
        duration: "6 saat",
        distance: "5.2 km",
        difficulty: "Orta",
        imageUrl: "https://images.unsplash.com/photo-1562699933-40e949987da1?w=800",
        tags: ["Mimari", "Lüks", "Alışveriş"],
        placeNames: pickMixedPlaces(
          areas: ["Eixample", "Passeig"],
          categories: ["Tarihi", "Alışveriş", "Restoran", "Kafe"],
        ),
        accentColor: const Color(0xFF9C27B0), // Purple
        icon: Icons.architecture,
      ),
      SuggestedRoute(
        id: "gracia_bohem",
        name: "Bohem Gràcia Ruhu",
        description: "Turistlerden uzak, yerel halk gibi yaşa. Meydanlar, kafeler ve huzur.",
        duration: "4 saat",
        distance: "3.0 km",
        difficulty: "Kolay",
        imageUrl: "https://images.unsplash.com/photo-1534353436292-078363401783?w=800",
        tags: ["Lokal", "Semt", "Keyif"],
        placeNames: pickMixedPlaces(
          areas: ["Gracia", "Gràcia"],
          categories: ["Park", "Kafe", "Meydan", "Bar"],
        ),
        accentColor: const Color(0xFF2ECC71), // Emerald
        icon: Icons.theater_comedy,
      ),
      SuggestedRoute(
        id: "beach_breeze",
        name: "Deniz & Paella",
        description: "Barceloneta sahilinde yürüyüş, deniz havası ve eşsiz deniz ürünleri.",
        duration: "3-4 saat",
        distance: "2.5 km",
        difficulty: "Çok Kolay",
        imageUrl: "https://images.unsplash.com/photo-1563725807-6bb9f25091a1?w=800",
        tags: ["Plaj", "Yemek", "Manzara"],
        placeNames: pickMixedPlaces(
          areas: ["Barceloneta", "Port"],
          categories: ["Plaj", "Restoran", "Manzara", "Bar"],
        ),
        accentColor: const Color(0xFF3498DB), // Blue
        icon: Icons.waves,
      ),
      SuggestedRoute(
        id: "montjuic_view",
        name: "Zirveden Bakış",
        description: "Montjuïc tepesinde panoramik manzaralar, müzeler ve yeşil bahçeler.",
        duration: "5 saat",
        distance: "6.0 km",
        difficulty: "Zor",
        imageUrl: "https://images.unsplash.com/photo-1528654636952-4fd9ae41865c?w=800",
        tags: ["Manzara", "Doğa", "Spor"],
        placeNames: pickMixedPlaces(
          areas: ["Montjuic", "Montjuïc", "Sants"],
          categories: ["Manzara", "Müze", "Park", "Tarihi"],
        ),
        accentColor: const Color(0xFFF1C40F), // Yellow
        icon: Icons.landscape,
      ),

    ];
  }

  void _filterRoutes(int filterIndex) {
    setState(() {
      _selectedRouteFilter = filterIndex;
      if (filterIndex == 0) {
        _filteredSuggestedRoutes = _allSuggestedRoutes;
      } else if (filterIndex == 1) {
        _filteredSuggestedRoutes = _allSuggestedRoutes.where((route) {
          if (_travelStyle == "Lokal" && route.id == "local_life") return true;
          if (_travelStyle == "Turist" && route.id == "classic_tour")
            return true;
          for (var interest in _interests) {
            if (interest == "Yemek" && route.id == "foodie_tour") return true;
            if (interest == "Sanat" && route.id == "art_culture") return true;
            if (interest == "Fotoğraf" && route.id == "sunset_walk")
              return true;
          }
          return false;
        }).toList();
        if (_filteredSuggestedRoutes.isEmpty) {
          _filteredSuggestedRoutes = _allSuggestedRoutes.take(2).toList();
        }
      } else {
        _filteredSuggestedRoutes = _allSuggestedRoutes.take(3).toList();
      }
    });
  }

  Future<void> _removeFromTrip(String name) async {
    HapticFeedback.mediumImpact();
    setState(() {
      _tripPlaceNames.remove(name);
      _tripPlaces.removeWhere((p) => p.name == name);
      for (var day in _dayPlans.keys) {
        _dayPlans[day]?.removeWhere((p) => p.name == name);
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
    });
  }

  void _optimizeRoute() {
    HapticFeedback.heavyImpact();
    for (var day in _dayPlans.keys) {
      _dayPlans[day]?.sort(
        (a, b) => a.distanceFromCenter.compareTo(b.distanceFromCenter),
      );
    }
    setState(() {});
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: const Row(
          children: [
            Icon(Icons.check_circle, color: Colors.white, size: 20),
            SizedBox(width: 12),
            Text("Rota optimize edildi! ✨"),
          ],
        ),
        backgroundColor: Colors.green.shade600,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // GOOGLE MAPS INTEGRATION - İSİMLİ DURAKLAR
  // ══════════════════════════════════════════════════════════════════════════

  /// Google Maps'te rotayı başlat - MEKAN İSİMLERİYLE
  Future<void> _startRouteInGoogleMaps(int day) async {
    final places = _dayPlans[day] ?? [];
    if (places.length < 2) return;

    HapticFeedback.heavyImpact();

    // Google Maps Parameterized URL
    // https://www.google.com/maps/dir/?api=1&origin=...&destination=...&waypoints=...
    
    // Yardımcı: İsim kodlama
    String encodePlace(Highlight p) => Uri.encodeComponent("${p.name}, ${_city?.city ?? ''}");

    final origin = encodePlace(places.first);
    final destination = encodePlace(places.last);
    
    String waypoints = "";
    if (places.length > 2) {
       final wpList = places.sublist(1, places.length - 1).map(encodePlace).toList();
       waypoints = "&waypoints=${wpList.join('|')}";
    }

    final url = "https://www.google.com/maps/dir/?api=1&origin=$origin&destination=$destination$waypoints&travelmode=walking";

    try {
      final uri = Uri.parse(url);
      if (await canLaunchUrl(uri)) {
        await launchUrl(uri, mode: LaunchMode.externalApplication);
      } else {
        _openMapsWithCoordinates(day); // Fallback
      }
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
      final origin = "${places.first.lat},${places.first.lng}";
      final destination = "${places.last.lat},${places.last.lng}";

      String waypointsParam = "";
      if (places.length > 2) {
        final middlePoints = places.sublist(1, places.length - 1);
        waypointsParam =
            "&waypoints=${middlePoints.map((p) => "${p.lat},${p.lng}").join("|")}";
      }

      final url =
          "https://www.google.com/maps/dir/?api=1"
          "&origin=$origin"
          "&destination=$destination"
          "$waypointsParam"
          "&travelmode=walking";

      await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: const Text("Harita açılamadı"),
          backgroundColor: Colors.red.shade600,
          behavior: SnackBarBehavior.floating,
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
    // Önce kullanıcıya gün seçtir
    final selectedDay = await _showDaySelectionDialog(route.name);
    if (selectedDay == null) return; // İptal edildi

    HapticFeedback.mediumImpact();
    
    setState(() {
      _loading = true;
    });

    // Yapay gecikme (loader görünsün)
    await Future.delayed(const Duration(milliseconds: 600));

    final prefs = await SharedPreferences.getInstance();

    setState(() {
      _loading = false;
      
      // Eğer yeni gün seçildiyse toplam gün sayısını artır
      if (selectedDay > _totalDays) {
          _totalDays = selectedDay;
          _dayPlans[selectedDay] = [];
      }
      
      // İlgili güne mekanları ekle
      final targetList = _dayPlans[selectedDay] ?? [];

      for (var placeName in route.placeNames) {
        if (!_tripPlaceNames.contains(placeName)) {
          _tripPlaceNames.add(placeName);
          
          final place = _city?.highlights
              .where((h) => h.name == placeName)
              .firstOrNull;
              
          if (place != null) {
              _tripPlaces.add(place);
              targetList.add(place);
          }
        }
      }
      
      _dayPlans[selectedDay] = targetList;

    });

    await _saveTripData();
    TripUpdateService().notifyTripChanged();
    
    // Manuel ekleme olduğu için reorganize yapmıyoruz, 
    // ancak _tripPlaces listesini güncel tutmak için _dayPlans'den yeniden oluşturabiliriz.
    // Şimdilik sadece persist ettik.
    
    setState(() {
         // Tab controller'ı güncelle (eğer gün sayısı değiştiyse)
         if (_dayTabController == null || _dayTabController!.length != _totalDays) {
              _dayTabController?.dispose();
              _dayTabController = TabController(length: _totalDays, vsync: this);
         }
    });
    
    // Geri bildirim
    if (!mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Row(
          children: [
            const Icon(Icons.check_circle, color: Colors.white, size: 20),
            const SizedBox(width: 12),
            Expanded(child: Text("${route.name}, ${selectedDay}. güne eklendi! 🎉")),
          ],
        ),
        backgroundColor: route.accentColor,
        behavior: SnackBarBehavior.floating,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
        action: SnackBarAction(
          label: "Görüntüle",
          textColor: Colors.white,
          onPressed: () {
               _mainTabController.animateTo(1);
               _dayTabController?.animateTo(selectedDay - 1);
          },
        ),
      ),
    );
  }

  Future<int?> _showDaySelectionDialog(String routeName) async {
    return showDialog<int>(
      context: context,
      builder: (context) {
        return Dialog(
          backgroundColor: bgCard,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  "Hangi Güne Eklensin?",
                  style: const TextStyle(
                      color: textWhite, fontSize: 18, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 8),
                Text(
                  "'$routeName' rotasını hangi gün planına dahil etmek istersiniz?",
                  textAlign: TextAlign.center,
                  style: const TextStyle(color: textGrey, fontSize: 14),
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
                               title: Text("Gün $day", style: const TextStyle(color: textWhite)),
                               subtitle: Text("$count mekan var", style: const TextStyle(color: textGrey, fontSize: 12)),
                               trailing: const Icon(Icons.arrow_forward_ios, color: accent, size: 16),
                               onTap: () => Navigator.pop(context, day),
                               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
                               tileColor: Colors.transparent,
                               hoverColor: bgCardLight,
                             );
                         }),
                         const Divider(color: borderColor),
                         ListTile(
                             title: const Text("Yeni Gün Oluştur", style: TextStyle(color: textWhite, fontWeight: FontWeight.bold)),
                             subtitle: Text("Gün ${_totalDays + 1}", style: const TextStyle(color: textGrey, fontSize: 12)),
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

  double _calculateTotalDistance(int day) {
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
    return total;
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
      (_calculateTotalDistance(day) / 5 * 60).round();

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
        backgroundColor: bgDark,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  gradient: primaryGradient,
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

    return Scaffold(
      backgroundColor: bgDark,
      body: SafeArea(
        child: Column(
          children: [
            _buildHeader(),
            _buildMainTabs(),
            Expanded(
              child: TabBarView(
                controller: _mainTabController,
                children: [_buildSuggestedRoutesTab(), _buildMyRouteTab()],
              ),
            ),
          ],
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
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              gradient: primaryGradient,
              borderRadius: BorderRadius.circular(14),
            ),
            child: const Icon(Icons.route, color: Colors.white, size: 24),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "${_city?.city ?? ''} Rotaları",
                  style: const TextStyle(
                    color: textWhite,
                    fontSize: 22,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                Text(
                  "${_allSuggestedRoutes.length} hazır rota • ${_tripPlaces.length} seçili nokta • $_tripDays gün",
                  style: const TextStyle(color: textGrey, fontSize: 13),
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
      margin: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      height: 50,
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor),
      ),
      child: TabBar(
        controller: _mainTabController,
        indicator: BoxDecoration(
          gradient: primaryGradient,
          borderRadius: BorderRadius.circular(12),
        ),
        indicatorSize: TabBarIndicatorSize.tab,
        indicatorPadding: const EdgeInsets.all(4),
        dividerColor: Colors.transparent,
        labelColor: Colors.white,
        unselectedLabelColor: textGrey,
        labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
        tabs: [
          const Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.auto_awesome, size: 18),
                SizedBox(width: 8),
                Text("Hazır Rotalar"),
              ],
            ),
          ),
          Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.edit_road, size: 18),
                const SizedBox(width: 8),
                const Text("Benim Rotam"),
                if (_tripPlaces.isNotEmpty) ...[
                  const SizedBox(width: 6),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 6,
                      vertical: 2,
                    ),
                    decoration: BoxDecoration(
                      color: accent,
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: Text(
                      "${_tripPlaces.length}",
                      style: const TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // MY ROUTE TAB - GERÇEK HARİTA ÖNİZLEMESİ
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildMyRouteTab() {
    if (_tripPlaces.isEmpty) {
      return _buildEmptyMyRoute();
    }

    return NestedScrollView(
        headerSliverBuilder: (context, innerBoxIsScrolled) {
            return [
                SliverToBoxAdapter(
                    child: Column(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                            _buildStatsBar(),
                            _buildRealMapPreview(),
                            _buildStartRouteButton(),
                            if (_totalDays <= 1 || _dayTabController == null)
                                const SizedBox(height: 16),
                        ],
                    ),
                ),
                if (_dayTabController != null && _totalDays > 1)
                    SliverPersistentHeader(
                        delegate: _SliverAppBarDelegate(_buildDayTabs()),
                        pinned: true,
                    ),
            ];
        },
        body: _dayTabController != null && _totalDays > 1
              ? TabBarView(
                  controller: _dayTabController,
                  children: List.generate(
                    _totalDays,
                    (i) => _buildDayContent(i + 1),
                  ),
                )
              : _buildDayContent(1),
    );
  }

  Widget _buildEmptyMyRoute() {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(24),
            decoration: const BoxDecoration(
              color: bgCard,
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.map_outlined, size: 48, color: textGrey),
          ),
          const SizedBox(height: 24),
          const Text(
            "Henüz rotanız boş",
            style: TextStyle(
              color: textWhite,
              fontSize: 20,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            "$_tripDays günlük seyahatiniz için\nrotanızı oluşturun",
            style: const TextStyle(color: textGrey, fontSize: 14),
            textAlign: TextAlign.center,
          ),
          const SizedBox(height: 32),
          GestureDetector(
            onTap: () => _mainTabController.animateTo(0),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 28, vertical: 14),
              decoration: BoxDecoration(
                gradient: primaryGradient,
                borderRadius: BorderRadius.circular(14),
                boxShadow: [
                  BoxShadow(
                    color: accentLight.withOpacity(0.4),
                    blurRadius: 16,
                    offset: const Offset(0, 6),
                  ),
                ],
              ),
              child: const Text(
                "Hazır Rotalara Göz At",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildStatsBar() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final distance = _calculateTotalDistance(currentDay);
    final walkTime = _estimateWalkingTime(currentDay);
    final placesCount = _dayPlans[currentDay]?.length ?? 0;

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _buildStatItem(Icons.place, "$placesCount", "Nokta"),
          Container(width: 1, height: 40, color: borderColor),
          _buildStatItem(
            Icons.straighten,
            "${distance.toStringAsFixed(1)} km",
            "Mesafe",
          ),
          Container(width: 1, height: 40, color: borderColor),
          _buildStatItem(Icons.directions_walk, "$walkTime dk", "Yürüyüş"),
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
            color: textWhite,
            fontSize: 16,
            fontWeight: FontWeight.w700,
          ),
        ),
        Text(label, style: const TextStyle(color: textGrey, fontSize: 11)),
      ],
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
        Future.delayed(const Duration(milliseconds: 500), _fitRouteBounds);
    }
  }

  void _fitRouteBounds() {
    if (_routeMarkers.isEmpty || _routeMapController == null) return;
    
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
    
    _routeMapController!.animateCamera(
        CameraUpdate.newLatLngBounds(
            LatLngBounds(
                southwest: LatLng(minLat, minLng),
                northeast: LatLng(maxLat, maxLng),
            ),
            50,
        ),
    );
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
                "Günlük Rota Haritası",
                style: TextStyle(
                    color: textWhite, 
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
                           _updateRouteMapMarkers(places);
                       });
                   }
                },
                borderRadius: BorderRadius.circular(8),
                child: Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: bgCardLight,
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: borderColor),
                  ),
                  child: Row(
                    children: [
                       Text(
                         _showMapPreview ? "Gizle" : "Göster", 
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
          Container(
            height: 240, // Daha kompakt, kaydırma alanı açar
            margin: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: borderColor),
              boxShadow: [
                  BoxShadow(color: Colors.black.withOpacity(0.2), blurRadius: 10, offset: const Offset(0,4)),
              ],
            ),
            child: ClipRRect(
              borderRadius: BorderRadius.circular(16),
              child: GoogleMap(
                initialCameraPosition: const CameraPosition(target: LatLng(41.3851, 2.1734), zoom: 12), // Barcelona default
                onMapCreated: (controller) {
                    _routeMapController = controller;
                    _routeMapController!.setMapStyle(darkMapStyle);
                    _updateRouteMapMarkers(places);
                },
                markers: _routeMarkers,
                polylines: _routePolylines,
                scrollGesturesEnabled: true,
                zoomGesturesEnabled: true,
                myLocationButtonEnabled: false,
                zoomControlsEnabled: true,
                mapToolbarEnabled: false,
                compassEnabled: false,
                trafficEnabled: false,
              ),
            ),
          )
        else
          // Kapalıyken gösterilecek alternatif (boşluk veya çizgi)
          const SizedBox(height: 0),
      ],
    );
  }

  /// API key yoksa custom çizim
  Widget _buildCustomMapFallback(List<Highlight> places) {
    return CustomPaint(
      painter: RouteMapPainter(
        places: places,
        accentColor: accent,
        bgColor: bgCardLight,
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
            gradient: primaryGradient,
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

  /// "Rotayı Başlat" butonu
  Widget _buildStartRouteButton() {
    final currentDay = (_dayTabController?.index ?? 0) + 1;
    final places = _dayPlans[currentDay] ?? [];

    if (places.isEmpty) return const SizedBox.shrink();

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 12, 20, 0),
      child: GestureDetector(
        onTap: () => _startRouteInGoogleMaps(currentDay),
        child: Container(
          width: double.infinity,
          padding: const EdgeInsets.symmetric(vertical: 16),
          decoration: BoxDecoration(
            gradient: greenGradient,
            borderRadius: BorderRadius.circular(14),
            boxShadow: [
              BoxShadow(
                color: accentGreen.withOpacity(0.4),
                blurRadius: 16,
                offset: const Offset(0, 6),
              ),
            ],
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Icon(
                  Icons.navigation,
                  color: Colors.white,
                  size: 20,
                ),
              ),
              const SizedBox(width: 14),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  const Text(
                    "Rotayı Başlat",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  Text(
                    "${places.length} durak • Google Maps'te aç",
                    style: const TextStyle(color: Colors.white70, fontSize: 11),
                  ),
                ],
              ),
              const SizedBox(width: 14),
              const Icon(
                Icons.arrow_forward_ios,
                color: Colors.white70,
                size: 16,
              ),
            ],
          ),
        ),
      ),
    );
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
          gradient: primaryGradient,
          borderRadius: BorderRadius.circular(12),
        ),
        indicatorSize: TabBarIndicatorSize.tab,
        dividerColor: Colors.transparent,
        labelColor: Colors.white,
        unselectedLabelColor: textGrey,
        labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
        unselectedLabelStyle: const TextStyle(
          fontWeight: FontWeight.w500,
          fontSize: 14,
        ),
        onTap: (_) => setState(() {}),
        tabs: List.generate(_totalDays, (index) {
          final day = index + 1;
          final count = _dayPlans[day]?.length ?? 0;
          return Tab(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 14),
              child: Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text("Gün $day"),
                  if (count > 0) ...[
                    const SizedBox(width: 6),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 6,
                        vertical: 2,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.2),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Text(
                        "$count",
                        style: const TextStyle(fontSize: 10),
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

    if (places.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              Icons.wb_sunny_outlined,
              size: 48,
              color: textGrey.withOpacity(0.5),
            ),
            const SizedBox(height: 16),
            Text(
              "Gün $day henüz boş",
              style: const TextStyle(color: textGrey, fontSize: 16),
            ),
            const SizedBox(height: 8),
            Text(
              "Keşfet'ten mekan ekleyin",
              style: TextStyle(color: textGrey.withOpacity(0.7), fontSize: 13),
            ),
          ],
        ),
      );
    }

    return Stack(
      children: [
        ReorderableListView.builder(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 100),
          itemCount: places.length,
          onReorder: (oldIndex, newIndex) =>
              _reorderPlace(day, oldIndex, newIndex),
          proxyDecorator: (child, index, animation) {
            return AnimatedBuilder(
              animation: animation,
              builder: (context, child) {
                final scale = Tween<double>(
                  begin: 1,
                  end: 1.03,
                ).animate(animation);
                return Transform.scale(scale: scale.value, child: child);
              },
              child: child,
            );
          },
          itemBuilder: (context, index) {
            return _buildMyRouteCard(
              key: ValueKey(places[index].name),
              place: places[index],
              index: index,
              isLast: index == places.length - 1,
            );
          },
        ),
        Positioned(
          right: 20,
          bottom: 100,
          child: GestureDetector(
            onTap: _optimizeRoute,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 14),
              decoration: BoxDecoration(
                gradient: primaryGradient,
                borderRadius: BorderRadius.circular(16),
                boxShadow: [
                  BoxShadow(
                    color: accentLight.withOpacity(0.4),
                    blurRadius: 20,
                    offset: const Offset(0, 8),
                  ),
                ],
              ),
              child: const Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(Icons.auto_fix_high, color: Colors.white, size: 20),
                  SizedBox(width: 10),
                  Text(
                    "Optimize Et",
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 14,
                      fontWeight: FontWeight.w600,
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

  Widget _buildMyRouteCard({
    required Key key,
    required Highlight place,
    required int index,
    required bool isLast,
  }) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);

    return Column(
      key: key,
      children: [
        Container(
          decoration: BoxDecoration(
            color: bgCard,
            borderRadius: BorderRadius.circular(16),
            border: Border.all(color: borderColor.withOpacity(0.5)),
          ),
          child: Padding(
            padding: const EdgeInsets.all(12),
            child: Row(
              children: [
                Container(
                  width: 30,
                  height: 30,
                  decoration: BoxDecoration(
                    gradient: primaryGradient,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Center(
                    child: Text(
                      String.fromCharCode(65 + index),
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 13,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: SizedBox(
                    width: 50,
                    height: 50,
                    child: hasImage
                        ? Image.network(
                            place.imageUrl!,
                            fit: BoxFit.cover,
                            errorBuilder: (_, __, ___) => Container(
                              color: color.withOpacity(0.2),
                              child: Icon(Icons.place, color: color, size: 22),
                            ),
                          )
                        : Container(
                            color: color.withOpacity(0.2),
                            child: Icon(Icons.place, color: color, size: 22),
                          ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: GestureDetector(
                    onTap: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => DetailScreen(place: place),
                      ),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          place.name,
                          style: const TextStyle(
                            color: textWhite,
                            fontSize: 14,
                            fontWeight: FontWeight.w600,
                          ),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                        const SizedBox(height: 4),
                        Row(
                          children: [
                            Container(
                              padding: const EdgeInsets.symmetric(
                                horizontal: 6,
                                vertical: 2,
                              ),
                              decoration: BoxDecoration(
                                color: color.withOpacity(0.15),
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: Text(
                                place.category,
                                style: TextStyle(
                                  color: color,
                                  fontSize: 9,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ),
                            const SizedBox(width: 6),
                            Expanded(
                              child: Text(
                                place.area,
                                style: const TextStyle(
                                  color: textGrey,
                                  fontSize: 11,
                                ),
                                overflow: TextOverflow.ellipsis,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
                Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    ReorderableDragStartListener(
                      index: index,
                      child: const Padding(
                        padding: EdgeInsets.all(8),
                        child: Icon(
                          Icons.drag_handle,
                          color: textGrey,
                          size: 20,
                        ),
                      ),
                    ),
                    GestureDetector(
                      onTap: () => _removeFromTrip(place.name),
                      child: const Padding(
                        padding: EdgeInsets.all(8),
                        child: Icon(
                          Icons.close,
                          color: Color(0xFFFF5252),
                          size: 18,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
        if (!isLast)
          Padding(
            padding: const EdgeInsets.only(left: 28),
            child: Container(
              width: 2,
              height: 20,
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    accentLight.withOpacity(0.5),
                    accent.withOpacity(0.3),
                  ],
                ),
              ),
            ),
          ),
      ],
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SUGGESTED ROUTES TAB
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSuggestedRoutesTab() {
    return Column(
      children: [
        _buildRouteFilters(),
        Expanded(
          child: ListView.builder(
            padding: const EdgeInsets.fromLTRB(20, 16, 20, 100),
            itemCount: _filteredSuggestedRoutes.length,
            itemBuilder: (context, index) =>
                _buildSuggestedRouteCard(_filteredSuggestedRoutes[index]),
          ),
        ),
      ],
    );
  }

  Widget _buildRouteFilters() {
    final filters = [
      {"label": "Tümü", "icon": Icons.apps},
      {"label": "Sana Özel", "icon": Icons.auto_awesome},
      {"label": "Popüler", "icon": Icons.trending_up},
    ];
    return Container(
      height: 44,
      margin: const EdgeInsets.only(top: 16),
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 16),
        itemCount: filters.length,
        itemBuilder: (context, index) {
          final filter = filters[index];
          final isSelected = _selectedRouteFilter == index;
          return Padding(
            padding: const EdgeInsets.only(right: 10),
            child: GestureDetector(
              onTap: () => _filterRoutes(index),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 16),
                decoration: BoxDecoration(
                  gradient: isSelected ? primaryGradient : null,
                  color: isSelected ? null : bgCard,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isSelected ? Colors.transparent : borderColor,
                  ),
                ),
                child: Row(
                  children: [
                    Icon(
                      filter["icon"] as IconData,
                      size: 18,
                      color: isSelected ? Colors.white : textGrey,
                    ),
                    const SizedBox(width: 8),
                    Text(
                      filter["label"] as String,
                      style: TextStyle(
                        fontSize: 13,
                        fontWeight: FontWeight.w500,
                        color: isSelected ? Colors.white : textGrey,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  Widget _buildSuggestedRouteCard(SuggestedRoute route) {
    return GestureDetector(
      onTap: () => _showRouteDetail(route),
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Column(
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
                    child: Image.network(
                      route.imageUrl,
                      fit: BoxFit.cover,
                      errorBuilder: (_, __, ___) => Container(
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [
                              route.accentColor,
                              route.accentColor.withOpacity(0.6),
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
                  child: Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: route.accentColor,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Icon(route.icon, color: Colors.white, size: 20),
                  ),
                ),
                Positioned(
                  top: 12,
                  right: 12,
                  child: Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 10,
                      vertical: 5,
                    ),
                    decoration: BoxDecoration(
                      color: Colors.black.withOpacity(0.5),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      route.difficulty,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
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
                        "${route.placeNames.length} durak",
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
                      color: textWhite,
                      fontSize: 18,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    route.description,
                    style: const TextStyle(
                      color: textGrey,
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
                              color: route.accentColor.withOpacity(0.15),
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Text(
                              tag,
                              style: TextStyle(
                                color: route.accentColor,
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
                              color: bgCardLight,
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: const Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(
                                  Icons.visibility,
                                  color: textGrey,
                                  size: 18,
                                ),
                                SizedBox(width: 8),
                                Text(
                                  "Detaylar",
                                  style: TextStyle(
                                    color: textGrey,
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
                        child: GestureDetector(
                          onTap: () => _applySuggestedRoute(route),
                          child: Container(
                            padding: const EdgeInsets.symmetric(vertical: 12),
                            decoration: BoxDecoration(
                              gradient: LinearGradient(
                                colors: [
                                  route.accentColor,
                                  route.accentColor.withOpacity(0.8),
                                ],
                              ),
                              borderRadius: BorderRadius.circular(12),
                            ),
                            child: const Row(
                              mainAxisAlignment: MainAxisAlignment.center,
                              children: [
                                Icon(Icons.add, color: Colors.white, size: 18),
                                SizedBox(width: 8),
                                Text(
                                  "Uygula",
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 13,
                                    fontWeight: FontWeight.w600,
                                  ),
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
          ],
        ),
      ),
    );
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
    final places = <Highlight>[];
    for (var name in route.placeNames) {
      final place = _city?.highlights.where((h) => h.name == name).firstOrNull;
      if (place != null) places.add(place);
    }

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
                    color: borderColor,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(20),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: route.accentColor,
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
                                color: textWhite,
                                fontSize: 20,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                            const SizedBox(height: 4),
                            Row(
                              children: [
                                const Icon(
                                  Icons.schedule,
                                  color: textGrey,
                                  size: 14,
                                ),
                                const SizedBox(width: 4),
                                Text(
                                  route.duration,
                                  style: const TextStyle(
                                    color: textGrey,
                                    fontSize: 13,
                                  ),
                                ),
                                const SizedBox(width: 12),
                                const Icon(
                                  Icons.straighten,
                                  color: textGrey,
                                  size: 14,
                                ),
                                const SizedBox(width: 4),
                                Text(
                                  route.distance,
                                  style: const TextStyle(
                                    color: textGrey,
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
                            color: bgCard,
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(
                            Icons.close,
                            color: textGrey,
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
                      color: textGrey,
                      fontSize: 14,
                      height: 1.5,
                    ),
                  ),
                ),
                const SizedBox(height: 20),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: Row(
                    children: [
                      const Text(
                        "Duraklar",
                        style: TextStyle(
                          color: textWhite,
                          fontSize: 16,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                      const Spacer(),
                      Text(
                        "${places.length} nokta",
                        style: const TextStyle(color: textGrey, fontSize: 13),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 12),
                Expanded(
                  child: ListView.builder(
                    controller: scrollController,
                    padding: const EdgeInsets.fromLTRB(20, 0, 20, 20),
                    itemCount: places.length,
                    itemBuilder: (context, index) => _buildStopCard(
                      places[index],
                      index,
                      places.length,
                      route.accentColor,
                    ),
                  ),
                ),
                Container(
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: bgCard,
                    border: Border(
                      top: BorderSide(color: borderColor.withOpacity(0.5)),
                    ),
                  ),
                  child: SafeArea(
                    child: GestureDetector(
                      onTap: () {
                        Navigator.pop(context);
                        _applySuggestedRoute(route);
                      },
                      child: Container(
                        width: double.infinity,
                        padding: const EdgeInsets.symmetric(vertical: 16),
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            colors: [
                              route.accentColor,
                              route.accentColor.withOpacity(0.8),
                            ],
                          ),
                          borderRadius: BorderRadius.circular(14),
                          boxShadow: [
                            BoxShadow(
                              color: route.accentColor.withOpacity(0.4),
                              blurRadius: 16,
                              offset: const Offset(0, 6),
                            ),
                          ],
                        ),
                        child: const Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(
                              Icons.add_circle_outline,
                              color: Colors.white,
                              size: 22,
                            ),
                            SizedBox(width: 10),
                            Text(
                              "Bu Rotayı Uygula",
                              style: TextStyle(
                                color: Colors.white,
                                fontSize: 16,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                          ],
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

  Widget _buildStopCard(
    Highlight place,
    int index,
    int total,
    Color accentColor,
  ) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final isLast = index == total - 1;

    return Column(
      children: [
        GestureDetector(
          onTap: () {
            Navigator.pop(context);
            Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
            );
          },
          child: Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: bgCard,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: borderColor.withOpacity(0.5)),
            ),
            child: Row(
              children: [
                Container(
                  width: 32,
                  height: 32,
                  decoration: BoxDecoration(
                    color: accentColor,
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Center(
                    child: Text(
                      "${index + 1}",
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 14,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                ClipRRect(
                  borderRadius: BorderRadius.circular(10),
                  child: SizedBox(
                    width: 50,
                    height: 50,
                    child: hasImage
                        ? Image.network(
                            place.imageUrl!,
                            fit: BoxFit.cover,
                            errorBuilder: (_, __, ___) => Container(
                              color: accentColor.withOpacity(0.2),
                              child: Icon(
                                Icons.place,
                                color: accentColor,
                                size: 24,
                              ),
                            ),
                          )
                        : Container(
                            color: accentColor.withOpacity(0.2),
                            child: Icon(
                              Icons.place,
                              color: accentColor,
                              size: 24,
                            ),
                          ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        place.name,
                        style: const TextStyle(
                          color: textWhite,
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                        ),
                        maxLines: 1,
                        overflow: TextOverflow.ellipsis,
                      ),
                      const SizedBox(height: 4),
                      Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 6,
                              vertical: 2,
                            ),
                            decoration: BoxDecoration(
                              color: accentColor.withOpacity(0.15),
                              borderRadius: BorderRadius.circular(4),
                            ),
                            child: Text(
                              place.category,
                              style: TextStyle(
                                color: accentColor,
                                fontSize: 10,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                          const SizedBox(width: 8),
                          Expanded(
                            child: Text(
                              place.area,
                              style: const TextStyle(
                                color: textGrey,
                                fontSize: 11,
                              ),
                              overflow: TextOverflow.ellipsis,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
                const Icon(Icons.chevron_right, color: textGrey, size: 20),
              ],
            ),
          ),
        ),
        if (!isLast)
          Padding(
            padding: const EdgeInsets.only(left: 30),
            child: Row(
              children: [
                Container(
                  width: 2,
                  height: 24,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      colors: [
                        accentColor.withOpacity(0.5),
                        accentColor.withOpacity(0.2),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
      ],
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
      color: const Color(0xFF0D0D1A), // bgDark
      child: child,
    );
  }

  @override
  bool shouldRebuild(_SliverAppBarDelegate oldDelegate) {
    return true;
  }
}
