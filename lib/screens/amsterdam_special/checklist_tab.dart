import 'package:flutter/material.dart';
import '../../models/amsterdam_special/city_guide_model.dart';
import '../../theme/wanderlust_colors.dart';
import '../../l10n/app_localizations.dart';

class ChecklistTab extends StatefulWidget {
  final ChecklistSection data;
  const ChecklistTab({super.key, required this.data});

  @override
  State<ChecklistTab> createState() => _ChecklistTabState();
}

class _ChecklistTabState extends State<ChecklistTab> {
  final Set<int> _done = {};

  @override
  Widget build(BuildContext context) {
    final total = widget.data.items.length;
    final doneCount = _done.length;
    final progress = total == 0 ? 0.0 : doneCount / total;
    final isComplete = doneCount == total;

    return ListView(
      padding: const EdgeInsets.all(20),
      children: [
        Text(widget.data.title, 
          style: TextStyle(
            fontSize: 22, 
            fontWeight: FontWeight.bold,
            color: WanderlustColors.textWhite,
          )
        ),
        const SizedBox(height: 12),
        Row(
          children: [
            Expanded(
              child: ClipRRect(
                borderRadius: BorderRadius.circular(10),
                child: LinearProgressIndicator(
                  value: progress,
                  backgroundColor: WanderlustColors.bgCardLight,
                  valueColor: const AlwaysStoppedAnimation<Color>(WanderlustColors.accent),
                  minHeight: 8,
                ),
              ),
            ),
            const SizedBox(width: 12),
            Text(
              isComplete ? '🎉' : '${(progress * 100).toInt()}%',
              style: TextStyle(fontWeight: FontWeight.bold, color: WanderlustColors.accent),
            ),
          ],
        ),
        const SizedBox(height: 8),
        Text(
          isComplete ? widget.data.completionMessage : '$doneCount / $total ${AppLocalizations.instance.isEnglish ? 'completed' : 'tamamlandı'}',
          style: TextStyle(
            fontSize: 12,
            color: isComplete ? WanderlustColors.success : WanderlustColors.textGrey,
            fontWeight: isComplete ? FontWeight.bold : FontWeight.normal,
          ),
        ),
        const SizedBox(height: 24),
        ...List.generate(widget.data.items.length, (i) {
          final item = widget.data.items[i];
          final isDone = _done.contains(i);
          return GestureDetector(
            onTap: () => setState(() {
              isDone ? _done.remove(i) : _done.add(i);
            }),
            child: Container(
              padding: const EdgeInsets.all(16),
              margin: const EdgeInsets.only(bottom: 12),
              decoration: BoxDecoration(
                color: isDone ? WanderlustColors.accent.withOpacity(0.04) : WanderlustColors.bgCard,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(
                  color: isDone ? WanderlustColors.accent.withOpacity(0.2) : WanderlustColors.borderLight,
                ),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  AnimatedContainer(
                    duration: const Duration(milliseconds: 250),
                    width: 24,
                    height: 24,
                    decoration: BoxDecoration(
                      color: isDone ? WanderlustColors.accent : Colors.transparent,
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(
                        color: isDone ? WanderlustColors.accent : WanderlustColors.textGreyLight,
                        width: 2,
                      ),
                    ),
                    child: isDone
                        ? const Icon(Icons.check, size: 16, color: Colors.white)
                        : null,
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          item.label,
                          style: TextStyle(
                            fontSize: 15,
                            fontWeight: FontWeight.bold,
                            color: isDone ? WanderlustColors.textGreyLight : WanderlustColors.textWhite,
                            decoration: isDone ? TextDecoration.lineThrough : null,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          item.sub,
                          style: TextStyle(
                            fontSize: 12, 
                            color: isDone ? WanderlustColors.textGreyLight.withOpacity(0.5) : WanderlustColors.textGrey, 
                            height: 1.4
                          )
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          );
        }),
        const SizedBox(height: 16),
      ],
    );
  }
}
