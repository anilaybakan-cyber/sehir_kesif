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
                if url and 'storage.googleapis.com' in url and 'firebasestorage.app' in url:
                    # Convert to v0 format
                    # Example: https://storage.googleapis.com/bucket/cities/id/file.jpg
                    # To: https://firebasestorage.googleapis.com/v0/b/bucket/o/cities%2Fid%2Ffile.jpg?alt=media
                    new_url = url.replace('https://storage.googleapis.com/', 'https://firebasestorage.googleapis.com/v0/b/')
                    
                    # Replace the first / after the bucket name with /o/
                    parts = new_url.split('.firebasestorage.app/')
                    if len(parts) == 2:
                        new_url = parts[0] + '.firebasestorage.app/o/' + parts[1].replace('/', '%2F')
                    
                    if '?alt=media' not in new_url:
                        new_url += '?alt=media'
                        
                    h['imageUrl'] = new_url
                    updated = True
            
            if updated:
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"✅ Updated URLs in {json_file.name}")
        except Exception as e:
            print(f"❌ Error processing {json_file.name}: {e}")

if __name__ == "__main__":
    main()
