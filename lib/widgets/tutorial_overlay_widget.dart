import 'package:flutter/material.dart';
import '../l10n/app_localizations.dart';
import 'dashed_arrow_painter.dart';

class TutorialOverlayWidget extends StatelessWidget {
  final String title;
  final String description;
  final int currentStep;
  final int totalSteps;
  final VoidCallback onSkip;
  final VoidCallback? onNext; // Callback for next step
  final bool isArrowUp;
  final bool isArrowFlipped;
  final double? arrowHeight;

  const TutorialOverlayWidget({
    super.key,
    required this.title,
    required this.description,
    required this.currentStep,
    required this.totalSteps,
    required this.onSkip,
    this.onNext,
    this.isArrowUp = true,
    this.isArrowFlipped = false,
    this.arrowHeight,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        if (isArrowUp) ...[
           const SizedBox(height: 20),
           // Arrow points UP to target above
           SizedBox(
             height: arrowHeight ?? 80, 
             width: 60,
             child: CurvedArrowWidget(pointsUp: true, isFlipped: isArrowFlipped), 
           ),
           const SizedBox(height: 10),
        ],

        // Content Box (Title + Desc) - Clickable to advance
        GestureDetector(
          onTap: onNext ?? onSkip,
          behavior: HitTestBehavior.opaque,
          child: Container(
            constraints: const BoxConstraints(maxWidth: 300),
            padding: const EdgeInsets.symmetric(vertical: 20, horizontal: 20),
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.6), // Slightly darker for better contrast
              borderRadius: BorderRadius.circular(16),
              border: Border.all(
                color: Colors.white.withOpacity(0.1),
                width: 1,
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withOpacity(0.2),
                  blurRadius: 10,
                  spreadRadius: 2,
                ),
              ],
            ),
            child: Column(
               children: [
                 Text(
                  title,
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 24,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 12),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: Text(
                    description,
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      color: Colors.white70,
                      fontSize: 16,
                      height: 1.4,
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                // Tap to continue hint
                Text(
                  onNext != null 
                    ? (AppLocalizations.instance.isEnglish ? "Tap to continue" : "Devam etmek için dokun")
                    : (AppLocalizations.instance.isEnglish ? "Tap to finish" : "Bitirmek için dokun"),
                  style: TextStyle(
                    color: Colors.white.withOpacity(0.4),
                    fontSize: 12,
                    fontWeight: FontWeight.w500,
                  ),
                ),
              ],
            ),
          ),
        ),

        // Arrow points DOWN to target below
        if (!isArrowUp) ...[
           // Larger arrow, adjust padding based on flip
           Padding(
             padding: EdgeInsets.only(
               left: isArrowFlipped ? 0 : 40, 
               right: isArrowFlipped ? 40 : 0,
               top: 5
             ), 
             child: SizedBox(
               height: arrowHeight ?? 140, 
               width: 100, 
               child: CurvedArrowWidget(pointsUp: false, isFlipped: isArrowFlipped), 
             ),
           ),
        ]
      ],
    );
  }
}
