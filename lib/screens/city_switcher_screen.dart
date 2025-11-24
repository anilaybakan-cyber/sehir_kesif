import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class CitySwitcherScreen extends StatelessWidget {
  const CitySwitcherScreen({super.key});

  final List<Map<String, dynamic>> cities = const [
    {"name": "Barcelona", "tagline": "Gaudí, tapas ve Akdeniz sokakları"},
    {"name": "Nice", "tagline": "Fransız Rivierası'nın incisi"},
    {"name": "Paris", "tagline": "Aşkın ve ışıkların şehri"},
    {"name": "Roma", "tagline": "Tarihin kalbi, İtalya’nın ruhu"},
    {"name": "Amsterdam", "tagline": "Kanallar, bisikletler ve özgür ruh"},
    {"name": "London", "tagline": "Modern, dinamik, kültürel başkent"},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                "Şehir Seç",
                style: TextStyle(
                  fontSize: 28,
                  fontWeight: FontWeight.bold,
                  color: Colors.black87,
                ),
              ),
              const SizedBox(height: 10),
              const Text(
                "Keşfetmek istediğin şehri seçerek uygulamayı kişiselleştir.",
                style: TextStyle(fontSize: 14, color: Colors.black54),
              ),
              const SizedBox(height: 20),
              Expanded(
                child: GridView.builder(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 2,
                    crossAxisSpacing: 14,
                    mainAxisSpacing: 14,
                    childAspectRatio: 0.78,
                  ),
                  itemCount: cities.length,
                  itemBuilder: (context, index) {
                    final city = cities[index];
                    return _CityCard(
                      name: city["name"],
                      tagline: city["tagline"],
                      onSelected: () async {
                        final prefs = await SharedPreferences.getInstance();
                        await prefs.setString("selectedCity", city["name"]);
                        // 🔥 burada artık pop YOK
                        Navigator.pushReplacementNamed(context, "/main");
                      },
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

class _CityCard extends StatelessWidget {
  final String name;
  final String tagline;
  final VoidCallback onSelected;

  const _CityCard({
    required this.name,
    required this.tagline,
    required this.onSelected,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onSelected,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(18),
          color: Colors.grey.shade200,
        ),
        child: Stack(
          children: [
            Positioned.fill(
              child: Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    colors: [
                      Colors.grey.shade300,
                      Colors.grey.shade200,
                      Colors.grey.shade100,
                    ],
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                  ),
                ),
              ),
            ),
            Positioned(
              left: 14,
              bottom: 18,
              right: 14,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    name,
                    style: const TextStyle(
                      fontSize: 22,
                      fontWeight: FontWeight.bold,
                      color: Colors.black87,
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    tagline,
                    maxLines: 2,
                    overflow: TextOverflow.ellipsis,
                    style: const TextStyle(fontSize: 13, color: Colors.black87),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
