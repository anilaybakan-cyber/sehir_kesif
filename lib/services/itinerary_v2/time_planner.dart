// =============================================================================
// ITINERARY V2 - TIME PLANNER
// Esnek saat anchor'lama ve kayma yönetimi.
// Eski sistemde saatler "cumulative" idi - bir mekan uzun sürdüyse hepsi kayardı.
// Yeni sistemde her beat kendi anchor'ına göre yerleşir, sapma toleransla sınırlı.
// =============================================================================

import '../../models/city_model.dart';
import 'beat.dart';
import 'feasibility.dart';

/// Bir beat için "ideal saat" + kısıtlar = "gerçek başlangıç saati" hesaplar.
class TimePlanner {
  /// Bir beat için en iyi başlangıç saatini bulur.
  ///
  /// Kurallar (öncelik sırasıyla):
  ///   1. Mekan açılmamışsa → açılış saatini bekle (saatçe makulse)
  ///   2. Önceki beat'in bitişinden sonra olmalı (transit dahil)
  ///   3. Beat'in tolerance window'una yakın olmalı (anchor ± tolerance)
  ///   4. Mekan kapanmadan önce ziyaret bitmeli
  ///
  /// Döndürür:
  ///   - actualStart: gerçek başlangıç saati
  ///   - durationMin: ziyaret süresi (kategori bazlı, openHours ile sınırlanmış)
  ///   - feasibility: [TimeFeasibility] eğer kabul edilebilir mi
  static TimePlannerResult planBeat({
    required ActivityBeat beat,
    required Highlight place,
    required TimeOfDayLite earliestStart, // Önceki beat sonu + transit
    required String dayOfWeekKey, // "monday".."sunday"
  }) {
    // 1. Beat anchor'a en yakın saat: max(anchor-tolerance, earliestStart)
    int targetMin = beat.time.anchor.totalMinutes;

    // earliestStart, anchor'dan büyük olabilir → onu al
    if (earliestStart.totalMinutes > targetMin) {
      targetMin = earliestStart.totalMinutes;
    }

    // earliestStart, beat.time.earliest'ten küçükse → anchor'a yaklaştır
    if (targetMin < beat.time.earliest.totalMinutes) {
      targetMin = beat.time.earliest.totalMinutes;
    }

    // 2. Mekan açılış saati kontrolü
    final openMin = place.getOpeningMinutes(dayOfWeekKey);
    final closeMin = place.getClosingMinutes(dayOfWeekKey);

    // openHours yoksa kontrolü atla
    bool delayedForOpening = false;
    if (openMin >= 0 && targetMin < openMin) {
      // Açılışı bekle (max 120 dk bekleme; daha fazlaysa beat infeasible)
      // Barcelona/Roma gibi şehirlerde mekanlar 10-11'de açılıyor
      if (openMin - targetMin > 120) {
        return TimePlannerResult.infeasible(
          beat: beat,
          place: place,
          reason: TimeFeasibility.tooEarlyForVenue,
        );
      }
      targetMin = openMin;
      delayedForOpening = true;
    }

    // 3. Beat tolerance üst sınırı kontrolü
    // Açılış nedeniyle ertelendiyse, beat'in latest sınırını bypass et
    // (kullanıcı zaten beklemeyi kabul etti).
    if (!delayedForOpening && targetMin > beat.time.latest.totalMinutes) {
      return TimePlannerResult.infeasible(
        beat: beat,
        place: place,
        reason: TimeFeasibility.tooLateForBeat,
      );
    }

    // 4. Süre hesabı
    int durationMin = beat.estimatedDurationMin;
    // Mekan tipi farklıysa süre tahminini güncelle
    durationMin = _adjustDurationForCategory(place, durationMin);

    // 5. Kapanış saati kontrolü - mekan ziyaret tamamlanmadan kapanırsa
    if (closeMin >= 0 && targetMin + durationMin > closeMin) {
      // Ziyareti kısalt (min 20 dk olmalı - kısa duraklar için)
      final available = closeMin - targetMin;
      if (available < 20) {
        return TimePlannerResult.infeasible(
          beat: beat,
          place: place,
          reason: TimeFeasibility.closesTooSoon,
        );
      }
      durationMin = available;
    }

    // Başarılı
    return TimePlannerResult(
      beat: beat,
      place: place,
      actualStart: TimeOfDayLite.fromMinutes(targetMin),
      durationMin: durationMin,
      feasibility: TimeFeasibility.ok,
    );
  }

  /// Mekan kategorisine göre ziyaret süresini güncelle.
  /// Eski koddan adapte (90 / 45 / 120 / 60 dakikalar).
  static int _adjustDurationForCategory(Highlight h, int defaultMin) {
    final c = h.category.toLowerCase();
    final n = h.name.toLowerCase();

    // Müze - büyük müze 180dk, küçük müze 120dk
    if (c.contains("müze") || c.contains("museum") || n.contains("museum")) {
      // Büyük müze sinyalleri
      if ((h.reviewCount ?? 0) > 5000 ||
          n.contains("national") ||
          n.contains("milli")) {
        return 180;
      }
      return 120;
    }
    // Restoran
    if (c.contains("yeme") ||
        c.contains("restoran") ||
        c.contains("food") ||
        n.contains("restaurant") ||
        n.contains("trattoria")) {
      return 90;
    }
    // Kafe / pastane
    if (c.contains("kafe") ||
        c.contains("cafe") ||
        c.contains("coffee") ||
        n.contains("pastane") ||
        n.contains("bakery")) {
      return 45;
    }
    // Bar / gece hayatı
    if (c.contains("bar") ||
        c.contains("pub") ||
        c.contains("club") ||
        n.contains("bar")) {
      return 120;
    }
    // Manzara / teras
    if (c.contains("manzara") || c.contains("view") || c.contains("teras")) {
      return 60;
    }
    // Park / doğa
    if (c.contains("park") || c.contains("bahçe") || c.contains("garden")) {
      return 75;
    }
    // Pazar / çarşı
    if (c.contains("pazar") ||
        c.contains("market") ||
        c.contains("bazaar") ||
        c.contains("çarşı")) {
      return 60;
    }
    // Meydan
    if (c.contains("meydan") || c.contains("square")) return 30;

    return defaultMin > 0 ? defaultMin : 90;
  }
}

/// TimePlanner'ın sonucu - başarılı veya başarısız.
class TimePlannerResult {
  final ActivityBeat beat;
  final Highlight place;
  final TimeOfDayLite? actualStart;
  final int durationMin;
  final TimeFeasibility feasibility;
  final String? reason;

  bool get isOk => feasibility == TimeFeasibility.ok;

  const TimePlannerResult({
    required this.beat,
    required this.place,
    required this.actualStart,
    required this.durationMin,
    required this.feasibility,
    this.reason,
  });

  factory TimePlannerResult.infeasible({
    required ActivityBeat beat,
    required Highlight place,
    required TimeFeasibility reason,
  }) {
    return TimePlannerResult(
      beat: beat,
      place: place,
      actualStart: null,
      durationMin: 0,
      feasibility: reason,
      reason: reason.name,
    );
  }
}
