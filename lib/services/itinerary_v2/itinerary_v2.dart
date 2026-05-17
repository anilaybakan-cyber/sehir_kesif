// =============================================================================
// ITINERARY V2 - MAIN ORCHESTRATOR
// Tüm modülleri birleştirip nihai gün planını üreten servis.
//
// Akış:
//   1. CityModel yükle
//   2. CityAnalyzer ile şehir profili çıkar
//   3. User preferences oku
//   4. ThemeDistributor ile günlere tema ata
//   5. Her gün için:
//      - Anchor seç (gün cluster'ının merkezi)
//      - Cluster oluştur (yakındaki mekanlar)
//      - Tema beat'lerini sırayla doldur (BeatFiller)
//      - FilledBeat'leri eski JSON formatına dönüştür
//   6. Schedule'ı döndür
// =============================================================================

import 'dart:math' as math;
import 'package:collection/collection.dart';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../debug/agent_ndjson_log.dart';
import '../../models/city_model.dart';
import '../city_data_loader.dart';
import '../plan_repository.dart';
import '../travel_time_estimator.dart';
import '../trip_update_service.dart';
import 'beat.dart';
import 'beat_filler.dart';
import 'city_analyzer.dart';
import 'day_theme.dart';
import 'theme_catalog.dart';
import 'theme_distributor.dart';
import 'variety_tracker.dart';

Map<String, int> _groupHistogramFromFilled(List<FilledBeat> beats) {
  final m = <String, int>{};
  for (final f in beats) {
    final g = TripVarietyTracker.groupOf(f.place);
    m[g] = (m[g] ?? 0) + 1;
  }
  return m;
}

/// Aynı mekanın farklı isimlerle (ör. "Santiago Bernabéu" vs
/// "Estadio Santiago Bernabéu") iki kez eklenmesini engellemek için
/// id öncelikli, isim normalize edilmiş karşılaştırma anahtarı.
String _placeKey(Highlight h) {
  final id = h.id?.trim();
  if (id != null && id.isNotEmpty) return 'id:$id';
  final slug = h.name
      .toLowerCase()
      .trim()
      .replaceAll(RegExp(r'[^a-z0-9]'), '');
  return 'name:$slug';
}

bool _alreadyFilled(List<FilledBeat> filled, Highlight h) {
  final key = _placeKey(h);
  for (final f in filled) {
    if (_placeKey(f.place) == key) return true;
  }
  return false;
}

class ItineraryV2 {
  /// Ana entry point - eski SmartItineraryBuilder.generateAndSavePlan ile uyumlu.
  static Future<void> generateAndSavePlan(String cityId, int totalDays) async {
    try {
      final schedule = await generatePlan(cityId, totalDays);
      if (schedule != null) {
        await savePlan(cityId, schedule);
      }
    } catch (e, st) {
      debugPrint("❌ ItineraryV2 generateAndSave error: $e\n$st");
    }
  }

  static Future<void> savePlan(
      String cityId, Map<String, dynamic> schedule) async {
    final normalized = cityId.toLowerCase();
    await PlanRepository.saveSchedule(normalized, schedule);
    await PlanRepository.markPlanCreated(normalized, isAiPlan: true);
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool("has_migrated_to_per_city", true);
    TripUpdateService().notifyTripChanged();
    debugPrint("✅ ItineraryV2 plan saved for $normalized.");
  }

  /// Plan üret - schedule döndür (kaydetmeden).
  static Future<Map<String, dynamic>?> generatePlan(
      String cityId, int totalDays) async {
    try {
      // 1. Veriyi yükle
      final cityData = await CityDataLoader.loadCity(cityId);
      final allHighlights = List<Highlight>.from(cityData.highlights);
      if (allHighlights.isEmpty) {
        debugPrint("⚠️ ItineraryV2: No highlights for $cityId");
        return null;
      }

      // 2. Şehir profili
      final profile = CityAnalyzer.analyze(allHighlights);
      debugPrint(
          "📊 ItineraryV2 city profile: ${profile.totalCityPlaces} places, "
          "day-trip:${profile.dayTripCandidates}, top theme:${profile.rankedThemes.firstOrNull?.nameTr}");

      // 3. Tercihler
      final prefs = await SharedPreferences.getInstance();
      final tripPrefs = TripPreferences(
        interests: (prefs.getStringList("interests") ?? [])
            .map((e) => e.toLowerCase())
            .toList(),
        travelStyle: _mapTravelStyle(prefs.getString("travelStyle")),
        budgetLevel: _mapBudgetLevel(prefs.getString("budgetLevel")),
      );

      // 4. Tema dağıtımı
      final themePlan = ThemeDistributor.distribute(
        totalDays: totalDays,
        cityProfile: profile,
        prefs: tripPrefs,
      );
      debugPrint("🎨 ItineraryV2 theme plan: ${themePlan.dayThemeNames}");

      // 5. Trip variety tracker
      final tripTracker = TripVarietyTracker();

      // 6. Must-see icon havuzu
      final mustSeeIcons = _selectMustSeeIcons(allHighlights, totalDays);

      // 7. Day-trip aday havuzu
      final dayTripCandidates =
          allHighlights.where((h) => h.isDayTrip).toList();
      _sortByPrestige(dayTripCandidates);

      // 8. Şehir-içi havuz
      final cityPool = allHighlights.where((h) => !h.isDayTrip).toList();
      _sortByPrestige(cityPool);

      // 9. Her gün için plan üret
      final Map<String, dynamic> schedule = {};
      final rng = math.Random(); // Her seferinde taze sonuç için seed kaldırıldı

      // Day-trip atamalarını hazırla
      final dayTripAssignments = <int, Highlight>{};
      _assignDayTrips(
        themePlan: themePlan,
        candidates: dayTripCandidates,
        assignments: dayTripAssignments,
      );

      // Anchor atamaları (regular günler için)
      final anchorAssignments = <int, Highlight>{};
      _assignAnchors(
        themePlan: themePlan,
        cityPool: cityPool,
        mustSeeIcons: mustSeeIcons,
        assignments: anchorAssignments,
      );

      for (int day = 1; day <= totalDays; day++) {
        final themeId = themePlan.dayThemes[day];
        if (themeId == null) continue;
        final dayKey = _dayKeyForTripDay(day);

        final theme = ThemeCatalog.themeFor(themeId);
        debugPrint(
            "🗓️ ItineraryV2 building day $day - ${themeId.nameTr}");

        List<Map<String, dynamic>> dayJson;

        if (themeId == DayThemeId.dayTrip) {
          // Day-trip günü
          final dt = dayTripAssignments[day];
          if (dt == null) {
            // Day-trip aday yoksa boş gün
            agentNdjsonLog(
              hypothesisId: 'H5',
              location: 'itinerary_v2.dart:generatePlan',
              message: 'day_trip_skipped_no_candidate',
              data: {'dayIndex': day, 'theme': themeId.name},
            );
            schedule[day.toString()] = <Map<String, dynamic>>[];
            continue;
          }
          dayJson = _buildDayTripDay(
            theme: theme,
            dayTripPlace: dt,
            cityPool: cityPool,
            tripTracker: tripTracker,
            mustSeeIcons: mustSeeIcons,
            tripPrefs: tripPrefs,
            rng: rng,
            cityId: cityId,
            dayOfWeekKey: dayKey,
            dayIndex: day,
          );
        } else {
          // Regular gün
          final anchor = anchorAssignments[day];
          dayJson = _buildRegularDay(
            theme: theme,
            anchor: anchor,
            cityPool: cityPool,
            tripTracker: tripTracker,
            mustSeeIcons: mustSeeIcons,
            tripPrefs: tripPrefs,
            rng: rng,
            cityId: cityId,
            dayOfWeekKey: dayKey,
            dayIndex: day,
          );
        }

        schedule[day.toString()] = dayJson;
      }

      agentNdjsonLog(
        hypothesisId: 'H3',
        location: 'itinerary_v2.dart:generatePlan',
        message: 'schedule_summary',
        data: {
          'cityId': cityId,
          'totalDays': totalDays,
          'source': 'ItineraryV2.generatePlan',
          'days': schedule.keys.map((k) {
            final list = schedule[k] as List<dynamic>? ?? [];
            final names = list
                .map((e) => (e as Map)['name']?.toString() ?? '')
                .where((n) => n.isNotEmpty)
                .toList();
            final cats = list
                .map((e) => (e as Map)['category']?.toString() ?? '')
                .toList();
            return {
              'day': k,
              'count': list.length,
              'names': names,
              'categories': cats,
            };
          }).toList(),
        },
      );

      return schedule;
    } catch (e, st) {
      debugPrint("❌ ItineraryV2 generatePlan error: $e\n$st");
      return null;
    }
  }

  // ─────────────────────────────────────────────────────────────────
  // DAY BUILDING - REGULAR
  // ─────────────────────────────────────────────────────────────────

  static List<Map<String, dynamic>> _buildRegularDay({
    required DayTheme theme,
    required Highlight? anchor,
    required List<Highlight> cityPool,
    required TripVarietyTracker tripTracker,
    required Set<String> mustSeeIcons,
    required TripPreferences tripPrefs,
    required math.Random rng,
    required String cityId,
    required String dayOfWeekKey,
    required int dayIndex,
  }) {
    // Cluster oluştur - anchor merkezli (radius artırıldı: 4km → 8km)
    final cluster = _buildCluster(anchor, cityPool, radiusKm: 8.0);
    if (cluster.isEmpty) return [];

    // Beat'leri sırayla doldur
    final filled = <FilledBeat>[];
    Highlight? prevPlace;
    TimeOfDayLite earliestStart = theme.preferredStart;
    int beatOk = 0;
    int beatFail = 0;

    for (final beat in theme.beats) {
      // KURAL: Eğer günün bir Anchor'ı varsa ve bu bir MUST-SEE ise,
      // Icon beat'ini zorla bu anchor ile doldur.
      if (beat.role == BeatRole.icon &&
          anchor != null &&
          mustSeeIcons.contains(anchor.name)) {
        final forceFill = BeatFiller.fillBeat(
          beat: beat,
          candidatePool: [anchor],
          previouslyFilled: filled,
          tripTracker: tripTracker,
          prevPlace: prevPlace,
          earliestStart: earliestStart,
          dayKey: dayOfWeekKey,
          dayAnchor: anchor,
          mustSeeIcons: mustSeeIcons,
          prefs: tripPrefs,
          rng: rng,
          forceInclude: true,
        );
        if (forceFill != null) {
          filled.add(forceFill);
          prevPlace = forceFill.place;
          earliestStart = forceFill.actualEnd.addMinutes(5);
          beatOk++;
          continue;
        }
      }

      final candidatePool = cluster
          .where((h) => !tripTracker.isPlaceUsed(h))
          .where((h) => !_alreadyFilled(filled, h))
          .toList();

      FilledBeat? result = BeatFiller.fillBeat(
        beat: beat,
        candidatePool: candidatePool,
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: prevPlace,
        earliestStart: earliestStart,
        dayKey: dayOfWeekKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );

      if (result == null) {
        if (!beat.isOptional) {
          // Required beat dolmadıysa, mustGroups'u gevşetip bir kez daha dene.
          final relaxedBeat = ActivityBeat(
            id: "${beat.id}_relaxed",
            role: beat.role,
            time: beat.time,
            categoryPolicy: BeatCategoryPolicy(
              mustGroups: const [],
              preferGroups: [
                ...beat.categoryPolicy.mustGroups,
                ...beat.categoryPolicy.preferGroups,
              ],
              preferKeywords: beat.categoryPolicy.preferKeywords,
            ),
            estimatedDurationMin: beat.estimatedDurationMin,
            label: "${beat.label} (relaxed)",
            isOptional: beat.isOptional,
          );

          result = BeatFiller.fillBeat(
            beat: relaxedBeat,
            candidatePool: candidatePool,
            previouslyFilled: filled,
            tripTracker: tripTracker,
            prevPlace: prevPlace,
            earliestStart: earliestStart,
            dayKey: dayOfWeekKey,
            dayAnchor: anchor,
            mustSeeIcons: mustSeeIcons,
            prefs: tripPrefs,
            rng: rng,
          );
        }

        if (result == null && !beat.isOptional) {
          debugPrint(
              "⚠️ ItineraryV2: required beat ${beat.id} couldn't be filled");
        }
      }
      if (result == null) {
        beatFail++;
        continue;
      }

      filled.add(result);
      beatOk++;
      prevPlace = result.place;
      // Bir sonraki beat için earliestStart = bu beat'in bitişi + minimum 5 dk yürüyüş buffer
      earliestStart = result.actualEnd.addMinutes(5);
    }

    agentNdjsonLog(
      hypothesisId: 'H1',
      location: 'itinerary_v2.dart:_buildRegularDay',
      message: 'after_beat_loop',
      data: {
        'dayIndex': dayIndex,
        'theme': theme.id.name,
        'dayKey': dayOfWeekKey,
        'anchor': anchor?.name,
        'clusterSize': cluster.length,
        'filledAfterBeats': filled.length,
        'beatOk': beatOk,
        'beatFail': beatFail,
        'histogram': _groupHistogramFromFilled(filled),
      },
    );

    // Gün kalite kapısı:
    // - En az 6 durak
    // - En az 1 non-consumption (CULTURE/NATURE/VIEW/...)
    _applyDayQualityGate(
      theme: theme,
      anchor: anchor,
      cluster: cluster,
      cityPool: cityPool,
      filled: filled,
      tripTracker: tripTracker,
      mustSeeIcons: mustSeeIcons,
      tripPrefs: tripPrefs,
      rng: rng,
      dayKey: dayOfWeekKey,
      minPlaces: _minRegularDayPlaces,
      requireExperience: true,
      dayIndex: dayIndex,
    );

    agentNdjsonLog(
      hypothesisId: 'H2',
      location: 'itinerary_v2.dart:_buildRegularDay',
      message: 'after_quality_gate',
      data: {
        'dayIndex': dayIndex,
        'theme': theme.id.name,
        'filledFinal': filled.length,
        'histogram': _groupHistogramFromFilled(filled),
      },
    );

    // KURAL 8: Coğrafi A→B→C→D sıralaması (nearest-neighbor)
    // Yemek slotlarını sabitleyip, aradaki deneyimleri coğrafi olarak optimize et.
    _applyGeographicSort(filled, dayIndex <= 0 ? "monday" : _dayKeyForTripDay(dayIndex));

    // Gün başına tavan: fazla mekan varsa transition/optional olanlardan başla.
    _trimToMaxPlaces(filled, _maxRegularDayPlaces);

    // Bar / gece yerlerini akşam yemeğinden sonraya it (kronoloji kuralı):
    // bir bar günün ortasındaki bir müzeden önce gelmemeli.
    _pushSocialToEvening(filled);

    // Saatler her durumda ileri akmalı (geo-sort + trim + insert sonrası).
    _enforceMonotonicSchedule(filled, _dayKeyForTripDay(dayIndex));

    // Trip tracker'a kaydet
    tripTracker.recordDay(theme, filled.map((f) => f.place).toList());

    // JSON'a çevir
    return filled.map((f) => _filledBeatToJson(f, cityId)).toList();
  }

  // ─────────────────────────────────────────────────────────────────
  // DAY BUILDING - DAY TRIP
  // ─────────────────────────────────────────────────────────────────

  static List<Map<String, dynamic>> _buildDayTripDay({
    required DayTheme theme,
    required Highlight dayTripPlace,
    required List<Highlight> cityPool,
    required TripVarietyTracker tripTracker,
    required Set<String> mustSeeIcons,
    required TripPreferences tripPrefs,
    required math.Random rng,
    required String cityId,
    required String dayOfWeekKey,
    required int dayIndex,
  }) {
    final filled = <FilledBeat>[];
    Highlight? prevPlace;
    TimeOfDayLite earliestStart = theme.preferredStart;
    // Day-trip teması beat'leri:
    // 1. morning_coffee (cityPool'dan)
    // 2. day_trip_main (dayTripPlace SABİT)
    // 3. return_break (cityPool'dan, opsiyonel)
    // 4. city_dinner (cityPool'dan)

    for (final beat in theme.beats) {
      if (beat.role == BeatRole.dayTripMain) {
        // Day-trip ana mekanı sabit
        final timing = TimeOfDayLite.fromMinutes(beat.time.anchor.totalMinutes);
        filled.add(FilledBeat(
          beat: beat,
          place: dayTripPlace,
          actualStart: timing,
          durationMin: dayTripPlace.dayTripDurationMinutes,
        ));
        prevPlace = null; // Day trip dönüşü saatleri sıfırlanır
        earliestStart = TimeOfDayLite.fromMinutes(
            timing.totalMinutes + dayTripPlace.dayTripDurationMinutes);
        continue;
      }

      // Diğer beat'ler şehir içi mekanlardan
      final candidatePool = cityPool
          .where((h) => !tripTracker.isPlaceUsed(h))
          .where((h) => !_alreadyFilled(filled, h))
          .toList();

      final result = BeatFiller.fillBeat(
        beat: beat,
        candidatePool: candidatePool,
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: prevPlace,
        earliestStart: earliestStart,
        dayKey: dayOfWeekKey,
        dayAnchor: null,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );

      if (result == null) continue;

      filled.add(result);
      prevPlace = result.place;
      earliestStart = result.actualEnd.addMinutes(5);
    }

    // Day-trip günlerinde de en az 4 durak hedeflenir.
    _applyDayQualityGate(
      theme: theme,
      anchor: null,
      cluster: cityPool,
      cityPool: cityPool,
      filled: filled,
      tripTracker: tripTracker,
      mustSeeIcons: mustSeeIcons,
      tripPrefs: tripPrefs,
      rng: rng,
      dayKey: dayOfWeekKey,
      minPlaces: _minDayTripPlaces,
      requireExperience: false,
      dayIndex: dayIndex,
    );

    agentNdjsonLog(
      hypothesisId: 'H5',
      location: 'itinerary_v2.dart:_buildDayTripDay',
      message: 'day_trip_built',
      data: {
        'dayIndex': dayIndex,
        'dayTrip': dayTripPlace.name,
        'filledFinal': filled.length,
        'histogram': _groupHistogramFromFilled(filled),
      },
    );

    // Day-trip günü ana mekan + 4 şehir-içi durak yeterli.
    _trimToMaxPlaces(filled, _maxDayTripPlaces, protectDayTrip: true);
    _pushSocialToEvening(filled);
    _enforceMonotonicSchedule(filled, dayOfWeekKey);

    tripTracker.recordDay(theme, filled.map((f) => f.place).toList());

    return filled.map((f) => _filledBeatToJson(f, cityId)).toList();
  }

  // ─────────────────────────────────────────────────────────────────
  // DAY QUALITY GATE
  // ─────────────────────────────────────────────────────────────────
  static const int _minRegularDayPlaces = 6;
  static const int _minDayTripPlaces = 4;
  // Gün başına gerçekçi tavan. Yemek + 3-4 deneyim + 1 mola: ~7 durak.
  // Day-trip günlerinde ana mekan zaten uzun süreli olduğu için daha az.
  static const int _maxRegularDayPlaces = 7;
  static const int _maxDayTripPlaces = 5;
  static const Set<String> _consumptionGroups = {"FOOD", "COFFEE", "SOCIAL"};
  static const Set<String> _experienceGroups = {
    "CULTURE",
    "NATURE",
    "VIEW",
    "SQUARE",
    "MARKET",
  };

  static void _applyDayQualityGate({
    required DayTheme theme,
    required Highlight? anchor,
    required List<Highlight> cluster,
    required List<Highlight> cityPool,
    required List<FilledBeat> filled,
    required TripVarietyTracker tripTracker,
    required Set<String> mustSeeIcons,
    required TripPreferences tripPrefs,
    required math.Random rng,
    required String dayKey,
    required int minPlaces,
    required bool requireExperience,
    required int dayIndex,
  }) {
    final startLen = filled.length;
    final startHist = _groupHistogramFromFilled(filled);

    // KURAL 2: Deneyim sayacı (min 3 hedef)
    int experienceCount() => filled
        .where((f) => _experienceGroups.contains(TripVarietyTracker.groupOf(f.place)))
        .length;
    bool hasEnoughExperience() => experienceCount() >= 3;
    // KURAL 5: Consumption sayacı (max 3 hedef)
    int consumptionCount() => filled
        .where((f) => _consumptionGroups.contains(TripVarietyTracker.groupOf(f.place)))
        .length;
    // KURAL 5: Günde maksimum 3 yeme-içme
    int maxConsumptionAllowed(int total) => 3;

    TimeOfDayLite currentEarliest() {
      if (filled.isEmpty) return theme.preferredStart;
      return filled.last.actualEnd.addMinutes(5);
    }

    Highlight? currentPrev() => filled.isEmpty ? null : filled.last.place;

    List<Highlight> buildCandidatePool() {
      final merged = [...cluster, ...cityPool];
      final seen = <String>{};
      return merged
          .where((h) => !h.isDayTrip)
          .where((h) => !tripTracker.isPlaceUsed(h))
          .where((h) => !_alreadyFilled(filled, h))
          // Aynı havuzda da duplicate'leri tek geçir
          .where((h) => seen.add(_placeKey(h)))
          .toList();
    }

    FilledBeat? tryFillWithGroups({
      required List<String> mustGroups,
      required List<String> preferGroups,
      required String idSuffix,
      int toleranceMin = 180,
    }) {
      final beat = ActivityBeat(
        id: "quality_fill_$idSuffix",
        role: BeatRole.transition,
        time: BeatTime(currentEarliest(), toleranceMin: toleranceMin),
        categoryPolicy: BeatCategoryPolicy(
          mustGroups: mustGroups,
          preferGroups: preferGroups,
        ),
        estimatedDurationMin: 60,
        label: "Quality fill",
      );

      return BeatFiller.fillBeat(
        beat: beat,
        candidatePool: buildCandidatePool(),
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: currentPrev(),
        earliestStart: currentEarliest(),
        dayKey: dayKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );
    }

    FilledBeat? replaceOneConsumptionWithExperience() {
      if (filled.isEmpty) return null;
      final candidatePool = buildCandidatePool()
          .where((h) => _experienceGroups.contains(TripVarietyTracker.groupOf(h)))
          .toList();
      if (candidatePool.isEmpty) return null;

      int replaceIdx = -1;
      for (int i = filled.length - 1; i >= 0; i--) {
        final group = TripVarietyTracker.groupOf(filled[i].place);
        if (_consumptionGroups.contains(group)) {
          replaceIdx = i;
          break;
        }
      }
      if (replaceIdx < 0) return null;

      final prev = replaceIdx > 0 ? filled[replaceIdx - 1].place : anchor;
      candidatePool.sort((a, b) {
        double da = 0;
        double db = 0;
        if (prev != null) {
          da = TravelTimeEstimator.haversine(prev.lat, prev.lng, a.lat, a.lng);
          db = TravelTimeEstimator.haversine(prev.lat, prev.lng, b.lat, b.lng);
        }
        final sa = (a.rating ?? 4.0) * 10 - da;
        final sb = (b.rating ?? 4.0) * 10 - db;
        return sb.compareTo(sa);
      });

      final replacement = candidatePool.first;
      final current = filled[replaceIdx];
      final replaced = FilledBeat(
        beat: current.beat,
        place: replacement,
        actualStart: current.actualStart,
        durationMin: current.durationMin,
        transitMinFromPrev: current.transitMinFromPrev,
        transitDistKm: current.transitDistKm,
      );
      filled[replaceIdx] = replaced;
      return replaced;
    }

    // 1) KURAL 2: En az 3 deneyim durağı olmadan devam etme.
    int expFillAttempts = 0;
    while (requireExperience && experienceCount() < 3 && expFillAttempts < 5) {
      expFillAttempts++;
      final experienceFill = tryFillWithGroups(
        mustGroups: _experienceGroups.toList(),
        preferGroups: _experienceGroups.toList(),
        idSuffix: "experience_${expFillAttempts}",
      );
      if (experienceFill != null) {
        filled.add(experienceFill);
      } else {
        break;
      }
    }

    // 2) Minimum durak sayısını garanti et.
    int safetyCounter = 0;
    while (filled.length < minPlaces && safetyCounter < 12) {
      safetyCounter++;
      final lastGroup = filled.isNotEmpty
          ? TripVarietyTracker.groupOf(filled.last.place)
          : "ANY";

      // KURAL: Peş peşe 3 consumption ekleme
      if (filled.length >= 2) {
        final last1 = TripVarietyTracker.groupOf(filled.last.place);
        final last2 = TripVarietyTracker.groupOf(filled[filled.length - 2].place);
        if (_consumptionGroups.contains(last1) &&
            _consumptionGroups.contains(last2)) {
          // Son 2 consumption, bu yüzden consumption eklemeyi yasakla
          final preferExperience = _consumptionGroups.contains(lastGroup) ||
              (requireExperience && !hasEnoughExperience());
          final strictGroups = preferExperience
              ? _experienceGroups.toList()
              : _experienceGroups.toList(); // Consumption değil, experience zorla

          FilledBeat? fill = tryFillWithGroups(
            mustGroups: strictGroups,
            preferGroups: strictGroups,
            idSuffix: "${filled.length}_strict_no_consumption",
          );

          fill ??= tryFillWithGroups(
            mustGroups: const [],
            preferGroups: strictGroups,
            idSuffix: "${filled.length}_relaxed_no_consumption",
          );

          fill ??= tryFillWithGroups(
            mustGroups: const [],
            preferGroups: const [],
            idSuffix: "${filled.length}_any_no_consumption",
            toleranceMin: 300,
          );

          if (fill == null) break;
          filled.add(fill);
          continue;
        }
      }

      final preferExperience = _consumptionGroups.contains(lastGroup) ||
          (requireExperience && !hasEnoughExperience());
      final strictGroups = preferExperience
          ? _experienceGroups.toList()
          : _consumptionGroups.toList();

      FilledBeat? fill = tryFillWithGroups(
        mustGroups: strictGroups,
        preferGroups: strictGroups,
        idSuffix: "${filled.length}_strict",
      );

      fill ??= tryFillWithGroups(
        mustGroups: const [],
        preferGroups: strictGroups,
        idSuffix: "${filled.length}_relaxed",
      );

      // Son çare: tamamen serbest, herhangi bir mekan
      fill ??= tryFillWithGroups(
        mustGroups: const [],
        preferGroups: const [],
        idSuffix: "${filled.length}_any",
        toleranceMin: 300,
      );

      if (fill == null) break;
      filled.add(fill);
    }

    // 3) Yeme-içme baskınlığını kır.
    // Önce fazla consumption'ı deneyim ile DEĞİŞTİR (replace). Replace adayı
    // yoksa fazlalığı sil. Yeni deneyim eklemek consumption sayısını
    // azaltmadığı için burada `add` YAPMA — aksi hâlde döngü sonsuza yakın
    // mekan ekler ve gün başına 13 mekan çıkar.
    int mixFixCounter = 0;
    while (consumptionCount() > maxConsumptionAllowed(filled.length) &&
        mixFixCounter < 6) {
      mixFixCounter++;
      final replaced = replaceOneConsumptionWithExperience();
      if (replaced != null) continue;

      // Replace adayı yoksa fazla consumption'ı sil.
      bool removed = false;
      for (int i = filled.length - 1; i >= 0; i--) {
        if (_consumptionGroups.contains(TripVarietyTracker.groupOf(filled[i].place))) {
          filled.removeAt(i);
          removed = true;
          break;
        }
      }
      if (!removed) break;
    }

    // 4) Akşam yemeği garantisi: Dinner yoksa zorla ekle.
    final hasDinner = filled.any((f) =>
        f.beat.role == BeatRole.dinner ||
        (TripVarietyTracker.groupOf(f.place) == "FOOD" &&
            f.actualStart.hour >= 19));
    if (!hasDinner) {
      final dinnerBeat = _createGuaranteedDinnerBeat();
      final dinnerFill = BeatFiller.fillBeat(
        beat: dinnerBeat,
        candidatePool: buildCandidatePool(),
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: currentPrev(),
        earliestStart: filled.isNotEmpty
            ? filled.last.actualEnd.addMinutes(5)
            : const TimeOfDayLite(hour: 19, minute: 0),
        dayKey: dayKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );
      if (dinnerFill != null) filled.add(dinnerFill);
    }

    // 5) Akşam sonrası deneyim: Yemek sonrası meydan/manzara/gece yürüyüşü
    final lastBeat = filled.isNotEmpty ? filled.last : null;
    final lastHour = lastBeat?.actualEnd.hour ?? 0;
    if (lastHour >= 20 && lastHour < 23) {
      final lateCultureBeat = ActivityBeat(
        id: "late_experience",
        role: BeatRole.transition,
        time: BeatTime(
          lastBeat!.actualEnd.addMinutes(10),
          toleranceMin: 90,
        ),
        categoryPolicy: const BeatCategoryPolicy(
          preferGroups: ["SQUARE", "VIEW", "CULTURE"],
          preferKeywords: ["meydan", "manzara", "gece", "köprü", "rıhtım", "aydınlatılmış"],
        ),
        estimatedDurationMin: 45,
        label: "Akşam deneyimi",
        isOptional: true,
      );
      final lateFill = BeatFiller.fillBeat(
        beat: lateCultureBeat,
        candidatePool: buildCandidatePool()
            .where((h) => _experienceGroups.contains(TripVarietyTracker.groupOf(h)))
            .toList(),
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: currentPrev(),
        earliestStart: lastBeat.actualEnd.addMinutes(5),
        dayKey: dayKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );
      if (lateFill != null) filled.add(lateFill);
    }

    // 6) BOŞLUK DOLDURMA (Gap Filling):
    // Mekanlar arasında 300 dk'dan fazla boşluk varsa araya bir deneyim sıkıştır.
    int gapSafety = 0;
    while (gapSafety < 5) {
      gapSafety++;
      int? gapIdx;
      for (int i = 0; i < filled.length - 1; i++) {
        final end = filled[i].actualEnd;
        final start = filled[i + 1].actualStart;
        if (start.totalMinutes - end.totalMinutes > 300) {
          gapIdx = i;
          break;
        }
      }

      if (gapIdx == null) break; // Boşluk kalmadı

      final gapStart = filled[gapIdx].actualEnd.addMinutes(5);
      final gapEnd = filled[gapIdx + 1].actualStart.subtractMinutes(5);
      final availableMin = gapEnd.totalMinutes - gapStart.totalMinutes;

      final gapBeat = ActivityBeat(
        id: "gap_filler_${gapIdx}",
        role: BeatRole.transition,
        time: BeatTime(gapStart, toleranceMin: 15),
        categoryPolicy: const BeatCategoryPolicy(
          preferGroups: ["CULTURE", "SQUARE", "VIEW", "NATURE"],
          preferKeywords: ["müze", "meydan", "park", "yürüyüş", "manzara"],
        ),
        estimatedDurationMin: (availableMin * 0.7).ceil().toInt().clamp(30, 90),
        label: "Ara durak (boşluk doldurma)",
      );

      final gapFill = BeatFiller.fillBeat(
        beat: gapBeat,
        candidatePool: buildCandidatePool(),
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: filled[gapIdx].place,
        earliestStart: gapStart,
        dayKey: dayKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );

      if (gapFill != null) {
        filled.insert(gapIdx + 1, gapFill);
      } else {
        // Bu boşluk dolmuyor, pas geçmek için bir işaret koyamayız ama loop'u kırmalıyız
        // çünkü aynı boşluk için tekrar deneyecek.
        break;
      }
    }

    agentNdjsonLog(
      hypothesisId: 'H2',
      location: 'itinerary_v2.dart:_applyDayQualityGate',
      message: 'quality_gate_done',
      data: {
        'dayIndex': dayIndex,
        'theme': theme.id.name,
        'dayKey': dayKey,
        'minPlaces': minPlaces,
        'requireExperience': requireExperience,
        'startLen': startLen,
        'endLen': filled.length,
        'startHist': startHist,
        'endHist': _groupHistogramFromFilled(filled),
        'candidatePoolSize': () {
          final merged = [...cluster, ...cityPool];
          return merged
              .where((h) => !h.isDayTrip)
              .where((h) => !tripTracker.isPlaceUsed(h))
              .where((h) => !_alreadyFilled(filled, h))
              .length;
        }(),
      },
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // POST-PROCESS: TRIM + MONOTONIC TIME GUARD
  // ─────────────────────────────────────────────────────────────────

  /// Günü `maxPlaces` mekana indirir. Önce optional/transition rolündekileri,
  /// sonra ortadaki "ekstra" duraklari kırpar; yemek slotları (lunch/dinner)
  /// ve `protectDayTrip` true ise day-trip ana mekanı korunur.
  static void _trimToMaxPlaces(
    List<FilledBeat> filled,
    int maxPlaces, {
    bool protectDayTrip = false,
  }) {
    if (filled.length <= maxPlaces) return;

    bool isProtected(FilledBeat f) {
      if (f.beat.role == BeatRole.lunch) return true;
      if (f.beat.role == BeatRole.dinner) return true;
      if (protectDayTrip && f.beat.role == BeatRole.dayTripMain) return true;
      return false;
    }

    // 1) Optional veya transition rolündeki en sondaki kırpılabilir item'i bul
    while (filled.length > maxPlaces) {
      int idx = -1;
      for (int i = filled.length - 1; i >= 0; i--) {
        final f = filled[i];
        if (isProtected(f)) continue;
        if (f.beat.isOptional || f.beat.role == BeatRole.transition) {
          idx = i;
          break;
        }
      }
      if (idx < 0) break;
      filled.removeAt(idx);
    }

    // 2) Hâlâ fazlaysa, korunmayan herhangi bir item'i (en sondan) sil.
    while (filled.length > maxPlaces) {
      int idx = -1;
      for (int i = filled.length - 1; i >= 0; i--) {
        if (!isProtected(filled[i])) {
          idx = i;
          break;
        }
      }
      if (idx < 0) break; // Sadece korunan mekanlar kaldı; daha fazla kırpma.
      filled.removeAt(idx);
    }
  }

  /// Bar/gece (SOCIAL) yerleri için en erken makul başlangıç saati.
  /// Daha erken bir slot'a (örn. öğleden sonra) kaymalarını engeller.
  static const TimeOfDayLite _earliestSocialStart =
      TimeOfDayLite(hour: 20, minute: 0);

  /// Bar / gece (SOCIAL) yerlerini günün en sonuna iter. Algoritma müzeden
  /// önce bir bar planlayabiliyor; bu kronolojik açıdan kötü bir UX, ayrıca
  /// barlar genelde 19:00+ açılır ve müzeler 19:30 civarında kapanır.
  static void _pushSocialToEvening(List<FilledBeat> filled) {
    if (filled.length < 2) return;

    // Tüm SOCIAL item'ları sıralarını koruyarak çek.
    final socials = <FilledBeat>[];
    for (int i = filled.length - 1; i >= 0; i--) {
      final f = filled[i];
      if (TripVarietyTracker.groupOf(f.place) == "SOCIAL") {
        socials.insert(0, f);
        filled.removeAt(i);
      }
    }
    if (socials.isEmpty) return;

    // Sona ekle ve hâlâ erken bir saatte ise minimum akşam saatine çek.
    // Monotonic guard ardından önceki bitiş + 5 dk ile çakışmayı çözer.
    for (final s in socials) {
      final adjusted = s.actualStart.totalMinutes <
              _earliestSocialStart.totalMinutes
          ? s.copyWith(actualStart: _earliestSocialStart)
          : s;
      filled.add(adjusted);
    }
  }

  /// Saatlerin asla geriye gitmediğini garanti eder ve kapanış saatlerine
  /// uyduğunu kontrol eder. Geo-sort, gap-fill, trim ve sosyal-itme sonrası
  /// listede olası "geriye dönüş"leri ve "kapalı yere atama"yı düzeltir.
  static void _enforceMonotonicSchedule(
    List<FilledBeat> filled, [
    String? dayKey,
  ]) {
    if (filled.length < 2) return;

    for (int i = 1; i < filled.length; i++) {
      final prevEnd = filled[i - 1].actualEnd;
      final cur = filled[i];

      // 1) Saat asla geriye gitmesin (en az 5 dk buffer).
      if (cur.actualStart.totalMinutes < prevEnd.totalMinutes) {
        filled[i] = cur.copyWith(actualStart: prevEnd.addMinutes(5));
      }

      // 2) Kapanış saati ihlali: bu mekan, ileri kaydırılan saatte kapalıysa
      //    süreyi sığacak şekilde kısalt; sığmıyorsa mekanı listeden çıkar.
      if (dayKey != null) {
        final f = filled[i];
        final closeMin = f.place.getClosingMinutes(dayKey);
        if (closeMin >= 0) {
          final endMin = f.actualEnd.totalMinutes;
          if (endMin > closeMin) {
            final available = closeMin - f.actualStart.totalMinutes;
            if (available >= 30) {
              // Mekan için en az 30 dk kalıyorsa süreyi kısalt.
              filled[i] = f.copyWith(durationMin: available);
            } else {
              // Hiç sığmıyor; mekanı kaldır.
              filled.removeAt(i);
              i--;
            }
          }
        }
      }
    }
  }

  static String _dayKeyForTripDay(int day) {
    const keys = [
      "monday",
      "tuesday",
      "wednesday",
      "thursday",
      "friday",
      "saturday",
      "sunday",
    ];
    final idx = (day - 1) % keys.length;
    return keys[idx];
  }
  // ─────────────────────────────────────────────────────────────────
  // KURAL 8: COĞRAFİ OPTİMİZASYON (A→B→C→D)
  // ─────────────────────────────────────────────────────────────────

  /// Günün doldurulan beat'lerini coğrafi olarak optimize eder.
  /// Yemek slotlarını (kahvaltı, öğle, akşam) sabit zaman noktaları olarak
  /// koruyup, aradaki deneyim/kültür duraklarını nearest-neighbor ile sıralar.
  static void _applyGeographicSort(List<FilledBeat> filled, String dayKey) {
    if (filled.length <= 3) return; // Çok az durak varsa sıralama gereksiz

    // Segmentlere böl: yemek slotları sabit tutulacak.
    // Yemek = lunch veya dinner role, ya da FOOD group saat 12-15 veya 19+
    bool isMealPin(FilledBeat f) {
      if (f.beat.role == BeatRole.lunch || f.beat.role == BeatRole.dinner) {
        return true;
      }
      // Sabah kahvaltı slotu (ilk beat ve consumption ise)
      if (f == filled.first &&
          _consumptionGroups.contains(TripVarietyTracker.groupOf(f.place))) {
        return true;
      }
      return false;
    }

    // Segmentler oluştur: meal→meal arası gruplara böl
    final segments = <List<FilledBeat>>[];
    var currentSeg = <FilledBeat>[];

    for (final f in filled) {
      if (isMealPin(f) && currentSeg.isNotEmpty) {
        segments.add(currentSeg);
        currentSeg = <FilledBeat>[f]; // Yemeği yeni segmentin başına koy
      } else {
        currentSeg.add(f);
      }
    }
    if (currentSeg.isNotEmpty) segments.add(currentSeg);

    // Her segment içinde nearest-neighbor sort uygula
    final result = <FilledBeat>[];
    for (final seg in segments) {
      if (seg.length <= 2) {
        result.addAll(seg);
        continue;
      }

      // İlk eleman sabit (meal pin veya günün ilk durağı)
      final sorted = <FilledBeat>[seg.first];
      final remaining = seg.sublist(1).toList();

      while (remaining.isNotEmpty) {
        final lastPlace = sorted.last.place;
        // En yakın mekanı bul
        remaining.sort((a, b) {
          final da = TravelTimeEstimator.haversine(
              lastPlace.lat, lastPlace.lng, a.place.lat, a.place.lng);
          final db = TravelTimeEstimator.haversine(
              lastPlace.lat, lastPlace.lng, b.place.lat, b.place.lng);
          return da.compareTo(db);
        });
        sorted.add(remaining.removeAt(0));
      }
      result.addAll(sorted);
    }

    // Zaman damgalarını yeniden hesapla (sıra değiştiği için)
    if (result.length == filled.length) {
      TimeOfDayLite currentTime = filled.first.actualStart;
      for (int i = 0; i < result.length; i++) {
        final f = result[i];
        int transitMin = 0;
        double transitDist = 0;
        if (i > 0) {
          final prev = result[i - 1].place;
          transitDist = TravelTimeEstimator.haversine(
              prev.lat, prev.lng, f.place.lat, f.place.lng);
          transitMin = TravelTimeEstimator.estimateMinutesForDistance(
            distKm: transitDist,
            mode: TravelMode.walking,
          );
          currentTime = result[i - 1].actualEnd.addMinutes(transitMin.clamp(5, 30));
        }

        // Yemek slotlarını orijinal zamanlarına yakın tut
        if (isMealPin(f)) {
          // Yemek orijinal zamanından daha erken ise beklet
          if (currentTime.totalMinutes < f.actualStart.totalMinutes) {
            currentTime = f.actualStart;
          }
        }

        result[i] = FilledBeat(
          beat: f.beat,
          place: f.place,
          actualStart: currentTime,
          durationMin: f.durationMin,
          transitMinFromPrev: transitMin,
          transitDistKm: transitDist,
        );
        currentTime = result[i].actualEnd;
      }

      // 3. SAATLERİ YENİDEN HESAPLA VE UYGULA (Çünkü sıra değişti)
      TimeOfDayLite checkTime = result.first.actualStart;
      final updatedResult = <FilledBeat>[];
      bool isViolation = false;

      for (int i = 0; i < result.length; i++) {
        final f = result[i];
        
        // Yeni başlangıç saati (öncekine göre)
        final newStart = i == 0 ? f.actualStart : checkTime.addMinutes(f.transitMinFromPrev + 5);
        final newEnd = newStart.addMinutes(f.durationMin);

        // Validasyon: Kapanış saatini geçti mi?
        final closeMin = f.place.getClosingMinutes(dayKey);
        if (closeMin >= 0 && newEnd.totalMinutes > closeMin) {
          debugPrint("⚠️ GeoSort violation: ${f.place.name} closed at new time.");
          isViolation = true;
          break;
        }

        // Validasyon: 3 tane peş peşe consumption (Food/Social/Coffee)
        if (i >= 2) {
          final g1 = TripVarietyTracker.groupOf(f.place);
          final g2 = TripVarietyTracker.groupOf(updatedResult[i - 1].place);
          final g3 = TripVarietyTracker.groupOf(updatedResult[i - 2].place);
          if (_consumptionGroups.contains(g1) &&
              _consumptionGroups.contains(g2) &&
              _consumptionGroups.contains(g3)) {
            isViolation = true;
            break;
          }
        }

        // Objeyi yeni saatlerle güncelle
        updatedResult.add(f.copyWith(
          actualStart: newStart,
        ));
        checkTime = newEnd;
      }

      if (isViolation) {
        debugPrint("⚠️ GeoSort violated rules, keeping original safe order.");
        return;
      }

      filled.clear();
      filled.addAll(updatedResult);
    }
  }

  // ─────────────────────────────────────────────────────────────────
  // ANCHOR / CLUSTER YARDIMCILARI
  // ─────────────────────────────────────────────────────────────────

  /// Bir anchor mekan etrafında 'radiusKm' yarıçapında cluster oluştur.
  /// `anchor` null ise, tüm cityPool prestige sırasıyla döndürülür.
  static List<Highlight> _buildCluster(
    Highlight? anchor,
    List<Highlight> cityPool, {
    required double radiusKm,
  }) {
    if (anchor == null) return List.from(cityPool);

    final near = cityPool.where((h) {
      if (h.name == anchor.name) return false;
      final d =
          TravelTimeEstimator.haversine(anchor.lat, anchor.lng, h.lat, h.lng);
      return d <= radiusKm;
    }).toList();

    // Anchor'ı listenin başına ekle
    return [anchor, ...near];
  }

  /// Day-trip günlerine en uygun day-trip mekanlarını ata.
  /// Aynı bölgeye 2 day-trip atamaktan kaçın.
  static void _assignDayTrips({
    required ThemePlan themePlan,
    required List<Highlight> candidates,
    required Map<int, Highlight> assignments,
  }) {
    final used = <Highlight>[];
    for (final day in themePlan.dayTripDays) {
      Highlight? pick;
      for (final c in candidates) {
        if (used.contains(c)) continue;
        // Daha önce atanmış day-trip'lerden 50km'den uzak olsun
        bool tooClose = used.any((u) =>
            TravelTimeEstimator.haversine(c.lat, c.lng, u.lat, u.lng) < 50.0);
        if (!tooClose) {
          pick = c;
          break;
        }
      }
      pick ??= candidates.firstWhere((c) => !used.contains(c),
          orElse: () => candidates.isEmpty ? candidates.first : candidates.first);
      if (candidates.isNotEmpty) {
        used.add(pick);
        assignments[day] = pick;
      }
    }
  }

  /// Regular günlere "anchor" mekan ata (gün cluster'ının merkezi).
  /// Aynı semt'te 2 anchor olmasın (≥1 km).
  static void _assignAnchors({
    required ThemePlan themePlan,
    required List<Highlight> cityPool,
    required Set<String> mustSeeIcons,
    required Map<int, Highlight> assignments,
  }) {
    // Önce mustSeeIcons'tan başla, sonra prestige listesi
    final iconList = cityPool.where((h) => mustSeeIcons.contains(h.name)).toList();
    final fallbackList = cityPool.where((h) => !mustSeeIcons.contains(h.name)).toList();

    final ordered = [...iconList, ...fallbackList];
    final usedAnchors = <Highlight>[];

    for (final entry in themePlan.dayThemes.entries) {
      final day = entry.key;
      final themeId = entry.value;
      if (themeId == DayThemeId.dayTrip) continue;

      Highlight? pick;

      // KURAL: Eğer 1. günse ve havuzda Sagrada Familia varsa, ONU SEÇ.
      if (day == 1) {
        final sagrada = ordered.firstWhereOrNull((h) => h.name.toLowerCase().contains("sagrada familia"));
        if (sagrada != null) {
          pick = sagrada;
        }
      }

      if (pick == null) {
        for (final h in ordered) {
          if (usedAnchors.contains(h)) continue;
          // Daha önceki anchor'lardan en az 1.5 km uzak (Çeşitlilik)
          // AMA: Eğer h bir "must-see" ikon ise bu kısıtlamayı del (popülerlik > coğrafya)
          bool tooClose = usedAnchors.any((u) =>
              TravelTimeEstimator.haversine(h.lat, h.lng, u.lat, u.lng) < 1.5);
          
          if (tooClose && !mustSeeIcons.contains(h.name)) continue;
          
          pick = h;
          break;
        }
      }
      if (pick == null) {
        // Mesafe kısıtı uydurulamadı, henüz kullanılmamış ilk mekanı al
        for (final h in ordered) {
          if (!usedAnchors.contains(h)) {
            pick = h;
            break;
          }
        }
      }

      if (pick != null) {
        usedAnchors.add(pick);
        assignments[day] = pick;
      }
    }
  }

  /// "Must-see" iconic mekanları seç.
  /// (rating ≥ 4.6 OR reviewCount ≥ 2000) AND non-consumption.
  static Set<String> _selectMustSeeIcons(List<Highlight> all, int totalDays) {
    final icons = <String>{};
    final sorted = List<Highlight>.from(all);
    _sortByPrestige(sorted); // En popülerler başa

    for (final h in sorted) {
      if (h.isDayTrip) continue;
      final group = TripVarietyTracker.groupOf(h);
      if (_consumptionGroups.contains(group)) continue;

      final isHighPrestige = (h.reviewCount ?? 0) >= 2000 ||
          (h.rating ?? 0) >= 4.6 ||
          h.id == "ChIJk_s92NyipBIRUMnDG8Kq2Js" || // Sagrada Familia (BİZE ÖZEL)
          h.name.toLowerCase().contains("sagrada familia");
      if (isHighPrestige) icons.add(h.name);

      // Havuz genişliği: Her gün için 10 seçenek (eski 5 idi)
      if (icons.length >= totalDays * 10) break;
    }
    return icons;
  }

  /// Highlight listesini prestige (rating + log review count) sırasına göre dizer.
  static void _sortByPrestige(List<Highlight> list) {
    list.sort((a, b) {
      double sa = (a.rating ?? 4.0) * 10 + math.log((a.reviewCount ?? 1) + 1);
      double sb = (b.rating ?? 4.0) * 10 + math.log((b.reviewCount ?? 1) + 1);

      // KURAL: Sagrada Familia her zaman en üstte olmalı
      if (a.name.toLowerCase().contains("sagrada familia")) sa += 10000;
      if (b.name.toLowerCase().contains("sagrada familia")) sb += 10000;

      return sb.compareTo(sa);
    });
  }

  // ─────────────────────────────────────────────────────────────────
  // JSON DÖNÜŞÜM (eski schedule formatıyla uyumlu)
  // ─────────────────────────────────────────────────────────────────

  static Map<String, dynamic> _filledBeatToJson(FilledBeat f, String cityId) {
    final h = f.place;
    return {
      "name": h.name,
      "area": h.area,
      "category": h.category,
      "city": cityId,
      "tags": h.tags,
      "lat": h.lat,
      "lng": h.lng,
      "description": h.description,
      "imageUrl": h.imageUrl,
      "name_en": h.nameEn,
      "description_en": h.descriptionEn,
      "rating": h.rating,
      "reviewCount": h.reviewCount,
      "openHours": h.openHours,
      "calculatedDuration": f.durationMin,
      "startTime": f.actualStart.formatted,
      "isDayTrip": h.isDayTrip,
      // Yeni: beat metadata (UI istemese de, debug için ve gelecekte UI için)
      "beatRole": f.beat.role.name,
      "beatLabel": f.beat.label,
      "transitMin": f.transitMinFromPrev,
    };
  }

  // ─────────────────────────────────────────────────────────────────
  // PREFERENCE MAPPING
  // ─────────────────────────────────────────────────────────────────

  static String _mapTravelStyle(String? tr) {
    switch (tr) {
      case "Maceracı":
        return "adventure";
      case "Turistik":
        return "tourist";
      case "Yerel":
        return "local";
      default:
        return "balanced";
    }
  }

  static String _mapBudgetLevel(String? tr) {
    switch (tr) {
      case "Ekonomik":
        return "economic";
      case "Premium":
        return "premium";
      default:
        return "medium";
    }
  }

  static void _applySandwichEffect(
    List<FilledBeat> filled,
    List<Highlight> pool,
    TripVarietyTracker tripTracker,
    Highlight? anchor,
    Set<String> mustSeeIcons,
    TripPreferences tripPrefs,
    math.Random rng,
    String dayKey,
  ) {
    if (filled.length < 4) return;
    int expStreak = 0;
    int insertAt = -1;

    for (int i = 0; i < filled.length; i++) {
      if (!_consumptionGroups.contains(
          TripVarietyTracker.groupOf(filled[i].place))) {
        expStreak++;
        if (expStreak >= 3) {
          insertAt = i;
          break;
        }
      } else {
        expStreak = 0;
      }
    }

    if (insertAt != -1 && insertAt < filled.length - 1) {
      final gapStart = filled[insertAt].actualEnd;
      final snackBeat = ActivityBeat(
        id: "sandwich_snack",
        role: BeatRole.transition,
        time: BeatTime(gapStart, toleranceMin: 60),
        categoryPolicy: const BeatCategoryPolicy(
          mustGroups: ["COFFEE", "SOCIAL", "FOOD"],
          preferGroups: ["COFFEE"],
        ),
        estimatedDurationMin: 45,
        label: "Mola & Atıştırmalık",
      );

      final fill = BeatFiller.fillBeat(
        beat: snackBeat,
        candidatePool: pool,
        previouslyFilled: filled,
        tripTracker: tripTracker,
        prevPlace: filled[insertAt].place,
        earliestStart: gapStart,
        dayKey: dayKey,
        dayAnchor: anchor,
        mustSeeIcons: mustSeeIcons,
        prefs: tripPrefs,
        rng: rng,
      );
      if (fill != null) {
        filled.insert(insertAt + 1, fill);
      }
    }
  }

  static ActivityBeat _createGuaranteedDinnerBeat() {
    return ActivityBeat(
      id: "guaranteed_dinner",
      role: BeatRole.dinner,
      time: BeatTime(
        TimeOfDayLite(hour: 20, minute: 0),
        toleranceMin: 120,
      ),
      categoryPolicy: const BeatCategoryPolicy(
        mustGroups: ["FOOD"],
        preferGroups: ["FOOD"],
        preferKeywords: ["restoran", "restaurant", "tapas", "dinner"],
      ),
      estimatedDurationMin: 90,
      label: "Akşam Yemeği",
    );
  }
}
