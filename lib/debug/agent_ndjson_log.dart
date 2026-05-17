import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;

/// Cursor debug session NDJSON (dosya + ingest). Telefonda workspace yolu yoktur;
/// ingest HTTP ile makineye log düşer (iOS Sim / macOS: 127.0.0.1, Android emu: 10.0.2.2).
// #region agent log
const String kAgentDebugSessionId = '7eed1b';

const String _agentIngestPath =
    '/ingest/a4b9fd26-3def-48b5-b586-25fc4941a7be';

const String kAgentDebugNdjsonLogPath =
    '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/.cursor/debug-7eed1b.log';

void agentNdjsonLog({
  required String hypothesisId,
  required String location,
  required String message,
  Map<String, Object?> data = const {},
  String runId = 'run1',
}) {
  final payload = <String, Object?>{
    'sessionId': kAgentDebugSessionId,
    'runId': runId,
    'hypothesisId': hypothesisId,
    'location': location,
    'message': message,
    'data': data,
    'timestamp': DateTime.now().millisecondsSinceEpoch,
  };
  final body = jsonEncode(payload);

  try {
    final f = File(kAgentDebugNdjsonLogPath);
    if (f.parent.existsSync()) {
      f.writeAsStringSync('$body\n', mode: FileMode.append, flush: true);
    }
  } catch (_) {}

  final host = Platform.isAndroid ? '10.0.2.2' : '127.0.0.1';
  final uri = Uri.parse('http://$host:7614$_agentIngestPath');
  unawaited(
    http
        .post(
          uri,
          headers: {
            'Content-Type': 'application/json',
            'X-Debug-Session-Id': kAgentDebugSessionId,
          },
          body: body,
        )
        .timeout(const Duration(seconds: 2))
        .then((_) {}, onError: (_) {}),
  );

  if (kDebugMode) {
    debugPrint('[agent_ndjson] $body');
  }
}
// #endregion
