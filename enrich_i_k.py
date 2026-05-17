import json
import os

def enrich_ibiza_kas():
    # --- IBIZA ---
    i_path = "assets/cities/ibiza.json"
    if os.path.exists(i_path):
        with open(i_path, "r", encoding="utf-8") as f:
            i_data = json.load(f)
        
        i_enrich = {
            "ChIJac27E7BGmRIR3ivh3HRaxyQ": {
                "tr": "Ibiza'nın UNESCO koruması altındaki eski şehir bölgesi Dalt Vila, şehri tepeden selamlayan tarihi surları ve Arnavut kaldırımlı sokaklarıyla büyüleyicidir. Katedrali ve panoramik deniz manzarasıyla adanın asırlık tarihine tanıklık eder.",
                "en": "Ibiza's UNESCO-protected Old Town, Dalt Vila, features ancient defensive walls and winding cobblestone streets overlooking the city. Its majestic cathedral and panoramic sea views offer a timeless journey through the island's history."
            },
            "ChIJoUI2LSOznhIR3cAManclxOc": {
                "tr": "Denizden yükselen devasa bir kireç taşı kayası olan Es Vedrà, dünyanın en güçlü manyetik alanlarından biri olarak kabul edilir. Efsanelerle çevrili bu gizemli ada, özellikle gün batımında Ibiza'nın en ruhani ve büyüleyici manzarasını sunar.",
                "en": "Rising dramatically from the sea, Es Vedrà is a massive limestone rock island shrouded in myth and mystery. Said to be one of the most magnetic spots on Earth, it provides Mykonos' most spiritual and breathtaking sunset backdrop."
            },
            "ChIJS5DBd_1JmRIRLnc_uM5Oego": {
                "tr": "Chill-out müziğin doğum yeri olan Café del Mar, San Antonio sahilinde yer alan bir Ibiza efsanesidir. Gün batımını müzik ve kokteyller eşliğinde uğurlama klasiğinin dünyadaki en bilinen adresi olarak kabul edilir.",
                "en": "The birthplace of chill-out music, Café del Mar is an Ibiza legend situated on the San Antonio coast. It is world-renowned as the definitive spot to celebrate the sunset with iconic music and creative cocktails."
            },
            "ChIJBUmiFTVBmRIREVzO4Q3XWvQ": {
                "tr": "1973 yılında kurulan Pacha, Ibiza'nın gece hayatı kültürünü dünyaya yayan en ikonik kulüptür. Kiraz simgesiyle özdeşleşen bu mekan, sofistike tasarımı ve dünya çapındaki DJ'leriyle lüks eğlencenin değişmez adresidir.",
                "en": "Founded in 1973, Pacha is the most iconic club in Ibiza and the global symbol of the island's nightlife. Known for its cherry logo and sophisticated vibe, it remains a playground for the international elite and top-tier DJs."
            }
        }
        
        for h in i_data["highlights"]:
            if h["id"] in i_enrich:
                h["description"] = i_enrich[h["id"]]["tr"]
                h["description_en"] = i_enrich[h["id"]]["en"]
        
        with open(i_path, "w", encoding="utf-8") as f:
            json.dump(i_data, f, ensure_ascii=False, indent=2)

    # --- KAŞ ---
    k_path = "assets/cities/kas.json"
    if os.path.exists(k_path):
        with open(k_path, "r", encoding="utf-8") as f:
            k_data = json.load(f)
            
        k_enrich = {
            "ChIJaQPCYHDTwRQR1cQU17ycULA": {
                "tr": "Kaş ile Kalkan arasında yer alan Kaputaş Plajı, turkuaz suları ve sarp kayalıklar arasından süzülen 187 basamağıyla Türkiye'nin en ikonik plajlarından biridir. Bir kanyonun ağzında yer alan konumu, buraya eşsiz bir renk ve atmosfer katar.",
                "en": "Situated between Kas and Kalkan, Kaputaş Beach is famous for its brilliant turquoise waters and the 187 steps carved into the cliffs. Its location at the mouth of a canyon gives it a unique color and a stunning natural setting."
            },
            "ChIJAQAAACstwBQRslW1-2qzS6A": {
                "tr": "Kaş'ın antik kenti Antiphellos, denize karşı kurulu mükemmel korunmuş tiyatrosuyla ünlüdür. Chukurbağ Yarımadası'na bakan bu antik tiyatroda gün batımını izlemek, Kaş seyahatinin en unutulmaz tarihi deneyimidir.",
                "en": "The ancient city of Antiphellos features a perfectly preserved theater built right against the Mediterranean coast. Watching the sunset from its stone steps, overlooking the peninsula, is an essential historical highlight in Kaş."
            },
            "ChIJY8GEqTXbwRQRJl9cXTo9hOw": {
                "tr": "Kaş'ın kalbi sayılan Uzun Çarşı, begonvillerle süslü cumbalı evleri ve butik dükkanlarıyla masalsı bir havaya sahiptir. Çarşının sonundaki tarihi Aslanlı Lahit, ilçenin antik Lykia mirasını kentin göbeğinde temsil eder.",
                "en": "The heart of Kaş, Uzun Çarşı, is a fairy-tale alley lined with colorful bougainvillea and historic wooden-shuttered houses. At its end, the iconic Lion Sarcophagus stands as a monumental reminder of the town's Lycian past."
            },
            "ChIJV9zSblPvwRQRLoKVtgj0Bf4": {
                "tr": "Tekne turlarıyla ulaşılabilen Kekova, 'Batık Şehir' kalıntılarıyla dünya çapında bir doğa ve tarih harikasıdır. Turkuaz suların altındaki antik merdivenleri ve ev kalıntılarını teknenizin altından cam bölmelerle görebilirsiniz.",
                "en": "Accessible only by boat, Kekova is a world-renowned natural wonder famous for its 'Sunken City' ruins. You can spot ancient staircases and house walls beneath the crystal-clear turquoise waters through glass-bottom boats."
            }
        }
        
        for h in k_data["highlights"]:
            if h["id"] in k_enrich:
                h["description"] = k_enrich[h["id"]]["tr"]
                h["description_en"] = k_enrich[h["id"]]["en"]
        
        with open(k_path, "w", encoding="utf-8") as f:
            json.dump(k_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    enrich_ibiza_kas()
