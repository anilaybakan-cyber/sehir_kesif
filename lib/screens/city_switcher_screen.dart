// =============================================================================
// CITY SWITCHER SCREEN - MODAL BOTTOM SHEET VERSION
// Dark theme, açılır pencere şeklinde
// 6 şehir: Barcelona, Paris, Roma, İstanbul, Amsterdam, Tokyo
// "Henüz karar vermedim" seçeneği eklendi
// =============================================================================

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../services/trip_update_service.dart';
import '../services/ai_service.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import 'dart:math'; // Added for random if needed, but using microsecond/millisecond logic is fine or import math

class CitySwitcherScreen extends StatefulWidget {
  final bool isOnboarding;
  
  const CitySwitcherScreen({super.key, this.isOnboarding = false});

  @override
  State<CitySwitcherScreen> createState() => _CitySwitcherScreenState();

  /// Modal olarak açmak için static method
  static Future<String?> showAsModal(BuildContext context, {bool updateGlobalState = true}) async {
    return await showModalBottomSheet<String>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => _CitySwitcherModal(updateGlobalState: updateGlobalState),
    );
  }

  static final List<Map<String, dynamic>> allCities = [
    {"id": "amsterdam", "name": "Amsterdam", "name_en": "Amsterdam", "country": "Hollanda", "country_en": "Netherlands", "flag": "🇳🇱", "networkImage": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800"},
    {"id": "antalya", "name": "Antalya", "name_en": "Antalya", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://emaadmin.emahouses.com//Content/Blog/pVPrGzHbS\u0131dfdsfsd.jpg"},
    {"id": "atina", "name": "Atina", "name_en": "Athens", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg"},
    {"id": "bangkok", "name": "Bangkok", "name_en": "Bangkok", "country": "Tayland", "country_en": "Thailand", "flag": "🇹🇭", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg"},
    {"id": "barcelona", "name": "Barcelona", "name_en": "Barcelona", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800"},
    {"id": "belgrad", "name": "Belgrad", "name_en": "Belgrade", "country": "Sırbistan", "country_en": "Serbia", "flag": "🇷🇸", "networkImage": "https://cdnp.flypgs.com/files/Sehirler-long-tail/Belgrad/belgrad_otelleri.jpg"},
    {"id": "berlin", "name": "Berlin", "name_en": "Berlin", "country": "Almanya", "country_en": "Germany", "flag": "🇩🇪", "networkImage": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800"},
    {"id": "bruksel", "name": "Brüksel", "name_en": "Brussels", "country": "Belçika", "country_en": "Belgium", "flag": "🇧🇪", "networkImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Grand_Place_Bruselas_2.jpg/1280px-Grand_Place_Bruselas_2.jpg"},
    {"id": "budapeste", "name": "Budapeşte", "name_en": "Budapest", "country": "Macaristan", "country_en": "Hungary", "flag": "🇭🇺", "networkImage": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltfde92aef92ecf073/6787eae0bf32fe28813c50fe/BCC-2024-EXPLORER-BUDAPEST-LANDMARKS-HEADER-_MOBILE.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart"},
    {"id": "cenevre", "name": "Cenevre", "name_en": "Geneva", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/jet_deau.jpg"},
    {"id": "dubai", "name": "Dubai", "name_en": "Dubai", "country": "BAE", "country_en": "UAE", "flag": "🇦🇪", "networkImage": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800"},
    {"id": "dublin", "name": "Dublin", "name_en": "Dublin", "country": "İrlanda", "country_en": "Ireland", "flag": "🇮🇪", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/temple_bar.jpg"},
    {"id": "edinburgh", "name": "Edinburgh", "name_en": "Edinburgh", "country": "İskoçya", "country_en": "Scotland", "flag": "🏴󠁧󠁢󠁳󠁣󠁴󠁿", "networkImage": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt9d8daa2acc7bb33c/6797dc563b4101992b03092a/iStock-1153650218-MOBILE-HEADER.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart"},
    {"id": "fes", "name": "Fes", "name_en": "Fez", "country": "Fas", "country_en": "Morocco", "flag": "🇲🇦", "networkImage": "https://images.unsplash.com/photo-1548013146-72479768bada?w=800"},
    {"id": "floransa", "name": "Floransa", "name_en": "Florence", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://italien.expert/wp-content/uploads/2021/05/Florenz-Toskana-Italien0.jpg"},
    {"id": "hongkong", "name": "Hong Kong", "name_en": "Hong Kong", "country": "Çin (ÖİB)", "country_en": "China (SAR)", "flag": "🇭🇰", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/hongkong/victoria_peak.jpg"},
    {"id": "istanbul", "name": "İstanbul", "name_en": "Istanbul", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=800"},
    {"id": "kahire", "name": "Kahire", "name_en": "Cairo", "country": "Mısır", "country_en": "Egypt", "flag": "🇪🇬", "networkImage": "https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2019-11/image-explore-ancient-egypt-merl.jpg"},
    {"id": "kapadokya", "name": "Kapadokya", "name_en": "Cappadocia", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://images.unsplash.com/photo-1641128324972-af3212f0f6bd?w=800"},
    {"id": "kopenhag", "name": "Kopenhag", "name_en": "Copenhagen", "country": "Danimarka", "country_en": "Denmark", "flag": "🇩🇰", "networkImage": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800"},
    {"id": "kotor", "name": "Kotor", "name_en": "Kotor", "country": "Karadağ", "country_en": "Montenegro", "flag": "🇲🇪", "networkImage": "https://www.etstur.com/letsgo/wp-content/uploads/2025/12/montenegro-kotorda-gezilecek-yerler-en-populer-rotalar-guncel-liste-1024x576.png"},
    {"id": "lizbon", "name": "Lizbon", "name_en": "Lisbon", "country": "Portekiz", "country_en": "Portugal", "flag": "🇵🇹", "networkImage": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800"},
    {"id": "londra", "name": "Londra", "name_en": "London", "country": "İngiltere", "country_en": "United Kingdom", "flag": "🇬🇧", "networkImage": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800"},
    {"id": "lucerne", "name": "Lucerne", "name_en": "Lucerne", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lucerne/chapel_bridge_kapellbrucke.jpg"},
    {"id": "lyon", "name": "Lyon", "name_en": "Lyon", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/lyon/basilica_of_notre_dame_de_fourviere.jpg"},
    {"id": "madrid", "name": "Madrid", "name_en": "Madrid", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=800"},
    {"id": "marakes", "name": "Marakeş", "name_en": "Marrakech", "country": "Fas", "country_en": "Morocco", "flag": "🇲🇦", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/marakes/jemaa_el_fna.jpg"},
    {"id": "marsilya", "name": "Marsilya", "name_en": "Marseille", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt0feb4d48a3fc134c/67c5fafa304ea9666082ff3e/iStock-956215674-2-Header_Mobile.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart"},

    {"id": "milano", "name": "Milano", "name_en": "Milan", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800"},
    {"id": "napoli", "name": "Napoli", "name_en": "Naples", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?w=800"},
    {"id": "newyork", "name": "New York", "name_en": "New York", "country": "ABD", "country_en": "USA", "flag": "🇺🇸", "networkImage": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800"},
    {"id": "nice", "name": "Nice", "name_en": "Nice", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://www.flypgs.com/blog/wp-content/uploads/2024/05/nice-sahilleri.jpeg"},
    {"id": "oslo", "name": "Oslo", "name_en": "Oslo", "country": "Norveç", "country_en": "Norway", "flag": "🇳🇴", "networkImage": "https://www.journavel.com/wp-content/uploads/2024/10/IMG_1851-scaled.webp"},
    {"id": "paris", "name": "Paris", "name_en": "Paris", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800"},
    {"id": "porto", "name": "Porto", "name_en": "Porto", "country": "Portekiz", "country_en": "Portugal", "flag": "🇵🇹", "networkImage": "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=800"},
    {"id": "prag", "name": "Prag", "name_en": "Prague", "country": "Çekya", "country_en": "Czech Republic", "flag": "🇨🇿", "networkImage": "https://images.unsplash.com/photo-1541849546-216549ae216d?w=800"},
    {"id": "roma", "name": "Roma", "name_en": "Rome", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800"},
    {"id": "saraybosna", "name": "Saraybosna", "name_en": "Sarajevo", "country": "Bosna Hersek", "country_en": "Bosnia", "flag": "🇧🇦", "networkImage": "https://images.themagger.net/wp-content/uploads/2022/12/saraybosna-kapak-633x433.jpg"},
    {"id": "seul", "name": "Seul", "name_en": "Seoul", "country": "Güney Kore", "country_en": "South Korea", "flag": "🇰🇷", "networkImage": "https://www.agoda.com/wp-content/uploads/2019/03/Seoul-attractions-Gyeongbokgung-palace.jpg"},
    {"id": "sevilla", "name": "Sevilla", "name_en": "Seville", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://images.unsplash.com/photo-1558370781-d6196949e317?w=800"},
    {"id": "singapur", "name": "Singapur", "name_en": "Singapore", "country": "Singapur", "country_en": "Singapore", "flag": "🇸🇬", "networkImage": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?w=800"},
    {"id": "stockholm", "name": "Stockholm", "name_en": "Stockholm", "country": "İsveç", "country_en": "Sweden", "flag": "🇸🇪", "networkImage": "https://images.unsplash.com/photo-1509356843151-3e7d96241e11?w=800"},
    {"id": "strazburg", "name": "Strazburg", "name_en": "Strasbourg", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://www.avruparuyasi.com.tr/uploads/tour-gallery/36c44666-5e5a-4c2d-a341-2fa8285c3fb6.webp"},
    {"id": "tokyo", "name": "Tokyo", "name_en": "Tokyo", "country": "Japonya", "country_en": "Japan", "flag": "🇯🇵", "networkImage": "https://img.piri.net/mnresize/900/-/resim/imagecrop/2023/01/17/11/54/resized_d9b02-8b17feafkapak2.jpg"},
    {"id": "venedik", "name": "Venedik", "name_en": "Venice", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=800"},
    {"id": "viyana", "name": "Viyana", "name_en": "Vienna", "country": "Avusturya", "country_en": "Austria", "flag": "🇦🇹", "networkImage": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800"},
    {"id": "zurih", "name": "Zürih", "name_en": "Zurich", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800"},
    // New Featured Cities from Guide Articles
    {"id": "rovaniemi", "name": "Rovaniemi", "name_en": "Rovaniemi", "country": "Finlandiya", "country_en": "Finland", "flag": "🇫🇮", "networkImage": "https://www.visitfinland.com/dam/jcr:70734834-7ba2-4bf1-9f6e-bf185e014367/central-plaza-santa-claus-village-rovaniemi-lapland-finland%20(1).jpg"},
    {"id": "tromso", "name": "Tromsø", "name_en": "Tromsø", "country": "Norveç", "country_en": "Norway", "flag": "🇳🇴", "networkImage": "https://www.flightgift.com/media/wp/FG/2024/02/tromso.webp"},
    {"id": "zermatt", "name": "Zermatt", "name_en": "Zermatt", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://holidaystoswitzerland.com/wp-content/uploads/2020/07/Zermatt-and-the-Matterhorn-at-dawn.jpg"},
    {"id": "matera", "name": "Matera", "name_en": "Matera", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://ita.travel/user/blogimg/ostatni/aerial-view_matera_sunset.jpg"},
    {"id": "giethoorn", "name": "Giethoorn", "name_en": "Giethoorn", "country": "Hollanda", "country_en": "Netherlands", "flag": "🇳🇱", "networkImage": "https://www.onedayinacity.com/wp-content/uploads/2021/03/Giethoorn-Village.png"},
    {"id": "colmar", "name": "Colmar", "name_en": "Colmar", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://images.goway.com/production/hero/iStock-1423136049.jpg"},
    {"id": "sintra", "name": "Sintra", "name_en": "Sintra", "country": "Portekiz", "country_en": "Portugal", "flag": "🇵🇹", "networkImage": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt75a384a61f2efa5b/68848225e7cb649650cc2d81/BCC-2024-EXPLORER-SINTRA-BEST_PLACES_TO_VISIT-HEADER-MOBILE.jpg?format=webp&auto=avif&quality=60&crop=16%3A9&width=1440"},
    {"id": "san_sebastian", "name": "San Sebastian", "name_en": "San Sebastian", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://cdn.bunniktours.com.au/public/posts/images/Europe/Blog%20Header%20-%20Spain%20-%20San%20Sebastian%20-%20credit%20Raul%20Cacho%20Oses%20%28Unsplash%29-feature.jpg"},
    {"id": "bologna", "name": "Bologna", "name_en": "Bologna", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://www.datocms-assets.com/57243/1661342703-6245af628d40974c9ab5a7fd_petr-slovacek-sxk8bwkvoxe-unsplash-20-1.jpg?auto=compress%2Cformat"},
    {"id": "gaziantep", "name": "Gaziantep", "name_en": "Gaziantep", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://www.brandlifemag.com/wp-content/uploads/2021/04/acilis-gaziantep-december-06gaziantep-coppersmith-bazaar-600w-549044518.jpg"},
    {"id": "brugge", "name": "Brugge", "name_en": "Bruges", "country": "Belçika", "country_en": "Belgium", "flag": "🇧🇪", "networkImage": "https://gezimanya.com/sites/default/files/styles/800x600_/public/lokasyon-detay/2021-08/brugge-hakkinda-bilinmesi-gerekenler.jpg"},
    {"id": "santorini", "name": "Santorini", "name_en": "Santorini", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://www.kucukoteller.com.tr/storage/images/2024/07/14/5e7eaf11eb5ec2dda2f7a602232faa8961347f29.webp"},
    {"id": "heidelberg", "name": "Heidelberg", "name_en": "Heidelberg", "country": "Almanya", "country_en": "Germany", "flag": "🇩🇪", "networkImage": "https://image.hurimg.com/i/hurriyet/90/1110x740/56b3325818c7730e3cdb6757.jpg"},
  ];
}

// =============================================================================
// MODAL VERSION (Bottom Sheet)
// =============================================================================

class _CitySwitcherModal extends StatefulWidget {
  final bool updateGlobalState;
  
  const _CitySwitcherModal({this.updateGlobalState = true});

  @override
  State<_CitySwitcherModal> createState() => _CitySwitcherModalState();
}

class _CitySwitcherModalState extends State<_CitySwitcherModal> {
  String _selectedCity = "barcelona";
  String _searchQuery = "";
  final TextEditingController _searchController = TextEditingController();

  // Design tokens - AMBER THEME
  static const _bgDark = WanderlustColors.bgDark;
  static const _bgCard = WanderlustColors.bgCard;
  static const _bgCardLight = WanderlustColors.bgCardLight;
  static const _accent = WanderlustColors.accent; // Purple
  static const _accentLight = Color(0xFFFFB800); // Gold
  static const _textGrey = Color(0xFF9CA3AF);

  final List<Map<String, dynamic>> _cities = List.from(CitySwitcherScreen.allCities);
    
  final ScrollController _scrollController = ScrollController();

  @override
  void initState() {
    super.initState();
    _loadSelectedCity();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _initializeAndSortCities();
  }

  void _initializeAndSortCities() {
    // Reset list from source
    _cities.clear();
    _cities.addAll(CitySwitcherScreen.allCities);

    // Add "Undecided" option at the top
    _cities.insert(0, {
      "id": "undecided",
      "name": "undecided_label", // Special flag
      "country": "MyWay",
      "flag": "🌍",
      "networkImage": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800",
    });

    // Sort remaining cities alphabetically based on current language
    final isEnglish = AppLocalizations.instance.isEnglish;
    
    // Sort logic: Keep index 0 (undecided) at top, sort the rest
    final undecided = _cities.first;
    final others = _cities.sublist(1);
    
    others.sort((a, b) {
       final nameA = isEnglish ? (a["name_en"] ?? a["name"]) : a["name"];
       final nameB = isEnglish ? (b["name_en"] ?? b["name"]) : b["name"];
       return (nameA as String).compareTo(nameB as String);
    });
    
    // Reconstruct list
    _cities.clear();
    _cities.add(undecided);
    _cities.addAll(others);
  }

  Future<void> _loadSelectedCity() async {
    final prefs = await SharedPreferences.getInstance();
    final savedCity = prefs.getString("selectedCity") ?? "barcelona";
    setState(() {
      _selectedCity = savedCity;
    });
    
    // Auto-scroll to selected city
    WidgetsBinding.instance.addPostFrameCallback((_) {
      if (_searchQuery.isEmpty) {
        final index = _cities.indexWhere((c) => c["id"] == savedCity);
        if (index != -1 && _scrollController.hasClients) {
          // Estimated item height is ~92px
          final offset = index * 92.0; 
          _scrollController.jumpTo(offset);
        }
      }
    });
  }

  Future<void> _selectCity(String cityId) async {
    HapticFeedback.mediumImpact();

    if (widget.updateGlobalState) {
      final prefs = await SharedPreferences.getInstance();
      
      String finalCityId = cityId;
      if (cityId == "undecided") {
         // Pick a random city (excluding the undecided item at index 0)
         // Use existing list _cities but skip index 0
         final randomCity = CitySwitcherScreen.allCities[DateTime.now().millisecond % CitySwitcherScreen.allCities.length];
         finalCityId = randomCity['id'];
         
         await prefs.setBool("suggest_city_popup", true);
      }
      
      await prefs.setString("selectedCity", finalCityId);

      // Diğer ekranları bilgilendir
      TripUpdateService().notifyCityChanged();
      
      // If undecided, we return the decided city id so ExploreScreen knows what to load
      cityId = finalCityId;
    }

    // Kısa bir gecikme ile kapat
    Future.delayed(const Duration(milliseconds: 200), () {
      if (mounted) Navigator.pop(context, cityId);
    });
  }

  @override
  Widget build(BuildContext context) {
    final bottomPadding = MediaQuery.of(context).padding.bottom;

    return Container(
      height: MediaQuery.of(context).size.height * 0.65,
      decoration: const BoxDecoration(
        color: _bgDark,
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: Column(
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
                Text(
                  AppLocalizations.instance.selectCity,
                  style: const TextStyle(
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

          // Arama alanı
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
            child: Container(
              decoration: BoxDecoration(
                color: _bgCard,
                borderRadius: BorderRadius.circular(14),
                border: Border.all(color: Colors.white.withOpacity(0.08)),
              ),
              child: TextField(
                controller: _searchController,
                style: const TextStyle(color: Colors.white, fontSize: 15),
                decoration: InputDecoration(
                  hintText: AppLocalizations.instance.searchCity,
                  hintStyle: TextStyle(color: _textGrey.withOpacity(0.6)),
                  prefixIcon: Icon(Icons.search, color: _textGrey, size: 22),
                  suffixIcon: _searchQuery.isNotEmpty
                      ? GestureDetector(
                          onTap: () {
                            _searchController.clear();
                            setState(() => _searchQuery = "");
                          },
                          child: Icon(Icons.close, color: _textGrey, size: 20),
                        )
                      : null,
                  border: InputBorder.none,
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                ),
                onChanged: (value) => setState(() => _searchQuery = value.toLowerCase()),
              ),
            ),
          ),

          // Şehirler listesi (filtrelenmiş)
          Flexible(
            child: Builder(
              builder: (context) {
                // Filtreleme
                final isEnglish = AppLocalizations.instance.isEnglish;
                final filteredCities = _cities.where((city) {
                  if (_searchQuery.isEmpty) return true;
                  
                  // Dile göre arama (Sadece seçili dilin ismini ve ülkesini kontrol et)
                  final name = (isEnglish ? (city["name_en"] ?? city["name"]) : city["name"]).toString().toLowerCase();
                  final country = (isEnglish ? (city["country_en"] ?? city["country"]) : city["country"]).toString().toLowerCase();
                  
                  return name.contains(_searchQuery) || country.contains(_searchQuery);
                }).toList();

                if (filteredCities.isEmpty) {
                  return Center(
                    child: Column(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Icon(Icons.location_off, color: _textGrey, size: 48),
                        const SizedBox(height: 12),
                        Text(
                          AppLocalizations.instance.cityNotFoundMessage,
                          style: TextStyle(color: _textGrey, fontSize: 16),
                        ),
                      ],
                    ),
                  );
                }

                return ListView.builder(
                  controller: _scrollController,
                  // shrinkWrap removed to allow filling the expanded space
                  padding: EdgeInsets.fromLTRB(16, 4, 16, bottomPadding + 16),
                  itemCount: filteredCities.length,
                  itemBuilder: (context, index) {
                    final city = filteredCities[index];
                    final isSelected = city["id"] == _selectedCity;
                    return _buildCityTile(city, isSelected);
                  },
                );
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
                  city["id"] == "undecided" 
                      ? city["networkImage"] 
                      : AIService.getCityImage(city["id"]),
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
                    city["id"] == "undecided" 
                        ? AppLocalizations.instance.undecidedCity 
                        : (AppLocalizations.instance.isEnglish && city["name_en"] != null 
                            ? city["name_en"] 
                            : city["name"]),
                    style: TextStyle(
                      color: isSelected ? _accent : Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    city["id"] == "undecided" 
                        ? AppLocalizations.instance.ourSuggestion
                        : (AppLocalizations.instance.isEnglish && city["country_en"] != null
                            ? city["country_en"]
                            : AppLocalizations.instance.translateCountry(city["country"])),
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
    // Onboarding modunda full page şehir seçimi göster
    if (widget.isOnboarding) {
      return _CitySwitcherFullPage(
        onCitySelected: (cityId) {
          // Şehir seçildi, direkt ana sayfaya git - paywall'u main.dart gösterecek
          Navigator.of(context).pushNamedAndRemoveUntil('/main', (route) => false);
        },
      );
    }
    
    // Normal modda direkt modal'ı aç ve sonucu döndür
    WidgetsBinding.instance.addPostFrameCallback((_) async {
      final result = await CitySwitcherScreen.showAsModal(context);
      if (mounted) {
        Navigator.pop(context, result);
      }
    });

    // Geçici loading ekranı
    return const Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: Center(
        child: CircularProgressIndicator(
          color: WanderlustColors.accent,
          strokeWidth: 2,
        ),
      ),
    );
  }
}

// =============================================================================
// FULL PAGE VERSION (Onboarding için)
// =============================================================================

class _CitySwitcherFullPage extends StatefulWidget {
  final Function(String) onCitySelected;
  
  const _CitySwitcherFullPage({required this.onCitySelected});

  @override
  State<_CitySwitcherFullPage> createState() => _CitySwitcherFullPageState();
}

class _CitySwitcherFullPageState extends State<_CitySwitcherFullPage> {
  String _selectedCity = "";
  String _searchQuery = "";
  final TextEditingController _searchController = TextEditingController();

  // Design tokens - AMBER THEME
  static const _bgDark = WanderlustColors.bgDark;
  static const _bgCard = WanderlustColors.bgCard;
  static const _accent = WanderlustColors.accent;
  static const _accentLight = Color(0xFFFFB800);
  static const _textGrey = Color(0xFF9CA3AF);

  // Alphabetically sorted city list
  final List<Map<String, dynamic>> _cities = List.from(CitySwitcherScreen.allCities);

  @override
  void initState() {
    super.initState();
  }

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    _initializeAndSortCities();
  }

  void _initializeAndSortCities() {
    // Reset list from source
    _cities.clear();
    _cities.addAll(CitySwitcherScreen.allCities);

    // Add "Undecided" option at the top
    _cities.insert(0, {
      "id": "undecided",
      "name": "undecided_label", // Special flag
      "country": "MyWay",
      "flag": "🌍",
      "networkImage": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800", // Inspirational travel image
    });

    // Sort remaining cities alphabetically based on current language
    final isEnglish = AppLocalizations.instance.isEnglish;
    
    // Sort logic
    final undecided = _cities.first;
    final others = _cities.sublist(1);
    
    others.sort((a, b) {
       final nameA = isEnglish ? (a["name_en"] ?? a["name"]) : a["name"];
       final nameB = isEnglish ? (b["name_en"] ?? b["name"]) : b["name"];
       return (nameA as String).compareTo(nameB as String);
    });
    
    // Reconstruct list
    _cities.clear();
    _cities.add(undecided);
    _cities.addAll(others);
  }

  Future<void> _selectCity(String cityId) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();

    String finalCityId = cityId;

    if (cityId == "undecided") {
        // Pick a random city (excluding the undecided item which is at index 0)
        // Ensure index 0 is skipped if it's "undecided".
        // Original allCities is safe to pick from.
        final randomCity = CitySwitcherScreen.allCities[DateTime.now().millisecond % CitySwitcherScreen.allCities.length];
        finalCityId = randomCity['id'];
        
        // Mark flag to show popup in MainScreen
        await prefs.setBool("suggest_city_popup", true);
    } 

    await prefs.setString("selectedCity", finalCityId);
    
    setState(() => _selectedCity = finalCityId);
    
    // Kısa gecikme ile callback
    Future.delayed(const Duration(milliseconds: 300), () {
      widget.onCitySelected(finalCityId);
    });
  }

  @override
  Widget build(BuildContext context) {
    final filteredCities = _cities.where((city) {
      if (_searchQuery.isEmpty) return true;
      final name = city["name"].toString().toLowerCase();
      final country = city["country"].toString().toLowerCase();
      return name.contains(_searchQuery) || country.contains(_searchQuery);
    }).toList();

    return Scaffold(
      backgroundColor: _bgDark,
      body: SafeArea(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header
            Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    AppLocalizations.instance.whereTo,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 28,
                      fontWeight: FontWeight.w700,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    AppLocalizations.instance.selectCityDesc,
                    style: TextStyle(color: _textGrey, fontSize: 15),
                  ),
                ],
              ),
            ),
            
            // Arama
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 24),
              child: Container(
                decoration: BoxDecoration(
                  color: _bgCard,
                  borderRadius: BorderRadius.circular(14),
                ),
                child: TextField(
                  controller: _searchController,
                  style: const TextStyle(color: Colors.white),
                  decoration: InputDecoration(
                    hintText: AppLocalizations.instance.searchCity,
                    hintStyle: TextStyle(color: _textGrey.withOpacity(0.6)),
                    prefixIcon: Icon(Icons.search, color: _textGrey),
                    border: InputBorder.none,
                    contentPadding: const EdgeInsets.all(16),
                  ),
                  onChanged: (v) => setState(() => _searchQuery = v.toLowerCase()),
                ),
              ),
            ),
            
            const SizedBox(height: 20),
            
            // Şehir listesi
            Expanded(
              child: ListView.builder(
                padding: const EdgeInsets.symmetric(horizontal: 24),
                itemCount: filteredCities.length,
                itemBuilder: (context, index) {
                  final city = filteredCities[index];
                  final isSelected = city["id"] == _selectedCity;
                  
                  return GestureDetector(
                    onTap: () => _selectCity(city["id"]),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 200),
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        color: isSelected ? _accent.withOpacity(0.15) : _bgCard,
                        borderRadius: BorderRadius.circular(16),
                        border: Border.all(
                          color: isSelected ? _accent : Colors.transparent,
                          width: 2,
                        ),
                      ),
                      child: Row(
                        children: [
                          // Şehir fotoğrafı
                          ClipRRect(
                            borderRadius: BorderRadius.circular(12),
                            child: Image.network(
                              city["id"] == "undecided" 
                                  ? city["networkImage"] 
                                  : AIService.getCityImage(city["id"]),
                              width: 60,
                              height: 60,
                              fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(
                                width: 60,
                                height: 60,
                                color: _accent.withOpacity(0.3),
                                child: Center(child: Text(city["flag"], style: const TextStyle(fontSize: 28))),
                              ),
                            ),
                          ),
                          const SizedBox(width: 16),
                          // Bilgi
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  city["id"] == "undecided" 
                                      ? AppLocalizations.instance.undecidedCity 
                                      : (AppLocalizations.instance.isEnglish && city["name_en"] != null 
                                          ? city["name_en"] 
                                          : city["name"]),
                                  style: TextStyle(
                                    color: isSelected ? _accent : Colors.white,
                                    fontSize: 17,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                                Text(
                                  city["id"] == "undecided" 
                                      ? AppLocalizations.instance.ourSuggestion
                                      : (AppLocalizations.instance.isEnglish && city["country_en"] != null
                                          ? city["country_en"]
                                          : AppLocalizations.instance.translateCountry(city["country"])),
                                  style: TextStyle(color: _textGrey, fontSize: 13),
                                ),
                              ],
                            ),
                          ),
                          // Check
                          if (isSelected)
                            Container(
                              width: 28,
                              height: 28,
                              decoration: const BoxDecoration(
                                color: _accent,
                                shape: BoxShape.circle,
                              ),
                              child: const Icon(Icons.check, color: Colors.white, size: 18),
                            ),
                        ],
                      ),
                    ),
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
