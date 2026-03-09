import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:package_info_plus/package_info_plus.dart';

class ContentUpdateService {
  // GITHUB RAW CONTENT
  // Üretim URL'leri
  static const String _baseUrl = 'https://raw.githubusercontent.com/anilaybakan-cyber/myway-data/refs/heads/main/cities';
  
  // Versiyon kontrolü için manifest dosyası
  static const String _manifestUrl = 'https://raw.githubusercontent.com/anilaybakan-cyber/myway-data/refs/heads/main/version_manifest.json';
  static const String _configBaseUrl = 'https://raw.githubusercontent.com/anilaybakan-cyber/myway-data/refs/heads/main/config';

  /// Güncellemeleri kontrol et ve indir
  static Future<void> checkForUpdates() async {
    debugPrint("🔄 ContentUpdateService: Güncellemeler kontrol ediliyor...");

    try {
      // 0. Önce App Update kontrolü yap (Versiyon değiştiyse cache'i temizle)
      await _checkAppVersionAndCleanup();

      // 1. Manifest dosyasını çek (Hangi şehir hangi versiyonda?)
      final response = await http.get(Uri.parse(_manifestUrl));
      
      if (response.statusCode != 200) {
        debugPrint("⚠️ Manifest dosyası çekilemedi: ${response.statusCode}");
        return;
      }

      final Map<String, dynamic> remoteManifest = json.decode(response.body);
      final prefs = await SharedPreferences.getInstance();

      // 2. Her anahtar için kontrol et (Şehirler ve Configler)
      for (final key in remoteManifest.keys) {
        final value = remoteManifest[key];
        if (value is! int) continue;

        final int remoteVersion = value;
        final int localVersion = prefs.getInt('version_$key') ?? 0;

        if (remoteVersion > localVersion) {
            debugPrint("⬇️ $key için güncelleme bulundu (v$localVersion -> v$remoteVersion). İndiriliyor...");
            if (key == 'paywall_config') {
              await _downloadAndSaveConfig(key, remoteVersion, prefs);
            } else {
              await _downloadAndSaveCity(key, remoteVersion, prefs);
            }
        }
      }
      
      debugPrint("🏁 Güncelleme kontrolü tamamlandı.");

    } catch (e) {
      debugPrint("❌ Güncelleme hatası: $e");
    }
  }

  /// Uygulama güncellendiyse (App Store update), eski cache dosyalarını temizle.
  /// Böylece bundled asset (gömülü dosya) devreye girer.
  static Future<void> _checkAppVersionAndCleanup() async {
    try {
      final PackageInfo packageInfo = await PackageInfo.fromPlatform();
      final String currentAppVersion = "${packageInfo.version}+${packageInfo.buildNumber}";
      
      final prefs = await SharedPreferences.getInstance();
      final String? lastKnownVersion = prefs.getString('last_app_version');

      if (lastKnownVersion != null && lastKnownVersion != currentAppVersion) {
        debugPrint("🚀 UYGULAMA GÜNCELLENDİ: $lastKnownVersion -> $currentAppVersion");
        debugPrint("🧹 Eski cache dosyaları temizleniyor...");
        await _clearAllCache(prefs);
      } else {
        // İlk açılış veya aynı versiyon
        if (lastKnownVersion == null) {
             debugPrint("🆕 İlk kurulum algılandı. Versiyon kaydediliyor: $currentAppVersion");
        }
      }

      // Yeni versiyonu kaydet
      await prefs.setString('last_app_version', currentAppVersion);

    } catch (e) {
      debugPrint("⚠️ Versiyon kontrol hatası: $e");
    }
  }

  /// Tüm indirilmiş şehir verilerini siler
  static Future<void> _clearAllCache(SharedPreferences prefs) async {
    try {
      final dir = await getApplicationDocumentsDirectory();
      final citiesDir = Directory('${dir.path}/cities');
      
      if (await citiesDir.exists()) {
        await citiesDir.delete(recursive: true);
        debugPrint("🗑 Cities klasörü silindi.");
      }

      // SharedPreferences'daki versiyon bilgilerini de sil (version_istanbul, version_paris vb.)
      final keys = prefs.getKeys().where((k) => k.startsWith('version_')).toList();
      for (final key in keys) {
        await prefs.remove(key);
      }
      debugPrint("🧹 Versiyon kayıtları temizlendi.");

    } catch (e) {
      debugPrint("❌ Cache temizleme hatası: $e");
    }
  }

  /// Tek bir şehri indir ve kaydet
  static Future<void> _downloadAndSaveCity(String city, int version, SharedPreferences prefs) async {
    try {
      final url = '$_baseUrl/$city.json';
      final response = await http.get(Uri.parse(url));

      if (response.statusCode == 200) {
        // UTF-8 decode işlemi
        final String jsonContent = utf8.decode(response.bodyBytes);
        
        // JSON validasyonu
        try {
           json.decode(jsonContent); 
        } catch (e) {
           debugPrint("❌ İndirilen $city.json hatalı, kaydedilmedi.");
           return;
        }

        // Dosyayı kaydet
        final dir = await getApplicationDocumentsDirectory();
        final file = File('${dir.path}/cities/$city.json');
        
        if (!await file.parent.exists()) {
          await file.parent.create(recursive: true);
        }

        await file.writeAsString(jsonContent);
        
        // Versiyonu güncelle
        await prefs.setInt('version_$city', version);
        debugPrint("✅ $city başarıyla güncellendi ve kaydedildi.");
        
      } else {
        debugPrint("❌ $city indirilemedi: ${response.statusCode}");
      }
    } catch (e) {
      debugPrint("❌ Dosya yazma hatası ($city): $e");
    }
  }

  /// Config dosyasını indir ve kaydet
  static Future<void> _downloadAndSaveConfig(String configName, int version, SharedPreferences prefs) async {
    try {
      final url = '$_configBaseUrl/$configName.json';
      final response = await http.get(Uri.parse(url));

      if (response.statusCode == 200) {
        final String jsonContent = utf8.decode(response.bodyBytes);
        
        try { json.decode(jsonContent); } catch (e) {
           debugPrint("❌ İndirilen $configName.json hatalı.");
           return;
        }

        final dir = await getApplicationDocumentsDirectory();
        final file = File('${dir.path}/config/$configName.json');
        
        if (!await file.parent.exists()) {
          await file.parent.create(recursive: true);
        }

        await file.writeAsString(jsonContent);
        await prefs.setInt('version_$configName', version);
        debugPrint("✅ $configName başarıyla güncellendi.");
      }
    } catch (e) {
      debugPrint("❌ Config indirme hatası ($configName): $e");
    }
  }

  /// İndirilmiş (cached) dosyanın yolunu döndürür
  static Future<File?> getLocalCityFile(String cityName) async {
    try {
      final dir = await getApplicationDocumentsDirectory();
      final file = File('${dir.path}/cities/$cityName.json');
      
      if (await file.exists()) {
        return file;
      }
    } catch (e) {
      debugPrint("⚠️ Dosya yolu hatası: $e");
    }
    return null;
  }

  /// İndirilmiş (cached) config dosyasının yolunu döndürür
  static Future<File?> getLocalConfigFile(String fileName) async {
    try {
      final dir = await getApplicationDocumentsDirectory();
      final file = File('${dir.path}/config/$fileName.json');
      if (await file.exists()) return file;
    } catch (e) {
      debugPrint("⚠️ Config yolu hatası: $e");
    }
    return null;
  }
}
