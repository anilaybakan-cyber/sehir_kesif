import 'package:flutter/material.dart';

enum RouteSpirit {
  classic,        // 1. İlk Kez Gelenler
  history,        // 2. Tarih & Kültür
  localDiscovery, // 3. Yan Sokaklar
  foodie,         // 4. Lezzet Avı
  shopping,       // 5. Alışveriş & Chill
  nature,         // 6. Yeşile Kaçış
  romantic,       // 7. Altın Saat
  creative,       // 8. Sanat & Tasarım
  nightlife,      // 9. Gece Hayatı
  relaxed         // 10. Yormayan Mod
}

class RouteArchetype {
  final RouteSpirit spirit;
  final String titleTr;
  final String titleEn;
  final String descriptionTr;
  final String descriptionEn;
  final String spiritQuoteTr;
  final String spiritQuoteEn;
  final IconData icon;
  final Color color;
  final List<String> primaryTags;
  final List<String> secondaryTags;
  final int pacingInterval; // How many stops before a break?

  const RouteArchetype({
    required this.spirit,
    required this.titleTr,
    required this.titleEn,
    required this.descriptionTr,
    required this.descriptionEn,
    required this.spiritQuoteTr,
    required this.spiritQuoteEn,
    required this.icon,
    required this.color,
    required this.primaryTags,
    required this.secondaryTags,
    this.pacingInterval = 2,
  });

  String getTitle(bool isEnglish) => isEnglish ? titleEn : titleTr;
  String getDescription(bool isEnglish) => isEnglish ? descriptionEn : descriptionTr;
  String getQuote(bool isEnglish) => isEnglish ? spiritQuoteEn : spiritQuoteTr;
}
