import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class OnboardingScreen extends StatefulWidget {
  const OnboardingScreen({super.key});

  @override
  State<OnboardingScreen> createState() => _OnboardingScreenState();
}

class _OnboardingScreenState extends State<OnboardingScreen> {
  final PageController _controller = PageController();
  int currentPage = 0;

  String travelStyle = "";
  int walkingLevel = 1;
  String budgetLevel = "";
  List<String> interests = [];

  Future<void> completeOnboarding() async {
    final prefs = await SharedPreferences.getInstance();

    await prefs.setBool("onboarding_completed", true);
    await prefs.setString("travelStyle", travelStyle);
    await prefs.setInt("walkingLevel", walkingLevel);
    await prefs.setString("budgetLevel", budgetLevel);
    await prefs.setStringList("interests", interests);

    Navigator.pushReplacementNamed(context, "/city-switch");
  }

  void next() {
    if (currentPage < 4) {
      _controller.animateToPage(
        currentPage + 1,
        duration: const Duration(milliseconds: 350),
        curve: Curves.easeOut,
      );
    } else {
      completeOnboarding();
    }
  }

  void back() {
    if (currentPage > 0) {
      _controller.animateToPage(
        currentPage - 1,
        duration: const Duration(milliseconds: 350),
        curve: Curves.easeOut,
      );
    }
  }

  Widget _dots() {
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: List.generate(5, (i) {
        bool active = i == currentPage;
        return AnimatedContainer(
          duration: const Duration(milliseconds: 250),
          margin: const EdgeInsets.symmetric(horizontal: 4),
          height: 8,
          width: active ? 22 : 8,
          decoration: BoxDecoration(
            color: active ? Colors.teal : Colors.grey.shade300,
            borderRadius: BorderRadius.circular(10),
          ),
        );
      }),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF5F5F7),
      body: SafeArea(
        child: Column(
          children: [
            Expanded(
              child: PageView(
                controller: _controller,
                onPageChanged: (i) => setState(() => currentPage = i),
                children: [
                  _welcomeStep(),
                  _travelStyleStep(),
                  _walkingStep(),
                  _budgetStep(),
                  _interestsStep(),
                ],
              ),
            ),

            const SizedBox(height: 12),
            _dots(),

            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 22, vertical: 16),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  currentPage > 0
                      ? TextButton(
                          onPressed: back,
                          child: const Text(
                            "Geri",
                            style: TextStyle(fontSize: 16),
                          ),
                        )
                      : const SizedBox(width: 60),

                  ElevatedButton(
                    onPressed: next,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.teal,
                      foregroundColor: Colors.white,
                      padding: const EdgeInsets.symmetric(
                        horizontal: 28,
                        vertical: 12,
                      ),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(14),
                      ),
                    ),
                    child: Text(
                      currentPage == 4 ? "Başla!" : "İleri",
                      style: const TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ---------------------
  // 1 — Welcome
  // ---------------------
  Widget _welcomeStep() {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          const SizedBox(height: 20),
          const Text(
            "Seyahat Tarzını Keşfedelim",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 28, fontWeight: FontWeight.w700),
          ),
          const SizedBox(height: 12),
          const Text(
            "Şehri sana göre kişiselleştirmek için birkaç kısa soru soracağız.",
            textAlign: TextAlign.center,
            style: TextStyle(fontSize: 16, color: Colors.black54),
          ),
        ],
      ),
    );
  }

  // ---------------------
  // 2 — Travel Style
  // ---------------------
  Widget _travelStyleStep() {
    final items = {
      "Turistik": Icons.account_balance,
      "Lokal": Icons.store_mall_directory,
      "Chill": Icons.spa,
      "Instagramlık": Icons.camera_alt,
    };

    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "Gezme Tarzın?",
            style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          const Text(
            "En çok seni anlatanı seç",
            style: TextStyle(fontSize: 15, color: Colors.black54),
          ),
          const SizedBox(height: 22),

          Expanded(
            child: GridView.count(
              crossAxisCount: 2,
              mainAxisSpacing: 18,
              crossAxisSpacing: 18,
              childAspectRatio: 1,
              children: items.entries.map((e) {
                bool selected = travelStyle == e.key;

                return GestureDetector(
                  onTap: () => setState(() => travelStyle = e.key),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: selected ? Colors.teal : Colors.white,
                      borderRadius: BorderRadius.circular(18),
                      border: Border.all(
                        color: selected ? Colors.teal : Colors.grey.shade300,
                        width: selected ? 2 : 1,
                      ),
                    ),
                    child: Column(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Icon(
                          e.value,
                          size: 42,
                          color: selected ? Colors.white : Colors.teal,
                        ),
                        const SizedBox(height: 10),
                        Text(
                          e.key,
                          style: TextStyle(
                            fontSize: 16,
                            color: selected ? Colors.white : Colors.black87,
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
        ],
      ),
    );
  }

  // ---------------------
  // 3 — Walking Level
  // ---------------------
  Widget _walkingStep() {
    final labels = [
      "Minimum (1–3 km)",
      "Orta (3–6 km)",
      "Aktif (6–10 km)",
      "Keşifçi (10+ km)",
    ];

    return Padding(
      padding: const EdgeInsets.all(26),
      child: Column(
        children: [
          const SizedBox(height: 18),
          const Text(
            "Yürüyüş Tempon?",
            style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          const Text(
            "Ne kadar yürümek sana uygun?",
            style: TextStyle(color: Colors.black54),
          ),
          const SizedBox(height: 30),

          Slider(
            value: walkingLevel.toDouble(),
            min: 0,
            max: 3,
            divisions: 3,
            activeColor: Colors.teal,
            onChanged: (v) => setState(() => walkingLevel = v.toInt()),
          ),

          Text(labels[walkingLevel], style: const TextStyle(fontSize: 18)),
          const Spacer(),
        ],
      ),
    );
  }

  // ---------------------
  // 4 — Budget
  // ---------------------
  Widget _budgetStep() {
    final budgets = {
      "Ekonomik": Icons.savings,
      "Dengeli": Icons.balance,
      "Premium": Icons.diamond,
    };

    return Padding(
      padding: const EdgeInsets.all(26),
      child: Column(
        children: [
          const SizedBox(height: 18),
          const Text(
            "Bütçe Tercihin?",
            style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          const Text(
            "Öneriler buna göre şekillenecek",
            style: TextStyle(color: Colors.black54),
          ),
          const SizedBox(height: 30),

          ...budgets.entries.map((e) {
            bool selected = budgetLevel == e.key;

            return GestureDetector(
              onTap: () => setState(() => budgetLevel = e.key),
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 200),
                padding: const EdgeInsets.all(18),
                margin: const EdgeInsets.only(bottom: 18),
                decoration: BoxDecoration(
                  color: selected ? Colors.teal : Colors.white,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.grey.shade300),
                ),
                child: Row(
                  children: [
                    Icon(
                      e.value,
                      size: 28,
                      color: selected ? Colors.white : Colors.teal,
                    ),
                    const SizedBox(width: 12),
                    Text(
                      e.key,
                      style: TextStyle(
                        fontSize: 18,
                        color: selected ? Colors.white : Colors.black87,
                      ),
                    ),
                  ],
                ),
              ),
            );
          }),
        ],
      ),
    );
  }

  // ---------------------
  // 5 — Interests
  // ---------------------
  Widget _interestsStep() {
    final options = [
      "Kafe",
      "Kokteyl",
      "Plaj",
      "Müze",
      "Tarihi",
      "Hidden gems",
      "Manzara",
      "Alışveriş",
      "Fine-dining",
    ];

    return Padding(
      padding: const EdgeInsets.all(26),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text(
            "İlgi Alanların?",
            style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          const Text(
            "Birden fazla seçebilirsin",
            style: TextStyle(color: Colors.black54),
          ),
          const SizedBox(height: 20),

          Wrap(
            spacing: 12,
            runSpacing: 12,
            children: options.map((opt) {
              bool selected = interests.contains(opt);

              return GestureDetector(
                onTap: () {
                  setState(() {
                    if (selected) {
                      interests.remove(opt);
                    } else {
                      interests.add(opt);
                    }
                  });
                },
                child: AnimatedContainer(
                  duration: const Duration(milliseconds: 200),
                  padding: const EdgeInsets.symmetric(
                    horizontal: 16,
                    vertical: 10,
                  ),
                  decoration: BoxDecoration(
                    color: selected ? Colors.teal : Colors.white,
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: Colors.grey.shade300),
                  ),
                  child: Text(
                    opt,
                    style: TextStyle(
                      fontSize: 15,
                      color: selected ? Colors.white : Colors.black87,
                    ),
                  ),
                ),
              );
            }).toList(),
          ),

          const Spacer(),
          const Text(
            "Sonraki ekranda sana göre öneriler göreceksin.",
            style: TextStyle(color: Colors.black54),
          ),
          const SizedBox(height: 12),
        ],
      ),
    );
  }
}
