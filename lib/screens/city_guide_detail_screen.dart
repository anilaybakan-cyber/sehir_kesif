import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import '../theme/wanderlust_colors.dart';
import 'detail_screen.dart';
import 'dart:ui';
import '../services/premium_service.dart';
import 'paywall_screen.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../widgets/resilient_network_image.dart';
import '../services/image_prefetch_service.dart';
import '../utils/image_utils.dart';

class _GuideSectionVisual {
  final List<String> imageUrls;

  const _GuideSectionVisual({
    required this.imageUrls,
  });

  String get imageUrl => imageUrls.first;
}

class CityGuideDetailScreen extends StatefulWidget {
  final String city;
  final String imageUrl;

  const CityGuideDetailScreen({
    super.key,
    required this.city,
    required this.imageUrl,
  });

  @override
  State<CityGuideDetailScreen> createState() => _CityGuideDetailScreenState();
}

class _CityGuideDetailScreenState extends State<CityGuideDetailScreen> {
  String _content = "";
  bool _isLoading = true;
  List<Highlight> _guideHighlights = [];
  String? _guideHeroImageUrl;
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;
  bool _showStickyButton = false;
  double _scrollOffset = 0;
  bool _isNavigating = false;
  final GlobalKey _triggerKey = GlobalKey();
  final Map<String, Highlight> _highlightMap = {};

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  void initState() {
    super.initState();
    _loadAllCityHighlights();
    _scrollController.addListener(() {
      // Scroll offset for UI effects
      if (_scrollController.offset != _scrollOffset) {
        setState(() => _scrollOffset = _scrollController.offset);
      }

      // Back to top button logic
      final showTop = _scrollController.offset > 200;
      if (showTop != _showScrollToTop) {
        setState(() => _showScrollToTop = showTop);
      }

      // Sticky button logic
      if (!PremiumService.instance.isPremium) {
        _checkStickyButtonVisibility();
      }
    });

    _loadContent();
  }

  void _checkStickyButtonVisibility() {
    try {
      final context = _triggerKey.currentContext;
      if (context == null) return;

      final RenderBox? renderBox = context.findRenderObject() as RenderBox?;
      if (renderBox != null) {
        final position = renderBox.localToGlobal(Offset.zero);
        final screenHeight = MediaQuery.of(context).size.height;
        
        // Show button as soon as the trigger point enters the bottom half of the screen
        final bool showSticky = position.dy < (screenHeight - 100);
        
        if (showSticky != _showStickyButton) {
          setState(() => _showStickyButton = showSticky);
        }
      }
    } catch (e) {
      // Logic might fail during layout transitions, ignore
    }
  }

  Future<void> _loadAllCityHighlights() async {
    final allCities = CityDataLoader.supportedCities;
    for (var cityId in allCities) {
      try {
        final cityModel = await CityDataLoader.loadCity(cityId);
        for (var h in cityModel.highlights) {
          _highlightMap[h.name.toLowerCase().trim()] = h;
        }
      } catch (_) {}
    }
    if (mounted) setState(() {});
  }

  Highlight? _findHighlight(String query) {
    final cleanQuery = query.toLowerCase().trim();
    if (_highlightMap.containsKey(cleanQuery)) {
      return _highlightMap[cleanQuery];
    }
    for (var entry in _highlightMap.entries) {
      if (entry.key.contains(cleanQuery) || cleanQuery.contains(entry.key)) {
        return entry.value;
      }
    }
    return null;
  }

  Future<void> _loadContent() async {
    setState(() => _isLoading = true);
    
    final isEnglish = AppLocalizations.instance.isEnglish;
    final contentFuture = AIService.getCityBlogContent(widget.city, isEnglish);
    CityModel? cityModel;

    try {
      cityModel = await CityDataLoader.loadCity(widget.city);
    } catch (e) {
      debugPrint('Guide visuals loading error for ${widget.city}: $e');
    }

    final content = await contentFuture;

    if (mounted) {
      setState(() {
        _content = content;
        _guideHighlights = cityModel?.highlights.where((highlight) {
          final imageUrl = highlight.imageUrl?.trim() ?? '';
          return imageUrl.isNotEmpty;
        }).toList() ?? [];
        _guideHeroImageUrl = cityModel?.heroImage;
        _isLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: Stack(
        children: [
          CustomScrollView(
            controller: _scrollController,
            physics: const BouncingScrollPhysics(),
            slivers: [
              // AppBar (Fotoğraflı ve Sabit)
              SliverAppBar(
                expandedHeight: 320,
                collapsedHeight: 140, // Fotoğraf çok küçülmesin diye yüksek bir sınır
                toolbarHeight: 60,
                pinned: true,
                backgroundColor: WanderlustColors.bgDark,
                surfaceTintColor: Colors.transparent,
                foregroundColor: Colors.white,
                elevation: 0,
                leading: IconButton(
                  onPressed: () => Navigator.pop(context),
                  icon: Icon(
                    Icons.arrow_back_ios_new,
                    color: _scrollOffset > 150 ? WanderlustColors.textWhite : Colors.white,
                  ),
                ),
                title: Text(
                  widget.city.toUpperCase(),
                  style: GoogleFonts.poppins(
                    color: _scrollOffset > 150 ? WanderlustColors.textWhite : Colors.white,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 1.2,
                  ),
                ),
                flexibleSpace: LayoutBuilder(
                  builder: (context, constraints) {
                    final top = constraints.biggest.height;
                    // App bar'ın ne kadar küçüldüğünü hesaplıyoruz (140 civarına indiğinde collapsed say)
                    final isCollapsed = top <= 150;
                    
                    return Hero(
                      tag: 'guide_img_${widget.city}',
                      child: Stack(
                        fit: StackFit.expand,
                        children: [
                          Positioned.fill(
                            child: ResilientNetworkImage(
                              imageUrl: widget.imageUrl,
                              placeName: widget.city,
                              city: widget.city,
                              category: 'guide',
                              fit: BoxFit.cover,
                              memCacheWidth: 900,
                              memCacheHeight: 700,
                              placeholderBuilder: (_) =>
                                  Container(color: WanderlustColors.bgDark),
                            ),
                          ),
                          Positioned.fill(
                            child: Container(
                              color: Colors.black.withOpacity(0.35),
                            ),
                          ),
                          // Geçiş gradient'i (sadece tam açıkken veya yarı açıkken görünür)
                          if (!isCollapsed)
                            Positioned(
                              bottom: -1,
                              left: 0,
                              right: 0,
                              height: 100,
                              child: Container(
                                decoration: BoxDecoration(
                                  gradient: LinearGradient(
                                    begin: Alignment.topCenter,
                                    end: Alignment.bottomCenter,
                                    colors: [
                                      WanderlustColors.bgDark.withOpacity(0.0),
                                      WanderlustColors.bgDark,
                                    ],
                                  ),
                                ),
                              ),
                            ),
                        ],
                      ),
                    );
                  },
                ),
              ),

              // Content
              SliverToBoxAdapter(
                child: Container(
                  padding: const EdgeInsets.all(24),
                  decoration: const BoxDecoration(
                    color: WanderlustColors.bgDark,
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Blog İçeriği
                      _isLoading
                          ? const Center(child: CircularProgressIndicator(color: WanderlustColors.accent))
                          : _buildMarkdownContent(_content),
                      
                      const SizedBox(height: 100), // Extra space for sticky button
                    ],
                  ),
                ),
              ),
            ],
          ),
          
          // Sticky Unlock Button
          if (!PremiumService.instance.isPremium)
            _buildStickyUnlockButton(),

          if (_showScrollToTop)
            Positioned(
              right: 20,
              bottom: _showStickyButton ? 120 : 30, // Adjust based on sticky button
              child: AnimatedOpacity(
                opacity: _showScrollToTop ? 1.0 : 0.0,
                duration: const Duration(milliseconds: 200),
                child: GestureDetector(
                  onTap: () {
                     _scrollController.animateTo(0, duration: const Duration(milliseconds: 500), curve: Curves.easeOutCubic);
                  },
                  child: Container(
                    width: 44,
                    height: 44,
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard.withOpacity(0.8),
                      shape: BoxShape.circle,
                      border: Border.all(color: WanderlustColors.borderLight),
                    ),
                    child: const Icon(Icons.keyboard_arrow_up_rounded, color: WanderlustColors.textGrey, size: 28),
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }

  /// Çok basit bir "Markdown" renderer
  Widget _buildMarkdownContent(String rawContent) {
    final List<Widget> unlockedWidgets = [];
    final List<Widget> lockedWidgets = [];
    final lines = rawContent.split('\n');
    final isPremium = PremiumService.instance.isPremium;
    
    bool hasReachedTrigger = false;
    final triggerPhrases = [
      "Takviminizi Ayarlayın", 
      "Semt Rehberi",
      "Timing is Everything",
      "Neighborhood Guide",
      "Finding Your Base",
      "Why Now?"
    ];
    int sectionCount = 0;
    int insertedVisualCount = 0;
    final usedVisuals = <String>{};

    for (var line in lines) {
      final trimmedLine = line.trim();
      
      // Update section count for fallback
      if (trimmedLine.startsWith('## ') || trimmedLine.startsWith('### ')) {
        sectionCount++;
      }

      // Check for lock triggers
      if (!isPremium && !hasReachedTrigger) {
        // 1. Phrased based trigger
        for (var phrase in triggerPhrases) {
          if (trimmedLine.contains(phrase)) {
            hasReachedTrigger = true;
            break;
          }
        }

        // 2. Generic fallback: if we have more than 3 sections (headers), start blurring
        if (!hasReachedTrigger && sectionCount >= 3) {
          hasReachedTrigger = true;
        }
      }

      final targetList = hasReachedTrigger ? lockedWidgets : unlockedWidgets;
      
      // We want to apply the key to the VERY FIRST rendered widget of the locked section
      // regardless of its markdown type (H1, H2, paragraph, etc.)
      final bool shouldApplyKey = !isPremium && hasReachedTrigger && targetList.isEmpty && !trimmedLine.isEmpty;

      if (trimmedLine.isEmpty) {
        targetList.add(const SizedBox(height: 6));
        continue;
      }

      if (trimmedLine.startsWith('# ')) {
        // H1 Başlık
        String titleText = trimmedLine.substring(2);
        // Emojileri temizle
        titleText = titleText.replaceAll(RegExp(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'), '').trim();

        targetList.add(
          Padding(
            key: shouldApplyKey ? _triggerKey : null,
            padding: const EdgeInsets.only(top: 12, bottom: 6),
            child: Text(
              titleText,
              style: GoogleFonts.poppins(
                color: WanderlustColors.textWhite,
                fontSize: 24,
                fontWeight: FontWeight.w500,
              ),
            ),
          ),
        );
      } else if (trimmedLine.startsWith('## ') || trimmedLine.startsWith('### ')) {
        // H2/H3 Başlık - Premium Icon Header transformation
        final cleanLine = trimmedLine.replaceAll('#', '').trim();
        final iconData = _getCategoryIcon(cleanLine);
        final currentSectionIndex = sectionCount;
        
        // Emojileri temizle
        String titleText = cleanLine.replaceAll(RegExp(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'), '').trim();

        // SECTION VISUALS TEMPORARILY DISABLED - Code preserved for reactivation
        // if (insertedVisualCount < 3 && _shouldShowSectionVisual(currentSectionIndex)) {
        //   final visual = _pickSectionVisual(titleText, currentSectionIndex, usedVisuals);
        //   if (visual != null) {
        //     targetList.add(
        //       Padding(
        //         padding: const EdgeInsets.only(top: 8, bottom: 6),
        //         child: _buildSectionVisualCard(visual),
        //       ),
        //     );
        //     usedVisuals.add(visual.imageUrl);
        //     insertedVisualCount++;
        //   }
        // }

        targetList.add(
          Padding(
            key: shouldApplyKey ? _triggerKey : null,
            padding: EdgeInsets.zero,
            child: _buildSectionHeader(titleText, iconData),
          )
        );

      } else if (trimmedLine.startsWith('- ')) {
        // Bullet Point
        targetList.add(
          Padding(
            key: shouldApplyKey ? _triggerKey : null,
            padding: const EdgeInsets.only(bottom: 8.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  margin: const EdgeInsets.only(top: 8, right: 10),
                  width: 6,
                  height: 6,
                  decoration: const BoxDecoration(
                    color: WanderlustColors.accent,
                    shape: BoxShape.circle,
                  ),
                ),
                Expanded(child: _buildRichText(trimmedLine.substring(2).trim())),
              ],
            ),
          ),
        );
      } else if (trimmedLine.startsWith('1. ') || (trimmedLine.length > 2 && trimmedLine[1] == '.')) {
         // Numbered List -> ŞIK MOR NOKTAYA (POINT) DÖNÜŞTÜRÜLDÜ
         final dotIndex = trimmedLine.indexOf('.');
         final content = trimmedLine.substring(dotIndex + 1).trim();
         targetList.add(
           Padding(
             key: shouldApplyKey ? _triggerKey : null,
             padding: const EdgeInsets.only(bottom: 8.0),
             child: Row(
               crossAxisAlignment: CrossAxisAlignment.start,
               children: [
                 Container(
                   margin: const EdgeInsets.only(top: 8, right: 10),
                   width: 6,
                   height: 6,
                   decoration: const BoxDecoration(
                     color: WanderlustColors.accent,
                     shape: BoxShape.circle,
                   ),
                 ),
                 Expanded(child: _buildRichText(content)),
               ],
             ),
           ),
         );
      } else if (trimmedLine.startsWith('> ')) {
        // Quote
        targetList.add(
          Container(
            key: shouldApplyKey ? _triggerKey : null,
            margin: const EdgeInsets.symmetric(vertical: 12),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: WanderlustColors.bgCardLight,
              border: const Border(left: BorderSide(color: WanderlustColors.accent, width: 4)),
              borderRadius: BorderRadius.circular(12),
            ),
            child: _buildRichText(trimmedLine.substring(2)),
          ),
        );
      } else {
        // Normal paragraf
        targetList.add(
          Padding(
            key: shouldApplyKey ? _triggerKey : null,
            padding: const EdgeInsets.only(bottom: 8),
            child: _buildRichText(trimmedLine),
          ),
        );
      }
    }

    final List<Widget> finalWidgets = [...unlockedWidgets];

    if (hasReachedTrigger) {
      // Subtle transition indicator instead of bulky card
      finalWidgets.add(
        Padding(
          padding: const EdgeInsets.symmetric(vertical: 20),
          child: Center(
            child: Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: WanderlustColors.accent.withOpacity(0.3),
                borderRadius: BorderRadius.circular(2),
              ),
            ),
          ),
        ),
      );
      
      // Wrap locked content in a blur effect
      finalWidgets.add(
        ImageFiltered(
          imageFilter: ImageFilter.blur(sigmaX: 8.0, sigmaY: 8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: lockedWidgets,
          ),
        ),
      );
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: finalWidgets,
    );
  }

  bool _shouldShowSectionVisual(int sectionIndex) {
    return sectionIndex == 1 || sectionIndex == 3 || sectionIndex == 5;
  }

  _GuideSectionVisual? _pickSectionVisual(String title, int sectionIndex, Set<String> usedImageUrls) {
    final heroImage = (_guideHeroImageUrl?.trim().isNotEmpty ?? false)
        ? _guideHeroImageUrl!.trim()
        : widget.imageUrl.trim();

    final distinctCandidates = _guideHighlights.where((highlight) {
      final imageUrl = highlight.imageUrl?.trim();
      return imageUrl != null &&
          imageUrl.isNotEmpty &&
          imageUrl != heroImage &&
          !usedImageUrls.contains(imageUrl);
    }).toList();

    final candidates = distinctCandidates.isNotEmpty
        ? distinctCandidates
        : _guideHighlights.where((highlight) {
            final imageUrl = highlight.imageUrl?.trim();
            return imageUrl != null && imageUrl.isNotEmpty && !usedImageUrls.contains(imageUrl);
          }).toList();

    if (candidates.isEmpty) {
      if (heroImage.isEmpty || usedImageUrls.contains(heroImage)) return null;
      return _GuideSectionVisual(imageUrls: [heroImage]);
    }

    candidates.sort((a, b) {
      final scoreDiff = _scoreHighlightForSection(b, title).compareTo(_scoreHighlightForSection(a, title));
      if (scoreDiff != 0) return scoreDiff;

      final ratingDiff = (b.rating ?? 0).compareTo(a.rating ?? 0);
      if (ratingDiff != 0) return ratingDiff;

      return a.distanceFromCenter.compareTo(b.distanceFromCenter);
    });

    final fallbackUrls = candidates
        .map((highlight) => highlight.imageUrl!.trim())
        .where((url) => url.isNotEmpty)
        .take(4)
        .toList();

    if (heroImage.isNotEmpty && !fallbackUrls.contains(heroImage)) {
      fallbackUrls.add(heroImage);
    }

    if (fallbackUrls.isEmpty) {
      return null;
    }

    return _GuideSectionVisual(
      imageUrls: fallbackUrls,
    );
  }

  int _scoreHighlightForSection(Highlight highlight, String title) {
    final normalizedTitle = _normalize(title);
    final bag = _normalize([
      highlight.category,
      highlight.name,
      highlight.area,
      highlight.description,
      ...highlight.tags,
    ].join(' '));

    const foodKeywords = ['food', 'eat', 'yemek', 'lezzet', 'mutfak', 'gastronom', 'restaurant', 'restoran', 'cafe', 'kahve', 'coffee', 'bar', 'tapas'];
    const cultureKeywords = ['history', 'tarih', 'hafiza', 'memory', 'heritage', 'antik', 'culture', 'kultur', 'art', 'sanat', 'museum', 'muze', 'architecture', 'mimari', 'gaudi'];
    const neighborhoodKeywords = ['neighborhood', 'district', 'quarter', 'semt', 'mahalle', 'bolge', 'base', 'stay', 'konaklama', 'accommodation', 'otel', 'hotel'];
    const transportKeywords = ['transport', 'ulasim', 'getting around', 'route', 'metro', 'train', 'tram', 'bus', 'airport'];
    const natureKeywords = ['beach', 'sea', 'plaj', 'deniz', 'nature', 'doga', 'park', 'outdoor', 'hike'];
    const nightlifeKeywords = ['nightlife', 'gece', 'eglence', 'cocktail', 'bar', 'wine'];
    const shoppingKeywords = ['shopping', 'alisveris', 'market', 'bazaar', 'carsi'];
    const coffeeKeywords = ['coffee', 'kahve', 'cafe', 'brunch', 'bakery', 'pastane'];

    bool sectionHas(List<String> keywords) => keywords.any(normalizedTitle.contains);
    int keywordScore(List<String> keywords, int weight) {
      return keywords.fold(0, (total, keyword) => total + (bag.contains(keyword) ? weight : 0));
    }

    int score = ((highlight.rating ?? 0) * 4).round();
    score += 12 - highlight.distanceFromCenter.clamp(0, 12).round();

    if (sectionHas(foodKeywords)) {
      score += 60 + keywordScore(foodKeywords, 8);
    }
    if (sectionHas(cultureKeywords)) {
      score += 60 + keywordScore(cultureKeywords, 7);
    }
    if (sectionHas(natureKeywords)) {
      score += 50 + keywordScore(natureKeywords, 8);
    }
    if (sectionHas(nightlifeKeywords)) {
      score += 50 + keywordScore(nightlifeKeywords, 8);
    }
    if (sectionHas(shoppingKeywords)) {
      score += 45 + keywordScore(shoppingKeywords, 7);
    }
    if (sectionHas(coffeeKeywords)) {
      score += 45 + keywordScore(coffeeKeywords, 8);
    }
    if (sectionHas(neighborhoodKeywords)) {
      score += 24;
      if (highlight.distanceFromCenter <= 2.5) score += 18;
      score += keywordScore(['mahalle', 'semt', 'district', 'quarter', 'center', 'merkez', 'street', 'sokak'], 5);
    }
    if (sectionHas(transportKeywords)) {
      score += 16;
      if (highlight.distanceFromCenter <= 1.5) score += 18;
      score += keywordScore(['center', 'merkez', 'station', 'istasyon', 'metro'], 4);
    }

    return score;
  }

  Widget _buildSectionVisualCard(_GuideSectionVisual visual) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: WanderlustColors.borderLight),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.18),
            blurRadius: 18,
            offset: const Offset(0, 10),
          ),
        ],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(18),
        child: AspectRatio(
          aspectRatio: 16 / 9,
          child: _buildSectionVisualImage(visual.imageUrls),
        ),
      ),
    );
  }

  Widget _buildSectionVisualImage(List<String> imageUrls, [int index = 0]) {
    if (index >= imageUrls.length) {
      return Container(color: WanderlustColors.bgCard);
    }

    return CachedNetworkImage(
      imageUrl: firebaseCompatibleImageUrl(imageUrls[index]),
      key: ValueKey(imageUrls[index]),
      fit: BoxFit.cover,
      fadeInDuration: Duration.zero,
      fadeOutDuration: Duration.zero,
      placeholder: (_, __) => Container(color: WanderlustColors.bgCard),
      errorWidget: (_, __, ___) =>
          _buildSectionVisualImage(imageUrls, index + 1),
    );
  }

  Widget _buildStickyUnlockButton() {
    final isEnglish = AppLocalizations.instance.isEnglish;
    
    return Positioned(
      bottom: 30,
      left: 24,
      right: 24,
      child: AnimatedSlide(
        duration: const Duration(milliseconds: 400),
        offset: _showStickyButton ? Offset.zero : const Offset(0, 1),
        child: AnimatedOpacity(
          duration: const Duration(milliseconds: 400),
          opacity: _showStickyButton ? 1.0 : 0.0,
          child: GestureDetector(
            onTap: () {
              showModalBottomSheet(
                context: context,
                isScrollControlled: true,
                backgroundColor: Colors.transparent,
                builder: (context) => const PaywallScreen(),
              );
            },
            child: ClipRRect(
              borderRadius: BorderRadius.circular(20),
              child: BackdropFilter(
                filter: ImageFilter.blur(sigmaX: 15, sigmaY: 15),
                child: Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: WanderlustColors.accent.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(
                      color: WanderlustColors.accent.withOpacity(0.5),
                      width: 1.5,
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withOpacity(0.3),
                        blurRadius: 20,
                        offset: const Offset(0, 10),
                      ),
                    ],
                  ),
                  child: Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.all(8),
                        decoration: BoxDecoration(
                          color: WanderlustColors.accent,
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: const Icon(Icons.lock_open_rounded, color: Colors.white, size: 20),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              isEnglish ? "Unlock Full Guide" : "Rehberin Tamamını Aç",
                              style: GoogleFonts.poppins(
                                color: Colors.white,
                                fontSize: 15,
                                fontWeight: FontWeight.bold,
                                letterSpacing: 0.3,
                              ),
                            ),
                            Text(
                              isEnglish ? "Continue reading with My Way Pro" : "Pro ile okumaya devam et",
                              style: GoogleFonts.poppins(
                                color: Colors.white70,
                                fontSize: 12,
                              ),
                            ),
                          ],
                        ),
                      ),
                      const Icon(Icons.arrow_forward_ios_rounded, color: WanderlustColors.accent, size: 16),
                    ],
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  // Bulky teaser removed - simplified or deleted

  // Premium Section Header Widget
  Widget _buildSectionHeader(String title, IconData icon) {
    final imagePath = _getCategoryImage(title);
    return Container(
      margin: const EdgeInsets.only(top: 12, bottom: 8),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: WanderlustColors.accent.withOpacity(0.08),
        borderRadius: BorderRadius.circular(14),
        border: Border.all(
          color: WanderlustColors.borderLight,
          width: 1,
        ),
      ),
      child: Row(
        children: [
          // Icon
          imagePath != null
              ? Image.asset(
                  imagePath,
                  width: 36,
                  height: 36,
                  fit: BoxFit.contain,
                  color: WanderlustColors.accent,
                  colorBlendMode: BlendMode.srcIn,
                  errorBuilder: (context, error, stackTrace) => Icon(
                    icon,
                    color: WanderlustColors.accent,
                    size: 36,
                  ),
                )
              : Icon(
                  icon,
                  color: WanderlustColors.accent,
                  size: 36,
                ),
          const SizedBox(width: 12),
          // Title
          Expanded(
            child: Text(
              title,
              style: GoogleFonts.poppins(
                color: WanderlustColors.textWhite,
                fontSize: 16,
                fontWeight: FontWeight.w500,
                letterSpacing: 0.3,
              ),
            ),
          ),
        ],
      ),
    );
  }

  String? _getCategoryImage(String text) {
    final t = text.toLowerCase();
    if (t.contains('ne zaman') || t.contains('when to go') || t.contains('zaman gid') || t.contains('takvim') || t.contains('calendar')) {
      return 'assets/icons/icon_calendar.png';
    }
    if (t.contains('nerede kal') || t.contains('where to stay') || t.contains('konaklama') || t.contains('accommodation')) {
      return 'assets/icons/icon_bed.png';
    }
    if (t.contains('noktasından') || t.contains('a\'dan b\'ye') || t.contains('from a to') || 
        t.contains('ulaş') || t.contains('ulasim') || t.contains('getting around') || 
        t.contains('transport') || t.contains('mobility') || t.contains('lojistik') || 
        t.contains('logistics') || t.contains('gezinme')) {
      return 'assets/icons/icon_route.png';
    }
    if (t.contains('hafıza') || t.contains('memory') || t.contains('şehrin ruhu') || t.contains('tarihi miras') || t.contains('ancient')) {
      return 'assets/icons/icon_history.png';
    }
    if (t.contains('lezzet') || t.contains('food map') || t.contains('yemek haritası') || t.contains('gastronom') || t.contains('mutfak') || t.contains('ne yenir') || t.contains('ne içilir') || t.contains('what to eat') || t.contains('what to drink')) {
      return 'assets/icons/icon_food.png';
    }
    if (t.contains('fısıldadık') || t.contains('lokal sır') || t.contains('local secret') || t.contains('whisper') || t.contains('insider')) {
      return 'assets/icons/local_sirlar.png';
    }
    if (t.contains('mutlaka') || t.contains('yapmadan dönme') || t.contains('must do') || t.contains('must-do') || t.contains('don\'t miss') || t.contains('kaçırma') || t.contains('semt rehberi') || t.contains('neighborhood guide') || t.contains('district guide')) {
      return 'assets/icons/checklist.png';
    }
    return null;
  }

  IconData _getCategoryIcon(String text) {
    final t = text.toLowerCase();

    // When to go / Seasons
    if (t.contains('ne zaman') || t.contains('when to') || t.contains('mevsim') || t.contains('season') || t.contains('timing') || t.contains('zaman gid')) return Icons.calendar_month_rounded;
    // Accommodation
    if (t.contains('nerede kal') || t.contains('konaklama') || t.contains('otel') || t.contains('hotel') || t.contains('where to stay') || t.contains('accommodation')) return Icons.hotel_rounded;
    // Getting around / Transport
    if (t.contains('ulaşım') || t.contains('ulasim') || t.contains('transport') || 
        t.contains('getting around') || t.contains('gezinme') || t.contains('mobility') ||
        t.contains('metro') || t.contains('tren') || t.contains('train') || 
        t.contains('otobüs') || t.contains('bus') || t.contains('taksi') || t.contains('taxi')) return Icons.directions_transit_rounded;
    // Food & Drink
    if (t.contains('yemek') || t.contains('food') || t.contains('gastronom') || t.contains('lezzet') || t.contains('restoran') || t.contains('eating') || t.contains('cuisine') || t.contains('mutfak')) return Icons.restaurant_rounded;
    // Neighborhoods / Districts
    if (t.contains('semt') || t.contains('mahalle') || t.contains('neighborhood') || t.contains('district') || t.contains('quarter') || t.contains('bölge')) return Icons.location_city_rounded;
    // Practical tips
    if (t.contains('pratik') || t.contains('ipucu') || t.contains('tips') || t.contains('practical') || t.contains('önemli bilgi') || t.contains('bilinmesi')) return Icons.lightbulb_rounded;
    // Budget / Money
    if (t.contains('bütçe') || t.contains('budget') || t.contains('para') || t.contains('money') || t.contains('cost') || t.contains('fiyat')) return Icons.account_balance_wallet_rounded;
    // Culture / Art / Museum
    if (t.contains('kültür') || t.contains('culture') || t.contains('sanat') || t.contains('art') || t.contains('müze') || t.contains('museum')) return Icons.palette_rounded;
    // Shopping
    if (t.contains('alışveriş') || t.contains('shopping') || t.contains('çarşı') || t.contains('bazaar') || t.contains('market')) return Icons.shopping_bag_rounded;
    // Nightlife
    if (t.contains('gece hayat') || t.contains('nightlife') || t.contains('eğlence') || t.contains('entertainment')) return Icons.local_bar_rounded;
    // Nature / Outdoor
    if (t.contains('doğa') || t.contains('nature') || t.contains('park') || t.contains('hike') || t.contains('dağ') || t.contains('mountain') || t.contains('orman')) return Icons.nature_rounded;
    // Beach / Sea
    if (t.contains('plaj') || t.contains('beach') || t.contains('deniz') || t.contains('sea') || t.contains('kanal') || t.contains('canal')) return Icons.beach_access_rounded;
    // Safety / Security
    if (t.contains('güvenlik') || t.contains('safety') || t.contains('security') || t.contains('dikkat')) return Icons.shield_rounded;
    // Language / Communication
    if (t.contains('dil') || t.contains('language') || t.contains('iletişim')) return Icons.translate_rounded;
    // History / Heritage
    if (t.contains('tarih') || t.contains('history') || t.contains('heritage') || t.contains('antik') || t.contains('ancient')) return Icons.account_balance_rounded;
    // Architecture / Landmarks
    if (t.contains('mimari') || t.contains('architecture') || t.contains('landmark') || t.contains('anıt')) return Icons.domain_rounded;
    // Winter / Snow
    if (t.contains('kış') || t.contains('winter') || t.contains('snow') || t.contains('kar')) return Icons.ac_unit_rounded;
    // Coffee / Cafe
    if (t.contains('kahve') || t.contains('coffee') || t.contains('cafe')) return Icons.coffee_rounded;
    // Castle / Palace
    if (t.contains('kale') || t.contains('castle') || t.contains('saray') || t.contains('palace')) return Icons.castle_rounded;
    // Romance
    if (t.contains('aşk') || t.contains('love') || t.contains('roman') || t.contains('romantic')) return Icons.favorite_rounded;
    // Exploration / Discovery
    if (t.contains('keşif') || t.contains('explore') || t.contains('discover') || t.contains('hazine') || t.contains('gem')) return Icons.explore_rounded;
    // General guide / overview
    if (t.contains('guide') || t.contains('rehber') || t.contains('genel') || t.contains('overview')) return Icons.map_rounded;

    return Icons.travel_explore_rounded;
  }

  /// **Bold** metinleri ve [Link](search:...) formatını ayrıştırır
  Widget _buildRichText(String text) {
    // Link pattern: [DisplayName](search:SearchName)
    final linkPattern = RegExp(r'\[([^\]]+)\]\(search:([^\)]+)\)');
    final boldPattern = RegExp(r'\*\*([^\*]+)\*\*');
    
    // Önce linkleri işle
    if (linkPattern.hasMatch(text)) {
      final List<InlineSpan> spans = [];
      int lastEnd = 0;

      for (final match in linkPattern.allMatches(text)) {
        // Link öncesi metin
        if (match.start > lastEnd) {
          final beforeText = text.substring(lastEnd, match.start);
          spans.addAll(_parseTextWithBold(beforeText));
        }

        // Tıklanabilir link
        final displayName = match.group(1)!;
        final searchName = match.group(2)!;
        final foundPlace = _findHighlight(searchName);
        
        if (foundPlace != null) {
          spans.add(WidgetSpan(
            alignment: PlaceholderAlignment.baseline,
            baseline: TextBaseline.alphabetic,
            child: GestureDetector(
              onTap: () => _navigateToPlace(foundPlace),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                margin: const EdgeInsets.symmetric(horizontal: 1, vertical: 1),
                decoration: BoxDecoration(
                  color: WanderlustColors.accent.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Text(
                  displayName,
                  style: GoogleFonts.poppins(
                    color: WanderlustColors.accentLight,
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    decoration: TextDecoration.none,
                  ),
                ),
              ),
            ),
          ));
        } else {
          // Mekan veritabanımızda YOK! Düz ve şık metin olarak ekle, asla tıklanabilir olmasın!
          spans.add(TextSpan(
            text: displayName,
            style: GoogleFonts.poppins(
              color: WanderlustColors.textWhite,
              fontSize: 15,
              fontWeight: FontWeight.w600,
            ),
          ));
        }

        lastEnd = match.end;
      }

      // Son kalan metin
      if (lastEnd < text.length) {
        spans.addAll(_parseTextWithBold(text.substring(lastEnd)));
      }

      return Text.rich(
        TextSpan(
          style: GoogleFonts.poppins(
            color: WanderlustColors.textWhite, 
            fontSize: 16, 
            height: 1.6
          ),
          children: spans,
        ),
      );
    }

    // Link yoksa sadece bold parsing yap
    if (!text.contains('**')) {
      return Text(
        text,
        style: GoogleFonts.poppins(color: WanderlustColors.textWhite, fontSize: 16, height: 1.6),
      );
    }

    final List<TextSpan> spans = [];
    final parts = text.split('**');

    for (int i = 0; i < parts.length; i++) {
      if (i % 2 == 0) {
        spans.add(TextSpan(text: parts[i]));
      } else {
        spans.add(TextSpan(
          text: parts[i],
          style: GoogleFonts.poppins(
            color: WanderlustColors.textWhite, 
            fontSize: 16,
            fontWeight: FontWeight.w500
          ),
        ));
      }
    }

    return Text.rich(
      TextSpan(
        style: GoogleFonts.poppins(
          color: WanderlustColors.textWhite, 
          fontSize: 16, 
          height: 1.6
        ),
        children: spans,
      ),
    );
  }

  /// Bold text içeren metni parse eder
  List<InlineSpan> _parseTextWithBold(String text) {
    if (!text.contains('**')) {
      return [TextSpan(text: text)];
    }

    final List<InlineSpan> spans = [];
    final parts = text.split('**');

    for (int i = 0; i < parts.length; i++) {
      if (i % 2 == 0) {
        spans.add(TextSpan(text: parts[i]));
      } else {
        spans.add(TextSpan(
          text: parts[i],
          style: GoogleFonts.poppins(color: WanderlustColors.textWhite, fontWeight: FontWeight.w500),
        ));
      }
    }

    return spans;
  }

  /// Aksanlı karakterleri normalize eder (é→e, í→i, ü→u, etc.)
  String _normalize(String s) {
    const diacritics = 'àáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿăąćčďđęěğĺľłńňőœřśšşťţűůźżž';
    const replacements = 'aaaaaaaceeeeiiiidnoooooouuuuybyyaaccddeeglllnnoorssssttuuzzz';
    var result = s.toLowerCase().trim();
    for (int i = 0; i < diacritics.length && i < replacements.length; i++) {
      result = result.replaceAll(diacritics[i], replacements[i]);
    }
    // Also handle Turkish İ/ı
    result = result.replaceAll('İ', 'i').replaceAll('ı', 'i').replaceAll('i̇', 'i');
    return result;
  }

  /// Yer adına göre navigasyon yapar (Cross-city destekli ve sıfır gecikmeli)
  void _navigateToPlace(Highlight foundPlace) async {
    if (_isNavigating) return;
    _isNavigating = true;

    try {
      if (mounted) {
        // En fazla 250ms bekle, kullanıcı bekletilmeden sayfa şak diye açılsın!
        try {
          await ImagePrefetchService.prefetchSinglePhoto(context, foundPlace.imageUrl, heroDecode: true)
              .timeout(const Duration(milliseconds: 250));
        } catch (_) {}

        if (!mounted) {
          _isNavigating = false;
          return;
        }

        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: foundPlace)),
        ).then((_) {
          if (mounted) _isNavigating = false;
        });
      } else {
        _isNavigating = false;
      }
    } catch (e) {
      debugPrint('Place navigation error: $e');
      if (mounted) _isNavigating = false;
    }
  }
}
