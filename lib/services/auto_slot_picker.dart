import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';
import '../models/city_model.dart';
import 'city_data_loader.dart';
import 'travel_time_estimator.dart';

/// Manuel "Rotama Ekle" akışı için en uygun günü otomatik seçer.
///
/// Kullanım:
/// ```dart
/// final result = await AutoSlotPicker.pickBestDay(
///   place: highlight,
///   cityId: 'sevilla',
/// );
/// // result.day → eklenecek gün (1..N veya yeni bir gün)
/// // result.reason → kullanıcıya gösterilecek kısa açıklama
/// ```
class AutoSlotPicker {
  /// Maksimum günlük slot sayısı (yorgunluk eşiği).
  static const int _maxSlotsPerDay = 8;

  /// Day-trip için tolerans bölge yarıçapı (km).
  static const double _dayTripAreaRadiusKm = 50.0;

  /// Verilen yer için en uygun günü bul.
  static Future<AutoSlotResult> pickBestDay({
    required Highlight place,
    required String cityId,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    final normalizedCity = cityId.toLowerCase();

    final scheduleJson = prefs.getString("trip_schedule_$normalizedCity");
    final onboardingDays =
        prefs.getInt("tripDays_$normalizedCity") ?? prefs.getInt("tripDays") ?? 3;

    Map<String, dynamic> schedule = {};
    if (scheduleJson != null) {
      try {
        schedule = jsonDecode(scheduleJson) as Map<String, dynamic>;
      } catch (_) {}
    }

    // Mevcut günlerin hepsini topla
    int maxDay = onboardingDays;
    schedule.forEach((k, _) {
      final d = int.tryParse(k) ?? 1;
      if (d > maxDay) maxDay = d;
    });

    // Şehir verisini yükle (mevcut günlerdeki yerleri Highlight'a çevirmek için)
    CityModel cityData;
    try {
      cityData = await CityDataLoader.loadCity(normalizedCity);
    } catch (_) {
      // Fallback: ilk güne koy
      return AutoSlotResult(day: 1, reason: AutoSlotReason.fallback, isNewDay: false);
    }

    // Her günü Highlight listesine çevir
    final Map<int, List<Highlight>> dayPlans = {};
    for (int d = 1; d <= maxDay; d++) {
      final entries = schedule[d.toString()];
      final List<Highlight> dayPlaces = [];
      if (entries is List) {
        for (var item in entries) {
          String? placeName;
          if (item is Map<String, dynamic>) {
            placeName = item['name']?.toString();
          } else if (item is String) {
            placeName = item;
          }
          if (placeName == null || placeName.isEmpty) continue;

          final match =
              cityData.highlights.where((h) => h.name == placeName).firstOrNull;
          if (match != null) dayPlaces.add(match);
        }
      }
      dayPlans[d] = dayPlaces;
    }

    // ───────────────────────────────────────────────────────────
    // CASE A: Day-trip yer eklendi
    // ───────────────────────────────────────────────────────────
    if (place.isDayTrip) {
      // 1. Boş gün ara
      for (int d = 1; d <= maxDay; d++) {
        if ((dayPlans[d] ?? []).isEmpty) {
          return AutoSlotResult(
            day: d,
            reason: AutoSlotReason.dayTripEmptyDay,
            isNewDay: false,
          );
        }
      }

      // 2. Aynı bölgeye yakın bir gün varsa onu seç (kümeleme)
      for (int d = 1; d <= maxDay; d++) {
        final places = dayPlans[d] ?? [];
        if (places.any((p) =>
            p.isDayTrip &&
            TravelTimeEstimator.haversine(
                    p.lat, p.lng, place.lat, place.lng) <
                _dayTripAreaRadiusKm)) {
          // Aynı bölgede başka bir day-trip var, ona ekle
          return AutoSlotResult(
            day: d,
            reason: AutoSlotReason.dayTripSameRegion,
            isNewDay: false,
          );
        }
      }

      // 3. Yeni gün oluştur (totalDays + 1)
      return AutoSlotResult(
        day: maxDay + 1,
        reason: AutoSlotReason.dayTripNewDay,
        isNewDay: true,
      );
    }

    // ───────────────────────────────────────────────────────────
    // CASE B: Normal şehir-içi yer
    // ───────────────────────────────────────────────────────────
    int bestDay = 1;
    double bestScore = double.negativeInfinity;

    for (int d = 1; d <= maxDay; d++) {
      final places = dayPlans[d] ?? [];

      // Day-trip günlerine normal yer eklenmez (akşam yemeği hariç)
      // Akşam yemeği = FOOD kategori, gün zaten 1 day-trip + 0/1 yer içerir
      final hasDayTrip = places.any((p) => p.isDayTrip);
      if (hasDayTrip) {
        // Sadece FOOD kategori ve günde <= 1 yer varsa kabul et
        final placeCat = _categoryGroup(place);
        if (placeCat != 'FOOD' || places.length >= 2) continue;
      }

      // Dolu gün ise -∞ skor (atla)
      if (places.length >= _maxSlotsPerDay) continue;

      double score = _scoreDayForPlace(place, places, d);
      if (score > bestScore) {
        bestScore = score;
        bestDay = d;
      }
    }

    if (bestScore == double.negativeInfinity) {
      // Hiçbir gün uygun değil → yeni gün oluştur
      return AutoSlotResult(
        day: maxDay + 1,
        reason: AutoSlotReason.allDaysFull,
        isNewDay: true,
      );
    }

    return AutoSlotResult(
      day: bestDay,
      reason: AutoSlotReason.bestFit,
      isNewDay: false,
    );
  }

  /// Bir yerin günün içine ne kadar iyi uyduğunu skorlar.
  /// Yüksek skor = daha iyi gün.
  static double _scoreDayForPlace(
      Highlight place, List<Highlight> currentPlaces, int dayIndex) {
    double score = 0;

    // 1. Yük (boş gün +50, dolu gün -10/her yer)
    final load = currentPlaces.length;
    score += (8 - load) * 8.0;

    // 2. Coğrafi affinite — günün ortalama merkezine yakınlık
    if (currentPlaces.isNotEmpty) {
      double avgLat = 0, avgLng = 0;
      for (var p in currentPlaces) {
        avgLat += p.lat;
        avgLng += p.lng;
      }
      avgLat /= currentPlaces.length;
      avgLng /= currentPlaces.length;
      final distKm = TravelTimeEstimator.haversine(
          avgLat, avgLng, place.lat, place.lng);
      // 0 km = +30, 5 km = 0, 10 km = -30
      score += (5.0 - distKm) * 6.0;
    } else {
      // Boş gün → bonus
      score += 25.0;
    }

    // 3. Kategori boşluğu (FOOD eksikse FOOD'a bonus)
    final placeCat = _categoryGroup(place);
    final dayCats = currentPlaces.map(_categoryGroup).toSet();
    if (placeCat == 'FOOD' && !dayCats.contains('FOOD')) score += 15.0;
    if (placeCat == 'COFFEE' && !dayCats.contains('COFFEE')) score += 8.0;
    if (placeCat == 'CULTURE' && currentPlaces.length < 2) score += 12.0;

    // 4. Tekrar cezası (aynı kategori 3+ kez varsa eklenenede ceza)
    final sameCategoryCount =
        currentPlaces.where((p) => _categoryGroup(p) == placeCat).length;
    if (sameCategoryCount >= 3) score -= 25.0;

    // 5. İlk günlere hafif öncelik (kullanıcı erken planlasın)
    score -= dayIndex * 2.0;

    return score;
  }

  static String _categoryGroup(Highlight h) {
    final cat = h.category.toLowerCase();
    final name = h.name.toLowerCase();
    final tags = h.tags.map((t) => t.toLowerCase()).toList();

    bool looksLikeFood = name.contains("gelateria") ||
        name.contains("restaurant") ||
        name.contains("tapas") ||
        name.contains("pasta") ||
        name.contains("pizza") ||
        tags.contains("kafe") ||
        tags.contains("restoran") ||
        tags.contains("yemek");

    if (looksLikeFood) {
      if (name.contains("cafe") || name.contains("kafe") || name.contains("coffee")) return "COFFEE";
      if (name.contains("bar") || name.contains("pub")) return "SOCIAL";
      return "FOOD";
    }
    if (cat.contains("yeme") || cat.contains("food") || cat.contains("restoran")) return "FOOD";
    if (cat.contains("kafe") || cat.contains("cafe") || cat.contains("coffee")) return "COFFEE";
    if (cat.contains("bar") || cat.contains("pub") || cat.contains("gece")) return "SOCIAL";
    if (cat.contains("park") || cat.contains("bahçe") || cat.contains("garden")) return "NATURE";
    if (cat.contains("view") || cat.contains("manzara") || cat.contains("teras")) return "VIEW";
    if (cat.contains("meydan") || cat.contains("square")) return "SQUARE";
    return "CULTURE";
  }
}

class AutoSlotResult {
  final int day;
  final AutoSlotReason reason;
  final bool isNewDay;

  AutoSlotResult({
    required this.day,
    required this.reason,
    required this.isNewDay,
  });

  /// Kullanıcıya gösterilecek kısa açıklama (TR).
  String get reasonTextTr {
    switch (reason) {
      case AutoSlotReason.dayTripEmptyDay:
        return "Günübirlik gezi için boş gün ayrıldı";
      case AutoSlotReason.dayTripSameRegion:
        return "Aynı bölgedeki diğer geziye eklendi";
      case AutoSlotReason.dayTripNewDay:
        return "Yeni bir gün oluşturuldu (günübirlik)";
      case AutoSlotReason.allDaysFull:
        return "Tüm günler dolu, yeni gün oluşturuldu";
      case AutoSlotReason.bestFit:
        return "En uygun güne eklendi";
      case AutoSlotReason.fallback:
        return "İlk güne eklendi";
    }
  }

  String get reasonTextEn {
    switch (reason) {
      case AutoSlotReason.dayTripEmptyDay:
        return "Empty day reserved for day trip";
      case AutoSlotReason.dayTripSameRegion:
        return "Added to existing trip in same region";
      case AutoSlotReason.dayTripNewDay:
        return "New day created (day trip)";
      case AutoSlotReason.allDaysFull:
        return "All days full, new day created";
      case AutoSlotReason.bestFit:
        return "Added to best-fit day";
      case AutoSlotReason.fallback:
        return "Added to day 1";
    }
  }
}

enum AutoSlotReason {
  bestFit,
  dayTripEmptyDay,
  dayTripSameRegion,
  dayTripNewDay,
  allDaysFull,
  fallback,
}

extension on Iterable<Highlight> {
  Highlight? get firstOrNull => isEmpty ? null : first;
}
