import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/city_model.dart';
import '../services/city_data_loader.dart';
import 'detail_screen.dart';
import 'onboarding_screen.dart';

class ProfileScreen extends StatefulWidget {
  const ProfileScreen({super.key});

  @override
  State<ProfileScreen> createState() => _ProfileScreenState();
}

class _ProfileScreenState extends State<ProfileScreen> {
  String userName = "Gezgin";
  String userCity = "Barcelona";
  String travelStyle = "";
  String walkingLevel = "";
  String budget = "";
  List<String> interests = [];
  List<String> favorites = [];
  List<Highlight> favoriteHighlights = [];

  bool isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadUserData();
  }

  Future<void> _loadUserData() async {
    final prefs = await SharedPreferences.getInstance();

    setState(() {
      userName = prefs.getString("user_name") ?? "Gezgin";
      userCity = prefs.getString("selected_city") ?? "Barcelona";
      travelStyle = prefs.getString("travel_style") ?? "";
      walkingLevel = prefs.getString("walking_level") ?? "";
      budget = prefs.getString("budget") ?? "";
      interests = prefs.getStringList("interests") ?? [];
      favorites = prefs.getStringList("favorite_places") ?? [];
    });

    await _loadFavoriteHighlights();

    setState(() {
      isLoading = false;
    });
  }

  Future<void> _loadFavoriteHighlights() async {
    if (favorites.isEmpty) return;

    final cityData = await CityDataLoader.loadCity(userCity);
    if (cityData != null) {
      favoriteHighlights = cityData.highlights
          .where((h) => favorites.contains(h.name))
          .toList();
    }
  }

  Future<void> _editPreferences() async {
    final result = await Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => OnboardingScreen()),
    );

    if (result == true) {
      _loadUserData();
    }
  }

  @override
  Widget build(BuildContext context) {
    if (isLoading) {
      return Scaffold(
        backgroundColor: Colors.white,
        body: Center(child: CircularProgressIndicator(color: Colors.teal)),
      );
    }

    return Scaffold(
      backgroundColor: Colors.grey.shade50,
      body: CustomScrollView(
        slivers: [
          // 🎨 HEADER
          SliverAppBar(
            expandedHeight: 200,
            pinned: true,
            backgroundColor: Colors.teal,
            elevation: 0,
            flexibleSpace: FlexibleSpaceBar(
              background: Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [Colors.teal.shade400, Colors.teal.shade700],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                ),
                child: SafeArea(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      SizedBox(height: 20),
                      // Avatar
                      Container(
                        width: 90,
                        height: 90,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: Colors.white,
                          boxShadow: [
                            BoxShadow(
                              color: Colors.black.withOpacity(0.2),
                              blurRadius: 15,
                              offset: Offset(0, 5),
                            ),
                          ],
                        ),
                        child: Icon(
                          Icons.person,
                          size: 50,
                          color: Colors.teal.shade700,
                        ),
                      ),
                      SizedBox(height: 12),
                      Text(
                        userName,
                        style: TextStyle(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      SizedBox(height: 4),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(
                            Icons.location_on,
                            size: 16,
                            color: Colors.white70,
                          ),
                          SizedBox(width: 4),
                          Text(
                            userCity,
                            style: TextStyle(
                              fontSize: 15,
                              color: Colors.white70,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ),

          // 📊 İSTATİSTİKLER
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: _statCard(
                          Icons.favorite,
                          favorites.length.toString(),
                          "Favoriler",
                          Colors.red,
                        ),
                      ),
                      SizedBox(width: 12),
                      Expanded(
                        child: _statCard(
                          Icons.map,
                          "0",
                          "Rotalar",
                          Colors.blue,
                        ),
                      ),
                      SizedBox(width: 12),
                      Expanded(
                        child: _statCard(
                          Icons.place,
                          "0",
                          "Ziyaretler",
                          Colors.orange,
                        ),
                      ),
                    ],
                  ),

                  SizedBox(height: 24),

                  // 🎯 SEYAHAT TERCİHLERİ
                  _sectionTitle("Seyahat Tercihlerim"),
                  SizedBox(height: 12),

                  Container(
                    padding: EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.05),
                          blurRadius: 10,
                          offset: Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        _preferenceRow(
                          Icons.style,
                          "Seyahat Tarzı",
                          _getTravelStyleText(travelStyle),
                        ),
                        Divider(height: 24),
                        _preferenceRow(
                          Icons.directions_walk,
                          "Yürüyüş Seviyesi",
                          _getWalkingLevelText(walkingLevel),
                        ),
                        Divider(height: 24),
                        _preferenceRow(
                          Icons.payments,
                          "Bütçe",
                          _getBudgetText(budget),
                        ),
                        Divider(height: 24),
                        _preferenceRow(
                          Icons.interests,
                          "İlgi Alanları",
                          interests.join(", "),
                        ),
                      ],
                    ),
                  ),

                  SizedBox(height: 16),

                  // Düzenle Butonu
                  ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      minimumSize: Size(double.infinity, 50),
                      backgroundColor: Colors.teal,
                      foregroundColor: Colors.white,
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    onPressed: _editPreferences,
                    icon: Icon(Icons.edit, size: 20),
                    label: Text(
                      "Tercihleri Düzenle",
                      style: TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                  ),

                  SizedBox(height: 24),

                  // ❤️ FAVORİLER
                  _sectionTitle("Favorilerim (${favorites.length})"),
                  SizedBox(height: 12),

                  if (favoriteHighlights.isEmpty)
                    Container(
                      padding: EdgeInsets.all(40),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Column(
                        children: [
                          Icon(
                            Icons.favorite_border,
                            size: 60,
                            color: Colors.grey.shade300,
                          ),
                          SizedBox(height: 16),
                          Text(
                            "Henüz favori yerin yok",
                            style: TextStyle(
                              fontSize: 16,
                              color: Colors.grey.shade600,
                            ),
                          ),
                          SizedBox(height: 8),
                          Text(
                            "Keşfet'ten beğendiğin yerleri favorilere ekle!",
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              fontSize: 14,
                              color: Colors.grey.shade400,
                            ),
                          ),
                        ],
                      ),
                    )
                  else
                    ...favoriteHighlights.map((place) => _favoriteCard(place)),

                  SizedBox(height: 24),

                  // ⚙️ AYARLAR
                  _sectionTitle("Ayarlar"),
                  SizedBox(height: 12),

                  Container(
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(20),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withOpacity(0.05),
                          blurRadius: 10,
                          offset: Offset(0, 4),
                        ),
                      ],
                    ),
                    child: Column(
                      children: [
                        _settingsTile(
                          Icons.notifications_outlined,
                          "Bildirimler",
                          () {},
                        ),
                        Divider(height: 1),
                        _settingsTile(Icons.language, "Dil", () {}),
                        Divider(height: 1),
                        _settingsTile(Icons.dark_mode_outlined, "Tema", () {}),
                        Divider(height: 1),
                        _settingsTile(
                          Icons.help_outline,
                          "Yardım & Destek",
                          () {},
                        ),
                        Divider(height: 1),
                        _settingsTile(Icons.info_outline, "Hakkında", () {}),
                      ],
                    ),
                  ),

                  SizedBox(height: 40),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  // 📊 İstatistik Kartı
  Widget _statCard(IconData icon, String value, String label, Color color) {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.05),
            blurRadius: 10,
            offset: Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        children: [
          Icon(icon, size: 32, color: color),
          SizedBox(height: 8),
          Text(
            value,
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.black87,
            ),
          ),
          SizedBox(height: 4),
          Text(
            label,
            style: TextStyle(fontSize: 13, color: Colors.grey.shade600),
          ),
        ],
      ),
    );
  }

  // 📝 Bölüm Başlığı
  Widget _sectionTitle(String title) {
    return Text(
      title,
      style: TextStyle(
        fontSize: 20,
        fontWeight: FontWeight.bold,
        color: Colors.black87,
      ),
    );
  }

  // 🎯 Tercih Satırı
  Widget _preferenceRow(IconData icon, String label, String value) {
    return Row(
      children: [
        Container(
          padding: EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Colors.teal.withOpacity(0.1),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Icon(icon, size: 22, color: Colors.teal),
        ),
        SizedBox(width: 16),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                label,
                style: TextStyle(fontSize: 13, color: Colors.grey.shade600),
              ),
              SizedBox(height: 4),
              Text(
                value.isEmpty ? "Belirtilmemiş" : value,
                style: TextStyle(
                  fontSize: 15,
                  fontWeight: FontWeight.w600,
                  color: Colors.black87,
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  // ❤️ Favori Kartı
  Widget _favoriteCard(Highlight place) {
    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
        );
      },
      child: Container(
        margin: EdgeInsets.only(bottom: 12),
        padding: EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.05),
              blurRadius: 10,
              offset: Offset(0, 4),
            ),
          ],
        ),
        child: Row(
          children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: Image.network(
                place.displayImage,
                width: 70,
                height: 70,
                fit: BoxFit.cover,
                errorBuilder: (_, __, ___) => Container(
                  width: 70,
                  height: 70,
                  color: Colors.grey.shade200,
                  child: Icon(Icons.place, color: Colors.grey.shade400),
                ),
              ),
            ),
            SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    place.name,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Colors.black87,
                    ),
                  ),
                  SizedBox(height: 4),
                  Text(
                    place.area,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(fontSize: 13, color: Colors.grey.shade600),
                  ),
                ],
              ),
            ),
            Icon(Icons.chevron_right, color: Colors.grey.shade400),
          ],
        ),
      ),
    );
  }

  // ⚙️ Ayarlar Satırı
  Widget _settingsTile(IconData icon, String title, VoidCallback onTap) {
    return ListTile(
      leading: Icon(icon, color: Colors.grey.shade700),
      title: Text(title, style: TextStyle(fontSize: 15, color: Colors.black87)),
      trailing: Icon(Icons.chevron_right, color: Colors.grey.shade400),
      onTap: onTap,
    );
  }

  // 🎨 Metin Dönüşümleri
  String _getTravelStyleText(String style) {
    switch (style) {
      case "tourist":
        return "Turistik";
      case "local":
        return "Lokal";
      case "instagram":
        return "Instagram'lık";
      case "chill":
        return "Chill";
      default:
        return style;
    }
  }

  String _getWalkingLevelText(String level) {
    switch (level) {
      case "low":
        return "Az Yürüyüş";
      case "medium":
        return "Orta";
      case "high":
        return "Çok Yürüyüş";
      default:
        return level;
    }
  }

  String _getBudgetText(String budget) {
    switch (budget) {
      case "low":
        return "Ekonomik";
      case "medium":
        return "Orta";
      case "high":
        return "Lüks";
      default:
        return budget;
    }
  }
}
