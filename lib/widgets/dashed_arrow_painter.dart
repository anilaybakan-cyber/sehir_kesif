import 'package:flutter/material.dart';
import 'dart:math';
import 'dart:ui'; // Required for PathMetric

class DashedArrowPainter extends CustomPainter {
  final Color color;
  final double strokeWidth;

  DashedArrowPainter({
    this.color = Colors.white,
    this.strokeWidth = 3.0,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final Paint paint = Paint()
      ..color = color
      ..strokeWidth = strokeWidth
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;

    final Path path = Path();
    
    // Start point (bottom center of the text area)
    final double startX = size.width / 2;
    final double startY = size.height;
    
    // End point (top center, pointing to target)
    // We'll draw a curved path
    
    path.moveTo(size.width, size.height * 0.2); // Start from right
    
    // Cubic bezier curve for a nice arc
    path.cubicTo(
      size.width * 0.6, size.height * 0.2, // Control point 1
      size.width * 0.2, size.height * 0.5,  // Control point 2
      0, size.height // End point
    );

    // Draw dashed line
    final Path dashedPath = _createDashedPath(path, dashWidth: 8, dashSpace: 5);
    canvas.drawPath(dashedPath, paint);

    // Draw Arrow Head at the end (0, size.height)
    // Actually our curve goes from top to bottom-left roughly.
    // Let's adjust for the specific use case: Text is BELOW, Button is ABOVE.
    // So Arrow should point UP.
    
    _drawArrowHead(canvas, 0, size.height, paint);
  }
  
  void _drawArrowHead(Canvas canvas, double x, double y, Paint paint) {
     // Simple arrow head logic, possibly rotated
     // For this specific design, we can just draw lines manually or use path
  }

  Path _createDashedPath(Path source, {required double dashWidth, required double dashSpace}) {
    final Path dest = Path();
    for (final PathMetric metric in source.computeMetrics()) {
      double distance = 0.0;
      while (distance < metric.length) {
        final double len = (distance + dashWidth < metric.length) ? dashWidth : metric.length - distance;
        dest.addPath(metric.extractPath(distance, distance + len), Offset.zero);
        distance += dashWidth + dashSpace;
      }
    }
    return dest;
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

class CurvedArrowWidget extends StatelessWidget {
  final bool isFlipped;
  final bool pointsUp; // NEW
  
  const CurvedArrowWidget({super.key, this.isFlipped = false, this.pointsUp = false});

  @override
  Widget build(BuildContext context) {
    return CustomPaint(
      size: const Size(60, 80), // Approx size
      painter: _SimpleCurvedArrowPainter(isFlipped: isFlipped, pointsUp: pointsUp),
    );
  }
}

class _SimpleCurvedArrowPainter extends CustomPainter {
  final bool isFlipped;
  final bool pointsUp; // NEW: true = points to target above, false = points to target below
  
  _SimpleCurvedArrowPainter({this.isFlipped = false, this.pointsUp = false});

  @override
  void paint(Canvas canvas, Size size) {
    // Shadow Paint
    final shadowPaint = Paint()
      ..color = Colors.black54
      ..strokeWidth = 4.0
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 4);

    // Main Paint
    final paint = Paint()
      ..color = Colors.white
      ..strokeWidth = 3.5
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round;

    final path = Path();
    
    if (pointsUp) {
      // Arrow Points UP (Target is ABOVE the text/arrow)
      // Start: Bottom, End: Top
      if (!isFlipped) {
        // Start Bottom-Right, loop, end Top-Center
        path.moveTo(size.width * 0.9, size.height);
        path.cubicTo(
          size.width * -0.3, size.height * 0.9,  // C1: Pull far Left
          size.width * 1.4, size.height * 0.3,   // C2: Pull far Right (loop)
          size.width * 0.5, 0                     // End: Top Center
        );
      } else {
        // Start Bottom-Left, loop, end Top-Center
        path.moveTo(size.width * 0.1, size.height);
        path.cubicTo(
          size.width * 1.3, size.height * 0.9,
          size.width * -0.4, size.height * 0.3,
          size.width * 0.5, 0
        );
      }
    } else {
      // Arrow Points DOWN (Target is BELOW the text/arrow)
      // Start: Top, End: Bottom
      if (!isFlipped) {
        // Start Top-Left, loop, end Bottom-Right
        path.moveTo(size.width * 0.1, 0);
        path.cubicTo(
          size.width * 1.4, size.height * 0.1,   // C1: Far Right Top
          size.width * -0.3, size.height * 0.5,  // C2: Left Middle
          size.width, size.height                 // End: Bottom Right Tip
        );
      } else {
        // Start Top-Right, loop, end Bottom-Left
        path.moveTo(size.width * 0.9, 0);
        path.cubicTo(
          size.width * -0.4, size.height * 0.1,
          size.width * 1.3, size.height * 0.5,
          0, size.height
        );
      }
    }

    // Create dashes
    final dashPath = Path();
    double dashWidth = 8.0;
    double dashSpace = 6.0;
    double distance = 0.0;
    
    // Get Path Metrics to find the end position and tangent for the arrow head
    final metrics = path.computeMetrics().toList();
    if (metrics.isEmpty) return;
    
    final pathMetric = metrics.first;
    
    // Draw Dashes
    while (distance < pathMetric.length) {
      dashPath.addPath(
        pathMetric.extractPath(distance, distance + dashWidth),
        Offset.zero,
      );
      distance += dashWidth + dashSpace;
    }

    // Draw Shadow
    canvas.drawPath(dashPath.shift(const Offset(0, 2)), shadowPaint);
    // Draw Main Path
    canvas.drawPath(dashPath, paint);

    // --- Draw Arrow Tip ---
    // Get tangent at the very end of the path
    final Tangent? tangent = pathMetric.getTangentForOffset(pathMetric.length);
    if (tangent == null) return;

    final Offset endPoint = tangent.position;
    
    canvas.save();
    canvas.translate(endPoint.dx, endPoint.dy);
    
    // Rotate to match the path's direction at the end point
    // atan2(dy, dx) gives the angle of the tangent vector
    final double rotationAngle = atan2(tangent.vector.dy, tangent.vector.dx);
    canvas.rotate(rotationAngle);
    
    // Draw V-Shape Tip
    // Tip is at (0,0). Wings open backwards (negative X direction).
    // With rotation 0 pointing Right, this V opens to the left, tip pointing right.
    final tipPath = Path();
    tipPath.moveTo(-12, -8); // Left wing (upper)
    tipPath.lineTo(0, 0);     // Tip
    tipPath.lineTo(-12, 8);   // Right wing (lower)
    
    // Shadow for Tip
    final tipShadowPaint = Paint()
      ..color = Colors.black54
      ..strokeWidth = 3.5
      ..style = PaintingStyle.stroke
      ..strokeCap = StrokeCap.round
      ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 4);

    canvas.drawPath(tipPath.shift(const Offset(0, 2)), tipShadowPaint);
    canvas.drawPath(tipPath, paint);
    
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true; // Repaint for safety
}
