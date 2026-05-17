import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';
import 'package:flutter/services.dart';
import 'dart:ui';
import 'package:purchases_flutter/purchases_flutter.dart';
import 'package:url_launcher/url_launcher.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../services/premium_service.dart';
import '../services/photo_service.dart';
import '../services/content_update_service.dart';
import 'dart:convert';
import 'dart:io';

class PaywallScreen extends StatefulWidget {
  final VoidCallback? onDismiss;
  final Function(String planId)? onSubscribe;

  const PaywallScreen({super.key, this.onDismiss, this.onSubscribe});

  @override
  State<PaywallScreen> createState() => _PaywallScreenState();
}

class _PaywallScreenState extends State<PaywallScreen> {
  int _selectedPlan = 0; // Default to Monthly (new index 0)
  bool _isLoading = false;
  final PageController _pageController = PageController(viewportFraction: 1.0); // Full width
  int _currentPage = 0;
  /// 0 = ana paywall, 1 = çıkış / son teklif ekranı (retention)
  int _paywallStep = 1;
  Offerings? _offerings;
  bool _isTrialEligible = true; // Default to true
  List<Map<String, dynamic>>? _dynamicFeatures;
  VideoPlayerController? _videoController;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  List<Map<String, dynamic>> get _features {
    final List<Map<String, dynamic>> baseFeatures = [
      {
        'image': 'assets/images/paywall_daily_plan.jpg',
        'title': isEnglish
            ? 'Ditch the hour-by-hour stress.'
            : 'Saat saat plan stresine son verin.',
        'desc': isEnglish
            ? 'Tell us how many days you’re in town.\nWe’ll shape a smart day-by-day flow for you.'
            : 'Kaç gün şehirde kalacağınızı söyleyin.\nGünlük akışınızı birlikte şekillendirelim.',
      },
    ];

    return [
      ...baseFeatures,
      {
        'image': 'assets/images/paywall_smart_routes.jpg', // Smart Routes
        'title': isEnglish
            ? 'Less distance to cover. More of your day to savor.'
            : 'Mesafeyi kısaltın, günü uzatın.',
        'desc': isEnglish
            ? 'Your route threads the places you chose into one graceful flow—fewer empty steps, more room for what stays with you.'
            : 'Rota, seçtiğiniz mekanları tek akışta toplar; gereksiz mesafe yerine anı bırakır.',
      },
      {
        'image': 'https://www.cityrometours.com//upload/CONF93/20230912/rialto-bridge-auto-728X430-zoom.jpg', // Rialto Bridge
        'title': isEnglish ? 'Travel like a local insider.' : 'Tıpkı bir yerel gibi gezin.',
        'desc': isEnglish ? 'Forget boring tourist traps. Discover hidden cafes and spots picked exactly for your taste.' : 'Sıkıcı turist tuzaklarını unutun. Tamamen sizin zevkinize uygun gizli kafeleri ve noktaları keşfedin.',
      },
      {
        'image': 'assets/images/bruksel_header.jpg', // Using local Bruksel image to guarantee it loads
        'title': isEnglish ? 'Your 24/7 personal guide.' : '7/24 kişisel rehberiniz.',
        'desc': isEnglish ? 'Don’t search the web for hours. Just ask your assistant for the best local food, and go.' : 'İnternette saatler harcamayın. Asistanınıza en iyi restoranı sorun ve yola çıkın.',
      },
      {
        'image': 'https://tripaim.com/blog/wp-content/uploads/2020/11/Torre-Eiffel-en-Paris.jpg', // Eiffel
        'title': isEnglish ? 'Never get lost again.' : 'Bir daha asla kaybolmayın.',
        'desc': isEnglish ? 'Move with confidence. Get instant and precise directions to your next stop with one tap.' : 'Şehrin tadını çıkarırken stres yapmayın. Bir sonraki durağınıza tek dokunuşla yol tarifi alın.',
      },
      {
        'image': 'assets/images/paywall_capture_memories_v2.jpg', // New Amsterdam Image
        'title': isEnglish
            ? 'Keep the memories, skip the stress.'
            : 'Anılara odaklanın, stresi geride bırakın.',
        'desc': isEnglish
            ? 'Focus on exploring. We’ll build a beautiful digital diary of everywhere you visit.'
            : 'Keşfe odaklanın; gittiğiniz her noktayı haritada zarif bir günlükte bir arada tutalım.',
      },
    ];
  }

  @override
  void initState() {
    super.initState();
    _fetchOfferings();
    _loadDynamicConfig();
    _initVideoPlayer();
  }

  void _initVideoPlayer() {
    _videoController = VideoPlayerController.asset('assets/videos/paywall_bg.mp4')
      ..initialize().then((_) {
        if (mounted) {
          _videoController?.setLooping(true);
          _videoController?.setVolume(0); // Arka plan videosu sessiz olmalı
          _videoController?.play();
          setState(() {});
        }
      });
  }

  Future<void> _loadDynamicConfig() async {
    try {
      final file = await ContentUpdateService.getLocalConfigFile('paywall_config');
      if (file != null) {
        final content = await file.readAsString();
        final data = json.decode(content);
        if (data['features'] != null) {
          final List rawFeatures = data['features'];
          final List<Map<String, dynamic>> processed = rawFeatures.map((f) {
            return {
              'image': f['image'],
              'title': isEnglish ? (f['title']['en'] ?? f['title']['tr']) : (f['title']['tr'] ?? f['title']['en']),
              'desc': isEnglish ? (f['desc']['en'] ?? f['desc']['tr']) : (f['desc']['tr'] ?? f['desc']['en']),
            };
          }).toList();
          
          if (mounted) {
            setState(() {
              _dynamicFeatures = processed;
            });
          }
        }
      }
    } catch (e) {
      debugPrint("⚠️ Paywall dynamic config load error: $e");
    }
  }

  Future<void> _fetchOfferings() async {
    debugPrint("🔄 Fetching offerings...");
    try {
      final offerings = await PremiumService.instance.getOfferings();
      debugPrint("📦 Offerings fetched: ${offerings?.current?.availablePackages.length ?? 0} packages found.");
      if (offerings?.current == null) {
        debugPrint("⚠️ Offerings CURRENT is null. Available offerings: ${offerings?.all.keys}");
      }
      
      if (mounted) {
        final isEligible = await PremiumService.instance.isTrialEligible();
        setState(() {
          _offerings = offerings;
          _isTrialEligible = isEligible;
        });
      }
    } catch (e) {
      debugPrint("❌ Error fetching offerings: $e");
    }
  }

  // Helper to get package based on selected index
  Package? get _selectedPackage {
    if (_offerings?.current == null) return null;
    switch (_plans[_selectedPlan]['id']) {
      case 'monthly':
        return _offerings!.current!.monthly;
      case 'weekly':
        return _offerings!.current!.weekly;
      default:
        return null;
    }
  }

  List<Map<String, dynamic>> get _plans {
    const compareMonthlyEn = '\$17.99';
    const compareWeeklyEn = '\$5.99';
    const compareMonthlyTr = '₺399,99';
    const compareWeeklyTr = '₺149,99';

    String annualPrice = isEnglish ? "\$129.99" : "₺4.999";
    String monthlyPrice = isEnglish ? "\$9.99" : "₺189,99";
    String weeklyPrice = isEnglish ? "\$3.99" : "₺99,99";

    if (_offerings?.current?.annual?.storeProduct.priceString != null) {
      annualPrice = _offerings!.current!.annual!.storeProduct.priceString;
    }
    if (_offerings?.current?.monthly?.storeProduct.priceString != null) {
      monthlyPrice = _offerings!.current!.monthly!.storeProduct.priceString;
    }
    if (_offerings?.current?.weekly?.storeProduct.priceString != null) {
      weeklyPrice = _offerings!.current!.weekly!.storeProduct.priceString;
    }

    String dailyAnnual = isEnglish ? "\$0.36" : "₺13.70";
    String dailyMonthly = isEnglish ? "\$0.33" : "₺6.33";
    String dailyWeekly = isEnglish ? "\$0.57" : "₺14.28";

    String getCurrency(String priceStr, String code) {
      return priceStr.replaceAll(RegExp(r'[0-9.,\s]'), '').isEmpty ? code : priceStr.replaceAll(RegExp(r'[0-9.,\s]'), '');
    }

    if (_offerings?.current?.annual != null) {
      double price = _offerings!.current!.annual!.storeProduct.price;
      String priceStr = _offerings!.current!.annual!.storeProduct.priceString;
      String symbol = getCurrency(priceStr, _offerings!.current!.annual!.storeProduct.currencyCode);
      dailyAnnual = "$symbol${(price / 365).toStringAsFixed(2)}";
    }
    if (_offerings?.current?.monthly != null) {
      double price = _offerings!.current!.monthly!.storeProduct.price;
      String priceStr = _offerings!.current!.monthly!.storeProduct.priceString;
      String symbol = getCurrency(priceStr, _offerings!.current!.monthly!.storeProduct.currencyCode);
      dailyMonthly = "$symbol${(price / 30).toStringAsFixed(2)}";
    }
    if (_offerings?.current?.weekly != null) {
      double price = _offerings!.current!.weekly!.storeProduct.price;
      String priceStr = _offerings!.current!.weekly!.storeProduct.priceString;
      String symbol = getCurrency(priceStr, _offerings!.current!.weekly!.storeProduct.currencyCode);
      dailyWeekly = "$symbol${(price / 7).toStringAsFixed(2)}";
    }

    String compareForPlan(String? storeCurrency, {required bool isMonthly}) {
      if (storeCurrency == 'TRY' || storeCurrency == 'TRL') {
        return isMonthly ? compareMonthlyTr : compareWeeklyTr;
      }
      if (storeCurrency == 'USD') {
        return isMonthly ? compareMonthlyEn : compareWeeklyEn;
      }
      if (storeCurrency == null) {
        return isEnglish
            ? (isMonthly ? compareMonthlyEn : compareWeeklyEn)
            : (isMonthly ? compareMonthlyTr : compareWeeklyTr);
      }
      return '';
    }

    final monthlyCur = _offerings?.current?.monthly?.storeProduct.currencyCode;
    final weeklyCur = _offerings?.current?.weekly?.storeProduct.currencyCode;

    return [
      {
        "id": "monthly",
        "title": isEnglish ? "Monthly" : "Aylık",
        "price": monthlyPrice,
        "compareAtPrice": compareForPlan(monthlyCur, isMonthly: true),
        "daily": dailyMonthly,
        "sub": isEnglish ? "Billed Monthly" : "Aylık Faturalanır",
        "save": null,
        "trial": _isTrialEligible,
      },
      {
        "id": "weekly",
        "title": isEnglish ? "Weekly" : "Haftalık",
        "price": weeklyPrice,
        "compareAtPrice": compareForPlan(weeklyCur, isMonthly: false),
        "daily": dailyWeekly,
        "sub": isEnglish ? "Billed Weekly" : "Haftalık Faturalanır",
        "save": null,
        "trial": _isTrialEligible,
      },
    ];
  }

  @override
  void dispose() {
    _pageController.dispose();
    _videoController?.dispose();
    super.dispose();
  }

  Future<void> _handleSubscribe() async {
    if (_isLoading) return;
    setState(() => _isLoading = true);
    
    try {
      final package = _selectedPackage;
      if (package == null) {
        setState(() => _isLoading = false);
        return;
      }

      final success = await PremiumService.instance.purchasePackage(package);
      
      if (success) {
        final planId = _plans[_selectedPlan]['id'];
        await widget.onSubscribe?.call(planId);
        if (mounted) {
           Navigator.of(context).pop(); 
        }
      }
    } catch (e) {
      debugPrint('❌ Purchase error: $e');
    } finally {
      if (mounted) setState(() => _isLoading = false);
    }
  }

  Future<void> _restorePurchases() async {
     setState(() => _isLoading = true);
     try {
       final success = await PremiumService.instance.restorePurchases();
       if (success) {
          await widget.onSubscribe?.call('restored');
          if (mounted) Navigator.of(context).pop();
       } else {
         if (mounted) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text(isEnglish ? "No active subscription found" : "Aktif abonelik bulunamadı")),
            );
         }
       }
     } finally {
       if (mounted) setState(() => _isLoading = false);
     }
  }

  Future<void> _launchURL(String url) async {
    final uri = Uri.parse(url);
    if (!await launchUrl(uri, mode: LaunchMode.externalApplication)) {
      debugPrint('Could not launch $url');
    }
  }

  void _dismissPaywall() {
    widget.onDismiss?.call();
    if (mounted) Navigator.of(context).pop();
  }

  void _onMainCloseTap() {
    _dismissPaywall();
  }

  double? _msrpAmount(String? currency, bool isMonthly) {
    if (currency == 'TRY' || currency == 'TRL') {
      return isMonthly ? 399.99 : 149.99;
    }
    if (currency == 'USD') {
      return isMonthly ? 17.99 : 5.99;
    }
    return null;
  }

  int? _discountPercentComputed() {
    final pkg = _selectedPackage;
    if (pkg == null) return null;
    final currency = pkg.storeProduct.currencyCode;
    final isMonthly = _plans[_selectedPlan]['id'] == 'monthly';
    final msrp = _msrpAmount(currency, isMonthly);
    final price = pkg.storeProduct.price;
    if (msrp == null || price <= 0 || msrp <= price) return null;
    return ((msrp - price) / msrp * 100).round().clamp(5, 95);
  }

  int _discountPercentFallback() {
    final isMonthly = _plans[_selectedPlan]['id'] == 'monthly';
    if (isEnglish) {
      return isMonthly ? 44 : 33;
    }
    return isMonthly ? 53 : 33;
  }

  int _discountPercentForRetentionUi() {
    return _discountPercentComputed() ?? _discountPercentFallback();
  }

  Widget _buildRetentionPage({
    required BuildContext context,
    required BoxConstraints constraints,
    required Color bgDark,
    required Color accentLilac,
    required Color cardDark,
  }) {
    final pct = _discountPercentForRetentionUi();
    final plan = _plans[_selectedPlan];
    final compare = plan['compareAtPrice'] as String?;
    final price = plan['price'] as String;
    final hasCompare = compare != null && compare.isNotEmpty;
    final planId = plan['id'] as String;

    return Container(
      color: bgDark,
      child: Stack(
        children: [
          // 1. Summer Sale Background Video (or Image Fallback)
          Positioned.fill(
            child: (_videoController != null && _videoController!.value.isInitialized)
                ? SizedBox.expand(
                    child: FittedBox(
                      fit: BoxFit.cover,
                      child: SizedBox(
                        width: _videoController!.value.size.width,
                        height: _videoController!.value.size.height,
                        child: VideoPlayer(_videoController!),
                      ),
                    ),
                  )
                : Image.asset(
                    'assets/images/summer_sale_bg.png',
                    fit: BoxFit.cover,
                  ),
          ),
          
          // 2. Dark Overlay for readability
          Positioned.fill(
            child: Container(
              color: Colors.black.withOpacity(0.25), // Subtle dark overlay
            ),
          ),

          // 3. Gradient Overlay for additional depth
          Positioned.fill(
            child: Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    Colors.black.withOpacity(0.3),
                    Colors.transparent,
                    Colors.transparent,
                    Colors.black.withOpacity(0.5),
                  ],
                  stops: const [0.0, 0.3, 0.7, 1.0],
                ),
              ),
            ),
          ),

          // 4. Content
          SafeArea(
            child: LayoutBuilder(
              builder: (context, innerConstraints) {
                return SingleChildScrollView(
                  padding: const EdgeInsets.symmetric(horizontal: 24),
                  child: ConstrainedBox(
                    constraints: BoxConstraints(minHeight: innerConstraints.maxHeight),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        const SizedBox(height: 60),
                        
                        // Summer Sale Badge -> Special Offer
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                          decoration: BoxDecoration(
                            gradient: const LinearGradient(
                              colors: [Color(0xFFFF8C00), Color(0xFFFF0080)],
                            ),
                            borderRadius: BorderRadius.circular(30),
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xFFFF0080).withOpacity(0.3),
                                blurRadius: 15,
                                offset: const Offset(0, 5),
                              ),
                            ],
                          ),
                          child: Text(
                            isEnglish ? 'SPECIAL OFFER' : 'SANA ÖZEL',
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 14,
                              fontWeight: FontWeight.w900,
                              letterSpacing: 2,
                            ),
                          ),
                        ),
                        
                        const SizedBox(height: 24),
                        
                        Text(
                          isEnglish
                              ? 'Plan your perfect\ntrip in seconds'
                              : 'Mükemmel tatilini\nsaniyeler içinde planla',
                          textAlign: TextAlign.center,
                          style: const TextStyle(
                            fontSize: 34,
                            fontWeight: FontWeight.w900,
                            color: Colors.white,
                            height: 1.1,
                            letterSpacing: -1.2,
                          ),
                        ),
                        
                        const SizedBox(height: 40),

                        Text(
                          isEnglish ? '• LIMITED TIME OFFER •' : '• SINIRLI SÜRE İÇİN •',
                          style: TextStyle(
                            color: const Color(0xFFFFD700), // Gold/Yellow
                            fontSize: 18,
                            fontWeight: FontWeight.w600,
                            letterSpacing: 2,
                            shadows: [
                              Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 10),
                            ],
                          ),
                        ),

                        const SizedBox(height: 20),
                        
                        // Price Info - Floating (Enhanced Readability)
                        Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Row(
                              mainAxisSize: MainAxisSize.min,
                              crossAxisAlignment: CrossAxisAlignment.baseline,
                              textBaseline: TextBaseline.alphabetic,
                              children: [
                                if (hasCompare) ...[
                                  Text(
                                    compare,
                                    style: TextStyle(
                                      color: Colors.white.withOpacity(0.6),
                                      fontSize: 22,
                                      fontWeight: FontWeight.w600,
                                      decoration: TextDecoration.lineThrough,
                                      decorationColor: const Color(0xFFFFD700).withOpacity(0.8), // Gold strike-through
                                      decorationThickness: 2.0,
                                      shadows: [
                                        Shadow(color: Colors.black.withOpacity(0.6), blurRadius: 12, offset: const Offset(0, 2)),
                                      ],
                                    ),
                                  ),
                                  const SizedBox(width: 12),
                                ],
                                Text(
                                  price,
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 38,
                                    fontWeight: FontWeight.w900,
                                    letterSpacing: -1,
                                    shadows: [
                                      Shadow(color: Colors.black.withOpacity(0.6), blurRadius: 20, offset: const Offset(0, 4)),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                            const SizedBox(height: 8),
                            Text(
                              planId == 'monthly'
                                  ? (isEnglish ? 'PER MONTH' : 'AYLIK')
                                  : (isEnglish ? 'PER WEEK' : 'HAFTALIK'),
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                color: Colors.white.withOpacity(0.9),
                                fontSize: 14,
                                fontWeight: FontWeight.w800,
                                letterSpacing: 1.5,
                                shadows: [
                                  Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 10, offset: const Offset(0, 2)),
                                ],
                              ),
                            ),
                          ],
                        ),

                        const SizedBox(height: 20),

                        // Free Trial Info - Minimalist
                        Text(
                          isEnglish ? "• 3 DAYS FREE TRIAL •" : "• 3 GÜN ÜCRETSİZ DENE •",
                          style: TextStyle(
                            color: Colors.white.withOpacity(0.9),
                            fontSize: 17, // Slightly larger
                            fontWeight: FontWeight.w800,
                            letterSpacing: 1.5,
                            shadows: [
                              Shadow(color: Colors.black.withOpacity(0.6), blurRadius: 12, offset: const Offset(0, 2)),
                            ],
                          ),
                        ),
                        
                        const SizedBox(height: 48),
                        
                        // Outlined 'Continue' Button - Slightly Smaller
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 55),
                          child: SizedBox(
                            width: double.infinity,
                            height: 52, // Slightly shorter
                            child: OutlinedButton(
                              onPressed: () {
                                setState(() => _paywallStep = 0);
                              },
                              style: OutlinedButton.styleFrom(
                                side: const BorderSide(color: Colors.white60, width: 2.0),
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(30),
                                ),
                                foregroundColor: Colors.white,
                                backgroundColor: Colors.black12, 
                              ),
                              child: Text(
                                isEnglish ? 'CONTINUE' : 'DEVAM ET',
                                style: TextStyle(
                                  fontSize: 16, // Slightly smaller text
                                  fontWeight: FontWeight.w900,
                                  letterSpacing: 1.5,
                                  shadows: [
                                    Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 8, offset: const Offset(0, 2)),
                                  ],
                                ),
                              ),
                            ),
                          ),
                        ),
                        
                        const SizedBox(height: 24),
                        
                        // No thanks - Enhanced Readability
                        TextButton(
                          onPressed: _dismissPaywall,
                          child: Text(
                            isEnglish ? 'No, thanks' : 'Hayır, teşekkürler',
                            style: TextStyle(
                              color: Colors.white.withOpacity(0.8),
                              fontSize: 15,
                              fontWeight: FontWeight.w800,
                              shadows: [
                                Shadow(color: Colors.black.withOpacity(0.5), blurRadius: 10, offset: const Offset(0, 2)),
                              ],
                            ),
                          ),
                        ),
                        
                        const SizedBox(height: 40),
                      ],
                    ),
                  ),
                );
              },
            ),
          ),

          // 5. Close Button at Top Left (Moved to LAST in Stack to ensure it's on top)
          Positioned(
            top: 50,
            left: 20,
            child: GestureDetector(
              onTap: _dismissPaywall,
              behavior: HitTestBehavior.opaque, // Ensures the entire area is clickable
              child: Container(
                padding: const EdgeInsets.all(12), // Larger hit area
                color: Colors.transparent, // Ensures the padding is also clickable
                child: Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.black.withOpacity(0.3),
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.white24),
                  ),
                  child: const Icon(Icons.close, size: 20, color: Colors.white),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    const Color bgDark = Color(0xFF15121E);
    const Color cardDark = Color(0xFF252131);
    final Color accentLilac = WanderlustColors.accent;
    
    return PopScope(
      canPop: _paywallStep == 0,
      onPopInvokedWithResult: (bool didPop, dynamic result) {
        if (didPop) return;
        if (_paywallStep == 1) {
          _dismissPaywall();
        }
      },
      child: Material(
        type: MaterialType.transparency,
        child: Container(
          height: MediaQuery.of(context).size.height,
          clipBehavior: Clip.antiAlias,
          decoration: const BoxDecoration(
            color: bgDark,
            borderRadius: BorderRadius.vertical(top: Radius.circular(32)),
          ),
          child: LayoutBuilder(
            builder: (context, constraints) {
              if (_paywallStep == 1) {
                return _buildRetentionPage(
                  context: context,
                  constraints: constraints,
                  bgDark: bgDark,
                  accentLilac: accentLilac,
                  cardDark: cardDark,
                );
              }
              final bool isTablet =
                  MediaQuery.of(context).size.shortestSide > 600;
              final double headerHeight =
                  MediaQuery.of(context).size.height * (isTablet ? 0.30 : 0.45);

              return SingleChildScrollView(
              physics: const ClampingScrollPhysics(),
              child: ConstrainedBox(
                constraints: BoxConstraints(
                  minHeight: constraints.maxHeight,
                ),
                child: IntrinsicHeight(
                  child: Stack(
                    children: [
                      Positioned(
                        top: 0,
                        left: 0,
                        right: 0,
                        height: headerHeight,
                        child: ShaderMask(
                          shaderCallback: (rect) {
                            return const LinearGradient(
                              begin: Alignment.topCenter,
                              end: Alignment.bottomCenter,
                              colors: [Colors.black, Colors.black, Colors.transparent],
                              stops: [0.0, 0.7, 1.0],
                            ).createShader(rect);
                          },
                          blendMode: BlendMode.dstIn,
                          child: PageView.builder(
                            controller: _pageController,
                            itemCount: _features.length,
                            onPageChanged: (idx) => setState(() => _currentPage = idx),
                            itemBuilder: (context, index) {
                              final imagePath = _features[index]['image'];
                              final isNetwork = imagePath.startsWith('http');
                              
                              if (isNetwork) {
                                return Image.network(
                                  imagePath,
                                  fit: BoxFit.cover,
                                  alignment: Alignment.center,
                                  errorBuilder: (_,__,___) => Container(
                                    color: const Color(0xFF252131),
                                    child: const Center(child: Icon(Icons.image_not_supported, color: Colors.white24, size: 50)),
                                  ),
                                );
                              } else {
                                return Image.asset(
                                  imagePath,
                                  fit: BoxFit.cover,
                                  alignment: Alignment.center,
                                  errorBuilder: (_,__,___) => Container(
                                    color: const Color(0xFF252131),
                                    child: const Center(child: Icon(Icons.image_not_supported, color: Colors.white24, size: 50)),
                                  ),
                                );
                              }
                            },
                          ),
                        ),
                      ),

                      Positioned(
                        top: 0,
                        left: 0,
                        right: 0,
                        height: headerHeight + 100, 
                        child: IgnorePointer(
                          child: Container(
                            decoration: BoxDecoration(
                              gradient: LinearGradient(
                                begin: Alignment.topCenter,
                                end: Alignment.bottomCenter,
                                stops: const [0.0, 0.4, 0.7, 1.0], 
                                colors: [
                                  Colors.transparent, 
                                  bgDark.withOpacity(0.0), 
                                  bgDark.withOpacity(0.8), 
                                  bgDark, 
                                ],
                              ),
                            ),
                          ),
                        ),
                      ),
                      
                      Column(
                        children: [
                          Padding(
                            padding: const EdgeInsets.fromLTRB(20, 50, 20, 10),
                            child: Row(
                              children: [
                                 GestureDetector(
                                  onTap: _onMainCloseTap,
                                  child: Container(
                                    padding: const EdgeInsets.all(8),
                                    decoration: BoxDecoration( color: Colors.black.withOpacity(0.4), shape: BoxShape.circle ), 
                                    child: const Icon(Icons.close, size: 20, color: Colors.white),
                                  ),
                                ),
                                const Spacer(),
                              ],
                            ),
                          ),
                          
                          const Spacer(flex: 2),

                          Padding(
                            padding: const EdgeInsets.symmetric(horizontal: 24),
                            child: Column(
                              children: [
                                AnimatedSwitcher(
                                  duration: const Duration(milliseconds: 400),
                                  switchInCurve: Curves.easeOut,
                                  switchOutCurve: Curves.easeIn,
                                  child: Container(
                                    key: ValueKey<int>(_currentPage),
                                    height: isTablet ? 100 : 110,
                                    alignment: Alignment.center,
                                    child: Column(
                                      mainAxisSize: MainAxisSize.min,
                                      children: [
                                       Text(
                                          _features[_currentPage]['title'],
                                          textAlign: TextAlign.center,
                                          style: TextStyle(
                                            fontSize: isTablet ? 28 : 24,
                                            fontWeight: FontWeight.w800,
                                            letterSpacing: -0.5,
                                            color: Colors.white,
                                            height: 1.1,
                                            shadows: [
                                              const Shadow(color: Colors.black, blurRadius: 20, offset: Offset(0, 4)), 
                                              Shadow(color: Colors.black.withOpacity(0.8), blurRadius: 8, offset: const Offset(0, 2)), 
                                            ],
                                          ),
                                        ),
                                        const SizedBox(height: 12),
                                        Text(
                                          _features[_currentPage]['desc'],
                                          textAlign: TextAlign.center,
                                          style: TextStyle(
                                            fontSize: isTablet ? 19 : 17,
                                            color: Colors.white.withOpacity(0.95), 
                                            fontWeight: FontWeight.w500,
                                            height: 1.4,
                                            shadows: [
                                              const Shadow(color: Colors.black, blurRadius: 20, offset: Offset(0, 4)), 
                                              Shadow(color: Colors.black.withOpacity(0.8), blurRadius: 8, offset: const Offset(0, 2)), 
                                            ],
                                          ),
                                        ),
                                    ],
                                  ),
                                ),
                                ),
                              ],
                            ),
                          ),
                          
                          const SizedBox(height: 10),

                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 24),
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: List.generate(_features.length, (index) {
                                    return AnimatedContainer(
                                      duration: const Duration(milliseconds: 300),
                                      margin: const EdgeInsets.symmetric(horizontal: 4),
                                      width: _currentPage == index ? 32 : 8, 
                                      height: 6,
                                      decoration: BoxDecoration(
                                        color: _currentPage == index ? accentLilac : Colors.white30,
                                        borderRadius: BorderRadius.circular(3),
                                      ),
                                    );
                                  }),
                                ),
                                const SizedBox(height: 20),

                                Column(
                                  children: [
                                    Text(
                                      isEnglish
                                          ? 'Unlock My Way Pro'
                                          : 'My Way Pro’yu açın',
                                      style: const TextStyle(
                                        fontSize: 18,
                                        fontWeight: FontWeight.bold,
                                        color: Colors.white70,
                                        letterSpacing: 0.3,
                                      ),
                                    ),
                                    const SizedBox(height: 6),
                                    Padding(
                                      padding: const EdgeInsets.symmetric(horizontal: 8),
                                      child: Text(
                                        isEnglish
                                            ? 'Smart routes, turn-by-turn directions, AI trip help & more.'
                                            : 'Akıllı rotalar, yol tarifi, yapay zekâ ile plan desteği ve daha fazlası.',
                                        textAlign: TextAlign.center,
                                        style: TextStyle(
                                          fontSize: 13,
                                          height: 1.35,
                                          color: Colors.white.withOpacity(0.55),
                                          fontWeight: FontWeight.w500,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                                const SizedBox(height: 16),

                                Column(
                                  children: List.generate(_plans.length, (index) {
                                    return Padding(
                                      padding: const EdgeInsets.only(bottom: 8),
                                      child: GestureDetector(
                                        onTap: () =>
                                            setState(() => _selectedPlan = index),
                                        child: _buildPlanRow(
                                          plan: _plans[index],
                                          isSelected: _selectedPlan == index,
                                          cardColor: cardDark,
                                          accentColor: accentLilac,
                                          showPopularBadge: index == 0,
                                          popularLabel:
                                              isEnglish ? "POPULAR" : "POPÜLER",
                                        ),
                                      ),
                                    );
                                  }),
                                ),
                                
                                Builder(
                                  builder: (context) {
                                    final plan = _plans[_selectedPlan];
                                    final price = plan['price'];
                                    final hasTrial = plan['trial'] == true;
                                    final planId = plan['id'];
                                    
                                    final String periodEN = planId == 'monthly' ? 'month' : (planId == 'weekly' ? 'week' : 'period');
                                    final String periodTR = planId == 'monthly' ? 'ay' : (planId == 'weekly' ? 'hafta' : 'dönem');
                                    
                                    if (hasTrial) {
                                      return Padding(
                                        padding: const EdgeInsets.only(bottom: 12, top: 4),
                                        child: Column(
                                          children: [
                                            Container(
                                              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
                                              decoration: BoxDecoration(
                                                color: Colors.white.withOpacity(0.08),
                                                borderRadius: BorderRadius.circular(12),
                                                border: Border.all(color: Colors.white12),
                                              ),
                                              child: Text(
                                                isEnglish
                                                    ? "Start with 3 free days — no charge today."
                                                    : "Önce 3 gün ücretsiz deneyin — bugün ödeme yok.",
                                                style: const TextStyle(color: Colors.white, fontSize: 13, fontWeight: FontWeight.w600),
                                              ),
                                            ),
                                            const SizedBox(height: 6),
                                            Text(
                                              isEnglish
                                                ? "Then $price/$periodEN. Cancel anytime."
                                                : "Sonrasında $price/$periodTR. İstediğin zaman iptal et.",
                                              style: const TextStyle(color: Colors.white54, fontSize: 11),
                                            )
                                          ],
                                        ),
                                      );
                                    } else {
                                      return Padding(
                                        padding: const EdgeInsets.only(bottom: 12, top: 4),
                                        child: Text(
                                          isEnglish
                                             ? "$price/$periodEN. Cancel anytime."
                                             : "$price/$periodTR. İstediğin zaman iptal et.",
                                          textAlign: TextAlign.center,
                                          style: const TextStyle(color: Colors.white54, fontSize: 12),
                                        ),
                                      );
                                    }
                                  }
                                ),

                                SizedBox(
                                  width: double.infinity,
                                  child: ElevatedButton(
                                    onPressed: _isLoading ? null : _handleSubscribe,
                                    style: ElevatedButton.styleFrom(
                                      backgroundColor: accentLilac,
                                      foregroundColor: Colors.white,
                                      padding: const EdgeInsets.symmetric(vertical: 18),
                                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
                                      elevation: 8,
                                      shadowColor: accentLilac.withOpacity(0.4),
                                    ),
                                    child: _isLoading 
                                      ? const SizedBox(width: 24, height: 24, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                                      : Text(
                                          _plans[_selectedPlan]['trial'] == true
                                            ? (isEnglish ? "Start Free Trial" : "Ücretsiz Denemeyi Başlat")
                                            : (isEnglish ? "Subscribe Now" : "Abone Ol"),
                                          style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.white),
                                        ),
                                  ),
                                ),
                                
                                const SizedBox(height: 12),
                                
                                Padding(
                                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                                  child: Column(
                                    children: [
                                      Text(
                                        isEnglish 
                                          ? "Subscription automatically renews unless auto-renew is turned off at least 24-hours before the end of the current period. Payment will be charged to your ${Platform.isAndroid ? 'Google Play' : 'iTunes'} Account. You can manage or cancel your subscription in your Account Settings."
                                          : "Abonelik, geçerli dönemin bitiminden en az 24 saat önce otomatik yenileme kapatılmadıkça otomatik olarak yenilenir. Ödeme ${Platform.isAndroid ? 'Google Play' : 'iTunes'} Hesabınızdan tahsil edilecektir. Aboneliğinizi Hesap Ayarlarınızdan yönetebilir veya iptal edebilirsiniz.",
                                        textAlign: TextAlign.center,
                                        style: const TextStyle(color: Colors.white54, fontSize: 10, height: 1.3),
                                      ),
                                      const SizedBox(height: 12),
                                      Wrap(
                                        alignment: WrapAlignment.center,
                                        crossAxisAlignment: WrapCrossAlignment.center,
                                        children: [
                                          Text(
                                            isEnglish ? "By continuing, you agree to the " : "Devam ederek, ",
                                            style: const TextStyle(color: Colors.white54, fontSize: 10),
                                          ),
                                          GestureDetector(
                                            onTap: () => _launchURL('https://www.apple.com/legal/internet-services/itunes/dev/stdeula/'),
                                            child: Text(
                                              isEnglish ? "Terms of Use (EULA)" : "Kullanım Koşulları (EULA)",
                                              style: TextStyle(color: accentLilac, fontSize: 10, fontWeight: FontWeight.bold, decoration: TextDecoration.underline),
                                            ),
                                          ),
                                          Text(
                                            isEnglish ? " and " : " ve ",
                                            style: const TextStyle(color: Colors.white54, fontSize: 10),
                                          ),
                                          GestureDetector(
                                            onTap: () => _launchURL(isEnglish ? 'https://mywaytravelapp.com/privacy.html' : 'https://mywaytravelapp.com/privacy-tr.html'),
                                            child: Text(
                                              isEnglish ? "Privacy Policy" : "Gizlilik Politikası",
                                              style: TextStyle(color: accentLilac, fontSize: 10, fontWeight: FontWeight.bold, decoration: TextDecoration.underline),
                                            ),
                                          ),
                                          Text(
                                            isEnglish ? "." : "'nı kabul etmiş olursunuz.",
                                            style: const TextStyle(color: Colors.white54, fontSize: 10),
                                          ),
                                        ],
                                      ),
                                    ],
                                  ),
                                ),

                                const SizedBox(height: 12),
                                
                                TextButton(
                                  onPressed: _restorePurchases,
                                  child: Text(
                                    isEnglish ? "Restore Purchases" : "Satın Alımları Geri Yükle",
                                    style: const TextStyle(
                                      color: Colors.white60,
                                      fontSize: 12,
                                      fontWeight: FontWeight.w600,
                                    ),
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            );
          },
        ),
      ),
    ),
    );
  }

  Widget _buildPlanRow({
    required Map<String, dynamic> plan,
    required bool isSelected,
    required Color cardColor,
    required Color accentColor,
    bool showPopularBadge = false,
    String popularLabel = 'POPÜLER',
  }) {
    final compareRaw = plan['compareAtPrice'];
    final hasCompare =
        compareRaw != null && (compareRaw as String).isNotEmpty;

    final card = AnimatedContainer(
      duration: const Duration(milliseconds: 200),
      padding: const EdgeInsets.fromLTRB(12, 10, 12, 10),
      decoration: BoxDecoration(
        color: isSelected ? cardColor.withOpacity(1.0) : cardColor.withOpacity(0.6),
        border: Border.all(
          color: isSelected ? accentColor : Colors.transparent,
          width: 2,
        ),
        borderRadius: BorderRadius.circular(14),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Container(
            width: 22,
            height: 22,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(
                color: isSelected ? accentColor : Colors.white24,
                width: 2,
              ),
            ),
            padding: const EdgeInsets.all(3),
            child: isSelected
                ? Container(
                    decoration:
                        BoxDecoration(shape: BoxShape.circle, color: accentColor),
                  )
                : null,
          ),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  plan['title'],
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                if (plan['save'] != null) ...[
                  const SizedBox(height: 4),
                  Container(
                    padding: const EdgeInsets.symmetric(
                      horizontal: 6,
                      vertical: 2,
                    ),
                    decoration: BoxDecoration(
                      color: accentColor.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      plan['save'],
                      style: TextStyle(
                        color: accentColor,
                        fontSize: 10,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
                const SizedBox(height: 2),
                Text(
                  plan['sub'],
                  style: TextStyle(
                    color: Colors.white.withOpacity(0.55),
                    fontSize: 11,
                  ),
                ),
              ],
            ),
          ),
          Builder(
            builder: (context) {
              final isEn = AppLocalizations.instance.isEnglish;

              return Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Row(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.baseline,
                    textBaseline: TextBaseline.alphabetic,
                    children: [
                      if (hasCompare) ...[
                        Text(
                          compareRaw as String,
                          style: TextStyle(
                            color: Colors.white.withOpacity(0.58),
                            fontSize: 12,
                            fontWeight: FontWeight.w600,
                            decoration: TextDecoration.lineThrough,
                            decorationThickness: 2.5,
                            decorationColor:
                                Colors.white.withOpacity(0.45),
                          ),
                        ),
                        const SizedBox(width: 6),
                      ],
                      Text(
                        plan['price'] as String,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 16,
                          fontWeight: FontWeight.w700,
                          height: 1,
                        ),
                      ),
                    ],
                  ),
                  if (plan['daily'] != null) ...[
                    const SizedBox(height: 3),
                    Text(
                      "${plan['daily']} / ${isEn ? 'day' : 'gün'}",
                      textAlign: TextAlign.end,
                      style: TextStyle(
                        color: accentColor.withOpacity(0.95),
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ],
              );
            },
          ),
        ],
      ),
    );

    return Stack(
      clipBehavior: Clip.none,
      children: [
        card,
        if (showPopularBadge)
          Positioned(
            top: -9,
            right: 10,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
              decoration: BoxDecoration(
                color: accentColor,
                borderRadius: BorderRadius.circular(8),
                border: Border.all(
                  color: cardColor.withOpacity(0.95),
                  width: 1.5,
                ),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.35),
                    blurRadius: 5,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Text(
                popularLabel,
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 9,
                  fontWeight: FontWeight.w800,
                  letterSpacing: 0.5,
                ),
              ),
            ),
          ),
      ],
    );
  }
}

Future<void> showPaywall(BuildContext context, {Function(String)? onSubscribe, VoidCallback? onDismiss}) {
  return showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    enableDrag: true,
    builder: (context) => PaywallScreen(
      onDismiss: onDismiss,
      onSubscribe: onSubscribe,
    ),
  );
}
