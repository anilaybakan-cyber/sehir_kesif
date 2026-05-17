import json
import urllib.request
import urllib.parse
from urllib.error import URLError

places = [
    ("Concertgebouw", "Concertgebouw"),
    ("Newmarkt", "Nieuwmarkt"),
    ("IJ Ferry Cruise", "IJ (Amsterdam)")
]

def get_wiki_image(page_title):
    query = urllib.parse.quote(page_title)
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={query}&prop=pageimages&format=json&pithumbsize=1000"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            for page_id, page_info in pages.items():
                if 'thumbnail' in page_info:
                    return page_info['thumbnail']['source']
    except Exception as e:
        print(f"Error fetching {page_title}: {e}")
    
    # Try Dutch wiki as fallback
    url_nl = f"https://nl.wikipedia.org/w/api.php?action=query&titles={query}&prop=pageimages&format=json&pithumbsize=1000"
    try:
        req = urllib.request.Request(url_nl, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            pages = data['query']['pages']
            for page_id, page_info in pages.items():
                if 'thumbnail' in page_info:
                    return page_info['thumbnail']['source']
    except Exception as e:
        pass
        
    return None

new_images = {}
for app_name, search_name in places:
    img_url = get_wiki_image(search_name)
    if img_url:
        print(f"✅ Found for {app_name}: {img_url}")
        new_images[app_name] = img_url
    else:
        print(f"❌ Failed for {app_name}")

file_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/amsterdam.json'

with open(file_path, 'r', encoding='utf-8') as f:
    city_data = json.load(f)

updated_count = 0
for highlight in city_data.get('highlights', []):
    name = highlight.get('name')
    if name in new_images:
        highlight['image'] = new_images[name]
        updated_count += 1
        print(f"Updated JSON for {name}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"Done. Updated {updated_count} highlights.")
