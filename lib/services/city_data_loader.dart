import 'dart:convert';
import 'package:flutter/services.dart';
import '../models/city_model.dart';

class CityDataLoader {
  static Future<CityModel> loadCity(String cityName) async {
    final safe = cityName.toLowerCase().trim();
    final data = await rootBundle.loadString("assets/cities/$safe.json");
    final jsonData = json.decode(data) as Map<String, dynamic>;
    return CityModel.fromJson(jsonData);
  }
}
