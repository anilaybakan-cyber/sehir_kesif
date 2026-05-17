import 'dart:math';
import 'package:flutter/material.dart';
import '../models/city_model.dart';
import '../models/route_archetype.dart';
import 'curated_routes_service.dart';

// User Preferences Simulation for now (can be replaced by real model)
class UserPreferences {
  final List<String> interests;
  final String budget; // low, medium, high

  UserPreferences({
    this.interests = const [],
    this.budget = 'medium',
  });
}

class DynamicRouteService {
  // ---------------------------------------------------------------------------
  // ARCHETYPE DEFINITIONS
  // ---------------------------------------------------------------------------
  static final Map<RouteSpirit, RouteArchetype> archetypes = {
    RouteSpirit.classic: RouteArchetype(
      spirit: RouteSpirit.classic,
      titleTr: "İlk Kez Gelenler",
      titleEn: "First Time Classics",
      descriptionTr: "Şehrin olmazsa olmazları: Meydanlar ve ikonik yapılar.",
      descriptionEn: "City essentials: Squares and iconic landmarks.",
      spiritQuoteTr: "Şehre hoş geldin, kaybolmak yok.",
      spiritQuoteEn: "Welcome to the city, no getting lost.",
      icon: Icons.flag,
      color: Colors.redAccent,
      primaryTags: [
        "landmark", "iconic", "history", "square", "must_see", "tarihi", "meydan", "ikonik", 
        "müze", "museum", "saray", "palace", "kilise", "church", "mosque", "cami", "kale", "castle", "monument", "anıt"
      ],
      secondaryTags: ["cafe", "view", "photo", "kafe", "manzara", "fotoğraf"],
    ),
    RouteSpirit.history: RouteArchetype(
      spirit: RouteSpirit.history,
      titleTr: "Tarih & Kültür",
      titleEn: "History & Culture",
      descriptionTr: "Müzeler, eski sokaklar ve zaman yolculuğu.",
      descriptionEn: "Museums, old streets and time travel.",
      spiritQuoteTr: "Taşların hikayesini dinle.",
      spiritQuoteEn: "Listen to the story of the stones.",
      icon: Icons.account_balance,
      color: Colors.brown,
      primaryTags: ["museum", "history", "ancient", "culture", "church", "mosque", "müze", "tarihi", "kilise", "cami", "kültür", "arkeoloji", "saray", "bazilika"],
      secondaryTags: ["historic_cafe", "park", "quiet", "tarihi kafe", "sessiz"],
    ),
    RouteSpirit.localDiscovery: RouteArchetype(
      spirit: RouteSpirit.localDiscovery,
      titleTr: "Yan Sokaklar",
      titleEn: "Hidden Gems",
      descriptionTr: "Turist rotasından bilinçli kaçış.",
      descriptionEn: "Conscious escape from the tourist path.",
      spiritQuoteTr: "Yan sokaklara güven.",
      spiritQuoteEn: "Trust the side streets.",
      icon: Icons.map,
      color: Colors.orange,
      primaryTags: ["local", "hidden", "street", "neighborhood", "authentic", "yerel", "gizli", "sokak", "mahalle", "deneyim", "duvar resmi", "pasaj"],
      secondaryTags: ["street_food", "coffee", "bistro", "sokak lezzeti", "kahve"],
    ),
    RouteSpirit.foodie: RouteArchetype(
      spirit: RouteSpirit.foodie,
      titleTr: "Lezzet Avı",
      titleEn: "Taste Hunter",
      descriptionTr: "Sokak lezzetleri ve yerel tatlar.",
      descriptionEn: "Street food and local flavors.",
      spiritQuoteTr: "Şehri tadarak keşfet.",
      spiritQuoteEn: "Discover the city by tasting it.",
      icon: Icons.restaurant,
      color: Colors.deepOrange,
      primaryTags: ["food", "restaurant", "street_food", "local_dish", "dessert", "yemek", "restoran", "lezzet", "tatlı", "yeme-içme", "gurme", "geleneksel", "pastane", "çikolata", "waffle", "bira", "midye"],
      secondaryTags: ["walk", "park", "view", "yürüyüş"],
    ),
    RouteSpirit.shopping: RouteArchetype(
      spirit: RouteSpirit.shopping,
      titleTr: "Alışveriş & Keyif",
      titleEn: "Shop & Chill",
      descriptionTr: "Butikler, pazarlar ve kahve molaları.",
      descriptionEn: "Boutiques, markets and coffee breaks.",
      spiritQuoteTr: "Kendini şımartma günü.",
      spiritQuoteEn: "Treat yourself day.",
      icon: Icons.shopping_bag,
      color: Colors.purple,
      primaryTags: ["shopping", "boutique", "market", "souvenir", "fashion", "alışveriş", "butik", "pazar", "hediyelik", "moda", "tasarım"],
      secondaryTags: ["cafe", "bakery", "dessert", "kafe", "tatlı"],
    ),
    RouteSpirit.nature: RouteArchetype(
      spirit: RouteSpirit.nature,
      titleTr: "Yeşile Kaçış",
      titleEn: "Nature Escape",
      descriptionTr: "Parklar, bahçeler ve derin bir nefes.",
      descriptionEn: "Parks, gardens and a deep breath.",
      spiritQuoteTr: "Şehirden bir adım uzaklaş.",
      spiritQuoteEn: "Step away from the noise.",
      icon: Icons.park,
      color: Colors.green,
      primaryTags: ["park", "nature", "garden", "lake", "forest", "doğa", "bahçe", "göl", "orman", "yeşil alan"],
      secondaryTags: ["picnic", "cafe", "reading", "piknik", "kitap"],
    ),
    RouteSpirit.romantic: RouteArchetype(
      spirit: RouteSpirit.romantic,
      titleTr: "Altın Saat (Romantik)",
      titleEn: "Golden Hour",
      descriptionTr: "Manzara noktaları ve gün batımı.",
      descriptionEn: "Viewpoints and sunset vibes.",
      spiritQuoteTr: "Anın tadını çıkar.",
      spiritQuoteEn: "Enjoy the moment.",
      icon: Icons.favorite,
      color: Colors.pink,
      primaryTags: ["romantic", "view", "sunset", "terrace", "cocktail", "romantik", "manzara", "gün batımı", "teras", "aşk"],
      secondaryTags: ["photo", "wine", "dinner", "şarap", "akşam yemeği"],
    ),
    RouteSpirit.creative: RouteArchetype(
      spirit: RouteSpirit.creative,
      titleTr: "Sanat & Tasarım",
      titleEn: "Art & Design",
      descriptionTr: "Galeriler, sokak sanatı ve tasarım.",
      descriptionEn: "Galleries, street art and design.",
      spiritQuoteTr: "İlham her yerde.",
      spiritQuoteEn: "Inspiration is everywhere.",
      icon: Icons.palette,
      color: Colors.indigo,
      primaryTags: ["art", "gallery", "street_art", "design", "museum_art", "sanat", "galeri", "tasarım", "sokak sanatı", "müze", "heykel"],
      secondaryTags: ["concept_store", "coffee", "bookstore", "kitapçı"],
    ),
    RouteSpirit.nightlife: RouteArchetype(
      spirit: RouteSpirit.nightlife,
      titleTr: "Gece Hayatı",
      titleEn: "Night Owl",
      descriptionTr: "Karanlık çökünce şehir canlanır.",
      descriptionEn: "City comes alive after dark.",
      spiritQuoteTr: "Gece henüz genç.",
      spiritQuoteEn: "The night is still young.",
      icon: Icons.nightlife,
      color: Colors.deepPurple,
      primaryTags: ["nightlife", "bar", "pub", "club", "music", "gece", "kulüp", "müzik", "eğlence", "kokteyl", "bira"],
      secondaryTags: ["late_night_food", "view", "square", "gece atıştırmalığı", "meydan"],
    ),
    RouteSpirit.relaxed: RouteArchetype(
      spirit: RouteSpirit.relaxed,
      titleTr: "Yormayan Rota",
      titleEn: "Easy & Relaxed",
      descriptionTr: "Az yürüyüş, sık mola, maksimum keyif.",
      descriptionEn: "Less walking, more breaks, maximum joy.",
      spiritQuoteTr: "Acelemiz yok.",
      spiritQuoteEn: "No rush today.",
      icon: Icons.family_restroom,
      color: Colors.teal,
      primaryTags: ["easy", "kids", "museum_kids", "park", "kolay", "çocuk", "oyun", "eğlence", "müze"],
      secondaryTags: ["ice_cream", "rest", "waffles", "dondurma", "mola"],
    ),
  };

  // ---------------------------------------------------------------------------
  // GENERATION LOGIC
  // ---------------------------------------------------------------------------
  
  static Future<CuratedRoute?> generateRoute({
     required CityModel city,
     required RouteSpirit spirit,
     required bool isEnglish,
     UserPreferences? preferences,
   }) async {
    final archetype = archetypes[spirit]!;
    // V4.3: Day-trip yerleri normal tematik rotalara katma
    final List<Highlight> allPlaces = city.highlights.where((h) => !h.isDayTrip).toList();
    
    // 1. Filter Candidates based on Primary Tags & Interests
    List<Highlight> primaryCandidates = allPlaces.where((h) {
      if (h.lat == 0 || h.lng == 0) return false;
      return _matchesTags(h, archetype.primaryTags, preferences?.interests);
    }).toList();

    // 2. Filter Secondary Candidates (Rest/Support spots)
    List<Highlight> secondaryCandidates = allPlaces.where((h) {
      if (h.lat == 0 || h.lng == 0) return false;
      return _matchesTags(h, archetype.secondaryTags, null) && 
             !primaryCandidates.contains(h);
    }).toList();

    // 3. Select Backbone (Main Stops) - Limit to 3-4 main stops
    // Sorting Heuristic: Prioritize Landmarks/Museums, then by rating
    primaryCandidates.sort((a, b) {
      // High priority categories for "Classic" routes
      const highPriorityCategories = ["landmark", "museum", "square", "ikonik", "müze", "meydan", "tarihi"];
      
      bool aIsHigh = highPriorityCategories.contains(a.category.toLowerCase()) || 
                     a.tags.any((t) => highPriorityCategories.contains(t.toLowerCase()));
      bool bIsHigh = highPriorityCategories.contains(b.category.toLowerCase()) || 
                     b.tags.any((t) => highPriorityCategories.contains(t.toLowerCase()));

      if (aIsHigh && !bIsHigh) return -1;
      if (!aIsHigh && bIsHigh) return 1;

      // Secondary: Rating
      return (b.rating ?? 0).compareTo(a.rating ?? 0);
    });
    final mainStops = primaryCandidates.take(4).toList();

    if (mainStops.isEmpty) {
      // Fallback if no matching places found - Return null instead of "fake" route
      return null;
    }

    // 4. Build Route with Breaks
    List<String> routePlaceNames = [];
    Highlight? lastStop;
    
    for (int i = 0; i < mainStops.length; i++) {
      final stop = mainStops[i];
      routePlaceNames.add(stop.getLocalizedName(isEnglish));
      
      lastStop = stop;

      // Smart Break Injection
      if ((i + 1) % archetype.pacingInterval == 0 && i < mainStops.length - 1) {
        // Find a break spot near the current stop
        final breakSpot = _findNearest(lastStop, secondaryCandidates);
        if (breakSpot != null) {
          routePlaceNames.add(breakSpot.getLocalizedName(isEnglish));
          secondaryCandidates.remove(breakSpot); // Don't reuse
        }
      }
    }

    // 5. Trim to Max 7 Stops
    if (routePlaceNames.length > 7) {
      routePlaceNames = routePlaceNames.take(7).toList();
    }

    // 6. Create Result
    return CuratedRoute(
      id: "dynamic_${spirit.name}_${city.city.toLowerCase()}",
      name: archetype.getTitle(isEnglish),
      description: "${archetype.getDescription(isEnglish)}\n\n\"${archetype.getQuote(isEnglish)}\"",
      duration: isEnglish ? "4-5 hours" : "4-5 saat", // Estimate based on stop count
      distance: "~4 km", // Estimate
      difficulty: isEnglish ? "Easy" : "Kolay",
      imageUrl: mainStops.first.imageUrl ?? city.heroImage ?? "",
      tags: archetype.primaryTags.take(3).toList(),
      placeNames: routePlaceNames,
      interests: archetype.primaryTags.take(3).toList(),
      accentColor: archetype.color,
      icon: archetype.icon,
    );
  }

  // ---------------------------------------------------------------------------
  // HELPERS
  // ---------------------------------------------------------------------------

  static bool _matchesTags(Highlight place, List<String> targetTags, List<String>? userInterests) {
    // Check tags
    bool tagMatch = place.tags.any((t) => targetTags.contains(t.toLowerCase()));
    
    // Check category
    bool categoryMatch = targetTags.contains(place.category.toLowerCase());
    
    bool match = tagMatch || categoryMatch;
    
    // Boost score if matches user interest (could implement scoring later)
    if (userInterests != null && userInterests.isNotEmpty) {
      bool interestMatch = place.tags.any((t) => userInterests.contains(t.toLowerCase()));
      // For now, strict OR logic. Later can be scoring.
      return match || interestMatch;
    }
    
    return match;
  }

  static Highlight? _findNearest(Highlight origin, List<Highlight> candidates) {
    if (candidates.isEmpty) return null;
    
    Highlight? nearest;
    double minDist = double.infinity;

    for (var candidate in candidates) {
      final dist = _calculateDistance(origin.lat, origin.lng, candidate.lat, candidate.lng);
      if (dist < minDist && dist < 1.0) { // Only break spots within 1km
        minDist = dist;
        nearest = candidate;
      }
    }
    return nearest;
  }

  // Haversine formula for distance
  static double _calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    var p = 0.017453292519943295;
    var c = cos;
    var a = 0.5 - c((lat2 - lat1) * p)/2 + 
          c(lat1 * p) * c(lat2 * p) * 
          (1 - c((lon2 - lon1) * p))/2;
    return 12742 * asin(sqrt(a));
  }
}
