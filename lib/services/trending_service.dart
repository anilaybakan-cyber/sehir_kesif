// =============================================================================
// TRENDING SERVICE - Akıllı Trending Today Algoritması
// Saat, gün ve kategori bazlı trending mekan hesaplama
// =============================================================================

import 'dart:math';
import '../models/city_model.dart';

class TrendingService {
  // Kategori bazlı saat ağırlıkları
  // Her kategori için günün hangi saatlerinde daha popüler olduğunu tanımlar
  static final Map<String, List<int>> _categoryPeakHours = {
    'Cafe': [7, 8, 9, 10, 11, 14, 15, 16], // Sabah ve öğleden sonra
    'Restoran': [12, 13, 19, 20, 21, 22], // Öğle ve akşam yemeği
    'Bar': [18, 19, 20, 21, 22, 23, 0, 1], // Akşam ve gece
    'Müze': [10, 11, 12, 13, 14, 15, 16], // Gündüz saatleri
    'Park': [8, 9, 10, 11, 16, 17, 18, 19], // Sabah ve akşamüstü
    'Tarihi': [9, 10, 11, 12, 14, 15, 16, 17], // Gündüz
    'Manzara': [6, 7, 17, 18, 19, 20], // Gün doğumu ve batımı
    'Deneyim': [10, 11, 12, 14, 15, 16, 17], // Gündüz aktiviteleri
    'Alışveriş': [11, 12, 13, 14, 15, 16, 17, 18, 19], // Alışveriş saatleri
  };

  // Hafta sonu bonus kategorileri
  static final List<String> _weekendBoostCategories = [
    'Park',
    'Manzara',
    'Restoran',
    'Cafe',
    'Deneyim',
  ];

  // Hafta içi bonus kategorileri
  static final List<String> _weekdayBoostCategories = [
    'Müze',
    'Tarihi',
    'Alışveriş',
  ];

  /// Ana fonksiyon: Trending mekanları hesaplar
  /// [places] - Tüm mekanlar listesi
  /// [limit] - Kaç mekan döndürülecek (varsayılan 8)
  static List<Highlight> getTrendingPlaces(List<Highlight> places, {int limit = 8}) {
    if (places.isEmpty) return [];

    final now = DateTime.now();
    final hour = now.hour;
    final isWeekend = now.weekday == DateTime.saturday || now.weekday == DateTime.sunday;
    
    // Her mekan için trending skoru hesapla
    final scoredPlaces = places.map((place) {
      final score = _calculateTrendingScore(place, hour, isWeekend, now);
      return MapEntry(place, score);
    }).toList();

    // Skora göre sırala
    scoredPlaces.sort((a, b) => b.value.compareTo(a.value));

    // Kategori çeşitliliği sağla (max 2 aynı kategoriden)
    final result = <Highlight>[];
    final categoryCount = <String, int>{};

    for (final entry in scoredPlaces) {
      final category = entry.key.category;
      final count = categoryCount[category] ?? 0;
      
      if (count < 2) {
        result.add(entry.key);
        categoryCount[category] = count + 1;
      }
      
      if (result.length >= limit) break;
    }

    return result;
  }

  /// Tek bir mekan için trending skoru hesaplar
  static double _calculateTrendingScore(
    Highlight place,
    int hour,
    bool isWeekend,
    DateTime now,
  ) {
    double score = 0.0;

    // 1. Rating skoru (0-25 puan)
    final rating = place.rating ?? 3.5;
    score += (rating / 5.0) * 25;

    // 2. Saat uyumu skoru (0-35 puan)
    final peakHours = _categoryPeakHours[place.category] ?? [];
    if (peakHours.contains(hour)) {
      score += 35;
    } else if (peakHours.contains((hour - 1) % 24) || peakHours.contains((hour + 1) % 24)) {
      // Peak saate yakın
      score += 20;
    }

    // 3. Hafta sonu/hafta içi bonus (0-20 puan)
    if (isWeekend && _weekendBoostCategories.contains(place.category)) {
      score += 20;
    } else if (!isWeekend && _weekdayBoostCategories.contains(place.category)) {
      score += 20;
    }

    // 4. Günlük rotasyon için seed bazlı bonus (0-15 puan)
    final seed = now.year * 10000 + now.month * 100 + now.day;
    final random = Random(seed + place.name.hashCode);
    score += random.nextDouble() * 15;

    // 5. Görsel olan mekanlara bonus (0-5 puan)
    if (place.imageUrl != null && place.imageUrl!.isNotEmpty) {
      score += 5;
    }

    return score;
  }

  /// Günün bölümünü döndürür (UI için)
  static String getDayPeriod() {
    final hour = DateTime.now().hour;
    if (hour >= 5 && hour < 12) return 'morning';
    if (hour >= 12 && hour < 17) return 'afternoon';
    if (hour >= 17 && hour < 21) return 'evening';
    return 'night';
  }

  /// Günün bölümüne göre emoji döndürür
  static String getDayPeriodEmoji() {
    switch (getDayPeriod()) {
      case 'morning':
        return '☀️';
      case 'afternoon':
        return '🌤️';
      case 'evening':
        return '🌅';
      case 'night':
        return '🌙';
      default:
        return '🔥';
    }
  }

  /// Günün bölümüne göre başlık döndürür
  static String getTrendingTitle({bool isEnglish = false}) {
    final period = getDayPeriod();
    if (isEnglish) {
      switch (period) {
        case 'morning':
          return 'Trending This Morning';
        case 'afternoon':
          return 'Hot This Afternoon';
        case 'evening':
          return 'Tonight\'s Picks';
        case 'night':
          return 'Late Night Spots';
        default:
          return 'Trending Now';
      }
    } else {
      switch (period) {
        case 'morning':
          return 'Bu Sabah Popüler';
        case 'afternoon':
          return 'Öğleden Sonra Trend';
        case 'evening':
          return 'Bu Akşam Popüler';
        case 'night':
          return 'Gece Açık Yerler';
        default:
          return 'Şu An Trend';
      }
    }
  }
}
