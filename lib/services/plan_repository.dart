import 'dart:convert';
import 'package:shared_preferences/shared_preferences.dart';

class PlanRepository {
  static String normalizeCityId(String cityId) => cityId.toLowerCase().trim();

  static String scheduleKey(String cityId) =>
      "trip_schedule_${normalizeCityId(cityId)}";

  static String placesKey(String cityId) =>
      "trip_places_${normalizeCityId(cityId)}";

  static String aiPlanKey(String cityId) =>
      "is_ai_plan_${normalizeCityId(cityId)}";

  static String trialCountKey(String cityId) =>
      "itinerary_trial_count_${normalizeCityId(cityId)}";

  static String hasCreatedPlanKey(String cityId) =>
      "has_created_plan_${normalizeCityId(cityId)}";

  static Future<void> saveSchedule(
    String cityId,
    Map<String, dynamic> schedule,
  ) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(scheduleKey(cityId), jsonEncode(schedule));
  }

  static Future<int> getTrialCount(String cityId) async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getInt(trialCountKey(cityId)) ?? 0;
  }

  static Future<bool> hasUsedPlanForCity(String cityId) async {
    final prefs = await SharedPreferences.getInstance();
    return (prefs.getBool(hasCreatedPlanKey(cityId)) ?? false) ||
        (prefs.getBool("has_created_plan") ?? false);
  }

  static Future<int> incrementTrialCount(String cityId) async {
    final prefs = await SharedPreferences.getInstance();
    final nextValue = (prefs.getInt(trialCountKey(cityId)) ?? 0) + 1;
    await prefs.setInt(trialCountKey(cityId), nextValue);
    return nextValue;
  }

  static Future<void> markPlanCreated(
    String cityId, {
    bool isAiPlan = false,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(hasCreatedPlanKey(cityId), true);
    // Backward compatibility for existing checks.
    await prefs.setBool("has_created_plan", true);
    if (isAiPlan) {
      await prefs.setBool(aiPlanKey(cityId), true);
    }
  }
}
