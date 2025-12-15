import 'package:flutter/material.dart';
import '../models/place_model.dart';

class PlaceListTile extends StatelessWidget {
  final PlaceModel place;

  const PlaceListTile({super.key, required this.place});

  Color _getCategoryColor() {
    switch (place.category.toLowerCase()) {
      case "kafe":
        return const Color(0xFFFDAA5D);
      case "restoran":
        return const Color(0xFFFF7675);
      case "bar":
        return const Color(0xFFA29BFE);
      case "müze":
        return const Color(0xFF74B9FF);
      case "park":
        return const Color(0xFF00B894);
      default:
        return const Color(0xFF636E72);
    }
  }

  IconData _getCategoryIcon() {
    switch (place.category.toLowerCase()) {
      case "kafe":
        return Icons.local_cafe_rounded;
      case "restoran":
        return Icons.restaurant_rounded;
      case "bar":
        return Icons.local_bar_rounded;
      case "müze":
        return Icons.museum_rounded;
      case "park":
        return Icons.park_rounded;
      default:
        return Icons.place_rounded;
    }
  }

  Widget _buildPlaceholder() {
    final color = _getCategoryColor();
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [color, color.withOpacity(0.7)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
      ),
      child: Center(
        child: Icon(
          _getCategoryIcon(),
          size: 28,
          color: Colors.white.withOpacity(0.9),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final color = _getCategoryColor();
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;

    return Container(
      margin: const EdgeInsets.only(bottom: 14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.grey.shade200),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          // Image
          ClipRRect(
            borderRadius: const BorderRadius.horizontal(
              left: Radius.circular(16),
            ),
            child: SizedBox(
              width: 90,
              height: 90,
              child: hasImage
                  ? Image.network(
                      place.imageUrl!,
                      fit: BoxFit.cover,
                      loadingBuilder: (_, child, progress) {
                        if (progress == null) return child;
                        return _buildPlaceholder();
                      },
                      errorBuilder: (_, __, ___) => _buildPlaceholder(),
                    )
                  : _buildPlaceholder(),
            ),
          ),

          // Content
          Expanded(
            child: Padding(
              padding: const EdgeInsets.all(12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Expanded(
                        child: Text(
                          place.name,
                          style: const TextStyle(
                            color: Color(0xFF2D3436),
                            fontSize: 15,
                            fontWeight: FontWeight.w700,
                          ),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                        ),
                      ),
                      Row(
                        children: [
                          Icon(
                            Icons.star_rounded,
                            size: 14,
                            color: Colors.amber.shade600,
                          ),
                          const SizedBox(width: 2),
                          Text(
                            "${place.rating}",
                            style: const TextStyle(
                              fontSize: 13,
                              fontWeight: FontWeight.w600,
                              color: Color(0xFF2D3436),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 4),
                  Text(
                    place.address,
                    style: TextStyle(color: Colors.grey.shade500, fontSize: 12),
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                  ),
                  const SizedBox(height: 8),
                  Row(
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 3,
                        ),
                        decoration: BoxDecoration(
                          color: color.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          place.category,
                          style: TextStyle(
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                            color: color,
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),
                      Icon(
                        Icons.directions_walk_rounded,
                        size: 12,
                        color: Colors.grey.shade400,
                      ),
                      const SizedBox(width: 2),
                      Text(
                        "${place.distanceKm} km",
                        style: TextStyle(
                          fontSize: 11,
                          color: Colors.grey.shade500,
                        ),
                      ),
                      const Spacer(),
                      Container(
                        padding: const EdgeInsets.symmetric(
                          horizontal: 8,
                          vertical: 3,
                        ),
                        decoration: BoxDecoration(
                          color: place.isOpen
                              ? const Color(0xFF00B894).withOpacity(0.1)
                              : Colors.grey.shade100,
                          borderRadius: BorderRadius.circular(6),
                        ),
                        child: Text(
                          place.isOpen ? "Açık" : "Kapalı",
                          style: TextStyle(
                            color: place.isOpen
                                ? const Color(0xFF00B894)
                                : Colors.grey.shade500,
                            fontWeight: FontWeight.w600,
                            fontSize: 11,
                          ),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
