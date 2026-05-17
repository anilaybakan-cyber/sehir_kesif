import 'package:flutter_dotenv/flutter_dotenv.dart';

class ApiConfig {
  static String get openAiApiKey =>
      dotenv.env['OPENAI_API_KEY'] ?? "YOUR_OPENAI_API_KEY_HERE";

  static const String openAiBaseUrl = "https://api.openai.com/v1";
}
