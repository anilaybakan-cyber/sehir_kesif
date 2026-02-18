class RecommendationsModel {
  final List<String> breakfast;
  final List<String> coffee;
  final List<String> dinner;
  final List<String> bars;
  final List<String> hiddenGems;

  RecommendationsModel({
    required this.breakfast,
    required this.coffee,
    required this.dinner,
    required this.bars,
    required this.hiddenGems,
  });

  factory RecommendationsModel.fromJson(Map<String, dynamic> json) {
    return RecommendationsModel(
      breakfast: List<String>.from(json['breakfast']),
      coffee: List<String>.from(json['coffee']),
      dinner: List<String>.from(json['dinner']),
      bars: List<String>.from(json['bars']),
      hiddenGems: List<String>.from(json['hidden_gems']),
    );
  }
}
