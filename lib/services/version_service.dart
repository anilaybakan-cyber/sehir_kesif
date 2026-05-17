import 'package:package_info_plus/package_info_plus.dart';
import 'remote_config_service.dart';
import 'package:flutter/foundation.dart';

class VersionService {
  static final VersionService instance = VersionService._();
  VersionService._();

  /// Compares the current app version with the remote min_app_version.
  /// Returns [true] if the current version is strictly less than the min version.
  Future<bool> isUpdateRequired() async {
    try {
      final PackageInfo info = await PackageInfo.fromPlatform();
      final String currentVersion = info.version;
      final String minVersion = RemoteConfigService.instance.minAppVersion;

      if (minVersion.isEmpty) return false;

      return _isVersionLower(currentVersion, minVersion);
    } catch (e) {
      debugPrint("Error checking version: $e");
      return false; // Safely default to false on error 
    }
  }

  /// Helper to compare semantic version strings (e.g. "1.0.0" < "1.0.1")
  bool _isVersionLower(String current, String minimum) {
    try {
      // Clean up version strings (remove build numbers or suffixes like +4 or -beta)
      String cleanCurrent = current.split('+')[0].split('-')[0];
      String cleanMinimum = minimum.split('+')[0].split('-')[0];

      List<int> currentParts = cleanCurrent.split('.').map(int.parse).toList();
      List<int> minimumParts = cleanMinimum.split('.').map(int.parse).toList();

      // Pad with zeros to ensure equal length
      while (currentParts.length < minimumParts.length) currentParts.add(0);
      while (minimumParts.length < currentParts.length) minimumParts.add(0);

      for (int i = 0; i < currentParts.length; i++) {
        if (currentParts[i] < minimumParts[i]) return true;
        if (currentParts[i] > minimumParts[i]) return false;
      }
      return false; // Equal versions meaning update is not strictly required
    } catch (e) {
      debugPrint("Version parsing error: $e");
      return false; // Safe fallback
    }
  }
}

