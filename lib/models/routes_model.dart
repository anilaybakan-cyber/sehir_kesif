import 'package:hive/hive.dart';
import '../models/city_model.dart';
part 'routes_model.g.dart';

@HiveType(typeId: 3)
class RouteModel {
  @HiveField(0)
  final String id;

  @HiveField(1)
  final String city;

  @HiveField(2)
  final List<Highlight> places;

  @HiveField(3)
  final DateTime createdAt;

  RouteModel({
    required this.id,
    required this.city,
    required this.places,
    required this.createdAt,
  });
}
