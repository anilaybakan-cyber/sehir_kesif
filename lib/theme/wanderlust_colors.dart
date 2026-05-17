// =============================================================================
// WANDERLUST COLORS - VIBEMAP THEME
// Deep Purple, Glassmorphism, Neon Accents
// =============================================================================

import 'package:flutter/material.dart';

class WanderlustColors {
  // Arka plan renkleri
  static const Color bgDark = Color(0xFFF7F2EA);
  
  // Card Colors
  static const Color bgCard = Color(0xFFFFFCF8);
  static const Color bgCardLight = Color(0xFFF2EBE3);

  // Ana accent renkler
  static const Color accent = Color(0xFF807AF5);
  static const Color accentLight = Color(0xFFA5A1FA);
  static const Color accentDark = Color(0xFF6E67E8);
  
  // Auxiliary Accents (Derived or complementary)
  static const Color accentPink = Color(0xFFB68CFF); 
  static const Color accentBlue = Color(0xFFC8C1FF); 
  static const Color accentGreen = Color(0xFF4EA97E);

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

  static const LinearGradient accentGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [accent, accentLight],
  );

  // Metin renkleri
  static const Color textWhite = Color(0xFF2F2638);
  static const Color textGrey = Color(0xFF7D738A);
  static const Color textGreyLight = Color(0xFFB0A7BA);

  // Border & Divider
  static const Color border = Color(0x14A095B2);
  static const Color borderLight = Color(0x26A095B2);

  // Kategori renkleri (Vibrant Pastels)
  static const Color categoryFood = Color(0xFFE6A574);
  static const Color categoryCafe = Color(0xFFD4B07A);
  static const Color categoryMuseum = Color(0xFFA8A2FF);
  static const Color categoryPark = Color(0xFF90B89E);
  static const Color categoryBar = Color(0xFF9C95F7);
  static const Color categoryHistoric = Color(0xFF807AF5);

  // Durum renkleri
  static const Color success = Color(0xFF4EA97E);
  static const Color error = Color(0xFFD96B6B);
  static const Color warning = Color(0xFFE0AE67);

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
