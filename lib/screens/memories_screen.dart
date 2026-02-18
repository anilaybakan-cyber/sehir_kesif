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
import '../services/premium_service.dart';
import 'paywall_screen.dart';

class MemoriesScreen extends StatefulWidget {
  const MemoriesScreen({super.key});

  @override
  State<MemoriesScreen> createState() => _MemoriesScreenState();
}

class _MemoriesScreenState extends State<MemoriesScreen> {
  final _memoryService = MemoryService();
  String? _selectedCityFilter;
  int? _selectedYearFilter;
  int? _selectedMonthFilter; // 1-12
  final ScrollController _scrollController = ScrollController();
  bool _showScrollToTop = false;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  @override
  void initState() {
    super.initState();
    _memoryService.initialize();
    _memoryService.memoriesNotifier.addListener(_onMemoriesUpdated);
    _scrollController.addListener(() {
      final show = _scrollController.offset > 200;
      if (show != _showScrollToTop) {
        setState(() => _showScrollToTop = show);
      }
    });
  }

  @override
  void dispose() {
    _memoryService.memoriesNotifier.removeListener(_onMemoriesUpdated);
    _scrollController.dispose();
    super.dispose();
  }

  void _showPaywall() {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => const PaywallScreen(),
    );
  }

  void _onMemoriesUpdated() => setState(() {});

  List<TravelMemory> get _filteredMemories {
    return _memoryService.memories.where((m) {
      final cityMatch = _selectedCityFilter == null || m.cityId == _selectedCityFilter;
      final yearMatch = _selectedYearFilter == null || m.date.year == _selectedYearFilter;
      final monthMatch = _selectedMonthFilter == null || m.date.month == _selectedMonthFilter;
      return cityMatch && yearMatch && monthMatch;
    }).toList();
  }

  List<int> get _availableYears {
    return _memoryService.memories.map((m) => m.date.year).toSet().toList()..sort((a, b) => b.compareTo(a));
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
          onPressed: () => Navigator.pop(context),
        ),
        title: Text(
          isEnglish ? 'My Memories' : 'Anılarım',
          style: const TextStyle(
            color: Colors.white,
            fontSize: 20,
            fontWeight: FontWeight.w700,
          ),
        ),
      ),
      body: Column(
        children: [
          // Filters Section
          _buildFilterSection(),
          
          // Grid Section
          Expanded(
            child: Stack(
              children: [
                memories.isEmpty
                    ? _buildEmptyState()
                    : _buildMemoriesGrid(memories),
                if (_showScrollToTop)
                  Positioned(
                    right: 20,
                    bottom: 30,
                    child: AnimatedOpacity(
                      opacity: _showScrollToTop ? 1.0 : 0.0,
                      duration: const Duration(milliseconds: 200),
                      child: GestureDetector(
                        onTap: () {
                          HapticFeedback.lightImpact();
                          _scrollController.animateTo(
                            0, 
                            duration: const Duration(milliseconds: 500), 
                            curve: Curves.easeOutCubic
                          );
                        },
                        child: Container(
                          width: 44,
                          height: 44,
                          decoration: BoxDecoration(
                            color: WanderlustColors.bgCard.withOpacity(0.8),
                            shape: BoxShape.circle,
                            border: Border.all(color: WanderlustColors.border.withOpacity(0.5)),
                          ),
                          child: const Icon(
                            Icons.keyboard_arrow_up_rounded,
                            color: WanderlustColors.textGrey,
                            size: 28,
                          ),
                        ),
                      ),
                    ),
                  ),
              ],
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton.extended(
        onPressed: () async {
          // Premium limit kontrolü
          if (!PremiumService.instance.canSaveMemory()) {
            _showPaywall();
            return;
          }

          HapticFeedback.mediumImpact();
          final result = await AddMemorySheet.show(context);
          
          if (result != null) {
            // Anı kaydedildi, limit düş
            await PremiumService.instance.useSaveMemory();
          }
        },
        backgroundColor: WanderlustColors.accent,
        icon: const Icon(Icons.add_a_photo_rounded),
        label: Text(isEnglish ? 'Add Memory' : 'Anı Ekle'),
      ),
    );
  }

  Widget _buildFilterSection() {
    final hasFilters = _selectedCityFilter != null || _selectedYearFilter != null || _selectedMonthFilter != null;

    String cityLabel = isEnglish ? 'All Cities' : 'Tüm Şehirler';
    if (_selectedCityFilter != null) {
      final cityMemories = _memoryService.getMemoriesByCity(_selectedCityFilter!);
      if (cityMemories.isNotEmpty) cityLabel = cityMemories.first.cityName;
    }

    String dateLabel = isEnglish ? 'All Time' : 'Tüm Zamanlar';
    if (_selectedYearFilter != null) {
      if (_selectedMonthFilter != null) {
        final months = isEnglish
            ? ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            : ['', 'Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
        dateLabel = '${months[_selectedMonthFilter!]} $_selectedYearFilter';
      } else {
        dateLabel = '$_selectedYearFilter';
      }
    } else if (_selectedMonthFilter != null) {
      final months = isEnglish
          ? ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
          : ['', 'Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
      dateLabel = months[_selectedMonthFilter!];
    }

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
      decoration: BoxDecoration(
        color: WanderlustColors.bgDark,
        border: Border(bottom: BorderSide(color: WanderlustColors.border.withOpacity(0.3))),
      ),
      child: Row(
        children: [
          // City Filter Button
          Expanded(
            child: _buildFilterButton(
              icon: Icons.location_city_rounded,
              label: cityLabel,
              isActive: _selectedCityFilter != null,
              onTap: _showCityPicker,
            ),
          ),
          const SizedBox(width: 12),
          // Date Filter Button
          Expanded(
            child: _buildFilterButton(
              icon: Icons.calendar_month_rounded,
              label: dateLabel,
              isActive: _selectedYearFilter != null || _selectedMonthFilter != null,
              onTap: _showDatePicker,
            ),
          ),
          if (hasFilters) ...[
            const SizedBox(width: 8),
            GestureDetector(
              onTap: () {
                HapticFeedback.lightImpact();
                setState(() {
                  _selectedCityFilter = null;
                  _selectedYearFilter = null;
                  _selectedMonthFilter = null;
                });
              },
              child: Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: WanderlustColors.error.withOpacity(0.1),
                  shape: BoxShape.circle,
                ),
                child: const Icon(Icons.close_rounded, color: WanderlustColors.error, size: 20),
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildFilterButton({
    required IconData icon,
    required String label,
    required bool isActive,
    required VoidCallback onTap,
  }) {
    return GestureDetector(
      onTap: () {
        HapticFeedback.lightImpact();
        onTap();
      },
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
        decoration: BoxDecoration(
          color: isActive ? WanderlustColors.accent.withOpacity(0.15) : WanderlustColors.bgCard.withOpacity(0.4),
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isActive ? WanderlustColors.accent.withOpacity(0.5) : WanderlustColors.border,
          ),
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(icon, color: isActive ? WanderlustColors.accent : Colors.white60, size: 18),
            const SizedBox(width: 8),
            Flexible(
              child: Text(
                label,
                style: TextStyle(
                  color: isActive ? Colors.white : Colors.white70,
                  fontSize: 13,
                  fontWeight: isActive ? FontWeight.w600 : FontWeight.w400,
                ),
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
              ),
            ),
            const SizedBox(width: 4),
            Icon(Icons.keyboard_arrow_down_rounded, color: isActive ? WanderlustColors.accent : Colors.white30, size: 16),
          ],
        ),
      ),
    );
  }

  void _showCityPicker() {
    final cities = _memoryService.citiesWithMemories;
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => Container(
        height: MediaQuery.of(context).size.height * 0.6,
        decoration: BoxDecoration(
          color: WanderlustColors.bgDark,
          borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
          border: Border.all(color: WanderlustColors.border),
        ),
        child: Column(
          children: [
            const SizedBox(height: 12),
            Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2))),
            const SizedBox(height: 20),
            Text(isEnglish ? 'Select City' : 'Şehir Seç', style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 20),
            Expanded(
              child: ListView(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                children: [
                   ListTile(
                    title: Text(isEnglish ? 'All Cities' : 'Tüm Şehirler', style: const TextStyle(color: Colors.white70)),
                    leading: const Icon(Icons.location_on_outlined, color: Colors.white38),
                    trailing: _selectedCityFilter == null ? const Icon(Icons.check_circle, color: WanderlustColors.accent) : null,
                    onTap: () {
                      setState(() => _selectedCityFilter = null);
                      Navigator.pop(context);
                    },
                  ),
                  ...cities.map((cityId) {
                    final memories = _memoryService.getMemoriesByCity(cityId);
                    final name = memories.first.cityName;
                    final isSelected = _selectedCityFilter == cityId;
                    return ListTile(
                      title: Text(name, style: TextStyle(color: isSelected ? Colors.white : Colors.white70)),
                      subtitle: Text('${memories.length} ${isEnglish ? 'memories' : 'anı'}', style: const TextStyle(color: Colors.white38, fontSize: 12)),
                      leading: Icon(Icons.location_on, color: isSelected ? WanderlustColors.accent : Colors.white30),
                      trailing: isSelected ? const Icon(Icons.check_circle, color: WanderlustColors.accent) : null,
                      onTap: () {
                        setState(() => _selectedCityFilter = cityId);
                        Navigator.pop(context);
                      },
                    );
                  }),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  void _showDatePicker() {
    final years = _availableYears;
    final months = isEnglish
        ? ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        : ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];

    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (context) => StatefulBuilder(
        builder: (context, setLocalState) => Container(
          height: MediaQuery.of(context).size.height * 0.7,
          decoration: BoxDecoration(
            color: WanderlustColors.bgDark,
            borderRadius: const BorderRadius.vertical(top: Radius.circular(24)),
            border: Border.all(color: WanderlustColors.border),
          ),
          child: Column(
            children: [
              const SizedBox(height: 12),
              Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2))),
              const SizedBox(height: 20),
              Text(isEnglish ? 'Select Date' : 'Tarih Seç', style: const TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
              const SizedBox(height: 20),
              
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(isEnglish ? 'Year' : 'Yıl', style: const TextStyle(color: Colors.white70, fontWeight: FontWeight.w600)),
                    if (_selectedYearFilter != null)
                      TextButton(
                        onPressed: () {
                          setLocalState(() => _selectedYearFilter = null);
                          setState(() => _selectedYearFilter = null);
                        },
                        child: Text(isEnglish ? 'Clear' : 'Sıfırla', style: const TextStyle(color: WanderlustColors.error, fontSize: 12)),
                      ),
                  ],
                ),
              ),
              SizedBox(
                height: 50,
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  children: years.map((year) {
                    final isSelected = _selectedYearFilter == year;
                    return Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 4),
                      child: ChoiceChip(
                        label: Text(year.toString()),
                        selected: isSelected,
                        onSelected: (val) {
                          setLocalState(() => _selectedYearFilter = year);
                          setState(() => _selectedYearFilter = year);
                        },
                        backgroundColor: WanderlustColors.bgCard,
                        selectedColor: WanderlustColors.accent,
                        labelStyle: TextStyle(color: isSelected ? Colors.white : Colors.white70),
                      ),
                    );
                  }).toList(),
                ),
              ),
              
              const SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(isEnglish ? 'Month' : 'Ay', style: const TextStyle(color: Colors.white70, fontWeight: FontWeight.w600)),
                    if (_selectedMonthFilter != null)
                      TextButton(
                        onPressed: () {
                          setLocalState(() => _selectedMonthFilter = null);
                          setState(() => _selectedMonthFilter = null);
                        },
                        child: Text(isEnglish ? 'Clear' : 'Sıfırla', style: const TextStyle(color: WanderlustColors.error, fontSize: 12)),
                      ),
                  ],
                ),
              ),
              Expanded(
                child: GridView.builder(
                  padding: const EdgeInsets.all(20),
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 3,
                    childAspectRatio: 2.5,
                    crossAxisSpacing: 10,
                    mainAxisSpacing: 10,
                  ),
                  itemCount: months.length,
                  itemBuilder: (context, index) {
                    final monthIdx = index + 1;
                    final isSelected = _selectedMonthFilter == monthIdx;
                    return GestureDetector(
                      onTap: () {
                        setLocalState(() => _selectedMonthFilter = monthIdx);
                        setState(() => _selectedMonthFilter = monthIdx);
                      },
                      child: Container(
                        alignment: Alignment.center,
                        decoration: BoxDecoration(
                          color: isSelected ? WanderlustColors.accent : WanderlustColors.bgCard.withOpacity(0.5),
                          borderRadius: BorderRadius.circular(10),
                          border: Border.all(color: isSelected ? WanderlustColors.accent : WanderlustColors.border),
                        ),
                        child: Text(
                          months[index],
                          style: TextStyle(color: isSelected ? Colors.white : Colors.white70, fontSize: 12, fontWeight: isSelected ? FontWeight.bold : FontWeight.normal),
                        ),
                      ),
                    );
                  },
                ),
              ),
              
              Padding(
                padding: const EdgeInsets.all(20),
                child: SizedBox(
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: WanderlustColors.accent,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(14)),
                    ),
                    onPressed: () => Navigator.pop(context),
                    child: Text(isEnglish ? 'Apply' : 'Uygula', style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  ),
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
      controller: _scrollController,
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

              // Delete button
              Positioned(
                top: 8,
                right: 8,
                child: GestureDetector(
                  onTap: () {
                     HapticFeedback.mediumImpact();
                     onDelete();
                  },
                  child: Container(
                    padding: const EdgeInsets.all(6),
                    decoration: BoxDecoration(
                      color: Colors.black.withOpacity(0.4),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(
                      Icons.delete_outline_rounded,
                      color: Colors.white,
                      size: 18,
                    ),
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
                    color: WanderlustColors.accent.withOpacity(0.85),
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
