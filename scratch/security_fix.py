import os
import re

# Bulunan anahtarlar
KEYS_TO_REPLACE = [
    "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g",
    "AIzaSyBSZJmb9IIINxWbxXgCLTPiWC9SLcaDrMk"
]

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for key in KEYS_TO_REPLACE:
        if key in content:
            # Replace the key string with os.getenv call
            # Note: We need to make sure os is imported
            content = content.replace(f'"{key}"', 'os.getenv("GOOGLE_MAPS_API_KEY")')
            content = content.replace(f"'{key}'", 'os.getenv("GOOGLE_MAPS_API_KEY")')
            modified = True
            
    if modified:
        # Check if 'import os' exists
        if "import os" not in content:
            # Insert import os at the top
            lines = content.split('\n')
            lines.insert(0, "import os")
            content = '\n'.join(lines)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    py_files = [f for f in os.listdir('.') if f.endswith('.py')]
    count = 0
    for f in py_files:
        if fix_file(f):
            print(f"✅ Fixed: {f}")
            count += 1
    print(f"\nDone! Fixed {count} files.")

if __name__ == "__main__":
    main()
