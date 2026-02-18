import json
import os
import urllib.request
import urllib.parse
import time

API_KEY = "AIzaSyBOXbf-5v4aXyEYgciwX4EfPYAGXX6Yy9g"

# Detailed descriptions for Batch 2 cities
DESCRIPTIONS = {
    "giethoorn": {
        "Giethoorn Canals": {
            "tr": "Giethoorn'un 'Kuzeyin Venedik'i' olarak anılmasını sağlayan bu huzurlu kanallar, köyün ana ulaşım ağıdır. Motorlu taşıtların yasak olduğu bu sularda, sessiz teknelerle süzülürken saz çatılı evlerin büyüleyici manzarasının tadını çıkarabilirsiniz.",
             "en": "These peaceful canals, earning Giethoorn the nickname 'Venice of the North', form the village's main transportation network. While gliding through these waters where motorized vehicles are banned, you can enjoy the enchanting view of thatched-roof houses."
        },
        "Museum Giethoorn 't Olde Maat Uus": {
            "tr": "Tarihi bir çiftlik evinde kurulan bu müze, Giethoorn'un son yüzyıldaki yaşam tarzını ve turba çıkarma tarihini gözler önüne seriyor. Geleneksel kostümler ve ev eşyalarıyla donatılmış odalarda geçmişe yolculuk yapabilirsiniz.",
            "en": "Set in a historic farmhouse, this museum reveals the lifestyle and peat mining history of Giethoorn over the last century. You can travel back in time in rooms furnished with traditional costumes and household items."
        },
         "Weerribben-Wieden National Park": {
             "tr": "Kuzeybatı Avrupa'nın en büyük bataklık alanı olan bu milli park, nadir su kuşları ve bitki türlerine ev sahipliği yapar. Kano ile sazlıkların arasında kaybolmak, doğa severler için eşsiz bir deneyimdir.",
             "en": "As Northwestern Europe's largest peat marsh, this national park is home to rare water birds and plant species. Getting lost among the reeds in a canoe is a unique experience for nature lovers."
         }
    },
    "kotor": {
         "Kotor Old Town": {
             "tr": "UNESCO Dünya Mirası listesindeki bu ortaçağ şehri, daracık taş sokakları ve Venedik mimarisiyle bir labirenti andırır. Her köşede karşınıza çıkan kediler, tarihi meydanlar ve gizli avlular şehrin ruhunu oluşturur.",
             "en": "This UNESCO World Heritage medieval city resembles a labyrinth with its narrow stone streets and Venetian architecture. The cats meeting you at every corner, historic squares, and hidden courtyards make up the city's soul."
         },
         "Castle of San Giovanni": {
             "tr": "Şehri kuşbakışı izlemek isteyenler için 1350 basamaklı zorlu bir tırmanış sunan kale, körfezin en ikonik manzarasına sahiptir. Zirveye ulaştığınızda göreceğiniz Kotor Körfezi manzarası, tüm yorgunluğunuza değecek.",
             "en": "Offering a challenging 1350-step climb for those wanting a bird's-eye view, the castle boasts the most iconic panorama of the bay. The view of the Bay of Kotor from the summit makes all the effort worthwhile."
         }
    },
    "colmar": {
         "La Petite Venise": {
             "tr": "Lauch nehri boyunca sıralanmış rengarenk yarı ahşap evleriyle Colmar'ın en romantik ve fotojenik bölgesidir. Küçük teknelerle yapacağınız gezinti, bu masalsı atmosferi su üzerinden deneyimlemenizi sağlar.",
             "en": "Lined with colorful half-timbered houses along the Lauch River, this is Colmar's most romantic and photogenic district. A trip on small boats allows you to experience this fairytale atmosphere from the water."
         },
         "Unterlinden Museum": {
             "tr": "Eski bir manastırda yer alan müze, ünlü Isenheim Sunağı başta olmak üzere Ortaçağ ve Rönesans sanatının başyapıtlarını barındırır. Picasso ve Monet gibi modern ustaların eserleri de koleksiyonun önemli bir parçasıdır.",
             "en": "Housed in a former convent, the museum hosts masterpieces of Medieval and Renaissance art, notably the famous Isenheim Altarpiece. Works by modern masters like Picasso and Monet are also a significant part of the collection."
         }
    },
     "sintra": {
         "Pena Palace": {
             "tr": "Tepenin zirvesinde yükselen sarı ve kırmızı kuleleriyle Pena Sarayı, Romantizm mimarisinin dünyadaki en çarpıcı örneğidir. Masalsı görünümü ve egzotik bahçeleri, ziyaretçileri kralların hayal dünyasına davet eder.",
             "en": "Rising atop the hill with its yellow and red towers, Pena Palace is the world's most striking example of Romanticist architecture. Its fairytale appearance and exotic gardens invite visitors into the dream world of kings."
         },
         "Quinta da Regaleira": {
             "tr": "Gotik mimarisi, gizli tünelleri ve sembolik 'İnisiyasyon Kuyusu' ile ünlü bu malikane, tam bir gizem bahçesidir. Kuyuya inen spiral merdivenler, Dante'nin İlahi Komedya'sına atıfta bulunan mistik bir yolculuğu simgeler.",
             "en": "Famous for its Gothic architecture, secret tunnels, and symbolic 'Initiation Well', this estate is a true garden of mystery. The spiral stairs descending into the well symbolize a mystical journey referencing Dante's Divine Comedy."
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
                 place["description"] = f"{original_tr} Bu mekan, etkileyici atmosferi ve sunduğu eşsiz deneyimlerle {city_name.capitalize()}'nın en sevilen noktalarından biridir. Ziyaretçiler burada hem yerel kültürü tanıyabilir hem de unutulmaz anılar biriktirebilirler."
                 
            original_en = place.get("description_en", "")
            if len(original_en.split('.')) < 2 and len(original_en) > 5:
                 place["description_en"] = f"{original_en} With its impressive atmosphere and unique experiences, this venue is one of {city_name.capitalize()}'s most beloved spots. Visitors can discover local culture here and create unforgettable memories."

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ {city_name} updated: {updated_count} photos fetched.")

if __name__ == "__main__":
    cities = ["giethoorn", "kotor", "colmar", "sintra"]
    for city in cities:
        update_city(city)
