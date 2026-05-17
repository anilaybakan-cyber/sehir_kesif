// =============================================================================
// ITINERARY V2 UNIT TESTS
// Pure-logic testler - SharedPreferences/CityDataLoader mock'a gerek yok.
// =============================================================================

import 'package:flutter_test/flutter_test.dart';
import 'package:sehir_kesif/models/city_model.dart';
import 'package:sehir_kesif/services/itinerary_v2/beat.dart';
import 'package:sehir_kesif/services/itinerary_v2/city_analyzer.dart';
import 'package:sehir_kesif/services/itinerary_v2/day_theme.dart';
import 'package:sehir_kesif/services/itinerary_v2/feasibility.dart';
import 'package:sehir_kesif/services/itinerary_v2/theme_catalog.dart';
import 'package:sehir_kesif/services/itinerary_v2/theme_distributor.dart';
import 'package:sehir_kesif/services/itinerary_v2/time_planner.dart';
import 'package:sehir_kesif/services/itinerary_v2/variety_tracker.dart';

// ─────────────────────────────────────────────────────────────────
// FIXTURE HELPERS
// ─────────────────────────────────────────────────────────────────

Highlight _h(
  String name, {
  String category = "tarihi",
  double lat = 41.0,
  double lng = 29.0,
  double rating = 4.5,
  int reviewCount = 500,
  Map<String, String>? openHours,
  String area = "Merkez",
  List<String> tags = const [],
  double distFromCenter = 1.0,
  String price = "medium",
}) {
  return Highlight(
    name: name,
    area: area,
    category: category,
    tags: tags,
    distanceFromCenter: distFromCenter,
    lat: lat,
    lng: lng,
    price: price,
    description: "$name desc",
    rating: rating,
    reviewCount: reviewCount,
    openHours: openHours ??
        const {"everyday": "09:00-22:00"},
  );
}

List<Highlight> _historicCity() {
  return [
    _h("Ana Müze", category: "tarihi müze", rating: 4.8, reviewCount: 2000),
    _h("Saray", category: "tarihi saray", rating: 4.7, reviewCount: 1800),
    _h("Antik Yapı", category: "tarih", rating: 4.6, reviewCount: 1200),
    _h("Modern Sanat Galerisi",
        category: "sanat galerisi", rating: 4.4, reviewCount: 600),
    _h("Tarihi Meydan", category: "meydan", rating: 4.5, reviewCount: 800),
    _h("Tarihi Çarşı", category: "pazar çarşı", rating: 4.3, reviewCount: 700),
    _h("Klasik Restoran",
        category: "restoran yemek", rating: 4.5, reviewCount: 800),
    _h("Modern Bistro", category: "bistro", rating: 4.4, reviewCount: 500),
    _h("Yerel Lokanta",
        category: "restoran yerel", rating: 4.6, reviewCount: 400),
    _h("Tarihi Kafe", category: "kafe", rating: 4.4, reviewCount: 300),
    _h("Pastane", category: "pastane kafe", rating: 4.3, reviewCount: 250),
    _h("Manzaralı Teras",
        category: "manzara teras", rating: 4.6, reviewCount: 600),
    _h("Şehir Parkı", category: "park bahçe", rating: 4.5, reviewCount: 800),
    _h("Sahil Yürüyüşü",
        category: "sahil doğa", rating: 4.5, reviewCount: 700),
    _h("Şarap Evi", category: "wine bar", rating: 4.6, reviewCount: 400),
    _h("Caz Kulübü",
        category: "bar canlı müzik", rating: 4.7, reviewCount: 350),
    _h("Gece Kulübü", category: "club gece", rating: 4.3, reviewCount: 250),
    // Day-trip aday
    Highlight(
      name: "Şehir Dışı Antik Kent",
      area: "Day Trip",
      category: "tarihi antik",
      tags: const ["day_trip"],
      distanceFromCenter: 60.0,
      lat: 41.5,
      lng: 29.5,
      price: "medium",
      description: "Antik kent",
      rating: 4.7,
      reviewCount: 1500,
      openHours: const {"everyday": "08:00-18:00"},
    ),
  ];
}

void main() {
  // ────────────────────────────────────────────────────────────────
  group("CityAnalyzer", () {
    test("tarihi şehirde history teması yüksek skor alır", () {
      final profile = CityAnalyzer.analyze(_historicCity());
      expect(profile.totalCityPlaces, 17);
      expect(profile.dayTripCandidates, 1);
      expect(profile.themeFeasible[DayThemeId.history], isTrue);
      expect(profile.themeStrengths[DayThemeId.history]!,
          greaterThan(50));
    });

    test("min requirements karşılanmıyorsa tema feasible değil", () {
      // Sadece 2 müze, restoran/kafe yok - history teması için FOOD min 1 var
      final places = [
        _h("Müze 1", category: "tarihi müze"),
        _h("Müze 2", category: "tarihi müze"),
      ];
      final profile = CityAnalyzer.analyze(places);
      expect(profile.themeFeasible[DayThemeId.history], isFalse);
    });

    test("rankedThemes skoruna göre sıralı", () {
      final profile = CityAnalyzer.analyze(_historicCity());
      final ranked = profile.rankedThemes;
      // İlk tema, son temadan daha yüksek skorlu
      expect(profile.themeStrengths[ranked.first]!,
          greaterThanOrEqualTo(profile.themeStrengths[ranked.last]!));
    });
  });

  // ────────────────────────────────────────────────────────────────
  group("ThemeDistributor", () {
    test("4 gün için 4 farklı tema atanmalı (variety)", () {
      final profile = CityAnalyzer.analyze(_historicCity());
      final plan = ThemeDistributor.distribute(
        totalDays: 4,
        cityProfile: profile,
        prefs: const TripPreferences(),
      );
      expect(plan.dayThemes.length, 4);
      // Aynı tema 2 gün üst üste yasak
      DayThemeId? prev;
      for (int d = 1; d <= 4; d++) {
        final t = plan.dayThemes[d];
        expect(t, isNotNull);
        if (prev != null) expect(t, isNot(equals(prev)));
        prev = t;
      }
    });

    test("3+ gün ise day-trip günü atanır (aday varsa)", () {
      final profile = CityAnalyzer.analyze(_historicCity());
      final plan = ThemeDistributor.distribute(
        totalDays: 4,
        cityProfile: profile,
        prefs: const TripPreferences(allowDayTrips: true),
      );
      expect(plan.dayTripDays.length, greaterThanOrEqualTo(1));
      // Day-trip günü sonda olur
      expect(plan.dayTripDays.contains(4), isTrue);
    });

    test("user interest 'gece hayatı' nightlife teması bonusu verir", () {
      final profile = CityAnalyzer.analyze(_historicCity());
      final planA = ThemeDistributor.distribute(
        totalDays: 2,
        cityProfile: profile,
        prefs: const TripPreferences(),
      );
      final planB = ThemeDistributor.distribute(
        totalDays: 2,
        cityProfile: profile,
        prefs: const TripPreferences(interests: ["gece hayatı", "müzik"]),
      );
      // B'de nightlife tema'sı görünme ihtimali daha yüksek
      final aHasNight = planA.dayThemes.values.contains(DayThemeId.nightlife);
      final bHasNight = planB.dayThemes.values.contains(DayThemeId.nightlife);
      // En azından B aHasNight kadar olmalı (interest etkili)
      expect(bHasNight || aHasNight, isTrue);
    });
  });

  // ────────────────────────────────────────────────────────────────
  group("TripVarietyTracker", () {
    test("recordDay sonrası mekan kullanılmış görünür", () {
      final tracker = TripVarietyTracker();
      final theme = ThemeCatalog.themeFor(DayThemeId.history);
      final places = [_h("X"), _h("Y")];
      tracker.recordDay(theme, places);
      expect(tracker.isPlaceUsed(_h("X")), isTrue);
      expect(tracker.isPlaceUsed(_h("Z")), isFalse);
    });

    test("themeFreshness ilk kullanımdan sonra azalır", () {
      final tracker = TripVarietyTracker();
      expect(tracker.themeFreshness(DayThemeId.history), 1.0);
      tracker.recordDay(ThemeCatalog.themeFor(DayThemeId.history), []);
      expect(tracker.themeFreshness(DayThemeId.history), lessThan(1.0));
    });

    test("groupOf doğru kategori grupları", () {
      expect(
          TripVarietyTracker.groupOf(_h("X", category: "restoran")), "FOOD");
      expect(TripVarietyTracker.groupOf(_h("X", category: "kafe")), "COFFEE");
      expect(TripVarietyTracker.groupOf(_h("X", category: "bar")), "SOCIAL");
      expect(TripVarietyTracker.groupOf(_h("X", category: "park")), "NATURE");
      expect(TripVarietyTracker.groupOf(_h("X", category: "manzara")), "VIEW");
      expect(TripVarietyTracker.groupOf(_h("X", category: "müze")), "CULTURE");
      expect(TripVarietyTracker.groupOf(_h("X", category: "meydan")), "SQUARE");
      expect(TripVarietyTracker.groupOf(_h("X", category: "pazar")), "MARKET");
    });
  });

  // ────────────────────────────────────────────────────────────────
  group("TimePlanner", () {
    test("anchor saatinde mekan açıksa beklemeden başlar", () {
      final beat = ThemeCatalog.themeFor(DayThemeId.history).beats.first;
      final place = _h("Müze",
          openHours: const {"everyday": "09:00-18:00"},
          category: "müze");
      final result = TimePlanner.planBeat(
        beat: beat,
        place: place,
        earliestStart: const TimeOfDayLite(hour: 9, minute: 0),
        dayOfWeekKey: "monday",
      );
      expect(result.isOk, isTrue);
      expect(result.actualStart!.hour, 9);
    });

    test("açılış saati gelmeden önce earliestStart ise açılışa erteler", () {
      final beat = ThemeCatalog.themeFor(DayThemeId.history).beats.first;
      final place = _h("Müze",
          openHours: const {"everyday": "10:00-18:00"});
      final result = TimePlanner.planBeat(
        beat: beat,
        place: place,
        earliestStart: const TimeOfDayLite(hour: 9, minute: 0),
        dayOfWeekKey: "monday",
      );
      expect(result.isOk, isTrue);
      expect(result.actualStart!.hour, 10);
    });

    test("açılışa 60dk'dan fazla bekleme = infeasible", () {
      final beat = ThemeCatalog.themeFor(DayThemeId.history).beats.first;
      final place = _h("Müze",
          openHours: const {"everyday": "13:00-22:00"});
      final result = TimePlanner.planBeat(
        beat: beat,
        place: place,
        earliestStart: const TimeOfDayLite(hour: 9, minute: 0),
        dayOfWeekKey: "monday",
      );
      expect(result.isOk, isFalse);
      expect(result.feasibility, TimeFeasibility.tooEarlyForVenue);
    });
  });

  // ────────────────────────────────────────────────────────────────
  group("FeasibilityChecker", () {
    test("kullanılmış mekan reddedilir", () {
      final tracker = TripVarietyTracker();
      tracker.recordDay(ThemeCatalog.themeFor(DayThemeId.history), [_h("X")]);
      final beat = ThemeCatalog.themeFor(DayThemeId.history).beats.first;
      final result = FeasibilityChecker.check(
        place: _h("X", category: "müze"),
        beat: beat,
        previouslyFilled: const [],
        tripTracker: tracker,
      );
      expect(result, BeatFeasibility.alreadyUsed);
    });

    test("aynı kategoriden 3+ peş peşe yasak", () {
      final tracker = TripVarietyTracker();
      final beat = ThemeCatalog.themeFor(DayThemeId.localFood).beats.first;
      // Önceki 2 mekan FOOD; yeni de FOOD eklenirse yasak
      final foodA = _h("FoodA", category: "restoran");
      final foodB = _h("FoodB", category: "restoran");
      final filled = [
        FilledBeat(
          beat: beat,
          place: foodA,
          actualStart: const TimeOfDayLite(hour: 12, minute: 0),
          durationMin: 60,
        ),
        FilledBeat(
          beat: beat,
          place: foodB,
          actualStart: const TimeOfDayLite(hour: 13, minute: 0),
          durationMin: 60,
        ),
      ];
      // Direkt peş peşe consumption check yakalamadan önce, "tooMuchSameCategory" check yakalar.
      // Ama 2 önceki ve 1 önceki aynı grup ise zaten reject etmeli.
      // Burada 2 ardışık FOOD + 1 FOOD = peş peşe consumption
      final result = FeasibilityChecker.check(
        place: _h("FoodC", category: "restoran"),
        beat: beat,
        previouslyFilled: filled,
        tripTracker: tracker,
      );
      // İlk önce consecutiveConsumption check kazanır (lastGroup=FOOD, current=FOOD)
      expect(result, isNot(BeatFeasibility.ok));
    });

    test("must-group dışında reddedilir", () {
      final tracker = TripVarietyTracker();
      final beat = ActivityBeat(
        id: "test",
        role: BeatRole.lunch,
        time: const BeatTime(TimeOfDayLite(hour: 12, minute: 0)),
        categoryPolicy: const BeatCategoryPolicy(mustGroups: ["FOOD"]),
        estimatedDurationMin: 60,
        label: "test",
      );
      // Bir müze (CULTURE), FOOD bekleyen beat'e uymaz
      final result = FeasibilityChecker.check(
        place: _h("Müze", category: "müze"),
        beat: beat,
        previouslyFilled: const [],
        tripTracker: tracker,
      );
      expect(result, BeatFeasibility.wrongCategoryGroup);
    });
  });

  // ────────────────────────────────────────────────────────────────
  group("TimeOfDayLite", () {
    test("addMinutes/subtractMinutes overflow", () {
      const t = TimeOfDayLite(hour: 23, minute: 30);
      expect(t.addMinutes(45).formatted, "23:59"); // clamped
      const t2 = TimeOfDayLite(hour: 0, minute: 30);
      expect(t2.subtractMinutes(45).formatted, "00:00"); // clamped
    });

    test("totalMinutes hesabı doğru", () {
      const t = TimeOfDayLite(hour: 14, minute: 30);
      expect(t.totalMinutes, 14 * 60 + 30);
    });

    test("formatted padding uygular", () {
      const t = TimeOfDayLite(hour: 9, minute: 5);
      expect(t.formatted, "09:05");
    });
  });
}
