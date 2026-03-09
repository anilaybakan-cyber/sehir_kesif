import 'package:flutter/material.dart';
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
  Offerings? _offerings;
  bool _isTrialEligible = true; // Default to true
  List<Map<String, dynamic>>? _dynamicFeatures;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  List<Map<String, dynamic>> get _features {
    if (_dynamicFeatures != null && _dynamicFeatures!.isNotEmpty) {
      return _dynamicFeatures!;
    }
    
    return [
      {
        'image': 'assets/images/paywall_smart_routes.jpg', // Smart Routes (Local)
        'title': isEnglish ? 'Smart Routes' : 'Akıllı Rotalar',
        'desc': isEnglish ? 'Create your route in seconds and hit the road immediately.' : 'Rotanı saniyeler içinde oluştur ve hemen yola çık.',
      },
      {
        'image': 'https://www.cityrometours.com//upload/CONF93/20230912/rialto-bridge-auto-728X430-zoom.jpg', // Rialto Bridge
        'title': isEnglish ? 'Personalized Suggestions' : 'Kişiselleştirilmiş Öneriler',
        'desc': isEnglish ? 'Quick suggestions based on your interests and preferences.' : 'İlgi alanların ve tercihlerine göre hızlı öneriler.',
      },
      {
        'image': 'https://www.royalcaribbean.com/media-assets/pmc/content/dam/shore-x/dubrovnik-dbv/duh7-seaside-resort-of-cavtat/stock-photo-panoramic-view-of-the-old-town-of-dubrovnik-croatia-273082328.jpg?w=800', // Dubrovnik
        'title': isEnglish ? 'My Way Assistant' : 'My Way Asistan',
        'desc': isEnglish ? 'Fast one-question answers. "Where is the best coffee shop?"' : 'Tek soruluk hızlı cevaplar. "En iyi kahveci nerede?"',
      },
      {
        'image': 'https://tripaim.com/blog/wp-content/uploads/2020/11/Torre-Eiffel-en-Paris.jpg', // Eiffel
        'title': isEnglish ? 'Instant Directions' : 'Anında Yol Tarifi',
        'desc': isEnglish ? 'Reach anywhere you want in the fastest way.' : 'Dilediğin yere en hızlı şekilde ulaş.',
      },
      {
        'image': 'assets/images/paywall_capture_memories.jpg', // Capture Memories (Local)
        'title': isEnglish ? 'Capture Memories' : 'Anı Kaydet',
        'desc': isEnglish ? 'Photograph places you visit, collect memories city by city.' : 'Gezdiğin yerleri fotoğrafla, şehir şehir anılar biriktir.',
      },
    ];
  }

  @override
  void initState() {
    super.initState();
    _fetchOfferings();
    _loadDynamicConfig();
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
    // Default Fallbacks (TR vs EN)
    String annualPrice = isEnglish ? "\$129.99" : "₺4.999";
    String monthlyPrice = isEnglish ? "\$17.99" : "₺499,99";
    String weeklyPrice = isEnglish ? "\$8.99" : "₺244,99";

    // Dynamic Overrides from RevenueCat
    if (_offerings?.current?.annual?.storeProduct.priceString != null) {
      annualPrice = _offerings!.current!.annual!.storeProduct.priceString;
      debugPrint("💰 Overriding Annual Price: $annualPrice");
    }
    if (_offerings?.current?.monthly?.storeProduct.priceString != null) {
      monthlyPrice = _offerings!.current!.monthly!.storeProduct.priceString;
      debugPrint("💰 Overriding Monthly Price: $monthlyPrice");
    }
    if (_offerings?.current?.weekly?.storeProduct.priceString != null) {
      weeklyPrice = _offerings!.current!.weekly!.storeProduct.priceString;
      debugPrint("💰 Overriding Weekly Price: $weeklyPrice");
    } else {
      debugPrint("⚠️ No overrides found. Offerings current: ${_offerings?.current}");
    }

    // Calculate Daily Prices (Default Fallbacks)
    // USD: 129.99/365=~0.36, 17.99/30=~0.60, 8.99/7=~1.28
    // TR: 4999/365=~13.70, 499.99/30=~16.67, 244.99/7=~35.00
    String dailyAnnual = isEnglish ? "\$0.36" : "₺13.70";
    String dailyMonthly = isEnglish ? "\$0.60" : "₺16.67";
    String dailyWeekly = isEnglish ? "\$1.28" : "₺35.00";

    // Helper: Extract currency symbol from priceString if possible, else code
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

    return [
      {
        "id": "monthly",
        "title": isEnglish ? "Monthly" : "Aylık",
        "price": monthlyPrice,
        "daily": dailyMonthly,
        "sub": isEnglish ? "Billed Monthly" : "Aylık Faturalanır",
        "save": null,
        "trial": _isTrialEligible, // 3-day free trial
      },
      {
        "id": "weekly",
        "title": isEnglish ? "Weekly" : "Haftalık",
        "price": weeklyPrice,
        "daily": dailyWeekly,
        "sub": isEnglish ? "Billed Weekly" : "Haftalık Faturalanır",
        "save": null,
        "trial": _isTrialEligible, // Added 3-day trial as requested
      },
    ];
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  Future<void> _handleSubscribe() async {
    if (_isLoading) return;
    setState(() => _isLoading = true);
    
    try {
      final package = _selectedPackage;
      if (package == null) {
        debugPrint("❌ No package found for selected plan.");
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

  @override
  Widget build(BuildContext context) {
    // Define Dark Theme Colors
    const Color bgDark = Color(0xFF15121E); // Main Background (Very Dark)
    const Color cardDark = Color(0xFF252131); // Card Surface
    final Color accentLilac = WanderlustColors.accent; // Use Global Accent
    
    return Material(
      type: MaterialType.transparency,
      child: Container(
        height: MediaQuery.of(context).size.height, // Full Screen Card (1.0)
        clipBehavior: Clip.antiAlias,
        decoration: const BoxDecoration(
          color: bgDark,
          borderRadius: BorderRadius.vertical(top: Radius.circular(32)),
        ),
        child: LayoutBuilder(
          builder: (context, constraints) {
            // Detect Tablet/iPad
            final bool isTablet = MediaQuery.of(context).size.shortestSide > 600;
            final double headerHeight = MediaQuery.of(context).size.height * (isTablet ? 0.30 : 0.45);

            return SingleChildScrollView(
              physics: const ClampingScrollPhysics(), // Keep it tight
              child: ConstrainedBox(
                constraints: BoxConstraints(
                  minHeight: constraints.maxHeight,
                ),
                child: IntrinsicHeight(
                  child: Stack(
                    children: [
                      // 1. Full-Width Background Images with PageView (With Smooth Fade)
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
                              stops: [0.0, 0.7, 1.0], // Start fading out at 70%
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

                      // 2. Strong Gradient Overlay (Transition to Body)
                      Positioned(
                        top: 0,
                        left: 0,
                        right: 0,
                        // Extended deeper to ensure seamless dark transition
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
                      
                      // 3. Content Layer
                      Column(
                        children: [
                          // Header (Close Only)
                          Padding(
                            padding: const EdgeInsets.fromLTRB(20, 50, 20, 10), // Increased top padding slightly for SafeArea
                            child: Row(
                              children: [
                                 GestureDetector(
                                  onTap: () {
                                    if (widget.onDismiss != null) widget.onDismiss!();
                                    else Navigator.pop(context);
                                  },
                                  child: Container(
                                    padding: const EdgeInsets.all(8),
                                    decoration: BoxDecoration( color: Colors.black.withOpacity(0.4), shape: BoxShape.circle ), 
                                    child: const Icon(Icons.close, size: 20, color: Colors.white),
                                  ),
                                ),
                                const Spacer(), // Pushes close button to left (or just fills space if we wanted right alignment, but here just empty)
                              ],
                            ),
                          ),
                          
                          const Spacer(flex: 2), // Reduced from 4 to 2 (pulled content up)

                          // Centered Text Content (Synced with PageView)
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
                                    height: isTablet ? 100 : 110, // Increased from 80/90 to accommodate larger text
                                    alignment: Alignment.center,
                                    child: Column(
                                      mainAxisSize: MainAxisSize.min,
                                      children: [
                                       Text(
                                          _features[_currentPage]['title'],
                                          textAlign: TextAlign.center,
                                          style: TextStyle(
                                            fontSize: isTablet ? 28 : 24, // Increased from 24/20
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
                                            fontSize: isTablet ? 19 : 17, // Increased from 17/15
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
                                ), // Closes AnimatedSwitcher
                              ],
                            ),
                          ),
                          
                          const SizedBox(height: 10), // Changed from Spacer(flex: 1) for more control

                          // Bottom Section: Plans & Checkouts
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 24),
                            child: Column(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                 // Indicators (Moved Here)
                                Row(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: List.generate(_features.length, (index) {
                                    return AnimatedContainer(
                                      duration: const Duration(milliseconds: 300),
                                      margin: const EdgeInsets.symmetric(horizontal: 4),
                                      // Slightly bigger active indicator per user image
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

                                // "Unlimited Access" Small Header
                                 Text(
                                  isEnglish ? "Unlimited Access" : "Sınırsız Erişim",
                                  style: const TextStyle(
                                    fontSize: 18, 
                                    fontWeight: FontWeight.bold,
                                    color: Colors.white70, 
                                    letterSpacing: 0.5,
                                  ),
                                ),
                                const SizedBox(height: 16),

                                // Plans
                                Column(
                                  children: List.generate(_plans.length, (index) {
                                     // Stack for "Best Offer" Badge
                                     return Stack(
                                       clipBehavior: Clip.none,
                                       children: [
                                         Padding(
                                           padding: const EdgeInsets.only(bottom: 12),
                                           child: GestureDetector(
                                            onTap: () => setState(() => _selectedPlan = index),
                                            child: _buildPlanRow(
                                              plan: _plans[index], 
                                              isSelected: _selectedPlan == index,
                                              cardColor: cardDark,
                                              accentColor: accentLilac,
                                            ),
                                           ),
                                         ),
                                         // "Best Offer" Badge (Only for Annual - Index 0)
                                         if (index == 0)
                                           Positioned(
                                             top: -8,
                                             right: 12,
                                             child: Container(
                                               padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                                               decoration: BoxDecoration(
                                                 color: accentLilac,
                                                 borderRadius: BorderRadius.circular(12),
                                                 boxShadow: [BoxShadow(color: Colors.black.withOpacity(0.3), blurRadius: 4, offset: const Offset(0, 2))],
                                               ),
                                               child: Text(
                                                 isEnglish ? "BEST OFFER" : "EN İYİ TEKLİF",
                                                 style: const TextStyle(color: Colors.white, fontSize: 10, fontWeight: FontWeight.bold, letterSpacing: 0.5),
                                               ),
                                             ),
                                           ),
                                       ],
                                     );
                                  }),
                                ),
                                
                                // Trial Text (only for plans with trial)
                                Builder(
                                  builder: (context) {
                                    final plan = _plans[_selectedPlan];
                                    final price = plan['price'];
                                    final hasTrial = plan['trial'] == true;
                                    
                                    return Padding(
                                      padding: const EdgeInsets.only(bottom: 12, top: 4),
                                      child: Text(
                                        hasTrial
                                          ? (isEnglish 
                                             ? "3 days free, then $price/period. Cancel anytime."
                                             : "3 gün ücretsiz deneme, sonra iptal etmezsen $price.")
                                          : (isEnglish
                                             ? "$price/week. Cancel anytime."
                                             : "$price/hafta. İstediğin zaman iptal et."),
                                        textAlign: TextAlign.center,
                                        style: const TextStyle(color: Colors.white38, fontSize: 12),
                                      ),
                                    );
                                  }
                                ),

                                // CTA
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
                                            ? (isEnglish ? "Start 3-day free trial" : "3 günlük ücretsiz denemeni başlat")
                                            : (isEnglish ? "Subscribe Now" : "Hemen Abone Ol"),
                                          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.white),
                                        ),
                                  ),
                                ),
                                
                                const SizedBox(height: 12),
                                
                                // Subscription Terms Text
                                Padding(
                                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                                  child: Column(
                                    children: [
                                      Text(
                                        isEnglish 
                                          ? "Subscription automatically renews unless auto-renew is turned off at least 24-hours before the end of the current period. Payment will be charged to your iTunes Account. You can manage or cancel your subscription in your Account Settings."
                                          : "Abonelik, geçerli dönemin bitiminden en az 24 saat önce otomatik yenileme kapatılmadıkça otomatik olarak yenilenir. Ödeme iTunes Hesabınızdan tahsil edilecektir. Aboneliğinizi Hesap Ayarlarınızdan yönetebilir veya iptal edebilirsiniz.",
                                        textAlign: TextAlign.center,
                                        style: const TextStyle(color: Colors.white54, fontSize: 10, height: 1.3),
                                      ),
                                      const SizedBox(height: 12),
                                      GestureDetector(
                                         onTap: () {
                                           // Link handling is done via individual text spans if using RichText, 
                                           // but to keep it simple and hit-testable, we can wrap the whole row or use a Wrap of Widgets.
                                           // Using Wrap for better multi-line support if needed.
                                         },
                                         child: Wrap(
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
                                      ),
                                    ],
                                  ),
                                ),

                                const SizedBox(height: 12),
                                
                                // Footer
                                // Restore Purchases Button
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
    );

  }

  Widget _buildPlanRow({
    required Map<String, dynamic> plan,
    required bool isSelected,
    required Color cardColor,
    required Color accentColor,
  }) {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 200),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12), // Reduced vertical padding
      decoration: BoxDecoration(
        color: isSelected ? cardColor.withOpacity(1.0) : cardColor.withOpacity(0.6),
        border: Border.all(
          color: isSelected ? accentColor : Colors.transparent,
          width: 2,
        ),
        borderRadius: BorderRadius.circular(16),
      ),
      child: Row(
        children: [
          // Radio Circle
          Container(
            width: 24,
            height: 24,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(
                color: isSelected ? accentColor : Colors.white24,
                width: 2,
              ),
            ),
            padding: const EdgeInsets.all(4),
            child: isSelected 
              ? Container(
                  decoration: BoxDecoration(shape: BoxShape.circle, color: accentColor),
                )
              : null,
          ),
          const SizedBox(width: 16),
          
          // Left Column (Title + Subtitle)
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      plan['title'],
                      style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
                    ),
                    if (plan['save'] != null) ...[
                      const SizedBox(width: 8),
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: accentColor.withOpacity(0.2),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          plan['save'],
                          style: TextStyle(color: accentColor, fontSize: 11, fontWeight: FontWeight.bold),
                        ),
                      )
                    ]
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                 plan['sub'],
                 style: const TextStyle(color: Colors.white54, fontSize: 12),
                ),
              ],
            ),
          ),
          
          // Right Column (Price + Daily Price)
          Column(
            crossAxisAlignment: CrossAxisAlignment.end,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                plan['price'],
                style: const TextStyle(color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
              ),
              if (plan['daily'] != null) ...[
                 const SizedBox(height: 2), // Small gap
                 Text(
                   "${plan['daily']} / ${AppLocalizations.instance.isEnglish ? 'day' : 'gün'}",
                   style: TextStyle(color: accentColor, fontSize: 13, fontWeight: FontWeight.bold),
                 ),
              ]
            ],
          ),
        ],
      ),
    );
  }
}

// Helper for showing the paywall via modal bottom sheet
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
