// =============================================================================
// NOTIFICATIONS SCREEN – Bildirim Geçmişi
// =============================================================================

import 'package:flutter/material.dart';
import '../services/notification_service.dart';
import '../theme/wanderlust_colors.dart';
import '../l10n/app_localizations.dart';

class NotificationsScreen extends StatefulWidget {
  const NotificationsScreen({super.key});

  @override
  State<NotificationsScreen> createState() => _NotificationsScreenState();
}

class _NotificationsScreenState extends State<NotificationsScreen> {
  List<Map<String, dynamic>> _notifications = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadNotifications();
  }

  Future<void> _loadNotifications() async {
    final notifications = await NotificationService().getNotifications();
    setState(() {
      _notifications = notifications;
      _isLoading = false;
    });
    // Mark all as read when viewing
    await NotificationService().markAllAsRead();
  }

  Future<void> _clearAll() async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: WanderlustColors.bgCard,
        title: Text(
          AppLocalizations.currentLanguage == AppLanguage.en 
              ? 'Clear All Notifications' 
              : 'Tüm Bildirimleri Sil',
          style: const TextStyle(color: Colors.white),
        ),
        content: Text(
          AppLocalizations.currentLanguage == AppLanguage.en
              ? 'Are you sure you want to delete all notifications?'
              : 'Tüm bildirimleri silmek istediğinizden emin misiniz?',
          style: const TextStyle(color: Colors.white70),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(
              AppLocalizations.currentLanguage == AppLanguage.en ? 'Cancel' : 'İptal',
              style: const TextStyle(color: Colors.white54),
            ),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(
              AppLocalizations.currentLanguage == AppLanguage.en ? 'Delete' : 'Sil',
              style: const TextStyle(color: Colors.red),
            ),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      await NotificationService().clearNotifications();
      setState(() {
        _notifications = [];
      });
    }
  }

  String _formatDate(String isoString) {
    try {
      final date = DateTime.parse(isoString);
      final now = DateTime.now();
      final diff = now.difference(date);

      if (diff.inMinutes < 1) {
        return AppLocalizations.currentLanguage == AppLanguage.en ? 'Just now' : 'Az önce';
      } else if (diff.inMinutes < 60) {
        return '${diff.inMinutes} ${AppLocalizations.currentLanguage == AppLanguage.en ? 'min ago' : 'dk önce'}';
      } else if (diff.inHours < 24) {
        return '${diff.inHours} ${AppLocalizations.currentLanguage == AppLanguage.en ? 'hours ago' : 'saat önce'}';
      } else if (diff.inDays < 7) {
        return '${diff.inDays} ${AppLocalizations.currentLanguage == AppLanguage.en ? 'days ago' : 'gün önce'}';
      } else {
        return '${date.day}.${date.month}.${date.year}';
      }
    } catch (e) {
      return '';
    }
  }

  @override
  Widget build(BuildContext context) {
    final isEnglish = AppLocalizations.currentLanguage == AppLanguage.en;

    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      appBar: AppBar(
        backgroundColor: WanderlustColors.bgDark,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_ios, color: Colors.white),
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          isEnglish ? 'Notifications' : 'Bildirimler',
          style: const TextStyle(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.w600,
          ),
        ),
        actions: [
          if (_notifications.isNotEmpty)
            IconButton(
              icon: const Icon(Icons.delete_outline, color: Colors.white54),
              onPressed: _clearAll,
              tooltip: isEnglish ? 'Clear all' : 'Tümünü sil',
            ),
        ],
      ),
      body: _isLoading
          ? const Center(
              child: CircularProgressIndicator(color: WanderlustColors.accent),
            )
          : _notifications.isEmpty
              ? _buildEmptyState(isEnglish)
              : _buildNotificationsList(),
    );
  }

  Widget _buildEmptyState(bool isEnglish) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            width: 100,
            height: 100,
            decoration: BoxDecoration(
              color: WanderlustColors.bgCard,
              borderRadius: BorderRadius.circular(50),
            ),
            child: const Icon(
              Icons.notifications_none_rounded,
              size: 48,
              color: Colors.white24,
            ),
          ),
          const SizedBox(height: 24),
          Text(
            isEnglish ? 'No notifications yet' : 'Henüz bildirim yok',
            style: const TextStyle(
              color: Colors.white,
              fontSize: 18,
              fontWeight: FontWeight.w600,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            isEnglish
                ? 'You\'ll see your notifications here'
                : 'Bildirimleriniz burada görünecek',
            style: const TextStyle(
              color: Colors.white54,
              fontSize: 14,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildNotificationsList() {
    return ListView.separated(
      padding: const EdgeInsets.all(16),
      itemCount: _notifications.length,
      separatorBuilder: (_, __) => const SizedBox(height: 12),
      itemBuilder: (context, index) {
        final notification = _notifications[index];
        return _buildNotificationCard(notification);
      },
    );
  }

  Widget _buildNotificationCard(Map<String, dynamic> notification) {
    final title = notification['title'] as String? ?? '';
    final body = notification['body'] as String? ?? '';
    final timestamp = notification['timestamp'] as String? ?? '';

    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: Colors.white.withOpacity(0.05),
          width: 1,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 40,
                height: 40,
                decoration: BoxDecoration(
                    gradient: LinearGradient(
                    colors: [WanderlustColors.accent, Color(0xFF651FFF)],
                  ),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: const Icon(
                  Icons.notifications_rounded,
                  color: Colors.white,
                  size: 20,
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      title,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.w600,
                      ),
                    ),
                    if (timestamp.isNotEmpty)
                      Text(
                        _formatDate(timestamp),
                        style: const TextStyle(
                          color: Colors.white38,
                          fontSize: 12,
                        ),
                      ),
                  ],
                ),
              ),
            ],
          ),
          if (body.isNotEmpty) ...[
            const SizedBox(height: 12),
            Text(
              body,
              style: const TextStyle(
                color: Colors.white70,
                fontSize: 14,
                height: 1.4,
              ),
            ),
          ],
        ],
      ),
    );
  }
}
