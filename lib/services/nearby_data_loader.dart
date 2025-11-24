import '../models/city_model.dart';

class NearbyDataLoader {
  static Future<List<Highlight>> loadNearbyPlaces() async {
    await Future.delayed(const Duration(milliseconds: 400)); // mini delay

    final mockData = [
      {
        "name": "Nomad Coffee",
        "area": "Gràcia",
        "category": "lokal",
        "tags": ["kahve", "çalışma", "wifi"],
        "distanceFromCenter": 0.2,
        "lat": 41.4036,
        "lng": 2.1586,
        "price": "medium",
        "description":
            "Barcelona'nın en iyi specialty coffee mekanlarından biri. Sakin atmosfer, hızlı wifi ve lezzetli kahveler.",
        "displayImage":
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
        "images": [
          "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
          "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
        ],
      },
      {
        "name": "El Nacional",
        "area": "Eixample",
        "category": "lokal",
        "tags": ["restoran", "tapas", "şarap"],
        "distanceFromCenter": 0.5,
        "lat": 41.3926,
        "lng": 2.1637,
        "price": "high",
        "description":
            "Muhteşem mimarisi ve çeşitli mutfaklarıyla ünlü gastronomi merkezi. 4 farklı restoran bir arada.",
        "displayImage":
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
        "images": [
          "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
          "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800",
        ],
      },
      {
        "name": "Paradiso",
        "area": "El Born",
        "category": "lokal",
        "tags": ["bar", "kokteyl", "gece hayatı"],
        "distanceFromCenter": 1.1,
        "lat": 41.3851,
        "lng": 2.1834,
        "price": "high",
        "description":
            "Dünyanın en iyi barlarından biri. Gizli kapısıyla ünlü, yaratıcı kokteyller sunan speakeasy bar.",
        "displayImage":
            "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800",
        "images": [
          "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800",
          "https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800",
        ],
      },
      {
        "name": "La Boqueria Market",
        "area": "La Rambla",
        "category": "turistik",
        "tags": ["pazar", "yemek", "alışveriş"],
        "distanceFromCenter": 0.9,
        "lat": 41.3818,
        "lng": 2.1713,
        "price": "medium",
        "description":
            "Barcelona'nın en ünlü pazarı. Taze meyve, deniz ürünleri, tapas ve yerel lezzetler.",
        "displayImage":
            "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
        "images": [
          "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
          "https://images.unsplash.com/photo-1488459716781-31db52582fe9?w=800",
        ],
      },
      {
        "name": "Barceloneta Beach",
        "area": "Barceloneta",
        "category": "chill",
        "tags": ["plaj", "deniz", "güneş"],
        "distanceFromCenter": 1.3,
        "lat": 41.3773,
        "lng": 2.1900,
        "price": "free",
        "description":
            "Barcelona'nın en popüler plajı. Altın kumlar, beach bar'lar ve Akdeniz'in tadını çıkarın.",
        "displayImage":
            "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
        "images": [
          "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800",
          "https://images.unsplash.com/photo-1519046904884-53103b34b206?w=800",
        ],
      },
      {
        "name": "Park Güell",
        "area": "Gràcia",
        "category": "turistik",
        "tags": ["gaudí", "park", "manzara"],
        "distanceFromCenter": 2.1,
        "lat": 41.4145,
        "lng": 2.1527,
        "price": "medium",
        "description":
            "Gaudí'nin renkli mozaik eserleriyle süslü muhteşem parkı. Barcelona'nın en ikonik yerlerinden.",
        "displayImage":
            "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=800",
        "images": [
          "https://images.unsplash.com/photo-1523531294919-4bcd7c65e216?w=800",
          "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800",
        ],
      },
      {
        "name": "Bunkers del Carmel",
        "area": "El Carmel",
        "category": "instagramlik",
        "tags": ["manzara", "gün batımı", "fotoğraf"],
        "distanceFromCenter": 3.2,
        "lat": 41.4169,
        "lng": 2.1569,
        "price": "free",
        "description":
            "Barcelona'nın en iyi gün batımı noktası. 360 derece şehir manzarası ve ücretsiz giriş.",
        "displayImage":
            "https://images.unsplash.com/photo-1562883676-8c7feb83f09b?w=800",
        "images": [
          "https://images.unsplash.com/photo-1562883676-8c7feb83f09b?w=800",
          "https://images.unsplash.com/photo-1558642452-9d2a7deb7f62?w=800",
        ],
      },
      {
        "name": "Casa Batlló",
        "area": "Eixample",
        "category": "turistik",
        "tags": ["gaudí", "mimari", "müze"],
        "distanceFromCenter": 1.5,
        "lat": 41.3916,
        "lng": 2.1649,
        "price": "high",
        "description":
            "Gaudí'nin en ünlü eserlerinden biri. Renkli cephesi ve organik tasarımıyla büyüleyici.",
        "displayImage":
            "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
        "images": [
          "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800",
          "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800",
        ],
      },
    ];

    return mockData.map((e) => Highlight.fromJson(e)).toList();
  }
}
