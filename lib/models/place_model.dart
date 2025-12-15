class PlaceModel {
  final String name;
  final String category;
  final double distanceKm;
  final double rating;
  final String address;
  final bool isOpen;
  final String? imageUrl;

  PlaceModel({
    required this.name,
    required this.category,
    required this.distanceKm,
    required this.rating,
    required this.address,
    required this.isOpen,
    this.imageUrl,
  });

  factory PlaceModel.fromJson(Map<String, dynamic> json) {
    return PlaceModel(
      name: json['name'],
      category: json['category'],
      distanceKm: (json['distance_km'] as num).toDouble(),
      rating: (json['rating'] as num).toDouble(),
      address: json['address'],
      isOpen: json['is_open'],
      imageUrl: json['imageUrl'],
    );
  }
}
