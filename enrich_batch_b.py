import json
import os

def enrich_batch_b():
    # --- PALERMO ---
    p_path = "assets/cities/palermo.json"
    if os.path.exists(p_path):
        with open(p_path, "r", encoding="utf-8") as f:
            p_data = json.load(f)
        
        p_enrich = {
            "ChIJySXqmGHvGRMRancw-ZBf2ow": {
                "tr": "Palermo Katedrali, Mağrip, Gotik ve Barok mimarinin eşsiz bir karışımıdır. 12. yüzyıldan beri şehrin kalbinde yükselen bu yapı, kraliyet kriptaları ve çatı katından sunduğu panoramik şehir manzarasıyla büyüleyicidir.",
                "en": "Palermo Cathedral is a unique blend of Moorish, Gothic, and Baroque architecture. Rising in the heart of the city since the 12th century, it is famous for its royal tombs and breathtaking panoramic views from its rooftop terraces."
            },
            "ChIJSc5EgvXlGRMRLUA6cDzA7I4": {
                "tr": "İtalya'nın en büyük, Avrupa'nın ise üçüncü büyük opera binası olan Teatro Massimo, Palermo'nun sanat ve ihtişam merkezidir. Akustik kalitesi ve 'The Godfather' sahneleriyle dünya çapında bir üne sahiptir.",
                "en": "The largest opera house in Italy and the third-largest in Europe, Teatro Massimo is Palermo's center for art and grandeur. It is world-renowned for its perfect acoustics and its appearance in 'The Godfather III' iconic finale."
            },
            "ChIJmcmp1orlGRMRoPpbuqeU7yI": {
                "tr": "Palermo'nun tarihi merkezinin tam kalbinde yer alan Quattro Canti, Barok tarzındaki dört görkemli cephesiyle kentin simgesidir. 'Güneşin Tiyatrosu' olarak da anılan bu meydan, şehrin antik ana caddelerinin kesişim noktasıdır.",
                "en": "Located at the heart of Palermo's historic center, Quattro Canti is an iconic Baroque square featuring four ornate facades. Also known as the 'Theater of the Sun,' it marks the intersection of the city's ancient main streets."
            }
        }
        
        for h in p_data["highlights"]:
            if h["id"] in p_enrich:
                h["description"] = p_enrich[h["id"]]["tr"]
                h["description_en"] = p_enrich[h["id"]]["en"]
        
        with open(p_path, "w", encoding="utf-8") as f:
            json.dump(p_data, f, ensure_ascii=False, indent=2)

    # --- CATANIA ---
    c_path = "assets/cities/catania.json"
    if os.path.exists(c_path):
        with open(c_path, "r", encoding="utf-8") as f:
            c_data = json.load(f)
            
        c_enrich = {
            "ChIJQ35Z_S7jExMRuOKCpFq-5XM": {
                "tr": "Catania'nın kalbi Piazza del Duomo, kentin simgesi olan siyah lav taşından yapılmış Fil Çeşmesi'ne ev sahipliği yapar. UNESCO mirası olan bu Barok meydan, görkemli katedralleri ve canlı atmosferiyle kentin merkezidir.",
                "en": "The heart of Catania, Piazza del Duomo, houses the iconic Elephant Fountain carved from black volcanic rock. This UNESCO World Heritage Baroque square is the city's hub, surrounded by grand cathedrals and a vibrant street life."
            },
            "ChIJ66CnFDeqFhMRcCrFpSoECx0": {
                "tr": "Avrupa'nın en yüksek ve en aktif yanardağı olan Etna, Catania'nın silüetine hakimdir. Ay yüzeyini andıran manzaraları, kraterleri ve lav akıntıları arasında yapılan yürüyüş turları, Sicilya'nın en efsanevi doğa deneyimidir.",
                "en": "Europe's highest and most active volcano, Mt. Etna, dominates Catania's skyline. Hiking tours among its craters, ancient lava flows, and lunar-like landscapes offer Sicily's most legendary and awe-inspiring natural experience."
            }
        }
        
        for h in c_data["highlights"]:
            if h["id"] in c_enrich:
                h["description"] = c_enrich[h["id"]]["tr"]
                h["description_en"] = c_enrich[h["id"]]["en"]
        
        with open(c_path, "w", encoding="utf-8") as f:
            json.dump(c_data, f, ensure_ascii=False, indent=2)

    # --- BARI ---
    b_path = "assets/cities/bari.json"
    if os.path.exists(b_path):
        with open(b_path, "r", encoding="utf-8") as f:
            b_data = json.load(f)
            
        b_enrich = {
            "ChIJAQV0ZWPoRxMRpltjt0sPOHs": {
                "tr": "Bari'nin koruyucu azizi Aziz Nikolaos'un kemiklerine ev sahipliği yapan bu bazilika, Hristiyan dünyası için önemli bir hac merkezidir. Romanesk mimarinin zirvesi olan yapı, şehrin 'Bari Vecchia' olarak bilinen tarihi dar sokaklarında yer alır.",
                "en": "Housing the relics of Saint Nicholas, the city's patron saint, this basilica is a major pilgrimage site for both Catholics and Orthodox Christians. It is a masterpiece of Romanesque architecture in the heart of old Bari Vecchia."
            },
            "ChIJSwdpfGPoRxMRMXWEJG8CwI4": {
                "tr": "Bari'nin antik kalbi olan Bari Vecchia, taze makarna yapan kadınları, daracık sokakları ve tarihi kiliseleriyle gerçek bir İtalyan deneyimi sunar. 'Orecchiette' caddesinde yürürken yerel halkın geleneklerini yakından görebilirsiniz.",
                "en": "The ancient heart of the city, Bari Vecchia, offers an authentic Italian experience with its narrow alleys, historic churches, and local women making fresh pasta. Walking down 'Orecchiette Street' reveals the town's living traditions."
            }
        }
        
        for h in b_data["highlights"]:
            if h["id"] in b_enrich:
                h["description"] = b_enrich[h["id"]]["tr"]
                h["description_en"] = b_enrich[h["id"]]["en"]
        
        with open(b_path, "w", encoding="utf-8") as f:
            json.dump(b_data, f, ensure_ascii=False, indent=2)

    # --- SARDINYA ---
    s_path = "assets/cities/sardinya.json"
    if os.path.exists(s_path):
        with open(s_path, "r", encoding="utf-8") as f:
            s_data = json.load(f)
            
        s_enrich = {
            "ChIJMWQQfbpA2RIR8TAyoPtICsc": {
                "tr": "Costa Smeralda'nın parlayan yıldızı Porto Cervo, dünyanın en lüks yat limanlarından ve tatil köylerinden biridir. Aga Khan tarafından yaratılan bu sahil köyü, sofistike mimarisi, lüks butikleri ve cemiyet hayatıyla ünlüdür.",
                "en": "The crown jewel of Costa Smeralda, Porto Cervo is one of the world's most luxurious marinas and resort villages. Created by the Aga Khan, it is famous for its sophisticated architecture, high-end boutiques, and elite jet-set society."
            },
            "ChIJ32oIu1da3hIR2FGlOthxLvg": {
                "tr": "Sadece tekneyle veya zorlu bir yürüyüşle ulaşılabilen Cala Goloritzé, beyaz mermer çakılları ve turkuaz sularıyla Sardinya'nın en dokunulmamış koyudur. 143 metrelik kireçtaşı kulesi ile kaya tırmanışçıları ve doğa tutkunları için bir cennetten farksızdır.",
                "en": "Accessible only by boat or a hike, Cala Goloritzé is Sardinia's most pristine cove with white marble pebbles and turquoise waters. Featuring a 143-meter limestone spire, it is a paradise for rock climbers and nature lovers alike."
            }
        }
        
        for h in s_data["highlights"]:
            if h["id"] in s_enrich:
                h["description"] = s_enrich[h["id"]]["tr"]
                h["description_en"] = s_enrich[h["id"]]["en"]
        
        with open(s_path, "w", encoding="utf-8") as f:
            json.dump(s_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_batch_b()
