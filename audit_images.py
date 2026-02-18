import os
import json

def audit_images():
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    city_files = [f for f in os.listdir(assets_dir) if f.endswith('.json')]
    
    report = {}
    total_highlights = 0
    total_missing = 0
    
    for city_file in city_files:
        city_path = os.path.join(assets_dir, city_file)
        try:
            with open(city_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            continue
            
        highlights = data.get('highlights', [])
        missing_in_city = []
        
        for h in highlights:
            total_highlights += 1
            img = h.get('imageUrl')
            if not img or str(img).strip() == "" or "placeholder" in str(img).lower():
                missing_in_city.append(h.get('name', 'Unknown'))
                total_missing += 1
        
        if missing_in_city:
            report[city_file] = {
                "count": len(missing_in_city),
                "samples": missing_in_city[:5]
            }

    print(f"--- IMAGE AUDIT REPORT ---")
    print(f"Total Highlights Scanned: {total_highlights}")
    print(f"Total Missing/Placeholder Images: {total_missing}")
    print(f"Percentage Missing: {(total_missing/total_highlights)*100:.2f}%" if total_highlights > 0 else "0%")
    print("\nTop cities with missing images:")
    
    # Sort by count descending
    sorted_report = sorted(report.items(), key=lambda x: x[1]['count'], reverse=True)
    
    for city, info in sorted_report[:10]:
        print(f"- {city}: {info['count']} missing (e.g., {', '.join(info['samples'])})")

    if total_missing > 0:
        # Save full list to a file for review
        with open('missing_images_full.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"\nFull report saved to 'missing_images_full.json'")

if __name__ == "__main__":
    audit_images()
