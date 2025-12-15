// =============================================================================
// EXPLORE SCREEN – WANDERLUST DARK THEME
// Dark background, purple/pink gradients, glassmorphism, hero city image
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:ui';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/ai_service.dart';
import 'detail_screen.dart';
import 'dart:convert';
import '../services/trip_update_service.dart';
import 'city_switcher_screen.dart';

class ExploreScreen extends StatefulWidget {
  const ExploreScreen({super.key});

  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen>
    with TickerProviderStateMixin {
  // ══════════════════════════════════════════════════════════════════════════
  // RENK PALETİ - AMBER/GOLD THEME
  // ══════════════════════════════════════════════════════════════════════════

  static const Color bgDark = Color(0xFF0D0D1A);
  static const Color bgCard = Color(0xFF1A1A2E);
  static const Color bgCardLight = Color(0xFF252542);
  static const Color accent = Color(0xFFF5A623); // Amber
  static const Color accentLight = Color(0xFFFFB800); // Gold
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);
  static const Color accentGreen = Color(0xFF4CAF50);

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFF5A623), Color(0xFFFFB800)],
  );

  static const LinearGradient primaryGradientDark = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFE09000), Color(0xFFF5A623)],
  );

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  CityModel? _city;
  bool _loading = true;
  bool _aiLoading = false;
  String? _error;
  String _userName = "Gezgin";
  String _currentCityId = ""; // Mevcut şehir ID'si

  List<Highlight> _allHighlights = [];
  List<Highlight> _filteredHighlights = [];
  List<Highlight> _aiRecommendations = [];
  String? _aiChatResponse; // Kişiselleştirilmiş AI yanıtı
  bool _aiCardExpanded = true; // AI kartı açık/kapalı

  // Şehir bazlı AI yanıt cache'i
  final Map<String, String> _aiChatCache = {};

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

  // Şehir görselleri - 18 şehir
  final Map<String, String> _cityImages = {
    'istanbul':
        'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800',
    'barcelona':
        'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800',
    'madrid':
        'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800',
    'sevilla':
        'https://images.pexels.com/photos/16487643/pexels-photo-16487643.jpeg?w=800',
    'paris':
        'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800',
    'roma': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800',
    'milano': 'https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800',
    'amsterdam':
        'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800',
    'londra':
        'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800',
    'berlin': 'https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800',
    'viyana':
        'https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800',
    'prag':
        'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=800',
    'lizbon':
        'https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800',
    'tokyo':
        'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800',
    'seul':
        'https://images.unsplash.com/photo-1538485399081-7191377e8241?w=800',
    'singapur':
        'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800',
    'dubai':
        'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800',
    'newyork':
        'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800',
  };

  final List<Map<String, dynamic>> _categories = const [
    {"id": "Tümü", "label": "Tümü"},
    {"id": "Restoran", "label": "Restoran"},
    {"id": "Kafe", "label": "Kafe"},
    {"id": "Müze", "label": "Müze"},
    {"id": "Park", "label": "Park"},
    {"id": "Bar", "label": "Bar"},
    {"id": "Tarihi", "label": "Tarihi"},
    {"id": "Manzara", "label": "Manzara"},
  ];

  final List<Map<String, dynamic>> _moods = const [
    {"id": 0, "label": "Sakin"},
    {"id": 1, "label": "Keşif"},
    {"id": 2, "label": "Popüler"},
  ];

  // ══════════════════════════════════════════════════════════════════════════
  // LIFECYCLE
  // ══════════════════════════════════════════════════════════════════════════

  @override
  void initState() {
    super.initState();
    _loadData();
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
  }

  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    _searchController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  void _onTripDataChanged() {
    _loadData();
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DATA LOADING
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _loadData() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      _favorites = prefs.getStringList("favorite_places") ?? [];
      _tripPlaces = prefs.getStringList("trip_places") ?? [];
      _userName = prefs.getString("userName") ?? "Gezgin";

      // Onboarding verilerini yükle
      _travelStyle = prefs.getString("travelStyle") ?? "Lokal";
      _interests = prefs.getStringList("interests") ?? [];
      _budgetLevel = prefs.getString("budgetLevel") ?? "Dengeli";
      _tripDays = prefs.getInt("tripDays") ?? 3;
      _transportMode = prefs.getString("transportMode") ?? "Karışık";

      final selectedCity = prefs.getString("selectedCity") ?? "barcelona";
      final normalizedCity = selectedCity.toLowerCase();
      final city = await CityDataLoader.loadCity(normalizedCity);

      // Şehir değişti mi kontrol et
      final cityChanged = _currentCityId != normalizedCity;

      if (!mounted) return;

      setState(() {
        _city = city;
        _currentCityId = normalizedCity;
        _allHighlights = city.highlights;
        _filteredHighlights = List.from(_allHighlights);
        _loading = false;

        // Şehir değiştiyse: cache'te varsa göster, yoksa sıfırla
        if (cityChanged) {
          if (_aiChatCache.containsKey(normalizedCity)) {
            // Bu şehir için daha önce tavsiye alınmış, cache'ten getir
            _aiChatResponse = _aiChatCache[normalizedCity];
            _aiCardExpanded = false; // Kapalı göster, kullanıcı açabilir
          } else {
            // Yeni şehir, tavsiye yok - Tavsiye İste butonu görünsün
            _aiChatResponse = null;
            _aiCardExpanded = true;
          }
        }
      });

      _fetchAIRecommendations();
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _error = e.toString();
        _loading = false;
      });
    }
  }

  void _applyFilters() {
    var filtered = List<Highlight>.from(_allHighlights);

    if (_selectedCategory != "Tümü") {
      filtered = filtered
          .where((h) => h.category == _selectedCategory)
          .toList();
    }

    if (_searchQuery.isNotEmpty) {
      final query = _searchQuery.toLowerCase();
      filtered = filtered.where((h) {
        return h.name.toLowerCase().contains(query) ||
            h.area.toLowerCase().contains(query) ||
            h.category.toLowerCase().contains(query) ||
            h.tags.any((tag) => tag.toLowerCase().contains(query));
      }).toList();
    }

    // Mood'a göre sırala
    if (_selectedMood == 0) {
      // Sakin - parklar, müzeler önce
      filtered.sort((a, b) {
        final aScore = (a.category == 'Park' || a.category == 'Manzara')
            ? 0
            : 1;
        final bScore = (b.category == 'Park' || b.category == 'Manzara')
            ? 0
            : 1;
        return aScore.compareTo(bScore);
      });
    } else if (_selectedMood == 2) {
      // Popüler - rating'e göre
      filtered.sort((a, b) => (b.rating ?? 0).compareTo(a.rating ?? 0));
    }

    setState(() => _filteredHighlights = filtered);
  }

  // Otomatik çağrılan - sadece mekan önerileri için, AI chat yanıtı ALMAZ
  Future<void> _fetchAIRecommendations() async {
    if (_city == null) return;

    try {
      // Mood bazlı mekan önerilerini al (chat yanıtı değil)
      final recs = await AIService.getSerendipityRecommendations(
        city: _city!.city,
        travelStyle: _travelStyle,
        interests: _interests,
        moodLevel: _selectedMood / 2.0,
      );

      if (!mounted) return;
      setState(() {
        _aiRecommendations = recs;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _aiRecommendations = _allHighlights.take(4).toList();
      });
    }
  }

  // Kullanıcı "Tavsiye İste" butonuna basınca çağrılır
  Future<void> _fetchAIChatResponse() async {
    if (_city == null) return;
    setState(() {
      _aiLoading = true;
    });

    try {
      // Kişiselleştirilmiş AI chat yanıtını al
      final chatResponse = await AIService.getPersonalizedChatResponse(
        city: _city!.city,
        userName: _userName,
        travelStyle: _travelStyle,
        interests: _interests,
        budgetLevel: _budgetLevel,
        tripDays: _tripDays,
        transportMode: _transportMode,
      );

      if (!mounted) return;
      setState(() {
        _aiChatResponse = chatResponse;
        _aiLoading = false;
        _aiCardExpanded = true;

        // Cache'e kaydet
        _aiChatCache[_currentCityId] = chatResponse;
      });
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _aiLoading = false;
      });
    }
  }

  Future<void> _toggleFavorite(String name) async {
    HapticFeedback.lightImpact();
    final prefs = await SharedPreferences.getInstance();

    setState(() {
      if (_favorites.contains(name)) {
        _favorites.remove(name);
      } else {
        _favorites.add(name);
      }
    });

    await prefs.setStringList("favorite_places", _favorites);
  }

  Future<void> _addToTrip(String name) async {
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

    final bool alreadyInTrip = _tripPlaces.contains(name);

    if (alreadyInTrip) {
        // ÇIKARMA İŞLEMİ
        setState(() {
          _tripPlaces.remove(name);
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

         final selectedDay = await _showDaySelectionDialogForExplore(maxDay, name);
         if (selectedDay == null) return; // İptal
         
         setState(() {
           _tripPlaces.add(name);
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

    await prefs.setStringList("trip_places", tripPlaces);
    await prefs.setString("trip_schedule", jsonEncode(scheduleMap));
    
    // Global bildirim
    TripUpdateService().notifyTripChanged();
  }

  Future<int?> _showDaySelectionDialogForExplore(int totalDays, String placeName) async {
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

  String _getGreeting() {
    final hour = DateTime.now().hour;
    if (hour < 12) return "Günaydın";
    if (hour < 18) return "Merhaba";
    return "İyi akşamlar";
  }

  String _getMoodText() {
    switch (_selectedMood) {
      case 0:
        return "Bugün sakin bir gün geçireceksin.";
      case 1:
        return "Bugün keşif modundasın.";
      case 2:
        return "Bugün popüler yerleri keşfedeceksin.";
      default:
        return "Bugün keşif modundasın.";
    }
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
                child: const Icon(Icons.explore, color: Colors.white, size: 32),
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
              Text("Veri yüklenemedi", style: TextStyle(color: textGrey)),
              const SizedBox(height: 16),
              _buildGradientButton("Tekrar Dene", () {
                setState(() => _loading = true);
                _loadData();
              }),
            ],
          ),
        ),
      );
    }

    return Scaffold(
      backgroundColor: bgDark,
      body: Stack(
        children: [
          // Ana içerik
          CustomScrollView(
            controller: _scrollController,
            physics: const BouncingScrollPhysics(),
            slivers: [
              // Hero Section
              SliverToBoxAdapter(child: _buildHeroSection()),

              // AI Önerileri Kartı
              SliverToBoxAdapter(child: _buildAICard()),

              // Arama
              SliverToBoxAdapter(child: _buildSearchBar()),

              // Mood Chips
              SliverToBoxAdapter(child: _buildMoodChips()),

              // Kategori Chips
              SliverToBoxAdapter(child: _buildCategoryChips()),

              // Başlık
              SliverToBoxAdapter(child: _buildSectionTitle()),

              // Mekan Listesi
              SliverPadding(
                padding: const EdgeInsets.fromLTRB(20, 0, 20, 100),
                sliver: SliverList(
                  delegate: SliverChildBuilderDelegate(
                    (context, index) =>
                        _buildPlaceCard(_filteredHighlights[index]),
                    childCount: _filteredHighlights.length,
                  ),
                ),
              ),
            ],
          ),

          // Floating AI Button
          Positioned(right: 20, bottom: 100, child: _buildFloatingAIButton()),
        ],
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
          .replaceAll('İ', 'i')
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
    final imageUrl = _cityImages[cityKey] ?? _cityImages['barcelona']!;

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
              child: Image.network(
                imageUrl,
                fit: BoxFit.cover,
                loadingBuilder: (context, child, loadingProgress) {
                  if (loadingProgress == null) return child;
                  return Container(
                    decoration: BoxDecoration(gradient: primaryGradient),
                    child: Center(
                      child: CircularProgressIndicator(
                        value: loadingProgress.expectedTotalBytes != null
                            ? loadingProgress.cumulativeBytesLoaded /
                                  loadingProgress.expectedTotalBytes!
                            : null,
                        color: Colors.white,
                        strokeWidth: 2,
                      ),
                    ),
                  );
                },
                errorBuilder: (_, __, ___) => Container(
                  decoration: BoxDecoration(gradient: primaryGradient),
                  child: const Center(
                    child: Icon(
                      Icons.landscape_rounded,
                      color: Colors.white54,
                      size: 64,
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
              onTap: () async {
                final result = await CitySwitcherScreen.showAsModal(context);
                if (result != null && mounted) {
                  setState(() => _loading = true);
                  _loadData();
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
                        const Icon(
                          Icons.language,
                          color: Colors.white,
                          size: 18,
                        ),
                        const SizedBox(width: 8),
                        Text(
                          _city?.city ?? "Şehir",
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

          // Selamlama (Alt kısım)
          Positioned(
            left: 20,
            bottom: 24,
            right: 20,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "${_getGreeting()}, $_userName 👋",
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 28,
                    fontWeight: FontWeight.w700,
                    height: 1.2,
                  ),
                ),
                const SizedBox(height: 6),
                Text(
                  _getMoodText(),
                  style: TextStyle(
                    color: Colors.white.withOpacity(0.85),
                    fontSize: 15,
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
        ? "İlgi alanlarınıza"
        : _interests.take(3).join(", ");

    // Eğer yanıt var ve kart kapalıysa küçük versiyon göster
    if (_aiChatResponse != null && !_aiCardExpanded) {
      return _buildCollapsedAICard(interestsPreview);
    }

    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      margin: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [accentLight.withOpacity(0.6), accent.withOpacity(0.4)],
              ),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: Colors.white.withOpacity(0.15)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Header
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.2),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: const Icon(
                        Icons.auto_awesome,
                        color: Colors.white,
                        size: 20,
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text(
                            "Sana Özel Öneriler",
                            style: TextStyle(
                              color: Colors.white,
                              fontSize: 17,
                              fontWeight: FontWeight.w700,
                            ),
                          ),
                          const SizedBox(height: 2),
                          Text(
                            "$interestsPreview ilginize göre",
                            style: TextStyle(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 13,
                            ),
                          ),
                        ],
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
                            color: Colors.white.withOpacity(0.2),
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: const Icon(
                            Icons.keyboard_arrow_up_rounded,
                            color: Colors.white,
                            size: 22,
                          ),
                        ),
                      ),
                  ],
                ),

                const SizedBox(height: 16),

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
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: GestureDetector(
            onTap: () {
              HapticFeedback.lightImpact();
              setState(() => _aiCardExpanded = true);
            },
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [
                    accentLight.withOpacity(0.6),
                    accent.withOpacity(0.4),
                  ],
                ),
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: Colors.white.withOpacity(0.15)),
              ),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Icon(
                      Icons.auto_awesome,
                      color: Colors.white,
                      size: 18,
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          "Öneriler Hazır",
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                        Text(
                          "Tekrar görmek için dokun",
                          style: TextStyle(
                            color: Colors.white.withOpacity(0.7),
                            fontSize: 12,
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Icon(
                      Icons.keyboard_arrow_down_rounded,
                      color: Colors.white,
                      size: 22,
                    ),
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
          "${_city?.city ?? 'Şehir'} için $_tripDays günlük kişisel öneriler hazırlanıyor...",
          style: TextStyle(color: Colors.white.withOpacity(0.85), fontSize: 14),
        ),
        const SizedBox(height: 14),
        GestureDetector(
          onTap: () {
            HapticFeedback.mediumImpact();
            _fetchAIChatResponse();
          },
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 10),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Text(
              "Tavsiye İste",
              style: TextStyle(
                color: accent,
                fontSize: 14,
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
        ),
      ],
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
              color: Colors.white,
              strokeWidth: 2.5,
            ),
          ),
        ),
        const SizedBox(height: 16),
        Text(
          "Sana özel öneriler hazırlanıyor...",
          style: TextStyle(color: Colors.white.withOpacity(0.9), fontSize: 14),
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

        const SizedBox(height: 16),

        // Yeniden sor butonu
        Row(
          children: [
            GestureDetector(
              onTap: () {
                HapticFeedback.mediumImpact();
                _fetchAIChatResponse();
              },
              child: Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 14,
                  vertical: 8,
                ),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(
                      Icons.refresh_rounded,
                      color: Colors.white,
                      size: 16,
                    ),
                    const SizedBox(width: 6),
                    const Text(
                      "Yenile",
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 13,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildFormattedResponse(String response) {
    // Basit markdown benzeri formatting
    final lines = response.split('\n');

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: lines.map((line) {
        if (line.trim().isEmpty) {
          return const SizedBox(height: 8);
        }

        // Bold başlık (** ** arası)
        if (line.contains('**')) {
          return Padding(
            padding: const EdgeInsets.only(bottom: 6),
            child: _buildRichText(line),
          );
        }

        // Emoji ile başlayan satırlar (⭐, 💡 vb.)
        if (line.startsWith('⭐') || line.startsWith('💡')) {
          return Padding(
            padding: const EdgeInsets.only(bottom: 10, top: 4),
            child: _buildRichText(line),
          );
        }

        return Padding(
          padding: const EdgeInsets.only(bottom: 4),
          child: Text(
            line,
            style: TextStyle(
              color: Colors.white.withOpacity(0.9),
              fontSize: 14,
              height: 1.5,
            ),
          ),
        );
      }).toList(),
    );
  }

  Widget _buildRichText(String text) {
    // ** ** arasını bold yap
    final List<InlineSpan> spans = [];
    final regex = RegExp(r'\*\*(.*?)\*\*');
    int lastEnd = 0;

    for (final match in regex.allMatches(text)) {
      // Match öncesi normal text
      if (match.start > lastEnd) {
        spans.add(
          TextSpan(
            text: text.substring(lastEnd, match.start),
            style: TextStyle(color: Colors.white.withOpacity(0.9)),
          ),
        );
      }
      // Bold text
      spans.add(
        TextSpan(
          text: match.group(1),
          style: const TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.w700,
          ),
        ),
      );
      lastEnd = match.end;
    }

    // Kalan text
    if (lastEnd < text.length) {
      spans.add(
        TextSpan(
          text: text.substring(lastEnd),
          style: TextStyle(color: Colors.white.withOpacity(0.9)),
        ),
      );
    }

    return RichText(
      text: TextSpan(
        style: const TextStyle(fontSize: 14, height: 1.5),
        children: spans,
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SEARCH BAR
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSearchBar() {
    return Container(
      margin: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      height: 52,
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor),
      ),
      child: TextField(
        controller: _searchController,
        onChanged: (v) {
          setState(() => _searchQuery = v);
          _applyFilters();
        },
        style: const TextStyle(color: textWhite, fontSize: 15),
        decoration: InputDecoration(
          hintText: "${_city?.city ?? 'Şehir'} içinde ara...",
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

  Widget _buildMoodChips() {
    return Container(
      margin: const EdgeInsets.fromLTRB(16, 16, 16, 0),
      child: Row(
        children: _moods.map((mood) {
          final isSelected = _selectedMood == mood["id"];
          return Padding(
            padding: const EdgeInsets.only(right: 10),
            child: GestureDetector(
              onTap: () {
                HapticFeedback.selectionClick();
                setState(() => _selectedMood = mood["id"]);
                _applyFilters();
                _fetchAIRecommendations();
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(
                  horizontal: 18,
                  vertical: 10,
                ),
                decoration: BoxDecoration(
                  gradient: isSelected ? primaryGradient : null,
                  color: isSelected ? null : Colors.transparent,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(
                    color: isSelected ? Colors.transparent : borderColor,
                    width: 1.5,
                  ),
                ),
                child: Text(
                  mood["label"],
                  style: TextStyle(
                    color: isSelected ? Colors.white : textGrey,
                    fontSize: 14,
                    fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                  ),
                ),
              ),
            ),
          );
        }).toList(),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // CATEGORY CHIPS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildCategoryChips() {
    return Container(
      height: 44,
      margin: const EdgeInsets.only(top: 16),
      child: ListView.builder(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 16),
        itemCount: _categories.length,
        itemBuilder: (context, index) {
          final cat = _categories[index];
          final isSelected = _selectedCategory == cat["id"];

          return Padding(
            padding: const EdgeInsets.only(right: 10),
            child: GestureDetector(
              onTap: () {
                HapticFeedback.selectionClick();
                setState(() => _selectedCategory = cat["id"]);
                _applyFilters();
              },
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.symmetric(horizontal: 18),
                decoration: BoxDecoration(
                  color: isSelected ? Colors.white : Colors.transparent,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isSelected ? Colors.white : borderColor,
                    width: 1.5,
                  ),
                ),
                child: Center(
                  child: Text(
                    cat["label"],
                    style: TextStyle(
                      color: isSelected ? bgDark : textGrey,
                      fontSize: 14,
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
    final title = _selectedCategory != "Tümü"
        ? "$_selectedCategory (${_filteredHighlights.length})"
        : "Popüler Noktalar (${_city?.city ?? ''})";

    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 24, 20, 16),
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
                "Temizle",
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

  Widget _buildPlaceCard(Highlight place) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final isFavorite = _favorites.contains(place.name);
    final isInTrip = _tripPlaces.contains(place.name);

    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
      ),
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
                    height: 160,
                    width: double.infinity,
                    child: hasImage
                        ? Image.network(
                            place.imageUrl!,
                            fit: BoxFit.cover,
                            errorBuilder: (_, __, ___) =>
                                _buildPlaceholder(place.category),
                          )
                        : _buildPlaceholder(place.category),
                  ),
                ),

                // Gradient overlay
                Container(
                  height: 160,
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
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: Colors.black.withOpacity(0.4),
                        shape: BoxShape.circle,
                      ),
                      child: Icon(
                        isFavorite ? Icons.favorite : Icons.favorite_border,
                        color: isFavorite ? accent : Colors.white,
                        size: 20,
                      ),
                    ),
                  ),
                ),

                // Kategori chip
                Positioned(
                  top: 12,
                  left: 12,
                  child: Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 10,
                      vertical: 5,
                    ),
                    decoration: BoxDecoration(
                      color: _getCategoryColor(place.category),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      place.category,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),
                ),

                // Rating
                if (place.rating != null)
                  Positioned(
                    bottom: 12,
                    left: 12,
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
                            Icons.star,
                            color: Color(0xFFFFC107),
                            size: 14,
                          ),
                          const SizedBox(width: 4),
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
                    place.name,
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 6),
                  // Konum
                  Row(
                    children: [
                      Icon(
                        Icons.location_on_outlined,
                        color: textGrey,
                        size: 14,
                      ),
                      const SizedBox(width: 4),
                      Expanded(
                        child: Text(
                          place.area,
                          style: TextStyle(color: textGrey, fontSize: 13),
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  // Alt satır
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      // Mesafe
                      if (place.distanceFromCenter != null)
                        Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 10,
                            vertical: 5,
                          ),
                          decoration: BoxDecoration(
                            color: bgCardLight,
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Text(
                            "${place.distanceFromCenter} km",
                            style: TextStyle(
                              color: textGrey,
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                            ),
                          ),
                        ),
                      // Rotaya ekle butonu
                      GestureDetector(
                        onTap: () => _addToTrip(place.name),
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 14,
                            vertical: 8,
                          ),
                          decoration: BoxDecoration(
                            gradient: isInTrip ? null : primaryGradient,
                            color: isInTrip ? Colors.green : null,
                            borderRadius: BorderRadius.circular(10),
                          ),
                          child: Row(
                            children: [
                              Icon(
                                isInTrip ? Icons.check : Icons.add,
                                color: Colors.white,
                                size: 16,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                isInTrip ? "Eklendi ✓" : "Rotaya Ekle",
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
      onTap: () {
        HapticFeedback.mediumImpact();
        _showAISheet();
      },
      child: Container(
        width: 56,
        height: 56,
        decoration: BoxDecoration(
          gradient: primaryGradient,
          shape: BoxShape.circle,
          boxShadow: [
            BoxShadow(
              color: accentLight.withOpacity(0.4),
              blurRadius: 16,
              offset: const Offset(0, 6),
            ),
          ],
        ),
        child: const Icon(Icons.auto_awesome, color: Colors.white, size: 26),
      ),
    );
  }

  void _showAISheet() {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => Container(
        height: MediaQuery.of(context).size.height * 0.6,
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
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
              padding: const EdgeInsets.all(24),
              child: Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      gradient: primaryGradient,
                      borderRadius: BorderRadius.circular(14),
                    ),
                    child: const Icon(
                      Icons.auto_awesome,
                      color: Colors.white,
                      size: 22,
                    ),
                  ),
                  const SizedBox(width: 14),
                  Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        "AI Asistan",
                        style: TextStyle(
                          color: textWhite,
                          fontSize: 18,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      Text(
                        "${_city?.city ?? 'Şehir'} hakkında sor",
                        style: TextStyle(color: textGrey, fontSize: 14),
                      ),
                    ],
                  ),
                ],
              ),
            ),
            Divider(color: borderColor, height: 1),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.all(24),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "Hızlı Sorular",
                      style: TextStyle(color: textGrey, fontSize: 14),
                    ),
                    const SizedBox(height: 14),
                    Wrap(
                      spacing: 10,
                      runSpacing: 10,
                      children: [
                        "En iyi kahve nerede?",
                        "Gün batımı için neresi?",
                        "Yerel lezzetler",
                        "Sakin bir park",
                      ].map((q) => _buildQuickQuestion(q)).toList(),
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

  Widget _buildQuickQuestion(String question) {
    return GestureDetector(
      onTap: () => Navigator.pop(context),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: bgCardLight,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: borderColor),
        ),
        child: Text(question, style: TextStyle(color: textGrey, fontSize: 14)),
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
          gradient: primaryGradient,
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

  IconData _getCategoryIcon(String category) {
    final icons = {
      'Restoran': Icons.restaurant,
      'Bar': Icons.local_bar,
      'Kafe': Icons.coffee,
      'Müze': Icons.museum,
      'Tarihi': Icons.account_balance,
      'Park': Icons.park,
      'Manzara': Icons.landscape,
      'Alışveriş': Icons.shopping_bag,
      'Semt': Icons.location_city,
    };
    return icons[category] ?? Icons.place;
  }
}
