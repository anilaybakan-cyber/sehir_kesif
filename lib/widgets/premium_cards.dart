// =============================================================================
// PREMIUM GLASS CARD
// Modern Glassmorphism efektli, animasyonlu kart widget'ı
// =============================================================================

import 'dart:ui';
import 'package:flutter/material.dart';
import '../core/theme/app_theme.dart';

class PremiumGlassCard extends StatefulWidget {
  final Widget child;
  final double blur;
  final double opacity;
  final Color? borderColor;
  final Color? backgroundColor;
  final Gradient? gradient;
  final EdgeInsets? padding;
  final EdgeInsets? margin;
  final double borderRadius;
  final VoidCallback? onTap;
  final bool enableHover;
  final List<BoxShadow>? shadows;

  const PremiumGlassCard({
    super.key,
    required this.child,
    this.blur = 20,
    this.opacity = 0.1,
    this.borderColor,
    this.backgroundColor,
    this.gradient,
    this.padding,
    this.margin,
    this.borderRadius = 24,
    this.onTap,
    this.enableHover = true,
    this.shadows,
  });

  @override
  State<PremiumGlassCard> createState() => _PremiumGlassCardState();
}

class _PremiumGlassCardState extends State<PremiumGlassCard>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;
  late Animation<double> _elevationAnimation;
  bool _isPressed = false;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(duration: AppDurations.fast, vsync: this);

    _scaleAnimation = Tween<double>(
      begin: 1.0,
      end: 0.98,
    ).animate(CurvedAnimation(parent: _controller, curve: AppCurves.smooth));

    _elevationAnimation = Tween<double>(
      begin: 0.0,
      end: 8.0,
    ).animate(CurvedAnimation(parent: _controller, curve: AppCurves.smooth));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _onTapDown(TapDownDetails details) {
    if (widget.onTap != null && widget.enableHover) {
      setState(() => _isPressed = true);
      _controller.forward();
    }
  }

  void _onTapUp(TapUpDetails details) {
    if (widget.onTap != null && widget.enableHover) {
      setState(() => _isPressed = false);
      _controller.reverse();
    }
  }

  void _onTapCancel() {
    if (widget.onTap != null && widget.enableHover) {
      setState(() => _isPressed = false);
      _controller.reverse();
    }
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return Transform.scale(
          scale: _scaleAnimation.value,
          child: GestureDetector(
            onTap: widget.onTap,
            onTapDown: _onTapDown,
            onTapUp: _onTapUp,
            onTapCancel: _onTapCancel,
            child: Container(
              margin: widget.margin ?? const EdgeInsets.only(bottom: 16),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(widget.borderRadius),
                child: BackdropFilter(
                  filter: ImageFilter.blur(
                    sigmaX: widget.blur,
                    sigmaY: widget.blur,
                  ),
                  child: AnimatedContainer(
                    duration: AppDurations.fast,
                    padding: widget.padding ?? const EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      gradient:
                          widget.gradient ??
                          LinearGradient(
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                            colors: [
                              (widget.backgroundColor ?? Colors.white)
                                  .withOpacity(widget.opacity + 0.05),
                              (widget.backgroundColor ?? Colors.white)
                                  .withOpacity(widget.opacity),
                            ],
                          ),
                      borderRadius: BorderRadius.circular(widget.borderRadius),
                      border: Border.all(
                        color:
                            widget.borderColor ??
                            Colors.white.withOpacity(_isPressed ? 0.4 : 0.2),
                        width: 1.5,
                      ),
                      boxShadow:
                          widget.shadows ??
                          [
                            BoxShadow(
                              color: Colors.black.withOpacity(
                                0.05 + (_elevationAnimation.value * 0.01),
                              ),
                              blurRadius: 20 + _elevationAnimation.value,
                              offset: Offset(0, 8 + _elevationAnimation.value),
                              spreadRadius: -4,
                            ),
                          ],
                    ),
                    child: widget.child,
                  ),
                ),
              ),
            ),
          ),
        );
      },
    );
  }
}

// =============================================================================
// FEATURED CARD - Öne çıkan içerikler için büyük kart
// =============================================================================
class FeaturedCard extends StatelessWidget {
  final String title;
  final String subtitle;
  final String? imageUrl;
  final String? tag;
  final Color? tagColor;
  final Gradient? gradient;
  final VoidCallback? onTap;
  final double height;
  final Widget? bottomWidget;

  const FeaturedCard({
    super.key,
    required this.title,
    required this.subtitle,
    this.imageUrl,
    this.tag,
    this.tagColor,
    this.gradient,
    this.onTap,
    this.height = 220,
    this.bottomWidget,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        height: height,
        margin: const EdgeInsets.only(bottom: 20),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(28),
          gradient: gradient ?? AppGradients.primary,
          boxShadow: AppShadows.medium,
        ),
        child: Stack(
          children: [
            // Background image (optional)
            if (imageUrl != null)
              Positioned.fill(
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(28),
                  child: Image.network(
                    imageUrl!,
                    fit: BoxFit.cover,
                    errorBuilder: (_, __, ___) => const SizedBox(),
                  ),
                ),
              ),

            // Gradient overlay
            Positioned.fill(
              child: Container(
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(28),
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [Colors.transparent, Colors.black.withOpacity(0.7)],
                  ),
                ),
              ),
            ),

            // Content
            Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Tag
                  if (tag != null) ...[
                    Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: tagColor ?? AppColors.accent,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        tag!.toUpperCase(),
                        style: AppTypography.labelSmall.copyWith(
                          color: Colors.white,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 1,
                        ),
                      ),
                    ),
                    const SizedBox(height: 12),
                  ],

                  const Spacer(),

                  // Title
                  Text(
                    title,
                    style: AppTypography.headlineLarge.copyWith(
                      color: Colors.white,
                      fontWeight: FontWeight.w800,
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 8),

                  // Subtitle
                  Text(
                    subtitle,
                    style: AppTypography.bodyMedium.copyWith(
                      color: Colors.white.withOpacity(0.85),
                    ),
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                  ),

                  // Bottom widget
                  if (bottomWidget != null) ...[
                    const SizedBox(height: 16),
                    bottomWidget!,
                  ],
                ],
              ),
            ),

            // Arrow indicator
            Positioned(
              right: 20,
              top: 20,
              child: Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.white.withOpacity(0.2),
                  shape: BoxShape.circle,
                ),
                child: const Icon(
                  Icons.arrow_forward_rounded,
                  color: Colors.white,
                  size: 20,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

// =============================================================================
// CATEGORY CARD - Kategori kartları için
// =============================================================================
class CategoryCard extends StatefulWidget {
  final String title;
  final String? subtitle;
  final IconData icon;
  final Color color;
  final VoidCallback? onTap;
  final bool isSelected;
  final double width;
  final double height;

  const CategoryCard({
    super.key,
    required this.title,
    this.subtitle,
    required this.icon,
    required this.color,
    this.onTap,
    this.isSelected = false,
    this.width = 120,
    this.height = 140,
  });

  @override
  State<CategoryCard> createState() => _CategoryCardState();
}

class _CategoryCardState extends State<CategoryCard>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(duration: AppDurations.fast, vsync: this);
    _scaleAnimation = Tween<double>(
      begin: 1.0,
      end: 0.95,
    ).animate(CurvedAnimation(parent: _controller, curve: AppCurves.smooth));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  List<BoxShadow> _getShadow() {
    if (widget.isSelected) {
      return AppShadows.coloredSoft(widget.color);
    }
    return AppShadows.soft;
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTapDown: (_) => _controller.forward(),
      onTapUp: (_) => _controller.reverse(),
      onTapCancel: () => _controller.reverse(),
      onTap: widget.onTap,
      child: AnimatedBuilder(
        animation: _scaleAnimation,
        builder: (context, child) {
          return Transform.scale(
            scale: _scaleAnimation.value,
            child: AnimatedContainer(
              duration: AppDurations.normal,
              width: widget.width,
              height: widget.height,
              decoration: BoxDecoration(
                gradient: widget.isSelected
                    ? LinearGradient(
                        begin: Alignment.topLeft,
                        end: Alignment.bottomRight,
                        colors: [widget.color, widget.color.withOpacity(0.8)],
                      )
                    : null,
                color: widget.isSelected ? null : AppColors.surface,
                borderRadius: BorderRadius.circular(24),
                border: Border.all(
                  color: widget.isSelected
                      ? widget.color
                      : AppColors.surfaceVariant,
                  width: widget.isSelected ? 2 : 1,
                ),
                boxShadow: _getShadow(),
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // Icon container
                  AnimatedContainer(
                    duration: AppDurations.normal,
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: widget.isSelected
                          ? Colors.white.withOpacity(0.2)
                          : widget.color.withOpacity(0.1),
                      shape: BoxShape.circle,
                    ),
                    child: Icon(
                      widget.icon,
                      size: 28,
                      color: widget.isSelected ? Colors.white : widget.color,
                    ),
                  ),
                  const SizedBox(height: 12),

                  // Title
                  Text(
                    widget.title,
                    style: AppTypography.labelLarge.copyWith(
                      color: widget.isSelected
                          ? Colors.white
                          : AppColors.textPrimary,
                    ),
                    textAlign: TextAlign.center,
                  ),

                  // Subtitle
                  if (widget.subtitle != null) ...[
                    const SizedBox(height: 4),
                    Text(
                      widget.subtitle!,
                      style: AppTypography.bodySmall.copyWith(
                        color: widget.isSelected
                            ? Colors.white.withOpacity(0.8)
                            : AppColors.textTertiary,
                      ),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}

// =============================================================================
// PLACE CARD - Mekan kartı (yatay scroll için)
// =============================================================================
class PlaceCardPremium extends StatelessWidget {
  final String name;
  final String location;
  final String? imageUrl;
  final double? rating;
  final String? distance;
  final String? price;
  final List<String>? tags;
  final VoidCallback? onTap;
  final VoidCallback? onFavorite;
  final bool isFavorite;

  const PlaceCardPremium({
    super.key,
    required this.name,
    required this.location,
    this.imageUrl,
    this.rating,
    this.distance,
    this.price,
    this.tags,
    this.onTap,
    this.onFavorite,
    this.isFavorite = false,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: 200,
        margin: const EdgeInsets.only(right: 16),
        decoration: BoxDecoration(
          color: AppColors.surface,
          borderRadius: BorderRadius.circular(24),
          boxShadow: AppShadows.soft,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Image section
            Stack(
              children: [
                Container(
                  height: 130,
                  decoration: const BoxDecoration(
                    borderRadius: BorderRadius.vertical(
                      top: Radius.circular(24),
                    ),
                    gradient: AppGradients.ocean,
                  ),
                  child: imageUrl != null
                      ? ClipRRect(
                          borderRadius: const BorderRadius.vertical(
                            top: Radius.circular(24),
                          ),
                          child: Image.network(
                            imageUrl!,
                            fit: BoxFit.cover,
                            width: double.infinity,
                            errorBuilder: (_, __, ___) => Center(
                              child: Icon(
                                Icons.place_rounded,
                                size: 48,
                                color: Colors.white.withOpacity(0.5),
                              ),
                            ),
                          ),
                        )
                      : Center(
                          child: Icon(
                            Icons.place_rounded,
                            size: 48,
                            color: Colors.white.withOpacity(0.5),
                          ),
                        ),
                ),

                // Favorite button
                Positioned(
                  top: 10,
                  right: 10,
                  child: GestureDetector(
                    onTap: onFavorite,
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        shape: BoxShape.circle,
                        boxShadow: AppShadows.soft,
                      ),
                      child: Icon(
                        isFavorite ? Icons.favorite : Icons.favorite_border,
                        size: 18,
                        color: isFavorite
                            ? AppColors.error
                            : AppColors.textTertiary,
                      ),
                    ),
                  ),
                ),

                // Rating badge
                if (rating != null)
                  Positioned(
                    bottom: 10,
                    left: 10,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 5,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(12),
                        boxShadow: AppShadows.soft,
                      ),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(
                            Icons.star_rounded,
                            size: 14,
                            color: AppColors.warning,
                          ),
                          const SizedBox(width: 4),
                          Text(
                            rating!.toStringAsFixed(1),
                            style: AppTypography.labelSmall.copyWith(
                              fontWeight: FontWeight.w700,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
              ],
            ),

            // Content section
            Padding(
              padding: const EdgeInsets.all(14),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    name,
                    style: AppTypography.labelLarge,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 4),
                  Row(
                    children: [
                      Icon(
                        Icons.location_on_outlined,
                        size: 14,
                        color: AppColors.textTertiary,
                      ),
                      const SizedBox(width: 4),
                      Expanded(
                        child: Text(
                          location,
                          style: AppTypography.bodySmall,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),

                  // Tags or info row
                  Row(
                    children: [
                      if (distance != null)
                        _InfoChip(
                          icon: Icons.directions_walk_rounded,
                          text: distance!,
                        ),
                      if (price != null) ...[
                        const SizedBox(width: 8),
                        _InfoChip(icon: Icons.payments_outlined, text: price!),
                      ],
                    ],
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _InfoChip extends StatelessWidget {
  final IconData icon;
  final String text;

  const _InfoChip({required this.icon, required this.text});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: AppColors.surfaceVariant,
        borderRadius: BorderRadius.circular(8),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 12, color: AppColors.textSecondary),
          const SizedBox(width: 4),
          Text(
            text,
            style: AppTypography.labelSmall.copyWith(
              color: AppColors.textSecondary,
            ),
          ),
        ],
      ),
    );
  }
}
