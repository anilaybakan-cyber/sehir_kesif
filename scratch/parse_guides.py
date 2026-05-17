import re

with open('lib/services/city_blog_content.dart', 'r') as f:
    content = f.read()

# Find all static const _cityTR = '''...''';
pattern = re.compile(r"static const _(\w+)TR = '''(.*?)''';", re.DOTALL)
matches = pattern.findall(content)

for name, text in matches:
    if "**Hızlı Bakış:**" not in text and "Hızlı Bakış:" not in text:
        print(f"Needs update: {name}TR")
