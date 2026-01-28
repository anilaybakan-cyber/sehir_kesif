import json
import os
import csv
import re

def extract_sections(content):
    if not content:
        return []
    
    # Split by headers (## )
    # We want to capture both the header and the following content
    pattern = r'## (.*?)\n(.*?)(?=## |\Z)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    sections = []
    for title, body in matches:
        sections.append({
            'title': title.strip(),
            'content': body.strip()
        })
        
    return sections

def main():
    guides_dir = '/Users/anilebru/Desktop/Uygulamalar/myway-data/guides'
    output_file = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/city_guides_export.csv'
    
    files = [f for f in os.listdir(guides_dir) if f.endswith('.json')]
    files.sort()
    
    header = ['City', 'Index', 'Header (TR)', 'Content (TR)', 'Header (EN)', 'Content (EN)']
    
    with open(output_file, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        
        for filename in files:
            city_name = filename.replace('.json', '').capitalize()
            # Special cases for capitalization
            if city_name == 'Newyork': city_name = 'New York'
            
            with open(os.path.join(guides_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                tr_content = data.get('tr', '')
                en_content = data.get('en', '')
                
                tr_sections = extract_sections(tr_content)
                en_sections = extract_sections(en_content)
                
                # Pair them up
                max_len = max(len(tr_sections), len(en_sections))
                
                for i in range(max_len):
                    tr_title = tr_sections[i]['title'] if i < len(tr_sections) else ''
                    tr_body = tr_sections[i]['content'] if i < len(tr_sections) else ''
                    en_title = en_sections[i]['title'] if i < len(en_sections) else ''
                    en_body = en_sections[i]['content'] if i < len(en_sections) else ''
                    
                    writer.writerow([city_name, i+1, tr_title, tr_body, en_title, en_body])
                    
    print(f"Export completed: {output_file}")

if __name__ == '__main__':
    main()
