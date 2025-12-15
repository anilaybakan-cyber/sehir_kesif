import 'dart:convert';
import 'package:http/http.dart' as http;

class FoursquarePhotoService {
  static const String apiKey =
      "fsq3zPCpGPvKh94yzfpp7j3IcTdkQ9YPlfRpsxwwlEuU3Ak";

  /// ============================================
  /// 1) NAME NORMALIZER (Catalan ↔ English fixes)
  /// ============================================
  static List<String> generateQueries(String name, String city) {
    final base = _clean(name);

    final variants = <String>[
      base,
      "$base $city",
      "$base near $city",
      "$city $base",

      // Catalan → English normalizations
      base.replaceAll("Parc", "Park"),
      base.replaceAll("Mercat", "Market"),
      base.replaceAll("Barri", "District"),
      base.replaceAll("Gòtic", "Gothic"),
      base.replaceAll("Playa", "Beach"),
      base.replaceAll("Platja", "Beach"),
      base.replaceAll("Basílica", "Basilica"),

      // Inverse
      base.replaceAll("Park", "Parc"),
      base.replaceAll("Market", "Mercat"),
      base.replaceAll("Gothic", "Gòtic"),
    ];

    // Parts
    final words = base.split(" ");
    if (words.length > 1) {
      variants.add(words.first);
      variants.add(words.sublist(0, 2).join(" "));
    }

    // Aksan temiz
    final noAccents = _removeAccents(base);
    variants.add(noAccents);
    variants.add("$noAccents $city");

    return variants.map((e) => e.trim()).toSet().toList();
  }

  static String _clean(String s) {
    return s
        .replaceAll("(", "")
        .replaceAll(")", "")
        .replaceAll("'", "")
        .replaceAll("´", "")
        .replaceAll("`", "")
        .replaceAll("·", "")
        .trim();
  }

  static String _removeAccents(String s) {
    const accents = {
      'á': 'a',
      'à': 'a',
      'ä': 'a',
      'â': 'a',
      'é': 'e',
      'è': 'e',
      'ë': 'e',
      'ê': 'e',
      'í': 'i',
      'ï': 'i',
      'ó': 'o',
      'ò': 'o',
      'ö': 'o',
      'ô': 'o',
      'ú': 'u',
      'ü': 'u',
      'ç': 'c',
      'ñ': 'n',
      '·': '',
    };

    return s.split('').map((c) => accents[c] ?? c).join();
  }

  /// ============================================
  /// 2) SMART SEARCH (mass multi-query)
  /// ============================================
  static Future<String?> searchPlaceIdByName(String name, String city) async {
    final queries = generateQueries(name, city);

    for (final q in queries) {
      final url = Uri.parse(
        "https://api.foursquare.com/v3/places/search?"
        "query=$q&near=$city&limit=1",
      );

      final res = await http.get(
        url,
        headers: {"Authorization": apiKey, "accept": "application/json"},
      );

      if (res.statusCode == 200) {
        final data = jsonDecode(res.body);
        if (data["results"] != null && data["results"].isNotEmpty) {
          return data["results"][0]["fsq_id"];
        }
      }
    }

    return null;
  }

  /// ============================================
  /// 3) SMART NEARBY (coordinate fallback)
  /// ============================================
  static Future<String?> searchPlaceNearby(double? lat, double? lng) async {
    if (lat == null || lng == null) return null;

    final url = Uri.parse(
      "https://api.foursquare.com/v3/places/nearby?"
      "ll=$lat,$lng&radius=200&limit=1",
    );

    final res = await http.get(
      url,
      headers: {"Authorization": apiKey, "accept": "application/json"},
    );

    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      if (data["results"] != null && data["results"].isNotEmpty) {
        return data["results"][0]["fsq_id"];
      }
    }

    return null;
  }

  /// ============================================
  /// 4) GET PHOTO FROM ID
  /// ============================================
  static Future<String?> getPhotoUrl(String fsqId) async {
    final url = Uri.parse(
      "https://api.foursquare.com/v3/places/$fsqId/photos?limit=1",
    );

    final res = await http.get(
      url,
      headers: {"Authorization": apiKey, "accept": "application/json"},
    );

    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      if (data is List && data.isNotEmpty) {
        final p = data[0];
        return "${p["prefix"]}1000x800${p["suffix"]}";
      }
    }

    return null;
  }

  /// ============================================
  /// 5) MAIN FETCH FUNCTION
  /// ============================================
  static Future<String?> fetchPhoto(
    String name,
    String city, {
    double? lat,
    double? lng,
  }) async {
    // 1) Name search
    String? fsqId = await searchPlaceIdByName(name, city);

    // 2) Nearby fallback
    if (fsqId == null && lat != null && lng != null) {
      fsqId = await searchPlaceNearby(lat, lng);
    }

    if (fsqId == null) return null;

    return await getPhotoUrl(fsqId);
  }
}
