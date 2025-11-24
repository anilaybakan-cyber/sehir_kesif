// Dosya: lib/screens/explore_screen.dart

import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:shimmer/shimmer.dart';

import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import '../services/ai_service.dart';
import '../services/user_preferences.dart';
import 'detail_screen.dart';

class ExploreScreen extends StatefulWidget {
  const ExploreScreen({super.key});

  @override
  State<ExploreScreen> createState() => _ExploreScreenState();
}

class _ExploreScreenState extends State<ExploreScreen> {
  CityModel? _city;
  bool _loading = true;

  // AI ve Mood Durumları
  bool _aiLoading = false;
  List<Highlight> _aiRecommendations = [];
  double _moodValue = 0.5;

  // Kullanıcı Verileri
  Map<String, dynamic> _userProfile = {};
  List<String> favoriteList = [];

  // 🎯 Kişiselleştirilmiş öneriler
  List<Highlight> _personalizedPlaces = [];

  @override
  void initState() {
    super.initState();
    _loadAll();
  }

  Future<void> _loadAll() async {
    setState(() => _loading = true);
    final prefs = await SharedPreferences.getInstance();

    _userProfile = await UserPreferences.getUserProfile();
    favoriteList = prefs.getStringList("favorite_places") ?? [];

    String selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    _city = await CityDataLoader.loadCity(selectedCity.toLowerCase());

    // 🎯 Kişiselleştirilmiş yerler
    _personalizedPlaces = _getPersonalizedPlaces();

    setState(() => _loading = false);
    _fetchAIRecommendations();
  }

  // 🎯 Kişiselleştirilmiş yerler
  List<Highlight> _getPersonalizedPlaces() {
    if (_city == null) return [];

    final travelStyle = _userProfile['travelStyle'] as String? ?? 'Turistik';
    final walkingLevel = _userProfile['walkingLevel'] as int? ?? 1;
    final budgetLevel = _userProfile['budgetLevel'] as String? ?? 'Dengeli';
    final interests = _userProfile['interests'] as List<String>? ?? [];

    final maxDistance = UserPreferences.getMaxDistanceForWalkingLevel(
      walkingLevel,
    );
    final allowedBudgets = UserPreferences.getAllowedPricesForBudget(
      budgetLevel,
    );
    final preferredCategories = UserPreferences.getCategoriesForTravelStyle(
      travelStyle,
    );

    List<MapEntry<Highlight, int>> scoredPlaces = [];

    for (var place in _city!.highlights) {
      int score = 0;

      if (place.distanceFromCenter <= maxDistance) score += 10;
      if (allowedBudgets.contains(place.price)) {
        score += 15;
      } else {
        score += 5;
      }

      if (preferredCategories.any(
        (pref) => pref.toLowerCase() == place.category.toLowerCase(),
      )) {
        score += 20;
      }

      for (var interest in interests) {
        if (place.tags.any(
          (tag) => tag.toLowerCase().contains(interest.toLowerCase()),
        )) {
          score += 15;
        }
        if (place.name.toLowerCase().contains(interest.toLowerCase())) {
          score += 10;
        }
      }

      scoredPlaces.add(MapEntry(place, score));
    }

    scoredPlaces.sort((a, b) => b.value.compareTo(a.value));
    return scoredPlaces.take(10).map((e) => e.key).toList();
  }

  Future<void> _fetchAIRecommendations() async {
    if (_city == null) return;

    setState(() => _aiLoading = true);

    final travelStyle = _userProfile['travelStyle'] as String? ?? 'Lokal';
    final interests = _userProfile['interests'] as List<String>? ?? [];

    final recs = await AIService.getSerendipityRecommendations(
      city: _city!.city,
      travelStyle: travelStyle,
      interests: interests,
      moodLevel: _moodValue,
    );

    if (mounted) {
      setState(() {
        _aiRecommendations = recs;
        _aiLoading = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_loading || _city == null) {
      return Scaffold(
        backgroundColor: Colors.white,
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              CircularProgressIndicator(color: Colors.teal),
              SizedBox(height: 16),
              Text(
                "Şehir yükleniyor...",
                style: TextStyle(color: Colors.grey.shade600, fontSize: 15),
              ),
            ],
          ),
        ),
      );
    }

    return Scaffold(
      backgroundColor: Colors.white,
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.white, Colors.grey.shade50],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SafeArea(
          child: RefreshIndicator(
            onRefresh: _loadAll,
            color: Colors.teal,
            child: ListView(
              padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
              children: [
                // 🏙️ Üst Başlık
                _buildHeader(),

                const SizedBox(height: 24),

                // 👤 Profil Özeti
                _buildProfileSummary(),

                const SizedBox(height: 24),

                // 🎭 Mood Slider
                _buildMoodSlider(),

                const SizedBox(height: 28),

                // 🎯 SANA ÖZEL ÖNERİLER (YENİ!)
                _buildPersonalizedSection(),

                const SizedBox(height: 32),

                // 🤖 AI Önerileri
                _buildAISection(),

                const SizedBox(height: 32),

                // 📍 Kategoriler
                _section("Popüler Duraklar", "turistik", Icons.star_rounded),
                _section("Lokal Lezzetler", "lokal", Icons.restaurant_rounded),
                _section(
                  "Instagramlık Noktalar",
                  "instagramlik",
                  Icons.camera_alt_rounded,
                ),
                _section("Chill & Beach", "chill", Icons.beach_access_rounded),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // 🏙️ HEADER
  Widget _buildHeader() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              "Keşfet",
              style: TextStyle(
                fontSize: 34,
                fontWeight: FontWeight.bold,
                color: Colors.black87,
                letterSpacing: -0.5,
              ),
            ),
            const SizedBox(height: 4),
            Row(
              children: [
                Icon(Icons.location_on, size: 16, color: Colors.teal),
                SizedBox(width: 4),
                Text(
                  _city!.city,
                  style: TextStyle(
                    fontSize: 16,
                    color: Colors.grey.shade600,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ],
        ),
        Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(12),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.06),
                blurRadius: 10,
                offset: Offset(0, 2),
              ),
            ],
          ),
          child: IconButton(
            icon: Icon(Icons.tune_rounded, color: Colors.teal),
            onPressed: () => Navigator.pushNamed(context, "/city-switch"),
          ),
        ),
      ],
    );
  }

  // 👤 Profil Özeti
  Widget _buildProfileSummary() {
    final travelStyle = _userProfile['travelStyle'] as String? ?? 'Turistik';
    final interests = _userProfile['interests'] as List<String>? ?? [];

    return Container(
      padding: EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.teal.shade100, width: 1.5),
        boxShadow: [
          BoxShadow(
            color: Colors.teal.withOpacity(0.08),
            blurRadius: 20,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: EdgeInsets.all(12),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [Colors.teal.shade400, Colors.teal.shade600],
              ),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(Icons.person_rounded, color: Colors.white, size: 26),
          ),
          SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Gezme Tarzın: $travelStyle",
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w700,
                    color: Colors.black87,
                  ),
                ),
                if (interests.isNotEmpty) ...[
                  SizedBox(height: 4),
                  Text(
                    "İlgi: ${interests.take(3).join(', ')}",
                    style: TextStyle(fontSize: 13, color: Colors.grey.shade600),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }

  // 🎭 MOOD SLIDER
  Widget _buildMoodSlider() {
    return Container(
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 20,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                "Bugün nasıl hissediyorsun?",
                style: TextStyle(
                  fontWeight: FontWeight.w600,
                  fontSize: 16,
                  color: Colors.black87,
                ),
              ),
              Container(
                padding: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                decoration: BoxDecoration(
                  color: Colors.teal.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(20),
                ),
                child: Text(
                  _moodValue < 0.3
                      ? "☕️ Chill"
                      : _moodValue < 0.7
                      ? "😊 Normal"
                      : "⚡️ Enerjik",
                  style: TextStyle(
                    fontSize: 13,
                    color: Colors.teal.shade700,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          SliderTheme(
            data: SliderThemeData(
              activeTrackColor: Colors.teal,
              inactiveTrackColor: Colors.grey.shade200,
              thumbColor: Colors.teal,
              overlayColor: Colors.teal.withOpacity(0.2),
              trackHeight: 6,
              thumbShape: RoundSliderThumbShape(enabledThumbRadius: 10),
            ),
            child: Slider(
              value: _moodValue,
              onChanged: (val) => setState(() => _moodValue = val),
              onChangeEnd: (val) => _fetchAIRecommendations(),
            ),
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                "☕️ Sakin",
                style: TextStyle(fontSize: 12, color: Colors.grey),
              ),
              Text(
                "⚡️ Enerjik",
                style: TextStyle(fontSize: 12, color: Colors.grey),
              ),
            ],
          ),
        ],
      ),
    );
  }

  // 🎯 SANA ÖZEL ÖNERİLER BÖLÜMÜ
  Widget _buildPersonalizedSection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Container(
              padding: EdgeInsets.all(8),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: [Colors.amber.shade400, Colors.orange.shade500],
                ),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(Icons.stars_rounded, size: 20, color: Colors.white),
            ),
            SizedBox(width: 12),
            Text(
              "Sana Özel Öneriler",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Colors.black87,
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),
        _personalizedPlaces.isEmpty
            ? Container(
                padding: EdgeInsets.all(20),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Center(
                  child: Text(
                    "Sana özel yer bulunamadı 😔",
                    style: TextStyle(color: Colors.grey.shade600),
                  ),
                ),
              )
            : SizedBox(
                height: 300,
                child: ListView.separated(
                  scrollDirection: Axis.horizontal,
                  itemCount: _personalizedPlaces.length,
                  separatorBuilder: (_, __) => const SizedBox(width: 16),
                  itemBuilder: (_, i) =>
                      _personalizedCard(_personalizedPlaces[i], i),
                ),
              ),
      ],
    );
  }

  // 🎯 Kişiselleştirilmiş Kart
  Widget _personalizedCard(Highlight place, int index) {
    String imageUrl = place.imageUrl ?? place.displayImage ?? '';

    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
      ),
      child: Container(
        width: 260,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(24),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.08),
              blurRadius: 20,
              offset: Offset(0, 8),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Stack(
              children: [
                ClipRRect(
                  borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
                  child: (imageUrl != null && imageUrl.isNotEmpty)
                      ? CachedNetworkImage(
                          imageUrl: imageUrl,
                          height: 160,
                          width: double.infinity,
                          fit: BoxFit.cover,
                          placeholder: (context, url) => Shimmer.fromColors(
                            baseColor: Colors.grey.shade200,
                            highlightColor: Colors.grey.shade50,
                            child: Container(color: Colors.white),
                          ),
                          errorWidget: (context, url, error) => Container(
                            color: Colors.grey.shade100,
                            child: Icon(
                              Icons.place,
                              color: Colors.teal.shade200,
                              size: 50,
                            ),
                          ),
                        )
                      : Container(
                          height: 160,
                          color: Colors.grey.shade100,
                          child: Icon(
                            Icons.place,
                            color: Colors.teal.shade200,
                            size: 50,
                          ),
                        ),
                ),
                if (index < 3)
                  Positioned(
                    top: 12,
                    left: 12,
                    child: Container(
                      padding: EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: index == 0
                              ? [Colors.amber.shade400, Colors.orange.shade500]
                              : [Colors.teal.shade400, Colors.teal.shade600],
                        ),
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: (index == 0 ? Colors.amber : Colors.teal)
                                .withOpacity(0.4),
                            blurRadius: 8,
                            offset: Offset(0, 2),
                          ),
                        ],
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            index == 0
                                ? Icons.star_rounded
                                : Icons.recommend_rounded,
                            size: 12,
                            color: Colors.white,
                          ),
                          SizedBox(width: 4),
                          Text(
                            index == 0 ? "En Uygun" : "#${index + 1}",
                            style: TextStyle(
                              fontSize: 11,
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    place.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.black87,
                    ),
                  ),
                  SizedBox(height: 6),
                  Row(
                    children: [
                      Icon(
                        Icons.location_on,
                        size: 14,
                        color: Colors.grey.shade400,
                      ),
                      SizedBox(width: 4),
                      Expanded(
                        child: Text(
                          place.area,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 13,
                            color: Colors.grey.shade600,
                          ),
                        ),
                      ),
                    ],
                  ),
                  SizedBox(height: 10),
                  Wrap(
                    spacing: 6,
                    runSpacing: 4,
                    children: place.tags.take(2).map((tag) {
                      return Container(
                        padding: EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 4,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.teal.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          tag,
                          style: TextStyle(
                            fontSize: 11,
                            color: Colors.teal.shade700,
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      );
                    }).toList(),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // 🤖 AI ÖNERİLERİ
  Widget _buildAISection() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Container(
              padding: EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: Colors.teal.withOpacity(0.1),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(Icons.auto_awesome, size: 20, color: Colors.teal),
            ),
            SizedBox(width: 12),
            Text(
              "Senin İçin Seçtiklerim",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Colors.black87,
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),
        _aiLoading
            ? _buildAILoading()
            : _aiRecommendations.isEmpty
            ? _buildAIEmpty()
            : _buildAICards(),
      ],
    );
  }

  Widget _buildAILoading() {
    return SizedBox(
      height: 280,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        itemCount: 3,
        separatorBuilder: (_, __) => const SizedBox(width: 16),
        itemBuilder: (_, i) => _shimmerCard(),
      ),
    );
  }

  Widget _buildAIEmpty() {
    return Container(
      height: 120,
      alignment: Alignment.center,
      child: Text(
        "AI önerileri yükleniyor...",
        style: TextStyle(color: Colors.grey.shade500),
      ),
    );
  }

  Widget _buildAICards() {
    return SizedBox(
      height: 320,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        itemCount: _aiRecommendations.length,
        separatorBuilder: (_, __) => const SizedBox(width: 16),
        itemBuilder: (_, i) => _aiCard(_aiRecommendations[i]),
      ),
    );
  }

  Widget _aiCard(Highlight h) {
    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: h)),
      ),
      child: Container(
        width: 260,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(24),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.08),
              blurRadius: 20,
              offset: Offset(0, 8),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Stack(
              children: [
                ClipRRect(
                  borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
                  child: CachedNetworkImage(
                    imageUrl: h.displayImage,
                    height: 180,
                    width: double.infinity,
                    fit: BoxFit.cover,
                    placeholder: (context, url) => Shimmer.fromColors(
                      baseColor: Colors.grey.shade200,
                      highlightColor: Colors.grey.shade50,
                      child: Container(color: Colors.white),
                    ),
                    errorWidget: (context, url, error) => Container(
                      color: Colors.grey.shade100,
                      child: Icon(Icons.image_not_supported, size: 50),
                    ),
                  ),
                ),
                Positioned(
                  top: 12,
                  left: 12,
                  child: Container(
                    padding: EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                    decoration: BoxDecoration(
                      color: Colors.teal,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.teal.withOpacity(0.4),
                          blurRadius: 8,
                          offset: Offset(0, 2),
                        ),
                      ],
                    ),
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.auto_awesome, size: 12, color: Colors.white),
                        SizedBox(width: 4),
                        Text(
                          "AI Önerisi",
                          style: TextStyle(
                            fontSize: 11,
                            color: Colors.white,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
            Padding(
              padding: const EdgeInsets.all(16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    h.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                      color: Colors.black87,
                    ),
                  ),
                  SizedBox(height: 6),
                  Text(
                    h.description,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 13,
                      color: Colors.grey.shade600,
                      height: 1.4,
                    ),
                  ),
                  SizedBox(height: 12),
                  Row(
                    children: [
                      Icon(
                        Icons.location_on,
                        size: 14,
                        color: Colors.grey.shade400,
                      ),
                      SizedBox(width: 4),
                      Text(
                        h.area,
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey.shade600,
                        ),
                      ),
                      Spacer(),
                      Container(
                        padding: EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 4,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.grey.shade100,
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          "${h.distanceFromCenter.toStringAsFixed(1)} km",
                          style: TextStyle(
                            fontSize: 11,
                            color: Colors.teal.shade700,
                            fontWeight: FontWeight.w600,
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
      ),
    );
  }

  Widget _section(String title, String category, IconData icon) {
    final items = _city!.highlights
        .where((h) => h.category == category)
        .toList();
    if (items.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          children: [
            Container(
              padding: EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: _getCategoryColor(category).withOpacity(0.1),
                borderRadius: BorderRadius.circular(10),
              ),
              child: Icon(icon, size: 20, color: _getCategoryColor(category)),
            ),
            SizedBox(width: 12),
            Text(
              title,
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
                color: Colors.black87,
              ),
            ),
          ],
        ),
        const SizedBox(height: 16),
        SizedBox(
          height: 240,
          child: ListView.separated(
            scrollDirection: Axis.horizontal,
            itemCount: items.length,
            separatorBuilder: (_, __) => const SizedBox(width: 16),
            itemBuilder: (_, i) => _placeCard(items[i]),
          ),
        ),
        const SizedBox(height: 32),
      ],
    );
  }

  Widget _placeCard(Highlight h) {
    return GestureDetector(
      onTap: () => Navigator.push(
        context,
        MaterialPageRoute(builder: (_) => DetailScreen(place: h)),
      ),
      child: Container(
        width: 200,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.06),
              blurRadius: 15,
              offset: Offset(0, 4),
            ),
          ],
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            ClipRRect(
              borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
              child: CachedNetworkImage(
                imageUrl: h.displayImage,
                height: 140,
                width: double.infinity,
                fit: BoxFit.cover,
                placeholder: (context, url) => Shimmer.fromColors(
                  baseColor: Colors.grey.shade200,
                  highlightColor: Colors.grey.shade50,
                  child: Container(color: Colors.white),
                ),
                errorWidget: (context, url, error) => Container(
                  color: Colors.grey.shade100,
                  child: Icon(
                    Icons.place,
                    color: Colors.teal.shade200,
                    size: 40,
                  ),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    h.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                      color: Colors.black87,
                    ),
                  ),
                  SizedBox(height: 6),
                  Text(
                    h.area,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(color: Colors.grey.shade600, fontSize: 13),
                  ),
                  SizedBox(height: 10),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Container(
                        padding: EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 4,
                        ),
                        decoration: BoxDecoration(
                          color: _getCategoryColor(h.category).withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          h.category,
                          style: TextStyle(
                            fontSize: 11,
                            color: _getCategoryColor(h.category),
                            fontWeight: FontWeight.w600,
                          ),
                        ),
                      ),
                      Text(
                        "${h.distanceFromCenter.toStringAsFixed(1)} km",
                        style: TextStyle(
                          fontSize: 12,
                          color: Colors.grey.shade600,
                          fontWeight: FontWeight.w500,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _shimmerCard() {
    return Shimmer.fromColors(
      baseColor: Colors.grey.shade200,
      highlightColor: Colors.grey.shade50,
      child: Container(
        width: 260,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(24),
        ),
      ),
    );
  }

  Color _getCategoryColor(String category) {
    switch (category.toLowerCase()) {
      case 'turistik':
        return Colors.blue;
      case 'lokal':
        return Colors.orange;
      case 'instagramlik':
        return Colors.pink;
      case 'chill':
        return Colors.green;
      default:
        return Colors.teal;
    }
  }
}
