// =============================================================================
// CITY SWITCHER SCREEN - MODAL BOTTOM SHEET VERSION
// Dark theme, açılır pencere şeklinde
// 6 şehir: Barcelona, Paris, Roma, İstanbul, Amsterdam, Tokyo
// =============================================================================

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';

class CitySwitcherScreen extends StatefulWidget {
  const CitySwitcherScreen({super.key});

  @override
  State<CitySwitcherScreen> createState() => _CitySwitcherScreenState();

  /// Modal olarak açmak için static method
  static Future<String?> showAsModal(BuildContext context) async {
    return await showModalBottomSheet<String>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const _CitySwitcherModal(),
    );
  }
}

// =============================================================================
// MODAL VERSION (Bottom Sheet)
// =============================================================================

class _CitySwitcherModal extends StatefulWidget {
  const _CitySwitcherModal();

  @override
  State<_CitySwitcherModal> createState() => _CitySwitcherModalState();
}

class _CitySwitcherModalState extends State<_CitySwitcherModal> {
  String _selectedCity = "barcelona";

  // Design tokens - AMBER THEME
  static const _bgDark = Color(0xFF0D0D1A);
  static const _bgCard = Color(0xFF1A1A2E);
  static const _accent = Color(0xFFF5A623); // Amber
  static const _accentLight = Color(0xFFFFB800); // Gold

  final List<Map<String, dynamic>> _cities = [
    // Türkiye
    {
      "id": "istanbul",
      "name": "İstanbul",
      "country": "Türkiye",
      "flag": "🇹🇷",
      "image": "assets/cities/istanbul.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=400",
    },
    // İspanya
    {
      "id": "barcelona",
      "name": "Barcelona",
      "country": "İspanya",
      "flag": "🇪🇸",
      "image": "assets/cities/barcelona.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=400",
    },
    {
      "id": "madrid",
      "name": "Madrid",
      "country": "İspanya",
      "flag": "🇪🇸",
      "image": "assets/cities/madrid.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=400",
    },
    {
      "id": "sevilla",
      "name": "Sevilla",
      "country": "İspanya",
      "flag": "🇪🇸",
      "image": "assets/cities/sevilla.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1515443961218-a51367888e4b?w=400",
    },
    // Fransa
    {
      "id": "paris",
      "name": "Paris",
      "country": "Fransa",
      "flag": "🇫🇷",
      "image": "assets/cities/paris.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=400",
    },
    // İtalya
    {
      "id": "roma",
      "name": "Roma",
      "country": "İtalya",
      "flag": "🇮🇹",
      "image": "assets/cities/roma.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=400",
    },
    {
      "id": "milano",
      "name": "Milano",
      "country": "İtalya",
      "flag": "🇮🇹",
      "image": "assets/cities/milano.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1520440229-6469a149ac59?w=400",
    },
    // Hollanda
    {
      "id": "amsterdam",
      "name": "Amsterdam",
      "country": "Hollanda",
      "flag": "🇳🇱",
      "image": "assets/cities/amsterdam.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=400",
    },
    // İngiltere
    {
      "id": "londra",
      "name": "Londra",
      "country": "İngiltere",
      "flag": "🇬🇧",
      "image": "assets/cities/londra.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=400",
    },
    // Almanya
    {
      "id": "berlin",
      "name": "Berlin",
      "country": "Almanya",
      "flag": "🇩🇪",
      "image": "assets/cities/berlin.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=400",
    },
    // Avusturya
    {
      "id": "viyana",
      "name": "Viyana",
      "country": "Avusturya",
      "flag": "🇦🇹",
      "image": "assets/cities/viyana.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=400",
    },
    // Çekya
    {
      "id": "prag",
      "name": "Prag",
      "country": "Çekya",
      "flag": "🇨🇿",
      "image": "assets/cities/prag.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400",
    },
    // Portekiz
    {
      "id": "lizbon",
      "name": "Lizbon",
      "country": "Portekiz",
      "flag": "🇵🇹",
      "image": "assets/cities/lizbon.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=400",
    },
    // Japonya
    {
      "id": "tokyo",
      "name": "Tokyo",
      "country": "Japonya",
      "flag": "🇯🇵",
      "image": "assets/cities/tokyo.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=400",
    },
    // Güney Kore
    {
      "id": "seul",
      "name": "Seul",
      "country": "Güney Kore",
      "flag": "🇰🇷",
      "image": "assets/cities/seul.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1538485399081-7191377e8241?w=400",
    },
    // Singapur
    {
      "id": "singapur",
      "name": "Singapur",
      "country": "Singapur",
      "flag": "🇸🇬",
      "image": "assets/cities/singapur.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=400",
    },
    // BAE
    {
      "id": "dubai",
      "name": "Dubai",
      "country": "BAE",
      "flag": "🇦🇪",
      "image": "assets/cities/dubai.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=400",
    },
    // ABD
    {
      "id": "newyork",
      "name": "New York",
      "country": "ABD",
      "flag": "🇺🇸",
      "image": "assets/cities/newyork.jpg",
      "networkImage":
          "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=400",
    },
  ];

  @override
  void initState() {
    super.initState();
    _loadSelectedCity();
  }

  Future<void> _loadSelectedCity() async {
    final prefs = await SharedPreferences.getInstance();
    setState(() {
      _selectedCity = prefs.getString("selectedCity") ?? "barcelona";
    });
  }

  Future<void> _selectCity(String cityId) async {
    HapticFeedback.mediumImpact();

    final prefs = await SharedPreferences.getInstance();
    await prefs.setString("selectedCity", cityId);

    setState(() => _selectedCity = cityId);

    // Kısa bir gecikme ile kapat
    Future.delayed(const Duration(milliseconds: 200), () {
      if (mounted) Navigator.pop(context, cityId);
    });
  }

  @override
  Widget build(BuildContext context) {
    final bottomPadding = MediaQuery.of(context).padding.bottom;

    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.65,
      ),
      decoration: const BoxDecoration(
        color: _bgDark,
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Handle bar
          Container(
            margin: const EdgeInsets.only(top: 12),
            width: 40,
            height: 4,
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(2),
            ),
          ),

          // Header
          Padding(
            padding: const EdgeInsets.fromLTRB(24, 20, 16, 12),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  "Şehir Seç",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 22,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                GestureDetector(
                  onTap: () => Navigator.pop(context),
                  child: Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Icon(
                      Icons.close_rounded,
                      color: Colors.white70,
                      size: 20,
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Şehirler listesi
          Flexible(
            child: ListView.builder(
              shrinkWrap: true,
              padding: EdgeInsets.fromLTRB(16, 4, 16, bottomPadding + 16),
              itemCount: _cities.length,
              itemBuilder: (context, index) {
                final city = _cities[index];
                final isSelected = city["id"] == _selectedCity;
                return _buildCityTile(city, isSelected);
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCityTile(Map<String, dynamic> city, bool isSelected) {
    return GestureDetector(
      onTap: () => _selectCity(city["id"]),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isSelected ? _accent.withOpacity(0.15) : _bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected ? _accent : Colors.white.withOpacity(0.06),
            width: isSelected ? 2 : 1,
          ),
        ),
        child: Row(
          children: [
            // Şehir fotoğrafı
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: SizedBox(
                width: 56,
                height: 56,
                child: Image.network(
                  city["networkImage"],
                  fit: BoxFit.cover,
                  errorBuilder: (context, error, stackTrace) {
                    return Container(
                      decoration: BoxDecoration(
                        gradient: LinearGradient(
                          colors: [
                            _accentLight.withOpacity(0.5),
                            _accent.withOpacity(0.5),
                          ],
                        ),
                      ),
                      child: Center(
                        child: Text(
                          city["flag"],
                          style: const TextStyle(fontSize: 24),
                        ),
                      ),
                    );
                  },
                ),
              ),
            ),

            const SizedBox(width: 14),

            // Şehir bilgileri
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    city["name"],
                    style: TextStyle(
                      color: isSelected ? _accent : Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    city["country"],
                    style: TextStyle(
                      color: Colors.white.withOpacity(0.5),
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),

            // Seçili indicator
            if (isSelected)
              Container(
                width: 24,
                height: 24,
                decoration: const BoxDecoration(
                  color: _accent,
                  shape: BoxShape.circle,
                ),
                child: const Icon(
                  Icons.check_rounded,
                  color: Colors.white,
                  size: 16,
                ),
              )
            else
              Container(
                width: 24,
                height: 24,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(
                    color: Colors.white.withOpacity(0.2),
                    width: 2,
                  ),
                ),
              ),
          ],
        ),
      ),
    );
  }
}

// =============================================================================
// FULL PAGE VERSION (Eski kullanım için - Opsiyonel)
// =============================================================================

class _CitySwitcherScreenState extends State<CitySwitcherScreen> {
  @override
  Widget build(BuildContext context) {
    // Direkt modal'ı aç ve sonucu döndür
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      final result = await CitySwitcherScreen.showAsModal(context);
      if (mounted) {
        Navigator.pop(context, result);
      }
    });

    // Geçici loading ekranı
    return const Scaffold(
      backgroundColor: Color(0xFF0D0D1A),
      body: Center(
        child: CircularProgressIndicator(
          color: Color(0xFFE91E8C),
          strokeWidth: 2,
        ),
      ),
    );
  }
}
