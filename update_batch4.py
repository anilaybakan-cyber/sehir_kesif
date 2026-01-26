import json
import os
import urllib.request
import urllib.parse
import time

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

DESCRIPTIONS = {
    "santorini": {
        "Oia Castle": {
             "tr": "Dünyanın en ünlü gün batımı manzaralarından birine ev sahipliği yapan Oia Kalesi, her akşam binlerce ziyaretçiyi ağırlar. Ege Denizi'nin sonsuz maviliği üzerinde batan güneşin turuncu ve pembe tonları, unutulmaz bir görsel şölen sunar.",
             "en": "Home to one of the world's most famous sunset views, Oia Castle welcomes thousands of visitors every evening. The orange and pink hues of the sun setting over the endless blue of the Aegean Sea offer an unforgettable visual feast."
        },
        "Red Beach": {
             "tr": "Volkanik kökenli kızıl kayalıkları ve koyu renkli kumsalıyla Santorini'nin en çarpıcı plajlarından biridir. Akrotiri antik kentine yakın konumuyla hem tarih hem de deniz keyfini bir arada sunan eşsiz bir doğal güzelliktir.",
             "en": "With its volcanic red cliffs and dark sands, this is one of Santorini's most striking beaches. Located near the ancient site of Akrotiri, it is a unique natural beauty offering both history and seaside enjoyment."
        }
    },
    "heidelberg": {
         "Heidelberg Castle": {
             "tr": "Alman Romantizminin sembolü sayılan bu görkemli kale kalıntısı, Neckar Nehri ve şehir manzarasını ayaklarınızın altına serer. Dünyanın en büyük şarap fıçısını görebileceğiniz mahzenleri ve tarihi eczane müzesiyle keşfedilmeyi bekler.",
             "en": "Considered the symbol of German Romanticism, these majestic castle ruins lay the view of the Neckar River and city at your feet. It awaits discovery with its cellars housing the world's largest wine barrel and the historic pharmacy museum."
         },
         "Old Bridge (Karl Theodor Bridge)": {
             "tr": "Neckar Nehri üzerinde uzanan bu zarif taş köprü, üzerindeki heykeller ve şehir kapısıyla Heidelberg'in en ikonik manzaralarından biridir. Köprüden kaleye bakış, şehrin romantik atmosferini hissetmek için en iyi açılardan birini sunar.",
             "en": "Spanning the Neckar River, this elegant stone bridge is one of Heidelberg's most iconic sights with its statues and city gate. The view of the castle from the bridge offers one of the best angles to feel the romantic atmosphere of the city."
         }
    },
    "viyana": {
         "Schönbrunn Palace": {
             "tr": "Habsburg hanedanının yazlık sarayı olan Schönbrunn, Barok mimarisi ve uçsuz bucaksız bahçeleriyle imparatorluk ihtişamını yansıtır. Rokoko tarzı odaları gezebilir, Gloriette tepesinden Viyana'yı seyredebilirsiniz.",
             "en": "The summer residence of the Habsburg dynasty, Schönbrunn reflects imperial splendor with its Baroque architecture and endless gardens. You can tour the Rococo style rooms and gaze at Vienna from the Gloriette hill."
         },
         "St. Stephen's Cathedral": {
             "tr": "Viyana'nın kalbinde yükselen bu Gotik şaheser, renkli çatı kiremitleri ve devasa kulesiyle şehrin en önemli simgesidir. Kuleye tırmanarak şehrin panoramik manzarasını izleyebilir ve yüzyıllık tarihi dokuyu hissedebilirsiniz.",
             "en": "Rising in the heart of Vienna, this Gothic masterpiece is the city's most important landmark with its colorful roof tiles and massive tower. Climbing the tower, you can view the city's panoramic landscape and feel the century-old historic texture."
         }
    },
     "prag": {
         "Charles Bridge": {
             "tr": "Vltava Nehri üzerindeki bu efsanevi taş köprü, barok heykelleri ve sokak sanatçılarıyla açık hava müzesi gibidir. Özellikle sabahın erken saatlerinde sisler arasından beliren kuleleriyle Prag'ın mistik havasını en iyi burada soluyabilirsiniz.",
             "en": "This legendary stone bridge over the Vltava River is like an open-air museum with its baroque statues and street artists. Especially in the early morning as towers emerge from the mist, this is where you can best breathe in Prague's mystical atmosphere."
         },
         "Astronomical Clock": {
             "tr": "Eski Şehir Meydanı'nda bulunan 600 yıllık bu astronomik saat, her saat başı gerçekleşen havari geçişi gösterisiyle turistleri büyüler. Ortaçağ mühendisliğinin bu harikası, zamanın ötesinde bir sanat eseri olarak varlığını sürdürüyor.",
             "en": "Located in the Old Town Square, this 600-year-old astronomical clock mesmerizes tourists with its hourly apostle parade show. This marvel of medieval engineering continues to exist as a timeless work of art."
         },
         "Prague Castle": {
             "tr": "Dünyanın en büyük antik kalesi unvanına sahip bu kompleks, sarayları, kiliseleri ve bahçeleriyle adeta bir şehir içinde şehirdir. Vitus Katedrali'nin görkemi ve Altın Yol'un masalsı evleri, ziyaretçileri büyülü bir tarih yolculuğuna çıkarır.",
             "en": "Holding the title of the world's largest ancient castle, this complex is a city within a city with its palaces, churches, and gardens. The grandeur of St. Vitus Cathedral and the fairytale houses of Golden Lane take visitors on a magical journey through history."
         }
    }
}

def get_google_photo(query):
    try:
        search_url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={urllib.parse.quote(query)}&key={API_KEY}"
        with urllib.request.urlopen(search_url) as response:
            data = json.loads(response.read().decode())
        
        if "results" in data and len(data["results"]) > 0:
            result = data["results"][0]
            if "photos" in result:
                photo_ref = result["photos"][0]["photo_reference"]
                return f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=800&photo_reference={photo_ref}&key={API_KEY}"
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
        if "unsplash" in place.get("imageUrl", "") or not place.get("imageUrl"):
            print(f"  Fetching photo for {place['name']}...")
            new_photo = get_google_photo(f"{place['name']} {city_name}")
            if new_photo:
                place["imageUrl"] = new_photo
                updated_count += 1
                time.sleep(0.2)

        city_desc = DESCRIPTIONS.get(city_name, {})
        place_desc = city_desc.get(place['name'])
        
        if place_desc:
            place["description"] = place_desc["tr"]
            place["description_en"] = place_desc["en"]
        else:
            original_tr = place.get("description", "")
            if len(original_tr.split('.')) < 2 and len(original_tr) > 5:
                 place["description"] = f"{original_tr} Tarihi dokusu ve kültürel önemiyle dikkat çeken bu nokta, {city_name.capitalize()} gezinizin en keyifli duraklarından biri olmaya aday. Etkileyici manzarası ve kendine has hikayesiyle sizi büyüleyecek."
                 
            original_en = place.get("description_en", "")
            if len(original_en.split('.')) < 2 and len(original_en) > 5:
                 place["description_en"] = f"{original_en} Notable for its historic texture and cultural significance, this spot is a candidate to be one of the most enjoyable stops of your {city_name.capitalize()} trip. It will captivate you with its impressive view and unique story."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {city_name} updated: {updated_count} photos fetched.")

if __name__ == "__main__":
    cities = ["santorini", "heidelberg", "viyana", "prag"]
    for city in cities:
        update_city(city)
