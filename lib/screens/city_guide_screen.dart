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
import '../widgets/resilient_network_image.dart';

class CityGuideScreen extends StatefulWidget {
  const CityGuideScreen({super.key});

  @override
  State<CityGuideScreen> createState() => _CityGuideScreenState();
}

class _CityGuideScreenState extends State<CityGuideScreen> {
  List<Map<String, dynamic>> _cities = [];
  List<Map<String, dynamic>> _filteredCities = [];
  bool _isLoading = true;
  String _searchQuery = '';
  final TextEditingController _searchController = TextEditingController();
  final FocusNode _searchFocusNode = FocusNode();
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;
  Timer? _searchTimer; // Added for debouncing analytics

  @override
  void initState() {
    super.initState();
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
    final cities = AIService.getAllCitiesForGuide(isEnglish);

    setState(() {
      _cities = cities;
      _filteredCities = cities;
      _isLoading = false;
    });
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
                    : SliverPadding(
                        padding: const EdgeInsets.symmetric(horizontal: 20),
                        sliver: SliverGrid(
                          delegate: SliverChildBuilderDelegate(
                            (context, index) {
                              final city = _filteredCities[index];
                              return _buildCityCard(city);
                            },
                            childCount: _filteredCities.length,
                          ),
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: 2,
                            childAspectRatio: 0.75, // Dikey kartlar
                            crossAxisSpacing: 16,
                            mainAxisSpacing: 16,
                          ),
                        ),
                      ),
              
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

  Widget _buildCityCard(Map<String, dynamic> cityData) {
    return GestureDetector(
      onTap: () {
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
      },
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.2),
              blurRadius: 8,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: Stack(
            fit: StackFit.expand,
            children: [
              Positioned.fill(
                child: Hero(
                  tag: 'guide_img_${cityData['city']}',
                  child: ResilientNetworkImage(
                    imageUrl: cityData['imageUrl'] as String?,
                    placeName: cityData['city']?.toString() ?? 'guide',
                    city: cityData['city']?.toString() ?? '',
                    category: 'guide',
                    fit: BoxFit.cover,
                    memCacheWidth: 800,
                    memCacheHeight: 600,
                    placeholderBuilder: (_) =>
                        Container(color: WanderlustColors.bgCardLight),
                  ),
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
                        Colors.black.withValues(alpha: 0.3),
                        Colors.black.withValues(alpha: 0.9),
                      ],
                      stops: const [0.4, 0.7, 1.0],
                    ),
                  ),
                ),
              ),

              // Content
              Padding(
                padding: const EdgeInsets.all(12.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      cityData['city'],
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      cityData['subtitle'],
                      maxLines: 2,
                      overflow: TextOverflow.ellipsis,
                      style: GoogleFonts.poppins(
                        color: Colors.white.withValues(alpha: 0.8),
                        fontSize: 12,
                        fontWeight: FontWeight.w400,
                      ),
                    ),
                  ],
                ),
              ),
            ],
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

  Widget _buildFeaturedCarousel() {
    return SizedBox(
      height: 220,
      child: ListView.builder(
        padding: const EdgeInsets.symmetric(horizontal: 20),
        scrollDirection: Axis.horizontal,
        physics: const BouncingScrollPhysics(),
        itemCount: _featuredItems.length,
        itemBuilder: (context, index) {
          final item = _featuredItems[index];
          return _buildFeaturedCard(item);
        },
      ),
    );
  }

  Widget _buildFeaturedCard(Map<String, String> item) {
    return GestureDetector(
      onTap: () {
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
            pageBuilder: (context, animation, secondaryAnimation) => GuideArticleScreen(
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
      },
      child: Container(
        width: 280,
        margin: const EdgeInsets.only(right: 16),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.3),
              blurRadius: 10,
              offset: const Offset(0, 4),
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
                imageUrl: item['image'],
                placeName: item['title'] ?? 'featured',
                city: '',
                category: 'article',
                width: 280,
                height: 220,
                fit: BoxFit.cover,
                placeholderBuilder: (_) =>
                    Container(color: const Color(0xFF1E1E2C)),
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
                      Colors.black.withValues(alpha: 0.2),
                      Colors.black.withValues(alpha: 0.8),
                    ],
                    stops: const [0.3, 0.6, 1.0],
                  ),
                ),
              ),
            ),

            // Content
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  // Tag
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: WanderlustColors.accent,
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      item['tag']!,
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.5,
                      ),
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    item['title']!,
                    style: GoogleFonts.poppins(
                      color: Colors.white,
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    item['subtitle']!,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: GoogleFonts.poppins(
                      color: Colors.white.withValues(alpha: 0.8),
                      fontSize: 12,
                      fontWeight: FontWeight.w400,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    ),
  );
}

  Widget _buildShimmerGrid() {
    return Shimmer.fromColors(
      baseColor: WanderlustColors.bgCardLight,
      highlightColor: WanderlustColors.bgCard,
      child: GridView.builder(
        shrinkWrap: true,
        physics: const NeverScrollableScrollPhysics(),
        padding: const EdgeInsets.symmetric(horizontal: 20),
        itemCount: 6,
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          childAspectRatio: 0.75,
          crossAxisSpacing: 16,
          mainAxisSpacing: 16,
        ),
        itemBuilder: (context, index) {
          return Container(
            decoration: BoxDecoration(
              color: WanderlustColors.bgCard,
              borderRadius: BorderRadius.circular(16),
            ),
          );
        },
      ),
    );
  }
}
