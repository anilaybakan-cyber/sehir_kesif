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

  // 🔥 YENİ: Görsel sistemi
  final String? imageUrl;
  final List<String> images; // Birden fazla fotoğraf için
  final String? videoUrl;

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
    this.images = const [],
    this.videoUrl,
  });

  // 🔥 Fallback görsel (Unsplash'ten otomatik çeker)
  String get displayImage {
    if (imageUrl != null && imageUrl!.isNotEmpty) return imageUrl!;
    if (images.isNotEmpty) return images.first;

    // Unsplash'ten kategori bazlı görsel
    final query = _getUnsplashQuery();
    return 'https://source.unsplash.com/800x600/?$query';
  }

  String _getUnsplashQuery() {
    switch (category.toLowerCase()) {
      case 'turistik':
        return 'landmark,architecture,monument';
      case 'lokal':
        return 'local,street,market';
      case 'instagramlik':
        return 'aesthetic,colorful,beautiful';
      case 'chill':
        return 'beach,relax,nature';
      case 'yemek':
        return 'food,restaurant,cuisine';
      default:
        return name.replaceAll(' ', ',');
    }
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
      images:
          (json["images"] as List?)?.map((e) => e.toString()).toList() ?? [],
      videoUrl: json["videoUrl"] as String?,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      "name": name,
      "area": area,
      "category": category,
      "tags": tags,
      "distanceFromCenter": distanceFromCenter,
      "lat": lat,
      "lng": lng,
      "price": price,
      "description": description,
      "imageUrl": imageUrl,
      "images": images,
      "videoUrl": videoUrl,
    };
  }
}
