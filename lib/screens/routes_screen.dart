// Dosya: lib/screens/routes_screen.dart

import 'package:flutter/material.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:shimmer/shimmer.dart';
import '../services/user_preferences.dart';
import 'route_detail_screen.dart';

class RoutesScreen extends StatefulWidget {
  const RoutesScreen({super.key});

  @override
  State<RoutesScreen> createState() => _RoutesScreenState();
}

class _RoutesScreenState extends State<RoutesScreen> {
  List<RouteModel> _allRoutes = [];
  List<RouteModel> _personalizedRoutes = [];
  bool _loading = true;
  String _selectedTab = "Sana Özel"; // Sana Özel, Tüm Rotalar, Favoriler

  Map<String, dynamic> _userProfile = {};

  @override
  void initState() {
    super.initState();
    _loadUserProfileAndRoutes();
  }

  Future<void> _loadUserProfileAndRoutes() async {
    setState(() => _loading = true);

    // Kullanıcı profilini yükle
    _userProfile = await UserPreferences.getUserProfile();

    await Future.delayed(Duration(milliseconds: 500));

    // Tüm rotalar
    _allRoutes = _getAllRoutes();

    // Kişiselleştirilmiş rotalar
    _personalizedRoutes = _getPersonalizedRoutes();

    setState(() => _loading = false);
  }

  // Tüm rotalar
  List<RouteModel> _getAllRoutes() {
    return [
      RouteModel(
        id: "1",
        name: "Gaudí'nin İzinde",
        description: "Barcelona'nın en ikonik Gaudí eserlerini keşfedin",
        duration: "4-5 saat",
        distance: "8.5 km",
        stops: 5,
        difficulty: "Orta",
        imageUrl:
            "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        tags: ["Mimari", "Kültür", "Fotoğraf"],
        categories: ["Turistik", "Instagramlık"],
        budget: "medium",
        walkingLevel: 2,
        isPopular: true,
      ),
      RouteModel(
        id: "2",
        name: "Lokal Lezzetler Turu",
        description: "Yerel pazarlar ve tapas barlarında gastronomi deneyimi",
        duration: "3-4 saat",
        distance: "5.2 km",
        stops: 7,
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
        tags: ["Yemek", "Lokal", "Kültür"],
        categories: ["Lokal"],
        budget: "medium",
        walkingLevel: 1,
        isPopular: true,
      ),
      RouteModel(
        id: "3",
        name: "Gün Batımı Rotası",
        description: "En güzel manzara noktalarında gün batımı keyfi",
        duration: "2-3 saat",
        distance: "6.8 km",
        stops: 4,
        difficulty: "Orta",
        imageUrl:
            "https://images.unsplash.com/photo-1562883676-8c7feb83f09b?w=800",
        tags: ["Manzara", "Fotoğraf", "Romantik"],
        categories: ["Instagramlık", "Chill"],
        budget: "free",
        walkingLevel: 2,
        isPopular: false,
      ),
      RouteModel(
        id: "4",
        name: "Plaj ve Deniz Rotası",
        description: "Sahil şeridi boyunca rahat bir yürüyüş",
        duration: "3 saat",
        distance: "7.5 km",
        stops: 6,
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
        tags: ["Plaj", "Chill", "Doğa"],
        categories: ["Chill"],
        budget: "low",
        walkingLevel: 2,
        isPopular: false,
      ),
      RouteModel(
        id: "5",
        name: "Gece Hayatı Turu",
        description: "En iyi bar ve kulüplerde unutulmaz bir gece",
        duration: "5-6 saat",
        distance: "4.2 km",
        stops: 8,
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800",
        tags: ["Gece Hayatı", "Bar", "Eğlence"],
        categories: ["Lokal"],
        budget: "high",
        walkingLevel: 1,
        isPopular: true,
      ),
      RouteModel(
        id: "6",
        name: "Sanat ve Müze Turu",
        description:
            "Barcelona'nın en önemli müze ve sanat galerilerini keşfedin",
        duration: "5-6 saat",
        distance: "6.3 km",
        stops: 5,
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
        tags: ["Müze", "Sanat", "Kültür"],
        categories: ["Turistik"],
        budget: "medium",
        walkingLevel: 1,
        isPopular: false,
      ),
      RouteModel(
        id: "7",
        name: "Hidden Gems Rotası",
        description: "Turistlerin bilmediği gizli köşeleri keşfedin",
        duration: "4 saat",
        distance: "9.2 km",
        stops: 8,
        difficulty: "Orta",
        imageUrl:
            "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=800",
        tags: ["Hidden gems", "Lokal", "Keşif"],
        categories: ["Lokal"],
        budget: "low",
        walkingLevel: 2,
        isPopular: false,
      ),
      RouteModel(
        id: "8",
        name: "Kahve ve Kafe Turu",
        description: "Barcelona'nın en iyi specialty coffee mekanları",
        duration: "3 saat",
        distance: "4.5 km",
        stops: 6,
        difficulty: "Kolay",
        imageUrl:
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
        tags: ["Kafe", "Kahve", "Çalışma"],
        categories: ["Lokal", "Chill"],
        budget: "medium",
        walkingLevel: 1,
        isPopular: false,
      ),
    ];
  }

  // Kişiselleştirilmiş rotalar
  List<RouteModel> _getPersonalizedRoutes() {
    final travelStyle = _userProfile['travelStyle'] as String;
    final walkingLevel = _userProfile['walkingLevel'] as int;
    final budgetLevel = _userProfile['budgetLevel'] as String;
    final interests = _userProfile['interests'] as List<String>;

    // Maksimum mesafe
    final maxDistance = UserPreferences.getMaxDistanceForWalkingLevel(
      walkingLevel,
    );

    // İzin verilen fiyatlar
    final allowedBudgets = UserPreferences.getAllowedPricesForBudget(
      budgetLevel,
    );

    // Tercih edilen kategoriler
    final preferredCategories = UserPreferences.getCategoriesForTravelStyle(
      travelStyle,
    );

    // Filtreleme ve skorlama
    List<MapEntry<RouteModel, int>> scoredRoutes = [];

    for (var route in _allRoutes) {
      int score = 0;

      // Mesafe kontrolü
      final routeDistance = double.parse(route.distance.split(' ')[0]);
      if (routeDistance > maxDistance) continue;

      // Bütçe kontrolü
      if (!allowedBudgets.contains(route.budget)) continue;

      // Walking level uyumu
      if (route.walkingLevel <= walkingLevel) score += 10;

      // Kategori uyumu
      for (var cat in route.categories) {
        if (preferredCategories.contains(cat)) score += 20;
      }

      // İlgi alanı uyumu
      for (var interest in interests) {
        if (route.tags.any(
          (tag) => tag.toLowerCase().contains(interest.toLowerCase()),
        )) {
          score += 15;
        }
      }

      // Popüler rotalar bonus
      if (route.isPopular) score += 5;

      scoredRoutes.add(MapEntry(route, score));
    }

    // Skora göre sırala
    scoredRoutes.sort((a, b) => b.value.compareTo(a.value));

    // En iyi 5 rotayı döndür
    return scoredRoutes.take(5).map((e) => e.key).toList();
  }

  List<RouteModel> get _displayedRoutes {
    if (_selectedTab == "Sana Özel") {
      return _personalizedRoutes;
    } else if (_selectedTab == "Tüm Rotalar") {
      return _allRoutes;
    } else {
      return []; // Favoriler
    }
  }

  @override
  Widget build(BuildContext context) {
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
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // 🏙️ Header
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          "Rotalar",
                          style: TextStyle(
                            fontSize: 34,
                            fontWeight: FontWeight.bold,
                            color: Colors.black87,
                            letterSpacing: -0.5,
                          ),
                        ),
                        SizedBox(height: 4),
                        Text(
                          _selectedTab == "Sana Özel"
                              ? "Sana özel ${_personalizedRoutes.length} rota"
                              : "Tüm rotalar",
                          style: TextStyle(
                            fontSize: 16,
                            color: Colors.grey.shade600,
                            fontWeight: FontWeight.w400,
                          ),
                        ),
                      ],
                    ),
                    // Yeni Rota Oluştur Butonu
                    Container(
                      decoration: BoxDecoration(
                        color: Colors.teal,
                        borderRadius: BorderRadius.circular(12),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.teal.withOpacity(0.3),
                            blurRadius: 10,
                            offset: Offset(0, 4),
                          ),
                        ],
                      ),
                      child: IconButton(
                        icon: Icon(Icons.add_rounded, color: Colors.white),
                        onPressed: () {
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              content: Text(
                                "Rota oluşturma yakında eklenecek!",
                              ),
                              backgroundColor: Colors.teal,
                            ),
                          );
                        },
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 24),

              // 🎯 Tabs
              _buildTabs(),

              // Kullanıcı profil özeti (Sana Özel sekmesinde)
              if (_selectedTab == "Sana Özel" && !_loading)
                _buildProfileSummary(),

              const SizedBox(height: 20),

              // 📍 Rotalar
              Expanded(child: _loading ? _buildLoading() : _buildRoutesList()),
            ],
          ),
        ),
      ),
    );
  }

  // 👤 Profil Özeti
  Widget _buildProfileSummary() {
    final travelStyle = _userProfile['travelStyle'] as String;
    final interests = _userProfile['interests'] as List<String>;

    return Container(
      margin: EdgeInsets.symmetric(horizontal: 20, vertical: 12),
      padding: EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [Colors.teal.shade50, Colors.teal.shade100],
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.teal.shade200),
      ),
      child: Row(
        children: [
          Container(
            padding: EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: Colors.teal,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(Icons.person_rounded, color: Colors.white, size: 24),
          ),
          SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Gezme Tarzın: $travelStyle",
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    color: Colors.teal.shade900,
                  ),
                ),
                if (interests.isNotEmpty) ...[
                  SizedBox(height: 4),
                  Text(
                    "İlgi: ${interests.take(3).join(', ')}",
                    style: TextStyle(fontSize: 13, color: Colors.teal.shade700),
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

  // 🎯 TABS
  Widget _buildTabs() {
    final tabs = ["Sana Özel", "Tüm Rotalar", "Favoriler"];

    return SizedBox(
      height: 44,
      child: ListView.separated(
        scrollDirection: Axis.horizontal,
        padding: const EdgeInsets.symmetric(horizontal: 20),
        itemCount: tabs.length,
        separatorBuilder: (_, __) => const SizedBox(width: 12),
        itemBuilder: (_, i) {
          final tab = tabs[i];
          final isSelected = _selectedTab == tab;

          return GestureDetector(
            onTap: () {
              setState(() => _selectedTab = tab);
            },
            child: AnimatedContainer(
              duration: Duration(milliseconds: 200),
              padding: EdgeInsets.symmetric(horizontal: 20, vertical: 10),
              decoration: BoxDecoration(
                color: isSelected ? Colors.teal : Colors.white,
                borderRadius: BorderRadius.circular(22),
                border: Border.all(
                  color: isSelected ? Colors.teal : Colors.grey.shade300,
                  width: 1.5,
                ),
                boxShadow: isSelected
                    ? [
                        BoxShadow(
                          color: Colors.teal.withOpacity(0.3),
                          blurRadius: 8,
                          offset: Offset(0, 2),
                        ),
                      ]
                    : [],
              ),
              child: Center(
                child: Text(
                  tab,
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.w600,
                    color: isSelected ? Colors.white : Colors.grey.shade700,
                  ),
                ),
              ),
            ),
          );
        },
      ),
    );
  }

  // 📍 ROTALAR LİSTESİ
  Widget _buildRoutesList() {
    final routes = _displayedRoutes;

    if (routes.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              _selectedTab == "Favoriler"
                  ? Icons.favorite_border_rounded
                  : Icons.route_rounded,
              size: 64,
              color: Colors.grey.shade300,
            ),
            SizedBox(height: 16),
            Text(
              _selectedTab == "Favoriler"
                  ? "Henüz favori rota yok"
                  : "Sana uygun rota bulunamadı",
              style: TextStyle(
                fontSize: 18,
                color: Colors.grey.shade600,
                fontWeight: FontWeight.w600,
              ),
            ),
            SizedBox(height: 8),
            Text(
              _selectedTab == "Favoriler"
                  ? "Beğendiğiniz rotaları favorilere ekleyin"
                  : "Tüm rotalar sekmesine göz atın",
              style: TextStyle(fontSize: 14, color: Colors.grey.shade400),
            ),
          ],
        ),
      );
    }

    return ListView.separated(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
      itemCount: routes.length,
      separatorBuilder: (_, __) => const SizedBox(height: 20),
      itemBuilder: (_, i) {
        final route = routes[i];
        return _routeCard(route, i);
      },
    );
  }

  // 🗺️ ROUTE CARD
  Widget _routeCard(RouteModel route, int index) {
    // Sana Özel sekmesinde sıralama göster
    final showRank = _selectedTab == "Sana Özel";

    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => RouteDetailScreen(route: route)),
        );
      },
      child: Container(
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
            // 🖼️ Görsel
            Stack(
              children: [
                ClipRRect(
                  borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
                  child: CachedNetworkImage(
                    imageUrl: route.imageUrl,
                    height: 200,
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
                        Icons.route,
                        color: Colors.teal.shade200,
                        size: 50,
                      ),
                    ),
                  ),
                ),

                // Gradient overlay
                Positioned.fill(
                  child: Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.vertical(
                        top: Radius.circular(20),
                      ),
                      gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.transparent,
                          Colors.black.withOpacity(0.4),
                        ],
                      ),
                    ),
                  ),
                ),

                // Sıralama Badge (Sana Özel'de)
                if (showRank)
                  Positioned(
                    top: 12,
                    left: 12,
                    child: Container(
                      padding: EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: index == 0 ? Colors.amber : Colors.teal,
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
                            size: 14,
                            color: Colors.white,
                          ),
                          SizedBox(width: 4),
                          Text(
                            index == 0 ? "En Uygun" : "#${index + 1}",
                            style: TextStyle(
                              fontSize: 12,
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),

                // Popüler Badge
                if (route.isPopular && !showRank)
                  Positioned(
                    top: 12,
                    left: 12,
                    child: Container(
                      padding: EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.orange,
                        borderRadius: BorderRadius.circular(20),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.orange.withOpacity(0.4),
                            blurRadius: 8,
                            offset: Offset(0, 2),
                          ),
                        ],
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          Icon(
                            Icons.local_fire_department_rounded,
                            size: 14,
                            color: Colors.white,
                          ),
                          SizedBox(width: 4),
                          Text(
                            "Popüler",
                            style: TextStyle(
                              fontSize: 12,
                              color: Colors.white,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),

                // Favori Butonu
                Positioned(
                  top: 12,
                  right: 12,
                  child: Container(
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.9),
                      shape: BoxShape.circle,
                    ),
                    child: IconButton(
                      icon: Icon(
                        Icons.favorite_border_rounded,
                        color: Colors.grey.shade700,
                        size: 20,
                      ),
                      onPressed: () {
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(
                            content: Text("Favorilere eklendi!"),
                            backgroundColor: Colors.teal,
                            duration: Duration(seconds: 2),
                          ),
                        );
                      },
                    ),
                  ),
                ),
              ],
            ),

            // Bilgiler
            Padding(
              padding: const EdgeInsets.all(18),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // İsim
                  Text(
                    route.name,
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.black87,
                    ),
                  ),

                  SizedBox(height: 6),

                  // Açıklama
                  Text(
                    route.description,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: TextStyle(
                      fontSize: 14,
                      color: Colors.grey.shade600,
                      height: 1.4,
                    ),
                  ),

                  SizedBox(height: 16),

                  // İstatistikler
                  Row(
                    children: [
                      _statChip(Icons.access_time_rounded, route.duration),
                      SizedBox(width: 10),
                      _statChip(Icons.straighten_rounded, route.distance),
                      SizedBox(width: 10),
                      _statChip(
                        Icons.location_on_rounded,
                        "${route.stops} durak",
                      ),
                    ],
                  ),

                  SizedBox(height: 14),

                  // Tags
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: route.tags
                        .map(
                          (tag) => Container(
                            padding: EdgeInsets.symmetric(
                              horizontal: 10,
                              vertical: 5,
                            ),
                            decoration: BoxDecoration(
                              color: Colors.teal.withOpacity(0.1),
                              borderRadius: BorderRadius.circular(8),
                            ),
                            child: Text(
                              tag,
                              style: TextStyle(
                                fontSize: 12,
                                color: Colors.teal.shade700,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
                          ),
                        )
                        .toList(),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // 📊 Stat Chip
  Widget _statChip(IconData icon, String text) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: Colors.grey.shade100,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 14, color: Colors.grey.shade600),
          SizedBox(width: 4),
          Text(
            text,
            style: TextStyle(
              fontSize: 12,
              color: Colors.grey.shade700,
              fontWeight: FontWeight.w600,
            ),
          ),
        ],
      ),
    );
  }

  // 🔄 LOADING
  Widget _buildLoading() {
    return ListView.separated(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
      itemCount: 3,
      separatorBuilder: (_, __) => const SizedBox(height: 20),
      itemBuilder: (_, i) => _shimmerCard(),
    );
  }

  Widget _shimmerCard() {
    return Shimmer.fromColors(
      baseColor: Colors.grey.shade200,
      highlightColor: Colors.grey.shade50,
      child: Container(
        height: 350,
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(20),
        ),
      ),
    );
  }
}

// 🗺️ ROUTE MODEL (Güncellenmiş)
class RouteModel {
  final String id;
  final String name;
  final String description;
  final String duration;
  final String distance;
  final int stops;
  final String difficulty;
  final String imageUrl;
  final List<String> tags;
  final List<String> categories; // YENİ
  final String budget; // YENİ: free, low, medium, high
  final int walkingLevel; // YENİ: 0-3
  final bool isPopular;

  RouteModel({
    required this.id,
    required this.name,
    required this.description,
    required this.duration,
    required this.distance,
    required this.stops,
    required this.difficulty,
    required this.imageUrl,
    required this.tags,
    required this.categories,
    required this.budget,
    required this.walkingLevel,
    this.isPopular = false,
  });
}
