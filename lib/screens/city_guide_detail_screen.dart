import 'package:flutter/material.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import '../theme/wanderlust_colors.dart';
import 'detail_screen.dart';

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

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(() {
      final show = _scrollController.offset > 200;
      if (show != _showScrollToTop) {
        setState(() => _showScrollToTop = show);
      }
    });

    _loadContent();
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
                    CachedNetworkImage(
                      imageUrl: widget.imageUrl,
                      fit: BoxFit.cover,
                      color: Colors.black.withOpacity(0.3),
                      colorBlendMode: BlendMode.darken,
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
                  
                  const SizedBox(height: 50),
                ],
              ),
            ),
          ),
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
    final List<Widget> widgets = [];
    final lines = rawContent.split('\n');

    for (var line in lines) {
      line = line.trim();
      if (line.isEmpty) {
        widgets.add(const SizedBox(height: 12));
        continue;
      }

      if (line.startsWith('# ')) {
        // H1 Başlık
        String titleText = line.substring(2);
        // Emojileri temizle
        titleText = titleText.replaceAll(RegExp(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'), '').trim();

        widgets.add(
          Padding(
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
      } else if (line.startsWith('## ') || line.startsWith('### ')) {
        // H2/H3 Başlık - Premium Icon Header transformation
        final cleanLine = line.replaceAll('#', '').trim();
        final iconData = _getCategoryIcon(cleanLine);
        
        // Emojileri temizle
        String titleText = cleanLine.replaceAll(RegExp(r'(\u00a9|\u00ae|[\u2000-\u3300]|\ud83c[\ud000-\udfff]|\ud83d[\ud000-\udfff]|\ud83e[\ud000-\udfff])'), '').trim();

        widgets.add(_buildSectionHeader(titleText, iconData));

      } else if (line.startsWith('- ')) {
        // Bullet Point
        widgets.add(
          Padding(
            padding: const EdgeInsets.only(bottom: 8.0, left: 8.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text("• ", style: GoogleFonts.poppins(color: WanderlustColors.accent, fontSize: 16)),
                Expanded(child: _buildRichText(line.substring(2))),
              ],
            ),
          ),
        );
      } else if (line.startsWith('1. ') || (line.length > 2 && line[1] == '.')) {
         // Numbered List (Basit kontrol)
         final dotIndex = line.indexOf('.');
        widgets.add(
          Padding(
            padding: const EdgeInsets.only(bottom: 8.0, left: 8.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                 Text("${line.substring(0, dotIndex + 1)} ", style: GoogleFonts.poppins(color: WanderlustColors.accent, fontSize: 16, fontWeight: FontWeight.bold)),
                Expanded(child: _buildRichText(line.substring(dotIndex + 1).trim())),
              ],
            ),
          ),
        );
      } else if (line.startsWith('> ')) {
        // Quote
        widgets.add(
          Container(
            margin: const EdgeInsets.symmetric(vertical: 12),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.05),
              border: const Border(left: BorderSide(color: WanderlustColors.accent, width: 4)),
              borderRadius: BorderRadius.circular(12),
            ),
            child: _buildRichText(line.substring(2)),
          ),
        );
      } else {
        // Normal paragraf
        widgets.add(
          Padding(
            padding: const EdgeInsets.only(bottom: 8),
            child: _buildRichText(line),
          ),
        );
      }
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: widgets,
    );
  }

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
          style: GoogleFonts.poppins(color: Colors.white.withOpacity(0.85), fontSize: 16, height: 1.6),
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
          style: GoogleFonts.poppins(color: Colors.white, fontWeight: FontWeight.bold),
        ));
      }
    }

    return RichText(
      text: TextSpan(
        style: GoogleFonts.poppins(color: Colors.white.withOpacity(0.85), fontSize: 16, height: 1.6),
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

  /// Yer adına göre navigasyon yapar
  void _navigateToPlace(String query) async {
    try {
      String? targetCity;
      String searchPlace = query;

      // 1. Önce mevcut şehri dene
      final currentCityModel = await CityDataLoader.loadCity(widget.city);
      Highlight? foundPlace;

      try {
        foundPlace = currentCityModel.highlights.firstWhere(
          (h) => h.name.toLowerCase().trim() == searchPlace.toLowerCase().trim() || 
                 searchPlace.toLowerCase().contains(h.name.toLowerCase().trim()) ||
                 h.name.toLowerCase().contains(searchPlace.toLowerCase().trim())
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
              (h) => h.name.toLowerCase().trim() == searchPlace.toLowerCase().trim() || 
                     searchPlace.toLowerCase().contains(h.name.toLowerCase().trim()) ||
                     h.name.toLowerCase().contains(searchPlace.toLowerCase().trim())
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
