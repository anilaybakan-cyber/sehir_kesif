import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import '../secrets.dart';

class DirectionsService {
  static const String _baseUrl =
      'https://maps.googleapis.com/maps/api/directions/json';

  /// Başlangıç ve Bitiş noktaları arasındaki rotayı getirir.
  /// Waypoints: Aradaki duraklar
  Future<Map<String, dynamic>?> getDirections({
    required LatLng origin,
    required LatLng destination,
    List<LatLng>? waypoints,
  }) async {
    // 1. Durakları string formatına çevir (via:lat,lng|via:lat,lng...)
    String waypointsString = "";
    if (waypoints != null && waypoints.isNotEmpty) {
      waypointsString = waypoints
          .map((e) => "via:${e.latitude},${e.longitude}")
          .join("|");
    }

    // 2. İsteği oluştur
    final queryParameters = {
      'origin': '${origin.latitude},${origin.longitude}',
      'destination': '${destination.latitude},${destination.longitude}',
      'key': Secrets.googleMapsApiKey,
      'mode': 'walking', // Yürüyüş modu
    };

    if (waypointsString.isNotEmpty) {
      queryParameters['waypoints'] = waypointsString;
    }

    final uri = Uri.parse(_baseUrl).replace(queryParameters: queryParameters);

    try {
      final response = await http.get(uri);

      if (response.statusCode == 200) {
        final data = json.decode(response.body);

        if ((data['routes'] as List).isEmpty) return null;

        // Rota verisi (Polyline string)
        final overviewPolyline =
            data['routes'][0]['overview_polyline']['points'];

        // Mesafe ve Süre bilgisi (Legs toplamı)
        // Waypoint varsa birden fazla "leg" olur, bunları toplamalıyız.
        double totalDistanceMeters = 0;
        double totalDurationSeconds = 0;

        for (var leg in data['routes'][0]['legs']) {
          totalDistanceMeters += leg['distance']['value'];
          totalDurationSeconds += leg['duration']['value'];
        }

        return {
          'polyline_points': _decodePolyline(overviewPolyline),
          'distance_text': _formatDistance(totalDistanceMeters),
          'duration_text': _formatDuration(totalDurationSeconds),
          'bounds': data['routes'][0]['bounds'], // Haritayı ortalamak için
        };
      }
    } catch (e) {
      print("Directions API Hatası: $e");
    }
    return null;
  }

  // Encoded String'i LatLng listesine çevirir
  // Encoded String'i LatLng listesine çevirir
  List<LatLng> _decodePolyline(String encoded) {
    // DÜZELTME 1: Parantez içi boş olmalı. (apiKey parametresi yok)
    PolylinePoints polylinePoints = PolylinePoints();

    // DÜZELTME 2: Büyük harfle başlayan Class ismiyle değil,
    // yukarıda oluşturduğumuz küçük harfli 'polylinePoints' değişkeniyle çağırıyoruz.
    List<PointLatLng> result = polylinePoints.decodePolyline(encoded);

    return result.map((p) => LatLng(p.latitude, p.longitude)).toList();
  }

  String _formatDistance(double meters) {
    if (meters < 1000) return "${meters.round()} m";
    return "${(meters / 1000).toStringAsFixed(1)} km";
  }

  String _formatDuration(double seconds) {
    final int minutes = (seconds / 60).round();
    if (minutes < 60) return "$minutes dk";
    final int hours = minutes ~/ 60;
    final int remainingMinutes = minutes % 60;
    return "$hours sa $remainingMinutes dk";
  }
}
