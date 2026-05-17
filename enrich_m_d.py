import json
import os

def enrich_mikonos_dubrovnik():
    # --- MYKONOS ---
    m_path = "assets/cities/mykonos.json"
    if os.path.exists(m_path):
        with open(m_path, "r", encoding="utf-8") as f:
            m_data = json.load(f)
        
        m_enrich = {
            "ChIJTXh2Pqm_ohQRtAPRZ-6TJ7I": {
                "tr": "18. yüzyıldan kalma balkonlu evlerin denizin hemen üzerine kurulduğu Little Venice, Mikonos'un en ikonik gün batımı noktasıdır. Eskiden korsanların ganimetlerini sakladığı bu bölge, şimdilerde şık kokteyl barlarıyla ünlüdür.",
                "en": "Little Venice is Mykonos' most iconic sunset spot, where 18th-century houses with hanging balconies are built right over the sea. Once a hideout for pirate loot, it is now famous for its chic cocktail bars and romantic views."
            },
            "ChIJBye6dBW_ohQRjkT0ucLhnpc": {
                "tr": "Ada silüetinin en tanınmış simgeleri olan tarihi yel değirmenleri, Chora tepesinde gururla yükselir. Venedikliler tarafından inşa edilen bu yedi değirmen, Ege'nin sert rüzgarlarını kullanarak asırlarca un üretimi sağlamıştır.",
                "en": "The iconic Windmills of Mykonos stand proudly on a hill overlooking Chora. Originally built by the Venetians in the 16th century to grind grain, they remain the island's most photographed landmark and a symbol of its heritage."
            },
            "ChIJGe2LNKm_ohQR2y7UkVt7ekU": {
                "tr": "Bembeyaz mimarisiyle Mykonos'un en eski ve en fotojenik kilisesi olan Panagia Paraportiani, aslında birbirine bitişik beş ayrı küçük kiliseden oluşur. Mimari formu, yüzyıllar süren doğal aşınma ve eklemelerle bugünkü eşsiz halini almıştır.",
                "en": "The stunning white-washed Panagia Paraportiani is Mykonos' oldest and most unique church. Composed of five separate small chapels built on top of or next to each other, its organic shape has been perfected by centuries of wind and sea salt."
            },
            "ChIJ36vmITuWohQRC8DNvi8Urb0": {
                "tr": "Antik Yunan dünyasının en kutsal adası sayılan Delos, Mykonos'tan kısa bir tekne yolculuğu mesafesindedir. UNESCO mirası olan bu açık hava müzesinde, Apollon ve Artemis'in doğduğu topraklardaki devasa tapınak kalıntılarını görebilirsiniz.",
                "en": "Regarded as the most sacred island of Ancient Greece, Delos is a short boat trip from Mykonos. This UNESCO World Heritage open-air museum features monumental temple ruins where Apollo and Artemis were famously born."
            },
            "ChIJOXBwpJC-ohQRcW7o3YddSes": {
                "tr": "Paraga Koyu'nda yer alan Scorpios, sadece bir plaj kulübü değil, modern bir 'pazar yeri' ve ritüel alanıdır. Bohem-lüks tasarımı, dünya çapındaki DJ'leri ve gün batımı seremonileriyle adanın en prestijli eğlence noktasıdır.",
                "en": "Located on Paraga Beach, Scorpios is more than a beach club; it is a holistic 'agora' and social ritual site. Its bohemian-luxury design, world-class DJs, and sunset rituals make it the most prestigious hangout on the island."
            }
        }
        
        for h in m_data["highlights"]:
            if h["id"] in m_enrich:
                h["description"] = m_enrich[h["id"]]["tr"]
                h["description_en"] = m_enrich[h["id"]]["en"]
        
        with open(m_path, "w", encoding="utf-8") as f:
            json.dump(m_data, f, ensure_ascii=False, indent=2)

    # --- DUBROVNIK ---
    d_path = "assets/cities/dubrovnik.json"
    if os.path.exists(d_path):
        with open(d_path, "r", encoding="utf-8") as f:
            d_data = json.load(f)
            
        d_enrich = {
            "ChIJV0zVnDILTBMRkekZb2h93ZY": {
                "tr": "Dubrovnik'i çevreleyen ve 2 kilometre boyunca uzanan bu devasa surlar, Orta Çağ savunma mimarisinin başyapıtıdır. Surların üzerinde yürürken hem Adriyatik'in masmavi sonsuzluğunu hem de şehrin ikonik turuncu çatılarını izleyebilirsiniz.",
                "en": "Stretching for nearly 2 kilometers, the Dubrovnik City Walls are a masterpiece of medieval defense architecture. Walking atop them offers breathtaking views of the blue Adriatic and the city's iconic terracotta rooftops."
            },
            "ChIJKU9Y8jILTBMR9V8NPzgOYKA": {
                "tr": "Eski Şehrin ana damarı olan Stradun, kireçtaşıyla döşeli parıl parıl parlayan bir yaya yoludur. Mağazalar, kafeler ve tarihi binalarla çevrili bu cadde, şehrin nabzının attığı en canlı ve görkemli noktadır.",
                "en": "The main artery of the Old Town, Stradun is a gleaming limestone-paved pedestrian street. Lined with historic buildings, shops, and cafes, it is the vibrant heart of Dubrovnik where history meets modern life."
            },
            "ChIJQUK5_ywLTBMRBQIbxzDZ1T8": {
                "tr": "Denizden 37 metre yükseklikteki sarp kayalıkların üzerine kurulu Lovrjenac Kalesi, Dubrovnik'in 'Cebelitarık'ı olarak bilinir. Şehri denizden gelen saldırılara karşı korumak için inşa edilen bu hisar, Game of Thrones sahnelerine de ev sahipliği yapmıştır.",
                "en": "Perched on a 37-meter high cliff, Lovrjenac Fortress is often called Dubrovnik's 'Gibraltar.' Built to defend the city from sea invasions, it is now an iconic cultural site and a famous filming location for Game of Thrones."
            },
            "ChIJs4R9FjILTBMRMnlEynjHdms": {
                "tr": "Surların dış tarafındaki kayalıklara asılmış olan Buža Bar, şehrin en gizli ve romantik duraklarından biridir. Adriyatik'e karşı bir şeyler yudumlarken, surların üzerinden denize atlayanları izleyebileceğiniz eşsiz bir atmosfer sunar.",
                "en": "Clinging to the rocks outside the city walls, Buža Bar is one of Dubrovnik's most unique and romantic spots. It offers a front-row seat to the Adriatic sunset and the daring divers leaping from the cliffs."
            }
        }
        
        for h in d_data["highlights"]:
            if h["id"] in d_enrich:
                h["description"] = h["description"] if len(h.get("description", "")) > 100 else d_enrich[h["id"]]["tr"]
                h["description"] = d_enrich[h["id"]]["tr"]
                h["description_en"] = d_enrich[h["id"]]["en"]
        
        with open(d_path, "w", encoding="utf-8") as f:
            json.dump(d_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_mikonos_dubrovnik()
