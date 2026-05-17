import 'package:flutter/material.dart';
import 'package:flutter_blurhash/flutter_blurhash.dart';
import 'package:cached_network_image/cached_network_image.dart';
import '../utils/image_utils.dart';
import '../theme/wanderlust_colors.dart';

/// Görselleri yüksek hızla ve otomatik hata kurtarmayla yükleyen widget.
class ResilientNetworkImage extends StatefulWidget {
  final String? imageUrl;
  final String placeName;
  final String city;
  final String category;
  final double? width;
  final double? height;
  final BoxFit fit;
  final BorderRadius? borderRadius;
  final Widget Function(BuildContext context)? placeholderBuilder;
  final String? blurHash;
  final int? memCacheWidth;
  final int? memCacheHeight;
  final int? maxWidthDiskCache;
  final int? maxHeightDiskCache;
  final bool highQualityDecode;
  final Duration fadeInDuration;

  const ResilientNetworkImage({
    super.key,
    required this.imageUrl,
    required this.placeName,
    required this.city,
    required this.category,
    this.width,
    this.height,
    this.fit = BoxFit.cover,
    this.borderRadius,
    this.placeholderBuilder,
    this.fadeInDuration = const Duration(milliseconds: 50),
    this.blurHash,
    this.memCacheWidth,
    this.memCacheHeight,
    this.maxWidthDiskCache,
    this.maxHeightDiskCache,
    this.highQualityDecode = false,
  });

  @override
  State<ResilientNetworkImage> createState() => _ResilientNetworkImageState();
}

class _ResilientNetworkImageState extends State<ResilientNetworkImage> {
  bool _useFallback = false;

  String? _getPrimaryUrl() {
    if (widget.imageUrl == null) return null;
    final trimmed = widget.imageUrl!.trim();
    if (trimmed.isEmpty) return null;
    return resolveOptimizedImageUrl(trimmed, isHero: widget.highQualityDecode);
  }

  String? _getFallbackUrl() {
    if (widget.imageUrl == null) return null;
    final trimmed = widget.imageUrl!.trim();
    if (trimmed.isEmpty) return null;
    return firebaseCompatibleImageUrl(trimmed);
  }

  Widget _buildPlaceholder(BuildContext context) {
    if (widget.placeholderBuilder != null) {
      return widget.placeholderBuilder!(context);
    }

    // 🌟 BlurHash varsa anında göster (Sıfır placeholder hissi)
    if (widget.blurHash != null && widget.blurHash!.isNotEmpty) {
      return Container(
        width: widget.width ?? double.infinity,
        height: widget.height ?? double.infinity,
        decoration: BoxDecoration(borderRadius: widget.borderRadius),
        clipBehavior: widget.borderRadius != null ? Clip.antiAlias : Clip.none,
        child: BlurHash(
          hash: widget.blurHash!,
          imageFit: widget.fit,
        ),
      );
    }

    final gradient = _getCategoryGradient(widget.category);
    return Container(
      width: widget.width ?? double.infinity,
      height: widget.height ?? double.infinity,
      decoration: BoxDecoration(
        gradient: gradient,
        borderRadius: widget.borderRadius,
      ),
      child: Center(
        child: Icon(
          _getCategoryIcon(widget.category),
          color: Colors.white.withOpacity(0.8),
          size: 48,
        ),
      ),
    );
  }

  LinearGradient _getCategoryGradient(String cat) {
    final lowerCat = cat.toLowerCase();
    if (lowerCat.contains('food') || lowerCat.contains('restaurant') || lowerCat.contains('cafe')) {
      return WanderlustColors.primaryGradient;
    } else if (lowerCat.contains('night') || lowerCat.contains('bar') || lowerCat.contains('club')) {
      return const LinearGradient(colors: [Color(0xFF9C27B0), Color(0xFFE91E63)]);
    } else if (lowerCat.contains('nature') || lowerCat.contains('park') || lowerCat.contains('garden')) {
      return const LinearGradient(colors: [Color(0xFF4CAF50), Color(0xFF8BC34A)]);
    } else if (lowerCat.contains('art') || lowerCat.contains('museum') || lowerCat.contains('gallery')) {
      return const LinearGradient(colors: [Color(0xFFFF9800), Color(0xFFFFC107)]);
    } else if (lowerCat.contains('shopping') || lowerCat.contains('market')) {
      return const LinearGradient(colors: [Color(0xFFE91E63), Color(0xFF9C27B0)]);
    } else if (lowerCat.contains('history') || lowerCat.contains('monument') || lowerCat.contains('castle')) {
      return const LinearGradient(colors: [Color(0xFF795548), Color(0xFFA1887F)]);
    } else if (lowerCat.contains('beach') || lowerCat.contains('sea') || lowerCat.contains('water')) {
      return const LinearGradient(colors: [Color(0xFF2196F3), Color(0xFF03A9F4)]);
    } else if (lowerCat.contains('adventure') || lowerCat.contains('sport') || lowerCat.contains('hike')) {
      return const LinearGradient(colors: [Color(0xFFFF5722), Color(0xFFFF9800)]);
    } else {
      return WanderlustColors.accentGradient;
    }
  }

  IconData _getCategoryIcon(String cat) {
    final lowerCat = cat.toLowerCase();
    if (lowerCat.contains('food') || lowerCat.contains('restaurant') || lowerCat.contains('cafe')) {
      return Icons.restaurant;
    } else if (lowerCat.contains('night') || lowerCat.contains('bar') || lowerCat.contains('club')) {
      return Icons.nightlife;
    } else if (lowerCat.contains('nature') || lowerCat.contains('park') || lowerCat.contains('garden')) {
      return Icons.nature;
    } else if (lowerCat.contains('art') || lowerCat.contains('museum') || lowerCat.contains('gallery')) {
      return Icons.palette;
    } else if (lowerCat.contains('shopping') || lowerCat.contains('market')) {
      return Icons.shopping_bag;
    } else if (lowerCat.contains('history') || lowerCat.contains('monument') || lowerCat.contains('castle')) {
      return Icons.account_balance;
    } else if (lowerCat.contains('beach') || lowerCat.contains('sea') || lowerCat.contains('water')) {
      return Icons.beach_access;
    } else if (lowerCat.contains('adventure') || lowerCat.contains('sport') || lowerCat.contains('hike')) {
      return Icons.terrain;
    } else {
      return Icons.location_on;
    }
  }

  Widget _buildFastImage(BuildContext context, String url, double lw, double lh) {
    final effectiveWidth = lw.isFinite && lw > 0 ? lw : null;
    final effectiveHeight = lh.isFinite && lh > 0 ? lh : null;

    Widget image = CachedNetworkImage(
      imageUrl: url,
      key: ValueKey(url),
      width: effectiveWidth,
      height: effectiveHeight,
      fit: widget.fit,
      cacheManager: AppImageCacheManager.instance,
      fadeInDuration: widget.fadeInDuration,
      memCacheWidth: widget.memCacheWidth,
      memCacheHeight: widget.memCacheHeight,
      placeholder: (ctx, url) => _buildPlaceholder(ctx),
      errorWidget: (ctx, url, error) {
        if (!_useFallback) {
          WidgetsBinding.instance.addPostFrameCallback((_) {
            if (mounted) {
              setState(() {
                _useFallback = true;
              });
            }
          });
          return _buildPlaceholder(ctx);
        }
        return _buildPlaceholder(ctx);
      },
    );

    if (widget.borderRadius != null) {
      image = ClipRRect(borderRadius: widget.borderRadius!, child: image);
    }

    return image;
  }

  @override
  Widget build(BuildContext context) {
    final url = _useFallback ? _getFallbackUrl() : _getPrimaryUrl();
    if (url == null) return _buildPlaceholder(context);

    return _buildFastImage(
      context, 
      url, 
      widget.width ?? double.infinity, 
      widget.height ?? double.infinity,
    );
  }
}
