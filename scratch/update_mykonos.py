import json
import os

UPDATES = {
    "mykonos.json": {
        "ChIJn6Wflay_ohQRVP0VIqpNGAM": { # Paradise Beach Club
            "tr": "Mykonos'un en ikonik ve canlı plajlarından biridir. Özellikle öğleden sonra başlayan yüksek sesli müzik ve partileriyle ünlüdür. Turkuaz suları ve geniş kumsalıyla hem güneşlenmek hem de eğlenmek isteyenlerin ilk durağıdır.",
            "en": "One of Mykonos' most iconic and lively beaches. Famous for its high-energy parties and music that usually kick off in the afternoon. With its turquoise waters and vast sandy shore, it's a top choice for both sunbathing and partying."
        },
        "ChIJmTndipW-ohQRU8nVD4FLx5c": { # Super Paradise
            "tr": "Efsanevi plaj partileri ve özgürlükçü atmosferiyle tanınan Super Paradise, kristal berraklığındaki sularıyla büyüleyicidir. Gün boyu süren eğlencesi ve şık plaj kulüpleriyle Mykonos gece hayatının plajdaki yansımasıdır.",
            "en": "Known for its legendary beach parties and inclusive atmosphere, Super Paradise is stunning with its crystal-clear waters. With entertainment lasting all day and chic beach clubs, it's the beachside reflection of Mykonos nightlife."
        },
        "ChIJUQXXb4u4ohQRU4DdMAU52y8": { # Kalafati Beach
            "tr": "Özellikle rüzgar sörfü tutkunları için bir cennet olan Kalafati, geniş kumsalı ve daha sakin atmosferiyle bilinir. Su sporları yapmak isteyenler ve aileler için ideal, geniş ve huzurlu bir plajdır.",
            "en": "A paradise especially for windsurfing enthusiasts, Kalafati is known for its wide sandy shore and calmer atmosphere. It's an ideal, spacious, and peaceful beach for water sports lovers and families."
        },
        "ChIJkcvmGA-_ohQR1jb08ltTwsk": { # Ornos Beach
            "tr": "Şehir merkezine yakınlığı ve sığ, sakin sularıyla aileler için en popüler noktalardan biridir. Çevresindeki çok sayıda restoran ve kafe ile gün boyu konforlu bir deniz keyfi sunar.",
            "en": "One of the most popular spots for families due to its proximity to the town center and shallow, calm waters. It offers a comfortable day at the sea with many surrounding restaurants and cafes."
        },
        "ChIJtUVAGQDBohQRzEJBhezqKz0": { # Panormos Beach
            "tr": "Mykonos'un kuzey kıyısında yer alan bu koy, bohem ve şık plaj kulüpleriyle ünlüdür. Daha sofistike bir atmosfer arayanların tercihi olan plaj, muhteşem kum yapısı ve rüzgara karşı korunaklı yapısıyla dikkat çeker.",
            "en": "Located on the northern coast of Mykonos, this bay is famous for its bohemian and chic beach clubs. Preferred by those seeking a more sophisticated atmosphere, the beach stands out with its great sand and sheltered position against the wind."
        },
        "ChIJ1ZguRlK_ohQRfdi5KWfxN6I": { # Paralia Ftelias
            "tr": "Kuzey rüzgarlarını alan yapısı sayesinde sörfçülerin uğrak noktasıdır. Daha doğal ve daha az kalabalık bir seçenek arayanlar için idealdir; bohem restoranları ve vahşi güzelliğiyle bilinir.",
            "en": "A favorite spot for surfers thanks to its exposure to northern winds. Ideal for those looking for a more natural and less crowded option, known for its bohemian restaurants and wild beauty."
        },
        "ChIJcXSe8ui4ohQRtZGsixRki4A": { # Paralia Kalo Livadi
            "tr": "Adanın en büyük kumsallarından birine sahip olan Kalo Livadi, geniş alanı ve trend plaj kulüpleriyle öne çıkar. Gençler ve moda tutkunları arasında oldukça popüler olan, ferah bir yüzme alanıdır.",
            "en": "Boasting one of the island's largest sandy shores, Kalo Livadi stands out with its vast area and trendy beach clubs. It's a spacious swimming spot very popular among young people and fashion enthusiasts."
        },
        "ChIJgaK6vV2-ohQRF5BMBTfZDB4": { # Farina Cucina Italiana
            "tr": "Ornos Plajı yakınında yer alan bu şık İtalyan restoranı, odun fırınında pişen gerçek pizzaları ve taze makarnalarıyla ünlüdür. Deniz keyfine lezzetli bir İtalyan molası vermek isteyenlerin favorisidir.",
            "en": "Located near Ornos Beach, this chic Italian restaurant is famous for its authentic wood-fired pizzas and fresh pastas. It's a favorite for those wanting to take a delicious Italian break during their beach day."
        },
        "ChIJ22TzgSi5ohQR5XRgwFeCc-U": { # GoDive Mykonos
            "tr": "Lia Plajı'nın kristal sularında hizmet veren bu dalış merkezi, sualtı dünyasını keşfetmek isteyenler için PADI eğitimleri ve keşif dalışları sunar. Profesyonel ekibiyle güvenli ve unutulmaz bir deneyim vadeder.",
            "en": "Operating in the crystal waters of Lia Beach, this diving center offers PADI courses and discovery dives for those wanting to explore the underwater world. It promises a safe and unforgettable experience with its professional team."
        }
    }
}

def apply_updates():
    base_path = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
    for city_file, data_updates in UPDATES.items():
        file_path = os.path.join(base_path, city_file)
        if not os.path.exists(file_path): continue
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        highlights = data.get('highlights', [])
        updated_count = 0
        for h in highlights:
            h_id = h.get('id')
            if h_id in data_updates:
                h['description'] = data_updates[h_id]['tr']
                h['description_en'] = data_updates[h_id]['en']
                updated_count += 1
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {updated_count} items in {city_file}")

if __name__ == "__main__":
    apply_updates()
