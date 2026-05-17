// =============================================================================
// CITY MODEL v3 - TÜM JSON ALANLARI DESTEKLİ
// Paris, Roma, İstanbul, Barcelona uyumlu
// =============================================================================

import 'package:flutter/material.dart';
import '../l10n/app_localizations.dart';

class CityModel {
  String city;
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
  final CityGuide? guide;
  final List<CuratedRouteData> curatedRoutes;


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
    this.guide,
    this.curatedRoutes = const [],
  });


  factory CityModel.fromJson(Map<String, dynamic> json) {
    // Koordinatlar - hem eski format (centerCoords) hem yeni format (coordinates) destekli
    double lat = 0.0;
    double lng = 0.0;

    if (json["coordinates"] != null) {
      if (json["coordinates"] is Map) {
        final coords = json["coordinates"] as Map<String, dynamic>;
        lat = (coords["lat"] as num?)?.toDouble() ?? (coords["latitude"] as num?)?.toDouble() ?? 0.0;
        lng = (coords["lng"] as num?)?.toDouble() ?? (coords["longitude"] as num?)?.toDouble() ?? 0.0;
      } else if (json["coordinates"] is List) {
        final coords = json["coordinates"] as List;
        if (coords.length >= 2) {
          lat = (coords[0] as num).toDouble();
          lng = (coords[1] as num).toDouble();
        }
      }
    } else if (json["centerCoords"] != null) {
      final center = json["centerCoords"] as List;
      lat = (center[0] as num).toDouble();
      lng = (center[1] as num).toDouble();
    }

    return CityModel(
      city: json["city"] ?? json["name"] ?? json["cityName"] ?? "",
      country: json["country"] ?? "",
      currency: json["currency"] ?? "EUR",
      language: json["language"] ?? "",
      timezone: json["timezone"] ?? "",
      emergency: json["emergency"] ?? "112",
      description: json["description"] ?? "",
      descriptionEn: json["description_en"] ?? json["descriptionEn"],
      cityEn: json["city_en"] ?? json["cityEn"],
      countryEn: json["country_en"] ?? json["countryEn"],
      centerLat: lat,
      centerLng: lng,
      transport: json["transport"] != null
          ? TransportInfo.fromJson(json["transport"])
          : null,
      highlights:
          (json["highlights"] as List?)
              ?.map((e) => Highlight.fromJson(e, city: json["city"] ?? json["name"]))
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
      heroImage: json["heroImage"] ?? json["hero_image"] ?? json["image"],
      guide: json["guide"] != null ? CityGuide.fromJson(json["guide"]) : null,
      curatedRoutes: (json["curated_routes"] as List?)
              ?.map((e) => CuratedRouteData.fromJson(e))
              .toList() ??
          [],
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
  final String? id;
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
  final String? blurHash;
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
    this.id,
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
    this.blurHash,
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

  /// Bu mekan günübirlik bir gezi mi? (şehir merkezinden uzak, tüm gün alır)
  /// 4 farklı sinyale bakar:
  ///   1. distanceFromCenter > 30 km
  ///   2. area / areaEn içinde "günübirlik" / "day trip" geçiyor mu
  ///   3. bestTime / bestTimeEn "tüm gün" / "full day" ise
  ///   4. tags içinde "day_trip" / "daytrip" / "günübirlik" var mı
  bool get isDayTrip {
    if (distanceFromCenter > 25.0) return true;

    final nameLower = name.toLowerCase();
    final areaLower = area.toLowerCase();
    final areaEnLower = (areaEn ?? '').toLowerCase();
    final descLower = description.toLowerCase();
    final descEnLower = (descriptionEn ?? '').toLowerCase();

    // V4.4: Ada (Island) veya feribot/tekne turu gerektiren yerler her zaman günübirliktir
    final isIslandRelated = nameLower.contains('ada') || nameLower.contains('island') || 
                          areaLower.contains('meis') || nameLower.contains('megisti') ||
                          descLower.contains('feribot') || descLower.contains('ferry') ||
                          nameLower.contains('yunan') || nameLower.contains('greek');
    
    final isBoatTour = nameLower.contains('tekne turu') || nameLower.contains('boat tour') ||
                       nameLower.contains('boğaz turu') || nameLower.contains('bosphorus tour');

    if (isIslandRelated || isBoatTour) return true;

    if (areaLower.contains('günübirlik') ||
        areaLower.contains('gunubirlik') ||
        areaEnLower.contains('day trip') ||
        areaEnLower.contains('daytrip')) {
      return true;
    }

    final btLower = (bestTime ?? '').toLowerCase();
    final btEnLower = (bestTimeEn ?? '').toLowerCase();
    if (btLower.contains('tüm gün') ||
        btLower.contains('tum gun') ||
        btEnLower.contains('full day') ||
        btEnLower.contains('all day')) {
      return true;
    }

    for (final t in tags) {
      final tl = t.toLowerCase();
      if (tl == 'day_trip' ||
          tl == 'daytrip' ||
          tl == 'day-trip' ||
          tl == 'günübirlik' ||
          tl == 'gunubirlik') {
        return true;
      }
    }

    return false;
  }

  /// Day-trip için tahmini toplam süre (gidiş + ziyaret + dönüş, dakika).
  /// Mesafeye göre kabaca: 30-80 km → 6 saat, 80-150 km → 8 saat, 150+ → 10 saat.
  int get dayTripDurationMinutes {
    if (distanceFromCenter <= 80) return 360; // 6h
    if (distanceFromCenter <= 150) return 480; // 8h
    return 600; // 10h
  }

  /// Mekanın ideal zaman penceresi (Time Window).
  /// Schedule atama sırasında sabah/akşam uyumunu kontrol etmek için kullanılır.
  /// 
  /// Örnek:
  /// - Karaoke/bar → NIGHT (21:00+)
  /// - Akşam yemeği → EVENING (17:00-21:00)
  /// - Müze → MORNING veya AFTERNOON (09:00-17:00)
  TimeWindow get idealTimeWindow {
    final cat = category.toLowerCase();
    final nameLower = name.toLowerCase();
    final bt = (bestTime ?? '').toLowerCase();
    final btEn = (bestTimeEn ?? '').toLowerCase();
    final tagList = tags.map((t) => t.toLowerCase()).toList();

    // 1. Explicit bestTime parsing (en güçlü sinyal)
    if (bt.contains('gece') || bt.contains('gece') || btEn.contains('night') || btEn.contains('late')) {
      return TimeWindow.NIGHT;
    }
    if (bt.contains('akşam') || bt.contains('aksam') || btEn.contains('evening')) {
      return TimeWindow.EVENING;
    }
    if (bt.contains('sabah') || bt.contains('kahvaltı') || btEn.contains('morning')) {
      return TimeWindow.MORNING;
    }
    if (bt.contains('öğle') || bt.contains('ogle') || btEn.contains('afternoon')) {
      return TimeWindow.AFTERNOON;
    }

    // 2. Category-based inference
    bool isNightlife = cat.contains('bar') || cat.contains('pub') || cat.contains('gece') ||
                       cat.contains('night') || cat.contains('club') || cat.contains('karaoke') ||
                       nameLower.contains('karaoke') || nameLower.contains('bar') ||
                       tagList.contains('gece hayatı') || tagList.contains('nightlife') ||
                       tagList.contains('bar') || tagList.contains('pub');

    if (isNightlife) {
      // Akşam yemeği arası barlar EVENING, gece kulüpleri NIGHT
      if (cat.contains('restoran') || cat.contains('yemek') || nameLower.contains('restaurant')) {
        return TimeWindow.EVENING;
      }
      return TimeWindow.NIGHT;
    }

    // 3. Food with meal-time inference
    if (cat.contains('yemek') || cat.contains('food') || cat.contains('restoran') ||
        tagList.contains('yemek') || tagList.contains('restoran')) {
      // İsim bazlı meal time inference
      if (nameLower.contains('kahvaltı') || nameLower.contains('breakfast') ||
          nameLower.contains('kahve') || nameLower.contains('brunch')) {
        return TimeWindow.MORNING;
      }
      if (nameLower.contains('öğle') || nameLower.contains('lunch')) {
        return TimeWindow.AFTERNOON;
      }
      if (nameLower.contains('akşam') || nameLower.contains('dinner') ||
          nameLower.contains('gece') || nameLower.contains('night')) {
        return TimeWindow.EVENING;
      }
      // Default food = flexible (lunch/afternoon preferred)
      return TimeWindow.AFTERNOON;
    }

    // 4. Coffee → Morning or Afternoon
    if (cat.contains('kafe') || cat.contains('cafe') || cat.contains('coffee') ||
        tagList.contains('kahve') || tagList.contains('coffee')) {
      return TimeWindow.MORNING; // Kahve sabah öğleden önce tercih edilir
    }

    // 5. Culture/Museum → Morning-Afternoon (daylight hours)
    if (cat.contains('müze') || cat.contains('museum') || cat.contains('tarih') ||
        cat.contains('kültür') || cat.contains('culture') || cat.contains('sanat') ||
        cat.contains('art') || cat.contains('gallery')) {
      return TimeWindow.MORNING; // Müzeler sabah daha az kalabalık
    }

    // 6. Nature/View → Morning-Afternoon (daylight)
    if (cat.contains('doğa') || cat.contains('nature') || cat.contains('park') ||
        cat.contains('manzara') || cat.contains('view') || cat.contains('teras') ||
        cat.contains('garden') || cat.contains('bahçe')) {
      return TimeWindow.AFTERNOON; // Manzara öğleden sonra güneşle daha iyi
    }

    // Default: flexible (morning preferred for efficiency)
    return TimeWindow.MORNING;
  }

  /// Verilen saat (HH:MM formatında) bu mekanın ideal zaman penceresine uyuyor mu?
  bool isTimeSuitable(String timeStr) {
    final parts = timeStr.split(':');
    if (parts.length != 2) return true; // Parse error = flexible
    final hour = int.tryParse(parts[0]) ?? 12;

    final window = idealTimeWindow;

    switch (window) {
      case TimeWindow.MORNING:
        return hour >= 7 && hour <= 12; // 07:00-12:00
      case TimeWindow.AFTERNOON:
        return hour >= 11 && hour <= 17; // 11:00-17:00
      case TimeWindow.EVENING:
        return hour >= 17 && hour <= 21; // 17:00-21:00
      case TimeWindow.NIGHT:
        return hour >= 20 || hour <= 3; // 20:00-03:00 (gece yarısı geçişi)
      default:
        return true;
    }
  }

  // ===========================================================================
  // OPENING HOURS PARSING
  // ===========================================================================

  /// Verilen saatte mekan açık mı?
  /// [hour]: 0-23, [minute]: 0-59, [dayOfWeek]: monday, tuesday, ... (küçük harf)
  /// openHours yoksa veya parse edilemezse true döner (esnek davranış)
  bool isOpenAt(int hour, int minute, {String? dayOfWeek}) {
    if (openHours == null || openHours!.isEmpty) return true;

    // Gün belirtilmemişse veya geçersizse, tüm günlerin ortak aralığını kullan
    String day = dayOfWeek?.toLowerCase() ?? '';
    final validDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

    if (!validDays.contains(day)) {
      // Gün belirtilmemiş - tüm günlerde ortak açık saatler varsa onları kullan
      // Yoksa true döner (esnek)
      return _isOpenConsideringAllDays(hour, minute);
    }

    final hoursStr = openHours![day] ?? openHours!['everyday'] ?? openHours!['daily'];
    if (hoursStr == null || hoursStr.isEmpty) return true;

    return _parseAndCheckOpen(hoursStr, hour, minute);
  }

  /// Belirli bir gün için açılış saatini dakika cinsinden döndürür (0-1439)
  /// -1 = parse edilemedi veya kapalı
  int getOpeningMinutes(String dayOfWeek) {
    if (openHours == null) return -1;

    final day = dayOfWeek.toLowerCase();
    final hoursStr = openHours![day] ?? openHours!['everyday'] ?? openHours!['daily'];
    if (hoursStr == null || hoursStr.isEmpty) return -1;

    return _parseOpeningMinutes(hoursStr);
  }

  /// Belirli bir gün için kapanış saatini dakika cinsinden döndürür (0-1439)
  /// -1 = parse edilemedi veya kapalı
  int getClosingMinutes(String dayOfWeek) {
    if (openHours == null) return -1;

    final day = dayOfWeek.toLowerCase();
    final hoursStr = openHours![day] ?? openHours!['everyday'] ?? openHours!['daily'];
    if (hoursStr == null || hoursStr.isEmpty) return -1;

    return _parseClosingMinutes(hoursStr);
  }

  /// Tüm günlerde ortak olan açılış/kapanış saatlerini bul
  /// Schedule oluşturma için ideal başlangıç ve bitiş saatlerini döndürür
  ({int openMinutes, int closeMinutes})? getTypicalHours() {
    if (openHours == null || openHours!.isEmpty) return null;

    final validDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
    List<int> openingTimes = [];
    List<int> closingTimes = [];

    for (final day in validDays) {
      final hoursStr = openHours![day] ?? openHours!['everyday'] ?? openHours!['daily'];
      if (hoursStr == null || hoursStr.isEmpty) continue;

      final openMin = _parseOpeningMinutes(hoursStr);
      final closeMin = _parseClosingMinutes(hoursStr);

      if (openMin >= 0 && closeMin >= 0) {
        openingTimes.add(openMin);
        closingTimes.add(closeMin);
      }
    }

    if (openingTimes.isEmpty || closingTimes.isEmpty) return null;

    // En geç açılış ve en erken kapanış (en kısıtlayıcı ama güvenli)
    openingTimes.sort();
    closingTimes.sort();

    return (
      openMinutes: openingTimes.last, // En geç açılış (güvenli taraf)
      closeMinutes: closingTimes.first, // En erken kapanış (güvenli taraf)
    );
  }

  // ===========================================================================
  // PRIVATE HELPERS
  // ===========================================================================

  bool _isOpenConsideringAllDays(int hour, int minute) {
    // Tüm günlerde açık mı kontrol et
    final validDays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

    for (final day in validDays) {
      final hoursStr = openHours![day] ?? openHours!['everyday'] ?? openHours!['daily'];
      if (hoursStr == null || hoursStr.isEmpty) continue;

      if (!_parseAndCheckOpen(hoursStr, hour, minute)) {
        return false; // En az bir günde kapalıysa false
      }
    }
    return true;
  }

  bool _parseAndCheckOpen(String hoursStr, int hour, int minute) {
    // Format: "09:00-17:00" veya "09:00-12:00, 14:00-18:00" (çift vardiya)
    // Veya: "closed", "kapalı", "24 hours", "always open"

    final lower = hoursStr.toLowerCase().trim();

    // Kapalı durumları
    if (lower == 'closed' || lower == 'kapalı' || lower == 'kapali') return false;

    // 24 saat açık
    if (lower.contains('24') || lower.contains('always')) return true;

    // Birden fazla vardiya (örn: "09:00-12:00, 14:00-18:00")
    final shifts = hoursStr.split(',');
    final currentMinutes = hour * 60 + minute;

    for (final shift in shifts) {
      final openMin = _parseOpeningMinutes(shift.trim());
      final closeMin = _parseClosingMinutes(shift.trim());

      if (openMin < 0 || closeMin < 0) continue;

      // Gece yarısı geçişi var mı? (örn: 22:00-02:00)
      if (closeMin < openMin) {
        // Gece yarısına kadar veya gece yarısından sonra
        if (currentMinutes >= openMin || currentMinutes <= closeMin) return true;
      } else {
        // Normal durum
        if (currentMinutes >= openMin && currentMinutes <= closeMin) return true;
      }
    }

    return false;
  }

  int _parseOpeningMinutes(String hoursStr) {
    // "09:00-17:00" -> 540 (dakika)
    final match = RegExp(r'(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})').firstMatch(hoursStr);
    if (match == null) return -1;

    final openHour = int.tryParse(match.group(1)!) ?? -1;
    final openMin = int.tryParse(match.group(2)!) ?? 0;

    if (openHour < 0 || openHour > 23) return -1;

    return openHour * 60 + openMin;
  }

  int _parseClosingMinutes(String hoursStr) {
    // "09:00-17:00" -> 1020 (dakika)
    final match = RegExp(r'(\d{1,2}):(\d{2})\s*-\s*(\d{1,2}):(\d{2})').firstMatch(hoursStr);
    if (match == null) return -1;

    final closeHour = int.tryParse(match.group(3)!) ?? -1;
    final closeMin = int.tryParse(match.group(4)!) ?? 0;

    if (closeHour < 0 || closeHour > 23) return -1;

    return closeHour * 60 + closeMin;
  }

  /// Dil seçimine göre isim döndürür. nameEn yoksa name kullanır.
  /// Ayrıca aktif dile uymayan "Museum" / "Müzesi" / "Müze" geçişlerini
  /// otomatik olarak düzeltir (örn. TR seçili → "Pergamon Museum" → "Pergamon Müzesi").
  String getLocalizedName(bool isEnglish) {
    final base = (isEnglish && nameEn != null && nameEn!.isNotEmpty)
        ? nameEn!
        : name;
    return _localizeMuseumWord(base, isEnglish);
  }

  /// "Museum" ↔ "Müzesi"/"Müze" arası geçiş.
  static final RegExp _reMuseumU = RegExp(r'\bMuseum\b');
  static final RegExp _reMuseumL = RegExp(r'\bmuseum\b');
  static final RegExp _reMuzesiU = RegExp(r'\bMüzesi\b');
  static final RegExp _reMuzesiL = RegExp(r'\bmüzesi\b');
  static final RegExp _reMuzeU = RegExp(r'\bMüze\b');
  static final RegExp _reMuzeL = RegExp(r'\bmüze\b');

  static String _localizeMuseumWord(String input, bool isEnglish) {
    if (input.isEmpty) return input;
    if (isEnglish) {
      // TR formları → Museum (önce uzunu eşle: "Müzesi" → "Museum")
      var s = input.replaceAll(_reMuzesiU, 'Museum');
      s = s.replaceAll(_reMuzesiL, 'museum');
      s = s.replaceAll(_reMuzeU, 'Museum');
      s = s.replaceAll(_reMuzeL, 'museum');
      return s;
    }
    var s = input.replaceAll(_reMuseumU, 'Müzesi');
    s = s.replaceAll(_reMuseumL, 'müzesi');
    return s;
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

  /// Dil seçimine göre en iyi zamanı döndürür.
  String getLocalizedBestTime(bool isEnglish) {
    if (isEnglish) {
      if (bestTimeEn != null && bestTimeEn!.isNotEmpty) return bestTimeEn!;
      if (bestTime != null && bestTime!.isNotEmpty) {
        return AppLocalizations.instance.translateFeature(bestTime!);
      }
      return AppLocalizations.instance.anytime;
    }
    return bestTime ?? AppLocalizations.instance.anytime;
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

    // Güvenli Koordinat Dönüşümü: JSON'da bazen ondalık noktası unutulabiliyor (Örn: 52521.0 -> 52.521 olmalı)
    double safeParseCoordinate(dynamic value, bool isLat) {
      if (value == null) return 0.0;
      double parsed = (value as num).toDouble();
      if (parsed == 0.0) return 0.0;
      
      final limit = isLat ? 90.0 : 180.0;
      while (parsed.abs() > limit) {
        parsed /= 10.0;
      }
      return parsed; // Daha tutarlı olması için yuvarlanabilir ama Google Maps hassasiyeti için direkt dönüyoruz
    }

    double lat = safeParseCoordinate(json["lat"] ?? json["latitude"], true);
    double lng = safeParseCoordinate(json["lng"] ?? json["longitude"], false);

    return Highlight(
      id: json["id"]?.toString(),
      name: json["name"] ?? "",
      area: json["area"] ?? "",
      category: json["category"] ?? "",
      city: city,
      tags: (json["tags"] as List?)?.map((e) => e.toString()).toList() ?? [],
      distanceFromCenter:
          (json["distanceFromCenter"] as num?)?.toDouble() ?? 0.0,
      lat: lat,
      lng: lng,
      price: json["price"] ?? "medium",
      description: json["description"] ?? "",
      imageUrl: (json["imageUrl"]?.toString().isNotEmpty == true) ? json["imageUrl"] :
                (json["image"]?.toString().isNotEmpty == true) ? json["image"] :
                (json["photo"]?.toString().isNotEmpty == true) ? json["photo"] :
                (json["image_url"]?.toString().isNotEmpty == true) ? json["image_url"] :
                (json["image_path"]?.toString().isNotEmpty == true) ? json["image_path"] : null,
      blurHash: json["blurHash"] ?? json["blurhash"],
      tips: json["tips"],
      nameEn: json["name_en"] ?? json["nameEn"],
      areaEn: json["area_en"] ?? json["areaEn"],
      descriptionEn: json["description_en"] ?? json["descriptionEn"],
      tipsEn: json["tips_en"] ?? json["tipsEn"],
      bestTime: json["bestTime"],
      bestTimeEn: json["bestTime_en"],
      duration: json["duration"],
      rating: (json["rating"] as num?)?.toDouble() ?? 4.5,
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

class CityGuide {
  final String intro;
  final String introEn;
  final String recommendations;
  final String recommendationsEn;
  final String tips;
  final String tipsEn;
  final String hiddenGems;
  final String hiddenGemsEn;
  final String transport;
  final String transportEn;

  CityGuide({
    this.intro = "",
    this.introEn = "",
    this.recommendations = "",
    this.recommendationsEn = "",
    this.tips = "",
    this.tipsEn = "",
    this.hiddenGems = "",
    this.hiddenGemsEn = "",
    this.transport = "",
    this.transportEn = "",
  });

  factory CityGuide.fromJson(Map<String, dynamic> json) {
    return CityGuide(
      intro: json["intro"] ?? "",
      introEn: json["intro_en"] ?? "",
      recommendations: json["recommendations"] ?? "",
      recommendationsEn: json["recommendations_en"] ?? "",
      tips: json["tips"] ?? "",
      tipsEn: json["tips_en"] ?? "",
      hiddenGems: json["hidden_gems"] ?? "",
      hiddenGemsEn: json["hidden_gems_en"] ?? "",
      transport: json["transport_guide"] ?? "",
      transportEn: json["transport_guide_en"] ?? "",
    );
  }
}

class CuratedRouteData {
  final String id;
  final String title;
  final String titleEn;
  final String description;
  final String descriptionEn;
  final List<String> places;

  CuratedRouteData({
    required this.id,
    required this.title,
    required this.titleEn,
    required this.description,
    required this.descriptionEn,
    required this.places,
  });

  factory CuratedRouteData.fromJson(Map<String, dynamic> json) {
    return CuratedRouteData(
      id: json["id"] ?? "",
      title: json["title"] ?? "",
      titleEn: json["title_en"] ?? "",
      description: json["description"] ?? "",
      descriptionEn: json["description_en"] ?? "",
      places: (json["places"] as List?)?.map((e) => e.toString()).toList() ?? [],
    );
  }

  /// Dil seçimine göre başlığı döndürür.
  String getLocalizedTitle(bool isEnglish) {
    if (isEnglish && titleEn.isNotEmpty) return titleEn;
    return title;
  }

  /// Dil seçimine göre açıklamayı döndürür.
  String getLocalizedDescription(bool isEnglish) {
    if (isEnglish && descriptionEn.isNotEmpty) return descriptionEn;
    return description;
  }
}

/// Mekanların ideal zaman pencereleri.
/// Schedule oluşturma sırasında sabah/akşam uyumunu sağlamak için kullanılır.
enum TimeWindow {
  /// 07:00-12:00 - Kahvaltı, müzeler, sabah aktiviteleri
  MORNING,

  /// 11:00-17:00 - Öğle yemeği, alışveriş, turistik yerler
  AFTERNOON,

  /// 17:00-21:00 - Akşam yemeği, gezinti, erken aktiviteler
  EVENING,

  /// 20:00-03:00 - Bar, karaoke, gece kulübü, gece pazarı
  NIGHT,
}
