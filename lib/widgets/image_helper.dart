// =============================================================================
// IMAGE HELPER - Güvenilir placeholder sistemi
// Unsplash yavaş/güvenilmez olduğunda kullanılır
// =============================================================================

import 'package:flutter/material.dart';

class PlaceholderImage extends StatelessWidget {
  final String category;
  final String? name;
  final double? width;
  final double? height;
  final BorderRadius? borderRadius;

  const PlaceholderImage({
    super.key,
    required this.category,
    this.name,
    this.width,
    this.height,
    this.borderRadius,
  });

  // Kategoriye göre renk ve ikon
  static Map<String, dynamic> getCategoryStyle(String category) {
    switch (category.toLowerCase()) {
      case "kafe":
      case "cafe":
      case "coffee":
        return {
          "color": const Color(0xFFFDAA5D),
          "gradient": [const Color(0xFFFDAA5D), const Color(0xFFE17055)],
          "icon": Icons.local_cafe_rounded,
        };
      case "restoran":
      case "restaurant":
      case "food":
        return {
          "color": const Color(0xFFFF7675),
          "gradient": [const Color(0xFFFF7675), const Color(0xFFD63031)],
          "icon": Icons.restaurant_rounded,
        };
      case "bar":
      case "gece":
      case "nightlife":
        return {
          "color": const Color(0xFFA29BFE),
          "gradient": [const Color(0xFFA29BFE), const Color(0xFF6C5CE7)],
          "icon": Icons.local_bar_rounded,
        };
      case "müze":
      case "museum":
      case "kültür":
      case "culture":
        return {
          "color": const Color(0xFF74B9FF),
          "gradient": [const Color(0xFF74B9FF), const Color(0xFF0984E3)],
          "icon": Icons.museum_rounded,
        };
      case "park":
      case "doğa":
      case "nature":
        return {
          "color": const Color(0xFF00B894),
          "gradient": [const Color(0xFF00B894), const Color(0xFF00A085)],
          "icon": Icons.park_rounded,
        };
      case "tarihi":
      case "historic":
        return {
          "color": const Color(0xFF6C5CE7),
          "gradient": [const Color(0xFF6C5CE7), const Color(0xFF5B4CC4)],
          "icon": Icons.account_balance_rounded,
        };
      case "plaj":
      case "beach":
        return {
          "color": const Color(0xFF00CEC9),
          "gradient": [const Color(0xFF00CEC9), const Color(0xFF00B5B1)],
          "icon": Icons.beach_access_rounded,
        };
      case "alışveriş":
      case "shopping":
        return {
          "color": const Color(0xFFE84393),
          "gradient": [const Color(0xFFE84393), const Color(0xFFD63384)],
          "icon": Icons.shopping_bag_rounded,
        };
      default:
        return {
          "color": const Color(0xFF636E72),
          "gradient": [const Color(0xFF636E72), const Color(0xFF2D3436)],
          "icon": Icons.place_rounded,
        };
    }
  }

  @override
  Widget build(BuildContext context) {
    final style = getCategoryStyle(category);
    final List<Color> gradient = style["gradient"];
    final IconData icon = style["icon"];

    return Container(
      width: width,
      height: height,
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: gradient,
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: borderRadius,
      ),
      child: Stack(
        children: [
          // Decorative circles
          Positioned(
            right: -20,
            top: -20,
            child: Container(
              width: 80,
              height: 80,
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.1),
                shape: BoxShape.circle,
              ),
            ),
          ),
          Positioned(
            left: -15,
            bottom: -15,
            child: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(
                color: Colors.white.withOpacity(0.1),
                shape: BoxShape.circle,
              ),
            ),
          ),

          // Icon
          Center(
            child: Icon(
              icon,
              size: (height ?? 100) * 0.35,
              color: Colors.white.withOpacity(0.9),
            ),
          ),
        ],
      ),
    );
  }
}

// =============================================================================
// SMART IMAGE - Önce Unsplash dener, başarısız olursa placeholder gösterir
// =============================================================================
class SmartImage extends StatelessWidget {
  final String? imageUrl;
  final String category;
  final String? name;
  final double? width;
  final double? height;
  final BorderRadius? borderRadius;
  final BoxFit fit;

  const SmartImage({
    super.key,
    this.imageUrl,
    required this.category,
    this.name,
    this.width,
    this.height,
    this.borderRadius,
    this.fit = BoxFit.cover,
  });

  @override
  Widget build(BuildContext context) {
    // Eğer URL yoksa direkt placeholder göster
    if (imageUrl == null || imageUrl!.isEmpty) {
      return ClipRRect(
        borderRadius: borderRadius ?? BorderRadius.zero,
        child: PlaceholderImage(
          category: category,
          name: name,
          width: width,
          height: height,
        ),
      );
    }

    return ClipRRect(
      borderRadius: borderRadius ?? BorderRadius.zero,
      child: Image.network(
        imageUrl!,
        width: width,
        height: height,
        fit: fit,
        // Yükleme durumu
        loadingBuilder: (context, child, loadingProgress) {
          if (loadingProgress == null) return child;
          return PlaceholderImage(
            category: category,
            name: name,
            width: width,
            height: height,
          );
        },
        // Hata durumu - placeholder göster
        errorBuilder: (context, error, stackTrace) {
          return PlaceholderImage(
            category: category,
            name: name,
            width: width,
            height: height,
          );
        },
      ),
    );
  }
}
