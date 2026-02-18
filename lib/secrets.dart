import 'package:flutter_dotenv/flutter_dotenv.dart';

class Secrets {
  // Google Cloud Console'dan aldığın API Key'i buraya yapıştır.
  // Lütfen Console'da "Maps SDK for iOS", "Maps SDK for Android"
  // ve "Directions API" servislerini aktif ettiğinden emin ol.
  static String get googleMapsApiKey {
    final key = dotenv.env['GOOGLE_MAPS_API_KEY'];
    if (key == null || key.isEmpty) {
      // Fallback or empty, but preferably should prevent app start if critical
      return "";
    }
    return key;
  }
}
