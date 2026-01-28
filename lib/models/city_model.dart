// =============================================================================
// CITY MODEL v3 - TÜM JSON ALANLARI DESTEKLİ
// Paris, Roma, İstanbul, Barcelona uyumlu
// =============================================================================

class CityModel {
  final String city;
  final String country;
  final String currency;
  final String language;
  final String timezone;
  final String emergency;
  final String description;
  final String? descriptionEn;
  final String? cityEn;
  final String? countryEn;
  final double centerLat;
  final double centerLng;
  final TransportInfo? transport;
  final List<Highlight> highlights;
  final List<Region> regions;
  final List<String> localTips;
  final FoodGuide? foodGuide;
  final String? heroImage;

  CityModel({
    required this.city,
    this.country = "",
    this.currency = "EUR",
    this.language = "",
    this.timezone = "",
    this.emergency = "112",
    this.description = "",
    this.descriptionEn,
    this.cityEn,
    this.countryEn,
    required this.centerLat,
    required this.centerLng,
    this.transport,
    required this.highlights,
    this.regions = const [],
    this.localTips = const [],
    this.foodGuide,
    this.heroImage,
  });

  factory CityModel.fromJson(Map<String, dynamic> json) {
    // Koordinatlar - hem eski format (centerCoords) hem yeni format (coordinates) destekli
    double lat = 0.0;
    double lng = 0.0;

    if (json["coordinates"] != null) {
      final coords = json["coordinates"] as Map<String, dynamic>;
      lat = (coords["lat"] as num?)?.toDouble() ?? 0.0;
      lng = (coords["lng"] as num?)?.toDouble() ?? 0.0;
    } else if (json["centerCoords"] != null) {
      final center = json["centerCoords"] as List;
      lat = (center[0] as num).toDouble();
      lng = (center[1] as num).toDouble();
    }

    return CityModel(
      city: json["city"] ?? "",
      country: json["country"] ?? "",
      currency: json["currency"] ?? "EUR",
      language: json["language"] ?? "",
      timezone: json["timezone"] ?? "",
      emergency: json["emergency"] ?? "112",
      description: json["description"] ?? "",
      descriptionEn: json["description_en"],
      cityEn: json["city_en"],
      countryEn: json["country_en"],
      centerLat: lat,
      centerLng: lng,
      transport: json["transport"] != null
          ? TransportInfo.fromJson(json["transport"])
          : null,
      highlights:
          (json["highlights"] as List?)
              ?.map((e) => Highlight.fromJson(e, city: json["city"]))
              .toList() ??
          [],
      regions:
          (json["regions"] as List?)?.map((e) => Region.fromJson(e)).toList() ??
          [],
      localTips:
          (json["localTips"] as List?)?.map((e) => e.toString()).toList() ?? [],
      foodGuide: json["foodGuide"] != null
          ? FoodGuide.fromJson(json["foodGuide"])
          : null,
      heroImage: json["heroImage"],
    );
  }

  /// Dil seçimine göre şehir ismini döndürür.
  String getLocalizedCityName(bool isEnglish) {
    if (isEnglish && cityEn != null && cityEn!.isNotEmpty) {
      return cityEn!;
    }
    return city;
  }
}

class TransportInfo {
  final bool metro;
  final bool bus;
  final bool tram;
  final bool bikeSharing;
  final String taxiApp;
  final String airportCode;
  final String airportTransfer;

  TransportInfo({
    this.metro = false,
    this.bus = false,
    this.tram = false,
    this.bikeSharing = false,
    this.taxiApp = "",
    this.airportCode = "",
    this.airportTransfer = "",
  });

  factory TransportInfo.fromJson(Map<String, dynamic> json) {
    return TransportInfo(
      metro: json["metro"] ?? false,
      bus: json["bus"] ?? false,
      tram: json["tram"] ?? false,
      bikeSharing: json["bike_sharing"] ?? false,
      taxiApp: json["taxi_app"] ?? "",
      airportCode: json["airport_code"] ?? "",
      airportTransfer: json["airport_transfer"] ?? "",
    );
  }
}

class Highlight {
  final String name;
  final String area;
  final String category;
  final String? city;
  final List<String> tags;
  final double distanceFromCenter;
  final double lat;
  final double lng;
  final String price;
  final String description;
  final String? imageUrl;
  final String? tips;
  final String? descriptionEn;
  final String? nameEn;
  final String? areaEn; // Added areaEn
  final String? tipsEn;
  final String? bestTime;
  final String? bestTimeEn;
  final String? duration;
  final double? rating;
  final int? reviewCount;
  final String? metro;
  final String? priceRange;
  final String? website;
  final String? phone;
  final String? instagram;
  final bool? parking;
  final String? reservation;
  final Map<String, String>? openHours;
  final List<String>? features;

  Highlight({
    required this.name,
    required this.area,
    required this.category,
    this.city,
    required this.tags,
    required this.distanceFromCenter,
    required this.lat,
    required this.lng,
    required this.price,
    required this.description,
    this.imageUrl,
    this.tips,
    this.nameEn,
    this.areaEn,
    this.descriptionEn,
    this.tipsEn,
    this.bestTime,
    this.bestTimeEn,
    this.duration,
    this.rating,
    this.reviewCount,
    this.metro,
    this.priceRange,
    this.website,
    this.phone,
    this.instagram,
    this.parking,
    this.reservation,
    this.openHours,
    this.features,
  });

  // Backward compatibility
  String? get displaydetImage => imageUrl;

  /// Dil seçimine göre isim döndürür. nameEn yoksa name kullanır.
  String getLocalizedName(bool isEnglish) {
    if (isEnglish && nameEn != null && nameEn!.isNotEmpty) {
      return nameEn!;
    }
    return name;
  }

  /// Dil seçimine göre açıklama döndürür. descriptionEn yoksa description kullanır.
  String getLocalizedDescription(bool isEnglish) {
    if (isEnglish && descriptionEn != null && descriptionEn!.isNotEmpty) {
      return descriptionEn!;
    }
    return description;
  }

  /// Dil seçimine göre bölge döndürür. areaEn yoksa area kullanır.
  String getLocalizedArea(bool isEnglish) {
    if (isEnglish && areaEn != null && areaEn!.isNotEmpty) {
      return areaEn!;
    }
    return area;
  }

  factory Highlight.fromJson(Map<String, dynamic> json, {String? city}) {
    // openHours'u parse et
    Map<String, String>? openHours;
    if (json["openHours"] != null) {
      openHours = Map<String, String>.from(
        (json["openHours"] as Map).map(
          (k, v) => MapEntry(k.toString(), v.toString()),
        ),
      );
    }

    return Highlight(
      name: json["name"] ?? "",
      area: json["area"] ?? "",
      category: json["category"] ?? "",
      city: city,
      tags: (json["tags"] as List?)?.map((e) => e.toString()).toList() ?? [],
      distanceFromCenter:
          (json["distanceFromCenter"] as num?)?.toDouble() ?? 0.0,
      lat: (json["lat"] as num?)?.toDouble() ?? 0.0,
      lng: (json["lng"] as num?)?.toDouble() ?? 0.0,
      price: json["price"] ?? "medium",
      description: json["description"] ?? "",
      imageUrl: json["imageUrl"],
      tips: json["tips"],
      nameEn: json["name_en"],
      areaEn: json["area_en"], // Parse area_en
      descriptionEn: json["description_en"],
      tipsEn: json["tips_en"],
      bestTime: json["bestTime"],
      bestTimeEn: json["bestTime_en"],
      duration: json["duration"],
      rating: (json["rating"] as num?)?.toDouble(),
      reviewCount: json["reviewCount"] as int?,
      metro: json["metro"],
      priceRange: json["priceRange"],
      website: json["website"],
      phone: json["phone"],
      instagram: json["instagram"],
      parking: json["parking"] as bool?,
      reservation: json["reservation"],
      openHours: openHours,
      features: (json["features"] as List?)?.map((e) => e.toString()).toList(),
    );
  }
}

class Region {
  final String name;
  final String localName;
  final String description;
  final String vibe;
  final List<String> bestFor;
  final int walkability;
  final int safetyRating;
  final String priceLevel;

  Region({
    required this.name,
    this.localName = "",
    this.description = "",
    this.vibe = "",
    this.bestFor = const [],
    this.walkability = 3,
    this.safetyRating = 4,
    this.priceLevel = "medium",
  });

  factory Region.fromJson(Map<String, dynamic> json) {
    return Region(
      name: json["name"] ?? "",
      localName: json["localName"] ?? "",
      description: json["description"] ?? "",
      vibe: json["vibe"] ?? "",
      bestFor:
          (json["bestFor"] as List?)?.map((e) => e.toString()).toList() ?? [],
      walkability: json["walkability"] ?? 3,
      safetyRating: json["safetyRating"] ?? 4,
      priceLevel: json["priceLevel"]?.toString() ?? "medium",
    );
  }
}

class FoodGuide {
  final List<String> mustTry;
  final List<String> localDrinks;
  final String tipping;

  FoodGuide({
    this.mustTry = const [],
    this.localDrinks = const [],
    this.tipping = "",
  });

  factory FoodGuide.fromJson(Map<String, dynamic> json) {
    return FoodGuide(
      mustTry:
          (json["must_try"] as List?)?.map((e) => e.toString()).toList() ?? [],
      localDrinks:
          (json["local_drinks"] as List?)?.map((e) => e.toString()).toList() ??
          [],
      tipping: json["tipping"] ?? "",
    );
  }
}
