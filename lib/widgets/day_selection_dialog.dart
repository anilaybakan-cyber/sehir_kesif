import 'package:flutter/material.dart';

import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';

/// Keşfet / detay / yakınımda paylaşılan “hangi güne eklensin?” diyaloğu.
/// Başlık ve liste sol hizalı; gün satırlarında Listem ile aynı leading genişliği kullanılır.
Future<int?> showDaySelectionDialog(
  BuildContext context, {
  required int totalDays,
  required Map<String, dynamic> scheduleMap,
  required String confirmMessage,
}) {
  final l10n = AppLocalizations.instance;
  const accent = WanderlustColors.accent;
  const listPurple = Color(0xFF6C5CE7);

  return showDialog<int>(
    context: context,
    barrierColor: Colors.black.withOpacity(0.65),
    builder: (dialogContext) {
      final maxListHeight = MediaQuery.sizeOf(dialogContext).height * 0.48;

      Widget dayLeading(int day) {
        return SizedBox(
          width: 40,
          height: 40,
          child: Center(
            child: Container(
              width: 36,
              height: 36,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: const Color(0xFF1A1A2E).withOpacity(0.08),
                shape: BoxShape.circle,
              ),
              child: Text(
                '$day',
                style: const TextStyle(
                  color: Color(0xFF1A1A2E),
                  fontWeight: FontWeight.w800,
                  fontSize: 14,
                ),
              ),
            ),
          ),
        );
      }

      Widget leadingIcon({
        required IconData icon,
        required Color fg,
        required Color bg,
      }) {
        return SizedBox(
          width: 40,
          height: 40,
          child: Center(
            child: Container(
              width: 36,
              height: 36,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: bg,
                shape: BoxShape.circle,
              ),
              child: Icon(icon, color: fg, size: 20),
            ),
          ),
        );
      }

      return Dialog(
        backgroundColor: Colors.white,
        elevation: 0,
        surfaceTintColor: Colors.transparent,
        insetPadding: const EdgeInsets.symmetric(horizontal: 22, vertical: 20),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(16),
          side: BorderSide(color: Colors.black.withOpacity(0.06)),
        ),
        child: Padding(
          padding: const EdgeInsets.fromLTRB(18, 14, 18, 10),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text(
                l10n.whichDay,
                textAlign: TextAlign.left,
                style: const TextStyle(
                  color: Color(0xFF1A1A2E),
                  fontSize: 17,
                  fontWeight: FontWeight.w800,
                  height: 1.25,
                ),
              ),
              const SizedBox(height: 6),
              Text(
                confirmMessage,
                textAlign: TextAlign.left,
                style: TextStyle(
                  color: Colors.black.withOpacity(0.52),
                  fontSize: 13.5,
                  height: 1.35,
                ),
              ),
              const SizedBox(height: 14),
              ConstrainedBox(
                constraints: BoxConstraints(maxHeight: maxListHeight.clamp(120, 440)),
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      ListTile(
                        contentPadding: const EdgeInsets.symmetric(horizontal: 4, vertical: 2),
                        visualDensity: VisualDensity.compact,
                        dense: true,
                        minLeadingWidth: 40,
                        leading: leadingIcon(
                          icon: Icons.list_alt_rounded,
                          fg: listPurple,
                          bg: listPurple.withOpacity(0.12),
                        ),
                        title: Text(
                          l10n.myList,
                          style: const TextStyle(
                            color: listPurple,
                            fontWeight: FontWeight.w800,
                            fontSize: 15,
                          ),
                        ),
                        subtitle: Text(
                          l10n.addToList,
                          style: TextStyle(
                            color: Colors.black.withOpacity(0.42),
                            fontSize: 12,
                          ),
                        ),
                        trailing: Icon(
                          Icons.chevron_right_rounded,
                          color: listPurple.withOpacity(0.85),
                          size: 22,
                        ),
                        onTap: () => Navigator.pop(dialogContext, 0),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.only(left: 48, top: 4, bottom: 4),
                        child: Divider(
                          height: 1,
                          thickness: 1,
                          color: Colors.black.withOpacity(0.06),
                        ),
                      ),
                      ...List.generate(totalDays, (index) {
                        final day = index + 1;
                        final dayKey = day.toString();
                        final List<dynamic> dayPlaces =
                            scheduleMap[dayKey] ?? [];
                        final count = dayPlaces.length;
                        return ListTile(
                          contentPadding:
                              const EdgeInsets.symmetric(horizontal: 4, vertical: 2),
                          visualDensity: VisualDensity.compact,
                          dense: true,
                          minLeadingWidth: 40,
                          leading: dayLeading(day),
                          title: Text(
                            l10n.dayN(day),
                            style: const TextStyle(
                              color: Color(0xFF1A1A2E),
                              fontWeight: FontWeight.w700,
                              fontSize: 15,
                            ),
                          ),
                          subtitle: Text(
                            l10n.nPlaces(count),
                            style: TextStyle(
                              color: Colors.black.withOpacity(0.42),
                              fontSize: 12.5,
                            ),
                          ),
                          trailing: Icon(
                            Icons.chevron_right_rounded,
                            color: accent.withOpacity(0.75),
                            size: 22,
                          ),
                          onTap: () => Navigator.pop(dialogContext, day),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10),
                          ),
                        );
                      }),
                      Padding(
                        padding: const EdgeInsets.only(left: 48, top: 4, bottom: 4),
                        child: Divider(
                          height: 1,
                          thickness: 1,
                          color: Colors.black.withOpacity(0.06),
                        ),
                      ),
                      ListTile(
                        contentPadding:
                            const EdgeInsets.symmetric(horizontal: 4, vertical: 2),
                        visualDensity: VisualDensity.compact,
                        dense: true,
                        minLeadingWidth: 40,
                        leading: leadingIcon(
                          icon: Icons.add_rounded,
                          fg: accent,
                          bg: accent.withOpacity(0.12),
                        ),
                        title: Text(
                          l10n.createNewDay,
                          style: const TextStyle(
                            color: Color(0xFF1A1A2E),
                            fontWeight: FontWeight.w700,
                            fontSize: 15,
                          ),
                        ),
                        subtitle: Text(
                          l10n.dayN(totalDays + 1),
                          style: TextStyle(
                            color: Colors.black.withOpacity(0.42),
                            fontSize: 12.5,
                          ),
                        ),
                        trailing: Icon(
                          Icons.chevron_right_rounded,
                          color: accent.withOpacity(0.75),
                          size: 22,
                        ),
                        onTap: () =>
                            Navigator.pop(dialogContext, totalDays + 1),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    },
  );
}
