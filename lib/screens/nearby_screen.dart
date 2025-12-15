
// =============================================================================
// NEARBY SCREEN v5 - DARK THEME + AMBER + HAİTA TOGGLE + ANİMASYONLAR
// =============================================================================

import 'dart:ui' as ui;
import 'dart:convert';
import '../services/trip_update_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import '../utils/map_theme.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import 'detail_screen.dart';

// Tema renkleri
const Color bgDark = Color(0xFF0D0D1A);
const Color bgCard = Color(0xFF1A1A2E);
const Color bgCardLight = Color(0xFF252542);
const Color accent = Color(0xFFF5A623);
const Color accentLight = Color(0xFFFFB800);
const Color textPrimary = Color(0xFFFFFFFF);
const Color textSecondary = Color(0xFFB0B0C0);
const Color textWhite = Color(0xFFFFFFFF);
const Color textGrey = Color(0xFF9E9E9E);
const Color accentGreen = Color(0xFF4CAF50);
const Color borderColor = Color(0xFF2C2C4E);

class NearbyScreen extends StatefulWidget {
  const NearbyScreen({super.key});

  @override
  State<NearbyScreen> createState() => _NearbyScreenState();
}

class _NearbyScreenState extends State<NearbyScreen>
    with TickerProviderStateMixin {
  List<_NearbyPlace> _allPlaces = [];
  List<_NearbyPlace> _filteredPlaces = [];
  bool _loading = true;
  String _selectedCity = "berlin";

  String _selectedCategory = "Tümü";
  String _selectedSort = "Mesafe";
  double _maxDistance = 5.0;

  List<String> _routePlaces = [];
  bool _showMap = false;

  late AnimationController _animController;
  late AnimationController _listAnimController;
  late Animation<double> _fadeAnim;

  // Harita değişkenleri
  GoogleMapController? _mapController;
  Set<Marker> _markers = {};
  String? _darkMapStyle;
  // Varsayılan kamera pozisyonu (Barcelona)
  static const CameraPosition _initialCameraPosition = CameraPosition(
    target: LatLng(41.3851, 2.1734),
    zoom: 13,
  );

  final List<Map<String, dynamic>> _categories = [
    {"name": "Tümü", "icon": Icons.apps_rounded},
    {"name": "Restoran", "icon": Icons.restaurant_rounded},
    {"name": "Kafe", "icon": Icons.local_cafe_rounded},
    {"name": "Bar", "icon": Icons.local_bar_rounded},
    {"name": "Müze", "icon": Icons.museum_rounded},
    {"name": "Park", "icon": Icons.park_rounded},
    {"name": "Tarihi", "icon": Icons.account_balance_rounded},
    {"name": "Mahalle", "icon": Icons.location_city_rounded},
  ];

  @override
  void initState() {
    super.initState();
    _setupAnimations();
    _loadMapStyle();
    _loadData();
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
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
    _selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    if (prefs.containsKey("trip_places")) {
      setState(() {
        _routePlaces = prefs.getStringList("trip_places") ?? [];
      });
    }
    await Future.delayed(const Duration(milliseconds: 300));

    // Gerçek şehir verisini yükle
    try {
      final cityData = await CityDataLoader.loadCity(_selectedCity);

      final places = cityData.highlights
          .map(
            (h) => _NearbyPlace(
              name: h.name,
              category: h.category,
              distanceKm: h.distanceFromCenter,
              rating: h.rating ?? 4.5,
              area: h.area,
              imageUrl: h.imageUrl,
              description: h.description,
              price: h.price,
              highlight: h,
            ),
          )
          .toList();

      if (mounted) {
        setState(() {
          _allPlaces = places;
          _filteredPlaces = List.from(places);
          _loading = false;
        });
        _animController.forward();
        _applyFilters();
      }
    } catch (e) {
      debugPrint("Yakınımda veri yükleme hatası: $e");
      if (mounted) {
        setState(() => _loading = false);
      }
    }
  }

  void _applyFilters() {
    if (_allPlaces.isEmpty) return;

    // Liste animasyonu
    _listAnimController.reset();

    List<_NearbyPlace> filtered = List.from(_allPlaces);

    if (_selectedCategory != "Tümü") {
      filtered = filtered
          .where((p) => p.category == _selectedCategory)
          .toList();
    }
    filtered = filtered.where((p) => p.distanceKm <= _maxDistance).toList();

    switch (_selectedSort) {
      case "Mesafe":
        filtered.sort((a, b) => a.distanceKm.compareTo(b.distanceKm));
        break;
      case "Puan":
        filtered.sort((a, b) => b.rating.compareTo(a.rating));
        break;
      case "İsim":
        filtered.sort((a, b) => a.name.compareTo(b.name));
        break;
    }

    setState(() => _filteredPlaces = filtered);
    _updateMarkers(); // Markerları güncelle
    _listAnimController.forward();
  }

  Future<void> _toggleRoute(String name) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    
    // 1. Güncel verileri oku
    final List<String> tripPlaces = prefs.getStringList("trip_places") ?? [];
    final String? scheduleJson = prefs.getString("trip_schedule");
    
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
        tripPlaces.remove(name);
        
        // Schedule'dan da sil
        scheduleMap.keys.forEach((day) {
             final List<dynamic> list = scheduleMap[day] ?? [];
             list.remove(name);
             scheduleMap[day] = list;
        });

        if (mounted) {
           ScaffoldMessenger.of(context).showSnackBar(SnackBar(
             content: Text("$name rotadan çıkarıldı."),
             backgroundColor: Colors.redAccent,
             behavior: SnackBarBehavior.floating,
             duration: const Duration(milliseconds: 1500),
          ));
        }
    } else {
        // EKLEME İŞLEMİ
        // Toplam gün sayısını bul
        int maxDay = 1;
        scheduleMap.keys.forEach((k) {
           final d = int.tryParse(k) ?? 1;
           if (d > maxDay) maxDay = d;
        });
        final onboardingDays = prefs.getInt("tripDays") ?? 3;
        if (maxDay < onboardingDays) maxDay = onboardingDays;

        final selectedDay = await _showDaySelectionDialogForNearby(maxDay, name);
        if (selectedDay == null) return; // İptal
        
        setState(() {
           _routePlaces.add(name);
        });
        
        tripPlaces.add(name);
        
        final dayKey = selectedDay.toString();
        List<dynamic> targetList = scheduleMap[dayKey] ?? [];
        if (!targetList.contains(name)) {
           targetList.add(name);
        }
        scheduleMap[dayKey] = targetList;
        
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(SnackBar(
             content: Text("$name, $selectedDay. güne eklendi!"),
             backgroundColor: Colors.green,
             behavior: SnackBarBehavior.floating,
             duration: const Duration(milliseconds: 1500),
          ));
        }
    }

    await prefs.setStringList("trip_places", tripPlaces); // Key düzeltildi
    await prefs.setString("trip_schedule", jsonEncode(scheduleMap));
    
    // Global servisi tetikle (RoutesScreen güncellensin)
    TripUpdateService().notifyTripChanged();
  }
  
  Future<int?> _showDaySelectionDialogForNearby(int totalDays, String placeName) async {
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
                const Text("Hangi Güne Eklensin?", style: TextStyle(color: textWhite, fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                Text("'$placeName' rotaya eklensin mi?", textAlign: TextAlign.center, style: const TextStyle(color: textGrey, fontSize: 14)),
                const SizedBox(height: 20),
                ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 400),
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                         ...List.generate(totalDays, (index) {
                             final day = index + 1;
                             return ListTile(
                               title: Text("Gün $day", style: const TextStyle(color: textWhite)),
                               trailing: const Icon(Icons.add_circle_outline, color: accent),
                               onTap: () => Navigator.pop(context, day),
                             );
                         }),
                         const Divider(color: borderColor),
                         ListTile(
                             title: const Text("Yeni Gün Oluştur", style: TextStyle(color: textWhite)),
                             subtitle: Text("Gün ${totalDays + 1}", style: const TextStyle(color: textGrey, fontSize: 12)),
                             leading: const Icon(Icons.add, color: accentGreen),
                             onTap: () => Navigator.pop(context, totalDays + 1),
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



  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    _animController.dispose();
    _listAnimController.dispose();
    super.dispose();
  }
  
  void _onTripDataChanged() {
      _refreshRouteState();
  }
  
  Future<void> _refreshRouteState() async {
     final prefs = await SharedPreferences.getInstance();
     if (prefs.containsKey("trip_places")) {
       final newList = prefs.getStringList("trip_places") ?? [];
       if (mounted) {
         setState(() {
           _routePlaces = newList;
         });
       }
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
      case "Mahalle":
        return const Color(0xFF00CEC9);
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
      case "Mahalle":
        return Icons.location_city_rounded;
      case "Alışveriş":
        return Icons.shopping_bag_rounded;
      default:
        return Icons.place_rounded;
    }
  }

  String _getCityDisplayName(String cityId) {
    final names = {
      'istanbul': 'İstanbul',
      'barcelona': 'Barcelona',
      'paris': 'Paris',
      'roma': 'Roma',
      'berlin': 'Berlin',
      'londra': 'Londra',
      'amsterdam': 'Amsterdam',
      'tokyo': 'Tokyo',
    };
    return names[cityId] ?? cityId;
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
              child: Column(
                children: [
                  _buildHeader(),
                  _buildLocationCard(),
                  _buildDistanceSlider(),
                  _buildCategories(),
                  Expanded(
                    child: _showMap ? _buildMapView() : _buildPlacesList(),
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
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [accent, accentLight],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(14),
              ),
              child: const Icon(
                Icons.near_me_rounded,
                color: Colors.white,
                size: 24,
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    "Yakınımda",
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
                child: Icon(
                  _showMap ? Icons.list_rounded : Icons.map_rounded,
                  color: _showMap ? Colors.white : textSecondary,
                  size: 22,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLocationCard() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.white.withOpacity(0.05)),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: const Color(0xFF00B894).withOpacity(0.15),
                borderRadius: BorderRadius.circular(12),
              ),
              child: const Icon(
                Icons.my_location_rounded,
                color: Color(0xFF00B894),
                size: 22,
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Text(
                    "Şehir merkezi baz alınıyor",
                    style: TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w600,
                      color: textPrimary,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    "${_filteredPlaces.length} yer bulundu",
                    style: const TextStyle(fontSize: 13, color: textSecondary),
                  ),
                ],
              ),
            ),
            GestureDetector(
              onTap: () {
                HapticFeedback.lightImpact();
                _loadData();
              },
              child: Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: bgCardLight,
                  borderRadius: BorderRadius.circular(10),
                ),
                child: const Icon(
                  Icons.refresh_rounded,
                  color: textSecondary,
                  size: 20,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDistanceSlider() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                "Maksimum Mesafe",
                style: TextStyle(fontSize: 14, color: textSecondary),
              ),
              Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 12,
                  vertical: 6,
                ),
                decoration: BoxDecoration(
                  color: accent.withOpacity(0.15),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Text(
                  "${_maxDistance.toStringAsFixed(1)} km",
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w700,
                    color: accent,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
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
              value: _maxDistance,
              min: 0.5,
              max: 10,
              onChanged: (val) {
                setState(() => _maxDistance = val);
              },
              onChangeEnd: (val) {
                _applyFilters();
              },
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
            final isSelected = _selectedCategory == cat["name"];

            return GestureDetector(
              onTap: () {
                HapticFeedback.selectionClick();
                setState(() => _selectedCategory = cat["name"]);
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
          initialCameraPosition: _initialCameraPosition,
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
        position: LatLng(place.highlight.lat ?? 0, place.highlight.lng ?? 0),
        infoWindow: InfoWindow(
          title: place.name,
          snippet: place.category,
          onTap: () {
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
      final lat = place.highlight.lat ?? 0;
      final lng = place.highlight.lng ?? 0;
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
    switch (category) {
      case "Park": return BitmapDescriptor.hueGreen;
      case "Restoran": return BitmapDescriptor.hueRed;
      case "Kafe": return BitmapDescriptor.hueOrange;
      case "Müze": return BitmapDescriptor.hueAzure;
      case "Tarihi": return BitmapDescriptor.hueRose;
      case "Bar": return BitmapDescriptor.hueViolet;
      default: return BitmapDescriptor.hueYellow;
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
                    color: _getCategoryColor(place.category),
                    borderRadius: BorderRadius.circular(14),
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
                        place.name,
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                        ),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        place.area,
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
                    color: accent.withOpacity(0.15),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.star_rounded, size: 16, color: accent),
                      const SizedBox(width: 4),
                      Text(
                        place.rating.toString(),
                        style: TextStyle(
                          fontSize: 14,
                          fontWeight: FontWeight.w700,
                          color: accent,
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
                      _toggleRoute(place.name);
                    },
                    child: Container(
                      padding: const EdgeInsets.symmetric(vertical: 14),
                      decoration: BoxDecoration(
                        color: _routePlaces.contains(place.name)
                            ? Colors.green.shade600
                            : accent,
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            _routePlaces.contains(place.name)
                                ? Icons.check_circle
                                : Icons.add_rounded,
                            color: Colors.white,
                            size: 20,
                          ),
                          const SizedBox(width: 8),
                          Text(
                            _routePlaces.contains(place.name)
                                ? "Eklendi ✓"
                                : "Rotaya Ekle",
                            style: const TextStyle(
                              fontSize: 15,
                              fontWeight: FontWeight.w600,
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
                      child: place.imageUrl != null
                          ? Image.network(
                              place.imageUrl!,
                              height: 200,
                              width: double.infinity,
                              fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) =>
                                  _buildPlaceholderImage(color, icon),
                            )
                          : _buildPlaceholderImage(color, icon),
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
                            color: color.withOpacity(0.15),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(icon, size: 16, color: color),
                              const SizedBox(width: 6),
                              Text(
                                place.category,
                                style: TextStyle(
                                  fontSize: 13,
                                  fontWeight: FontWeight.w600,
                                  color: color,
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
                            color: accent.withOpacity(0.15),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Row(
                            children: [
                              Icon(Icons.star_rounded, size: 16, color: accent),
                              const SizedBox(width: 4),
                              Text(
                                place.rating.toStringAsFixed(1),
                                style: TextStyle(
                                  fontSize: 14,
                                  fontWeight: FontWeight.w700,
                                  color: accent,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 16),

                    // İsim
                    Text(
                      place.name,
                      style: const TextStyle(
                        fontSize: 26,
                        fontWeight: FontWeight.w700,
                        color: textPrimary,
                        letterSpacing: -0.5,
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
                          place.area,
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
                      const Text(
                        "Hakkında",
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                          color: textPrimary,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        place.description!,
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
                              _toggleRoute(place.name);
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
                                    ? bgCardLight
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
                                        : "Rotaya Ekle",
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
        gradient: LinearGradient(
          colors: [color, color.withOpacity(0.7)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
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
            const Text(
              "Bu kriterlere uygun mekan bulunamadı",
              style: TextStyle(fontSize: 16, color: textSecondary),
            ),
            const SizedBox(height: 12),
            GestureDetector(
              onTap: () {
                setState(() {
                  _selectedCategory = "Tümü";
                  _maxDistance = 5.0;
                });
                _applyFilters();
              },
              child: Text(
                "Filtreleri temizle",
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
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 100),
      itemCount: _filteredPlaces.length,
      itemBuilder: (context, index) {
        final place = _filteredPlaces[index];
        final color = _getCategoryColor(place.category);
        final icon = _getCategoryIcon(place.category);

        return _buildPlaceCard(place, color, icon);
      },
    );
  }

  Widget _buildPlaceCard(_NearbyPlace place, Color color, IconData icon) {
    final isInRoute = _routePlaces.contains(place.name);

    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (_) => DetailScreen(place: place.highlight),
          ),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white.withOpacity(0.05)),
        ),
        child: Row(
          children: [
            // Fotoğraf alanı
            Container(
              width: 110,
              height: 130,
              decoration: BoxDecoration(
                borderRadius: const BorderRadius.horizontal(
                  left: Radius.circular(20),
                ),
                image: place.imageUrl != null
                    ? DecorationImage(
                        image: NetworkImage(place.imageUrl!),
                        fit: BoxFit.cover,
                      )
                    : null,
              ),
              child: place.imageUrl == null
                  ? Container(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [color, color.withOpacity(0.7)],
                          begin: Alignment.topLeft,
                          end: Alignment.bottomRight,
                        ),
                        borderRadius: const BorderRadius.horizontal(
                          left: Radius.circular(20),
                        ),
                      ),
                      child: Center(
                        child: Icon(
                          icon,
                          size: 40,
                          color: Colors.white.withOpacity(0.9),
                        ),
                      ),
                    )
                  : Stack(
                      children: [
                        // Gradient overlay
                        Positioned.fill(
                          child: Container(
                            decoration: BoxDecoration(
                              borderRadius: const BorderRadius.horizontal(
                                left: Radius.circular(20),
                              ),
                              gradient: LinearGradient(
                                begin: Alignment.topCenter,
                                end: Alignment.bottomCenter,
                                colors: [
                                  Colors.transparent,
                                  Colors.black.withOpacity(0.5),
                                ],
                              ),
                            ),
                          ),
                        ),
                        // Mesafe badge
                        Positioned(
                          bottom: 10,
                          left: 10,
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
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Icon(
                                  Icons.directions_walk_rounded,
                                  size: 12,
                                  color: accent,
                                ),
                                const SizedBox(width: 4),
                                Text(
                                  "${place.distanceKm} km",
                                  style: const TextStyle(
                                    fontSize: 11,
                                    fontWeight: FontWeight.w600,
                                    color: Colors.white,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
            ),

            // İçerik
            Expanded(
              child: Padding(
                padding: const EdgeInsets.all(14),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 8,
                            vertical: 4,
                          ),
                          decoration: BoxDecoration(
                            color: color.withOpacity(0.15),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            place.category,
                            style: TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              color: color,
                            ),
                          ),
                        ),
                        const Spacer(),
                        Icon(Icons.star_rounded, size: 16, color: accent),
                        const SizedBox(width: 4),
                        Text(
                          place.rating.toStringAsFixed(1),
                          style: const TextStyle(
                            fontSize: 13,
                            fontWeight: FontWeight.w700,
                            color: textPrimary,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 10),
                    Text(
                      place.name,
                      style: const TextStyle(
                        fontSize: 17,
                        fontWeight: FontWeight.w700,
                        color: textPrimary,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    const SizedBox(height: 4),
                    Text(
                      place.area,
                      style: const TextStyle(
                        fontSize: 13,
                        color: textSecondary,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    const SizedBox(height: 12),
                    Row(
                      children: [
                        // Favori butonu
                        Container(
                          padding: const EdgeInsets.all(8),
                          decoration: BoxDecoration(
                            color: bgCardLight,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Icon(
                            Icons.favorite_border_rounded,
                            size: 18,
                            color: textSecondary,
                          ),
                        ),
                        const SizedBox(width: 10),
                            // Rotaya ekle butonu
                        Expanded(
                          child: GestureDetector(
                            onTap: () => _toggleRoute(place.name),
                            child: Container(
                              padding: const EdgeInsets.symmetric(vertical: 10),
                              decoration: BoxDecoration(
                                gradient: isInRoute
                                    ? null
                                    : LinearGradient(
                                        colors: [accent, accentLight],
                                        begin: Alignment.centerLeft,
                                        end: Alignment.centerRight,
                                      ),
                                color: isInRoute ? Colors.green : null,
                                borderRadius: BorderRadius.circular(10),
                              ),
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.center,
                                children: [
                                  Icon(
                                    isInRoute
                                        ? Icons.check
                                        : Icons.add_rounded,
                                    size: 18,
                                    color: Colors.white,
                                  ),
                                  const SizedBox(width: 6),
                                  Text(
                                    isInRoute ? "Eklendi ✓" : "Rotaya Ekle",
                                    style: const TextStyle(
                                      fontSize: 13,
                                      fontWeight: FontWeight.w600,
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
                  ],
                ),
              ),
            ),
          ],
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
  final double distanceKm;
  final double rating;
  final String area;
  final String? imageUrl;
  final String? description;
  final String? price;
  final Highlight highlight; // Original highlight for detail screen

  _NearbyPlace({
    required this.name,
    required this.category,
    required this.distanceKm,
    required this.rating,
    required this.area,
    this.imageUrl,
    this.description,
    this.price,
    required this.highlight,
  });
}
