import 'dart:convert';
import 'dart:io';
import 'package:sehir_kesif/services/google_photo_service.dart';

void main() async {
  final cities = [
    {"path": "assets/cities/barcelona.json", "name": "Barcelona"},
  ];

  for (final city in cities) {
    await updateCityPhotos(city["path"]!, city["name"]!);
  }
}

Future<void> updateCityPhotos(String jsonPath, String cityName) async {
  print("\n🔍 Loading: $jsonPath");
  final file = File(jsonPath);
  
  if (!await file.exists()) {
    print("❌ File not found: $jsonPath");
    return;
  }
  
  final data = jsonDecode(await file.readAsString());

  // ---------------------------------------------------------
  // 1) HIGHLIGHTS / MEKANLAR
  // ---------------------------------------------------------
  final highlights = data["highlights"] as List;

  for (final h in highlights) {
    final name = h["name"];
    print("➡️ Processing: $name");

    // Her zaman yeni fotoğraf çek
    final photo = await GooglePhotoService.fetchPhoto(name, cityName);

    if (photo != null) {
      print("   ✅ Google Photo FOUND");
      h["imageUrl"] = photo;
    } else {
      print("   ❌ No Google photo found for $name");
    }
  }

  // ---------------------------------------------------------
  // 2) JSON KAYDET
  // ---------------------------------------------------------
  await file.writeAsString(const JsonEncoder.withIndent("  ").convert(data));

  print("🎉 DONE — $cityName JSON updated!");
}
