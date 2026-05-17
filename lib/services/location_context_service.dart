import 'dart:async';

import 'package:flutter/foundation.dart';
import 'package:geolocator/geolocator.dart';

import '../l10n/app_localizations.dart';
import '../models/city_model.dart';

enum LocationMode {
  planning,
  travel,
}

enum LocationReferenceMode {
  auto,
  cityCenter,
  liveLocation,
}

enum LocationContextReason {
  automaticTravel,
  automaticCityCenter,
  manualCityCenter,
  manualLiveLocation,
  permissionDenied,
  permissionDeniedForever,
  serviceDisabled,
  locationUnavailable,
}

class LocationContextService with ChangeNotifier {
  static final LocationContextService _instance = LocationContextService._internal();
  static LocationContextService get instance => _instance;

  LocationContextService._internal();

  LocationMode _mode = LocationMode.planning;
  LocationReferenceMode _referenceMode = LocationReferenceMode.auto;
  LocationContextReason _reason = LocationContextReason.automaticCityCenter;
  Position? _userPosition;
  double _cityCenterLat = 0;
  double _cityCenterLng = 0;
  double _travelModeRadiusMeters = 15000;
  CityModel? _currentCity;
  StreamSubscription<Position>? _positionSubscription;
  bool _nearbyActive = false;

  LocationMode get mode => _mode;
  LocationReferenceMode get referenceMode => _referenceMode;
  LocationContextReason get reason => _reason;
  bool get isTravelMode => _mode == LocationMode.travel;
  double get travelModeRadiusKm => _travelModeRadiusMeters / 1000;
  ({double lat, double lng})? get currentUserCoordinate {
    if (_userPosition == null) return null;
    return (lat: _userPosition!.latitude, lng: _userPosition!.longitude);
  }

  String get statusTitle {
    final isEnglish = AppLocalizations.instance.isEnglish;
    if (_mode == LocationMode.travel) {
      return isEnglish ? "Based on your location" : "Konumun baz alınıyor";
    }
    return AppLocalizations.instance.basedOnCityCenter;
  }

  String get statusDescription {
    final isEnglish = AppLocalizations.instance.isEnglish;
    switch (_reason) {
      case LocationContextReason.automaticTravel:
        return isEnglish
            ? "You appear to be in the selected city, so distances are calculated from your current location."
            : "Seçili şehirde göründüğün için mesafeler mevcut konumuna göre hesaplanıyor.";
      case LocationContextReason.automaticCityCenter:
        return isEnglish
            ? "You appear to be outside the selected city, so distances are calculated from city center."
            : "Seçili şehrin dışında göründüğün için mesafeler şehir merkezine göre hesaplanıyor.";
      case LocationContextReason.manualCityCenter:
        return isEnglish
            ? "City center is selected manually for planning."
            : "Planlama için şehir merkezi manuel olarak seçildi.";
      case LocationContextReason.manualLiveLocation:
        return isEnglish
            ? "Your location is selected manually for nearby results."
            : "Yakındaki sonuçlar için konumun manuel olarak seçildi.";
      case LocationContextReason.permissionDenied:
        return isEnglish
            ? "Location permission was not granted, so city center is being used."
            : "Konum izni verilmediği için şehir merkezi kullanılıyor.";
      case LocationContextReason.permissionDeniedForever:
        return isEnglish
            ? "Location permission is permanently disabled, so city center is being used."
            : "Konum izni kalıcı olarak kapalı olduğu için şehir merkezi kullanılıyor.";
      case LocationContextReason.serviceDisabled:
        return isEnglish
            ? "Location services are off, so city center is being used."
            : "Konum servisleri kapalı olduğu için şehir merkezi kullanılıyor.";
      case LocationContextReason.locationUnavailable:
        return isEnglish
            ? "Your location could not be determined, so city center is being used."
            : "Konumun alınamadığı için şehir merkezi kullanılıyor.";
    }
  }

  Future<void> updateContext(CityModel city) async {
    _currentCity = city;
    _cityCenterLat = city.centerLat;
    _cityCenterLng = city.centerLng;
    _travelModeRadiusMeters = _calculateTravelModeRadius(city);
    await _resolveContext();
  }

  Future<void> setNearbyActive(bool active) async {
    _nearbyActive = active;
    if (!_nearbyActive) {
      await _stopPositionStream();
      return;
    }
    if (_currentCity != null && _referenceMode != LocationReferenceMode.cityCenter) {
      await _resolveContext();
    }
  }

  Future<bool> setReferenceMode(
    LocationReferenceMode mode, {
    bool requestPermissionIfNeeded = false,
  }) async {
    final previousMode = _referenceMode;
    final modeChanged = _referenceMode != mode;
    _referenceMode = mode;
    final success = await _resolveContext(
      requestPermissionIfNeeded: requestPermissionIfNeeded,
      forceNotify: modeChanged,
    );

    if (!success && mode == LocationReferenceMode.liveLocation) {
      _referenceMode = previousMode;
      await _resolveContext(forceNotify: true);
    }

    return success;
  }

  Future<bool> _resolveContext({
    bool requestPermissionIfNeeded = false,
    bool forceNotify = false,
  }) async {
    if (_currentCity == null) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.locationUnavailable,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return false;
    }

    if (_referenceMode == LocationReferenceMode.cityCenter) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.manualCityCenter,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return true;
    }

    final servicesEnabled = await Geolocator.isLocationServiceEnabled();
    if (!servicesEnabled) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.serviceDisabled,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return false;
    }

    var permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied && requestPermissionIfNeeded) {
      permission = await Geolocator.requestPermission();
    }

    if (permission == LocationPermission.denied) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.permissionDenied,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return false;
    }

    if (permission == LocationPermission.deniedForever) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.permissionDeniedForever,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return false;
    }

    try {
      _userPosition = await Geolocator.getCurrentPosition(
        desiredAccuracy: LocationAccuracy.medium,
        timeLimit: const Duration(seconds: 5),
      );
    } catch (e) {
      debugPrint("LocationContextService: GPS Timeout or error: $e");
      _userPosition = null;
    }

    if (_userPosition == null) {
      _setResolvedState(
        mode: LocationMode.planning,
        reason: LocationContextReason.locationUnavailable,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return false;
    }

    if (_referenceMode == LocationReferenceMode.liveLocation) {
      _setResolvedState(
        mode: LocationMode.travel,
        reason: LocationContextReason.manualLiveLocation,
        forceNotify: forceNotify,
      );
      await _syncPositionTracking();
      return true;
    }

    _resolveAutoModeFromPosition(_userPosition!, forceNotify: forceNotify);
    await _syncPositionTracking();
    return true;
  }

  void _resolveAutoModeFromPosition(
    Position position, {
    bool forceNotify = false,
  }) {
    final distanceToCity = Geolocator.distanceBetween(
      position.latitude,
      position.longitude,
      _cityCenterLat,
      _cityCenterLng,
    );

    if (distanceToCity <= _travelModeRadiusMeters) {
      _setResolvedState(
        mode: LocationMode.travel,
        reason: LocationContextReason.automaticTravel,
        forceNotify: forceNotify,
      );
      return;
    }

    _setResolvedState(
      mode: LocationMode.planning,
      reason: LocationContextReason.automaticCityCenter,
      forceNotify: forceNotify,
    );
  }

  Future<void> _syncPositionTracking() async {
    final shouldTrack =
        _nearbyActive &&
        _currentCity != null &&
        _referenceMode != LocationReferenceMode.cityCenter;

    if (!shouldTrack) {
      await _stopPositionStream();
      return;
    }

    final servicesEnabled = await Geolocator.isLocationServiceEnabled();
    if (!servicesEnabled) {
      await _stopPositionStream();
      return;
    }

    final permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied ||
        permission == LocationPermission.deniedForever) {
      await _stopPositionStream();
      return;
    }

    await _startPositionStream();
  }

  Future<void> _startPositionStream() async {
    if (_positionSubscription != null) return;

    _positionSubscription = Geolocator.getPositionStream(
      locationSettings: const LocationSettings(
        accuracy: LocationAccuracy.medium,
        distanceFilter: 100,
      ),
    ).listen(
      (position) {
        _userPosition = position;
        if (_referenceMode == LocationReferenceMode.liveLocation) {
          _setResolvedState(
            mode: LocationMode.travel,
            reason: LocationContextReason.manualLiveLocation,
            forceNotify: true,
          );
          return;
        }

        if (_referenceMode == LocationReferenceMode.auto) {
          _resolveAutoModeFromPosition(position, forceNotify: true);
        }
      },
      onError: (error) {
        debugPrint("LocationContextService stream error: $error");
      },
    );
  }

  Future<void> _stopPositionStream() async {
    await _positionSubscription?.cancel();
    _positionSubscription = null;
  }

  double _calculateTravelModeRadius(CityModel city) {
    final distances = city.highlights
        .where((highlight) => highlight.lat != 0 && highlight.lng != 0)
        .map(
          (highlight) => Geolocator.distanceBetween(
            city.centerLat,
            city.centerLng,
            highlight.lat,
            highlight.lng,
          ),
        )
        .where((distance) => distance > 0)
        .toList()
      ..sort();

    if (distances.isEmpty) {
      return 15000;
    }

    final percentileIndex = ((distances.length - 1) * 0.8).floor();
    final percentileDistance = distances[percentileIndex];
    final bufferedDistance = percentileDistance + 5000;
    return bufferedDistance.clamp(15000, 50000).toDouble();
  }

  void _setResolvedState({
    required LocationMode mode,
    required LocationContextReason reason,
    bool forceNotify = false,
  }) {
    final stateChanged = _mode != mode || _reason != reason;
    _mode = mode;
    _reason = reason;

    if (stateChanged || forceNotify) {
      notifyListeners();
      debugPrint(
        "Location state changed: mode=$_mode reference=$_referenceMode reason=$_reason radiusKm=${travelModeRadiusKm.toStringAsFixed(1)}",
      );
    }
  }

  double getDistance(double targetLat, double targetLng) {
    if (_mode == LocationMode.travel && _userPosition != null) {
      return Geolocator.distanceBetween(
        _userPosition!.latitude,
        _userPosition!.longitude,
        targetLat,
        targetLng,
      );
    }

    return Geolocator.distanceBetween(
      _cityCenterLat,
      _cityCenterLng,
      targetLat,
      targetLng,
    );
  }

  String getDistanceLabel(double targetLat, double targetLng) {
    final dist = getDistance(targetLat, targetLng);
    final distStr = dist >= 1000
        ? "${(dist / 1000).toStringAsFixed(1)} km"
        : "${dist.toInt()} m";
    return distStr;
  }
}
