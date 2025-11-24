class CityModel {
  final String city;
  final double centerLat;
  final double centerLng;
  final List<Highlight> highlights;

  CityModel({
    required this.city,
    required this.centerLat,
    required this.centerLng,
    required this.highlights,
  });

  factory CityModel.fromJson(Map<String, dynamic> json) {
    final center = json["centerCoords"] as List? ?? [0.0, 0.0];

    return CityModel(
      city: json["city"] ?? "",
      centerLat: (center[0] as num).toDouble(),
      centerLng: (center[1] as num).toDouble(),
      highlights: (json["highlights"] as List)
          .map((e) => Highlight.fromJson(e))
          .toList(),
    );
  }
}

class Highlight {
  final String name;
  final String area;
  final String category;
  final List<String> tags;
  final double distanceFromCenter;

  final double lat;
  final double lng;

  final String price;
  final String description;

  final String? imageUrl;
  final String displayImage;

  Highlight({
    required this.name,
    required this.area,
    required this.category,
    required this.tags,
    required this.distanceFromCenter,
    required this.lat,
    required this.lng,
    required this.price,
    required this.description,
    this.imageUrl,
    required this.displayImage,
  });

  // 🔥 IMAGES GETTER
  List<String> get images {
    List<String> result = [];

    // imageUrl varsa ekle
    if (imageUrl != null && imageUrl!.isNotEmpty) {
      result.add(imageUrl!);
    }

    // displayImage varsa ve zaten listede yoksa ekle
    if (displayImage.isNotEmpty && !result.contains(displayImage)) {
      result.add(displayImage);
    }

    // Hiç görsel yoksa placeholder ekle
    if (result.isEmpty) {
      result.add("https://via.placeholder.com/400x300?text=No+Image");
    }

    return result;
  }

  factory Highlight.fromJson(Map<String, dynamic> json) {
    return Highlight(
      name: json["name"] ?? "",
      area: json["area"] ?? "",
      category: json["category"] ?? "",
      tags: (json["tags"] as List?)?.map((e) => e.toString()).toList() ?? [],
      distanceFromCenter:
          (json["distanceFromCenter"] as num?)?.toDouble() ?? 0.0,
      lat: (json["lat"] as num?)?.toDouble() ?? 0.0,
      lng: (json["lng"] as num?)?.toDouble() ?? 0.0,
      price: json["price"] ?? "medium",
      description: json["description"] ?? "",
      imageUrl: json["imageUrl"] as String?,
      displayImage:
          json["displayImage"] ??
          "https://via.placeholder.com/400x300?text=No+Image",
    );
  }
}
