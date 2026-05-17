// =============================================================================
// ITINERARY V2 - TRIP VARIETY TRACKER
// Tüm seyahat (multi-day) boyunca çeşitliliği koruyan tracker.
// "4 gün üst üste gece kulübü" tipi monotonluğu engeller.
// =============================================================================

import '../../models/city_model.dart';
import 'day_theme.dart';

/// Tüm seyahat boyunca kullanılan tema/mekan/kategori bilgisini tutar.
/// Yeni gün planlanırken "henüz kullanılmamış" şeyleri tercih etmek için kullanılır.
class TripVarietyTracker {
  /// Hangi tema-id'leri kullanıldı (her tema en fazla 1-2 kez tekrar edebilir).
  final List<DayThemeId> usedThemes = [];

  /// Hangi mekan isimleri kullanıldı (tüm trip'te asla tekrar etmesin).
  final Set<String> usedPlaceNames = {};

  /// Hangi mekan ID'leri kullanıldı (Google Place ID; isim eşleşmesi başarısız olursa).
  final Set<String> usedPlaceIds = {};

  /// Trip boyunca kategori grubu sayacı (FOOD: 5, CULTURE: 8 vs.).
  final Map<String, int> categoryCounts = {};

  /// Hangi "evening signature"lar kullanıldı (4 gün club_or_live tekrar etmesin).
  /// Örn: "club_or_live", "rooftop_or_bistro", "wine_or_meyhane"
  final List<String> usedEveningSignatures = [];

  /// Hangi semt/area'lar daha çok kullanıldı (tüm trip aynı mahallede geçmesin).
  final Map<String, int> areaCounts = {};

  // ─────────────────────────────────────────────────────────────────
  // KAYIT
  // ─────────────────────────────────────────────────────────────────

  /// Bir günü trip'e dahil et - tema, mekanlar, alan vs.
  void recordDay(DayTheme theme, List<Highlight> places) {
    usedThemes.add(theme.id);
    usedEveningSignatures.add(theme.id.eveningSignature);

    for (final p in places) {
      usedPlaceNames.add(p.name);
      if (p.id != null && p.id!.isNotEmpty) usedPlaceIds.add(p.id!);

      final group = _categoryGroup(p);
      categoryCounts[group] = (categoryCounts[group] ?? 0) + 1;

      if (p.area.isNotEmpty) {
        areaCounts[p.area] = (areaCounts[p.area] ?? 0) + 1;
      }
    }
  }

  // ─────────────────────────────────────────────────────────────────
  // SORGU
  // ─────────────────────────────────────────────────────────────────

  /// Bir tema kaç kez kullanıldı?
  int themeUsageCount(DayThemeId id) =>
      usedThemes.where((t) => t == id).length;

  /// Bir evening signature kaç kez kullanıldı?
  int eveningUsageCount(String signature) =>
      usedEveningSignatures.where((s) => s == signature).length;

  /// Mekan daha önce kullanıldı mı?
  bool isPlaceUsed(Highlight h) {
    if (usedPlaceNames.contains(h.name)) return true;
    if (h.id != null && usedPlaceIds.contains(h.id!)) return true;
    return false;
  }

  /// Bu tema'yı henüz kullanmadıysak, daha az kullandıysak onu tercih et.
  /// 0..1 arası bir score değeri döner (1 = hiç kullanılmadı).
  double themeFreshness(DayThemeId id) {
    final count = themeUsageCount(id);
    if (count == 0) return 1.0;
    if (count == 1) return 0.4;
    return 0.1;
  }

  /// Bir kategori grubu trip'te ne kadar baskın?
  /// 0..1 arası (yüksek = çok baskın, daha az tercih edilmeli).
  double categoryDominance(String group) {
    final total = categoryCounts.values.fold<int>(0, (a, b) => a + b);
    if (total == 0) return 0.0;
    final c = categoryCounts[group] ?? 0;
    return c / total;
  }

  /// Bir bölge trip'te ne kadar dolduruldu?
  int areaUsage(String area) => areaCounts[area] ?? 0;

  // ─────────────────────────────────────────────────────────────────
  // YARDIMCILAR
  // ─────────────────────────────────────────────────────────────────

  static String _categoryGroup(Highlight h) {
    // Tüm metinleri küçük harf yapıp birleştiriyoruz (Name + Category + Tags)
    final blob = "${h.name} ${h.category} ${h.tags.join(' ')}".toLowerCase();

    // 1. COFFEE / DESSERT
    if (blob.contains("coffee") ||
        blob.contains("kahve") ||
        blob.contains("cafe") ||
        blob.contains("kafe") ||
        blob.contains("pastane") ||
        blob.contains("patisserie") ||
        blob.contains("bakery") ||
        blob.contains("fırın") ||
        blob.contains("dondurma") ||
        blob.contains("gelateria") ||
        blob.contains("ice cream") ||
        blob.contains("tatlı")) {
      return "COFFEE";
    }

    // 2. FOOD
    if (blob.contains("restoran") ||
        blob.contains("restaurant") ||
        blob.contains("yeme") ||
        blob.contains("yemek") ||
        blob.contains("food") ||
        blob.contains("gastronomi") ||
        blob.contains("bistro") ||
        blob.contains("brunch") ||
        blob.contains("tapas") ||
        blob.contains("bodega") ||
        blob.contains("mutfa") ||
        blob.contains("delicatessen") ||
        blob.contains("trattoria") ||
        blob.contains("osteria") ||
        blob.contains("steak") ||
        blob.contains("burger") ||
        blob.contains("pizza") ||
        blob.contains("sushi") ||
        blob.contains("tapas") ||
        blob.contains("taberna") ||
        blob.contains("meyhane") ||
        blob.contains("lokanta")) {
      return "FOOD";
    }

    // 3. SOCIAL (BAR / NIGHTLIFE)
    if (blob.contains("bar") ||
        blob.contains("pub") ||
        blob.contains("gece") ||
        blob.contains("night") ||
        blob.contains("club") ||
        blob.contains("kulüp") ||
        blob.contains("meyhane") ||
        blob.contains("vermuteria") ||
        blob.contains("cerveceria") ||
        blob.contains("birahane") ||
        blob.contains("social") ||
        blob.contains("cocktail") ||
        blob.contains("kokteyl")) {
      return "SOCIAL";
    }

    // 4. VIEW
    if (blob.contains("view") ||
        blob.contains("manzara") ||
        blob.contains("teras") ||
        blob.contains("rooftop") ||
        blob.contains("seyir") ||
        blob.contains("panoramik") ||
        blob.contains("panorama") ||
        blob.contains("miradouro")) {
      return "VIEW";
    }

    // 5. SQUARE
    if (blob.contains("meydan") ||
        blob.contains("square") ||
        blob.contains("plaza") ||
        blob.contains("plaça") ||
        blob.contains("largo") ||
        blob.contains("piazza")) {
      return "SQUARE";
    }

    // 6. MARKET
    if (blob.contains("market") ||
        blob.contains("pazar") ||
        blob.contains("çarşı") ||
        blob.contains("bazaar") ||
        blob.contains("mercado") ||
        blob.contains("feria") ||
        blob.contains("pasaj")) {
      return "MARKET";
    }

    // 7. NATURE
    if (blob.contains("park") ||
        blob.contains("bahçe") ||
        blob.contains("garden") ||
        blob.contains("doğa") ||
        blob.contains("nature") ||
        blob.contains("sahil") ||
        blob.contains("plaj") ||
        blob.contains("beach") ||
        blob.contains("göl") ||
        blob.contains("lake") ||
        blob.contains("river") ||
        blob.contains("nehir") ||
        blob.contains("orman") ||
        blob.contains("forest")) {
      return "NATURE";
    }

    // 8. CULTURE (Default)
    return "CULTURE";
  }

  /// Highlight için kategori grubu tahmini (helper - dışarıdan da kullanılabilir).
  static String groupOf(Highlight h) => _categoryGroup(h);
}
