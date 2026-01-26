import json
import os

new_milano_final = [
    {
        "name": "Museo del Risorgimento",
        "name_en": "Risorgimento Museum",
        "area": "Brera",
        "category": "Müze",
        "tags": ["tarih", "italya", "birleşme", "saray"],
        "distanceFromCenter": 0.7,
        "lat": 45.4718,
        "lng": 9.1888,
        "price": "medium",
        "rating": 4.4,
        "description": "İtalya'nın birleşme tarihini (Risorgimento) anlatan, Napolyon'dan Garibaldi'ye kadar uzanan önemli bir koleksiyona sahip tarihi saray müzesi.",
        "description_en": "Housed in the 18th-century Palazzo Moriggia, this museum details Italy's unification history with rare artifacts from the era of Napoleon and Garibaldi.",
        "imageUrl": "https://images.unsplash.com/photo-1543083477-4f7f44aad226?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Tarih meraklıları için mutlaka görülmesi gereken, kentin asil ruhunu yansıtan sessiz bir müzedir.",
        "tips_en": "Perfect for history buffs; the building itself is a masterpiece of late 18th-century architecture and usually very peaceful."
    },
    {
        "name": "Giardini Pubblici Indro Montanelli",
        "name_en": "Indro Montanelli Public Gardens",
        "area": "Venezia",
        "category": "Park",
        "tags": ["yeşil", "yürüyüş", "doğa", "merkezi"],
        "distanceFromCenter": 1.1,
        "lat": 45.4745,
        "lng": 9.2002,
        "price": "free",
        "rating": 4.6,
        "description": "Milano'nun tam merkezinde yer alan, göletleri ve asırlık ağaçlarıyla kentin nefes aldığı en büyük tarihi parklardan biri.",
        "description_en": "A historic urban oasis in the city center, featuring beautiful lakes, century-old trees, and plenty of space for a morning stroll or a picnic.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Hafta sonu öğleden sonra",
        "bestTime_en": "Weekend afternoon",
        "tips": "İçindeki gezegen evi (Planetarium) çocuklarla ziyaret etmek için harikadır.",
        "tips_en": "The park also houses the Natural History Museum and the Planetarium; it's the heart of Milanese outdoor family life."
    },
    {
        "name": "Torre Branca",
        "name_en": "Branca Tower",
        "area": "Sempione",
        "category": "Manzara",
        "tags": ["kule", "panoramik", "demir yapı", "tasarım"],
        "distanceFromCenter": 1.6,
        "lat": 45.4735,
        "lng": 9.1725,
        "price": "medium",
        "rating": 4.5,
        "description": "Gio Ponti tarafından tasarlanan, 108 metre yüksekliğindeki bu demir kule kentin en iyi panoramik manzarasını sunar.",
        "description_en": "A 108-meter iron panoramic tower designed by the famous Gio Ponti, offering a 360-degree view that covers the Duomo, Sforza Castle, and the Alps.",
        "imageUrl": "https://images.unsplash.com/photo-1520440229-6469a149ac59?w=800",
        "bestTime": "Gün batımı",
        "bestTime_en": "Sunset",
        "tips": "Asansörle çıkış oldukça hızlıdır, havanın açık olduğu bir günü tercih edin.",
        "tips_en": "Pre-purchase your ticket to save time; on clear days, the entire Alpine chain is visible behind the city's skyline."
    },
    {
        "name": "Via Savona (Tasarım Sokağı)",
        "name_en": "Via Savona Design Street",
        "area": "Tortona",
        "category": "Tarihi",
        "tags": ["tasarım", "moda", "sanat", "showroom"],
        "distanceFromCenter": 3.4,
        "lat": 45.4505,
        "lng": 9.1625,
        "price": "free",
        "rating": 4.6,
        "description": "Eski endüstriyel binaların tasarım stüdyolarına ve moda showroomlarına dönüştüğü, kentin en yaratıcı sokaklarından biri.",
        "description_en": "A legendary street in the Tortona district, where old factories have been reinvented as trendy design lofts, showrooms, and artistic event spaces.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Tasarım Haftası dönemi",
        "bestTime_en": "During Design Week",
        "tips": "Sokak üzerindeki gizli avlulara (cortili) girin, genellikle sürpriz sanat eserleriyle karşılaşabilirsiniz.",
        "tips_en": "Look for the iron gates that are slightly ajar; they often lead to stunning plant-filled industrial courtyards used for private fashion events."
    },
    {
        "name": "Piazza Sant'Eustorgio",
        "name_en": "Piazza Sant'Eustorgio",
        "area": "Ticinese",
        "category": "Tarihi",
        "tags": ["meydan", "kilise", "antik", "huzur"],
        "distanceFromCenter": 1.6,
        "lat": 45.4552,
        "lng": 9.1818,
        "price": "free",
        "rating": 4.7,
        "description": "Navigli'ye giden yol üzerinde, kentin en eski bazilikalarından birine bakan, ağaçlıklı ve çok huzurlu bir meydan.",
        "description_en": "A charming and quiet plaza on the way to the Navigli, home to one of Milan's most ancient basilicas (supposedly holding the relics of the Three Kings).",
        "imageUrl": "https://images.unsplash.com/photo-1515488764276-beab7607c1e6?w=800",
        "bestTime": "Gündüz",
        "bestTime_en": "Daytime",
        "tips": "Meydandaki barlardan birinde oturup Ticinese bölgesinin yerel yaşamını izlemek çok keyiflidir.",
        "tips_en": "Visit the Portinari Chapel inside the basilica for some of the finest Renaissance frescoes in Northern Italy."
    },
    {
        "name": "Fondazione Prada (Bar Luce)",
        "name_en": "Bar Luce by Wes Anderson",
        "area": "Güney Milano",
        "category": "Kafe",
        "tags": ["tasarım", "sinema", "wes anderson", "ikonik"],
        "distanceFromCenter": 3.7,
        "lat": 45.4455,
        "lng": 9.2095,
        "price": "medium",
        "rating": 4.9,
        "description": "Sinema yönetmeni Wes Anderson tarafından tasarlanan, 1950'ler Milano atmosferini yansıtan kentin en fotojenik kafesi.",
        "description_en": "A cinematic cafe within Fondazione Prada designed by filmmaker Wes Anderson, evoking the whimsical atmosphere of a traditional 1950s Milanese bar.",
        "imageUrl": "https://images.unsplash.com/photo-1544333346-bf0375179462?w=800",
        "bestTime": "Öğleden sonra",
        "bestTime_en": "Afternoon",
        "tips": "Özel tasarım langırt masasını mutlaka deneyin ve pastel tonlardaki tatlılardan tadın.",
        "tips_en": "Try the Steve Zissou pinball machine—the decor is a masterpiece of form-ica and retro colors, making it a design pilgrimage site."
    },
    {
        "name": "Via Montenapoleone",
        "name_en": "Via Montenapoleone",
        "area": "Moda Dörtgeni",
        "category": "Alışveriş",
        "tags": ["lüks", "moda", "dünya markaları", "prestij"],
        "distanceFromCenter": 0.5,
        "lat": 45.4682,
        "lng": 9.1945,
        "price": "high",
        "rating": 4.6,
        "description": "Dünyanın en pahalı ve prestijli alışveriş caddelerinden biri. Tüm global lüks markaların amiral gemisi mağazaları burada bulunur.",
        "description_en": "The crown jewel of the Golden Quad and one of the world's most expensive streets, featuring the flagship boutiques of every major global fashion house.",
        "imageUrl": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?w=800",
        "bestTime": "Gündüz / Hafta içi",
        "bestTime_en": "Daytime / Weekdays",
        "tips": "Alışveriş yapmasanız bile buradaki abartılı vitrinleri ve kapı önündeki süper lüks arabaları görmek bir Milano deneyimidir.",
        "tips_en": "A must-walk for fashion lovers to see the latest global trends in window display design; it's the heart of the Italian 'Alta Moda' world."
    },
    {
        "name": "Teatro Dal Verme",
        "name_en": "Dal Verme Theatre",
        "area": "Centro",
        "category": "Tarihi",
        "tags": ["tiyatro", "konser", "mimari", "kültür"],
        "distanceFromCenter": 0.5,
        "lat": 45.4675,
        "lng": 9.1818,
        "price": "medium",
        "rating": 4.5,
        "description": "Milano'nun önemli konser ve etkinlik mekanlarından biri olan tarihi tiyatro binası.",
        "description_en": "An important historic theater and concert venue in Milan, hosting everything from classical symphonies to modern jazz and world festivals.",
        "imageUrl": "https://images.unsplash.com/photo-1518998053574-53f02ca7c98a?w=800",
        "bestTime": "Akşam (konser varken)",
        "bestTime_en": "Evening (during concerts)",
        "tips": "Binanın modern ile klasiği birleştiren mimarisi ve akustiği oldukça başarılıdır.",
        "tips_en": "Check the schedule for the Orchestra Pomeriggi Musicali, their resident orchestra; it's a great way to experience high culture at reasonable prices."
    },
    {
        "name": "Pasticceria Marchesi (Galleria)",
        "name_en": "Marchesi 1824 Galleria",
        "area": "Centro",
        "category": "Kafe",
        "tags": ["pastane", "lüks", "manzara", "gelenek"],
        "distanceFromCenter": 0.1,
        "lat": 45.4658,
        "lng": 9.1895,
        "price": "high",
        "rating": 4.8,
        "description": "Galleria'nın üst katında yer alan, yeşil ipek duvarları ve Galleria manzaralı pencereleriyle kentin en şık pastanesi.",
        "description_en": "Located above the Prada store in the Galleria, this legendary pastry shop features iconic pistachio-green velvet interiors and stunning arcade views.",
        "imageUrl": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?w=800",
        "bestTime": "Sabah",
        "bestTime_en": "Morning",
        "tips": "Pencere önünde yer bulup Galleria'nın kalabalığını yukarıdan izleyerek kahvenizi yudumlayın.",
        "tips_en": "Grab a window seat to enjoy the best people-watching spot in the city while tasting their world-famous cream-filled cannoncini."
    }
]

def enrich_milano_final():
    filepath = 'assets/cities/milano.json'
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    existing_names = set(h['name'].lower() for h in data.get('highlights', []))
    for new_h in new_milano_final:
        if new_h['name'].lower() not in existing_names:
            data['highlights'].append(new_h)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return len(data['highlights'])

count = enrich_milano_final()
print(f"Milan now has {count} highlights.")
