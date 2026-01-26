// =============================================================================
// BADGE SERVICE – City Icon Badges
// Simple icon-based badge system with unlock tracking
// =============================================================================

import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Represents a city badge with icon or image
class CityBadge {
  final String id;
  final String name;
  final String subtitle;
  final IconData? icon;
  final Color color;
  final String? imagePath; // Custom image path for badge
  bool isUnlocked;

  CityBadge({
    required this.id,
    required this.name,
    required this.subtitle,
    this.icon,
    required this.color,
    this.imagePath,
    this.isUnlocked = false,
  });

  bool get hasImage => imagePath != null && imagePath!.isNotEmpty;
}


/// Service to manage city badges
class BadgeService {
  static final BadgeService _instance = BadgeService._internal();
  factory BadgeService() => _instance;
  BadgeService._internal();

  final ValueNotifier<int> badgesNotifier = ValueNotifier(0);
  
  List<CityBadge> _badges = [];
  Set<String> _visitedCityIds = {};

  double _totalDistanceKm = 0.0;
  
  List<CityBadge> get badges => _badges;
  int get unlockedCount => _badges.where((b) => b.isUnlocked).length;
  int get totalCount => _badges.length;
  double get totalDistanceKm => _totalDistanceKm;

  /// Initialize the badge service
  Future<void> initialize() async {
    _createBadges();
    await _loadData();
    _updateUnlockedStatus();
  }

  /// Sync with visited places
  Future<void> syncVisits() async {
    await _loadData();
    _updateUnlockedStatus();
    badgesNotifier.value++;
  }
  
  /// Add distance to total
  Future<void> addDistance(double km) async {
    _totalDistanceKm += km;
    final prefs = await SharedPreferences.getInstance();
    await prefs.setDouble('total_distance_km', _totalDistanceKm);
    badgesNotifier.value++;
  }
  
  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();
    _totalDistanceKm = prefs.getDouble('total_distance_km') ?? 0.0;
    
    // Load visited cities
    final visitedPlaces = prefs.getStringList('visited_places') ?? [];
    
    _visitedCityIds.clear();
    for (final visit in visitedPlaces) {
      if (visit.contains(':')) {
        _visitedCityIds.add(visit.split(':')[0].toLowerCase());
      }
    }
    
    // Also check selectedCity
    final selectedCity = prefs.getString('selectedCity');
    if (selectedCity != null) {
      _visitedCityIds.add(selectedCity.toLowerCase());
    }
  }

  /// Create all city badges with icons
  void _createBadges() {
    _badges = [
      CityBadge(id: 'amsterdam', name: 'Amsterdam', subtitle: 'Canals', imagePath: 'assets/badges/amsterdam.png', color: const Color(0xFFF4C430)),

      CityBadge(id: 'antalya', name: 'Antalya', subtitle: 'Mediterranean', icon: Icons.beach_access, color: const Color(0xFF00CED1)),
      CityBadge(id: 'atina', name: 'Atina', subtitle: 'Parthenon', icon: Icons.account_balance, color: const Color(0xFF87CEEB)),
      CityBadge(id: 'bangkok', name: 'Bangkok', subtitle: 'Temple', icon: Icons.temple_buddhist, color: const Color(0xFFFF69B4)),
      CityBadge(id: 'barcelona', name: 'Barcelona', subtitle: 'Sagrada Familia', icon: Icons.church, color: const Color(0xFFADD8E6)),
      CityBadge(id: 'belgrad', name: 'Belgrad', subtitle: 'Fortress', icon: Icons.fort, color: const Color(0xFFDC143C)),
      CityBadge(id: 'berlin', name: 'Berlin', subtitle: 'Brandenburg Gate', icon: Icons.account_balance, color: const Color(0xFF2F4F4F)),
      CityBadge(id: 'bologna', name: 'Bologna', subtitle: 'Towers', icon: Icons.location_city, color: const Color(0xFFD2691E)),
      CityBadge(id: 'brugge', name: 'Brugge', subtitle: 'Medieval Town', icon: Icons.home, color: const Color(0xFF8B4513)),
      CityBadge(id: 'bruksel', name: 'Brüksel', subtitle: 'Atomium', icon: Icons.science, color: const Color(0xFF9370DB)),
      CityBadge(id: 'budapeste', name: 'Budapeşte', subtitle: 'Parliament', icon: Icons.account_balance, color: const Color(0xFF228B22)),
      CityBadge(id: 'cenevre', name: 'Cenevre', subtitle: "Jet d'Eau", icon: Icons.water, color: const Color(0xFF1E90FF)),
      CityBadge(id: 'colmar', name: 'Colmar', subtitle: 'Half-Timbered', icon: Icons.home, color: const Color(0xFFFF6347)),
      CityBadge(id: 'dubai', name: 'Dubai', subtitle: 'Burj Khalifa', icon: Icons.business, color: const Color(0xFF7B68EE)),
      CityBadge(id: 'dublin', name: 'Dublin', subtitle: 'Georgian', icon: Icons.home, color: const Color(0xFF008080)),
      CityBadge(id: 'edinburgh', name: 'Edinburgh', subtitle: 'Castle', icon: Icons.castle, color: const Color(0xFF483D8B)),
      CityBadge(id: 'fes', name: 'Fes', subtitle: 'Medina', icon: Icons.store, color: const Color(0xFFD2691E)),
      CityBadge(id: 'floransa', name: 'Floransa', subtitle: 'Duomo', icon: Icons.church, color: const Color(0xFFFF4500)),
      CityBadge(id: 'gaziantep', name: 'Gaziantep', subtitle: 'Castle', icon: Icons.castle, color: const Color(0xFFA52A2A)),
      CityBadge(id: 'giethoorn', name: 'Giethoorn', subtitle: 'Water Village', icon: Icons.houseboat, color: const Color(0xFF3CB371)),
      CityBadge(id: 'hallstatt', name: 'Hallstatt', subtitle: 'Alpine Lake', icon: Icons.landscape, color: const Color(0xFF4682B4)),
      CityBadge(id: 'heidelberg', name: 'Heidelberg', subtitle: 'Castle', icon: Icons.castle, color: const Color(0xFFD2691E)),
      CityBadge(id: 'hongkong', name: 'Hong Kong', subtitle: 'Skyline', icon: Icons.location_city, color: const Color(0xFFFF6347)),
      CityBadge(id: 'istanbul', name: 'İstanbul', subtitle: 'Mosque', icon: Icons.mosque, color: const Color(0xFF32CD32)),
      CityBadge(id: 'kahire', name: 'Kahire', subtitle: 'Pyramids', icon: Icons.change_history, color: const Color(0xFFDAA520)),
      CityBadge(id: 'kapadokya', name: 'Kapadokya', subtitle: 'Balloons', icon: Icons.airplanemode_active, color: const Color(0xFFFF7F50)),
      CityBadge(id: 'kopenhag', name: 'Kopenhag', subtitle: 'Harbor', icon: Icons.anchor, color: const Color(0xFF4169E1)),
      CityBadge(id: 'kotor', name: 'Kotor', subtitle: 'Bay', icon: Icons.landscape, color: const Color(0xFF008B8B)),
      CityBadge(id: 'lizbon', name: 'Lizbon', subtitle: 'Tile Buildings', icon: Icons.home, color: const Color(0xFFFFA500)),
      CityBadge(id: 'londra', name: 'Londra', subtitle: 'Big Ben', icon: Icons.access_time, color: const Color(0xFF87CEEB)),
      CityBadge(id: 'lucerne', name: 'Lucerne', subtitle: 'Mountains', icon: Icons.terrain, color: const Color(0xFF4682B4)),
      CityBadge(id: 'lyon', name: 'Lyon', subtitle: 'Old Town', icon: Icons.home, color: const Color(0xFFCD5C5C)),
      CityBadge(id: 'madrid', name: 'Madrid', subtitle: 'Royal Palace', icon: Icons.account_balance, color: const Color(0xFFD2691E)),
      CityBadge(id: 'marakes', name: 'Marakeş', subtitle: 'Minaret', icon: Icons.mosque, color: const Color(0xFFFF8C00)),
      CityBadge(id: 'marsilya', name: 'Marsilya', subtitle: 'Port', icon: Icons.anchor, color: const Color(0xFF4682B4)),
      CityBadge(id: 'matera', name: 'Matera', subtitle: 'Sassi', icon: Icons.home, color: const Color(0xFFDAA520)),

      CityBadge(id: 'milano', name: 'Milano', subtitle: 'Duomo', icon: Icons.church, color: const Color(0xFFFF6347)),
      CityBadge(id: 'napoli', name: 'Napoli', subtitle: 'Vesuvius', icon: Icons.volcano, color: const Color(0xFFD2691E)),
      CityBadge(id: 'newyork', name: 'New York', subtitle: 'Skyline', icon: Icons.location_city, color: const Color(0xFF00CED1)),
      CityBadge(id: 'nice', name: 'Nice', subtitle: 'Riviera', icon: Icons.beach_access, color: const Color(0xFF1E90FF)),
      CityBadge(id: 'oslo', name: 'Oslo', subtitle: 'Fjord', icon: Icons.landscape, color: const Color(0xFF2F4F4F)),
      CityBadge(id: 'paris', name: 'Paris', subtitle: 'Eiffel Tower', icon: Icons.architecture, color: const Color(0xFFFF69B4)),
      CityBadge(id: 'porto', name: 'Porto', subtitle: 'Riverside', icon: Icons.water, color: const Color(0xFF4169E1)),
      CityBadge(id: 'prag', name: 'Prag', subtitle: 'Castle', icon: Icons.castle, color: const Color(0xFFD2691E)),
      CityBadge(id: 'roma', name: 'Roma', subtitle: 'Colosseum', icon: Icons.stadium, color: const Color(0xFFFA8072)),
      CityBadge(id: 'rovaniemi', name: 'Rovaniemi', subtitle: 'Lapland', icon: Icons.ac_unit, color: const Color(0xFF87CEEB)),
      CityBadge(id: 'sansebastian', name: 'San Sebastian', subtitle: 'Beach', icon: Icons.beach_access, color: const Color(0xFF00CED1)),
      // Additional cities
      CityBadge(id: 'seul', name: 'Seul', subtitle: 'Palace', icon: Icons.account_balance, color: const Color(0xFFE91E63)),
      CityBadge(id: 'singapur', name: 'Singapur', subtitle: 'Marina Bay', icon: Icons.location_city, color: const Color(0xFF9B59B6)),
      CityBadge(id: 'stockholm', name: 'Stockholm', subtitle: 'Old Town', icon: Icons.home, color: const Color(0xFF2980B9)),
      CityBadge(id: 'tokyo', name: 'Tokyo', subtitle: 'Tower', icon: Icons.cell_tower, color: const Color(0xFFE84A5F)),
      CityBadge(id: 'venedik', name: 'Venedik', subtitle: 'Gondola', icon: Icons.directions_boat, color: const Color(0xFF3498DB)),
      CityBadge(id: 'viyana', name: 'Viyana', subtitle: 'Opera', icon: Icons.theater_comedy, color: const Color(0xFFE6B422)),
      CityBadge(id: 'zurih', name: 'Zürih', subtitle: 'Lake', icon: Icons.water, color: const Color(0xFF2980B9)),
    ];
  }

  /// Load visited cities from SharedPreferences
  Future<void> _loadVisitedCities() async {
    final prefs = await SharedPreferences.getInstance();
    final visitedPlaces = prefs.getStringList('visited_places') ?? [];
    
    _visitedCityIds.clear();
    for (final visit in visitedPlaces) {
      if (visit.contains(':')) {
        _visitedCityIds.add(visit.split(':')[0].toLowerCase());
      }
    }
    
    // Also check selectedCity
    final selectedCity = prefs.getString('selectedCity');
    if (selectedCity != null) {
      _visitedCityIds.add(selectedCity.toLowerCase());
    }
  }

  /// Update unlocked status based on visited cities
  void _updateUnlockedStatus() {
    for (final badge in _badges) {
      if (_visitedCityIds.contains(badge.id)) {
        badge.isUnlocked = true;
      }
    }
  }
}
