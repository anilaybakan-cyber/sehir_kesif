// =============================================================================
// DETAIL SCREEN – WANDERLUST DARK THEME
// Full-screen hero, glassmorphism cards, purple/pink accents
// Compatible with city_model.dart v3
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'dart:convert';
import '../services/trip_update_service.dart';
import 'dart:ui';

import '../models/city_model.dart';

class DetailScreen extends StatefulWidget {
  final Highlight place;

  const DetailScreen({super.key, required this.place});

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen>
    with SingleTickerProviderStateMixin {
  // ══════════════════════════════════════════════════════════════════════════
  // RENK PALETİ
  // ══════════════════════════════════════════════════════════════════════════
  // AMBER/GOLD THEME
  // ══════════════════════════════════════════════════════════════════════════

  static const Color bgDark = Color(0xFF0D0D1A);
  static const Color bgCard = Color(0xFF1A1A2E);
  static const Color bgCardLight = Color(0xFF252542);
  static const Color accent = Color(0xFFF5A623); // Amber
  static const Color accentLight = Color(0xFFFFB800); // Gold
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFF5A623), Color(0xFFFFB800)],
  );

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  final ScrollController _scrollController = ScrollController();
  double _scrollOffset = 0;
  bool _isFavorite = false;
  bool _isInTrip = false;
  List<String> _tripPlaces = [];

  late AnimationController _animController;
  late Animation<double> _fadeAnim;

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    _loadPreferences();
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);

    _animController = AnimationController(
      duration: const Duration(milliseconds: 600),
      vsync: this,
    );
    _fadeAnim = Tween<double>(
      begin: 0,
      end: 1,
    ).animate(CurvedAnimation(parent: _animController, curve: Curves.easeOut));
    _animController.forward();
  }

  @override
  void dispose() {
    TripUpdateService().tripUpdated.removeListener(_onTripDataChanged);
    _scrollController.dispose();
    _animController.dispose();
    super.dispose();
  }

  void _onTripDataChanged() {
    _loadPreferences();
  }

  void _onScroll() {
    setState(() => _scrollOffset = _scrollController.offset);
  }

  Future<void> _loadPreferences() async {
    final prefs = await SharedPreferences.getInstance();
    final favorites = prefs.getStringList("favorite_places") ?? [];
    _tripPlaces = prefs.getStringList("trip_places") ?? [];

    setState(() {
      _isFavorite = favorites.contains(widget.place.name);
      _isInTrip = _tripPlaces.contains(widget.place.name);
    });
  }

  Future<void> _toggleFavorite() async {
    HapticFeedback.lightImpact();
    final prefs = await SharedPreferences.getInstance();
    final favorites = prefs.getStringList("favorite_places") ?? [];

    setState(() {
      _isFavorite = !_isFavorite;
      if (_isFavorite) {
        favorites.add(widget.place.name);
      } else {
        favorites.remove(widget.place.name);
      }
    });

    await prefs.setStringList("favorite_places", favorites);
  }

  Future<void> _toggleTrip() async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();

    final String name = widget.place.name;
    
    // 1. Güncel verileri oku
    final List<String> tripPlaces = prefs.getStringList("trip_places") ?? [];
    final String? scheduleJson = prefs.getString("trip_schedule");
    
    // Schedule'ı parse et
    Map<String, dynamic> scheduleMap = {};
    if (scheduleJson != null) {
      try {
        scheduleMap = jsonDecode(scheduleJson);
      } catch (e) { print(e); }
    }
    
    // Toplam gün sayısını bul
    int maxDay = 1;
    scheduleMap.keys.forEach((k) {
       final d = int.tryParse(k) ?? 1;
       if (d > maxDay) maxDay = d;
    });
    final onboardingDays = prefs.getInt("tripDays") ?? 3;
    if (maxDay < onboardingDays) maxDay = onboardingDays;

    // Logic: Şimdiki durumu kaydet
    final bool wasInTrip = _isInTrip;

    if (wasInTrip) {
        // ÇIKARMA İŞLEMİ
        setState(() => _isInTrip = false);
        tripPlaces.remove(name);
        
         // Schedule'dan da sil
        scheduleMap.keys.forEach((day) {
             final List<dynamic> list = scheduleMap[day] ?? [];
             list.remove(name);
             scheduleMap[day] = list;
        });
        
        // Save & Notify
        await prefs.setStringList("trip_places", tripPlaces);
        await prefs.setString("trip_schedule", jsonEncode(scheduleMap));
        TripUpdateService().notifyTripChanged();
        
         if (mounted) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Row(
                 children: [
                   const Icon(Icons.remove_circle_outline, color: Colors.white, size: 20),
                   const SizedBox(width: 12),
                   const Text("Rotadan çıkarıldı", style: TextStyle(fontWeight: FontWeight.w500)),
                 ],
               ),
               backgroundColor: bgCardLight,
               behavior: SnackBarBehavior.floating,
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 90),
            ));
         }

    } else {
        // EKLEME İŞLEMİ (Dialog)
         final selectedDay = await _showDaySelectionDialogForDetail(maxDay, name);
         if (selectedDay == null) return;
         
         setState(() => _isInTrip = true);
         tripPlaces.add(name);
         
         final dayKey = selectedDay.toString();
         List<dynamic> targetList = scheduleMap[dayKey] ?? [];
         if (!targetList.contains(name)) {
            targetList.add(name);
         }
         scheduleMap[dayKey] = targetList;
         
        // Save & Notify
        await prefs.setStringList("trip_places", tripPlaces);
        await prefs.setString("trip_schedule", jsonEncode(scheduleMap));
        TripUpdateService().notifyTripChanged();

         if (mounted) {
            ScaffoldMessenger.of(context).showSnackBar(SnackBar(
               content: Row(
                 children: [
                   const Icon(Icons.check_circle, color: Colors.white, size: 20),
                   const SizedBox(width: 12),
                   Text("Rotaya eklendi! ($selectedDay. Gün)", style: const TextStyle(fontWeight: FontWeight.w500)),
                 ],
               ),
               backgroundColor: Colors.green.shade600,
               behavior: SnackBarBehavior.floating,
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 90),
            ));
         }
    }
  }

  Future<int?> _showDaySelectionDialogForDetail(int totalDays, String placeName) async {
    return showDialog<int>(
      context: context,
      builder: (context) {
        return Dialog(
          backgroundColor: bgCard,
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Text("Hangi Güne Eklensin?", style: TextStyle(color: textWhite, fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                Text("'$placeName' rotaya eklensin mi?", textAlign: TextAlign.center, style: const TextStyle(color: textGrey, fontSize: 14)),
                const SizedBox(height: 20),
                ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 400),
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                         ...List.generate(totalDays, (index) {
                             final day = index + 1;
                             return ListTile(
                               title: Text("Gün $day", style: const TextStyle(color: textWhite)),
                               trailing: const Icon(Icons.add_circle_outline, color: accent),
                               onTap: () => Navigator.pop(context, day),
                             );
                         }),
                         const Divider(color: borderColor),
                         ListTile(
                             title: const Text("Yeni Gün Oluştur", style: TextStyle(color: textWhite)),
                             subtitle: Text("Gün ${totalDays + 1}", style: const TextStyle(color: textGrey, fontSize: 12)),
                             leading: const Icon(Icons.add, color: accentLight), // accentGreen yerine accentLight kullandim detail screen renk paletine uysun diye
                             onTap: () => Navigator.pop(context, totalDays + 1),
                         ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  Future<void> _openMaps() async {
    final place = widget.place;
    final query = Uri.encodeComponent("${place.name}, ${place.area}");
    final url = "https://www.google.com/maps/search/?api=1&query=$query";

    if (await canLaunchUrl(Uri.parse(url))) {
      await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
    }
  }

  Future<void> _sharePlace() async {
    HapticFeedback.lightImpact();
    // Share functionality
  }

  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    final place = widget.place;
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final screenHeight = MediaQuery.of(context).size.height;
    final heroHeight = screenHeight * 0.45;

    final appBarOpacity = ((_scrollOffset / (heroHeight - 120)).clamp(
      0.0,
      1.0,
    ));

    return Scaffold(
      backgroundColor: bgDark,
      extendBodyBehindAppBar: true,
      appBar: _buildAppBar(appBarOpacity),
      body: Stack(
        children: [
          // Content
          FadeTransition(
            opacity: _fadeAnim,
            child: CustomScrollView(
              controller: _scrollController,
              physics: const BouncingScrollPhysics(),
              slivers: [
                // Hero Image
                SliverToBoxAdapter(
                  child: _buildHeroImage(heroHeight, hasImage),
                ),

                // Content
                SliverToBoxAdapter(child: _buildContent()),
              ],
            ),
          ),

          // Floating Button
          _buildFloatingButton(),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // APP BAR
  // ══════════════════════════════════════════════════════════════════════════

  PreferredSizeWidget _buildAppBar(double opacity) {
    return AppBar(
      backgroundColor: bgDark.withOpacity(opacity),
      elevation: 0,
      systemOverlayStyle: SystemUiOverlayStyle.light,
      leading: Padding(
        padding: const EdgeInsets.all(8),
        child: GestureDetector(
          onTap: () => Navigator.pop(context),
          child: Container(
            decoration: BoxDecoration(
              color: opacity > 0.5
                  ? bgCardLight
                  : Colors.black.withOpacity(0.4),
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.arrow_back, color: Colors.white),
          ),
        ),
      ),
      title: AnimatedOpacity(
        opacity: opacity,
        duration: const Duration(milliseconds: 150),
        child: Text(
          widget.place.name,
          style: const TextStyle(
            color: textWhite,
            fontWeight: FontWeight.w600,
            fontSize: 18,
          ),
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
        ),
      ),
      actions: [
        // Favorite
        Padding(
          padding: const EdgeInsets.only(right: 4),
          child: GestureDetector(
            onTap: _toggleFavorite,
            child: Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: opacity > 0.5
                    ? bgCardLight
                    : Colors.black.withOpacity(0.4),
                shape: BoxShape.circle,
              ),
              child: Icon(
                _isFavorite ? Icons.favorite : Icons.favorite_border,
                color: _isFavorite ? accent : Colors.white,
                size: 22,
              ),
            ),
          ),
        ),
        // Share
        Padding(
          padding: const EdgeInsets.only(right: 16),
          child: GestureDetector(
            onTap: _sharePlace,
            child: Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: opacity > 0.5
                    ? bgCardLight
                    : Colors.black.withOpacity(0.4),
                shape: BoxShape.circle,
              ),
              child: const Icon(
                Icons.share_outlined,
                color: Colors.white,
                size: 22,
              ),
            ),
          ),
        ),
      ],
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // HERO IMAGE
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildHeroImage(double height, bool hasImage) {
    final place = widget.place;

    return SizedBox(
      height: height,
      child: Stack(
        fit: StackFit.expand,
        children: [
          // Image
          if (hasImage)
            Image.network(
              place.imageUrl!,
              fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => _buildPlaceholder(),
            )
          else
            _buildPlaceholder(),

          // Gradient overlay
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  Colors.black.withOpacity(0.3),
                  Colors.transparent,
                  bgDark.withOpacity(0.8),
                  bgDark,
                ],
                stops: const [0.0, 0.3, 0.8, 1.0],
              ),
            ),
          ),

          // Bottom info
          Positioned(
            left: 20,
            right: 20,
            bottom: 20,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Category + Rating row
                Row(
                  children: [
                    // Category chip
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        gradient: primaryGradient,
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            _getCategoryIcon(place.category),
                            color: Colors.white,
                            size: 14,
                          ),
                          const SizedBox(width: 6),
                          Text(
                            place.category,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(width: 10),
                    // Rating
                    if (place.rating != null)
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 10,
                          vertical: 6,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.5),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Row(
                          children: [
                            const Icon(
                              Icons.star,
                              color: Color(0xFFFFC107),
                              size: 16,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              place.rating!.toStringAsFixed(1),
                              style: const TextStyle(
                                color: Colors.white,
                                fontSize: 14,
                                fontWeight: FontWeight.w700,
                              ),
                            ),
                            if (place.reviewCount != null) ...[
                              const SizedBox(width: 4),
                              Text(
                                "(${place.reviewCount})",
                                style: TextStyle(
                                  color: Colors.white.withOpacity(0.7),
                                  fontSize: 12,
                                ),
                              ),
                            ],
                          ],
                        ),
                      ),
                  ],
                ),
                const SizedBox(height: 14),
                // Name
                Text(
                  place.name,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 28,
                    fontWeight: FontWeight.w700,
                    height: 1.2,
                  ),
                ),
                const SizedBox(height: 8),
                // Location
                Row(
                  children: [
                    Icon(Icons.location_on, color: textGrey, size: 16),
                    const SizedBox(width: 4),
                    Expanded(
                      child: Text(
                        place.area,
                        style: const TextStyle(color: textGrey, fontSize: 14),
                        overflow: TextOverflow.ellipsis,
                      ),
                    ),
                    const SizedBox(width: 12),
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 8,
                        vertical: 4,
                      ),
                      decoration: BoxDecoration(
                        color: bgCardLight,
                        borderRadius: BorderRadius.circular(6),
                      ),
                      child: Text(
                        "${place.distanceFromCenter.toStringAsFixed(1)} km",
                        style: const TextStyle(
                          color: textWhite,
                          fontSize: 12,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildPlaceholder() {
    final color = _getCategoryColor(widget.place.category);
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [color, color.withOpacity(0.6)],
        ),
      ),
      child: Center(
        child: Icon(
          _getCategoryIcon(widget.place.category),
          size: 80,
          color: Colors.white.withOpacity(0.3),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // CONTENT
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildContent() {
    final place = widget.place;

    return Container(
      color: bgDark,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Quick Actions
          _buildQuickActions(),

          // Description
          if (place.description.isNotEmpty) _buildDescriptionCard(),

          // Info Cards
          _buildInfoCards(),

          // Tags
          if (place.tags.isNotEmpty) _buildTagsSection(),

          // Tips (Local Tip)
          if (place.tips != null && place.tips!.isNotEmpty) _buildTipsCard(),

          // Features
          if (place.features != null && place.features!.isNotEmpty)
            _buildFeaturesSection(),

          // Open Hours
          if (place.openHours != null && place.openHours!.isNotEmpty)
            _buildOpenHoursSection(),

          // Related Places
          _buildRelatedSection(),

          // Bottom padding
          const SizedBox(height: 120),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // QUICK ACTIONS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildQuickActions() {
    return Container(
      margin: const EdgeInsets.all(20),
      child: Row(
        children: [
          _buildActionButton(
            icon: Icons.directions,
            label: "Yol Tarifi",
            onTap: _openMaps,
          ),
          const SizedBox(width: 12),
          _buildActionButton(
            icon: _isFavorite ? Icons.favorite : Icons.favorite_border,
            label: "Kaydet",
            onTap: _toggleFavorite,
            isActive: _isFavorite,
          ),
          const SizedBox(width: 12),
          _buildActionButton(
            icon: Icons.share_outlined,
            label: "Paylaş",
            onTap: _sharePlace,
          ),
        ],
      ),
    );
  }

  Widget _buildActionButton({
    required IconData icon,
    required String label,
    required VoidCallback onTap,
    bool isActive = false,
  }) {
    return Expanded(
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 14),
          decoration: BoxDecoration(
            color: isActive ? accent.withOpacity(0.15) : bgCard,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: isActive ? accent : borderColor),
          ),
          child: Column(
            children: [
              Icon(icon, color: isActive ? accent : textWhite, size: 22),
              const SizedBox(height: 6),
              Text(
                label,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w500,
                  color: isActive ? accent : textGrey,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DESCRIPTION CARD
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildDescriptionCard() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Icon(Icons.info_outline, color: accentLight, size: 20),
              SizedBox(width: 10),
              Text(
                "Hakkında",
                style: TextStyle(
                  color: textWhite,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            widget.place.description,
            style: const TextStyle(color: textGrey, fontSize: 14, height: 1.6),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // INFO CARDS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildInfoCards() {
    final place = widget.place;

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      child: Column(
        children: [
          // Row 1: Konum + Mesafe
          Row(
            children: [
              Expanded(
                child: _buildInfoCard(
                  icon: Icons.location_on_outlined,
                  title: "Konum",
                  value: place.area,
                  color: const Color(0xFF4CAF50),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _buildInfoCard(
                  icon: Icons.straighten,
                  title: "Mesafe",
                  value: "${place.distanceFromCenter.toStringAsFixed(1)} km",
                  color: const Color(0xFF2196F3),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          // Row 2: Fiyat + En İyi Zaman
          Row(
            children: [
              Expanded(
                child: _buildInfoCard(
                  icon: Icons.euro,
                  title: "Fiyat",
                  value: _getPriceText(place.price),
                  color: const Color(0xFFFF9800),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _buildInfoCard(
                  icon: Icons.schedule,
                  title: "En İyi Zaman",
                  value: place.bestTime ?? "Her zaman",
                  color: accentLight,
                ),
              ),
            ],
          ),
          // Row 3: Metro + Duration (if available)
          if (place.metro != null || place.duration != null) ...[
            const SizedBox(height: 12),
            Row(
              children: [
                if (place.metro != null)
                  Expanded(
                    child: _buildInfoCard(
                      icon: Icons.subway,
                      title: "Metro",
                      value: place.metro!,
                      color: const Color(0xFFE91E63),
                    ),
                  ),
                if (place.metro != null && place.duration != null)
                  const SizedBox(width: 12),
                if (place.duration != null)
                  Expanded(
                    child: _buildInfoCard(
                      icon: Icons.timer_outlined,
                      title: "Süre",
                      value: place.duration!,
                      color: const Color(0xFF00BCD4),
                    ),
                  ),
              ],
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildInfoCard({
    required IconData icon,
    required String title,
    required String value,
    required Color color,
  }) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: color.withOpacity(0.15),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Icon(icon, color: color, size: 20),
          ),
          const SizedBox(height: 12),
          Text(title, style: const TextStyle(color: textGrey, fontSize: 12)),
          const SizedBox(height: 4),
          Text(
            value,
            style: const TextStyle(
              color: textWhite,
              fontSize: 14,
              fontWeight: FontWeight.w600,
            ),
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
          ),
        ],
      ),
    );
  }

  String _getPriceText(String price) {
    switch (price.toLowerCase()) {
      case "free":
        return "Ücretsiz";
      case "low":
        return "€ Uygun";
      case "medium":
        return "€€ Orta";
      case "high":
        return "€€€ Pahalı";
      case "luxury":
        return "€€€€ Lüks";
      default:
        return price;
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TAGS SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTagsSection() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Özellikler",
            style: TextStyle(
              color: textWhite,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: widget.place.tags.map((tag) {
              return Container(
                padding: const EdgeInsets.symmetric(
                  horizontal: 14,
                  vertical: 8,
                ),
                decoration: BoxDecoration(
                  color: bgCard,
                  borderRadius: BorderRadius.circular(20),
                  border: Border.all(color: borderColor),
                ),
                child: Text(
                  tag,
                  style: const TextStyle(fontSize: 13, color: textGrey),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TIPS CARD (Local Tip)
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTipsCard() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(16),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  const Color(0xFFFFC107).withOpacity(0.2),
                  const Color(0xFFFF9800).withOpacity(0.1),
                ],
              ),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(
                color: const Color(0xFFFFC107).withOpacity(0.3),
              ),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.all(10),
                  decoration: BoxDecoration(
                    color: const Color(0xFFFFC107),
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Icon(
                    Icons.lightbulb_outline,
                    color: Colors.white,
                    size: 20,
                  ),
                ),
                const SizedBox(width: 14),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      const Text(
                        "Lokal İpucu 💡",
                        style: TextStyle(
                          color: Color(0xFFFFC107),
                          fontSize: 15,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                      const SizedBox(height: 6),
                      Text(
                        widget.place.tips!,
                        style: TextStyle(
                          color: textWhite.withOpacity(0.9),
                          fontSize: 14,
                          height: 1.5,
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // FEATURES SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildFeaturesSection() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Icon(Icons.star_outline, color: accent, size: 20),
              SizedBox(width: 10),
              Text(
                "Öne Çıkanlar",
                style: TextStyle(
                  color: textWhite,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          ...widget.place.features!.map((feature) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Row(
                children: [
                  const Icon(Icons.check_circle, color: accentLight, size: 18),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      feature,
                      style: const TextStyle(color: textGrey, fontSize: 14),
                    ),
                  ),
                ],
              ),
            );
          }).toList(),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // OPEN HOURS SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildOpenHoursSection() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Row(
            children: [
              Icon(Icons.access_time, color: Color(0xFF4CAF50), size: 20),
              SizedBox(width: 10),
              Text(
                "Çalışma Saatleri",
                style: TextStyle(
                  color: textWhite,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          ...widget.place.openHours!.entries.map((entry) {
            return Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    entry.key,
                    style: const TextStyle(color: textGrey, fontSize: 14),
                  ),
                  Text(
                    entry.value,
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 14,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ),
            );
          }).toList(),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // RELATED SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildRelatedSection() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Yakınlarda Keşfet",
            style: TextStyle(
              color: textWhite,
              fontSize: 18,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 16),
          SizedBox(
            height: 140,
            child: ListView(
              scrollDirection: Axis.horizontal,
              children: [
                _buildRelatedCard(
                  "Yürüyüş Turu",
                  Icons.directions_walk,
                  const Color(0xFF4CAF50),
                ),
                _buildRelatedCard(
                  "Gastronomi",
                  Icons.restaurant,
                  const Color(0xFFFF5252),
                ),
                _buildRelatedCard(
                  "Fotoğraf Noktaları",
                  Icons.camera_alt,
                  const Color(0xFF2196F3),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildRelatedCard(String title, IconData icon, Color color) {
    return Container(
      width: 130,
      margin: const EdgeInsets.only(right: 12),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: color.withOpacity(0.15),
              shape: BoxShape.circle,
            ),
            child: Icon(icon, color: color, size: 28),
          ),
          const SizedBox(height: 12),
          Text(
            title,
            style: const TextStyle(
              color: textWhite,
              fontSize: 13,
              fontWeight: FontWeight.w500,
            ),
            textAlign: TextAlign.center,
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // FLOATING BUTTON
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildFloatingButton() {
    return Positioned(
      left: 20,
      right: 20,
      bottom: 20,
      child: SafeArea(
        child: GestureDetector(
          onTap: _toggleTrip,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 250),
            height: 58,
            decoration: BoxDecoration(
              gradient: _isInTrip ? null : primaryGradient,
              color: _isInTrip ? Colors.green.shade600 : null,
              borderRadius: BorderRadius.circular(16),
              boxShadow: [
                BoxShadow(
                  color: (_isInTrip ? Colors.green : accentLight).withOpacity(
                    0.4,
                  ),
                  blurRadius: 20,
                  offset: const Offset(0, 8),
                ),
              ],
            ),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  _isInTrip ? Icons.check_circle : Icons.add_circle_outline,
                  color: Colors.white,
                  size: 24,
                ),
                const SizedBox(width: 10),
                Text(
                  _isInTrip ? "Rotaya Eklendi ✓" : "Rotaya Ekle",
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // HELPERS
  // ══════════════════════════════════════════════════════════════════════════

  Color _getCategoryColor(String category) {
    final colors = {
      'Restoran': const Color(0xFFFF5252),
      'Bar': const Color(0xFF9C27B0),
      'Kafe': const Color(0xFFFF9800),
      'Müze': const Color(0xFF2196F3),
      'Tarihi': const Color(0xFF795548),
      'Park': const Color(0xFF4CAF50),
      'Manzara': const Color(0xFF00BCD4),
      'Alışveriş': const Color(0xFFE91E63),
      'Semt': const Color(0xFF673AB7),
    };
    return colors[category] ?? const Color(0xFF607D8B);
  }

  IconData _getCategoryIcon(String category) {
    final icons = {
      'Restoran': Icons.restaurant,
      'Bar': Icons.local_bar,
      'Kafe': Icons.coffee,
      'Müze': Icons.museum,
      'Tarihi': Icons.account_balance,
      'Park': Icons.park,
      'Manzara': Icons.landscape,
      'Alışveriş': Icons.shopping_bag,
      'Semt': Icons.location_city,
    };
    return icons[category] ?? Icons.place;
  }
}
