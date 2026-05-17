import 'dart:convert';
import 'dart:io';
import 'dart:async';

import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:firebase_analytics/firebase_analytics.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:app_links/app_links.dart';

import '../app_navigator.dart';
import '../constants/store_urls.dart';
import 'premium_service.dart';
import 'remote_config_service.dart';

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
  final _appLinks = AppLinks();
  StreamSubscription<Uri>? _linkSubscription;
  
  String? _fcmToken;
  String? get fcmToken => _fcmToken;

  /// Stores a deep link that arrived while the UI wasn't ready yet
  Map<String, dynamic>? _pendingDeepLink;

  /// Called by MainScreen after splash completes to deliver any queued deep link.
  void consumePendingDeepLink() {
    final pending = _pendingDeepLink;
    if (pending == null) return;
    _pendingDeepLink = null;
    debugPrint('🔗 Consuming pending deep link: $pending');
    Future.delayed(const Duration(milliseconds: 250), () {
      _navigateFromData(pending);
    });
  }

  /// Initialize the notification service
  Future<void> initialize() async {
    debugPrint('🔔 NotificationService.initialize() starting...');
    
    // 🔗 Initialize App Links (Browser/Deep Links)
    _initDeepLinks();

    // Set background message handler
    FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

    // Request permission
    try {
      await _requestPermission();
      await _getToken();
      await _initializeLocalNotifications();
    } catch (e) {
      debugPrint('🔔 Initialization error: $e');
    }

    // Listeners
    FirebaseMessaging.onMessage.listen(_handleForegroundMessage);
    FirebaseMessaging.onMessageOpenedApp.listen(_handleMessageOpenedApp);

    // Initial message (Terminated state)
    final initialMessage = await _firebaseMessaging.getInitialMessage();
    if (initialMessage != null) {
      _pendingDeepLink = Map<String, dynamic>.from(initialMessage.data);
    }

    try {
      await _firebaseMessaging.subscribeToTopic('all_users');
    } catch (_) {}

    await _firebaseMessaging.setForegroundNotificationPresentationOptions(
      alert: true,
      badge: true,
      sound: true,
    );
    debugPrint('🔔 NotificationService.initialize() COMPLETE');
  }

  /// URL tabanlı derin linkleri yakalar
  void _initDeepLinks() {
    _appLinks.getInitialLink().then((uri) {
      if (uri != null) {
        debugPrint('🔗 Initial App Link: $uri');
        _navigateFromUrl(uri);
      }
    });

    _linkSubscription = _appLinks.uriLinkStream.listen((uri) {
      debugPrint('🔗 Incoming App Link: $uri');
      _navigateFromUrl(uri);
    });
  }

  /// URL -> Navigation Data mapping
  void _navigateFromUrl(Uri uri) {
    final Map<String, dynamic> data = {};
    String host = uri.host.toLowerCase();
    
    // Örn: myway://explore -> /main (tab=0)
    // Örn: myway://detail?cityId=bari&placeName=Pane%20e%20Pomodoro
    
    if (host == "explore" || host == "main") {
      data['route'] = "/main";
      data['tab'] = uri.queryParameters['tab'] ?? "0";
      final inner = uri.queryParameters['routesTab'];
      if (inner != null) data['routesTab'] = inner;
      final profileTab = uri.queryParameters['profileTab'];
      if (profileTab != null) data['profileTab'] = profileTab;
      final profileAction = uri.queryParameters['profileAction'];
      if (profileAction != null) data['profileAction'] = profileAction;
    } else if (host == "routes") {
      // Doğrudan Rotalar sekmesine atlama: myway://routes?inner=2
      data['route'] = "/main";
      data['tab'] = "1";
      final inner = uri.queryParameters['inner'] ??
          uri.queryParameters['routesTab'] ??
          uri.pathSegments.firstOrNull;
      if (inner != null) data['routesTab'] = inner;
    } else if (host == "profile") {
      // Profil deeplinkleri:
      //   myway://profile?section=favorites|visited|routes
      //   myway://profile?action=add-memory|preferences|memories
      data['route'] = "/main";
      data['tab'] = "4";
      final section = (uri.queryParameters['section'] ??
              uri.pathSegments.firstOrNull ??
              '')
          .toLowerCase();
      const sectionMap = {
        'favorites': '0',
        'favoriler': '0',
        'favoris': '0',
        'visits': '1',
        'visited': '1',
        'ziyaret': '1',
        'routes': '2',
        'history': '2',
        'rotalar': '2',
      };
      if (sectionMap.containsKey(section)) {
        data['profileTab'] = sectionMap[section]!;
      }
      final action = uri.queryParameters['action'];
      if (action != null && action.isNotEmpty) {
        data['profileAction'] = action;
      }
    } else if (host == "detail" || host == "place") {
      data['route'] = "/detail-by-id";
      data['cityId'] = uri.queryParameters['cityId'] ?? uri.pathSegments.firstOrNull;
      data['placeName'] = uri.queryParameters['placeName'] ?? (uri.pathSegments.length > 1 ? uri.pathSegments[1] : null);
    } else if (host == "guide") {
      data['route'] = "/guide";
      data['cityId'] = uri.queryParameters['cityId'] ?? uri.pathSegments.firstOrNull;
    } else if (host == "paywall") {
      data['route'] = "/paywall";
    } else if (host == "city-switch") {
      data['route'] = "/city-switch";
    }

    if (data.containsKey('route')) {
      _navigateFromData(data);
    }
  }

  /// CENTRAL ANALYTICS LOGGER
  /// Bu metod üzerinden tüm kullanıcı aksiyonlarını takip edebilirsin.
  Future<void> logEvent(String name, {Map<String, Object>? parameters}) async {
    await _analytics.logEvent(name: name, parameters: parameters);
    debugPrint('📊 Analytics Event Logged: $name | Params: $parameters');
  }

  Future<void> _requestPermission() async {
    await _firebaseMessaging.requestPermission(alert: true, badge: true, sound: true);
  }

  Future<void> _getToken() async {
    _fcmToken = await _firebaseMessaging.getToken();
    debugPrint('🔔 FCM Token: $_fcmToken');
  }

  Future<void> _initializeLocalNotifications() async {
    const androidSettings = AndroidInitializationSettings('@mipmap/ic_launcher');
    const iosSettings = DarwinInitializationSettings();
    const initSettings = InitializationSettings(android: androidSettings, iOS: iosSettings);

    await _localNotifications.initialize(initSettings, onDidReceiveNotificationResponse: (details) {
      if (details.payload != null) {
        final data = Map<String, dynamic>.from(jsonDecode(details.payload!));
        _navigateFromData(data);
      }
    });
  }

  void _handleForegroundMessage(RemoteMessage message) {
    if (message.notification != null) {
      final title = message.notification!.title ?? 'MyWay';
      final body = message.notification!.body ?? '';
      
      _saveNotification(title, body, message.data);
      
      _showLocalNotification(
        title: title,
        body: body,
        payload: jsonEncode(message.data),
      );
    }
  }

  void _handleMessageOpenedApp(RemoteMessage message) {
    _saveNotification(
      message.notification?.title ?? 'MyWay',
      message.notification?.body ?? '',
      message.data,
    );
    _navigateFromData(message.data);
  }

  void _navigateFromData(Map<String, dynamic> data) {
    final route = data['route']?.toString() ?? '';
    if (route.isEmpty) return;

    final navigator = navigatorKey.currentState;
    if (navigator == null) {
      _pendingDeepLink = data; // Navigator hazır değilse kuyruğa at
      return;
    }

    logEvent('deep_link_opened', parameters: {'route': route});

    switch (route) {
      case '/main':
        final tab = int.tryParse(data['tab']?.toString() ?? '') ?? 0;
        final routesTab = int.tryParse(data['routesTab']?.toString() ?? '') ?? 0;
        final profileTab = int.tryParse(data['profileTab']?.toString() ?? '') ?? 0;
        final profileAction = data['profileAction']?.toString();
        navigator.pushNamedAndRemoveUntil(
          '/main',
          (route) => false,
          arguments: {
            'initialIndex': tab,
            'initialRoutesTabIndex': routesTab,
            'initialProfileTabIndex': profileTab,
            'initialProfileAction': profileAction,
          },
        );
        break;
      case '/guide':
        final cityId = data['cityId']?.toString().toLowerCase() ?? '';
        navigator.pushNamed('/guide', arguments: {'cityId': cityId});
        break;
      case '/detail-by-id':
        final cityId = data['cityId']?.toString().toLowerCase() ?? '';
        final placeName = data['placeName']?.toString() ?? '';
        navigator.pushNamed('/detail-by-id', arguments: {'cityId': cityId, 'placeName': placeName});
        break;
      case '/paywall':
        if (PremiumService.instance.isPremium) {
          navigator.pushNamedAndRemoveUntil(
            '/main',
            (route) => false,
            arguments: {'initialIndex': 0},
          );
        } else {
          navigator.pushNamed('/paywall');
        }
        break;
      case '/city-switch':
        navigator.pushNamed('/city-switch');
        break;
      case '/rate-us':
      case '/rate':
      case '/review':
        StoreUrls.launchReviewPage();
        break;
      case '/store':
      case '/app-store':
      case '/update':
        StoreUrls.launchStorePage();
        break;
      default:
        navigator.pushNamed(route);
    }
  }

  Future<void> _showLocalNotification({required String title, required String body, String? payload}) async {
    const androidDetails = AndroidNotificationDetails('high_importance_channel', 'High Importance');
    const details = NotificationDetails(android: androidDetails, iOS: DarwinNotificationDetails());
    await _localNotifications.show(DateTime.now().millisecond, title, body, details, payload: payload);
  }

  // --- Notification History & Management ---
  static const String _notificationsKey = 'notifications_history';

  /// Subscribe to a city topic
  Future<void> subscribeToCity(String cityId) async {
    final topic = 'city_${cityId.toLowerCase().replaceAll(' ', '_')}';
    try {
      await _firebaseMessaging.subscribeToTopic(topic);
      debugPrint('🔔 Subscribed to topic: $topic');
    } catch (e) {
      debugPrint('🔔 Error subscribing to topic $topic: $e');
    }
  }

  /// Get saved notifications from SharedPreferences
  Future<List<Map<String, dynamic>>> getNotifications() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonList = prefs.getStringList(_notificationsKey) ?? [];
    return jsonList
        .map((e) => jsonDecode(e) as Map<String, dynamic>)
        .toList()
        .reversed
        .toList();
  }

  /// Save a new notification to history
  Future<void> _saveNotification(String title, String body, Map<String, dynamic> data) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final notifications = prefs.getStringList(_notificationsKey) ?? [];

      final newNotification = {
        'title': title,
        'body': body,
        'data': data,
        'timestamp': DateTime.now().toIso8601String(),
        'isRead': false,
      };

      notifications.add(jsonEncode(newNotification));
      // Keep only last 50 notifications
      if (notifications.length > 50) {
        notifications.removeAt(0);
      }

      await prefs.setStringList(_notificationsKey, notifications);
      debugPrint('🔔 Notification saved to local history');
    } catch (e) {
      debugPrint('🔔 Error saving notification: $e');
    }
  }

  /// Mark all notifications as read
  Future<void> markAllAsRead() async {
    final prefs = await SharedPreferences.getInstance();
    final jsonList = prefs.getStringList(_notificationsKey) ?? [];
    final notifications = jsonList.map((e) => jsonDecode(e) as Map<String, dynamic>).toList();

    for (var n in notifications) {
      n['isRead'] = true;
    }

    await prefs.setStringList(_notificationsKey, notifications.map((e) => jsonEncode(e)).toList());
    debugPrint('🔔 All notifications marked as read');
  }

  /// Clear all notification history
  Future<void> clearNotifications() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(_notificationsKey);
    debugPrint('🔔 Notification history cleared');
  }

  Future<void> _launchStore() async {
    final url = Uri.parse(Platform.isIOS ? RemoteConfigService.instance.storeUrlIOS : RemoteConfigService.instance.storeUrlAndroid);
    if (await canLaunchUrl(url)) await launchUrl(url, mode: LaunchMode.externalApplication);
  }
}
