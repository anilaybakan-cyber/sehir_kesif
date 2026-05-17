// =============================================================================
// ITINERARY V2 - BEAT FILLER
// Bir beat için en uygun mekanı seçer.
//   - Hard constraints (FeasibilityChecker) ile filtre
//   - Soft scoring ile en iyiyi seç
//   - TimePlanner ile gerçek başlangıç saatini hesapla
//   - TravelTimeEstimator ile transit süresini ölç
// =============================================================================

import 'dart:math' as math;

import '../../models/city_model.dart';
import '../travel_time_estimator.dart';
import 'beat.dart';
import 'feasibility.dart';
import 'theme_distributor.dart';
import 'time_planner.dart';
import 'variety_tracker.dart';

/// Bir beat için aday değerlendirme sonucu.
class _Candidate {
  final Highlight place;
  final double score;
  final TimePlannerResult timing;
  final int transitMin;
  final double transitDistKm;

  const _Candidate({
    required this.place,
    required this.score,
    required this.timing,
    required this.transitMin,
    required this.transitDistKm,
  });
}

class BeatFiller {
  /// Bir beat için en iyi mekanı seç ve FilledBeat olarak döndür.
  ///
  /// `candidatePool` o gün için aday mekan havuzu.
  /// `previouslyFilled` o günde önceden seçilenler (diversity için).
  /// `tripTracker` tüm trip'i kapsayan variety tracker.
  /// `prevPlace` önceki mekan (transit hesabı için, null=ilk beat).
  /// `prevEnd` önceki mekanın bitiş saati (yoksa beat'in earliest'i).
  /// `dayKey` "monday".."sunday" - openHours kontrolü için.
  /// `dayAnchor` günün merkez mekanı (varsa) - aşırı uzaklaşmayı önler.
  /// `mustSeeIcons` "ikonik" sayılan mekanlar (icon role beat'lerinde bonus).
  static FilledBeat? fillBeat({
    required ActivityBeat beat,
    required List<Highlight> candidatePool,
    required List<FilledBeat> previouslyFilled,
    required TripVarietyTracker tripTracker,
    required Highlight? prevPlace,
    required TimeOfDayLite earliestStart,
    required String dayKey,
    required Highlight? dayAnchor,
    required Set<String> mustSeeIcons,
    required TripPreferences prefs,
    required math.Random rng,
    TravelMode travelMode = TravelMode.walking,
    bool forceInclude = false,
  }) {
    final candidates = <_Candidate>[];

    for (final h in candidatePool) {
      // 1. Hard constraint kontrolü
      final feas = FeasibilityChecker.check(
        place: h,
        beat: beat,
        previouslyFilled: previouslyFilled,
        tripTracker: tripTracker,
        forceInclude: forceInclude,
      );
      if (feas != BeatFeasibility.ok) continue;

      // 2. Transit hesabı (önceki mekan varsa)
      int transitMin = 0;
      double transitDist = 0;
      TimeOfDayLite candidateEarliest = earliestStart;
      if (prevPlace != null) {
        transitDist = TravelTimeEstimator.haversine(
          prevPlace.lat,
          prevPlace.lng,
          h.lat,
          h.lng,
        );
        transitMin = TravelTimeEstimator.estimateMinutesForDistance(
          distKm: transitDist,
          mode: travelMode,
        );
        candidateEarliest = earliestStart.addMinutes(transitMin);
      }

      // 3. Time feasibility
      final timing = TimePlanner.planBeat(
        beat: beat,
        place: h,
        earliestStart: candidateEarliest,
        dayOfWeekKey: dayKey,
      );
      if (!timing.isOk) continue;

      // 4. Skor hesabı
      final score = _calculateScore(
        place: h,
        beat: beat,
        prevPlace: prevPlace,
        dayAnchor: dayAnchor,
        transitMin: transitMin,
        mustSeeIcons: mustSeeIcons,
        tripTracker: tripTracker,
        prefs: prefs,
        rng: rng,
      );

      candidates.add(_Candidate(
        place: h,
        score: score,
        timing: timing,
        transitMin: transitMin,
        transitDistKm: transitDist,
      ));
    }

    if (candidates.isEmpty) return null;

    // En yüksek skoru seç
    candidates.sort((a, b) => b.score.compareTo(a.score));
    final best = candidates.first;

    return FilledBeat(
      beat: beat,
      place: best.place,
      actualStart: best.timing.actualStart!,
      durationMin: best.timing.durationMin,
      transitMinFromPrev: best.transitMin,
      transitDistKm: best.transitDistKm,
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // SOFT SCORING
  // ─────────────────────────────────────────────────────────────────

  static double _calculateScore({
    required Highlight place,
    required ActivityBeat beat,
    required Highlight? prevPlace,
    required Highlight? dayAnchor,
    required int transitMin,
    required Set<String> mustSeeIcons,
    required TripVarietyTracker tripTracker,
    required TripPreferences prefs,
    required math.Random rng,
  }) {
    double score = 1000.0;

    // 1. Prestij (Rating + Review Count) - KURAL: Popülerlik öncelikli
    // Review count etkisi logaritmik ama ağırlığı artırıldı
    final reviewLog = math.log((place.reviewCount ?? 1) + 1);
    final prestige = (place.rating ?? 4.0) * 15 + reviewLog * 10.0;
    score += prestige * 3.0;

    // Ekstra popülerlik bonusu (Örn: Sagrada Familia gibi dev mekanlar için)
    if ((place.reviewCount ?? 0) > 5000) {
      score += 500.0;
    }

    // 2. Kategori uyumu
    if (beat.categoryPolicy.mustGroups.isNotEmpty) {
      // mustGroups zaten Feasibility'de elendi, burası garanti
    }
    final placeGroup = TripVarietyTracker.groupOf(place);
    if (beat.categoryPolicy.preferGroups.contains(placeGroup)) {
      score += 300.0;
    }

    // 5. Must-see icon bonusu (Çapa etkisi - ÇOK GÜÇLÜ)
    if (mustSeeIcons.contains(place.name)) {
      score += 800.0;
    }

    // KURAL: Sagrada Familia Kutsal Kasedir.
    if (place.name.toLowerCase().contains("sagrada familia")) {
      score += 5000.0;
    }

    // 4. PreferKeywords bonus (mekan adı/kategori/tags eşleşmesi)
    final blob =
        "${place.name} ${place.category} ${place.tags.join(' ')}".toLowerCase();
    int keywordHits = 0;
    for (final kw in beat.categoryPolicy.preferKeywords) {
      if (blob.contains(kw.toLowerCase())) keywordHits++;
    }
    score += keywordHits * 120.0;

    // 5. TimeWindow uyumu (mekanın idealTimeWindow'u beat saatine uyuyor mu)
    if (place.isTimeSuitable(beat.time.anchor.formatted)) {
      score += 200.0;
    } else {
      score -= 350.0;
    }

    // 6. KURAL 6 + 8: Coğrafi yakınlık - önceki mekana ve günün anchor'ına
    // Hard cap: 5km'den uzak ardışık mekanlar → çok büyük ceza (fiilen elenir)
    if (transitMin > 45) score -= 9999.0; // ~5km yürüme = pratik olarak elenmiş

    // Transit süresi cezası (güçlendirildi)
    if (transitMin > 20) score -= (transitMin - 20) * 15.0;

    if (dayAnchor != null && place.name != dayAnchor.name) {
      final distAnchor = TravelTimeEstimator.haversine(
        place.lat,
        place.lng,
        dayAnchor.lat,
        dayAnchor.lng,
      );
      // 0-1.5 km +250, 1.5-3 km nötr, 3+ km ceza
      if (distAnchor < 1.5) {
        score += (1.5 - distAnchor) * 170.0;
      } else if (distAnchor > 3.0) {
        score -= (distAnchor - 3.0) * 120.0;
      }
    }

    // 7. Interests bonus
    score += _interestBonus(place, prefs.interests);

    // 8. Bütçe uyumu
    score += _budgetBonus(place, prefs.budgetLevel);

    // 9. Trip-genelinde aşırı tekrar eden kategori cezası
    final domRatio = tripTracker.categoryDominance(placeGroup);
    if (domRatio > 0.4) {
      score -= (domRatio - 0.4) * 600.0; // Çok baskınsa ceza
    }

    // 10. Trip-genelinde area tekrarı (3+ kez aynı bölgeye düşmesin)
    if (place.area.isNotEmpty) {
      final areaUse = tripTracker.areaUsage(place.area);
      if (areaUse >= 3) score -= 250.0;
    }

    // 11. Açılış saati kalitesi (beat anchor'a yakın mı)
    final openMin = place.getOpeningMinutes("monday"); // ortalama
    if (openMin >= 0) {
      final beatMin = beat.time.anchor.totalMinutes;
      // Tam o saatte açıkken bonus
      if (openMin <= beatMin && beatMin <= openMin + 240) {
        score += 60.0;
      }
    }

    // 12. Hafif rastgelelik (deterministik+çeşitlilik)
    score += rng.nextDouble() * 30.0;

    return score;
  }

  static double _interestBonus(Highlight h, List<String> interests) {
    if (interests.isEmpty) return 0;
    final blob = "${h.name} ${h.category} ${h.tags.join(' ')}".toLowerCase();
    int hits = 0;
    for (final i in interests) {
      final lower = i.toLowerCase();
      if (blob.contains(lower)) hits++;
    }
    return hits * 110.0;
  }

  static double _budgetBonus(Highlight h, String budget) {
    final price = h.price.toLowerCase();
    if (budget == "economic") {
      if (price.contains("low") ||
          price.contains("ucuz") ||
          price.contains("ekonomik") ||
          price == "free" ||
          h.priceRange == "\$" ||
          h.priceRange == "₺") {
        return 80;
      }
      if (price.contains("high") ||
          price.contains("premium") ||
          h.priceRange == "\$\$\$\$") {
        return -100;
      }
      return 0;
    }
    if (budget == "premium") {
      if (price.contains("high") ||
          price.contains("premium") ||
          h.priceRange == "\$\$\$\$") {
        return 100;
      }
      if (price.contains("low") || price.contains("ucuz")) {
        return -40;
      }
      return 0;
    }
    // medium: ne çok ucuz ne çok pahalı
    if (price.contains("medium") || price == "" || h.priceRange == "\$\$") {
      return 50;
    }
    return 0;
  }
}
