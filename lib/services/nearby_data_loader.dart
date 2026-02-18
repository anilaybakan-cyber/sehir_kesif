import '../models/place_model.dart';

class NearbyDataLoader {
  static Future<List<PlaceModel>> loadPlaces() async {
    await Future.delayed(const Duration(milliseconds: 400));

    final mockData = [
      {
        "name": "Nomad Coffee",
        "category": "Kafe",
        "distance_km": 0.2,
        "rating": 4.8,
        "address": "Passatge Sert 12, Gracia",
        "is_open": true,
        "imageUrl":
            "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
      },
      {
        "name": "Can Culleretes",
        "category": "Restoran",
        "distance_km": 0.4,
        "rating": 4.2,
        "address": "Carrer d'en Quintana 5",
        "is_open": false,
        "imageUrl":
            "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800",
      },
      {
        "name": "El Nacional",
        "category": "Restoran",
        "distance_km": 0.5,
        "rating": 4.6,
        "address": "Passeig de Gràcia 24",
        "is_open": true,
        "imageUrl":
            "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=800",
      },
      {
        "name": "Satan's Coffee Corner",
        "category": "Kafe",
        "distance_km": 0.7,
        "rating": 4.9,
        "address": "Carrer de l'Arc de Sant Ramon",
        "is_open": true,
        "imageUrl":
            "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800",
      },
      {
        "name": "Paradiso",
        "category": "Bar",
        "distance_km": 0.7,
        "rating": 4.7,
        "address": "Carrer de Rera Palau 4",
        "is_open": false,
        "imageUrl":
            "https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800",
      },
      {
        "name": "Picasso Museum",
        "category": "Müze",
        "distance_km": 0.9,
        "rating": 4.5,
        "address": "Carrer Montcada 15-23",
        "is_open": true,
        "imageUrl":
            "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Museu_Picasso_Barcelona_-_panoramio.jpg/800px-Museu_Picasso_Barcelona_-_panoramio.jpg",
      },
      {
        "name": "Federal Café",
        "category": "Kafe",
        "distance_km": 1.1,
        "rating": 4.4,
        "address": "Carrer del Parlament 39",
        "is_open": true,
        "imageUrl":
            "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800",
      },
      {
        "name": "Bar Mut",
        "category": "Bar",
        "distance_km": 1.3,
        "rating": 4.3,
        "address": "Carrer de Pau Claris 192",
        "is_open": true,
        "imageUrl":
            "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800",
      },
    ];

    return mockData.map((e) => PlaceModel.fromJson(e)).toList();
  }
}
