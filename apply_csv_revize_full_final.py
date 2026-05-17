import json
import os

all_updates = {
    "Bari": {
        "Palazzo Jannuzzi | Dimora Storica | Eventi | Bari": {"description": "Bari'nin kalbinde yer alan bu tarihi malikane, kentin aristokratik geçmişini ve mimari ihtişamını yansıtan bir mücevherdir. Şık davetlere ev sahipliği yapan ve kentsel zarafetin sembolü olan bu yapı, kentin en prestijli tarihi duraklarından biridir.", "description_en": "Located in the heart of Bari, this historical mansion is a jewel reflecting the city's aristocratic past and architectural grandeur. Hosting elegant events and being a symbol of urban elegance, it's one of the city's most prestigious historical stops.", "tips": "Özel etkinlikler dışında dış cephesindeki işçilikleri inceleyin; kentin en fotojenik tarihi binalarından biridir.", "tips_en": "Examine the craftsmanship on its exterior outside of private events; it's one of the city's most photogenic historical buildings.", "category": "Tarihi"},
        "Associazione Culturale Fillide": {"description": "Bari'nin sanatsal ruhunu besleyen Fillide Kültür Derneği, kentin yerel sanatçılarını ve yaratıcı projelerini bir araya getiren bağımsız bir sanat merkezidir. Sergiler ve workshoplarla kentin entelektüel dokusuna katkı sağlayan samimi bir duraktır.", "description_en": "Nurturing Bari's artistic soul, the Fillide Cultural Association is an independent art center bringing together local artists and creative projects. It's a sincere stop contributing to the city's intellectual fabric with exhibitions and workshops.", "tips": "Ziyaret etmeden önce o haftaki sergi veya etkinlik programını kontrol edin; kentin alternatif sanat sahnesini keşfetmek için idealdir.", "tips_en": "Check the exhibition or event schedule for that week before visiting; it's ideal for discovering the city's alternative art scene.", "category": "Kültür"},
        "Vecchio tracciato ferroviario Bari-Taranto": {"description": "Bari ile Taranto arasındaki bu eski demiryolu güzergahı, kentin endüstriyel tarihine tanıklık eden ve şimdi doğa yürüyüşleri için kullanılan nostaljik bir rotadır. Kentin geçmişine dair izler barındıran bu yol, sessiz ve huzurlu bir keşif imkanı sunar.", "description_en": "This old railway route between Bari and Taranto is a nostalgic route witnessing the city's industrial history and now used for nature walks. Containing traces of the city's past, this road offers a quiet and peaceful exploration opportunity.", "tips": "Yürüyüş veya bisiklet için uygundur; yol boyunca Puglia'nın karakteristik zeytinliklerini ve eski istasyon yapılarını görebilirsiniz.", "tips_en": "Suitable for walking or cycling; along the way, you can see Puglia's characteristic olive groves and old station structures.", "category": "Doğa"}
    },
    "Budva": {
        "Caffe Kadmo": {"description": "Budva'nın neşeli ve samimi atmosferini yansıtan Caffe Kadmo, kentin en sevilen mahalle kafelerinden biridir. Geleneksel Karadağ kahvesi ve kentin yerel halkıyla iç içe olabileceğiniz sıcak ortamıyla kentsel yaşamın kalbindedir.", "description_en": "Reflecting Budva's cheerful and sincere atmosphere, Caffe Kadmo is one of the city's most beloved neighborhood cafes. It's at the heart of urban life with its traditional Montenegrin coffee and warm environment where you can mingle with the locals.", "tips": "Sabah saatlerinde yerel halkın gazete okuduğu masalarda oturup kentin ritmini hissedin; ev yapımı tatlıları mutlaka deneyin.", "tips_en": "Sit at the tables where locals read newspapers in the morning and feel the city's rhythm; be sure to try their homemade sweets.", "category": "Sosyal"},
        "Lucky Karaoke": {"description": "Budva'nın gece hayatına eğlenceli bir soluk getiren Lucky Karaoke, kentin en popüler interaktif eğlence duraklarından biridir. Geniş şarkı listesi ve enerjik atmosferiyle kentsel sosyal yaşamın en neşeli noktalarından biridir.", "description_en": "Bringing a fun breath to Budva's nightlife, Lucky Karaoke is one of the city's most popular interactive entertainment stops. With its wide song list and energetic atmosphere, it's one of the most cheerful points of urban social life.", "tips": "Hafta sonları oldukça kalabalık olabilir, erken gitmekte fayda var; kentin en enerjik karaoke performanslarını burada izleyebilirsiniz.", "tips_en": "It can be quite crowded on weekends, better to go early; you can watch the city's most energetic karaoke performances here.", "category": "Sosyal"},
        "Piramida": {"description": "Budva'nın modern ve şık alışveriş duraklarından biri olan Piramida, yerel markaları ve kentsel tasarım ürünlerini bir araya getiren bir merkezdir. Kentin moda dünyasına ve yerel zanaatlarına ışık tutan butikleriyle keşfedilmeye değerdir.", "description_en": "One of Budva's modern and stylish shopping stops, Piramida is a center bringing together local brands and urban design products. It's worth discovering with its boutiques shedding light on the city's fashion world and local crafts.", "tips": "Yerel tasarımcıların takı ve aksesuar koleksiyonlarına mutlaka bakın; hediye alışverişi için kentin en özgün noktalarından biridir.", "tips_en": "Be sure to check out the jewelry and accessory collections of local designers; it's one of the city's most unique spots for gift shopping.", "category": "Alışveriş"}
    }
}

def apply_updates(city_file, city_updates):
    if not os.path.exists(city_file): return
    with open(city_file, 'r') as f:
        data = json.load(f)
    
    changed = False
    highlights = data if isinstance(data, list) else data.get('highlights', [])
        
    for h in highlights:
        name = h.get('name')
        if name in city_updates:
            upd = city_updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
            
    if changed:
        with open(city_file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Updated {city_file}")

# Apply updates
apply_updates('assets/cities/bari.json', all_updates['Bari'])
apply_updates('assets/cities/budva.json', all_updates['Budva'])
