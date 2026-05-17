import os
import re

files = [f for f in os.listdir('.') if f.startswith('generate_routes_') and f.endswith('.py')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update the loading logic to handle list or dict
    if 'data = json.load(f)' in content and 'if isinstance(data, list):' not in content:
        content = content.replace(
            'data = json.load(f)',
            'data = json.load(f)\n    if isinstance(data, list):\n        highlights = data\n    else:\n        highlights = data.get("highlights", [])'
        )
    
    # 2. Update get_id to use 'highlights' variable instead of data.get("highlights")
    content = content.replace('for p in data.get("highlights", []):', 'for p in highlights:')
    
    # 3. Update the saving logic
    if 'data["curated_routes"] = routes_data' in content:
        content = content.replace(
            'data["curated_routes"] = routes_data',
            'if isinstance(data, list):\n    # If it is a list, we can\'t easily inject routes unless we change format\n    # For now, let\'s skip or wrap it\n    pass\nelse:\n    data["curated_routes"] = routes_data'
        )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Updated {f}")
