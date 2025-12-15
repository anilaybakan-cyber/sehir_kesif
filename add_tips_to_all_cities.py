import json
import os
import glob

# Cities directory
cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

# General tips by category
category_tips = {
    "Tarihi": "Erken saatlerde veya kapanışa yakın giderseniz kalabalıktan kaçınabilirsiniz.",
    "Manzara": "Gün batımında gitmek için ideal bir nokta. Fotoğraf makinenizi unutmayın.",
    "Müze": "Biletinizi önceden online alarak sıra beklemekten kurtulabilirsiniz.",
    "Park": "Hafta içi daha sakin olur. Yanınıza su ve atıştırmalık almayı unutmayın.",
    "Restoran": "Özellikle akşam yemekleri için rezervasyon yaptırmanızı öneririz.",
    "Kafe": "Kahve yanında yerel tatlılarını denemeyi unutmayın.",
    "Bar": "Happy Hour saatlerini (genelde 17:00-20:00) yakalamaya çalışın.",
    "Alışveriş": "Yerel butikleri keşfetmek için harika bir bölge.",
    "Semt": "Ara sokaklarında kaybolarak şehrin gerçek ruhunu hissedin.",
    "Meydan": "Çevredeki kafelerden birinde oturup gelip geçeni izlemek çok keyifli.",
    "Plaj": "Havlunuzu, güneş kreminizi ve şapkanızı almayı unutmayın.",
    "Eğlence": "Etkinlik takvimini önceden kontrol etmenizde fayda var.",
    "Sanat": "Sergiler hakkında önceden bilgi alarak gitmenizi öneririz."
}

# Specific tips for famous places
specific_tips = {
    # Barcelona
    "Sagrada Familia": "Kulelere çıkmak için biletinizi aylar öncesinden ayırtın.",
    "Park Güell": "Ücretsiz bölümleri de var ancak anıtsal bölge için bilet şart.",
    "Casa Batlló": "Akşam ışıklandırmasıyla dışarıdan fotoğraf çekmeyi unutmayın.",
    "La Boqueria": "Sabah erken saatlerde daha taze ürünler bulabilirsiniz.",
    "Picasso Müzesi": "Perşembe akşamları veya ayın ilk Pazar günü ücretsiz giriş olabilir, kontrol edin.",
    "Camp Nou": "Maç günleri çok kalabalık olur, müze turu için maç olmadığı günleri seçin.",
    "La Rambla": "Kalabalıkta cüzdanınıza dikkat edin, sokak sanatçılarını izleyin.",
    "Barceloneta Beach": "Sabah erken saatlerde deniz daha temiz ve sahil sakin olur.",
    "Gothic Quarter": "Dar sokaklarda kaybolun, akşamları atmosfer çok daha büyüleyici.",
    
    # Istanbul
    "Ayasofya": "Namaz vakitleri dışında ziyaret etmek daha rahat olabilir.",
    "Topkapı Sarayı": "Harem bölümü için ayrı bilet gerektiğini unutmayın.",
    "Kapalıçarşı": "Pazarlık yapmaktan çekinmeyin, esnafla sohbet edin.",
    "Galata Kulesi": "Gün batımında sıra çok olabilir, sabah erken gitmeyi deneyin.",
    "Sultanahmet Camii": "Ziyaret kıyafet kurallarına dikkat edin, örtülerinizi yanınıza alın.",
    "Yerebatan Sarnıcı": "Nemli olabilir, ince bir hırka yanınızda bulunsun.",
    "Dolmabahçe Sarayı": "Günlük ziyaretçi kotası olabilir, biletinizi erken alın.",
    "Mısır Çarşısı": "Baharatların kokusunu içinize çekin, tadım yapmaktan çekinmeyin.",
    "Taksim Meydanı": "İstiklal Caddesi boyunca yürüyüp nostaljik tramvayı izleyin.",
    "Kız Kulesi": "Restorasyonu kontrol edin, sahilden gün batımını izlemek de harika.",
    "Balat": "Renkli evleri ve vintage dükkanları keşfetmek için yürüyüş yapın.",
    "Moda Sahili": "Akşamüstü çimlere yayılıp gün batımını seyretmek bir klasik.",
}

def get_tip(place):
    name = place.get("name", "")
    category = place.get("category", "")
    
    # 1. Check specific tips
    if name in specific_tips:
        return specific_tips[name]
    
    # 2. Check partial matches for keys (e.g. "Ayasofya Camii" matches "Ayasofya")
    for key, tip in specific_tips.items():
        if key in name:
            return tip
            
    # 3. Check category tips
    if category in category_tips:
        return category_tips[category]
        
    # 4. Default tip
    return "Yerel halkın favori noktalarından biri, keyfini çıkarın!"

def process_files():
    json_files = glob.glob(os.path.join(cities_dir, "*.json"))
    print(f"Found {len(json_files)} JSON files.")
    
    count = 0
    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            city_name = data.get("city", "Unknown")
            highlights = data.get("highlights", [])
            updated_count = 0
            
            for place in highlights:
                if "tips" not in place or not place["tips"]:
                    place["tips"] = get_tip(place)
                    updated_count += 1
            
            if updated_count > 0:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Updated {city_name}: Added tips to {updated_count} places.")
                count += 1
            else:
                print(f"Skipped {city_name}: No updates needed.")
                
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            
    print(f"Finished! Updated {count} files.")

if __name__ == "__main__":
    process_files()
