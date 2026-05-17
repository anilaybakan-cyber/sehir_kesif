// =============================================================================
// ITINERARY V2 - FEASIBILITY CHECKS
// Hard constraint kontrolleri (asla ihlal edilmemeli).
// Soft constraint'ler (skor bonusu/cezası) BeatFiller'da yapılır.
// =============================================================================

import '../../models/city_model.dart';
import 'beat.dart';
import 'variety_tracker.dart';

/// Bir mekanın bir beat'e uyumu - feasibility sonucu.
enum BeatFeasibility {
  ok,

  /// Mekan zaten kullanıldı (variety tracker).
  alreadyUsed,

  /// Mekan day-trip ama beat day-trip değil veya tersi.
  dayTripMismatch,

  /// Beat policy "must" kategorisi şart koşmuş, mekan o gruptan değil.
  wrongCategoryGroup,

  /// Önceki mekan da consumption ise, peş peşe consumption yasak.
  consecutiveConsumption,

  /// Aynı kategoriden çok arka arkaya (3+).
  tooMuchSameCategory,
}

/// Bir saatin bir mekana uyumu - time planner sonucu.
enum TimeFeasibility {
  ok,
  tooEarlyForVenue,
  tooLateForBeat,
  closesTooSoon,
}

/// Hard constraint (filter) kontrolleri.
/// Bu kontroller "binary" - ya geçer ya geçmez. Skorlama yok.
class FeasibilityChecker {
  /// Yeme-içme grupları (peş peşe yasak için).
  static const Set<String> _consumptionGroups = {"FOOD", "COFFEE", "SOCIAL"};

  /// Bir mekanın bir beat'e uygun olup olmadığını kontrol eder.
  /// Önceki seçilen mekanları gözeterek diversity kontrolü yapar.
  static BeatFeasibility check({
    required Highlight place,
    required ActivityBeat beat,
    required List<FilledBeat> previouslyFilled,
    required TripVarietyTracker tripTracker,
    bool forceInclude = false,
  }) {
    if (forceInclude) return BeatFeasibility.ok;
    // 1. Trip-genelinde tekrar?
    if (tripTracker.isPlaceUsed(place)) {
      return BeatFeasibility.alreadyUsed;
    }

    // 2. Day-trip mismatch
    final isDayTripBeat = beat.role == BeatRole.dayTripMain;
    if (place.isDayTrip != isDayTripBeat) {
      return BeatFeasibility.dayTripMismatch;
    }

    // 3. Beat must-group kontrolü
    final placeGroup = TripVarietyTracker.groupOf(place);
    if (beat.categoryPolicy.mustGroups.isNotEmpty &&
        !beat.categoryPolicy.mustGroups.contains(placeGroup)) {
      return BeatFeasibility.wrongCategoryGroup;
    }

    // 4. KURAL 5: Arka arkaya MAX 2 consumption izin, 3. KESİNLİKLE engellenir.
    // Örn: Kafe → Restoran OK ✓ ama Kafe → Restoran → Bar YASAK ✗
    // Hiçbir istisna yok (lunch/dinner dahil), çünkü 3 yeme-içme fazla.
    if (_consumptionGroups.contains(placeGroup)) {
      if (previouslyFilled.length >= 2) {
        final last1 = TripVarietyTracker.groupOf(previouslyFilled.last.place);
        final last2 = TripVarietyTracker.groupOf(
            previouslyFilled[previouslyFilled.length - 2].place);
        if (_consumptionGroups.contains(last1) &&
            _consumptionGroups.contains(last2)) {
          return BeatFeasibility.consecutiveConsumption;
        }
      }
    }

    // 5. Aynı grup 3+ peş peşe yasak
    if (previouslyFilled.length >= 2) {
      final last1 = TripVarietyTracker.groupOf(previouslyFilled.last.place);
      final last2 =
          TripVarietyTracker.groupOf(previouslyFilled[previouslyFilled.length - 2].place);
      if (last1 == placeGroup && last2 == placeGroup) {
        return BeatFeasibility.tooMuchSameCategory;
      }
    }

    return BeatFeasibility.ok;
  }

  /// Bir grup consumption mı?
  static bool isConsumption(String group) =>
      _consumptionGroups.contains(group);

  /// Bir mekan o gün bu saatte ziyaret edilebilir mi (sadece açılış kontrolü)?
  /// `null` dayKey → tüm günler için ortak kontrolü yapar (esnek).
  static bool isOpenForVisit({
    required Highlight place,
    required TimeOfDayLite startTime,
    required int durationMin,
    required String? dayKey,
  }) {
    // 1. Başlangıç saatinde açık mı?
    if (!place.isOpenAt(startTime.hour, startTime.minute,
        dayOfWeek: dayKey)) {
      return false;
    }

    // 2. Bitiş saatinde de açık mı? (Kapanışta zorla atılmasın)
    final end = startTime.addMinutes(durationMin);
    if (!place.isOpenAt(end.hour, end.minute, dayOfWeek: dayKey)) {
      return false;
    }

    return true;
  }
}
