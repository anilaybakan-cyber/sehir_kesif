// =============================================================================
// PHOTO SERVICE - Yüksek Kaliteli Fotoğraf Yönetimi
// - Wikimedia Commons API entegrasyonu
// - Unsplash fallback
// - Local caching
// - Placeholder sistemi
// =============================================================================

import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'package:crypto/crypto.dart';

class PhotoService {
  // Wikimedia Commons API endpoint
  static const String _wikimediaApi = 'https://commons.wikimedia.org/w/api.php';

  // Cache süresi (7 gün)
  static const Duration _cacheDuration = Duration(days: 7);

  // Önbellek key prefix
  static const String _cachePrefix = 'photo_cache_';

  /// Mekan için en iyi fotoğrafı getir
  /// Önce cache'e bakar, yoksa API'den çeker
  static Future<String?> getPhotoUrl({
    required String placeName,
    required String city,
    String? category,
    int width = 800,
  }) async {
    // 1. Cache'e bak
    final cacheKey = _getCacheKey(placeName, city);
    final cachedUrl = await _getCachedPhoto(cacheKey);
    if (cachedUrl != null) {
      return cachedUrl;
    }

    // 2. Wikimedia'dan ara
    String? photoUrl = await _searchWikimediaCommons(
      query: '$placeName $city',
      width: width,
    );

    // 3. Bulunamadıysa sadece mekan adıyla dene
    if (photoUrl == null) {
      photoUrl = await _searchWikimediaCommons(query: placeName, width: width);
    }

    // 4. Cache'e kaydet
    if (photoUrl != null) {
      await _cachePhoto(cacheKey, photoUrl);
    }

    return photoUrl;
  }

  /// Wikimedia Commons'ta fotoğraf ara
  static Future<String?> _searchWikimediaCommons({
    required String query,
    int width = 800,
  }) async {
    try {
      // API isteği oluştur
      final uri = Uri.parse(_wikimediaApi).replace(
        queryParameters: {
          'action': 'query',
          'format': 'json',
          'generator': 'search',
          'gsrnamespace': '6', // File namespace
          'gsrsearch': 'filetype:bitmap $query',
          'gsrlimit': '5',
          'prop': 'imageinfo',
          'iiprop': 'url|size|mime',
          'iiurlwidth': width.toString(),
        },
      );

      final response = await http.get(uri).timeout(const Duration(seconds: 10));

      if (response.statusCode != 200) return null;

      final data = json.decode(response.body);
      final pages = data['query']?['pages'] as Map<String, dynamic>?;

      if (pages == null || pages.isEmpty) return null;

      // En uygun fotoğrafı seç (en yüksek çözünürlük)
      String? bestUrl;
      int bestWidth = 0;

      for (final page in pages.values) {
        final imageInfo = (page['imageinfo'] as List?)?.first;
        if (imageInfo == null) continue;

        final thumbUrl = imageInfo['thumburl'] as String?;
        final thumbWidth = imageInfo['thumbwidth'] as int? ?? 0;
        final mime = imageInfo['mime'] as String? ?? '';

        // Sadece JPEG ve PNG kabul et
        if (!mime.contains('jpeg') && !mime.contains('png')) continue;

        if (thumbUrl != null && thumbWidth > bestWidth) {
          bestUrl = thumbUrl;
          bestWidth = thumbWidth;
        }
      }

      return bestUrl;
    } catch (e) {
      debugPrint('Wikimedia API hatası: $e');
      return null;
    }
  }

  /// Önceden tanımlı yüksek kaliteli fotoğraflar
  /// Popüler turistik mekanlar için manuel seçilmiş URL'ler
  static final Map<String, String> _curatedPhotos = {
    // Barcelona
    'Sagrada Familia':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/Basilica_de_la_Sagrada_Familia_-_panoramio_%283%29.jpg/1280px-Basilica_de_la_Sagrada_Familia_-_panoramio_%283%29.jpg',
    'Park Güell':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Parc_G%C3%BCell_-_Entrada_Drac.JPG/1280px-Parc_G%C3%BCell_-_Entrada_Drac.JPG',
    'Casa Batlló':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Casa_Batll%C3%B3_%288623240352%29.jpg/1024px-Casa_Batll%C3%B3_%288623240352%29.jpg',
    'La Boqueria':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Mercat_de_la_Boqueria.jpg/1280px-Mercat_de_la_Boqueria.jpg',
    'Gothic Quarter':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Barri_G%C3%B2tic_-_Barcelona_%28Catalonia%29.jpg/1280px-Barri_G%C3%B2tic_-_Barcelona_%28Catalonia%29.jpg',
    'Camp Nou':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/57/2019-06-11_Altenburger_Stra%C3%9Fe_1_by_OlsaW_MG_1381.jpg/1280px-2019-06-11_Altenburger_Stra%C3%9Fe_1_by_OlsaW_MG_1381.jpg',
    'Montjuïc':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Castell_de_Montju%C3%AFc_-_panoramio_%281%29.jpg/1280px-Castell_de_Montju%C3%AFc_-_panoramio_%281%29.jpg',
    'Bunkers del Carmel':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Bunkers_del_Carmel_-_panoramio.jpg/1280px-Bunkers_del_Carmel_-_panoramio.jpg',

    // Paris
    'Eiffel Kulesi':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg/800px-Tour_Eiffel_Wikimedia_Commons_%28cropped%29.jpg',
    'Louvre Müzesi':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Louvre_Museum_Wikimedia_Commons.jpg/1280px-Louvre_Museum_Wikimedia_Commons.jpg',
    'Notre-Dame Katedrali':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Notre-Dame_de_Paris%2C_4_October_2017.jpg/1280px-Notre-Dame_de_Paris%2C_4_October_2017.jpg',
    'Sacré-Cœur Bazilikası':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Le_sacre_coeur.jpg/1280px-Le_sacre_coeur.jpg',
    'Arc de Triomphe':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Arc_de_Triomphe%2C_Paris_21_October_2010.jpg/1280px-Arc_de_Triomphe%2C_Paris_21_October_2010.jpg',
    'Musée d\'Orsay':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Mus%C3%A9e_d%27Orsay%2C_North-West_view%2C_Paris_7e_140402.jpg/1280px-Mus%C3%A9e_d%27Orsay%2C_North-West_view%2C_Paris_7e_140402.jpg',
    'Centre Pompidou':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Centre_Georges-Pompidou_34.jpg/1280px-Centre_Georges-Pompidou_34.jpg',
    'Jardin du Luxembourg':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Luxembourg_Garden.jpg/1280px-Luxembourg_Garden.jpg',
    'Montmartre':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Montmartre_amanecer.jpg/1280px-Montmartre_amanecer.jpg',
    'Pont Alexandre III':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Pont_Alexandre_III_-_01.jpg/1280px-Pont_Alexandre_III_-_01.jpg',

    // Roma
    'Colosseum':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Colosseo_2020.jpg/1280px-Colosseo_2020.jpg',
    'Pantheon':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Rome_Pantheon_front.jpg/1280px-Rome_Pantheon_front.jpg',
    'Vatikan Müzeleri':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Sistine_Chapel_ceiling_photo_2.jpg/1280px-Sistine_Chapel_ceiling_photo_2.jpg',
    'San Pietro Bazilikası':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg/1280px-Basilica_di_San_Pietro_in_Vaticano_September_2015-1a.jpg',
    'Trevi Çeşmesi':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d9/Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg/1280px-Trevi_Fountain%2C_Rome%2C_Italy_2_-_May_2007.jpg',
    'Piazza Navona':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Piazza_Navona_2020.jpg/1280px-Piazza_Navona_2020.jpg',
    'Foro Romano':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Forum_Romanum_Rom.jpg/1280px-Forum_Romanum_Rom.jpg',
    'Spanish Steps':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Spanische_Treppe_Rom.jpg/1280px-Spanische_Treppe_Rom.jpg',
    'Trastevere':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Trastevere_-_panoramio_%289%29.jpg/1280px-Trastevere_-_panoramio_%289%29.jpg',
    'Villa Borghese':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Villa_Borghese_Park_in_Rome.jpg/1280px-Villa_Borghese_Park_in_Rome.jpg',

    // İstanbul
    'Ayasofya':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Hagia_Sophia_Mars_2013.jpg/1280px-Hagia_Sophia_Mars_2013.jpg',
    'Sultanahmet Camii':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Blue_Mosque_Courtyard_Dusk_Wikimedia_Commons.jpg/1280px-Blue_Mosque_Courtyard_Dusk_Wikimedia_Commons.jpg',
    'Topkapı Sarayı':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Topkap%C4%B1_-_01.jpg/1280px-Topkap%C4%B1_-_01.jpg',
    'Galata Kulesi':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Galata_Tower%2C_Istanbul.jpg/800px-Galata_Tower%2C_Istanbul.jpg',
    'Yerebatan Sarnıcı':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Basilica_Cistern_Yerebatan_Istanbul.jpg/1280px-Basilica_Cistern_Yerebatan_Istanbul.jpg',
    'Dolmabahçe Sarayı':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Dolmabah%C3%A7e_Palace.jpg/1280px-Dolmabah%C3%A7e_Palace.jpg',
    'Kapalıçarşı':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Kapalicarsi-2023-11-DSC05497.jpg/1280px-Kapalicarsi-2023-11-DSC05497.jpg',
    'Ortaköy':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Ortakoy_Mosque_and_Bosphorus_Bridge.jpg/1280px-Ortakoy_Mosque_and_Bosphorus_Bridge.jpg',
    'Kız Kulesi':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Kiz_Kulesi_Sunset.jpg/1280px-Kiz_Kulesi_Sunset.jpg',
    'Boğaz':
        'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Bosphorus._Istanbul%2C_Turkey.jpg/1280px-Bosphorus._Istanbul%2C_Turkey.jpg',
  };

  /// Küratörlü fotoğraf URL'i getir (varsa)
  static String? getCuratedPhoto(String placeName) {
    return _curatedPhotos[placeName];
  }

  /// Tüm küratörlü fotoğrafları getir
  static Map<String, String> getAllCuratedPhotos() {
    return Map.from(_curatedPhotos);
  }

  /// Cache key oluştur
  static String _getCacheKey(String placeName, String city) {
    final input = '$placeName|$city'.toLowerCase();
    final bytes = utf8.encode(input);
    final hash = md5.convert(bytes);
    return '$_cachePrefix${hash.toString()}';
  }

  /// Cache'den fotoğraf URL'i getir
  static Future<String?> _getCachedPhoto(String key) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final cached = prefs.getString(key);
      if (cached == null) return null;

      final data = json.decode(cached);
      final timestamp = DateTime.parse(data['timestamp']);

      // Cache süresi dolmuş mu?
      if (DateTime.now().difference(timestamp) > _cacheDuration) {
        await prefs.remove(key);
        return null;
      }

      return data['url'];
    } catch (e) {
      return null;
    }
  }

  /// Fotoğraf URL'ini cache'e kaydet
  static Future<void> _cachePhoto(String key, String url) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final data = json.encode({
        'url': url,
        'timestamp': DateTime.now().toIso8601String(),
      });
      await prefs.setString(key, data);
    } catch (e) {
      debugPrint('Cache kayıt hatası: $e');
    }
  }

  /// Cache'i temizle
  static Future<void> clearCache() async {
    final prefs = await SharedPreferences.getInstance();
    final keys = prefs.getKeys().where((k) => k.startsWith(_cachePrefix));
    for (final key in keys) {
      await prefs.remove(key);
    }
  }

  /// Placeholder fotoğraf URL'i (kategori bazlı)
  static String getPlaceholderUrl(String category) {
    final placeholders = {
      'Kafe':
          'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=800',
      'Restoran':
          'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800',
      'Bar':
          'https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=800',
      'Müze':
          'https://images.unsplash.com/photo-1566127444979-b3d2b654e3d7?w=800',
      'Tarihi':
          'https://images.unsplash.com/photo-1467269204594-9661b134dd2b?w=800',
      'Park':
          'https://images.unsplash.com/photo-1519331379826-f10be5486c6f?w=800',
      'Manzara':
          'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
      'Plaj':
          'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800',
      'Alışveriş':
          'https://images.unsplash.com/photo-1555529669-e69e7aa0ba9a?w=800',
    };

    return placeholders[category] ??
        'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800';
  }
}

/// Fotoğraf widget'ı - otomatik fallback ile
class SmartPhoto extends StatelessWidget {
  final String? imageUrl;
  final String placeName;
  final String category;
  final double? width;
  final double? height;
  final BoxFit fit;
  final BorderRadius? borderRadius;

  const SmartPhoto({
    super.key,
    this.imageUrl,
    required this.placeName,
    required this.category,
    this.width,
    this.height,
    this.fit = BoxFit.cover,
    this.borderRadius,
  });

  @override
  Widget build(BuildContext context) {
    // 1. Önce küratörlü fotoğrafa bak
    final curatedUrl = PhotoService.getCuratedPhoto(placeName);
    final finalUrl =
        curatedUrl ?? imageUrl ?? PhotoService.getPlaceholderUrl(category);

    return ClipRRect(
      borderRadius: borderRadius ?? BorderRadius.zero,
      child: Image.network(
        finalUrl,
        width: width,
        height: height,
        fit: fit,
        loadingBuilder: (context, child, loadingProgress) {
          if (loadingProgress == null) return child;
          return Container(
            width: width,
            height: height,
            color: Colors.grey.shade200,
            child: Center(
              child: CircularProgressIndicator(
                strokeWidth: 2,
                value: loadingProgress.expectedTotalBytes != null
                    ? loadingProgress.cumulativeBytesLoaded /
                          loadingProgress.expectedTotalBytes!
                    : null,
              ),
            ),
          );
        },
        errorBuilder: (context, error, stackTrace) {
          // Hata durumunda placeholder göster
          return Container(
            width: width,
            height: height,
            color: _getCategoryColor(category).withOpacity(0.1),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  _getCategoryIcon(category),
                  size: 40,
                  color: _getCategoryColor(category).withOpacity(0.5),
                ),
                const SizedBox(height: 8),
                Text(
                  placeName,
                  style: TextStyle(fontSize: 12, color: Colors.grey.shade600),
                  textAlign: TextAlign.center,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          );
        },
      ),
    );
  }

  Color _getCategoryColor(String category) {
    final colors = {
      'Kafe': const Color(0xFFFDAA5D),
      'Restoran': const Color(0xFFFF7675),
      'Bar': const Color(0xFFA29BFE),
      'Müze': const Color(0xFF74B9FF),
      'Tarihi': const Color(0xFF6C5CE7),
      'Park': const Color(0xFF00B894),
      'Manzara': const Color(0xFF0984E3),
      'Plaj': const Color(0xFF00CEC9),
      'Alışveriş': const Color(0xFFE17055),
    };
    return colors[category] ?? const Color(0xFF636E72);
  }

  IconData _getCategoryIcon(String category) {
    final icons = {
      'Kafe': Icons.local_cafe_rounded,
      'Restoran': Icons.restaurant_rounded,
      'Bar': Icons.nightlife_rounded,
      'Müze': Icons.museum_rounded,
      'Tarihi': Icons.account_balance_rounded,
      'Park': Icons.park_rounded,
      'Manzara': Icons.landscape_rounded,
      'Plaj': Icons.beach_access_rounded,
      'Alışveriş': Icons.shopping_bag_rounded,
    };
    return icons[category] ?? Icons.place_rounded;
  }
}
