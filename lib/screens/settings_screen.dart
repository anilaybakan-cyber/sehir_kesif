// =============================================================================
// SETTINGS SCREEN - Offline Mod, Cache, Fotoğraf Ayarları
// =============================================================================

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../services/cache_service.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  bool _offlineMode = false;
  bool _highQualityPhotos = true;
  bool _autoDownload = true;
  String _cacheSize = "Hesaplanıyor...";
  List<String> _cachedCities = [];
  DateTime? _lastSync;
  bool _loading = true;

  final CacheService _cacheService = CacheService();

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
    final offlineMode = await _cacheService.isOfflineModeEnabled();

    setState(() {
      _offlineMode = offlineMode;
      _highQualityPhotos = prefs.getBool('high_quality_photos') ?? true;
      _autoDownload = prefs.getBool('auto_download_cities') ?? true;
      _cacheSize = _cacheService.formatCacheSize(cacheSize);
      _cachedCities = cachedCities;
      _lastSync = lastSync;
      _loading = false;
    });
  }

  Future<void> _toggleOfflineMode(bool value) async {
    HapticFeedback.selectionClick();
    await _cacheService.setOfflineMode(value);
    setState(() => _offlineMode = value);

    if (value && _cachedCities.isEmpty) {
      _showDownloadDialog();
    }
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
    final confirm = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text("Cache'i Temizle"),
        content: const Text(
          "Tüm indirilen şehir verileri silinecek. Offline modda kullanılamayacaklar.\n\nDevam etmek istiyor musun?",
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: const Text("İptal"),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            style: TextButton.styleFrom(foregroundColor: Colors.red),
            child: const Text("Temizle"),
          ),
        ],
      ),
    );

    if (confirm == true) {
      await _cacheService.clearAllCache();
      await _loadSettings();

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: const Text("Cache temizlendi"),
            backgroundColor: const Color(0xFF2D3436),
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(12),
            ),
          ),
        );
      }
    }
  }

  void _showDownloadDialog() {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => Container(
        decoration: const BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.vertical(top: Radius.circular(24)),
        ),
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Container(
              width: 40,
              height: 4,
              decoration: BoxDecoration(
                color: Colors.grey.shade300,
                borderRadius: BorderRadius.circular(2),
              ),
            ),
            const SizedBox(height: 24),
            const Icon(
              Icons.download_for_offline_rounded,
              size: 48,
              color: Color(0xFF00B894),
            ),
            const SizedBox(height: 16),
            const Text(
              "Şehirleri İndir",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.w700),
            ),
            const SizedBox(height: 8),
            Text(
              "Offline modda kullanmak için şehirleri şimdi indirebilirsin.",
              style: TextStyle(fontSize: 14, color: Colors.grey.shade600),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 24),
            _buildCityDownloadTile("Barcelona", true),
            _buildCityDownloadTile("Paris", false),
            _buildCityDownloadTile("Roma", false),
            _buildCityDownloadTile("İstanbul", false),
            const SizedBox(height: 24),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: () {
                  Navigator.pop(context);
                  _downloadSelectedCities();
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: const Color(0xFF00B894),
                  foregroundColor: Colors.white,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16),
                  ),
                ),
                child: const Text(
                  "Seçilenleri İndir",
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600),
                ),
              ),
            ),
            const SizedBox(height: 16),
          ],
        ),
      ),
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
                  isDownloaded ? "İndirildi • ~2 MB" : "~2 MB",
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
        content: const Text("Şehirler indiriliyor..."),
        backgroundColor: const Color(0xFF2D3436),
        behavior: SnackBarBehavior.floating,
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
        title: const Text(
          "Ayarlar",
          style: TextStyle(
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
                // Network Durumu
                _buildNetworkStatus(),
                const SizedBox(height: 24),

                // Offline Mod
                _buildSectionTitle("Offline Mod"),
                const SizedBox(height: 12),
                _buildSwitchTile(
                  icon: Icons.offline_bolt_rounded,
                  iconColor: const Color(0xFF6C5CE7),
                  title: "Offline Mod",
                  subtitle: "İnternet olmadan da kullan",
                  value: _offlineMode,
                  onChanged: _toggleOfflineMode,
                ),
                const SizedBox(height: 12),
                _buildSwitchTile(
                  icon: Icons.download_rounded,
                  iconColor: const Color(0xFF00B894),
                  title: "Otomatik İndirme",
                  subtitle: "Yeni şehirleri WiFi'da indir",
                  value: _autoDownload,
                  onChanged: _toggleAutoDownload,
                ),
                const SizedBox(height: 24),

                // Fotoğraf Ayarları
                _buildSectionTitle("Fotoğraflar"),
                const SizedBox(height: 12),
                _buildSwitchTile(
                  icon: Icons.high_quality_rounded,
                  iconColor: const Color(0xFF0984E3),
                  title: "Yüksek Kalite",
                  subtitle: "Daha net fotoğraflar, daha fazla veri",
                  value: _highQualityPhotos,
                  onChanged: _toggleHighQualityPhotos,
                ),
                const SizedBox(height: 24),

                // Cache Yönetimi
                _buildSectionTitle("Depolama"),
                const SizedBox(height: 12),
                _buildInfoTile(
                  icon: Icons.storage_rounded,
                  iconColor: const Color(0xFFFDAA5D),
                  title: "Cache Boyutu",
                  value: _cacheSize,
                ),
                const SizedBox(height: 12),
                _buildInfoTile(
                  icon: Icons.location_city_rounded,
                  iconColor: const Color(0xFF00B894),
                  title: "İndirilen Şehirler",
                  value: _cachedCities.isEmpty
                      ? "Henüz yok"
                      : _cachedCities.map((c) => c.capitalize()).join(", "),
                ),
                const SizedBox(height: 12),
                _buildInfoTile(
                  icon: Icons.sync_rounded,
                  iconColor: const Color(0xFF74B9FF),
                  title: "Son Güncelleme",
                  value: _lastSync != null
                      ? _formatDate(_lastSync!)
                      : "Henüz yok",
                ),
                const SizedBox(height: 24),

                // Temizle butonu
                GestureDetector(
                  onTap: _clearCache,
                  child: Container(
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(
                      color: Colors.red.shade50,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(color: Colors.red.shade200),
                    ),
                    child: Row(
                      children: [
                        Icon(
                          Icons.delete_outline_rounded,
                          color: Colors.red.shade400,
                          size: 24,
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                "Cache'i Temizle",
                                style: TextStyle(
                                  fontSize: 16,
                                  fontWeight: FontWeight.w600,
                                  color: Colors.red.shade700,
                                ),
                              ),
                              const SizedBox(height: 2),
                              Text(
                                "Tüm indirilen verileri sil",
                                style: TextStyle(
                                  fontSize: 13,
                                  color: Colors.red.shade400,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Icon(
                          Icons.chevron_right_rounded,
                          color: Colors.red.shade300,
                        ),
                      ],
                    ),
                  ),
                ),

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
