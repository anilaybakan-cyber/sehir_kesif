import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:shimmer/shimmer.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import 'city_guide_detail_screen.dart';
import 'guide_article_screen.dart';
import '../theme/wanderlust_colors.dart';

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
                          color: Colors.white.withValues(alpha: 0.7),
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
                          color: Colors.white.withValues(alpha: 0.9),
                          fontSize: 20,
                          fontWeight: FontWeight.bold,
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
                              color: Colors.white,
                              fontSize: 28,
                              fontWeight: FontWeight.bold,
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
                            color: const Color(0xFF2C2C4E).withOpacity(0.5),
                          ),
                        ),
                        child: TextField(
                          controller: _searchController,
                          focusNode: _searchFocusNode,
                          onChanged: _filterCities,
                          style: GoogleFonts.poppins(color: Colors.white, fontSize: 16),
                          decoration: InputDecoration(
                            hintText: AppLocalizations.instance.isEnglish 
                              ? "Search cities..." 
                              : "Şehir ara...",
                            hintStyle: GoogleFonts.poppins(
                              color: Colors.white.withValues(alpha: 0.4),
                              fontSize: 16,
                            ),
                            prefixIcon: Icon(
                              Icons.search_rounded,
                              color: Colors.white.withValues(alpha: 0.5),
                              size: 22,
                            ),
                            suffixIcon: _searchQuery.isNotEmpty
                              ? IconButton(
                                  icon: Icon(
                                    Icons.close_rounded,
                                    color: Colors.white.withValues(alpha: 0.5),
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
                                color: Colors.white.withValues(alpha: 0.3),
                              ),
                              const SizedBox(height: 16),
                              Text(
                                AppLocalizations.instance.isEnglish 
                                  ? "No cities found" 
                                  : "Şehir bulunamadı",
                                style: GoogleFonts.poppins(
                                  color: Colors.white.withValues(alpha: 0.5),
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
                          border: Border.all(color: const Color(0xFF2C2C4E).withOpacity(0.5)),
                        ),
                        child: const Icon(
                          Icons.keyboard_arrow_up_rounded,
                          color: Color(0xFF9E9E9E), // TextGrey equivalent
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
        Navigator.push(
          context,
          PageRouteBuilder(
            transitionDuration: const Duration(milliseconds: 400),
            reverseTransitionDuration: const Duration(milliseconds: 350),
            pageBuilder: (context, animation, secondaryAnimation) => CityGuideDetailScreen(
              city: cityData['city'],
              imageUrl: cityData['imageUrl'],
            ),
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
              // Background Image
              Hero(
                tag: 'guide_img_${cityData['city']}',
                  child: Image.network(
                  cityData['imageUrl'],
                  fit: BoxFit.cover,
                  cacheWidth: 800, // Optimize memory decode size
                  loadingBuilder: (context, child, loadingProgress) {
                    if (loadingProgress == null) return child;
                    return Container(color: const Color(0xFF1E1E2C));
                  },
                  errorBuilder: (context, error, stackTrace) {
                    return Container(
                      color: const Color(0xFF1E1E2C),
                      child: const Icon(Icons.image_not_supported, color: Colors.white24),
                    );
                  },
                ),
              ),
              
              // Gradient Overlay
              Container(
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
    return [
      {
        "id": "winter_routes",
        "title": isEnglish ? "Top 5 Winter Routes" : "Kış Tatili İçin En İyi 5 Rota",
        "subtitle": isEnglish ? "From snowy mountains to cozy fireplaces..." : "Karlı dağlardan sıcak şöminelere...",
        "image": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?q=80&w=2070&auto=format&fit=crop",
        "tag": isEnglish ? "SEASONAL" : "SEZONLUK",
      },
      {
        "id": "hidden_gems",
        "title": isEnglish ? "Europe's Hidden Gems" : "Avrupa'nın Gizli Hazineleri",
        "subtitle": isEnglish ? "Places waiting to be discovered away from crowds." : "Kalabalıktan uzak, keşfedilmeyi bekleyen yerler.",
        "image": "https://images.unsplash.com/photo-1519677100203-a0e668c92439?q=80&w=2072&auto=format&fit=crop",
        "tag": isEnglish ? "DISCOVER" : "KEŞFET",
      },
      {
        "id": "gastronomy",
        "title": isEnglish ? "For Gastronomy Lovers" : "Gastronomi Tutkunları İçin",
        "subtitle": isEnglish ? "From Michelin stars to street food." : "Michelin yıldızlı restoranlardan sokak lezzetlerine.",
        "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=2070&auto=format&fit=crop",
        "tag": isEnglish ? "TREND" : "TREND",
      },
      {
        "id": "romantic",
        "title": isEnglish ? "Romantic Getaways" : "Romantik Haftasonu Kaçamakları",
        "subtitle": isEnglish ? "Unforgettable moments with your loved one." : "Sevgilinizle unutulmaz anlar yaşayın.",
        "image": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?q=80&w=2073&auto=format&fit=crop",
        "tag": isEnglish ? "ROMANTIC" : "ROMANTİK",
      },
    ];
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
        margin: const EdgeInsets.only(right: 16), // Bottom margin removed to prevent clipping if any
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
            // Image
            CachedNetworkImage(
              imageUrl: item['image']!,
              fit: BoxFit.cover,
              placeholder: (context, url) => Container(color: const Color(0xFF1E1E2C)),
              errorWidget: (context, url, error) => Container(color: const Color(0xFF1E1E2C)),
            ),
            
            // Gradient Overlay
            Container(
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
                      fontSize: 18,
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
      baseColor: const Color(0xFF1E1E2C),
      highlightColor: const Color(0xFF2D2D44),
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
              color: Colors.white,
              borderRadius: BorderRadius.circular(16),
            ),
          );
        },
      ),
    );
  }
}
