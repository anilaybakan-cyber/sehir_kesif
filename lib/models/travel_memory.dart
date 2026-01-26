// =============================================================================
// TRAVEL MEMORY MODEL
// Kullanıcının seyahat anılarını temsil eden model
// =============================================================================



class TravelMemory {
  final String id;
  final String cityId;
  final String cityName;
  final String imagePath; // Local file path
  final String? note;
  final DateTime date;
  final DateTime createdAt;

  TravelMemory({
    required this.id,
    required this.cityId,
    required this.cityName,
    required this.imagePath,
    this.note,
    required this.date,
    required this.createdAt,
  });

  // Generate unique ID
  static String generateId() {
    return '${DateTime.now().millisecondsSinceEpoch}_${DateTime.now().microsecond}';
  }

  // JSON serialization
  Map<String, dynamic> toJson() => {
    'id': id,
    'cityId': cityId,
    'cityName': cityName,
    'imagePath': imagePath,
    'note': note,
    'date': date.toIso8601String(),
    'createdAt': createdAt.toIso8601String(),
  };

  factory TravelMemory.fromJson(Map<String, dynamic> json) => TravelMemory(
    id: json['id'] as String,
    cityId: json['cityId'] as String,
    cityName: json['cityName'] as String,
    imagePath: json['imagePath'] as String,
    note: json['note'] as String?,
    date: DateTime.parse(json['date'] as String),
    createdAt: DateTime.parse(json['createdAt'] as String),
  );

  // Copy with
  TravelMemory copyWith({
    String? note,
    DateTime? date,
  }) => TravelMemory(
    id: id,
    cityId: cityId,
    cityName: cityName,
    imagePath: imagePath,
    note: note ?? this.note,
    date: date ?? this.date,
    createdAt: createdAt,
  );

  @override
  String toString() => 'TravelMemory($cityName, $date)';
}
