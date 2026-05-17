// =============================================================================
// CITY SWITCHER SCREEN - MODAL & FULL PAGE VERSIONS
// =============================================================================

import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../services/trip_update_service.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';
import '../widgets/resilient_network_image.dart';
import 'dart:math';
import 'analysis_loading_screen.dart';
import '../services/premium_service.dart';
import '../services/content_update_service.dart';
import '../services/plan_repository.dart';
import '../services/analytics_service.dart'; // Added

class CitySwitcherScreen extends StatefulWidget {
  final bool isOnboarding;
  const CitySwitcherScreen({super.key, this.isOnboarding = false});

  @override
  State<CitySwitcherScreen> createState() => _CitySwitcherScreenState();

  /// Modal version
  static Future<String?> showAsModal(BuildContext context, {bool updateGlobalState = true}) async {
    return await showModalBottomSheet<String>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => _CitySwitcherModal(updateGlobalState: updateGlobalState),
    );
  }

  static List<Map<String, dynamic>> allCities = _hardcodedCities;

  static const Map<String, String> _networkImageOverrides = {
    'cannes': 'https://www.rivieraloisirs.com/public/uploads/2021/05/Port-de-Cannes.jpg',
    'selanik': 'https://www.etstur.com/letsgo/wp-content/uploads/2025/09/01-selanik-letsgo.jpg',
    'dubrovnik': 'https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/blt2a81d63f958fcf8a/67eecf23b0297a9afcc4c514/BCC-2025-EXPLORER-DUBROVNIK-BEACHES-HEADER-DESKTOP.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart&width=1920&height=1080',
    'mykonos': 'https://rtwin30days.com/wp-content/uploads/2025/02/Mykonos-Island-Greece-Things-to-Do.jpg',
    'bodrum': 'https://cdn.sanity.io/images/nxpteyfv/goguides/70798769a89c1527ed1467f7f56b36cc5146e5da-1600x1066.jpg',
    'cesme': 'https://cdn.renticar.com/cms/Izmir_Cesme_Gezilecek_Yerler_1500x1000px_blog_goersel_cesme_marina_baa7fead07.jpg',
    'kas': 'https://cdn.renticar.com/cms/Antalya_Kas_ta_Gezilecek_Yerler_1500x1000px_blog_goersel_kaputas_f9c367417e.jpg',
    'amalfi': 'https://www.royalcaribbean.com/media-assets/pmc/content/dam/shore-x/amalfi-coast-salerno-sno/es61-capri-on-your-own/stock-positano-amalfi-coast-campania-sorrento-italy-376017433.jpg?w=1920',
    'ibiza': 'https://www.visitspain.info/en/wp-content/uploads/sites/162/cala-d-hort-ibiza-hd.jpg',
    'mallorca': 'https://gotripzi.com/cdn-cgi/image/onerror=redirect,width=3200,height=2400,fit=cover,format=png/_astro/palma-es-hero.GAL_VPiM.webp',
    'valencia': 'https://img.static-kl.com/transform/81017f83-1bd0-46c4-9459-c199cf4e1dd7/',
    'palermo': 'https://gotripzi.com/cdn-cgi/image/onerror=redirect,width=3200,height=2400,fit=cover,format=png/_astro/palma-es-hero.GAL_VPiM.webp',
    'catania': 'https://images.ctfassets.net/80dqdqpre1qk/cckCqd5EJjW09siSdf6Xo/dacc69a5bffc0e3a145df995c8684fa3/Catania_overzicht.jpg?fm=webp',
    'bari': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Puglia_bari_old-town.jpg/1280px-Puglia_bari_old-town.jpg',
    'budva': 'https://www.visit-montenegro.com/wp-content/uploads/2026/01/budva-drone-01-scaled.jpg',
    'ksamil': 'https://www.turizmtatilseyahat.com/wp-content/uploads/2020/07/ksamil-gezi-rehberi-.jpg',
    'rhodes': 'https://blog.obilet.com/wp-content/uploads/2024/04/ana-gorsel-min-scaled.jpeg',
    'bruksel': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Grand_Place_Bruselas_2.jpg',
    'lucerne': 'https://upload.wikimedia.org/wikipedia/commons/7/7c/2009_08_24_06262_Lucerne.jpg',
    'rovaniemi': 'https://www.visitrovaniemi.fi/wp-content/uploads/Christmas-season-winter-snow-Santa-Claus-Village-Arctic-Circle-Rovaniemi-Lapland-Finland-15.jpg',
    'saint_tropez': 'https://cdn.sanity.io/images/nxpteyfv/goguides/3a6c92c8b52d99de1f3ef6d2fcebadfd646bf990-1600x1066.jpg',
    'san_sebastian': 'https://cdn.sanity.io/images/nxpteyfv/goguides/c77f6d1df757d922c8a164f8d063bd965cb65e99-1600x1066.jpg',
    'saraybosna': 'https://bookingcar.eu/blog/uploads/public/20250506/aerial-view-of-sarajevo-downtown-2025-01-08-03-39-59-utc_GZjdzu.jpg',
    'midilli': 'https://cdn.agentis.com.tr/www.drabostravel.com/files/actv/148/115540_b-f.jpg',
  };

  static const Set<String> _blockedCityIds = {'catania_final', 'sardinya'};

  static Future<void> loadRemoteCities() async {
    try {
      final remoteCities = await ContentUpdateService.getRemoteCitiesList();
      if (remoteCities != null && remoteCities.isNotEmpty) {
        final filteredRemote = remoteCities.where((city) => !_blockedCityIds.contains(city['id'])).toList();
        final remoteIds = filteredRemote.map((c) => c['id']).toSet();
        final mergedList = List<Map<String, dynamic>>.from(filteredRemote);
        for (final city in _hardcodedCities) {
          if (!remoteIds.contains(city['id'])) mergedList.add(city);
        }
        _applyNetworkImageOverrides(mergedList);
        allCities = mergedList;
      }
    } catch (e) {
      debugPrint('Error loading remote cities: $e');
    }
  }

  static final List<Map<String, dynamic>> _hardcodedCities = [
    {"id": "amalfi", "name": "Amalfi", "name_en": "Amalfi", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1612698093158-e07ac200d44e?w=800"},
    {"id": "amsterdam", "name": "Amsterdam", "name_en": "Amsterdam", "country": "Hollanda", "country_en": "Netherlands", "flag": "🇳🇱", "networkImage": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800"},
    {"id": "antalya", "name": "Antalya", "name_en": "Antalya", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://emaadmin.emahouses.com//Content/Blog/pVPrGzHbS\u0131dfdsfsd.jpg"},
    {"id": "atina", "name": "Atina", "name_en": "Athens", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/atina/akropolis.jpg"},
    {"id": "bangkok", "name": "Bangkok", "name_en": "Bangkok", "country": "Tayland", "country_en": "Thailand", "flag": "🇹🇭", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/bangkok/grand_palace.jpg"},
    {"id": "barcelona", "name": "Barcelona", "name_en": "Barcelona", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800"},
    {"id": "belgrad", "name": "Belgrad", "name_en": "Belgrade", "country": "Sırbistan", "country_en": "Serbia", "flag": "🇷🇸", "networkImage": "https://cdnp.flypgs.com/files/Sehirler-long-tail/Belgrad/belgrad_otelleri.jpg"},
    {"id": "berlin", "name": "Berlin", "name_en": "Berlin", "country": "Almanya", "country_en": "Germany", "flag": "🇩🇪", "networkImage": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=800"},
    {"id": "bodrum", "name": "Bodrum", "name_en": "Bodrum", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://images.unsplash.com/photo-1665673931787-c2df9e00fa28?w=800"},
    {"id": "bruksel", "name": "Brüksel", "name_en": "Brussels", "country": "Belçika", "country_en": "Belgium", "flag": "🇧🇪", "networkImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Grand_Place_Bruselas_2.jpg/1280px-Grand_Place_Bruselas_2.jpg"},
    {"id": "budapeste", "name": "Budapeşte", "name_en": "Budapest", "country": "Macaristan", "country_en": "Hungary", "flag": "🇭🇺", "networkImage": "https://images.contentstack.io/v3/assets/blt06f605a34f1194ff/bltfde92aef92ecf073/6787eae0bf32fe28813c50fe/BCC-2024-EXPLORER-BUDAPEST-LANDMARKS-HEADER-_MOBILE.jpg?fit=crop&disable=upscale&auto=webp&quality=60&crop=smart"},
    {"id": "cenevre", "name": "Cenevre", "name_en": "Geneva", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/cenevre/jet_deau.jpg"},
    {"id": "cesme", "name": "Çeşme", "name_en": "Cesme", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://images.unsplash.com/photo-1596627116790-af6f46dddbae?w=800"},
    {"id": "dubai", "name": "Dubai", "name_en": "Dubai", "country": "BAE", "country_en": "UAE", "flag": "🇦🇪", "networkImage": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800"},
    {"id": "dublin", "name": "Dublin", "name_en": "Dublin", "country": "İrlanda", "country_en": "Ireland", "flag": "🇮🇪", "networkImage": "https://storage.googleapis.com/myway-3fe75.firebasestorage.app/cities/dublin/temple_bar.jpg"},
    {"id": "dubrovnik", "name": "Dubrovnik", "name_en": "Dubrovnik", "country": "Hırvatistan", "country_en": "Croatia", "flag": "🇭🇷", "networkImage": "https://images.unsplash.com/photo-1555990538-c48ed2061c43?w=800"},
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
    {"id": "mykonos", "name": "Mikonos", "name_en": "Mykonos", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://images.unsplash.com/photo-1601581875309-fafbf2d3ed3a?w=800"},
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
    {"id": "tokyo", "name": "Tokyo", "name_en": "Tokyo", "country": "Japonya", "country_en": "Japan", "flag": "🇮🇹", "networkImage": "https://img.piri.net/mnresize/900/-/resim/imagecrop/2023/01/17/11/54/resized_d9b02-8b17feafkapak2.jpg"},
    {"id": "venedik", "name": "Venedik", "name_en": "Venice", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.unsplash.com/photo-1514890547357-a9ee288728e0?w=800"},
    {"id": "viyana", "name": "Viyana", "name_en": "Vienna", "country": "Avusturya", "country_en": "Austria", "flag": "🇦🇹", "networkImage": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=800"},
    {"id": "zurih", "name": "Zürih", "name_en": "Zurich", "country": "İsviçre", "country_en": "Switzerland", "flag": "🇨🇭", "networkImage": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800"},
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
    {"id": "cannes", "name": "Cannes", "name_en": "Cannes", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://www.rivieraloisirs.com/public/uploads/2021/05/Port-de-Cannes.jpg"},
    {"id": "selanik", "name": "Selanik", "name_en": "Thessaloniki", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://www.etstur.com/letsgo/wp-content/uploads/2025/09/01-selanik-letsgo.jpg"},
    {"id": "kas", "name": "Kaş", "name_en": "Kas", "country": "Türkiye", "country_en": "Turkey", "flag": "🇹🇷", "networkImage": "https://cdn.renticar.com/cms/Antalya_Kas_ta_Gezilecek_Yerler_1500x1000px_blog_goersel_kaputas_f9c367417e.jpg"},
    {"id": "ibiza", "name": "İbiza", "name_en": "Ibiza", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://www.visitspain.info/en/wp-content/uploads/sites/162/cala-d-hort-ibiza-hd.jpg"},
    {"id": "mallorca", "name": "Mallorca", "name_en": "Mallorca", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://gotripzi.com/cdn-cgi/image/onerror=redirect,width=3200,height=2400,fit=cover,format=png/_astro/palma-es-hero.GAL_VPiM.webp"},
    {"id": "valencia", "name": "Valencia", "name_en": "Valencia", "country": "İspanya", "country_en": "Spain", "flag": "🇪🇸", "networkImage": "https://img.static-kl.com/transform/81017f83-1bd0-46c4-9459-c199cf4e1dd7/"},
    {"id": "palermo", "name": "Palermo", "name_en": "Palermo", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://gotripzi.com/cdn-cgi/image/onerror=redirect,width=3200,height=2400,fit=cover,format=png/_astro/palma-es-hero.GAL_VPiM.webp"},
    {"id": "catania", "name": "Catania", "name_en": "Catania", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://images.ctfassets.net/80dqdqpre1qk/cckCqd5EJjW09siSdf6Xo/dacc69a5bffc0e3a145df995c8684fa3/Catania_overzicht.jpg?fm=webp"},
    {"id": "bari", "name": "Bari", "name_en": "Bari", "country": "İtalya", "country_en": "Italy", "flag": "🇮🇹", "networkImage": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Puglia_bari_old-town.jpg/1280px-Puglia_bari_old-town.jpg"},
    {"id": "budva", "name": "Budva", "name_en": "Budva", "country": "Karadağ", "country_en": "Montenegro", "flag": "🇲🇪", "networkImage": "https://www.visit-montenegro.com/wp-content/uploads/2026/01/budva-drone-01-scaled.jpg"},
    {"id": "ksamil", "name": "Ksamil", "name_en": "Ksamil", "country": "Arnavutluk", "country_en": "Albania", "flag": "🇦🇱", "networkImage": "https://www.turizmtatilseyahat.com/wp-content/uploads/2020/07/ksamil-gezi-rehberi-.jpg"},
    {"id": "rhodes", "name": "Rodos", "name_en": "Rhodes", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://blog.obilet.com/wp-content/uploads/2024/04/ana-gorsel-min-scaled.jpeg"},
    {"id": "saint_tropez", "name": "Saint Tropez", "name_en": "Saint Tropez", "country": "Fransa", "country_en": "France", "flag": "🇫🇷", "networkImage": "https://cdn.sanity.io/images/nxpteyfv/goguides/3a6c92c8b52d99de1f3ef6d2fcebadfd646bf990-1600x1066.jpg"},
    {"id": "midilli", "name": "Midilli", "name_en": "Lesbos", "country": "Yunanistan", "country_en": "Greece", "flag": "🇬🇷", "networkImage": "https://cdn.agentis.com.tr/www.drabostravel.com/files/actv/148/115540_b-f.jpg"},
  ];

  static void _applyNetworkImageOverrides(List<Map<String, dynamic>> cities) {
    for (final city in cities) {
      final id = city['id'];
      if (id is String && _networkImageOverrides.containsKey(id)) {
        city['networkImage'] = _networkImageOverrides[id];
      }
    }
  }

  static int _compareStrings(String a, String b) {
    const turkishAlphabet = "AaBbCcÇçDdEeFfGgĞğHhIıİiJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz";
    int len = a.length < b.length ? a.length : b.length;
    for (int i = 0; i < len; i++) {
      if (a[i] == b[i]) continue;
      int indexA = turkishAlphabet.indexOf(a[i]);
      int indexB = turkishAlphabet.indexOf(b[i]);
      if (indexA != -1 && indexB != -1) return indexA.compareTo(indexB);
      return a[i].compareTo(b[i]);
    }
    return a.length.compareTo(b.length);
  }
}

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
  static const _bgDark = Color(0xFFF5F1E9); // Light cream as seen in screenshot
  static const _bgCard = Colors.white;
  static const _accent = Color(0xFF1F2937); // Dark charcoal for contrast
  static const _textGrey = Color(0xFF6B7280); // Darker grey for subtitles
  String? _selectedCountry;
  late final List<Map<String, dynamic>> _cities;
  late final List<Map<String, String>> _countries;

  @override
  void initState() {
    super.initState();
    final isEnglish = AppLocalizations.instance.isEnglish;
    final Map<String, Map<String, String>> countryMaster = {
      'turkey': {'tr': 'Türkiye', 'en': 'Turkey', 'flag': '🇹🇷'},
      'spain': {'tr': 'İspanya', 'en': 'Spain', 'flag': '🇪🇸'},
      'france': {'tr': 'Fransa', 'en': 'France', 'flag': '🇫🇷'},
      'italy': {'tr': 'İtalya', 'en': 'Italy', 'flag': '🇮🇹'},
      'netherlands': {'tr': 'Hollanda', 'en': 'Netherlands', 'flag': '🇳🇱'},
      'united kingdom': {'tr': 'İngiltere', 'en': 'United Kingdom', 'flag': '🇬🇧'},
      'germany': {'tr': 'Almanya', 'en': 'Germany', 'flag': '🇩🇪'},
      'austria': {'tr': 'Avusturya', 'en': 'Austria', 'flag': '🇦🇹'},
      'czechia': {'tr': 'Çekya', 'en': 'Czechia', 'flag': '🇨🇿'},
      'portugal': {'tr': 'Portekiz', 'en': 'Portugal', 'flag': '🇵🇹'},
      'japan': {'tr': 'Japonya', 'en': 'Japan', 'flag': '🇯🇵'},
      'south korea': {'tr': 'Güney Kore', 'en': 'South Korea', 'flag': '🇰🇷'},
      'singapore': {'tr': 'Singapur', 'en': 'Singapur', 'flag': '🇸🇬'},
      'uae': {'tr': 'BAE', 'en': 'UAE', 'flag': '🇦🇪'},
      'usa': {'tr': 'ABD', 'en': 'USA', 'flag': '🇺🇸'},
      'greece': {'tr': 'Yunanistan', 'en': 'Greece', 'flag': '🇬🇷'},
      'thailand': {'tr': 'Tayland', 'en': 'Thailand', 'flag': '🇹🇭'},
      'serbia': {'tr': 'Sırbistan', 'en': 'Serbia', 'flag': '🇷🇸'},
      'belgium': {'tr': 'Belçika', 'en': 'Belgium', 'flag': '🇧🇪'},
      'hungary': {'tr': 'Macaristan', 'en': 'Hungary', 'flag': '🇭🇺'},
      'switzerland': {'tr': 'İsviçre', 'en': 'Switzerland', 'flag': '🇨🇭'},
      'ireland': {'tr': 'İrlanda', 'en': 'Ireland', 'flag': '🇮🇪'},
      'scotland': {'tr': 'İskoçya', 'en': 'Scotland', 'flag': '🏴󠁧󠁢󠁳󠁣󠁴󠁿'},
      'morocco': {'tr': 'Fas', 'en': 'Morocco', 'flag': '🇲🇦'},
      'china (sar)': {'tr': 'Çin (ÖİB)', 'en': 'China (SAR)', 'flag': '🇭🇰'},
      'egypt': {'tr': 'Mısır', 'en': 'Egypt', 'flag': '🇪🇬'},
      'denmark': {'tr': 'Danimarka', 'en': 'Denmark', 'flag': '🇩🇰'},
      'montenegro': {'tr': 'Karadağ', 'en': 'Montenegro', 'flag': '🇲🇪'},
      'norway': {'tr': 'Norveç', 'en': 'Norway', 'flag': '🇳🇴'},
      'bosnia and herzegovina': {'tr': 'Bosna Hersek', 'en': 'Bosnia and Herzegovina', 'flag': '🇧🇦'},
      'sweden': {'tr': 'İsveç', 'en': 'Sweden', 'flag': '🇸🇪'},
      'finland': {'tr': 'Finlandiya', 'en': 'Finland', 'flag': '🇫🇮'},
      'albania': {'tr': 'Arnavutluk', 'en': 'Albania', 'flag': '🇦🇱'},
    };

    final Map<String, String> trToEnKey = {
      'türkiye': 'turkey', 'ispanya': 'spain', 'fransa': 'france', 'italy': 'italy', 'italya': 'italy',
      'hollanda': 'netherlands', 'ingiltere': 'united kingdom', 'almanya': 'germany', 'avusturya': 'austria',
      'çekya': 'czechia', 'portekiz': 'portugal', 'japonya': 'japan', 'güney kore': 'south korea',
      'singapur': 'singapore', 'bae': 'uae', 'abd': 'usa', 'yunanistan': 'greece', 'tayland': 'thailand',
      'sırbistan': 'serbia', 'belçika': 'belgium', 'macaristan': 'hungary', 'isviçre': 'switzerland',
      'irlanda': 'ireland', 'iskoçya': 'scotland', 'fas': 'morocco', 'mısır': 'egypt', 'danimarka': 'denmark',
      'karadağ': 'montenegro', 'norveç': 'norway', 'bosna hersek': 'bosnia and herzegovina', 'isveç': 'sweden',
      'finlandiya': 'finland', 'arnavutluk': 'albania'
    };

    _cities = [];
    final rawCities = List<Map<String, dynamic>>.from(CitySwitcherScreen.allCities);
    for (var city in rawCities) {
      if (city["id"] == "undecided") continue;
      final cTr = (city["country"] ?? "").toString().toLowerCase().trim();
      final cEn = (city["country_en"] ?? "").toString().toLowerCase().trim();
      String? masterKey = trToEnKey[cTr] ?? (countryMaster.containsKey(cEn) ? cEn : (countryMaster.containsKey(cTr) ? cTr : null));
      if (masterKey != null) {
        final master = countryMaster[masterKey]!;
        city["country"] = master['tr'];
        city["country_en"] = master['en'];
        city["flag"] = master['flag'];
      }
      _cities.add(city);
    }

    _cities.sort((a, b) {
      final nameA = isEnglish ? (a["name_en"] ?? a["name"]) : a["name"];
      final nameB = isEnglish ? (b["name_en"] ?? b["name"]) : b["name"];
      return CitySwitcherScreen._compareStrings(nameA.toString(), nameB.toString());
    });

    final countryMap = <String, Map<String, String>>{};
    for (var city in _cities) {
      final key = city["country_en"].toString().toLowerCase().trim();
      if (!countryMap.containsKey(key)) {
        countryMap[key] = {
          "name": city["country"],
          "name_en": city["country_en"],
          "flag": city["flag"] as String,
        };
      }
    }
    _countries = countryMap.values.toList();
    _countries.sort((a, b) {
      final nA = isEnglish ? a["name_en"]! : a["name"]!;
      final nB = isEnglish ? b["name_en"]! : b["name"]!;
      return CitySwitcherScreen._compareStrings(nA, nB);
    });

    _cities.insert(0, {
      "id": "undecided",
      "name": "undecided_label",
      "name_en": "undecided_label",
      "country": "MyWay",
      "country_en": "MyWay",
      "flag": "🌍",
      "networkImage": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800",
    });
    _loadSelectedCity();
  }

  Future<void> _loadSelectedCity() async {
    final prefs = await SharedPreferences.getInstance();
    final savedCity = prefs.getString("selectedCity") ?? "barcelona";
    setState(() => _selectedCity = savedCity);
    final cityData = _cities.firstWhere((c) => c["id"] == savedCity, orElse: () => _cities[1]);
    if (cityData["id"] != "undecided") _selectedCountry = cityData["country_en"];
  }

  Future<void> _selectCity(String cityId) async {
    HapticFeedback.mediumImpact();
    if (widget.updateGlobalState) {
      final prefs = await SharedPreferences.getInstance();
      String finalCityId = cityId;
      if (cityId == "undecided") {
        final randomCity = CitySwitcherScreen.allCities[DateTime.now().millisecond % CitySwitcherScreen.allCities.length];
        finalCityId = randomCity['id'];
        await prefs.setBool("suggest_city_popup", true);
      }
      await prefs.setString("selectedCity", finalCityId);
      
      // Şehir değişikliğini hemen bildir - ExploreScreen arka planda veri ve görsel yükleyecek
      TripUpdateService().notifyCityChanged();
      
      final normalizedCity = finalCityId.toLowerCase();
      final hasExistingPlan = prefs.getString("trip_schedule_$normalizedCity") != null ||
                               prefs.getInt("tripDays_$normalizedCity") != null;
      
      if (!hasExistingPlan) {
        final selectedDays = await _showDaysSelectionDialog();
        if (selectedDays != null && selectedDays > 0) {
          await prefs.setInt("tripDays_$normalizedCity", selectedDays);
        }
      }

      cityId = finalCityId;
      
      // --- ANALYTICS: City Selection ---
      AnalyticsService.instance.logSelectContent(
        contentType: 'city',
        itemId: cityId,
      );
    }
    Future.delayed(const Duration(milliseconds: 200), () {
      if (mounted) Navigator.pop(context, cityId);
    });
  }

  Future<int?> _showDaysSelectionDialog() async {
    final isEn = AppLocalizations.instance.isEnglish;
    const bgCard = Color(0xFFFFFCF8);
    const textPrimary = Color(0xFF2F2638);
    const accent = WanderlustColors.accent;

    int tempDays = 3; // Varsayılan 3 gün

    return showModalBottomSheet<int>(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => StatefulBuilder(
        builder: (context, setModalState) {
          return Container(
            padding: const EdgeInsets.all(28),
            decoration: const BoxDecoration(
              color: bgCard,
              borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
            ),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: textPrimary.withOpacity(0.2),
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
                const SizedBox(height: 24),
                Text(
                  isEn ? "How many days will you stay?" : "Kaç gün kalacaksın?",
                  style: const TextStyle(
                    color: textPrimary,
                    fontSize: 22,
                    fontWeight: FontWeight.w800,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 8),
                Text(
                  isEn
                      ? "This helps us plan your trip better"
                      : "Bu bize rotanı daha iyi planlamamıza yardımcı olur",
                  style: TextStyle(
                    color: textPrimary.withOpacity(0.6),
                    fontSize: 14,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 36),
                // Seçilen gün sayısı büyük gösterim
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                  decoration: BoxDecoration(
                    color: accent.withOpacity(0.12),
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(color: accent.withOpacity(0.3)),
                  ),
                  child: Text(
                    isEn ? "$tempDays Days" : "$tempDays Gün",
                    style: const TextStyle(
                      color: accent,
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                const SizedBox(height: 28),
                // Şık Slider (1-14 gün)
                SliderTheme(
                  data: SliderThemeData(
                    activeTrackColor: accent,
                    inactiveTrackColor: textPrimary.withOpacity(0.1),
                    thumbColor: accent,
                    thumbShape: const RoundSliderThumbShape(enabledThumbRadius: 10),
                    trackHeight: 6,
                    overlayColor: accent.withOpacity(0.2),
                  ),
                  child: Slider(
                    value: tempDays.toDouble(),
                    min: 1,
                    max: 14,
                    divisions: 13,
                    onChanged: (v) {
                      HapticFeedback.selectionClick();
                      setModalState(() => tempDays = v.toInt());
                    },
                  ),
                ),
                const SizedBox(height: 36),
                // Onay Butonu
                SizedBox(
                  width: double.infinity,
                  height: 54,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: accent,
                      foregroundColor: Colors.white,
                      elevation: 0,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    onPressed: () => Navigator.pop(context, tempDays),
                    child: Text(
                      isEn ? "Confirm" : "Onayla",
                      style: const TextStyle(
                        fontSize: 17,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                GestureDetector(
                  onTap: () => Navigator.pop(context, null),
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(
                      isEn ? "Skip for now" : "Şimdilik geç",
                      style: TextStyle(
                        color: textPrimary.withOpacity(0.5),
                        fontSize: 14,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 20),
              ],
            ),
          );
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final bottomPadding = MediaQuery.of(context).padding.bottom;
    final isEn = AppLocalizations.instance.isEnglish;
    return Container(
      height: MediaQuery.of(context).size.height * 0.85,
      decoration: const BoxDecoration(color: _bgDark, borderRadius: BorderRadius.vertical(top: Radius.circular(28))),
      child: Column(
        children: [
          Container(
            margin: const EdgeInsets.only(top: 12),
            width: 40, height: 4,
            decoration: BoxDecoration(color: Colors.black.withOpacity(0.1), borderRadius: BorderRadius.circular(2)),
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 20, 16, 12),
            child: Row(
              children: [
                if (_selectedCountry != null && _searchQuery.isEmpty)
                  GestureDetector(
                    onTap: () => setState(() => _selectedCountry = null),
                    child: Container(
                      padding: const EdgeInsets.all(8),
                      margin: const EdgeInsets.only(right: 12),
                      decoration: BoxDecoration(color: Colors.black.withOpacity(0.05), borderRadius: BorderRadius.circular(10)),
                      child: const Icon(Icons.arrow_back_rounded, color: Colors.black, size: 20),
                    ),
                  ),
                Expanded(
                  child: Text(
                    _searchQuery.isNotEmpty
                        ? (isEn ? "Search Results" : "Arama Sonuçları")
                        : (_selectedCountry == null ? (isEn ? "Select Country" : "Ülke Seç") : (isEn ? "Select City" : "Şehir Seç")),
                    style: const TextStyle(color: Colors.black, fontSize: 22, fontWeight: FontWeight.w700),
                  ),
                ),
                GestureDetector(
                  onTap: () => Navigator.pop(context),
                  child: Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(color: Colors.black.withOpacity(0.05), borderRadius: BorderRadius.circular(10)),
                    child: const Icon(Icons.close_rounded, color: Colors.black, size: 20),
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              decoration: BoxDecoration(color: _bgCard, borderRadius: BorderRadius.circular(16), border: Border.all(color: Colors.black.withOpacity(0.06))),
              child: TextField(
                controller: _searchController,
                onChanged: (value) => setState(() => _searchQuery = value),
                style: const TextStyle(color: Colors.black, fontSize: 16),
                decoration: InputDecoration(
                  hintText: isEn ? "Search city or country..." : "Şehir veya ülke ara...",
                  hintStyle: TextStyle(color: _textGrey, fontSize: 15),
                  border: InputBorder.none,
                  icon: Icon(Icons.search_rounded, color: _textGrey, size: 20),
                  suffixIcon: _searchQuery.isNotEmpty ? IconButton(icon: Icon(Icons.close_rounded, color: _textGrey, size: 20), onPressed: () { _searchController.clear(); setState(() => _searchQuery = ""); }) : null,
                ),
              ),
            ),
          ),
          Expanded(
            child: Builder(
              builder: (context) {
                if (_searchQuery.isNotEmpty) {
                  final filteredCities = _cities.where((city) {
                    final name = (isEn ? (city["name_en"] ?? city["name"]) : city["name"]).toString().toLowerCase();
                    final country = (isEn ? (city["country_en"] ?? city["country"]) : city["country"]).toString().toLowerCase();
                    final query = _searchQuery.toLowerCase();
                    return name.contains(query) || country.contains(query);
                  }).toList();
                  if (filteredCities.isEmpty) return _buildEmptyState();
                  return ListView.builder(
                    padding: EdgeInsets.fromLTRB(16, 4, 16, bottomPadding + 16),
                    itemCount: filteredCities.length,
                    itemBuilder: (context, index) => _buildCityTile(filteredCities[index], filteredCities[index]["id"] == _selectedCity),
                  );
                }
                if (_selectedCountry == null) {
                  return ListView.builder(
                    key: const PageStorageKey('country_list'), // Added to preserve scroll position
                    padding: EdgeInsets.fromLTRB(16, 4, 16, bottomPadding + 16),
                    itemCount: _countries.length + 1,
                    itemBuilder: (context, index) {
                      if (index == 0) return _buildCityTile(_cities[0], _selectedCity == "undecided");
                      return _buildCountryTile(_countries[index - 1]);
                    },
                  );
                }
                final countryCities = _cities.where((c) => c["country_en"] == _selectedCountry).toList();
                return ListView.builder(
                  padding: EdgeInsets.fromLTRB(16, 4, 16, bottomPadding + 16),
                  itemCount: countryCities.length,
                  itemBuilder: (context, index) => _buildCityTile(countryCities[index], countryCities[index]["id"] == _selectedCity),
                );
              },
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildCountryTile(Map<String, String> country) {
    final isEn = AppLocalizations.instance.isEnglish;
    final name = isEn ? country["name_en"]! : country["name"]!;
    return GestureDetector(
      onTap: () => setState(() => _selectedCountry = country["name_en"]),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 18),
        decoration: BoxDecoration(color: _bgCard, borderRadius: BorderRadius.circular(16), border: Border.all(color: Colors.black.withOpacity(0.06))),
        child: Row(
          children: [
            Text(country["flag"]!, style: const TextStyle(fontSize: 24)),
            const SizedBox(width: 16),
            Expanded(child: Text(name, style: const TextStyle(color: Colors.black, fontSize: 16, fontWeight: FontWeight.w600))),
            const Icon(Icons.chevron_right_rounded, color: _textGrey),
          ],
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.location_off, color: _textGrey, size: 48),
          const SizedBox(height: 12),
          Text(AppLocalizations.instance.cityNotFoundMessage, style: TextStyle(color: _textGrey, fontSize: 16)),
        ],
      ),
    );
  }

  Widget _buildCityTile(Map<String, dynamic> city, bool isSelected) {
    return GestureDetector(
      onTap: () => _selectCity(city["id"]),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isSelected ? _accent.withOpacity(0.05) : _bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: isSelected ? _accent : Colors.black.withOpacity(0.06), width: 1),
        ),
        child: Row(
          children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: SizedBox(
                width: 56, height: 56,
                child: ResilientNetworkImage(
                  imageUrl: city["networkImage"] as String?,
                  placeName: (city["name"] ?? city["id"]).toString(),
                  city: city["id"].toString(),
                  category: 'city',
                  width: 56,
                  height: 56,
                  fit: BoxFit.cover,
                  placeholderBuilder: (_) => Container(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        colors: [_accent.withOpacity(0.2), _accent.withOpacity(0.2)],
                      ),
                    ),
                    child: Center(child: Text(city["flag"], style: const TextStyle(fontSize: 24))),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    city["id"] == "undecided" ? AppLocalizations.instance.undecidedCity : (AppLocalizations.instance.isEnglish && city["name_en"] != null ? city["name_en"] : city["name"]),
                    style: TextStyle(color: isSelected ? _accent : Colors.black, fontSize: 16, fontWeight: FontWeight.w600),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    city["id"] == "undecided" ? AppLocalizations.instance.ourSuggestion : (AppLocalizations.instance.isEnglish ? city["country_en"] : city["country"]),
                    style: TextStyle(color: Colors.black.withOpacity(0.55), fontSize: 13),
                  ),
                ],
              ),
            ),
            if (isSelected)
              Container(width: 24, height: 24, decoration: const BoxDecoration(color: _accent, shape: BoxShape.circle), child: const Icon(Icons.check_rounded, color: Colors.white, size: 16))
            else
              Container(width: 24, height: 24, decoration: BoxDecoration(shape: BoxShape.circle, border: Border.all(color: Colors.black.withOpacity(0.1), width: 2))),
          ],
        ),
      ),
    );
  }
}

class _CitySwitcherScreenState extends State<CitySwitcherScreen> {
  @override
  Widget build(BuildContext context) {
    if (widget.isOnboarding) {
      return _CitySwitcherFullPage(
        onCitySelected: (cityId) async {
          final isPremium = PremiumService.instance.hasFullAccess;
          final hasCreatedPlan = await PlanRepository.hasUsedPlanForCity(cityId);
          final trialCount = await PlanRepository.getTrialCount(cityId);
          if ((!isPremium && hasCreatedPlan) || trialCount > 0) {
            Navigator.pushReplacementNamed(context, '/main');
          } else {
            Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => AnalysisLoadingScreen(cityId: cityId)));
          }
        },
      );
    }
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: Stack(
        children: [
          _CitySwitcherFullPage(onCitySelected: (cityId) => Navigator.pop(context, cityId)),
          Positioned(
            top: MediaQuery.of(context).padding.top + 10, left: 20,
            child: IconButton(icon: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.black), onPressed: () => Navigator.pop(context)),
          ),
        ],
      ),
    );
  }
}

class _CitySwitcherFullPage extends StatefulWidget {
  final Function(String) onCitySelected;
  const _CitySwitcherFullPage({required this.onCitySelected});
  @override
  State<_CitySwitcherFullPage> createState() => _CitySwitcherFullPageState();
}

/// Onboarding'de kullanılan tam-ekran şehir seçici. Modal versiyonu ile
/// aynı zengin akışı kullanır: arama + ülke kademesi + ülkenin şehirleri.
/// Tek fark: tam ekran, drag handle yok, üstte hoş geldin başlığı var.
class _CitySwitcherFullPageState extends State<_CitySwitcherFullPage> {
  static const _bgDark = Color(0xFFF5F1E9);
  static const _bgCard = Colors.white;
  static const _accent = Color(0xFF1F2937);
  static const _textGrey = Color(0xFF6B7280);

  String _selectedCity = "barcelona";
  String _searchQuery = "";
  final TextEditingController _searchController = TextEditingController();
  String? _selectedCountry;

  late final List<Map<String, dynamic>> _cities;
  late final List<Map<String, String>> _countries;

  @override
  void initState() {
    super.initState();
    final isEnglish = AppLocalizations.instance.isEnglish;

    // Modal versiyonuyla aynı ülke master tablosu
    final Map<String, Map<String, String>> countryMaster = {
      'turkey': {'tr': 'Türkiye', 'en': 'Turkey', 'flag': '🇹🇷'},
      'spain': {'tr': 'İspanya', 'en': 'Spain', 'flag': '🇪🇸'},
      'france': {'tr': 'Fransa', 'en': 'France', 'flag': '🇫🇷'},
      'italy': {'tr': 'İtalya', 'en': 'Italy', 'flag': '🇮🇹'},
      'netherlands': {'tr': 'Hollanda', 'en': 'Netherlands', 'flag': '🇳🇱'},
      'united kingdom': {'tr': 'İngiltere', 'en': 'United Kingdom', 'flag': '🇬🇧'},
      'germany': {'tr': 'Almanya', 'en': 'Germany', 'flag': '🇩🇪'},
      'austria': {'tr': 'Avusturya', 'en': 'Austria', 'flag': '🇦🇹'},
      'czechia': {'tr': 'Çekya', 'en': 'Czechia', 'flag': '🇨🇿'},
      'czech republic': {'tr': 'Çekya', 'en': 'Czechia', 'flag': '🇨🇿'},
      'portugal': {'tr': 'Portekiz', 'en': 'Portugal', 'flag': '🇵🇹'},
      'japan': {'tr': 'Japonya', 'en': 'Japan', 'flag': '🇯🇵'},
      'south korea': {'tr': 'Güney Kore', 'en': 'South Korea', 'flag': '🇰🇷'},
      'singapore': {'tr': 'Singapur', 'en': 'Singapore', 'flag': '🇸🇬'},
      'uae': {'tr': 'BAE', 'en': 'UAE', 'flag': '🇦🇪'},
      'usa': {'tr': 'ABD', 'en': 'USA', 'flag': '🇺🇸'},
      'greece': {'tr': 'Yunanistan', 'en': 'Greece', 'flag': '🇬🇷'},
      'thailand': {'tr': 'Tayland', 'en': 'Thailand', 'flag': '🇹🇭'},
      'serbia': {'tr': 'Sırbistan', 'en': 'Serbia', 'flag': '🇷🇸'},
      'belgium': {'tr': 'Belçika', 'en': 'Belgium', 'flag': '🇧🇪'},
      'hungary': {'tr': 'Macaristan', 'en': 'Hungary', 'flag': '🇭🇺'},
      'switzerland': {'tr': 'İsviçre', 'en': 'Switzerland', 'flag': '🇨🇭'},
      'ireland': {'tr': 'İrlanda', 'en': 'Ireland', 'flag': '🇮🇪'},
      'scotland': {'tr': 'İskoçya', 'en': 'Scotland', 'flag': '🏴󠁧󠁢󠁳󠁣󠁴󠁿'},
      'morocco': {'tr': 'Fas', 'en': 'Morocco', 'flag': '🇲🇦'},
      'china (sar)': {'tr': 'Çin (ÖİB)', 'en': 'China (SAR)', 'flag': '🇭🇰'},
      'egypt': {'tr': 'Mısır', 'en': 'Egypt', 'flag': '🇪🇬'},
      'denmark': {'tr': 'Danimarka', 'en': 'Denmark', 'flag': '🇩🇰'},
      'montenegro': {'tr': 'Karadağ', 'en': 'Montenegro', 'flag': '🇲🇪'},
      'norway': {'tr': 'Norveç', 'en': 'Norway', 'flag': '🇳🇴'},
      'bosnia and herzegovina': {'tr': 'Bosna Hersek', 'en': 'Bosnia and Herzegovina', 'flag': '🇧🇦'},
      'bosnia': {'tr': 'Bosna Hersek', 'en': 'Bosnia and Herzegovina', 'flag': '🇧🇦'},
      'sweden': {'tr': 'İsveç', 'en': 'Sweden', 'flag': '🇸🇪'},
      'finland': {'tr': 'Finlandiya', 'en': 'Finland', 'flag': '🇫🇮'},
      'albania': {'tr': 'Arnavutluk', 'en': 'Albania', 'flag': '🇦🇱'},
      'croatia': {'tr': 'Hırvatistan', 'en': 'Croatia', 'flag': '🇭🇷'},
    };

    final Map<String, String> trToEnKey = {
      'türkiye': 'turkey', 'ispanya': 'spain', 'fransa': 'france',
      'italya': 'italy', 'hollanda': 'netherlands', 'ingiltere': 'united kingdom',
      'almanya': 'germany', 'avusturya': 'austria', 'çekya': 'czechia',
      'portekiz': 'portugal', 'japonya': 'japan', 'güney kore': 'south korea',
      'singapur': 'singapore', 'bae': 'uae', 'abd': 'usa',
      'yunanistan': 'greece', 'tayland': 'thailand', 'sırbistan': 'serbia',
      'belçika': 'belgium', 'macaristan': 'hungary', 'isviçre': 'switzerland',
      'irlanda': 'ireland', 'iskoçya': 'scotland', 'fas': 'morocco',
      'mısır': 'egypt', 'danimarka': 'denmark', 'karadağ': 'montenegro',
      'norveç': 'norway', 'bosna hersek': 'bosnia and herzegovina',
      'isveç': 'sweden', 'finlandiya': 'finland', 'arnavutluk': 'albania',
      'hırvatistan': 'croatia',
    };

    _cities = [];
    final rawCities = List<Map<String, dynamic>>.from(CitySwitcherScreen.allCities);
    for (var city in rawCities) {
      if (city["id"] == "undecided") continue;
      final cTr = (city["country"] ?? "").toString().toLowerCase().trim();
      final cEn = (city["country_en"] ?? "").toString().toLowerCase().trim();
      final masterKey = trToEnKey[cTr] ??
          (countryMaster.containsKey(cEn)
              ? cEn
              : (countryMaster.containsKey(cTr) ? cTr : null));
      if (masterKey != null) {
        final master = countryMaster[masterKey]!;
        city["country"] = master['tr'];
        city["country_en"] = master['en'];
        city["flag"] = master['flag'];
      }
      _cities.add(city);
    }

    _cities.sort((a, b) {
      final nameA = isEnglish ? (a["name_en"] ?? a["name"]) : a["name"];
      final nameB = isEnglish ? (b["name_en"] ?? b["name"]) : b["name"];
      return CitySwitcherScreen._compareStrings(nameA.toString(), nameB.toString());
    });

    final countryMap = <String, Map<String, String>>{};
    for (var city in _cities) {
      final key = city["country_en"].toString().toLowerCase().trim();
      if (!countryMap.containsKey(key)) {
        countryMap[key] = {
          "name": (city["country"] ?? '').toString(),
          "name_en": (city["country_en"] ?? '').toString(),
          "flag": (city["flag"] ?? '').toString(),
        };
      }
    }
    _countries = countryMap.values.toList();
    _countries.sort((a, b) {
      final nA = isEnglish ? a["name_en"]! : a["name"]!;
      final nB = isEnglish ? b["name_en"]! : b["name"]!;
      return CitySwitcherScreen._compareStrings(nA, nB);
    });

    // "Henüz karar vermedim" kartı listenin başında
    _cities.insert(0, {
      "id": "undecided",
      "name": "undecided_label",
      "name_en": "undecided_label",
      "country": "MyWay",
      "country_en": "MyWay",
      "flag": "🌍",
      "networkImage":
          "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800",
    });

    _loadSelectedCity();
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadSelectedCity() async {
    final prefs = await SharedPreferences.getInstance();
    final saved = prefs.getString("selectedCity") ?? "barcelona";
    if (!mounted) return;
    setState(() => _selectedCity = saved);
  }

  Future<void> _selectCity(String cityId) async {
    HapticFeedback.mediumImpact();
    final prefs = await SharedPreferences.getInstance();

    String finalCityId = cityId;
    if (cityId == "undecided") {
      // Kullanıcı "kararsızım" dedi → rastgele bir şehir seç ve sonra "öneri popup"unu tetikle.
      final candidates = CitySwitcherScreen.allCities
          .where((c) => c['id'] != null && c['id'] != 'undecided')
          .toList();
      if (candidates.isNotEmpty) {
        final randomCity =
            candidates[Random().nextInt(candidates.length)];
        finalCityId = randomCity['id'].toString();
      }
      await prefs.setBool("suggest_city_popup", true);
    } else {
      await prefs.setBool("suggest_city_popup", false);
    }

    await prefs.setString("selectedCity", finalCityId);
    TripUpdateService().notifyCityChanged();

    AnalyticsService.instance.logSelectContent(
      contentType: 'city',
      itemId: finalCityId,
    );

    Future.delayed(
      const Duration(milliseconds: 250),
      () => widget.onCitySelected(finalCityId),
    );
  }

  @override
  Widget build(BuildContext context) {
    final isEn = AppLocalizations.instance.isEnglish;
    final bottomPadding = MediaQuery.of(context).padding.bottom;

    return Material(
      color: _bgDark,
      child: SafeArea(
        bottom: false,
        child: Column(
          children: [
            // ── 1. Onboarding hoş geldin başlığı ──────────────────────────────
            Padding(
              padding: const EdgeInsets.fromLTRB(24, 16, 24, 12),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    isEn ? "Where to explore?" : "Nereyi keşfedeceksin?",
                    style: const TextStyle(
                      color: Colors.black,
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 6),
                  Text(
                    isEn
                        ? "Select a city to start your journey"
                        : "Yolculuğuna başlamak için bir şehir seç",
                    style: const TextStyle(color: _textGrey, fontSize: 16),
                  ),
                ],
              ),
            ),

            // ── 2. Akış başlığı + opsiyonel geri butonu ──────────────────────
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
              child: Row(
                children: [
                  if (_selectedCountry != null && _searchQuery.isEmpty)
                    GestureDetector(
                      onTap: () => setState(() => _selectedCountry = null),
                      child: Container(
                        padding: const EdgeInsets.all(8),
                        margin: const EdgeInsets.only(right: 12),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.05),
                          borderRadius: BorderRadius.circular(10),
                        ),
                        child: const Icon(Icons.arrow_back_rounded,
                            color: Colors.black, size: 20),
                      ),
                    ),
                  Expanded(
                    child: Text(
                      _searchQuery.isNotEmpty
                          ? (isEn ? "Search Results" : "Arama Sonuçları")
                          : (_selectedCountry == null
                              ? (isEn ? "Select Country" : "Ülke Seç")
                              : (isEn ? "Select City" : "Şehir Seç")),
                      style: const TextStyle(
                        color: Colors.black,
                        fontSize: 20,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ),
                ],
              ),
            ),

            // ── 3. Arama kutusu ──────────────────────────────────────────────
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                decoration: BoxDecoration(
                  color: _bgCard,
                  borderRadius: BorderRadius.circular(16),
                  border: Border.all(color: Colors.black.withOpacity(0.06)),
                ),
                child: TextField(
                  controller: _searchController,
                  onChanged: (value) =>
                      setState(() => _searchQuery = value),
                  style: const TextStyle(color: Colors.black, fontSize: 16),
                  decoration: InputDecoration(
                    hintText: isEn
                        ? "Search city or country..."
                        : "Şehir veya ülke ara...",
                    hintStyle: const TextStyle(color: _textGrey, fontSize: 15),
                    border: InputBorder.none,
                    icon: const Icon(Icons.search_rounded,
                        color: _textGrey, size: 20),
                    suffixIcon: _searchQuery.isNotEmpty
                        ? IconButton(
                            icon: const Icon(Icons.close_rounded,
                                color: _textGrey, size: 20),
                            onPressed: () {
                              _searchController.clear();
                              setState(() => _searchQuery = "");
                            },
                          )
                        : null,
                  ),
                ),
              ),
            ),

            // ── 4. Liste (ülke / şehir / arama) ──────────────────────────────
            Expanded(
              child: Builder(
                builder: (context) {
                  if (_searchQuery.isNotEmpty) {
                    final query = _searchQuery.toLowerCase();
                    final filteredCities = _cities.where((city) {
                      if (city["id"] == "undecided") return false;
                      final name = (isEn
                              ? (city["name_en"] ?? city["name"])
                              : city["name"])
                          .toString()
                          .toLowerCase();
                      final country = (isEn
                              ? (city["country_en"] ?? city["country"])
                              : city["country"])
                          .toString()
                          .toLowerCase();
                      return name.contains(query) ||
                          country.contains(query);
                    }).toList();
                    if (filteredCities.isEmpty) return _buildEmptyState();
                    return ListView.builder(
                      padding: EdgeInsets.fromLTRB(
                          16, 4, 16, bottomPadding + 24),
                      itemCount: filteredCities.length,
                      itemBuilder: (context, index) => _buildCityTile(
                        filteredCities[index],
                        filteredCities[index]["id"] == _selectedCity,
                      ),
                    );
                  }

                  if (_selectedCountry == null) {
                    return ListView.builder(
                      key: const PageStorageKey('onb_country_list'),
                      padding: EdgeInsets.fromLTRB(
                          16, 4, 16, bottomPadding + 24),
                      itemCount: _countries.length + 1,
                      itemBuilder: (context, index) {
                        if (index == 0) {
                          return _buildCityTile(
                              _cities[0], _selectedCity == "undecided");
                        }
                        return _buildCountryTile(_countries[index - 1]);
                      },
                    );
                  }

                  final countryCities = _cities
                      .where((c) =>
                          c["country_en"] == _selectedCountry &&
                          c["id"] != "undecided")
                      .toList();
                  return ListView.builder(
                    padding: EdgeInsets.fromLTRB(
                        16, 4, 16, bottomPadding + 24),
                    itemCount: countryCities.length,
                    itemBuilder: (context, index) => _buildCityTile(
                      countryCities[index],
                      countryCities[index]["id"] == _selectedCity,
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

  Widget _buildCountryTile(Map<String, String> country) {
    final isEn = AppLocalizations.instance.isEnglish;
    final name = isEn ? country["name_en"]! : country["name"]!;
    return GestureDetector(
      onTap: () => setState(() => _selectedCountry = country["name_en"]),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 18),
        decoration: BoxDecoration(
          color: _bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.black.withOpacity(0.06)),
        ),
        child: Row(
          children: [
            Text(country["flag"]!, style: const TextStyle(fontSize: 24)),
            const SizedBox(width: 16),
            Expanded(
              child: Text(
                name,
                style: const TextStyle(
                  color: Colors.black,
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
            const Icon(Icons.chevron_right_rounded, color: _textGrey),
          ],
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(Icons.location_off, color: _textGrey, size: 48),
          const SizedBox(height: 12),
          Text(
            AppLocalizations.instance.cityNotFoundMessage,
            style: const TextStyle(color: _textGrey, fontSize: 16),
          ),
        ],
      ),
    );
  }

  Widget _buildCityTile(Map<String, dynamic> city, bool isSelected) {
    final isEn = AppLocalizations.instance.isEnglish;
    return GestureDetector(
      onTap: () => _selectCity(city["id"]),
      child: Container(
        margin: const EdgeInsets.only(bottom: 10),
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: isSelected ? _accent.withOpacity(0.05) : _bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isSelected ? _accent : Colors.black.withOpacity(0.06),
            width: isSelected ? 2 : 1,
          ),
        ),
        child: Row(
          children: [
            ClipRRect(
              borderRadius: BorderRadius.circular(12),
              child: SizedBox(
                width: 56,
                height: 56,
                child: ResilientNetworkImage(
                  imageUrl: city["networkImage"] as String?,
                  placeName: (city["name"] ?? city["id"]).toString(),
                  city: city["id"].toString(),
                  category: 'city',
                  width: 56,
                  height: 56,
                  fit: BoxFit.cover,
                  placeholderBuilder: (_) => Container(
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        colors: [
                          _accent.withOpacity(0.15),
                          _accent.withOpacity(0.05),
                        ],
                      ),
                    ),
                    child: Center(
                      child: Text(
                        (city["flag"] ?? '🌍').toString(),
                        style: const TextStyle(fontSize: 24),
                      ),
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    city["id"] == "undecided"
                        ? AppLocalizations.instance.undecidedCity
                        : (isEn && city["name_en"] != null
                            ? city["name_en"]
                            : city["name"]),
                    style: TextStyle(
                      color: isSelected ? _accent : Colors.black,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    city["id"] == "undecided"
                        ? AppLocalizations.instance.ourSuggestion
                        : (isEn ? city["country_en"] : city["country"]),
                    style: TextStyle(
                      color: Colors.black.withOpacity(0.55),
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),
            if (isSelected)
              Container(
                width: 24,
                height: 24,
                decoration: const BoxDecoration(
                  color: _accent,
                  shape: BoxShape.circle,
                ),
                child: const Icon(Icons.check_rounded,
                    color: Colors.white, size: 16),
              )
            else
              Container(
                width: 24,
                height: 24,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  border: Border.all(
                      color: Colors.black.withOpacity(0.1), width: 2),
                ),
              ),
          ],
        ),
      ),
    );
  }
}
