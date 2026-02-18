class RegionModel {
  final String name;
  final String type;
  final String price;
  final List<String> highlights;

  RegionModel({
    required this.name,
    required this.type,
    required this.price,
    required this.highlights,
  });

  factory RegionModel.fromJson(Map<String, dynamic> json) {
    return RegionModel(
      name: json['name'],
      type: json['type'],
      price: json['price'],
      highlights: List<String>.from(json['highlights']),
    );
  }
}
