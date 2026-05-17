import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../widgets/amsterdam_special/shared_widgets.dart';

class NeighborhoodsTab extends StatelessWidget {
  final NeighborhoodsSection data;
  const NeighborhoodsTab({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        SectionHeader(title: data.title, intro: data.intro),
        PhraseBox(word: data.localWord),
        ...data.items.map((n) => _NeighborhoodCard(item: n)),
        CalloutBox(callout: data.callout),
        const SizedBox(height: 16),
      ],
    );
  }
}

class _NeighborhoodCard extends StatelessWidget {
  final Neighborhood item;
  const _NeighborhoodCard({required this.item});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 16),
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
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          GuideBadge(label: item.badge, type: item.badgeType),
          const SizedBox(height: 6),
          Text(
            item.name, 
            style: const TextStyle(
              fontSize: 18, 
              fontWeight: FontWeight.bold,
              color: WanderlustColors.textWhite,
            )
          ),
          const SizedBox(height: 6),
          Text(
            item.description, 
            style: const TextStyle(
              fontSize: 13, 
              color: WanderlustColors.textGrey, 
              height: 1.55
            )
          ),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            children: item.tags.map((t) => Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
              decoration: BoxDecoration(
                color: WanderlustColors.bgCardLight.withOpacity(0.4),
                borderRadius: BorderRadius.circular(6),
              ),
              child: Text(
                t,
                style: const TextStyle(fontSize: 11, color: WanderlustColors.textGrey),
              ),
            )).toList(),
          ),
        ],
      ),
    );
  }
}
