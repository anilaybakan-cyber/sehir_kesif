import json
import os

def enrich_batch_c():
    # --- BUDVA ---
    b_path = "assets/cities/budva.json"
    if os.path.exists(b_path):
        with open(b_path, "r", encoding="utf-8") as f:
            b_data = json.load(f)
        
        b_enrich = {
            "ChIJifScjpPUTRMRixAqbrNNr9Q": {
                "tr": "Adriyatik'in en eski yerleşimlerinden biri olan Budva Eski Şehir, labirent gibi sokakları ve tarihi surlarıyla bir açık hava müzesidir. Denizin hemen kıyısında yer alan bu Orta Çağ kasabası, masalsı atmosferiyle Karadağ'ın mücevheridir.",
                "en": "One of the oldest settlements on the Adriatic, Budva Old Town is an open-air museum with its labyrinthine streets and medieval walls. This coastal fortress town offers a fairy-tale atmosphere and is the crown jewel of Montenegro."
            },
            "ChIJucb7_iXUTRMRELZT-vjgG9c": {
                "tr": "Karadağ'ın en ikonik simgesi olan Sveti Stefan, ince bir kum yoluyla karaya bağlı olan tarihi bir ada-köydür. Kırmızı çatılı taş evleri ve lüks atmosferiyle dünyaca ünlü bu yarımada, Adriyatik'in en prestijli noktasıdır.",
                "en": "Montenegro's most iconic landmark, Sveti Stefan, is a historic island-village connected to the mainland by a narrow sand spit. With its red-tiled stone houses and luxury vibe, it is the most prestigious destination on the Adriatic."
            }
        }
        
        for h in b_data["highlights"]:
            if h["id"] in b_enrich:
                h["description"] = b_enrich[h["id"]]["tr"]
                h["description_en"] = b_enrich[h["id"]]["en"]
        
        with open(b_path, "w", encoding="utf-8") as f:
            json.dump(b_data, f, ensure_ascii=False, indent=2)

    # --- KSAMIL ---
    k_path = "assets/cities/ksamil.json"
    if os.path.exists(k_path):
        with open(k_path, "r", encoding="utf-8") as f:
            k_data = json.load(f)
            
        k_enrich = {
            "ChIJk5FPXTNqWxMRUpA0CsHZd6s": {
                "tr": "Arnavutluk Rivierası'nın incisi olan Ksamil Adaları, turkuaz suları ve bembeyaz kumlarıyla Maldivleri andıran bir doğa harikasıdır. Sadece tekne veya kano ile ulaşılabilen bu dört küçük ada, kristal netliğindeki deniziyle büyüleyicidir.",
                "en": "The jewel of the Albanian Riviera, the Ksamil Islands feature turquoise waters and white sands reminiscent of the Maldives. These four small islands, accessible only by boat or kayak, are breathtaking with their crystal-clear sea."
            },
            "ChIJtaO8wQEPWxMRa9Z5FU1XI0s": {
                "tr": "Ksamil yakınlarındaki Mavi Göz (Syri i Kaltër), yerin derinliklerinden kaynayan buz gibi suyu ve inanılmaz derinlikteki mavi rengiyle efsanevi bir doğal su kaynağıdır. Yoğun bitki örtüsü arasındaki bu doğa harikası görülmeye değerdir.",
                "en": "The Blue Eye (Syri i Kaltër) near Ksamil is a legendary natural spring with icy water bubbling from the depths and an incredible deep blue color. This natural wonder amidst lush vegetation is a must-see transformation of nature."
            }
        }
        
        for h in k_data["highlights"]:
            if h["id"] in k_enrich:
                h["description"] = k_enrich[h["id"]]["tr"]
                h["description_en"] = k_enrich[h["id"]]["en"]
        
        with open(k_path, "w", encoding="utf-8") as f:
            json.dump(k_data, f, ensure_ascii=False, indent=2)

    # --- SELANIK ---
    s_path = "assets/cities/selanik.json"
    if os.path.exists(s_path):
        with open(s_path, "r", encoding="utf-8") as f:
            s_data = json.load(f)
            
        s_enrich = {
            "ChIJacxIJa85qBQRFi10gJ0wGO8": {
                "tr": "Selanik'in en tanınmış simgesi olan Beyaz Kule, kentin sahil şeridinde tüm görkemiyle yükselir. Osmanlı döneminden kalan bu tarihi kule, günümüzde şehrin Bizans tarihini anlatan modern bir müze olarak hizmet vermektedir.",
                "en": "The White Tower, the most famous symbol of Thessaloniki, rises majestically on the city's waterfront. A remnant of the Ottoman era, this historic tower now houses a modern museum dedicated to the city's Byzantine history."
            },
            "ChIJ6coVkAg5qBQR4j9wLCNUa84": {
                "tr": "Kentin kalbi olan Aristotelous Meydanı, Neoklasik binaları ve deniz manzarasıyla Selanik'in en popüler buluşma noktasıdır. Fransız mimar Ernest Hébrard tarafından tasarlanan bu görkemli meydan, kentin kozmopolit ruhunu yansıtır.",
                "en": "The heart of the city, Aristotelous Square, is Thessaloniki's most popular meeting point with its Neoclassical buildings and sea views. Designed by French architect Ernest Hébrard, this grand square reflects the city's cosmopolitan soul."
            }
        }
        
        for h in s_data["highlights"]:
            if h["id"] in s_enrich:
                h["description"] = s_enrich[h["id"]]["tr"]
                h["description_en"] = s_enrich[h["id"]]["en"]
        
        with open(s_path, "w", encoding="utf-8") as f:
            json.dump(s_data, f, ensure_ascii=False, indent=2)

    # --- RHODES ---
    r_path = "assets/cities/rhodes.json"
    if os.path.exists(r_path):
        with open(r_path, "r", encoding="utf-8") as f:
            r_data = json.load(f)
            
        r_enrich = {
            "ChIJEWPxPsJhlRQR_bpd3aiKclU": {
                "tr": "Rodos'un UNESCO Dünya Mirası listesindeki Orta Çağ şehri, Avrupa'nın en iyi korunmuş kale-kentlerinden biridir. Şövalye burçları, dar sokakları ve Bizans ile Osmanlı izleriyle tarihin içinde bir yolculuk sunar.",
                "en": "Rhodes' UNESCO World Heritage Medieval City is one of Europe's best-preserved fortified towns. With its Knight's bastions, narrow alleys, and Byzantine-Ottoman influences, it offers a true journey through history."
            },
            "ChIJRV1YO3UOlRQR0KKtXtb1Vos": {
                "tr": "Rodos'un doğu kıyısında bir tepe üzerinde yükselen Lindos Akropolisi, antik tapınakları ve masmavi deniz manzarasıyla büyüleyicidir. Beyaz evleriyle ünlü Lindos köyünün üzerindeki bu antik alan, Ege'nin en muazzam manzaralarından birini sunar.",
                "en": "Rising on a hill on Rhodes' eastern coast, the Lindos Acropolis is breathtaking with its ancient temples and deep blue sea views. This ancient site overlooking the famous white-washed Lindos village offers one of the Aegean's grandest vistas."
            }
        }
        
        for h in r_data["highlights"]:
            if h["id"] in r_enrich:
                h["description"] = r_enrich[h["id"]]["tr"]
                h["description_en"] = r_enrich[h["id"]]["en"]
        
        with open(r_path, "w", encoding="utf-8") as f:
            json.dump(r_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_batch_c()
