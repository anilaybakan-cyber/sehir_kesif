import 'package:flutter/material.dart';
import '../models/region_model.dart';
import 'base_glass_card.dart';

class RegionCard extends StatelessWidget {
  final RegionModel region;

  const RegionCard({super.key, required this.region});

  @override
  Widget build(BuildContext context) {
    return BaseGlassCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            region.name,
            style: const TextStyle(
              color: Colors.black87,
              fontSize: 16,
              fontWeight: FontWeight.w700,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            "${region.type} · ${region.price}",
            style: const TextStyle(color: Colors.black45, fontSize: 13),
          ),
          const SizedBox(height: 10),
          ...region.highlights.map(
            (h) => Padding(
              padding: const EdgeInsets.only(bottom: 4),
              child: Text(
                "• $h",
                style: const TextStyle(color: Colors.black87, fontSize: 13),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
