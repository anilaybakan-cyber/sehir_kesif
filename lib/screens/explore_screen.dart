// =============================================================================
// EXPLORE SCREEN – WANDERLUST DARK THEME
// Dark background, purple/pink gradients, glassmorphism, hero city image
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:cached_network_image/cached_network_image.dart'; // 🔥 EKLENDİ
import 'package:flutter_markdown/flutter_markdown.dart';
import 'dart:ui';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/ai_service.dart';
import 'detail_screen.dart';
import 'dart:convert';
import '../services/trip_update_service.dart';
import 'city_switcher_screen.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../widgets/map_background.dart';
import 'dart:ui'; // For ImageFilter
import '../services/notification_service.dart';
import '../services/trending_service.dart';
import 'city_guide_detail_screen.dart';
import 'ai_chat_screen.dart';
import '../models/chat_message.dart';
import 'paywall_screen.dart';
import '../services/premium_service.dart';

class ExploreScreen extends StatefulWidget {
  const ExploreScreen({super.key});

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
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);
  static const Color accentGreen = Color(0xFF4CAF50);

  static const LinearGradient primaryGradient = WanderlustColors.primaryGradient;

  static const LinearGradient primaryGradientDark = WanderlustColors.primaryGradientVertical;

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  CityModel? _city;
  bool _loading = true;
  bool _aiLoading = false;
  String? _error;
  String _userName = "Gezgin";
  String _currentCityId = ""; // Mevcut şehir ID'si
  bool _showScrollToTop = false; // Scroll-to-top butonu görünürlüğü

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

  // Şehir görselleri - Tüm şehirler
  final Map<String, String> _cityImages = {
    'amsterdam': 'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800',
    'atina': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg',
    'bangkok': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg',
    'barcelona': 'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800',
    'berlin': 'https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800',
    'budapeste': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltfde92aef92ecf073/6787eae0bf32fe28813c50fe/BCC-2024-EXPLORER-BUDAPEST-LANDMARKS-HEADER-_MOBILE.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'cenevre': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/jet_deau.jpg',
    'dubai': 'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800',
    'dublin': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/temple_bar.jpg',
    'floransa': 'https://italien.expert/wp-content/uploads/2021/05/Florenz-Toskana-Italien0.jpg',
    'hongkong': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/victoria_peak.jpg',
    'istanbul': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800',
    'kopenhag': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800',
    'lizbon': 'https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800',
    'londra': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800',
    'lucerne': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/chapel_bridge_kapellbrucke.jpg',
    'lyon': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/basilica_of_notre_dame_de_fourviere.jpg',
    'madrid': 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800',
    'marakes': 'https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/jemaa_el_fna.jpg',
    'marsilya': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt0feb4d48a3fc134c/67c5fafa304ea9666082ff3e/iStock-956215674-2-Header_Mobile.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart',
    'milano': 'https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800',
    'napoli': 'https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800',
    'newyork': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800',
    'nice': 'https://www.flypgs.com/blog/wp-content/uploads/2024/05/nice-sahilleri.jpeg',
    'paris': 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800',
    'porto': 'https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=800',
    'prag': 'https://images.unsplash.com/photo-1541849546-216549ae216d?w=800',
    'roma': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800',
    'seul': 'https://www.agoda.com/wp-content/uploads/2019/03/Seoul-attractions-Gyeongbokgung-palace.jpg',
    'sevilla': 'https://images.unsplash.com/photo-1558370781-d6196949e317?w=800',
    'singapur': 'https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800',
    'stockholm': 'https://images.unsplash.com/photo-1509356843151-3e7d96241e11?w=800',
    'tokyo': 'https://img.piri.net/mnresize/900/-/resim/imagecrop/2023/01/17/11/54/resized_d9b02-8b17feafkapak2.jpg',
    'venedik': 'https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=800',
    'viyana': 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800',
    'zurih': 'https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800',
    'fes': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=800', // Fes Tanning
    'safsavan': 'https://images.unsplash.com/photo-1558258695-0e4284b3975d?w=800', // Chefchaouen blue
    'kahire': 'https://images.unsplash.com/photo-1572252009289-9ef997e21242?w=800', // Pyramids
    'kopenhag': 'https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800', // Nyhavn
    'stockholm': 'https://images.unsplash.com/photo-1509356843151-3e7d96241e11?w=800', // Gamla Stan
    'saraybosna': 'https://images.unsplash.com/photo-1596715694269-80838637ba76?w=800', // Sarajevo
    'mostar': 'https://images.unsplash.com/photo-1605198089408-0138977114b0?w=800', // Mostar Bridge
    'strazburg': 'https://images.unsplash.com/photo-1549144511-6099e7dab944?w=800', // Strasbourg
    'midilli': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800', // Generic Greece/Sea
    'antalya': 'https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=800', // Antalya/Turkey
    'edinburgh': 'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=800',
    'belgrad': 'https://images.unsplash.com/photo-1563214532-6a84c3116972?w=800', // Belgrade
    'kotor': 'https://images.unsplash.com/photo-1565620958742-832746497241?w=800', // Kotor
    'tiran': 'https://images.unsplash.com/photo-1599593442654-e1b088b7538c?w=800', // Tirana
    'selanik': 'https://images.unsplash.com/photo-1562608460-f97577579893?w=800', // Thessaloniki
    'kapadokya': 'https://images.unsplash.com/photo-1641128324972-af3212f0f6bd?w=800', // Cappadocia
    // New Featured Cities
    'rovaniemi': 'https://www.visitfinland.com/dam/jcr:70734834-7ba2-4bf1-9f6e-bf185e014367/central-plaza-santa-claus-village-rovaniemi-lapland-finland%20(1).jpg',
    'tromso': 'https://www.flightgift.com/media/wp/FG/2024/02/tromso.webp',
    'zermatt': 'https://holidaystoswitzerland.com/wp-content/uploads/2020/07/Zermatt-and-the-Matterhorn-at-dawn.jpg',
    'matera': 'https://ita.travel/user/blogimg/ostatni/aerial-view_matera_sunset.jpg',
    'giethoorn': 'https://www.onedayinacity.com/wp-content/uploads/2021/03/Giethoorn-Village.png',
    'colmar': 'https://images.goway.com/production/hero/iStock-1423136049.jpg',
    'sintra': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt75a384a61f2efa5b/68848225e7cb649650cc2d81/BCC-2024-EXPLORER-SINTRA-BEST_PLACES_TO_VISIT-HEADER-MOBILE.jpg?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440',
    'sansebastian': 'https://cdn.bunniktours.com.au/public/posts/images/Europe/Blog%20Header%20-%20Spain%20-%20San%20Sebastian%20-%20credit%20Raul%20Cacho%20Oses%20%28Unsplash%29-feature.jpg',
    'bologna': 'https://www.datocms-assets.com/57243/1661342703-6245af628d40974c9ab5a7fd_petr-slovacek-sxk8bwkvoxe-unsplash-20-1.jpg?auto=compress%2Cformat',
    'gaziantep': 'https://www.brandlifemag.com/wp-content/uploads/2021/04/acilis-gaziantep-december-06gaziantep-coppersmith-bazaar-600w-549044518.jpg',
    'brugge': 'https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2021-08/brugge-hakkinda-bilinmesi-gerekenler.jpg',
    'santorini': 'https://www.kucukoteller.com.tr/storage/images/2024/07/14/5e7eaf11eb5ec2dda2f7a602232faa8961347f29.webp',
    'heidelberg': 'https://image.hurimg.com/i/hurriyet/90/1110x740/56b3325818c7730e3cdb6757.jpg',
  };

  List<Map<String, dynamic>> get _categories => [
    {"id": "Tümü", "label": AppLocalizations.instance.allCategories},
    {"id": "Restoran", "label": AppLocalizations.instance.restaurant},
    {"id": "Kafe", "label": AppLocalizations.instance.cafe},
    {"id": "Müze", "label": AppLocalizations.instance.museum},
    {"id": "Park", "label": AppLocalizations.instance.park},
    {"id": "Bar", "label": AppLocalizations.instance.bar},
    {"id": "Pub", "label": AppLocalizations.instance.pub},
    {"id": "Tarihi", "label": AppLocalizations.instance.historical},
    {"id": "Deneyim", "label": AppLocalizations.instance.experience},
    {"id": "Alışveriş", "label": AppLocalizations.instance.shopping},
    {"id": "Plaj", "label": AppLocalizations.instance.beach},
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
    TripUpdateService().cityChanged.addListener(_onTripDataChanged);
    
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
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    TripUpdateService().cityChanged.removeListener(_onTripDataChanged);
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
          // 🔥 FCM Üyeliğini güncelle
          NotificationService().subscribeToCity(normalizedCity);

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

      // 🔥 Analytics: Ekran görüntüleme
      NotificationService().logEvent('explore_city', parameters: {
        'city_id': normalizedCity,
        'city_name': city.city,
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

    // 1. Kategori filtresi (kesin filtre)
    // Comprehensive category mappings - maps orphan categories to filter buttons
    const categoryMappings = {
      // Kafe filtresi
      'Kafe': ['Kafe', 'Cafe', 'Kahve', 'Tatlı', 'Fırın', 'Dondurma', 'Atıştırmalık'],
      
      // Restoran filtresi
      'Restoran': ['Restoran', 'Yeme & İçme', 'Yeme İçme', 'Yeme-İçme', 'Sokak Lezzeti', 'Yemek'],
      
      // Müze filtresi
      'Müze': ['Müze', 'Sanat', 'Kültür', 'Bilim', 'Modern', 'Akvaryum'],
      
      // Park filtresi
      'Park': ['Park', 'Doğa', 'Göl', 'Hayvanat Bahçesi', 'Mağara'],
      
      // Bar filtresi
      'Bar': ['Bar', 'Gece Hayatı', 'Gece Kulübü', 'Şarap'],
      
      // Pub filtresi (yeni)
      'Pub': ['Pub'],
      
      // Tarihi filtresi
      'Tarihi': ['Tarihi', 'Meydan', 'Mimari', 'Tarih', 'Simge', 'Landmark', 'Heykel', 'Mimar', 'Saray', 'Merkez'],
      
      // Deneyim filtresi (genişletilmiş - Manzara dahil)
      'Deneyim': ['Deneyim', 'Manzara', 'Aktivite', 'Eğlence', 'Yürüyüş', 'Spor', 'Gezi', 'Macera', 'Rahatlama', 
                  'Günlük Gezi', 'Etkinlik', 'Müzik', 'Atölye', 'Mahalle', 'Sokak',
                  'Görülmesi Gereken Yerler', 'Köy', 'Kasaba', 'Şehir', 'Bölge', 'Liman'],
      
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
      final validCategories = categoryMappings[_selectedCategory] ?? [_selectedCategory];
      filtered = filtered
          .where((h) => validCategories.contains(h.category))
          .toList();
    }

    // 2. Arama filtresi
    if (_searchQuery.isNotEmpty) {
      final query = _searchQuery.toLowerCase();
      filtered = filtered.where((h) {
        return h.name.toLowerCase().contains(query) ||
            h.area.toLowerCase().contains(query) ||
            h.category.toLowerCase().contains(query) ||
            (h.description.toLowerCase().contains(query)) ||
            h.tags.any((tag) => tag.toLowerCase().contains(query));
      }).toList();
    }

    // 3. Kişiselleştirilmiş sıralama (popülerlik + ilgi alanları serpiştirilmiş)
    // Mood seçili değilse veya Keşif modundaysa kişiselleştirilmiş sıralama uygula
    if (_selectedMood == 1 || _selectedMood == -1) {
      // 🌍 Keşif modu veya varsayılan: Popülerlik önce, ilgi alanları serpiştirilmiş
      filtered = _applyPersonalizedSorting(filtered);
    } else if (_selectedMood == 0) {
      // 🧘 Sakin: Önce kişiselleştir, sonra sakin kategorileri öne al
      filtered = _applyPersonalizedSorting(filtered);
      filtered.sort((a, b) {
        int scoreA = _getCalmScore(a.category);
        int scoreB = _getCalmScore(b.category);
        if (scoreA != scoreB) return scoreA.compareTo(scoreB);
        // Eşit ise popülerliğe göre
        return _getPopularityScore(b).compareTo(_getPopularityScore(a));
      });
    } else if (_selectedMood == 2) {
      // 🎉 Canlı: Önce kişiselleştir, sonra canlı kategorileri öne al
      filtered = _applyPersonalizedSorting(filtered);
      filtered.sort((a, b) {
        int scoreA = _getLivelyScore(a.category);
        int scoreB = _getLivelyScore(b.category);
        if (scoreA != scoreB) return scoreA.compareTo(scoreB);
        // Eşit ise popülerliğe göre
        return _getPopularityScore(b).compareTo(_getPopularityScore(a));
      });
    }

    setState(() => _filteredHighlights = filtered);
  }

  // Mood skor fonksiyonları (düşük = daha öncelikli)
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
    'yemek': ['Restoran', 'Yeme & İçme', 'Yeme İçme', 'Sokak Lezzeti'],
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
    'yerel lezzetler': ['Restoran', 'Sokak Lezzeti', 'Yeme & İçme', 'Pazar'],
  };

  /// Popülerlik skoru hesapla (0-1 arası)
  double _getPopularityScore(Highlight h) {
    final rating = h.rating ?? 0;
    final reviewCount = h.reviewCount ?? 0;
    
    // Rating ağırlığı: %60, Review count ağırlığı: %30, Landmark bonus: %10
    final ratingScore = (rating / 5.0).clamp(0.0, 1.0);
    final reviewScore = (reviewCount / 5000.0).clamp(0.0, 1.0);
    
    // Tarihi/Simge kategorileri için bonus
    final isLandmark = ['Tarihi', 'Simge', 'Landmark', 'Mimari'].contains(h.category);
    final landmarkBonus = isLandmark ? 0.1 : 0.0;
    
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

  /// Kişiselleştirilmiş sıralama uygula
  List<Highlight> _applyPersonalizedSorting(List<Highlight> places) {
    if (places.isEmpty) return places;
    
    // 1. Tüm yerleri popülerliğe göre sırala (en yüksek önce)
    final sortedByPopularity = List<Highlight>.from(places);
    sortedByPopularity.sort((a, b) {
      final scoreA = _getPopularityScore(a);
      final scoreB = _getPopularityScore(b);
      return scoreB.compareTo(scoreA); // Descending
    });
    
    // 2. Kullanıcının ilgi alanlarına uyan yerleri ayır
    final interestMatches = places.where((h) => _matchesUserInterests(h)).toList();
    
    // İlgi alanı eşleşenler de bütçe ve popülerliğe göre sıralı olsun
    interestMatches.sort((a, b) {
      final budgetA = _getBudgetMatchScore(a);
      final budgetB = _getBudgetMatchScore(b);
      final popA = _getPopularityScore(a);
      final popB = _getPopularityScore(b);
      
      final scoreA = (popA * 0.6) + (budgetA * 0.4);
      final scoreB = (popB * 0.6) + (budgetB * 0.4);
      return scoreB.compareTo(scoreA);
    });
    
    // 3. Karma liste oluştur: Her 4 popüler yerden sonra 1 ilgi alanı yeri ekle
    final result = <Highlight>[];
    final usedInterestIndices = <int>{};
    int interestIndex = 0;
    
    for (int i = 0; i < sortedByPopularity.length; i++) {
      final place = sortedByPopularity[i];
      
      // Bu yer zaten ilgi alanı olarak eklendiyse atla
      if (usedInterestIndices.contains(places.indexOf(place))) continue;
      
      result.add(place);
      
      // Her 4 yerden sonra bir ilgi alanı yeri ekle (ilk 4'ten sonra başla)
      if ((result.length % 5) == 4 && interestIndex < interestMatches.length) {
        final interestPlace = interestMatches[interestIndex];
        // Zaten eklenmemişse ekle
        if (!result.contains(interestPlace)) {
          result.add(interestPlace);
          usedInterestIndices.add(places.indexOf(interestPlace));
        }
        interestIndex++;
      }
    }
    
    return result;
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

  // Kullanıcı AppLocalizations.instance.askAI butonuna basınca çağrılır
  Future<void> _fetchAIChatResponse() async {
    if (_city == null) return;
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
        isEnglish: AppLocalizations.instance.isEnglish, // Dil parametresi
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
  }

  Future<void> _addToTrip(String name) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();
    final String currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
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
               content: Text(AppLocalizations.instance.removedFromRoute(name)),
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

         final selectedDay = await _showDaySelectionDialogForExplore(maxDay, name, scheduleMap);
         if (selectedDay == null) return; // İptal
         
         setState(() {
           _tripPlaces.add(name);
         });
         tripPlaces.add(name);
         
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
         
         if (mounted) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Row(
                 children: [
                   const Icon(Icons.check_circle, color: WanderlustColors.accent, size: 20),
                   const SizedBox(width: 12),
                   Expanded(child: Text(AppLocalizations.instance.addedToDay(name, selectedDay))),
                 ],
               ),
               backgroundColor: const Color(0xFF1F1F1F),
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

  Future<int?> _showDaySelectionDialogForExplore(int totalDays, String placeName, Map<String, dynamic> scheduleMap) async {
    return showDialog<int>(
      context: context,
      barrierColor: Colors.black.withOpacity(0.7),
      builder: (context) {
        return Dialog(
          backgroundColor: const Color(0xFF1A1A2E),

          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(AppLocalizations.instance.whichDay, style: TextStyle(color: textWhite, fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                Text(AppLocalizations.instance.addToRouteConfirm(placeName), textAlign: TextAlign.center, style: const TextStyle(color: textGrey, fontSize: 14)),
                const SizedBox(height: 20),
                ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 400),
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                         ...List.generate(totalDays, (index) {
                             final day = index + 1;
                             final dayKey = day.toString();
                             final List<dynamic> dayPlaces = scheduleMap[dayKey] ?? [];
                             final count = dayPlaces.length;
                             return ListTile(
                               title: Text(AppLocalizations.instance.dayN(day), style: const TextStyle(color: textWhite)),
                               subtitle: Text(AppLocalizations.instance.nPlaces(count), style: const TextStyle(color: textGrey, fontSize: 12)),
                               trailing: const Icon(Icons.arrow_forward_ios, color: accent, size: 16),
                               onTap: () => Navigator.pop(context, day),
                             );
                         }),
                         const Divider(color: borderColor),
                         ListTile(
                             title: Text(AppLocalizations.instance.createNewDay, style: TextStyle(color: textWhite)),
                             subtitle: Text(AppLocalizations.instance.dayN(totalDays + 1), style: const TextStyle(color: textGrey, fontSize: 12)),
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
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: accent,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Image.asset(
                  'assets/images/splash_logo.png',
                  width: 32,
                  height: 32,
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
            // Ana içerik
            CustomScrollView(
              controller: _scrollController,
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
          
          // Scroll-to-top Button
          if (_showScrollToTop)
            Positioned(
              right: 20,
              bottom: 170,
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
    final cityName = _city!.city;
    // Şehir görselini bul
    final imageUrl = _cityImages[_currentCityId] ?? 'https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=800';

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
                // 1. Arka Plan Resmi
                CachedNetworkImage(
                  imageUrl: imageUrl,
                  fit: BoxFit.cover,
                  color: Colors.black.withOpacity(0.2), // Hafif karartma
                  colorBlendMode: BlendMode.darken,
                  placeholder: (context, url) => Container(color: bgCard),
                  errorWidget: (context, url, error) => Container(color: bgCard),
                ),

                // 2. Gradient Overlay (Okunabilirlik için)
                Container(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.centerLeft,
                      end: Alignment.centerRight,
                      colors: [
                        Colors.black.withOpacity(0.9), // Solda tam siyah (yazı altı)
                        Colors.black.withOpacity(0.4), // Ortada geçiş
                        Colors.transparent, // Sağda resim görünsün
                      ],
                      stops: const [0.0, 0.6, 1.0],
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
                              isEnglish ? "Visa, transport, history & more" : "Vize, ulaşım, tarih ve ipuçları",
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
    // Öncelik JSON'dan gelen heroImage'da, yoksa hardcoded listeden al
    final imageUrl = _city?.heroImage ?? _cityImages[cityKey] ?? _cityImages['barcelona']!;

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
                    decoration: BoxDecoration(color: accent),
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
                  decoration: BoxDecoration(color: accent),
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
                          _city?.city ?? AppLocalizations.instance.city,
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
            child: Builder(
              builder: (context) {
                final isPremium = PremiumService.instance.isPremium;
                if (isPremium) return const SizedBox.shrink();
                
                return GestureDetector(
                  onTap: () {
                    HapticFeedback.mediumImpact();
                    showPaywall(context);
                  },
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(20),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                        decoration: BoxDecoration(
                          color: accent, 
                          borderRadius: BorderRadius.circular(20),
                          border: Border.all(color: Colors.white.withOpacity(0.2)),
                        ),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: const [
                            Icon(Icons.star_rounded, color: Colors.white, size: 18),
                            SizedBox(width: 6),
                            Text(
                              'PRO',
                              style: TextStyle(
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
        ? AppLocalizations.instance.basedOnInterests
        : _interests.take(2).join(", ");

    // Eğer yanıt var ve kart kapalıysa küçük versiyon göster
    if (_aiChatResponse != null && !_aiCardExpanded) {
      return _buildCollapsedAICard(interestsPreview);
    }

    return AnimatedContainer(
      duration: const Duration(milliseconds: 300),
      margin: const EdgeInsets.fromLTRB(16, 20, 16, 0),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(24),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 15, sigmaY: 15),
          child: Container(
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.08),
              borderRadius: BorderRadius.circular(24),
              border: Border.all(color: Colors.white.withOpacity(0.12), width: 1.2),
            ),
            child: Stack(
              children: [
                // Background Symbols
                _buildGlassSymbols(),
                
                // Content
                Padding(
                  padding: const EdgeInsets.all(20),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Header
                      Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.all(4),
                            decoration: BoxDecoration(
                              color: accent,
                              borderRadius: BorderRadius.circular(10),
                            ),
                            child: Image.asset(
                              'assets/images/splash_logo.png',
                              width: 18,
                              height: 18,
                              fit: BoxFit.contain,
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  AppLocalizations.instance.aiRecommendations,
                                  style: const TextStyle(
                                    color: Colors.white,
                                    fontSize: 18,
                                    fontWeight: FontWeight.w700,
                                    letterSpacing: -0.5,
                                  ),
                                ),
                                const SizedBox(height: 4),
                                Row(
                                  children: [
                                    Icon(Icons.auto_awesome, color: accent, size: 12),
                                    const SizedBox(width: 4),
                                    Text(
                                      _interests.isNotEmpty 
                                        ? AppLocalizations.instance.t("Senin tercihlerine göre öneriler", "Suggestions based on your interests")
                                        : AppLocalizations.instance.t("Kişiselleştirilmiş öneriler", "Personalized suggestions"),
                                      style: TextStyle(
                                        color: accent.withOpacity(0.9),
                                        fontSize: 12,
                                        fontWeight: FontWeight.w500,
                                      ),
                                    ),
                                  ],
                                ),
                              ],
                            ),
                          ),
                          // Yenile butonu
                          if (_aiChatResponse != null && !_aiLoading)
                            GestureDetector(
                              onTap: () {
                                HapticFeedback.lightImpact();
                                // Cache'i temizle ve yeniden üret
                                _aiChatCache.remove(_currentCityId);
                                setState(() => _aiChatResponse = null);
                                _fetchAIChatResponse();
                              },
                              child: Container(
                                padding: const EdgeInsets.all(8),
                                margin: const EdgeInsets.only(right: 8),
                                decoration: BoxDecoration(
                                  color: Colors.white.withOpacity(0.1),
                                  borderRadius: BorderRadius.circular(10),
                                ),
                                child: const Icon(
                                  Icons.refresh_rounded,
                                  color: Colors.white70,
                                  size: 20,
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
                                child: const Icon(
                                  Icons.keyboard_arrow_up_rounded,
                                  color: Colors.white70,
                                  size: 22,
                                ),
                              ),
                            ),
                        ],
                      ),


                      const SizedBox(height: 18),

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
                child: const Icon(Icons.flight_takeoff_rounded, size: 80, color: WanderlustColors.accent),
              ),
            ),
            Positioned(
              left: -15,
              bottom: -10,
              child: Transform.rotate(
                angle: -0.1,
                child: const Icon(Icons.luggage_rounded, size: 70, color: WanderlustColors.accent),
              ),
            ),
            Positioned(
              right: 40,
              bottom: -20,
              child: const Icon(Icons.confirmation_number_rounded, size: 60, color: WanderlustColors.accent),
            ),
            Positioned(
              left: 30,
              top: 40,
              child: Transform.rotate(
                angle: 0.5,
                child: const Icon(Icons.train_rounded, size: 40, color: Colors.white10),
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
              child: Row(
                children: [
                    Container(
                      padding: const EdgeInsets.all(0),
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
                          AppLocalizations.instance.recommendationsReady,
                          style: const TextStyle(
                            color: Colors.white,
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                        Text(
                          AppLocalizations.instance.tapToSeeAgain,
                          style: TextStyle(
                            color: Colors.white.withOpacity(0.6),
                            fontSize: 12,
                          ),
                        ),
                      ],
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.08),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Icon(
                      Icons.keyboard_arrow_down_rounded,
                      color: Colors.white60,
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
          AppLocalizations.instance.preparingRecommendations(_city?.city ?? AppLocalizations.instance.city, _tripDays),
          style: const TextStyle(
            color: textGrey,
            fontSize: 14,
            height: 1.5,
          ),
        ),
        const SizedBox(height: 16),
        Center(
          child: GestureDetector(
            onTap: () {
              HapticFeedback.mediumImpact();
              _fetchAIChatResponse();
            },
            child: ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: BackdropFilter(
                filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: accent.withOpacity(0.4)),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.auto_awesome_rounded, color: accent, size: 16),
                      const SizedBox(width: 8),
                      Text(
                        AppLocalizations.instance.askAI,
                        style: const TextStyle(
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
          AppLocalizations.instance.preparingForYou,
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
                // Cache'i temizle ve yeniden üret
                _aiChatCache.remove(_currentCityId);
                setState(() => _aiChatResponse = null);
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
            ),
          ),
      ],
    );
  }

  // Markdown Stili (Ortak)
  MarkdownStyleSheet _getMarkdownStyle() {
    return MarkdownStyleSheet(
      p: TextStyle(
        color: Colors.white.withOpacity(0.9),
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
      child: Container(
        margin: const EdgeInsets.only(bottom: 20),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.05),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: Colors.white.withOpacity(0.1),
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.2),
              blurRadius: 10,
              offset: const Offset(0, 4),
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
                  CachedNetworkImage(
                    imageUrl: imageUrl,
                    fit: BoxFit.cover,
                    placeholder: (context, url) => Container(
                      color: Colors.white.withOpacity(0.1),
                    ),
                    errorWidget: (context, url, error) => Container(
                      color: Colors.grey[900],
                      child: const Icon(Icons.image_not_supported, color: Colors.white54),
                    ),
                  ),
                  // Gradient Overlay (Yazı okunabilirliği için)
                  Container(
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
                         color: Colors.white54,
                         size: 14,
                       ),
                     ],
                   ),
                   const SizedBox(height: 8),
                   // Açıklama
                   Text(
                     item.description,
                     style: TextStyle(
                       color: Colors.white.withOpacity(0.85),
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
    );
  }

  // AI Yanıtını Ayrıştırıcı
  Map<String, dynamic> _parseAIResponse(String response) {
    String intro = "";
    String tip = "";
    List<RecommendationItem> items = [];

    // 1. İpucunu ayır (Tip veya İpucu)
    // AI Service formatı: ... \n\n**Tip:** Text
    final tipRegex = RegExp(r'\*\*(Tip|İpucu):\*\*\s*(.*)', dotAll: true);
    final tipMatch = tipRegex.firstMatch(response);
    
    String mainContent = response;

    if (tipMatch != null) {
      tip = "**${tipMatch.group(1)}:** ${tipMatch.group(2)?.trim()}";
      mainContent = response.substring(0, tipMatch.start).trim();
    }

    // 2. Intro ve Önerileri ayır
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
      final itemRegex = RegExp(r'-\s*\[(.*?)\]\(search:(.*?)\)\s*-\s*(.*?)(?=\n-\s*\[|$)', dotAll: true);
      
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

  void _navigateToPlaceDetail(String query) {
    if (_city == null) return;

    // Şehrin highlight'ları içinde ismi eşleşen (veya içeren) yeri bul
    try {
      final highlight = _city!.highlights.firstWhere(
        (h) => h.name.toLowerCase().contains(query.toLowerCase()) || 
               query.toLowerCase().contains(h.name.toLowerCase()),
      );

      // Bulunan yerin detay sayfasına git
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => DetailScreen(
            place: highlight,
          ),
        ),
      );
    } catch (e) {
      // Yer bulunamazsa kullanıcıya bilgi ver
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(AppLocalizations.instance.placeNotFound(query)),
          backgroundColor: Colors.redAccent,
          behavior: SnackBarBehavior.floating,
          duration: const Duration(seconds: 2),
        ),
      );
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TRENDING TODAY SECTION
  // ══════════════════════════════════════════════════════════════════════════

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
                    Icon(Icons.local_fire_department_rounded, color: accent, size: 14),
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
        SizedBox(
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
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final placeKey = "$_currentCityId:${place.name}";
    final isFavorite = _favorites.contains(place.name) || _favorites.contains(placeKey);

    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
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
                    child: hasImage
                        ? Image.network(
                            place.imageUrl!,
                            fit: BoxFit.cover,
                            errorBuilder: (_, __, ___) => _buildPlaceholderImage(place.category),
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
                        place.name,
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
                              place.area.isNotEmpty ? place.area : (place.city ?? ""),
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
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: TextField(
        controller: _searchController,
        onChanged: (v) {
          setState(() => _searchQuery = v);
          _applyFilters();
        },
        style: const TextStyle(color: textWhite, fontSize: 15),
        decoration: InputDecoration(
          hintText: AppLocalizations.instance.searchInCity(_city?.city ?? AppLocalizations.instance.city),
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
      {"id": 0, "label": AppLocalizations.instance.moodCalm},
      {"id": 1, "label": AppLocalizations.instance.moodDiscover},
      {"id": 2, "label": AppLocalizations.instance.moodLively},
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: const EdgeInsets.only(left: 24, top: 24, bottom: 8),
          child: AnimatedSwitcher(
            duration: const Duration(milliseconds: 300),
            child: Text(
              _getMoodDescription(_selectedMood),
              key: ValueKey<int>(_selectedMood),
              style: TextStyle(
                color: textGrey.withOpacity(0.6),
                fontSize: 13,
                fontWeight: FontWeight.w500,
                letterSpacing: 0.5,
              ),
            ),
          ),
        ),

        Container(
          margin: const EdgeInsets.symmetric(horizontal: 20),
      height: 54,
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.05), // Çok hafif taban
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Colors.white.withOpacity(0.08)),
      ),
      child: Stack(
        children: [
          // Liquid Glass Indicator (Kayan Buzlu Cam)
          AnimatedAlign(
            duration: const Duration(milliseconds: 500),
            curve: Curves.easeInOutCubic, // Daha akışkan (liquid) hissi
            alignment: Alignment(
              -1.0 + (_selectedMood * 1.0), 
               0.0
            ),
            child: LayoutBuilder(
              builder: (context, constraints) {
                return Container(
                  width: constraints.maxWidth / 3,
                  height: double.infinity,
                  margin: const EdgeInsets.all(4),
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(14),
                    color: Colors.white.withOpacity(0.12), // Buzlu cam rengi
                    border: Border.all(color: Colors.white.withOpacity(0.2)),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.1),
                        blurRadius: 10,
                        offset: const Offset(0, 4),
                      ),
                    ],
                  ),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(14),
                    child: BackdropFilter(
                      filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
                      child: Container(color: Colors.transparent),
                    ),
                  ),
                );
              },
            ),
          ),

          // Butonlar
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
                        // Aktifse küçük nokta
                        if (isSelected) 
                          Container(
                            margin: const EdgeInsets.only(right: 6),
                            width: 6,
                            height: 6,
                            decoration: BoxDecoration(
                              color: accent, // Amber rengi nokta
                              shape: BoxShape.circle,
                              boxShadow: [
                                BoxShadow(
                                  color: accent.withOpacity(0.5),
                                  blurRadius: 6,
                                  spreadRadius: 1,
                                ),
                              ],
                            ),
                          ),
                        AnimatedDefaultTextStyle(
                          duration: const Duration(milliseconds: 300),
                          style: TextStyle(
                            fontFamily: 'Ubuntu',
                            color: isSelected ? Colors.white : textGrey.withOpacity(0.8),
                            fontSize: 14,
                            fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                            letterSpacing: 0.5,
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
                  color: isSelected ? accent : Colors.transparent,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: isSelected ? accent : borderColor,
                    width: 1.5,
                  ),
                ),
                child: Center(
                  child: Text(
                    AppLocalizations.instance.translateCategory(cat["label"]),
                    style: TextStyle(
                      color: isSelected ? Colors.white : textGrey,
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

  Widget _buildPlaceCard(Highlight place) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final placeKey = "$_currentCityId:${place.name}";
    final isFavorite = _favorites.contains(placeKey) || _favorites.contains(place.name);
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

                // Rating - tıklanabilir (Google Maps'e yönlendirir)
                if (place.rating != null)
                  Positioned(
                    bottom: 12,
                    left: 12,
                    child: GestureDetector(
                      onTap: () async {
                        HapticFeedback.lightImpact();
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
                          place.area.isNotEmpty ? place.area : (place.city ?? ""),
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
                              color: Colors.white, // White text
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
                            color: isInTrip ? accent : bgCardLight, // Filled accent when active
                            borderRadius: BorderRadius.circular(10),
                            border: Border.all(
                              color: isInTrip ? accent : borderColor.withOpacity(0.5),
                              width: isInTrip ? 1.5 : 1,
                            ),
                          ),
                          child: Row(
                            children: [
                              Icon(
                                isInTrip ? Icons.check : Icons.add_location_alt_outlined,
                                color: isInTrip ? Colors.white : textGrey, // White icon when active
                                size: 16,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                isInTrip ? AppLocalizations.instance.addedToRoute : AppLocalizations.instance.addToRoute,
                                style: TextStyle(
                                  color: isInTrip ? Colors.white : textGrey, // White text when active
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
          padding: const EdgeInsets.all(8),
          child: Image.asset(
            'assets/images/splash_logo.png',
            fit: BoxFit.contain,
          ),
        ),
      ),
    );
  }

  void _showAISheet() {
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


