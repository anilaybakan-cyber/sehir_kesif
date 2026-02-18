import UIKit
import Flutter
import GoogleMaps
import FirebaseCore
import FirebaseMessaging
import UserNotifications

@main
@objc class AppDelegate: FlutterAppDelegate {

  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {

    // 🔥 Firebase Configuration
    FirebaseApp.configure()
    
    // 🔔 Push Notification Setup
    UNUserNotificationCenter.current().delegate = self
    
    let authOptions: UNAuthorizationOptions = [.alert, .badge, .sound]
    UNUserNotificationCenter.current().requestAuthorization(options: authOptions) { _, _ in }
    
    application.registerForRemoteNotifications()
    
    // Set Messaging delegate
    Messaging.messaging().delegate = self

    // 🚀 Google Maps SDK API Key
    GMSServices.provideAPIKey("AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk")

    GeneratedPluginRegistrant.register(with: self)
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
