import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../l10n/app_localizations.dart';
import '../models/city_model.dart';
import '../models/chat_message.dart';
import '../services/ai_service.dart';
import '../services/city_data_loader.dart';
import '../services/premium_service.dart';
import 'detail_screen.dart';
import 'paywall_screen.dart';

class AIChatScreen extends StatefulWidget {
  final CityModel? city;
  final AIService aiService;
  final List<Highlight> allHighlights;
  final List<ChatMessage> initialMessages;
  final Function(ChatMessage) onMessageAdded;

  const AIChatScreen({
    super.key,
    required this.city,
    required this.aiService,
    required this.allHighlights,
    required this.initialMessages,
    required this.onMessageAdded,
  });

  @override
  State<AIChatScreen> createState() => _AIChatScreenState();
}

class _AIChatScreenState extends State<AIChatScreen> {
  final ScrollController _scrollController = ScrollController();
  late List<ChatMessage> _messages;
  bool _isLoading = false;
  bool _showingHistory = false; // Geçmiş görünümü mü?

  // Colors
  static const Color bgDark = Color(0xFF0D0D1A);
  static const Color bgCard = Color(0xFF1C1C2E);
  static const Color accent = Color(0xFF9B8FE8);
  static const Color textWhite = Color(0xFFFFFFFF);
  static const Color textGrey = Color(0xFF9CA3AF);
  static const Color borderColor = Color(0xFF2D2D4A);

  List<String> get _quickQuestions => [
    // Yemek & İçecek
    AppLocalizations.instance.bestCoffeeWhere,
    AppLocalizations.instance.localFoodWhere,
    AppLocalizations.instance.bestBrunchSpots,
    AppLocalizations.instance.rooftopBars,
    
    // Keşif & Gizli Yerler
    AppLocalizations.instance.hiddenGems,
    AppLocalizations.instance.offTheBeatenPath,
    
    // Doğa & Manzara
    AppLocalizations.instance.sunsetSpotWhere,
    AppLocalizations.instance.quietParkSuggest,
    AppLocalizations.instance.bestViewpoints,
    
    // Kültür & Sanat
    AppLocalizations.instance.mustSeeMuseums,
    AppLocalizations.instance.artGalleries,
    
    // Romantik & Özel
    AppLocalizations.instance.romanticDinnerSpot,
    AppLocalizations.instance.uniqueDateIdeas,
  ];

  @override
  void initState() {
    super.initState();
    _messages = List.from(widget.initialMessages);
  }

  @override
  void dispose() {
    _scrollController.dispose();
    super.dispose();
  }

  void _scrollToBottom() {
    if (_scrollController.hasClients) {
      Future.delayed(const Duration(milliseconds: 100), () {
        if (_scrollController.hasClients) {
          _scrollController.animateTo(
            _scrollController.position.maxScrollExtent,
            duration: const Duration(milliseconds: 300),
            curve: Curves.easeOut,
          );
        }
      });
    }
  }

  Future<void> _sendMessage(String text) async {
    if (text.trim().isEmpty) return;

    // Premium limit kontrolü (My Way Asistan)
    if (!PremiumService.instance.canUseMyWay()) {
      _showPaywall();
      return;
    }

    final userMsg = ChatMessage(text: text, isUser: true);
    widget.onMessageAdded(userMsg);
    setState(() {
      _messages.add(userMsg);
      _isLoading = true;
      _showingHistory = true; // Mesaj gönderilince geçmiş görünümüne geç
    });
    _scrollToBottom();
    
    // Kullanımı artır
    await PremiumService.instance.useMyWay();

    try {
      final cityName = widget.city?.city ?? 'şehir';
      final response = await widget.aiService.getChatResponse(
        cityName: cityName,
        question: text,
        interests: [],
        places: widget.allHighlights
            .map((h) => {
                  'name': h.name,
                  'category': AppLocalizations.instance.translateCategory(h.category),
                  'rating': h.rating,
                  'description': AppLocalizations.instance.isEnglish ? (h.descriptionEn ?? h.description) : h.description,
                })
            .toList(),
        isEnglish: AppLocalizations.instance.isEnglish,
      );

      if (mounted) {
        final aiMsg = ChatMessage(text: response, isUser: false);
        widget.onMessageAdded(aiMsg);
        setState(() {
          _messages.add(aiMsg);
          _isLoading = false;
        });
        _scrollToBottom();
      }
    } catch (e) {
      if (mounted) {
        final errorMsg = ChatMessage(
            text: AppLocalizations.instance.aiErrorMessage,
            isUser: false,
        );
        widget.onMessageAdded(errorMsg);
        
        setState(() {
          _messages.add(errorMsg);
          _isLoading = false;
        });
      }
    }
  }

  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }

  void _navigateToPlace(String query) async {
    try {
      String? targetCity;
      String searchPlace = query;

      // 1. Önce mevcut şehrin highlight'larında ara
      Highlight? foundPlace;
      try {
        foundPlace = widget.allHighlights.firstWhere(
          (h) => h.name.toLowerCase().trim() == searchPlace.toLowerCase().trim() || 
                 searchPlace.toLowerCase().contains(h.name.toLowerCase().trim()) ||
                 h.name.toLowerCase().contains(searchPlace.toLowerCase().trim())
        );
      } catch (_) {}

      // 2. Bulunamadıysa cross-city ara
      if (foundPlace == null) {
        // Query içinde şehir adı var mı kontrol et
        final allCities = CityDataLoader.supportedCities;
        for (var cityId in allCities) {
          if (query.toLowerCase().contains(cityId)) {
            targetCity = cityId;
            break;
          }
        }

        List<String> citiesToSearch = targetCity != null 
            ? [targetCity] 
            : ['roma', 'paris', 'barcelona', 'istanbul', 'londra', 'viyana', 'prag', 'lizbon', 'rovaniemi', 'matera', 'sintra', 'colmar', 'newyork', 'seul', 'singapur', 'tokyo'];
        
        for (var cityId in citiesToSearch) {
          try {
            final cityModel = await CityDataLoader.loadCity(cityId);
            foundPlace = cityModel.highlights.firstWhere(
              (h) {
                final hName = h.name.toLowerCase().trim();
                final sName = searchPlace.toLowerCase().trim();
                return hName == sName || sName.contains(hName) || hName.contains(sName);
              }
            );
            if (foundPlace != null) break;
          } catch (_) {}
        }
      }

      if (foundPlace != null && mounted) {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => DetailScreen(place: foundPlace!)),
        );
      } else {
         ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(AppLocalizations.instance.isEnglish ? "Place not found: $query" : "Yer bulunamadı: $query"),
            backgroundColor: borderColor,
            behavior: SnackBarBehavior.floating,
          ),
        );
      }
    } catch (e) {
      debugPrint('Place navigation error: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: bgDark,
      appBar: AppBar(
        backgroundColor: bgDark,
        elevation: 0,
        scrolledUnderElevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_ios_new_rounded, color: textWhite, size: 20),
          onPressed: () {
            if (_showingHistory) {
              setState(() => _showingHistory = false);
            } else {
              Navigator.pop(context);
            }
          },
        ),
        titleSpacing: 0,
        title: Row(
          children: [
            Container(
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: accent, // iOS icon background color
                borderRadius: BorderRadius.circular(10),
              ),
              child: Image.asset(
                'assets/images/splash_logo.png',
                width: 24,
                height: 24,
                fit: BoxFit.contain,
              ),
            ),
            const SizedBox(width: 12),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  AppLocalizations.instance.aiAssistant,
                  style: const TextStyle(
                    color: textWhite,
                    fontSize: 16,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                Text(
                  widget.city?.city ?? AppLocalizations.instance.city,
                  style: TextStyle(
                    color: textWhite.withOpacity(0.6),
                    fontSize: 12,
                    fontWeight: FontWeight.w400,
                  ),
                ),
              ],
            ),
          ],
        ),
        actions: [
          // Geçmiş butonu (mesaj varsa göster)
          if (_messages.isNotEmpty && !_showingHistory)
            IconButton(
              icon: Stack(
                children: [
                  const Icon(Icons.history_rounded, color: textWhite, size: 24),
                  Positioned(
                    right: 0,
                    top: 0,
                    child: Container(
                      padding: const EdgeInsets.all(4),
                      decoration: const BoxDecoration(
                        color: accent,
                        shape: BoxShape.circle,
                      ),
                      child: Text(
                        _messages.length.toString(),
                        style: const TextStyle(color: textWhite, fontSize: 10, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ),
                ],
              ),
              onPressed: () => setState(() => _showingHistory = true),
              tooltip: AppLocalizations.instance.isEnglish ? "Chat History" : "Sohbet Geçmişi",
            ),
          const SizedBox(width: 8),
        ],
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(1),
          child: Container(color: borderColor, height: 1),
        ),
      ),
      body: _showingHistory ? _buildHistoryView() : _buildHomeView(),
    );
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // ANA SAYFA (Home View) - Hoş geldin + Ortada dağınık sorular
  // ═══════════════════════════════════════════════════════════════════════════
  Widget _buildHomeView() {
    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Logo
            Container(
              padding: const EdgeInsets.all(28),
              decoration: BoxDecoration(
                color: accent, // iOS icon background color
                shape: BoxShape.circle,
              ),
              child: Image.asset(
                'assets/images/splash_logo.png',
                width: 60,
                height: 60,
                fit: BoxFit.contain,
              ),
            ),
            const SizedBox(height: 28),
            
            // Hoş geldin mesajı
            Text(
              AppLocalizations.instance.helloAI,
              style: const TextStyle(
                color: textWhite,
                fontSize: 24,
                fontWeight: FontWeight.w700,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 12),
            Text(
              AppLocalizations.instance.askAnythingAboutCity(widget.city?.city ?? AppLocalizations.instance.city),
              style: const TextStyle(color: textGrey, fontSize: 15, height: 1.5),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 40),
            
            // Örnek Sorular başlığı
            Text(
              AppLocalizations.instance.exampleQuestions,
              style: TextStyle(
                color: textGrey.withOpacity(0.6), 
                fontSize: 12, 
                fontWeight: FontWeight.w600, 
                letterSpacing: 0.5
              ),
            ),
            const SizedBox(height: 20),
            
            // Sorular - Ortada dağınık (Wrap)
            Wrap(
              spacing: 12,
              runSpacing: 12,
              alignment: WrapAlignment.center,
              children: _quickQuestions.map((q) => _buildQuestionCard(q)).toList(),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildQuestionCard(String question) {
    return GestureDetector(
      onTap: _isLoading ? null : () => _sendMessage(question),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
        decoration: BoxDecoration(
          color: bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: accent.withOpacity(0.2)),
          boxShadow: [
            BoxShadow(
              color: accent.withOpacity(0.05),
              blurRadius: 10,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(Icons.chat_bubble_outline_rounded, size: 18, color: accent),
            const SizedBox(width: 10),
            Flexible(
              child: Text(
                question,
                style: const TextStyle(
                  color: textWhite, 
                  fontSize: 14, 
                  fontWeight: FontWeight.w500
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // ═══════════════════════════════════════════════════════════════════════════
  // GEÇMİŞ GÖRÜNÜMÜ (History View) - Mesaj listesi + Alt panel
  // ═══════════════════════════════════════════════════════════════════════════
  Widget _buildHistoryView() {
    return Column(
      children: [
        Expanded(
          child: ListView.builder(
            controller: _scrollController,
            padding: const EdgeInsets.all(16),
            itemCount: _messages.length + (_isLoading ? 1 : 0),
            itemBuilder: (context, index) {
              if (index == _messages.length && _isLoading) {
                return _buildTypingIndicator();
              }
              return _buildMessageBubble(_messages[index]);
            },
          ),
        ),
        _buildSelectionPanel(),
      ],
    );
  }

  Widget _buildSelectionPanel() {
    return Container(
      padding: EdgeInsets.fromLTRB(16, 16, 16, MediaQuery.of(context).padding.bottom + 16),
      decoration: BoxDecoration(
        color: bgCard,
        border: Border(top: BorderSide(color: borderColor)),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.2),
            blurRadius: 10,
            offset: const Offset(0, -5),
          ),
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            AppLocalizations.instance.askAnotherQuestion,
            style: const TextStyle(color: textGrey, fontSize: 13, fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 12),
          SingleChildScrollView(
            scrollDirection: Axis.horizontal,
            child: Row(
              children: _quickQuestions.map((q) {
                return Padding(
                  padding: const EdgeInsets.only(right: 10),
                  child: _buildSelectionChip(q),
                );
              }).toList(),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSelectionChip(String question) {
    return GestureDetector(
      onTap: _isLoading ? null : () => _sendMessage(question),
      child: Opacity(
        opacity: _isLoading ? 0.5 : 1.0,
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          decoration: BoxDecoration(
            color: bgDark,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: accent.withOpacity(0.3)),
          ),
          child: Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.chat_bubble_outline_rounded, size: 16, color: accent),
              const SizedBox(width: 8),
              Text(
                question,
                style: const TextStyle(color: textWhite, fontSize: 13, fontWeight: FontWeight.w500),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildMessageBubble(ChatMessage message) {
    final isUser = message.isUser;

    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Row(
        mainAxisAlignment: isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (!isUser) ...[
            Container(
              margin: const EdgeInsets.only(top: 4),
              padding: const EdgeInsets.all(6),
              decoration: BoxDecoration(
                color: accent,
                shape: BoxShape.circle,
              ),
              child: Image.asset(
                'assets/images/splash_logo.png',
                width: 14,
                height: 14,
                fit: BoxFit.contain,
              ),
            ),
            const SizedBox(width: 10),
          ],
          Flexible(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 18, vertical: 14),
              decoration: BoxDecoration(
                color: isUser ? accent : bgCard,
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(20),
                  topRight: const Radius.circular(20),
                  bottomLeft: Radius.circular(isUser ? 20 : 4),
                  bottomRight: Radius.circular(isUser ? 4 : 20),
                ),
                border: isUser ? null : Border.all(color: borderColor),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.05),
                    blurRadius: 10,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: isUser
                  ? Text(
                      message.text,
                      style: const TextStyle(
                        color: textWhite,
                        fontSize: 15,
                        height: 1.4,
                      ),
                    )
                  : _buildParsedMessage(message.text),
            ),
          ),
          if (isUser) const SizedBox(width: 8),
        ],
      ),
    );
  }

  Widget _buildParsedMessage(String text) {
    final linkPattern = RegExp(r'\[([^\]]+)\]\(search:([^\)]+)\)');
    final List<InlineSpan> spans = [];
    int lastEnd = 0;

    for (final match in linkPattern.allMatches(text)) {
      if (match.start > lastEnd) {
        spans.add(TextSpan(
          text: text.substring(lastEnd, match.start),
          style: const TextStyle(color: textWhite, fontSize: 15, height: 1.5),
        ));
      }

      final displayName = match.group(1)!;
      final searchName = match.group(2)!;
      
      spans.add(WidgetSpan(
        alignment: PlaceholderAlignment.middle,
        child: GestureDetector(
          onTap: () {
            HapticFeedback.selectionClick();
            _navigateToPlace(searchName);
          },
          child: Container(
            constraints: BoxConstraints(
              maxWidth: MediaQuery.of(context).size.width * 0.6, // %60 screen width max
            ),
            margin: const EdgeInsets.symmetric(horizontal: 2, vertical: 2),
            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
            decoration: BoxDecoration(
              color: accent.withOpacity(0.12),
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: accent.withOpacity(0.35), width: 1),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                const Icon(Icons.location_on_rounded, size: 14, color: accent),
                const SizedBox(width: 4),
                Flexible(
                  child: Text(
                    displayName,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 13,
                      fontWeight: FontWeight.w600,
                      letterSpacing: -0.2,
                    ),
                    overflow: TextOverflow.ellipsis,
                    maxLines: 1,
                  ),
                ),
              ],
            ),
          ),
        ),
      ));

      lastEnd = match.end;
    }

    if (lastEnd < text.length) {
      spans.add(TextSpan(
        text: text.substring(lastEnd),
        style: const TextStyle(color: textWhite, fontSize: 15, height: 1.5),
      ));
    }

    if (spans.isEmpty) {
      return Text(
        text,
        style: const TextStyle(color: textWhite, fontSize: 15, height: 1.5),
      );
    }

    return RichText(
      text: TextSpan(children: spans),
    );
  }

  Widget _buildTypingIndicator() {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(
              color: accent,
              shape: BoxShape.circle,
            ),
            child: Image.asset(
              'assets/images/splash_logo.png',
              width: 14,
              height: 14,
              fit: BoxFit.contain,
            ),
          ),
          const SizedBox(width: 10),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
            decoration: BoxDecoration(
              color: bgCard,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: borderColor),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                _buildDot(0),
                const SizedBox(width: 4),
                _buildDot(1),
                const SizedBox(width: 4),
                _buildDot(2),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDot(int index) {
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0, end: 1),
      duration: const Duration(milliseconds: 600),
      curve: Curves.easeInOut,
      builder: (context, value, child) {
        final offset = (value + index * 0.2) % 1.0;
        return Transform.translate(
          offset: Offset(0, -3 * (offset < 0.5 ? offset : (1 - offset))),
          child: Container(
            width: 6,
            height: 6,
            decoration: BoxDecoration(
              color: textGrey,
              shape: BoxShape.circle,
            ),
          ),
        );
      },
    );
  }
}
