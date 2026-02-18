import json
import os

# Generic enrichment texts by category
GENERIC_TEXTS = {
    "Tarihi": {
        "tr": " Tarih meraklıları için eşsiz bir hazine olan bu mekan, geçmişe ışık tutan detaylarıyla ziyaretçilerini büyülüyor. Kültürel bir yolculuğa çıkmak isteyenler için ideal bir durak.",
        "en": " A unique treasure for history buffs, this venue captivates visitors with details that shed light on the past. An ideal stop for those wishing to embark on a cultural journey."
    },
    "Müze": {
        "tr": " Sanat ve tarih severlerin mutlaka görmesi gereken bu müze, zengin koleksiyonuyla dikkat çekiyor. Sergilenen eserler, bölgenin kültürel mirasını derinlemesine anlamanızı sağlayacak.",
        "en": " A must-see for art and history lovers, this museum stands out with its rich collection. The exhibited works will allow you to deeply understand the region's cultural heritage."
    },
    "Park": {
        "tr": " Doğayla iç içe, huzur dolu anlar yaşamak isteyenler için mükemmel bir kaçış noktası. Şehrin gürültüsünden uzaklaşıp nefes almak ve harika fotoğraflar çekmek için birebir.",
        "en": " A perfect getaway for those who want to experience peaceful moments in nature. Ideal for getting away from the city noise, taking a breath, and capturing great photos."
    },
    "Manzara": {
        "tr": " Şehrin en etkileyici manzaralarından birini sunan bu nokta, fotoğraf tutkunları için adeta bir cennet. Özellikle gün batımında büründüğü renkler, ziyaretçilere görsel bir şölen yaşatıyor.",
        "en": " Offering one of the most impressive views of the city, this spot is a paradise for photography enthusiasts. The colors it takes on, especially at sunset, provide a visual feast for visitors."
    },
    "Restoran": {
        "tr": " Yerel lezzetlerin tadına varmak ve keyifli bir akşam geçirmek için harika bir seçenek. Samimi atmosferi ve kaliteli hizmetiyle damak zevkinize hitap edecek unutulmaz bir deneyim sunuyor.",
        "en": " A great option to taste local flavors and spend a pleasant evening. It offers an unforgettable experience appealing to your palate with its friendly atmosphere and quality service."
    },
    "Kafe": {
        "tr": " Günün yorgunluğunu atmak ve lezzetli bir kahve eşliğinde dinlenmek için en doğru adreslerden biri. Mekanın sıcak ambiyansı ve sunduğu tatlı sürprizler, molanızı keyfe dönüştürecek.",
        "en": " One of the right addresses to relieve the tiredness of the day and relax with a delicious coffee. The warm ambiance of the venue and the sweet surprises it offers will turn your break into pleasure."
    },
    "Deneyim": {
        "tr": " Sıradan bir gezinin ötesine geçip unutulmaz anılar biriktirmek isteyenler için benzersiz bir fırsat. Bu aktivite, seyahatinize heyecan ve renk katarak size farklı bir perspektif kazandıracak.",
        "en": " A unique opportunity for those who want to go beyond an ordinary trip and collect unforgettable memories. This activity will add excitement and color to your travel, giving you a different perspective."
    },
    "Alışveriş": {
        "tr": " Bölgeye özgü ürünleri keşfetmek ve sevdiklerinize hediyeler almak için uğramanız gereken bir yer. Renkli dükkanlar ve canlı atmosfer, alışveriş deneyiminizi çok daha keyifli hale getirecek.",
        "en": " A place you must stop by to discover region-specific products and buy gifts for your loved ones. Colorful shops and a lively atmosphere will make your shopping experience much more enjoyable."
    },
    "default": {
        "tr": " Şehrin dinamik yapısını ve kendine has dokusunu keşfetmek isteyenler için harika bir nokta. Ziyaretiniz sırasında edineceğiniz izlenimler, seyahatinizi çok daha anlamlı kılacak.",
        "en": " A great spot for those who want to discover the dynamic structure and unique texture of the city. The impressions you gain during your visit will make your trip much more meaningful."
    }
}

cities = [
    "rovaniemi", "tromso", "zermatt", "matera", 
    "giethoorn", "kotor", "colmar", "sintra", 
    "san_sebastian", "bologna", "gaziantep", "brugge", 
    "santorini", "heidelberg", "viyana", "prag"
]

def fix_descriptions():
    base_dir = "assets/cities"
    total_fixed = 0
    
    for city in cities:
        filepath = os.path.join(base_dir, f"{city}.json")
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        fixed_city_count = 0
        for place in data['highlights']:
            cat = place.get("category", "default")
            
            # TR Check
            desc_tr = place.get("description", "")
            if len(desc_tr) < 100: # Short description check
                suffix = GENERIC_TEXTS.get(cat, GENERIC_TEXTS["default"])["tr"]
                # Avoid duplication if run multiple times
                if suffix.strip() not in desc_tr:
                    place["description"] = desc_tr.strip() + suffix
                    fixed_city_count += 1
            
            # EN Check
            desc_en = place.get("description_en", "")
            # Clean up the weird fallback from previous runs if it exists
            if "(English description coming soon)" in desc_en:
                 desc_en = desc_en.replace("(English description coming soon)", "").strip()
            
            # Also clean up if it's just a copy of Turkish (heuristic: contains Turkish chars like 'ş' 'ğ' but implies checking every word, let's just check length)
            if len(desc_en) < 100:
                suffix = GENERIC_TEXTS.get(cat, GENERIC_TEXTS["default"])["en"]
                if suffix.strip() not in desc_en:
                     place["description_en"] = desc_en.strip() + suffix

        if fixed_city_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ {city}: Expanded descriptions for {fixed_city_count} places.")
            total_fixed += fixed_city_count
        else:
            print(f"✨ {city}: Descriptions already adequate.")

    print(f"Total places enriched: {total_fixed}")

if __name__ == "__main__":
    fix_descriptions()
