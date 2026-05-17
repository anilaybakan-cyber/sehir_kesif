#!/usr/bin/env python3
import os
import json

assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
total_removed = 0
cities_affected = 0

print("🔍 Scanning all city JSON files for duplicate highlight IDs...\n")

for filename in sorted(os.listdir(assets_dir)):
    if filename.endswith('.json'):
        filepath = os.path.join(assets_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            highlights = data.get('highlights', [])
            if not highlights:
                continue
            
            seen_ids = set()
            unique_highlights = []
            removed_in_city = 0
            
            for h in highlights:
                hid = h.get('id')
                if not hid:
                    # If for some reason there's no id, keep it
                    unique_highlights.append(h)
                    continue
                
                if hid in seen_ids:
                    removed_in_city += 1
                    total_removed += 1
                    print(f"  🗑️  Removed duplicate in [{filename}]: ID='{hid}' (Name='{h.get('name', 'N/A')}')")
                else:
                    seen_ids.add(hid)
                    unique_highlights.append(h)
            
            if removed_in_city > 0:
                data['highlights'] = unique_highlights
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
                cities_affected += 1
                
        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print(f"\n🎉 Duplicate removal complete!")
print(f"📊 Summary: Removed a total of {total_removed} duplicate cards across {cities_affected} city files.")
