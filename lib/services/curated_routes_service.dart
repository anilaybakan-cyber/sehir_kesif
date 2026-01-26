// lib/services/curated_routes_service.dart
// Şehre özgü hazır rotalar servisi

import 'package:flutter/material.dart';
import '../models/city_model.dart';
import '../theme/wanderlust_colors.dart';
import 'dart:math';

class CuratedRoute {
  final String id;
  final String name;
  final String description;
  final String duration;
  final String distance;
  final String difficulty;
  final String imageUrl;
  final List<String> tags;
  final List<String> placeNames;
  final List<String> interests; // Kullanıcı ilgi alanlarına göre eşleştirme
  final Color accentColor;
  final IconData icon;

  const CuratedRoute({
    required this.id,
    required this.name,
    required this.description,
    required this.duration,
    required this.distance,
    required this.difficulty,
    required this.imageUrl,
    required this.tags,
    required this.placeNames,
    required this.interests,
    required this.accentColor,
    required this.icon,
  });
}

class CuratedRoutesService {
  
  /// Şehir modelinden otomatik rotalar oluşturur
  static Future<List<CuratedRoute>> generateRoutes(CityModel city, bool isEnglish) async {
    final existingRoutes = getRoutes(city.city, isEnglish);
    final allHighlights = List<Highlight>.from(city.highlights);
    final generatedRoutes = <CuratedRoute>[];
    
    // Var olan rota isimlerini kontrol et (çakışmayı önlemek için)
    final existingNames = existingRoutes.map((r) => r.name).toSet();

    // Yardımcı fonksiyon: Rota ekle
    void addRoute(CuratedRoute route) {
      if (!existingNames.contains(route.name)) {
        generatedRoutes.add(route);
        existingNames.add(route.name);
      }
    }

    // 1. "Iconic [City]" / "[City] Klasikleri" (En yüksek puanlı 6 yer - Coğrafi Olarak Kümelenmiş)
    allHighlights.sort((a, b) => (b.rating ?? 0).compareTo(a.rating ?? 0));
    
    if (allHighlights.isNotEmpty) {
      final anchor = allHighlights.first;
      // Anchor'a yakın (maks 80km) ve yüksek puanlı diğer yerleri bul
      final nearbyTopPlaces = _getNearbyHighlights(anchor, allHighlights, 80.0);
      // Puanına göre sırala ve ilk 6'yı al (Anchor dahil)
      nearbyTopPlaces.sort((a, b) => (b.rating ?? 0).compareTo(a.rating ?? 0));
      final topPlaces = nearbyTopPlaces.take(6).toList();

      if (topPlaces.length >= 4) {
        addRoute(_createRoute(
          id: "${city.city.toLowerCase()}_top",
          name: isEnglish ? "Best of ${city.city}" : "${city.city} Klasikleri",
          description: isEnglish 
              ? "The absolute must-see landmarks of ${city.city}. Perfect for first-time visitors."
              : "${city.city}'nin mutlaka görülmesi gereken simge yapıları. İlk kez gelenler için ideal.",
          places: _optimizeRoute(topPlaces),
          color: const Color(0xFFE91E63), // Pink
          icon: Icons.star_rounded,
          tags: isEnglish ? ["iconic", "must-see", "popular"] : ["ikonik", "popüler", "klasik"],
          interests: ["history", "photo", "culture"],
        ));
      }
    }

    // 2. Kültür ve Tarih Rotası (Müze, Tarihi - Coğrafi Kümelenmiş)
    final culturePlaces = allHighlights.where((h) => 
      h.category.toLowerCase().contains("müze") || 
      h.category.toLowerCase().contains("tarih") ||
      h.category.toLowerCase().contains("museum") ||
      h.category.toLowerCase().contains("history")
    ).toList();
    
    if (culturePlaces.isNotEmpty) {
       // En popüler tarihi yeri merkez al
       culturePlaces.sort((a, b) => (b.rating ?? 0).compareTo(a.rating ?? 0));
       final anchor = culturePlaces.first;
       final nearbyCulture = _getNearbyHighlights(anchor, culturePlaces, 50.0);
       
        if (nearbyCulture.length >= 4) {
          // Yakın bir kafe ekle (mola için)
          final cafe = allHighlights.firstWhere(
            (h) => (h.category.toLowerCase().contains("kafe") || h.category.toLowerCase().contains("cafe")) &&
                   _calculateDistance(anchor.lat, anchor.lng, h.lat, h.lng) < 5.0, // 5km içindeki kafe
            orElse: () => allHighlights.first
          );
          
          // Eğer kafe gerçekten yakınsa ve listede yoksa ekle
          if (!nearbyCulture.contains(cafe) && _calculateDistance(anchor.lat, anchor.lng, cafe.lat, cafe.lng) < 10.0) {
             nearbyCulture.insert(nearbyCulture.length ~/ 2, cafe);
          }
          
          addRoute(_createRoute(
            id: "${city.city.toLowerCase()}_culture",
            name: isEnglish ? "Culture & History Walk" : "Kültür ve Tarih Yürüyüşü",
            description: isEnglish
                ? "Immerse yourself in the rich history and artistic heritage of the city."
                : "Şehrin zengin tarihi ve sanatsal mirasına derin bir yolculuk.",
            places: _optimizeRoute(nearbyCulture.take(6).toList()),
            color: const Color(0xFF9C27B0), // Purple
            icon: Icons.museum_rounded,
            tags: isEnglish ? ["history", "art", "museum"] : ["tarih", "sanat", "müze"],
            interests: ["history", "art"],
          ));
        }
    }

    // 3. Doğa ve Manzara (Park, Manzara - Coğrafi Kümelenmiş)
    final naturePlaces = allHighlights.where((h) => 
      h.category.toLowerCase().contains("park") || 
      h.category.toLowerCase().contains("manzara") ||
      h.category.toLowerCase().contains("doğa") ||
      h.category.toLowerCase().contains("nature") ||
      h.category.toLowerCase().contains("view")
    ).toList();

    if (naturePlaces.isNotEmpty) {
      naturePlaces.sort((a, b) => (b.rating ?? 0).compareTo(a.rating ?? 0));
      final anchor = naturePlaces.first;
      final nearbyNature = _getNearbyHighlights(anchor, naturePlaces, 60.0);

      if (nearbyNature.length >= 3) {
        addRoute(_createRoute(
          id: "${city.city.toLowerCase()}_nature",
          name: isEnglish ? "Green & Scenic Views" : "Doğa ve Manzara",
          description: isEnglish
              ? "Escape the crowd and enjoy the most beautiful parks and panoramic viewpoints."
              : "Kalabalıktan kaçın ve şehrin en güzel parkları ile manzaralarının tadını çıkarın.",
          places: _optimizeRoute(nearbyNature.take(5).toList()),
          color: const Color(0xFF4CAF50), // Green
          icon: Icons.landscape_rounded,
          tags: isEnglish ? ["nature", "parks", "relax"] : ["doğa", "park", "huzur"],
          interests: ["nature", "photo"],
        ));
      }
    }

    // 4. Lezzet Turu (Restoran, Kafe, Yemek - Coğrafi Kümelenmiş)
    final foodPlaces = allHighlights.where((h) => 
      h.category.toLowerCase().contains("restoran") || 
      h.category.toLowerCase().contains("kafe") || 
      h.category.toLowerCase().contains("yemek") ||
      h.category.toLowerCase().contains("food") ||
      h.category.toLowerCase().contains("restaurant") ||
      h.category.toLowerCase().contains("cafe")
    ).toList();

    if (foodPlaces.isNotEmpty) {
      foodPlaces.shuffle(); // Lezzette rastgelelik iyidir ama yakınlık şart
      final anchor = foodPlaces.first;
      final nearbyFood = _getNearbyHighlights(anchor, foodPlaces, 15.0); // Yemek için daha dar alan (yürünebilir)
      
      if (nearbyFood.length >= 4) {
        addRoute(_createRoute(
          id: "${city.city.toLowerCase()}_food",
          name: isEnglish ? "Gastronomy Tour" : "Lezzet Durakları",
          description: isEnglish
              ? "A delicious journey through local flavors, best cafes and cozy restaurants."
              : "Yerel lezzetler, en iyi kafeler ve keyifli restoranlarla dolu leziz bir rota.",
          places: _optimizeRoute(nearbyFood.take(6).toList()),
          color: const Color(0xFFFF9800), // Orange
          icon: Icons.restaurant_rounded,
          tags: isEnglish ? ["food", "local", "delicious"] : ["yemek", "lezzet", "yerel"],
          interests: ["food"],
        ));
      }
    }

    // 5. Gizli Hazineler / Alternatif Rota (Yüksek puanlı ama klasik listede olmayanlar - Coğrafi)
    final usedNames = generatedRoutes.expand((r) => r.placeNames).toSet();
    final hiddenGems = allHighlights.where((h) => 
      !usedNames.contains(h.name) && (h.rating ?? 0) >= 4.3
    ).toList();

    if (hiddenGems.isNotEmpty) {
       hiddenGems.shuffle();
       final anchor = hiddenGems.first;
       final nearbyHidden = _getNearbyHighlights(anchor, hiddenGems, 40.0);

       if (nearbyHidden.length >= 4) {
        addRoute(_createRoute(
          id: "${city.city.toLowerCase()}_hidden",
          name: isEnglish ? "Hidden Gems" : "Gizli Hazineler",
          description: isEnglish
              ? "Discover the lesser-known but highly rated spots loved by locals."
              : "Turistlerin gözünden kaçan ama yerlilerin sevdiği o özel yerleri keşfedin.",
          places: _optimizeRoute(nearbyHidden.take(5).toList()),
          color: const Color(0xFF607D8B), // Blue Grey
          icon: Icons.explore_rounded,
          tags: isEnglish ? ["secret", "local", "quiet"] : ["gizli", "yerel", "sakin"],
          interests: ["culture", "photo"],
        ));
      }
    }

    // 6. Bölge/Semt Rotaları (Neighborhoods)
    // Area bazlı grupla
    final Map<String, List<Highlight>> byArea = {};
    for (var h in allHighlights) {
      if (h.area.isNotEmpty) {
        byArea.putIfAbsent(h.area, () => []).add(h);
      }
    }

    byArea.forEach((area, places) {
      if (places.length >= 4 && generatedRoutes.length + existingRoutes.length < 15) {
        
        final titlesEn = ["Explore $area", "Walk through $area", "$area Highlights", "$area Vibes", "Step by Step $area"];
        final titlesTr = ["Adım Adım $area", "$area Sokakları", "$area Ruhu", "$area Gezintisi", "$area Turu", "$area Keşfi", "$area'yı Yaşa"];
        
        final randomTitle = isEnglish 
            ? titlesEn[Random().nextInt(titlesEn.length)]
            : titlesTr[Random().nextInt(titlesTr.length)];

        addRoute(_createRoute(
          id: "${city.city.toLowerCase()}_${area.toLowerCase().replaceAll(' ', '_')}",
          name: randomTitle,
          description: isEnglish
              ? "A focused walking tour through the charming streets of $area."
              : "$area bölgesinin büyüleyici sokaklarında odaklanmış bir yürüyüş turu.",
          places: _optimizeRoute(places.take(6).toList()),
          color: const Color(0xFF3F51B5), // Indigo
          icon: Icons.map_outlined,
          tags: isEnglish ? ["neighborhood", "walking", "area"] : ["semt", "yürüyüş", "bölge"],
          interests: ["culture", "walking"],
        ));
      }
    });

    // Toplam rota sayısı 10'a tamamlanana kadar karışık rotalar ekle (Mix - Coğrafi Kümelenmiş)
    int attempt = 1;
    while (generatedRoutes.length + existingRoutes.length < 10 && attempt < 10) { // attempt limitini artırdık
      
      // Rastgele bir başlangıç noktası seç
      final potentialAnchors = allHighlights.toList()..shuffle();
      if (potentialAnchors.isEmpty) break;
      
      final anchor = potentialAnchors.first;
      
      // Bu anchor'a yakın (maks 50km) diğer noktaları bul
      final nearbyCluster = _getNearbyHighlights(anchor, allHighlights, 50.0);
      
      // Kendi içinde karıştır
      nearbyCluster.shuffle();
      
      if (nearbyCluster.length >= 4) {
         final mixPlaces = nearbyCluster.take(6).toList();
         
         final mixTitlesEn = ["City Mix", "Day Tripper", "Urban Explorer", "Random Delights", "Full Day Joy"];
         final mixTitlesTr = ["Günü Yakala", "Karışık Rota", "Şehrin Tadı", "Hızlı Bakış", "Tam Günlük Macera", "Şehir Turu", "Rastgele Rota"];
         
         final randomMixTitle = isEnglish 
             ? "${mixTitlesEn[Random().nextInt(mixTitlesEn.length)]} $attempt"
             : "${mixTitlesTr[Random().nextInt(mixTitlesTr.length)]} $attempt";

         // Benzer isimde rota var mı kontrol et (Döngüye girmesin)
         if (!generatedRoutes.any((r) => r.name == randomMixTitle)) {
             addRoute(_createRoute(
               id: "${city.city.toLowerCase()}_mix_$attempt",
               name: randomMixTitle,
               description: isEnglish
                   ? "A balanced mix of sights to maximize your day."
                   : "Gününüzü en iyi şekilde değerlendirmeniz için dengeli bir karışım.",
               places: _optimizeRoute(mixPlaces),
               color: const Color(0xFF009688), // Teal
               icon: Icons.directions_walk_rounded,
               tags: ["mix", "walking"],
               interests: ["walking"],
             ));
         }
      }
      attempt++;
    }

    // TÜM ROTALARI BİRLEŞTİR VE GÖRSEL KONTROLÜ YAP (HARDCODED DAHİL)
    final allRoutesResult = [...existingRoutes, ...generatedRoutes];
    final enrichedRoutes = <CuratedRoute>[];

    // Mekanları hızlı bulmak için Map yapısı
    final highlightsMap = {for (var h in allHighlights) h.name: h};

    for (var route in allRoutesResult) {
      // Eğer görseli varsa ve geçerli bir URL ise dokunma
      bool hasValidImage = route.imageUrl.isNotEmpty && 
                           !route.imageUrl.contains("placeholder") &&
                           route.imageUrl.startsWith("http");

      if (hasValidImage) {
        enrichedRoutes.add(route);
        continue;
      }

      // Görsel yoksa veya geçersizse, rota içindeki mekanlardan bul
      String newImage = route.imageUrl;
      
      // 1. Önce tam eşleşme ara
      if (newImage.isEmpty || !newImage.startsWith("http")) {
        for (var placeName in route.placeNames) {
          final highlight = highlightsMap[placeName];
          if (highlight != null && 
              highlight.imageUrl != null && 
              highlight.imageUrl!.isNotEmpty &&
              highlight.imageUrl!.startsWith("http")) {
            newImage = highlight.imageUrl!;
            break;
          }
        }
      }

      // 2. Hala görsel yoksa, gevşek eşleşme (contains) ara
      if (newImage.isEmpty || !newImage.startsWith("http")) {
         for (var placeName in route.placeNames) {
            // Mekan ismini normalize et
            final normalizedPlace = placeName.toLowerCase().trim();
            
            // Tüm highlight'ları tara
            try {
              final bestMatch = allHighlights.firstWhere((h) => 
                h.imageUrl != null && 
                h.imageUrl!.startsWith("http") &&
                (h.name.toLowerCase().contains(normalizedPlace) || normalizedPlace.contains(h.name.toLowerCase()))
              );
              newImage = bestMatch.imageUrl!;
              break;
            } catch (e) {
              // Eşleşme yoksa devam et
            }
         }
      }

      // Rotayı güncelle (CuratedRoute immutable olduğu için yeni instance oluştur)
      if (newImage != route.imageUrl) {
         enrichedRoutes.add(CuratedRoute(
            id: route.id,
            name: route.name,
            description: route.description,
            duration: route.duration,
            distance: route.distance,
            difficulty: route.difficulty,
            imageUrl: newImage, // Güncellenmiş görsel
            tags: route.tags,
            placeNames: route.placeNames,
            interests: route.interests,
            accentColor: route.accentColor,
            icon: route.icon,
         ));
      } else {
        enrichedRoutes.add(route);
      }
    }

    return enrichedRoutes;
  }

  // Yardımcı: CuratedRoute oluştur
  static CuratedRoute _createRoute({
    required String id,
    required String name,
    required String description,
    required List<Highlight> places,
    required Color color,
    required IconData icon,
    required List<String> tags,
    required List<String> interests,
  }) {
    double totalDist = 0;
    for (int i = 0; i < places.length - 1; i++) {
      totalDist += _calculateDistance(
        places[i].lat, places[i].lng, 
        places[i+1].lat, places[i+1].lng
      );
    }
    
    // Yürüme hızı ~4km/h + her durakta 45dk
    final totalHours = (totalDist / 4) + (places.length * 0.75);

    // İlk geçerli görseli bul
    String bestImage = "";
    for (var place in places) {
      if (place.imageUrl != null && place.imageUrl!.isNotEmpty) {
        bestImage = place.imageUrl!;
        break;
      }
    }
    
    return CuratedRoute(
      id: id,
      name: name,
      description: description,
      duration: "${totalHours.toStringAsFixed(1)} h",
      distance: "${totalDist.toStringAsFixed(1)} km",
      difficulty: totalDist > 5 ? "Medium" : "Easy",
      imageUrl: bestImage, // İlk bulunan geçerli görseli kullan
      tags: tags,
      placeNames: places.map((h) => h.name).toList(),
      interests: interests,
      accentColor: color,
      icon: icon,
    );
  }

  // Yardımcı: Basit TSP (Nearest Neighbor) ile sırala
  static List<Highlight> _optimizeRoute(List<Highlight> places) {
    if (places.isEmpty) return [];
    
    final sorted = <Highlight>[places.first];
    final remaining = List<Highlight>.from(places.skip(1));
    
    while (remaining.isNotEmpty) {
      final current = sorted.last;
      Highlight? nearest;
      double minDist = double.infinity;
      
      for (var p in remaining) {
        final d = _calculateDistance(current.lat, current.lng, p.lat, p.lng);
        if (d < minDist) {
          minDist = d;
          nearest = p;
        }
      }
      
      if (nearest != null) {
        sorted.add(nearest);
        remaining.remove(nearest);
      } else {
        break;
      }
    }
    return sorted;
  }

  // Haversine
  static double _calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    const p = 0.017453292519943295;
    final a = 0.5 - cos((lat2 - lat1) * p)/2 + 
              cos(lat1 * p) * cos(lat2 * p) * 
              (1 - cos((lon2 - lon1) * p))/2;
    return 12742 * asin(sqrt(a));
  }

  // Belirli bir anchor noktasına yakın olan highlight'ları filtrele
  static List<Highlight> _getNearbyHighlights(Highlight anchor, List<Highlight> all, double radiusKM) {
    return all.where((h) {
      final dist = _calculateDistance(anchor.lat, anchor.lng, h.lat, h.lng);
      return dist <= radiusKM; // Yarıçap içindekiler
    }).toList();
  }

  static List<CuratedRoute> getRoutes(String city, bool isEnglish) {
    final normalizedCity = city.toLowerCase().trim();
    
    switch (normalizedCity) {
      case 'istanbul':
      case 'İstanbul':
        return _getIstanbulRoutes(isEnglish);
      case 'barcelona':
        return _getBarcelonaRoutes(isEnglish);
      case 'paris':
        return _getParisRoutes(isEnglish);
      case 'roma':
      case 'rome':
        return _getRomeRoutes(isEnglish);
      case 'londra':
      case 'london':
        return _getLondonRoutes(isEnglish);
      case 'berlin':
        return _getBerlinRoutes(isEnglish);
      case 'amsterdam':
        return _getAmsterdamRoutes(isEnglish);
      case 'new york':
      case 'nyc':
        return _getNewYorkRoutes(isEnglish);
      case 'tokyo':
        return _getTokyoRoutes(isEnglish);
      case 'sevilla':
      case 'seville':
        return _getSevillaRoutes(isEnglish);
      case 'madrid':
        return _getMadridRoutes(isEnglish);
      case 'lizbon':
      case 'lisbon':
        return _getLisbonRoutes(isEnglish);
      case 'porto':
        return _getPortoRoutes(isEnglish);
      case 'napoli':
      case 'naples':
        return _getNaplesRoutes(isEnglish);
      case 'milano':
      case 'milan':
        return _getMilanRoutes(isEnglish);
      case 'venedik':
      case 'venice':
        return _getVeniceRoutes(isEnglish);
      case 'floransa':
      case 'florence':
        return _getFlorenceRoutes(isEnglish);
      case 'atina':
      case 'athens':
        return _getAthensRoutes(isEnglish);
      case 'viyana':
      case 'vienna':
        return _getViennaRoutes(isEnglish);
      case 'prag':
      case 'prague':
        return _getPragueRoutes(isEnglish);
      case 'budapeste':
      case 'budapest':
        return _getBudapestRoutes(isEnglish);
      case 'zurih':
      case 'zurich':
        return _getZurichRoutes(isEnglish);
      case 'cenevre':
      case 'geneva':
        return _getGenevaRoutes(isEnglish);
      case 'lucerne':
        return _getLucerneRoutes(isEnglish);
      case 'kopenhag':
      case 'copenhagen':
        return _getCopenhagenRoutes(isEnglish);
      case 'stockholm':
        return _getStockholmRoutes(isEnglish);
      case 'dubai':
        return _getDubaiRoutes(isEnglish);
      case 'marakes':
      case 'marrakech':
        return _getMarrakechRoutes(isEnglish);
      case 'bangkok':
        return _getBangkokRoutes(isEnglish);
      case 'hongkong':
        return _getHongKongRoutes(isEnglish);
      case 'singapur':
      case 'singapore':
        return _getSingaporeRoutes(isEnglish);
      case 'seul':
      case 'seoul':
        return _getSeoulRoutes(isEnglish);
      case 'nice':
        return _getNiceRoutes(isEnglish);
      case 'lyon':
        return _getLyonRoutes(isEnglish);
      case 'marsilya':
      case 'marseille':
        return _getMarseilleRoutes(isEnglish);
      case 'dublin':
        return _getDublinRoutes(isEnglish);
      case 'antalya':
        return _getAntalyaRoutes(isEnglish);
      case 'gaziantep':
        return _getGaziantepRoutes(isEnglish);
      case 'kapadokya':
      case 'cappadocia':
        return _getCappadociaRoutes(isEnglish);
      case 'midilli':
      case 'lesbos':
      case 'lesvos':
        return _getLesbosRoutes(isEnglish);
      case 'belgrad':
      case 'belgrade':
        return _getBelgradeRoutes(isEnglish);
      case 'bologna':
        return _getBolognaRoutes(isEnglish);
      case 'brugge':
      case 'bruges':
        return _getBrugesRoutes(isEnglish);
      case 'bruksel':
      case 'brussels':
        return _getBrusselsRoutes(isEnglish);
      case 'colmar':
        return _getColmarRoutes(isEnglish);
      case 'edinburgh':
        return _getEdinburghRoutes(isEnglish);
      case 'giethoorn':
        return _getGiethoornRoutes(isEnglish);
      case 'hallstatt':
        return _getHallstattRoutes(isEnglish);
      case 'heidelberg':
        return _getHeidelbergRoutes(isEnglish);
      case 'kotor':
        return _getKotorRoutes(isEnglish);
      case 'matera':
        return _getMateraRoutes(isEnglish);
      case 'oslo':
        return _getOsloRoutes(isEnglish);
      case 'rovaniemi':
        return _getRovaniemiRoutes(isEnglish);
      case 'san sebastian':
      case 'sansebastian':
      case 'donostia':
        return _getSanSebastianRoutes(isEnglish);
      case 'santorini':
        return _getSantoriniRoutes(isEnglish);
      case 'saraybosna':
      case 'sarajevo':
        return _getSarajevoRoutes(isEnglish);
      case 'sintra':
        return _getSintraRoutes(isEnglish);
      case 'strazburg':
      case 'strasbourg':
        return _getStrasbourgRoutes(isEnglish);
      case 'tromso':
      case 'tromsø':
        return _getTromsoRoutes(isEnglish);
      case 'zermatt':
        return _getZermattRoutes(isEnglish);
      default:
        return _getGenericRoutes(city, isEnglish);
    }
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // İSTANBUL ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getIstanbulRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ist_historic",
        name: isEnglish ? "Historic Peninsula Heritage" : "Tarihi Yarımada Mirası",
        description: isEnglish 
          ? "Explore the heart of the empires: Hagia Sophia, Blue Mosque, Topkapi Palace and the deep cisterns"
          : "İmparatorlukların kalbini keşfedin: Ayasofya, Sultanahmet, Topkapı ve derin sarnıçlar.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_33_bf6a6e64da0e.jpg",
        tags: [isEnglish ? "Historical" : "Tarihi", isEnglish ? "Must See" : "Görülmeli", "UNESCO"],
        placeNames: ["Ayasofya", "Sultanahmet Camii", "Yerebatan Sarnıcı", "Topkapı Sarayı", "Kapalıçarşı", "Mısır Çarşısı", "Süleymaniye Camii"],
        interests: ["Tarih", "Mimari", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "ist_bosphorus",
        name: isEnglish ? "Bosphorus & Palaces" : "Boğaz & Saraylar Keyfi",
        description: isEnglish
          ? "Magnificent palaces and seaside charms from Dolmabahçe to the Rumeli Fortress"
          : "Dolmabahçe'den Rumeli Hisarı'na muhteşem saraylar ve deniz kenarı durakları.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_88_4976cb0e6db1.jpg",
        tags: [isEnglish ? "Bosphorus" : "Boğaz", isEnglish ? "Palace" : "Saray", "Scenic"],
        placeNames: ["Boğaz Turu", "Dolmabahçe Sarayı", "Ortaköy", "Bebek", "Galata Kulesi", "Rumeli Hisarı"],
        interests: ["Tarih", "Fotoğraf", "Manzara"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.directions_boat,
      ),
      CuratedRoute(
        id: "ist_kadikoy",
        name: isEnglish ? "Kadıköy Local Spirit" : "Kadıköy Lokal Hayat",
        description: isEnglish 
          ? "Taste the Asian side: Markets, vintage streets, record stores and the best local food"
          : "Asya yakasının tadına bakın: Pazarlar, vintage sokaklar, plakçılar ve en iyi yerel yemekler.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_99_f6cd10d3d204.jpg",
        tags: [isEnglish ? "Asian Side" : "Anadolu Yakası", "Lifestyle", isEnglish ? "Food" : "Yemek"],
        placeNames: ["Kadıköy", "Moda", "Çiya Sofrası", "Akmar Pasajı", "Haydarpaşa Garı", "Tellalzade Sokak"],
        interests: ["Yemek", "Lokal", "Alışveriş"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.storefront,
      ),
      CuratedRoute(
        id: "ist_food",
        name: isEnglish ? "Eternal Street Flavors" : "Sokak Lezzetleri Turu",
        description: isEnglish 
          ? "From syrupy desserts to iconic kebabs and historical bazaar bites"
          : "Şerbetli tatlılardan ikonik kebaplara ve tarihi çarşı atıştırmalıklarına.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "5.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_26_1e38c772cbf3.jpg",
        tags: [isEnglish ? "Food" : "Yemek", isEnglish ? "Street Food" : "Sokak", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Mısır Çarşısı", "Kapalıçarşı", "Karaköy Güllüoğlu", "Hafız Mustafa 1864", "Tarihi Sultanahmet Köftecisi", "Şehzade Cağ Kebap"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "ist_art",
        name: isEnglish ? "Modern Art & Haliç" : "Modern Sanat Rotası",
        description: isEnglish 
          ? "Contemporary Istanbul: World-class museums and the colorful streets of Balat"
          : "Modern İstanbul: Dünya sınıfı müzeler ve Balat'ın renkli sokakları.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "5.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_46_aed14e46560e.jpg",
        tags: [isEnglish ? "Art" : "Sanat", isEnglish ? "Modern" : "Modern", isEnglish ? "Gallery" : "Galeri"],
        placeNames: ["İstanbul Modern", "Galata Kulesi", "Balat", "SALT Galata", "Pera Müzesi", "Tersane İstanbul"],
        interests: ["Sanat", "Kültür"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "ist_night",
        name: isEnglish ? "Beyoğlu Night Pulse" : "Beyoğlu Gece Hayatı",
        description: isEnglish 
          ? "From high-end fine dining to legendary taverns and live music clubs"
          : "Şık restoranlardan efsanevi meyhanelere ve canlı müzik kulüplerine.",
        duration: isEnglish ? "Whole night" : "Tüm gece",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_90_fd58ffaa0f77.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Bars" : "Barlar", "Meyhane"],
        placeNames: ["İstiklal Caddesi", "Galata Kulesi", "Mikla", "Asmalı Cavit", "Babylon", "Nevizade Sokak"],
        interests: ["Gece Hayatı", "Yemek"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "ist_markets",
        name: isEnglish ? "Bazaars & Artisans" : "Çarşılar & Baharatlar",
        description: isEnglish 
          ? "Uncover hidden gems in the world's most ancient shopping arcades"
          : "Dünyanın en eski alışveriş pasajlarındaki gizli hazineleri keşfedin.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_31_47705dd9899e.jpg",
        tags: [isEnglish ? "Shopping" : "Alışveriş", isEnglish ? "Traditional" : "Geleneksel", isEnglish ? "Spices" : "Baharat"],
        placeNames: ["Kapalıçarşı", "Mısır Çarşısı", "Hafız Mustafa 1864", "Arasta Çarşısı", "Mahmutpaşa", "Sahaflar Çarşısı"],
        interests: ["Alışveriş", "Kültür"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.shopping_bag,
      ),
      CuratedRoute(
        id: "ist_princes",
        name: isEnglish ? "Princes' Islands Escape" : "Adalar Kaçamağı",
        description: isEnglish 
          ? "No cars, just bikes and horses: A peaceful retreat in Büyükada and Heybeliada"
          : "Araba yok, sadece bisiklet ve huzur: Büyükada ve Heybeliada'da bir gün.",
        duration: isEnglish ? "Whole day" : "Tam gün",
        distance: "15 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_72_a487746e2470.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", isEnglish ? "Bike" : "Bisiklet", isEnglish ? "Escape" : "Kaçış"],
        placeNames: ["Kabataş İskelesi", "Büyükada", "Aya Yorgi Kilisesi", "Büyükada Marina", "Heybeliada", "Dilburnu Tabiat Parkı"],
        interests: ["Doğa", "Bisiklet", "Romantik"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.pedal_bike,
      ),
      CuratedRoute(
        id: "ist_coffee",
        name: isEnglish ? "Specialty Coffee Hunt" : "Kahve Avcılığı",
        description: isEnglish 
          ? "Third-wave beans and cool aesthetic cafes in the trendiest neighborhoods"
          : "Şehrin en havalı mahallelerinde nitelikli kahve ve üçüncü dalga kafeler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_10_85b2a283408c.jpg",
        tags: [isEnglish ? "Coffee" : "Kahve", "Hipster", isEnglish ? "Chill" : "Sakin"],
        placeNames: ["Petra Roasting", "Kronotrop", "Coffee Sapiens", "MOC", "Mandabatmaz", "Federal Coffee"],
        interests: ["Kahve", "Lokal"],
        accentColor: const Color(0xFF795548),
        icon: Icons.coffee,
      ),
      CuratedRoute(
        id: "ist_sunset",
        name: isEnglish ? "Golden Hour Views" : "Gün Batımı Noktaları",
        description: isEnglish 
          ? "The most photogenic sunset spots over the Bosphorus and Golden Horn"
          : "Boğaz ve Haliç üzerinde en fotojenik gün batımı noktaları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "15 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_93_4dc9ba4b368e.jpg",
        tags: [isEnglish ? "Sunset" : "Gün Batımı", isEnglish ? "Photo" : "Fotoğraf", isEnglish ? "Romantic" : "Romantik"],
        placeNames: ["Üsküdar Salacak", "Galata Kulesi", "Pierre Loti", "Süleymaniye", "Maidens Tower (Kız Kulesi)", "Sanatkarlar Parkı"],
        interests: ["Fotoğraf", "Romantik", "Manzara"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.wb_twilight,
      ),
    ];
  }

  // Placeholder for other cities - will be added
  static List<CuratedRoute> _getBarcelonaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bcn_gothic",
        name: isEnglish ? "Gothic Quarter & Born Maze" : "Gotik & Born Labirenti",
        description: isEnglish 
          ? "Uncover the medieval heart of Barcelona: Roman ruins, hidden squares and the majestic Cathedral"
          : "Barcelona'nın ortaçağ kalbini keşfedin: Roma kalıntıları, gizli meydanlar ve görkemli Katedral.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_89_4e20eb109d8a.jpg",
        tags: [isEnglish ? "Historical" : "Tarihi", isEnglish ? "Medieval" : "Ortaçağ", isEnglish ? "Walking" : "Yürüyüş"],
        placeNames: ["Gothic Quarter", "Plaça Reial", "Las Ramblas", "El Born", "Museu Picasso", "Santa Caterina Market"],
        interests: ["Tarih", "Kültür", "Fotoğraf"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "bcn_gaudi",
        name: isEnglish ? "Gaudí's Imaginative Path" : "Gaudí'nin Hayal Rotası",
        description: isEnglish 
          ? "A deep dive into Modernism: From the unfinished Sagrada Familia to the whimsical Park Güell"
          : "Modernizmin derinliklerine yolculuk: Bitmeyen Sagrada Familia'dan masalsı Park Güell'e.",
        duration: isEnglish ? "Whole day" : "Tam gün",
        distance: "10 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_6_0eb6a2602df8.jpg",
        tags: ["Gaudí", isEnglish ? "Architecture" : "Mimari", "UNESCO"],
        placeNames: ["Sagrada Familia", "Casa Batlló", "Casa Milà (La Pedrera)", "Park Güell", "Casa Vicens"],
        interests: ["Sanat", "Mimari", "Fotoğraf"],
        accentColor: const Color(0xFF9C27B0),
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "bcn_beach",
        name: isEnglish ? "Sea & Salt Breezes" : "Deniz & Tuz Kokusu",
        description: isEnglish 
          ? "From the old fisherman's quarter to the modern Olympic port: Beach life and maritime soul"
          : "Eski balıkçı mahallesinden modern Olimpiyat limanına: Plaj hayatı ve deniz ruhu.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_96_45f890a38613.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", "Paella", isEnglish ? "Coastal" : "Sahil"],
        placeNames: ["Barceloneta Beach", "Barceloneta Mahallesi", "Parc de la Ciutadella", "Poblenou"],
        interests: ["Plaj", "Yemek", "Romantik"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.beach_access,
      ),
      CuratedRoute(
        id: "bcn_born",
        name: isEnglish ? "El Born Chic & Culture" : "El Born Şıklığı & Kültür",
        description: isEnglish 
          ? "Hip boutiques, world-class art at Picasso Museum and the best mixology bars"
          : "Hip butikler, Picasso Müzesi'nde dünya sınıfı sanat ve en iyi kokteyl barları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_69_68b54418ba32.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Tapas", isEnglish ? "Lifestyle" : "Yaşam Tarzı"],
        placeNames: ["Museu Picasso", "El Born", "Santa Caterina Market", "Palau de la Música Catalana"],
        interests: ["Sanat", "Yemek", "Gece Hayatı"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "bcn_gracia",
        name: isEnglish ? "Gracia Village Vibes" : "Gracia Köy Havası",
        description: isEnglish
          ? "Local squares, indie shops and vermouth culture"
          : "Yerel meydanlar, bağımsız dükkanlar ve vermut kültürü.",
        duration: isEnglish ? "3-4 hours" : "3-4 saat",
        distance: "2.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_21_4ef501140861.jpg",
        tags: ["Lokal", isEnglish ? "Bohemian" : "Bohem", "Vermut"],
        placeNames: ["Gràcia", "Park Güell", "Casa Vicens"],
        interests: ["Lokal", "Yemek", "Alışveriş"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.local_cafe,
      ),
      CuratedRoute(
        id: "bcn_food",
        name: isEnglish ? "Tapas & Market Trail" : "Tapas & Pazar Turu",
        description: isEnglish 
          ? "A culinary journey through world-famous markets and hidden tapas gems"
          : "Dünyaca ünlü pazarlardan gizli tapas duraklarına lezzet dolu bir yolculuk.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_17_a0f723a5473f.jpg",
        tags: ["Pintxos", "Tapas", isEnglish ? "Market" : "Pazar"],
        placeNames: ["La Boqueria", "Santa Caterina Market", "El Born", "El Raval", "Gràcia"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "bcn_montjuic",
        name: isEnglish ? "Montjuïc Heights" : "Montjuïc Tepeleri",
        description: isEnglish 
          ? "Panoramic views, historic fortress and the Magic Fountain's dance"
          : "Panoramik manzaralar, tarihi kale ve Sihirli Çeşme'nin dansı.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "7 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_55_900090f84888.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "History" : "Tarih", isEnglish ? "Show" : "Gösteri"],
        placeNames: ["Montjuïc", "MNAC", "Fundació Joan Miró", "Magic Fountain of Montjuïc"],
        interests: ["Doğa", "Manzara", "Sanat"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "bcn_raval",
        name: isEnglish ? "Raval Street Spirit" : "Raval Sokak Ruhu",
        description: isEnglish 
          ? "Edgy art, skater vibes and hidden gems in the city's most diverse district"
          : "Sıradışı sanat, kaykaycı ruhu ve şehrin en kozmopolit semtindeki gizli hazineler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_78_0a29a942fe24.jpg",
        tags: [isEnglish ? "Street Art" : "Sokak Sanatı", "Alternative", "Hipster"],
        placeNames: ["MACBA", "El Raval", "Las Ramblas"],
        interests: ["Sanat", "Alışveriş"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.brush,
      ),
      CuratedRoute(
        id: "bcn_romantic",
        name: isEnglish ? "Romantic Fairytale" : "Romantik Masal",
        description: isEnglish 
          ? "Candlelit gardens, panoramic sunrises and the city's most enchanting spots"
          : "Mum ışığında bahçeler, panoramik güneş batışları ve şehrin en tılsımlı noktaları.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_8_158db484b4fc.jpg",
        tags: [isEnglish ? "Romantic" : "Romantik", isEnglish ? "Fairytale" : "Masalsı", isEnglish ? "Sunset" : "Günbatımı"],
        placeNames: ["Bunkers del Carmel", "Tibidabo", "Parc del Laberint d'Horta", "Parc de la Ciutadella", "Magic Fountain of Montjuïc"],
        interests: ["Romantik", "Yemek"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.favorite,
      ),
      CuratedRoute(
        id: "bcn_eixample",
        name: isEnglish ? "Eixample Grandeur" : "Eixample Görkemi",
        description: isEnglish 
          ? "Magnificent modernist block, high-end fashion and art nouveau gems"
          : "Görkemli modernist yapılar, lüks moda ve art nouveau hazineleri.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_11_80274a290974.jpg",
        tags: [isEnglish ? "Architecture" : "Mimari", isEnglish ? "Shopping" : "Alışveriş", isEnglish ? "Arty" : "Sanatsal"],
        placeNames: ["Casa Batlló", "Casa Milà (La Pedrera)", "Sant Pau Recinte Modernista"],
        interests: ["Mimari", "Alışveriş", "Kahve"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.apartment,
      ),
    ];
  }
  static List<CuratedRoute> _getParisRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "par_classic",
        name: isEnglish ? "Parisian Landmarks" : "Paris İkonları",
        description: isEnglish 
          ? "The essential Paris experience: From the Eiffel Tower to the historic Arc de Triomphe"
          : "Temel Paris deneyimi: Eyfel Kulesi'nden tarihi Zafer Takı'na kadar en ikonik duraklar.",
        duration: isEnglish ? "6-7 hours" : "6-7 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_67_ead25968001b.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Eiffel", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Eyfel Kulesi", "Trocadéro", "Arc de Triomphe", "Champs-Élysées", "Place de la Concorde", "Musée d'Orsay"],
        interests: ["Tarih", "Fotoğraf", "Turist"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "par_montmartre",
        name: isEnglish ? "Montmartre's Artistic Soul" : "Montmartre'ın Sanat Ruhu",
        description: isEnglish 
          ? "Step into the bohemian village of Paris: Artist squares, hidden vineyards and the white basilica"
          : "Paris'in bohem köyüne adım atın: Sanatçı meydanları, gizli üzüm bağları ve beyaz bazilika.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_48_cbaa1b6dec35.jpg",
        tags: [isEnglish ? "Art" : "Sanat", isEnglish ? "Village" : "Köy", "Sacré-Cœur"],
        placeNames: ["Montmartre", "Sacré-Cœur Bazilikası", "Place du Tertre", "Moulin Rouge", "Mur des Je t'aime", "Musée de Montmartre"],
        interests: ["Sanat", "Fotoğraf", "Romantik"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "par_marais",
        name: isEnglish ? "Le Marais Merchant History" : "Le Marais Tüccar Tarihi",
        description: isEnglish 
          ? "Uncover the coolest neighborhood: 17th-century mansions, historic Jewish quarter and trendy boutiques"
          : "En havalı mahalleyi keşfedin: 17. yüzyıl konakları, tarihi Yahudi mahallesi ve trendy butikler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/paris/le_marais.jpg",
        tags: ["Marais", "Falafel", isEnglish ? "Trendy" : "Trendy"],
        placeNames: ["Le Marais", "Place des Vosges", "Rue des Rosiers", "Museé Carnavalet", "Saint-Paul-Saint-Louis", "L'As du Fallafel"],
        interests: ["Yemek", "Alışveriş", "Lokal"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.storefront,
      ),
      CuratedRoute(
        id: "par_museums",
        name: isEnglish ? "Art Immersion Marathon" : "Sanat Maratonu",
        description: isEnglish 
          ? "A journey through art history: Royal palaces, Impressionist masterpieces and modern wonders"
          : "Sanat tarihinde bir yolculuk: Kraliyet sarayları, Empresyonist başyapıtlar ve modern harikalar.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "7 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_0_07607c15f585.jpg",
        tags: [isEnglish ? "Museums" : "Müzeler", "Louvre", "Art"],
        placeNames: ["Louvre Müzesi", "Musée d'Orsay", "Musée de l'Orangerie", "Centre Pompidou", "Musée Rodin", "Palais Royal"],
        interests: ["Sanat", "Kültür", "Tarih"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "par_food",
        name: isEnglish ? "Gourmet Paris Trail" : "Gurme Paris Rotası",
        description: isEnglish 
          ? "Indulge in the finest flavours: Crusty baguettes, aged cheeses and world-class patisseries"
          : "En iyi lezzetlerin tadını çıkarın: Çıtır bagetler, yıllanmış peynirler ve dünya çapında pastaneler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_51_be1a058d1665.jpg",
        tags: [isEnglish ? "Gastronomy" : "Gastronomi", "Coffee", isEnglish ? "Market" : "Pazar"],
        placeNames: ["Marché d'Aligre", "Rue Cler", "Saint-Germain-des-Prés", "Café de Flore", "Canal Saint-Martin", "Belleville"],
        interests: ["Yemek", "Kahve"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.bakery_dining,
      ),
      CuratedRoute(
        id: "par_seine",
        name: isEnglish ? "Islands & River Secrets" : "Adalar & Nehir Sırları",
        description: isEnglish 
          ? "Wander through the birthplace of Paris: From the Gothic spires of Notre-Dame to romantic riverbanks"
          : "Paris'in doğduğu topraklarda gezinin: Notre-Dame'ın Gotik kulelerinden romantik nehir kıyılarına.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_60_5399dbd91a5e.jpg",
        tags: ["Seine", isEnglish ? "Picnic" : "Piknik", isEnglish ? "Islands" : "Adalar"],
        placeNames: ["Notre-Dame Katedrali", "Sainte-Chapelle", "Pont Neuf", "Pont Alexandre III", "Shakespeare and Company", "Île de la Cité"],
        interests: ["Romantik", "Doğa", "Fotoğraf"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.water,
      ),
      CuratedRoute(
        id: "par_latin",
        name: isEnglish ? "Latin Quarter Scholarly Life" : "Latin Mahallesi Öğrenci Hayatı",
        description: isEnglish 
          ? "Explore the intellectual heart: Medieval universities, the Pantheon and charming bookshops"
          : "Entelektüel kalbi keşfedin: Ortaçağ üniversiteleri, Panthéon ve büyüleyici kitapçılar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_65_8b8fe7766b61.jpg",
        tags: [isEnglish ? "Scholarly" : "Akademik", "Sorbonne", isEnglish ? "History" : "Tarih"],
        placeNames: ["Sorbonne", "Panthéon", "Jardin du Luxembourg", "Shakespeare and Company", "Rue Mouffetard", "Latin Quarter"],
        interests: ["Kültür", "Kahve", "Lokal"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.school,
      ),
      CuratedRoute(
        id: "par_night",
        name: isEnglish ? "City of Lights Nocturne" : "Işıklar Şehri Gecesi",
        description: isEnglish 
          ? "Experience Paris as the sun sets: Illuminated monuments, midnight jazz and shimmering river views"
          : "Güneş batarken Paris'i deneyimleyin: Işıklı anıtlar, gece yarısı cazı ve parıldayan nehir manzaraları.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_41_9a6c2a06d853.jpg",
        tags: [isEnglish ? "Night" : "Gece", isEnglish ? "Lights" : "Işıklar", isEnglish ? "Evening" : "Akşam"],
        placeNames: ["Eyfel Kulesi", "Pont Alexandre III", "Moulin Rouge", "Canal Saint-Martin", "Notre-Dame Katedrali", "Arc de Triomphe"],
        interests: ["Romantik", "Gece Hayatı", "Fotoğraf"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlight,
      ),
      CuratedRoute(
        id: "par_versailles",
        name: isEnglish ? "Versailles Royal Escape" : "Versay Kraliyet Kaçamağı",
        description: isEnglish 
          ? "Step into the world of French Kings: Hall of Mirrors, majestic gardens and the Queen's Hamlet"
          : "Fransız Kralları'nın dünyasına adım atın: Aynalı Salon, görkemli bahçeler ve Kraliçe'nin Köyü.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "12 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_70_1e960c1fa6c6.jpg",
        tags: ["Versailles", isEnglish ? "Palace" : "Saray", isEnglish ? "Royal" : "Kraliyet"],
        placeNames: ["Palace of Versailles", "Gardens of Versailles", "Petit Trianon", "Grand Trianon", "Queen's Hamlet", "Hall of Mirrors"],
        interests: ["Tarih", "Kültür", "Doğa"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "par_canal",
        name: isEnglish ? "Canal Saint-Martin & Beyond" : "Canal Saint-Martin ve Ötesi",
        description: isEnglish 
          ? "The soul of hip Paris: Scenic canal walks, independent boutiques, street art and the best brunch spots"
          : "Modern Paris'in ruhu: Manzaralı kanal yürüyüşleri, bağımsız butikler, sokak sanatı ve en iyi brunch mekanları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_94_d0eef0992036.jpg",
        tags: ["Canal", "Hipster", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Canal Saint-Martin", "Belleville", "Buttes-Chaumont Parkı", "Le Marais", "Place de la République", "Bassin de la Villette"],
        interests: ["Kahve", "Lokal", "Fotoğraf"],
        accentColor: const Color(0xFF16A085),
        icon: Icons.local_cafe,
      ),
    ];
  }

  static List<CuratedRoute> _getRomeRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "rom_ancient",
        name: isEnglish ? "Ancient Imperial Wonders" : "Antik İmparatorluk Yolu",
        description: isEnglish 
          ? "Step back in time: The grandeur of the Colosseum, the ruins of the Roman Forum and the Palatine Hill"
          : "Zamanda geriye gidin: Kolezyum'un ihtişamı, Roma Forumu kalıntıları ve Palatin Tepesi.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_28_f9996e9397f7.jpg",
        tags: [isEnglish ? "Ancient" : "Antik", "Colosseum", "UNESCO"],
        // Updated names to match JSON
        placeNames: ["Kolezyum", "Roma Forumu", "Palatino Tepesi (Palatine Hill)", "Altare della Patria (Vittoriano)", "Largo di Torre Argentina", "Baths of Caracalla"],
        interests: ["Tarih", "Kültür", "Fotoğraf"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "rom_vatican",
        name: isEnglish ? "Vatican Masterpieces" : "Vatikan Başyapıtları",
        description: isEnglish 
          ? "The spiritual and artistic heart: From the Vatican Museums to the majestic St. Peter's Basilica"
          : "Ruhani ve sanatsal kalp: Vatikan Müzeleri'nden görkemli San Pietro Bazilikası'na.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_27_e8251a946240.jpg",
        tags: ["Vatican", isEnglish ? "Art" : "Sanat", "Holy"],
        // Updated names to match JSON
        placeNames: ["Vatikan Müzeleri", "St. Peter's Basilica (San Pietro Bazilikası)", "Castel Sant'Angelo", "Borgo", "Villa Farnesina", "Janiculum (Gianicolo)"],
        interests: ["Sanat", "Tarih", "Kültür"],
        accentColor: const Color(0xFF9C27B0),
        icon: Icons.church,
      ),
      CuratedRoute(
        id: "rom_trastevere",
        name: isEnglish ? "Trastevere Bohemian Night" : "Trastevere Bohem Gecesi",
        description: isEnglish 
          ? "Rome's most charming neighborhood: Ivy-clad walls, vibrant plazas and authentic family-run trattorias"
          : "Roma'nın en tılsımlı mahallesi: Sarmaşıklı duvarlar, canlı meydanlar ve otantik aile işletmeleri.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_14_a082a4012e15.jpg",
        tags: ["Trastevere", isEnglish ? "Food" : "Yemek", isEnglish ? "Nightlife" : "Gece Hayatı"],
        // Updated names to match JSON
        placeNames: ["Trastevere", "Basilica di Santa Maria in Trastevere", "Piazza Trilussa", "Da Enzo al 29", "Supplì Roma", "Vicolo del Moro"],
        interests: ["Yemek", "Gece Hayatı", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "rom_food",
        name: isEnglish ? "Gourmet Roman Flavours" : "Roma Gurme Lezzetler",
        description: isEnglish 
          ? "Taste the best of Rome: Authentic carbonara, golden supplì and the freshest market finds"
          : "Roma'nın en iyilerini tadın: Gerçek carbonara, altın supplì ve en taze pazar keşifleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_73_5c8b38dd46bf.jpg",
        tags: ["Carbonara", "Supplì", isEnglish ? "Gourmet" : "Gurme"],
        placeNames: ["Mercato di Testaccio", "Roscioli", "Campo de' Fiori", "Da Enzo al 29", "Mordi e Vai", "Supplì Roma"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFF39C12),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "rom_baroque",
        name: isEnglish ? "Baroque Squares & Fountains" : "Barok Meydanlar & Çeşmeler",
        description: isEnglish 
          ? "Rome's living museum: Masterpieces by Bernini, the Pantheon and the legendary Trevi Fountain"
          : "Roma'nın yaşayan müzesi: Bernini'nin başyapıtları, Pantheon ve efsanevi Trevi Çeşmesi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_13_dd658c7019cb.jpg",
        tags: ["Trevi", isEnglish ? "Baroque" : "Barok", isEnglish ? "Squares" : "Meydanlar"],
        // Updated names to match JSON
        placeNames: ["Trevi Çeşmesi", "Pantheon", "Piazza Navona", "Spanish Steps (İspanyol Merdivenleri)", "Piazza del Popolo", "Piazza Venezia"],
        interests: ["Tarih", "Fotoğraf", "Romantik"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.view_quilt,
      ),
      CuratedRoute(
        id: "rom_gelato",
        name: isEnglish ? "Artisanal Gelato Trail" : "Artizan Dondurma Yolu",
        description: isEnglish 
          ? "A sweet journey through Rome: From the oldest legendary gelaterias to modern experimental flavours"
          : "Roma genelinde tatlı bir yolculuk: En eski efsanevi dondurmacılardan modern deneysel lezzetlere.",
        duration: isEnglish ? "3-4 hours" : "3-4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_66_3cdd57473cb5.jpg",
        tags: ["Gelato", isEnglish ? "Sweet" : "Tatlı", isEnglish ? "Artisanal" : "Artizan"],
        placeNames: ["Giolitti", "Frigidarium", "Fatamorgana", "Gelateria del Teatro", "Old Bridge Gelateria", "Come il Latte"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.icecream,
      ),
      CuratedRoute(
        id: "rom_views",
        name: isEnglish ? "Eternal City Horizons" : "Ebedi Şehir Ufukları",
        description: isEnglish 
          ? "Rome's most stunning panoramas: From secret keyholes to historic hills at sunset"
          : "Roma'nın en etkileyici panoramaları: Gizli anahtar deliklerinden tarihi tepelere gün batımı.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_3_563dd24e0407.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Hills" : "Tepeler", "Sunset"],
        // Updated names to match JSON (USER REPORTED ISSUE FIXED HERE)
        placeNames: ["Knights of Malta Keyhole", "Giardino degli Aranci", "Pincio Tepesi", "Janiculum (Gianicolo)", "Villa Borghese", "Altare della Patria (Vittoriano)"],
        interests: ["Manzara", "Fotoğraf", "Doğa"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "rom_aperitivo",
        name: isEnglish ? "Aperitivo Hour & Views" : "Aperitivo Saati & Manzaralar",
        description: isEnglish 
          ? "Experience the Roman lifestyle: Sunset drinks on the city's best rooftops and historic squares"
          : "Roma yaşam tarzını deneyimleyin: Şehrin en iyi teraslarında ve tarihi meydanlarında gün batımı içecekleri.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_32_fadce2eed52a.jpg",
        tags: ["Aperitivo", isEnglish ? "Rooftop" : "Teras", isEnglish ? "Social" : "Sosyal"],
        placeNames: ["Hotel Raphael Terrace", "Salotto 42", "Etablì", "Terrazza Borromini", "Freni e Frizioni", "Jerry Thomas Speakeasy"],
        interests: ["Gece Hayatı", "Yemek", "Romantik"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.local_bar,
      ),
      CuratedRoute(
        id: "rom_jewish",
        name: isEnglish ? "Jewish Ghetto Heritage" : "Yahudi Mahallesi Mirası",
        description: isEnglish 
          ? "Uncover one of Rome's oldest districts: Historic ruins, profound history and the best artichokes in town"
          : "Roma'nın en eski bölgelerinden birini keşfedin: Tarihi kalıntılar, derin bir geçmiş ve şehirdeki en iyi enginarlar.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_42_2ea9f5fbc3c8.jpg",
        tags: [isEnglish ? "Historical" : "Tarihi", isEnglish ? "Food" : "Yemek", isEnglish ? "Ghetto" : "Ghetto"],
        placeNames: ["Portico d'Ottavia", "Great Synagogue", "Nonna Betta", "Turtle Fountain", "Theatre of Marcellus", "Campo de' Fiori"],
        interests: ["Tarih", "Yemek", "Kültür"],
        accentColor: const Color(0xFF795548),
        icon: Icons.synagogue,
      ),
      CuratedRoute(
        id: "rom_morning",
        name: isEnglish ? "Early Bird's Rome" : "Erken Kuş Roma Turu",
        description: isEnglish 
          ? "Beat the crowds: Discover Rome's most famous monuments in the soft morning light and quiet streets"
          : "Kalabalıklardan korunun: Roma'nın en ünlü anıtlarını yumuşak sabah ışığında ve sessiz sokaklarda keşfedin.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_13_dd658c7019cb.jpg",
        tags: [isEnglish ? "Early" : "Erken", isEnglish ? "Quiet" : "Sakin", isEnglish ? "Iconic" : "İkonik"],
        placeNames: ["Trevi Çeşmesi", "Pantheon", "Piazza Navona", "İspanyol Merdivenleri", "Piazza del Popolo", "Castel Sant'Angelo"],
        interests: ["Fotoğraf", "Turist", "Sakinlik"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.wb_sunny,
      ),
    ];
  }
  static List<CuratedRoute> _getLondonRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "lon_royal",
        name: isEnglish ? "Royal London Walk" : "Kraliyet Londra Turu",
        description: isEnglish ? "Buckingham, Westminster, Big Ben" : "Buckingham Sarayı, Westminster ve Big Ben.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_105_d71f8b45f6c3.jpg",
        tags: [isEnglish ? "Royal" : "Kraliyet", "Big Ben", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Buckingham Palace", "Big Ben & Westminster", "Tower Bridge", "Hyde Park"],
        interests: ["Tarih", "Fotoğraf", "Turist"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "lon_museums",
        name: isEnglish ? "Free Museum Day" : "Ücretsiz Müze Günü",
        description: isEnglish ? "British Museum, Tate, V&A - all free!" : "British Museum, Tate, V&A - hepsi ücretsiz!",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_85_6c84d4c877fd.jpg",
        tags: [isEnglish ? "Museums" : "Müzeler", isEnglish ? "Free" : "Ücretsiz", isEnglish ? "Art" : "Sanat"],
        placeNames: ["British Museum", "Natural History Museum", "V&A Museum", "Tate Modern"],
        interests: ["Sanat", "Tarih", "Kültür"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "lon_eastend",
        name: isEnglish ? "East End Street Art" : "East End Sokak Sanatı",
        description: isEnglish ? "Shoreditch graffiti, Brick Lane curry" : "Shoreditch graffitileri, Brick Lane köri sokağı.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_34_ba96372362cc.jpg",
        tags: [isEnglish ? "Street Art" : "Sokak Sanatı", "Shoreditch", "Curry"],
        placeNames: ["Brick Lane", "Shoreditch", "Borough Market"],
        interests: ["Sanat", "Yemek", "Lokal"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.brush,
      ),
      CuratedRoute(
        id: "lon_southbank",
        name: isEnglish ? "South Bank Culture" : "South Bank Kültür Rotası",
        description: isEnglish ? "Thames walk, Tate, Shakespeare's Globe" : "Thames yürüyüşü, Tate Modern, Shakespeare's Globe.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_29_37cbdc3c13db.jpg",
        tags: ["Thames", "Tate", "Shakespeare"],
        placeNames: ["Tate Modern", "Borough Market", "Tower Bridge", "St. Paul's Cathedral"],
        interests: ["Sanat", "Kültür", "Yemek"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.theater_comedy,
      ),
      CuratedRoute(
        id: "lon_food",
        name: isEnglish ? "Borough & Beyond" : "Borough Market Turu",
        description: isEnglish ? "Best food market and Sunday roast pubs" : "En iyi yemek pazarı ve Pazar rostosu pubları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_95_0c0d4ef9805a.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Borough", isEnglish ? "Pub" : "Pub"],
        placeNames: ["Borough Market", "Maltby Street Market", "The George Inn"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "lon_notting",
        name: isEnglish ? "Notting Hill Colors" : "Notting Hill Renkleri",
        description: isEnglish ? "Pastel houses, Portobello Market" : "Pastel evler, Portobello Pazarı.",
        duration: isEnglish ? "3-4 hours" : "3-4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_58_354d46c47f92.jpg",
        tags: ["Notting Hill", "Portobello", isEnglish ? "Vintage" : "Vintage"],
        placeNames: ["Portobello Road Market", "Notting Hill", "Hyde Park"],
        interests: ["Fotoğraf", "Alışveriş", "Romantik"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.home,
      ),
      CuratedRoute(
        id: "lon_pubs",
        name: isEnglish ? "Historic Pub Crawl" : "Tarihi Pub Turu",
        description: isEnglish ? "Oldest and quirkiest pubs in London" : "Londra'nın en eski ve ilginç pubları.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_12_6bf25c0316f1.jpg",
        tags: ["Pub", isEnglish ? "Historic" : "Tarihi", isEnglish ? "Beer" : "Bira"],
        placeNames: ["Ye Olde Cheshire Cheese", "The Lamb and Flag", "Gordon's Wine Bar"],
        interests: ["Gece Hayatı", "Tarih", "Lokal"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.sports_bar,
      ),
      CuratedRoute(
        id: "lon_parks",
        name: isEnglish ? "Royal Parks Escape" : "Kraliyet Parkları",
        description: isEnglish ? "Hyde Park, Kensington Gardens, picnic spots" : "Hyde Park, Kensington Bahçeleri, piknik noktaları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_36_d2054a672897.jpg",
        tags: [isEnglish ? "Parks" : "Parklar", isEnglish ? "Nature" : "Doğa", isEnglish ? "Picnic" : "Piknik"],
        placeNames: ["Hyde Park", "Notting Hill", "Regent's Park"],
        interests: ["Doğa", "Romantik", "Bisiklet"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "lon_views",
        name: isEnglish ? "Free Viewpoints" : "Ücretsiz Manzara Noktaları",
        description: isEnglish ? "Sky Garden, Tate roof, Primrose Hill" : "Sky Garden, Tate çatısı, Primrose Hill.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "Varies",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_45_7ad5e80a64fa.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Free" : "Ücretsiz", isEnglish ? "Photo" : "Fotoğraf"],
        placeNames: ["Sky Garden", "Tate Modern", "Tower Bridge"],
        interests: ["Manzara", "Fotoğraf"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "lon_camden",
        name: isEnglish ? "Camden Alternative" : "Camden Alternatif Rota",
        description: isEnglish ? "Markets, music venues and canal walks" : "Pazarlar, müzik mekanları ve kanal yürüyüşü.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_50_babdfe64744f.jpg",
        tags: ["Camden", isEnglish ? "Music" : "Müzik", isEnglish ? "Markets" : "Pazarlar"],
        placeNames: ["Camden Market", "Shoreditch", "Brick Lane"],
        interests: ["Alışveriş", "Lokal", "Müzik"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.music_note,
      ),
    ];
  }

  static List<CuratedRoute> _getBerlinRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ber_history",
        name: isEnglish ? "Cold War Berlin" : "Soğuk Savaş Berlini",
        description: isEnglish ? "Wall, Checkpoint Charlie, Topography of Terror and more history" : "Duvar, Checkpoint Charlie, Terör Topografyası ve daha fazlası.",
        duration: isEnglish ? "6-7 hours" : "6-7 saat",
        distance: "6.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/berlin_duvari_aniti.jpg",
        tags: [isEnglish ? "History" : "Tarih", isEnglish ? "Wall" : "Duvar", "Cold War"],
        placeNames: ["Berlin Duvarı Anıtı", "Checkpoint Charlie", "Topography of Terror", "Tränenpalast", "Holokost Anıtı", "Potsdamer Platz", "DDR Museum"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF795548),
        icon: Icons.history,
      ),
      CuratedRoute(
        id: "ber_kreuzberg",
        name: isEnglish ? "Kreuzberg Local Life" : "Kreuzberg Lokal Hayat",
        description: isEnglish ? "Best döner, canal vibes, parks and street art" : "En iyi döner, kanal kenarı, parklar ve sokak sanatı.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_64_937fe82a24bb.jpg",
        tags: ["Kreuzberg", "Döner", isEnglish ? "Canal" : "Kanal"],
        placeNames: ["Türkischer Markt", "Markthalle Neun", "Badeschiff", "Victoriapark", "Görlitzer Park", "Oberbaumbrücke", "Curry 36"],
        interests: ["Yemek", "Lokal", "Sanat"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.storefront,
      ),
      CuratedRoute(
        id: "ber_museums",
        name: isEnglish ? "Museum Island" : "Müze Adası",
        description: isEnglish ? "5 world-class museums on one historic island" : "Tek adada 5 dünya sınıfı müze.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "2.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/muze_adasi.jpg",
        tags: [isEnglish ? "Museums" : "Müzeler", "UNESCO", isEnglish ? "Art" : "Sanat"],
        placeNames: ["Müze Adası", "Neues Museum", "Berliner Dom", "Altes Museum", "Bode Müzesi", "Pergamon Müzesi", "James Simon Galeri"],
        interests: ["Sanat", "Tarih", "Kültür"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "ber_food",
        name: isEnglish ? "Döner & Currywurst Trail" : "Döner & Currywurst Turu",
        description: isEnglish ? "Berlin's most iconic street food spots and old imbiss joints" : "Berlin'in en ikonik sokak lezzetleri ve eski büfeleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "7 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/mustafas_gemuse_kebap.jpg",
        tags: ["Döner", "Currywurst", isEnglish ? "Street Food" : "Sokak"],
        placeNames: ["Mustafa's Gemüse Kebap", "Curry 36", "Burgermeister", "Markthalle Neun", "Konnopke's Imbiss", "Risa Chicken"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "ber_nightlife",
        name: isEnglish ? "Club Scene Intro" : "Gece Hayatı Girişi",
        description: isEnglish ? "From industrial rooftop bars to the world's most legendary clubs" : "Endüstriyel teras barlardan dünyanın en efsanevi kulüplerine.",
        duration: isEnglish ? "Evening/Night" : "Akşam/Gece",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/raw_gelande.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", "Techno", isEnglish ? "Clubs" : "Kulüpler"],
        placeNames: ["RAW-Gelände", "Urban Spree", "Berghain", "Watergate", "Tresor", "Wilden Renate", "Kater Blau"],
        interests: ["Gece Hayatı", "Müzik"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "ber_tempelhof",
        name: isEnglish ? "Tempelhof Freedom" : "Tempelhof Özgürlüğü",
        description: isEnglish ? "Skate on runways of abandoned airport and explore local kiez life" : "Terk edilmiş havalimanı pistinde bisiklet ve mahalle hayatı.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/tempelhof_park.jpg",
        tags: ["Tempelhof", isEnglish ? "Bike" : "Bisiklet", isEnglish ? "Unique" : "Benzersiz"],
        placeNames: ["Tempelhof Park", "Schillerkiez", "Klunkerkranich", "Körnerpark", "Hasenheide", "Bergmannkiez"],
        interests: ["Doğa", "Bisiklet", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.pedal_bike,
      ),
      CuratedRoute(
        id: "ber_mauerpark",
        name: isEnglish ? "Sunday at Mauerpark" : "Pazar Günü Mauerpark",
        description: isEnglish ? "Legendary flea market, open-air karaoke and local beer gardens" : "Efsanevi bit pazarı, açık hava karaoke ve lokal bira bahçeleri.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/mauerpark.jpg",
        tags: ["Mauerpark", isEnglish ? "Flea Market" : "Bit Pazarı", "Karaoke"],
        placeNames: ["Mauerpark", "Prenzlauer Berg", "Bernauer Strasse", "Kulturbrauerei", "Arkonaplatz Flea Market", "Prater Biergarten"],
        interests: ["Alışveriş", "Lokal", "Müzik"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.mic,
      ),
      CuratedRoute(
        id: "ber_prenzlauer",
        name: isEnglish ? "Prenzlauer Berg Brunch" : "Prenzlauer Berg Kahvaltısı",
        description: isEnglish ? "Chic cafes, vintage shops and beautiful residential streets" : "Şık kafeler, vintage dükkanlar ve güzel konut sokakları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/prenzlauer_berg.jpg",
        tags: ["Brunch", isEnglish ? "Cafes" : "Kafeler", isEnglish ? "Chic" : "Şık"],
        placeNames: ["Prenzlauer Berg", "Mauerpark", "Kollwitzplatz", "Kastanienallee", "Rykestrasse Synagogue", "Helmholtzplatz"],
        interests: ["Kahve", "Lokal"],
        accentColor: const Color(0xFF16A085),
        icon: Icons.brunch_dining,
      ),
      CuratedRoute(
        id: "ber_jewish",
        name: isEnglish ? "Jewish Berlin" : "Yahudi Berlin",
        description: isEnglish ? "Explore the profound history through memorials, museums and the Scheunenviertel" : "Anıtlar, müzeler ve Scheunenviertel üzerinden derin tarihi keşfedin.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/holokost_aniti.jpg",
        tags: [isEnglish ? "Memorial" : "Anıt", isEnglish ? "History" : "Tarih", isEnglish ? "Culture" : "Kültür"],
        placeNames: ["Holokost Anıtı", "Jewish Museum", "Topography of Terror", "New Synagogue", "Otto Weidt's Workshop", "Gleis 17"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.synagogue,
      ),
      CuratedRoute(
        id: "ber_street_art",
        name: isEnglish ? "Street Art Safari" : "Sokak Sanatı Turu",
        description: isEnglish ? "Iconic murals, hidden graffiti alleys and abandoned stations" : "İkonik duvar resimleri, gizli graffiti sokakları ve terk edilmiş istasyonlar.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/berlin/east_side_gallery.jpg",
        tags: [isEnglish ? "Street Art" : "Sokak Sanatı", "Graffiti", isEnglish ? "Urban" : "Kentsel"],
        placeNames: ["East Side Gallery", "RAW Gelände", "Urban Spree", "Haus Schwarzenberg", "Teufelsberg", "Mauerpark Murals"],
        interests: ["Sanat", "Fotoğraf"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.format_paint,
      ),
    ];
  }
  static List<CuratedRoute> _getAmsterdamRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ams_canals",
        name: isEnglish ? "Golden Age Canals" : "Altın Çağ Kanalları",
        description: isEnglish 
          ? "The heart of Amsterdam: UNESCO-protected waterways, historic gabled houses and hidden courtyards"
          : "Amsterdam'ın kalbi: UNESCO korumalı su yolları, tarihi çatı evleri ve gizli avlular.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_56_41f150e87d0c.jpg",
        tags: [isEnglish ? "Canals" : "Kanallar", "UNESCO", isEnglish ? "Scenic" : "Manzaralı"],
        placeNames: ["Kanal Turu", "Dam Meydanı", "Begijnhof", "Anne Frank Evi", "Westerkerk", "De 9 Straatjes"],
        interests: ["Fotoğraf", "Tarih", "Romantik"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.water,
      ),
      CuratedRoute(
        id: "ams_museums",
        name: isEnglish ? "Art & Masterpieces Trail" : "Sanat & Başyapıtlar Yolu",
        description: isEnglish 
          ? "A journey through Dutch brilliance: From Rembrandt's shadows to Van Gogh's vibrant sunflowers"
          : "Hollanda dehasına yolculuk: Rembrandt'ın gölgelerinden Van Gogh'un canlı günebakanlarına.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_15_651c61044bd3.jpg",
        tags: ["Van Gogh", isEnglish ? "Museums" : "Müzeler", "Rembrandt"],
        placeNames: ["Rijksmuseum", "Van Gogh Müzesi", "Stedelijk Museum", "Moco Museum", "Vondelpark", "Concertgebouw"],
        interests: ["Sanat", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "ams_jordaan",
        name: isEnglish ? "Jordaan Bohemian Wander" : "Jordaan Bohem Gezisi",
        description: isEnglish 
          ? "Experience the soul of Amsterdam: Cozy canalside cafes, local art galleries and the Anne Frank House"
          : "Amsterdam'ın ruhunu deneyimleyin: Samimi kanal kafeleri, yerel sanat galerileri ve Anne Frank Evi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_61_40f4aed3d424.jpg",
        tags: ["Jordaan", isEnglish ? "Bohemian" : "Bohem", "Anne Frank"],
        placeNames: ["Jordaan", "Anne Frank Evi", "Winkel 43", "Noordermarkt", "Prinsengracht", "Westerstraat"],
        interests: ["Tarih", "Lokal", "Alışveriş"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.storefront,
      ),
      CuratedRoute(
        id: "ams_food",
        name: isEnglish ? "Dutch Flavours & Markets" : "Hollanda Lezzetleri & Pazarlar",
        description: isEnglish 
          ? "A delicious journey through Amsterdam's food scene: From world-famous stroopwafels and herring to local craft beers"
          : "Amsterdam'ın lezzet sahnesinde nefis bir yolculuk: Dünyaca ünlü stroopwafel ve ringadan yerel biralara.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_1_fe811e66bd7d.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Stroopwafel", isEnglish ? "Markets" : "Pazarlar"],
        placeNames: ["Albert Cuyp Markt", "Foodhallen", "Heineken Experience", "Brouwerij 't IJ", "Van Stapele", "Winkel 43"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "ams_bike",
        name: isEnglish ? "Bike Like a Local" : "Yerel Gibi Bisiklet Turu",
        description: isEnglish 
          ? "The ultimate Amsterdam experience: Rent a bike and explore the secret alleys, iconic parks and creative waterfronts"
          : "En temel Amsterdam deneyimi: Bisiklet kiralayın ve gizli sokakları, ikonik parkları ve yaratıcı kıyıları keşfedin.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "12 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_68_2d5d958d20e2.jpg",
        tags: [isEnglish ? "Bike" : "Bisiklet", isEnglish ? "Parks" : "Parklar", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Vondelpark", "NDSM Wharf", "A'DAM Lookout", "Westerpark", "IJ Ferry Cruise", "Museumplein"],
        interests: ["Bisiklet", "Doğa", "Lokal"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.pedal_bike,
      ),
      CuratedRoute(
        id: "ams_depijp",
        name: isEnglish ? "De Pijp Bohemian Vibes" : "De Pijp Bohem Rotaları",
        description: isEnglish 
          ? "Explore the city's trendiest neighborhood: Multicultural markets, hip boutiques and the history of Heineken"
          : "Şehrin en popüler mahallesini keşfedin: Çok kültürlü pazarlar, havalı butikler ve Heineken'in tarihi.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_19_47aa434a6272.jpg",
        tags: ["De Pijp", isEnglish ? "Bohemian" : "Bohem", "Market"],
        placeNames: ["Albert Cuyp Markt", "Sarphatipark", "Gerard Douplein", "Heineken Experience", "Museumplein", "Rijksmuseum"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFF16A085),
        icon: Icons.brunch_dining,
      ),
      CuratedRoute(
        id: "ams_night",
        name: isEnglish ? "Red Light & Hidden Gems" : "Red Light & Gizli Cevherler",
        description: isEnglish 
          ? "A journey through Amsterdam's historic night: From the oldest streets to elite speakeasy cocktail bars"
          : "Amsterdam'ın tarihi gecesinde bir yolculuk: En eski sokaklardan seçkin gizli kokteyl barlarına.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/amsterdam/red_light_district_de_wallen.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Hidden" : "Gizli", isEnglish ? "Active" : "Canlı"],
        placeNames: ["Red Light District", "Nieuwmarkt", "Rembrandtplein", "Door 74", "Tales & Spirits", "SkyLounge Amsterdam"],
        interests: ["Gece Hayatı", "Tarih", "Kültür"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "ams_noord",
        name: isEnglish ? "Noord Industrial Cool" : "Noord Endüstriyel Stil",
        description: isEnglish 
          ? "Cross the IJ river: A hub of futuristic architecture, massive street art and creative warehouses"
          : "IJ nehrini geçin: Fütüristik mimarinin, devasa sokak sanatının ve yaratıcı depoların merkezi.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "7 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: ["Noord", "NDSM", isEnglish ? "Modern" : "Modern"],
        placeNames: ["EYE Filmmuseum", "NDSM Wharf", "A'DAM Lookout", "Straat Museum", "Pllek", "IJ Ferry Cruise"],
        interests: ["Sanat", "Fotoğraf", "Modern"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.movie,
      ),
      CuratedRoute(
        id: "ams_parks",
        name: isEnglish ? "Amsterdam's Green Oases" : "Amsterdam'ın Yeşil Bahçeleri",
        description: isEnglish 
          ? "Relax and rejuvenate in the city's beautiful parks, botanical gardens and peaceful retreats"
          : "Şehrin güzel parklarında, botanik bahçelerinde ve huzurlu duraklarında dinlenin ve tazelenin.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_92_718fd760d92b.jpg",
        tags: [isEnglish ? "Parks" : "Parklar", isEnglish ? "Nature" : "Doğa", isEnglish ? "Quiet" : "Sessiz"],
        placeNames: ["Vondelpark", "Hortus Botanicus", "Oosterpark", "Rembrandtpark", "Westerpark", "Beatrixpark"],
        interests: ["Doğa", "Fotoğraf", "Sakinlik"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "ams_coffee",
        name: isEnglish ? "Artisanal Coffee & Cafes" : "Artizan Kahve & Kafeler",
        description: isEnglish 
          ? "A tour of Amsterdam's third-wave coffee scene, cozy canal-side spots and the best breakfast joints"
          : "Amsterdam'ın artizan kahve sahnesi, samimi kanal kafeleri ve en iyi kahvaltı durakları turu.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_9_68fb5a366682.jpg",
        tags: [isEnglish ? "Coffee" : "Kahve", isEnglish ? "Brunch" : "Brunch", isEnglish ? "Hipster" : "Hipster"],
        placeNames: ["Lot Sixty One Coffee", "Coffee & Coconuts", "Pluk", "Winkel 43", "De Laatste Kruimel", "Hannekes Boom"],
        interests: ["Kahve", "Yemek", "Lokal"],
        accentColor: const Color(0xFF795548),
        icon: Icons.coffee,
      ),
    ];
  }

  static List<CuratedRoute> _getNewYorkRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "nyc_classic",
        name: isEnglish ? "Iconic Manhattan" : "İkonik Manhattan",
        description: isEnglish ? "Times Square, Empire State, Central Park" : "Times Meydanı, Empire State, Central Park.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "8 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_16_f7740ba93d19.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Manhattan", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Times Square", "Empire State Building", "Central Park", "Rockefeller Center"],
        interests: ["Turist", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "nyc_brooklyn",
        name: isEnglish ? "Brooklyn Bridge & DUMBO" : "Brooklyn Köprüsü",
        description: isEnglish ? "Best Manhattan views and pizza" : "En iyi Manhattan manzarası ve pizza.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_4_d08de5b5755a.jpg",
        tags: ["Brooklyn", "DUMBO", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Brooklyn Bridge", "DUMBO", "Pebble Beach", "Time Out Market", "Brooklyn Bridge Park", "Grimaldi's"],
        interests: ["Fotoğraf", "Romantik", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "nyc_highline",
        name: isEnglish ? "High Line & Chelsea" : "High Line Parkuru",
        description: isEnglish ? "Elevated park, galleries and markets" : "Yükseltilmiş park, galeriler ve pazarlar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_30_ab8b1e3d6ad0.jpg",
        tags: ["High Line", "Chelsea", isEnglish ? "Art" : "Sanat"],
        placeNames: ["High Line", "Chelsea Market", "Little Island", "Whitney Museum"],
        interests: ["Sanat", "Yemek", "Doğa"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "nyc_food",
        name: isEnglish ? "NYC Food Crawl" : "NY Yemek Turu",
        description: isEnglish ? "Pizza, bagels, pastrami and cheesecake" : "Pizza, bagel, pastrami ve cheesecake.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_24_123e054ad350.jpg",
        tags: ["Pizza", "Bagel", isEnglish ? "Food" : "Yemek"],
        placeNames: ["Joe's Pizza", "Katz's Deli", "Ess-a-Bagel", "Junior's"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "nyc_museums",
        name: isEnglish ? "Museum Mile" : "Müze Rotası",
        description: isEnglish ? "Met, MoMA and Guggenheim" : "Met, MoMA ve Guggenheim.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_25_b20418c90853.jpg",
        tags: [isEnglish ? "Museums" : "Müzeler", "MoMA", "Met"],
        placeNames: ["Metropolitan Museum", "MoMA", "Guggenheim", "Neue Galerie"],
        interests: ["Sanat", "Kültür"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "nyc_williamsburg",
        name: isEnglish ? "Williamsburg Hipster" : "Williamsburg",
        description: isEnglish ? "Brooklyn's coolest neighborhood" : "Brooklyn'in en cool mahallesi.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_76_959be52e6cc7.jpg",
        tags: ["Williamsburg", "Hipster", isEnglish ? "Coffee" : "Kahve"],
        placeNames: ["Bedford Avenue", "Smorgasburg", "Domino Park"],
        interests: ["Lokal", "Kahve", "Alışveriş"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.local_cafe,
      ),
      CuratedRoute(
        id: "nyc_views",
        name: isEnglish ? "Skyline Views" : "Gökdelen Manzaraları",
        description: isEnglish ? "Top of the Rock, SUMMIT and Brooklyn" : "Top of the Rock, SUMMIT ve Brooklyn.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "Varies",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_7_4da1cace1dc8.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Skyline" : "Siluet", isEnglish ? "Photo" : "Fotoğraf"],
        placeNames: ["Top of the Rock", "SUMMIT One Vanderbilt", "Brooklyn Promenade"],
        interests: ["Fotoğraf", "Manzara"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "nyc_night",
        name: isEnglish ? "Broadway & Nightlife" : "Broadway Gecesi",
        description: isEnglish ? "Shows, rooftop bars and jazz clubs" : "Gösteriler, teras barlar ve caz kulüpleri.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_97_c9d270445613.jpg",
        tags: ["Broadway", isEnglish ? "Nightlife" : "Gece Hayatı", "Jazz"],
        placeNames: ["Broadway Theater District", "230 Fifth Rooftop", "Blue Note"],
        interests: ["Gece Hayatı", "Kültür", "Müzik"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.theater_comedy,
      ),
      CuratedRoute(
        id: "nyc_central",
        name: isEnglish ? "Central Park Deep Dive" : "Central Park Keşfi",
        description: isEnglish ? "Beyond the basics - hidden gems" : "Klasiklerin ötesi - gizli köşeler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_81_e90a64c74a6c.jpg",
        tags: ["Central Park", isEnglish ? "Nature" : "Doğa", isEnglish ? "Walking" : "Yürüyüş"],
        placeNames: ["Bethesda Fountain", "The Ramble", "Belvedere Castle"],
        interests: ["Doğa", "Romantik", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.forest,
      ),
      CuratedRoute(
        id: "nyc_soho",
        name: isEnglish ? "SoHo Shopping" : "SoHo Alışverişi",
        description: isEnglish ? "Cast-iron buildings and boutiques" : "Dökme demir binalar ve butikler.",
        duration: isEnglish ? "3-4 hours" : "3-4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_62_f641e83684c1.jpg",
        tags: ["SoHo", isEnglish ? "Shopping" : "Alışveriş", isEnglish ? "Architecture" : "Mimari"],
        placeNames: ["Broadway SoHo", "Greene Street", "Nolita"],
        interests: ["Alışveriş", "Mimari"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.shopping_bag,
      ),
    ];
  }

  static List<CuratedRoute> _getTokyoRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "tok_classic",
        name: isEnglish ? "Tokyo Essentials" : "Tokyo Temelleri",
        description: isEnglish ? "Shibuya, Senso-ji, Tokyo Tower" : "Shibuya, Senso-ji, Tokyo Kulesi.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "10 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_23_349502cf700d.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Shibuya", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Shibuya Crossing", "Hachiko Statue", "Meiji Shrine", "Yoyogi Park", "Senso-ji Temple", "Tokyo Tower"],
        interests: ["Turist", "Kültür", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.temple_buddhist,
      ),
      CuratedRoute(
        id: "tok_ramen",
        name: isEnglish ? "Ramen Pilgrimage" : "Ramen Rotası",
        description: isEnglish ? "Best ramen shops from different regions" : "Farklı bölgelerden en iyi ramen dükkanları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_53_c6ec9d7690bc.jpg",
        tags: ["Ramen", isEnglish ? "Food" : "Yemek", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Ichiran Ramen", "Afuri Ramen (Yuzu Ramen)", "Fuunji (Tsukemen)", "Ramen Street (Tokyo Station)", "Rokurinsha", "Nakiryu (Michelin Star)"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.ramen_dining,
      ),
      CuratedRoute(
        id: "tok_akihabara",
        name: isEnglish ? "Akihabara Geek Tour" : "Akihabara Geek Turu",
        description: isEnglish ? "Anime, manga and electronics" : "Anime, manga ve elektronik.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_54_e745cc8c71c5.jpg",
        tags: ["Akihabara", "Anime", isEnglish ? "Electronics" : "Elektronik"],
        placeNames: ["Akihabara Electric Town", "Mandarake Complex", "Yodobashi Camera", "Radio Kaikan", "Super Potato (Retro Games)", "Maid Cafe"],
        interests: ["Alışveriş", "Kültür", "Eğlence"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.videogame_asset,
      ),
      CuratedRoute(
        id: "tok_shibuya",
        name: isEnglish ? "Shibuya & Harajuku" : "Shibuya & Harajuku",
        description: isEnglish ? "Fashion, cafes and youth culture" : "Moda, kafeler ve gençlik kültürü.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_80_c6e351c137a4.jpg",
        tags: ["Shibuya", "Harajuku", isEnglish ? "Fashion" : "Moda"],
        placeNames: ["Shibuya Crossing", "Miyashita Park", "Takeshita Street", "Cat Street", "Omotesando"],
        interests: ["Alışveriş", "Fotoğraf", "Lokal"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.accessibility_new,
      ),
      CuratedRoute(
        id: "tok_tsukiji",
        name: isEnglish ? "Tsukiji Outer Market" : "Tsukiji Pazar",
        description: isEnglish ? "Fresh sushi and seafood breakfast" : "Taze sushi ve deniz ürünleri kahvaltısı.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_74_7ece1d166382.jpg",
        tags: ["Tsukiji", isEnglish ? "Sushi" : "Sushi", isEnglish ? "Market" : "Pazar"],
        placeNames: ["Tsukiji Outer Market", "Sushizanmai Main Branch", "Tamagoyaki shops", "Tsukiji Hongwanji Temple", "Kitsuneya (Beef Bowls)"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "tok_shinjuku",
        name: isEnglish ? "Shinjuku Night" : "Shinjuku Gecesi",
        description: isEnglish ? "Neon lights, Golden Gai and izakayas" : "Neon ışıklar, Golden Gai ve izakayalar.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_84_9d50396aa03a.jpg",
        tags: ["Shinjuku", isEnglish ? "Nightlife" : "Gece Hayatı", "Neon"],
        placeNames: ["Kabukicho", "Golden Gai", "Omoide Yokocho (Piss Alley)", "Shinjuku Gyoen National Garden", "Hanazono Shrine", "Tokyo Metropolitan Govt Building"],
        interests: ["Gece Hayatı", "Yemek", "Fotoğraf", "Manzara"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "tok_teamlab",
        name: isEnglish ? "TeamLab Digital Art" : "TeamLab Dijital Sanat",
        description: isEnglish ? "Immersive art museum experience" : "Sürükleyici sanat müzesi deneyimi.",
        duration: isEnglish ? "3-4 hours" : "3-4 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_18_c80ee539f623.jpg",
        tags: ["TeamLab", isEnglish ? "Digital Art" : "Dijital Sanat", isEnglish ? "Immersive" : "Sürükleyici"],
        placeNames: ["TeamLab Planets TOYOSU", "TeamLab Borderless (Azabudai Hills)", "Mori Art Museum", "Tokyo City View", "Roppongi Hills"],
        interests: ["Sanat", "Fotoğraf", "Manzara"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.light_mode,
      ),
      CuratedRoute(
        id: "tok_shimokita",
        name: isEnglish ? "Shimokitazawa Vintage" : "Shimokitazawa",
        description: isEnglish ? "Indie shops, cafes and live music" : "Bağımsız dükkanlar, kafeler ve canlı müzik.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "2.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_100_c85c5f25d737.jpg",
        tags: ["Shimokitazawa", "Vintage", isEnglish ? "Music" : "Müzik"],
        placeNames: ["Shimokitazawa Station", "Vintage Clothing Shops", "Basement Bar (Live Music)", "Shirohige’s Cream Puff Factory", "Setagaya Park"],
        interests: ["Alışveriş", "Müzik", "Lokal", "Yemek"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.music_note,
      ),
      CuratedRoute(
        id: "tok_konbini",
        name: isEnglish ? "Konbini Food Tour" : "Konbini Turu",
        description: isEnglish ? "Discover convenience store gourmet" : "Market gurmeliğini keşfet.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_102_70fac3d60aee.jpg",
        tags: ["Konbini", "7-Eleven", isEnglish ? "Street Food" : "Sokak"],
        placeNames: ["7-Eleven", "Lawson", "Family Mart"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.store,
      ),
      CuratedRoute(
        id: "tok_asakusa",
        name: isEnglish ? "Old Tokyo Asakusa" : "Eski Tokyo Asakusa",
        description: isEnglish ? "Senso-ji, traditional crafts and street food" : "Senso-ji, geleneksel el sanatları ve sokak yemekleri.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_82_cd622bd22762.jpg",
        tags: ["Asakusa", "Senso-ji", isEnglish ? "Traditional" : "Geleneksel"],
        placeNames: ["Senso-ji Temple", "Nakamise Street", "Kaminarimon Gate"],
        interests: ["Tarih", "Kültür", "Yemek"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.temple_buddhist,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SEVILLA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSevillaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sev_historic",
        name: isEnglish ? "Historic Heart of Seville" : "Sevilla'nın Tarihi Kalbi",
        description: isEnglish 
          ? "The essential Seville: Cathedral, Alcázar, Jewish Quarter and hidden colonial archives"
          : "Sevilla'nın olmazsa olmazları: Katedral, Alcázar, Santa Cruz ve koloni arşivleri.",
        duration: isEnglish ? "7-8 hours" : "7-8 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_44_1d53c785d361.jpg",
        tags: [isEnglish ? "Historical" : "Tarihi", "UNESCO", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Real Alcázar", "Catedral & Giralda", "Plaza de España", "Plaza del Cabildo", "Archivo de Indias", "Santa Cruz Neighborhood", "Hospital de los Venerables", "Jardines de Murillo"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "sev_triana",
        name: isEnglish ? "Triana & River Vibes" : "Triana & Nehir Keyfi",
        description: isEnglish
          ? "Cross the bridge for ceramics, flamenco and riverfront walks in the old sailors' district"
          : "Köprüyü geçin: Seramikler, flamenko ruhu ve eski denizci mahallesinde nehir yürüyüşü.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "5.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/sevilla/triana.jpg",
        tags: ["Triana", isEnglish ? "Flamenco" : "Flamenko", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Triana", "Torre del Oro", "Mercado Lonja del Barranco", "Castillo de San Jorge", "Calle Betis", "Puente de Isabel II", "Mercado de Triana"],
        interests: ["Kültür", "Lokal", "Yemek"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.music_note,
      ),
      CuratedRoute(
        id: "sev_modern",
        name: isEnglish ? "Modern Seville & Parks" : "Modern Sevilla & Parklar",
        description: isEnglish
          ? "Stunning Architecture: From Metropol Parasol to the lush Maria Luisa Park and Expo legacy"
          : "Göz alıcı mimari: Metropol Parasol'dan Maria Luisa Parkı'na ve Expo mirasına.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "7.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/sevilla/metropol_parasol_las_setas.jpg",
        tags: [isEnglish ? "Modern" : "Modern", isEnglish ? "Parks" : "Parklar", isEnglish ? "Architecture" : "Mimari"],
        placeNames: ["Metropol Parasol (Las Setas)", "Plaza de España", "Torre Sevilla", "Maria Luisa Park", "Pabellón de la Navegación", "CaixaForum Sevilla", "Puente de la Barqueta"],
        interests: ["Mimari", "Fotoğraf", "Doğa"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "sev_tapas",
        name: isEnglish ? "Authentic Tapas Crawl" : "Otantik Tapas Turu",
        description: isEnglish
          ? "Sample the best local flavors in the city's oldest and most iconic taverns"
          : "Şehrin en eski ve ikonik tavernalarında en iyi yerel lezzetleri tadın.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_2_ce590176e001.jpg",
        tags: ["Tapas", isEnglish ? "Food" : "Yemek", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Bodega Santa Cruz (Las Columnas)", "Eslava", "El Rinconcillo", "Casa Morales", "Las Teresas", "Mercado de la Encarnación", "Cañabota"],
        interests: ["Yemek", "Lokal", "Yemek"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.restaurant,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MADRİD ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getMadridRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "mad_classic",
        name: isEnglish ? "Imperial Madrid Landmarks" : "Kraliyet Madrid İkonları",
        description: isEnglish 
          ? "Step into the grandeur of the Spanish Empire: Majestic palaces, historic plazas and the bustling heart of the city"
          : "İspanya İmparatorluğu'nun ihtişamına adım atın: Görkemli saraylar, tarihi meydanlar ve şehrin kalbi.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/madrid/palacio_real.jpg",
        tags: [isEnglish ? "Imperial" : "İmparatorluk", "Palace", isEnglish ? "Historical" : "Tarihi"],
        placeNames: ["Palacio Real", "Plaza Mayor", "Puerta del Sol", "Gran Vía", "Plaza de Cibeles", "Templo de Debod"],
        interests: ["Tarih", "Fotoğraf", "Mimari"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "mad_art",
        name: isEnglish ? "Art Triangle Masterpieces" : "Sanat Üçgeni Başyapıtları",
        description: isEnglish 
          ? "A journey through the world's finest collections: From Velázquez's realism to Picasso's bold Guernica"
          : "Dünyanın en iyi koleksiyonlarında bir yolculuk: Velázquez'in gerçekçiliğinden Picasso'nun Guernica'sına.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_47_a5f48b322403.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Museums", "Picasso"],
        placeNames: ["Prado Müzesi", "Reina Sofía Müzesi", "Thyssen-Bornemisza", "Retiro Parkı", "CaixaForum", "Atocha"],
        interests: ["Sanat", "Kültür", "Tarih"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "mad_royal",
        name: isEnglish ? "Royal & Historic Madrid" : "Kraliyet & Tarihi Madrid",
        description: isEnglish
          ? "Step into the grandeur of the Spanish Empire: Majestic palaces, historic plazas and the royal gardens of the monarchy"
          : "İspanya İmparatorluğu'nun ihtişamına adım atın: Görkemli saraylar, tarihi meydanlar ve kraliyet bahçeleri.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_101_ac38dc5796e7.jpg",
        tags: [isEnglish ? "Royal" : "Kraliyet", isEnglish ? "History" : "Tarihi", isEnglish ? "Palace" : "Saray"],
        placeNames: ["Palacio Real", "Jardines de Sabatini", "Plaza de la Villa", "Teatro Real", "Plaza de España", "Templo de Debod"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "mad_park",
        name: isEnglish ? "Retiro Park & City Icons" : "Retiro Parkı & Şehir İkonları",
        description: isEnglish
          ? "A breath of fresh air followed by Madrid's most iconic monuments, grand boulevards and skyline views"
          : "Madrid'in ciğerlerinde bir mola; ardından ikonik anıtlar, görkemli bulvarlar ve şehir manzaraları.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "6.5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_103_2d857e5bef56.jpg",
        tags: [isEnglish ? "Parks" : "Parklar", isEnglish ? "Views" : "Manzara", isEnglish ? "Outdoor" : "Açık Hava"],
        placeNames: ["Retiro Parkı", "Puerta de Alcalá", "Plaza de Cibeles", "Gran Vía", "Círculo de Bellas Artes", "Edificio Metrópolis"],
        interests: ["Doğa", "Manzara", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "mad_tapas",
        name: isEnglish ? "Tapas & Flavours of Old Madrid" : "Eski Madrid'in Tapas Lezzetleri",
        description: isEnglish
          ? "A culinary journey through historic markets, legendary tabernas and the most authentic foodie neighborhoods"
          : "Tarihi pazarlardan, efsanevi meyhanelere ve en otantik lezzet duraklarına gastronomik bir yolculuk.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_87_61aeada8c835.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Tapas", isEnglish ? "Markets" : "Pazarlar"],
        placeNames: ["Mercado de San Miguel", "La Latina", "El Rastro", "Chocolatería San Ginés", "Casa Labra", "Sobrino de Botín", "Casa Lucio"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // FLORANSA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getFlorenceRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "flo_renaissance",
        name: isEnglish ? "Renaissance Masterpieces" : "Rönesans Başyapıtları",
        description: isEnglish 
          ? "The essential sites of the cradle of the Renaissance"
          : "Rönesans'ın beşiğinin olmazsa olmaz noktaları.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_98_d84aee96b2c5.jpg",
        tags: [isEnglish ? "Renaissance" : "Rönesans", "UNESCO", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Duomo (Santa Maria del Fiore)", "Uffizi Galerisi", "Accademia Galerisi", "Palazzo Vecchio"],
        interests: ["Sanat", "Tarih", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "flo_oltrarno",
        name: isEnglish ? "Oltrarno Discovery" : "Oltrarno Keşfi",
        description: isEnglish
          ? "Cross the Arno for artisan workshops, gardens and panoramic views"
          : "Zanaatkar atölyeleri, bahçeler ve panoramik manzaralar için Arno'nun diğer yakasına geçin.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "5.5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_43_5af81c975d0a.jpg",
        tags: ["Oltrarno", isEnglish ? "Views" : "Manzara", isEnglish ? "Artisans" : "Zanaatkarlar"],
        placeNames: ["Ponte Vecchio", "Palazzo Pitti", "Boboli Bahçeleri", "Piazzale Michelangelo", "San Miniato al Monte"],
        interests: ["Manzara", "Doğa", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "flo_local",
        name: isEnglish ? "Local Flavor & Markets" : "Lokal Lezzet & Pazarlar",
        description: isEnglish
          ? "A culinary journey through Florence's historic food halls and street corners"
          : "Floransa'nın tarihi yemek salonlarından ve sokak köşelerinden geçen lezzetli bir yolculuk.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_77_df3e17678144.jpg",
        tags: [isEnglish ? "Food" : "Yemek", isEnglish ? "Market" : "Pazar", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Mercato Centrale", "Mercato di Sant'Ambrogio", "Vivoli", "San Lorenzo Pazarı"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "flo_churches",
        name: isEnglish ? "Sacred Florence" : "Kutsal Floransa",
        description: isEnglish
          ? "Explore the city's most beautiful basilicas and hidden chapels"
          : "Şehrin en güzel bazilikalarını ve gizli şapellerini keşfedin.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "4.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_79_6a9a8e501e0d.jpg",
        tags: [isEnglish ? "Churches" : "Kiliseler", isEnglish ? "Art" : "Sanat", isEnglish ? "History" : "Tarih"],
        placeNames: ["Santa Maria Novella", "Santa Croce Bazilikası", "Museo San Marco", "Cappelle Medicee"],
        interests: ["Tarih", "Sanat", "Kültür"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.church,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ATİNA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getAthensRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ath_glory",
        name: isEnglish ? "Ancient Glory" : "Antik İhtişam",
        description: isEnglish 
          ? "The cradle of Western civilization: Parthenon and the Acropolis"
          : "Batı medeniyetinin beşiği: Parthenon ve Akropolis.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_86_c8e30c3ff1f7.jpg",
        tags: [isEnglish ? "Ancient" : "Antik", "UNESCO", "History"],
        placeNames: ["Akropolis", "Parthenon", "Akropolis Müzesi", "Odeon of Herodes Atticus"],
        interests: ["Tarih", "Kültür", "Mimari"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "ath_streets",
        name: isEnglish ? "Historic Neighborhoods" : "Tarihi Mahalleler",
        description: isEnglish
          ? "Stroll through Plaka, Anafiotika and the vibrant Monastiraki"
          : "Plaka, Anafiotika ve canlı Monastiraki sokaklarında dolaşın.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3.5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_37_ac91d5383bf8.jpg",
        tags: [isEnglish ? "Atmospheric" : "Atmosferik", isEnglish ? "Local" : "Lokal", isEnglish ? "Walking" : "Yürüyüş"],
        placeNames: ["Plaka", "Anafiotika", "Monastiraki", "Hadrian's Library"],
        interests: ["Fotoğraf", "Lokal", "Tarih"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.streetview,
      ),
      CuratedRoute(
        id: "ath_agora",
        name: isEnglish ? "Agoras & Ancient Markets" : "Agoralar & Antik Pazarlar",
        description: isEnglish
          ? "Where democracy was born: Explore the central markets of antiquity"
          : "Demokrasinin doğduğu yer: Antik çağın merkezi pazarlarını keşfedin.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_59_773c97a627dc.jpg",
        tags: [isEnglish ? "Ancient" : "Antik", isEnglish ? "Agora" : "Agora", isEnglish ? "Culture" : "Kültür"],
        placeNames: ["Antik Agora", "Hephaistos Tapınağı", "Roman Agora", "Areopagus Hill (Mars Hill)"],
        interests: ["Tarih", "Kültür", "Felsefe"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.temple_buddhist,
      ),
      CuratedRoute(
        id: "ath_views",
        name: isEnglish ? "Heights & Views" : "Tepeler & Manzaralar",
        description: isEnglish
          ? "Epic panoramic views of Athens from its most famous hills"
          : "Atina'nın en ünlü tepelerinden epik panoramik manzaralar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/routes/route_photo_40_cadfa55fbc1a.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Hiking" : "Hafif Yürüyüş", isEnglish ? "Photography" : "Fotoğraf"],
        placeNames: ["Lykavittos Tepesi", "Filopappos Tepesi", "Syntagma Meydanı"],
        interests: ["Manzara", "Fotoğraf", "Doğa"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
    ];
  }
  // ═══════════════════════════════════════════════════════════════════════════
  // DUBAİ ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getDubaiRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "dub_iconic",
        name: isEnglish ? "Dubai Icons & Superlatives" : "Dubai İkonları",
        description: isEnglish 
          ? "The world's tallest tower, largest mall, and most spectacular fountain show"
          : "Dünyanın en yüksek kulesi, en büyük alışveriş merkezi ve en muhteşem çeşme gösterisi.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/burj_khalifa.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Burj Khalifa", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Burj Khalifa", "Dubai Mall", "Dubai Fountain", "Dubai Opera", "Souk Al Bahar"],
        interests: ["Mimari", "Alışveriş", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "dub_oldnew",
        name: isEnglish ? "Old Dubai Heritage Walk" : "Eski Dubai Mirası",
        description: isEnglish 
          ? "Step back in time: Gold and spice souks, creek boat rides and historic Al Fahidi"
          : "Zamanda geriye yolculuk: Altın ve baharat sokakları, tekne gezisi ve tarihi Al Fahidi.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/old_dubai_deira.jpg",
        tags: [isEnglish ? "Heritage" : "Miras", "Souk", isEnglish ? "Traditional" : "Geleneksel"],
        placeNames: ["Old Dubai - Deira", "Gold Souk", "Spice Souk", "Dubai Creek", "Al Fahidi Historical District", "Al Seef"],
        interests: ["Tarih", "Kültür", "Alışveriş"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.history,
      ),
      CuratedRoute(
        id: "dub_beach",
        name: isEnglish ? "Beach & Marina Life" : "Plaj & Marina Hayatı",
        description: isEnglish 
          ? "Sun, sand and skyline: JBR Beach, Marina walks and sunset at La Mer"
          : "Güneş, kum ve siluet: JBR Plajı, Marina yürüyüşü ve La Mer'de gün batımı.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/jbr_beach.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", "Marina", isEnglish ? "Sunset" : "Günbatımı"],
        placeNames: ["JBR Beach", "Dubai Marina", "La Mer", "Aura Skypool", "The View at The Palm"],
        interests: ["Plaj", "Romantik", "Fotoğraf"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.beach_access,
      ),
      CuratedRoute(
        id: "dub_luxury",
        name: isEnglish ? "Luxury & Extravagance" : "Lüks & Gösteriş",
        description: isEnglish 
          ? "Experience Dubai's opulence: 7-star hotel, Palm views and world-class dining"
          : "Dubai'nin ihtişamını yaşayın: 7 yıldızlı otel, Palm manzarası ve dünya sınıfı yemekler.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "15 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/burj_al_arab.jpg",
        tags: [isEnglish ? "Luxury" : "Lüks", "Burj Al Arab", "Palm"],
        placeNames: ["Burj Al Arab", "Palm Jumeirah", "Atlantis Aquaventure", "Madinat Jumeirah", "The View at The Palm"],
        interests: ["Lüks", "Romantik", "Yemek"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.diamond,
      ),
      CuratedRoute(
        id: "dub_future",
        name: isEnglish ? "Future & Innovation" : "Gelecek & İnovasyon",
        description: isEnglish 
          ? "Cutting-edge Dubai: Museum of the Future, Dubai Frame and record-breaking attractions"
          : "Son teknoloji Dubai: Gelecek Müzesi, Dubai Çerçevesi ve rekor kıran yerler.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/museum_of_the_future.jpg",
        tags: [isEnglish ? "Futuristic" : "Fütüristik", isEnglish ? "Tech" : "Teknoloji", isEnglish ? "Museum" : "Müze"],
        placeNames: ["Museum of the Future", "Dubai Frame", "Deep Dive Dubai", "Ski Dubai", "IMG Worlds of Adventure"],
        interests: ["Teknoloji", "Macera", "Sanat"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.rocket_launch,
      ),
      CuratedRoute(
        id: "dub_desert",
        name: isEnglish ? "Desert Safari Adventure" : "Çöl Safari Macerası",
        description: isEnglish 
          ? "Dune bashing, camel rides and Bedouin dinner under the stars"
          : "Kum tepelerinde macera, deve gezisi ve yıldızlar altında Bedevi yemeği.",
        duration: isEnglish ? "Half day" : "Yarım gün",
        distance: "60 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dubai/global_village.jpg",
        tags: [isEnglish ? "Desert" : "Çöl", "Safari", isEnglish ? "Adventure" : "Macera"],
        placeNames: ["Dubai Desert Conservation Reserve", "Dune Bashing & Camel Rides", "Global Village", "Miracle Garden", "Dragon Mart"],
        interests: ["Macera", "Doğa", "Fotoğraf", "Eğlence"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.terrain,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // LİZBON ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getLisbonRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "lis_classic",
        name: isEnglish ? "Lisbon Essential Icons" : "Lizbon Klasikleri",
        description: isEnglish 
          ? "The must-see Lisbon: Belém Tower, Jerónimos Monastery and the iconic Tram 28"
          : "Mutlaka görülmesi gereken Lizbon: Belém Kulesi, Jerónimos Manastırı ve ikonik 28 Numaralı Tramvay.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "8 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/belem_kulesi.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Belém", "UNESCO"],
        placeNames: ["Belém Kulesi", "Jerónimos Manastırı", "Padrão dos Descobrimentos", "Pastéis de Belém", "Tramvay 28"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "lis_alfama",
        name: isEnglish ? "Alfama Soul & Fado" : "Alfama Ruhu & Fado",
        description: isEnglish 
          ? "Wander the oldest neighborhood: Castle views, fado music and Lisbon's authentic heart"
          : "En eski mahallelerde kaybolun: Kale manzaraları, fado müziği ve Lizbon'un otantik kalbi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/alfama.jpg",
        tags: ["Alfama", "Fado", isEnglish ? "Traditional" : "Geleneksel"],
        placeNames: ["Alfama", "Castelo de São Jorge", "Miradouro da Senhora do Monte", "Miradouro da Graça", "Feira da Ladra"],
        interests: ["Kültür", "Müzik", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.music_note,
      ),
      CuratedRoute(
        id: "lis_viewpoints",
        name: isEnglish ? "Miradouros & Views" : "Manzara Noktaları",
        description: isEnglish 
          ? "Chase the best panoramas: Hilltop viewpoints, elevators and rooftop bars"
          : "En iyi panoramaların peşinde: Tepe manzaraları, asansörler ve çatı barları.",
        duration: isEnglish ? "4-5 hours" : "4-5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/miradouro_da_senhora_do_monte.jpg",
        tags: [isEnglish ? "Views" : "Manzara", "Miradouro", isEnglish ? "Sunset" : "Günbatımı"],
        placeNames: ["Miradouro da Senhora do Monte", "Miradouro da Graça", "Elevador de Santa Justa", "Ponte 25 de Abril", "Basílica da Estrela"],
        interests: ["Fotoğraf", "Romantik", "Manzara"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "lis_food",
        name: isEnglish ? "Pastéis & Petiscos Trail" : "Pastéis & Petiscos Turu",
        description: isEnglish 
          ? "A delicious journey: Famous custard tarts, time out market and authentic seafood"
          : "Lezzetli bir yolculuk: Ünlü pastéis, Time Out Market ve otantik deniz ürünleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/pasteis_de_belem.jpg",
        tags: ["Pastéis", isEnglish ? "Seafood" : "Deniz Ürünleri", isEnglish ? "Market" : "Pazar"],
        placeNames: ["Pastéis de Belém", "Time Out Market", "Mercado da Ribeira", "Cervejaria Ramiro", "Ginjinha"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "lis_trendy",
        name: isEnglish ? "LX Factory & Cool Spots" : "LX Factory & Trend Noktalar",
        description: isEnglish 
          ? "Creative Lisbon: Industrial-chic spaces, street art and rooftop cocktails"
          : "Yaratıcı Lizbon: Endüstriyel-şık mekanlar, sokak sanatı ve çatı kokteylleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/lx_factory.jpg",
        tags: ["LX Factory", isEnglish ? "Trendy" : "Trend", isEnglish ? "Art" : "Sanat"],
        placeNames: ["LX Factory", "Príncipe Real", "Bairro Alto", "Pink Street", "MAAT"],
        interests: ["Sanat", "Alışveriş", "Gece Hayatı"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "lis_tiles",
        name: isEnglish ? "Azulejo Art Journey" : "Azulejo Sanat Yolculuğu",
        description: isEnglish 
          ? "Discover Portugal's iconic tiles: Museums, decorated facades and hidden gems"
          : "Portekiz'in ikonik çinilerini keşfedin: Müzeler, süslü cepheler ve gizli hazineler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lizbon/museu_nacional_do_azulejo.jpg",
        tags: ["Azulejo", isEnglish ? "Art" : "Sanat", isEnglish ? "Museum" : "Müze"],
        placeNames: ["Museu Nacional do Azulejo", "Alfama", "Convento do Carmo", "Casa do Alentejo", "Chiado"],
        interests: ["Sanat", "Kültür", "Fotoğraf"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.grid_view,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // PRAG ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getPragueRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "pra_classic",
        name: isEnglish ? "Prague Castle & Old Town" : "Prag Kalesi & Eski Şehir",
        description: isEnglish 
          ? "The essential Prague: Castle complex, Charles Bridge and the magical Old Town Square"
          : "Temel Prag deneyimi: Kale kompleksi, Charles Köprüsü ve masalsı Eski Şehir Meydanı.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "6 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/old_town_squares.jpg",
        tags: [isEnglish ? "Castle" : "Kale", isEnglish ? "Historical" : "Tarihi", "UNESCO"],
        placeNames: ["Prague Castle", "St. Vitus Cathedral", "Golden Lane", "Charles Bridge", "Old Town Square", "Astronomical Clock"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "pra_jewish",
        name: isEnglish ? "Jewish Quarter & History" : "Yahudi Mahallesi & Tarih",
        description: isEnglish 
          ? "A moving journey through Josefov: Ancient synagogues, cemetery and Franz Kafka's world"
          : "Josefov'da duygu dolu bir yolculuk: Kadim sinagoglar, mezarlık ve Franz Kafka'nın dünyası.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/istanbul/arter.jpg",
        tags: ["Josefov", "Kafka", isEnglish ? "History" : "Tarih"],
        placeNames: ["Jewish Quarter (Josefov)", "Franz Kafka Museum", "Old Town Square", "Tyn Church"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.history_edu,
      ),
      CuratedRoute(
        id: "pra_beer",
        name: isEnglish ? "Czech Beer Pilgrimage" : "Çek Bira Haccı",
        description: isEnglish 
          ? "Experience the world's best beer culture: Historic breweries and authentic beer halls"
          : "Dünyanın en iyi bira kültürünü yaşayın: Tarihi bira fabrikaları ve otantik bira salonları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Beer" : "Bira", isEnglish ? "Pub" : "Bar", isEnglish ? "Local" : "Lokal"],
        placeNames: ["U Fleků", "Lokál Dlouhááá", "Kantýna", "Havelska Koruna"],
        interests: ["Bira", "Yemek", "Lokal"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.sports_bar,
      ),
      CuratedRoute(
        id: "pra_coffee",
        name: isEnglish ? "Historic Cafés & Culture" : "Tarihi Kafeler & Kültür",
        description: isEnglish 
          ? "Elegant coffee houses where artists and writers found inspiration for a century"
          : "Sanatçıların ve yazarların yüzyıldır ilham bulduğu zarif kahve evleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Coffee" : "Kahve", isEnglish ? "Historic" : "Tarihi", isEnglish ? "Elegant" : "Zarif"],
        placeNames: ["Cafe Louvre", "Cafe Savoy", "Kavárna Slavia", "National Gallery", "Dancing House"],
        interests: ["Kahve", "Kültür", "Sanat"],
        accentColor: const Color(0xFF795548),
        icon: Icons.coffee,
      ),
      CuratedRoute(
        id: "pra_night",
        name: isEnglish ? "Prague After Dark" : "Gece Prag",
        description: isEnglish 
          ? "The city's legendary nightlife: Speakeasies, jazz clubs and the illuminated old town"
          : "Şehrin efsanevi gece hayatı: Gizli barlar, caz kulüpleri ve ışıl ışıl eski şehir.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/old_town_squares.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Cocktails" : "Kokteyl", "Jazz"],
        placeNames: ["Hemingway Bar", "Old Town Square", "Charles Bridge", "Venceslas Square"],
        interests: ["Gece Hayatı", "Romantik"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "pra_views",
        name: isEnglish ? "Panoramic Prague" : "Panoramik Prag",
        description: isEnglish 
          ? "The best viewpoints: Petřín Hill, Vyšehrad fortress and hidden rooftops"
          : "En iyi manzara noktaları: Petřín Tepesi, Vyšehrad kalesi ve gizli çatılar.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "7 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/prag/petrin-tower.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Nature" : "Doğa", isEnglish ? "Sunset" : "Günbatımı"],
        placeNames: ["Petrin Hill", "Vyšehrad", "Charles Bridge", "Prague Castle"],
        interests: ["Manzara", "Fotoğraf", "Doğa"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // VİYANA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getViennaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "vie_imperial",
        name: isEnglish ? "Imperial Vienna" : "İmparatorluk Viyana'sı",
        description: isEnglish 
          ? "Habsburg grandeur: Schönbrunn Palace, Hofburg and the magnificent State Opera"
          : "Habsburg ihtişamı: Schönbrunn Sarayı, Hofburg ve muhteşem Devlet Operası.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "8 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Palace" : "Saray", "Habsburg", isEnglish ? "Imperial" : "İmparatorluk"],
        placeNames: ["Schönbrunn Palace", "Hofburg", "Vienna State Opera", "Rathaus", "Graben"],
        interests: ["Tarih", "Mimari", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "vie_art",
        name: isEnglish ? "Art & Museums Mile" : "Sanat & Müzeler Rotası",
        description: isEnglish 
          ? "World-class art: Klimt at Belvedere, Old Masters and cutting-edge Albertina"
          : "Dünya sınıfı sanat: Belvedere'de Klimt, Ustalar ve çağdaş Albertina.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: ["Klimt", isEnglish ? "Museum" : "Müze", isEnglish ? "Art" : "Sanat"],
        placeNames: ["Belvedere Museum", "Kunsthistorisches Museum", "Albertina", "Mozarthaus Vienna"],
        interests: ["Sanat", "Kültür"],
        accentColor: const Color(0xFF9C27B0),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "vie_coffee",
        name: isEnglish ? "Viennese Coffee House Tour" : "Viyana Kahve Evi Turu",
        description: isEnglish 
          ? "UNESCO heritage: Historic cafés with Sachertorte, melange and imperial ambiance"
          : "UNESCO mirası: Sachertorte, melange ve imparatorluk atmosferiyle tarihi kafeler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/cafe_central_palace.jpg",
        tags: [isEnglish ? "Coffee" : "Kahve", "Sachertorte", isEnglish ? "Historic" : "Tarihi"],
        placeNames: ["Cafe Central", "Cafe Sacher", "Cafe Sperl", "Demel", "Chiado"],
        interests: ["Kahve", "Yemek", "Kültür"],
        accentColor: const Color(0xFF795548),
        icon: Icons.coffee,
      ),
      CuratedRoute(
        id: "vie_music",
        name: isEnglish ? "Classical Music Heritage" : "Klasik Müzik Mirası",
        description: isEnglish 
          ? "In the footsteps of Mozart and Beethoven: Concert halls and composers' homes"
          : "Mozart ve Beethoven'ın izinde: Konser salonları ve bestecilerin evleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: ["Mozart", "Beethoven", isEnglish ? "Classical" : "Klasik"],
        placeNames: ["Musikverein", "Vienna State Opera", "Mozarthaus Vienna", "St. Stephen's Cathedral", "Stadtpark"],
        interests: ["Müzik", "Kültür", "Tarih"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.music_note,
      ),
      CuratedRoute(
        id: "vie_food",
        name: isEnglish ? "Schnitzel & Naschmarkt" : "Şnitzel & Naschmarkt",
        description: isEnglish 
          ? "Viennese cuisine: The famous schnitzel, vibrant markets and traditional wine taverns"
          : "Viyana mutfağı: Ünlü şnitzel, canlı pazarlar ve geleneksel şarap meyhaneleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Schnitzel", "Naschmarkt"],
        placeNames: ["Naschmarkt", "Figlmüller", "Plachutta", "Zum Schwarzen Kameel", "Steirereck"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "vie_parks",
        name: isEnglish ? "Green Vienna & Prater" : "Yeşil Viyana & Prater",
        description: isEnglish 
          ? "Escape to nature: Iconic Giant Wheel, imperial gardens and peaceful Volksgarten"
          : "Doğaya kaçış: İkonik Dönme Dolap, imparatorluk bahçeleri ve huzurlu Volksgarten.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference=AZLasHqht8C8K6-nfxETO4ot6iCblYiL7L6uc0Y-UtZJtjqhihzyAdH7NhNpvUtEJ_p_ZSbZUez3Mwgl-TWdUmOTX_2aJoS94c7OJF_QlQJpRyDMq55BPrdV4mtFIs9PS2be30tJYpR8UEs9lW33prh2G0sHRzlz-HlPu8b7aFveihcgQ5EwmihJ_JEBq_7CiqV0wamHYmrKYZVvw8FPpTX96lmjuYuiFFgamGu5w97hwIFpVcuF48a1LwV_VLbJaGuHVDOdwBR7nJTVp8afL03Sxa7oEF7OHOm00OmUuluy8RqBM13iqMR82oWFFL2h3dO1hGiqiek5x7YlXSy8mm-GIEhQXt-3YrGyT4lYHaRad7DGYLf1lMKNQJvXUZpqpQhO7CFFmB5AEElK8NltB3jtKYug1HOAG0uZEujEBb9vIFNsNHHmQUCJiycviQoz9c3DwnntEyEagRch5AnHXVmL202hN839ShQHYt9NBewlHIY74dzMYbNcZKUYJ_-Y7kbuddmVWpTE72J1Uq2ZPEHtnxGpHHR7whJNs-CdaXALueJbj0ewNlraTI00rXSZAy_SwXBc_b65&key=AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g",
        tags: ["Prater", isEnglish ? "Parks" : "Parklar", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["Prater Park", "Stadtpark", "Volksgarten", "Schönbrunn Palace"],
        interests: ["Doğa", "Romantik", "Bisiklet"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // PORTO ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getPortoRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "por_classic",
        name: isEnglish ? "Porto Essentials" : "Porto Klasikleri",
        description: isEnglish 
          ? "The must-see Porto: Ribeira waterfront, iconic bridge and stunning São Bento station"
          : "Mutlaka görülmesi gereken Porto: Ribeira sahili, ikonik köprü ve muhteşem São Bento istasyonu.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/ribeira.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Ribeira", "UNESCO"],
        placeNames: ["Ribeira", "Dom Luís I Köprüsü", "São Bento Tren İstasyonu", "Clérigos Kulesi", "Sé do Porto (Katedral)"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "por_wine",
        name: isEnglish ? "Port Wine Cellars" : "Port Şarabı Mahzenleri",
        description: isEnglish 
          ? "Cross the bridge to Gaia: Historic wine cellars, tastings and Douro views"
          : "Gaia'ya geçin: Tarihi şarap mahzenleri, tadımlar ve Douro manzaraları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/vila_nova_de_gaia_port_mahzenleri.jpg",
        tags: [isEnglish ? "Wine" : "Şarap", "Port", "Gaia"],
        placeNames: ["Vila Nova de Gaia - Port Mahzenleri", "Teleferico de Gaia", "WOW (World of Wine)", "Dom Luís I Köprüsü"],
        interests: ["Şarap", "Yemek", "Manzara"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.wine_bar,
      ),
      CuratedRoute(
        id: "por_food",
        name: isEnglish ? "Francesinha & Local Bites" : "Francesinha & Yerel Tatlar",
        description: isEnglish 
          ? "Porto's legendary sandwich, fresh markets and the best pastéis de nata"
          : "Porto'nun efsanevi sandviçi, taze pazarlar ve en iyi pastéis de nata.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/cafe_santiago.jpg",
        tags: ["Francesinha", isEnglish ? "Food" : "Yemek", isEnglish ? "Market" : "Pazar"],
        placeNames: ["Café Santiago", "Mercado do Bolhão", "Manteigaria", "Cais da Ribeira", "Matosinhos"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "por_art",
        name: isEnglish ? "Azulejos & Street Art" : "Azulejo & Sokak Sanatı",
        description: isEnglish 
          ? "Blue tiles and urban art: Chapel of Souls, Lello Bookstore and hidden murals"
          : "Mavi çiniler ve urban sanat: Ruhlar Şapeli, Lello Kitabevi ve gizli duvar resimleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/capela_das_almas.jpg",
        tags: ["Azulejo", isEnglish ? "Street Art" : "Sokak Sanatı", isEnglish ? "Art" : "Sanat"],
        placeNames: ["Capela das Almas", "Livraria Lello", "Igreja do Carmo & Carmelitas", "Street Art Porto", "Rua das Flores"],
        interests: ["Sanat", "Fotoğraf", "Kültür"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "por_views",
        name: isEnglish ? "Miradouros & Sunsets" : "Manzara & Günbatımı",
        description: isEnglish 
          ? "Porto's best viewpoints: Crystal Palace gardens, riverside sunsets and bridge panoramas"
          : "Porto'nun en iyi manzara noktaları: Kristal Saray bahçeleri, nehir kenarı gün batımları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/jardins_do_palacio_de_cristal.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Sunset" : "Günbatımı", isEnglish ? "Romantic" : "Romantik"],
        placeNames: ["Jardins do Palácio de Cristal", "Miradouro da Vitória", "Dom Luís I Köprüsü", "Foz do Douro"],
        interests: ["Manzara", "Fotoğraf", "Romantik"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "por_beach",
        name: isEnglish ? "Atlantic Coast & Foz" : "Atlantik Sahili & Foz",
        description: isEnglish 
          ? "Escape to the sea: Beach walks, fresh seafood in Matosinhos and ocean sunsets"
          : "Denize kaçış: Sahil yürüyüşleri, Matosinhos'ta taze deniz ürünleri ve okyanus gün batımları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/porto/foz_do_douro.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", isEnglish ? "Seafood" : "Deniz Ürünleri", isEnglish ? "Coastal" : "Sahil"],
        placeNames: ["Foz do Douro", "Matosinhos", "Praia do Carneiro", "Jardins do Palácio de Cristal"],
        interests: ["Plaj", "Yemek", "Doğa"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.beach_access,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BUDAPEŞTE ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBudapestRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bud_classic",
        name: isEnglish ? "Buda Castle & Historic Hills" : "Buda Kalesi & Tarihi Tepeler",
        description: isEnglish 
          ? "The royal side: Castle District, Fisherman's Bastion and the majestic Matthias Church"
          : "Kraliyet tarafı: Kale Mahallesi, Balıkçı Kalesi ve görkemli Matthias Kilisesi.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/buda_kalesi.jpg",
        tags: [isEnglish ? "Castle" : "Kale", isEnglish ? "Historical" : "Tarihi", "UNESCO"],
        placeNames: ["Buda Kalesi", "Balıkçı Kalesi", "Matthias Kilisesi", "Gellért Tepesi", "Zincir Köprüsü"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "bud_thermal",
        name: isEnglish ? "Thermal Baths Journey" : "Termal Hamam Turu",
        description: isEnglish 
          ? "Soak in history: World-famous thermal baths from Ottoman to Art Nouveau"
          : "Tarihe dalın: Osmanlı'dan Art Nouveau'ya dünyaca ünlü termal hamamlar.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/szechenyi_termal_hamami.jpg",
        tags: [isEnglish ? "Thermal" : "Termal", "Spa", isEnglish ? "Relax" : "Huzur"],
        placeNames: ["Széchenyi Termal Hamamı", "Gellért Hamamı", "Rudas Hamamı", "Vajdahunyad Kalesi"],
        interests: ["Wellness", "Romantik"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.hot_tub,
      ),
      CuratedRoute(
        id: "bud_ruin",
        name: isEnglish ? "Ruin Bars & Jewish Quarter" : "Harabe Barlar & Yahudi Mahallesi",
        description: isEnglish 
          ? "The legendary nightlife: Iconic ruin bars, historic synagogue and street art"
          : "Efsanevi gece hayatı: İkonik harabe barlar, tarihi sinagog ve sokak sanatı.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/szimpla_kert.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Ruin Bars" : "Harabe Bar", isEnglish ? "Party" : "Eğlence"],
        placeNames: ["Szimpla Kert", "Instant-Fogas Complex", "Dohány Synagogu", "Gettó Gulyás"],
        interests: ["Gece Hayatı", "Kültür"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "bud_food",
        name: isEnglish ? "Hungarian Flavors" : "Macar Lezzetleri",
        description: isEnglish 
          ? "Culinary Budapest: Goulash, lángos, market halls and legendary cafés"
          : "Gastronomi Budapeşte: Gulaş, lángos, pazar salonları ve efsanevi kafeler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/merkez_pazar.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Goulash", isEnglish ? "Market" : "Pazar"],
        placeNames: ["Merkez Pazar", "Gettó Gulyás", "Retró Lángos Büfé", "New York Café"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "bud_danube",
        name: isEnglish ? "Danube Promenade" : "Tuna Sahili Yürüyüşü",
        description: isEnglish 
          ? "River romance: Parliament views, memorial shoes and evening cruises"
          : "Nehir romantizmi: Parlamento manzaraları, anıt ayakkabılar ve akşam tekneleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/parlamento.jpg",
        tags: [isEnglish ? "River" : "Nehir", isEnglish ? "Parliament" : "Parlamento", isEnglish ? "Romantic" : "Romantik"],
        placeNames: ["Parlamento", "Shoes on the Danube", "Zincir Köprüsü", "Tuna Nehir Gezisi", "Margaret Island (Margitsziget)"],
        interests: ["Romantik", "Fotoğraf", "Manzara"],
        accentColor: const Color(0xFFFF9800),
        icon: Icons.directions_boat,
      ),
      CuratedRoute(
        id: "bud_history",
        name: isEnglish ? "Dark History & Memorials" : "Karanlık Tarih & Anıtlar",
        description: isEnglish 
          ? "Moving stories: House of Terror, Hospital in the Rock and Cold War memories"
          : "Duygu dolu hikayeler: Terör Evi, Kayalık Hastane ve Soğuk Savaş anıları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/budapeste/house_of_terror.jpg",
        tags: [isEnglish ? "History" : "Tarih", isEnglish ? "Memorial" : "Anıt", "WWII"],
        placeNames: ["House of Terror", "Hospital in the Rock", "Memento Park", "Dohány Synagogu"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.history_edu,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BANGKOK ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBangkokRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bkk_temples",
        name: isEnglish ? "Temple & Palace Grandeur" : "Tapınak & Saray İhtişamı",
        description: isEnglish 
          ? "The sacred Bangkok: Grand Palace, reclining Buddha and the Temple of Dawn"
          : "Kutsal Bangkok: Büyük Saray, yatan Buda ve Şafak Tapınağı.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "6 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg",
        tags: [isEnglish ? "Temple" : "Tapınak", isEnglish ? "Palace" : "Saray", isEnglish ? "Sacred" : "Kutsal"],
        placeNames: ["Grand Palace", "Wat Pho", "Wat Arun", "Wat Saket (Golden Mount)", "Wat Traimit (Golden Buddha)"],
        interests: ["Kültür", "Tarih", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.temple_buddhist,
      ),
      CuratedRoute(
        id: "bkk_street",
        name: isEnglish ? "Street Food Safari" : "Sokak Yemekleri Safarisi",
        description: isEnglish 
          ? "Legendary flavors: Chinatown noodles, night markets and hidden food gems"
          : "Efsanevi tatlar: Chinatown noodle'ları, gece pazarları ve gizli lezzet durakları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/chinatown_yaowarat.jpg",
        tags: [isEnglish ? "Street Food" : "Sokak Yemeği", isEnglish ? "Night Market" : "Gece Pazarı", "Chinatown"],
        placeNames: ["Chinatown (Yaowarat)", "Jodd Fairs", "Pak Khlong Talat", "Chatuchak Pazarı"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "bkk_river",
        name: isEnglish ? "Chao Phraya River Life" : "Chao Phraya Nehir Hayatı",
        description: isEnglish 
          ? "Explore by boat: Floating markets, riverside temples and sunset cocktails"
          : "Tekneyle keşfedin: Yüzen pazarlar, nehir kenarı tapınakları ve gün batımı kokteylleri.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "15 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/chao_phraya_nehri_teknesi.jpg",
        tags: [isEnglish ? "River" : "Nehir", isEnglish ? "Boat" : "Tekne", isEnglish ? "Floating Market" : "Yüzen Pazar"],
        placeNames: ["Chao Phraya Nehri Teknesi", "Floating Market", "Wat Arun", "Asiatique The Riverfront"],
        interests: ["Macera", "Fotoğraf"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.directions_boat,
      ),
      CuratedRoute(
        id: "bkk_night",
        name: isEnglish ? "Bangkok After Dark" : "Gece Bangkok",
        description: isEnglish 
          ? "The city that never sleeps: Rooftop bars, night markets and Thai nightlife"
          : "Hiç uyumayan şehir: Çatı barları, gece pazarları ve Tayland gece hayatı.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/rooftop_barlar.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Rooftop" : "Çatı Bar", isEnglish ? "Party" : "Eğlence"],
        placeNames: ["Rooftop Barlar", "Khao San Road", "Soi Cowboy", "Mahanakhon SkyWalk"],
        interests: ["Gece Hayatı", "Manzara"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "bkk_shopping",
        name: isEnglish ? "Shopping Paradise" : "Alışveriş Cenneti",
        description: isEnglish 
          ? "From mega malls to weekend markets: Bangkok's legendary shopping scene"
          : "Devasa AVM'lerden hafta sonu pazarlarına: Bangkok'un efsanevi alışveriş sahnesi.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/chatuchak_pazari.jpg",
        tags: [isEnglish ? "Shopping" : "Alışveriş", isEnglish ? "Markets" : "Pazarlar", isEnglish ? "Malls" : "AVM"],
        placeNames: ["Chatuchak Pazarı", "MBK Center", "Terminal 21 Asok", "ICONSIAM", "Siam Paragon"],
        interests: ["Alışveriş"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.shopping_bag,
      ),
      CuratedRoute(
        id: "bkk_wellness",
        name: isEnglish ? "Thai Massage & Wellness" : "Tai Masajı & Wellness",
        description: isEnglish 
          ? "Relax and rejuvenate: Traditional Thai massage and peaceful temples"
          : "Rahatlayın ve yenilenin: Geleneksel Tai masajı ve huzurlu tapınaklar.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/thai_masaj.jpg",
        tags: [isEnglish ? "Massage" : "Masaj", "Wellness", isEnglish ? "Relax" : "Huzur"],
        placeNames: ["Thai Masaj", "Wat Pho", "Lumpini Park", "Wat Benchamabophit"],
        interests: ["Wellness", "Huzur"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.spa,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SİNGAPUR ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSingaporeRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sgp_iconic",
        name: isEnglish ? "Singapore Iconic Landmarks" : "Singapur İkonları",
        description: isEnglish 
          ? "The postcard shots: Marina Bay Sands, Gardens by the Bay and Merlion"
          : "Kartpostal kareleri: Marina Bay Sands, Gardens by the Bay ve Merlion.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/singapur/gardens_by_the_bay.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Marina Bay", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Gardens by the Bay", "Marina Bay Sands", "Merlion Park", "Helix Bridge", "ArtScience Museum", "Spectra Light Show", "Supertree Grove"],
        interests: ["Fotoğraf", "Mimari", "Manzara"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "sgp_hawker",
        name: isEnglish ? "Hawker Food Adventure" : "Hawker Yemek Macerası",
        description: isEnglish 
          ? "UNESCO-listed food culture: Best hawker centres and chilli crab"
          : "UNESCO listesindeki yemek kültürü: En iyi hawker center'ları ve chilli crab.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/singapur/hawker_centre.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Hawker", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Lau Pa Sat Hawker Centre", "Maxwell Food Centre", "Chinatown Complex Food Centre", "Old Airport Road Food Centre", "Ya Kun Kaya Toast (Amoy St)"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "sgp_heritage",
        name: isEnglish ? "Cultural Neighborhoods" : "Kültürel Mahalleler",
        description: isEnglish 
          ? "Multicultural harmony: Chinatown, Little India and Kampong Glam"
          : "Çok kültürlü uyum: Chinatown, Little India ve Kampong Glam.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "7 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/chinatown_yaowarat.jpg",
        tags: [isEnglish ? "Culture" : "Kültür", isEnglish ? "Heritage" : "Miras", isEnglish ? "Neighborhoods" : "Mahalleler"],
        placeNames: ["Chinatown", "Little India", "Haji Lane", "Sultan Mosque", "Buddha Tooth Relic Temple", "Sri Mariamman Temple", "Arab Street"],
        interests: ["Kültür", "Fotoğraf", "Tarih"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.temple_hindu,
      ),
      CuratedRoute(
        id: "sgp_nature",
        name: isEnglish ? "Green Singapore" : "Yeşil Singapur",
        description: isEnglish 
          ? "The garden city: Botanic gardens, treetop walks and reservoir adventures"
          : "Bahçe şehri: Botanik bahçeleri, ağaç tepesi yürüyüşleri ve rezervuar maceraları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/singapur/singapore_botanic_gardens.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", isEnglish ? "Parks" : "Parklar", isEnglish ? "Gardens" : "Bahçeler"],
        placeNames: ["Singapore Botanic Gardens", "Gardens by the Bay", "MacRitchie Reservoir", "Fort Canning Park", "Sungei Buloh Wetland Reserve"],
        interests: ["Doğa", "Yürüyüş", "Huzur"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "sgp_sentosa",
        name: isEnglish ? "Sentosa Island Fun" : "Sentosa Adası Eğlencesi",
        description: isEnglish 
          ? "Theme park paradise: Universal Studios, aquarium and beach clubs"
          : "Tema parkı cenneti: Universal Studios, akvaryum ve plaj kulüpleri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/singapur/sentosa_island.jpg",
        tags: [isEnglish ? "Theme Park" : "Tema Parkı", isEnglish ? "Beach" : "Plaj", isEnglish ? "Family" : "Aile"],
        placeNames: ["Sentosa Island", "Universal Studios Singapore", "S.E.A. Aquarium", "Skyline Luge Sentosa", "Siloso Beach", "Wings of Time Show"],
        interests: ["Macera", "Aile", "Eğlence"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.attractions,
      ),
      CuratedRoute(
        id: "sgp_night",
        name: isEnglish ? "Singapore After Dark" : "Gece Singapur",
        description: isEnglish 
          ? "Night magic: Light shows, rooftop bars and nocturnal wildlife"
          : "Gece sihri: Işık gösterileri, çatı barları ve gece hayvanat bahçesi.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/singapur/gardens_by_the_bay.jpg",
        tags: [isEnglish ? "Night" : "Gece", isEnglish ? "Light Show" : "Işık Gösterisi", isEnglish ? "Rooftop" : "Çatı Bar"],
        placeNames: ["Gardens by the Bay", "Marina Bay Sands", "Clarke Quay", "Night Safari"],
        interests: ["Gece Hayatı", "Romantik"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // KOPENHAG ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getCopenhagenRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "cph_classic",
        name: isEnglish ? "Copenhagen Essentials" : "Kopenhag Klasikleri",
        description: isEnglish 
          ? "The must-sees: Colorful Nyhavn, Little Mermaid and Tivoli Gardens"
          : "Mutlaka görülecekler: Renkli Nyhavn, Küçük Deniz Kızı ve Tivoli Bahçeleri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "7 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/oslo/stroget.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Nyhavn", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Nyhavn", "Tivoli Bahçeleri", "Küçük Deniz Kızı", "Amalienborg Sarayı", "Strøget"],
        interests: ["Turist", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "cph_design",
        name: isEnglish ? "Danish Design & Architecture" : "Danimarka Tasarımı & Mimarisi",
        description: isEnglish 
          ? "Scandinavian aesthetics: Design museum, iconic furniture and modern architecture"
          : "İskandinav estetiği: Tasarım müzesi, ikonik mobilyalar ve modern mimari.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: [isEnglish ? "Design" : "Tasarım", isEnglish ? "Architecture" : "Mimari", isEnglish ? "Modern" : "Modern"],
        placeNames: ["Designmuseum Danmark", "Hay House", "Illums Bolighus", "CopenHill (Amager Bakke)", "Superkilen Parkı"],
        interests: ["Tasarım", "Mimari"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.design_services,
      ),
      CuratedRoute(
        id: "cph_hygge",
        name: isEnglish ? "Hygge & Coffee Culture" : "Hygge & Kahve Kültürü",
        description: isEnglish 
          ? "Cozy Copenhagen: World-class coffee, pastries and the Danish art of hygge"
          : "Rahat Kopenhag: Dünya sınıfı kahve, pastalar ve Danimarka'nın hygge sanatı.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/the_coffee.jpg",
        tags: ["Hygge", isEnglish ? "Coffee" : "Kahve", isEnglish ? "Cozy" : "Rahat"],
        placeNames: ["The Coffee Collective", "Democratic Coffee", "Atelier September", "Andersen Bakery", "Hart Bageri"],
        interests: ["Kahve", "Huzur"],
        accentColor: const Color(0xFF795548),
        icon: Icons.coffee,
      ),
      CuratedRoute(
        id: "cph_food",
        name: isEnglish ? "New Nordic Cuisine" : "Yeni İskandinav Mutfağı",
        description: isEnglish 
          ? "Gastronomic Copenhagen: From food halls to Michelin stars"
          : "Gastronomi Kopenhagı: Yemek salonlarından Michelin yıldızlarına.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Nordic", "Michelin"],
        placeNames: ["Torvehallerne", "Reffen Street Food", "Gasoline Grill", "Hija de Sanchez", "WarPigs"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "cph_royal",
        name: isEnglish ? "Royal Copenhagen" : "Kraliyet Kopenhag",
        description: isEnglish 
          ? "Royal heritage: Palaces, crown jewels and the changing of the guard"
          : "Kraliyet mirası: Saraylar, taç mücevherleri ve nöbet değişimi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/strazburg/christian.jpg",
        tags: [isEnglish ? "Royal" : "Kraliyet", isEnglish ? "Palace" : "Saray", isEnglish ? "History" : "Tarih"],
        placeNames: ["Amalienborg Sarayı", "Rosenborg Kalesi", "Christiansborg Sarayı", "Mermer Kilise (Frederiks Kirke)", "Kastellet"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "cph_alt",
        name: isEnglish ? "Alternative Copenhagen" : "Alternatif Kopenhag",
        description: isEnglish 
          ? "The unconventional side: Freetown Christiania and creative neighborhoods"
          : "Alışılmadık taraf: Christiania Özgür Bölgesi ve yaratıcı mahalleler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/strazburg/christian.jpg",
        tags: [isEnglish ? "Alternative" : "Alternatif", "Christiania", isEnglish ? "Creative" : "Yaratıcı"],
        placeNames: ["Freetown Christiania", "Superkilen Parkı", "Reffen Street Food", "CopenHill (Amager Bakke)"],
        interests: ["Alternatif", "Sanat"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.explore,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MARAKEŞ ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getMarrakechRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "mar_medina",
        name: isEnglish ? "Medina & Souks Maze" : "Medina & Çarşı Labirenti",
        description: isEnglish 
          ? "The heart of Morocco: Jemaa el-Fna, spice souks and hidden riads"
          : "Fas'ın kalbi: Jemaa el-Fna, baharat çarşıları ve gizli riad'lar.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/jemaa_el_fna.jpg",
        tags: [isEnglish ? "Medina" : "Medina", "Souk", isEnglish ? "Traditional" : "Geleneksel"],
        placeNames: ["Jemaa el-Fna", "Souk Semmarine", "Rahba Kedima Square (Spice Square)", "Tanneries", "Ben Youssef Medersa"],
        interests: ["Kültür", "Alışveriş"],
        accentColor: WanderlustColors.accent,
        icon: Icons.store,
      ),
      CuratedRoute(
        id: "mar_palaces",
        name: isEnglish ? "Palaces & Gardens" : "Saraylar & Bahçeler",
        description: isEnglish 
          ? "Moroccan elegance: Bahia Palace, YSL's Majorelle and secret gardens"
          : "Fas zarafeti: Bahia Sarayı, YSL'nin Majorelle'i ve gizli bahçeler.",
        duration: isEnglish ? "5-6 hours" : "5-6 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/bahia_sarayi.jpg",
        tags: [isEnglish ? "Palace" : "Saray", isEnglish ? "Gardens" : "Bahçe", isEnglish ? "Elegant" : "Zarif"],
        placeNames: ["Bahia Sarayı", "Majorelle Bahçesi", "Musée Yves Saint Laurent", "Secret Garden", "Menara Gardens"],
        interests: ["Mimari", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "mar_food",
        name: isEnglish ? "Moroccan Flavors" : "Fas Lezzetleri",
        description: isEnglish 
          ? "Culinary journey: Tagine, couscous, rooftop cafés and cooking classes"
          : "Lezzet yolculuğu: Tajin, kuskus, çatı kafeleri ve yemek kursları.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/al_fassia.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Tagine", isEnglish ? "Cooking" : "Yemek Kursu"],
        placeNames: ["Al Fassia", "Cafés des Épices", "Rooftop Kafeler", "Cooking Class", "Jemaa el-Fna"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "mar_history",
        name: isEnglish ? "Historic Monuments" : "Tarihi Anıtlar",
        description: isEnglish 
          ? "Centuries of history: Ancient tombs, historic mosques and hidden museums"
          : "Yüzyıllık tarih: Kadim mezarlar, tarihi camiler ve gizli müzeler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/koutoubia_camii.jpg",
        tags: [isEnglish ? "History" : "Tarih", isEnglish ? "Monuments" : "Anıtlar", isEnglish ? "Heritage" : "Miras"],
        placeNames: ["Koutoubia Camii", "Saadian Tombs", "Ben Youssef Medersa", "Dar el Bacha (Musée des Confluences)", "El Badi Palace"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.mosque,
      ),
      CuratedRoute(
        id: "mar_hammam",
        name: isEnglish ? "Hammam & Wellness" : "Hamam & Wellness",
        description: isEnglish 
          ? "Moroccan spa rituals: Traditional hammams, argan oil treatments and relaxation"
          : "Fas spa ritüelleri: Geleneksel hamamlar, argan yağı bakımları ve rahatlama.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/les_bains_de_marrakech.png",
        tags: [isEnglish ? "Hammam" : "Hamam", "Spa", isEnglish ? "Wellness" : "Wellness"],
        placeNames: ["Les Bains de Marrakech", "El Fenn", "Heritage Spa", "La Mamounia Garden Spa", "Hammam de la Rose"],
        interests: ["Wellness", "Huzur", "Kültür"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.spa,
      ),
      CuratedRoute(
        id: "mar_desert",
        name: isEnglish ? "Desert & Mountains" : "Çöl & Dağlar",
        description: isEnglish 
          ? "Beyond the city: Agafay desert, Atlas mountains and Berber villages"
          : "Şehrin ötesi: Agafay çölü, Atlas dağları ve Berber köyleri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "100 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/agafay_colu.jpg",
        tags: [isEnglish ? "Desert" : "Çöl", isEnglish ? "Mountains" : "Dağlar", isEnglish ? "Adventure" : "Macera"],
        placeNames: ["Agafay Çölü", "Atlas Dağları Günübirlik", "Essaouira Günübirlik", "Ouzoud Waterfalls"],
        interests: ["Macera", "Doğa"],
        accentColor: const Color(0xFF795548),
        icon: Icons.terrain,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // DİĞER ŞEHİRLER (Stub - Sadece generic routes üretilecek)
  // ═══════════════════════════════════════════════════════════════════════════
  // ═══════════════════════════════════════════════════════════════════════════
  // NAPOLI ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getNaplesRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "nap_classic",
        name: isEnglish ? "Naples Essentials" : "Napoli Klasikleri",
        description: isEnglish 
          ? "The soul of the city: Spaccanapoli, historic castles and underground secrets"
          : "Şehrin ruhu: Spaccanapoli, tarihi kaleler ve yeraltı sırları.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/spaccanapoli.jpg",
        tags: [isEnglish ? "History" : "Tarih", isEnglish ? "Culture" : "Kültür", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Spaccanapoli", "Napoli Sotterranea", "Castel dell'Ovo", "Piazza del Plebiscito", "Castel Nuovo"],
        interests: ["Tarih", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "nap_pizza",
        name: isEnglish ? "The Pizza Pilgrimage" : "Pizza Hacıları",
        description: isEnglish 
          ? "Eat,pray, love pizza: The world's most famous pizzerias and street food"
          : "Pizza aşkına: Dünyanın en ünlü pizzacıları ve sokak lezzetleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/pizzeria_da_michele.jpg",
        tags: [isEnglish ? "Pizza" : "Pizza", "Food", isEnglish ? "Culinary" : "Gastronomi"],
        placeNames: ["Pizzeria Da Michele", "Gino Sorbillo Pizzeria", "Pintauro", "Passione di Sofi"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.local_pizza,
      ),
      CuratedRoute(
        id: "nap_maradona",
        name: isEnglish ? "Maradona & Spanish Quarter" : "Maradona & İspanyol Mahallesi",
        description: isEnglish 
          ? "Football faith: Murals, shrines and the vibrant Quartieri Spagnoli"
          : "Futbol inancı: Duvar resimleri, sunaklar ve canlı Quartieri Spagnoli.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/quartieri_spagnoli.jpg",
        tags: [isEnglish ? "Maradona" : "Maradona", isEnglish ? "Street Art" : "Sokak Sanatı", isEnglish ? "Vibrant" : "Canlı"],
        placeNames: ["Quartieri Spagnoli", "Maradona Mural", "Via Toledo"],
        interests: ["Kültür", "Sanat"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.sports_soccer,
      ),
      CuratedRoute(
        id: "nap_ancient",
        name: isEnglish ? "Pompeii & Vesuvius (Day Trip)" : "Pompei & Vezüv (Günübirlik)",
        description: isEnglish 
          ? "Volcanic history: The frozen city of Pompeii and the mighty volcano crater"
          : "Volkanik tarih: Donmuş şehir Pompei ve kudretli volkan krateri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "25 km",
        difficulty: isEnglish ? "Hard" : "Zor",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/pompei.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Pompeii", isEnglish ? "Volcano" : "Volkan"],
        placeNames: ["Pompei", "Mount Vesuvius", "Herculaneum"],
        interests: ["Tarih", "Macera"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.volcano,
      ),
      CuratedRoute(
        id: "nap_views",
        name: isEnglish ? "Views of the Gulf" : "Körfez Manzaraları",
        description: isEnglish 
          ? "Panoramic beauty: Castles, waterfronts and stunning sunsets over the sea"
          : "Panoramik güzellik: Kaleler, sahil şeridi ve deniz üzerinde muhteşem gün batımları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/castel_santelmo.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Sea" : "Deniz", "Castel"],
        placeNames: ["Castel Sant'Elmo", "Certosa di San Martino", "Lungomare Caracciolo", "Posillipo"],
        interests: ["Manzara", "Fotoğraf"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.camera_alt,
      ),
      CuratedRoute(
        id: "nap_amalfi",
        name: isEnglish ? "Amalfi & Capri (Day Trip)" : "Amalfi & Capri (Günübirlik)",
        description: isEnglish 
          ? "La Dolce Vita: Positano, Capri's Blue Grotto and coastal glamour"
          : "Tatlı Hayat: Positano, Capri'nin Mavi Mağarası ve sahil ihtişamı.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "50 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/napoli/amalfi_coast.jpg",
        tags: ["Amalfi", "Capri", isEnglish ? "Coast" : "Sahil"],
        placeNames: ["Amalfi Coast", "Capri", "Positano", "Sorrento"],
        interests: ["Manzara", "Lüks"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.beach_access,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MİLANO ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getMilanRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "mil_iconic",
        name: isEnglish ? "Milan Icons & Duomo" : "Milano İkonları & Duomo",
        description: isEnglish 
          ? "City of style: The magnificent cathedral, Galleria and La Scala opera"
          : "Stil şehri: Muhteşem katedral, Galleria ve La Scala operası.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/floransa/duomo_santa_maria_del_fiore.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Duomo", isEnglish ? "Must See" : "Görülmeli"],
        placeNames: ["Duomo di Milano", "Galleria Vittorio Emanuele II", "La Scala", "Castello Sforzesco", "Museo del Novecento"],
        interests: ["Mimari", "Tarih", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "mil_art",
        name: isEnglish ? "Da Vinci & Fine Art" : "Da Vinci & Güzel Sanatlar",
        description: isEnglish 
          ? "Masterpieces: The Last Supper and Brera's artistic treasures"
          : "Başyapıtlar: Son Akşam Yemeği ve Brera'nın sanatsal hazineleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/milano/son_aksam_yemegi_lultima_cena.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Da Vinci", isEnglish ? "Museum" : "Müze"],
        placeNames: ["Son Akşam Yemeği (L'Ultima Cena)", "Pinacoteca di Brera", "Basilica di Sant'Ambrogio", "Chiesa di San Maurizio"],
        interests: ["Sanat", "Tarih"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "mil_fashion",
        name: isEnglish ? "Fashion & Luxury" : "Moda & Lüks",
        description: isEnglish 
          ? "Fashion capital: Golden Rectangle boutiques and trendy vibes"
          : "Moda başkenti: Altın Dörtgen butikleri ve trendi atmosfer.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/milano/quadrilatero_della_moda.jpg",
        tags: [isEnglish ? "Fashion" : "Moda", isEnglish ? "Luxury" : "Lüks", "Shopping"],
        placeNames: ["Quadrilatero della Moda", "Galleria Vittorio Emanuele II", "La Rinascente", "Corso Como"],
        interests: ["Alışveriş", "Lüks"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.shopping_bag,
      ),
      CuratedRoute(
        id: "mil_navigli",
        name: isEnglish ? "Navigli & Nightlife" : "Navigli & Gece Hayatı",
        description: isEnglish 
          ? "Canal vibes: Aperitivo hour, sunset reflections and lively bars"
          : "Kanal havası: Aperitivo saati, gün batımı yansımaları ve canlı barlar.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/milano/navigli.jpg",
        tags: [isEnglish ? "Nightlife" : "Gece Hayatı", isEnglish ? "Canals" : "Kanallar", "Aperitivo"],
        placeNames: ["Navigli", "Darsena", "Mercato Metropolitano", "Porta Ticinese"],
        interests: ["Gece Hayatı", "Yemek"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.nightlife,
      ),
      CuratedRoute(
        id: "mil_modern",
        name: isEnglish ? "Modern Milan" : "Modern Milano",
        description: isEnglish 
          ? "Future city: Vertical forests, skyscrapers and contemporary spaces"
          : "Geleceğin şehri: Dikey ormanlar, gökdelenler ve çağdaş mekanlar.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/milano/bosco_verticale.jpg",
        tags: [isEnglish ? "Modern" : "Modern", "Architecture", isEnglish ? "Green" : "Yeşil"],
        placeNames: ["Bosco Verticale", "Porta Nuova", "Piazza Gae Aulenti", "Fondazione Prada (Bar Luce)"],
        interests: ["Mimari", "Fotoğraf"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.apartment,
      ),
      CuratedRoute(
        id: "mil_food",
        name: isEnglish ? "Milanese Flavors" : "Milano Lezzetleri",
        description: isEnglish 
          ? "Taste of Lombardy: Panerottis, saffron risotto and historic bakeries"
          : "Lombardiya tadı: Panerotti, safranlı risotto ve tarihi pastaneler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/milano/luini.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Bakery", isEnglish ? "Traditional" : "Geleneksel"],
        placeNames: ["Luini", "Pasticceria Marchesi", "Eataly Milano Smeraldo", "Terrazza Aperol"],
        interests: ["Yemek", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // VENEDİK ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getVeniceRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ven_iconic",
        name: isEnglish ? "Venice Essentials" : "Venedik Klasikleri",
        description: isEnglish 
          ? "The Grand Canal: St. Mark's Basilica, Rialto and the Doge's Palace"
          : "Büyük Kanal: San Marco Bazilikası, Rialto ve Dükler Sarayı.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/san_marco_meydani.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", isEnglish ? "Must See" : "Görülmeli", "Canal"],
        placeNames: ["San Marco Meydanı", "San Marco Bazilikası", "Rialto Köprüsü", "Dükler Sarayı (Palazzo Ducale)", "İç Çekiş Köprüsü"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "ven_islands",
        name: isEnglish ? "Murano & Burano Islands" : "Murano & Burano Adaları",
        description: isEnglish 
          ? "Glass & colors: Glassblowing in Murano and colorful houses of Burano"
          : "Cam & renkler: Murano'da cam üfleme ve Burano'nun renkli evleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/murano_adasi.jpg",
        tags: [isEnglish ? "Islands" : "Adalar", "Murano", "Burano", isEnglish ? "Colorful" : "Renkli"],
        placeNames: ["Murano Adası", "Burano Adası", "Torcello Adası"],
        interests: ["Sanat", "Fotoğraf", "Alışveriş"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.waves,
      ),
      CuratedRoute(
        id: "ven_gondola",
        name: isEnglish ? "Romantic Venice" : "Romantik Venedik",
        description: isEnglish 
          ? "Love on water: Gondola rides, sunset bridges and historic cafes"
          : "Suda aşk: Gondol gezileri, gün batımı köprüleri ve tarihi kafeler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/gondol_turu.jpg",
        tags: [isEnglish ? "Romantic" : "Romantik", "Gondola", isEnglish ? "Sunset" : "Gün Batımı"],
        placeNames: ["Gondol Turu", "Caffè Florian", "Accademia Köprüsü", "Santa Maria della Salute"],
        interests: ["Romantik", "Manzara"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.favorite,
      ),
      CuratedRoute(
        id: "ven_art",
        name: isEnglish ? "Art & Treasures" : "Sanat & Hazineler",
        description: isEnglish 
          ? "Venetian masters: Galleries, opera and intricate architecture"
          : "Venedik ustaları: Galeriler, opera ve girift mimari.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/gallerie_dellaccademia.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Museum", "Opera"],
        placeNames: ["Gallerie dell'Accademia", "Peggy Guggenheim Koleksiyonu", "Teatro La Fenice", "Scuola Grande di San Rocco"],
        interests: ["Sanat", "Kültür"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "ven_hidden",
        name: isEnglish ? "Hidden Venice" : "Gizli Venedik",
        description: isEnglish 
          ? "Off the beaten path: Quiet canals, bookshops and secret gardens"
          : "Alışılmışın dışında: Sessiz kanallar, kitapçılar ve gizli bahçeler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/libreria_acqua_alta.jpg",
        tags: [isEnglish ? "Hidden" : "Gizli", isEnglish ? "Quiet" : "Sessiz", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Libreria Acqua Alta", "Cannaregio", "Yahudi Getto", "Scala Contarini del Bovolo", "Dorsoduro"],
        interests: ["Keşif", "Fotoğraf"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.visibility_off,
      ),
      CuratedRoute(
        id: "ven_food",
        name: isEnglish ? "Cicchetti & Wine" : "Cicchetti & Şarap",
        description: isEnglish 
          ? "Venetian tapas: Hopping between bàcari bars for snacks and spritz"
          : "Venedik tapasları: Atıştırmalık ve spritz için bàcari barları gezintisi.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/venedik/rialto_pazari.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Cicchetti", "Wine"],
        placeNames: ["Rialto Pazarı", "Cicchetti & Bàcari", "Campo Santa Margherita"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.wine_bar,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ZÜRİH ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getZurichRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "zur_classic",
        name: isEnglish ? "Zurich Essentials" : "Zürih Klasikleri",
        description: isEnglish 
          ? "Old Town charm: History, coffee and Dada"
          : "Eski Şehir cazibesi: Tarih, kahve ve Dada.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Z%C3%BCrich_Switzerland-Grossm%C3%BCnster-01.jpg/800px-Z%C3%BCrich_Switzerland-Grossm%C3%BCnster-01.jpg",
        tags: [isEnglish ? "Old Town" : "Eski Şehir", "Cafe", isEnglish ? "History" : "Tarih"],
        placeNames: ["Grossmünster", "Fraumünster", "Cabaret Voltaire (Dada House)", "Café & Conditorei 1842", "Lindenhof"],
        interests: ["Tarih", "Mimari", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "zur_money",
        name: isEnglish ? "Luxury & Chocolate" : "Lüks & Çikolata",
        description: isEnglish 
          ? "Sweet life: Exclusive shopping, chocolate and dining"
          : "Tatlı hayat: Özel alışveriş, çikolata ve yemek.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zurih/bahnhofstrasse.jpg",
        tags: [isEnglish ? "Chocolate" : "Çikolata", "Shopping", "Food"],
        placeNames: ["Bahnhofstrasse", "Lindt Home of Chocolate", "Confiserie Sprüngli", "Paradeplatz", "Zeughauskeller"],
        interests: ["Alışveriş", "Yemek", "Tarih"],
        accentColor: const Color(0xFF795548),
        icon: Icons.shopping_bag,
      ),
      CuratedRoute(
        id: "zur_modern",
        name: isEnglish ? "Urban & Trendy West" : "Modern Batı Zürih",
        description: isEnglish 
          ? "Industrial cool: Viaduct shops, umbrella street and nightlife"
          : "Endüstriyel hava: Viyadük mağazaları, şemsiyeli sokak ve gece hayatı.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zurih/zurich_west_im_viadukt.jpg",
        tags: [isEnglish ? "Modern" : "Modern", "Food", "Hipster"],
        placeNames: ["Im Viadukt", "Frau Gerolds Garten", "Gerold Cuchi (Umbrella Street)", "Freitag Flagship Store", "Markthalle"],
        interests: ["Tasarım", "Alışveriş", "Yemek"],
        accentColor: const Color(0xFF1ABC9C),
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "zur_art",
        name: isEnglish ? "Art & Culture" : "Sanat & Kültür",
        description: isEnglish 
          ? "Cultural treasures: Museums, opera and gardens"
          : "Kültürel hazineler: Müzeler, opera ve bahçeler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zurih/kunsthaus_zurich.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Museum", "Opera"],
        placeNames: ["Kunsthaus Zürich", "Swiss National Museum", "Zürich Opera House", "Pavillon Le Corbusier", "Rietberg Museum"],
        interests: ["Sanat", "Tarih", "Mimari"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "zur_lake",
        name: isEnglish ? "Lake & Mountain" : "Göl & Dağ",
        description: isEnglish 
          ? "Nature escape: Lake promenade, boat trip and viewpoints"
          : "Doğa kaçamağı: Göl yolu, tekne turu ve manzaralar.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zurih/lake_zurich_zurichsee.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Lake", "View"],
        placeNames: ["Lake Zurich Promenade", "Bürkliplatz", "Uetliberg Mountain", "China Garden", "Seebad Enge"],
        interests: ["Doğa", "Manzara"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "zur_football",
        name: isEnglish ? "Football History" : "Futbol Tarihi",
        description: isEnglish 
          ? "For fans: FIFA museum and sports history"
          : "Taraftarlar için: FIFA müzesi ve spor tarihi.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "1 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zurih/fifa_world_football_museum.jpg",
        tags: ["Football", "FIFA", "Sports"],
        placeNames: ["FIFA World Football Museum", "Sportsbar 1904", "Enge"],
        interests: ["Spor", "Tarih"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.sports_soccer,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // CENEVRE ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getGenevaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "gva_peace",
        name: isEnglish ? "Capital of Peace" : "Barışın Başkenti",
        description: isEnglish 
          ? "Global diplomacy: UN, Red Cross and local flavors"
          : "Küresel diplomasi: BM, Kızıl Haç ve yerel lezzetler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Palais_des_Nations_Geneva.jpg/800px-Palais_des_Nations_Geneva.jpg",
        tags: [isEnglish ? "Diplomacy" : "Diplomasi", "Food", isEnglish ? "Park" : "Park"],
        placeNames: ["Palais des Nations", "Ariana Park", "Red Cross Museum", "Broken Chair", "Café du Soleil"],
        interests: ["Tarih", "Yemek", "Doğa"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.public,
      ),
      CuratedRoute(
        id: "gva_science",
        name: isEnglish ? "Science & Innovation" : "Bilim & İnovasyon",
        description: isEnglish 
          ? "Unlocking the universe: CERN, tram rides and science"
          : "Evrenin kilidini açmak: CERN, tramvay gezisi ve bilim.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Globe_of_Science_and_Innovation_CERN.jpg/800px-Globe_of_Science_and_Innovation_CERN.jpg",
        tags: ["Science", "CERN", "Tram"],
        placeNames: ["CERN Globe", "Microcosm", "Tram 18 Experience", "Meyrin Centre", "Bois de la Bâtie"],
        interests: ["Bilim", "Teknoloji", "Doğa"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.science,
      ),
      CuratedRoute(
        id: "gva_classic",
        name: isEnglish ? "Geneva Old & New" : "Eski & Yeni Cenevre",
        description: isEnglish 
          ? "City highlights: Jet d'Eau, Cathedral and fondue"
          : "Şehir özetleri: Jet d'Eau, Katedral ve fondü.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Jet_d%27eau_de_Gen%C3%A8ve_%28swiss%29.jpg/800px-Jet_d%27eau_de_Gen%C3%A8ve_%28swiss%29.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", "Fondue", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Jet d'Eau", "Jardin Anglais", "St. Pierre Cathedral", "Maison Tavel", "Restaurant Les Armures"],
        interests: ["Tarih", "Yemek", "Manzara"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "gva_luxury",
        name: isEnglish ? "Watchmaking & Luxury" : "Saatçilik & Lüks",
        description: isEnglish 
          ? "Timeless elegance: Swiss watches, chocolate and shopping"
          : "Zamansız zarafet: İsviçre saatleri, çikolata ve alışveriş.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/patek_philippe_museum.jpg",
        tags: [isEnglish ? "Watches" : "Saatler", "Shopping", "Chocolate"],
        placeNames: ["Patek Philippe Museum", "Rue du Rhône", "Manor Genève", "Confiserie Arn", "L'Horloge Fleurie"],
        interests: ["Alışveriş", "Sanat", "Yemek"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.watch,
      ),
      CuratedRoute(
        id: "gva_lake",
        name: isEnglish ? "Lake Geneva Relax" : "Cenevre Gölü Keyfi",
        description: isEnglish 
          ? "Lakeside leisure: Baths, parks and beach cafes"
          : "Göl kenarı keyfi: Hamamlar, parklar ve plaj kafeleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/bains_des_paquis.jpg",
        tags: [isEnglish ? "Lake" : "Göl", "Cafe", isEnglish ? "Relax" : "Huzur"],
        placeNames: ["Bains des Pâquis", "Baby Plage", "La Potinière", "Perle du Lac", "Jardin Botanique"],
        interests: ["Doğa", "Yemek", "Huzur"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.pool,
      ),
      CuratedRoute(
        id: "gva_bohemian",
        name: isEnglish ? "Bohemian Carouge" : "Bohem Carouge",
        description: isEnglish 
          ? "Mediterranean vibes: Cafes, cinema and artisan shops"
          : "Akdeniz havası: Kafeler, sinema ve zanaatkar dükkanları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/strazburg/place-du-marche-aux-cochons-de-lait.jpg",
        tags: [isEnglish ? "Bohemian" : "Bohem", "Cinema", "Cafe"],
        placeNames: ["Place du Marché", "Cinéma Bio", "Boulangerie Wolfisberg", "Rue Saint-Joseph", "Carouge Museum"],
        interests: ["Kültür", "Yemek", "Sanat"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.brush,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // LUZERN ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getLucerneRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "luc_classic",
        name: isEnglish ? "Lucerne Essentials" : "Luzern Klasikleri",
        description: isEnglish 
          ? "Medieval mix: Bridge, bakery and historic squares"
          : "Ortaçağ karışımı: Köprü, fırın ve tarihi meydanlar.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Luzern_Kapellbruecke.jpg/800px-Luzern_Kapellbruecke.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Food", isEnglish ? "Iconic" : "İkonik"],
        placeNames: ["Kapellbrücke", "Water Tower", "Rathaus Brauerei", "Jesuit Church", "Bachmann Bakery"],
        interests: ["Tarih", "Yemek", "Mimari"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "luc_walls",
        name: isEnglish ? "City Walls & Views" : "Şehir Surları & Manzara",
        description: isEnglish 
          ? "Historic hike: Towers, walls and local lunch"
          : "Tarihi yürüyüş: Kuleler, surlar ve yerel öğle yemeği.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: [isEnglish ? "Walls" : "Surlar", "View", "Food"],
        placeNames: ["Museggmauer", "Zyt Tower", "Männleturm", "Restaurant Lapin", "Bourbaki Panorama"],
        interests: ["Tarih", "Manzara", "Yemek"],
        accentColor: const Color(0xFF795548),
        icon: Icons.security,
      ),
      CuratedRoute(
        id: "luc_transport",
        name: isEnglish ? "Transport Museum & Beach" : "Ulaşım Müzesi & Plaj",
        description: isEnglish 
          ? "Family fun: Trains, planes and lakeside relax"
          : "Aile eğlencesi: Trenler, uçaklar ve göl kenarı keyfi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/swiss_museum_of_transport.jpg",
        tags: ["Museum", "Beach", "Family"],
        placeNames: ["Swiss Museum of Transport", "Planetarium", "Lido Luzern", "Verkehrshaus Filmtheatre", "Hans Erni Museum"],
        interests: ["Bilim", "Aile", "Doğa"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.directions_train,
      ),
      CuratedRoute(
        id: "luc_mountain",
        name: isEnglish ? "Pilatus Golden Round" : "Pilatus Altın Tur",
        description: isEnglish 
          ? "Alpine adventure: Boat, cogwheel train and summit dining"
          : "Alp macerası: Tekne, dişli tren ve zirvede yemek.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "20 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Mountain" : "Dağ", "Food", "Tram"],
        placeNames: ["Kriens Gondola", "Fräkmüntegg", "Pilatus Kulm", "Hotel Pilatus-Kulm Restaurant", "Alpnachstad"],
        interests: ["Doğa", "Macera", "Yemek"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "luc_lake",
        name: isEnglish ? "Lake Culture & Cafe" : "Göl Kültürü & Kafe",
        description: isEnglish 
          ? "Lakeside vibe: KKL culture, park and coffee"
          : "Göl kenarı havası: KKL kültürü, park ve kahve.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/kkl_luzern.jpg",
        tags: [isEnglish ? "Lake" : "Göl", "Cafe", "Art"],
        placeNames: ["KKL Luzern", "Inseli Park", "World Café", "Rosengart Collection", "Lake Promenade"],
        interests: ["Doğa", "Sanat", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.directions_boat,
      ),
      CuratedRoute(
        id: "luc_art",
        name: isEnglish ? "Art & Music Walk" : "Sanat & Müzik Yürüyüşü",
        description: isEnglish 
          ? "Cultural beats: Picasso, Wagner and concerts"
          : "Kültürel ritimler: Picasso, Wagner ve konserler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/rosengart_collection.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Music", "Museum"],
        placeNames: ["Rosengart Collection", "Richard Wagner Museum", "KKL Foyer", "Bourbaki Panorama", "Alpineum"],
        interests: ["Sanat", "Kültür"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.music_note,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // STOCKHOLM ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getStockholmRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sto_classic",
        name: isEnglish ? "Stockholm Old Town" : "Stockholm Eski Şehir",
        description: isEnglish 
          ? "Gamla Stan charm: Royal Palace, narrow alleys and Nobel Museum"
          : "Gamla Stan cazibesi: Kraliyet Sarayı, dar sokaklar ve Nobel Müzesi.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Stortorget_Stockholm_2016.jpg/800px-Stortorget_Stockholm_2016.jpg",
        tags: [isEnglish ? "Old Town" : "Eski Şehir", isEnglish ? "History" : "Tarih", isEnglish ? "Royal" : "Kraliyet"],
        placeNames: ["Gamla Stan", "Stockholm Sarayı", "Stortorget", "Nobel Ödülü Müzesi", "Riddarholmen Kilisesi"],
        interests: ["Tarih", "Mimari", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "sto_museums",
        name: isEnglish ? "Djurgården Museums" : "Djurgården Müzeleri",
        description: isEnglish 
          ? "Cultural island: Vasa ship, ABBA Museum and open-air history"
          : "Kültür adası: Vasa gemisi, ABBA Müzesi ve açık hava tarihi.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Vasa_ship_stern.jpg/800px-Vasa_ship_stern.jpg",
        tags: ["Museum", "History", "ABBA"],
        placeNames: ["Vasa Müzesi", "Skansen Açık Hava Müzesi", "Abba The Museum", "Nordiska Müzesi"],
        interests: ["Tarih", "Müzik", "Kültür"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "sto_metro",
        name: isEnglish ? "Metro Art Gallery" : "Metro Sanat Galerisi",
        description: isEnglish 
          ? "Underground art: The world's longest art gallery in metro stations"
          : "Yeraltı sanatı: Metro istasyonlarında dünyanın en uzun sanat galerisi.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/T-Centralen_metro_station_Stockholm_2016_01.jpg/800px-T-Centralen_metro_station_Stockholm_2016_01.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Metro", isEnglish ? "Unique" : "Benzersiz"],
        placeNames: ["T-Centralen Metro İstasyonu", "Solna Centrum Metro İstasyonu", "Kungsträdgården Metro İstasyonu", "Stadion Metro İstasyonu"],
        interests: ["Sanat", "Fotoğraf"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.subway,
      ),
      CuratedRoute(
        id: "sto_photo",
        name: isEnglish ? "Views & Photography" : "Manzara & Fotoğraf",
        description: isEnglish 
          ? "Best panoramas: City Hall tower, Monteliusvägen and photography museum"
          : "En iyi panoramalar: Belediye Binası kulesi, Monteliusvägen ve fotoğraf müzesi.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/san_sebastian/ayuntamiento-de-san-sebastian.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Photography" : "Fotoğraf", isEnglish ? "Scenic" : "Manzaralı"],
        placeNames: ["Stockholm City Hall (Stadshuset)", "Fotografiska Museum", "Monteliusvägen Panoramic Path", "Fjällgatan Lookout", "Skinnarviksberget"],
        interests: ["Manzara", "Sanat", "Fotoğraf"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.camera_alt,
      ),
      CuratedRoute(
        id: "sto_archipelago",
        name: isEnglish ? "Archipelago Adventure" : "Takimada Macerası",
        description: isEnglish 
          ? "Island hopping: Boat tours to Fjäderholmarna or Vaxholm"
          : "Ada turu: Fjäderholmarna veya Vaxholm'a tekne turları.",
        duration: isEnglish ? "Half day" : "Yarım gün",
        distance: "15 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", isEnglish ? "Boat" : "Tekne", isEnglish ? "Islands" : "Adalar"],
        placeNames: ["Stockholm Archipelago Boat Tour", "Fjäderholmarna Islands", "Vaxholm Fortress", "Grinda Island", "Sandhamn"],
        interests: ["Doğa", "Huzur", "Macera"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.directions_boat,
      ),
      CuratedRoute(
        id: "sto_royal",
        name: isEnglish ? "Royal Drottningholm" : "Kraliyet Drottningholm",
        description: isEnglish 
          ? "UNESCO heritage: The magnificent Drottningholm Palace and gardens"
          : "UNESCO mirası: Muhteşem Drottningholm Sarayı ve bahçeleri.",
        duration: isEnglish ? "Half day" : "Yarım gün",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/kin.jpg",
        tags: [isEnglish ? "Royal" : "Kraliyet", "Palace", "UNESCO"],
        placeNames: ["Drottningholm Palace", "Chinese Pavilion", "Drottningholm Court Theatre", "Royal Palace Gardens", "Kina Slott"],
        interests: ["Tarih", "Mimari", "Kültür"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.account_balance,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // HONG KONG ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getHongKongRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "hk_iconic",
        name: isEnglish ? "HK Skyline & Peak" : "HK Silueti & Zirve",
        description: isEnglish 
          ? "The vertical city: Victoria Peak views, Star Ferry and light show"
          : "Dikey şehir: Victoria Zirvesi manzaraları, Star Ferry ve ışık şovu.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/victoria_peak.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", isEnglish ? "Views" : "Manzara", isEnglish ? "Skyline" : "Siluet"],
        placeNames: ["Victoria Peak", "Star Ferry", "Avenue of Stars", "Symphony of Lights", "Sky100"],
        interests: ["Manzara", "Fotoğraf"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "hk_culture",
        name: isEnglish ? "Temples & Tradition" : "Tapınaklar & Gelenek",
        description: isEnglish 
          ? "Spiritual center: Famous temples, incense coils and serene gardens"
          : "Ruhani merkez: Ünlü tapınaklar, tütsü bobinleri ve huzurlu bahçeler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/man_mo_temple.jpg",
        tags: [isEnglish ? "Culture" : "Kültür", "Temple", isEnglish ? "History" : "Tarih"],
        placeNames: ["Man Mo Temple", "Wong Tai Sin Temple", "Chi Lin Nunnery", "Nan Lian Garden", "Ten Thousand Buddhas Monastery"],
        interests: ["Kültür", "Fotoğraf", "Tarih"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.temple_buddhist,
      ),
      CuratedRoute(
        id: "hk_urban",
        name: isEnglish ? "Urban Jungle & Markets" : "Şehir Ormanı & Pazarlar",
        description: isEnglish 
          ? "Street energy: Mong Kok markets, neon lights and escalators"
          : "Sokak enerjisi: Mong Kok pazarları, neon ışıklar ve yürüyen merdivenler.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mong_kok.jpg",
        tags: [isEnglish ? "Markets" : "Pazarlar", isEnglish ? "Urban" : "Şehir", "Neon"],
        placeNames: ["Mong Kok (Ladies Market)", "Temple Street Night Market", "Central-Mid-Levels Escalator", "Choi Hung Estate", "Sneaker Street"],
        interests: ["Alışveriş", "Fotoğraf", "Lokal"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.store_mall_directory,
      ),
      CuratedRoute(
        id: "hk_lantau",
        name: isEnglish ? "Big Buddha & Lantau" : "Büyük Buda & Lantau",
        description: isEnglish 
          ? "Island escape: Cable car ride to the giant Buddha and fishing village"
          : "Ada kaçamağı: Büyük Buda'ya teleferik yolculuğu ve balıkçı köyü.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "10 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/big_buddha.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Buddha", "Cable Car"],
        placeNames: ["Tian Tan Big Buddha", "Po Lin Monastery", "Ngong Ping 360 Cable Car", "Tai O Fishing Village", "Wisdom Path"],
        interests: ["Doğa", "Kültür", "Huzur"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "hk_food",
        name: isEnglish ? "Dim Sum & Delights" : "Dim Sum & Lezzetler",
        description: isEnglish 
          ? "Culinary heaven: Michelin dim sum, egg tarts and tea houses"
          : "Lezzet cenneti: Michelin'li dim sum, yumurtalı tartlar ve çay evleri.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/tim_ho_wan.jpg",
        tags: [isEnglish ? "Food" : "Yemek", "Dim Sum", isEnglish ? "Local" : "Lokal"],
        placeNames: ["Tim Ho Wan (Sham Shui Po)", "Kam's Roast Goose", "Lan Fong Yuen (Milk Tea)", "Tai Cheong Bakery", "Yat Lok Roast Goose"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "hk_transport",
        name: isEnglish ? "Tram & Ferry Nostalgia" : "Tramvay & Feribot Nostaljisi",
        description: isEnglish 
          ? "Moving history: Riding the Ding Ding tram and Star Ferry"
          : "Hareketli tarih: Ding Ding tramvayı ve Star Feribotu gezisi.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/hong_kong_tramway.jpg",
        tags: ["Transport", "History", "Views"],
        placeNames: ["Hong Kong Tramway (Ding Ding)", "Star Ferry (Tsim Sha Tsui)", "Peak Tram", "Central Ferry Pier", "Hong Kong Observation Wheel"],
        interests: ["Tarih", "Manzara", "Fotoğraf"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.tram,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SEUL ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSeoulRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sel_royal",
        name: isEnglish ? "Royal Seoul" : "Kraliyet Seul'u",
        description: isEnglish 
          ? "Dynasty days: Grand palaces, changing of the guard and Hanok village"
          : "Hanedanlık günleri: Büyük saraylar, nöbet değişimi ve Hanok köyü.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/gyeongbokgung_sarayi.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Palace", isEnglish ? "Culture" : "Kültür"],
        placeNames: ["Gyeongbokgung Sarayı", "Changdeokgung Palace & Secret Garden", "Bukchon Hanok Köyü", "Insadong Culture Street", "Jogyesa Temple"],
        interests: ["Tarih", "Mimari", "Fotoğraf", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "sel_modern",
        name: isEnglish ? "Futuristic Seoul" : "Fütüristik Seul",
        description: isEnglish 
          ? "Modern marvels: Zaha Hadid's DDP, skyscrapers and Gangnam style"
          : "Modern harikalar: Zaha Hadid'in DDP'si, gökdelenler ve Gangnam stili.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/dongdaemun_design_plaza.jpg",
        tags: [isEnglish ? "Modern" : "Modern", "Architecture", "Shopping"],
        placeNames: ["Dongdaemun Design Plaza (DDP)", "Lotte World Tower (Seoul Sky)", "Starfield Library (COEX Mall)", "Banpo Bridge Moonlight Rainbow Fountain", "Gangnam District"],
        interests: ["Mimari", "Alışveriş", "Manzara"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "sel_shopping",
        name: isEnglish ? "Shopping & Youth" : "Alışveriş & Gençlik",
        description: isEnglish 
          ? "Trendsetter: Myeongdong beauty, Hongdae street art and fashion"
          : "Trend belirleyici: Myeongdong güzelliği, Hongdae sokak sanatı ve moda.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/myeongdong_shopping_street.jpg",
        tags: ["Shopping", "Fashion", "K-Pop"],
        placeNames: ["Myeongdong Shopping Street", "Hongdae (Hongik University Street)", "Hwayang-dong (Konkuk Univ)", "Ewha Womans University Area", "Stylenanda Pink Hotel"],
        interests: ["Alışveriş", "Eğlence", "Kültür"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.shopping_bag,
      ),
      CuratedRoute(
        id: "sel_food",
        name: isEnglish ? "K-Food Adventure" : "Kore Yemek Macerası",
        description: isEnglish 
          ? "Spicy & savory: Street food markets, Korean BBQ and fried chicken"
          : "Baharatlı & lezzetli: Sokak yemek pazarları, Kore Barbeküsü ve kızarmış tavuk.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/gwangjang_market.jpg",
        tags: ["Food", "BBQ", "Street Food"],
        placeNames: ["Gwangjang Market (Mayak Kimbap)", "Myeongdong Kyoja", "Myeongdong Street Food", "Tosokchon Samgyetang (Chicken Soup)", "Sulbing (Bingsu Dessert)"],
        interests: ["Yemek", "Lokal", "Kültür"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "sel_views",
        name: isEnglish ? "Panoramic Seoul" : "Panoramik Seul",
        description: isEnglish 
          ? "City from above: Namsan Tower and ancient city walls"
          : "Yukarıdan şehir: Namsan Kulesi ve antik şehir surları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/n_seoul_tower.jpg",
        tags: [isEnglish ? "Views" : "Manzara", "Tower", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["N Seoul Tower", "Namsan Park & Cable Car", "Hanyangdoseong (Ancient City Wall)", "Bugak Skyway", "Cheonggyecheon Stream Walk"],
        interests: ["Manzara", "Doğa", "Yürüyüş"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.visibility,
      ),
      CuratedRoute(
        id: "sel_history",
        name: isEnglish ? "War & Peace" : "Savaş & Barış",
        description: isEnglish 
          ? "Remembering history: War Memorial and DMZ trips"
          : "Tarihi hatırlamak: Savaş Anıtı ve DMZ gezileri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "50 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/seul/war_memorial_of_korea.jpg",
        tags: [isEnglish ? "History" : "Tarih", "DMZ", "War"],
        placeNames: ["War Memorial of Korea", "Imjingak Resort (DMZ)"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.history,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // NİCE ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getNiceRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "nce_promenade",
        name: isEnglish ? "Promenade & Old Town" : "Promenade & Eski Şehir",
        description: isEnglish 
          ? "The French Riviera spirit: Seafront walks, colorful markets and Castle Hill"
          : "Fransız Rivierası ruhu: Deniz kenarı yürüyüşleri, renkli pazarlar ve Kale Tepesi.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/nice/promenade_des_anglais.jpg",
        tags: [isEnglish ? "Sea" : "Deniz", "Old Town", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Promenade des Anglais", "Vieux Nice (Old Town)", "Cours Saleya Market", "Colline du Château (Castle Hill)", "Tour Bellanda"],
        interests: ["Manzara", "Fotoğraf", "Alışveriş"],
        accentColor: WanderlustColors.accent,
        icon: Icons.beach_access,
      ),
      CuratedRoute(
        id: "nce_art",
        name: isEnglish ? "Masters of Art" : "Sanatın Ustaları",
        description: isEnglish 
          ? "Cimiez hill heights: Matisse, Chagall and Roman ruins"
          : "Cimiez tepesi zirveleri: Matisse, Chagall ve Roma kalıntıları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/nice/marc_chagall_national_museum.jpg",
        tags: [isEnglish ? "Art" : "Sanat", "Museum", isEnglish ? "History" : "Tarih"],
        placeNames: ["Marc Chagall National Museum", "Matisse Museum", "Cimiez Monastery"],
        interests: ["Sanat", "Tarih"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.palette,
      ),
      CuratedRoute(
        id: "nce_royal",
        name: isEnglish ? "Royal & Russian" : "Kraliyet & Rus İzleri",
        description: isEnglish 
          ? "Architectural gems: The Russian Cathedral and Belle Époque hotels"
          : "Mimari cevherler: Rus Katedrali ve Belle Époque otelleri.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/nice/russian_orthodox_cathedral.jpg",
        tags: [isEnglish ? "Architecture" : "Mimari", isEnglish ? "History" : "Tarih", "Church"],
        placeNames: ["Russian Orthodox Cathedral", "Hotel Negresco", "Villa Masséna Musée"],
        interests: ["Mimari", "Tarih"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.church,
      ),
      CuratedRoute(
        id: "nce_nature",
        name: isEnglish ? "Green Nice" : "Yeşil Nice",
        description: isEnglish 
          ? "Parks and exotic flora: Phoenix park and the green corridor"
          : "Parklar ve egzotik bitki örtüsü: Phoenix parkı ve yeşil koridor.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/nice/phoenix_park_parc_phoenix.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Park", "Family"],
        placeNames: ["Phoenix Park (Parc Phoenix)", "Promenade du Paillon", "Jardin Albert 1er"],
        interests: ["Doğa", "Aile"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "nce_port",
        name: isEnglish ? "Port & Panorama" : "Liman & Panorama",
        description: isEnglish 
          ? "Marinelife: Colorful boats, antique shops and coastal paths"
          : "Deniz hayatı: Renkli tekneler, antika dükkanları ve sahil yolları.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/nice/port_lympia.jpg",
        tags: [isEnglish ? "Port" : "Liman", isEnglish ? "Sea" : "Deniz", "Antiques"],
        placeNames: ["Port Lympia", "Place Garibaldi", "Coco Beach"],
        interests: ["Manzara", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.directions_boat,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // LYON ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getLyonRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "lyo_old",
        name: isEnglish ? "Vieux Lyon & Traboules" : "Eski Lyon & Traboule'lar",
        description: isEnglish 
          ? "Renaissance secrets: Hidden passageways, cathedral and history"
          : "Rönesans sırları: Gizli geçitler, katedral ve tarih.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/vieux_lyon_ronesans_avlulari.jpg",
        tags: [isEnglish ? "Old Town" : "Eski Şehir", "Traboules", isEnglish ? "History" : "Tarih"],
        placeNames: ["Vieux Lyon (Rönesans Avluları)", "Traboules", "Cathédrale Saint-Jean-Baptiste", "Musée Cinéma et Miniature"],
        interests: ["Tarih", "Keşif"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "lyo_basilica",
        name: isEnglish ? "Fourvière & Roman Ruins" : "Fourvière & Roma Kalıntıları",
        description: isEnglish 
          ? "Hilltop history: The white basilica and ancient Roman theaters"
          : "Tepe tarihi: Beyaz bazilika ve antik Roma tiyatroları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/basilica_of_notre_dame_de_fourviere.jpg",
        tags: [isEnglish ? "Views" : "Manzara", "Basilica", isEnglish ? "Roman" : "Roma"],
        placeNames: ["Basilica of Notre-Dame de Fourvière", "Théâtres Romains de Fourvière", "Musée Gallo-Romain"],
        interests: ["Tarih", "Manzara"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "lyo_food",
        name: isEnglish ? "Capital of Gastronomy" : "Gastronomi Başkenti",
        description: isEnglish 
          ? "Foodie heaven: Paul Bocuse market and traditional bouchons"
          : "Gurme cenneti: Paul Bocuse pazarı ve geleneksel bouchon'lar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/les_halles_de_lyon_paul_bocuse.jpg",
        tags: ["Food", "Market", "Bouchon"],
        placeNames: ["Les Halles de Lyon Paul Bocuse", "Bouchon Daniel & Denise", "Café des Fédérations", "François Pralus - Lyon Presqu'île"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE74C3C),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "lyo_rivers",
        name: isEnglish ? "Music & Rivers" : "Müzik & Nehirler",
        description: isEnglish 
          ? "Between two rivers: Presqu'île, museums and opera"
          : "İki nehir arası: Presqu'île, müzeler ve opera.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/musee_des_beaux_arts.jpg",
        tags: [isEnglish ? "Rivers" : "Nehirler", isEnglish ? "City Center" : "Şehir Merkezi", "Museum"],
        placeNames: ["Musée des Beaux-Arts", "Place des Terreaux", "Place Bellecour", "Musée des Confluences"],
        interests: ["Sanat", "Yürüyüş"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.water,
      ),
      CuratedRoute(
        id: "lyo_murals",
        name: isEnglish ? "Painted Walls & Silk" : "Boyalı Duvarlar & İpek",
        description: isEnglish 
          ? "Croix-Rousse artistic vibes: Murals and silk weavers' history"
          : "Croix-Rousse sanatsal havası: Duvar resimleri ve ipek dokumacıları tarihi.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/croix_rousse.jpg",
        tags: [isEnglish ? "Street Art" : "Sokak Sanatı", isEnglish ? "History" : "Tarih", "Local"],
        placeNames: ["Croix-Rousse", "Mur des Canuts", "La Fresque des Lyonnais"],
        interests: ["Sanat", "Fotoğraf"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.brush,
      ),
      CuratedRoute(
        id: "lyo_nature",
        name: isEnglish ? "Golden Head Park" : "Altın Baş Parkı",
        description: isEnglish 
          ? "Urban oasis: Lake, zoo and botanical gardens"
          : "Şehir vahası: Göl, hayvanat bahçesi ve botanik bahçeler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/parc_de_la_tete_dor_gul_bahcesi.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Park", "Zoo"],
        placeNames: ["Parc de la Tête d'Or (Gül Bahçesi)", "L'Institut Lumière"],
        interests: ["Doğa", "Aile"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MARSİLYA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getMarseilleRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "mrs_oldport",
        name: isEnglish ? "Vieux Port & History" : "Vieux Port & Tarih",
        description: isEnglish 
          ? "The heart of Marseille: The old port, forts and panoramic basilica"
          : "Marsilya'nın kalbi: Eski liman, kaleler ve panoramik bazilika.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/vieux_port_old_port.jpg",
        tags: [isEnglish ? "Port" : "Liman", isEnglish ? "History" : "Tarih", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Vieux Port (Old Port)", "Notre-Dame de la Garde", "Fort Saint-Jean", "Abbaye Saint-Victor"],
        interests: ["Tarih", "Manzara"],
        accentColor: WanderlustColors.accent,
        icon: Icons.anchor,
      ),
      CuratedRoute(
        id: "mrs_culture",
        name: isEnglish ? "MuCEM & Le Panier" : "MuCEM & Le Panier",
        description: isEnglish 
          ? "Old & New: Modern museum architecture and the oldest district"
          : "Eski & Yeni: Modern müze mimarisi ve en eski mahalle.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/mucem.jpg",
        tags: [isEnglish ? "Culture" : "Kültür", "Museum", isEnglish ? "Old Town" : "Eski Şehir"],
        placeNames: ["MuCEM", "Le Panier", "Cathédrale La Major", "Les Terrasses du Port"],
        interests: ["Kültür", "Mimari"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "mrs_nature",
        name: isEnglish ? "Calanques & Islands" : "Calanques & Adalar",
        description: isEnglish 
          ? "Natural wonders: Limestone cliffs, turquoise waters and island forts"
          : "Doğa harikaları: Kireçtaşı kayalıklar, turkuaz sular ve ada kaleleri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "15 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/calanques_national_park.png",
        tags: [isEnglish ? "Nature" : "Doğa", isEnglish ? "Sea" : "Deniz", isEnglish ? "Adventure" : "Macera"],
        placeNames: ["Calanques National Park", "Château d'If", "Frioul Islands", "Vallon des Auffes (Viyadük)"],
        interests: ["Doğa", "Macera"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "mrs_bohemian",
        name: isEnglish ? "Bohemian Marseille" : "Bohem Marsilya",
        description: isEnglish 
          ? "Arty vibes: Street art, hip cafes and soap tradition"
          : "Sanatsal hava: Sokak sanatı, hip kafeler ve sabun geleneği.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/cours_julien.jpg",
        tags: [isEnglish ? "Street Art" : "Sokak Sanatı", "Local", "Soap"],
        placeNames: ["Cours Julien", "La Plaine", "Savonnerie de la Licorne"],
        interests: ["Sanat", "Alışveriş"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.brush,
      ),
      CuratedRoute(
        id: "mrs_corniche",
        name: isEnglish ? "Corniche & Beaches" : "Corniche & Plajlar",
        description: isEnglish 
          ? "Seaside life: Coastal drive, beaches and fishing ports"
          : "Sahil hayatı: Sahil yolu, plajlar ve balıkçı limanları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/la_corniche_kennedy.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", isEnglish ? "Sea" : "Deniz", "Relax"],
        placeNames: ["La Corniche Kennedy", "Plage des Catalans", "Vallon des Auffes (Viyadük)"],
        interests: ["Manzara", "Huzur"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.beach_access,
      ),
      CuratedRoute(
        id: "mrs_arch",
        name: isEnglish ? "Modern Architecture" : "Modern Mimari",
        description: isEnglish 
          ? "Design icons: Le Corbusier's city within a city"
          : "Tasarım ikonları: Le Corbusier'nin şehir içindeki şehri.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/cite_radieuse_le_corbusier.jpg",
        tags: ["Architecture", "Modern", "History"],
        placeNames: ["Cité Radieuse (Le Corbusier)", "Orange Vélodrome"],
        interests: ["Mimari", "Sanat"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.apartment,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // DUBLIN ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getDublinRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "dub_history",
        name: isEnglish ? "Dublin History & Uni" : "Dublin Tarihi & Üni",
        description: isEnglish 
          ? "Scholars & Kings: Trinity College, Book of Kells and the Castle"
          : "Alimler & Krallar: Trinity College, Kells Kitabı ve Kale.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/trinity_college_long_room.jpg",
        tags: [isEnglish ? "History" : "Tarih", "University", "Books"],
        placeNames: ["Trinity College - Long Room", "Dublin Castle", "Chester Beatty Library", "Christ Church Cathedral", "St. Patrick's Cathedral"],
        interests: ["Tarih", "Kültür"],
        accentColor: WanderlustColors.accent,
        icon: Icons.school,
      ),
      CuratedRoute(
        id: "dub_fun",
        name: isEnglish ? "Guinness & Temple Bar" : "Guinness & Temple Bar",
        description: isEnglish 
          ? "The Craic: Pints of the black stuff, whiskey and lively pubs"
          : "Eğlence: Siyah bira, viski ve canlı barlar.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/guinness_storehouse.jpg",
        tags: ["Pubs", "Beer", "Whiskey", "Nightlife"],
        placeNames: ["Guinness Storehouse", "Temple Bar", "Jameson Distillery Bow St.", "The Brazen Head", "Irish Whiskey Museum"],
        interests: ["Eğlence", "Yemek"],
        accentColor: const Color(0xFF795548),
        icon: Icons.local_drink,
      ),
      CuratedRoute(
        id: "dub_rebellion",
        name: isEnglish ? "Rebels & Emigrants" : "İsyancılar & Göçmenler",
        description: isEnglish 
          ? "Struggle for freedom: Kilmainham Gaol and the story of emigration"
          : "Özgürlük mücadelesi: Kilmainham Hapishanesi ve göç hikayesi.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/kilmainham_gaol.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Museum", isEnglish ? "Stories" : "Hikayeler"],
        placeNames: ["Kilmainham Gaol", "EPIC The Irish Emigration Museum", "GPO Witness History", "Jeanie Johnston Tall Ship", "Famine Memorial"],
        interests: ["Tarih", "Kültür", "Hikayeler"],
        accentColor: const Color(0xFF607D8B),
        icon: Icons.history,
      ),
      CuratedRoute(
        id: "dub_parks",
        name: isEnglish ? "Green Dublin Parks" : "Yeşil Dublin Parkları",
        description: isEnglish 
          ? "City lungs: Georgian squares, deer in the park and botanical gardens"
          : "Şehrin ciğerleri: Gürcü meydanları, parktaki geyikler ve botanik bahçeler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "6 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/st_stephens_green.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Park", "Relax"],
        placeNames: ["St. Stephen's Green", "Phoenix Park (Deer Watching)", "Merrion Square", "National Botanic Gardens", "Iveagh Gardens"],
        interests: ["Doğa", "Huzur", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
      CuratedRoute(
        id: "dub_music",
        name: isEnglish ? "Music & Folklore" : "Müzik & Folklor",
        description: isEnglish 
          ? "Irish soul: Traditional music sessions and folklore stories"
          : "İrlanda ruhu: Geleneksel müzik seansları ve folklor hikayeleri.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/the_cobblestone.jpg",
        tags: [isEnglish ? "Music" : "Müzik", "Folklore", "Pubs"],
        placeNames: ["The Cobblestone", "The Stag's Head", "O'Donoghue's", "Whelands"],
        interests: ["Müzik", "Kültür"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.music_note,
      ),
      CuratedRoute(
        id: "dub_coastal",
        name: isEnglish ? "Howth Coastal Walk" : "Howth Sahil Yürüyüşü",
        description: isEnglish 
          ? "Seaside escape: Cliff walks, seals and fresh seafood"
          : "Sahil kaçamağı: Yar yürüyüşleri, foklar ve taze deniz ürünleri.",
        duration: isEnglish ? "Half day" : "Yarım gün",
        distance: "15 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/howth.jpg",
        tags: [isEnglish ? "Coast" : "Sahil", isEnglish ? "Nature" : "Doğa", "Seafood"],
        placeNames: ["Howth", "Howth Cliff Walk", "Howth Market"],
        interests: ["Doğa", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.directions_walk,
      ),
    ];
  }


  // ═══════════════════════════════════════════════════════════════════════════
  // ANTALYA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getAntalyaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "ant_oldtown",
        name: isEnglish ? "Kaleiçi & History" : "Kaleiçi & Tarih",
        description: isEnglish 
          ? "The heart of Antalya: Narrow streets, Hadrian's Gate and ancient harbor"
          : "Antalya'nın kalbi: Dar sokaklar, Hadrian Kapısı ve antik liman.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/hadrian_kapisi_uc_kapilar.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Old Town", isEnglish ? "Food" : "Yemek"],
        placeNames: ["Hadrian Kapısı (Üç Kapılar)", "Kaleiçi", "Hıdırlık Kulesi", "Mermerli Plajı", "Vanilla Lounge", "Yivli Minare"],
        interests: ["Tarih", "Fotoğraf", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.history,
      ),
      CuratedRoute(
        id: "ant_ancient",
        name: isEnglish ? "Ancient Cities (Day Trip)" : "Antik Kentler (Günübirlik)",
        description: isEnglish 
          ? "Journey to the past: Perge, Aspendos and Termessos"
          : "Geçmişe yolculuk: Perge, Aspendos ve Termessos.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "40 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/aspendos_antik_tiyatrosu.jpg",
        tags: [isEnglish ? "Ancient" : "Antik", "Theater", isEnglish ? "History" : "Tarih"],
        placeNames: ["Aspendos Antik Tiyatrosu", "Perge Antik Kenti", "Termessos Antik Kenti", "Kurşunlu Şelalesi", "Köprülü Kanyon"],
        interests: ["Tarih", "Arkeoloji", "Doğa"],
        accentColor: const Color(0xFFD35400),
        icon: Icons.account_balance,
      ),
      CuratedRoute(
        id: "ant_nature",
        name: isEnglish ? "Waterfalls & Nature" : "Şelaleler & Doğa",
        description: isEnglish 
          ? "Refreshing escape: Düden and Kurşunlu waterfalls"
          : "Serinletici kaçış: Düden ve Kurşunlu şelaleleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "15 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/duden_selalesi_asagi.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", "Waterfall", isEnglish ? "Park" : "Park"],
        placeNames: ["Düden Şelalesi (Aşağı)", "Düden Parkı", "Kurşunlu Şelalesi", "Konyaaltı Plajı", "The Land of Legends Theme Park"],
        interests: ["Doğa", "Fotoğraf", "Eğlence"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.water_drop,
      ),
      CuratedRoute(
        id: "ant_lara",
        name: isEnglish ? "Lara Coast & Shopping" : "Lara Sahili ve Alışveriş",
        description: isEnglish 
          ? "Modern Antalya: Luxury beach clubs, TerraCity mall and scenic cliff walks"
          : "Modern Antalya: Lüks plaj kulüpleri, TerraCity AVM ve falez yürüyüşleri.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "8 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/antalya/lara_plaji.jpg",
        tags: [isEnglish ? "Modern" : "Modern", "Shopping", "Beach"],
        placeNames: ["Lara Plajı", "TerraCity AVM", "Falez Parkı", "Eski Lara Caddesi", "Lara Balıkçı Barınağı"],
        interests: ["Manzara", "Alışveriş", "Yemek"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.beach_access,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // GAZİANTEP ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getGaziantepRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "gaz_food",
        name: isEnglish ? "Gastronomy Capital" : "Gastronomi Başkenti",
        description: isEnglish 
          ? "World-famous flavors: Baklava, kebabs and historic coffee houses"
          : "Dünyaca ünlü lezzetler: Baklava, kebaplar ve tarihi kahvehaneler.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/gaziantep/i_mam_çağdaş.jpg",
        tags: ["Gastronomy", "Baklava", "Kebab"],
        placeNames: ["İmam Çağdaş", "Koçak Baklava", "Tahmis Kahvesi", "Mutfak Sanatları Merkezi", "Kebapçı Halil Usta", "Orkide Pastanesi (Katmer)"],
        interests: ["Yemek", "Kültür"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "gaz_culture",
        name: isEnglish ? "Zeugma & History" : "Zeugma & Tarih",
        description: isEnglish 
          ? "Mosaic masterpieces: Zeugma Museum, Coppersmith Bazaar and Castle"
          : "Mozaik başyapıtları: Zeugma Müzesi, Bakırcılar Çarşısı ve Kale.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/gaziantep/zeugma_mozaik_müzesi.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Mosaic", "Museum"],
        placeNames: ["Zeugma Mozaik Müzesi", "Gaziantep Kalesi", "Bakırcılar Çarşısı", "Zincirli Bedesten", "Hamam Müzesi", "Gümrük Hanı"],
        interests: ["Tarih", "Sanat", "Alışveriş"],
        accentColor: const Color(0xFF8E44AD),
        icon: Icons.museum,
      ),
      CuratedRoute(
        id: "gaz_artisans",
        name: isEnglish ? "Artisans & Bazaars" : "Bakırcılar ve El Sanatları",
        description: isEnglish 
          ? "Uncover century-old crafts: Coppersmiths, spice markets and silver masters"
          : "Yüzyıllık zanaatları keşfedin: Bakırcılar, baharat pazarları ve gümüş ustaları.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/saraybosna/bakircilar_carsisi_kazandziluk.jpg",
        tags: ["Artisans", "Shopping", "Local"],
        placeNames: ["Bakırcılar Çarşısı", "Almacı Pazarı", "Kutnu Kumaş Atölyeleri", "Sedef Kakma Atölyesi", "Naib Hamamı", "Tarihi Gümrük Hanı"],
        interests: ["Kültür", "Alışveriş", "Fotoğraf"],
        accentColor: const Color(0xFF795548),
        icon: Icons.handyman,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // KAPADOKYA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getCappadociaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "kap_classic",
        name: isEnglish ? "Red Tour (North)" : "Kırmızı Tur (Kuzey)",
        description: isEnglish 
          ? "Fairy chimneys & History: Göreme Museum, castles and pottery"
          : "Peri bacaları & Tarih: Göreme Müzesi, kaleler ve çömlekçilik.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "15 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/kapadokya/goreme_acik_hava_muzesi.jpg",
        tags: [isEnglish ? "Fairy Chimneys" : "Peri Bacaları", "Museum", "UNESCO"],
        placeNames: ["Göreme Açık Hava Müzesi", "Uçhisar Kalesi", "Paşabağ Peribacaları", "Devrent Vadisi", "Avanos Çömlek Atölyesi", "Dibek Restaurant"],
        interests: ["Doğa", "Tarih", "Yemek"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.landscape,
      ),
      CuratedRoute(
        id: "kap_underground",
        name: isEnglish ? "Green Tour (South)" : "Yeşil Tur (Güney)",
        description: isEnglish 
          ? "Underground secrets: Deep cities and canyon hikes"
          : "Yeraltı sırları: Derin şehirler ve kanyon yürüyüşleri.",
        duration: isEnglish ? "Full day" : "Tam gün",
        distance: "40 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/kapadokya/derinkuyu_yeralti_sehri.jpg",
        tags: [isEnglish ? "Underground" : "Yeraltı", isEnglish ? "Hiking" : "Yürüyüş", isEnglish ? "Valley" : "Vadi"],
        placeNames: ["Derinkuyu Yeraltı Şehri", "Ihlara Vadisi", "Selime Manastırı", "Belisirma Köyü (Yemek)", "Güvercinlik Vadisi"],
        interests: ["Macera", "Tarih", "Doğa"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.terrain,
      ),
      CuratedRoute(
        id: "kap_balloons",
        name: isEnglish ? "Balloons & Views" : "Balonlar & Manzara",
        description: isEnglish 
          ? "Magical sunrise: Watching hot air balloons from love valley"
          : "Büyülü gün doğumu: Aşk Vadisi'nden sıcak hava balonlarını izlemek.",
        duration: isEnglish ? "Morning" : "Sabah",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/kapadokya/ask_vadisi.jpg",
        tags: [isEnglish ? "Balloons" : "Balonlar", "Sunrise", "Photography"],
        placeNames: ["Aşk Vadisi (Love Valley)", "Kızılçukur Vadisi (Sunset Point)", "Ortahisar Kalesi", "Galerie Icman (Carpet Shop)", "Asmalı Konak Museum"],
        interests: ["Manzara", "Romantik", "Alışveriş", "Fotoğraf"],
        accentColor: const Color(0xFFE91E63),
        icon: Icons.air,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MİDİLLİ ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getLesbosRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "les_classic",
        name: isEnglish ? "Molyvos & Petra" : "Molyvos & Petra",
        description: isEnglish 
          ? "Northern charm: Medieval castles and cobblestone streets"
          : "Kuzey cazibesi: Ortaçağ kaleleri ve Arnavut kaldırımlı sokaklar.",
        duration: isEnglish ? "6 hours" : "6 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/midilli/molyvos_mithymna.jpg",
        tags: [isEnglish ? "Castle" : "Kale", isEnglish ? "Village" : "Köy", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Molyvos Castle", "Mithymna Old Town", "Women's Cooperative of Petra", "Panagia Glykofilousa", "Eftalou Hot Springs"],
        interests: ["Tarih", "Manzara", "Alışveriş"],
        accentColor: WanderlustColors.accent,
        icon: Icons.fort,
      ),
      CuratedRoute(
        id: "les_capital",
        name: isEnglish ? "Mytilene Capital" : "Midilli Merkez",
        description: isEnglish 
          ? "City highlights: Castle, waterfront corniche and shopping"
          : "Şehir merkezi: Kale, sahil kordonu ve alışveriş.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/midilli/midilli_kalesi_mytilene_castle.jpg",
        tags: [isEnglish ? "Capital" : "Merkez", isEnglish ? "Castle" : "Kale", isEnglish ? "City" : "Şehir"],
        placeNames: ["Mytilene Castle", "Ermou Street", "Agios Therapon Church", "Yeni Camii", "Museum of Industrial Olive-Oil Production"],
        interests: ["Kültür", "Alışveriş", "Tarih"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.location_city,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BELGRAD ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBelgradeRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "beg_vibe",
        name: isEnglish ? "Belgrade Vibes & History" : "Belgrad Havası & Tarih",
        description: isEnglish 
          ? "Fortress to walking street: Kalemegdan and Knez Mihailova"
          : "Kaleden yürüyüş caddesine: Kalemegdan ve Knez Mihailova.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Fortress" : "Kale", isEnglish ? "History" : "Tarih", "Must See"],
        placeNames: ["Kalemegdan Fortress", "Knez Mihailova Street", "Republic Square", "Hotel Moskva (Cafe)", "Beton Hala (Riverside)"],
        interests: ["Tarih", "Yürüyüş", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "beg_bohemian",
        name: isEnglish ? "Bohemian Skadarlija" : "Bohem Skadarlija",
        description: isEnglish 
          ? "Vintage street: Traditional kafanas, music and Serbian food"
          : "Nostaljik sokak: Geleneksel kafanalar, müzik ve Sırp yemekleri.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "1 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/belgrad/skadarlija.jpg",
        tags: [isEnglish ? "Bohemian" : "Bohem", "Food", "Music"],
        placeNames: ["Skadarlija Street", "Dva Jelena (Two Deer)", "Tri Sesira", "Bajloni Market", "Red Bar"],
        interests: ["Yemek", "Eğlence", "Alışveriş"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
      CuratedRoute(
        id: "beg_tesla",
        name: isEnglish ? "Tesla & Museums" : "Tesla & Müzeler",
        description: isEnglish 
          ? "Science and culture: Tesla Museum and the massive Saint Sava"
          : "Bilim ve kültür: Tesla Müzesi ve devasa Aziz Sava.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: ["Museum", "Science", "Church"],
        placeNames: ["Nikola Tesla Museum", "Saint Sava Temple", "National Museum of Serbia", "Botanical Garden Jevremovac", "Smokvica (Cafe)"],
        interests: ["Bilim", "Kültür", "Doğa"],
        accentColor: const Color(0xFF9B59B6),
        icon: Icons.museum,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BOLOGNA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBolognaRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bol_red",
        name: isEnglish ? "The Red City" : "Kızıl Şehir",
        description: isEnglish 
          ? "Medieval towers and plazas: Piazza Maggiore and the Two Towers"
          : "Ortaçağ kuleleri ve meydanlar: Piazza Maggiore ve İkiz Kuleler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bologna/piazza_maggiore.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Architecture", isEnglish ? "Towers" : "Kuleler"],
        placeNames: ["Piazza Maggiore", "Two Towers (Due Torri)", "San Petronio Basilica", "Archiginnasio (Teatro Anatomico)", "Salumeria Simoni (Food)"],
        interests: ["Tarih", "Mimari", "Yemek"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "bol_food",
        name: isEnglish ? "La Grassa (The Fat)" : "Şişman Bologna",
        description: isEnglish 
          ? "Culinary heaven: Tortellini, ragu and centuries-old markets"
          : "Lezzet cenneti: Tortellini, ragu ve asırlık pazarlar.",
        duration: isEnglish ? "Lunch" : "Öğle",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bologna/quadrilatero-eski-pazar.jpg",
        tags: ["Food", "Pasta", "Market"],
        placeNames: ["Quadrilatero Market", "Osteria dell'Orsa", "Cremeria Santo Stefano", "Mercato di Mezzo", "Trattoria da Danio"],
        interests: ["Yemek", "Lokal"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // HEIDELBERG ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getHeidelbergRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "hdb_classic",
        name: isEnglish ? "Castle & Old Bridge" : "Kale & Eski Köprü",
        description: isEnglish 
          ? "German romance: The magnificent castle ruins and Neckar views"
          : "Alman romantizmi: Muhteşem kale kalıntıları ve Neckar manzaraları.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/heidelberg/heidelberg_castle.jpg",
        tags: [isEnglish ? "Castle" : "Kale", isEnglish ? "Romance" : "Romantik", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Heidelberg Castle", "Old Bridge (Karl Theodor Bridge)", "Market Square (Marktplatz)", "Church of the Holy Spirit", "Vetter's Alt Heidelberger Brauhaus"],
        interests: ["Tarih", "Manzara", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "hdb_philo",
        name: isEnglish ? "Philosophers' Walk" : "Filozoflar Yolu",
        description: isEnglish 
          ? "Thinkers' path: Scenic trail with best city panorama"
          : "Düşünürlerin yolu: En iyi şehir panoramasına sahip manzaralı yol.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/heidelberg/philosophers__walk.jpg",
        tags: [isEnglish ? "Nature" : "Doğa", isEnglish ? "Walking" : "Yürüyüş", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Philosophers' Walk", "Heiligenberg", "Thingstätte Amphitheatre", "Neuburg Abbey"],
        interests: ["Doğa", "Manzara"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.terrain,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // KOTOR ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getKotorRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "kot_oldtown",
        name: isEnglish ? "Medieval Old Town" : "Ortaçağ Eski Şehir",
        description: isEnglish 
          ? "Venetian heritage: Maze of squares, churches and cats"
          : "Venedik mirası: Meydanlar, kiliseler ve kediler labirenti.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/kotor/kotor_old_town.jpg",
        tags: [isEnglish ? "Old Town" : "Eski Şehir", "Cats", "UNESCO"],
        placeNames: ["Kotor Old Town", "Cathedral of Saint Tryphon", "Cats Museum", "Church of St. Luke", "Bastion Restaurant", "Kampana Tower"],
        interests: ["Tarih", "Kültür", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "kot_fortress",
        name: isEnglish ? "San Giovanni Hike" : "San Giovanni Tırmanışı",
        description: isEnglish 
          ? "Steps to the sky: Hiking up to the castle for fjord views"
          : "Gökyüzüne basamaklar: Fiyort manzarası için kaleye tırmanış.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Hard" : "Zor",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/kotor/castle_of_san_giovanni.jpg",
        tags: [isEnglish ? "Hiking" : "Yürüyüş", isEnglish ? "Views" : "Manzara", isEnglish ? "Fortress" : "Kale"],
        placeNames: ["Castle of San Giovanni", "Church of Our Lady of Remedy", "Trail Cheese Shop", "North Gate"],
        interests: ["Macera", "Manzara"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.terrain,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // MATERA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getMateraRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "mat_sassi",
        name: isEnglish ? "Sassi di Matera" : "Matera Sassi",
        description: isEnglish 
          ? "City of stones: Ancient cave dwellings and rock churches"
          : "Taşlar şehri: Antik mağara evleri ve kaya kiliseleri.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/matera/church-of-san-pietro-barisano.jpg",
        tags: [isEnglish ? "Ancient" : "Antik", "Cave", "UNESCO"],
        placeNames: ["Sassi di Matera", "Casa Grotta nei Sassi", "Madonna de Idris", "San Pietro Caveoso", "Palombaro Lungo", "Antica Matera (Restaurant)"],
        interests: ["Tarih", "Fotoğraf", "Yemek"],
        accentColor: const Color(0xFF795548),
        icon: Icons.terrain,
      ),
      CuratedRoute(
        id: "mat_view",
        name: isEnglish ? "Belvedere Views" : "Belvedere Manzaraları",
        description: isEnglish 
          ? "Passion of Christ views: Panoramic look at the Sassi"
          : "İsa'nın Çilesi manzaraları: Sassi'ye panoramik bakış.",
        duration: isEnglish ? "2 hours" : "2 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/matera/belvedere-luigi-guerricchio.jpg",
        tags: [isEnglish ? "Views" : "Manzara", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["Belvedere di Murgia Timone", "Parco della Murgia Materana", "Pane e Pace (Bakery)", "MUSMA Museum"],
        interests: ["Manzara", "Doğa", "Yemek"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.camera_alt,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // OSLO ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getOsloRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "osl_arts",
        name: isEnglish ? "Opera & Munch" : "Opera & Munch",
        description: isEnglish 
          ? "Modern architecture: The Opera House and The Scream"
          : "Modern mimari: Opera Binası ve Çığlık tablosu.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/oslo/oslo-opera-house.jpg",
        tags: ["Art", "Architecture", "Museum"],
        placeNames: ["Oslo Opera House", "Munch Museum", "Deichman Bjørvika", "Salt (Sauna & Food)", "Vippa Food Court"],
        interests: ["Sanat", "Mimari", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.architecture,
      ),
      CuratedRoute(
        id: "osl_parks",
        name: isEnglish ? "Vigeland Sculpture Park" : "Vigeland Heykel Parkı",
        description: isEnglish 
          ? "Human condition in stone: World's largest sculpture park"
          : "Taştaki insanlık hali: Dünyanın en büyük heykel parkı.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: ["Art", "Park", "Sculpture"],
        placeNames: ["Vigeland Sculpture Park", "Frogner Park", "Holmenkollen Ski Museum & Tower", "Anne på landet (Cafe)", "The Emanuel Vigeland Museum"],
        interests: ["Sanat", "Doğa", "Yemek", "Manzara"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.park,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ROVANİEMİ ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getRovaniemiRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "rov_santa",
        name: isEnglish ? "Santa Claus Village" : "Noel Baba Köyü",
        description: isEnglish 
          ? "Arctic magic: Meeting Santa and crossing the Arctic Circle"
          : "Arktik büyüsü: Noel Baba ile tanışma ve Kuzey Kutup Dairesi'ni geçiş.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: ["Christmas", "Santa", "Arctic"],
        placeNames: ["Santa Claus Village", "Santa's Main Post Office", "Husky Park", "Santa's Salmon Place (Food)", "Reindeer Sleigh Ride"],
        interests: ["Eğlence", "Aile", "Yemek"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.ac_unit,
      ),
      CuratedRoute(
        id: "rov_arctic",
        name: isEnglish ? "Arktikum & Nature" : "Arktikum & Doğa",
        description: isEnglish 
          ? "Science and lights: Museum of the North and Ounasvaara hike"
          : "Bilim ve ışıklar: Kuzey Müzesi ve Ounasvaara yürüyüşü.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/mu.jpg",
        tags: ["Museum", "Nature", "Science"],
        placeNames: ["Arktikum Science Museum", "Pilke Science Centre", "Korundi House of Culture", "Ounasvaara Winter Trail", "Cafe & Bar 21"],
        interests: ["Bilim", "Doğa", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.science,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SAN SEBASTIAN ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSanSebastianRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "san_beach",
        name: isEnglish ? "La Concha & Views" : "La Concha & Manzara",
        description: isEnglish 
          ? "Best city beach: Walking the bay and funicular to Igueldo"
          : "En iyi şehir plajı: Koy yürüyüşü ve Igueldo'ya füniküler.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/san_sebastian/la_concha_beach.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", isEnglish ? "Views" : "Manzara", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["La Concha Beach", "Ondarreta Beach", "Miramar Palace Gardens", "Peine del Viento (Wind Comb)", "Monte Igueldo Funicular"],
        interests: ["Doğa", "Manzara", "Sanat"],
        accentColor: WanderlustColors.accent,
        icon: Icons.beach_access,
      ),
      CuratedRoute(
        id: "san_food",
        name: isEnglish ? "Pintxos Tour" : "Pintxos Turu",
        description: isEnglish 
          ? "Basque gastronomy: Hop from bar to bar in Old Town"
          : "Bask gastronomisi: Eski Şehir'de bardan bara lezzet turu.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "2 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/san_sebastian/parte_vieja__old_town_.jpg",
        tags: ["Food", "Pintxos", "Gastronomy"],
        placeNames: ["Parte Vieja (Old Town)", "La Viña (Cheesecake)", "Bar Zeruko", "Borda Berri", "Atari Gastroteka"],
        interests: ["Yemek", "Eğlence"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.restaurant,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SANTORINI ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSantoriniRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "san_oia",
        name: isEnglish ? "Oia Sunset & Views" : "Oia Gün Batımı & Manzara",
        description: isEnglish 
          ? "Iconic blue domes: Walking the marble streets of Oia"
          : "İkonik mavi kubbeler: Oia'nın mermer sokaklarında yürüyüş.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/santorini/oia_castle.jpg",
        tags: [isEnglish ? "Sunset" : "Gün Batımı", "Romance", "Views"],
        placeNames: ["Oia Castle", "Amoudi Bay (Fish Tavernas)", "Blue Domed Churches", "Melenio Cafe", "Atlantis Books"],
        interests: ["Manzara", "Romantik", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.wb_sunny,
      ),
      CuratedRoute(
        id: "san_hike",
        name: isEnglish ? "Fira to Oia Hike" : "Fira'dan Oia'ya Yürüyüş",
        description: isEnglish 
          ? "Caldera edge trail: The most scenic hike in the Cyclades"
          : "Kaldera kenarı yolu: Kiklad Adaları'nın en manzaralı yürüyüşü.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/santorini/fira_-_oia_hike.jpg",
        tags: [isEnglish ? "Hiking" : "Yürüyüş", isEnglish ? "Views" : "Manzara", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["Fira", "Skaros Rock", "Imerovigli", "Prophet Elias Church", "Avocado Restaurant (Lunch Stop)"],
        interests: ["Doğa", "Macera", "Yemek"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.terrain,
      ),
      CuratedRoute(
        id: "san_akrotiri",
        name: isEnglish ? "Red Beach & History" : "Kızıl Plaj & Tarih",
        description: isEnglish 
          ? "Ancient Thera: Akrotiri ruins and colorful beaches"
          : "Antik Thera: Akrotiri kalıntıları ve renkli plajlar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/santorini/red_beach.jpg",
        tags: [isEnglish ? "Beach" : "Plaj", isEnglish ? "History" : "Tarih", "Volcanic"],
        placeNames: ["Red Beach", "Akrotiri Archaeological Site", "Perissa Beach (Black Sand)", "Santo Wines Winery"],
        interests: ["Tarih", "Doğa", "Yemek"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.history,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SARAYBOSNA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSarajevoRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sar_bascarsija",
        name: isEnglish ? "Baščaršija & Old Town" : "Başçarşı & Eski Şehir",
        description: isEnglish 
          ? "Ottoman heart: Sebilj fountain, mosques and coffee"
          : "Osmanlı kalbi: Sebil, camiler ve kahve.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/saraybosna/bascarsi.jpg",
        tags: [isEnglish ? "History" : "Tarih", "Old Town", "Culture"],
        placeNames: ["Başçarşı", "Sebilj (Sebil)", "Gazi Husrev-beg Mosque", "Latin Bridge", "Inat Kuca", "Yellow Bastion (Sunset)"],
        interests: ["Tarih", "Kültür", "Manzara"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "sar_war",
        name: isEnglish ? "Tunnel of Hope" : "Umut Tüneli",
        description: isEnglish 
          ? "Recent history: The tunnel that saved the city"
          : "Yakın tarih: Şehri kurtaran tünel.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "History" : "Tarih", "War", "Museum"],
        placeNames: ["Tunnel of Hope", "Galerija 11/07/95", "War Childhood Museum", "Sniper Alley (Drive-by)"],
        interests: ["Tarih", "Kültür"],
        accentColor: const Color(0xFF795548),
        icon: Icons.history,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // SINTRA ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getSintraRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sin_fairytale",
        name: isEnglish ? "Pena & Moorish Castle" : "Pena & Mağribi Kalesi",
        description: isEnglish 
          ? "Colorful palaces: The romantic Pena Palace and ancient walls"
          : "Renkli saraylar: Romantik Pena Sarayı ve antik surlar.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/sintra/pena_palace.jpg",
        tags: [isEnglish ? "Palace" : "Saray", isEnglish ? "Fairytale" : "Masal", "UNESCO"],
        placeNames: ["Pena Palace", "Moorish Castle", "Park of Pena", "Chalet of the Countess of Edla"],
        interests: ["Tarih", "Mimari", "Doğa"],
        accentColor: const Color(0xFFF1C40F),
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "sin_mystic",
        name: isEnglish ? "Quinta da Regaleira" : "Quinta da Regaleira",
        description: isEnglish 
          ? "Mystical gardens: Initiation wells and hidden tunnels"
          : "Gizemli bahçeler: İnisiyasyon kuyuları ve gizli tüneller.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/sintra/quinta_da_regaleira.jpg",
        tags: [isEnglish ? "Garden" : "Bahçe", "Mystery", "Gothic"],
        placeNames: ["Quinta da Regaleira (Initiation Well)", "Sintra National Palace", "Piriquita (Pastries)", "Monserrate Palace"],
        interests: ["Keşif", "Doğa", "Yemek"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.yard,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // STRAZBURG ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getStrasbourgRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "sxb_petite",
        name: isEnglish ? "Petite France & Cathedral" : "Petite France & Katedral",
        description: isEnglish 
          ? "Alsace icons: Half-timbered houses and the gothic masterpiece"
          : "Alsace ikonları: Ahşap evler ve gotik başyapıt.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/strazburg/petite_france.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", isEnglish ? "Old Town" : "Eski Şehir", "Canal"],
        placeNames: ["Strasbourg Cathedral", "Petite France", "Ponts Couverts", "Barrage Vauban", "Maison Kammerzell"],
        interests: ["Tarih", "Mimari", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.location_city,
      ),
      CuratedRoute(
        id: "sxb_europe",
        name: isEnglish ? "European Quarter" : "Avrupa Bölgesi",
        description: isEnglish 
          ? "Modern institutions: European Parliament and Orangerie Park"
          : "Modern kurumlar: Avrupa Parlamentosu ve Orangerie Parkı.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/paris/lorangerie.jpg",
        tags: ["Modern", "EU", "Park"],
        placeNames: ["European Parliament", "Parc de l'Orangerie", "Josephine Pavilion", "Bowling de l'Orangerie"],
        interests: ["Politika", "Doğa", "Eğlence"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.public,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // TROMSO ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getTromsoRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "tos_city",
        name: isEnglish ? "Arctic Gateway" : "Arktik Kapısı",
        description: isEnglish 
          ? "City walk: Arctic Cathedral, Polar Museum and cable car"
          : "Şehir yürüyüşü: Arktik Katedrali, Kutup Müzesi ve teleferik.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: [isEnglish ? "Arctic" : "Arktik", isEnglish ? "Views" : "Manzara", isEnglish ? "City" : "Şehir"],
        placeNames: ["Arctic Cathedral", "Fjellheisen Cable Car", "Polar Museum", "Polaria Aquarium", "Mack Brewery (Ølhallen)"],
        interests: ["Kültür", "Manzara", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.ac_unit,
      ),
      CuratedRoute(
        id: "tos_nature",
        name: isEnglish ? "Northern Lights Spots" : "Kuzey Işıkları Noktaları",
        description: isEnglish 
          ? "Aurora hunting: Best spots near the city"
          : "Aurora avı: Şehre yakın en iyi noktalar.",
        duration: isEnglish ? "Evening" : "Akşam",
        distance: "5 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marsilya/f.jpg",
        tags: ["Aurora", "Nature", "Night"],
        placeNames: ["Telegrafbukta Beach", "Prestvannet Lake", "Fjellheisen Viewpoint", "Ersfjordbotn"],
        interests: ["Doğa", "Fotoğraf"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.flare,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ZERMATT ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getZermattRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "zerm_gornergrat",
        name: isEnglish ? "Gornergrat Railway" : "Gornergrat Treni",
        description: isEnglish 
          ? "Best Matterhorn view: Cogwheel train to the summit"
          : "En iyi Matterhorn manzarası: Zirveye dişli tren yolculuğu.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "10 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zermatt/gornergrat_railway.jpg",
        tags: [isEnglish ? "Mountain" : "Dağ", "Train", isEnglish ? "Views" : "Manzara"],
        placeNames: ["Gornergrat Railway", "Riffelsee Lake", "3100 Kulmhotel", "Riffelalp Resort", "Matterhorn Viewpoint"],
        interests: ["Doğa", "Manzara", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.train,
      ),
      CuratedRoute(
        id: "zerm_village",
        name: isEnglish ? "Zermatt Village" : "Zermatt Köyü",
        description: isEnglish 
          ? "Car-free charm: Old wooden barns and mountaineer's cemetery"
          : "Araçsız cazibe: Eski ahşap ambarlar ve dağcılar mezarlığı.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/zermatt/hinterdorf.jpg",
        tags: [isEnglish ? "Village" : "Köy", isEnglish ? "History" : "Tarih", "Shopping"],
        placeNames: ["Hinterdorf (Old Barns)", "Matterhorn Museum", "Mountaineers' Cemetery", "Bahnhofstrasse", "Fuchs Bakery"],
        interests: ["Kültür", "Yürüyüş", "Yemek"],
        accentColor: const Color(0xFF795548),
        icon: Icons.home,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BRUGGE ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBrugesRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bru_classic",
        name: isEnglish ? "Medieval Fairy Tale" : "Ortaçağ Masalı",
        description: isEnglish 
          ? "Canals & Chocolate: Markt square, Belfry and Minnewater"
          : "Kanallar ve Çikolata: Markt meydanı, Belfry kulesi ve Minnewater.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/brugge/belfry_of_bruges.jpg",
        tags: [isEnglish ? "Medieval" : "Ortaçağ", "Chocolate", isEnglish ? "Romance" : "Romantik"],
        placeNames: ["Markt Square", "Belfry of Bruges", "Minnewater Park", "Rozenhoedkaai", "Choco-Story Museum", "De Halve Maan Brewery"],
        interests: ["Tarih", "Yemek", "Romantik"],
        accentColor: const Color(0xFFC0392B),
        icon: Icons.castle,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // BRUKSEL ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getBrusselsRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "bru_grand",
        name: isEnglish ? "Grand Place & Icons" : "Grand Place & İkonlar",
        description: isEnglish 
          ? "Heart of EU: The magnificent square, Manneken Pis and chocolates"
          : "Avrupa'nın kalbi: Muhteşem meydan, İşeyen Çocuk ve çikolatalar.",
        duration: isEnglish ? "4 hours" : "4 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bruksel/grand-place.jpg",
        tags: [isEnglish ? "Iconic" : "İkonik", isEnglish ? "History" : "Tarih", "Waffles"],
        placeNames: ["Grand Place", "Manneken Pis", "Royal Gallery of Saint Hubert", "Atomium (View)", "Maison Dandoy (Waffles)", "Delirium Café"],
        interests: ["Tarih", "Kültür", "Yemek"],
        accentColor: WanderlustColors.accent,
        icon: Icons.star,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // COLMAR ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getColmarRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "col_venice",
        name: isEnglish ? "Little Venice" : "Küçük Venedik",
        description: isEnglish 
          ? "Alsatian charm: Colorful half-timbered houses and canals"
          : "Alsace cazibesi: Renkli ahşap evler ve kanallar.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/londra/little_venice.jpg",
        tags: [isEnglish ? "Fairytale" : "Masal", isEnglish ? "Romance" : "Romantik", "Wine"],
        placeNames: ["Little Venice (La Petite Venise)", "Pfister House", "Saint Martin's Church", "Covered Market (Marché Couvert)", "Maison des Têtes"],
        interests: ["Mimari", "Fotoğraf", "Yemek"],
        accentColor: const Color(0xFFE67E22),
        icon: Icons.local_florist,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // EDINBURGH ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getEdinburghRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "edi_royal",
        name: isEnglish ? "Royal Mile & Castle" : "Kraliyet Yolu & Kale",
        description: isEnglish 
          ? "Historic heart: From the ancient castle to Holyrood Palace"
          : "Tarihi kalp: Antik kaleden Holyrood Sarayı'na.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/edinburgh/royal_mile.jpg",
        tags: [isEnglish ? "Castle" : "Kale", isEnglish ? "History" : "Tarih", "Harry Potter"],
        placeNames: ["Edinburgh Castle", "The Royal Mile", "St Giles' Cathedral", "Victoria Street", "Camera Obscura", "Mary King's Close"],
        interests: ["Tarih", "Efsaneler", "Eğlence"],
        accentColor: WanderlustColors.accent,
        icon: Icons.castle,
      ),
      CuratedRoute(
        id: "edi_arthur",
        name: isEnglish ? "Arthur's Seat Hike" : "Arthur's Seat Yürüyüşü",
        description: isEnglish 
          ? "City summit: Panoramic views from an ancient volcano"
          : "Şehir zirvesi: Antik bir yanardağdan panoramik manzaralar.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "5 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/edinburgh/arthurs_seat.jpg",
        tags: [isEnglish ? "Hiking" : "Yürüyüş", isEnglish ? "Views" : "Manzara", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["Arthur's Seat", "Salisbury Crags", "Holyrood Park", "Duddingston Village", "Sheep Heid Inn (Pub)"],
        interests: ["Doğa", "Macera", "Yemek"],
        accentColor: const Color(0xFF27AE60),
        icon: Icons.landscape,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // GIETHOORN ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getGiethoornRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "gie_boat",
        name: isEnglish ? "Venice of the North" : "Kuzeyin Venediği",
        description: isEnglish 
          ? "No roads, just canals: Boat tour and thatched-roof cottages"
          : "Yol yok, sadece kanallar: Tekne turu ve saz çatılı evler.",
        duration: isEnglish ? "3 hours" : "3 saat",
        distance: "3 km",
        difficulty: isEnglish ? "Easy" : "Kolay",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/giethoorn/giethoorn_canals.jpg",
        tags: [isEnglish ? "Boat" : "Tekne", isEnglish ? "Village" : "Köy", isEnglish ? "Nature" : "Doğa"],
        placeNames: ["Giethoorn Canals", "Museum Giethoorn 't Olde Maat Uus", "Binnenpad (Walking Path)", "Smit's Paviljoen (Lunch)"],
        interests: ["Doğa", "Huzur", "Yemek"],
        accentColor: const Color(0xFF2980B9),
        icon: Icons.directions_boat,
      ),
    ];
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // HALLSTATT ROTALARI
  // ═══════════════════════════════════════════════════════════════════════════
  static List<CuratedRoute> _getHallstattRoutes(bool isEnglish) {
    return [
      CuratedRoute(
        id: "hal_view",
        name: isEnglish ? "Alpine Fairytale" : "Alp Masalı",
        description: isEnglish 
          ? "Postcard perfect: Lake views, salt mine and skywalk"
          : "Kartpostal gibi: Göl manzaraları, tuz madeni ve skywalk.",
        duration: isEnglish ? "5 hours" : "5 saat",
        distance: "4 km",
        difficulty: isEnglish ? "Medium" : "Orta",
        imageUrl: "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/oslo/salt.jpg",
        tags: [isEnglish ? "Lake" : "Göl", isEnglish ? "Mountain" : "Dağ", "UNESCO"],
        placeNames: ["Hallstatt Skywalk (Welterbeblick)", "Salt Mine (Salzwelten)", "Market Square", "Lake Hallstatt", "Bone House (Beinhaus)", "Seehotel Grüner Baum"],
        interests: ["Manzara", "Doğa", "Yemek"],
        accentColor: const Color(0xFF3498DB),
        icon: Icons.camera_alt,
      ),
    ];
  }

  static List<CuratedRoute> _getGenericRoutes(String city, bool isEnglish) {
    return [];
  }
}


