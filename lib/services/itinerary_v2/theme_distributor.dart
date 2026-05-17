// =============================================================================
// ITINERARY V2 - THEME DISTRIBUTOR
// N güne tema dağıtır - ÇEŞİTLİLİK öncelikli, şehir gücü ikincil.
// "4 gün üst üste club önerme" tipi monotonluğu engeller.
// =============================================================================

import 'city_analyzer.dart';
import 'day_theme.dart';
import 'theme_catalog.dart';

/// Kullanıcı tercihleri - tema seçiminde kullanılır.
class TripPreferences {
  /// Kullanıcının ilgi alanları (lowercase). Onboarding'den gelir.
  /// Örn: ["sanat", "yemek", "tarih", "doğa", "gece hayatı"]
  final List<String> interests;

  /// Travel style: "balanced" | "tourist" | "local" | "adventure"
  final String travelStyle;

  /// Bütçe seviyesi: "economic" | "medium" | "premium"
  final String budgetLevel;

  /// Kullanıcı day-trip istiyor mu? (ayar veya gün sayısına göre belirlenir)
  final bool allowDayTrips;

  const TripPreferences({
    this.interests = const [],
    this.travelStyle = "balanced",
    this.budgetLevel = "medium",
    this.allowDayTrips = true,
  });
}

/// N güne tema dağıtımı sonucu.
class ThemePlan {
  /// Gün indeksi (1-bazlı) → tema id.
  final Map<int, DayThemeId> dayThemes;

  /// Gün indeksi → tema'nın okunabilir adı (debug için).
  final Map<int, String> dayThemeNames;

  /// Day-trip günlerinin gün indeksleri (genelde son günler).
  final Set<int> dayTripDays;

  const ThemePlan({
    required this.dayThemes,
    required this.dayThemeNames,
    required this.dayTripDays,
  });
}

class ThemeDistributor {
  /// N güne tema dağıt.
  ///
  /// Algoritma:
  ///   1. Day-trip imkanı varsa, gün sayısına göre N day-trip ayır:
  ///      - 1-2 gün: 0 day-trip
  ///      - 3-4 gün: 1 day-trip
  ///      - 5-7 gün: 2 day-trip
  ///      - 8+ gün: 3 day-trip
  ///   2. Kalan günler için tema havuzu oluştur:
  ///      - Şehirde feasible olan temalar
  ///      - User interests'e uyan temaları öne al (skor bonus)
  ///   3. Her gün için: en yüksek skorlu + henüz az kullanılmış temayı seç
  ///   4. Tema sırası: çeşitlilik için karıştır (aynı tema 2 gün üst üste asla)
  static ThemePlan distribute({
    required int totalDays,
    required CityProfile cityProfile,
    required TripPreferences prefs,
  }) {
    if (totalDays < 1) {
      return const ThemePlan(
        dayThemes: {},
        dayThemeNames: {},
        dayTripDays: {},
      );
    }

    // 1. Day-trip kontenjanı belirle
    int maxDayTrips = 0;
    if (prefs.allowDayTrips && cityProfile.dayTripCandidates > 0) {
      if (totalDays >= 3) maxDayTrips = 1;
      if (totalDays >= 5) maxDayTrips = 2;
      if (totalDays >= 8) maxDayTrips = 3;
      // Eğer day-trip aday yoksa zorla 0
      if (cityProfile.dayTripCandidates == 0) maxDayTrips = 0;
    }
    final regularDays = totalDays - maxDayTrips;

    // 2. Day-trip günlerini belirle (genelde sonlarda)
    final dayTripDays = <int>{};
    for (int i = 0; i < maxDayTrips; i++) {
      dayTripDays.add(totalDays - i); // Son günler
    }

    // 3. Regular günler için tema havuzu
    // Skor: cityStrength + interestBonus
    final candidateThemes = <DayThemeId, double>{};
    for (final id in ThemeCatalog.allIds) {
      if (id == DayThemeId.dayTrip) continue;
      if (!(cityProfile.themeFeasible[id] ?? false)) continue;

      final cityScore = cityProfile.themeStrengths[id] ?? 0;
      final interestBonus = _interestBonus(id, prefs.interests);
      final styleBonus = _styleBonus(id, prefs.travelStyle);

      final total = cityScore + interestBonus + styleBonus;
      if (total > 0) candidateThemes[id] = total;
    }

    // Hiç tema feasible değilse -> "balanced" fallback (history)
    if (candidateThemes.isEmpty) {
      candidateThemes[DayThemeId.history] = 1.0;
    }

    // 4. Regular günleri tema'lara ata
    // Her tema için max kaç kez kullanılacağı (çeşitlilik için):
    // - 1-3 gün: her tema max 1 kez
    // - 4-6 gün: her tema max 2 kez
    // - 7+ gün: her tema max 3 kez
    int maxPerTheme;
    if (regularDays <= 3) {
      maxPerTheme = 1;
    } else if (regularDays <= 6) {
      maxPerTheme = 2;
    } else {
      maxPerTheme = 3;
    }

    final themeUsage = <DayThemeId, int>{};
    final assigned = <int, DayThemeId>{};

    DayThemeId? lastTheme;
    for (int day = 1; day <= regularDays; day++) {
      // Adayları skorla: temaSkoru × frekansCezası × ardışıklıkCezası
      DayThemeId? best;
      double bestScore = -double.infinity;

      for (final entry in candidateThemes.entries) {
        final id = entry.key;
        final used = themeUsage[id] ?? 0;
        if (used >= maxPerTheme) continue;

        // Aynı tema 2 gün üst üste yasak
        if (lastTheme == id) continue;

        // Frekans cezası: ne kadar çok kullanıldıysa o kadar düşük
        double freqMultiplier = 1.0;
        if (used == 1) freqMultiplier = 0.55;
        if (used == 2) freqMultiplier = 0.3;

        final score = entry.value * freqMultiplier;
        if (score > bestScore) {
          bestScore = score;
          best = id;
        }
      }

      // Eğer kimse uygun değilse (örn 4 gün 4 farklı tema istemek) yine de bir şey ata
      if (best == null) {
        // En yüksek skorlu (ardışıklık ihlali olsa bile)
        DayThemeId? fallback;
        double fallbackScore = -double.infinity;
        for (final entry in candidateThemes.entries) {
          if (entry.value > fallbackScore) {
            fallback = entry.key;
            fallbackScore = entry.value;
          }
        }
        best = fallback ?? DayThemeId.history;
      }

      assigned[day] = best;
      themeUsage[best] = (themeUsage[best] ?? 0) + 1;
      lastTheme = best;
    }

    // 5. Day-trip günlerini ekle
    for (final d in dayTripDays) {
      assigned[d] = DayThemeId.dayTrip;
    }

    // 6. İsim haritası
    final names = <int, String>{};
    assigned.forEach((d, id) => names[d] = id.nameTr);

    return ThemePlan(
      dayThemes: assigned,
      dayThemeNames: names,
      dayTripDays: dayTripDays,
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // BONUSLAR
  // ─────────────────────────────────────────────────────────────────

  /// Tema, kullanıcının ilgi alanlarına ne kadar uyuyor?
  static double _interestBonus(DayThemeId id, List<String> interests) {
    if (interests.isEmpty) return 0;

    final keywords = _interestKeywordsFor(id);
    int hits = 0;
    for (final interest in interests) {
      final lower = interest.toLowerCase();
      for (final kw in keywords) {
        if (lower.contains(kw) || kw.contains(lower)) {
          hits++;
          break;
        }
      }
    }
    return hits * 12.0;
  }

  static List<String> _interestKeywordsFor(DayThemeId id) {
    switch (id) {
      case DayThemeId.history:
        return const ["tarih", "history", "müze", "museum", "mimari", "antik"];
      case DayThemeId.localFood:
        return const [
          "yemek",
          "food",
          "lezzet",
          "şarap",
          "wine",
          "gourmet",
          "gastronomi"
        ];
      case DayThemeId.artStreet:
        return const ["sanat", "art", "tasarım", "sokak", "boutique", "galeri"];
      case DayThemeId.nature:
        return const [
          "doğa",
          "nature",
          "park",
          "sahil",
          "plaj",
          "manzara",
          "yürüyüş"
        ];
      case DayThemeId.nightlife:
        return const [
          "gece",
          "night",
          "bar",
          "club",
          "müzik",
          "music",
          "eğlence"
        ];
      case DayThemeId.dayTrip:
        return const ["gezi", "trip", "ada", "şehir dışı"];
      case DayThemeId.localRitual:
        return const ["yerel", "local", "mahalle", "yaşam", "kültür"];
    }
  }

  /// Travel style'a göre tema bonusu.
  static double _styleBonus(DayThemeId id, String style) {
    switch (style) {
      case "tourist":
        if (id == DayThemeId.history) return 15;
        if (id == DayThemeId.artStreet) return 8;
        if (id == DayThemeId.localRitual) return -5;
        return 0;
      case "local":
        if (id == DayThemeId.localRitual) return 18;
        if (id == DayThemeId.localFood) return 12;
        if (id == DayThemeId.history) return -5;
        return 0;
      case "adventure":
        if (id == DayThemeId.nature) return 18;
        if (id == DayThemeId.dayTrip) return 12;
        if (id == DayThemeId.history) return -3;
        return 0;
      case "balanced":
      default:
        return 0;
    }
  }
}
