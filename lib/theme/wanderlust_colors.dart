// =============================================================================
// WANDERLUST COLORS - VIBEMAP THEME
// Deep Purple, Glassmorphism, Neon Accents
// =============================================================================

import 'package:flutter/material.dart';

class WanderlustColors {
  // Arka plan renkleri (Deep Midnight Purple)
  static const Color bgDark = Color(0xFF252131); // Lighter, desaturated violet background
  
  // Card Colors (Glassy)
  // VibeMap uses very subtle, semi-transparent backgrounds for cards
  static const Color bgCard = Color(0x991C1C26); // Dark glass (~60% opacity)
  static const Color bgCardLight = Color(0x802D2D3A); // Lighter glass (~50% opacity)

  // Ana accent renkler (Solid Neon Violet - VibeMap style)
  static const Color accent = Color(0xFF807AF5); // Brand Logo Color
  static const Color accentLight = Color(0xFFA5A1FA); // Slightly lighter
  static const Color accentDark = Color(0xFF7672D9); // Slightly darker
  
  // Auxiliary Accents (Derived or complementary)
  static const Color accentPink = Color(0xFFEC4899); 
  static const Color accentBlue = Color(0xFF3B82F6); 
  static const Color accentGreen = Color(0xFF10B981); // Success Green 

  // Gradient (Defined as solid color list to eliminate transitions)
  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFF807AF5), Color(0xFF807AF5)], // Solid
  );

  static const LinearGradient primaryGradientVertical = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFF807AF5), Color(0xFF807AF5)], // Solid
  );

  // Metin renkleri
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF); // Cool Grey
  static const Color textGreyLight = Color(0xFFE5E7EB);

  // Border & Divider (Subtle White for Glass effect)
  static const Color border = Color(0x1FFFFFFF); // 12% White
  static const Color borderLight = Color(0x33FFFFFF); // 20% White

  // Kategori renkleri (Vibrant Pastels)
  static const Color categoryFood = Color(0xFFFF7675);
  static const Color categoryCafe = Color(0xFFFDAA5D);
  static const Color categoryMuseum = Color(0xFF74B9FF);
  static const Color categoryPark = Color(0xFF00B894);
  static const Color categoryBar = Color(0xFFA29BFE);
  static const Color categoryHistoric = Color(0xFF6C5CE7);

  // Durum renkleri
  static const Color success = Color(0xFF10B981);
  static const Color error = Color(0xFFEF4444);
  static const Color warning = Color(0xFFF59E0B);

  // Helper methodlar
  static Color withOpacity(Color color, double opacity) {
    return color.withOpacity(opacity);
  }

  // Global Glass Decoration Helper
  static BoxDecoration get cardDecoration => BoxDecoration(
    color: bgCard,
    borderRadius: BorderRadius.circular(20), // Rounded corners like VibeMap
    border: Border.all(color: border),
  );

  static BoxDecoration get accentCardDecoration => BoxDecoration(
    color: accent.withOpacity(0.15),
    borderRadius: BorderRadius.circular(20),
    border: Border.all(color: accent.withOpacity(0.3)),
  );
}
