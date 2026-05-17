import os
import re
import json

DART_FILE = "lib/services/city_blog_content.dart"
CACHE_FILE = "scratch/guide_cache.json"

with open(CACHE_FILE, "r") as f:
    cache = json.load(f)

with open(DART_FILE, "r") as f:
    content = f.read()

def replacer(match):
    prefix = match.group(1) 
    city_base = match.group(2) 
    lang = match.group(3) 
    suffix = match.group(5) 
    
    var_name = f"{city_base}{lang}"
    if var_name in cache:
        new_text = cache[var_name]
        new_text_escaped = new_text.replace('$', '\\$')
        return f"{prefix}\n{new_text_escaped}\n{suffix}"
    
    return match.group(0)

pattern = re.compile(r"(static const _(\w+?)(TR|EN) = ''')(.*?)(''';)", re.DOTALL)
new_content = pattern.sub(replacer, content)

with open(DART_FILE, "w") as f:
    f.write(new_content)

print("Applied guides from cache.")
