import os
import re

files = [f for f in os.listdir('.') if f.startswith('generate_routes_') and f.endswith('.py')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the return p["id"] with a safe version
    new_content = re.sub(
        r'return p\["id"\]', 
        r'return p.get("id") or str(p["name"]).lower().replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")', 
        content
    )
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Fixed {f}")
    else:
        print(f"Skipped or already fixed {f}")
