import 'dart:math' as math;
import '../models/city_model.dart';

/// Ulaşım modu — RoutesScreen'deki transport mode index'leriyle aynı.
/// 0 = walking, 1 = bicycling, 2 = transit, 3 = driving
enum TravelMode { walking, bicycling, transit, driving }

/// Mesafe ve mod bazlı travel time tahmincisi.
/// Google Directions cache'i yokken default 600 sn'lik kötü tahmin yerine
/// gerçekçi (haversine + ortalama hız) bir tahmin verir.
///
/// Şehir-içi ortalama hızlar (km/saat):
///   - walking:    ~4.5
///   - bicycling:  ~14
///   - transit:    ~22  (metro+yürüme; bekleme dahil amortizasyon)
///   - driving:    ~30  (şehir içi trafik)
///
/// Şehirler-arası (>30 km) için hızlar yükselir:
///   - transit:    ~70  (intercity tren/otobüs ortalama)
///   - driving:    ~80  (otoyol)
class TravelTimeEstimator {
  static const double _earthDiameterKm = 12742.0;
  static const double _degToRad = 0.017453292519943295;

  /// İki nokta arasındaki haversine mesafesi (km).
  static double haversine(double lat1, double lng1, double lat2, double lng2) {
    final dLat = (lat2 - lat1) * _degToRad;
    final dLng = (lng2 - lng1) * _degToRad;
    final a = math.sin(dLat / 2) * math.sin(dLat / 2) +
        math.cos(lat1 * _degToRad) *
            math.cos(lat2 * _degToRad) *
            math.sin(dLng / 2) *
            math.sin(dLng / 2);
    return _earthDiameterKm * math.asin(math.sqrt(a));
  }

  /// İki yer arasındaki tahmini seyahat süresini (dakika) döndürür.
  static int estimateMinutes({
    required double lat1,
    required double lng1,
    required double lat2,
    required double lng2,
    TravelMode mode = TravelMode.walking,
  }) {
    final distKm = haversine(lat1, lng1, lat2, lng2);
    return estimateMinutesForDistance(distKm: distKm, mode: mode);
  }

  /// Hazır mesafeden (km) süre tahmini.
  static int estimateMinutesForDistance({
    required double distKm,
    TravelMode mode = TravelMode.walking,
  }) {
    if (distKm <= 0.05) return 0;

    final bool isIntercity = distKm > 30.0;

    double speedKmh;
    int bufferMinutes;

    switch (mode) {
      case TravelMode.walking:
        // 30 km'den uzak yürünmez — ama yine de hesap kırılmasın
        speedKmh = 4.5;
        bufferMinutes = 0;
        break;
      case TravelMode.bicycling:
        speedKmh = 14.0;
        bufferMinutes = 2;
        break;
      case TravelMode.transit:
        speedKmh = isIntercity ? 70.0 : 22.0;
        bufferMinutes = isIntercity ? 25 : 8; // intercity bekleme + transfer
        break;
      case TravelMode.driving:
        speedKmh = isIntercity ? 80.0 : 30.0;
        bufferMinutes = isIntercity ? 10 : 5; // park etme vs.
        break;
    }

    final travelHours = distKm / speedKmh;
    final minutes = (travelHours * 60).round() + bufferMinutes;

    // Aynı şehir içi minimum 5 dk; intercity minimum 30 dk.
    if (isIntercity) return math.max(30, minutes);
    return math.max(5, minutes);
  }

  /// Highlight'lar arasındaki süre tahmini (kısayol).
  static int estimateBetween(
    Highlight a,
    Highlight b, {
    TravelMode mode = TravelMode.walking,
  }) {
    return estimateMinutes(
      lat1: a.lat,
      lng1: a.lng,
      lat2: b.lat,
      lng2: b.lng,
      mode: mode,
    );
  }

  /// RoutesScreen'deki int mode → TravelMode çevirisi.
  /// 0 = walking, 1 = bicycling, 2 = transit, 3 = driving
  static TravelMode modeFromInt(int v) {
    switch (v) {
      case 1:
        return TravelMode.bicycling;
      case 2:
        return TravelMode.transit;
      case 3:
        return TravelMode.driving;
      default:
        return TravelMode.walking;
    }
  }
}
