import UIKit
import Flutter
import GoogleMaps   // <-- Bunu mutlaka ekle

@main
@objc class AppDelegate: FlutterAppDelegate {

  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {

    // 🚀 Google Maps SDK API Key
    GMSServices.provideAPIKey("AIzaSyCMEuzJpyZtG-LPG-8DFiNrSn2-KfKrQp0")   // <-- ZORUNLU

    // (Opsiyonel) Places API kullanacaksan:
    // GMSPlacesClient.provideAPIKey("BURAYA_API_KEY_YAZ")

    GeneratedPluginRegistrant.register(with: self)
    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
}
