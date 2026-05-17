import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:google_maps_flutter/google_maps_flutter.dart';

import '../secrets.dart';
import '../l10n/app_localizations.dart';

class DirectionsService {
  static const String _baseUrl =
      'https://maps.googleapis.com/maps/api/directions/json';

  /// Başlangıç ve Bitiş noktaları arasındaki rotayı getirir.
  /// Waypoints: Aradaki duraklar
  /// Mode: walking, driving, transit
  /// optimizeWaypoints: Google Maps API waypoints optimizasyonu
  Future<Map<String, dynamic>?> getDirections({
    required LatLng origin,
    required LatLng destination,
    List<LatLng>? waypoints,
    String mode = 'walking',
    bool optimizeWaypoints = false,
  }) async {
    
    // 1. Durakları string formatına çevir
    String waypointsString = "";
    if (mode != 'transit' && waypoints != null && waypoints.isNotEmpty) {
      if (optimizeWaypoints) {
        waypointsString = "optimize:true|" + waypoints.map((e) => "${e.latitude},${e.longitude}").join("|");
      } else {
        // Standard waypoints (no via:) for reliable itinerary legs
        waypointsString = waypoints.map((e) => "${e.latitude},${e.longitude}").join("|");
      }
    }

    // 2. İsteği oluştur
    final queryParameters = {
      'origin': '${origin.latitude},${origin.longitude}',
      'destination': '${destination.latitude},${destination.longitude}',
      'key': Secrets.googleMapsApiKey,
      'mode': mode,
      'language': AppLocalizations.instance.isEnglish ? 'en' : 'tr',
    };

    // Transit mode requires departure_time
    if (mode == 'transit') {
      final now = DateTime.now();
      DateTime departure;
      
      // ÖZEL DURUM: Fransa'da (Marseille vb.) 1 Mayıs'ta ulaşım tamamen durur.
      if (now.month == 5 && now.day == 1) {
        departure = DateTime(now.year, 5, 2, 10, 0);
      } else {
        // Her zaman bir timestamp gönderelim (Google 'now' yerine bunu daha stabil işleyebilir)
        departure = now;
      }
      queryParameters['departure_time'] = (departure.millisecondsSinceEpoch ~/ 1000).toString();
      queryParameters['routing_preference'] = 'fewer_transfers';
    }

    if (waypointsString.isNotEmpty) {
      queryParameters['waypoints'] = waypointsString;
    }

    final uri = Uri.parse(_baseUrl).replace(queryParameters: queryParameters);

    try {
      final response = await http.get(uri);

      if (response.statusCode == 200) {
        final data = json.decode(response.body);
        return _parseResponse(data, mode);
      }
    } catch (e) {
      print("Directions API Error: $e");
    }
    return null;
  }

  // Ortak Parse Metodu
  Map<String, dynamic>? _parseResponse(dynamic data, String requestMode) {
    final status = data['status'] as String?;
    if (status != null && status != 'OK') {
      final err = data['error_message'] as String?;
      print(
        'Directions API status: $status'
        '${err != null && err.isNotEmpty ? ' — $err' : ''}',
      );
      return null;
    }

    final routes = (data['routes'] as List<dynamic>? ?? []);
    if (routes.isEmpty) return null;

    dynamic selectedRoute = routes.first;
    if (requestMode == 'transit' && routes.length > 1) {
      selectedRoute = _selectBestTransitRoute(routes) ?? routes.first;
    }

    final overviewRaw = selectedRoute['overview_polyline'];
    String? overviewEncoded;
    if (overviewRaw is Map && overviewRaw['points'] is String) {
      overviewEncoded = overviewRaw['points'] as String;
    }
    if (overviewEncoded == null || overviewEncoded.isEmpty) {
      print('Directions API: overview_polyline eksik');
      return null;
    }

    // Mesafe ve Süre bilgisi (Legs toplamı)
    double totalDistanceMeters = 0;
    double totalDurationSeconds = 0;

    // Step-by-step route details for multi-modal visualization
    final List<Map<String, dynamic>> routeSteps = [];

    final legs = selectedRoute['legs'] as List<dynamic>? ?? [];
    for (var leg in legs) {
      final dist = leg['distance']?['value'];
      final dur = leg['duration']?['value'];
      if (dist is num) totalDistanceMeters += dist.toDouble();
      if (dur is num) totalDurationSeconds += dur.toDouble();

      final stepList = leg['steps'] as List<dynamic>? ?? [];
      for (var step in stepList) {
        if (step is! Map) continue;

        final polyMap = step['polyline'];
        String enc = '';
        if (polyMap is Map && polyMap['points'] is String) {
          enc = polyMap['points'] as String;
        }
        final decodedPts =
            enc.isEmpty ? <LatLng>[] : _decodePolyline(enc);

        final durStep = step['duration'];
        final distStep = step['distance'];
        final stepData = <String, dynamic>{
          'travel_mode': step['travel_mode'] ?? 'WALKING',
          'duration_seconds': durStep is Map && durStep['value'] is num
              ? (durStep['value'] as num).toDouble()
              : 0.0,
          'duration_text':
              durStep is Map ? (durStep['text'] as String? ?? '') : '',
          'distance_meters': distStep is Map && distStep['value'] is num
              ? (distStep['value'] as num).toDouble()
              : 0.0,
          'polyline': enc,
          'polyline_points': decodedPts,
          'instructions': step['html_instructions'] ?? '',
        };

        // Add transit details if available
        final String tMode =
            (step['travel_mode'] ?? '').toString().toUpperCase();
        if ((tMode == 'TRANSIT' || step['transit_details'] != null) &&
            step['transit_details'] != null) {
          final transit = step['transit_details'] as Map<String, dynamic>;
          stepData['transit_details'] = {
            'line_name': transit['line']?['short_name'] ??
                transit['line']?['name'] ??
                '',
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
      'polyline_points': _decodePolyline(overviewEncoded),
      'distance_text': _formatDistance(totalDistanceMeters),
      'duration_text': _formatDuration(totalDurationSeconds),
      'duration_seconds': totalDurationSeconds,
      'bounds': selectedRoute['bounds'],
      'steps': routeSteps,
    };
  }

  dynamic _selectBestTransitRoute(List<dynamic> routes) {
    dynamic bestRoute;
    int bestTransitStepCount = -1;
    double bestDurationSeconds = double.infinity;

    for (final route in routes) {
      final legs = route['legs'] as List<dynamic>? ?? [];
      int transitStepCount = 0;
      double totalDuration = 0;

      for (final leg in legs) {
        final legDuration = leg['duration']?['value'];
        if (legDuration is num) {
          totalDuration += legDuration.toDouble();
        }
        final steps = leg['steps'] as List<dynamic>? ?? [];
        for (final step in steps) {
          if ((step['travel_mode'] as String? ?? '').toUpperCase() == 'TRANSIT') {
            transitStepCount += 1;
          }
        }
      }

      final isBetterDuration = totalDuration < bestDurationSeconds - 60; // En az 1 dakika fark varsa
      final similarDurationButFewerTransfers = (totalDuration - bestDurationSeconds).abs() <= 60 && transitStepCount < bestTransitStepCount;
      
      if (isBetterDuration || similarDurationButFewerTransfers || bestRoute == null) {
        bestTransitStepCount = transitStepCount;
        bestDurationSeconds = totalDuration;
        bestRoute = route;
      }
    }

    return bestRoute;
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
