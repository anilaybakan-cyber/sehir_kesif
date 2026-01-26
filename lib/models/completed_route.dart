
import 'dart:convert';

class CompletedRoute {
  final String id;
  final String name;
  final String cityName;
  final DateTime date;
  final int stopCount;
  final List<String> placeNames;

  CompletedRoute({
    required this.id,
    required this.name,
    required this.cityName,
    required this.date,
    required this.stopCount,
    required this.placeNames,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'name': name,
      'cityName': cityName,
      'date': date.toIso8601String(),
      'stopCount': stopCount,
      'placeNames': placeNames,
    };
  }

  factory CompletedRoute.fromMap(Map<String, dynamic> map) {
    return CompletedRoute(
      id: map['id'] ?? '',
      name: map['name'] ?? '',
      cityName: map['cityName'] ?? '',
      date: DateTime.parse(map['date']),
      stopCount: map['stopCount'] ?? 0,
      placeNames: List<String>.from(map['placeNames'] ?? []),
    );
  }

  String toJson() => json.encode(toMap());

  factory CompletedRoute.fromJson(String source) => CompletedRoute.fromMap(json.decode(source));
}
