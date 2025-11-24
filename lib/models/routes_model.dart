class RoutesModel {
  final List<String> touristic;
  final List<String> local;
  final List<String> ai;

  RoutesModel({required this.touristic, required this.local, required this.ai});

  factory RoutesModel.fromJson(Map<String, dynamic> json) {
    return RoutesModel(
      touristic: List<String>.from(json['touristic']),
      local: List<String>.from(json['local']),
      ai: List<String>.from(json['ai']),
    );
  }
}
