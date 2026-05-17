// =============================================================================
// ITINERARY V2 - BEAT MODEL
// Bir günün tema akışındaki tek bir "etkinlik anı" (beat).
// =============================================================================

import '../../models/city_model.dart';

/// Beat'in günün hikayesindeki rolü.
/// Slot kategorisinden farklı: kategori "ne tür mekan", role "günde ne işe yarıyor".
enum BeatRole {
  /// Günün ana ikonik durağı (ana müze, ana yapı, must-see).
  /// Genelde 1 günde 1-2 tane olur.
  icon,

  /// İkonlar arası geçiş - meydan, çarşı, yürüyüş bölgesi, manzara.
  /// Daha kısa, daha esnek, kategori toleransı geniş.
  transition,

  /// Öğle yemeği ana noktası.
  lunch,

  /// Akşam yemeği ana noktası.
  dinner,

  /// Hafif mola - kahve, tatlı, dondurma, kısa kafe oturuşu.
  softBreak,

  /// Akşam aktivitesi - manzara/teras/sunset/golden hour.
  goldenHour,

  /// Geç akşam aktivitesi - bar, canlı müzik, gece pazarı, tatlı yürüyüşü.
  /// Tema'ya göre tipi değişir (variety tracker'a kaydedilir).
  evening,

  /// Şehir dışı uzun gezi (day-trip için).
  dayTripMain,
}

/// Beat'in tercih ettiği saat aralığı.
/// `anchor` "ideal saat", `tolerance` "kayma toleransı" (dakika).
class BeatTime {
  /// Tercih edilen başlangıç saati (örn: TimeOfDayLite(hour: 9, minute: 0)).
  final TimeOfDayLite anchor;

  /// Anchor'dan ne kadar sapabilir (dakika). Tipik: 30-60.
  final int toleranceMin;

  /// Bu saatin alt sınırı (toleransı uygulanmış).
  TimeOfDayLite get earliest => anchor.subtractMinutes(toleranceMin);

  /// Bu saatin üst sınırı.
  TimeOfDayLite get latest => anchor.addMinutes(toleranceMin);

  const BeatTime(this.anchor, {this.toleranceMin = 30});
}

/// Hafif "TimeOfDay" tipi - flutter material'a bağımlı olmasın.
class TimeOfDayLite {
  final int hour; // 0-23
  final int minute; // 0-59

  const TimeOfDayLite({required this.hour, required this.minute});

  factory TimeOfDayLite.fromMinutes(int totalMinutes) {
    final m = totalMinutes.clamp(0, 23 * 60 + 59);
    return TimeOfDayLite(hour: m ~/ 60, minute: m % 60);
  }

  int get totalMinutes => hour * 60 + minute;

  TimeOfDayLite addMinutes(int min) =>
      TimeOfDayLite.fromMinutes(totalMinutes + min);

  TimeOfDayLite subtractMinutes(int min) =>
      TimeOfDayLite.fromMinutes(totalMinutes - min);

  String get formatted =>
      "${hour.toString().padLeft(2, '0')}:${minute.toString().padLeft(2, '0')}";

  @override
  String toString() => formatted;
}

/// Bir beat'i seçerken kullanılan kategori tercihleri.
/// `must` ve `prefer` farkı:
///   - must: bu kategorilerden biri OLMAK ZORUNDA (filter)
///   - prefer: bu kategorilerden biri tercih edilir (skor bonusu)
class BeatCategoryPolicy {
  /// Mekan bu kategori grup'larından birinde olmalı.
  /// (Eski code'daki "FOOD", "COFFEE", "CULTURE", "VIEW", "SQUARE", "SOCIAL", "NATURE")
  /// Boş liste = serbest, her grup kabul.
  final List<String> mustGroups;

  /// Mekan bu kategori grup'larından birindeyse skor bonusu alır.
  final List<String> preferGroups;

  /// Mekan bu özelliklerden birini taşırsa (tag/category text) bonus.
  /// Örn: "rooftop", "manzara", "yerel", "tarihi"
  final List<String> preferKeywords;

  const BeatCategoryPolicy({
    this.mustGroups = const [],
    this.preferGroups = const [],
    this.preferKeywords = const [],
  });

  /// Boş policy = her şeyi kabul et.
  static const BeatCategoryPolicy unrestricted = BeatCategoryPolicy();
}

/// Bir günün akışındaki tek bir "beat" (aktivite anı).
class ActivityBeat {
  /// Beat'in benzersiz id'si (tema içinde). Örn: "morning_icon", "lunch", "golden_hour".
  final String id;

  /// Günün hikayesindeki rolü.
  final BeatRole role;

  /// Tercih edilen saat ve toleransı.
  final BeatTime time;

  /// Hangi kategorilerden bir mekan seçilebilir.
  final BeatCategoryPolicy categoryPolicy;

  /// Beat'in tahmini süresi (mekan ziyareti, dakika).
  /// Mekan tipi belli olunca daha hassas hesaplanır - bu bir başlangıç tahmini.
  final int estimatedDurationMin;

  /// Beat opsiyonel mi? Kullanıcı yorgunsa, gün dolduysa atlanabilir.
  final bool isOptional;

  /// Beat'i tanımlayıcı kısa açıklama (UI'da bilgi/debug için).
  /// Örn: "Şehrin ikonik müzesi", "Yerel öğle yemeği".
  final String label;

  /// Eski kodla uyum için - varsayılan grup (categoryPolicy.preferGroups[0]).
  String get primaryGroup =>
      categoryPolicy.preferGroups.isNotEmpty
          ? categoryPolicy.preferGroups.first
          : (categoryPolicy.mustGroups.isNotEmpty
              ? categoryPolicy.mustGroups.first
              : "ANY");

  const ActivityBeat({
    required this.id,
    required this.role,
    required this.time,
    required this.categoryPolicy,
    required this.estimatedDurationMin,
    required this.label,
    this.isOptional = false,
  });
}

/// Bir beat'in çıktısı - seçilen mekan + gerçek başlangıç saati.
class FilledBeat {
  final ActivityBeat beat;
  final Highlight place;

  /// Gerçek başlangıç saati (açılış saati / önceki beat süresi nedeniyle anchor'dan kaymış olabilir).
  final TimeOfDayLite actualStart;

  /// Mekan için tahmini süre (gerçek - kategori/openHours ile).
  final int durationMin;

  /// Önceki beat'ten buraya gelmek için tahmini transit süresi (dakika).
  final int transitMinFromPrev;

  /// Önceki beat'ten mesafe (km).
  final double transitDistKm;

  TimeOfDayLite get actualEnd => actualStart.addMinutes(durationMin);

  const FilledBeat({
    required this.beat,
    required this.place,
    required this.actualStart,
    required this.durationMin,
    this.transitMinFromPrev = 0,
    this.transitDistKm = 0,
  });

  FilledBeat copyWith({
    TimeOfDayLite? actualStart,
    int? durationMin,
    int? transitMinFromPrev,
    double? transitDistKm,
  }) {
    return FilledBeat(
      beat: beat,
      place: place,
      actualStart: actualStart ?? this.actualStart,
      durationMin: durationMin ?? this.durationMin,
      transitMinFromPrev: transitMinFromPrev ?? this.transitMinFromPrev,
      transitDistKm: transitDistKm ?? this.transitDistKm,
    );
  }
}
