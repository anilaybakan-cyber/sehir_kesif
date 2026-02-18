// =============================================================================
// WANDERLUST COLORS - AMBER/GOLD THEME
// Tüm uygulamada kullanılacak renk paleti
// =============================================================================

import 'package:flutter/material.dart';

class WanderlustColors {
  // Arka plan renkleri
  static const Color bgDark = Color(0xFF121212); // Neutral Dark Background
  static const Color bgCard = Color(0xFF1E1E1E); // Neutral Dark Card
  static const Color bgCardLight = Color(0xFF2C2C2C); // Lighter Grey

  // Ana accent renkler (Amber/Gold)
  static const Color accent = Color(0xFFF5A623); // Ana amber
  static const Color accentLight = Color(0xFFFFB800); // Açık gold
  static const Color accentDark = Color(0xFFE09000); // Koyu amber

  // Gradient
  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFF5A623), Color(0xFFFFB800)],
  );

  static const LinearGradient primaryGradientVertical = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFFF5A623), Color(0xFFE09000)],
  );

  // Metin renkleri
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color textGreyLight = Color(0xFFD1D5DB);

  // Border & Divider
  static const Color border = Color(0xFF2D2D4A);
  static const Color borderLight = Color(0xFF3D3D5A);

  // Kategori renkleri
  static const Color categoryFood = Color(0xFFFF7675);
  static const Color categoryCafe = Color(0xFFFDAA5D);
  static const Color categoryMuseum = Color(0xFF74B9FF);
  static const Color categoryPark = Color(0xFF00B894);
  static const Color categoryBar = Color(0xFFA29BFE);
  static const Color categoryHistoric = Color(0xFF6C5CE7);

  // Durum renkleri
  static const Color success = Color(0xFF00B894);
  static const Color error = Color(0xFFFF6B6B);
  static const Color warning = Color(0xFFFFA502);

  // Helper methodlar
  static Color withOpacity(Color color, double opacity) {
    return color.withOpacity(opacity);
  }

  static BoxDecoration get cardDecoration => BoxDecoration(
    color: bgCard,
    borderRadius: BorderRadius.circular(16),
    border: Border.all(color: border.withOpacity(0.5)),
  );

  static BoxDecoration get accentCardDecoration => BoxDecoration(
    color: accent.withOpacity(0.15),
    borderRadius: BorderRadius.circular(16),
    border: Border.all(color: accent.withOpacity(0.3)),
  );
}
