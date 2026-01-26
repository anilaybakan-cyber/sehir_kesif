// =============================================================================
// APP LOCALIZATIONS - TR/EN DİL DESTEĞİ
// =============================================================================

import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'dart:io';

// Desteklenen diller
enum AppLanguage { tr, en }

class AppLocalizations {
  final AppLanguage language;
  
  AppLocalizations(this.language);

  // Singleton pattern for global access
  static AppLocalizations? _instance;
  static AppLanguage _currentLanguage = AppLanguage.tr;
  
  static AppLocalizations get instance {
    _instance ??= AppLocalizations(_currentLanguage);
    return _instance!;
  }

  static AppLanguage get currentLanguage => _currentLanguage;

  static Future<void> setLanguage(AppLanguage lang) async {
    _currentLanguage = lang;
    _instance = AppLocalizations(lang);
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString('app_language', lang.name);
  }

  static Future<void> loadSavedLanguage() async {
    final prefs = await SharedPreferences.getInstance();
    final savedLang = prefs.getString('app_language');
    
    if (savedLang != null) {
      // Kayıtlı tercih varsa onu kullan
      if (savedLang == 'en') {
        _currentLanguage = AppLanguage.en;
      } else {
        _currentLanguage = AppLanguage.tr;
      }
    } else {
      // Kayıtlı tercih yoksa cihaz diline bak
      try {
        // Platform.localeName returns 'en_US', 'tr_TR', etc.
        final String deviceLocale = Platform.localeName;
        if (deviceLocale.toLowerCase().startsWith('tr')) {
          _currentLanguage = AppLanguage.tr;
        } else {
          _currentLanguage = AppLanguage.en;
        }
      } catch (e) {
        // Hata durumunda (web vs.) varsayılan İngilizce olsun
        _currentLanguage = AppLanguage.en;
      }
    }
    _instance = AppLocalizations(_currentLanguage);
  }

  // Kısayol
  static AppLocalizations of(BuildContext context) => instance;

  // Helper method for translations
  String t(String tr, String en) {
    return language == AppLanguage.tr ? tr : en;
  }

  // Dil kontrolü
  bool get isEnglish => language == AppLanguage.en;
  bool get isTurkish => language == AppLanguage.tr;

  // ═══════════════════════════════════════════════════════════════════════════
  // GENEL
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get appName => t('MyWay', 'MyWay');
  String get loading => t('Yükleniyor...', 'Loading...');
  String get save => t('Kaydet', 'Save');
  String get confirm => t('Onayla', 'Confirm');
  String get cancel => t('İptal', 'Cancel');
  String get close => t('Kapat', 'Close');
  String get delete => t('Sil', 'Delete');
  String get edit => t('Düzenle', 'Edit');
  String get change => t('Değiştir', 'Change');
  String get continueText => t('Devam Et', 'Continue');
  String get done => t('Tamam', 'Done');

  // ═══════════════════════════════════════════════════════════════════════════
  // BOTTOM NAV BAR
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get navExplore =>
      isEnglish ? "Explore" : "Keşfet";
  String get navNearby =>
      isEnglish ? "Nearby" : "Yakınımda";
  String get navRoutes =>
      isEnglish ? "Routes" : "Rotalar";
  String get navGuide =>
      isEnglish ? "Guide" : "Rehber";
  String get navProfile =>
      isEnglish ? "Profile" : "Profil";

  // ═══════════════════════════════════════════════════════════════════════════
  // EXPLORE SCREEN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get exploreTitle => t('Keşfet', 'Explore');
  String get exploreSubtitle => t('Şehrin en iyilerini keşfet', 'Discover the best of the city');
  String get popularPlaces => t('Popüler Mekanlar', 'Popular Places');
  String get seeAll => t('Tümünü Gör', 'See All');
  String get recommendations => t('Sana Özel', 'For You');
  String get categories => t('Kategoriler', 'Categories');

  // ═══════════════════════════════════════════════════════════════════════════
  // NEARBY SCREEN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get nearbyTitle => t('Yakınımda', 'Nearby');
  String get searchPlaces => t('Mekan ara...', 'Search places...');
  String get allCategories => t('Tümü', 'All');
  String get restaurant => t('Restoran', 'Restaurant');
  String get cafe => t('Kafe', 'Cafe');
  String get bar => t('Bar', 'Bar');
  String get museum => t('Müze', 'Museum');
  String get park => t('Park', 'Park');
  String get historical => t('Tarihi', 'Historical');
  String get viewpoint => t('Manzara', 'Viewpoint');
  String get experience => t('Deneyim', 'Experience');
  String get shopping => t('Alışveriş', 'Shopping');
  String get beach => t('Plaj', 'Beach');
  String get pub => t('Pub', 'Pub');
  String get neighborhood => t('Mahalle', 'Neighborhood');
  String get noPlacesFound => t('Mekan bulunamadı', 'No places found');

  // ═══════════════════════════════════════════════════════════════════════════
  // ROUTES SCREEN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get myRoute => t('Rotam', 'My Route');
  String get day => t('Gün', 'Day');
  String get suggestedRoutes => t('Hazır Rotalar', 'Suggested Routes');
  String get emptyRoute => t('Henüz rota oluşturmadın', 'You haven\'t created a route yet');
  String get emptyRouteHint => t('Keşfet\'ten mekan ekleyerek başla', 'Start by adding places from Explore');
  String get addToRoute => t('Rotaya Ekle', 'Add to Route');
  String get addedToRoute => t('Rotada', 'In Route');
  String get removeFromRoute => t('Rotadan Çıkar', 'Remove from Route');
  String get selectDay => t('Gün Seç', 'Select Day');
  String get applyRoute => t('Rota Oluştur', 'Create Route');
  String get applied => t('Uygulandı', 'Applied');
  String get places => t('mekan', 'places');

  // ═══════════════════════════════════════════════════════════════════════════
  // PROFILE SCREEN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get profile => t('Profil', 'Profile');
  String get favorites => t('Favoriler', 'Favorites');
  String get visited => t('Ziyaret', 'Visited');
  String get noFavorites => t('Henüz favori yok', 'No favorites yet');
  String get noVisited => t('Henüz ziyaret yok', 'No visits yet');
  String get quickAccess => t('Hızlı Erişim', 'Quick Access');
  String get changeCity => t('Şehir Değiştir', 'Change City');
  String get editPreferences => t('Tercihlerimi Düzenle', 'Edit Preferences');
  String get settings => t('Ayarlar', 'Settings');
  String get travelStyle => t('Seyahat Tarzı', 'Travel Style');
  String get interests => t('İlgi Alanları', 'Interests');
  String get editName => t('İsim Değiştir', 'Edit Name');

  String get languageLabel => t('Dil', 'Language');
  String get turkish => t('Türkçe', 'Turkish');
  String get english => t('İngilizce', 'English');

  // ═══════════════════════════════════════════════════════════════════════════
  // DETAIL SCREEN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get about => t('Hakkında', 'About');
  String get tips => t('İpuçları', 'Tips');
  String get openingHours => t('Çalışma Saatleri', 'Opening Hours');
  String get location => t('Konum', 'Location');
  String get distance => t('Mesafe', 'Distance');
  String get getDirections => t('Yol Tarifi', 'Get Directions');
  String get share => t('Paylaş', 'Share');
  String get imHere => t('Buradayım', 'I\'m Here');
  String get visitedCheck => t('Ziyaret Edildi', 'Visited');

  // ═══════════════════════════════════════════════════════════════════════════
  // CITY SWITCHER
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get selectCity => t('Şehir Seç', 'Select City');
  String get searchCity => t('Şehir ara...', 'Search city...');
  String get cityNotFound => t('Şehir bulunamadı', 'City not found');

  // ═══════════════════════════════════════════════════════════════════════════
  // ONBOARDING
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get welcome => t('Hoş Geldin!', 'Welcome!');
  String get howManyDays => t('Kaç Gün Kalacaksın?', 'How long is your trip?');
  String get yourTravelStyle => t('Seyahat Tarzın', 'Your Travel Style');
  String get transportPreference => t('Ulaşım Tercihi', 'Transport Preference');
  String get yourInterests => t('İlgi Alanların', 'Your Interests');
  String get budgetPreference => t('Bütçe Tercihi', 'Budget Preference');
  String get letsStart => t('Başlayalım!', 'Let\'s Start!');
  String get next => t('İleri', 'Next');
  String get back => t('Geri', 'Back');

  // Travel Styles
  String get styleTourist => t('Turistik', 'Tourist');
  String get styleLocal => t('Lokal', 'Local');
  String get styleAdventurer => t('Maceracı', 'Adventurer');
  String get styleCultural => t('Kültürel', 'Cultural');

  // Transport
  String get walking => t('Yürüyerek', 'Walking');
  String get publicTransport => t('Toplu taşıma', 'Public Transport');
  String get byCar => t('Araçla', 'By Car');
  String get mixed => t('Karışık', 'Mixed');

  // Budget
  String get budgetEconomy => t('Ekonomik', 'Budget');
  String get budgetBalanced => t('Dengeli', 'Balanced');
  String get budgetPremium => t('Premium', 'Premium');

  // Onboarding Subtitles
  String get travelStyleSubtitle => t('Sana özel rotalar oluşturalım', 'Let\'s create custom routes for you');
  String get transportSubtitle => t('Rotaları buna göre optimize edelim', 'We\'ll optimize routes accordingly');
  String get budgetSubtitle => t('Önerileri buna göre filtreleyeceğiz', 'We\'ll filter recommendations accordingly');

  // Budget Descriptions
  String get budgetFriendly => t('Bütçe dostu', 'Budget friendly');
  String get pricePerformance => t('Fiyat/performans', 'Price/performance');
  String get bestExperience => t('En iyi deneyim', 'Best experience');

  // Walking Capacity
  String get walkingCapacity => t('Yürüme kapasiten', 'Walking capacity');

  // Explore Screen
  String get recommendationsReady => t('Öneriler Hazır', 'Recommendations Ready');
  String get tapToSeeAgain => t('Tekrar görmek için dokun', 'Tap to see again');
  String searchInCity(String city) => t('$city içinde ara...', 'Search in $city...');
  String askAboutCity(String city) => t('$city hakkında sor', 'Ask about $city');
  String get quickQuestions => t('Hızlı Sorular', 'Quick Questions');
  String get sunsetWhere => t('Gün batımı için neresi?', 'Where for sunset?');
  String get dataLoadError => t('Veri yüklenemedi', 'Could not load data');
  String preparingRecommendations(String city, int days) => 
      t('İlgi alanlarına göre sana özel öneriler oluşturmaya hazır mısın?', 'Are you ready to create personalized suggestions based on your interests?');
  String get preparingForYou => t('Sana özel öneriler hazırlanıyor...', 'Preparing recommendations for you...');
  String get basedOnInterests => t('İlgi alanlarınıza', 'Based on your interests');

  // Day Dialog
  String get whichDay => t('Hangi Güne Eklensin?', 'Which Day?');
  String dayN(int n) => t('Gün $n', 'Day $n');
  String get createNewDay => t('Yeni Gün Oluştur', 'Create New Day');
  String addToRouteConfirmDialog(String name) => t("'$name' rotaya eklensin mi?", "Add '$name' to route?");
  String nPlaces(int n) => t('$n mekan var', '$n places');
  String whichDayPlan(String name) => t("'$name' rotasını hangi gün planına dahil etmek istersiniz?", "Which day would you like to add '$name' route?");
  String removedFromRoute(String name) => t('$name rotadan çıkarıldı.', '$name removed from route.');
  String addedToDay(String name, int day) => t('$name, $day. güne eklendi!', '$name added to day $day!');
  String routeAddedToDay(String name, int day) => t('${name}, ${day}. güne eklendi!', '${name} added to day $day!');
  String get viewButton => t('Görüntüle', 'View');
  String addToRouteConfirm(String name) => t('\'$name\' rotaya eklensin mi?', 'Add \'$name\' to route?');
  String get tryAgain => t('Tekrar Dene', 'Try Again');

  // Routes
  String nStops(int n) => t('$n durak', '$n stops');
  String stopsOpenMaps(int n) => t('$n durak • Google Maps\'te aç', '$n stops • Open in Google Maps');
  String get localTip => t('Lokal İpucu 💡', 'Local Tip 💡');

  // Discover Nearby
  String get discoverNearby => t('Yakınlarda Keşfet', 'Discover Nearby');
  String get walkingTour => t('Yürüyüş Turu', 'Walking Tour');
  String get gastronomy => t('Gastronomi', 'Gastronomy');
  String get photoSpots => t('Fotoğraf Noktaları', 'Photo Spots');

  // ═══════════════════════════════════════════════════════════════════════════
  // CHECK-IN
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get checkInSuccess => t('Harika!', 'Awesome!');
  String get placeVisited => t('ziyaret edildi!', 'visited!');
  String totalDiscovered(int count) => t('Toplam $count yer keşfettin!', 'You discovered $count places!');
  String get continueButton => t('Devam Et', 'Continue');
  String get totalExplored => t('Toplam keşfettin', 'Total explored');
  // Duplicates removed (moved to bottom)

  // ═══════════════════════════════════════════════════════════════════════════
  // PREFERENCES BOTTOM SHEET
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get preferencesTitle => t('Tercihler', 'Preferences');
  String get preferencesSaved => t('Tercihler kaydedildi!', 'Preferences saved!');
  String get walkingLight => t('Hafif', 'Light');
  String get walkingNormal => t('Normal', 'Normal');
  String get walkingActive => t('Aktif', 'Active');
  String get walkingAthlete => t('Sporcu', 'Athlete');

  // ═══════════════════════════════════════════════════════════════════════════
  // MESAJLAR
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get addedToRouteMessage => t('Rotaya eklendi!', 'Added to route!');
  String get removedFromRouteMessage => t('Rotadan çıkarıldı', 'Removed from route');
  String get addedToFavorites => t('Favorilere eklendi', 'Added to favorites');
  String get removedFromFavorites => t('Favorilerden çıkarıldı', 'Removed from favorites');

  // ═══════════════════════════════════════════════════════════════════════════
  // HELPER
  // ═══════════════════════════════════════════════════════════════════════════
  
  // Rota Zorlukları
  String get difficultyEasy => t('Kolay', 'Easy');
  String get difficultyMedium => t('Orta', 'Medium');
  String get difficultyHard => t('Zor', 'Hard');

  // Özel Rotalar
  String gothicRouteTitle(String city) => t('Gotik & Gizem', 'Gothic & Mystery');
  String get gothicRouteDesc => t('Dar sokaklar, tarihi katedraller ve arada gizli kahve molaları.', 'Narrow streets, historic cathedrals and hidden coffee breaks.');
  
  String artBornRouteTitle(String city) => t('Sanat & Lezzet (El Born)', 'Art & Flavor (El Born)');
  String get artBornRouteDesc => t('Müzelerle dolu bir sabahın ardından parkta dinlenme ve tapas keyfi.', 'A morning full of museums followed by park relaxation and tapas.');
  
  String gaudiRouteTitle(String city) => t('Gaudí ve Modernizm', 'Gaudí & Modernism');
  String get gaudiRouteDesc => t('Eixample\'ın şık caddelerinde mimari bir şölen ve lüks mağazalar.', 'An architectural feast and luxury shops on the stylish streets of Eixample.');
  
  String seasideRouteTitle(String city) => t('Deniz & Plaj Keyfi', 'Sea & Beach Joy');
  String get seasideRouteDesc => t('Barceloneta sahilinde yürüyüş, deniz ürünleri ve gün batımı.', 'Walking on Barceloneta beach, seafood and sunset.');

  String localFlavorRouteTitle(String city) => t('$city Lezzet Durakları', '$city Culinary Stops');
  String get localFlavorRouteDesc => t('Şehrin en iyi tapas barları ve yerel lezzetleri.', 'The city\'s best tapas bars and local delicacies.');
  
  String hiddenGemsRouteTitle(String city) => t('Gizli Hazineler', 'Hidden Gems');
  String get hiddenGemsRouteDesc => t('Turistlerden uzakta, şehrin yerel yüzünü keşfedin.', 'Discover the local side of the city, away from tourists.');

  // Rota İsimleri ve Açıklamaları (Klasik)
  String classicRouteTitle(String city) => t('Klasik $city Turu', 'Classic $city Tour');
  String get classicRouteDesc => t('Şehrin en ikonik noktalarını keşfedin. İlk kez gelenler için ideal.', 'Discover the city\'s most iconic spots. Ideal for first-timers.');
  
  String photogenicRouteTitle(String city) => t('Fotojenik $city', 'Photogenic $city');
  String get photogenicRouteDesc => t('Instagram için en güzel kareleri yakalayabileceğiniz noktalar.', 'Best spots to capture Instagram-worthy shots.');

  String hours(dynamic h) => t('$h saat', '$h hours');
  String km(dynamic k) => t('$k km', '$k km');

  // Durak
  String get stop => t('Durak', 'Stop');
  String stopNumber(int number) => t('$number. DURAK', 'STOP $number');

  // Ayarlar Ekranı
  String get storageData => t('Depolama & Veri', 'Storage & Data');
  String get cityContent => t('Şehir İçerikleri', 'City Content');
  String get general => t('Genel', 'General');
  String get connectionStatus => t('Bağlantı Durumu', 'Connection Status');
  String get offlineModeDesc => t('İnternet bağlantısı olmadan kaydedilen şehirleri gezmenizi sağlar.', 'Allows browsing saved cities without internet connection.');
  String get highQualityPhotos => t('Yüksek Kalite Fotoğraflar', 'High Quality Photos');
  String get highQualityPhotosDesc => t('Veri tasarrufu için kapatın.', 'Turn off to save data.');
  String get autoDownload => t('Otomatik İndirme', 'Auto Download');
  String get autoDownloadDesc => t('Favori şehirleri otomatik güncelle.', 'Automatically update favorite cities.');
  String get cacheSize => t('Önbellek Boyutu', 'Cache Size');
  String get lastSync => t('Son Senkronizasyon', 'Last Sync');
  String get clearData => t('Verileri Temizle', 'Clear Data');
  String get clearCacheAction => t('Önbelleği Boşalt', 'Clear Cache');
  String get cacheCleared => t('Önbellek temizlendi', 'Cache cleared');
  String get connected => t('Bağlandı', 'Connected');
  String get noConnection => t('Bağlantı Yok', 'No Connection');
  String get online => t('Çevrimiçi', 'Online');
  String get offline => t('Çevrimdışı', 'Offline');
  String get selectCitiesToDownload => t('İndirilecek Şehirleri Seç', 'Select Cities to Download');
  String get download => t('İndir', 'Download');
  String get downloading => t('İndiriliyor...', 'Downloading...');
  String get downloaded => t('İndirildi', 'Downloaded');

  String get downloadSelected => t('Seçilenleri İndir', 'Download Selected');
  String get citiesDownloading => t('Şehirler indiriliyor...', 'Downloading cities...');

  
  // Onboarding
  String get skip => t('Atla', 'Skip');
  String get continueAction => t('Devam Et', 'Continue');
  String get finish => t('Tamamla', 'Finish');
  String get startExplore => t('Keşfetmeye Başla', 'Start Exploring');

  String get helloGreeting => t('Merhaba! 👋', 'Hello! 👋');
  String get howToCallYou => t('Sana nasıl hitap edelim?', 'How should we call you?');
  String get nameHint => t('İsminiz', 'Your Name');

  String get exactlyHowManyDays => t('Tam olarak kaç gün?', 'Exactly how many days?');
  String nDays(int n) => t('$n gün', '$n days');
  String get days => t('Gün', 'Days');

  String get readyRoutes => t('hazır rota', 'ready routes');
  String get selectedSpotsLabel => t('seçili nokta', 'selected spots');

  // UI Elements (NEW - no duplicates)
  String get hide => t('Gizle', 'Hide');
  String get show => t('Göster', 'Show');
  String get free => t('Ücretsiz', 'Free');
  String get features => t('Özellikler', 'Features');
  String get city => t('Şehir', 'City');

  // Moods (NEW - no duplicates)
  String get moodCalm => t('Sakin', 'Calm');
  String get moodExplore => t('Keşif', 'Explore');
  String get moodPopular => t('Popüler', 'Popular');

  // Transport Modes (NEW - no duplicates)
  String get transportWalking => t('Yürüyerek', 'Walking');
  String get transportPublic => t('Toplu taşıma', 'Public Transport');
  String get transportCar => t('Araçla', 'By Car');
  String get transportMixed => t('Karışık', 'Mixed');

  // User Levels (NEW - no duplicates)
  String get levelExplorer => t('Kaşif', 'Explorer');
  String get levelCurious => t('Meraklı', 'Curious');
  String get levelBeginner => t('Yeni Başlayan', 'Beginner');

  // Interests - only new ones not already defined
  String get interestCoffee => t('Kahve', 'Coffee');
  String get interestNight => t('Gece', 'Nightlife');
  String get interestPhoto => t('Fotoğraf', 'Photography');
  String get interestBeach => t('Plaj', 'Beach');
  String get interestLocalFood => t('Yerel Lezzetler', 'Local Cuisine');

  // Price Levels
  String get priceAffordable => t('Uygun', 'Affordable');
  String get priceMedium => t('Orta', 'Medium');
  String get priceExpensive => t('Pahalı', 'Expensive');
  String get priceLuxury => t('Lüks', 'Luxury');

  // Traveler Levels
  String get levelExpert => t('Uzman Gezgin', 'Expert Traveler');
  String get levelExperienced => t('Deneyimli', 'Experienced');

  // Section Titles
  String get travelStyleTitle => t('Seyahat Tarzı', 'Travel Style');
  String translateTravelStyle(String style) {
    if (language == AppLanguage.tr) return style;
    switch (style) {
      case 'Turistik': return 'Tourist';
      case 'Yerel': 
      case 'Lokal': return 'Local';
      case 'Maceracı': return 'Adventurer';
      case 'Kültürel': return 'Cultural';
      default: return style;
    }
  }

  String get interestsTitle => t('İlgi Alanları', 'Interests');



  // Transport Mode Translation
  String translateTransportMode(String mode) {
    switch(mode) {
      case 'Yürüyerek': return t('Yürüyerek', 'Walking');
      case 'Toplu taşıma': return t('Toplu taşıma', 'Public Transport');
      case 'Araçla': return t('Araçla', 'By Car');
      case 'Karışık': return t('Karışık', 'Mixed');
      default: return mode;
    }
  }

  // Interest Translation (used in profile preferences)
  String translateInterest(String interest) {
    switch(interest) {
      case 'Yemek': return t('Yemek', 'Food');
      case 'Kahve': return t('Kahve', 'Coffee');
      case 'Sanat': return t('Sanat', 'Art');
      case 'Tarih': return t('Tarih', 'History');
      case 'Doğa': return t('Doğa', 'Nature');
      case 'Gece Hayatı': return t('Gece Hayatı', 'Nightlife');
      case 'Gece': return t('Gece', 'Nightlife');
      case 'Alışveriş': return t('Alışveriş', 'Shopping');
      case 'Fotoğraf': return t('Fotoğraf', 'Photography');
      case 'Mimari': return t('Mimari', 'Architecture');
      case 'Plaj': return t('Plaj', 'Beach');
      case 'Spor': return t('Spor', 'Sports');
      case 'Müze': return t('Müze', 'Museum');
      case 'Müzik': return t('Müzik', 'Music');
      case 'Yerel Lezzetler': return t('Yerel Lezzetler', 'Local Cuisine');
      default: return interest;
    }
  }

  // Feature Translation (used in place details)
  String translateFeature(String feature) {
    switch(feature) {
      case 'WiFi': return 'WiFi';
      case 'Açık Alan': return t('Açık Alan', 'Outdoor Area');
      case 'Teras': return t('Teras', 'Terrace');
      case 'Otopark': return t('Otopark', 'Parking');
      case 'Engelli Erişimi': return t('Engelli Erişimi', 'Wheelchair Access');
      case 'Çocuk Dostu': return t('Çocuk Dostu', 'Kid Friendly');
      case 'Evcil Hayvan': return t('Evcil Hayvan', 'Pet Friendly');
      case 'Rezervasyon': return t('Rezervasyon', 'Reservation');
      case 'Kredi Kartı': return t('Kredi Kartı', 'Credit Card');
      case 'Ücretsiz Giriş': return t('Ücretsiz Giriş', 'Free Entry');
      case 'Sesli Rehber': return t('Sesli Rehber', 'Audio Guide');
      case 'Rehberli Tur': return t('Rehberli Tur', 'Guided Tour');
      case 'Hediyelik Mağaza': return t('Hediyelik Mağaza', 'Gift Shop');
      case 'Kafe': return t('Kafe', 'Café');
      case 'Restoran': return t('Restoran', 'Restaurant');
      case 'Manzara': return t('Manzara', 'View');
      case 'Fotoğraf Noktası': return t('Fotoğraf Noktası', 'Photo Spot');
      case 'Gün Batımı': return t('Gün Batımı', 'Sunset View');
      case 'Tarihi': return t('Tarihi', 'Historical');
      case 'Mimari': return t('Mimari', 'Architecture');
      case 'Ücretsiz WiFi': return t('Ücretsiz WiFi', 'Free WiFi');
      case 'Canlı Müzik': return t('Canlı Müzik', 'Live Music');
      case 'Happy Hour': return 'Happy Hour';
      case 'Kokteyl': return t('Kokteyl', 'Cocktails');
      case 'Vejetaryen': return t('Vejetaryen', 'Vegetarian');
      case 'Vegan': return 'Vegan';
      case 'Glutensiz': return t('Glutensiz', 'Gluten Free');
      case 'gizli': return t('gizli', 'hidden');
      case 'tarihi': return t('tarihi', 'historical');
      case 'huzurlu': return t('huzurlu', 'peaceful');
      case 'sakin': return t('sakin', 'quiet');
      case 'popüler': return t('popüler', 'popular');
      case 'romantik': return t('romantik', 'romantic');
      case 'doğal': return t('doğal', 'natural');
      case 'yerel': return t('yerel', 'local');
      case 'turistik': return t('turistik', 'touristic');
      case 'modern': return t('modern', 'modern');
      case 'geleneksel': return t('geleneksel', 'traditional');
      case 'lüks': return t('lüks', 'luxury');
      case 'bütçe dostu': return t('bütçe dostu', 'budget friendly');
      case 'aile': return t('aile', 'family');
      case 'çift': return t('çift', 'couple');
      case 'solo': return t('solo', 'solo');
      default: return feature;
    }
  }
  
  String get whereTo => t('Nereye gidiyoruz?', 'Where are we going?');
  String get selectCityDesc => t('Hangi şehri keşfetmek istersin?', 'Which city would you like to explore?');


  String get transportPref => t('Ulaşım Tercihi', 'Transport Preference');

  String get budget => t('Bütçe', 'Budget');

  String get balanced => t('Dengeli', 'Balanced');
  String get relaxed => t('Rahat', 'Relaxed');
  String get packed => t('Yoğun', 'Packed');
  
  String get walk => t('Yürüyüş', 'Walking');

  String get taxi => t('Taksi / Araç', 'Taxi / Car');
  
  String get economy => t('Ekonomik', 'Economy');
  String get luxury => t('Lüks', 'Luxury');
  String get lowBudget => t('Düşük Bütçe', 'Low Budget');
  String get highBudget => t('Yüksek Bütçe', 'High Budget');
  
  // Onboarding Interests
  String get interestHistory => t('Tarih & Kültür', 'History & Culture');
  String get interestFood => t('Yeme & İçme', 'Food & Drink');
  String get interestArt => t('Sanat & Müzeler', 'Art & Museums');
  String get interestNature => t('Doğa & Parklar', 'Nature & Parks');
  String get interestShopping => t('Alışveriş', 'Shopping');
  String get interestNightlife => t('Gece Hayatı', 'Nightlife');
  String get interestPhotography => t('Fotoğrafçılık', 'Photography');
  String get interestSports => t('Spor', 'Sports');
  String get interestArchitecture => t('Mimari', 'Architecture');
  String get interestMusic => t('Müzik', 'Music');

  // Step By Step
  String get nextStopLabel => t('Sonraki durak:', 'Next stop:');
  String get walkingTimeEstimate => t('Yürüme süresi tahmini: 6-12 dakika', 'Estimated walking time: 6-12 minutes');
  
  String montjuicRouteTitle(String city) => t('Zirveden Bakış', 'Peak View');
  String get montjuicRouteDesc => t('Montjuïc tepesinde panoramik manzaralar, müzeler ve yeşil bahçeler.', 'Panoramic views, museums and green gardens on Montjuïc hill.');
  
  String beachRouteTitle(String city) => t('Sahil & Keyif', 'Beach & Joy');
  String get beachRouteDesc => t('Güneş, kum ve deniz keyfini çıkarın.', 'Enjoy the sun, sand and sea.');
  
  // Formatlı string
  String dayNumber(int day) => t('$day. Gün', 'Day $day');
  String placesCount(int count) => t('$count mekan', '$count places');

  String get locationPermissionRequired => t('Konum izni gerekli', 'Location permission required');
  String get locationPermissionSettings => t('Konum izni ayarlardan açılmalı', 'Location permission must be enabled in settings');
  String tooFarAway(String distance) => t('Buraya $distance uzaklıktasın.\nDaha yaklaşınca tekrar dene!', 'You are $distance away.\nTry again when you get closer!');
  String get locationError => t('Konum alınamadı. GPS açık mı?', 'Could not get location. Is GPS on?');

  String distanceAway(String dist) => t('$dist uzaklıkta', '$dist away');

  // Explore Screen Extras
  String get popularSpots => t('Popüler Noktalar', 'Popular Spots');
  String get clear => t('Temizle', 'Clear');
  String get selectAll => t('Tümünü Seç', 'Select All');
  
  // Eksik Explore Strings
  String recommendationBasedOn(String interests) => t('$interests ilginize göre', 'Based on your $interests interests');
  
  // Eksik Nearby Strings
  String get basedOnCityCenter => t('Şehir merkezi baz alınıyor', 'Based on city center');
  String placesFound(int count) => t('$count yer bulundu', '$count places found');
  String get maxDistance => t('Maksimum Mesafe', 'Max Distance');
  
  // Eksik Routes Strings
  String cityRoutes(String city) => t('$city Rotaları', '$city Routes');
  String get dailyRouteMap => t('Günlük Rota Haritası', 'Daily Route Map'); // Added
  String get routeMap => t('Rota Haritası', 'Route Map'); // Added
  String get spots => t('Nokta', 'Spots'); // Added
  String get stops => t('Duraklar', 'Stops'); // Added
  String get bike => t('Bisiklet', 'Bike'); // Added
  String get car => t('Araç', 'Car'); // Added
  String get publicTransportShort => t('Toplu Taşıma', 'Public Transport'); // Added
  String get min => t('dk', 'min'); // Added
  String dayEmpty(int day) => t('Gün $day henüz boş', 'Day $day is empty yet'); // Added
  String routesCount(int count) => t('$count hazır rota', '$count curated routes');
  String selectedSpots(int count) => t('$count seçili nokta', '$count selected spots');
  String daysCount(int count) => t('$count gün', '$count days');
  String get tabAll => t('Tümü', 'All'); // Added missing key
  String get tabForYou => t('Sana Özel', 'For You');
  String get tabPopular => t('Popüler', 'Popular');
  String get details => t('Detaylar', 'Details');
  
  // Empty Route Screen
  String get emptyRouteTitle => t('Henüz rotanız boş', 'Your route is empty');
  String createRouteForTrip(int days) => t('$days günlük seyahatiniz için\nrotanızı oluşturun', 'Create your route for\nyour $days day trip');
  String get browseReadyRoutes => t('Hazır Rotalara Göz At', 'Browse Ready Routes');
  
  // Eksik Profile Strings
  String favoritesTab(int count) => t('Favoriler ($count)', 'Favorites ($count)');
  String visitedTab(int count) => t('Ziyaret ($count)', 'Visited ($count)');
  String get onRoute => t('Rotada', 'On Route'); // Added missing key
  String get createRoute => t('Rota Oluştur', 'Create Route');
  String get routeApplied => t('Rota Uygulandı', 'Route Applied');

  // ═══════════════════════════════════════════════════════════════════════════
  // KATEGORİ ÇEVİRİLERİ
  // ═══════════════════════════════════════════════════════════════════════════
  
  String translateCategory(String turkishCategory) {
    // Special handling for "Cafe" coming from JSON data
    if (turkishCategory == 'Cafe') {
      return t('Kafe', 'Cafe');
    }

    // 1. NORMALIZE: Map invalid/typo/bad-data categories to VALID Turkish categories first.
    // This ensures consistency in both TR and EN modes.
    String normalized = turkishCategory;
    final corrections = <String, String>{
      // "Görülmesi Gereken Yerler" is not a valid category -> Map to 'Deneyim'
      'Görülmesi Gereken Yerler': 'Deneyim',
      
      // User Requested Fixes (Mapped to valid TR keys)
      'Akvaryum': 'Deneyim',
      'Atıştırmalık': 'Yeme-İçme',
      'Atölye': 'Deneyim',
      'Eğitim': 'Tarihi',
      'Heyke': 'Tarihi',
      'Heykel': 'Tarihi',
      'Mağaza': 'Alışveriş',
      'Merkez': 'Deneyim',
      'Mimar': 'Tarihi',
      // 'Mimari' is valid ('Architecture') but user asked 'Mimar' -> 'Historical'. 
      // If 'Mimari' should also be 'Historical', add it here. Keeping 'Mimari' as is for now unless 'Mimar' was a typo for it.
      
      'Modern': 'Deneyim',
      'Neighborhood': 'Deneyim', // User said "Neighborhood olan Experience olacak"
      'Mahalle': 'Deneyim',      // Mapping Mahalle to Deneyim to be safe based on "Neighborhood" request
      'Pasaj': 'Deneyim',
      'Pazar': 'Deneyim',
      'Rahatlama': 'Deneyim',
      'Şarap': 'Yeme-İçme',
      'Saray': 'Tarihi',
      'Şehir': 'Deneyim',
      'Sokak': 'Deneyim',
      'Tarih': 'Tarihi', // 'Tarihi' is the valid key
      'Cafe': 'Kafe',    // Normalize Cafe to Kafe
    };

    if (corrections.containsKey(normalized)) {
      normalized = corrections[normalized]!;
    }

    // 2. TRANSLATE: If TR, return the normalized (valid) Turkish category.
    if (language == AppLanguage.tr) return normalized;
    
    // 3. ENGLISH MAPPING:
    final translations = {
      'Tümü': 'All',
      'Restoran': 'Restaurant',
      'Kafe': 'Cafe',
      'Bar': 'Bar',
      'Müze': 'Museum',
      'Park': 'Park',
      'Tarihi': 'Historical',
      'Manzara': 'Viewpoint',
      'Deneyim': 'Experience',
      'Alışveriş': 'Shopping',
      'Mahalle': 'Neighborhood', // Will be skipped if normalized to 'Deneyim' above
      'Semt': 'District',
      'Sakin': 'Calm',
      'Keşif': 'Discover',
      'Popüler': 'Popular',
      'Meydan': 'Square',
      'Fotoğraf': 'Photography',
      'Mimari': 'Architecture',
      'Spor': 'Sports',
      'Doğa': 'Nature',
      'Sanat': 'Art',
      'Gece Hayatı': 'Nightlife',
      'Yemek': 'Food',
      'Plaj': 'Beach',
      'Mistik': 'Mystic',
      'Yürüyüş': 'Walking',
      'Yeme-İçme': 'Food & Drink',
      'Gastronomi': 'Gastronomy',
      'Sokak Yemeği': 'Street Food',
      'Balık': 'Seafood',
      'Tatlı': 'Dessert',
      'Kokteyl Bar': 'Cocktail Bar',
      'Rooftop': 'Rooftop',
      'Kahve': 'Coffee',
      'Tapas': 'Tapas',
      'Köy': 'Village',
      'Kasaba': 'Town',
      'Bölge': 'Region',
      'Liman': 'Harbor',
      'Sağlık': 'Health',
      'Otel': 'Hotel',
    };
    return translations[turkishCategory] ?? turkishCategory;
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ÜLKE ÇEVİRİLERİ
  // ═══════════════════════════════════════════════════════════════════════════
  
  String translateCountry(String country) {
    if (language == AppLanguage.tr) return country;
    
    final translations = {
      'Türkiye': 'Turkey',
      'İspanya': 'Spain',
      'Fransa': 'France',
      'İtalya': 'Italy',
      'Hollanda': 'Netherlands',
      'İngiltere': 'England',
      'Almanya': 'Germany',
      'Avusturya': 'Austria',
      'Çekya': 'Czechia',
      'Portekiz': 'Portugal',
      'Japonya': 'Japan',
      'Güney Kore': 'South Korea',
      'Singapur': 'Singapore',
      'BAE': 'UAE',
      'ABD': 'USA',
    };
    return translations[country] ?? country;
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // EK ÇEVİRİLER
  // ═══════════════════════════════════════════════════════════════════════════
  
  // Şehir Seçimi
  String get cityNotFoundMessage => t('Şehir bulunamadı', 'City not found');
  String get undecidedCity => t('Henüz karar vermedim', 'I haven\'t decided yet');
  String get ourSuggestion => t('Senin İçin Önerimizi Gör', 'See Our Suggestion');
  String get undecidedSuggestionDesc => t('Kararsız mı kaldın? Şansına harika bir şehir seçtik:', 'Undecided? We picked a great city for your luck:');
  String get discoverNow => t('Hemen Keşfet', 'Discover Now');
  
  // AI Kartı
  String get aiRecommendations => t('Bugün Yönün Neresi?', 'Where is your direction today?');
  String get askAI => t('Öneri Oluştur', 'Create Suggestion');
  String get aiThinking => t('Düşünüyorum...', 'Thinking...');
  String placeNotFound(String query) => t("'$query' bulunamadı.", "'$query' not found.");
  
  // Rota Detayları
  String get routeDetail => t('Rota Detayı', 'Route Detail');
  String get routePlan => t('Rota Planı', 'Route Plan');
  String get startRoute => t('Rotayı Başlat', 'Start Route');
  String get finishRoute => t('Rotayı Bitir', 'Finish Route');
  String get nextStop => t('Sonraki Durağa Geç', 'Go to Next Stop');
  String get stepByStepRoute => t('Adım Adım Rota', 'Step by Step Route');
  String get currentStop => t('Şu anki durak:', 'Current stop:');
  String get noPlaceSelected => t('Mekan seçilmedi', 'No place selected');
  String get walkingEstimate => t('Yürüme süresi tahmini: 6-12 dakika', 'Estimated walking time: 6-12 min');
  String get calculating => t('Hesaplanıyor...', 'Calculating...');
  String get duration => t('Süre', 'Duration');
  String get price => t('Fiyat', 'Price');
  String get bestTime => t('En İyi Zaman', 'Best Time');
  String get anytime => t('Her zaman', 'Anytime');
  String get metro => t('Metro', 'Metro');
  
  // Ayarlar
  String get settingsTitle => t('Ayarlar', 'Settings');
  String get downloadCities => t('Şehirleri İndir', 'Download Cities');
  String get offlineMode => t('Çevrimdışı Mod', 'Offline Mode');
  String get clearCache => t('Önbelleği Temizle', 'Clear Cache');
  String get confirmClearCache => t('Tüm indirilen şehir verileri silinecek. Offline modda kullanılamayacaklar.\n\nDevam etmek istiyor musun?', 'All downloaded city data will be deleted. They won\'t be available offline.\n\nDo you want to continue?');
  
  // Gün seçim dialogu  
  String selectDayForPlace(String placeName) => t('$placeName için gün seç', 'Select day for $placeName');
  
  // Boş durumlar
  String get noRouteYet => t('Henüz rota oluşturmadın', 'No route created yet');
  String get startAddingPlaces => t('Keşfet\'ten mekan ekleyerek başla', 'Start by adding places from Explore');
  
  // Selamlaşma
  String get goodMorning => t('Günaydın', 'Good Morning');
  String get goodAfternoon => t('İyi Günler', 'Good Afternoon');
  String get goodEvening => t('İyi Akşamlar', 'Good Evening');
  
  // Favoriler
  String get addToFavorites => t('Favorilere Ekle', 'Add to Favorites');
  String get removeFromFavorites => t('Favorilerden Çıkar', 'Remove from Favorites');

  // ═══════════════════════════════════════════════════════════════════════════
  // AI CHAT PANEL
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get aiAssistant => t('My Way Asistan', 'My Way Assistant');
  String askAboutCityShort(String city) => t('$city hakkında sor', 'Ask about $city');
  String get helloAI => t('Merhaba! Ben My Way Asistanın.', 'Hello! I\'m your My Way Assistant.');
  String askAnythingAboutCity(String city) => t('$city hakkında her şeyi sorabilirsin!', 'Ask me anything about $city!');
  String get exampleQuestions => t('Örnek sorular:', 'Example questions:');
  String get askQuestion => t('Bir soru sor...', 'Ask a question...');
  String get bestCoffeeWhere => t('En iyi kahve nerede?', 'Where\'s the best coffee?');
  String get sunsetSpotWhere => t('Gün batımı için neresi?', 'Where for sunset?');
  String get localFoodWhere => t('Yerel lezzetler nereden yenir?', 'Where to eat local food?');
  String get quietParkSuggest => t('Sakin bir park önerir misin?', 'Can you suggest a quiet park?');
  String get aiErrorMessage => t('Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.', 'Sorry, an error occurred. Please try again.');
  
  // ═══════════════════════════════════════════════════════════════════════════
  // MOOD SECTION TITLES
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get peacefulCorners => t('Huzurlu Köşeler', 'Peaceful Corners');
  String get placesToExplore => t('Keşfedilecek Yerler', 'Places to Discover');
  String get cityRhythmFun => t('Şehrin Ritmi ve Eğlence', 'City Rhythm & Fun');
  
  // ═══════════════════════════════════════════════════════════════════════════
  // ONBOARDING MOOD SELECTOR
  // ═══════════════════════════════════════════════════════════════════════════
  
  String get tutorialCitySelectTitle => t('Şehir Seçimi', 'City Selection');
  String get tutorialCitySelectDesc => t('Buraya tıklayarak istediğin şehri seçebilir ve keşfetmeye başlayabilirsin.', 'You can select the city you want to explore by tapping here.');
  
  String get tutorialAiTitle => t('Kişisel Asistanın', 'Your Personal Assistant');
  String get tutorialAiDesc => t('Şehirle ilgili seçimlerine göre sana özel öneriler oluşturabilirsin.', 'You can create personalized suggestions based on your choices about the city.');

  String get tutorialAddRouteTitle => t('Rotanı Oluştur', 'Create Your Route');
  String get tutorialAddRouteDesc => t('Beğendiğin mekanları buradan rotana ekleyerek kendi planını yapabilirsin.', 'You can build your own plan by adding places you like to your route here.');

  
  String get moodLively => t('Canlı', 'Lively');
  String get moodDiscover => t('Keşfet', 'Discover');
  String walkToTarget(String from) => t('$from\'dan hedefe yürü', 'Walk from $from to target');
  String get onboardingTagline => t('Turist haritasını yak, gerçek şehri bul.', 'Burn the tourist map, find the real city.');
}
