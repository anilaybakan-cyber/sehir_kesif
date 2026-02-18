import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:http/http.dart' as http;
import 'curated_routes_service.dart';
import 'directions_service.dart';
import 'city_data_loader.dart';
import '../models/city_model.dart';
import '../secrets.dart';

class RouteBakerService {
  static final DirectionsService _directionsService = DirectionsService();

  /// Bakes a single route for a specific mode (e.g., 'transit', 'walking')
  /// Returns the JSON string ready to be saved to a file.
  static Future<String?> bakeRoute({
    required String cityId,
    required String routeId,
    required String mode,
  }) async {
    debugPrint("🍞 Baking route: $routeId ($mode) for city: $cityId...");

    // 1. Load City Data to find places
    CityModel city;
    try {
      city = await CityDataLoader.loadCity(cityId);
    } catch (e) {
      debugPrint("❌ Failed to load city $cityId: $e");
      return null;
    }

    // 2. Find the CuratedRoute definition
    final routes = CuratedRoutesService.getRoutes(cityId, true);
    
    CuratedRoute? targetRoute;
    try {
      targetRoute = routes.firstWhere((r) => r.id == routeId);
    } catch (e) {
        debugPrint("❌ Route ID $routeId not found in $cityId");
        return null;
    }

    if (targetRoute == null) return null;

    // 3. Resolve Waypoints
    List<LatLng> points = [];
    for (var name in targetRoute.placeNames) {
      try {
         final place = city.highlights.firstWhere((p) => 
           p.name.toLowerCase() == name.toLowerCase() || 
           (p.nameEn != null && p.nameEn!.toLowerCase() == name.toLowerCase())
         );
         points.add(LatLng(place.lat, place.lng));
      } catch (e) {
        debugPrint("⚠️ Warning: Place '$name' not found in city data. Skipping.");
      }
    }

    if (points.length < 2) {
      debugPrint("❌ Not enough points found for route $routeId (Found: ${points.length})");
      return null;
    }

    // 4. Zero-Cost Routing Implementation
    dynamic rawResult;
    
    if (mode == 'walking') {
      debugPrint("🚶 Use OSRM (Zero-Cost Walking)...");
      rawResult = await _bakeWithOSRM(points);
    } else if (mode == 'transit') {
      if (Secrets.hereApiKey.isEmpty) {
         debugPrint("⚠️ HERE API Key missing. Falling back to Google (Paid) for transit.");
         final origin = points.first;
         final destination = points.last;
         final waypoints = points.sublist(1, points.length - 1);
         rawResult = await _directionsService.getDirections(
           origin: origin,
           destination: destination,
           waypoints: waypoints,
           mode: mode,
           routeId: null,
         );
      } else {
         debugPrint("🚌 Use HERE (Zero-Cost Transit)...");
         rawResult = await _bakeWithHERE(points);
      }
    }

    if (rawResult == null) {
      debugPrint("❌ Baking failed for $routeId");
      return null;
    }

    // 5. Serialize
    JsonEncoder encoder = const JsonEncoder.withIndent('  ');
    String prettyJson = encoder.convert(rawResult);
    
    // 🔥 AI Capture Tags
    debugPrint("\n---BEGIN_BAKE---\nFILENAME: ${routeId}_$mode.json\nCONTENT:\n$prettyJson\n---END_BAKE---\n");
    
    debugPrint("✅ Done baking $routeId ($mode)");
    return prettyJson;
  }

  /// OSRM Implementation (Open Source Routing Machine) - TOTALLY FREE
  static Future<Map<String, dynamic>?> _bakeWithOSRM(List<LatLng> points) async {
    final coords = points.map((p) => "${p.longitude},${p.latitude}").join(";");
    final url = "http://router.project-osrm.org/route/v1/walking/$coords?overview=full&geometries=polyline&steps=true";
    
    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['code'] == 'Ok') {
          final route = data['routes'][0];
          
          // Calculate bounds from polyline
          final geometry = route['geometry'] as String;
          final polyPoints = _decodePolyline(geometry);
          final bounds = _calculateBounds(polyPoints);

          return {
            "routes": [
              {
                "overview_polyline": {"points": geometry},
                "legs": [
                  {
                    "distance": {"value": route['distance'], "text": "${(route['distance']/1000).toStringAsFixed(1)} km"},
                    "duration": {"value": route['duration'], "text": "${(route['duration']/60).toInt()} mins"},
                    "steps": (route['legs'] as List).expand((leg) => leg['steps']).map((step) {
                      return {
                        "travel_mode": "WALKING",
                        "distance": {"value": step['distance']},
                        "duration": {"value": step['duration']},
                        "polyline": {"points": step['geometry']},
                        "html_instructions": step['maneuver']['type'] + " " + (step['name'] ?? ""),
                      };
                    }).toList()
                  }
                ],
                "bounds": bounds
              }
            ],
            "status": "OK"
          };
        }
      }
    } catch (e) {
      debugPrint("❌ OSRM Error: $e");
    }
    return null;
  }

  /// HERE Maps Implementation - FREE Tier
  static Future<Map<String, dynamic>?> _bakeWithHERE(List<LatLng> points) async {
    final origin = points.first;
    final destination = points.last;
    final via = points.sublist(1, points.length - 1);
    
    String url = "https://router.hereapi.com/v8/routes?transportMode=publicTransport"
        "&origin=${origin.latitude},${origin.longitude}"
        "&destination=${destination.latitude},${destination.longitude}"
        "&return=polyline,summary,actions,instructions"
        "&apiKey=${Secrets.hereApiKey}";
    
    for (var p in via) {
      url += "&via=${p.latitude},${p.longitude}";
    }

    try {
      final response = await http.get(Uri.parse(url));
      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        if (data['routes'] != null && (data['routes'] as List).isNotEmpty) {
           final hRoute = data['routes'][0];
           final List<Map<String, dynamic>> legs = [];
           List<LatLng> allPoints = [];
           
           for (var hSection in hRoute['sections']) {
             final polyPoints = _decodePolyline(hSection['polyline']);
             allPoints.addAll(polyPoints);

             legs.add({
               "distance": {"value": hSection['summary']['length'], "text": ""},
               "duration": {"value": hSection['summary']['duration'], "text": ""},
               "steps": (hSection['actions'] as List? ?? []).map((action) {
                 return {
                   "travel_mode": hSection['type'] == 'pedestrian' ? "WALKING" : "TRANSIT",
                   "distance": {"value": 0},
                   "duration": {"value": 0},
                   "polyline": {"points": hSection['polyline']},
                   "html_instructions": action['instruction'] ?? "",
                 };
               }).toList()
             });
           }
           
           final bounds = _calculateBounds(allPoints);

           return {
             "routes": [
               {
                 "overview_polyline": {"points": hRoute['sections'][0]['polyline']},
                 "legs": legs,
                 "bounds": bounds
               }
             ],
             "status": "OK"
           };
        }
      }
    } catch (e) {
      debugPrint("❌ HERE Error: $e");
    }
    return null;
  }

  static Future<void> bakeAllRoutesForCity(String cityId) async {
    final routes = CuratedRoutesService.getRoutes(cityId, true);
    debugPrint("🥖 Starting zero-cost batch bake for ${routes.length} routes in $cityId");
    
    for (var route in routes) {
      await bakeRoute(cityId: cityId, routeId: route.id, mode: 'walking');
      await Future.delayed(const Duration(milliseconds: 500));
      
      if (Secrets.hereApiKey.isNotEmpty) {
        await bakeRoute(cityId: cityId, routeId: route.id, mode: 'transit');
        await Future.delayed(const Duration(milliseconds: 500));
      }
    }
    debugPrint("✅ Zero-cost batch bake complete for $cityId");
  }

  static Map<String, dynamic> _calculateBounds(List<LatLng> points) {
    if (points.isEmpty) {
      return {
        "northeast": {"lat": 0, "lng": 0},
        "southwest": {"lat": 0, "lng": 0}
      };
    }

    double minLat = 90.0, maxLat = -90.0, minLng = 180.0, maxLng = -180.0;
    for (var p in points) {
      if (p.latitude < minLat) minLat = p.latitude;
      if (p.latitude > maxLat) maxLat = p.latitude;
      if (p.longitude < minLng) minLng = p.longitude;
      if (p.longitude > maxLng) maxLng = p.longitude;
    }

    return {
      "northeast": {"lat": maxLat, "lng": maxLng},
      "southwest": {"lat": minLat, "lng": minLng}
    };
  }

  static List<LatLng> _decodePolyline(String encoded) {
    List<LatLng> points = [];
    int index = 0, len = encoded.length;
    int lat = 0, lng = 0;

    while (index < len) {
      int b, shift = 0, result = 0;
      do {
        b = encoded.codeUnitAt(index++) - 63;
        result |= (b & 0x1f) << shift;
        shift += 5;
      } while (b >= 0x20);
      int dlat = ((result & 1) != 0 ? ~(result >> 1) : (result >> 1));
      lat += dlat;

      shift = 0;
      result = 0;
      do {
        b = encoded.codeUnitAt(index++) - 63;
        result |= (b & 0x1f) << shift;
        shift += 5;
      } while (b >= 0x20);
      int dlng = ((result & 1) != 0 ? ~(result >> 1) : (result >> 1));
      lng += dlng;

      points.add(LatLng(lat / 1E5, lng / 1E5));
    }
    return points;
  }

  static Future<void> bakeAllCities() async {
    const cities = CityDataLoader.supportedCities;
    debugPrint("🌍 GLOBAL BAKE STARTED: ${cities.length} cities...");
    
    for (var cityId in cities) {
      debugPrint("🏙️ Preparing to bake: $cityId");
      await bakeAllRoutesForCity(cityId);
      // Wait a bit between cities to let the console catch up and avoid heavy spikes
      await Future.delayed(const Duration(seconds: 2));
    }
    debugPrint("🏁 ALL CITIES BAKED SUCCESSFULLY!");
  }
}
