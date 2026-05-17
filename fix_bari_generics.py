import json
import os

def is_generic(text):
    patterns = [
        "Yerel malzemelere ve mutfak sanatına olan bağlılığıyla",
        "kentinin kalbindeki en stil sahibi lezzet duraklarından",
        "kentinin gastronomi dünyasında otantik lezzetleri",
        "kentinin tarih silüetini",
        "kentinin tarihi dokusunda önemli bir yer tutan"
    ]
    for p in patterns:
        if p in text:
            return True
    return False

def fix_bari_enrichment():
    path = 'assets/cities/bari.json'
    if not os.path.exists(path): return
    
    with open(path, 'r') as f:
        data = json.load(f)
    
    updates = {
        "Speakeasy Bari": {
            "description": "Bari'nin kalbinde, 1920'lerin yasaklı dönem ruhunu yaşatan bu şık mekan, kentin en sofistike kokteyl duraklarından biridir. Gizemli atmosferi, loş ışıkları ve caz tınılarıyla, yerel halkın ve kenti keşfedenlerin favori akşam rotasıdır.",
            "description_en": "In the heart of Bari, this chic venue reviving the spirit of the 1920s Prohibition era is one of the city's most sophisticated cocktail stops. With its mysterious atmosphere, dim lights, and jazz notes, it's a favorite evening route for locals and travelers alike.",
            "tips": "Rezervasyon yapmanız önerilir; barmenin o güne özel hazırladığı 'signature' kokteylleri denemeyi unutmayın.",
            "tips_en": "Reservations are recommended; don't forget to try the bartender's daily signature cocktails.",
            "category": "Sosyal"
        },
        "Nicolaus Hotel Bari": {
            "description": "Bari'nin modern silüetinde prestijli bir konuma sahip olan Nicolaus Hotel, kentin iş ve turizm dünyasını lüksle buluşturan bir merkezdir. Panoramik manzaralı restoranı ve modern spa alanıyla kentsel konforun en rafine adreslerinden biridir.",
            "description_en": "With a prestigious position in Bari's modern skyline, the Nicolaus Hotel is a hub bringing together the city's business and tourism worlds with luxury. With its panoramic view restaurant and modern spa area, it's one of the most refined addresses for urban comfort.",
            "tips": "En üst kattaki restoranda Bari manzarasına karşı kahvaltı yapın; otelin sunduğu yerel tur önerilerini değerlendirin.",
            "tips_en": "Have breakfast at the top-floor restaurant facing the Bari view; check out the local tour suggestions offered by the hotel.",
            "category": "Deneyim"
        },
        "Joy's Pub": {
            "description": "Bari'nin neşeli ve samimi sosyal yaşamını yansıtan Joy's Pub, geniş bira seçeneği ve İrlanda pub kültürünü Akdeniz sıcaklığıyla harmanlayan atmosferiyle kentin sevilen buluşma noktasıdır. Canlı müzik geceleri ve futbol maçları için kentin en enerjik duraklarından biridir.",
            "description_en": "Reflecting Bari's cheerful and sincere social life, Joy's Pub is a beloved meeting point with its wide beer selection and atmosphere blending Irish pub culture with Mediterranean warmth. It's one of the city's most energetic stops for live music nights and football matches.",
            "tips": "Hafta sonları canlı müzik programını kontrol edin; yerel biralarla eşleştirilen atıştırmalık tabaklarını deneyin.",
            "tips_en": "Check the live music schedule on weekends; try the snack platters paired with local beers.",
            "category": "Sosyal"
        },
        "Al Sorso Preferito": {
            "description": "Bari'nin meşhur 'Assassina' makarnasının doğduğu yerlerden biri olan bu tarihi restoran, yerel mutfak mirasını en otantik haliyle sunar. Kentin geleneksel tatlarını modern bir dokunuşla buluşturan mekan, gerçek bir gastronomi yolculuğu vaat eder.",
            "description_en": "One of the birthplaces of Bari's famous 'Assassina' pasta, this historical restaurant offers local culinary heritage in its most authentic form. Blending the city's traditional flavors with a modern touch, it promises a true gastronomic journey.",
            "tips": "Spaghetti all'Assassina mutlaka denenmeli; mekan oldukça popüler olduğu için önceden yerinizi ayırtın.",
            "tips_en": "Spaghetti all'Assassina is a must-try; the place is very popular, so book your spot in advance.",
            "category": "Restoran"
        },
        "Jérôme Cafè": {
            "description": "Bari'nin zarif Murat bölgesinde yer alan Jérôme Cafè, Fransız bistro estetiğini Puglia misafirperverliğiyle buluşturan şık bir mola noktasıdır. Taze hamur işleri ve kentin en iyi kavrulmuş kahveleriyle kentsel koşturmacadan uzaklaşmak için idealdir.",
            "description_en": "Located in Bari's elegant Murat district, Jérôme Cafè is a stylish break point blending French bistro aesthetics with Puglia hospitality. It's ideal for moving away from urban hustle with fresh pastries and the city's best roasted coffees.",
            "tips": "Sabah saatlerinde taze kruvasanlarını yakalamaya çalışın; dışarıdaki masalarda kentin ritmini izleyin.",
            "tips_en": "Try to catch their fresh croissants in the morning; watch the city's rhythm from the outdoor tables.",
            "category": "Sosyal"
        }
    }
    
    # Fill in more automatically or handle common ones
    changed = False
    highlights = data if isinstance(data, list) else data.get('highlights', [])
    
    for h in highlights:
        name = h.get('name')
        desc = h.get('description', '')
        
        # If it's in our manual map
        if name in updates:
            upd = updates[name]
            h['description'] = upd['description']
            h['description_en'] = upd['description_en']
            h['tips'] = upd['tips']
            h['tips_en'] = upd['tips_en']
            h['category'] = upd['category']
            changed = True
        elif is_generic(desc):
            # For others that are still generic, let's at least fix the grammar and add some variety
            if "Yerel malzemelere" in desc:
                # Replace with a better generic-but-not-broken one if we don't have a manual one
                h['description'] = f"Bari'nin mutfak mirasını ve taze yerel lezzetlerini sunan {name}, kentin gastronomi haritasında özgün bir durak olarak öne çıkar."
                h['description_en'] = f"Presenting Bari's culinary heritage and fresh local flavors, {name} stands out as an authentic stop on the city's gastronomic map."
            elif "kentinin gastronomi" in desc:
                h['description'] = f"Bari'nin gastronomi dünyasında yerel tatları ve samimi atmosferiyle tanınan {name}, kenti keşfedenlerin uğrak noktalarından biridir."
                h['description_en'] = f"Known for its local flavors and friendly atmosphere in Bari's gastronomic world, {name} is a frequent stop for city explorers."
            elif "kentinin tarih" in desc or "kentinin tarihi" in desc:
                h['description'] = f"Bari'nin zengin tarihini ve kültürel dokusunu yansıtan bu alan, kentin geçmişine ışık tutan önemli bir mirastır."
                h['description_en'] = f"Reflecting Bari's rich history and cultural texture, this area is an important heritage shedding light on the city's past."
            changed = True

    if changed:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Bari file fully cleaned and updated.")

fix_bari_enrichment()
