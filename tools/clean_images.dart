import 'dart:convert';
import 'dart:io';

void main() async {
  final path = "assets/cities/barcelona.json";

  print("🧽 Cleaning old images in: $path");

  final file = File(path);
  final data = jsonDecode(await file.readAsString());

  int count = 0;

  for (final item in data["highlights"]) {
    if (item["imageUrl"] != null && item["imageUrl"].toString().isNotEmpty) {
      item["imageUrl"] = "";
      count++;
    }
  }

  await file.writeAsString(const JsonEncoder.withIndent("  ").convert(data));

  print("✨ DONE → $count eski foto silindi!");
}
