import UIKit
import Flutter
import GoogleMaps
import FirebaseMessaging
import UserNotifications

@main
@objc class AppDelegate: FlutterAppDelegate {

  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    // 🚀 Google Maps SDK API Key (before Flutter engine)
    GMSServices.provideAPIKey("AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk")

    // Registers Flutter plugins; firebase_core configures FIRApp from GoogleService-Info.plist here.
    GeneratedPluginRegistrant.register(with: self)

    // 🔔 Push / FCM — must run after FIRApp exists (see firebase_core FLTFirebaseCorePlugin).
    UNUserNotificationCenter.current().delegate = self

    let authOptions: UNAuthorizationOptions = [.alert, .badge, .sound]
    UNUserNotificationCenter.current().requestAuthorization(options: authOptions) { _, _ in }

    application.registerForRemoteNotifications()

    Messaging.messaging().delegate = self

    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }
  
  // Handle FCM Token refresh
  override func application(_ application: UIApplication,
                            didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    Messaging.messaging().apnsToken = deviceToken
    super.application(application, didRegisterForRemoteNotificationsWithDeviceToken: deviceToken)
  }
}

// MARK: - MessagingDelegate
extension AppDelegate: MessagingDelegate {
  func messaging(_ messaging: Messaging, didReceiveRegistrationToken fcmToken: String?) {
    print("🔔 FCM Token: \(fcmToken ?? "nil")")
    // Token can be sent to your server here
  }
}
