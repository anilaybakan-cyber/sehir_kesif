import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shimmer/shimmer.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import '../services/remote_config_service.dart';
import 'city_guide_detail_screen.dart';
import 'guide_article_screen.dart';
import 'amsterdam_special/amsterdam_guide_screen.dart';
import '../theme/wanderlust_colors.dart';
import '../services/analytics_service.dart'; // Added
import 'dart:async'; // Added
import 'dart:math' as math;
import 'dart:ui' show ImageFilter;
import '../widgets/resilient_network_image.dart';
import 'city_switcher_screen.dart'; // Added
class CityGuideScreen extends StatefulWidget {
  const CityGuideScreen({super.key});

  @override
  State<CityGuideScreen> createState() => _CityGuideScreenState();
}

class _CityGuideScreenState extends State<CityGuideScreen>
    with SingleTickerProviderStateMixin {
  List<Map<String, dynamic>> _cities = [];
  List<Map<String, dynamic>> _filteredCities = [];
  bool _isLoading = true;
  String _searchQuery = '';
  final TextEditingController _searchController = TextEditingController();
  final FocusNode _searchFocusNode = FocusNode();
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;
  Timer? _searchTimer; // Added for debouncing analytics

  /// Tüm kart görsellerindeki "Ken Burns" canlılığı (zoom + hafif pan).
  /// Tek controller döner; her kart kendi fazıyla sin/cos üzerinden hareket
  /// alır — böylece kartlar senkron "nefes almaz", her biri kendi ritminde
  /// yaşar.
  late final AnimationController _kenBurnsController;

  /// Vitrin carousel'i — komşu kartın ucu görünür, kaydırınca paralaks oluşur.
  final PageController _featuredController =
      PageController(viewportFraction: 0.86);

  @override
  void initState() {
    super.initState();
    _kenBurnsController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 9),
    )..repeat();
    _loadCities();
    _scrollController.addListener(() {
      final show = _scrollController.offset > 200;
      if (show != _showScrollToTop) {
        setState(() => _showScrollToTop = show);
      }
    });
  }

  @override
  void dispose() {
    _kenBurnsController.dispose();
    _featuredController.dispose();
    _searchController.dispose();
    _searchFocusNode.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  // Şehir listesini getir (Tüm şehirler)
  Future<void> _loadCities() async {
    setState(() => _isLoading = true);
    
    // Biraz gecikme ekle ki geçiş yumuşak olsun
    await Future.delayed(const Duration(milliseconds: 300));
    
    if (!mounted) return;
    
    final isEnglish = AppLocalizations.instance.isEnglish;
    
    // Orijinal hardcoded fonksiyon üzerinden mevcut şehirlere ait özel alt başlıkları alıyoruz
    final legacyCities = AIService.getAllCitiesForGuide(isEnglish);
    final subtitleMap = <String, String>{};
    for (final c in legacyCities) {
      subtitleMap[c['city'].toString().toLowerCase()] = c['subtitle'].toString();
    }
    
    // Şimdi OTA'dan gelen güncel şehir listesi ile harmanlayalım
    // city_switcher_screen import edilmediyse, reflection yerine basitçe AIService üzerinden geçebilirdik ama 
    // en kolayı CitySwitcherScreen'den çekmek
    // NOT: import '../screens/city_switcher_screen.dart'; eklendiğinden emin olacağız.
    final List<Map<String, dynamic>> cities = CitySwitcherScreen.allCities.map((c) {
      final name = isEnglish ? c['name_en'] : c['name'];
      final fallbackSub = isEnglish ? "Discover ${c['name_en']}" : "${c['name']} şehrini keşfedin";
      final subtitle = subtitleMap[name.toString().toLowerCase()] ?? fallbackSub;
      
      return {
        'id': c['id'],
        'city': name,
        'subtitle': subtitle,
        'imageUrl': c['networkImage'] ?? '',
      };
    }).toList();

    cities.sort((a, b) => _sortKey(a['city'].toString())
        .compareTo(_sortKey(b['city'].toString())));

    setState(() {
      _cities = cities;
      _filteredCities = cities;
      _isLoading = false;
    });
  }

  /// Türkçe karakterleri Latin karşılıklarına indirgeyerek alfabetik
  /// sıralama anahtarı üretir (yoksa Ç, İ, Ş, Ö, Ü Z'den sonraya düşer).
  static String _sortKey(String s) {
    const map = {
      'ç': 'c', 'Ç': 'c',
      'ğ': 'g', 'Ğ': 'g',
      'ı': 'i', 'I': 'i', 'İ': 'i',
      'ö': 'o', 'Ö': 'o',
      'ş': 's', 'Ş': 's',
      'ü': 'u', 'Ü': 'u',
      'â': 'a', 'î': 'i', 'û': 'u',
    };
    return s
        .split('')
        .map((c) => map[c] ?? c.toLowerCase())
        .join();
  }

  void _filterCities(String query) {
    setState(() {
      _searchQuery = query.toLowerCase();
      if (_searchQuery.isEmpty) {
        _filteredCities = _cities;
      } else {
        _filteredCities = _cities.where((city) {
          final cityName = city['city'].toString().toLowerCase();
          final subtitle = city['subtitle'].toString().toLowerCase();
          return cityName.contains(_searchQuery) || subtitle.contains(_searchQuery);
        }).toList();
      }
      // Liste değişti — açık bar artık başka şehre denk gelebilir
      _expandedIndex = null;
    });

    // --- ANALYTICS DEBOUNCE ---
    _searchTimer?.cancel();
    if (query.length >= 3) {
      _searchTimer = Timer(const Duration(seconds: 1), () {
        AnalyticsService.instance.logSearch(query);
      });
    }
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Dil değişirse güncelle
    _loadCities();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: SafeArea(
        child: GestureDetector(
          onTap: () => _searchFocusNode.unfocus(),
          child: Stack(
            children: [
              CustomScrollView(
                controller: _scrollController,
                physics: const BouncingScrollPhysics(),
                slivers: [
              // Header
              SliverToBoxAdapter(
                child: Padding(
                  padding: const EdgeInsets.all(20.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        AppLocalizations.instance.isEnglish ? "TRAVEL BLOG" : "SEYAHAT BLOGU",
                        style: GoogleFonts.poppins(
                          color: WanderlustColors.textGrey,
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                          letterSpacing: 1.2,
                        ),
                      ),
                      const SizedBox(height: 8),
                    ],
                  ),
                ),
              ),

              // Featured Carousel
              SliverToBoxAdapter(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Padding(
                      padding: const EdgeInsets.only(left: 20, bottom: 16),
                      child: Text(
                        AppLocalizations.instance.isEnglish ? "Discover & Inspire" : "Keşfet & İlham Al",
                        style: GoogleFonts.poppins(
                          color: WanderlustColors.textWhite,
                          fontSize: 20,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                    _buildFeaturedCarousel(),
                    const SizedBox(height: 32),
                  ],
                ),
              ),

              // Search Bar & Filters Header
              SliverToBoxAdapter(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20.0, vertical: 8.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            AppLocalizations.instance.isEnglish ? "City Guides" : "Şehir Rehberleri",
                            style: GoogleFonts.poppins(
                              color: WanderlustColors.textWhite,
                              fontSize: 28,
                              fontWeight: FontWeight.w500,
                              letterSpacing: -0.5,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 16),
                      // Search Bar
                      Container(
                        decoration: BoxDecoration(
                          color: WanderlustColors.bgCard,
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(
                            color: WanderlustColors.borderLight,
                          ),
                        ),
                        child: TextField(
                          controller: _searchController,
                          focusNode: _searchFocusNode,
                          onChanged: _filterCities,
                          style: GoogleFonts.poppins(color: WanderlustColors.textWhite, fontSize: 16),
                          decoration: InputDecoration(
                            hintText: AppLocalizations.instance.isEnglish 
                              ? "Search cities..." 
                              : "Şehir ara...",
                            hintStyle: GoogleFonts.poppins(
                              color: WanderlustColors.textGreyLight,
                              fontSize: 16,
                            ),
                            prefixIcon: Icon(
                              Icons.search_rounded,
                              color: WanderlustColors.textGrey,
                              size: 22,
                            ),
                            suffixIcon: _searchQuery.isNotEmpty
                              ? IconButton(
                                  icon: Icon(
                                    Icons.close_rounded,
                                    color: WanderlustColors.textGrey,
                                    size: 20,
                                  ),
                                  onPressed: () {
                                    _searchController.clear();
                                    _filterCities('');
                                    _searchFocusNode.unfocus();
                                  },
                                )
                              : null,
                            border: InputBorder.none,
                            contentPadding: const EdgeInsets.symmetric(
                              horizontal: 16,
                              vertical: 14,
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(height: 24),
                    ],
                  ),
                ),
              ),

              // Cities Grid
              _isLoading
                  ? SliverToBoxAdapter(child: _buildShimmerGrid())
                  : _filteredCities.isEmpty
                    ? SliverToBoxAdapter(
                        child: Padding(
                          padding: const EdgeInsets.all(40),
                          child: Column(
                            children: [
                              Icon(
                                Icons.search_off_rounded,
                                size: 64,
                                color: WanderlustColors.textGreyLight,
                              ),
                              const SizedBox(height: 16),
                              Text(
                                AppLocalizations.instance.isEnglish 
                                  ? "No cities found" 
                                  : "Şehir bulunamadı",
                                style: GoogleFonts.poppins(
                                  color: WanderlustColors.textGrey,
                                  fontSize: 18,
                                ),
                              ),
                            ],
                          ),
                        ),
                      )
                    : _buildEditorialSliver(),
              
                  const SliverToBoxAdapter(child: SizedBox(height: 80)),
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
                          color: WanderlustColors.bgCard.withOpacity(0.8),
                          shape: BoxShape.circle,
                          border: Border.all(color: WanderlustColors.borderLight),
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
          ),
        ),
      ),
    );
  }

  /// Kart başına deterministik, çok hafif "masaya bırakılmış fotoğraf" eğimi.
  void _openCity(Map<String, dynamic> cityData) {
    HapticFeedback.lightImpact();

    // --- ANALYTICS: Guide Selection ---
    AnalyticsService.instance.logSelectContent(
      contentType: 'guide',
      itemId: cityData['city'],
    );

    final cityName = cityData['city'].toString().toLowerCase();
    final bool isAmsterdam = cityName == 'amsterdam';

    Navigator.push(
      context,
      PageRouteBuilder(
        transitionDuration: const Duration(milliseconds: 400),
        reverseTransitionDuration: const Duration(milliseconds: 350),
        pageBuilder: (context, animation, secondaryAnimation) {
          if (isAmsterdam) {
            return const AmsterdamGuideScreen(citySlug: 'amsterdam');
          }
          return CityGuideDetailScreen(
            city: cityData['city'],
            imageUrl: cityData['imageUrl'],
          );
        },
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          // Apple tarzı scale + fade animasyonu
          final scaleAnimation = Tween<double>(begin: 0.85, end: 1.0).animate(
            CurvedAnimation(parent: animation, curve: Curves.easeOutCubic),
          );
          final fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
            CurvedAnimation(parent: animation, curve: const Interval(0.0, 0.6, curve: Curves.easeOut)),
          );
          return FadeTransition(
            opacity: fadeAnimation,
            child: ScaleTransition(
              scale: scaleAnimation,
              child: child,
            ),
          );
        },
      ),
    );
  }

  // ── Akordeon liste düzeni ────────────────────────────────────────────────
  // Şehirler alt alta geniş barlar; dokununca bar büyür ve fotoğraf sahneye
  // çıkar. Genişken tekrar dokunmak rehberi açar. Aynı anda tek bar açık.

  static const double _barCollapsedHeight = 64;
  static const double _barExpandedHeight = 270;
  int? _expandedIndex; // hepsi kapalı başlar

  Widget _buildEditorialSliver() {
    return SliverPadding(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      sliver: SliverList(
        delegate: SliverChildBuilderDelegate(
          (context, index) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: _EntranceReveal(
                delayMs: 30 * (index % 6),
                child: _buildExpandableBar(_filteredCities[index], index),
              ),
            );
          },
          childCount: _filteredCities.length,
        ),
      ),
    );
  }

  Widget _buildExpandableBar(Map<String, dynamic> cityData, int index) {
    final bool expanded = _expandedIndex == index;

    return GestureDetector(
      onTap: () {
        if (expanded) {
          _openCity(cityData);
        } else {
          HapticFeedback.selectionClick();
          setState(() => _expandedIndex = index);
        }
      },
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 420),
        curve: Curves.easeOutCubic,
        height: expanded ? _barExpandedHeight : _barCollapsedHeight,
        child: ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: Stack(
            fit: StackFit.expand,
            children: [
              // Görsel — kapalıyken statik ve loş, açıkken canlanır
              _livingImage(
                seed: index,
                active: expanded,
                child: Hero(
                  tag: 'guide_img_${cityData['city']}',
                  child: ResilientNetworkImage(
                    imageUrl: cityData['imageUrl'] as String?,
                    placeName: cityData['city']?.toString() ?? 'guide',
                    city: cityData['city']?.toString() ?? '',
                    category: 'guide',
                    fit: BoxFit.cover,
                    memCacheWidth: 900,
                    memCacheHeight: 700,
                    placeholderBuilder: (_) =>
                        Container(color: WanderlustColors.bgCardLight),
                  ),
                ),
              ),
              // Kapalı bar: koyu perde; açık kart: sinematik scrim
              AnimatedContainer(
                duration: const Duration(milliseconds: 420),
                curve: Curves.easeOutCubic,
                decoration: BoxDecoration(
                  color: expanded
                      ? Colors.transparent
                      : Colors.black.withValues(alpha: 0.45),
                  gradient: expanded
                      ? LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.black.withValues(alpha: 0.08),
                            Colors.transparent,
                            Colors.black.withValues(alpha: 0.28),
                            Colors.black.withValues(alpha: 0.62),
                          ],
                          stops: const [0.0, 0.42, 0.72, 1.0],
                        )
                      : null,
                ),
              ),
              // Kapalı durum içeriği: ad + genişletme ipucu
              AnimatedOpacity(
                duration: const Duration(milliseconds: 250),
                opacity: expanded ? 0 : 1,
                child: IgnorePointer(
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 18),
                    child: Row(
                      children: [
                        Expanded(
                          child: Text(
                            cityData['city'],
                            maxLines: 1,
                            overflow: TextOverflow.ellipsis,
                            style: GoogleFonts.poppins(
                              color: Colors.white,
                              fontSize: 16.5,
                              fontWeight: FontWeight.w600,
                              letterSpacing: 0.2,
                            ),
                          ),
                        ),
                        Icon(
                          Icons.unfold_more_rounded,
                          color: Colors.white.withValues(alpha: 0.7),
                          size: 20,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
              // Açık durum içeriği: büyük ad + alt yazı + frosted ok
              AnimatedOpacity(
                duration: const Duration(milliseconds: 300),
                opacity: expanded ? 1 : 0,
                child: IgnorePointer(
                  child: Padding(
                    padding: const EdgeInsets.fromLTRB(20, 0, 16, 16),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.end,
                      children: [
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.end,
                          children: [
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    cityData['city'],
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: GoogleFonts.poppins(
                                      color: Colors.white,
                                      fontSize: 27,
                                      fontWeight: FontWeight.w700,
                                      height: 1.05,
                                      letterSpacing: -0.3,
                                    ),
                                  ),
                                  const SizedBox(height: 4),
                                  Text(
                                    cityData['subtitle'],
                                    maxLines: 1,
                                    overflow: TextOverflow.ellipsis,
                                    style: GoogleFonts.poppins(
                                      color:
                                          Colors.white.withValues(alpha: 0.85),
                                      fontSize: 12.5,
                                      fontWeight: FontWeight.w400,
                                      letterSpacing: 0.3,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(width: 12),
                            _frostedArrow(),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  /// Görsele yumuşak bir zoom + gezinme hareketi verir.
  /// [active] false iken görsel statik durur; geçiş [amp] üzerinden yumuşak
  /// şekilde açılıp kapanır, böylece bar açılırken sıçrama olmaz.
  /// [seed] karta özgü faz kayması üretir; tam tur sin/cos kullanıldığı için
  /// döngü dikişsizdir.
  Widget _livingImage({
    required Widget child,
    required int seed,
    bool active = true,
  }) {
    final phase = (seed % 9) * 0.73;
    return TweenAnimationBuilder<double>(
      tween: Tween(end: active ? 1.0 : 0.0),
      duration: const Duration(milliseconds: 700),
      curve: Curves.easeInOut,
      child: child,
      builder: (context, amp, c) {
        if (amp == 0) {
          // Kapalı bar: hareketsiz, hafif zoom'lu (kadrajı doldurur)
          return Transform.scale(scale: 1.08, child: c);
        }
        return AnimatedBuilder(
          animation: _kenBurnsController,
          builder: (context, c2) {
            final t = _kenBurnsController.value * 2 * math.pi;
            final scale = 1.08 + amp * (0.06 + 0.06 * math.sin(t + phase));
            final dx = amp * 6.0 * math.sin(t + phase + 1.7);
            final dy = amp * 4.5 * math.cos(t + phase * 1.3);
            return Transform.translate(
              offset: Offset(dx, dy),
              child: Transform.scale(scale: scale, child: c2),
            );
          },
          child: c,
        );
      },
    );
  }

  /// Buzlu cam ok çipi — açık kartın davet eden köşesi.
  Widget _frostedArrow() {
    return ClipOval(
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
        child: Container(
          width: 42,
          height: 42,
          decoration: BoxDecoration(
            color: Colors.white.withValues(alpha: 0.18),
            shape: BoxShape.circle,
            border: Border.all(color: Colors.white.withValues(alpha: 0.35)),
          ),
          child: const Icon(
            Icons.arrow_forward_rounded,
            color: Colors.white,
            size: 20,
          ),
        ),
      ),
    );
  }

  // Featured Items Getter
  List<Map<String, String>> get _featuredItems {
    final isEnglish = AppLocalizations.instance.isEnglish;
    final defaults = _defaultFeaturedCards(isEnglish);

    // Önce Remote Config'den oku ve değerleri doğrula
    final remoteCards = RemoteConfigService.instance.featuredCards;
    if (remoteCards.isNotEmpty) {
      final fallbackById = {
        for (final card in defaults) if ((card['id'] ?? '').isNotEmpty) card['id']!: card,
      };

      final sanitized = <Map<String, String>>[];
      for (final card in remoteCards) {
        final id = card['id']?.toString().trim();
        if (id == null || id.isEmpty) continue;

        final fallback = fallbackById[id];
        final map = <String, String>{
          'id': id,
          'title': _valueOrFallback(
            primary: isEnglish ? card['title_en']?.toString() : card['title_tr']?.toString(),
            fallback: fallback?['title'],
          ),
          'subtitle': _valueOrFallback(
            primary: isEnglish ? card['subtitle_en']?.toString() : card['subtitle_tr']?.toString(),
            fallback: fallback?['subtitle'],
          ),
          'image': _valueOrFallback(
            primary: card['image']?.toString(),
            fallback: fallback?['image'],
          ),
          'tag': _valueOrFallback(
            primary: isEnglish ? card['tag_en']?.toString() : card['tag_tr']?.toString(),
            fallback: fallback?['tag'],
          ),
        };

        if (map['image']!.isEmpty) {
          // Hâlâ görsel yoksa bu kartı atla ki boş kutu gösterilmesin
          continue;
        }

        sanitized.add(map);
      }

      if (sanitized.isNotEmpty) {
        return sanitized;
      }
    }

    // Remote Config boş veya eksikse fallback'e dön
    return defaults;
  }

  List<Map<String, String>> _defaultFeaturedCards(bool isEnglish) => [
        {
          "id": "summer_routes",
          "title": isEnglish ? "Summer Escapes" : "Yazlık Rotalar",
          "subtitle": isEnglish
              ? "The sunniest coasts and beaches in the app."
              : "Uygulamadaki en güneşli kıyılar ve plajlar.",
          "image":
              "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80",
          "tag": isEnglish ? "SUMMER" : "YAZLIK",
        },
        {
          "id": "hidden_gems",
          "title": isEnglish ? "Europe's Hidden Gems" : "Avrupa'nın Gizli Hazineleri",
          "subtitle": isEnglish
              ? "Places waiting to be discovered away from crowds."
              : "Kalabalıktan uzak, keşfedilmeyi bekleyen yerler.",
          "image":
              "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=800&q=80",
          "tag": isEnglish ? "DISCOVER" : "KEŞFET",
        },
        {
          "id": "gastronomy",
          "title": isEnglish ? "For Gastronomy Lovers" : "Gastronomi Tutkunları İçin",
          "subtitle": isEnglish
              ? "From Michelin stars to street food."
              : "Michelin yıldızlı restoranlardan sokak lezzetlerine.",
          "image":
              "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80",
          "tag": isEnglish ? "TREND" : "TREND",
        },
        {
          "id": "romantic",
          "title": isEnglish ? "Romantic Getaways" : "Romantik Haftasonu Kaçamakları",
          "subtitle": isEnglish
              ? "Unforgettable moments with your loved one."
              : "Sevgilinizle unutulmaz anlar yaşayın.",
          "image":
              "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
          "tag": isEnglish ? "ROMANTIC" : "ROMANTİK",
        },
      ];

  String _valueOrFallback({String? primary, String? fallback}) {
    final trimmed = primary?.trim();
    if (trimmed != null && trimmed.isNotEmpty) return trimmed;
    return (fallback ?? '').trim();
  }

  void _openArticle(Map<String, String> item) {
    HapticFeedback.lightImpact();

    // --- ANALYTICS: Featured Guide Selection ---
    AnalyticsService.instance.logSelectContent(
      contentType: 'featured_guide',
      itemId: item['id']!,
    );

    Navigator.push(
      context,
      PageRouteBuilder(
        transitionDuration: const Duration(milliseconds: 400),
        reverseTransitionDuration: const Duration(milliseconds: 350),
        pageBuilder: (context, animation, secondaryAnimation) =>
            GuideArticleScreen(
          articleId: item['id']!,
          title: item['title']!,
          imageUrl: item['image']!,
        ),
        transitionsBuilder: (context, animation, secondaryAnimation, child) {
          final scaleAnimation = Tween<double>(begin: 0.9, end: 1.0).animate(
            CurvedAnimation(parent: animation, curve: Curves.easeOutCubic),
          );
          final fadeAnimation = Tween<double>(begin: 0.0, end: 1.0).animate(
            CurvedAnimation(parent: animation, curve: Curves.easeOut),
          );
          return FadeTransition(
            opacity: fadeAnimation,
            child: ScaleTransition(
              scale: scaleAnimation,
              child: child,
            ),
          );
        },
      ),
    );
  }

  // ── Vitrin carousel ──────────────────────────────────────────────────────
  // Sayfa sayfa kayan sinematik kartlar: komşu kartın ucu görünerek kaydırmaya
  // davet eder, aktif kart tam parlaklıkta öne çıkar, kaydırırken görsel ters
  // yönde paralaks yapar.

  Widget _buildFeaturedCarousel() {
    final items = _featuredItems;
    return Column(
      children: [
        SizedBox(
          height: 200,
          child: Padding(
            padding: const EdgeInsets.only(left: 20),
            child: PageView.builder(
              controller: _featuredController,
              physics: const BouncingScrollPhysics(),
              padEnds: false,
              itemCount: items.length,
              itemBuilder: (context, index) =>
                  _buildFeaturedCard(items[index], index),
            ),
          ),
        ),
        const SizedBox(height: 14),
        // Sayfa göstergesi — aktif nokta hap şekline uzar
        AnimatedBuilder(
          animation: _featuredController,
          builder: (context, _) {
            final page = _featuredController.hasClients &&
                    _featuredController.position.haveDimensions
                ? _featuredController.page ?? 0
                : 0.0;
            return Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: List.generate(items.length, (i) {
                final closeness = (1 - (page - i).abs()).clamp(0.0, 1.0);
                return AnimatedContainer(
                  duration: const Duration(milliseconds: 100),
                  margin: const EdgeInsets.symmetric(horizontal: 3),
                  width: 6 + 14 * closeness,
                  height: 6,
                  decoration: BoxDecoration(
                    color: Color.lerp(
                      WanderlustColors.textGrey.withValues(alpha: 0.35),
                      WanderlustColors.accent,
                      closeness,
                    ),
                    borderRadius: BorderRadius.circular(3),
                  ),
                );
              }),
            );
          },
        ),
      ],
    );
  }

  Widget _buildFeaturedCard(Map<String, String> item, int index) {
    return AnimatedBuilder(
      animation: _featuredController,
      builder: (context, child) {
        final page = _featuredController.hasClients &&
                _featuredController.position.haveDimensions
            ? _featuredController.page ?? 0
            : 0.0;
        final delta = (index - page).clamp(-1.0, 1.0);
        // Uzak kart hafifçe küçülür ve kararır; görsel ters yöne süzülür
        final scale = 1 - 0.05 * delta.abs();
        final dim = 0.30 * delta.abs();
        final parallax = delta * -34.0;

        return Transform.scale(
          scale: scale,
          child: GestureDetector(
            onTap: () => _openArticle(item),
            child: Container(
              margin: const EdgeInsets.only(right: 14),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.25),
                    blurRadius: 12,
                    offset: const Offset(0, 5),
                  ),
                ],
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Stack(
                  fit: StackFit.expand,
                  children: [
                    // Paralaks görsel — kadraj taşmasın diye hafif zoom'lu
                    Positioned.fill(
                      child: Transform.translate(
                        offset: Offset(parallax, 0),
                        child: Transform.scale(
                          scale: 1.18,
                          child: ResilientNetworkImage(
                            imageUrl: item['image'],
                            placeName: item['title'] ?? 'featured',
                            city: '',
                            category: 'article',
                            fit: BoxFit.cover,
                            placeholderBuilder: (_) =>
                                Container(color: const Color(0xFF1E1E2C)),
                          ),
                        ),
                      ),
                    ),
                    // Sinematik scrim
                    Positioned.fill(
                      child: DecoratedBox(
                        decoration: BoxDecoration(
                          gradient: LinearGradient(
                            begin: Alignment.topCenter,
                            end: Alignment.bottomCenter,
                            colors: [
                              Colors.black.withValues(alpha: 0.12),
                              Colors.transparent,
                              Colors.black.withValues(alpha: 0.35),
                              Colors.black.withValues(alpha: 0.72),
                            ],
                            stops: const [0.0, 0.38, 0.68, 1.0],
                          ),
                        ),
                      ),
                    ),
                    // Buzlu cam etiket — sol üst
                    Positioned(
                      top: 14,
                      left: 14,
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(20),
                        child: BackdropFilter(
                          filter: ImageFilter.blur(sigmaX: 8, sigmaY: 8),
                          child: Container(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 10, vertical: 5),
                            decoration: BoxDecoration(
                              color: Colors.white.withValues(alpha: 0.16),
                              borderRadius: BorderRadius.circular(20),
                              border: Border.all(
                                color: Colors.white.withValues(alpha: 0.3),
                              ),
                            ),
                            child: Text(
                              item['tag']!,
                              style: GoogleFonts.poppins(
                                color: Colors.white,
                                fontSize: 10,
                                fontWeight: FontWeight.w600,
                                letterSpacing: 1.2,
                              ),
                            ),
                          ),
                        ),
                      ),
                    ),
                    // Başlık + alt yazı + davet eden ok
                    Positioned(
                      left: 16,
                      right: 14,
                      bottom: 14,
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: [
                          Expanded(
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  item['title']!,
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: GoogleFonts.poppins(
                                    color: Colors.white,
                                    fontSize: 20,
                                    fontWeight: FontWeight.w700,
                                    height: 1.12,
                                    letterSpacing: -0.2,
                                  ),
                                ),
                                const SizedBox(height: 3),
                                Text(
                                  item['subtitle']!,
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: GoogleFonts.poppins(
                                    color: Colors.white.withValues(alpha: 0.82),
                                    fontSize: 11.5,
                                    fontWeight: FontWeight.w400,
                                    height: 1.25,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 10),
                          _frostedArrow(),
                        ],
                      ),
                    ),
                    // Kenardaki kartlar hafifçe kararır — aktif kart öne çıkar
                    Positioned.fill(
                      child: IgnorePointer(
                        child: ColoredBox(
                          color: Colors.black.withValues(alpha: dim),
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        );
      },
    );
  }

  Widget _buildShimmerGrid() {
    Widget bar(double height) => Container(
          height: height,
          margin: const EdgeInsets.only(bottom: 10),
          decoration: BoxDecoration(
            color: WanderlustColors.bgCard,
            borderRadius: BorderRadius.circular(16),
          ),
        );

    // Akordeon ritmi taklit eden placeholder: kapalı barlar
    return Shimmer.fromColors(
      baseColor: WanderlustColors.bgCardLight,
      highlightColor: WanderlustColors.bgCard,
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 20),
        child: Column(
          children: [
            for (int i = 0; i < 8; i++) bar(_barCollapsedHeight),
          ],
        ),
      ),
    );
  }
}

/// Liste öğeleri görünür olduklarında yumuşak fade + yukarı kayma ile gelir.
class _EntranceReveal extends StatefulWidget {
  final Widget child;
  final int delayMs;

  const _EntranceReveal({required this.child, this.delayMs = 0});

  @override
  State<_EntranceReveal> createState() => _EntranceRevealState();
}

class _EntranceRevealState extends State<_EntranceReveal>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller;
  late final Animation<double> _fade;
  late final Animation<Offset> _slide;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 550),
    );
    _fade = CurvedAnimation(parent: _controller, curve: Curves.easeOut);
    _slide = Tween<Offset>(
      begin: const Offset(0, 0.06),
      end: Offset.zero,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeOutCubic));

    Future.delayed(Duration(milliseconds: widget.delayMs), () {
      if (mounted) _controller.forward();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _fade,
      child: SlideTransition(position: _slide, child: widget.child),
    );
  }
}
