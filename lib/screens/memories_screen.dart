// =============================================================================
// MEMORIES SCREEN
// Tüm seyahat anılarını şehir bazlı görüntüleme
// =============================================================================

import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import '../theme/wanderlust_colors.dart';
import '../l10n/app_localizations.dart';
import '../services/memory_service.dart';
import '../models/travel_memory.dart';
import '../widgets/add_memory_sheet.dart';

class MemoriesScreen extends StatefulWidget {
  const MemoriesScreen({super.key});

  @override
  State<MemoriesScreen> createState() => _MemoriesScreenState();
}

class _MemoriesScreenState extends State<MemoriesScreen> {
  final _memoryService = MemoryService();
  String? _selectedCityFilter;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  @override
  void initState() {
    super.initState();
    _memoryService.initialize();
    _memoryService.memoriesNotifier.addListener(_onMemoriesUpdated);
  }

  @override
  void dispose() {
    _memoryService.memoriesNotifier.removeListener(_onMemoriesUpdated);
    super.dispose();
  }

  void _onMemoriesUpdated() => setState(() {});

  List<TravelMemory> get _filteredMemories {
    if (_selectedCityFilter == null) {
      return _memoryService.memories;
    }
    return _memoryService.getMemoriesByCity(_selectedCityFilter!);
  }

  @override
  Widget build(BuildContext context) {
    // Şehir filtrelemesi yoksa ve birden fazla şehirde anı varsa -> Klasör görünümü
    // Şehir filtrelemesi varsa veya tek şehir varsa -> Grid görünümü
    final cities = _memoryService.citiesWithMemories;
    final showFolders = _selectedCityFilter == null && cities.length > 1;

    // Gösterilecek anılar
    final memories = _filteredMemories;

    return Scaffold(
      backgroundColor: WanderlustColors.bgDark,
      appBar: AppBar(
        backgroundColor: WanderlustColors.bgDark,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_ios_rounded, color: Colors.white),
          onPressed: () {
            if (_selectedCityFilter != null && cities.length > 1) {
              // Filtre varsa geri tuşu klasörlere döner
              setState(() => _selectedCityFilter = null);
            } else {
              Navigator.pop(context);
            }
          },
        ),
        title: Text(
          _selectedCityFilter != null
            ? _memoryService.getMemoriesByCity(_selectedCityFilter!).first.cityName
            : (isEnglish ? 'My Memories' : 'Anılarım'),
          style: const TextStyle(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.w700,
          ),
        ),
        actions: [
          // Filter button (Sadece grid modunda ve birden çok şehir varsa göster)
          if (!showFolders && cities.length > 1)
            PopupMenuButton<String?>(
              icon: Icon(
                _selectedCityFilter != null ? Icons.filter_alt : Icons.filter_alt_outlined,
                color: _selectedCityFilter != null ? WanderlustColors.accent : Colors.white70,
              ),
              color: WanderlustColors.bgCard,
              onSelected: (value) {
                setState(() => _selectedCityFilter = value);
              },
              itemBuilder: (context) => [
                PopupMenuItem(
                  value: null,
                  child: Text(
                    isEnglish ? 'All Folders' : 'Tüm Klasörler',
                    style: const TextStyle(color: Colors.white),
                  ),
                ),
                ...cities.map((cityId) {
                  final cityMemories = _memoryService.getMemoriesByCity(cityId);
                  final cityName = cityMemories.first.cityName;
                  return PopupMenuItem(
                    value: cityId,
                    child: Text(
                      '$cityName (${cityMemories.length})',
                      style: TextStyle(
                        color: _selectedCityFilter == cityId ? WanderlustColors.accent : Colors.white,
                      ),
                    ),
                  );
                }),
              ],
            ),
        ],
      ),
      body: showFolders
          ? _buildCityFolders(cities)
          : (memories.isEmpty
              ? _buildEmptyState()
              : _buildMemoriesGrid(memories)),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () async {
          HapticFeedback.mediumImpact();
          await AddMemorySheet.show(context);
        },
        backgroundColor: WanderlustColors.accent,
        icon: const Icon(Icons.add_a_photo_rounded),
        label: Text(isEnglish ? 'Add Memory' : 'Anı Ekle'),
      ),
    );
  }

  Widget _buildCityFolders(List<String> cities) {
    return CustomScrollView(
      slivers: [
        SliverPadding(
          padding: const EdgeInsets.all(20),
          sliver: SliverGrid(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              mainAxisSpacing: 16,
              crossAxisSpacing: 16,
              childAspectRatio: 0.85,
            ),
            delegate: SliverChildBuilderDelegate(
              (context, index) {
                final cityId = cities[index];
                final cityMemories = _memoryService.getMemoriesByCity(cityId);
                // En yeni anı kapak olsun
                final cover = cityMemories.first; 
                
                return _buildCityFolderCard(
                  cityId: cityId,
                  cityName: cover.cityName,
                  count: cityMemories.length,
                  coverImage: cover.imagePath,
                  onTap: () {
                    setState(() => _selectedCityFilter = cityId);
                  },
                );
              },
              childCount: cities.length,
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildCityFolderCard({
    required String cityId,
    required String cityName,
    required int count,
    required String coverImage,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(20),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.2),
              blurRadius: 8,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(20),
          child: Stack(
            fit: StackFit.expand,
            children: [
              // Cover Image
              Image.file(
                File(coverImage),
                fit: BoxFit.cover,
                errorBuilder: (_, __, ___) => Container(
                  color: WanderlustColors.bgCard,
                  child: const Icon(Icons.broken_image, color: Colors.white38),
                ),
              ),
              
              // Gradient Overlay
              Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.transparent,
                      Colors.black.withOpacity(0.8),
                    ],
                    stops: const [0.5, 1.0],
                  ),
                ),
              ),

              // Folder Icon Badge
              Positioned(
                top: 12,
                right: 12,
                child: Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(
                    color: Colors.black.withOpacity(0.4),
                    shape: BoxShape.circle,
                    border: Border.all(color: Colors.white.withOpacity(0.2)),
                  ),
                  child: const Icon(
                    Icons.folder_open_rounded,
                    color: Colors.white,
                    size: 16,
                  ),
                ),
              ),

              // Content
              Positioned(
                left: 16,
                right: 16,
                bottom: 16,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      cityName,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.w700,
                      ),
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                    ),
                    const SizedBox(height: 4),
                    Text(
                      '$count ${isEnglish ? 'memories' : 'anı'}',
                      style: const TextStyle(
                        color: Colors.white70,
                        fontSize: 12,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmptyState() {
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(40),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                color: WanderlustColors.accent.withOpacity(0.1),
                shape: BoxShape.circle,
              ),
              child: const Icon(
                Icons.photo_album_rounded,
                color: WanderlustColors.accent,
                size: 64,
              ),
            ),
            const SizedBox(height: 24),
            Text(
              isEnglish ? 'No Memories Yet' : 'Henüz Anı Yok',
              style: const TextStyle(
                color: Colors.white,
                fontSize: 22,
                fontWeight: FontWeight.w700,
              ),
            ),
            const SizedBox(height: 12),
            Text(
              isEnglish
                  ? 'Start capturing your travel moments!'
                  : 'Seyahat anılarını kaydetmeye başla!',
              style: const TextStyle(
                color: Colors.white54,
                fontSize: 15,
              ),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 100), // Space for FAB
          ],
        ),
      ),
    );
  }

  Widget _buildMemoriesGrid(List<TravelMemory> memories) {
    return CustomScrollView(
      slivers: [
        // Stats header
        SliverToBoxAdapter(
          child: Padding(
            padding: const EdgeInsets.fromLTRB(20, 8, 20, 16),
            child: Row(
              children: [
                _buildStatChip(
                  icon: Icons.photo_library_rounded,
                  value: memories.length.toString(),
                  label: isEnglish ? 'memories' : 'anı',
                ),
                const SizedBox(width: 12),
                _buildStatChip(
                  icon: Icons.location_city_rounded,
                  value: _memoryService.citiesWithMemories.length.toString(),
                  label: isEnglish ? 'cities' : 'şehir',
                ),
              ],
            ),
          ),
        ),

        // Grid
        SliverPadding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          sliver: SliverGrid(
            gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
              crossAxisCount: 2,
              mainAxisSpacing: 12,
              crossAxisSpacing: 12,
              childAspectRatio: 0.75,
            ),
            delegate: SliverChildBuilderDelegate(
              (context, index) => _MemoryCard(
                memory: memories[index],
                onTap: () => _showMemoryDetail(memories[index]),
                onDelete: () => _deleteMemory(memories[index]),
              ),
              childCount: memories.length,
            ),
          ),
        ),

        // Bottom padding
        const SliverToBoxAdapter(
          child: SizedBox(height: 100),
        ),
      ],
    );
  }

  Widget _buildStatChip({
    required IconData icon,
    required String value,
    required String label,
  }) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
      decoration: BoxDecoration(
        color: WanderlustColors.bgCard,
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, color: WanderlustColors.accent, size: 18),
          const SizedBox(width: 8),
          Text(
            '$value $label',
            style: const TextStyle(
              color: Colors.white,
              fontSize: 13,
              fontWeight: FontWeight.w500,
            ),
          ),
        ],
      ),
    );
  }

  void _showMemoryDetail(TravelMemory memory) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => _MemoryDetailScreen(memory: memory),
      ),
    );
  }

  Future<void> _deleteMemory(TravelMemory memory) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder: (context) => AlertDialog(
        backgroundColor: WanderlustColors.bgCard,
        title: Text(
          isEnglish ? 'Delete Memory?' : 'Anıyı Sil?',
          style: const TextStyle(color: Colors.white),
        ),
        content: Text(
          isEnglish
              ? 'This action cannot be undone.'
              : 'Bu işlem geri alınamaz.',
          style: const TextStyle(color: Colors.white70),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context, false),
            child: Text(
              isEnglish ? 'Cancel' : 'İptal',
              style: const TextStyle(color: Colors.white54),
            ),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, true),
            child: Text(
              isEnglish ? 'Delete' : 'Sil',
              style: const TextStyle(color: Colors.red),
            ),
          ),
        ],
      ),
    );

    if (confirmed == true) {
      await _memoryService.deleteMemory(memory.id);
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(isEnglish ? 'Memory deleted' : 'Anı silindi'),
            backgroundColor: Colors.red.shade700,
          ),
        );
      }
    }
  }
}

// =============================================================================
// MEMORY CARD
// =============================================================================

class _MemoryCard extends StatelessWidget {
  final TravelMemory memory;
  final VoidCallback onTap;
  final VoidCallback onDelete;

  const _MemoryCard({
    required this.memory,
    required this.onTap,
    required this.onDelete,
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      onLongPress: onDelete,
      child: Container(
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.3),
              blurRadius: 8,
              offset: const Offset(0, 4),
            ),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: Stack(
            fit: StackFit.expand,
            children: [
              // Image
              Image.file(
                File(memory.imagePath),
                fit: BoxFit.cover,
                errorBuilder: (_, __, ___) => Container(
                  color: WanderlustColors.bgCard,
                  child: const Icon(Icons.broken_image, color: Colors.white38),
                ),
              ),

              // Gradient overlay
              Container(
                decoration: BoxDecoration(
                  gradient: LinearGradient(
                    begin: Alignment.topCenter,
                    end: Alignment.bottomCenter,
                    colors: [
                      Colors.transparent,
                      Colors.black.withOpacity(0.7),
                    ],
                    stops: const [0.5, 1.0],
                  ),
                ),
              ),

              // City badge
              Positioned(
                top: 10,
                left: 10,
                child: Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(
                    color: WanderlustColors.accent,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: Text(
                    memory.cityName,
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ),

              // Bottom info
              Positioned(
                left: 12,
                right: 12,
                bottom: 12,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    if (memory.note != null && memory.note!.isNotEmpty)
                      Text(
                        memory.note!,
                        maxLines: 2,
                        overflow: TextOverflow.ellipsis,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 13,
                          fontWeight: FontWeight.w500,
                          height: 1.3,
                        ),
                      ),
                    const SizedBox(height: 4),
                    Text(
                      _formatDate(memory.date),
                      style: const TextStyle(
                        color: Colors.white60,
                        fontSize: 11,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  String _formatDate(DateTime date) {
    final isEnglish = AppLocalizations.instance.isEnglish;
    final months = isEnglish
        ? ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        : ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    return '${date.day} ${months[date.month - 1]} ${date.year}';
  }
}

// =============================================================================
// MEMORY DETAIL SCREEN
// =============================================================================

class _MemoryDetailScreen extends StatelessWidget {
  final TravelMemory memory;

  const _MemoryDetailScreen({required this.memory});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0,
        leading: IconButton(
          icon: const Icon(Icons.close, color: Colors.white),
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          memory.cityName,
          style: const TextStyle(color: Colors.white),
        ),
      ),
      body: Column(
        children: [
          // Image
          Expanded(
            child: InteractiveViewer(
              child: Center(
                child: Image.file(
                  File(memory.imagePath),
                  fit: BoxFit.contain,
                ),
              ),
            ),
          ),

          // Info
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: WanderlustColors.bgCard,
              borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
            ),
            child: SafeArea(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      const Icon(Icons.calendar_today_rounded, color: WanderlustColors.accent, size: 18),
                      const SizedBox(width: 8),
                      Text(
                        _formatDate(memory.date),
                        style: const TextStyle(
                          color: Colors.white70,
                          fontSize: 14,
                        ),
                      ),
                    ],
                  ),
                  if (memory.note != null && memory.note!.isNotEmpty) ...[
                    const SizedBox(height: 16),
                    Text(
                      memory.note!,
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        height: 1.5,
                      ),
                    ),
                  ],
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  String _formatDate(DateTime date) {
    final isEnglish = AppLocalizations.instance.isEnglish;
    final months = isEnglish
        ? ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        : ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
    return '${date.day} ${months[date.month - 1]} ${date.year}';
  }
}
