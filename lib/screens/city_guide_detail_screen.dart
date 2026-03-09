import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import '../theme/wanderlust_colors.dart';
import 'detail_screen.dart';
import 'dart:io';
import '../services/premium_service.dart';
import 'paywall_screen.dart';
import 'dart:convert';
import 'dart:ui';

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
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;
  bool _showStickyButton = false;
  final GlobalKey _triggerKey = GlobalKey();

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(() {
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

  Future<void> _loadContent() async {
    setState(() => _isLoading = true);
    
    final isEnglish = AppLocalizations.instance.isEnglish;
    // Blog içeriğini getir
    final content = await AIService.getCityBlogContent(widget.city, isEnglish);

    if (mounted) {
      setState(() {
        _content = content;
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
              // AppBar & Hero Image
              SliverAppBar(
                expandedHeight: 300,
                pinned: true,
                backgroundColor: WanderlustColors.bgDark,
                leading: IconButton(
                  icon: const Icon(Icons.arrow_back_ios_new, color: Colors.white),
                  onPressed: () => Navigator.pop(context),
                ),
                flexibleSpace: FlexibleSpaceBar(
                  background: Hero(
                    tag: 'guide_img_${widget.city}',
                    child: Stack(
                      fit: StackFit.expand,
                      children: [
                        Image.network(
                          widget.imageUrl,
                          fit: BoxFit.cover,
                          color: Colors.black.withOpacity(0.3),
                          colorBlendMode: BlendMode.darken,
                          loadingBuilder: (context, child, loadingProgress) {
                            if (loadingProgress == null) return child;
                            return Container(color: WanderlustColors.bgDark);
                          },
                          errorBuilder: (context, error, stackTrace) => Container(color: WanderlustColors.bgDark),
                        ),
                        Positioned(
                          bottom: -1, // -1 to avoid any gap
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
                  ),
                ),
              ),

              // Content
              SliverToBoxAdapter(
                child: Container(
                  padding: const EdgeInsets.all(24),
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
                      border: Border.all(color: const Color(0xFF2C2C4E).withOpacity(0.5)),
                    ),
                    child: const Icon(Icons.keyboard_arrow_up_rounded, color: Color(0xFF9E9E9E), size: 28),
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
        targetList.add(const SizedBox(height: 12));
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
            padding: const EdgeInsets.only(top: 20, bottom: 12),
            child: Text(
              titleText,
              style: GoogleFonts.poppins(
                color: Colors.white,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        );
      } else if (trimmedLine.startsWith('## ') || trimmedLine.startsWith('### ')) {
        // H2/H3 Başlık - Premium Icon Header transformation
        final cleanLine = trimmedLine.replaceAll('#', '').trim();
        final iconData = _getCategoryIcon(cleanLine);
        
        // Emojileri temizle
        String titleText = cleanLine.replaceAll(RegExp(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'), '').trim();

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
            padding: const EdgeInsets.only(bottom: 8.0, left: 8.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("• ", style: GoogleFonts.poppins(color: WanderlustColors.accent, fontSize: 16)),
                Expanded(child: _buildRichText(trimmedLine.substring(2))),
              ],
            ),
          ),
        );
      } else if (trimmedLine.startsWith('1. ') || (trimmedLine.length > 2 && trimmedLine[1] == '.')) {
         // Numbered List (Basit kontrol)
         final dotIndex = trimmedLine.indexOf('.');
        targetList.add(
          Padding(
            key: shouldApplyKey ? _triggerKey : null,
            padding: const EdgeInsets.only(bottom: 8.0, left: 8.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                 Text("${trimmedLine.substring(0, dotIndex + 1)} ", style: GoogleFonts.poppins(color: WanderlustColors.accent, fontSize: 16, fontWeight: FontWeight.bold)),
                Expanded(child: _buildRichText(trimmedLine.substring(dotIndex + 1).trim())),
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
              color: Colors.white.withOpacity(0.05),
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
    return Container(
      margin: const EdgeInsets.only(top: 24, bottom: 16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(
          color: const Color(0xFF2C2C4E).withOpacity(0.5),
          width: 1,
        ),
      ),
      child: Row(
        children: [
          // Icon Container with Glow
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.15),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: WanderlustColors.accent.withOpacity(0.3),
                width: 1,
              ),
            ),
            child: Icon(
              icon,
              color: WanderlustColors.accent,
              size: 24,
            ),
          ),
          const SizedBox(width: 16),
          // Title
          Expanded(
            child: Text(
              title,
              style: GoogleFonts.poppins(
                color: Colors.white,
                fontSize: 18,
                fontWeight: FontWeight.bold,
                letterSpacing: 0.5,
              ),
            ),
          ),
        ],
      ),
    );
  }

  IconData _getCategoryIcon(String text) {
    // Keywords based matching since emojis are removed
    final t = text.toLowerCase();
    
    if (t.contains('finland') || t.contains('kış') || t.contains('winter')) return Icons.ac_unit_rounded;
    if (t.contains('vienna') || t.contains('viyana') || t.contains('coffee') || t.contains('kahve')) return Icons.coffee_rounded;
    if (t.contains('prague') || t.contains('prag') || t.contains('castle') || t.contains('kale')) return Icons.castle_rounded;
    if (t.contains('tromso') || t.contains('norway') || t.contains('norveç')) return Icons.landscape_rounded;
    if (t.contains('matera') || t.contains('cave') || t.contains('mağara')) return Icons.terrain_rounded;
    if (t.contains('giethoorn') || t.contains('canal') || t.contains('kanal')) return Icons.water_rounded;
    if (t.contains('food') || t.contains('yemek') || t.contains('gastronom') || t.contains('lezzet')) return Icons.restaurant_rounded;
    if (t.contains('love') || t.contains('aşk') || t.contains('roman') || t.contains('couple')) return Icons.favorite_rounded;
    if (t.contains('train') || t.contains('tren') || t.contains('metro')) return Icons.directions_transit_rounded;
    if (t.contains('gem') || t.contains('hazine') || t.contains('keşif')) return Icons.diamond_rounded;
    if (t.contains('guide') || t.contains('rehber')) return Icons.map_rounded;
    
    // Default
    return Icons.place_rounded; 
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
        
        spans.add(WidgetSpan(
          alignment: PlaceholderAlignment.baseline,
          baseline: TextBaseline.alphabetic,
          child: GestureDetector(
            onTap: () => _navigateToPlace(searchName),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
              margin: const EdgeInsets.symmetric(horizontal: 2),
              decoration: BoxDecoration(
                color: WanderlustColors.accent.withOpacity(0.2),
                borderRadius: BorderRadius.circular(6),
                border: Border.all(color: WanderlustColors.accent.withOpacity(0.5)),
              ),
              child: Text(
                displayName,
                style: GoogleFonts.poppins(
                  color: WanderlustColors.accent,
                  fontSize: 15,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
        ));

        lastEnd = match.end;
      }

      // Son kalan metin
      if (lastEnd < text.length) {
        spans.addAll(_parseTextWithBold(text.substring(lastEnd)));
      }

      return RichText(
        text: TextSpan(
          style: GoogleFonts.poppins(
            color: Colors.white.withOpacity(0.85), 
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
        style: GoogleFonts.poppins(color: Colors.white.withOpacity(0.85), fontSize: 16, height: 1.6),
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
            color: Colors.white, 
            fontSize: 16,
            fontWeight: FontWeight.bold
          ),
        ));
      }
    }

    return RichText(
      text: TextSpan(
        style: GoogleFonts.poppins(
          color: Colors.white.withOpacity(0.85), 
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
          style: GoogleFonts.poppins(color: Colors.white, fontWeight: FontWeight.bold),
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

  /// Yer adına göre navigasyon yapar
  void _navigateToPlace(String query) async {
    try {
      String? targetCity;
      String searchPlace = query;

      // 1. Önce mevcut şehri dene
      final currentCityModel = await CityDataLoader.loadCity(widget.city);
      Highlight? foundPlace;

      final normalizedSearch = _normalize(searchPlace);

      try {
        foundPlace = currentCityModel.highlights.firstWhere(
          (h) {
            final normalizedName = _normalize(h.name);
            return normalizedName == normalizedSearch || 
                   normalizedSearch.contains(normalizedName) ||
                   normalizedName.contains(normalizedSearch);
          }
        );
      } catch (_) {}

      // 2. Bulunamadıysa cross-city ara
      if (foundPlace == null) {
        // Query içinde şehir adı var mı kontrol et
        final allCities = CityDataLoader.supportedCities;
        for (var cityId in allCities) {
          if (query.toLowerCase().contains(cityId)) {
            targetCity = cityId;
            break;
          }
        }

        List<String> citiesToSearch = targetCity != null 
            ? [targetCity] 
            : ['roma', 'paris', 'barcelona', 'istanbul', 'londra', 'viyana', 'prag', 'lizbon', 'rovaniemi', 'matera', 'sintra', 'colmar'];
        
        for (var cityId in citiesToSearch) {
          if (cityId == widget.city) continue; // Zaten aradık
          final cityModel = await CityDataLoader.loadCity(cityId);
          try {
            foundPlace = cityModel.highlights.firstWhere(
              (h) {
                final normalizedName = _normalize(h.name);
                return normalizedName == normalizedSearch || 
                       normalizedSearch.contains(normalizedName) ||
                       normalizedName.contains(normalizedSearch);
              }
            );
            if (foundPlace != null) break;
          } catch (_) {}
        }
      }

      if (foundPlace != null && mounted) {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: foundPlace!)),
        );
      } else {
         ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(AppLocalizations.instance.isEnglish ? "Place not found: $query" : "Yer bulunamadı: $query"),
            backgroundColor: WanderlustColors.bgCard,
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    } catch (e) {
      debugPrint('Place navigation error: $e');
    }
  }
}
