import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../widgets/amsterdam_special/shared_widgets.dart';
import '../../l10n/app_localizations.dart';

class OverviewTab extends StatelessWidget {
  final Overview data;
  const OverviewTab({super.key, required this.data});

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 20),
      children: [
        Text(data.title, 
          style: const TextStyle(
            fontSize: 24, 
            fontWeight: FontWeight.bold,
            color: WanderlustColors.textWhite,
          )
        ),
        const SizedBox(height: 8),
        Text(data.intro, 
          style: const TextStyle(
            fontSize: 14, 
            color: WanderlustColors.textGrey, 
            height: 1.7
          )
        ),
        const SizedBox(height: 16),
        PhraseBox(word: data.localWord),
        const SizedBox(height: 16),
        Text(
          AppLocalizations.instance.isEnglish ? 'Know Before You Go' : 'Gitmeden Önce Bilmeniz Gerekenler',
          style: const TextStyle(
            fontSize: 18, 
            fontWeight: FontWeight.bold,
            color: WanderlustColors.textWhite,
          ),
        ),
        const SizedBox(height: 6),
        ...data.rules.map((r) => _RuleCard(rule: r)),
        const SizedBox(height: 12),
        Text(
          AppLocalizations.instance.isEnglish ? 'City at a Glance' : 'Bir Bakışta Şehir', 
          style: const TextStyle(
            fontSize: 18, 
            fontWeight: FontWeight.bold,
            color: WanderlustColors.textWhite,
          )
        ),
        const SizedBox(height: 4),
        GridView.count(
          crossAxisCount: 2,
          crossAxisSpacing: 4,
          mainAxisSpacing: 4,
          // width/height — yüksek değer = daha alçak kart, iç boşluk azalır
          childAspectRatio: 2.55,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          children: data.quickFacts.map((f) => _QuickFactCard(fact: f)).toList(),
        ),
        CalloutBox(callout: data.tip),
        const SizedBox(height: 16),
      ],
    );
  }
}

class _RuleCard extends StatelessWidget {
  final GuideRule rule;
  const _RuleCard({required this.rule});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 32,
            height: 32,
            decoration: BoxDecoration(
              color: WanderlustColors.accent.withOpacity(0.12),
              shape: BoxShape.circle,
            ),
            child: Center(
              child: Text(
                '${rule.number}',
                style: const TextStyle(
                  fontSize: 13, 
                  fontWeight: FontWeight.bold, 
                  color: WanderlustColors.accent
                ),
              ),
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  rule.title, 
                  style: const TextStyle(
                    fontSize: 15, 
                    fontWeight: FontWeight.bold,
                    color: WanderlustColors.textWhite,
                  )
                ),
                const SizedBox(height: 4),
                Text(
                  rule.description, 
                  style: const TextStyle(
                    fontSize: 13, 
                    color: WanderlustColors.textGrey, 
                    height: 1.5
                  )
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _QuickFactCard extends StatelessWidget {
  final QuickFact fact;
  const _QuickFactCard({required this.fact});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCardLight.withOpacity(0.5),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: WanderlustColors.borderLight),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        mainAxisAlignment: MainAxisAlignment.center,
        mainAxisSize: MainAxisSize.min,
        children: [
          Row(
            children: [
              Text(fact.icon, style: const TextStyle(fontSize: 14)),
              const SizedBox(width: 4),
              Expanded(
                child: Text(
                  fact.label.toUpperCase(),
                  style: const TextStyle(
                    fontSize: 8,
                    color: WanderlustColors.textGreyLight,
                    letterSpacing: 0.4,
                    fontWeight: FontWeight.w600,
                    height: 1.1,
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 1),
          FittedBox(
            fit: BoxFit.scaleDown,
            alignment: Alignment.centerLeft,
            child: Text(
              fact.value,
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
              style: const TextStyle(
                fontSize: 12,
                fontWeight: FontWeight.w600,
                color: WanderlustColors.textWhite,
                height: 1.15,
              ),
            ),
          ),
          Text(
            fact.sub,
            maxLines: 1,
            style: const TextStyle(
              fontSize: 9,
              height: 1.15,
              color: WanderlustColors.textGrey,
              overflow: TextOverflow.ellipsis,
            ),
          ),
        ],
      ),
    );
  }
}
