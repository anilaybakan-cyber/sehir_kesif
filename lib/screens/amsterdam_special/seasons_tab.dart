import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../widgets/amsterdam_special/shared_widgets.dart';

class SeasonsTab extends StatefulWidget {
  final SeasonsSection data;
  const SeasonsTab({super.key, required this.data});

  @override
  State<SeasonsTab> createState() => _SeasonsTabState();
}

class _SeasonsTabState extends State<SeasonsTab> {
  int _selected = 0;

  @override
  Widget build(BuildContext context) {
    final season = widget.data.items[_selected];
    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        SectionHeader(title: widget.data.title, intro: widget.data.intro),
        GridView.count(
          crossAxisCount: 2,
          crossAxisSpacing: 10,
          mainAxisSpacing: 10,
          childAspectRatio: 2.2,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          children: List.generate(widget.data.items.length, (i) {
            final s = widget.data.items[i];
            final sel = i == _selected;
            return GestureDetector(
              onTap: () => setState(() => _selected = i),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 250),
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: sel ? WanderlustColors.accent.withOpacity(0.12) : WanderlustColors.bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(
                    color: sel ? WanderlustColors.accent : WanderlustColors.borderLight,
                    width: sel ? 1.5 : 1,
                  ),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(s.label.toUpperCase(),
                        style: const TextStyle(fontSize: 9, color: WanderlustColors.textGreyLight, letterSpacing: 0.8, fontWeight: FontWeight.bold)),
                    Text(s.name,
                        style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold,
                            color: sel ? WanderlustColors.accent : WanderlustColors.textWhite)),
                    Text(s.months, style: const TextStyle(fontSize: 11, color: WanderlustColors.textGrey)),
                  ],
                ),
              ),
            );
          }),
        ),
        const SizedBox(height: 14),
        AnimatedSwitcher(
          duration: const Duration(milliseconds: 250),
          child: _SeasonDetail(key: ValueKey(_selected), season: season),
        ),
        const SizedBox(height: 16),
      ],
    );
  }
}

class _SeasonDetail extends StatelessWidget {
  final Season season;
  const _SeasonDetail({super.key, required this.season});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: WanderlustColors.accent.withOpacity(0.2)),
        boxShadow: [
          BoxShadow(
            color: WanderlustColors.accent.withOpacity(0.04),
            blurRadius: 15,
            offset: const Offset(0, 8),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(season.subtitle, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: WanderlustColors.textWhite)),
          const SizedBox(height: 10),
          Text(season.description, style: const TextStyle(fontSize: 13, color: WanderlustColors.textGrey, height: 1.6)),
          CalloutBox(callout: season.callout),
        ],
      ),
    );
  }
}
