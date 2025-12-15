import 'package:flutter/foundation.dart';

class TripUpdateService {
  // Singleton
  static final TripUpdateService _instance = TripUpdateService._internal();
  factory TripUpdateService() => _instance;
  TripUpdateService._internal();

  // Notifier
  final ValueNotifier<int> _tripUpdated = ValueNotifier(0);
  
  ValueListenable<int> get tripUpdated => _tripUpdated;

  // Tetikleyici
  void notifyTripChanged() {
    _tripUpdated.value++;
  }
}
