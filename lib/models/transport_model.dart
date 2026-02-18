class TransportModel {
  final String fastest;
  final String cheapest;
  final List<String> options;

  TransportModel({
    required this.fastest,
    required this.cheapest,
    required this.options,
  });

  factory TransportModel.fromJson(Map<String, dynamic> json) {
    return TransportModel(
      fastest: json['fastest'],
      cheapest: json['cheapest'],
      options: List<String>.from(json['options']),
    );
  }
}
