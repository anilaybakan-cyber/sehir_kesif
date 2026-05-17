import 'dart:io' show Platform;
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:url_launcher/url_launcher.dart';
import '../services/remote_config_service.dart';
import '../l10n/app_localizations.dart';
import '../theme/wanderlust_colors.dart';

class ForceUpdateScreen extends StatelessWidget {
  const ForceUpdateScreen({super.key});

  String get _storeUrl {
    if (Platform.isIOS) {
      return RemoteConfigService.instance.storeUrlIOS;
    }
    return RemoteConfigService.instance.storeUrlAndroid;
  }

  Future<void> _openStore() async {
    final url = _storeUrl;
    final uri = Uri.parse(url);
    try {
      if (await canLaunchUrl(uri)) {
        await launchUrl(uri, mode: LaunchMode.externalApplication);
      }
    } catch (e) {
      debugPrint("Could not launch store URL: $e");
    }
  }

  @override
  Widget build(BuildContext context) {
    final isEnglish = AppLocalizations.instance.isEnglish;
    
    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      body: Stack(
        children: [
          // Background Gradient Overlay
          Positioned.fill(
            child: Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  begin: Alignment.topCenter,
                  end: Alignment.bottomCenter,
                  colors: [
                    WanderlustColors.accent.withOpacity(0.05),
                    WanderlustColors.bgDark,
                  ],
                ),
              ),
            ),
          ),
          
          SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 40),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  // Icon with soft glow
                  Container(
                    padding: const EdgeInsets.all(24),
                    decoration: BoxDecoration(
                      color: WanderlustColors.accent.withOpacity(0.1),
                      shape: BoxShape.circle,
                    ),
                    child: Icon(
                      Icons.system_update_rounded,
                      size: 64,
                      color: WanderlustColors.accent,
                    ),
                  ),
                  
                  const SizedBox(height: 40),
                  
                  Text(
                    isEnglish ? "Update Required" : "Güncelleme Gerekli",
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      color: WanderlustColors.textWhite,
                      fontSize: 28,
                      fontWeight: FontWeight.bold,
                      letterSpacing: -0.5,
                    ),
                  ),
                  
                  const SizedBox(height: 16),
                  
                  Text(
                    isEnglish
                        ? "A new version of MyWay is available. Please update to enjoy the latest features and improvements."
                        : "MyWay'in yeni bir sürümü mevcut. En yeni özellikleri ve iyileştirmeleri kullanmaya devam etmek için lütfen güncelleyin.",
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: WanderlustColors.textGrey,
                      fontSize: 16,
                      height: 1.6,
                    ),
                  ),
                  
                  const SizedBox(height: 56),
                  
                  // Premium Button
                  Container(
                    width: double.infinity,
                    height: 60,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(20),
                      gradient: WanderlustColors.accentGradient,
                      boxShadow: [
                        BoxShadow(
                          color: WanderlustColors.accent.withOpacity(0.3),
                          blurRadius: 20,
                          offset: const Offset(0, 8),
                        ),
                      ],
                    ),
                    child: ElevatedButton(
                      onPressed: () {
                        HapticFeedback.heavyImpact();
                        _openStore();
                      },
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.transparent,
                        shadowColor: Colors.transparent,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(20),
                        ),
                      ),
                      child: Text(
                        isEnglish ? "Update Now" : "Şimdi Güncelle",
                        style: const TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          letterSpacing: 0.5,
                        ),
                      ),
                    ),
                  ),
                  
                  const SizedBox(height: 24),
                  
                  Text(
                    isEnglish
                        ? "The app will remain locked until you update."
                        : "Güncelleme yapana kadar uygulama kilitli kalacaktır.",
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: WanderlustColors.textGreyLight,
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}

