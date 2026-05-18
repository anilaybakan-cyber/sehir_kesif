import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../l10n/app_localizations.dart';
import '../services/ai_service.dart';
import '../services/city_data_loader.dart';
import '../models/city_model.dart';
import '../theme/wanderlust_colors.dart';
import 'detail_screen.dart';
import '../widgets/resilient_network_image.dart';
import '../services/image_prefetch_service.dart';

class GuideArticleScreen extends StatefulWidget {
  final String articleId;
  final String title;
  final String imageUrl;

  const GuideArticleScreen({
    super.key,
    required this.articleId,
    required this.title,
    required this.imageUrl,
  });

  @override
  State<GuideArticleScreen> createState() => _GuideArticleScreenState();
}

class _GuideArticleScreenState extends State<GuideArticleScreen> {
  String _content = "";
  bool _isLoading = true;
  bool _isNavigating = false;
  final Map<String, Highlight> _highlightMap = {};

  @override
  void initState() {
    super.initState();
    _loadContent();
    _loadAllCityHighlights();
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
    // Blog içeriğini getir
    final content = await AIService.getArticleContent(widget.articleId, isEnglish);

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
      body: CustomScrollView(
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
              // title: Text(
              //   widget.title,
              //   style: const TextStyle(
              //     color: Colors.white,
              //     fontWeight: FontWeight.bold,
              //     fontSize: 16,
              //     shadows: [Shadow(color: Colors.black, blurRadius: 4)],
              //     fontFamily: 'Poppins',
              //   ),
              // ),
              background: Hero(
                tag: 'guide_img_${widget.articleId}',
                child: Stack(
                  fit: StackFit.expand,
                  children: [
                    Positioned.fill(
                      child: ResilientNetworkImage(
                        imageUrl: widget.imageUrl,
                        placeName: widget.title,
                        city: '',
                        category: 'article',
                        fit: BoxFit.cover,
                        placeholderBuilder: (_) =>
                            Container(color: WanderlustColors.bgDark),
                      ),
                    ),
                    Positioned.fill(
                      child: Container(color: Colors.black.withOpacity(0.35)),
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
    );
  }

  /// Basit Markdown renderer
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
                color: WanderlustColors.textWhite,
                fontSize: 24,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
        );
      } else if (line.startsWith('## ') || line.startsWith('### ')) {
        // H2/H3 Başlık
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
                Container(
                  margin: const EdgeInsets.only(top: 8, right: 10),
                  width: 6,
                  height: 6,
                  decoration: const BoxDecoration(
                    color: WanderlustColors.accent,
                    shape: BoxShape.circle,
                  ),
                ),
                Expanded(child: _buildRichText(line.substring(2).trim(), fontSize: 14)),
              ],
            ),
          ),
        );
      } else if (line.startsWith('1. ') || (line.length > 2 && line[1] == '.')) {
         // Numbered List -> ŞIK MOR NOKTAYA (POINT) DÖNÜŞTÜRÜLDÜ
         final dotIndex = line.indexOf('.');
         final content = line.substring(dotIndex + 1).trim();
         widgets.add(
           Padding(
             padding: const EdgeInsets.only(bottom: 8.0, left: 8.0),
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
                 Expanded(child: _buildRichText(content, fontSize: 14)),
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
            child: _buildRichText(line.substring(2), fontSize: 14),
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

  // Compact Section Header Widget
  Widget _buildSectionHeader(String title, IconData icon) {
    // "1. Matera, İtalya — Taşa Oyulmuş Zaman" → split on em dash
    final parts = title.split('—');
    final mainTitle = parts[0].trim();
    final subtitle = parts.length > 1 ? parts[1].trim() : null;

    return Container(
      margin: const EdgeInsets.only(top: 16, bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(
          color: const Color(0xFF2C2C4E).withOpacity(0.5),
          width: 1,
        ),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.12),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Icon(icon, color: WanderlustColors.accent, size: 18),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  mainTitle,
                  style: GoogleFonts.poppins(
                    color: WanderlustColors.textWhite,
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    height: 1.3,
                  ),
                ),
                if (subtitle != null && subtitle.isNotEmpty)
                  Text(
                    subtitle,
                    style: GoogleFonts.poppins(
                      color: WanderlustColors.textGrey,
                      fontSize: 12,
                      fontWeight: FontWeight.w400,
                      height: 1.4,
                    ),
                  ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  IconData _getCategoryIcon(String text) {
    final t = text.toLowerCase();
    if (t.contains('finland') || t.contains('kış') || t.contains('winter')) return Icons.ac_unit_rounded;
    if (t.contains('vienna') || t.contains('viyana') || t.contains('coffee') || t.contains('kahve')) return Icons.coffee_rounded;
    if (t.contains('prague') || t.contains('prag') || t.contains('castle') || t.contains('kale')) return Icons.castle_rounded;
    if (t.contains('tromso') || t.contains('norway') || t.contains('norveç')) return Icons.landscape_rounded;
    if (t.contains('matera') || t.contains('cave') || t.contains('mağara')) return Icons.terrain_rounded;
    if (t.contains('giethoorn') || t.contains('canal') || t.contains('kanal')) return Icons.water_rounded;
    if (t.contains('food') || t.contains('yemek') || t.contains('gastronom') || t.contains('lezzet')) return Icons.restaurant_rounded;
    if (t.contains('love') || t.contains('aşk') || t.contains('roman') || t.contains('couple')) return Icons.favorite_rounded;
    
    return Icons.place_rounded; // Default
  }

  /// **Bold** metinleri ve [Link](search:...) formatını ayrıştırır
  Widget _buildRichText(String text, {double fontSize = 16}) {
    // Link pattern: [DisplayName](search:SearchName)
    final linkPattern = RegExp(r'\[([^\]]+)\]\(search:([^\)]+)\)');
    
    // Link yoksa ve bold yoksa düz Text döndür
    if (!linkPattern.hasMatch(text) && !text.contains('**')) {
      return Text(
        text,
        style: GoogleFonts.poppins(
          color: WanderlustColors.textGrey, 
          fontSize: fontSize, 
          height: 1.6, 
          fontWeight: FontWeight.w400
        ),
      );
    }

    // Link varsa isle
    if (linkPattern.hasMatch(text)) {
      final List<InlineSpan> spans = [];
      int lastEnd = 0;

      for (final match in linkPattern.allMatches(text)) {
        // Link öncesi metin
        if (match.start > lastEnd) {
          final beforeText = text.substring(lastEnd, match.start);
          spans.addAll(_parseTextWithBold(beforeText, fontSize: fontSize));
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
                    fontSize: fontSize - 1,
                    fontWeight: FontWeight.w600,
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
              fontSize: fontSize,
              fontWeight: FontWeight.w600,
            ),
          ));
        }

        lastEnd = match.end;
      }

      // Son kalan metin
      if (lastEnd < text.length) {
        spans.addAll(_parseTextWithBold(text.substring(lastEnd), fontSize: fontSize));
      }

      return RichText(
        text: TextSpan(
          style: GoogleFonts.poppins(
            color: WanderlustColors.textGrey, 
            fontSize: fontSize, 
            height: 1.6,
            fontWeight: FontWeight.w400,
          ),
          children: spans,
        ),
      );
    }

    // Link yoksa ama bold varsa
    return RichText(
      text: TextSpan(
        style: GoogleFonts.poppins(
          color: WanderlustColors.textGrey, 
          fontSize: fontSize, 
          height: 1.6,
          fontWeight: FontWeight.w400,
        ),
        children: _parseTextWithBold(text, fontSize: fontSize),
      ),
    );
  }

  /// Bold text içeren metni parse eder
  List<InlineSpan> _parseTextWithBold(String text, {double fontSize = 16}) {
    if (!text.contains('**')) {
      return [TextSpan(
        text: text,
        style: GoogleFonts.poppins(
          color: WanderlustColors.textGrey,
          fontSize: fontSize,
          fontWeight: FontWeight.w400,
        ),
      )];
    }

    final List<InlineSpan> spans = [];
    final parts = text.split('**');

    for (int i = 0; i < parts.length; i++) {
        if (i % 2 == 0) {
          if (parts[i].isNotEmpty) {
            spans.add(TextSpan(
              text: parts[i],
              style: GoogleFonts.poppins(
                color: WanderlustColors.textGrey,
                fontSize: fontSize,
                fontWeight: FontWeight.w400,
              ),
            ));
          }
        } else {
          // Sadece sonu : ile biten kelimeler (örn "Note:", "İpucu:") bold olsun
          final isKey = parts[i].trim().endsWith(':');
          
          spans.add(TextSpan(
            text: parts[i],
            style: GoogleFonts.poppins(
              color: isKey ? WanderlustColors.textWhite : WanderlustColors.textGrey, 
              fontSize: fontSize,
              fontWeight: isKey ? FontWeight.bold : FontWeight.w400,
            ),
          ));
        }
    }

    return spans;
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
