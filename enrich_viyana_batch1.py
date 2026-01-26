import json
import os

# Viyana Zenginleştirme - Batch 1: Kafeler ve Restoranlar
new_viyana_batch1 = [
    {
        "name": "Café Central",
        "name_en": "Café Central",
        "area": "Innere Stadt",
        "category": "Kafe",
        "tags": ["tarihi", "kahve", "pasta", "klasik"],
        "distanceFromCenter": 0.3,
        "lat": 48.2109,
        "lng": 16.3653,
        "price": "medium",
        "rating": 4.7,
        "description": "1876'dan beri hizmet veren, Freud ve Troçki'nin de uğrak noktası olan efsanevi Viyana kahve evi.",
        "description_en": "Legendary Viennese coffee house serving since 1876, frequented by Freud and Trotsky.",
        "imageUrl": "https://images.unsplash.com/photo-1559925393-8be0ec4767c8?w=800",
        "bestTime": "Sabah veya öğleden sonra",
        "bestTime_en": "Morning or afternoon",
        "tips": "Sachertorte ve Melange kahve kombinasyonunu deneyin. Hafta sonları çok kalabalık olabilir.",
        "tips_en": "Try the Sachertorte and Melange coffee combo. Can be very crowded on weekends."
    },
    {
        "name": "Café Sacher",
        "name_en": "Café Sacher",
        "area": "Innere Stadt",
        "category": "Kafe",
        "tags": ["orijinal", "sachertorte", "lüks", "tarihi"],
        "distanceFromCenter": 0.2,
        "lat": 48.2037,
        "lng": 16.3691,
        "price": "high",
        "rating": 4.6,
        "description": "Orijinal Sachertorte'nin doğduğu yer. 1832'den beri çikolata severler için vazgeçilmez adres.",
        "description_en": "Birthplace of the original Sachertorte. A must-visit for chocolate lovers since 1832.",
        "imageUrl": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
        "bestTime": "14:00-16:00",
        "bestTime_en": "2-4 PM",
        "tips": "Taze Sachertorte'yi kremalı olarak sipariş edin. Eve götürmek için orijinal kutulu pasta alabilirsiniz.",
        "tips_en": "Order fresh Sachertorte with cream. You can buy original boxed cake to take home."
    },
    {
        "name": "Demel",
        "name_en": "Demel",
        "area": "Innere Stadt",
        "category": "Kafe",
        "tags": ["kraliyet", "pasta", "tarihi", "tatlı"],
        "distanceFromCenter": 0.3,
        "lat": 48.2087,
        "lng": 16.3672,
        "price": "high",
        "rating": 4.7,
        "description": "Habsburg sarayının resmi şekerlemecisi. Kaiserschmarrn ve el yapımı pralinleriyle ünlü.",
        "description_en": "Official confectioner of the Habsburg court. Famous for Kaiserschmarrn and handmade pralines.",
        "imageUrl": "https://images.unsplash.com/photo-1509365465985-25d11c17e812?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Açık mutfağı izleyerek şeflerin çalışmasını görebilirsiniz.",
        "tips_en": "Watch the chefs work through the open kitchen."
    },
    {
        "name": "Café Landtmann",
        "name_en": "Café Landtmann",
        "area": "Innere Stadt",
        "category": "Kafe",
        "tags": ["tarihi", "politikacılar", "teras", "elite"],
        "distanceFromCenter": 0.5,
        "lat": 48.2109,
        "lng": 16.3596,
        "price": "high",
        "rating": 4.6,
        "description": "1873'ten beri politikacıların ve akademisyenlerin buluşma noktası. Burgtheater manzaralı teras.",
        "description_en": "Meeting point for politicians and academics since 1873. Terrace with Burgtheater views.",
        "imageUrl": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?w=800",
        "bestTime": "Öğle yemeği",
        "bestTime_en": "Lunch",
        "tips": "Terasta oturup Ringstrasse manzarasının keyfini çıkarın.",
        "tips_en": "Sit on the terrace and enjoy the views of Ringstrasse."
    },
    {
        "name": "Café Sperl",
        "name_en": "Café Sperl",
        "area": "Mariahilf",
        "category": "Kafe",
        "tags": ["otantik", "lokal", "bilardo", "sanatçılar"],
        "distanceFromCenter": 1.2,
        "lat": 48.1990,
        "lng": 16.3534,
        "price": "medium",
        "rating": 4.7,
        "description": "1880'den beri değişmeyen atmosferiyle Viyana'nın en otantik kahve evi. Bilardo masaları ve gazeteler.",
        "description_en": "Vienna's most authentic coffee house with unchanged atmosphere since 1880. Billiard tables and newspapers.",
        "imageUrl": "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800",
        "bestTime": "Pazar kahvaltısı",
        "bestTime_en": "Sunday breakfast",
        "tips": "Pazar günleri erkenen gelin ve bol lokanta seçeneği olan Viyana kahvaltısının tadını çıkarın.",
        "tips_en": "Come early on Sundays and enjoy the Viennese breakfast."
    },
    {
        "name": "Figlmüller",
        "name_en": "Figlmüller",
        "area": "Innere Stadt",
        "category": "Restoran",
        "tags": ["schnitzel", "geleneksel", "efsanevi", "büyük porsiyon"],
        "distanceFromCenter": 0.2,
        "lat": 48.2083,
        "lng": 16.3747,
        "price": "medium",
        "rating": 4.5,
        "description": "Tabaktan taşan dev schnitzelleriyle ünlü, 1905'ten beri hizmet veren efsane mekan.",
        "description_en": "Legendary since 1905, famous for giant schnitzels larger than the plate.",
        "imageUrl": "https://images.unsplash.com/photo-1599921841143-819065a55cc6?w=800",
        "bestTime": "12:00-14:00",
        "bestTime_en": "12-2 PM",
        "tips": "Mutlaka rezervasyon yapın. Patates salatası ile schnitzel kombinasyonu klasik.",
        "tips_en": "Make a reservation. Schnitzel with potato salad is the classic combo."
    },
    {
        "name": "Plachutta",
        "name_en": "Plachutta",
        "area": "Innere Stadt",
        "category": "Restoran",
        "tags": ["tafelspitz", "geleneksel", "özel", "lüks"],
        "distanceFromCenter": 0.4,
        "lat": 48.2072,
        "lng": 16.3807,
        "price": "high",
        "rating": 4.6,
        "description": "Viyana'nın en iyi Tafelspitz'ini (haşlanmış dana) sunan prestijli restoran.",
        "description_en": "Prestigious restaurant serving Vienna's best Tafelspitz (boiled beef).",
        "imageUrl": "https://images.unsplash.com/photo-1544025162-d76978e8db6e?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Tafelspitz'i geleneksel yöntemle, önce çorbayı sonra eti yiyin.",
        "tips_en": "Eat Tafelspitz traditionally - first the broth, then the meat."
    },
    {
        "name": "Gmoa Keller",
        "name_en": "Gmoa Keller",
        "area": "Innere Stadt",
        "category": "Restoran",
        "tags": ["bodrum", "geleneksel", "şarap", "lokal"],
        "distanceFromCenter": 0.3,
        "lat": 48.2048,
        "lng": 16.3761,
        "price": "medium",
        "rating": 4.5,
        "description": "Tarihi bodrum katta yer alan, Wiener Schnitzel ve mevsimsel yemekleriyle ünlü geleneksel restoran.",
        "description_en": "Traditional restaurant in a historic cellar, famous for Wiener Schnitzel and seasonal dishes.",
        "imageUrl": "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800",
        "bestTime": "Akşam",
        "bestTime_en": "Evening",
        "tips": "Şarap listesinden Avusturya şaraplarını deneyin.",
        "tips_en": "Try Austrian wines from their wine list."
    },
    {
        "name": "Neni am Naschmarkt",
        "name_en": "Neni am Naschmarkt",
        "area": "Naschmarkt",
        "category": "Restoran",
        "tags": ["orta doğu", "modern", "brunch", "trendy"],
        "distanceFromCenter": 0.8,
        "lat": 48.1988,
        "lng": 16.3621,
        "price": "medium",
        "rating": 4.6,
        "description": "Tel Aviv tarzı Orta Doğu mutfağı sunan trendy mekan. Naschmarkt'ın kalbinde.",
        "description_en": "Trendy spot serving Tel Aviv-style Middle Eastern cuisine. In the heart of Naschmarkt.",
        "imageUrl": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?w=800",
        "bestTime": "Brunch (hafta sonu)",
        "bestTime_en": "Brunch (weekend)",
        "tips": "Shakshuka kahvaltısı muhteşem. Mezeler paylaşmak için ideal.",
        "tips_en": "Shakshuka breakfast is amazing. Mezze are perfect for sharing."
    },
    {
        "name": "Mochi",
        "name_en": "Mochi",
        "area": "Innere Stadt",
        "category": "Restoran",
        "tags": ["japon", "sushi", "fusion", "modern"],
        "distanceFromCenter": 0.5,
        "lat": 48.2015,
        "lng": 16.3528,
        "price": "high",
        "rating": 4.7,
        "description": "Viyana'nın en sevilen Japon fusion restoranı. Sushi ve sashimi konusunda uzman.",
        "description_en": "Vienna's most beloved Japanese fusion restaurant. Expert in sushi and sashimi.",
        "imageUrl": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=800",
        "bestTime": "Akşam yemeği",
        "bestTime_en": "Dinner",
        "tips": "Omakase menüsünü deneyin. Rezervasyon şart.",
        "tips_en": "Try the omakase menu. Reservation required."
    }
]

def enrich_viyana_batch1():
    filepath = 'assets/cities/viyana.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    added = 0
    for new_h in new_viyana_batch1:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)
            added += 1
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights']), added

count, added = enrich_viyana_batch1()
print(f"Viyana: {count} highlights (added {added} new)")
