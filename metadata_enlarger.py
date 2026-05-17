import json
import os

CITY_FILES = [
    "ksamil.json", "rhodes.json", "selanik.json", "budva.json", 
    "ibiza.json", "mallorca.json", "valencia.json", "cesme.json", "kas.json"
]

CATEGORY_DEFAULTS = {
    "Tarihi": {
        "bestTime": "Sabah (09:00 - 11:00)",
        "duration": "1.5 - 2 Saat",
        "tips": "Kalabalıktan kaçınmak için erken saatlerde gelin ve rahat ayakkabı giymeyi unutmayın.",
        "tips_en": "Arrive early to avoid crowds and don't forget to wear comfortable walking shoes."
    },
    "Restoran": {
        "bestTime": "Akşam (19:00 - 21:00)",
        "duration": "1.5 - 2 Saat",
        "tips": "Akşam yemeği için mutlaka önceden rezervasyon yaptırmanızı öneririz.",
        "tips_en": "We highly recommend making a reservation in advance for dinner."
    },
    "Plaj": {
        "bestTime": "Öğleden Sonra (14:00 - 17:00)",
        "duration": "3 - 4 Saat",
        "tips": "Güneş kreminizi ve şapkanızı yanınıza alın; su altı dünyası için şnorkel önerilir.",
        "tips_en": "Bring your sunscreen and hat; a snorkel is recommended for the underwater life."
    },
    "Park": {
        "bestTime": "Sabah veya Gün Batımı",
        "duration": "1 - 2 Saat",
        "tips": "Gün batımı fotoğrafları için en ideal noktaları keşfetmek üzere biraz erken gelin.",
        "tips_en": "Arrive a bit early to discover the best spots for sunset photography."
    },
    "Default": {
        "bestTime": "Gün Boyu",
        "duration": "1 Saat",
        "tips": "Kameranızı yanınıza almayı ve yerel atmosferin tadını çıkarmayı unutmayın.",
        "tips_en": "Don't forget to bring your camera and enjoy the local atmosphere."
    }
}

CITY_LOCAL_TIPS = {
    "ksamil": [
        "Adalara ulaşım için mutlaka deniz bisikleti veya kano kiralayın.",
        "Temmuz ve Ağustos aylarında plajlar çok kalabalık olabilir, Haziran idealdir.",
        "Nakit para (Lek) bulundurmak küçük işletmelerde işinizi kolaylaştırır.",
        "Butrint Antik Kenti'ne giden yerel otobüsler çok ekonomiktir.",
        "Akşam yemeklerinde taze deniz mahsullerini denemeden dönmeyin."
    ],
    "rhodes": [
        "Eski Şehir (Old Town) içinde kaybolmak en güzel keşif yöntemidir.",
        "Şövalyeler Sokağı'nı (Street of Knights) boş yakalamak için sabah 08:00'de orada olun.",
        "Adanın batı kıyısı rüzgarlıdır, sakin deniz için doğu kıyısındaki plajları seçin.",
        "Lindos'a gidiş için erken saatleri veya deniz yoluyla ulaşımı tercih edin.",
        "Yerel 'Melekouni' tatlısını mutlaka deneyin."
    ],
    "selanik": [
        "Sahil şeridinde Kordon boyunca yürüyüş yapmak Selanik klasiğidir.",
        "Ano Poli (Yukarı Şehir) bölgesine gün batımında çıkıp manzarayı izleyin.",
        "Kapani ve Modiano pazarları yerel gastronomi keşfi için en doğru adreslerdir.",
        "Kahve kültürü çok yaygındır, bir 'Frappe' içip mola verin.",
        "Aristotelous Meydanı kentin kalbidir, buluşma noktası olarak kullanın."
    ],
    "budva": [
        "Stari Grad (Eski Şehir) sokakları akşamları çok daha büyüleyicidir.",
        "Sveti Nikola adasına giden uygun fiyatlı tekneleri limanda bulabilirsiniz.",
        "Adriyatik kıyısındaki kayalıklardan denize girerken dikkatli olun.",
        "Yerel şarap ve peynir çeşitlerini tatmak için yerel marketleri gezebilirsiniz.",
        "Mogren Plajı'na giden sahil yolu yürüyüşü çok fotojeniktir."
    ],
    "ibiza": [
        "Parti hayatı dışında Dalt Vila'nın (Eski Kent) tarihi sokaklarını gezin.",
        "Formentera adasına günübirlik geçiş yapmak için feribotları kullanın.",
        "En güzel gün batımı için Es Vedra manzaralı tepeleri tercih edin.",
        "Yerel 'Flaó' tatlısını geleneksel bir pastanede deneyin.",
        "Kiralık araç veya scooter, gizli koyları keşfetmek için şarttır."
    ],
    "mallorca": [
        "Palma Katedrali'ni mutlaka hem içeriden hem dışarıdan görün.",
        "Serra de Tramuntana dağ köylerine (Valldemossa, Deià) zaman ayırın.",
        "Mağaraları (Cuevas del Drach) ziyaret etmek için önceden bilet alın.",
        "Adanın meşhur hamur işi 'Ensaimada'yı denemeden dönmeyin.",
        "Kuzeydeki Cap de Formentor yolu dünyanın en güzel sürüş rotalarından biridir."
    ],
    "valencia": [
        "Gerçek 'Paella'nın anavatanındasınız, öğle yemeğinde denemenizi öneririz.",
        "Bilim ve Sanat Şehri (Ciudad de las Artes y las Ciencias) fütüristik bir keşiftir.",
        "Mercado Central Avrupa'nın en büyük taze gıda pazarlarından biridir.",
        "Turu Bahçeleri şehrin içindeki devasa bir yeşil alandır, bisikletle gezin.",
        "Horchata içeceğini orijinal yerinde (Alboraya) deneyin."
    ],
    "cesme": [
        "Alaçatı sokakları sabahın erken saatlerinde fotoğraf çekimi için en sakin halindedir.",
        "Ilıca Plajı'nın termal suları deniz içinde doğal bir spa etkisi yaratır.",
        "Çeşme kalesi müzesi bölgenin tarihini anlamak için iyi bir duraktır.",
        "Sakız reçeli ve sakızlı dondurma yörenin en meşhur lezzetleridir.",
        "Koyları gezmek için tekne turları harika bir seçenektir."
    ],
    "kas": [
        "Meis adasına günübirlik geçiş yapmak için pasaportunuzu yanınıza alın.",
        "Kekova tekne turu ile batık şehri ve kaleköyü keşfedin.",
        "Kaputaş Plajı'na iniş merdivenleri yorucu olsa da manzaraya değer.",
        "Antiphellos Antik Tiyatrosu'nda gün batımını seyredin.",
        "Kiralık motorlar çevre köyleri gezmek için en pratik yöntemdir."
    ]
}

def enrich_file(filename):
    path = os.path.join("assets/cities", filename)
    if not os.path.exists(path): return
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    city_key = filename.replace(".json", "")
    
    # Add root localTips
    if city_key in CITY_LOCAL_TIPS:
        data["localTips"] = CITY_LOCAL_TIPS[city_key]
        
    # Enrich highlights
    updated = 0
    for h in data.get("highlights", []):
        cat = h.get("category", "Default")
        if cat not in CATEGORY_DEFAULTS: cat = "Default"
        
        defaults = CATEGORY_DEFAULTS[cat]
        
        # Only add if not exists
        if "tips" not in h or not h["tips"]:
            h["tips"] = defaults["tips"]
            updated += 1
        if "tips_en" not in h or not h["tips_en"]:
            h["tips_en"] = defaults["tips_en"]
        if "bestTime" not in h or not h["bestTime"]:
            h["bestTime"] = defaults["bestTime"]
        if "duration" not in h or not h["duration"]:
            h["duration"] = defaults["duration"]
            
    if updated > 0 or "localTips" in data:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Enriched {filename} with metadata.")

def main():
    for f in CITY_FILES:
        enrich_file(f)

if __name__ == "__main__":
    main()
