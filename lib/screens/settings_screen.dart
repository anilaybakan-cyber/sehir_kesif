// =============================================================================
// SETTINGS SCREEN - Offline Mod, Cache, Fotoğraf Ayarları
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../services/cache_service.dart';
import '../l10n/app_localizations.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  final _cacheService = CacheService();
  static const Color bgCardLight = WanderlustColors.bgCardLight;
  

  bool _highQualityPhotos = true;
  bool _autoDownload = true;
  String _cacheSize = AppLocalizations.instance.calculating;
  String _lastUpdate = "-";
  List<String> _cachedCities = [];
  DateTime? _lastSync;
  bool _loading = true;

  @override
  void initState() {
    super.initState();
    _loadSettings();
  }

  Future<void> _loadSettings() async {
    final prefs = await SharedPreferences.getInstance();

    // Cache bilgilerini yükle
    final cacheSize = await _cacheService.getCacheSize();
    final cachedCities = await _cacheService.getCachedCities();
    final lastSync = await _cacheService.getLastSyncTime();

    setState(() {

      _highQualityPhotos = prefs.getBool('high_quality_photos') ?? true;
      _autoDownload = prefs.getBool('auto_download_cities') ?? true;
      _cacheSize = _cacheService.formatCacheSize(cacheSize);
      _cachedCities = cachedCities;
      _lastSync = lastSync;
      _loading = false;
    });
  }



  Future<void> _toggleHighQualityPhotos(bool value) async {
    HapticFeedback.selectionClick();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('high_quality_photos', value);
    setState(() => _highQualityPhotos = value);
  }

  Future<void> _toggleAutoDownload(bool value) async {
    HapticFeedback.selectionClick();
    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool('auto_download_cities', value);
    setState(() => _autoDownload = value);
  }

  Future<void> _clearCache() async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: const Color(0xFF1F1F1F),
        title: Text(AppLocalizations.instance.clearCacheAction, style: const TextStyle(color: Colors.white)),
        content: Text(
          AppLocalizations.instance.confirmClearCache,
          style: const TextStyle(color: Colors.white70),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(AppLocalizations.instance.cancel, style: const TextStyle(color: Colors.white)),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(AppLocalizations.instance.delete, style: const TextStyle(color: Colors.redAccent)),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      await _cacheService.clearAllCache();
      _loadSettings();
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(AppLocalizations.instance.cacheCleared),
            backgroundColor: bgCardLight,
            behavior: SnackBarBehavior.floating,
            duration: const Duration(milliseconds: 1200),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          ),
        );
      }
    }
  }

  void _showDownloadDialog() {
    showDialog(
      context: context,
      barrierDismissible: false, // İndirme sırasında kapatmayı engelle
      builder: (context) {
        return StatefulBuilder(
          builder: (context, setState) {
            return AlertDialog(
              backgroundColor: const Color(0xFF1F1F1F),
              title: Text(AppLocalizations.instance.selectCitiesToDownload, style: const TextStyle(color: Colors.white)),
              content: SizedBox(
                width: double.maxFinite,
                child: _loading 
                  ? Center(child: Text(AppLocalizations.instance.loading, style: const TextStyle(color: Colors.white)))
                  : ListView(
                      shrinkWrap: true,
                      children: [
                        _buildCityDownloadTile("Barcelona", true),
                        _buildCityDownloadTile("Paris", false),
                        _buildCityDownloadTile("Roma", false),
                        _buildCityDownloadTile("İstanbul", false),
                      ],
                    ),
              ),
              actions: [
                TextButton(
                  onPressed: () => Navigator.pop(context, false),
                  child: Text(AppLocalizations.instance.cancel, style: const TextStyle(color: Colors.white)),
                ),
                TextButton(
                  onPressed: () {
                    Navigator.pop(context);
                    _downloadSelectedCities();
                  },
                  child: Text(AppLocalizations.instance.downloadSelected, style: const TextStyle(color: Color(0xFF00B894))),
                ),
              ],
            );
          },
        );
      },
    );
  }

  Widget _buildCityDownloadTile(String city, bool isDownloaded) {
    return Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: isDownloaded
            ? const Color(0xFF00B894).withOpacity(0.1)
            : Colors.grey.shade100,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: isDownloaded ? const Color(0xFF00B894) : Colors.transparent,
        ),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: isDownloaded ? const Color(0xFF00B894) : Colors.white,
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(
              isDownloaded ? Icons.check_rounded : Icons.download_rounded,
              color: isDownloaded ? Colors.white : Colors.grey.shade600,
              size: 20,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  city,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                Text(
                  isDownloaded ? "${AppLocalizations.instance.downloaded} • ~2 MB" : "~2 MB",
                  style: TextStyle(fontSize: 13, color: Colors.grey.shade600),
                ),
              ],
            ),
          ),
          if (!isDownloaded)
            Checkbox(
              value: false,
              onChanged: (v) {},
              activeColor: const Color(0xFF00B894),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(4),
              ),
            ),
        ],
      ),
    );
  }

  Future<void> _downloadSelectedCities() async {
    // TODO: İndirme işlemi
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(AppLocalizations.instance.citiesDownloading),
        backgroundColor: bgCardLight,
        behavior: SnackBarBehavior.floating,
        duration: const Duration(milliseconds: 1200),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      ),
    );
  }



  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFFCFCFC),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(
            Icons.arrow_back_ios_new_rounded,
            color: Color(0xFF2D3436),
          ),
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          AppLocalizations.instance.settings,
          style: const TextStyle(
            color: Color(0xFF2D3436),
            fontWeight: FontWeight.w700,
          ),
        ),
        centerTitle: true,
      ),
      body: _loading
          ? const Center(child: CircularProgressIndicator())
          : ListView(
              padding: const EdgeInsets.all(20),
              children: [
                // Depolama
                _buildSectionTitle(AppLocalizations.instance.storageData),
                const SizedBox(height: 10),

                _buildSwitchTile(
                  icon: Icons.hd_outlined,
                  iconColor: const Color(0xFF0984E3),
                  title: AppLocalizations.instance.highQualityPhotos,
                  subtitle: AppLocalizations.instance.highQualityPhotosDesc,
                  value: _highQualityPhotos,
                  onChanged: _toggleHighQualityPhotos,
                ),
                _buildSwitchTile(
                  icon: Icons.download_for_offline_outlined,
                  iconColor: const Color(0xFF6C5CE7),
                  title: AppLocalizations.instance.autoDownload,
                  subtitle: AppLocalizations.instance.autoDownloadDesc,
                  value: _autoDownload,
                  onChanged: _toggleAutoDownload,
                ),
                
                const SizedBox(height: 20),
                
                // İNDİRİLENLER
                _buildSectionTitle(AppLocalizations.instance.cityContent),
                const SizedBox(height: 10),
                _buildInfoTile(
                  icon: Icons.sd_storage_outlined,
                  iconColor: const Color(0xFFFF7675),
                  title: AppLocalizations.instance.cacheSize,
                  value: _cacheSize,
                ),
                _buildInfoTile(
                  icon: Icons.sync,
                  iconColor: const Color(0xFF00CEC9),
                  title: AppLocalizations.instance.lastSync,
                  value: _lastUpdate,
                ),
                
                const SizedBox(height: 10),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: Row(
                    children: [
                      Expanded(
                        child: ElevatedButton.icon(
                          onPressed: _showDownloadDialog,
                          icon: const Icon(Icons.download),
                          label: Text(AppLocalizations.instance.download),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: const Color(0xFF00B894),
                            foregroundColor: Colors.white,
                            padding: const EdgeInsets.symmetric(vertical: 12),
                            elevation: 0,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                      ),
                      const SizedBox(width: 12),
                      Expanded(
                        child: ElevatedButton.icon(
                          onPressed: _cacheSize == "0 B" ? null : _clearCache,
                          icon: const Icon(Icons.delete_outline),
                          label: Text(AppLocalizations.instance.clearData),
                          style: ElevatedButton.styleFrom(
                            backgroundColor: const Color(0xFFFF7675).withOpacity(0.1),
                            foregroundColor: const Color(0xFFFF7675),
                            padding: const EdgeInsets.symmetric(vertical: 12),
                            elevation: 0,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                
                const SizedBox(height: 30),
                
                // GENEL
                _buildSectionTitle(AppLocalizations.instance.general),
                const SizedBox(height: 10),
                _buildNetworkStatus(),
                
                const SizedBox(height: 40),
              ],
            ),
    );
  }

  Widget _buildNetworkStatus() {
    final isOnline = _cacheService.isOnline;

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: isOnline
              ? [const Color(0xFF00B894), const Color(0xFF00CEC9)]
              : [Colors.grey.shade400, Colors.grey.shade500],
        ),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(
              isOnline ? Icons.wifi_rounded : Icons.wifi_off_rounded,
              color: Colors.white,
              size: 28,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  isOnline ? "Çevrimiçi" : "Çevrimdışı",
                  style: const TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w700,
                    color: Colors.white,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  isOnline
                      ? "Tüm özellikler kullanılabilir"
                      : "Sadece indirilen şehirler",
                  style: TextStyle(
                    fontSize: 13,
                    color: Colors.white.withOpacity(0.9),
                  ),
                ),
              ],
            ),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 8,
                  height: 8,
                  decoration: BoxDecoration(
                    color: isOnline ? Colors.greenAccent : Colors.orange,
                    shape: BoxShape.circle,
                  ),
                ),
                const SizedBox(width: 6),
                Text(
                  isOnline ? "Bağlı" : "Offline",
                  style: const TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                    color: Colors.white,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSectionTitle(String title) {
    return Text(
      title,
      style: const TextStyle(
        fontSize: 14,
        fontWeight: FontWeight.w600,
        color: Color(0xFF636E72),
        letterSpacing: 0.5,
      ),
    );
  }

  Widget _buildSwitchTile({
    required IconData icon,
    required Color iconColor,
    required String title,
    required String subtitle,
    required bool value,
    required Function(bool) onChanged,
  }) {
    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: iconColor.withOpacity(0.12),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: iconColor, size: 22),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: const TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: Color(0xFF2D3436),
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  subtitle,
                  style: TextStyle(fontSize: 13, color: Colors.grey.shade500),
                ),
              ],
            ),
          ),
          Switch.adaptive(
            value: value,
            onChanged: onChanged,
            activeColor: const Color(0xFF00B894),
          ),
        ],
      ),
    );
  }

  Widget _buildInfoTile({
    required IconData icon,
    required Color iconColor,
    required String title,
    required String value,
  }) {
    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.04),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: iconColor.withOpacity(0.12),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Icon(icon, color: iconColor, size: 22),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Text(
              title,
              style: const TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.w600,
                color: Color(0xFF2D3436),
              ),
            ),
          ),
          Text(
            value,
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.w500,
              color: Colors.grey.shade600,
            ),
          ),
        ],
      ),
    );
  }

  String _formatDate(DateTime date) {
    final now = DateTime.now();
    final diff = now.difference(date);

    if (diff.inMinutes < 1) return "Az önce";
    if (diff.inMinutes < 60) return "${diff.inMinutes} dk önce";
    if (diff.inHours < 24) return "${diff.inHours} saat önce";
    if (diff.inDays < 7) return "${diff.inDays} gün önce";

    return "${date.day}/${date.month}/${date.year}";
  }
}

extension StringExtension on String {
  String capitalize() {
    if (isEmpty) return this;
    return '${this[0].toUpperCase()}${substring(1)}';
  }
}
