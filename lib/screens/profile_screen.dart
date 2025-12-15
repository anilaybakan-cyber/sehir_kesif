// =============================================================================
// PROFILE SCREEN – WANDERLUST DARK THEME
// User profile with stats, favorites, visited places, and settings
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:ui';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import 'detail_screen.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen>
    with SingleTickerProviderStateMixin {
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

  String _userName = "Gezgin";
  String _travelStyle = "Lokal";
  List<String> _interests = [];
  List<String> _favorites = [];
  List<String> _visitedPlaces = [];
  List<String> _tripPlaces = [];
  List<Highlight> _favoriteHighlights = [];

  int _selectedTab = 0; // 0: Favoriler, 1: Ziyaret Edilenler

  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 2, vsync: this);
    _loadData();
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  // ══════════════════════════════════════════════════════════════════════════
  // DATA LOADING
  // ══════════════════════════════════════════════════════════════════════════

  Future<void> _loadData() async {
    final prefs = await SharedPreferences.getInstance();

    _userName = prefs.getString("user_name") ?? "Gezgin";
    _travelStyle = prefs.getString("travelStyle") ?? "Lokal";
    _interests = prefs.getStringList("interests") ?? [];
    _favorites = prefs.getStringList("favorite_places") ?? [];
    _visitedPlaces = prefs.getStringList("visited_places") ?? [];
    _tripPlaces = prefs.getStringList("trip_places") ?? [];

    // Favori mekanları yükle
    final selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    try {
      final city = await CityDataLoader.loadCity(selectedCity.toLowerCase());
      _favoriteHighlights = city.highlights
          .where((h) => _favorites.contains(h.name))
          .toList();
    } catch (e) {
      _favoriteHighlights = [];
    }

    if (!mounted) return;
    setState(() {});
  }

  Future<void> _editName() async {
    final controller = TextEditingController(text: _userName);

    final result = await showDialog<String>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: bgCard,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text("İsim Değiştir", style: TextStyle(color: textWhite)),
        content: TextField(
          controller: controller,
          style: const TextStyle(color: textWhite),
          decoration: InputDecoration(
            hintText: "İsminizi girin",
            hintStyle: TextStyle(color: textGrey),
            filled: true,
            fillColor: bgCardLight,
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(12),
              borderSide: BorderSide.none,
            ),
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: Text("İptal", style: TextStyle(color: textGrey)),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, controller.text),
            child: const Text("Kaydet", style: TextStyle(color: accent)),
          ),
        ],
      ),
    );

    if (result != null && result.isNotEmpty) {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString("user_name", result);
      setState(() => _userName = result);
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // BUILD
  // ══════════════════════════════════════════════════════════════════════════

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: bgDark,
      body: CustomScrollView(
        physics: const BouncingScrollPhysics(),
        slivers: [
          // Profile Header
          SliverToBoxAdapter(child: _buildProfileHeader()),

          // Stats Cards
          SliverToBoxAdapter(child: _buildStatsCards()),

          // Travel Style Card
          SliverToBoxAdapter(child: _buildTravelStyleCard()),

          // Interests
          SliverToBoxAdapter(child: _buildInterestsSection()),

          // Tab Bar
          SliverToBoxAdapter(child: _buildTabBar()),

          // Tab Content
          SliverToBoxAdapter(
            child: SizedBox(
              height: 400,
              child: TabBarView(
                controller: _tabController,
                children: [_buildFavoritesList(), _buildVisitedList()],
              ),
            ),
          ),

          // Settings Section
          SliverToBoxAdapter(child: _buildSettingsSection()),

          // Bottom padding
          const SliverToBoxAdapter(child: SizedBox(height: 100)),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // PROFILE HEADER
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildProfileHeader() {
    return Container(
      padding: EdgeInsets.fromLTRB(
        20,
        MediaQuery.of(context).padding.top + 20,
        20,
        20,
      ),
      child: Row(
        children: [
          // Avatar
          GestureDetector(
            onTap: _editName,
            child: Container(
              width: 80,
              height: 80,
              decoration: BoxDecoration(
                gradient: primaryGradient,
                shape: BoxShape.circle,
                boxShadow: [
                  BoxShadow(
                    color: accentLight.withOpacity(0.4),
                    blurRadius: 20,
                    offset: const Offset(0, 8),
                  ),
                ],
              ),
              child: Center(
                child: Text(
                  _userName.isNotEmpty ? _userName[0].toUpperCase() : "G",
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 32,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ),
            ),
          ),
          const SizedBox(width: 20),
          // Name and info
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      _userName,
                      style: const TextStyle(
                        color: textWhite,
                        fontSize: 24,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                    const SizedBox(width: 8),
                    GestureDetector(
                      onTap: _editName,
                      child: const Icon(Icons.edit, color: textGrey, size: 18),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Row(
                  children: [
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 4,
                      ),
                      decoration: BoxDecoration(
                        color: accent.withOpacity(0.15),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(Icons.star, color: accent, size: 14),
                          const SizedBox(width: 4),
                          Text(
                            _getTravelerLevel(),
                            style: TextStyle(
                              color: accent,
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
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
          // Settings button
          GestureDetector(
            onTap: () => Navigator.pushNamed(context, "/settings"),
            child: Container(
              padding: const EdgeInsets.all(12),
              decoration: BoxDecoration(
                color: bgCard,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: borderColor),
              ),
              child: const Icon(Icons.settings, color: textWhite, size: 22),
            ),
          ),
        ],
      ),
    );
  }

  String _getTravelerLevel() {
    final total = _favorites.length + _visitedPlaces.length;
    if (total >= 50) return "Uzman Gezgin";
    if (total >= 30) return "Deneyimli";
    if (total >= 15) return "Kaşif";
    if (total >= 5) return "Meraklı";
    return "Yeni Başlayan";
  }

  // ══════════════════════════════════════════════════════════════════════════
  // STATS CARDS
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildStatsCards() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 20),
      child: Row(
        children: [
          _buildStatCard(
            icon: Icons.favorite,
            value: "${_favorites.length}",
            label: "Favori",
            color: accent,
          ),
          const SizedBox(width: 12),
          _buildStatCard(
            icon: Icons.check_circle,
            value: "${_visitedPlaces.length}",
            label: "Ziyaret",
            color: Colors.green,
          ),
          const SizedBox(width: 12),
          _buildStatCard(
            icon: Icons.map,
            value: "${_tripPlaces.length}",
            label: "Rotada",
            color: accentLight,
          ),
        ],
      ),
    );
  }

  Widget _buildStatCard({
    required IconData icon,
    required String value,
    required String label,
    required Color color,
  }) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Column(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: color.withOpacity(0.15),
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: color, size: 22),
            ),
            const SizedBox(height: 10),
            Text(
              value,
              style: const TextStyle(
                color: textWhite,
                fontSize: 22,
                fontWeight: FontWeight.w700,
              ),
            ),
            Text(label, style: TextStyle(color: textGrey, fontSize: 12)),
          ],
        ),
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TRAVEL STYLE CARD
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTravelStyleCard() {
    final styleInfo = _getStyleInfo(_travelStyle);

    return Container(
      margin: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            styleInfo['color'].withOpacity(0.2),
            styleInfo['color'].withOpacity(0.05),
          ],
        ),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: styleInfo['color'].withOpacity(0.3)),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: styleInfo['color'].withOpacity(0.2),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(styleInfo['icon'], color: styleInfo['color'], size: 28),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "Seyahat Tarzı",
                  style: TextStyle(color: textGrey, fontSize: 12),
                ),
                const SizedBox(height: 4),
                Text(
                  _travelStyle,
                  style: const TextStyle(
                    color: textWhite,
                    fontSize: 18,
                    fontWeight: FontWeight.w700,
                  ),
                ),
              ],
            ),
          ),
          GestureDetector(
            onTap: () => Navigator.pushNamed(context, "/onboarding"),
            child: Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: bgCardLight,
                borderRadius: BorderRadius.circular(10),
              ),
              child: const Icon(Icons.edit, color: textGrey, size: 18),
            ),
          ),
        ],
      ),
    );
  }

  Map<String, dynamic> _getStyleInfo(String style) {
    switch (style) {
      case "Turist":
        return {'icon': Icons.camera_alt, 'color': const Color(0xFF2196F3)};
      case "Lokal":
        return {'icon': Icons.explore, 'color': const Color(0xFF4CAF50)};
      case "Macera":
        return {'icon': Icons.hiking, 'color': const Color(0xFFFF9800)};
      case "Lüks":
        return {'icon': Icons.diamond, 'color': const Color(0xFF9C27B0)};
      default:
        return {'icon': Icons.travel_explore, 'color': accentLight};
    }
  }

  // ══════════════════════════════════════════════════════════════════════════
  // INTERESTS SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildInterestsSection() {
    if (_interests.isEmpty) return const SizedBox.shrink();

    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 20, 20, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "İlgi Alanları",
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
            children: _interests.map((interest) {
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
                  interest,
                  style: TextStyle(color: textGrey, fontSize: 13),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // TAB BAR
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildTabBar() {
    return Container(
      margin: const EdgeInsets.fromLTRB(20, 24, 20, 0),
      decoration: BoxDecoration(
        color: bgCard,
        borderRadius: BorderRadius.circular(14),
      ),
      child: TabBar(
        controller: _tabController,
        indicator: BoxDecoration(
          gradient: primaryGradient,
          borderRadius: BorderRadius.circular(12),
        ),
        indicatorSize: TabBarIndicatorSize.tab,
        indicatorPadding: const EdgeInsets.all(4),
        dividerColor: Colors.transparent,
        labelColor: Colors.white,
        unselectedLabelColor: textGrey,
        labelStyle: const TextStyle(fontWeight: FontWeight.w600, fontSize: 14),
        tabs: [
          Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.favorite, size: 18),
                const SizedBox(width: 8),
                Text("Favoriler (${_favorites.length})"),
              ],
            ),
          ),
          Tab(
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.check_circle, size: 18),
                const SizedBox(width: 8),
                Text("Ziyaret (${_visitedPlaces.length})"),
              ],
            ),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // FAVORITES LIST
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildFavoritesList() {
    if (_favoriteHighlights.isEmpty) {
      return _buildEmptyTab(
        icon: Icons.favorite_border,
        title: "Henüz favori yok",
        subtitle: "Beğendiğin yerleri favorilere ekle",
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      itemCount: _favoriteHighlights.length,
      itemBuilder: (context, index) {
        return _buildMiniPlaceCard(_favoriteHighlights[index]);
      },
    );
  }

  Widget _buildVisitedList() {
    if (_visitedPlaces.isEmpty) {
      return _buildEmptyTab(
        icon: Icons.check_circle_outline,
        title: "Henüz ziyaret yok",
        subtitle: "Gittiğin yerleri işaretle",
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
      itemCount: _visitedPlaces.length,
      itemBuilder: (context, index) {
        return Container(
          margin: const EdgeInsets.only(bottom: 10),
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: bgCard,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: borderColor.withOpacity(0.5)),
          ),
          child: Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: Colors.green.withOpacity(0.15),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Icon(Icons.check, color: Colors.green, size: 18),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Text(
                  _visitedPlaces[index],
                  style: const TextStyle(color: textWhite, fontSize: 14),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  Widget _buildMiniPlaceCard(Highlight place) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;
    final color = _getCategoryColor(place.category);

    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
      ),
      child: Container(
        margin: const EdgeInsets.only(bottom: 12),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            // Image
            ClipRRect(
              borderRadius: BorderRadius.circular(10),
              child: SizedBox(
                width: 56,
                height: 56,
                child: hasImage
                    ? Image.network(place.imageUrl!, fit: BoxFit.cover)
                    : Container(
                        color: color.withOpacity(0.15),
                        child: Icon(Icons.place, color: color, size: 24),
                      ),
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
                      fontSize: 14,
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
                  const Icon(Icons.star, color: Color(0xFFFFC107), size: 14),
                  const SizedBox(width: 4),
                  Text(
                    place.rating!.toStringAsFixed(1),
                    style: const TextStyle(
                      color: textWhite,
                      fontSize: 12,
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

  Widget _buildEmptyTab({
    required IconData icon,
    required String title,
    required String subtitle,
  }) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(icon, size: 48, color: textGrey.withOpacity(0.5)),
          const SizedBox(height: 16),
          Text(
            title,
            style: TextStyle(
              color: textGrey,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            subtitle,
            style: TextStyle(color: textGrey.withOpacity(0.7), fontSize: 13),
          ),
        ],
      ),
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // SETTINGS SECTION
  // ══════════════════════════════════════════════════════════════════════════

  Widget _buildSettingsSection() {
    return Padding(
      padding: const EdgeInsets.fromLTRB(20, 24, 20, 0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Hızlı Erişim",
            style: TextStyle(
              color: textWhite,
              fontSize: 16,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 12),
          _buildSettingItem(
            icon: Icons.location_city,
            title: "Şehir Değiştir",
            onTap: () => Navigator.pushNamed(context, "/city-switch"),
          ),
          _buildSettingItem(
            icon: Icons.palette,
            title: "Tercihlerimi Düzenle",
            onTap: () => Navigator.pushNamed(context, "/onboarding"),
          ),
          _buildSettingItem(
            icon: Icons.settings,
            title: "Ayarlar",
            onTap: () => Navigator.pushNamed(context, "/settings"),
          ),
          _buildSettingItem(
            icon: Icons.info_outline,
            title: "Hakkında",
            onTap: () {},
          ),
        ],
      ),
    );
  }

  Widget _buildSettingItem({
    required IconData icon,
    required String title,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        onTap();
      },
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(color: borderColor.withOpacity(0.5)),
        ),
        child: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(10),
              decoration: BoxDecoration(
                color: bgCardLight,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, color: textGrey, size: 20),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Text(
                title,
                style: const TextStyle(
                  color: textWhite,
                  fontSize: 15,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ),
            const Icon(Icons.chevron_right, color: textGrey, size: 22),
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
      'Semt': const Color(0xFF673AB7),
    };
    return colors[category] ?? const Color(0xFF607D8B);
  }
}
