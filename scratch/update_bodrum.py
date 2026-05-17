import json
import os

UPDATES = {
    "bodrum.json": {
        "ChIJr4tIU1BsvhQRoS_Wr1ONa3c": { # Bardakçı koyu
            "tr": "Bodrum merkezine en yakın ve en güzel koylardan biridir. Muhteşem Bodrum Kalesi manzarası, berrak suları ve Zeki Müren'in de en sevdiği yer olmasıyla ünlüdür. Sakin deniziyle sabah yüzüşleri için vazgeçilmezdir.",
            "en": "One of the closest and most beautiful bays to the center of Bodrum. Famous for its stunning view of Bodrum Castle, crystal-clear waters, and for being the favorite spot of Zeki Müren. It's a must for morning swims with its calm sea."
        },
        "ChIJjXnfySxpvhQREHdF1R97SoU": { # Torba Plajı
            "tr": "Bodrum'un kuzeyinde, çam ormanlarıyla çevrili huzurlu bir koydur. Diğer Bodrum plajlarına göre daha sakin olan denizi ve şık iskeleleriyle bilinir. Doğayla iç içe, kaliteli bir dinlenme arayanlar için idealdir.",
            "en": "A peaceful bay north of Bodrum, surrounded by pine forests. Known for its calmer sea compared to other Bodrum beaches and its chic piers. Ideal for those seeking a quality retreat in touch with nature."
        },
        "ChIJlW24DwJ-vhQR0nYmhIFwRfI": { # Blue Point Didim Beach Club
            "tr": "Didim'in en popüler ve şık plaj kulüplerinden biridir. Modern tasarımı, kaliteli müzikleri ve geniş güneşlenme alanlarıyla konforlu bir plaj deneyimi sunar. Akşamüstü partileriyle de oldukça ilgi görür.",
            "en": "One of Didim's most popular and chic beach clubs. It offers a comfortable beach experience with its modern design, quality music, and vast sunbathing areas. Its late afternoon parties are also quite a draw."
        },
        "ChIJWYUGxK1tvhQR0iCNUnMPS_U": { # Nagi Beach Hotel
            "tr": "Gümbet'in hareketli sahilinde yer alan bu otel plajı, merkezi konumu ve eğlenceli atmosferiyle bilinir. Gündüz güneşin tadını çıkarırken, çevredeki sosyal olanaklara kolayca erişim sağlar.",
            "en": "Located on the vibrant coast of Gümbet, this hotel beach is known for its central location and fun atmosphere. It provides easy access to surrounding social amenities while enjoying the sun during the day."
        },
        "ChIJNQTYPqZtvhQR-bQKEunNvQc": { # AYAZ AQUA BEACH HOTEL
            "tr": "Özellikle aileler için tasarlanmış, denize sıfır bir konaklama ve dinlenme noktasıdır. Geniş havuz alanı ve plaj erişimiyle tatilcilere konforlu bir ortam sunar.",
            "en": "A seafront accommodation and relaxation spot designed especially for families. It offers a comfortable environment for vacationers with its large pool area and beach access."
        },
        "ChIJSQqN3GlxvhQRvBpAaSr4tEo": { # Yalıpark Beach Hotel
            "tr": "Yalıkavak ve Gündoğan arasında yer alan bu mekan, modern tasarımı ve tertemiz deniziyle dikkat çeker. Sakin bir ortamda güneşlenmek ve kaliteli servis almak isteyenlerin tercihidir.",
            "en": "Located between Yalıkavak and Gündoğan, this venue stands out with its modern design and pristine sea. It's preferred by those who want to sunbathe in a quiet environment and receive quality service."
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
