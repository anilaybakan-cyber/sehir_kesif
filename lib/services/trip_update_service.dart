import 'package:flutter/foundation.dart';

class TripUpdateService {
  // Singleton
  static final TripUpdateService _instance = TripUpdateService._internal();
  factory TripUpdateService() => _instance;
  TripUpdateService._internal();

  // Trip Notifier
  final ValueNotifier<int> _tripUpdated = ValueNotifier(0);
  ValueListenable<int> get tripUpdated => _tripUpdated;

  // City Change Notifier
  final ValueNotifier<int> _cityChanged = ValueNotifier(0);
  ValueListenable<int> get cityChanged => _cityChanged;

  // Tetikleyiciler
  void notifyTripChanged() {
    _tripUpdated.value++;
  }

  void notifyCityChanged() {
    _cityChanged.value++;
  }

  // Visit Notifier
  final ValueNotifier<int> _visitUpdated = ValueNotifier(0);
  ValueListenable<int> get visitUpdated => _visitUpdated;

  void notifyVisitChanged() {
    _visitUpdated.value++;
  }

  // Favorites Notifier
  final ValueNotifier<int> _favoritesUpdated = ValueNotifier(0);
  ValueListenable<int> get favoritesUpdated => _favoritesUpdated;

  void notifyFavoritesChanged() {
    _favoritesUpdated.value++;
  }
}
