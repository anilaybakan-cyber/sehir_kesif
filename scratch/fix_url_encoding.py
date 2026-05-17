import json
import os
from pathlib import Path

def main():
    cities_dir = Path("assets/cities")
    for json_file in cities_dir.glob("*.json"):
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            updated = False
            for h in data.get('highlights', []):
                url = h.get('imageUrl', '')
                if url and 'firebasestorage.googleapis.com' in url:
                    # Fix double /o/o%2F and ensure correct encoding
                    # Extract the path part
                    if '/o/' in url:
                        base = url.split('/o/')[0] + '/o/'
                        path_part = url.split('/o/')[-1].split('?')[0]
                        # Remove any leading 'o%2F' if accidentally added
                        if path_part.startswith('o%2F'):
                            path_part = path_part[4:]
                        
                        # Fix encoding: replace %2F with / then back to %2F to ensure single encoding
                        path_part = path_part.replace('%2F', '/')
                        # Remove double slashes
                        path_part = path_part.replace('//', '/')
                        # Encode properly
                        encoded_path = path_part.replace('/', '%2F')
                        
                        h['imageUrl'] = f"{base}{encoded_path}?alt=media"
                        updated = True
            
            if updated:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"✅ Fixed URLs in {json_file.name}")
        except Exception as e:
            print(f"❌ Error processing {json_file.name}: {e}")

if __name__ == "__main__":
    main()
