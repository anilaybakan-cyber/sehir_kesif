import 'package:shared_preferences/shared_preferences.dart';
import 'package:flutter/foundation.dart';
import 'trip_update_service.dart';
import 'plan_repository.dart';
import 'dart:math' as math;
import '../models/city_model.dart';
import '../debug/agent_ndjson_log.dart';
import 'city_data_loader.dart';
import 'travel_time_estimator.dart';
import 'itinerary_v2/itinerary_v2.dart';

/// Feature flag - yeni tema-bazlı V2 algoritması default olarak açıktır.
/// Eski (legacy) algoritmaya dönmek için SharedPreferences'a `use_itinerary_v2 = false`.
const bool kItineraryV2DefaultEnabled = true;

/// Zaman bilgisi içeren slot tanımı
class _TimeSlot {
  final String categoryGroup;
  final TimeWindow preferredWindow;
  final int startHour; // Tercih edilen başlangıç saati (örn: 9, 14, 19)

  const _TimeSlot(this.categoryGroup, this.preferredWindow, this.startHour);
}

class SmartItineraryBuilder {
  /// Haversine formula for distance between coordinates (km)
  static double _calculateDistance(double lat1, double lon1, double lat2, double lon2) {
    var p = 0.017453292519943295;
    var c = math.cos;
    var a = 0.5 - c((lat2 - lat1) * p) / 2 + 
            c(lat1 * p) * c(lat2 * p) * 
            (1 - c((lon2 - lon1) * p)) / 2;
    return 12742 * math.asin(math.sqrt(a));
  }

  static Future<void> generateAndSavePlan(String cityId, int totalDays) async {
    try {
      final schedule = await generatePlan(cityId, totalDays);
      if (schedule != null) {
        await savePlan(cityId, schedule);
      }
    } catch (e) {
      debugPrint("❌ Smart Itinerary Builder Error (Save): $e");
    }
  }

  static Future<void> savePlan(String cityId, Map<String, dynamic> schedule) async {
    final normalizedCityId = cityId.toLowerCase();
    await PlanRepository.saveSchedule(normalizedCityId, schedule);
    await PlanRepository.markPlanCreated(normalizedCityId, isAiPlan: true);
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool("has_migrated_to_per_city", true);
    TripUpdateService().notifyTripChanged();
    debugPrint("✅ Smart Itinerary Saved for $normalizedCityId.");
  }

  static Future<Map<String, dynamic>?> generatePlan(String cityId, int totalDays) async {
    // ─── Feature Flag: ItineraryV2 ───────────────────────────────────
    // Default açık. Geri dönmek için SharedPreferences'a use_itinerary_v2=false yazın.
    final prefs0 = await SharedPreferences.getInstance();
    final useV2 = prefs0.getBool("use_itinerary_v2") ?? kItineraryV2DefaultEnabled;
    bool v2Attempted = false;
    String? v2FailReason;

    try {
      if (useV2) {
        v2Attempted = true;
        debugPrint("🆕 Using ItineraryV2 (theme-based) for $cityId / $totalDays days");
        final v2Result = await ItineraryV2.generatePlan(cityId, totalDays);
        if (v2Result != null) return v2Result;
        v2FailReason = 'v2_returned_null';
        debugPrint("⚠️ ItineraryV2 returned null, falling back to legacy");
      } else {
        v2FailReason = 'use_itinerary_v2_false';
      }
    } catch (e) {
      v2FailReason = 'v2_exception:${e.runtimeType}';
      debugPrint("⚠️ ItineraryV2 dispatch error, falling back to legacy: $e");
    }

    agentNdjsonLog(
      hypothesisId: 'H3',
      location: 'smart_itinerary_builder.dart:generatePlan',
      message: 'entering_legacy_path',
      data: {
        'cityId': cityId,
        'totalDays': totalDays,
        'useV2Pref': useV2,
        'v2Attempted': v2Attempted,
        'v2FailReason': v2FailReason,
      },
    );

    // ─── Legacy algoritma (fallback) ─────────────────────────────────
    try {
      final cityData = await CityDataLoader.loadCity(cityId);
      final allHighlights = List<Highlight>.from(cityData.highlights);

      // --- 1. PRESTIGE RANKING ---
      final List<Highlight> sortedByPrestige = List.from(allHighlights);
      sortedByPrestige.sort((a, b) {
        double scoreA = (a.rating ?? 4.0) * 10 + math.log((a.reviewCount ?? 1) + 1);
        double scoreB = (b.rating ?? 4.0) * 10 + math.log((b.reviewCount ?? 1) + 1);
        return scoreB.compareTo(scoreA);
      });

      final List<Highlight> dayTripCandidates = sortedByPrestige.where((h) => h.isDayTrip).toList();
      final List<Highlight> mustSeeIcons = sortedByPrestige.where((h) {
        if (h.isDayTrip) return false;
        final group = _getCategoryGroup(h);
        bool isConsumption = group == "FOOD" || group == "COFFEE" || group == "SOCIAL";
        bool isHighPrestige = (h.reviewCount ?? 0) > 800 || (h.rating ?? 0) >= 4.7;
        return !isConsumption && isHighPrestige;
      }).take(totalDays * 5).toList();

      final topPool = sortedByPrestige.where((h) => !h.isDayTrip).take(totalDays * 50).toList();

      // --- 2. DAY-TRIP RESERVATION ---
      int maxDayTrips = 0;
      if (totalDays >= 3) maxDayTrips = 1;
      if (totalDays >= 5) maxDayTrips = 2;
      if (totalDays >= 8) maxDayTrips = 3;

      final List<Highlight> selectedDayTrips = [];
      for (var dt in dayTripCandidates) {
        if (selectedDayTrips.length >= maxDayTrips) break;
        bool sameArea = selectedDayTrips.any((s) => _calculateDistance(dt.lat, dt.lng, s.lat, s.lng) < 50.0);
        if (!sameArea) selectedDayTrips.add(dt);
      }
      final int regularDays = totalDays - selectedDayTrips.length;

      // --- 3. GEO-ANCHORING ---
      List<Highlight> dailyAnchors = [];
      for (var h in mustSeeIcons) {
        if (dailyAnchors.length >= regularDays) break;
        bool tooClose = dailyAnchors.any((a) => _calculateDistance(h.lat, h.lng, a.lat, a.lng) < 1.0);
        if (!tooClose) dailyAnchors.add(h);
      }
      
      if (dailyAnchors.length < regularDays) {
        var fallbacks = topPool.where((h) => !dailyAnchors.contains(h) && 
            !(_getCategoryGroup(h) == "FOOD" || _getCategoryGroup(h) == "COFFEE" || _getCategoryGroup(h) == "SOCIAL")).toList();
        dailyAnchors.addAll(fallbacks.take(regularDays - dailyAnchors.length));
      }

      Map<int, List<Highlight>> clusters = {};
      for (int i = 0; i < dailyAnchors.length; i++) {
        Highlight anchor = dailyAnchors[i];
        var neighbors = allHighlights.where((h) => !h.isDayTrip && _calculateDistance(h.lat, h.lng, anchor.lat, anchor.lng) <= 15.0).toList();
        neighbors.sort((a, b) => _calculateDistance(a.lat, a.lng, anchor.lat, anchor.lng).compareTo(_calculateDistance(b.lat, b.lng, anchor.lat, anchor.lng)));
        clusters[i] = neighbors.take(40).toList();
      }

      final prefs = await SharedPreferences.getInstance();
      final List<String> interests = (prefs.getStringList("interests") ?? []).map((e) => e.toLowerCase()).toList();
      final String travelStyle = _mapTravelStyle(prefs.getString("travelStyle") ?? "Dengeli");
      final String budgetLevel = _mapBudgetLevel(prefs.getString("budgetLevel") ?? "Dengeli");
      
      Map<String, dynamic> generatedSchedule = {};
      Set<String> usedNames = {};
      final random = math.Random();

      for (int day = 1; day <= totalDays; day++) {
        final bool isDayTripDay = day > regularDays;
        if (isDayTripDay) {
          final dtIdx = day - regularDays - 1;
          if (dtIdx >= selectedDayTrips.length) continue;
          final dayTripPlace = selectedDayTrips[dtIdx];
          final List<Map<String, dynamic>> dtJson = [];
          final morningCoffee = topPool.firstWhere((h) => !usedNames.contains(h.name) && (_getCategoryGroup(h) == "COFFEE" || _getCategoryGroup(h) == "FOOD"), orElse: () => topPool.firstWhere((h) => !usedNames.contains(h.name), orElse: () => topPool.first));
          dtJson.add(_highlightToJson(morningCoffee, cityId, startTime: "08:30", customDuration: 45));
          usedNames.add(morningCoffee.name);
          dtJson.add(_highlightToJson(dayTripPlace, cityId, startTime: "09:30", customDuration: dayTripPlace.dayTripDurationMinutes));
          usedNames.add(dayTripPlace.name);
          generatedSchedule[day.toString()] = dtJson;
          continue;
        }

        int anchorIdx = (day - 1) % dailyAnchors.length;
        Highlight dayAnchor = dailyAnchors[anchorIdx];
        List<Highlight> dayPool = List.from(clusters[anchorIdx] ?? []);
        dayPool.removeWhere((h) => usedNames.contains(h.name));

        int targetCount = 8 + random.nextInt(2);
        final timeSlots = _getTimeAwareTemplate(targetCount);
        List<Highlight> dayPlan = [dayAnchor];
        usedNames.add(dayAnchor.name);

        for (int slot = 1; slot < timeSlots.length; slot++) {
          final timeSlot = timeSlots[slot];
          final requiredGroup = timeSlot.categoryGroup;
          
          Highlight? best;
          double bestScore = -20000.0;

          // V4.6: Strict Diversity Check
          bool lastWasConsumption = dayPlan.isNotEmpty && _isConsumptionGroup(_getCategoryGroup(dayPlan.last));

          for (var h in dayPool) {
            if (usedNames.contains(h.name)) continue;
            
            final currentGroup = _getCategoryGroup(h);
            bool isCurrentConsumption = _isConsumptionGroup(currentGroup);
            
            // ASLA peş peşe iki yeme-içme-bar olamaz
            if (lastWasConsumption && isCurrentConsumption) continue;
            
            // Tercih edilen kategoride mi? (Değilse puan kır ama yasaklama - diversity için)
            double score = _calculateIndividualScore(h, requiredGroup, interests, budgetLevel, travelStyle, dayAnchor, dayPlan, random, mustSeeIcons);
            
            if (currentGroup != requiredGroup) {
               score -= 5000.0; // Yanlış slot kategorisi cezası
            }

            if (score > bestScore) {
              bestScore = score;
              best = h;
            }
          }
          if (best != null) {
            dayPlan.add(best);
            usedNames.add(best.name);
          }
        }

        // --- 3.5 SAFETY FILL: Dengeyi koruyarak doldur ---
        final List<Highlight> emergencyPool = List.from(allHighlights);
        emergencyPool.sort((a, b) => _calculateDistance(a.lat, a.lng, dayAnchor.lat, dayAnchor.lng).compareTo(_calculateDistance(b.lat, b.lng, dayAnchor.lat, dayAnchor.lng)));
        
        if (dayPlan.length < 7) {
          for (var h in emergencyPool) {
            if (dayPlan.length >= 8) break;
            if (usedNames.contains(h.name) || h.isDayTrip) continue;
            
            // KURAL: Peş peşe 3 yeme-içme ekleme
            if (dayPlan.length >= 2) {
              final last1 = _getCategoryGroup(dayPlan.last);
              final last2 = _getCategoryGroup(dayPlan[dayPlan.length - 2]);
              final thisGroup = _getCategoryGroup(h);
              if (_isConsumptionGroup(last1) && _isConsumptionGroup(last2) && _isConsumptionGroup(thisGroup)) {
                continue; // Son 2 consumption, 3. ekleme
              }
            }
            
            bool lastWasCons = dayPlan.isNotEmpty && _isConsumptionGroup(_getCategoryGroup(dayPlan.last));
            bool thisIsCons = _isConsumptionGroup(_getCategoryGroup(h));
            
            // Güvenlik dolgusunda da peş peşe yeme-içme yasağı
            if (lastWasCons && thisIsCons) continue;

            dayPlan.add(h);
            usedNames.add(h.name);
          }
        }

        DateTime currentTime = DateTime(2024, 1, 1, 9, 0);
        final reorderedDayPlan = _rebalanceDayPlanForOpenHours(dayPlan, currentTime);
        final List<Map<String, dynamic>> dayJson = [];
        for (var h in reorderedDayPlan) {
          if (!_canSchedulePlaceAtTime(h, currentTime, _dayKeyFromDate(currentTime))) {
            final fallback = topPool.firstWhere((p) => !usedNames.contains(p.name) && _canSchedulePlaceAtTime(p, currentTime, _dayKeyFromDate(currentTime)), orElse: () => h);
            if (fallback.name != h.name) { h = fallback; usedNames.add(h.name); }
          }
          currentTime = _adjustStartTimeForOpeningHours(h, currentTime);
          dayJson.add(_highlightToJson(h, cityId, startTime: "${currentTime.hour.toString().padLeft(2, '0')}:${currentTime.minute.toString().padLeft(2, '0')}"));
          currentTime = currentTime.add(Duration(minutes: _getMekanDuration(h) + 25));
          
          // BOŞLUK DOLDURMA: 180 dk'dan fazla boşluk varsa araya deneyim sıkıştır
          if (dayJson.isNotEmpty) {
            final prevEnd = currentTime.subtract(Duration(minutes: _getMekanDuration(h) + 25));
            final gapMinutes = currentTime.difference(prevEnd).inMinutes;
            if (gapMinutes > 180) {
              // Boşluk doldurma mekanı ekle
              final gapFiller = emergencyPool.firstWhere(
                (p) => !usedNames.contains(p.name) && !_isConsumptionGroup(_getCategoryGroup(p)),
                orElse: () => emergencyPool.firstWhere((p) => !usedNames.contains(p.name), orElse: () => h)
              );
              if (!usedNames.contains(gapFiller.name)) {
                final gapTime = prevEnd.add(Duration(minutes: gapMinutes ~/ 2));
                dayJson.add(_highlightToJson(gapFiller, cityId, startTime: "${gapTime.hour.toString().padLeft(2, '0')}:${gapTime.minute.toString().padLeft(2, '0')}"));
                usedNames.add(gapFiller.name);
                currentTime = gapTime.add(Duration(minutes: _getMekanDuration(gapFiller) + 25));
              }
            }
          }
          
          int rem = currentTime.minute % 5;
          if (rem != 0) currentTime = currentTime.add(Duration(minutes: 5 - rem));
          if (currentTime.hour >= 23) break;
        }
        generatedSchedule[day.toString()] = dayJson;
      }
      return generatedSchedule;
    } catch (e) {
      debugPrint("❌ Smart Itinerary Builder Error: $e");
      return null;
    }
  }

  static double _calculateIndividualScore(Highlight h, String group, List<String> interests, String budget, String style, Highlight anchor, List<Highlight> plan, math.Random r, List<Highlight> icons) {
    double score = 1000.0;
    if (icons.contains(h)) score += 2000.0;
    if (plan.isNotEmpty && _isConsumptionGroup(_getCategoryGroup(plan.last)) && _isConsumptionGroup(group)) score -= 5000.0;
    score += (h.rating ?? 4.0) * 100.0 + math.log((h.reviewCount ?? 1) + 1) * 30.0;
    Highlight ref = plan.isNotEmpty ? plan.last : anchor;
    score -= _calculateDistance(h.lat, h.lng, ref.lat, ref.lng) * 120.0;
    return score + r.nextDouble() * 50.0;
  }

  static bool _isConsumptionGroup(String g) => g == "FOOD" || g == "COFFEE" || g == "SOCIAL";
  
  static String _getCategoryGroup(Highlight h) {
    final c = h.category.toLowerCase();
    final n = h.name.toLowerCase();
    if (n.contains("gelateria") || n.contains("cafe") || n.contains("coffee") || n.contains("ice cream") || n.contains("pastane") || n.contains("patisserie") || n.contains("bakery")) return "COFFEE";
    if (c.contains("yeme") || c.contains("food") || c.contains("restoran") || c.contains("gastronomi") || c.contains("bistro") || c.contains("brunch") || n.contains("restaurant") || n.contains("bistro") || n.contains("trattoria")) return "FOOD";
    if (c.contains("bar") || c.contains("pub") || c.contains("gece") || c.contains("wine") || c.contains("şarap") || n.contains("bar") || n.contains("pub") || n.contains("caviste") || n.contains("winery")) return "SOCIAL";
    if (c.contains("park") || c.contains("bahçe") || c.contains("garden") || c.contains("doğa")) return "NATURE";
    if (c.contains("view") || c.contains("manzara") || c.contains("teras")) return "VIEW";
    if (c.contains("meydan") || c.contains("square")) return "SQUARE";
    return "CULTURE";
  }

  static List<_TimeSlot> _getTimeAwareTemplate(int count) {
    if (count <= 8) {
      return const [
        _TimeSlot("CULTURE", TimeWindow.MORNING, 9),
        _TimeSlot("SQUARE", TimeWindow.MORNING, 10),
        _TimeSlot("FOOD", TimeWindow.MORNING, 11),
        _TimeSlot("CULTURE", TimeWindow.AFTERNOON, 12),
        _TimeSlot("COFFEE", TimeWindow.AFTERNOON, 14),
        _TimeSlot("VIEW", TimeWindow.AFTERNOON, 15),
        _TimeSlot("CULTURE", TimeWindow.AFTERNOON, 16),
        _TimeSlot("SOCIAL", TimeWindow.EVENING, 19),
      ];
    }
    return const [
      _TimeSlot("CULTURE", TimeWindow.MORNING, 9),
      _TimeSlot("SQUARE", TimeWindow.MORNING, 10),
      _TimeSlot("FOOD", TimeWindow.MORNING, 11),
      _TimeSlot("CULTURE", TimeWindow.AFTERNOON, 12),
      _TimeSlot("COFFEE", TimeWindow.AFTERNOON, 14),
      _TimeSlot("VIEW", TimeWindow.AFTERNOON, 15),
      _TimeSlot("CULTURE", TimeWindow.AFTERNOON, 16),
      _TimeSlot("FOOD", TimeWindow.EVENING, 18),
      _TimeSlot("SOCIAL", TimeWindow.EVENING, 20),
    ];
  }

  static String _mapTravelStyle(String tr) {
    if (tr == "Maceracı") return "adventure";
    if (tr == "Turistik") return "tourist";
    if (tr == "Yerel") return "local";
    return "balanced";
  }

  static String _mapBudgetLevel(String tr) {
    if (tr == "Ekonomik") return "economic";
    if (tr == "Premium") return "premium";
    return "medium";
  }

  static int _getMekanDuration(Highlight h) {
    final g = _getCategoryGroup(h);
    if (g == "CULTURE") return (h.category.toLowerCase().contains("museum") || h.name.toLowerCase().contains("museum")) ? 180 : 120;
    if (g == "FOOD") return 90;
    if (g == "COFFEE") return 45;
    if (g == "SOCIAL") return 120;
    if (g == "VIEW") return 60;
    return 60;
  }

  static List<Highlight> _rebalanceDayPlanForOpenHours(List<Highlight> plan, DateTime start) {
    if (plan.length < 3) return plan;
    final rem = List<Highlight>.from(plan);
    final res = <Highlight>[];
    DateTime p = start;
    while (rem.isNotEmpty) {
      int bestIdx = 0; double bestS = -100000;
      for (int i = 0; i < rem.length; i++) {
        bool op = rem[i].isOpenAt(p.hour, p.minute, dayOfWeek: _dayKeyFromDate(p));
        double s = op ? 1000 : 0;
        if (s > bestS) { bestS = s; bestIdx = i; }
      }
      final picked = rem.removeAt(bestIdx);
      res.add(picked);
      p = _adjustStartTimeForOpeningHours(picked, p);
      p = p.add(Duration(minutes: _getMekanDuration(picked) + 10));
    }
    return res;
  }

  static DateTime _adjustStartTimeForOpeningHours(Highlight h, DateTime t) {
    final key = _dayKeyFromDate(t);
    if (h.isOpenAt(t.hour, t.minute, dayOfWeek: key)) return t;
    final op = h.getOpeningMinutes(key);
    if (op < 0) return t;
    int curr = t.hour * 60 + t.minute;
    int wait = op - curr;
    return (wait > 0 && wait < 180) ? t.add(Duration(minutes: wait)) : t;
  }

  static bool _canSchedulePlaceAtTime(Highlight h, DateTime t, String key) {
    if (!h.isOpenAt(t.hour, t.minute, dayOfWeek: key)) return false;
    final cl = h.getClosingMinutes(key);
    if (cl < 0) return true;
    int curr = t.hour * 60 + t.minute;
    return (cl - curr) >= _getMekanDuration(h);
  }

  static String _dayKeyFromDate(DateTime d) {
    const keys = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
    return keys[d.weekday - 1];
  }

  static Map<String, dynamic> _highlightToJson(Highlight h, String cityId, {String? startTime, int? customDuration}) {
    return {
      "name": h.name, "area": h.area, "category": h.category, "city": cityId,
      "tags": h.tags, "lat": h.lat, "lng": h.lng, "description": h.description,
      "imageUrl": h.imageUrl, "name_en": h.nameEn, "description_en": h.descriptionEn,
      "rating": h.rating, "reviewCount": h.reviewCount, "openHours": h.openHours,
      "calculatedDuration": customDuration ?? _getMekanDuration(h),
      "startTime": startTime, "isDayTrip": h.isDayTrip,
    };
  }
}
