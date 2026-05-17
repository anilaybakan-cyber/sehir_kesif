import json
import os

routes_data = {
    "bodrum": [
        {
            "id": "bodrum_tarih",
            "title": "Bodrum Tarih & Kale",
            "title_en": "Bodrum History & Castle",
            "description": "Şehrin kalbinde tarihe yolculuk.",
            "description_en": "A journey through history in the heart of the city.",
            "places": ["ChIJYw5gNEJsvhQRcRzUhvXx1Cs", "ChIJlwmXEkdsvhQR0fktlJphpF4", "ChIJv9W_9UdsvhQR2r-WmkBy9K4"]
        },
        {
            "id": "bodrum_marina_sunset",
            "title": "Marina & Gün Batımı",
            "title_en": "Marina & Sunset",
            "description": "Yalıkavak'ın lüks dokusu ve Gümüşlük'te gün batımı.",
            "description_en": "Luxury of Yalıkavak and sunset at Gümüşlük.",
            "places": ["ChIJ_759OOxxvhQRXZc1KZwApPw", "ChIJudEDCxVxvhQRyeydNG7I_m0", "ChIJ47Rqu_p0vhQRei2H38xNHuI"]
        }
    ],
    "mykonos": [
        {
            "id": "mykonos_highlights",
            "title": "Mikonos Klasikleri",
            "title_en": "Mykonos Classics",
            "description": "Yel değirmenleri ve Venedik esintileri.",
            "description_en": "Windmills and Venetian vibes.",
            "places": ["ChIJBye6dBW_ohQRjkT0ucLhnpc", "ChIJTXh2Pqm_ohQRtAPRZ-6TJ7I", "ChIJGe2LNKm_ohQR2y7UkVt7ekU"]
        },
        {
            "id": "mykonos_beach_party",
            "title": "Plaj & Eğlence",
            "title_en": "Beach & Party",
            "description": "Dünya çapında ünlü plaj kulüpleri.",
            "description_en": "World-famous beach clubs.",
            "places": ["ChIJmTndipW-ohQRU8nVD4FLx5c", "ChIJoZaDiIy-ohQRXtKtiak6Frs", "ChIJOXBwpJC-ohQRcW7o3YddSes"]
        }
    ],
    "dubrovnik": [
        {
            "id": "dubrovnik_walls",
            "title": "Surlar & Tarih",
            "title_en": "Walls & History",
            "description": "Adriyatik'in en ikonik manzaraları.",
            "description_en": "Iconic views of the Adriatic.",
            "places": ["ChIJV0zVnDILTBMRkekZb2h93ZY", "ChIJKU9Y8jILTBMR9V8NPzgOYKA", "ChIJQUK5_ywLTBMRBQIbxzDZ1T8"]
        },
        {
            "id": "dubrovnik_sea_view",
            "title": "Ada & Deniz Keyfi",
            "title_en": "Island & Sea Experience",
            "description": "Lokrum adası ve gizli mağara barları.",
            "description_en": "Lokrum island and hidden cave bars.",
            "places": ["ChIJC-2yT0cLTBMRLnDU_jziTis", "ChIJlczNgQQLTBMRabepoBhtYcA", "ChIJ63UJLUl1TBMRh4bDvuxByUQ"]
        }
    ],
    "cesme": [
        {
            "id": "cesme_alacati",
            "title": "Alaçatı Sokakları",
            "title_en": "Alacati Streets",
            "description": "Taş evler ve butik çarşı turu.",
            "description_en": "Stone houses and boutique bazaar tour.",
            "places": ["ChIJDz_6BuB4uxQR9iUno_n11tw", "ChIJJfjSQuB4uxQRZmr4XczsWXo", "ChIJCRS37Mp7uxQRPRiXrVHW7TA"]
        },
        {
            "id": "cesme_beach_life",
            "title": "Masmavi Plajlar",
            "title_en": "Turquoise Beaches",
            "description": "Alaçatı'nın ve Ayayorgi'nin en iyi plajları.",
            "description_en": "Best beaches of Alacati and Ayayorgi.",
            "places": ["ChIJbzHexKd5uxQRvvNz-lA85DE", "ChIJq-xipT16uxQRT8Xn-Hkeqpk", "ChIJO2S1fD16uxQR9cAnEovp1yk"]
        }
    ],
    "amalfi": [
        {
            "id": "amalfi_coastal_pearls",
            "title": "Kıyı İncileri",
            "title_en": "Coastal Pearls",
            "description": "Amalfi ve Positano'nun masalsı dokusu.",
            "description_en": "Fairytale texture of Amalfi and Positano.",
            "places": ["ChIJy2_bsYSVOxMR0Ugr2ptyZuo", "ChIJ-1a02a2VOxMRfwUCyL8wxEw", "ChIJJbN_PpiXOxMR54BkeDpk_Ps"]
        },
        {
            "id": "amalfi_panoramic_ravello",
            "title": "Panoramik Ravello",
            "title_en": "Panoramic Ravello",
            "description": "Villa bahçelerinden sonsuz deniz manzarası.",
            "description_en": "Infinite sea views from villa gardens.",
            "places": ["ChIJKx2evqCVOxMRx5wEJfjT_hw", "ChIJb8673Z-VOxMR3IhhgAAESjk", "ChIJqdTnAOSVOxMRY-xwBm8ZlIk"]
        }
    ]
}

def update_city_json(city_id, routes):
    path = f"assets/cities/{city_id}.json"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return
        
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    data["curated_routes"] = routes
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {city_id}.json with {len(routes)} routes.")

if __name__ == "__main__":
    for city_id, routes in routes_data.items():
        update_city_json(city_id, routes)
