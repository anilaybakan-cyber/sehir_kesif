import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../widgets/amsterdam_special/shared_widgets.dart';

class FoodTab extends StatelessWidget {
  final FoodSection data;
  const FoodTab({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        SectionHeader(title: data.title, intro: data.intro),
        PhraseBox(word: data.localWord),
        ...data.items.map((f) => _FoodCard(item: f)),
        CalloutBox(callout: data.callout),
        const SizedBox(height: 16),
      ],
    );
  }
}

class _FoodCard extends StatelessWidget {
  final FoodItem item;
  const _FoodCard({required this.item});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: WanderlustColors.borderLight),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.02),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 48,
            height: 48,
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.08),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Center(child: Text(item.icon, style: const TextStyle(fontSize: 24))),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(item.name, style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: WanderlustColors.textWhite)),
                const SizedBox(height: 4),
                Text(item.description, style: const TextStyle(fontSize: 12, color: WanderlustColors.textGrey, height: 1.5)),
                const SizedBox(height: 6),
                Text(item.tag.toUpperCase(),
                    style: const TextStyle(fontSize: 10, color: WanderlustColors.accent, fontWeight: FontWeight.bold, letterSpacing: 0.8)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
