import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:ui';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../services/premium_service.dart';

class PaywallScreen extends StatefulWidget {
  final VoidCallback? onDismiss;
  final Function(String planId)? onSubscribe;

  const PaywallScreen({super.key, this.onDismiss, this.onSubscribe});

  @override
  State<PaywallScreen> createState() => _PaywallScreenState();
}

class _PaywallScreenState extends State<PaywallScreen> {
  int _selectedPlan = 0; // Default to Annual (index 0)
  bool _isLoading = false;
  final PageController _pageController = PageController(viewportFraction: 0.85);
  int _currentPage = 0;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  final List<Map<String, dynamic>> _features = [
    {
      'icon': Icons.all_inclusive_rounded,
      'title': 'Unlimited Trips',
      'desc': 'Create unlimited travel plans for any city in the world.',
      'color': Colors.orange,
    },
    {
      'icon': Icons.smart_toy_rounded,
      'title': 'Smart AI Guide',
      'desc': 'Get personalized recommendations and real-time advice.',
      'color': Colors.purple,
    },

    {
      'icon': Icons.star_border_purple500_rounded,
      'title': 'Exclusive Routes',
      'desc': 'Access curated routes by local experts and travelers.',
      'color': Colors.pink,
    },
  ];

  List<Map<String, dynamic>> get _plans => [
    {
      "id": "annual",
      "title": isEnglish ? "Yearly" : "Yıllık",
      "price": "₺999,99",
      "sub": isEnglish ? "Billed Yearly" : "Yıllık Faturalanır",
      "save": isEnglish ? "58% Off" : "%58 İndirim",
      "trial": true,
    },
    {
      "id": "monthly",
      "title": isEnglish ? "Monthly" : "Aylık",
      "price": "₺199,99",
      "sub": isEnglish ? "Billed Monthly" : "Aylık Faturalanır",
      "save": null,
      "trial": false,
    },
    {
      "id": "weekly",
      "title": isEnglish ? "Weekly" : "Haftalık",
      "price": "₺59,99",
      "sub": isEnglish ? "Billed Weekly" : "Haftalık Faturalanır",
      "save": null,
      "trial": false,
    },
  ];

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  Future<void> _handleSubscribe() async {
    if (_isLoading) return;
    setState(() => _isLoading = true);
    
    try {
      final planId = _plans[_selectedPlan]['id'];
      final success = await PremiumService.instance.purchaseSubscription(planId);
      
      if (success) {
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

  String _calculateDailyPrice(String priceStr, String planId) {
    try {
      // Remove symbols and convert comma to dot
      String cleanPrice = priceStr.replaceAll('₺', '').replaceAll(' ', '').replaceAll(',', '.');
      double price = double.parse(cleanPrice);
      double dailyPrice = 0;

      switch (planId) {
        case 'weekly':
          dailyPrice = price / 7;
          break;
        case 'monthly':
          dailyPrice = price / 30;
          break;
        case 'annual':
          dailyPrice = price / 365;
          break;
      }
      
      return "₺${dailyPrice.toStringAsFixed(2)} / ${isEnglish ? 'day' : 'gün'}";
    } catch (e) {
      return "";
    }
  }

  @override
  Widget build(BuildContext context) {
    return Material(
      type: MaterialType.transparency,
      child: Container(
        height: MediaQuery.of(context).size.height * 0.90,
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [
              const Color(0xFFDCD6FF), // Light Lavender
              const Color(0xFFE8E5FF), 
              Colors.white,
            ],
            stops: const [0.0, 0.4, 0.8],
          ),
          borderRadius: const BorderRadius.vertical(top: Radius.circular(32)),
        ),
        child: Stack(
          children: [
            // 1. World Map Background
            Positioned.fill(
               child: Opacity(
                 opacity: 0.05,
                 child: Image.network(
                   "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/World_map_blank_without_borders.svg/2000px-World_map_blank_without_borders.svg.png",
                   fit: BoxFit.contain,
                   color: const Color(0xFF252131),
                 ),
               ),
            ),
            
            Column(
              mainAxisSize: MainAxisSize.min, 
              children: [
                const SizedBox(height: 20),
                
                // 2. Header
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: Row(
                    children: [
                       GestureDetector(
                        onTap: () {
                          if (widget.onDismiss != null) {
                            widget.onDismiss!();
                          } else {
                            Navigator.pop(context);
                          }
                        },
                        child: Container(
                          padding: const EdgeInsets.all(8),
                          decoration: const BoxDecoration(
                            color: Colors.white,
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(Icons.close, size: 20, color: Colors.black54),
                        ),
                      ),
                      Expanded(
                        child: Text(
                          isEnglish ? "Upgrade to Pro" : "Pro'ya Yükselt",
                          textAlign: TextAlign.center,
                          style: TextStyle(
                            fontSize: 18, 
                            fontWeight: FontWeight.w600,
                            color: WanderlustColors.accentDark,
                          ),
                        ),
                      ),
                      const SizedBox(width: 40),
                    ],
                  ),
                ),
                
                const SizedBox(height: 16),
                
                // 3. Feature Carousel (Restored)
                SizedBox(
                  height: 190,
                  child: PageView.builder(
                    controller: _pageController,
                    itemCount: _features.length,
                    onPageChanged: (idx) => setState(() => _currentPage = idx),
                    itemBuilder: (context, index) {
                      final item = _features[index];
                      final isSelected = _currentPage == index;
                      return AnimatedContainer(
                        duration: const Duration(milliseconds: 300),
                        margin: const EdgeInsets.symmetric(horizontal: 10, vertical: 12),
                        decoration: BoxDecoration(
                          color: isSelected ? Colors.white : Colors.white.withOpacity(0.9),
                          borderRadius: BorderRadius.circular(28),
                          gradient: isSelected 
                            ? LinearGradient(
                                begin: Alignment.topLeft,
                                end: Alignment.bottomRight,
                                colors: [Colors.white, item['color'].withOpacity(0.05)],
                              )
                            : null,
                          boxShadow: [
                            BoxShadow(
                              color: item['color'].withOpacity(isSelected ? 0.25 : 0.05),
                              blurRadius: isSelected ? 20 : 10,
                              offset: isSelected ? const Offset(0, 8) : const Offset(0, 4),
                              spreadRadius: isSelected ? 0 : -2,
                            )
                          ],
                          border: Border.all(
                            color: isSelected ? item['color'].withOpacity(0.5) : Colors.transparent,
                            width: 1.5
                          ),
                        ),
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Container(
                              padding: const EdgeInsets.all(16),
                              decoration: BoxDecoration(
                                color: item['color'].withOpacity(0.1),
                                shape: BoxShape.circle,
                              ),
                              child: Icon(item['icon'], size: 36, color: item['color']),
                            ),
                            const SizedBox(height: 16),
                            Text(
                              item['title'],
                              style: const TextStyle(
                                fontSize: 18, 
                                fontWeight: FontWeight.bold,
                                color: Colors.black87,
                                letterSpacing: -0.5,
                              ),
                            ),
                            const SizedBox(height: 6),
                            Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16),
                              child: Text(
                                item['desc'],
                                textAlign: TextAlign.center,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                                style: TextStyle(
                                  fontSize: 13, 
                                  color: Colors.black.withOpacity(0.6),
                                  height: 1.3,
                                ),
                              ),
                            ),
                          ],
                        ),
                      );
                    },
                  ),
                ),
                
                // Page Indicators
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: List.generate(_features.length, (index) {
                    return AnimatedContainer(
                      duration: const Duration(milliseconds: 300),
                      margin: const EdgeInsets.symmetric(horizontal: 4),
                      width: _currentPage == index ? 24 : 8,
                      height: 8,
                      decoration: BoxDecoration(
                        color: _currentPage == index 
                          ? WanderlustColors.accent 
                          : Colors.grey.withOpacity(0.3),
                        borderRadius: BorderRadius.circular(4),
                      ),
                    );
                  }),
                ),
                
                const SizedBox(height: 16),
                
                // 4. "Unlimited Trips" Title
                Text(
                  isEnglish ? "Unlimited Access" : "Sınırsız Erişim",
                  style: TextStyle(
                    fontSize: 24, 
                    fontWeight: FontWeight.bold,
                    color: WanderlustColors.bgDark, 
                    letterSpacing: -0.5,
                  ),
                ),
                
                const SizedBox(height: 16),
                
                // 5. Plan Selection
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: Column(
                    children: List.generate(_plans.length, (index) {
                       return Padding(
                         padding: const EdgeInsets.only(bottom: 10),
                         child: GestureDetector(
                          onTap: () => setState(() => _selectedPlan = index),
                          child: _buildPlanRow(
                            plan: _plans[index], 
                            isSelected: _selectedPlan == index
                          ),
                         ),
                       );
                    }),
                  ),
                ),
                
                // Terms & Trial Info
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 8),
                  child: Builder(
                    builder: (context) {
                      final plan = _plans[_selectedPlan];
                      final price = plan['price'];
                      final id = plan['id'];
                      final periodEn = id == 'annual' ? 'year' : id == 'monthly' ? 'month' : 'week';
                      final periodTr = id == 'annual' ? 'yıl' : id == 'monthly' ? 'ay' : 'hafta';

                      return Text(
                        isEnglish 
                           ? "1-day free trial, then $price/$periodEn. Cancel anytime."
                           : "1 gün ücretsiz deneme, sonra $price/$periodTr. İstediğin zaman iptal edilebilir.",
                        textAlign: TextAlign.center,
                        style: const TextStyle(color: Colors.black54, fontSize: 12, height: 1.4),
                      );
                    }
                  ),
                ),
                
                const SizedBox(height: 8),
                
                // 6. CTA Button
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(horizontal: 20),
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _handleSubscribe,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: WanderlustColors.bgDark,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(vertical: 16),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(30)),
                      elevation: 5,
                      shadowColor: WanderlustColors.bgDark.withOpacity(0.3),
                    ),
                    child: _isLoading 
                      ? const SizedBox(width: 24, height: 24, child: CircularProgressIndicator(color: Colors.white, strokeWidth: 2))
                      : Text(
                          isEnglish ? "Start My 1-day Free Trial" : "1 Günlük Ücretsiz Denemeyi Başlat",
                          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                  ),
                ),
                
                 // Restore
                 TextButton(
                  onPressed: () {},
                  child: Text(
                    isEnglish ? "Restore Purchases" : "Satın Almaları Geri Yükle",
                    style: TextStyle(color: WanderlustColors.bgDark.withOpacity(0.5), fontSize: 12),
                  ),
                ),
                
                const SizedBox(height: 10),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildPlanRow({required Map<String, dynamic> plan, required bool isSelected}) {
    return Stack(
      clipBehavior: Clip.none,
      children: [
        AnimatedContainer(
          duration: const Duration(milliseconds: 200),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 16),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
              color: isSelected ? WanderlustColors.accent : Colors.transparent,
              width: 2,
            ),
            boxShadow: isSelected 
              ? [BoxShadow(color: WanderlustColors.accent.withOpacity(0.2), blurRadius: 10, offset: const Offset(0, 4))]
              : [BoxShadow(color: Colors.black.withOpacity(0.05), blurRadius: 4, offset: const Offset(0, 2))],
          ),
          child: Row(
            children: [
              Container(
                width: 24,
                height: 24,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(
                    color: isSelected ? WanderlustColors.accent : Colors.grey.shade300,
                    width: isSelected ? 6 : 2,
                  ),
                ),
              ),
              const SizedBox(width: 16),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    plan['title'],
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.black87),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    _calculateDailyPrice(plan['price'], plan['id']),
                    style: TextStyle(
                      fontWeight: FontWeight.w500, 
                      fontSize: 12, 
                      color: isSelected ? WanderlustColors.accent : Colors.grey.shade400
                    ),
                  ),
                ],
              ),
              const Spacer(),
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    plan['price'],
                    style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.black87),
                  ),
                  Text(
                    plan['sub'],
                    style: const TextStyle(fontWeight: FontWeight.w500, fontSize: 11, color: Colors.black45),
                  ),
                ],
              ),
            ],
          ),
        ),
        
        // Discount Badge - positioned on top edge
        if (plan['save'] != null)
          Positioned(
            top: -10,
            right: 16,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: WanderlustColors.accentGreen,
                borderRadius: BorderRadius.circular(6),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.1), 
                    blurRadius: 4, 
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: Text(
                plan['save'],
                style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold),
              ),
            ),
          ),
      ],
    );
  }
}

void showPaywall(BuildContext context, {
  VoidCallback? onDismiss,
  Function(String plan)? onSubscribe,
}) {
  showModalBottomSheet(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.transparent,
    builder: (context) => PaywallScreen(
      onDismiss: onDismiss,
      onSubscribe: onSubscribe,
    ),
  );
}
