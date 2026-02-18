import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:crypto/crypto.dart';
import 'dart:convert';

class AICacheService {
  static final AICacheService _instance = AICacheService._internal();
  static AICacheService get instance => _instance;
  
  AICacheService._internal();

  final FirebaseFirestore _firestore = FirebaseFirestore.instance;
  static const String _collectionName = 'ai_response_cache';

  /// Generates a deterministic SHA-256 hash key from a map of parameters.
  /// Keys are sorted alphabetically to ensure consistency.
  String generateCacheKey(Map<String, dynamic> params) {
    // Sort keys to ensure deterministic output
    final sortedKeys = params.keys.toList()..sort();
    final sortedMap = {for (var key in sortedKeys) key: params[key]};
    
    // Convert to JSON string
    final jsonString = jsonEncode(sortedMap);
    
    // Generate SHA-256 hash
    final bytes = utf8.encode(jsonString);
    final digest = sha256.convert(bytes);
    
    return digest.toString();
  }

  /// Retrieves a cached response if it exists.
  Future<String?> getCachedResponse(String key) async {
    try {
      final doc = await _firestore.collection(_collectionName).doc(key).get();
      if (doc.exists && doc.data() != null) {
        // Optional: Check for expiration if needed in the future
        // final timestamp = doc.data()!['timestamp'] as Timestamp;
        // if (DateTime.now().difference(timestamp.toDate()).inDays > 30) return null;
        
        return doc.data()!['response'] as String?;
      }
    } catch (e) {
      print("AICacheService Get Error: $e");
    }
    return null;
  }

  /// Caches a response with metadata.
  Future<void> cacheResponse({
    required String key,
    required String response,
    required String type, // 'chat' or 'suggestion'
    required Map<String, dynamic> metadata,
  }) async {
    try {
      await _firestore.collection(_collectionName).doc(key).set({
        'response': response,
        'type': type,
        'metadata': metadata,
        'timestamp': FieldValue.serverTimestamp(),
        'version': 1, // Useful for invalidating cache if logic changes
      });
    } catch (e) {
      print("AICacheService Set Error: $e");
    }
  }
}
