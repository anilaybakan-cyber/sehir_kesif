import 'dart:async';
import 'package:shared_preferences/shared_preferences.dart';

class TutorialService {
  static final TutorialService _instance = TutorialService._internal();
  static TutorialService get instance => _instance;

  TutorialService._internal();

  // Keys - Version bump resets tutorials for all users
  static const String KEY_TUTORIAL_CITY_SELECTION = "tutorial_city_selection_v99";
  static const String KEY_TUTORIAL_AI_BUTTON = "tutorial_ai_button_v99";
  static const String KEY_TUTORIAL_MODE_SELECTION = "tutorial_mode_selection_v99";
  static const String KEY_TUTORIAL_FAB = "tutorial_fab_v99";
  static const String KEY_TUTORIAL_NEARBY = "tutorial_nearby_v99";
  static const String KEY_TUTORIAL_ADD_TO_ROUTE = "tutorial_add_to_route_v99";
  static const String KEY_TUTORIAL_ROUTES = "tutorial_routes_seen_v99";
  static const String KEY_TUTORIAL_MY_ROUTE = "tutorial_myroute_seen_v99";
  static const String KEY_TUTORIAL_MEMORIES = "tutorial_memories_seen_v99";

  // ⚠️ DEBUG: Set to true to force all tutorials to show (for testing)
  // ⚠️ CANLIYA ÇIKARKEN FALSE YAP!
  static const bool _forceShowAllTutorials = false;

  Future<bool> shouldShowTutorial(String key) async {
    return false; // TEMPORARILY DISABLED BY USER REQUEST
    // if (_forceShowAllTutorials) return true; // DEBUG MODE
    // final prefs = await SharedPreferences.getInstance();
    // return !(prefs.getBool(key) ?? false);
  }

  Future<void> markTutorialSeen(String key) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(key, true);
  }

  Future<void> skipAllTutorials() async {
    final prefs = await SharedPreferences.getInstance();
    final allKeys = [
      KEY_TUTORIAL_CITY_SELECTION,
      KEY_TUTORIAL_AI_BUTTON,
      KEY_TUTORIAL_MODE_SELECTION,
      KEY_TUTORIAL_FAB,
      KEY_TUTORIAL_NEARBY,
      KEY_TUTORIAL_ADD_TO_ROUTE,
      KEY_TUTORIAL_ROUTES,
      KEY_TUTORIAL_MY_ROUTE,
      KEY_TUTORIAL_MEMORIES,
    ];
    for (var key in allKeys) {
      await prefs.setBool(key, true);
    }
  }

  Future<void> resetAllTutorials() async {
    final prefs = await SharedPreferences.getInstance();
    final allKeys = [
      KEY_TUTORIAL_CITY_SELECTION,
      KEY_TUTORIAL_AI_BUTTON,
      KEY_TUTORIAL_MODE_SELECTION,
      KEY_TUTORIAL_FAB,
      KEY_TUTORIAL_NEARBY,
      KEY_TUTORIAL_ADD_TO_ROUTE,
      KEY_TUTORIAL_ROUTES,
      KEY_TUTORIAL_MY_ROUTE,
      KEY_TUTORIAL_MEMORIES,
    ];
    for (var key in allKeys) {
      await prefs.setBool(key, false);
    }
  }
  // Trigger stream
  final _tutorialTriggerController = StreamController<String>.broadcast();
  Stream<String> get tutorialTrigger => _tutorialTriggerController.stream;

  void triggerTutorial(String key) {
    _tutorialTriggerController.add(key);
  }
}
