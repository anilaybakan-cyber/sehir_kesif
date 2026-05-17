import 'package:flutter/material.dart';
import '../models/city_model.dart';
import '../services/travel_time_estimator.dart';
import '../theme/wanderlust_colors.dart';
import '../l10n/app_localizations.dart';

/// Rota kalitesi uyarı banner'ı.
/// Bir günün planını analiz eder ve sorunları varsa kullanıcıya gösterir.
///
/// Tetikleyiciler:
///   - Toplam mesafe > 80 km (yürüyüş için)
///   - Day-trip + non-day-trip karışımı (akşam yemeği hariç)
///   - 10+ yer (yorgunluk)
///   - Aynı kategoriden 4+ ardışık yer
class RouteQualityBanner extends StatelessWidget {
  final List<Highlight> places;
  final VoidCallback? onDismiss;
  final VoidCallback? onOptimize;

  const RouteQualityBanner({
    super.key,
    required this.places,
    this.onDismiss,
    this.onOptimize,
  });

  /// Plan kalitesi sorunları
  static List<RouteIssue> analyze(List<Highlight> places) {
    final issues = <RouteIssue>[];
    if (places.length < 2) return issues;

    // 1. Toplam mesafe kontrolü
    double totalDistanceKm = 0;
    for (int i = 0; i < places.length - 1; i++) {
      totalDistanceKm += TravelTimeEstimator.haversine(
        places[i].lat, places[i].lng,
        places[i + 1].lat, places[i + 1].lng,
      );
    }

    if (totalDistanceKm > 80) {
      issues.add(RouteIssue(
        type: RouteIssueType.tooFar,
        severity: IssueSeverity.high,
        valueKm: totalDistanceKm,
      ));
    } else if (totalDistanceKm > 30) {
      issues.add(RouteIssue(
        type: RouteIssueType.tooFar,
        severity: IssueSeverity.medium,
        valueKm: totalDistanceKm,
      ));
    }

    // 2. Day-trip + non-day-trip karışımı
    final dayTripCount = places.where((p) => p.isDayTrip).length;
    final regularCount = places.length - dayTripCount;
    if (dayTripCount > 0 && regularCount > 1) {
      // Day-trip günü 1 day-trip + max 1 evening food olmalı; daha fazlası bozuk plan
      issues.add(RouteIssue(
        type: RouteIssueType.dayTripMix,
        severity: IssueSeverity.high,
      ));
    }

    // 3. Çok fazla yer
    if (places.length >= 10) {
      issues.add(RouteIssue(
        type: RouteIssueType.tooMany,
        severity: IssueSeverity.medium,
        count: places.length,
      ));
    }

    // 4. Çok sayıda day-trip
    if (dayTripCount > 1) {
      issues.add(RouteIssue(
        type: RouteIssueType.multipleDayTrips,
        severity: IssueSeverity.high,
        count: dayTripCount,
      ));
    }

    return issues;
  }

  @override
  Widget build(BuildContext context) {
    final issues = analyze(places);
    if (issues.isEmpty) return const SizedBox.shrink();

    final isEn = AppLocalizations.instance.isEnglish;

    // En kritik sorun
    final highestSeverity = issues
        .map((e) => e.severity.index)
        .reduce((a, b) => a > b ? a : b);
    final isHigh = highestSeverity >= IssueSeverity.high.index;

    final accentColor = isHigh
        ? const Color(0xFFFF5252) // red
        : const Color(0xFFFF9800); // orange

    return Container(
      margin: const EdgeInsets.fromLTRB(16, 8, 16, 8),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: accentColor.withOpacity(0.1),
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: accentColor.withOpacity(0.4)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(
                isHigh ? Icons.warning_amber_rounded : Icons.info_outline_rounded,
                color: accentColor,
                size: 18,
              ),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  isEn
                      ? (isHigh ? "Route looks broken" : "Route may need attention")
                      : (isHigh ? "Rota bozuk görünüyor" : "Rota dikkat gerektirebilir"),
                  style: TextStyle(
                    color: accentColor,
                    fontWeight: FontWeight.w700,
                    fontSize: 13,
                  ),
                ),
              ),
              if (onDismiss != null)
                GestureDetector(
                  onTap: onDismiss,
                  child: Icon(Icons.close,
                      color: WanderlustColors.textGrey, size: 16),
                ),
            ],
          ),
          const SizedBox(height: 6),
          ...issues.map((issue) => Padding(
                padding: const EdgeInsets.only(left: 26, top: 2),
                child: Text(
                  "• ${issue.message(isEn)}",
                  style: TextStyle(
                    color: WanderlustColors.textWhite.withOpacity(0.85),
                    fontSize: 12,
                    height: 1.3,
                  ),
                ),
              )),
          if (onOptimize != null) ...[
            const SizedBox(height: 8),
            Padding(
              padding: const EdgeInsets.only(left: 26),
              child: GestureDetector(
                onTap: onOptimize,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: accentColor.withOpacity(0.18),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.auto_fix_high_rounded,
                          size: 14, color: accentColor),
                      const SizedBox(width: 6),
                      Text(
                        isEn ? "Optimize Route" : "Rotayı Optimize Et",
                        style: TextStyle(
                          color: accentColor,
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ],
      ),
    );
  }
}

class RouteIssue {
  final RouteIssueType type;
  final IssueSeverity severity;
  final double? valueKm;
  final int? count;

  RouteIssue({
    required this.type,
    required this.severity,
    this.valueKm,
    this.count,
  });

  String message(bool isEn) {
    switch (type) {
      case RouteIssueType.tooFar:
        final km = valueKm?.toStringAsFixed(0) ?? '?';
        return isEn
            ? "Total travel ~$km km in one day"
            : "Bir günde ~$km km yol";
      case RouteIssueType.dayTripMix:
        return isEn
            ? "Day trip mixed with city stops — schedule may not fit"
            : "Günübirlik gezi şehir içi mekanlarla karışık — program sığmayabilir";
      case RouteIssueType.tooMany:
        return isEn
            ? "${count ?? 0} places in one day — may be tiring"
            : "Bir günde ${count ?? 0} yer — yorucu olabilir";
      case RouteIssueType.multipleDayTrips:
        return isEn
            ? "${count ?? 0} day trips on the same day"
            : "Aynı günde ${count ?? 0} günübirlik gezi";
    }
  }
}

enum RouteIssueType {
  tooFar,
  dayTripMix,
  tooMany,
  multipleDayTrips,
}

enum IssueSeverity { low, medium, high }
