// lib/services/route_service.dart
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:google_maps_flutter/google_maps_flutter.dart';

class RouteResult {
  final List<LatLng> polyline;
  final int totalSeconds;
  final double totalKm;

  RouteResult({
    required this.polyline,
    required this.totalSeconds,
    required this.totalKm,
  });
}

class RouteService {
  // TODO: Aynı Google key'ini buraya koy (foto için kullandığın)
  static const String _apiKey = 'AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0';

  static Future<RouteResult?> fetchRoute(List<LatLng> points) async {
    if (points.length < 2) return null;

    final origin = points.first;
    final destination = points.last;

    // Ortadaki noktalar waypoints
    String waypoints = '';
    if (points.length > 2) {
      final mid = points.sublist(1, points.length - 1);
      waypoints =
          '&waypoints=optimize:true|${mid.map((p) => '${p.latitude},${p.longitude}').join('|')}';
    }

    final url = Uri.parse(
      'https://maps.googleapis.com/maps/api/directions/json'
      '?origin=${origin.latitude},${origin.longitude}'
      '&destination=${destination.latitude},${destination.longitude}'
      '&mode=walking$waypoints'
      '&key=$_apiKey',
    );

    final res = await http.get(url);
    if (res.statusCode != 200) return null;

    final data = jsonDecode(res.body);
    if (data['routes'] == null || (data['routes'] as List).isEmpty) {
      return null;
    }

    final route = data['routes'][0];
    final encoded = route['overview_polyline']['points'] as String;
    final legs = (route['legs'] as List);

    int totalSeconds = 0;
    double totalMeters = 0;
    for (final leg in legs) {
      totalSeconds += (leg['duration']['value'] as num).toInt();
      totalMeters += (leg['distance']['value'] as num).toDouble();
    }

    final decoded = _decodePolyline(encoded);

    return RouteResult(
      polyline: decoded,
      totalSeconds: totalSeconds,
      totalKm: totalMeters / 1000.0,
    );
  }

  // Google polyline decode
  static List<LatLng> _decodePolyline(String encoded) {
    List<LatLng> poly = [];
    int index = 0;
    int len = encoded.length;
    int lat = 0;
    int lng = 0;

    while (index < len) {
      int b;
      int shift = 0;
      int result = 0;

      do {
        b = encoded.codeUnitAt(index++) - 63;
        result |= (b & 0x1f) << shift;
        shift += 5;
      } while (b >= 0x20);

      int dlat = (result & 1) != 0 ? ~(result >> 1) : (result >> 1);
      lat += dlat;

      shift = 0;
      result = 0;

      do {
        b = encoded.codeUnitAt(index++) - 63;
        result |= (b & 0x1f) << shift;
        shift += 5;
      } while (b >= 0x20);

      int dlng = (result & 1) != 0 ? ~(result >> 1) : (result >> 1);
      lng += dlng;

      poly.add(LatLng(lat / 1e5, lng / 1e5));
    }

    return poly;
  }
}
