// lib/theme/wanderlust_design_system.dart
// 🎨 Wanderlust Design System
// Style: Organic + Soft + Bold Gradients
// Inspired by: Airbnb warmth + Apple fluidity + Spotify boldness

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:ui';

/// ═══════════════════════════════════════════════════════════════════════════
/// 🎨 COLOR PALETTE
/// Organic warmth meets bold gradients
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustDesignColors {
  WanderlustDesignColors._();

  // Primary Gradient - Sunset Coral to Warm Orange
  static const Color primaryStart = Color(0xFFFF6B6B);
  static const Color primaryEnd = Color(0xFFFFAB76);
  static const Color accent = Color(0xFFE91E8C);

  // Secondary Gradient - Ocean Blue to Teal
  static const Color secondaryStart = Color(0xFF4ECDC4);
  static const Color secondaryEnd = Color(0xFF44A08D);

  // Accent Gradient - Purple Dream
  static const Color accentStart = Color(0xFF667EEA);
  static const Color accentEnd = Color(0xFF764BA2);

  // Neutral Tones - Soft & Organic
  static const Color background = Color(0xFFFAF9F7);
  static const Color backgroundDark = Color(0xFF1A1A2E);
  static const Color surface = Color(0xFFFFFFFF);
  static const Color surfaceDark = Color(0xFF16213E);

  // Text Colors
  static const Color textPrimary = Color(0xFF2D3436);
  static const Color textSecondary = Color(0xFF636E72);
  static const Color textLight = Color(0xFFB2BEC3);
  static const Color textOnGradient = Color(0xFFFFFFFF);

  // Semantic Colors
  static const Color success = Color(0xFF00B894);
  static const Color warning = Color(0xFFFDCB6E);
  static const Color error = Color(0xFFE17055);
  static const Color info = Color(0xFF74B9FF);

  // Glass Effect Colors
  static const Color glassWhite = Color(0x40FFFFFF);
  static const Color glassBorder = Color(0x20FFFFFF);
  static const Color glassOverlay = Color(0x10000000);

  // Category Colors - Soft pastels with bold accents
  static const Map<String, Color> categoryColors = {
    'Restoran': Color(0xFFFF6B6B),
    'Bar': Color(0xFF9B59B6),
    'Kafe': Color(0xFFE17055),
    'Müze': Color(0xFF3498DB),
    'Tarihi': Color(0xFFD4A574),
    'Park': Color(0xFF00B894),
    'Manzara': Color(0xFF00CEC9),
    'Alışveriş': Color(0xFFFD79A8),
    'Semt': Color(0xFFA29BFE),
    'Deneyim': Color(0xFFFDCB6E),
    'Pazar': Color(0xFF6C5CE7),
  };

  // Gradients
  static const LinearGradient primaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [primaryStart, primaryEnd],
  );

  static const LinearGradient secondaryGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [secondaryStart, secondaryEnd],
  );

  static const LinearGradient accentGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [accentStart, accentEnd],
  );

  static const LinearGradient sunsetGradient = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFFFF6B6B), Color(0xFFFFAB76), Color(0xFFFDCB6E)],
  );

  static const LinearGradient oceanGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFF667EEA), Color(0xFF4ECDC4)],
  );

  static const LinearGradient softGradient = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFFF8F9FA), Color(0xFFE9ECEF)],
  );

  static const LinearGradient darkGradient = LinearGradient(
    begin: Alignment.topCenter,
    end: Alignment.bottomCenter,
    colors: [Color(0xFF1A1A2E), Color(0xFF16213E), Color(0xFF0F3460)],
  );
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 📝 TYPOGRAPHY
/// Distinctive, warm, and readable
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustTypography {
  WanderlustTypography._();

  // Font Families - Using Google Fonts
  // Display: Playfair Display (elegant, editorial)
  // Body: DM Sans (clean, modern, friendly)
  // Accent: Outfit (geometric, contemporary)

  static const String displayFont = 'Playfair Display';
  static const String bodyFont = 'DM Sans';
  static const String accentFont = 'Outfit';

  // Display Styles
  static const TextStyle displayLarge = TextStyle(
    fontFamily: displayFont,
    fontSize: 48,
    fontWeight: FontWeight.w700,
    letterSpacing: -1.5,
    height: 1.1,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle displayMedium = TextStyle(
    fontFamily: displayFont,
    fontSize: 36,
    fontWeight: FontWeight.w600,
    letterSpacing: -1.0,
    height: 1.2,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle displaySmall = TextStyle(
    fontFamily: displayFont,
    fontSize: 28,
    fontWeight: FontWeight.w600,
    letterSpacing: -0.5,
    height: 1.25,
    color: WanderlustDesignColors.textPrimary,
  );

  // Headlines
  static const TextStyle headlineLarge = TextStyle(
    fontFamily: accentFont,
    fontSize: 24,
    fontWeight: FontWeight.w700,
    letterSpacing: -0.5,
    height: 1.3,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle headlineMedium = TextStyle(
    fontFamily: accentFont,
    fontSize: 20,
    fontWeight: FontWeight.w600,
    letterSpacing: -0.25,
    height: 1.35,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle headlineSmall = TextStyle(
    fontFamily: accentFont,
    fontSize: 18,
    fontWeight: FontWeight.w600,
    letterSpacing: 0,
    height: 1.4,
    color: WanderlustDesignColors.textPrimary,
  );

  // Body Text
  static const TextStyle bodyLarge = TextStyle(
    fontFamily: bodyFont,
    fontSize: 16,
    fontWeight: FontWeight.w400,
    letterSpacing: 0.15,
    height: 1.5,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle bodyMedium = TextStyle(
    fontFamily: bodyFont,
    fontSize: 14,
    fontWeight: FontWeight.w400,
    letterSpacing: 0.25,
    height: 1.5,
    color: WanderlustDesignColors.textSecondary,
  );

  static const TextStyle bodySmall = TextStyle(
    fontFamily: bodyFont,
    fontSize: 12,
    fontWeight: FontWeight.w400,
    letterSpacing: 0.4,
    height: 1.5,
    color: WanderlustDesignColors.textLight,
  );

  // Labels & Buttons
  static const TextStyle labelLarge = TextStyle(
    fontFamily: accentFont,
    fontSize: 14,
    fontWeight: FontWeight.w600,
    letterSpacing: 0.5,
    height: 1.4,
    color: WanderlustDesignColors.textPrimary,
  );

  static const TextStyle labelMedium = TextStyle(
    fontFamily: accentFont,
    fontSize: 12,
    fontWeight: FontWeight.w600,
    letterSpacing: 0.5,
    height: 1.4,
    color: WanderlustDesignColors.textSecondary,
  );

  static const TextStyle labelSmall = TextStyle(
    fontFamily: accentFont,
    fontSize: 10,
    fontWeight: FontWeight.w500,
    letterSpacing: 0.5,
    height: 1.4,
    color: WanderlustDesignColors.textLight,
  );

  // Special
  static const TextStyle buttonText = TextStyle(
    fontFamily: accentFont,
    fontSize: 16,
    fontWeight: FontWeight.w600,
    letterSpacing: 0.5,
    height: 1.25,
    color: WanderlustDesignColors.textOnGradient,
  );

  static const TextStyle caption = TextStyle(
    fontFamily: bodyFont,
    fontSize: 11,
    fontWeight: FontWeight.w500,
    letterSpacing: 0.5,
    height: 1.4,
    color: WanderlustDesignColors.textLight,
  );
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 📐 SPACING & SIZING
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustSpacing {
  WanderlustSpacing._();

  // Base unit: 4px
  static const double xxs = 4;
  static const double xs = 8;
  static const double sm = 12;
  static const double md = 16;
  static const double lg = 24;
  static const double xl = 32;
  static const double xxl = 48;
  static const double xxxl = 64;

  // Screen padding
  static const EdgeInsets screenPadding = EdgeInsets.symmetric(horizontal: 20);
  static const EdgeInsets cardPadding = EdgeInsets.all(16);
  static const EdgeInsets listPadding = EdgeInsets.symmetric(
    horizontal: 20,
    vertical: 12,
  );

  // Border Radius
  static const double radiusXs = 8;
  static const double radiusSm = 12;
  static const double radiusMd = 16;
  static const double radiusLg = 24;
  static const double radiusXl = 32;
  static const double radiusFull = 999;

  // Card sizes
  static const double cardHeightSmall = 120;
  static const double cardHeightMedium = 180;
  static const double cardHeightLarge = 240;
  static const double cardHeightXL = 320;

  // Icons
  static const double iconXs = 16;
  static const double iconSm = 20;
  static const double iconMd = 24;
  static const double iconLg = 32;
  static const double iconXl = 48;
}

/// ═══════════════════════════════════════════════════════════════════════════
/// ✨ EFFECTS & SHADOWS
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustEffects {
  WanderlustEffects._();

  static List<BoxShadow> shadowSm = [
    BoxShadow(
      color: Colors.black.withOpacity(0.04),
      blurRadius: 8,
      offset: const Offset(0, 2),
    ),
  ];

  static List<BoxShadow> shadowMd = [
    BoxShadow(
      color: Colors.black.withOpacity(0.06),
      blurRadius: 16,
      offset: const Offset(0, 4),
    ),
    BoxShadow(
      color: Colors.black.withOpacity(0.02),
      blurRadius: 4,
      offset: const Offset(0, 1),
    ),
  ];

  static List<BoxShadow> shadowLg = [
    BoxShadow(
      color: Colors.black.withOpacity(0.08),
      blurRadius: 24,
      offset: const Offset(0, 8),
    ),
    BoxShadow(
      color: Colors.black.withOpacity(0.04),
      blurRadius: 8,
      offset: const Offset(0, 2),
    ),
  ];

  static List<BoxShadow> shadowXl = [
    BoxShadow(
      color: Colors.black.withOpacity(0.12),
      blurRadius: 40,
      offset: const Offset(0, 16),
    ),
    BoxShadow(
      color: Colors.black.withOpacity(0.04),
      blurRadius: 12,
      offset: const Offset(0, 4),
    ),
  ];

  static List<BoxShadow> primaryShadow = [
    BoxShadow(
      color: WanderlustDesignColors.primaryStart.withOpacity(0.3),
      blurRadius: 20,
      offset: const Offset(0, 8),
    ),
  ];

  static List<BoxShadow> accentShadow = [
    BoxShadow(
      color: WanderlustDesignColors.accentStart.withOpacity(0.3),
      blurRadius: 20,
      offset: const Offset(0, 8),
    ),
  ];

  static const double glassBlurAmount = 20.0;
  static const double glassOpacity = 0.15;

  static const Duration durationFast = Duration(milliseconds: 150);
  static const Duration durationNormal = Duration(milliseconds: 300);
  static const Duration durationSlow = Duration(milliseconds: 500);
  static const Duration durationVerySlow = Duration(milliseconds: 800);

  static const Curve curveDefault = Curves.easeOutCubic;
  static const Curve curveSpring = Curves.elasticOut;
  static const Curve curveSmooth = Curves.easeInOutCubic;
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🧩 REUSABLE DECORATIONS
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustDecorations {
  WanderlustDecorations._();

  static BoxDecoration glassCard = BoxDecoration(
    color: WanderlustDesignColors.glassWhite,
    borderRadius: BorderRadius.circular(WanderlustSpacing.radiusLg),
    border: Border.all(color: WanderlustDesignColors.glassBorder, width: 1.5),
  );

  static BoxDecoration solidCard = BoxDecoration(
    color: WanderlustDesignColors.surface,
    borderRadius: BorderRadius.circular(WanderlustSpacing.radiusLg),
    boxShadow: WanderlustEffects.shadowMd,
  );

  static BoxDecoration gradientCard(LinearGradient gradient) => BoxDecoration(
    gradient: gradient,
    borderRadius: BorderRadius.circular(WanderlustSpacing.radiusLg),
    boxShadow: WanderlustEffects.shadowLg,
  );

  static BoxDecoration inputField = BoxDecoration(
    color: WanderlustDesignColors.background,
    borderRadius: BorderRadius.circular(WanderlustSpacing.radiusMd),
    border: Border.all(
      color: WanderlustDesignColors.textLight.withOpacity(0.3),
      width: 1,
    ),
  );

  static BoxDecoration categoryChip(Color color) => BoxDecoration(
    color: color.withOpacity(0.12),
    borderRadius: BorderRadius.circular(WanderlustSpacing.radiusFull),
  );
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🎭 THEME DATA
/// ═══════════════════════════════════════════════════════════════════════════

class WanderlustTheme {
  WanderlustTheme._();

  static ThemeData get lightTheme => ThemeData(
    useMaterial3: true,
    brightness: Brightness.light,
    scaffoldBackgroundColor: WanderlustDesignColors.background,

    colorScheme: const ColorScheme.light(
      primary: WanderlustDesignColors.primaryStart,
      secondary: WanderlustDesignColors.secondaryStart,
      tertiary: WanderlustDesignColors.accentStart,
      surface: WanderlustDesignColors.surface,
      error: WanderlustDesignColors.error,
      onPrimary: WanderlustDesignColors.textOnGradient,
      onSecondary: WanderlustDesignColors.textOnGradient,
      onSurface: WanderlustDesignColors.textPrimary,
      onError: WanderlustDesignColors.textOnGradient,
    ),

    appBarTheme: const AppBarTheme(
      elevation: 0,
      scrolledUnderElevation: 0,
      backgroundColor: Colors.transparent,
      systemOverlayStyle: SystemUiOverlayStyle.dark,
      titleTextStyle: WanderlustTypography.headlineMedium,
      iconTheme: IconThemeData(color: WanderlustDesignColors.textPrimary),
    ),

    bottomNavigationBarTheme: BottomNavigationBarThemeData(
      backgroundColor: WanderlustDesignColors.surface,
      elevation: 0,
      selectedItemColor: WanderlustDesignColors.primaryStart,
      unselectedItemColor: WanderlustDesignColors.textLight,
      type: BottomNavigationBarType.fixed,
      selectedLabelStyle: WanderlustTypography.labelSmall,
      unselectedLabelStyle: WanderlustTypography.labelSmall,
    ),

    // IMPORTANT: CardThemeData (yeni Flutter)
    cardTheme: CardThemeData(
      elevation: 0,
      color: WanderlustDesignColors.surface,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(WanderlustSpacing.radiusLg),
      ),
    ),

    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: WanderlustDesignColors.background,
      border: OutlineInputBorder(
        borderRadius: BorderRadius.circular(WanderlustSpacing.radiusMd),
        borderSide: BorderSide.none,
      ),
      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
      hintStyle: WanderlustTypography.bodyMedium.copyWith(
        color: WanderlustDesignColors.textLight,
      ),
    ),

    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        elevation: 0,
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 14),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(WanderlustSpacing.radiusFull),
        ),
        textStyle: WanderlustTypography.buttonText,
      ),
    ),

    textTheme: const TextTheme(
      displayLarge: WanderlustTypography.displayLarge,
      displayMedium: WanderlustTypography.displayMedium,
      displaySmall: WanderlustTypography.displaySmall,
      headlineLarge: WanderlustTypography.headlineLarge,
      headlineMedium: WanderlustTypography.headlineMedium,
      headlineSmall: WanderlustTypography.headlineSmall,
      bodyLarge: WanderlustTypography.bodyLarge,
      bodyMedium: WanderlustTypography.bodyMedium,
      bodySmall: WanderlustTypography.bodySmall,
      labelLarge: WanderlustTypography.labelLarge,
      labelMedium: WanderlustTypography.labelMedium,
      labelSmall: WanderlustTypography.labelSmall,
    ),
  );

  static ThemeData get darkTheme => ThemeData(
    useMaterial3: true,
    brightness: Brightness.dark,
    scaffoldBackgroundColor: WanderlustDesignColors.backgroundDark,
    colorScheme: const ColorScheme.dark(
      primary: WanderlustDesignColors.primaryStart,
      secondary: WanderlustDesignColors.secondaryStart,
      tertiary: WanderlustDesignColors.accentStart,
      surface: WanderlustDesignColors.surfaceDark,
      error: WanderlustDesignColors.error,
      onPrimary: WanderlustDesignColors.textOnGradient,
      onSecondary: WanderlustDesignColors.textOnGradient,
      onSurface: WanderlustDesignColors.textOnGradient,
      onError: WanderlustDesignColors.textOnGradient,
    ),
    appBarTheme: const AppBarTheme(
      elevation: 0,
      scrolledUnderElevation: 0,
      backgroundColor: Colors.transparent,
      systemOverlayStyle: SystemUiOverlayStyle.light,
      titleTextStyle: WanderlustTypography.headlineMedium,
      iconTheme: IconThemeData(color: WanderlustDesignColors.textOnGradient),
    ),
    textTheme: TextTheme(
      displayLarge: WanderlustTypography.displayLarge.copyWith(
        color: Colors.white,
      ),
      displayMedium: WanderlustTypography.displayMedium.copyWith(
        color: Colors.white,
      ),
      displaySmall: WanderlustTypography.displaySmall.copyWith(
        color: Colors.white,
      ),
      headlineLarge: WanderlustTypography.headlineLarge.copyWith(
        color: Colors.white,
      ),
      headlineMedium: WanderlustTypography.headlineMedium.copyWith(
        color: Colors.white,
      ),
      headlineSmall: WanderlustTypography.headlineSmall.copyWith(
        color: Colors.white,
      ),
      bodyLarge: WanderlustTypography.bodyLarge.copyWith(
        color: Colors.white.withOpacity(0.9),
      ),
      bodyMedium: WanderlustTypography.bodyMedium.copyWith(
        color: Colors.white.withOpacity(0.7),
      ),
      bodySmall: WanderlustTypography.bodySmall.copyWith(
        color: Colors.white.withOpacity(0.5),
      ),
      labelLarge: WanderlustTypography.labelLarge.copyWith(color: Colors.white),
      labelMedium: WanderlustTypography.labelMedium.copyWith(
        color: Colors.white.withOpacity(0.7),
      ),
      labelSmall: WanderlustTypography.labelSmall.copyWith(
        color: Colors.white.withOpacity(0.5),
      ),
    ),
  );
}
