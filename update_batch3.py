import json
import os
import urllib.request
import urllib.parse
import time

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

DESCRIPTIONS = {
    "san_sebastian": {
        "La Concha Beach": {
             "tr": "Avrupa'nın en güzel şehir plajlarından biri olarak kabul edilen La Concha, altın sarısı kumsalı ve zarif sahil şeridiyle ünlüdür. Sakin sularında yüzebilir veya sahil boyunca keyifli bir yürüyüş yaparak körfezin büyüleyici manzarasını seyredebilirsiniz.",
             "en": "Considered one of Europe's most beautiful city beaches, La Concha is famous for its golden sands and elegant promenade. You can swim in its calm waters or take a pleasant walk along the coast to admire the captivating bay view."
        },
        "Parte Vieja (Old Town)": {
             "tr": "San Sebastian'ın kalbi olan bu tarihi bölge, dar sokaklarına gizlenmiş sayısız pintxos barı ile gastronomi tutkunlarını bekliyor. Her köşe başında farklı bir lezzet keşfedebilir ve Bask kültürünün canlı atmosferini deneyimleyebilirsiniz.",
             "en": "The heart of San Sebastian, this historic district awaits gastronomy lovers with countless pintxos bars hidden in its narrow streets. You can discover a different flavor around every corner and experience the vibrant atmosphere of Basque culture."
        },
         "Monte Igueldo": {
             "tr": "Eski bir fünikülerle çıkılan Monte Igueldo, şehrin ve körfezin en ikonik panoramik manzarasını sunar. Tepede bulunan tarihi lunapark, hem çocuklar hem de nostalji sevenler için keyifli anlar vaat ediyor.",
             "en": "Reached by an old funicular, Monte Igueldo offers the most iconic panoramic view of the city and bay. The historic amusement park at the top promises enjoyable moments for both children and nostalgia lovers."
         }
    },
    "bologna": {
         "Two Towers (Due Torri)": {
             "tr": "Ortaçağ'dan kalma bu iki eğik kule, Garisenda ve Asinelli, Bologna'nın en tanınmış simgeleridir. Asinelli Kulesi'nin 498 basamağını tırmananlar, şehrin kırmızı çatılarının oluşturduğu muazzam manzarayla ödüllendirilir.",
             "en": "These two leaning medieval towers, Garisenda and Asinelli, are Bologna's most recognizable landmarks. Those who climb the 498 steps of the Asinelli Tower are rewarded with a magnificent view formed by the city's red roofs."
         },
         "Piazza Maggiore": {
             "tr": "Şehrin kalbinin attığı bu devasa meydan, San Petronio Bazilikası ve Neptün Çeşmesi gibi tarihi yapılarla çevrilidir. Yaz aylarında açık hava sinemasına dönüşen meydan, günün her saati canlı ve hareketlidir.",
             "en": "This massive square where the city's heart beats is surrounded by historic structures like San Petronio Basilica and the Neptune Fountain. Turning into an open-air cinema in summer, the square is lively and bustling at all hours."
         }
    },
    "gaziantep": {
         "Zeugma Mozaik Müzesi": {
             "tr": "Dünyanın en büyük mozaik müzelerinden biri olan Zeugma, antik kentin kurtarılan eşsiz eserlerine ev sahipliği yapıyor. Müzenin en değerli parçası olan 'Çingene Kızı' mozaiği, büyüleyici bakışlarıyla ziyaretçileri kendine hayran bırakıyor.",
             "en": "One of the world's largest mosaic museums, Zeugma houses unique artifacts rescued from the ancient city. The museum's most precious piece, the 'Gypsy Girl' mosaic, mesmerizes visitors with her captivating gaze."
         },
         "Bakırcılar Çarşısı": {
             "tr": "Yüzyıllardır çekiç seslerinin yankılandığı bu tarihi çarşıda, bakır ustalarının el emeği göz nuru eserlerini görebilirsiniz. Geleneksel el sanatlarının yaşatıldığı sokaklarda dolaşmak, zamanda bir yolculuğa çıkmak gibidir.",
             "en": "In this historic bazaar where hammer sounds have echoed for centuries, you can see the handcrafted masterpieces of coppersmiths. Wandering through streets where traditional crafts are kept alive is like taking a journey back in time."
         },
         "Tahmis Kahvesi": {
             "tr": "1635 yılından beri hizmet veren Türkiye'nin en eski kahvehanelerinden biri olan Tahmis'te, meşhur menengiç kahvesini mutlaka denemelisiniz. Tarihi atmosferi ve otantik dokusuyla Antep kültürünün yaşayan bir parçasıdır.",
             "en": "Serving since 1635 as one of Turkey's oldest coffeehouses, Tahmis is a must-visit to try the famous menengiç coffee. With its historic atmosphere and authentic texture, it is a living part of Antep culture."
         }
    },
     "brugge": {
         "Grote Markt": {
             "tr": "Rengarenk lonca evleri ve görkemli Çan Kulesi ile çevrili Market Meydanı, Brugge'ün atan kalbidir. Meydandaki kafelerde oturup bu masalsı manzarayı izlemek veya at arabalarıyla tura çıkmak unutulmaz bir deneyimdir.",
             "en": "Surrounded by colorful guild houses and the majestic Belfry, the Market Square is the beating heart of Bruges. Sitting at cafes in the square to watch this fairytale view or taking a horse carriage tour is an unforgettable experience."
         },
         "Rozenhoedkaai": {
             "tr": "Brugge'ün en çok fotoğraflanan noktası olan Rozenhoedkaai, kanalların birleştiği büyüleyici bir manzaraya sahiptir. Özellikle gün batımında ve gece ışıklandırmasında, suyun üzerindeki yansımalarla tam bir kartpostal görüntüsü sunar.",
             "en": "The most photographed spot in Bruges, Rozenhoedkaai offers a captivating view where canals merge. Especially at sunset and with night illuminations, it presents a perfect postcard image with reflections on the water."
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
                 place["description"] = f"{original_tr} Şehrin dokusunu en iyi yansıtan bu mekan, hem yerli halkın hem de turistlerin uğrak noktasıdır. Mimari detayları ve sunduğu samimi ortam ile ziyaret listenizde mutlaka yer almalı."
                 
            original_en = place.get("description_en", "")
            if len(original_en.split('.')) < 2 and len(original_en) > 5:
                 place["description_en"] = f"{original_en} Best reflecting the city's texture, this venue is a frequent destination for both locals and tourists. It should definitely be on your visit list with its architectural details and welcoming atmosphere."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {city_name} updated: {updated_count} photos fetched.")

if __name__ == "__main__":
    cities = ["san_sebastian", "bologna", "gaziantep", "brugge"]
    for city in cities:
        update_city(city)
