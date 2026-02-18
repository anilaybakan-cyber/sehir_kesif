// Dosya: lib/services/user_preferences.dart

import 'package:shared_preferences/shared_preferences.dart';

class UserPreferences {
  static Future<Map<String, dynamic>> getUserProfile() async {
    final prefs = await SharedPreferences.getInstance();

    return {
      'travelStyle': prefs.getString('travelStyle') ?? 'Turistik',
      'walkingLevel': prefs.getInt('walkingLevel') ?? 1,
      'budgetLevel': prefs.getString('budgetLevel') ?? 'Dengeli',
      'interests': prefs.getStringList('interests') ?? [],
    };
  }

  static Future<String> getTravelStyle() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('travelStyle') ?? 'Turistik';
  }

  static Future<int> getWalkingLevel() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getInt('walkingLevel') ?? 1;
  }

  static Future<String> getBudgetLevel() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString('budgetLevel') ?? 'Dengeli';
  }

  static Future<List<String>> getInterests() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getStringList('interests') ?? [];
  }

  // Walking level'a göre maksimum mesafe (km)
  static double getMaxDistanceForWalkingLevel(int level) {
    switch (level) {
      case 0:
        return 3.0; // Minimum
      case 1:
        return 6.0; // Orta
      case 2:
        return 10.0; // Aktif
      case 3:
        return 15.0; // Keşifçi
      default:
        return 6.0;
    }
  }

  // Budget level'a göre fiyat filtresi
  static List<String> getAllowedPricesForBudget(String budget) {
    switch (budget) {
      case 'Ekonomik':
        return ['free', 'low'];
      case 'Dengeli':
        return ['free', 'low', 'medium'];
      case 'Premium':
        return ['free', 'low', 'medium', 'high'];
      default:
        return ['free', 'low', 'medium'];
    }
  }

  // Travel style'a göre kategori öncelikleri
  static List<String> getCategoriesForTravelStyle(String style) {
    switch (style) {
      case 'Turistik':
        return ['turistik', 'lokal'];
      case 'Lokal':
        return ['lokal', 'chill'];
      case 'Chill':
        return ['chill', 'lokal'];
      case 'Instagramlık':
        return ['instagramlik', 'turistik'];
      default:
        return ['turistik', 'lokal'];
    }
  }
}
