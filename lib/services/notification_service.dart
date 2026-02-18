import 'dart:convert';
import 'dart:io';

import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Background message handler - must be top-level function
@pragma('vm:entry-point')
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  await Firebase.initializeApp();
  debugPrint('🔔 Background message: ${message.messageId}');
}

class NotificationService {
  static final NotificationService _instance = NotificationService._internal();
  factory NotificationService() => _instance;
  NotificationService._internal();

  final FirebaseMessaging _firebaseMessaging = FirebaseMessaging.instance;
  final FirebaseAnalytics _analytics = FirebaseAnalytics.instance;
  final FlutterLocalNotificationsPlugin _localNotifications = FlutterLocalNotificationsPlugin();
  
  String? _fcmToken;
  String? get fcmToken => _fcmToken;

  /// Initialize the notification service
  Future<void> initialize() async {
    debugPrint('🔔 NotificationService.initialize() starting...');
    
    // Set background message handler
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);
    debugPrint('🔔 Step 1: Background handler set');

    // Request permission
    try {
      await _requestPermission();
      debugPrint('🔔 Step 2: Permission requested');
    } catch (e) {
      debugPrint('🔔 Step 2 ERROR - Permission request failed: $e');
    }

    // Get FCM token
    try {
      await _getToken();
      debugPrint('🔔 Step 3: Token retrieved');
    } catch (e) {
      debugPrint('🔔 Step 3 ERROR - Token retrieval failed: $e');
    }

    // Initialize local notifications for foreground
    try {
      await _initializeLocalNotifications();
      debugPrint('🔔 Step 4: Local notifications initialized');
    } catch (e) {
      debugPrint('🔔 Step 4 ERROR - Local notifications failed: $e');
    }

    // Handle foreground messages
    FirebaseMessaging.onMessage.listen(_handleForegroundMessage);
    debugPrint('🔔 Step 5: Foreground listener set');

    // Handle notification tap when app is in background
    FirebaseMessaging.onMessageOpenedApp.listen(_handleMessageOpenedApp);
    debugPrint('🔔 Step 6: Background tap listener set');

    // Check if app was opened from a notification
    final initialMessage = await _firebaseMessaging.getInitialMessage();
    if (initialMessage != null) {
      _handleMessageOpenedApp(initialMessage);
    }
    debugPrint('🔔 Step 7: Initial message checked');

    // Subscribe to topic for broadcast notifications
    try {
      await _firebaseMessaging.subscribeToTopic('all_users');
      debugPrint('🔔 Step 8: Subscribed to topic: all_users');
    } catch (e) {
      debugPrint('🔔 Step 8 ERROR - Topic subscription failed: $e');
    }

    // Enable foreground notification presentation (iOS)
    await _firebaseMessaging.setForegroundNotificationPresentationOptions(
      alert: true,
      badge: true,
      sound: true,
    );
    debugPrint('🔔 Step 9: Foreground presentation options set');
    debugPrint('🔔 NotificationService.initialize() COMPLETE');
  }

  /// Target: Subscribe to a specific city topic
  Future<void> subscribeToCity(String cityId) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final lastCity = prefs.getString('last_subscribed_city');

      // Unsubscribe from last city if exists
      if (lastCity != null && lastCity != cityId) {
        await _firebaseMessaging.unsubscribeFromTopic('city_$lastCity');
        debugPrint('🔔 Unsubscribed from: city_$lastCity');
      }

      // Subscribe to new city
      await _firebaseMessaging.subscribeToTopic('city_$cityId');
      await prefs.setString('last_subscribed_city', cityId);
      
      // Log as user property for Analytics targeting
      await _analytics.setUserProperty(name: 'current_city', value: cityId);
      
      debugPrint('🔔 Subscribed to: city_$cityId');
    } catch (e) {
      debugPrint('🔔 Error subscribing to city topic: $e');
    }
  }

  /// Target: Log custom event for behavior-based notifications
  Future<void> logEvent(String name, {Map<String, Object>? parameters}) async {
    await _analytics.logEvent(name: name, parameters: parameters);
    debugPrint('📊 Analytics Event: $name');
  }

  /// Request notification permission
  Future<void> _requestPermission() async {
    final settings = await _firebaseMessaging.requestPermission(
      alert: true,
      badge: true,
      sound: true,
      provisional: false,
    );

    debugPrint('🔔 Notification permission: ${settings.authorizationStatus}');
  }

  /// Get FCM token
  Future<void> _getToken() async {
    try {
      _fcmToken = await _firebaseMessaging.getToken();
      debugPrint('🔔 FCM Token: $_fcmToken');

      // Listen for token refresh
      _firebaseMessaging.onTokenRefresh.listen((newToken) {
        _fcmToken = newToken;
        debugPrint('🔔 FCM Token refreshed: $newToken');
      });
    } catch (e) {
      debugPrint('🔔 Error getting FCM token: $e');
    }
  }

  /// Initialize local notifications
  Future<void> _initializeLocalNotifications() async {
    const androidSettings = AndroidInitializationSettings('@mipmap/ic_launcher');
    const iosSettings = DarwinInitializationSettings(
      requestAlertPermission: false,
      requestBadgePermission: false,
      requestSoundPermission: false,
    );

    const initSettings = InitializationSettings(
      android: androidSettings,
      iOS: iosSettings,
    );

    await _localNotifications.initialize(
      initSettings,
      onDidReceiveNotificationResponse: (details) {
        debugPrint('🔔 Notification tapped: ${details.payload}');
      },
    );

    if (Platform.isAndroid) {
      const channel = AndroidNotificationChannel(
        'high_importance_channel',
        'High Importance Notifications',
        description: 'This channel is used for important notifications.',
        importance: Importance.high,
      );

      await _localNotifications
          .resolvePlatformSpecificImplementation<AndroidFlutterLocalNotificationsPlugin>()
          ?.createNotificationChannel(channel);
    }
  }

  /// Handle foreground messages
  void _handleForegroundMessage(RemoteMessage message) {
    debugPrint('🔔 Foreground message: ${message.notification?.title}');

    final notification = message.notification;
    if (notification != null) {
      // Save notification to history
      _saveNotification(
        title: notification.title ?? 'MyWay',
        body: notification.body ?? '',
      );
      
      _showLocalNotification(
        title: notification.title ?? 'MyWay',
        body: notification.body ?? '',
        payload: message.data.toString(),
      );
    }
  }

  /// Handle when user taps on notification
  void _handleMessageOpenedApp(RemoteMessage message) {
    debugPrint('🔔 Notification opened: ${message.data}');
    // Save notification if coming from background
    final notification = message.notification;
    if (notification != null) {
      _saveNotification(
        title: notification.title ?? 'MyWay',
        body: notification.body ?? '',
      );
    }
  }

  /// Show a local notification
  Future<void> _showLocalNotification({
    required String title,
    required String body,
    String? payload,
  }) async {
    const androidDetails = AndroidNotificationDetails(
      'high_importance_channel',
      'High Importance Notifications',
      channelDescription: 'This channel is used for important notifications.',
      importance: Importance.high,
      priority: Priority.high,
      icon: '@mipmap/ic_launcher',
    );

    const iosDetails = DarwinNotificationDetails(
      presentAlert: true,
      presentBadge: true,
      presentSound: true,
    );

    const details = NotificationDetails(
      android: androidDetails,
      iOS: iosDetails,
    );

    await _localNotifications.show(
      DateTime.now().millisecondsSinceEpoch.remainder(100000),
      title,
      body,
      details,
      payload: payload,
    );
  }

  /// Show Welcome Notification
  Future<void> showWelcomeNotification() async {
    // Wait for a few seconds to let the user settle in
    await Future.delayed(const Duration(seconds: 3));
    
    await _showLocalNotification(
      title: "Şehir Kaşifi'ne Hoş Geldin! 👋",
      body: "Sana özel rotanı hemen oluştur, şehri yerlisi gibi gezmeye başla! 🗺️",
    );
  }

  // ══════════════════════════════════════════════════════════════════════════
  // NOTIFICATION HISTORY STORAGE
  // ══════════════════════════════════════════════════════════════════════════

  static const String _notificationsKey = 'notification_history';

  /// Save a notification to local storage
  Future<void> _saveNotification({
    required String title,
    required String body,
  }) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final notificationsJson = prefs.getString(_notificationsKey);
      
      List<Map<String, dynamic>> notifications = [];
      if (notificationsJson != null) {
        final decoded = jsonDecode(notificationsJson) as List;
        notifications = decoded.map((e) => Map<String, dynamic>.from(e)).toList();
      }
      
      // Add new notification at the beginning
      notifications.insert(0, {
        'id': DateTime.now().millisecondsSinceEpoch.toString(),
        'title': title,
        'body': body,
        'timestamp': DateTime.now().toIso8601String(),
        'read': false,
      });
      
      // Keep only last 50 notifications
      if (notifications.length > 50) {
        notifications = notifications.sublist(0, 50);
      }
      
      await prefs.setString(_notificationsKey, jsonEncode(notifications));
      debugPrint('🔔 Notification saved to history');
    } catch (e) {
      debugPrint('🔔 Error saving notification: $e');
    }
  }

  /// Get all saved notifications
  Future<List<Map<String, dynamic>>> getNotifications() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final notificationsJson = prefs.getString(_notificationsKey);
      
      if (notificationsJson == null) return [];
      
      final decoded = jsonDecode(notificationsJson) as List;
      return decoded.map((e) => Map<String, dynamic>.from(e)).toList();
    } catch (e) {
      debugPrint('🔔 Error getting notifications: $e');
      return [];
    }
  }

  /// Get unread notification count
  Future<int> getUnreadCount() async {
    final notifications = await getNotifications();
    return notifications.where((n) => n['read'] == false).length;
  }

  /// Mark a notification as read
  Future<void> markAsRead(String id) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final notifications = await getNotifications();
      
      for (var notification in notifications) {
        if (notification['id'] == id) {
          notification['read'] = true;
          break;
        }
      }
      
      await prefs.setString(_notificationsKey, jsonEncode(notifications));
    } catch (e) {
      debugPrint('🔔 Error marking notification as read: $e');
    }
  }

  /// Mark all notifications as read
  Future<void> markAllAsRead() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final notifications = await getNotifications();
      
      for (var notification in notifications) {
        notification['read'] = true;
      }
      
      await prefs.setString(_notificationsKey, jsonEncode(notifications));
    } catch (e) {
      debugPrint('🔔 Error marking all as read: $e');
    }
  }

  /// Clear all notification history
  Future<void> clearNotifications() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove(_notificationsKey);
      debugPrint('🔔 Notification history cleared');
    } catch (e) {
      debugPrint('🔔 Error clearing notifications: $e');
    }
  }
}
