import 'dart:convert';
import 'package:http/http.dart' as http;

class GooglePhotoService {
  static const apiKey = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g";

  // Mekan ID bul (name + city)
  static Future<String?> searchPlaceId(String name, String city) async {
    final query = Uri.encodeComponent("$name $city");

    final url = Uri.parse(
      "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
      "?input=$query"
      "&inputtype=textquery"
      "&fields=place_id"
      "&key=$apiKey",
    );

    final res = await http.get(url);

    if (res.statusCode == 200) {
      final data = jsonDecode(res.body);
      if (data["candidates"] != null && data["candidates"].isNotEmpty) {
        return data["candidates"][0]["place_id"];
      }
    }
    return null;
  }

  // Fotoğraf URL al
  static Future<String?> getPhotoUrl(String placeId) async {
    final url = Uri.parse(
      "https://maps.googleapis.com/maps/api/place/details/json"
      "?place_id=$placeId"
      "&fields=photo"
      "&key=$apiKey",
    );

    final res = await http.get(url);
    if (res.statusCode != 200) return null;

    final data = jsonDecode(res.body);

    if (data["result"]?["photos"] != null &&
        data["result"]["photos"].isNotEmpty) {
      final photoRef = data["result"]["photos"][0]["photo_reference"];
      return _photoUrl(photoRef);
    }
    return null;
  }

  // Direct photo URL generator
  static String _photoUrl(String reference) {
    return "https://maps.googleapis.com/maps/api/place/photo"
        "?maxwidth=1200"
        "&photo_reference=$reference"
        "&key=$apiKey";
  }

  // Tek adımda fotoğraf bul
  static Future<String?> fetchPhoto(String name, String city) async {
    final id = await searchPlaceId(name, city);
    if (id == null) return null;
    return await getPhotoUrl(id);
  }
}
