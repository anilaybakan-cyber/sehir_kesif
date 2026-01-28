import 'package:geolocator/geolocator.dart';
import 'package:flutter/foundation.dart';
import '../models/city_model.dart';
import '../l10n/app_localizations.dart';

enum LocationMode {
  planning, // Remote: Distance from City Center
  travel,   // On-site: Distance from User
}

class LocationContextService with ChangeNotifier {
  static final LocationContextService _instance = LocationContextService._internal();
  static LocationContextService get instance => _instance;

  LocationContextService._internal();

  LocationMode _mode = LocationMode.planning;
  Position? _userPosition;
  double _cityCenterLat = 0;
  double _cityCenterLng = 0;

  LocationMode get mode => _mode;
  bool get isTravelMode => _mode == LocationMode.travel;

  /// Update context with the selected city
  /// Automatically determines mode based on distance to city center
  Future<void> updateContext(CityModel city) async {
    _cityCenterLat = city.centerLat;
    _cityCenterLng = city.centerLng;

    try {
        final permission = await Geolocator.checkPermission();
        if (permission == LocationPermission.denied || permission == LocationPermission.deniedForever) {
            _setMode(LocationMode.planning);
            return;
        }

        _userPosition = await Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.medium);
        
        if (_userPosition != null) {
            final distanceToCity = Geolocator.distanceBetween(
                _userPosition!.latitude, 
                _userPosition!.longitude, 
                _cityCenterLat, 
                _cityCenterLng
            );

            // If within 50km, assume Travel Mode
            if (distanceToCity < 50000) {
                _setMode(LocationMode.travel);
            } else {
                _setMode(LocationMode.planning);
            }
        }
    } catch (e) {
        debugPrint("LocationContextService error: $e");
        _setMode(LocationMode.planning);
    }
  }

  void _setMode(LocationMode newMode) {
    if (_mode != newMode) {
        _mode = newMode;
        notifyListeners();
        debugPrint("Location Mode changed to: $_mode");
    }
  }

  /// Calculates distance to a target point
  /// Returns distance in meters based on current mode
  double getDistance(double targetLat, double targetLng) {
    if (_mode == LocationMode.travel && _userPosition != null) {
        return Geolocator.distanceBetween(
            _userPosition!.latitude, 
            _userPosition!.longitude, 
            targetLat, 
            targetLng
        );
    } else {
        // Planning mode: Distance from City Center
        return Geolocator.distanceBetween(
            _cityCenterLat, 
            _cityCenterLng, 
            targetLat, 
            targetLng
        );
    }
  }

  /// Returns a formatted label for the distance
  /// e.g. "Merkeze 1.2 km" or "Sana 500 m"
  String getDistanceLabel(double targetLat, double targetLng) {
    final dist = getDistance(targetLat, targetLng);
    final isEnglish = AppLocalizations.instance.isEnglish;
    final distStr = dist >= 1000 
        ? "${(dist / 1000).toStringAsFixed(1)} km" 
        : "${dist.toInt()} m";

    // User requested only distance value for UI compactness
    return distStr;
  }
}
