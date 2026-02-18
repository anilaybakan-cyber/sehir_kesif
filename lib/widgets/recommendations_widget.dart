import 'package:flutter/material.dart';
import '../models/recommendations_model.dart';
import 'base_glass_card.dart';

class RecommendationsWidget extends StatelessWidget {
  final RecommendationsModel rec;

  const RecommendationsWidget({super.key, required this.rec});

  Widget _buildList(List<String> items) {
    return Wrap(
      spacing: 8,
      runSpacing: 6,
      children: items
          .map(
            (i) => Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
              decoration: BoxDecoration(
                color: Colors.grey.shade100,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: Colors.grey.shade200),
              ),
              child: Text(
                i,
                style: const TextStyle(color: Colors.black87, fontSize: 13),
              ),
            ),
          )
          .toList(),
    );
  }

  @override
  Widget build(BuildContext context) {
    return BaseGlassCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "ÖNERİLER",
            style: TextStyle(
              color: Colors.teal.shade700,
              fontSize: 14,
              letterSpacing: 1.1,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 14),

          const Text("Kahvaltı", style: TextStyle(color: Colors.black54)),
          const SizedBox(height: 6),
          _buildList(rec.breakfast),

          const SizedBox(height: 12),
          const Text("Kahve", style: TextStyle(color: Colors.black54)),
          const SizedBox(height: 6),
          _buildList(rec.coffee),

          const SizedBox(height: 12),
          const Text("Akşam Yemeği", style: TextStyle(color: Colors.black54)),
          const SizedBox(height: 6),
          _buildList(rec.dinner),

          const SizedBox(height: 12),
          const Text("Barlar", style: TextStyle(color: Colors.black54)),
          const SizedBox(height: 6),
          _buildList(rec.bars),

          const SizedBox(height: 12),
          const Text("Hidden Gems", style: TextStyle(color: Colors.black54)),
          const SizedBox(height: 6),
          _buildList(rec.hiddenGems),
        ],
      ),
    );
  }
}
