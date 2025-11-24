import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/city_model.dart';
import '../config/api_config.dart';

class AIService {
  /// Kullanıcı profiline göre gerçek AI önerileri üretir
  static Future<List<Highlight>> getSerendipityRecommendations({
    required String city,
    required String travelStyle,
    required List<String> interests,
    required double moodLevel, // 0.0 (Yorgun) - 1.0 (Enerjik)
  }) async {
    try {
      // AI'ya gönderilecek prompt
      String prompt = _buildPrompt(city, travelStyle, interests, moodLevel);

      // OpenAI API isteği
      final response = await http.post(
        Uri.parse('${ApiConfig.openAiBaseUrl}/chat/completions'),
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ${ApiConfig.openAiApiKey}',
        },
        body: jsonEncode({
          'model': 'gpt-4',
          'messages': [
            {
              'role': 'system',
              'content':
                  'Sen bir seyahat uzmanısın. Kullanıcılara kişiselleştirilmiş, sürpriz yerler öneriyorsun. JSON formatında yanıt ver.',
            },
            {'role': 'user', 'content': prompt},
          ],
          'temperature': 0.8,
          'max_tokens': 1500,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(utf8.decode(response.bodyBytes));
        final aiResponse = data['choices'][0]['message']['content'];

        // AI'dan gelen JSON'u parse et
        return _parseAIResponse(aiResponse);
      } else {
        print('AI API Hatası: ${response.statusCode}');
        return _getFallbackRecommendations(moodLevel);
      }
    } catch (e) {
      print('AI Servisi Hatası: $e');
      return _getFallbackRecommendations(moodLevel);
    }
  }

  /// AI için prompt oluştur
  static String _buildPrompt(
    String city,
    String travelStyle,
    List<String> interests,
    double moodLevel,
  ) {
    String mood = moodLevel < 0.3
        ? "yorgun ve dinlenmek istiyor"
        : moodLevel < 0.7
        ? "orta enerjili"
        : "çok enerjik ve macera peşinde";

    String styleText = travelStyle == "tourist"
        ? "turistik"
        : travelStyle == "local"
        ? "lokal ve otantik"
        : travelStyle == "instagram"
        ? "Instagram'lık ve fotojenik"
        : "sakin ve rahat";

    return '''
$city şehrinde gezecek bir kullanıcı için 3 sürpriz yer öner.

Kullanıcı Profili:
- Seyahat Tarzı: $styleText
- İlgi Alanları: ${interests.join(", ")}
- Şu anki Ruh Hali: $mood

Lütfen turistlerin pek bilmediği, özel yerler öner. Her yer için şu JSON formatını kullan:

[
  {
    "name": "Yer Adı",
    "area": "Bölge/Mahalle",
    "category": "lokal",
    "tags": ["etiket1", "etiket2"],
    "distanceFromCenter": 2.5,
    "lat": 41.3851,
    "lng": 2.1734,
    "price": "low",
    "description": "AI Önerisi: Kişiselleştirilmiş açıklama (kullanıcının ruh haline göre)",
    "imageUrl": null,
    "displayImage": "https://images.unsplash.com/photo-example"
  }
]

Sadece JSON array döndür, başka açıklama ekleme.
''';
  }

  /// AI'dan gelen yanıtı parse et
  static List<Highlight> _parseAIResponse(String aiResponse) {
    try {
      // JSON'u temizle (bazen AI ekstra metin ekleyebilir)
      String cleanJson = aiResponse.trim();
      if (cleanJson.startsWith('```json')) {
        cleanJson = cleanJson.substring(7);
      }
      if (cleanJson.startsWith('```')) {
        cleanJson = cleanJson.substring(3);
      }
      if (cleanJson.endsWith('```')) {
        cleanJson = cleanJson.substring(0, cleanJson.length - 3);
      }
      cleanJson = cleanJson.trim();

      final List<dynamic> jsonList = jsonDecode(cleanJson);

      return jsonList.map((json) => Highlight.fromJson(json)).toList();
    } catch (e) {
      print('AI Yanıtı Parse Hatası: $e');
      return _getFallbackRecommendations(0.5);
    }
  }

  /// API başarısız olursa fallback öneriler
  static List<Highlight> _getFallbackRecommendations(double moodLevel) {
    if (moodLevel < 0.3) {
      return [
        Highlight(
          name: "Gizli Kitap Kafe",
          area: "Arka Sokaklar",
          category: "chill",
          tags: ["kitap", "kahve", "sessiz"],
          distanceFromCenter: 1.2,
          lat: 41.3851,
          lng: 2.1734,
          price: "low",
          description:
              "AI Önerisi: Şu an yorgunsun, burası kalabalıktan kaçıp dinlenmek için şehirdeki en iyi nokta.",
          imageUrl: null,
          displayImage:
              "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800",
        ),
        Highlight(
          name: "Gün Batımı Terası",
          area: "Liman",
          category: "chill",
          tags: ["manzara", "kokteyl"],
          distanceFromCenter: 2.5,
          lat: 41.3851,
          lng: 2.1734,
          price: "medium",
          description:
              "AI Önerisi: Fazla yürümeden şehrin en iyi manzarasını buradan izleyebilirsin.",
          imageUrl: null,
          displayImage:
              "https://images.unsplash.com/photo-1514933651103-005eec06c04b?w=800",
        ),
      ];
    }

    return [
      Highlight(
        name: "Sokak Sanatı Turu",
        area: "Sanayi Bölgesi",
        category: "lokal",
        tags: ["sanat", "yürüyüş", "fotoğraf"],
        distanceFromCenter: 4.0,
        lat: 41.3851,
        lng: 2.1734,
        price: "free",
        description:
            "AI Önerisi: Enerjin yüksek! Turistlerin gitmediği bu bölgedeki graffitiler tam senlik.",
        imageUrl: null,
        displayImage:
            "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?w=800",
      ),
      Highlight(
        name: "Gece Pazarı",
        area: "Merkez",
        category: "lokal",
        tags: ["sokak lezzetleri", "kalabalık"],
        distanceFromCenter: 0.5,
        lat: 41.3851,
        lng: 2.1734,
        price: "low",
        description:
            "AI Önerisi: Aç mısın? Yerlilerin iş çıkışı uğradığı bu pazarı kaçırma.",
        imageUrl: null,
        displayImage:
            "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800",
      ),
      Highlight(
        name: "Yerel Müzisyenlerin Barı",
        area: "Gotik Mahalle",
        category: "lokal",
        tags: ["müzik", "gece hayatı", "canlı performans"],
        distanceFromCenter: 1.8,
        lat: 41.3851,
        lng: 2.1734,
        price: "medium",
        description:
            "AI Önerisi: Canlı müzik seversin! Bu gece burada yerel sanatçılar sahne alıyor.",
        imageUrl: null,
        displayImage:
            "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800",
      ),
    ];
  }
}
