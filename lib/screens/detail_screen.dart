// =============================================================================
// DETAIL SCREEN – WANDERLUST DARK THEME
// Full-screen hero, glassmorphism cards, purple/pink accents
// Compatible with city_model.dart v3
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:share_plus/share_plus.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:convert';
import '../services/badge_service.dart';
import '../services/trip_update_service.dart';
import 'dart:ui';

import 'dart:math' as math;

import '../models/city_model.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../services/location_context_service.dart';
import '../services/city_data_loader.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';
import '../services/tutorial_service.dart';
import '../widgets/tutorial_overlay_widget.dart';
import '../widgets/custom_toast.dart';
import '../services/premium_service.dart';
import 'paywall_screen.dart';

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

  static const Color bgDark = WanderlustColors.bgDark;
  static const Color bgCard = WanderlustColors.bgCard;
  static const Color bgCardLight = WanderlustColors.bgCardLight;
  static const Color accent = WanderlustColors.accent; // Standard Solid Violet
  static const Color accentLight = Color(0xFFFFB800); // Gold
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);

  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [WanderlustColors.accent, WanderlustColors.accent],
  );

  // ══════════════════════════════════════════════════════════════════════════
  // STATE
  // ══════════════════════════════════════════════════════════════════════════

  final ScrollController _scrollController = ScrollController();
  final GlobalKey _addToRouteKey = GlobalKey(); // Key for Tutorial
  final GlobalKey _checkInKey = GlobalKey(); // Key for Check-in Tutorial
  double _scrollOffset = 0;
  bool _isFavorite = false;
  bool _isInTrip = false;
  bool _isVisited = false;
  bool _isCheckingIn = false;
  List<String> _tripPlaces = [];

  late AnimationController _animController;
  late Animation<double> _fadeAnim;

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_onScroll);
    _loadPreferences();
    TripUpdateService().tripUpdated.addListener(_onTripDataChanged);
    _initLocationContext();

    _animController = AnimationController(
      duration: const Duration(milliseconds: 600),
      vsync: this,
    );
    _fadeAnim = Tween<double>(
      begin: 0,
      end: 1,
    ).animate(CurvedAnimation(parent: _animController, curve: Curves.easeOut));
    _animController.forward();
    
    // Schedule Tutorial
    WidgetsBinding.instance.addPostFrameCallback((_) {
       Future.delayed(const Duration(seconds: 1), _showRouteTutorial);
    });
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

  Future<void> _initLocationContext() async {
    final prefs = await SharedPreferences.getInstance();
    final currentCity = prefs.getString("selectedCity") ?? "barcelona";
    try {
      final cityModel = await CityDataLoader.loadCity(currentCity);
      LocationContextService.instance.updateContext(cityModel);
    } catch (e) {
      debugPrint("Context update error: $e");
    }
  }

  void _onScroll() {
    setState(() => _scrollOffset = _scrollController.offset);
  }

  Future<void> _loadPreferences() async {
    final prefs = await SharedPreferences.getInstance();
    final favorites = prefs.getStringList("favorite_places") ?? [];
    final visited = prefs.getStringList("visited_places") ?? [];
    _tripPlaces = prefs.getStringList("trip_places") ?? [];
    final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    final placeKey = "$currentCity:${widget.place.name}";

    setState(() {
      // Check both old format (name only) and new format (city:name)
      _isFavorite = favorites.contains(placeKey) || favorites.contains(widget.place.name);
      _isInTrip = _tripPlaces.contains(widget.place.name);
      _isVisited = visited.contains(placeKey) || visited.contains(widget.place.name);
    });
  }

  Future<void> _toggleFavorite() async {
    HapticFeedback.lightImpact();
    final prefs = await SharedPreferences.getInstance();
    final favorites = prefs.getStringList("favorite_places") ?? [];
    final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    final placeKey = "$currentCity:${widget.place.name}";

    setState(() {
      _isFavorite = !_isFavorite;
      if (_isFavorite) {
        // Remove old format if exists and add new format
        favorites.remove(widget.place.name);
        if (!favorites.contains(placeKey)) {
          favorites.add(placeKey);
        }
      } else {
        // Remove both old and new format
        favorites.remove(widget.place.name);
        favorites.remove(placeKey);
      }
    });

    await prefs.setStringList("favorite_places", favorites);
    TripUpdateService().notifyFavoritesChanged();
  }

  Future<void> _checkIn() async {
    if (_isVisited || _isCheckingIn) return;
    
    setState(() => _isCheckingIn = true);
    HapticFeedback.heavyImpact();

    try {
      // Check location permission
      LocationPermission permission = await Geolocator.checkPermission();
      if (permission == LocationPermission.denied) {
        permission = await Geolocator.requestPermission();
        if (permission == LocationPermission.denied) {
          _showCheckInError(AppLocalizations.instance.locationPermissionRequired);
          return;
        }
      }
      
      if (permission == LocationPermission.deniedForever) {
        _showCheckInError(AppLocalizations.instance.locationPermissionSettings);
        return;
      }

      // Get current location
      final position = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.high,
      );

      // Calculate distance to place
      final distance = Geolocator.distanceBetween(
        position.latitude,
        position.longitude,
        widget.place.lat,
        widget.place.lng,
      );

      // Check if within 200 meters (BYPASSED FOR TESTING)
      // TODO: Remove `|| true` after testing
      if (distance <= 200) {
        // Success! Save visited place
        final prefs = await SharedPreferences.getInstance();
        final visited = prefs.getStringList("visited_places") ?? [];
        final currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
        final placeKey = "$currentCity:${widget.place.name}";
        
        // Remove old format if exists
        visited.remove(widget.place.name);
        if (!visited.contains(placeKey)) {
          visited.add(placeKey);
          await prefs.setStringList("visited_places", visited);
        }
        
        setState(() {
          _isVisited = true;
          _isCheckingIn = false;
        });
        
        // Profile sayfasını güncelle
        TripUpdateService().notifyVisitChanged();
        BadgeService().addDistance(0.5); // Her check-in 0.5 km

        
        _showCheckInSuccess(visited.length);
      } else {
        // Too far away
        final distanceText = distance >= 1000 
            ? "${(distance / 1000).toStringAsFixed(1)} km"
            : "${distance.toInt()} m";
        _showCheckInError(AppLocalizations.instance.tooFarAway(distanceText));
      }
    } catch (e) {
      _showCheckInError(AppLocalizations.instance.locationError);
    } finally {
      if (mounted) setState(() => _isCheckingIn = false);
    }
  }

  void _showCheckInError(String message) {
    if (!mounted) return;
    CustomToast.show(context, message, isError: true);
  }

  void _showCheckInSuccess(int totalVisited) {
    if (!mounted) return;
    HapticFeedback.heavyImpact();
    
    showDialog(
      context: context,
      builder: (context) => Dialog(
        backgroundColor: Colors.transparent,
        insetPadding: const EdgeInsets.symmetric(horizontal: 40),
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 32, horizontal: 24),
          decoration: BoxDecoration(
            color: const Color(0xFF1A1A1A), // Sleek neutral dark
            borderRadius: BorderRadius.circular(28),
            border: Border.all(color: Colors.white.withOpacity(0.1)),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.5),
                blurRadius: 30,
                spreadRadius: 10,
              ),
            ],
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // Premium check icon with subtle outer ring
              Container(
                width: 90,
                height: 90,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(color: accent.withOpacity(0.3), width: 1.5),
                  color: accent.withOpacity(0.05),
                ),
                child: Center(
                  child: Container(
                    width: 70,
                    height: 70,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: accent,
                      boxShadow: [
                        BoxShadow(
                          color: accent.withOpacity(0.3),
                          blurRadius: 12,
                          offset: const Offset(0, 4),
                        ),
                      ],
                    ),
                    child: const Icon(Icons.check_rounded, color: Colors.white, size: 40),
                  ),
                ),
              ),
              const SizedBox(height: 28),
              
              // Place Name (Main Title)
              Text(
                widget.place.getLocalizedName(AppLocalizations.instance.isEnglish),
                textAlign: TextAlign.center,
                style: GoogleFonts.poppins(
                  color: accent,
                  fontSize: 22,
                  fontWeight: FontWeight.w800,
                  letterSpacing: -0.3,
                ),
              ),
              const SizedBox(height: 8),
              
              // "ziyaret edildi!" status
              Text(
                AppLocalizations.instance.placeVisited,
                style: GoogleFonts.poppins(
                  color: Colors.white.withOpacity(0.7),
                  fontSize: 16,
                  fontWeight: FontWeight.w500,
                ),
              ),
              const SizedBox(height: 24),
              
              // Discovery Badge (Dark minimal style)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.05),
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.white.withOpacity(0.05)),
                ),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Icon(Icons.location_on_rounded, color: accent, size: 20),
                    const SizedBox(width: 8),
                    Text(
                      AppLocalizations.instance.totalDiscovered(totalVisited),
                      style: GoogleFonts.poppins(
                        color: Colors.white.withOpacity(0.9),
                        fontSize: 14,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 32),
              
              // Action Button (Solid Premium Gold)
              ElevatedButton(
                onPressed: () => Navigator.pop(context),
                style: ElevatedButton.styleFrom(
                  backgroundColor: accent,
                  foregroundColor: Colors.white,
                  minimumSize: const Size(double.infinity, 56),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                  elevation: 0,
                ),
                child: Text(
                  AppLocalizations.instance.continueButton,
                  style: GoogleFonts.poppins(
                    fontSize: 16,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _toggleTrip() async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();

    final String name = widget.place.name;
    final String currentCity = (prefs.getString("selectedCity") ?? "barcelona").toLowerCase();
    
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
        
         // Schedule'dan da sil (hem eski hem yeni format)
        scheduleMap.keys.forEach((day) {
             final List<dynamic> list = scheduleMap[day] ?? [];
             // Eski format: string, yeni format: {name, city}
             list.removeWhere((item) {
               if (item is String) return item == name;
               if (item is Map<String, dynamic>) return item['name'] == name;
               return false;
             });
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
                   const Icon(Icons.remove_circle_outline, color: WanderlustColors.accent, size: 20),
                   const SizedBox(width: 12),
                   const Text("Rotadan çıkarıldı", style: TextStyle(fontWeight: FontWeight.w500)),
                 ],
               ),
               backgroundColor: bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 1200),
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 90),
            ));
         }

    } else {
        // EKLEME İŞLEMİ
        
        // Premium limit kontrolü
        if (!PremiumService.instance.canAddToRoute()) {
          _showPaywall();
          return;
        }
        
        final selectedDay = await _showDaySelectionDialogForDetail(maxDay, name, scheduleMap);
        if (selectedDay == null) return;
        
        // Kullanımı artır
        await PremiumService.instance.useRouteAdd();
         
         setState(() => _isInTrip = true);
         tripPlaces.add(name);
         
         final dayKey = selectedDay.toString();
         List<dynamic> targetList = scheduleMap[dayKey] ?? [];
         
         // Yeni format: {name, city} olarak ekle
         final placeEntry = {'name': name, 'city': currentCity};
         final alreadyExists = targetList.any((item) {
           if (item is Map<String, dynamic>) return item['name'] == name;
           if (item is String) return item == name;
           return false;
         });
         
         if (!alreadyExists) {
            targetList.add(placeEntry);
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
                   const Icon(Icons.check_circle, color: WanderlustColors.accent, size: 20),
                   const SizedBox(width: 12),
                   Text("Rotaya eklendi! ($selectedDay. Gün)", style: const TextStyle(fontWeight: FontWeight.w500)),
                 ],
               ),
               backgroundColor: bgCardLight,
               behavior: SnackBarBehavior.floating,
               duration: const Duration(milliseconds: 1200),
               shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
               margin: const EdgeInsets.fromLTRB(16, 0, 16, 90),
            ));
         }
    }
  }

  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }

  Future<int?> _showDaySelectionDialogForDetail(int totalDays, String placeName, Map<String, dynamic> scheduleMap) async {
    return showDialog<int>(
      context: context,
      barrierColor: Colors.black.withOpacity(0.7),
      builder: (context) {
        return Dialog(
          backgroundColor: const Color(0xFF1A1A2E),

          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          child: Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(AppLocalizations.instance.whichDay, style: TextStyle(color: textWhite, fontSize: 18, fontWeight: FontWeight.bold)),
                const SizedBox(height: 8),
                Text(AppLocalizations.instance.addToRouteConfirmDialog(placeName), textAlign: TextAlign.center, style: const TextStyle(color: textGrey, fontSize: 14)),
                const SizedBox(height: 20),
                ConstrainedBox(
                  constraints: const BoxConstraints(maxHeight: 400),
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                         ...List.generate(totalDays, (index) {
                             final day = index + 1;
                             final dayKey = day.toString();
                             final List<dynamic> dayPlaces = scheduleMap[dayKey] ?? [];
                             final count = dayPlaces.length;
                             return ListTile(
                               title: Text(AppLocalizations.instance.dayN(day), style: const TextStyle(color: textWhite)),
                               subtitle: Text(AppLocalizations.instance.nPlaces(count), style: const TextStyle(color: textGrey, fontSize: 12)),
                               trailing: const Icon(Icons.arrow_forward_ios, color: accent, size: 16),
                               onTap: () => Navigator.pop(context, day),
                             );
                         }),
                         const Divider(color: borderColor),
                         ListTile(
                             title: Text(AppLocalizations.instance.createNewDay, style: TextStyle(color: textWhite)),
                             subtitle: Text(AppLocalizations.instance.dayN(totalDays + 1), style: const TextStyle(color: textGrey, fontSize: 12)),
                             leading: const Icon(Icons.add, color: accentLight),
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
    // Premium limit kontrolü
    if (!PremiumService.instance.canGetDirections()) {
      _showPaywall();
      return;
    }
    
    final place = widget.place;
    final location = place.area.isNotEmpty ? place.area : (place.city ?? "");
    final query = Uri.encodeComponent("${place.name}, $location");
    final url = "https://www.google.com/maps/search/?api=1&query=$query";

    if (await canLaunchUrl(Uri.parse(url))) {
      await launchUrl(Uri.parse(url), mode: LaunchMode.externalApplication);
      // Kullanımı artır
      await PremiumService.instance.useDirections();
    }
  }

  Future<void> _sharePlace() async {
    HapticFeedback.lightImpact();
    final isEnglish = AppLocalizations.instance.isEnglish;
    final place = widget.place;
    
    // Construct Google Maps link
    final location = place.area.isNotEmpty ? place.area : (place.city ?? "");
    final query = Uri.encodeComponent("${place.name}, $location");
    final mapsUrl = "https://www.google.com/maps/search/?api=1&query=$query";
    
    final appLink = "https://apps.apple.com/app/id6741743515";
    
    final message = isEnglish
        ? "I found an amazing place on My Way: ${place.name}!\n\nLocation: $mapsUrl\n\nDiscover more smart routes and hidden gems: $appLink"
        : "My Way'de harika bir yer buldum: ${place.name}!\n\nKonum: $mapsUrl\n\nAkıllı rotalar ve gizli yerler keşfetmek için sen de indir: $appLink";
    
    await Share.share(message);
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
          widget.place.getLocalizedName(AppLocalizations.instance.isEnglish),
          style: GoogleFonts.poppins(
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
                        color: accent,
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
                            AppLocalizations.instance.translateCategory(place.category),
                            style: GoogleFonts.poppins(
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
                              Icons.star_rounded,
                              color: Color(0xFFFDCB6E),
                              size: 16,
                            ),
                            const SizedBox(width: 4),
                            Text(
                              place.rating!.toStringAsFixed(1),
                              style: GoogleFonts.poppins(
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
                  place.getLocalizedName(AppLocalizations.instance.isEnglish),
                  style: GoogleFonts.poppins(
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
                          place.area.isNotEmpty ? place.area : (place.city ?? ""),
                          style: GoogleFonts.poppins(color: textGrey, fontSize: 14),
                          overflow: TextOverflow.ellipsis,
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
            label: AppLocalizations.instance.getDirections,
            onTap: _openMaps,
          ),
          const SizedBox(width: 12),
          _buildActionButton(
            icon: _isFavorite ? Icons.favorite : Icons.favorite_border,
            label: AppLocalizations.instance.save,
            onTap: _toggleFavorite,
            isActive: _isFavorite,
          ),
          const SizedBox(width: 12),
          _buildActionButton(
            icon: Icons.share_outlined,
            label: AppLocalizations.instance.share,
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
            color: isActive ? accent : bgCard,
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: isActive ? accent : borderColor),
          ),
          child: Column(
            children: [
              Icon(icon, color: isActive ? Colors.white : textWhite, size: 22),
              const SizedBox(height: 6),
              Text(
                label,
                style: TextStyle(
                  fontSize: 12,
                  fontWeight: FontWeight.w500,
                  color: isActive ? Colors.white : textGrey,
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
          Row(
            children: [
              const Icon(Icons.info_outline, color: accentLight, size: 20),
              const SizedBox(width: 10),
              Text(
                AppLocalizations.instance.about,
                style: GoogleFonts.poppins(
                  color: textWhite,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Text(
            // Dil tercihine göre içerik seç
            (AppLocalizations.instance.isEnglish && widget.place.descriptionEn != null)
                ? widget.place.descriptionEn!
                : widget.place.description,
            style: GoogleFonts.poppins(color: textGrey, fontSize: 14, height: 1.6),
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
                  title: AppLocalizations.instance.location,
                  value: place.getLocalizedArea(AppLocalizations.instance.isEnglish).isNotEmpty 
                      ? place.getLocalizedArea(AppLocalizations.instance.isEnglish) 
                      : (place.city ?? "-"),
                  color: const Color(0xFF4CAF50),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: AnimatedBuilder(
                  animation: LocationContextService.instance,
                  builder: (context, child) {
                    // Fix for places with missing coordinates (lat/lng = 0)
                    if (place.lat == 0 && place.lng == 0) {
                       final distVal = place.distanceFromCenter;
                       final distStr = "${distVal.toStringAsFixed(1)} km";
                       final label = AppLocalizations.instance.isEnglish 
                           ? "$distStr to center" 
                           : "Merkeze $distStr";
                           
                       return _buildInfoCard(
                          icon: Icons.straighten,
                          title: AppLocalizations.instance.distance,
                          value: label,
                          color: const Color(0xFF2196F3),
                        );
                    }
                  
                    final distLabel = LocationContextService.instance.getDistanceLabel(place.lat, place.lng);
                    
                    return _buildInfoCard(
                      icon: Icons.straighten,
                      title: AppLocalizations.instance.distance,
                      value: distLabel,
                      color: const Color(0xFF2196F3),
                    );
                  }
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
                  title: AppLocalizations.instance.t(AppLocalizations.instance.price, "Price"),
                  value: _getPriceText(place.price),
                  color: const Color(0xFFFF9800),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: _buildInfoCard(
                  icon: Icons.schedule,
                  title: AppLocalizations.instance.bestTime,
                  value: (AppLocalizations.instance.isEnglish && place.bestTimeEn != null)
                      ? place.bestTimeEn!
                      : (place.bestTime ?? AppLocalizations.instance.anytime),
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
                      title: AppLocalizations.instance.t(AppLocalizations.instance.duration, "Duration"),
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
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: borderColor.withOpacity(0.5)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.1),
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: Colors.white.withOpacity(0.2)),
            ),
            child: Icon(icon, color: Colors.white.withOpacity(0.8), size: 18),
          ),
          const SizedBox(height: 8),
          Text(title, style: const TextStyle(color: textGrey, fontSize: 11)),
          const SizedBox(height: 2),
          Text(
            value,
            style: GoogleFonts.poppins(
              color: textWhite,
              fontSize: 13,
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
        return AppLocalizations.instance.free;
      case "low":
        return "€ ${AppLocalizations.instance.priceAffordable}";
      case "medium":
        return "€€ ${AppLocalizations.instance.priceMedium}";
      case "high":
        return "€€€ ${AppLocalizations.instance.priceExpensive}";
      case "luxury":
        return "€€€€ ${AppLocalizations.instance.priceLuxury}";
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
          Text(
            AppLocalizations.instance.features,
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
                  AppLocalizations.instance.translateFeature(tag),
                  style: GoogleFonts.poppins(fontSize: 13, color: textGrey),
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
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 24),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 12, sigmaY: 12),
          child: Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.05),
              borderRadius: BorderRadius.circular(20),
              border: Border.all(
                color: Colors.white.withOpacity(0.12),
                width: 1,
              ),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: accent.withOpacity(0.2),
                    shape: BoxShape.circle,
                  ),
                  child: const Icon(
                    Icons.lightbulb_outline_rounded,
                    color: Colors.white,
                    size: 22,
                  ),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        AppLocalizations.instance.localTip.replaceAll(' 💡', '').toUpperCase(),
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                          fontSize: 12,
                          fontWeight: FontWeight.w800,
                          letterSpacing: 1.2,
                        ),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        // Dil tercihine göre içerik seç
                        (AppLocalizations.instance.isEnglish && widget.place.tipsEn != null)
                            ? widget.place.tipsEn!
                            : widget.place.tips!,
                        style: GoogleFonts.poppins(
                          color: Colors.white.withOpacity(0.9),
                          fontSize: 14,
                          height: 1.6,
                          fontWeight: FontWeight.w500,
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
          Row(
            children: [
              const Icon(
                Icons.star_outline_rounded,
                color: textWhite,
                size: 20,
              ),
              const SizedBox(width: 10),
              Text(
                AppLocalizations.instance.highlightFeatures,
                style: const TextStyle(
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
                  const Icon(Icons.check_circle, color: Colors.white, size: 18),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(
                      AppLocalizations.instance.translateFeature(feature),
                      style: GoogleFonts.poppins(color: textGrey, fontSize: 14),
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
          Row(
            children: [
              Icon(Icons.access_time, color: Color(0xFF4CAF50), size: 20),
              SizedBox(width: 10),
              Text(
                "Çalışma Saatleri",
                style: GoogleFonts.poppins(
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
                    style: GoogleFonts.poppins(color: textGrey, fontSize: 14),
                  ),
                  Text(
                    entry.value,
                    style: GoogleFonts.poppins(
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
  // NEARBY PLACES BOTTOM SHEET
  // ══════════════════════════════════════════════════════════════════════════

  void _showNearbyPlacesSheet(String title, List<String> categories, Color color) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (ctx) => DraggableScrollableSheet(
        initialChildSize: 0.6,
        minChildSize: 0.4,
        maxChildSize: 0.9,
        builder: (_, scrollController) => Container(
          decoration: const BoxDecoration(
            color: bgDark, // Changed from bgCard (99) to bgDark (solid-ish)
            borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
          ),
          child: Column(
            children: [
              // Handle
              Container(
                margin: const EdgeInsets.only(top: 12),
                width: 40,
                height: 4,
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.3),
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
              // Header
              Padding(
                padding: const EdgeInsets.all(20),
                child: Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.all(10),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.1),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Icon(
                        categories.contains("Restoran") ? Icons.restaurant :
                        categories.contains("Manzara") ? Icons.camera_alt :
                        Icons.directions_walk,
                        color: Colors.white,
                        size: 24,
                      ),
                    ),
                    const SizedBox(width: 14),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            title,
                            style: GoogleFonts.poppins(
                              color: textWhite,
                              fontSize: 20,
                              fontWeight: FontWeight.w700,
                            ),
                          ),
                          Text(
                            AppLocalizations.instance.t(
                              'Mevcut konumunuza yakın yerler',
                              'Places near your current location',
                            ),
                            style: GoogleFonts.poppins(
                              color: textGrey,
                              fontSize: 13,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              const Divider(color: borderColor, height: 1),
              // Content
              Expanded(
                child: FutureBuilder<List<Highlight>>(
                  future: _loadNearbyPlaces(categories),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return const Center(
                        child: CircularProgressIndicator(color: accent),
                      );
                    }
                    
                    if (!snapshot.hasData || snapshot.data!.isEmpty) {
                      return Center(
                        child: Column(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            Icon(Icons.search_off, color: textGrey, size: 48),
                            const SizedBox(height: 12),
                            Text(
                              AppLocalizations.instance.t(
                                'Bu kategoride yakın mekan bulunamadı',
                                'No nearby places found in this category',
                              ),
                              style: TextStyle(color: textGrey),
                            ),
                          ],
                        ),
                      );
                    }
                    
                    final places = snapshot.data!;
                    return ListView.builder(
                      controller: scrollController,
                      padding: const EdgeInsets.all(16),
                      itemCount: places.length,
                      itemBuilder: (context, index) {
                        final place = places[index];
                        return _buildNearbyPlaceItem(place, color);
                      },
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future<List<Highlight>> _loadNearbyPlaces(List<String> categories) async {
    // Mevcut şehrin tüm mekanlarını yükle
    final prefs = await SharedPreferences.getInstance();
    // Use 'selectedCity' instead of 'selected_city' and ensure lowercase
    final cityId = (prefs.getString('selectedCity') ?? 'barcelona').toLowerCase();
    
    try {
      final jsonStr = await rootBundle.loadString('assets/cities/$cityId.json');
      final data = json.decode(jsonStr);
      final highlights = (data['highlights'] as List)
          .map((h) => Highlight.fromJson(h))
          .where((h) => 
            // Kategori tam eşleşmesi
            categories.any((cat) => 
              h.category.toLowerCase() == cat.toLowerCase()
            )
          )
          .take(10) // İlk 10 mekan
          .toList();
      return highlights;
    } catch (e) {
      return [];
    }
  }

  Widget _buildNearbyPlaceItem(Highlight place, Color accentColor) {
    return GestureDetector(
      onTap: () {
        Navigator.pop(context); // Bottom sheet'i kapat
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
        );
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: bgCardLight,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            // Image
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: place.imageUrl != null
                  ? Image.network(
                      place.imageUrl!,
                      width: 60,
                      height: 60,
                      fit: BoxFit.cover,
                      errorBuilder: (_, __, ___) => Container(
                        width: 60,
                        height: 60,
                        color: Colors.white.withOpacity(0.1),
                        child: const Icon(Icons.place, color: Colors.white),
                      ),
                    )
                  : Container(
                      width: 60,
                      height: 60,
                      color: Colors.white.withOpacity(0.1),
                      child: const Icon(Icons.place, color: Colors.white),
                    ),
            ),
            const SizedBox(width: 12),
            // Info
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    place.name,
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 15,
                      fontWeight: FontWeight.w600,
                    ),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),
                  Text(
                    place.area,
                    style: TextStyle(color: textGrey, fontSize: 12),
                  ),
                ],
              ),
            ),
            // Rating
            if (place.rating != null)
              Row(
                children: [
                  const Icon(
                    Icons.star_rounded,
                    color: Color(0xFFFDCB6E),
                    size: 14,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    place.rating!.toStringAsFixed(1),
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 13,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ],
              ),
          ],
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // RELATED SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildRelatedSection() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 0, 20, 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            AppLocalizations.instance.t('Öneriler', 'Suggestions'),
            style: const TextStyle(
              color: textWhite,
              fontSize: 18,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 16),
          SizedBox(
            height: 110,
            child: ListView(
              scrollDirection: Axis.horizontal,
              clipBehavior: Clip.none,
              children: [
                _buildRelatedCard(
                  AppLocalizations.instance.t('Benzer yerler', 'Similar places'),
                  null, // No IconData
                  accent,
                  [widget.place.category],
                  isAI: true,
                ),
                _buildRelatedCard(
                  AppLocalizations.instance.gastronomy,
                  Icons.restaurant_rounded,
                  const Color(0xFFFF5252),
                  ["Restoran", "Kafe", "Bar"],
                ),
                _buildRelatedCard(
                  AppLocalizations.instance.shopping,
                  Icons.shopping_bag_outlined,
                  const Color(0xFFE91E63),
                  ["Alışveriş"],
                ),
                _buildRelatedCard(
                  AppLocalizations.instance.experience,
                  Icons.explore_outlined,
                  const Color(0xFF2196F3),
                  ["Deneyim", "Müze"],
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildRelatedCard(String title, IconData? icon, Color color, List<String> categories, {bool isAI = false}) {
    return GestureDetector(
      onTap: () {
        // Yakındaki mekanları kategoriye göre filtrele ve bottom sheet'te göster
        _showNearbyPlacesSheet(title, categories, color);
      },
      child: Container(
        width: 110,
        margin: const EdgeInsets.only(right: 12),
        decoration: BoxDecoration(
          color: Colors.white.withOpacity(0.04),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(color: Colors.white.withOpacity(0.1), width: 1),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            isAI
                ? Image.asset(
                    'assets/images/splash_logo.png',
                    width: 24,
                    height: 24,
                    fit: BoxFit.contain,
                  )
                : Icon(icon, color: Colors.white.withOpacity(0.9), size: 24),
            const SizedBox(height: 10),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 8),
              child: Text(
                title,
                style: const TextStyle(
                  color: textWhite,
                  fontSize: 11,
                  fontWeight: FontWeight.w500,
                ),
                textAlign: TextAlign.center,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
            ),
          ],
        ),
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
        child: Row(
          children: [
            // Check-in Button
            Expanded(
              flex: 1,
              child: GestureDetector(
                onTap: _isVisited ? null : _checkIn,
                child: AnimatedContainer(
                  key: _checkInKey, // Key for Tutorial
                  duration: const Duration(milliseconds: 250),
                  height: 58,
                  margin: const EdgeInsets.only(right: 8),
                  decoration: BoxDecoration(
                    color: _isVisited 
                        ? accent
                        : _isCheckingIn 
                            ? bgCardLight
                            : bgCard,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: _isVisited ? accent : accent.withOpacity(0.5),
                    ),
                  ),
                  child: Center(
                    child: _isCheckingIn
                        ? const SizedBox(
                            width: 24,
                            height: 24,
                            child: CircularProgressIndicator(
                              color: accent,
                              strokeWidth: 2.5,
                            ),
                          )
                        : Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(
                                Icons.location_on,
                                color: _isVisited ? Colors.white : accent,
                                size: 22,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                _isVisited ? AppLocalizations.instance.t("Ziyaret", "Visited") : AppLocalizations.instance.imHere,
                                style: TextStyle(
                                  color: _isVisited ? Colors.white : textWhite,
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                            ],
                          ),
                  ),
                ),
              ),
            ),
            // Trip Button
            Expanded(
              flex: 1,
              child: GestureDetector(
                onTap: _toggleTrip,
                child: AnimatedContainer(
                  key: _addToRouteKey, // Key Assigned
                  duration: const Duration(milliseconds: 250),
                  height: 58,
                  decoration: BoxDecoration(
                    color: accent,
                    borderRadius: BorderRadius.circular(16),
                    border: _isInTrip ? Border.all(color: accent) : null,
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        _isInTrip ? Icons.check : Icons.add_location_alt_outlined,
                        color: Colors.white,
                        size: 22,
                      ),
                      const SizedBox(width: 6),
                      Text(
                        _isInTrip ? AppLocalizations.instance.addedToRoute : AppLocalizations.instance.addToRoute,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 14,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
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
      'Deneyim': const Color(0xFF673AB7),
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
      'Deneyim': Icons.explore,
    };
    return icons[category] ?? Icons.place;
  }
  
  // ══════════════════════════════════════════════════════════════════════════
  // TUTORIAL
  // ══════════════════════════════════════════════════════════════════════════

  void _showRouteTutorial() async {
      if (!mounted) return;
      final String tutorialKey = TutorialService.KEY_TUTORIAL_ADD_TO_ROUTE;
      final shouldShow = await TutorialService.instance.shouldShowTutorial(tutorialKey);
      if (!shouldShow) return;

      if (_addToRouteKey.currentContext == null || _checkInKey.currentContext == null) {
        return;
      }

      late TutorialCoachMark tutorial;
      final stepNotifier = ValueNotifier<int>(0);

      tutorial = TutorialCoachMark(
        targets: [
          // Step 1: Add to Route
          TargetFocus(
            identify: "add_route_detail",
            keyTarget: _addToRouteKey,
            color: Colors.black,
            contents: [
              TargetContent(
                align: ContentAlign.top,
                builder: (context, controller) {
                    stepNotifier.value = 0;
                    return TutorialOverlayWidget(
                    title: AppLocalizations.instance.isEnglish ? "Add to Route" : "Rotaya Ekle",
                    description: AppLocalizations.instance.isEnglish 
                        ? "Add this place to your travel route and plan your day." 
                        : "Bu mekanı seyahat rotana ekle ve gününü planla.",
                    currentStep: 1,
                    totalSteps: 2,
                    onSkip: () => controller.next(), 
                    onNext: () => controller.next(),
                    isArrowUp: false, 
                    isArrowFlipped: false, // Target is on the right
                   );
                },
              ),
            ],
            shape: ShapeLightFocus.RRect,
            radius: 16,
            paddingFocus: 0,
          ),
          // Step 2: I'm Here
          TargetFocus(
            identify: "check_in_detail",
            keyTarget: _checkInKey,
            color: Colors.black,
            contents: [
              TargetContent(
                align: ContentAlign.top,
                builder: (context, controller) {
                    stepNotifier.value = 1;
                    return TutorialOverlayWidget(
                    title: AppLocalizations.instance.isEnglish ? "I'm Here" : "Buradayım",
                    description: AppLocalizations.instance.isEnglish 
                        ? "Mark the places you visit to keep track of your journey and earn badges." 
                        : "Ziyaret ettiğin yerleri işaretleyerek yolculuğunu takip et ve rozetler kazan.",
                    currentStep: 2,
                    totalSteps: 2,
                    onSkip: () => controller.skip(),
                    isArrowUp: false,
                    isArrowFlipped: true, // Target is on the left
                   );
                },
              ),
            ],
            shape: ShapeLightFocus.RRect,
            radius: 16,
            paddingFocus: 0,
          ),
        ],
        colorShadow: Colors.black, 
        opacityShadow: 0.85, 
        textSkip: "", 
        skipWidget: ValueListenableBuilder<int>(
          valueListenable: stepNotifier,
          builder: (context, value, child) {
            return _buildSkipWidget(tutorial, value);
          },
        ),
        onFinish: () {
           TutorialService.instance.markTutorialSeen(tutorialKey);
           stepNotifier.dispose();
        },
        onSkip: () {
           TutorialService.instance.skipAllTutorials();
           stepNotifier.dispose();
           return true; 
        },
        // Universal click logic: Step 1 -> Next, Step 2 -> Skip
        onClickTarget: (target) {
          tutorial.next();
        },
        onClickOverlay: (target) {
          tutorial.next();
        },
      );
      
      tutorial.show(context: context);
  }

  Widget _buildSkipWidget(TutorialCoachMark tutorial, int stepIndex) {
    return GestureDetector(
      onTap: () {
        if (stepIndex == 0) {
          tutorial.next();
        } else {
          tutorial.skip();
        }
      },
      child: SafeArea(
        child: Align(
          alignment: Alignment.topRight,
          child: Padding(
            padding: const EdgeInsets.only(top: 20, right: 20),
            child: Container(
               padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
               decoration: BoxDecoration(
                 color: Colors.white24,
                 borderRadius: BorderRadius.circular(20),
               ),
               child: Text(
                 AppLocalizations.instance.isEnglish ? "Skip" : "Atla",
                 style: const TextStyle(
                   color: Colors.white,
                   fontWeight: FontWeight.bold,
                   fontSize: 14,
                 ),
               ),
            ),
          ),
        ),
      ),
    );
  }
}
