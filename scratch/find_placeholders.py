import json
import os

GENERIC_STRING = "kıyılarında yer alan bu plaj, kristal berraklığındaki suyu ve doğal yapısıyla bilinir"

def find_placeholders(dir_path):
    targets = []
    for filename in os.listdir(dir_path):
        if filename.endswith('.json'):
            file_path = os.path.join(dir_path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                highlights = data.get('highlights', [])
                for h in highlights:
                    desc = h.get('description', '')
                    if GENERIC_STRING in desc:
                        targets.append({
                            'city': filename,
                            'name': h.get('name'),
                            'id': h.get('id')
                        })
            except:
                continue
    return targets

if __name__ == "__main__":
    targets = find_placeholders('/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities')
    print(json.dumps(targets, indent=2, ensure_ascii=False))
