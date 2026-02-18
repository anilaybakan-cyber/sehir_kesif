import 'package:flutter/material.dart';
import '../theme/wanderlust_colors.dart';

class MapBackgroundPainter extends CustomPainter {
  final Color color;
  final double strokeWidth;

  MapBackgroundPainter({
    this.color = const Color(0xFFFFFFFF),
    this.strokeWidth = 1.0,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()
      ..color = color.withOpacity(0.03) // Very subtle
      ..style = PaintingStyle.stroke
      ..strokeWidth = strokeWidth
      ..strokeCap = StrokeCap.round;

    final path = Path();

    // Generate some random-looking map lines
    // Main roads (horizontal-ish)
    path.moveTo(0, size.height * 0.3);
    path.cubicTo(
      size.width * 0.3, size.height * 0.25,
      size.width * 0.6, size.height * 0.35,
      size.width, size.height * 0.2,
    );

    path.moveTo(0, size.height * 0.6);
    path.cubicTo(
      size.width * 0.4, size.height * 0.65,
      size.width * 0.7, size.height * 0.55,
      size.width, size.height * 0.7,
    );

    path.moveTo(size.width * 0.2, size.height);
    path.cubicTo(
      size.width * 0.25, size.height * 0.7,
      size.width * 0.15, size.height * 0.4,
      size.width * 0.3, 0,
    );

     path.moveTo(size.width * 0.6, size.height);
    path.cubicTo(
      size.width * 0.55, size.height * 0.6,
      size.width * 0.7, size.height * 0.3,
      size.width * 0.65, 0,
    );
    
    // Grid-like streets
    for (double i = 0; i < size.width; i += 80) {
       path.moveTo(i, 0);
       path.lineTo(i + 20, size.height);
    }
    
    for (double i = 0; i < size.height; i += 80) {
       path.moveTo(0, i);
       path.lineTo(size.width, i - 20);
    }

    canvas.drawPath(path, paint);
    
    // Draw some points/intersections
    final pointPaint = Paint()
      ..color = color.withOpacity(0.02)
      ..style = PaintingStyle.fill;
      
    canvas.drawCircle(Offset(size.width * 0.3, size.height * 0.3), 4, pointPaint);
    canvas.drawCircle(Offset(size.width * 0.7, size.height * 0.6), 6, pointPaint);
    canvas.drawCircle(Offset(size.width * 0.5, size.height * 0.5), 3, pointPaint);
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => false;
}

// Wrapper widget for easier use
class MapBackground extends StatelessWidget {
  final Widget child;

  const MapBackground({Key? key, required this.child}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Stack(
      children: [
        // Base background color
        Container(color: WanderlustColors.bgDark),
        
        // Map pattern
        Positioned.fill(
          child: CustomPaint(
            painter: MapBackgroundPainter(),
          ),
        ),
        
        // Content on top
        child,
      ],
    );
  }
}
