import 'package:flutter/widgets.dart';
import 'package:flutter_cache_manager/flutter_cache_manager.dart';

// ==========================================
// 🚀 GÖRSEL OPTİMİZASYON VE CDN AYARLARI
// ==========================================

/// Firebase Resize Images Extension kurulduktan ve mevcut resimler için
/// çalıştıktan sonra bu değeri [true] yapınız.
/// [true] olduğunda orijinal resimler yerine otomatik olarak _600x600.webp 
/// veya _1200x1200.webp kopyaları servis edilir.
const bool kResizeExtensionActive = true;

/// Firebase + Cloudflare (veya Firebase Hosting CDN) bağlandığında bu değeri [true] yapınız.
const bool kUseCdn = false;

/// Cloudflare veya özel CDN domain adresiniz (Örn: https://cdn.sehirkesif.com)
const String kCdnDomain = 'https://cdn.sehirkesif.com';

// ==========================================

/// Liste/grid kartları için decode genişliği (fiziksel piksel).
/// [CachedNetworkImage.memCacheWidth] ile [ImagePrefetchService] aynı değeri kullanmalı.
int memCacheWidthForListThumbnail(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  final w = (mq?.size.width ?? 390.0).clamp(280.0, 900.0);
  // ~2 sütunlu grid varsayımı (yatay padding payı)
  final logicalThumb = ((w - 40) / 2).clamp(130.0, 280.0);
  return (logicalThumb * dpr).round().clamp(384, 960);
}

/// Şehir seç listesindeki 56×56 dp thumbnail kartları için decode boyutu.
/// [CachedNetworkImage.memCacheWidth] ile uyumlu; tam çözünürlük decode önlenir.
int memCacheWidthForCitySwitcherThumb(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  return (56 * dpr).round().clamp(112, 360);
}

/// Tam genişlikte üst görsel (Keşfet mekan kartı vb.): yatay padding çıkarılmış genişlik × DPR.
int memCacheWidthForFullWidthCard(BuildContext context, {double horizontalInset = 40}) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  final logicalW = ((mq?.size.width ?? 390.0) - horizontalInset).clamp(280.0, 900.0);
  return (logicalW * dpr).round().clamp(600, 1400);
}

/// Kart üst şeridinin dikey dp karşılığı (örn. 200 = ana mekan kartı görseli).
int memCacheHeightForCardBand(BuildContext context, double logicalHeightDp) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  return (logicalHeightDp * dpr).round().clamp(200, 1200);
}

/// `place_card.dart` — 170×110 dp görsel alanı.
int memCacheWidthForCompactPlaceCard(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  return (170 * dpr).round().clamp(256, 640);
}

int memCacheHeightForCompactPlaceCard(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  return (110 * dpr).round().clamp(200, 520);
}

/// `place_list_tile.dart` — 90×90 dp thumb.
int memCacheExtentForPlaceListThumb(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  return (90 * dpr).round().clamp(180, 400);
}

/// Detay / tam genişlik hero için decode (daha ağır; yalnızca detayda kullan).
int memCacheWidthForHero(BuildContext context) {
  final mq = MediaQuery.maybeOf(context);
  final dpr = (mq?.devicePixelRatio ?? 2.0).clamp(1.0, 3.0);
  final w = (mq?.size.width ?? 390.0).clamp(280.0, 900.0);
  return (w * dpr).round().clamp(720, 1536);
}

/// `storage.googleapis.com/<bucket>/<path>` URL'lerini Firebase Storage REST
/// (`firebasestorage.googleapis.com/...?alt=media`) adresine çevirir.
String firebaseCompatibleImageUrl(String rawUrl) {
  final trimmed = rawUrl.trim();
  if (trimmed.isEmpty) return trimmed;
  final uri = Uri.tryParse(trimmed);
  if (uri == null) return trimmed;

  if (uri.host == 'storage.googleapis.com' && uri.pathSegments.length >= 2) {
    final bucket = uri.pathSegments.first;
    final objectPath = uri.pathSegments.sublist(1).join('/');
    if (bucket.isNotEmpty && objectPath.isNotEmpty) {
      final encoded = Uri.encodeComponent(objectPath);
      return 'https://firebasestorage.googleapis.com/v0/b/$bucket/o/$encoded?alt=media';
    }
  }

  return trimmed;
}

/// Hem CDN yönlendirmesini hem de Firebase Resize Extension kopyalarını
/// dinamik olarak çözümleyen ana fonksiyon.
String resolveOptimizedImageUrl(String rawUrl, {bool isHero = false}) {
  final trimmed = rawUrl.trim();
  if (trimmed.isEmpty) return trimmed;
  final uri = Uri.tryParse(trimmed);
  if (uri == null) return trimmed;

  String path = '';
  String bucket = 'myway-3fe75.firebasestorage.app';

  if (uri.host == 'storage.googleapis.com' && uri.pathSegments.length >= 2) {
    bucket = uri.pathSegments[0];
    path = uri.pathSegments.sublist(1).join('/');
  } else if (uri.host == 'firebasestorage.googleapis.com' && uri.pathSegments.contains('o')) {
    final oIndex = uri.pathSegments.indexOf('o');
    if (oIndex + 1 < uri.pathSegments.length) {
      final segment = uri.pathSegments[oIndex + 1];
      try {
        path = Uri.decodeComponent(segment);
      } catch (e) {
        path = segment; // If it fails due to illegal percent encoding, just use the decoded segment
      }
    }
  }

  // Eğer uygulama depolama alanımızdaysa (GCS / Firebase Storage)
  if (path.isNotEmpty && (path.startsWith('cities/') || path.startsWith('routes/') || path.startsWith('hotels/'))) {
    // Resize Extension devredeyse dosya adını optimize uzantıyla değiştir
    if (kResizeExtensionActive && !path.contains('_600x600') && !path.contains('_1200x1200')) {
      final extIndex = path.lastIndexOf('.');
      if (extIndex != -1 && extIndex > path.lastIndexOf('/')) {
        final base = path.substring(0, extIndex);
        // Firebase extension şu an sadece 600x600 üretiyor. 
        // 1200x1200 olmadığı için 404 hatası veriyor, bu yüzden hep 600x600 kullanıyoruz.
        final dimension = '_600x600';
        path = '$base$dimension.webp';
      }
    }

    if (kUseCdn) {
      return '$kCdnDomain/$path';
    } else {
      final encodedPath = Uri.encodeComponent(path);
      return 'https://firebasestorage.googleapis.com/v0/b/$bucket/o/$encodedPath?alt=media';
    }
  }

  // Harici linkse standart Firebase REST dönüşümünü uygula
  return firebaseCompatibleImageUrl(trimmed);
}

/// Uygulama genelinde kullanılan özel cache yöneticisi.
/// Subclass yapısı CachedNetworkImage ile daha stabil çalışır.
class AppImageCacheManager extends CacheManager {
  static const String _cacheKey = 'app_image_cache';

  static final AppImageCacheManager _instance = AppImageCacheManager._internal();
  factory AppImageCacheManager() => _instance;

  static AppImageCacheManager get instance => _instance;

  AppImageCacheManager._internal()
      : super(
          Config(
            _cacheKey,
            stalePeriod: const Duration(days: 90),
            maxNrOfCacheObjects: 1000,
            repo: JsonCacheInfoRepository(databaseName: _cacheKey),
            fileService: HttpFileService(),
          ),
        );
}

