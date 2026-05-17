import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import 'dart:ui';

// --- Callout Box (tip or warning) ---
class CalloutBox extends StatelessWidget {
  final Callout callout;
  const CalloutBox({super.key, required this.callout});

  @override
  Widget build(BuildContext context) {
    final isTip = callout.type == 'tip';
    return Container(
      margin: EdgeInsets.zero,
      decoration: BoxDecoration(
        color: isTip ? WanderlustColors.accent.withOpacity(0.08) : WanderlustColors.error.withOpacity(0.08),
        border: Border(
          left: BorderSide(
            color: isTip ? WanderlustColors.accent : WanderlustColors.error,
            width: 4,
          ),
        ),
        borderRadius: const BorderRadius.only(
          topRight: Radius.circular(12),
          bottomRight: Radius.circular(12),
        ),
      ),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                isTip ? Icons.lightbulb_outline_rounded : Icons.warning_amber_rounded,
                size: 14,
                color: isTip ? WanderlustColors.accent : WanderlustColors.error,
              ),
              const SizedBox(width: 6),
              Text(
                callout.label.toUpperCase(),
                style: TextStyle(
                  fontSize: 10,
                  fontWeight: isTip ? FontWeight.w400 : FontWeight.w600,
                  letterSpacing: 1.0,
                  color: isTip ? WanderlustColors.accent : WanderlustColors.error,
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          Text(
            callout.text,
            style: TextStyle(
              fontSize: 13,
              height: 1.5,
              color: WanderlustColors.textGrey,
            ),
          ),
        ],
      ),
    );
  }
}

// --- Phrase / Local Word Box ---
class PhraseBox extends StatelessWidget {
  final LocalWord word;
  const PhraseBox({super.key, required this.word});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: EdgeInsets.zero,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: WanderlustColors.borderLight),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.03),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
            decoration: BoxDecoration(
              color: WanderlustColors.categoryCafe.withOpacity(0.1),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text(
              '${word.word}  / ${word.pronunciation}',
              style: const TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: WanderlustColors.categoryCafe,
              ),
            ),
          ),
          const SizedBox(height: 10),
          Text(
            word.definition,
            style: const TextStyle(
              fontSize: 13,
              height: 1.6,
              color: WanderlustColors.textGrey,
            ),
          ),
        ],
      ),
    );
  }
}

// --- Badge ---
class GuideBadge extends StatelessWidget {
  final String label;
  final String type;
  const GuideBadge({super.key, required this.label, required this.type});

  Color get color {
    switch (type) {
      case 'vibe': return WanderlustColors.accentPink;
      case 'hot': return WanderlustColors.error;
      case 'local': return WanderlustColors.accentGreen;
      case 'value': return WanderlustColors.categoryCafe;
      default: return WanderlustColors.accent;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      decoration: BoxDecoration(
        color: color.withOpacity(0.12),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Text(
        label.toUpperCase(),
        style: TextStyle(
          fontSize: 10,
          fontWeight: FontWeight.bold,
          letterSpacing: 0.8,
          color: color,
        ),
      ),
    );
  }
}

// --- Section Header ---
class SectionHeader extends StatelessWidget {
  final String title, intro;
  const SectionHeader({super.key, required this.title, required this.intro});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          title, 
          style: const TextStyle(
            fontSize: 22, 
            fontWeight: FontWeight.bold,
            color: WanderlustColors.textWhite,
          )
        ),
        const SizedBox(height: 6),
        Text(
          intro, 
          style: const TextStyle(
            fontSize: 13, 
            color: WanderlustColors.textGrey, 
            height: 1.6
          )
        ),
        const SizedBox(height: 20),
      ],
    );
  }
}
