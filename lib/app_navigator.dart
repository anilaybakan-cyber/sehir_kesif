import 'package:flutter/material.dart';

/// Root navigator — kept out of `main.dart` so services avoid importing `main`.
final GlobalKey<NavigatorState> navigatorKey = GlobalKey<NavigatorState>();
