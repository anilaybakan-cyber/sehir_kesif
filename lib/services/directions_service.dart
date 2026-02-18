import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:google_maps_flutter/google_maps_flutter.dart';

import 'package:flutter/services.dart' show rootBundle;
import '../secrets.dart';
import '../l10n/app_localizations.dart';

class DirectionsService {
  static const String _baseUrl =
      'https://maps.googleapis.com/maps/api/directions/json';

  /// Başlangıç ve Bitiş noktaları arasındaki rotayı getirir.
  /// Waypoints: Aradaki duraklar
  /// Mode: walking, bicycling, driving, transit
  /// routeId: Eğer belirtilirse, önce assets/routes/{routeId}.json dosyasından okumayı dener (Maliyet: 0)
  Future<Map<String, dynamic>?> getDirections({
    required LatLng origin,
    required LatLng destination,
    List<LatLng>? waypoints,
    String mode = 'walking',
    String? routeId,
  }) async {
    
    // 0. Static Rota Kontrolü (Hız & Maliyet için)
    // Dosya adı: {routeId}_{mode}.json (örn: bcn_gaudi_walking.json)
    if (routeId != null) {
      try {
        final jsonString = await rootBundle.loadString('assets/routes/${routeId}_$mode.json');
        final data = json.decode(jsonString);
        print("✅ Static route loaded: ${routeId}_$mode (Cost: \$0)");
        return _parseResponse(data);
      } catch (e) {
        print("⚠️ Static route not found, falling back to API: ${routeId}_$mode");
        // Dosya yoksa API'ye devam et
      }
    }

    // 1. Durakları string formatına çevir (via:lat,lng|via:lat,lng...)
    String waypointsString = "";
    if (mode != 'transit' && waypoints != null && waypoints.isNotEmpty) {
      waypointsString = waypoints
          .map((e) => "via:${e.latitude},${e.longitude}")
          .join("|");
    }

    // 2. İsteği oluştur
    final queryParameters = {
      'origin': '${origin.latitude},${origin.longitude}',
      'destination': '${destination.latitude},${destination.longitude}',
      'key': Secrets.googleMapsApiKey,
      'mode': mode,
    };

    if (waypointsString.isNotEmpty) {
      queryParameters['waypoints'] = waypointsString;
    }

    final uri = Uri.parse(_baseUrl).replace(queryParameters: queryParameters);

    try {
      final response = await http.get(uri);

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return _parseResponse(data);
      }
    } catch (e) {
      print("Directions API Error: $e");
    }
    return null;
  }

  // Ortak Parse Metodu
  Map<String, dynamic>? _parseResponse(dynamic data) {
    if ((data['routes'] as List).isEmpty) return null;

    // Rota verisi (Polyline string)
    final overviewPolyline = data['routes'][0]['overview_polyline']['points'];

    // Mesafe ve Süre bilgisi (Legs toplamı)
    double totalDistanceMeters = 0;
    double totalDurationSeconds = 0;

    // Step-by-step route details for multi-modal visualization
    final List<Map<String, dynamic>> routeSteps = [];

    for (var leg in data['routes'][0]['legs']) {
      totalDistanceMeters += (leg['distance']['value'] as num).toDouble();
      totalDurationSeconds += (leg['duration']['value'] as num).toDouble();

      // Extract steps for multi-modal display
      for (var step in leg['steps']) {
        final stepData = <String, dynamic>{
          'travel_mode': step['travel_mode'],
          'duration_seconds': step['duration']['value'],
          'duration_text': step['duration']['text'],
          'distance_meters': step['distance']['value'],
          'polyline': step['polyline']['points'],
          'polyline_points': _decodePolyline(step['polyline']['points']),
          'instructions': step['html_instructions'] ?? '',
        };

        // Add transit details if available
        if (step['travel_mode'] == 'TRANSIT' && step['transit_details'] != null) {
          final transit = step['transit_details'];
          stepData['transit_details'] = {
            'line_name': transit['line']?['short_name'] ?? transit['line']?['name'] ?? '',
            'vehicle_type': transit['line']?['vehicle']?['type'] ?? 'BUS',
            'vehicle_name': transit['line']?['vehicle']?['name'] ?? '',
            'departure_stop': transit['departure_stop']?['name'] ?? '',
            'arrival_stop': transit['arrival_stop']?['name'] ?? '',
            'num_stops': transit['num_stops'] ?? 0,
            'color': transit['line']?['color'] ?? '#2196F3',
          };
        }

        routeSteps.add(stepData);
      }
    }

    return {
      'polyline_points': _decodePolyline(overviewPolyline),
      'distance_text': _formatDistance(totalDistanceMeters),
      'duration_text': _formatDuration(totalDurationSeconds),
      'duration_seconds': totalDurationSeconds,
      'bounds': data['routes'][0]['bounds'],
      'steps': routeSteps,
    };
  }

  // Encoded String'i LatLng listesine çevirir (Polyline Algorithm)
  List<LatLng> _decodePolyline(String encoded) {
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

  String _formatDistance(double meters) {
    if (meters < 1000) return "${meters.round()} m";
    return AppLocalizations.instance.km((meters / 1000).toStringAsFixed(1).replaceAll(" km", "")); 
  }

  String _formatDuration(double seconds) {
    final int minutes = (seconds / 60).round();
    if (minutes < 60) return "$minutes ${AppLocalizations.instance.t('dk', 'min')}"; 
    final int hours = minutes ~/ 60;
    final int remainingMinutes = minutes % 60;
    return "$hours ${AppLocalizations.instance.t('sa', 'hr')} $remainingMinutes ${AppLocalizations.instance.t('dk', 'min')}";
  }
}
