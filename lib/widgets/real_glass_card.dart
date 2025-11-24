// Dosya: lib/widgets/real_glass_card.dart

import 'dart:ui';
import 'package:flutter/material.dart';

class RealGlassCard extends StatelessWidget {
  final Widget child;
  final double opacity;

  const RealGlassCard({super.key, required this.child, this.opacity = 0.2});

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(24),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 12, sigmaY: 12), // Bulanıklık seviyesi
        child: Container(
          padding: const EdgeInsets.all(18),
          decoration: BoxDecoration(
            color: Colors.white.withOpacity(opacity), // Şeffaf beyaz
            borderRadius: BorderRadius.circular(24),
            border: Border.all(
              color: Colors.white.withOpacity(0.3), // İnce parlak kenarlık
              width: 1.5,
            ),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.05),
                blurRadius: 20,
                offset: const Offset(0, 10),
              ),
            ],
          ),
          child: child,
        ),
      ),
    );
  }
}
