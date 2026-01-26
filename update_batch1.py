import json
import os
import urllib.request
import urllib.parse
import time

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Detailed descriptions for Batch 1 cities
DESCRIPTIONS = {
    "rovaniemi": {
        "Pilke Science Centre": {
            "tr": "Pilke Bilim Merkezi, Finlandiya'nın kuzey ormanlarını ve sürdürülebilir ahşap kullanımını interaktif sergilerle anlatıyor. Ziyaretçiler, gerçek orman makinelerini deneyimleyebilir ve doğa ile iç içe eğlenceli vakit geçirebilirler.",
            "en": "Pilke Science Centre tells the story of northern forests and sustainable wood use through interactive exhibits. Visitors can experience real forest machines and have fun connecting with nature."
        },
        "Korundi House of Culture": {
            "tr": "Laponya'nın kalbinde yer alan Korundi, modern sanat sergilerine ve Rovaniemi Oda Orkestrası'nın konserlerine ev sahipliği yapıyor. Tarihi kırmızı tuğlalı bina, hem mimarisiyle hem de sunduğu kültürel etkinliklerle sanatseverleri büyülüyor.",
            "en": "Located in the heart of Lapland, Korundi hosts modern art exhibitions and concerts by the Rovaniemi Chamber Orchestra. The historic red brick building captivates art lovers with both its architecture and cultural events."
        },
        "Rovaniemi Art Museum": {
            "tr": "Eski bir posta otobüsü deposundan dönüştürülen bu müze, Fin çağdaş sanatına ve kuzey kültürüne odaklanıyor. Koleksiyonlarında Laponya'nın doğasından ve insanlarından ilham alan etkileyici eserler sergileniyor.",
            "en": "Converted from an old post bus depot, this museum focuses on Finnish contemporary art and northern culture. Its collections feature impressive works inspired by Lapland's nature and people."
        },
        "Santa Claus Village": {
            "tr": "Noel Baba'nın resmi evi olan bu büyülü köy, yılın her günü Noel ruhunu yaşatıyor. Kuzey Kutup Dairesi çizgisini geçebilir, Noel Baba ile tanışabilir ve sevdiklerinize özel mühürlü kartpostallar gönderebilirsiniz.",
            "en": "The official hometown of Santa Claus, this magical village keeps the Christmas spirit alive all year round. You can cross the Arctic Circle line, meet Santa Claus, and send specially stamped postcards to loved ones."
        },
         "Ounasvaara Ski Resort": {
             "tr": "Şehir merkezine sadece birkaç dakika uzaklıkta bulunan Ounasvaara, hem kayak hem de doğa yürüyüşü için mükemmel bir kaçış noktasıdır. Tepeden Rovaniemi'nin ve Kemijoki nehrinin nefes kesen manzarasını izleyebilirsiniz.",
             "en": "Located just minutes from the city center, Ounasvaara is a perfect getaway for both skiing and hiking. From the top, you can enjoy breathtaking views of Rovaniemi and the Kemijoki river."
         },
         "Arktikum Bridge": {
             "tr": "Arktikum Bilim Merkezi'ne giden bu cam tünel, özellikle kışın donmuş nehir manzarasıyla büyüleyicidir. Kuzey ışıklarını izlemek için şehrin içindeki en iyi ve en romantik noktalardan biridir.",
             "en": "This glass tunnel leading to the Arktikum Science Centre is mesmerizing, especially with frozen river views in winter. It is one of the best and most romantic spots within the city to watch the Northern Lights."
         }
         # Diğerleri için varsayılan zenginleştirilmiş metin kullanılacak
    },
    # ... Diğer şehirler için de benzer detaylı açıklamalar eklenecek
}

def get_google_photo(query):
    """Fetches a photo URL from Google Places API."""
    try:
        # 1. Text Search to get place_id and photo_reference
        search_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={urllib.parse.quote(query)}&key={API_KEY}"
        with urllib.request.urlopen(search_url) as response:
            data = json.loads(response.read().decode())
        
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            if "photos" in result:
                photo_ref = result["photos"][0]["photo_reference"]
                # 2. Construct Photo URL (max width 800)
                photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
                return photo_url
            else:
                 # Bazı yerlerin fotosu olmayabilir, o zaman icon veya geometry fotosu deneyebiliriz ama şimdilik placeholder kalsın
                 pass
        return None
    except Exception as e:
        print(f"Error fetching photo for {query}: {e}")
        return None

def update_city(city_name):
    filepath = f"assets/cities/{city_name}.json"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Updating {city_name} with {len(data['highlights'])} places...")
    
    updated_count = 0
    for place in data['highlights']:
        # 1. Update Photo
        # Sadece placeholder olanları güncelle veya hepsini (kullanıcı api ile çek dedi)
        # Unsplash linki varsa veya boşsa güncelle
        if "unsplash" in place.get("imageUrl", "") or not place.get("imageUrl"):
            print(f"  Fetching photo for {place['name']}...")
            new_photo = get_google_photo(f"{place['name']} {city_name}")
            if new_photo:
                place["imageUrl"] = new_photo
                updated_count += 1
                time.sleep(0.2) # API rate limit protection

        # 2. Update Description
        # Manuel sözlükten kontrol et
        city_desc = DESCRIPTIONS.get(city_name, {})
        place_desc = city_desc.get(place['name'])
        
        if place_desc:
            place["description"] = place_desc["tr"]
            place["description_en"] = place_desc["en"]
        else:
            # Eğer manuel açıklama yoksa, mevcut açıklamayı uzat (basit bir mantıkla)
            # Mevcut açıklama zaten var, ama tek cümle.
            # Zenginleştirme:
            original_tr = place.get("description", "")
            if len(original_tr.split('.')) < 2 and len(original_tr) > 5:
                 place["description"] = f"{original_tr} Bu mekan, {city_name.capitalize()} ziyaretinizde mutlaka görülmesi gereken, kendine has atmosferiyle büyüleyen özel bir yerdir."
                 
            original_en = place.get("description_en", "")
            if len(original_en.split('.')) < 2 and len(original_en) > 5:
                 place["description_en"] = f"{original_en} This venue is a must-see spot in {city_name.capitalize()} that captivates visitors with its unique atmosphere."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {city_name} updated: {updated_count} photos fetched.")

if __name__ == "__main__":
    cities = ["rovaniemi", "tromso", "zermatt", "matera"]
    for city in cities:
        update_city(city)
