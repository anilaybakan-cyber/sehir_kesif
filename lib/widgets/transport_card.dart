import 'package:flutter/material.dart';
import '../models/transport_model.dart';
import 'base_glass_card.dart';
import 'info_row.dart';

class TransportCard extends StatelessWidget {
  final TransportModel transport;

  const TransportCard({super.key, required this.transport});

  @override
  Widget build(BuildContext context) {
    return BaseGlassCard(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "HAVAALANI ULAŞIMI",
            style: TextStyle(
              color: Colors.teal.shade700,
              fontSize: 14,
              letterSpacing: 1.1,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 12),
          InfoRow(title: "En hızlı seçenek", value: transport.fastest),
          InfoRow(title: "En ucuz seçenek", value: transport.cheapest),
          const SizedBox(height: 8),
          const Text(
            "Alternatifler:",
            style: TextStyle(color: Colors.black87, fontSize: 14),
          ),
          const SizedBox(height: 6),
          ...transport.options.map(
            (o) => Padding(
              padding: const EdgeInsets.only(left: 6, bottom: 4),
              child: Text(
                "• $o",
                style: const TextStyle(color: Colors.black54, fontSize: 13),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
