import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../l10n/app_localizations.dart';
import 'overview_tab.dart';
import 'neighborhoods_tab.dart';
import 'seasons_tab.dart';
import 'food_tab.dart';
import 'hidden_gems_tab.dart';
import 'checklist_tab.dart';
import 'dart:ui';

class AmsterdamGuideScreen extends StatefulWidget {
  /// Pass the city slug e.g. 'amsterdam' — will load assets/data/{city}_{lang}.json
  final String citySlug;
  const AmsterdamGuideScreen({super.key, required this.citySlug});

  @override
  State<AmsterdamGuideScreen> createState() => _AmsterdamGuideScreenState();
}

class _AmsterdamGuideScreenState extends State<AmsterdamGuideScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  late String _lang;
  CityGuide? _guide;
  bool _loading = true;

  // Localized tab names
  List<String> get _tabs {
    final isEn = _lang == 'en';
    return [
      isEn ? 'Overview' : 'Genel Bakış',
      isEn ? 'Stay' : 'Konaklama',
      isEn ? 'Season' : 'Mevsim',
      isEn ? 'Food' : 'Yemek',
      isEn ? 'Gems' : 'Gizli Cevherler',
      isEn ? 'List' : 'Liste',
    ];
  }

  @override
  void initState() {
    super.initState();
    // Initialize language from AppLocalizations
    _lang = AppLocalizations.instance.isEnglish ? 'en' : 'tr';
    _tabController = TabController(length: 6, vsync: this);
    _loadGuide();
  }

  Future<void> _loadGuide() async {
    setState(() => _loading = true);
    final path = 'assets/data/${widget.citySlug}_$_lang.json';
    try {
      final raw = await rootBundle.loadString(path);
      final json = jsonDecode(raw) as Map<String, dynamic>;
      setState(() {
        _guide = CityGuide.fromJson(json);
        _loading = false;
      });
    } catch (e) {
      debugPrint('Error loading Amsterdam guide: $e');
      setState(() => _loading = false);
    }
  }

  void _switchLang(String lang) {
    // Language is now tied to app global state
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: _loading
          ? const Center(child: CircularProgressIndicator(color: WanderlustColors.accent))
          : _guide == null
                ? const Center(child: Text('Guide not found'))
                : NestedScrollView(
                    headerSliverBuilder: (context, _) => [
                      SliverAppBar(
                        expandedHeight: 220,
                        pinned: true,
                        stretch: true,
                        backgroundColor: WanderlustColors.bgCard,
                        leading: IconButton(
                          icon: const Icon(Icons.arrow_back_ios_new, size: 20, color: Colors.white),
                          onPressed: () => Navigator.pop(context),
                        ),
                        flexibleSpace: FlexibleSpaceBar(
                          stretchModes: const [
                            StretchMode.zoomBackground,
                            StretchMode.blurBackground,
                          ],
                          background: _HeroHeader(
                            guide: _guide!,
                          ),
                        ),
                        bottom: TabBar(
                          controller: _tabController,
                          isScrollable: true,
                          tabAlignment: TabAlignment.start,
                          indicatorColor: WanderlustColors.accent,
                          labelColor: Colors.white,
                          unselectedLabelColor: Colors.white70,
                          indicatorPadding: const EdgeInsets.symmetric(horizontal: 8),
                          tabs: _tabs.map((t) => Tab(text: t)).toList(),
                        ),
                      ),
                    ],
                    body: TabBarView(
                      controller: _tabController,
                      children: [
                        OverviewTab(data: _guide!.sections.overview),
                        NeighborhoodsTab(data: _guide!.sections.neighborhoods),
                        SeasonsTab(data: _guide!.sections.seasons),
                        FoodTab(data: _guide!.sections.food),
                        HiddenGemsTab(data: _guide!.sections.hiddenGems),
                        ChecklistTab(data: _guide!.sections.checklist),
                      ],
                    ),
      ),
    );
  }
}

class _HeroHeader extends StatelessWidget {
  final CityGuide guide;

  const _HeroHeader({
    required this.guide,
  });

  @override
  Widget build(BuildContext context) {
    return Stack(
      fit: StackFit.expand,
      children: [
        // Background Image
        Image.network(
          'https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=1200&q=80',
          fit: BoxFit.cover,
          loadingBuilder: (context, child, loadingProgress) {
            if (loadingProgress == null) return child;
            return Container(color: WanderlustColors.bgDark);
          },
        ),
        
        // Gradient Overlay
        Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [
                Colors.black.withOpacity(0.6),
                Colors.black.withOpacity(0.2),
                Colors.black.withOpacity(0.8),
              ],
              stops: const [0.0, 0.4, 1.0],
            ),
          ),
        ),
        
        Padding(
          padding: EdgeInsets.only(
            top: MediaQuery.of(context).padding.top + 40,
            left: 16,
            right: 16,
            bottom: 54, // Enough space for TabBar
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(AppLocalizations.instance.isEnglish ? 'CITY GUIDE' : 'ŞEHİR REHBERİ',
                  style: TextStyle(
                    fontSize: 10, 
                    color: Colors.white.withOpacity(0.9), 
                    letterSpacing: 1.2, 
                    fontWeight: FontWeight.bold,
                    shadows: [Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 4, offset: const Offset(0, 2))],
                  )),
              const SizedBox(height: 2),
              Text(guide.meta.city,
                  style: TextStyle(
                    fontSize: 32, 
                    fontWeight: FontWeight.bold, 
                    color: Colors.white,
                    shadows: [Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 8, offset: const Offset(0, 2))],
                  )),
              Text(guide.meta.tagline,
                  style: TextStyle(
                    fontSize: 13, 
                    color: Colors.white.withOpacity(0.9),
                    fontWeight: FontWeight.w500,
                    shadows: [Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 4, offset: const Offset(0, 1))],
                  )),
              const SizedBox(height: 16),
              SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  children: guide.pills.map((p) => Container(
                    margin: const EdgeInsets.only(right: 8),
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                    decoration: BoxDecoration(
                      color: Colors.black.withOpacity(0.3),
                      borderRadius: BorderRadius.circular(20),
                      border: Border.all(color: Colors.white.withOpacity(0.3)),
                    ),
                    child: Text(p, style: const TextStyle(fontSize: 11, color: Colors.white, fontWeight: FontWeight.bold)),
                  )).toList(),
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }
}

// Language switching buttons removed to follow global app language
