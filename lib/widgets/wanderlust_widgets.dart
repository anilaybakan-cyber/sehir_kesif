// lib/widgets/wanderlust_widgets.dart
// 🧩 Wanderlust UI Components
// Glassmorphism + Gradient + Organic animations

import 'package:flutter/material.dart';
import 'dart:ui';
import 'dart:math' as math;

// Eğer ileride direkt renkler/spacing kullanmak istersen açarsın.
// import '../theme/wanderlust_design_system.dart';

/// ═══════════════════════════════════════════════════════════════════════════
/// 🔮 GLASS CONTAINER
/// ═══════════════════════════════════════════════════════════════════════════

class GlassContainer extends StatelessWidget {
  final Widget child;
  final double? width;
  final double? height;
  final EdgeInsets? padding;
  final EdgeInsets? margin;
  final double borderRadius;
  final double blurAmount;
  final Color? tintColor;
  final double opacity;
  final bool hasBorder;
  final VoidCallback? onTap;

  const GlassContainer({
    super.key,
    required this.child,
    this.width,
    this.height,
    this.padding,
    this.margin,
    this.borderRadius = 24,
    this.blurAmount = 20,
    this.tintColor,
    this.opacity = 0.15,
    this.hasBorder = true,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final bgColor = (tintColor ?? Colors.white).withOpacity(opacity);

    return GestureDetector(
      onTap: onTap,
      child: Container(
        width: width,
        height: height,
        margin: margin,
        child: ClipRRect(
          borderRadius: BorderRadius.circular(borderRadius),
          child: BackdropFilter(
            filter: ImageFilter.blur(sigmaX: blurAmount, sigmaY: blurAmount),
            child: Container(
              padding: padding,
              decoration: BoxDecoration(
                color: bgColor,
                borderRadius: BorderRadius.circular(borderRadius),
                border: hasBorder
                    ? Border.all(
                        color: Colors.white.withOpacity(0.2),
                        width: 1.5,
                      )
                    : null,
              ),
              child: child,
            ),
          ),
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🌈 GRADIENT BUTTON
/// ═══════════════════════════════════════════════════════════════════════════

class GradientButton extends StatefulWidget {
  final String text;
  final VoidCallback onPressed;
  final LinearGradient? gradient;
  final IconData? icon;
  final bool isLoading;
  final bool isFullWidth;
  final double height;
  final double borderRadius;

  const GradientButton({
    super.key,
    required this.text,
    required this.onPressed,
    this.gradient,
    this.icon,
    this.isLoading = false,
    this.isFullWidth = false,
    this.height = 56,
    this.borderRadius = 28,
  });

  @override
  State<GradientButton> createState() => _GradientButtonState();
}

class _GradientButtonState extends State<GradientButton>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _scaleAnimation;

  static const _defaultGradient = LinearGradient(
    begin: Alignment.topLeft,
    end: Alignment.bottomRight,
    colors: [Color(0xFFFF6B6B), Color(0xFFFFAB76)],
  );

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 150),
      vsync: this,
    );
    _scaleAnimation = Tween<double>(
      begin: 1.0,
      end: 0.95,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeInOut));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _handleTap() {
    if (!widget.isLoading) widget.onPressed();
  }

  @override
  Widget build(BuildContext context) {
    final gradient = widget.gradient ?? _defaultGradient;

    return GestureDetector(
      onTapDown: (_) => _controller.forward(),
      onTapUp: (_) {
        _controller.reverse();
        _handleTap();
      },
      onTapCancel: () => _controller.reverse(),
      child: AnimatedBuilder(
        animation: _scaleAnimation,
        builder: (context, child) {
          return Transform.scale(scale: _scaleAnimation.value, child: child);
        },
        child: Container(
          width: widget.isFullWidth ? double.infinity : null,
          height: widget.height,
          decoration: BoxDecoration(
            gradient: gradient,
            borderRadius: BorderRadius.circular(widget.borderRadius),
            boxShadow: [
              BoxShadow(
                color: gradient.colors.first.withOpacity(0.4),
                blurRadius: 20,
                offset: const Offset(0, 8),
              ),
            ],
          ),
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              borderRadius: BorderRadius.circular(widget.borderRadius),
              onTap: widget.isLoading ? null : _handleTap,
              child: Padding(
                padding: const EdgeInsets.symmetric(horizontal: 32),
                child: Row(
                  mainAxisSize: widget.isFullWidth
                      ? MainAxisSize.max
                      : MainAxisSize.min,
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    if (widget.isLoading)
                      const SizedBox(
                        width: 24,
                        height: 24,
                        child: CircularProgressIndicator(
                          strokeWidth: 2.5,
                          valueColor: AlwaysStoppedAnimation<Color>(
                            Colors.white,
                          ),
                        ),
                      )
                    else ...[
                      if (widget.icon != null) ...[
                        Icon(widget.icon, color: Colors.white, size: 22),
                        const SizedBox(width: 10),
                      ],
                      const SizedBox(width: 2),
                      Text(
                        widget.text,
                        style: const TextStyle(
                          fontFamily: 'Outfit',
                          fontSize: 16,
                          fontWeight: FontWeight.w600,
                          color: Colors.white,
                          letterSpacing: 0.5,
                        ),
                      ),
                    ],
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🎴 GRADIENT CARD
/// ═══════════════════════════════════════════════════════════════════════════

class GradientCard extends StatefulWidget {
  final Widget child;
  final String? imageUrl;
  final LinearGradient? overlayGradient;
  final double height;
  final double? width; // ⭐ ExploreScreen için eklendi
  final double borderRadius;
  final VoidCallback? onTap;
  final List<BoxShadow>? boxShadow;

  const GradientCard({
    super.key,
    required this.child,
    this.imageUrl,
    this.overlayGradient,
    this.height = 200,
    this.width,
    this.borderRadius = 24,
    this.onTap,
    this.boxShadow,
  });

  @override
  State<GradientCard> createState() => _GradientCardState();
}

class _GradientCardState extends State<GradientCard>
    with SingleTickerProviderStateMixin {
  late AnimationController _hoverController;
  late Animation<double> _elevationAnimation;

  @override
  void initState() {
    super.initState();
    _hoverController = AnimationController(
      duration: const Duration(milliseconds: 200),
      vsync: this,
    );
    _elevationAnimation = Tween<double>(
      begin: 0,
      end: 1,
    ).animate(CurvedAnimation(parent: _hoverController, curve: Curves.easeOut));
  }

  @override
  void dispose() {
    _hoverController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTapDown: (_) => _hoverController.forward(),
      onTapUp: (_) {
        _hoverController.reverse();
        widget.onTap?.call();
      },
      onTapCancel: () => _hoverController.reverse(),
      child: AnimatedBuilder(
        animation: _elevationAnimation,
        builder: (context, child) {
          return Transform.scale(
            scale: 1 - (_elevationAnimation.value * 0.02),
            child: child,
          );
        },
        child: Container(
          height: widget.height,
          width: widget.width,
          decoration: BoxDecoration(
            borderRadius: BorderRadius.circular(widget.borderRadius),
            boxShadow:
                widget.boxShadow ??
                [
                  BoxShadow(
                    color: Colors.black.withOpacity(
                      0.08 + _elevationAnimation.value * 0.04,
                    ),
                    blurRadius: 20 + (_elevationAnimation.value * 10),
                    offset: Offset(0, 8 + (_elevationAnimation.value * 4)),
                  ),
                ],
          ),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(widget.borderRadius),
            child: Stack(
              fit: StackFit.expand,
              children: [
                if (widget.imageUrl != null)
                  Image.network(
                    widget.imageUrl!,
                    fit: BoxFit.cover,
                    errorBuilder: (_, __, ___) => Container(
                      decoration: BoxDecoration(
                        gradient:
                            widget.overlayGradient ??
                            const LinearGradient(
                              begin: Alignment.topLeft,
                              end: Alignment.bottomRight,
                              colors: [Color(0xFF667EEA), Color(0xFF764BA2)],
                            ),
                      ),
                    ),
                  )
                else
                  Container(
                    decoration: BoxDecoration(
                      gradient:
                          widget.overlayGradient ??
                          const LinearGradient(
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                            colors: [Color(0xFF667EEA), Color(0xFF764BA2)],
                          ),
                    ),
                  ),

                // Gradient overlay
                Container(
                  decoration: BoxDecoration(
                    gradient:
                        widget.overlayGradient ??
                        LinearGradient(
                          begin: Alignment.topCenter,
                          end: Alignment.bottomCenter,
                          colors: [
                            Colors.transparent,
                            Colors.black.withOpacity(0.3),
                            Colors.black.withOpacity(0.7),
                          ],
                          stops: const [0.0, 0.5, 1.0],
                        ),
                  ),
                ),

                widget.child,
              ],
            ),
          ),
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🏷️ CATEGORY CHIP
/// ═══════════════════════════════════════════════════════════════════════════

class CategoryChip extends StatelessWidget {
  final String label;
  final Color? color;
  final IconData? icon;
  final bool isSelected;
  final VoidCallback? onTap;

  const CategoryChip({
    super.key,
    required this.label,
    this.color,
    this.icon,
    this.isSelected = false,
    this.onTap,
  });

  Color _getCategoryColor() {
    final colors = {
      'Restoran': const Color(0xFFFF6B6B),
      'Bar': const Color(0xFF9B59B6),
      'Kafe': const Color(0xFFE17055),
      'Müze': const Color(0xFF3498DB),
      'Tarihi': const Color(0xFFD4A574),
      'Park': const Color(0xFF00B894),
      'Manzara': const Color(0xFF00CEC9),
      'Alışveriş': const Color(0xFFFD79A8),
      'Semt': const Color(0xFFA29BFE),
      'Deneyim': const Color(0xFFFDCB6E),
    };
    return color ?? colors[label] ?? const Color(0xFF667EEA);
  }

  @override
  Widget build(BuildContext context) {
    final chipColor = _getCategoryColor();

    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: isSelected ? chipColor : chipColor.withOpacity(0.12),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isSelected ? chipColor : chipColor.withOpacity(0.3),
            width: 1.5,
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            if (icon != null) ...[
              Icon(
                icon,
                size: 16,
                color: isSelected ? Colors.white : chipColor,
              ),
              const SizedBox(width: 6),
            ],
            Text(
              label,
              style: TextStyle(
                fontFamily: 'Outfit',
                fontSize: 13,
                fontWeight: FontWeight.w600,
                color: isSelected ? Colors.white : chipColor,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// ⭐ RATING BADGE
/// ═══════════════════════════════════════════════════════════════════════════

class RatingBadge extends StatelessWidget {
  final double rating;
  final int? reviewCount;
  final bool showReviews;
  final bool isGlass;

  const RatingBadge({
    super.key,
    required this.rating,
    this.reviewCount,
    this.showReviews = true,
    this.isGlass = false,
  });

  @override
  Widget build(BuildContext context) {
    final content = Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        const Icon(Icons.star_rounded, color: Color(0xFFFDCB6E), size: 18),
        const SizedBox(width: 4),
        Text(
          rating.toStringAsFixed(1),
          style: TextStyle(
            fontFamily: 'DM Sans',
            fontSize: 14,
            fontWeight: FontWeight.w700,
            color: isGlass ? Colors.white : const Color(0xFF2D3436),
          ),
        ),
        if (showReviews && reviewCount != null) ...[
          const SizedBox(width: 4),
          Text(
            '(${_formatCount(reviewCount!)})',
            style: TextStyle(
              fontFamily: 'DM Sans',
              fontSize: 12,
              fontWeight: FontWeight.w400,
              color: isGlass
                  ? Colors.white.withOpacity(0.7)
                  : const Color(0xFF636E72),
            ),
          ),
        ],
      ],
    );

    if (isGlass) {
      return ClipRRect(
        borderRadius: BorderRadius.circular(12),
        child: BackdropFilter(
          filter: ImageFilter.blur(sigmaX: 10, sigmaY: 10),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.3),
              borderRadius: BorderRadius.circular(12),
            ),
            child: content,
          ),
        ),
      );
    }

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
      decoration: BoxDecoration(
        color: const Color(0xFFFDCB6E).withOpacity(0.15),
        borderRadius: BorderRadius.circular(12),
      ),
      child: content,
    );
  }

  String _formatCount(int count) {
    if (count >= 1000) {
      return '${(count / 1000).toStringAsFixed(1)}K';
    }
    return count.toString();
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🔍 ANIMATED SEARCH BAR
/// ═══════════════════════════════════════════════════════════════════════════

class AnimatedSearchBar extends StatefulWidget {
  final String hintText;
  final ValueChanged<String>? onChanged;
  final VoidCallback? onTap;
  final bool isGlass;
  final TextEditingController? controller;

  const AnimatedSearchBar({
    super.key,
    this.hintText = 'Ara...',
    this.onChanged,
    this.onTap,
    this.isGlass = false,
    this.controller,
  });

  @override
  State<AnimatedSearchBar> createState() => _AnimatedSearchBarState();
}

class _AnimatedSearchBarState extends State<AnimatedSearchBar>
    with SingleTickerProviderStateMixin {
  late AnimationController _focusController;
  late Animation<double> _scaleAnimation;
  bool _isFocused = false;

  @override
  void initState() {
    super.initState();
    _focusController = AnimationController(
      duration: const Duration(milliseconds: 200),
      vsync: this,
    );
    _scaleAnimation = Tween<double>(
      begin: 1.0,
      end: 1.02,
    ).animate(CurvedAnimation(parent: _focusController, curve: Curves.easeOut));
  }

  @override
  void dispose() {
    _focusController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _scaleAnimation,
      builder: (context, child) {
        return Transform.scale(scale: _scaleAnimation.value, child: child);
      },
      child: widget.isGlass ? _buildGlassSearchBar() : _buildSolidSearchBar(),
    );
  }

  Widget _buildGlassSearchBar() {
    return ClipRRect(
      borderRadius: BorderRadius.circular(16),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: Container(
          height: 54,
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(0.15),
            borderRadius: BorderRadius.circular(16),
            border: Border.all(
              color: Colors.white.withOpacity(_isFocused ? 0.4 : 0.2),
              width: 1.5,
            ),
          ),
          child: _buildTextField(isGlass: true),
        ),
      ),
    );
  }

  Widget _buildSolidSearchBar() {
    return AnimatedContainer(
      duration: const Duration(milliseconds: 200),
      height: 54,
      decoration: BoxDecoration(
        color: const Color(0xFFF5F5F5),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: _isFocused
              ? const Color(0xFFFF6B6B).withOpacity(0.5)
              : Colors.transparent,
          width: 2,
        ),
        boxShadow: _isFocused
            ? [
                BoxShadow(
                  color: const Color(0xFFFF6B6B).withOpacity(0.15),
                  blurRadius: 20,
                  offset: const Offset(0, 4),
                ),
              ]
            : [],
      ),
      child: _buildTextField(isGlass: false),
    );
  }

  Widget _buildTextField({required bool isGlass}) {
    return TextField(
      controller: widget.controller,
      onChanged: widget.onChanged,
      onTap: () {
        widget.onTap?.call();
        setState(() => _isFocused = true);
        _focusController.forward();
      },
      onSubmitted: (_) {
        setState(() => _isFocused = false);
        _focusController.reverse();
      },
      style: TextStyle(
        fontFamily: 'DM Sans',
        fontSize: 16,
        color: isGlass ? Colors.white : const Color(0xFF2D3436),
      ),
      decoration: InputDecoration(
        hintText: widget.hintText,
        hintStyle: TextStyle(
          fontFamily: 'DM Sans',
          fontSize: 16,
          color: isGlass
              ? Colors.white.withOpacity(0.5)
              : const Color(0xFFB2BEC3),
        ),
        prefixIcon: Icon(
          Icons.search_rounded,
          color: isGlass
              ? Colors.white.withOpacity(0.7)
              : const Color(0xFF636E72),
        ),
        border: InputBorder.none,
        contentPadding: const EdgeInsets.symmetric(
          horizontal: 16,
          vertical: 16,
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 💰 PRICE INDICATOR
/// ═══════════════════════════════════════════════════════════════════════════

class PriceIndicator extends StatelessWidget {
  final int priceLevel; // 0-5
  final double iconSize;
  final Color? activeColor;
  final Color? inactiveColor;

  const PriceIndicator({
    super.key,
    required this.priceLevel,
    this.iconSize = 14,
    this.activeColor,
    this.inactiveColor,
  });

  @override
  Widget build(BuildContext context) {
    final active = activeColor ?? const Color(0xFF00B894);
    final inactive = inactiveColor ?? const Color(0xFFB2BEC3);

    if (priceLevel == 0) {
      return Text(
        'Ücretsiz',
        style: TextStyle(
          fontFamily: 'Outfit',
          fontSize: 12,
          fontWeight: FontWeight.w600,
          color: active,
        ),
      );
    }

    return Row(
      mainAxisSize: MainAxisSize.min,
      children: List.generate(
        4,
        (index) => Text(
          '₺',
          style: TextStyle(
            fontFamily: 'DM Sans',
            fontSize: iconSize,
            fontWeight: FontWeight.w700,
            color: index < priceLevel ? active : inactive,
          ),
        ),
      ),
    );
  }
}

/// ═══════════════════════════════════════════════════════════════════════════
/// 🎪 STAGGERED ANIMATION WRAPPER
/// ═══════════════════════════════════════════════════════════════════════════

class StaggeredAnimation extends StatefulWidget {
  final Widget child;
  final int index;
  final Duration delay;
  final Duration duration;
  final Offset offset;

  const StaggeredAnimation({
    super.key,
    required this.child,
    required this.index,
    this.delay = const Duration(milliseconds: 50),
    this.duration = const Duration(milliseconds: 400),
    this.offset = const Offset(0, 30),
  });

  @override
  State<StaggeredAnimation> createState() => _StaggeredAnimationState();
}

class _StaggeredAnimationState extends State<StaggeredAnimation>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _opacityAnimation;
  late Animation<Offset> _slideAnimation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(duration: widget.duration, vsync: this);

    _opacityAnimation = Tween<double>(
      begin: 0.0,
      end: 1.0,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeOut));

    _slideAnimation = Tween<Offset>(
      begin: widget.offset,
      end: Offset.zero,
    ).animate(CurvedAnimation(parent: _controller, curve: Curves.easeOutCubic));

    Future.delayed(widget.delay * widget.index, () {
      if (mounted) _controller.forward();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, child) {
        return Opacity(
          opacity: _opacityAnimation.value,
          child: Transform.translate(
            offset: _slideAnimation.value,
            child: child,
          ),
        );
      },
      child: widget.child,
    );
  }
}
