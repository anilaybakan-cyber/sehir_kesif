// =============================================================================
// ADD MEMORY SHEET
// Yeni anı ekleme bottom sheet
// =============================================================================

import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import '../theme/wanderlust_colors.dart';
import '../l10n/app_localizations.dart';
import '../services/memory_service.dart';
import '../services/premium_service.dart';
import '../models/travel_memory.dart';
import '../screens/city_switcher_screen.dart';

class AddMemorySheet extends StatefulWidget {
  final String? preselectedCityId;
  final String? preselectedCityName;
  final VoidCallback? onMemoryAdded;

  const AddMemorySheet({
    super.key,
    this.preselectedCityId,
    this.preselectedCityName,
    this.onMemoryAdded,
  });

  static Future<TravelMemory?> show(BuildContext context, {
    String? cityId,
    String? cityName,
  }) async {
    return showModalBottomSheet<TravelMemory>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.transparent,
      builder: (context) => AddMemorySheet(
        preselectedCityId: cityId,
        preselectedCityName: cityName,
      ),
    );
  }

  @override
  State<AddMemorySheet> createState() => _AddMemorySheetState();
}

class _AddMemorySheetState extends State<AddMemorySheet> {
  final _picker = ImagePicker();
  final _noteController = TextEditingController();
  final _memoryService = MemoryService();

  XFile? _selectedImage;
  String? _selectedCityId;
  String? _selectedCityName;
  DateTime _selectedDate = DateTime.now();
  bool _isLoading = false;

  bool get isEnglish => AppLocalizations.instance.isEnglish;

  @override
  void initState() {
    super.initState();
    _selectedCityId = widget.preselectedCityId;
    _selectedCityName = widget.preselectedCityName;
  }

  @override
  void dispose() {
    _noteController.dispose();
    super.dispose();
  }

  Future<void> _pickImage(ImageSource source) async {
    try {
      final image = await _picker.pickImage(
        source: source,
        maxWidth: 1920,
        maxHeight: 1080,
        imageQuality: 85,
      );
      if (image != null) {
        setState(() => _selectedImage = image);
      }
    } catch (e) {
      debugPrint('Error picking image: $e');
    }
  }

  Future<void> _selectCity() async {
    final result = await CitySwitcherScreen.showAsModal(context, updateGlobalState: false);
    if (result != null) {
      // Get city name from the result
      final cityData = CitySwitcherScreen.allCities.firstWhere(
        (c) => c['id'] == result,
        orElse: () => {'id': result, 'name': result},
      );
      setState(() {
        _selectedCityId = result;
        _selectedCityName = cityData['name'] as String;
      });
    }
  }

  Future<void> _selectDate() async {
    final picked = await showDatePicker(
      context: context,
      initialDate: _selectedDate,
      firstDate: DateTime(2000),
      lastDate: DateTime.now(),
      builder: (context, child) {
        return Theme(
          data: ThemeData.dark().copyWith(
            colorScheme: const ColorScheme.dark(
              primary: WanderlustColors.accent,
              surface: WanderlustColors.bgCard,
            ),
          ),
          child: child!,
        );
      },
    );
    if (picked != null) {
      setState(() => _selectedDate = picked);
    }
  }

  Future<void> _saveMemory() async {
    if (_selectedImage == null || _selectedCityId == null) return;

    setState(() => _isLoading = true);
    HapticFeedback.mediumImpact();

    final memory = await _memoryService.addMemory(
      cityId: _selectedCityId!,
      cityName: _selectedCityName ?? _selectedCityId!,
      imageFile: _selectedImage!,
      note: _noteController.text.trim().isEmpty ? null : _noteController.text.trim(),
      date: _selectedDate,
    );

    setState(() => _isLoading = false);

    if (memory != null && mounted) {
      widget.onMemoryAdded?.call();
      Navigator.pop(context, memory);
      

    }
  }

  @override
  Widget build(BuildContext context) {
    final bottomPadding = MediaQuery.of(context).viewInsets.bottom;
    final canSave = _selectedImage != null && _selectedCityId != null;

    return Container(
      constraints: BoxConstraints(
        maxHeight: MediaQuery.of(context).size.height * 0.85,
      ),
      decoration: const BoxDecoration(
        color: WanderlustColors.bgDark,
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          // Handle bar
          Container(
            margin: const EdgeInsets.only(top: 12),
            width: 40,
            height: 4,
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              borderRadius: BorderRadius.circular(2),
            ),
          ),

          // Header
          Padding(
            padding: const EdgeInsets.fromLTRB(24, 20, 16, 12),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  isEnglish ? 'New Memory' : 'Yeni Anı',
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 22,
                    fontWeight: FontWeight.w700,
                  ),
                ),
                GestureDetector(
                  onTap: () => Navigator.pop(context),
                  child: Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: const Icon(
                      Icons.close_rounded,
                      color: Colors.white70,
                      size: 20,
                    ),
                  ),
                ),
              ],
            ),
          ),

          // Content
          Flexible(
            child: SingleChildScrollView(
              padding: EdgeInsets.fromLTRB(20, 0, 20, bottomPadding + 20),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Image Picker
                  _buildImagePicker(),
                  const SizedBox(height: 20),

                  // City Selector
                  _buildSelectorTile(
                    icon: Icons.location_city_rounded,
                    label: isEnglish ? 'City' : 'Şehir',
                    value: _selectedCityName ?? (isEnglish ? 'Select city...' : 'Şehir seç...'),
                    onTap: _selectCity,
                    isRequired: true,
                  ),
                  const SizedBox(height: 12),

                  // Date Selector
                  _buildSelectorTile(
                    icon: Icons.calendar_today_rounded,
                    label: isEnglish ? 'Date' : 'Tarih',
                    value: _formatDate(_selectedDate),
                    onTap: _selectDate,
                  ),
                  const SizedBox(height: 20),

                  // Note Field
                  Text(
                    isEnglish ? 'Note (optional)' : 'Not (isteğe bağlı)',
                    style: const TextStyle(
                      color: Colors.white70,
                      fontSize: 14,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Container(
                    decoration: BoxDecoration(
                      color: WanderlustColors.bgCard,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: Colors.white.withOpacity(0.08)),
                    ),
                    child: TextField(
                      controller: _noteController,
                      maxLines: 3,
                      maxLength: 200,
                      style: const TextStyle(color: Colors.white),
                      decoration: InputDecoration(
                        hintText: isEnglish ? 'Write about this moment...' : 'Bu an hakkında yaz...',
                        hintStyle: TextStyle(color: WanderlustColors.textGrey.withOpacity(0.6)),
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.all(16),
                        counterStyle: const TextStyle(color: Colors.white38),
                      ),
                    ),
                  ),
                  const SizedBox(height: 24),

                  // Save Button
                  SizedBox(
                    width: double.infinity,
                    height: 56,
                    child: ElevatedButton(
                      onPressed: canSave && !_isLoading ? _saveMemory : null,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: WanderlustColors.accent,
                        foregroundColor: Colors.white,
                        disabledBackgroundColor: WanderlustColors.bgCardLight,
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(28),
                        ),
                      ),
                      child: _isLoading
                          ? const SizedBox(
                              width: 24,
                              height: 24,
                              child: CircularProgressIndicator(
                                color: Colors.white,
                                strokeWidth: 2,
                              ),
                            )
                          : Text(
                              isEnglish ? 'Save Memory' : 'Anıyı Kaydet',
                              style: const TextStyle(
                                fontSize: 16,
                                fontWeight: FontWeight.w600,
                              ),
                            ),
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

  Widget _buildImagePicker() {
    return GestureDetector(
      onTap: () => _showImageSourceSheet(),
      child: Container(
        height: 200,
        width: double.infinity,
        decoration: BoxDecoration(
          color: WanderlustColors.bgCard,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: _selectedImage != null
                ? WanderlustColors.accent
                : Colors.white.withOpacity(0.1),
            width: 2,
          ),
        ),
        child: _selectedImage != null
            ? Stack(
                fit: StackFit.expand,
                children: [
                  ClipRRect(
                    borderRadius: BorderRadius.circular(14),
                    child: Image.file(
                      File(_selectedImage!.path),
                      fit: BoxFit.cover,
                    ),
                  ),
                  Positioned(
                    top: 8,
                    right: 8,
                    child: GestureDetector(
                      onTap: () => setState(() => _selectedImage = null),
                      child: Container(
                        padding: const EdgeInsets.all(6),
                        decoration: BoxDecoration(
                          color: Colors.black.withOpacity(0.6),
                          shape: BoxShape.circle,
                        ),
                        child: const Icon(
                          Icons.close,
                          color: Colors.white,
                          size: 18,
                        ),
                      ),
                    ),
                  ),
                ],
              )
            : Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: WanderlustColors.accent.withOpacity(0.1),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(
                      Icons.add_a_photo_rounded,
                      color: WanderlustColors.accent,
                      size: 40,
                    ),
                  ),
                  const SizedBox(height: 12),
                  Text(
                    isEnglish ? 'Add Photo' : 'Fotoğraf Ekle',
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 16,
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    isEnglish ? 'Tap to select' : 'Seçmek için dokun',
                    style: const TextStyle(
                      color: Colors.white54,
                      fontSize: 13,
                    ),
                  ),
                ],
              ),
      ),
    );
  }

  Widget _buildSelectorTile({
    required IconData icon,
    required String label,
    required String value,
    required VoidCallback onTap,
    bool isRequired = false,
  }) {
    final hasValue = value != (isEnglish ? 'Select city...' : 'Şehir seç...');

    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(
          color: WanderlustColors.bgCard,
          borderRadius: BorderRadius.circular(14),
          border: Border.all(
            color: isRequired && !hasValue
                ? WanderlustColors.accent.withOpacity(0.5)
                : Colors.white.withOpacity(0.08),
          ),
        ),
        child: Row(
          children: [
            Icon(icon, color: WanderlustColors.accent, size: 22),
            const SizedBox(width: 12),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    label,
                    style: const TextStyle(
                      color: Colors.white54,
                      fontSize: 12,
                    ),
                  ),
                  const SizedBox(height: 2),
                  Text(
                    value,
                    style: TextStyle(
                      color: hasValue ? Colors.white : Colors.white38,
                      fontSize: 15,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ),
            ),
            const Icon(
              Icons.chevron_right_rounded,
              color: Colors.white38,
              size: 24,
            ),
          ],
        ),
      ),
    );
  }

  void _showImageSourceSheet() {
    showModalBottomSheet(
      context: context,
      backgroundColor: WanderlustColors.bgCard,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (context) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              ListTile(
                leading: const Icon(Icons.photo_library_rounded, color: WanderlustColors.accent),
                title: Text(
                  isEnglish ? 'Choose from Gallery' : 'Galeriden Seç',
                  style: const TextStyle(color: Colors.white),
                ),
                onTap: () {
                  Navigator.pop(context);
                  _pickImage(ImageSource.gallery);
                },
              ),
              ListTile(
                leading: const Icon(Icons.camera_alt_rounded, color: WanderlustColors.accent),
                title: Text(
                  isEnglish ? 'Take a Photo' : 'Fotoğraf Çek',
                  style: const TextStyle(color: Colors.white),
                ),
                onTap: () {
                  Navigator.pop(context);
                  _pickImage(ImageSource.camera);
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  String _formatDate(DateTime date) {
    final months = isEnglish
        ? ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        : ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
    return '${date.day} ${months[date.month - 1]} ${date.year}';
  }
}
