// =============================================================================
// ITINERARY V2 - CITY ANALYZER
// Şehrin highlight listesini analiz edip her tema için "uygunluk skoru" üretir.
// Theme distributor bu skorlara göre en uygun temaları seçer.
// =============================================================================

import '../../models/city_model.dart';
import 'day_theme.dart';
import 'theme_catalog.dart';
import 'variety_tracker.dart';

/// Bir şehrin "güç profili" - hangi temalarda ne kadar zengin.
class CityProfile {
  /// Tema → uygunluk skoru (0..100).
  final Map<DayThemeId, double> themeStrengths;

  /// Tema → tema'nın "min requirements"larını karşılayıp karşılamadığı.
  final Map<DayThemeId, bool> themeFeasible;

  /// Şehirde toplam day-trip aday sayısı.
  final int dayTripCandidates;

  /// Kategori grubu → mekan sayısı.
  final Map<String, int> groupCounts;

  /// Toplam (non-day-trip) mekan sayısı.
  final int totalCityPlaces;

  const CityProfile({
    required this.themeStrengths,
    required this.themeFeasible,
    required this.dayTripCandidates,
    required this.groupCounts,
    required this.totalCityPlaces,
  });

  /// En güçlü temalar (skoruna göre azalan).
  List<DayThemeId> get rankedThemes {
    final list = themeStrengths.keys.toList();
    list.sort(
        (a, b) => (themeStrengths[b] ?? 0).compareTo(themeStrengths[a] ?? 0));
    return list;
  }
}

/// Şehrin güç profilini hesaplar.
class CityAnalyzer {
  /// Bir şehir için CityProfile üretir.
  ///
  /// Skor hesabı:
  ///   - Tema'nın "preferKeywords"larıyla eşleşen mekan sayısı (her eşleşme +6)
  ///   - Tema'nın "preferGroups"u ile eşleşen mekan sayısı (her eşleşme +3)
  ///   - Yüksek rating'li mekanlar bonus (+2 her 4.5+)
  ///   - Min requirements karşılanıyorsa +20 baz puan
  static CityProfile analyze(List<Highlight> highlights) {
    final groupCounts = <String, int>{};
    int dayTripCount = 0;
    int normalCount = 0;

    for (final h in highlights) {
      if (h.isDayTrip) {
        dayTripCount++;
        continue;
      }
      normalCount++;
      final g = TripVarietyTracker.groupOf(h);
      groupCounts[g] = (groupCounts[g] ?? 0) + 1;
    }

    // Her tema için skor hesapla
    final strengths = <DayThemeId, double>{};
    final feasible = <DayThemeId, bool>{};

    for (final id in ThemeCatalog.allIds) {
      // Day trip teması özel - sadece day-trip aday var mı bak
      if (id == DayThemeId.dayTrip) {
        if (dayTripCount > 0) {
          strengths[id] = 30.0 + (dayTripCount * 8.0).clamp(0.0, 70.0);
          feasible[id] = true;
        } else {
          strengths[id] = 0.0;
          feasible[id] = false;
        }
        continue;
      }

      final theme = ThemeCatalog.themeFor(id);
      double score = 0.0;

      // Min requirements feasibility
      bool feasibleNow = true;
      for (final entry in theme.minPlaceRequirements.entries) {
        final available = groupCounts[entry.key] ?? 0;
        if (available < entry.value) {
          feasibleNow = false;
          break;
        }
      }
      feasible[id] = feasibleNow;

      // Eğer feasible değilse skor 0
      if (!feasibleNow) {
        strengths[id] = 0.0;
        continue;
      }

      // Baz puan
      score += 20.0;

      // PreferGroups eşleşmesi
      for (final beat in theme.beats) {
        for (final group in beat.categoryPolicy.preferGroups) {
          final count = groupCounts[group] ?? 0;
          score += (count * 1.5).clamp(0.0, 15.0);
        }
        // MustGroups eşleşmesi (daha düşük katsayı, çoğu beat zaten preferGroups'a sahip)
        for (final group in beat.categoryPolicy.mustGroups) {
          final count = groupCounts[group] ?? 0;
          score += (count * 1.0).clamp(0.0, 10.0);
        }
      }

      // PreferKeywords eşleşmesi (mekan name+category+tags üzerinde)
      final allKeywords = <String>{};
      for (final beat in theme.beats) {
        allKeywords.addAll(beat.categoryPolicy.preferKeywords);
      }

      int keywordHits = 0;
      for (final h in highlights) {
        if (h.isDayTrip) continue;
        final blob = "${h.name} ${h.category} ${h.tags.join(' ')}".toLowerCase();
        for (final kw in allKeywords) {
          if (blob.contains(kw.toLowerCase())) {
            keywordHits++;
            break; // Her mekan max 1 kez sayılsın
          }
        }
      }
      score += (keywordHits * 4.0).clamp(0.0, 40.0);

      // Yüksek rating bonus (4.5+ olan mekanlar)
      int highRated = 0;
      for (final h in highlights) {
        if (h.isDayTrip) continue;
        if ((h.rating ?? 0) >= 4.5 && (h.reviewCount ?? 0) >= 100) {
          highRated++;
        }
      }
      score += (highRated * 0.3).clamp(0.0, 10.0);

      strengths[id] = score.clamp(0.0, 100.0);
    }

    return CityProfile(
      themeStrengths: strengths,
      themeFeasible: feasible,
      dayTripCandidates: dayTripCount,
      groupCounts: groupCounts,
      totalCityPlaces: normalCount,
    );
  }
}
