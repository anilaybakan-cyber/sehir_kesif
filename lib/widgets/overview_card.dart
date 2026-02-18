import 'package:flutter/material.dart';
import 'base_glass_card.dart';

class OverviewCard extends StatelessWidget {
  final String overview;

  const OverviewCard({super.key, required this.overview});

  @override
  Widget build(BuildContext context) {
    return BaseGlassCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "ŞEHİR GENEL BAKIŞI",
            style: TextStyle(
              color: Colors.teal.shade700,
              fontSize: 14,
              letterSpacing: 1.1,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 10),
          Text(
            overview,
            style: const TextStyle(
              color: Colors.black87,
              height: 1.4,
              fontSize: 14,
            ),
          ),
        ],
      ),
    );
  }
}
