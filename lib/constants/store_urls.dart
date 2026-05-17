import 'dart:io';

import 'package:url_launcher/url_launcher.dart';

/// App Store / Play Store — tek kaynak (applicationId ile eşleşmeli).
abstract final class StoreUrls {
  static const String iosAppStoreId = '6757671492';
  /// `android/app/build.gradle.kts` → applicationId
  static const String androidApplicationId = 'com.anilaybakan.sehirkesif';

  static Uri iosStoreHttps =
      Uri.parse('https://apps.apple.com/app/id$iosAppStoreId');
  static Uri iosStoreItms = Uri.parse(
    'itms-apps://itunes.apple.com/app/id$iosAppStoreId',
  );
  static Uri iosReviewItms = Uri.parse(
    'itms-apps://itunes.apple.com/app/id$iosAppStoreId?action=write-review',
  );
  static Uri iosReviewHttps = Uri.parse(
    'https://apps.apple.com/app/id$iosAppStoreId?action=write-review',
  );

  static Uri androidPlayHttps = Uri.parse(
    'https://play.google.com/store/apps/details?id=$androidApplicationId',
  );
  static Uri androidMarket = Uri.parse(
    'market://details?id=$androidApplicationId',
  );

  /// Mağaza uygulamasına veya tarayıcıya yönlendirerek uygulama sayfasını / yorum akışını açar.
  static Future<void> launchReviewPage() async {
    if (Platform.isIOS) {
      try {
        if (await canLaunchUrl(iosReviewItms)) {
          await launchUrl(iosReviewItms, mode: LaunchMode.externalApplication);
          return;
        }
      } catch (_) {}
      await launchUrl(iosReviewHttps, mode: LaunchMode.externalApplication);
      return;
    }

    try {
      if (await canLaunchUrl(androidMarket)) {
        await launchUrl(androidMarket, mode: LaunchMode.externalApplication);
        return;
      }
    } catch (_) {}
    await launchUrl(androidPlayHttps, mode: LaunchMode.externalApplication);
  }

  /// Mağaza uygulamasında app sayfasını (yorum değil, listing) açar.
  /// Güncelleme push'u gibi akışlarda kullanılır.
  static Future<void> launchStorePage() async {
    if (Platform.isIOS) {
      try {
        if (await canLaunchUrl(iosStoreItms)) {
          await launchUrl(iosStoreItms, mode: LaunchMode.externalApplication);
          return;
        }
      } catch (_) {}
      await launchUrl(iosStoreHttps, mode: LaunchMode.externalApplication);
      return;
    }

    try {
      if (await canLaunchUrl(androidMarket)) {
        await launchUrl(androidMarket, mode: LaunchMode.externalApplication);
        return;
      }
    } catch (_) {}
    await launchUrl(androidPlayHttps, mode: LaunchMode.externalApplication);
  }
}
