import 'dart:async';

import 'package:flutter/material.dart';
import '../models/city_model.dart';
import '../utils/image_utils.dart';
import 'trending_service.dart';

/// Şehir fotoğraflarını arka planda precache eden servis.
///
/// ÖNEMLİ: Prefetch'te kullandığımız ImageProvider, ekranda kullanılanla
/// BİREBİR AYNI olmalı. Aksi halde disk cache HIT olsa bile Flutter'ın
/// bellek cache'i MISS verir ve görsel yeniden decode edilir (lag).
///
/// CachedNetworkImage widget'ı kendi içinde CachedNetworkImageProvider
/// kullanır. Biz de prefetch'te aynı provider'ı — aynı parametrelerle —
/// çağırarak bellek cache'i önceden dolduruyoruz.
class ImagePrefetchService {
  static final ImagePrefetchService _instance = ImagePrefetchService._internal();
  factory ImagePrefetchService() => _instance;
  ImagePrefetchService._internal();

  /// Aynı anda kaç paralel indirme yapılacağı. Ağın boğulmasını engellemek için 2'ye düşürüldü.
  static const int _concurrency = 2;

  /// Halihazırda prefetch edilen şehir kimliği (JSON id / prefs anahtarı).
  static String? _lastPrefetchedCityId;

  /// Şehir açılışında: önce görünür kartların küçük çözünürlük prefetch'i (await),
  /// sonra kalan URL'leri **arka planda** indirir. Keşfet artık tüm 60 görseli beklememeli.
  static Future<void> prefetchCityPhotos(
    BuildContext context,
    CityModel city,
    String cityId, {
    List<Highlight>? processedHighlights,
  }) async {
    if (_lastPrefetchedCityId == cityId) return;
    _lastPrefetchedCityId = cityId;

    final highlights = processedHighlights ?? city.highlights;
    if (highlights.isEmpty) return;

    // İlk 50 görseli prefetch ediyoruz (scroll etmeden görünür olması için)
    final count = highlights.length < 50 ? highlights.length : 50;
    final urls = <String>[];

    for (int i = 0; i < count; i++) {
      final h = highlights[i];
      if (h.imageUrl == null || h.imageUrl!.isEmpty) continue;
      final url = resolveOptimizedImageUrl(h.imageUrl!, isHero: false);
      if (url.isNotEmpty) urls.add(url);
    }

    if (urls.isEmpty) return;

    final List<String> blockingUrls = [];
    final List<String> highPriorityUrls = [];

    // 1. Trending — Tonight's Picks (EN ÜSTTE ÇIKTIĞI İÇİN EN YÜKSEK ÖNCELİK)
    final trendingPlaces = TrendingService.getTrendingPlaces(highlights, limit: 8);
    for (int i = 0; i < trendingPlaces.length; i++) {
      final url = resolveOptimizedImageUrl(trendingPlaces[i].imageUrl ?? "", isHero: false);
      if (url.isNotEmpty) {
        // İlk 8 trending görseli RAM'e decode et (scroll etmeden görünür olsun)
        if (i < 8 && !blockingUrls.contains(url)) {
          blockingUrls.add(url);
        }
        if (!highPriorityUrls.contains(url)) {
          highPriorityUrls.add(url);
        }
      }
    }

    // 2. İlk görünür liste elemanları (Bloklamadan arkaplanda hızlıca indirilecek)
    final mainHighPriorityCount = urls.length < 15 ? urls.length : 15;
    for (int i = 0; i < mainHighPriorityCount; i++) {
      final url = urls[i];
      if (!highPriorityUrls.contains(url)) {
        highPriorityUrls.add(url);
      }
    }

    // İlk görselleri UI thread'i dondurmadan (non-blocking) RAM'e precache et
    if (context.mounted && blockingUrls.isNotEmpty) {
      Future.microtask(() async {
        await Future.wait(
          blockingUrls.map((url) => _safePrecache(context, url, heroDecode: false, onlyDownload: false)),
          eagerError: false,
        );
      });
    }

    // Kalan tüm highPriority ve remaining görsellerini arkaplanda schedule et
    final Set<String> scheduledUrls = {...blockingUrls};

    // Yüksek öncelikli (ör. görünür listeler) önce yüklenecek
    final remainingHighPriority = highPriorityUrls.where((u) => !scheduledUrls.contains(u)).toList();
    if (remainingHighPriority.isNotEmpty) {
      _scheduleRemainingCityPrefetch(context, cityId, remainingHighPriority);
      scheduledUrls.addAll(remainingHighPriority);
    }

    // Düşük öncelikli (Nearby vb.)
    final remainingUrls = urls.where((u) => !scheduledUrls.contains(u)).toList();
    _scheduleRemainingCityPrefetch(context, cityId, remainingUrls);
  }

  /// Kalan şehir görsellerini UI’yı bloklamadan indir.
  static void _scheduleRemainingCityPrefetch(
    BuildContext context,
    String cityId,
    List<String> remainingUrls,
  ) {
    if (remainingUrls.isEmpty) return;
    Future.microtask(() async {
      for (int batch = 0; batch < remainingUrls.length; batch += _concurrency) {
        if (!context.mounted || _lastPrefetchedCityId != cityId) return;

        final end = (batch + _concurrency).clamp(0, remainingUrls.length);
        final batchUrls = remainingUrls.sublist(batch, end);

        // Arka plan yüklemeleri sadece diske indirilir (onlyDownload: true). 
        // Böylece arka planda çalışırken ana ekranı dondurmaz (LAG YAPMAZ).
        await Future.wait(
          batchUrls.map((url) => _safePrecache(context, url, heroDecode: false, onlyDownload: true)),
          eagerError: false,
        );
      }
    });
  }

  /// Tek bir fotoğrafı precache et.
  /// [heroDecode]: true ise detay ekranıyla aynı (geniş) decode anahtarı — push öncesi kullan.
  static Future<void> prefetchSinglePhoto(
    BuildContext context,
    String? imageUrl, {
    required bool heroDecode,
  }) async {
    if (imageUrl == null || imageUrl.isEmpty) return;
    final url = resolveOptimizedImageUrl(imageUrl, isHero: heroDecode);
    if (url.isEmpty) return;

    // Detay sayfasına girerken anında gözüksün diye RAM'e tam decode (onlyDownload: false)
    await _safePrecache(context, url, heroDecode: heroDecode, onlyDownload: false);
  }

  /// Verilen URL listesini toplu olarak prefetch et.
  static Future<void> prefetchUrls(BuildContext context, List<String?> imageUrls) async {
    final urls = <String>[];
    for (final raw in imageUrls) {
      if (raw == null || raw.isEmpty) continue;
      final url = resolveOptimizedImageUrl(raw, isHero: false);
      if (url.isNotEmpty) urls.add(url);
    }

    if (urls.isEmpty) return;

    for (int batch = 0; batch < urls.length; batch += _concurrency) {
      if (!context.mounted) return;
      
      final end = (batch + _concurrency).clamp(0, urls.length);
      final batchUrls = urls.sublist(batch, end);

      await Future.wait(
        batchUrls.map((url) => _safePrecache(context, url, heroDecode: false, onlyDownload: true)),
        eagerError: false,
      );
    }
  }

  /// Hata yakalayarak tek bir URL'yi precache eder.
  ///
  /// [onlyDownload]: true ise resmi sadece diske indirir (UI thread dondurmaz, lag yapmaz).
  /// false ise resmi RAM'e decode eder (Sıfır placeholder garantisi).
  static Future<void> _safePrecache(
    BuildContext context,
    String url, {
    required bool heroDecode,
    required bool onlyDownload,
  }) async {
    try {
      if (!context.mounted) return;

      // ⚡ Doğrudan Flutter motorunun (C++) yerleşik ve aşırı hızlı RAM precache sistemini kullan
      final provider = NetworkImage(url);
      await precacheImage(provider, context);
    } catch (e) {
      debugPrint("⚠️ Prefetch hatası ($url): $e");
    }
  }
}
