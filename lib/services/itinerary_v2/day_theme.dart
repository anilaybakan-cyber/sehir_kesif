// =============================================================================
// ITINERARY V2 - DAY THEME MODEL
// Bir günün hikayesini tanımlayan tema yapısı.
// =============================================================================

import 'beat.dart';

/// Tema kimliği - hangi tema olduğunu enum olarak tutar.
/// Multi-day variety için string identifier yerine enum kullanılır.
enum DayThemeId {
  /// Tarih & Mimari - müze, ikonik yapı, meydan, tarihi kafe.
  history,

  /// Yerel Lezzet - brunch, pazar, sokak yemeği, gourmet.
  localFood,

  /// Sanat & Sokak - galeri, sokak sanatı, butik, hipster bölge.
  artStreet,

  /// Doğa & Manzara - park, yürüyüş, manzara noktası, sahil.
  nature,

  /// Gece & Eğlence - geç başlangıç, canlı müzik, bar, gece pazarı.
  nightlife,

  /// Şehir Dışı - day trip, ada, antik kent.
  dayTrip,

  /// Yerel Ritüel - mahalle gezisi, brunch + park + matine, yavaş gün.
  localRitual,
}

/// DayThemeId için yardımcı extension.
extension DayThemeIdX on DayThemeId {
  /// Kullanıcıya gösterilecek Türkçe ad.
  String get nameTr {
    switch (this) {
      case DayThemeId.history:
        return "Tarih & Mimari";
      case DayThemeId.localFood:
        return "Yerel Lezzet";
      case DayThemeId.artStreet:
        return "Sanat & Sokak";
      case DayThemeId.nature:
        return "Doğa & Manzara";
      case DayThemeId.nightlife:
        return "Gece & Eğlence";
      case DayThemeId.dayTrip:
        return "Şehir Dışı";
      case DayThemeId.localRitual:
        return "Yerel Ritüel";
    }
  }

  String get nameEn {
    switch (this) {
      case DayThemeId.history:
        return "History & Architecture";
      case DayThemeId.localFood:
        return "Local Flavors";
      case DayThemeId.artStreet:
        return "Art & Streets";
      case DayThemeId.nature:
        return "Nature & Views";
      case DayThemeId.nightlife:
        return "Nightlife";
      case DayThemeId.dayTrip:
        return "Day Trip";
      case DayThemeId.localRitual:
        return "Local Ritual";
    }
  }

  /// Bu tema bir "akşam ana aktivite" tipi taşıyor mu? (variety tracker için)
  /// nightlife, localFood gibi temalar evening_main slot'unda farklı şeyler önerir.
  String get eveningSignature {
    switch (this) {
      case DayThemeId.history:
        return "classic_dinner"; // Klasik restoran
      case DayThemeId.localFood:
        return "wine_or_meyhane"; // Şarap evi / meyhane
      case DayThemeId.artStreet:
        return "rooftop_or_bistro"; // Rooftop / sanatçı bölge bistro
      case DayThemeId.nature:
        return "calm_dinner"; // Sakin manzaralı yemek
      case DayThemeId.nightlife:
        return "club_or_live"; // Gece kulübü / canlı müzik
      case DayThemeId.dayTrip:
        return "early_dinner"; // Erken dönüş yemeği
      case DayThemeId.localRitual:
        return "neighborhood_dinner"; // Mahalle yemeği
    }
  }
}

/// Bir günün tema iskeleti - hangi beat'lerden oluşuyor.
class DayTheme {
  /// Tema kimliği.
  final DayThemeId id;

  /// Beat akışı (sıralı).
  final List<ActivityBeat> beats;

  /// Bu tema için günün başlangıç saati (esnek - kullanıcı erteleyebilir).
  /// Çoğu tema 09:00, nightlife teması 11:00, day-trip 08:00.
  final TimeOfDayLite preferredStart;

  /// Tema'nın "hard requirement"ı: bu kategorilerden mekan yoksa tema atlanır.
  /// Örn: nature için en az 2 NATURE/VIEW kategori; nightlife için en az 1 SOCIAL.
  final Map<String, int> minPlaceRequirements;

  /// Tema'nın hedef toplam mekan sayısı (yorgunluk dengesi).
  final int targetPlaceCount;

  String get nameTr => id.nameTr;
  String get nameEn => id.nameEn;

  const DayTheme({
    required this.id,
    required this.beats,
    required this.preferredStart,
    required this.minPlaceRequirements,
    required this.targetPlaceCount,
  });
}
