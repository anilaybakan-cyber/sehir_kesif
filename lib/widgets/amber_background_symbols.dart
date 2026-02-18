
import 'package:flutter/material.dart';
import '../theme/wanderlust_colors.dart';

class AmberBackgroundSymbols extends StatelessWidget {
  final double opacity;
  final double scale;

  const AmberBackgroundSymbols({
    super.key,
    this.opacity = 0.15, // Default subtle opacity, user liked 0.25 for the main card but might be too strong for smaller cards? Let's default to a bit lower or keep 0.25 if they want "uniformity". User said "bunu tüm kartlara ekleyebilir miyiz", implying the same look. Let's try 0.20 as a safe middle or 0.25. Let's stick to 0.25 as requested implicitly.
    this.scale = 0.8, // Scale down for smaller cards
  });
  
  @override
  Widget build(BuildContext context) {
    final color = WanderlustColors.accent; // Purple

    return Positioned.fill(
      child: ClipRRect( // Ensure it doesn't bleed out of card corners
        borderRadius: BorderRadius.circular(16), // Match typical card radius
        child: Opacity(
          opacity: opacity,
          child: Stack(
            children: [
              Positioned(
                right: -15 * scale,
                top: -15 * scale,
                child: Transform.rotate(
                  angle: 0.2,
                  child: Icon(Icons.flight_takeoff_rounded, size: 80 * scale, color: color),
                ),
              ),
              Positioned(
                left: -20 * scale,
                bottom: -15 * scale,
                child: Transform.rotate(
                  angle: -0.1,
                  child: Icon(Icons.luggage_rounded, size: 70 * scale, color: color),
                ),
              ),
              Positioned(
                right: 30 * scale,
                bottom: -25 * scale,
                child: Transform.rotate(
                  angle: 0.15,
                  child: Icon(Icons.confirmation_number_rounded, size: 60 * scale, color: color),
                ),
              ),
              // Extra icon for variety on potentially larger or different cards? 
              // Keeping it simple with the 3 requested ones for now.
            ],
          ),
        ),
      ),
    );
  }
}
