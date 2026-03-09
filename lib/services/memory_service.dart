// =============================================================================
// MEMORY SERVICE
// Seyahat anılarını yönetmek için servis
// Local storage (SharedPreferences + File System)
// =============================================================================

import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:image_picker/image_picker.dart';
import 'package:path/path.dart' as p;
import '../models/travel_memory.dart';

class MemoryService {
  static const String _storageKey = 'travel_memories';
  
  // Singleton
  static final MemoryService _instance = MemoryService._internal();
  factory MemoryService() => _instance;
  MemoryService._internal();

  // In-memory cache
  List<TravelMemory> _memories = [];
  bool _isInitialized = false;

  // Notifier for UI updates
  final ValueNotifier<List<TravelMemory>> memoriesNotifier = ValueNotifier([]);

  /// Initialize service and load memories
  Future<void> initialize() async {
    if (_isInitialized) return;
    await _loadMemories();
    _isInitialized = true;
  }

  /// Get all memories (sorted by date, newest first)
  List<TravelMemory> get memories {
    final sorted = List<TravelMemory>.from(_memories);
    sorted.sort((a, b) => b.date.compareTo(a.date));
    return sorted;
  }

  /// Get memories by city
  List<TravelMemory> getMemoriesByCity(String cityId) {
    return memories.where((m) => m.cityId == cityId).toList();
  }

  /// Get unique cities with memories
  List<String> get citiesWithMemories {
    return _memories.map((m) => m.cityId).toSet().toList();
  }

  /// Get memory count
  int get totalCount => _memories.length;

  /// Get city-grouped memories
  Map<String, List<TravelMemory>> get memoriesByCity {
    final map = <String, List<TravelMemory>>{};
    for (final memory in memories) {
      map.putIfAbsent(memory.cityId, () => []).add(memory);
    }
    return map;
  }

  /// Add a new memory
  Future<TravelMemory?> addMemory({
    required String cityId,
    required String cityName,
    required XFile imageFile,
    String? note,
    DateTime? date,
  }) async {
    try {
      // 1. Copy image to app documents
      final savedPath = await _saveImage(imageFile, cityId);
      if (savedPath == null) return null;

      // 2. Create memory object
      final memory = TravelMemory(
        id: TravelMemory.generateId(),
        cityId: cityId,
        cityName: cityName,
        imagePath: savedPath,
        note: note,
        date: date ?? DateTime.now(),
        createdAt: DateTime.now(),
      );

      // 3. Add to list and save
      _memories.add(memory);
      await _saveMemories();
      _notifyListeners();

      debugPrint('📸 Memory added: ${memory.cityName}');
      return memory;

    } catch (e) {
      debugPrint('❌ Error adding memory: $e');
      rethrow;
    }
  }

  /// Update memory (note or date)
  Future<bool> updateMemory(String id, {String? note, DateTime? date}) async {
    try {
      final index = _memories.indexWhere((m) => m.id == id);
      if (index == -1) return false;

      _memories[index] = _memories[index].copyWith(
        note: note,
        date: date,
      );

      await _saveMemories();
      _notifyListeners();
      return true;

    } catch (e) {
      debugPrint('❌ Error updating memory: $e');
      return false;
    }
  }

  /// Delete memory
  Future<bool> deleteMemory(String id) async {
    try {
      final memory = _memories.firstWhere((m) => m.id == id);
      
      // Delete image file
      final file = File(memory.imagePath);
      if (await file.exists()) {
        await file.delete();
      }

      // Remove from list
      _memories.removeWhere((m) => m.id == id);
      await _saveMemories();
      _notifyListeners();

      debugPrint('🗑️ Memory deleted');
      return true;

    } catch (e) {
      debugPrint('❌ Error deleting memory: $e');
      return false;
    }
  }

  /// Save image to app documents directory
  Future<String> _saveImage(XFile imageFile, String cityId) async {
      final dir = await getApplicationDocumentsDirectory();
      final memoriesDir = Directory(p.join(dir.path, 'memories', cityId));
      
      if (!await memoriesDir.exists()) {
        await memoriesDir.create(recursive: true);
      }

      final extension = p.extension(imageFile.path).toLowerCase();
      // Ensure we have a valid extension, default to .jpg if empty or unexpected
      final validExt = extension.isNotEmpty ? extension : '.jpg';
      final fileName = '${DateTime.now().millisecondsSinceEpoch}$validExt';
      final savedPath = p.join(memoriesDir.path, fileName);
      
      // LOG: Check source existence
      if (!await File(imageFile.path).exists()) {
          throw Exception("Source file missing: ${imageFile.path}");
      }

      // Use readAsBytes/writeAsBytes for maximum reliability on iOS production/TestFlight
      // This bypasses OS-level 'move' restrictions on security-scoped temporary paths.
      final bytes = await imageFile.readAsBytes();
      if (bytes.isEmpty) throw Exception("Selected image is empty (0 bytes)");
      
      final destinationFile = File(savedPath);
      await destinationFile.writeAsBytes(bytes, flush: true);
      
      return savedPath;
  }

  /// Load memories from SharedPreferences
  Future<void> _loadMemories() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final jsonString = prefs.getString(_storageKey);
      
      if (jsonString != null) {
        final List<dynamic> jsonList = json.decode(jsonString);
        _memories = jsonList
            .map((json) => TravelMemory.fromJson(json as Map<String, dynamic>))
            .toList();
        
        // Validate image paths (remove memories with missing images)
        _memories = await _validateMemories(_memories);
      }

      _notifyListeners();
      debugPrint('📚 Loaded ${_memories.length} memories');

    } catch (e) {
      debugPrint('❌ Error loading memories: $e');
      _memories = [];
    }
  }

  /// Validate memories - remove ones with missing images
  Future<List<TravelMemory>> _validateMemories(List<TravelMemory> memories) async {
    final valid = <TravelMemory>[];
    for (final memory in memories) {
      final file = File(memory.imagePath);
      if (await file.exists()) {
        valid.add(memory);
      }
    }
    return valid;
  }

  /// Save memories to SharedPreferences
  Future<void> _saveMemories() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final jsonString = json.encode(_memories.map((m) => m.toJson()).toList());
      await prefs.setString(_storageKey, jsonString);
    } catch (e) {
      debugPrint('❌ Error saving memories: $e');
    }
  }

  void _notifyListeners() {
    memoriesNotifier.value = List.from(_memories);
  }

  /// Wipe all memory data (disk and memory)
  Future<void> clearAllData() async {
    try {
      // 1. Delete physical files
      final dir = await getApplicationDocumentsDirectory();
      final memoriesDir = Directory('${dir.path}/memories');
      if (await memoriesDir.exists()) {
        await memoriesDir.delete(recursive: true);
        debugPrint('🗑️ Physical memories directory deleted');
      }

      // 2. Clear SharedPreferences
      final prefs = await SharedPreferences.getInstance();
      await prefs.remove(_storageKey);

      // 3. Reset in-memory state
      _memories.clear();
      _notifyListeners();

      debugPrint('✅ MemoryService fully cleared');
    } catch (e) {
      debugPrint('❌ Error clearing all memories: $e');
    }
  }
}
