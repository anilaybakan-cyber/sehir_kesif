import json
import os
import html

def escape_xml(text):
    if text is None: return ""
    return html.escape(str(text))

def export_contents_xml():
    ota_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/ota_data_pack/cities'
    assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    output_path = '/Users/anilebru/Desktop/icerikler2.xls' # Excel can open this XML format
    
    ota_files = {f: os.path.join(ota_dir, f) for f in os.listdir(ota_dir) if f.endswith('.json') and not f.endswith('.tmp')}
    assets_files = {f: os.path.join(assets_dir, f) for f in os.listdir(assets_dir) if f.endswith('.json') and not f.endswith('.tmp') and not '.bak.' in f}
    all_city_keys = sorted(list(set(ota_files.keys()) | set(assets_files.keys())))

    xml_header = """<?xml version="1.0"?>
<?mso-application progid="Excel.Sheet"?>
<Workbook xmlns="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:o="urn:schemas-microsoft-com:office:office"
 xmlns:x="urn:schemas-microsoft-com:office:excel"
 xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet"
 xmlns:html="http://www.w3.org/TR/REC-html40">
 <Worksheet ss:Name="Icerikler">
  <Table>
   <Row>
    <Cell><Data ss:Type="String">Source</Data></Cell>
    <Cell><Data ss:Type="String">City</Data></Cell>
    <Cell><Data ss:Type="String">Place Name</Data></Cell>
    <Cell><Data ss:Type="String">Description (TR)</Data></Cell>
    <Cell><Data ss:Type="String">Description (EN)</Data></Cell>
    <Cell><Data ss:Type="String">Tips (TR)</Data></Cell>
    <Cell><Data ss:Type="String">Tips (EN)</Data></Cell>
   </Row>"""

    xml_footer = """  </Table>
 </Worksheet>
</Workbook>"""

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(xml_header)
        
        for filename in all_city_keys:
            if filename in assets_files:
                file_path = assets_files[filename]
                source = "Assets"
            else:
                file_path = ota_files[filename]
                source = "OTA"
                
            city_name = filename.replace('.json', '').capitalize()
            
            try:
                with open(file_path, 'r', encoding='utf-8') as jf:
                    city_data = json.load(jf)
                    highlights = city_data.get('highlights', [])
                    
                    for h in highlights:
                        f.write("\n   <Row>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(source)}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(city_name)}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(h.get('name', ''))}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(h.get('description', ''))}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(h.get('description_en', ''))}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(h.get('tips', ''))}</Data></Cell>")
                        f.write(f"\n    <Cell><Data ss:Type=\"String\">{escape_xml(h.get('tips_en', ''))}</Data></Cell>")
                        f.write("\n   </Row>")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        
        f.write(xml_footer)
    
    print(f"Exported items to {output_path}")

if __name__ == "__main__":
    export_contents_xml()
