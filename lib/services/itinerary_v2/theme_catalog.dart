// =============================================================================
// ITINERARY V2 - THEME CATALOG
// 7 day theme'in beat akışlarını tanımlar.
// Her tema: preferredStart + beats[] + minRequirements + targetPlaceCount
// =============================================================================

import 'beat.dart';
import 'day_theme.dart';

/// Tüm temaların kataloğu.
/// `themeFor(id)` ile bir tema'nın akışını al.
class ThemeCatalog {
  /// Bir tema kimliği için DayTheme nesnesi döndürür.
  static DayTheme themeFor(DayThemeId id) {
    switch (id) {
      case DayThemeId.history:
        return _history();
      case DayThemeId.localFood:
        return _localFood();
      case DayThemeId.artStreet:
        return _artStreet();
      case DayThemeId.nature:
        return _nature();
      case DayThemeId.nightlife:
        return _nightlife();
      case DayThemeId.dayTrip:
        return _dayTrip();
      case DayThemeId.localRitual:
        return _localRitual();
    }
  }

  /// Tüm tema kimlikleri (theme_distributor için).
  static const List<DayThemeId> allIds = [
    DayThemeId.history,
    DayThemeId.localFood,
    DayThemeId.artStreet,
    DayThemeId.nature,
    DayThemeId.nightlife,
    DayThemeId.dayTrip,
    DayThemeId.localRitual,
  ];

  // ───────────────────────────────────────────────────────────────────
  // 1. TARİH & MİMARİ
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _history() => DayTheme(
        id: DayThemeId.history,
        preferredStart: const TimeOfDayLite(hour: 9, minute: 0),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"CULTURE": 3, "FOOD": 1},
        beats: const [
          ActivityBeat(
            id: "morning_icon",
            role: BeatRole.icon,
            time: BeatTime(TimeOfDayLite(hour: 9, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE"],
              preferKeywords: ["müze", "saray", "kale", "bazilika", "katedral"],
            ),
            estimatedDurationMin: 150,
            label: "Sabah ikonik durağı",
          ),
          ActivityBeat(
            id: "transition_square",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 11, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SQUARE", "CULTURE"],
              preferKeywords: ["meydan", "tarihi yapı", "anıt"],
            ),
            estimatedDurationMin: 50,
            label: "Tarihi meydan/yapı",
          ),
          ActivityBeat(
            id: "lunch",
            role: BeatRole.lunch,
            time:
                BeatTime(TimeOfDayLite(hour: 12, minute: 45), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["yerel", "geleneksel", "trattoria", "bistro"],
            ),
            estimatedDurationMin: 90,
            label: "Yerel öğle yemeği",
          ),
          ActivityBeat(
            id: "afternoon_icon",
            role: BeatRole.icon,
            time:
                BeatTime(TimeOfDayLite(hour: 14, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE"],
              preferKeywords: ["müze", "kale", "saray", "tapınak"],
            ),
            estimatedDurationMin: 120,
            label: "Öğleden sonra ikinci ikonik durak",
          ),
          ActivityBeat(
            id: "historic_cafe",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 16, minute: 45), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE"],
              preferKeywords: ["tarihi", "klasik", "gelateria", "pastane"],
            ),
            estimatedDurationMin: 45,
            label: "Tarihi kafe molası",
            isOptional: true,
          ),
          ActivityBeat(
            id: "golden_hour_view",
            role: BeatRole.goldenHour,
            time:
                BeatTime(TimeOfDayLite(hour: 17, minute: 45), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["VIEW", "SQUARE"],
              preferKeywords: ["manzara", "panoramik", "köprü", "rıhtım"],
            ),
            estimatedDurationMin: 60,
            label: "Gün batımı manzarası",
          ),
          ActivityBeat(
            id: "classic_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 19, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["fine dining", "klasik", "geleneksel"],
            ),
            estimatedDurationMin: 100,
            label: "Klasik akşam yemeği",
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 2. YEREL LEZZET
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _localFood() => DayTheme(
        id: DayThemeId.localFood,
        preferredStart: const TimeOfDayLite(hour: 10, minute: 0),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"FOOD": 2, "COFFEE": 1},
        beats: const [
          ActivityBeat(
            id: "brunch",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 10, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE", "FOOD"],
              preferKeywords: ["brunch", "kahvaltı", "breakfast", "pastane"],
            ),
            estimatedDurationMin: 60,
            label: "Geç kahvaltı / brunch",
          ),
          ActivityBeat(
            id: "market_walk",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 11, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["MARKET", "SQUARE", "CULTURE"],
              preferKeywords: ["pazar", "çarşı", "market", "bazaar"],
            ),
            estimatedDurationMin: 60,
            label: "Yerel pazar / çarşı",
          ),
          ActivityBeat(
            id: "street_food",
            role: BeatRole.lunch,
            time:
                BeatTime(TimeOfDayLite(hour: 13, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["sokak", "street", "yerel", "trattoria", "tapas"],
            ),
            estimatedDurationMin: 75,
            label: "Sokak lezzeti",
          ),
          ActivityBeat(
            id: "sweet_break",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 15, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE"],
              preferKeywords:
                  ["gelato", "dondurma", "tatlı", "pastane", "patisserie"],
            ),
            estimatedDurationMin: 45,
            label: "Tatlı molası",
          ),
          ActivityBeat(
            id: "soft_culture",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 16, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE", "VIEW"],
              preferKeywords: ["yerel", "küçük müze", "manzara"],
            ),
            estimatedDurationMin: 60,
            label: "Hafif kültürel mola",
            isOptional: true,
          ),
          ActivityBeat(
            id: "wine_aperitivo",
            role: BeatRole.evening,
            time:
                BeatTime(TimeOfDayLite(hour: 18, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SOCIAL"],
              preferKeywords:
                  ["şarap", "wine", "aperitivo", "meyhane", "bar"],
            ),
            estimatedDurationMin: 60,
            label: "Şarap evi / aperitivo",
          ),
          ActivityBeat(
            id: "traditional_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 20, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords:
                  ["geleneksel", "yerel", "trattoria", "meyhane", "lokanta"],
            ),
            estimatedDurationMin: 100,
            label: "Geleneksel akşam yemeği",
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 3. SANAT & SOKAK
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _artStreet() => DayTheme(
        id: DayThemeId.artStreet,
        preferredStart: const TimeOfDayLite(hour: 10, minute: 0),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"CULTURE": 2, "FOOD": 1},
        beats: const [
          ActivityBeat(
            id: "art_morning",
            role: BeatRole.icon,
            time:
                BeatTime(TimeOfDayLite(hour: 10, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE"],
              preferKeywords:
                  ["sanat", "art", "galeri", "modern", "gallery", "müze"],
            ),
            estimatedDurationMin: 90,
            label: "Sanat galerisi / müze",
          ),
          ActivityBeat(
            id: "boutique_walk",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 12, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SQUARE", "CULTURE", "MARKET"],
              preferKeywords:
                  ["sokak sanatı", "street art", "butik", "shopping", "tasarım"],
            ),
            estimatedDurationMin: 60,
            label: "Butik sokak / sokak sanatı",
          ),
          ActivityBeat(
            id: "cool_lunch",
            role: BeatRole.lunch,
            time:
                BeatTime(TimeOfDayLite(hour: 13, minute: 15), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["bistro", "modern", "vegan", "fusion", "cool"],
            ),
            estimatedDurationMin: 80,
            label: "Modern bistro öğle",
          ),
          ActivityBeat(
            id: "hipster_coffee",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 15, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE"],
              preferKeywords: ["specialty", "third wave", "kahve", "atölye"],
            ),
            estimatedDurationMin: 45,
            label: "Specialty kafe",
          ),
          ActivityBeat(
            id: "second_culture",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 16, minute: 15), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE", "SQUARE"],
              preferKeywords:
                  ["sanat", "atölye", "studio", "concept", "tasarım"],
            ),
            estimatedDurationMin: 75,
            label: "İkinci sanat durağı",
            isOptional: true,
          ),
          ActivityBeat(
            id: "rooftop_view",
            role: BeatRole.goldenHour,
            time:
                BeatTime(TimeOfDayLite(hour: 18, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["VIEW", "SOCIAL"],
              preferKeywords:
                  ["rooftop", "manzara", "teras", "cocktail", "bar"],
            ),
            estimatedDurationMin: 75,
            label: "Rooftop / manzaralı bar",
          ),
          ActivityBeat(
            id: "artsy_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 20, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords:
                  ["bistro", "modern", "fusion", "creative", "boutique"],
            ),
            estimatedDurationMin: 90,
            label: "Sanat bölgesi bistro",
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 4. DOĞA & MANZARA
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _nature() => DayTheme(
        id: DayThemeId.nature,
        preferredStart: const TimeOfDayLite(hour: 9, minute: 0),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"NATURE": 1, "VIEW": 1, "FOOD": 1},
        beats: const [
          ActivityBeat(
            id: "morning_park",
            role: BeatRole.icon,
            time: BeatTime(TimeOfDayLite(hour: 9, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["NATURE"],
              preferKeywords: ["park", "bahçe", "garden", "doğa", "yürüyüş"],
            ),
            estimatedDurationMin: 90,
            label: "Sabah parkı / yürüyüş",
          ),
          ActivityBeat(
            id: "viewpoint",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 11, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["VIEW", "NATURE"],
              preferKeywords:
                  ["manzara", "panoramik", "viewpoint", "tepe", "lookout"],
            ),
            estimatedDurationMin: 50,
            label: "Manzara noktası",
          ),
          ActivityBeat(
            id: "scenic_lunch",
            role: BeatRole.lunch,
            time:
                BeatTime(TimeOfDayLite(hour: 12, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["manzaralı", "teras", "bahçe", "açık hava"],
            ),
            estimatedDurationMin: 90,
            label: "Manzaralı öğle yemeği",
          ),
          ActivityBeat(
            id: "nature_continued",
            role: BeatRole.icon,
            time:
                BeatTime(TimeOfDayLite(hour: 14, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["NATURE"],
              preferKeywords:
                  ["sahil", "plaj", "beach", "bahçe", "garden", "park"],
            ),
            estimatedDurationMin: 110,
            label: "Doğa devamı",
          ),
          ActivityBeat(
            id: "sunset_point",
            role: BeatRole.goldenHour,
            time:
                BeatTime(TimeOfDayLite(hour: 17, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["VIEW", "NATURE"],
              preferKeywords:
                  ["sunset", "gün batımı", "panoramik", "kıyı", "sahil"],
            ),
            estimatedDurationMin: 50,
            label: "Gün batımı noktası",
          ),
          ActivityBeat(
            id: "calm_break",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 18, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE"],
              preferKeywords: ["sakin", "bahçe", "garden", "açık hava"],
            ),
            estimatedDurationMin: 45,
            label: "Sakin kafe",
            isOptional: true,
          ),
          ActivityBeat(
            id: "calm_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 20, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["sakin", "bahçeli", "açık", "manzaralı"],
            ),
            estimatedDurationMin: 90,
            label: "Sakin akşam yemeği",
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 5. GECE & EĞLENCE
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _nightlife() => DayTheme(
        id: DayThemeId.nightlife,
        preferredStart: const TimeOfDayLite(hour: 11, minute: 0),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"SOCIAL": 1, "FOOD": 1},
        beats: const [
          ActivityBeat(
            id: "late_brunch",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 11, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE", "FOOD"],
              preferKeywords: ["brunch", "kahvaltı", "geç"],
            ),
            estimatedDurationMin: 60,
            label: "Geç kahvaltı",
          ),
          ActivityBeat(
            id: "city_explore",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 13, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SQUARE", "CULTURE", "MARKET"],
              preferKeywords: ["meydan", "yürüyüş", "merkez", "carşı"],
            ),
            estimatedDurationMin: 75,
            label: "Şehir keşfi",
          ),
          ActivityBeat(
            id: "light_culture",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 15, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE", "VIEW"],
              preferKeywords: ["müze", "galeri", "küçük"],
            ),
            estimatedDurationMin: 75,
            label: "Hafif kültür",
            isOptional: true,
          ),
          ActivityBeat(
            id: "aperitivo",
            role: BeatRole.evening,
            time:
                BeatTime(TimeOfDayLite(hour: 17, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SOCIAL"],
              preferKeywords: ["bar", "aperitivo", "kokteyl", "şarap"],
            ),
            estimatedDurationMin: 60,
            label: "Aperitivo / ön bar",
          ),
          ActivityBeat(
            id: "early_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 19, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["restoran", "akşam"],
            ),
            estimatedDurationMin: 80,
            label: "Akşam yemeği",
          ),
          ActivityBeat(
            id: "live_music",
            role: BeatRole.evening,
            time:
                BeatTime(TimeOfDayLite(hour: 21, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SOCIAL"],
              preferKeywords: ["canlı müzik", "live", "caz", "jazz", "konser"],
            ),
            estimatedDurationMin: 110,
            label: "Canlı müzik",
          ),
          ActivityBeat(
            id: "night_club",
            role: BeatRole.evening,
            time:
                BeatTime(TimeOfDayLite(hour: 23, minute: 0), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SOCIAL"],
              preferKeywords: ["club", "kulüp", "dance", "elektronik"],
            ),
            estimatedDurationMin: 120,
            label: "Gece kulübü",
            isOptional: true,
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 6. ŞEHİR DIŞI (DAY TRIP)
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _dayTrip() => DayTheme(
        id: DayThemeId.dayTrip,
        preferredStart: const TimeOfDayLite(hour: 8, minute: 0),
        targetPlaceCount: 4,
        minPlaceRequirements: const {},
        beats: const [
          ActivityBeat(
            id: "morning_coffee",
            role: BeatRole.softBreak,
            time: BeatTime(TimeOfDayLite(hour: 8, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE", "FOOD"],
              preferKeywords: ["kahve", "kahvaltı", "espresso"],
            ),
            estimatedDurationMin: 30,
            label: "Sabah kahvesi",
          ),
          ActivityBeat(
            id: "day_trip_main",
            role: BeatRole.dayTripMain,
            time: BeatTime(TimeOfDayLite(hour: 9, minute: 0), toleranceMin: 30),
            categoryPolicy: BeatCategoryPolicy(),
            estimatedDurationMin: 480,
            label: "Şehir dışı ana mekan",
          ),
          ActivityBeat(
            id: "return_break",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 17, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE", "FOOD"],
              preferKeywords: ["kafe", "yemek"],
            ),
            estimatedDurationMin: 60,
            label: "Dönüş molası",
            isOptional: true,
          ),
          ActivityBeat(
            id: "city_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 19, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["yerel", "şehir merkezi"],
            ),
            estimatedDurationMin: 90,
            label: "Şehirde akşam yemeği",
          ),
        ],
      );

  // ───────────────────────────────────────────────────────────────────
  // 7. YEREL RİTÜEL
  // ───────────────────────────────────────────────────────────────────
  static DayTheme _localRitual() => DayTheme(
        id: DayThemeId.localRitual,
        preferredStart: const TimeOfDayLite(hour: 10, minute: 30),
        targetPlaceCount: 7,
        minPlaceRequirements: const {"FOOD": 1, "COFFEE": 1, "CULTURE": 1},
        beats: const [
          ActivityBeat(
            id: "slow_brunch",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 10, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE", "FOOD"],
              preferKeywords: ["brunch", "kahvaltı", "yerel", "geleneksel"],
            ),
            estimatedDurationMin: 60,
            label: "Yavaş kahvaltı",
          ),
          ActivityBeat(
            id: "neighborhood_walk",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 12, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["SQUARE", "CULTURE", "MARKET"],
              preferKeywords: ["mahalle", "sokak", "yerel hayat"],
            ),
            estimatedDurationMin: 75,
            label: "Mahalle gezisi",
          ),
          ActivityBeat(
            id: "local_lunch",
            role: BeatRole.lunch,
            time:
                BeatTime(TimeOfDayLite(hour: 13, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords: ["yerel", "ev yemeği", "lokanta", "trattoria"],
            ),
            estimatedDurationMin: 90,
            label: "Yerel öğle yemeği",
          ),
          ActivityBeat(
            id: "matinee_culture",
            role: BeatRole.transition,
            time:
                BeatTime(TimeOfDayLite(hour: 15, minute: 30), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["CULTURE", "VIEW"],
              preferKeywords: ["küçük", "yerel", "atölye", "studio"],
            ),
            estimatedDurationMin: 75,
            label: "Matine kültür",
            isOptional: true,
          ),
          ActivityBeat(
            id: "coffee_ritual",
            role: BeatRole.softBreak,
            time:
                BeatTime(TimeOfDayLite(hour: 17, minute: 0), toleranceMin: 45),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["COFFEE"],
              preferKeywords: ["geleneksel", "klasik", "yerel"],
            ),
            estimatedDurationMin: 45,
            label: "Geleneksel kahve molası",
          ),
          ActivityBeat(
            id: "calm_view",
            role: BeatRole.goldenHour,
            time:
                BeatTime(TimeOfDayLite(hour: 18, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              preferGroups: ["VIEW", "SQUARE", "NATURE"],
              preferKeywords: ["sakin", "yerel", "mahalle manzara"],
            ),
            estimatedDurationMin: 50,
            label: "Sakin manzara",
            isOptional: true,
          ),
          ActivityBeat(
            id: "neighborhood_dinner",
            role: BeatRole.dinner,
            time:
                BeatTime(TimeOfDayLite(hour: 20, minute: 30), toleranceMin: 60),
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: ["FOOD"],
              preferGroups: ["FOOD"],
              preferKeywords:
                  ["mahalle", "lokanta", "yerel halk", "geleneksel"],
            ),
            estimatedDurationMin: 90,
            label: "Mahalle yemeği",
          ),
        ],
      );
}
