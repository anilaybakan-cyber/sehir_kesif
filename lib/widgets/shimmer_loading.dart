// =============================================================================
// SHIMMER LOADING WIDGETS
// Skeleton loading efektleri
// =============================================================================

import 'package:flutter/material.dart';
import '../core/theme/app_theme.dart';

// =============================================================================
// BASE SHIMMER
// =============================================================================
class ShimmerWidget extends StatefulWidget {
  final double width;
  final double height;
  final double borderRadius;
  final ShapeBorder? shape;

  const ShimmerWidget({
    super.key,
    required this.width,
    required this.height,
    this.borderRadius = 8,
    this.shape,
  });

  const ShimmerWidget.rectangular({
    super.key,
    required this.width,
    required this.height,
    this.borderRadius = 8,
  }) : shape = null;

  const ShimmerWidget.circular({
    super.key,
    required double size,
  })  : width = size,
        height = size,
        borderRadius = 0,
        shape = const CircleBorder();

  @override
  State<ShimmerWidget> createState() => _ShimmerWidgetState();
}

class _ShimmerWidgetState extends State<ShimmerWidget>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(milliseconds: 1500),
      vsync: this,
    )..repeat();

    _animation = Tween<double>(begin: -2, end: 2).animate(
      CurvedAnimation(parent: _controller, curve: Curves.easeInOutSine),
    );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return AnimatedBuilder(
      animation: _animation,
      builder: (context, child) {
        return Container(
          width: widget.width,
          height: widget.height,
          decoration: ShapeDecoration(
            shape: widget.shape ??
                RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(widget.borderRadius),
                ),
            gradient: LinearGradient(
              begin: Alignment(_animation.value - 1, 0),
              end: Alignment(_animation.value + 1, 0),
              colors: [
                Colors.grey.shade300,
                Colors.grey.shade100,
                Colors.grey.shade300,
              ],
            ),
          ),
        );
      },
    );
  }
}

// =============================================================================
// EXPLORE SCREEN LOADING
// =============================================================================
class ShimmerExploreLoading extends StatelessWidget {
  const ShimmerExploreLoading({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppColors.background,
      child: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Hero section shimmer
              const ShimmerWidget.rectangular(
                width: double.infinity,
                height: 200,
                borderRadius: 24,
              ),
              const SizedBox(height: 24),

              // Mood section shimmer
              const ShimmerWidget.rectangular(
                width: double.infinity,
                height: 120,
                borderRadius: 20,
              ),
              const SizedBox(height: 28),

              // Section title
              const ShimmerWidget.rectangular(
                width: 180,
                height: 24,
                borderRadius: 8,
              ),
              const SizedBox(height: 16),

              // AI Cards shimmer
              SizedBox(
                height: 260,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: 3,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: const EdgeInsets.only(right: 16),
                      child: ShimmerWidget.rectangular(
                        width: 220,
                        height: 260,
                        borderRadius: 24,
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 28),

              // Categories shimmer
              const ShimmerWidget.rectangular(
                width: 140,
                height: 24,
                borderRadius: 8,
              ),
              const SizedBox(height: 16),

              SizedBox(
                height: 100,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: 5,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: const EdgeInsets.only(right: 12),
                      child: ShimmerWidget.rectangular(
                        width: 100,
                        height: 100,
                        borderRadius: 20,
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 28),

              // Places shimmer
              const ShimmerWidget.rectangular(
                width: 160,
                height: 24,
                borderRadius: 8,
              ),
              const SizedBox(height: 16),

              SizedBox(
                height: 240,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  itemCount: 3,
                  itemBuilder: (context, index) {
                    return Padding(
                      padding: const EdgeInsets.only(right: 16),
                      child: ShimmerWidget.rectangular(
                        width: 200,
                        height: 240,
                        borderRadius: 24,
                      ),
                    );
                  },
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// =============================================================================
// CARD LOADING
// =============================================================================
class ShimmerCard extends StatelessWidget {
  final double? width;
  final double height;

  const ShimmerCard({
    super.key,
    this.width,
    this.height = 200,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: width,
      height: height,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: AppShadows.soft,
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Image placeholder
          Expanded(
            flex: 3,
            child: ShimmerWidget.rectangular(
              width: double.infinity,
              height: double.infinity,
              borderRadius: 16,
            ),
          ),
          const SizedBox(height: 12),

          // Title
          const ShimmerWidget.rectangular(
            width: 140,
            height: 18,
            borderRadius: 6,
          ),
          const SizedBox(height: 8),

          // Subtitle
          const ShimmerWidget.rectangular(
            width: 100,
            height: 14,
            borderRadius: 6,
          ),
          const SizedBox(height: 12),

          // Tags row
          Row(
            children: [
              ShimmerWidget.rectangular(
                width: 60,
                height: 24,
                borderRadius: 12,
              ),
              const SizedBox(width: 8),
              ShimmerWidget.rectangular(
                width: 50,
                height: 24,
                borderRadius: 12,
              ),
            ],
          ),
        ],
      ),
    );
  }
}

// =============================================================================
// LIST TILE LOADING
// =============================================================================
class ShimmerListTile extends StatelessWidget {
  const ShimmerListTile({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      margin: const EdgeInsets.only(bottom: 12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: AppShadows.soft,
      ),
      child: Row(
        children: [
          // Avatar
          const ShimmerWidget.circular(size: 50),
          const SizedBox(width: 14),

          // Content
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                ShimmerWidget.rectangular(
                  width: 160,
                  height: 16,
                  borderRadius: 6,
                ),
                SizedBox(height: 8),
                ShimmerWidget.rectangular(
                  width: 100,
                  height: 12,
                  borderRadius: 6,
                ),
              ],
            ),
          ),

          // Trailing
          const ShimmerWidget.rectangular(
            width: 60,
            height: 28,
            borderRadius: 14,
          ),
        ],
      ),
    );
  }
}

// =============================================================================
// DETAIL SCREEN LOADING
// =============================================================================
class ShimmerDetailLoading extends StatelessWidget {
  const ShimmerDetailLoading({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: AppColors.background,
      child: Column(
        children: [
          // Hero image
          const ShimmerWidget.rectangular(
            width: double.infinity,
            height: 300,
            borderRadius: 0,
          ),

          Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Title
                const ShimmerWidget.rectangular(
                  width: 250,
                  height: 28,
                  borderRadius: 8,
                ),
                const SizedBox(height: 12),

                // Subtitle
                const ShimmerWidget.rectangular(
                  width: 150,
                  height: 18,
                  borderRadius: 6,
                ),
                const SizedBox(height: 24),

                // Info row
                Row(
                  children: [
                    ShimmerWidget.rectangular(
                      width: 80,
                      height: 32,
                      borderRadius: 16,
                    ),
                    const SizedBox(width: 12),
                    ShimmerWidget.rectangular(
                      width: 80,
                      height: 32,
                      borderRadius: 16,
                    ),
                    const SizedBox(width: 12),
                    ShimmerWidget.rectangular(
                      width: 80,
                      height: 32,
                      borderRadius: 16,
                    ),
                  ],
                ),
                const SizedBox(height: 24),

                // Description
                const ShimmerWidget.rectangular(
                  width: double.infinity,
                  height: 16,
                  borderRadius: 6,
                ),
                const SizedBox(height: 8),
                const ShimmerWidget.rectangular(
                  width: double.infinity,
                  height: 16,
                  borderRadius: 6,
                ),
                const SizedBox(height: 8),
                const ShimmerWidget.rectangular(
                  width: 200,
                  height: 16,
                  borderRadius: 6,
                ),
                const SizedBox(height: 24),

                // Tags
                Wrap(
                  spacing: 8,
                  runSpacing: 8,
                  children: List.generate(
                    4,
                    (index) => ShimmerWidget.rectangular(
                      width: 70 + (index * 10),
                      height: 32,
                      borderRadius: 16,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
