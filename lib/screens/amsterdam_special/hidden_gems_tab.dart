import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../widgets/amsterdam_special/shared_widgets.dart';

class HiddenGemsTab extends StatelessWidget {
  final HiddenGemsSection data;
  const HiddenGemsTab({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        SectionHeader(title: data.title, intro: data.intro),
        ...data.items.map((g) => _GemCard(gem: g)),
        CalloutBox(callout: data.callout),
        const SizedBox(height: 16),
      ],
    );
  }
}

class _GemCard extends StatelessWidget {
  final HiddenGem gem;
  const _GemCard({required this.gem});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight),
        boxShadow: [
          BoxShadow(
            color: WanderlustColors.accentPink.withOpacity(0.03),
            blurRadius: 12,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      padding: const EdgeInsets.all(12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            gem.rarity.toUpperCase(),
            style: const TextStyle(fontSize: 10, color: WanderlustColors.accentPink, fontWeight: FontWeight.bold, letterSpacing: 1.0),
          ),
          const SizedBox(height: 6),
          Text(gem.name, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: WanderlustColors.textWhite)),
          const SizedBox(height: 6),
          Text(gem.description, style: const TextStyle(fontSize: 13, color: WanderlustColors.textGrey, height: 1.6)),
        ],
      ),
    );
  }
}
