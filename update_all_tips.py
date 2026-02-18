import json
import os
import random

# -------------------------------------------------------------------------
# 1. SPECIFIC TIPS (Hand-curated for top landmarks)
# -------------------------------------------------------------------------
SPECIFIC_TIPS = {
    # PRAGUE
    "Charles Bridge": {
        "tr": "En iyi fotoğraflar için sabah 06:00-07:00 arası veya gece geç saatlerde gidin, kalabalıktan kaçının. Kuleye çıkmayı unutmayın.",
        "en": "For the best photos, go between 06:00-07:00 AM or late at night to avoid crowds. Don't forget to climb the tower."
    },
    "Prague Castle": {
        "tr": "Kompleks çok büyük, gezmek için en az 3-4 saat ayırın. Güvenlik kontrolü sırasından kaçınmak için yan girişleri kullanın.",
        "en": "The complex is huge, allocate at least 3-4 hours. Use side entrances to avoid the security check queue."
    },
    "Astronomical Clock": {
        "tr": "Saat başı gösterisi çok kalabalık olur, kalabalığın arkasında durmak yerine yan taraftaki kafelerden birinden izleyin.",
        "en": "The hourly show gets very crowded; watch from one of the side cafes instead of standing behind the crowd."
    },
    
    # MATERA
    "Sassi di Matera": {
        "tr": "Rahat yürüyüş ayakkabıları şart, zemin çok kaygan olabilir. Gün batımında ışıkların yanışını izlemek büyülüdür.",
        "en": "Comfortable walking shoes are a must, the ground can be slippery. Watching the lights turn on at sunset is magical."
    },
    "Matera Cathedral": {
        "tr": "Öğle 12:00-15:00 arası siesta nedeniyle kapalı olabilir, ziyaretinizi buna göre planlayın.",
        "en": "It might be closed for siesta between 12:00-15:00, plan your visit accordingly."
    },
    
    # HEIDELBERG
    "Heidelberg Castle": {
        "tr": "Kaleye füniküler ile çıkıp yürüyerek inin, manzara harikadır. Mahzende şarap tadımı yapabilirsiniz.",
        "en": "Take the funicular up and walk down for great views. You can do wine tasting in the cellar."
    },
    "Philosophers' Walk": {
        "tr": "En güzel kale manzarası buradan görünür. Gün batımında yanınıza atıştırmalık alıp piknik yapın.",
        "en": "The best view of the castle is from here. Bring snacks for a picnic at sunset."
    },

    # SANTORINI
    "Oia Castle": {
        "tr": "Gün batımı için en popüler nokta, iyi bir yer kapmak için en az 1.5 saat önce gitmelisiniz.",
        "en": "The most popular spot for sunset; arrive at least 1.5 hours early to secure a good spot."
    },
    
    # VENICE
    "St. Mark's Basilica": {
        "tr": "Sıra beklememek için biletinizi önceden online alın. Kıyafet kuralına (omuzlar kapalı) dikkat edin.",
        "en": "Buy tickets online in advance to skip the line. Respect the dress code (shoulders covered)."
    },

    # PARIS
    "Eiffel Tower": {
        "tr": "Zirveye asansör biletleri aylar önce tükenir, merdivenle çıkmak hem daha ucuz hem de sıra daha azdır.",
        "en": "Elevator tickets to the summit sell out months ahead; taking the stairs is cheaper and has shorter lines."
    },
    "Louvre Museum": {
        "tr": "Ana piramit girişi çok kalabalıktır, Carrousel du Louvre alışveriş merkezi girişini kullanın.",
        "en": "The main pyramid entrance is very crowded; use the Carrousel du Louvre shopping mall entrance."
    },
    
    # ROME
    "Colosseum": {
        "tr": "Forum Romanum bileti ile birleşiktir. Önce Forum'u gezmek, Kolezyum girişinde avantaj sağlayabilir.",
        "en": "Combined with Forum Romanum ticket. Visiting the Forum first might give you an advantage at the Colosseum entrance."
    },
    
    # ISTANBUL
    "Hagia Sophia": {
        "tr": "Cuma günleri öğle saatlerinde ibadet nedeniyle ziyaret kısıtlaması olabilir. Sabah erken saatleri tercih edin.",
        "en": "Visits might be restricted during Friday prayers. Prefer early morning hours."
    },
    "Galata Tower": {
        "tr": "Akşam üstü sıra çok uzar, sabah açılış saatinde giderseniz manzaranın tadını rahatça çıkarırsınız.",
        "en": "Lines get very long in the afternoon; go at opening time to enjoy the view comfortably."
    },

    # VIENNA
    "Schönbrunn Palace": {
        "tr": "Bahçeleri gezmek ücretsizdir, biletiniz olmasa bile arka taraftaki Gloriette tepesine çıkın.",
        "en": "Visiting the gardens is free; climb Gloriette hill at the back even if you don't have a ticket."
    },
    "St. Stephen's Cathedral": {
        "tr": "Güney kulesine tırmanmak yorucudur (343 basamak) ama manzara buna değer. Asansör sadece Kuzey kulesinde var.",
        "en": "Climbing the South tower is tiring (343 steps) but the view is worth it. Elevator is only in the North tower."
    },

    # BUDAPEST
    "Fisherman's Bastion": {
        "tr": "Alt katlar ücretsizdir ve manzara neredeyse aynıdır. Gün doğumu burada efsanevidir.",
        "en": "Lower levels are free and the view is almost the same. Sunrise here is legendary."
    },
    
    # AMSTERDAM
    "Anne Frank House": {
        "tr": "Biletler 6 hafta öncesinden satışa çıkar ve hemen tükenir. Planınızı erkenden yapın.",
        "en": "Tickets go on sale 6 weeks in advance and sell out immediately. Plan early."
    },
    "Rijksmuseum": {
        "tr": "Gece Nöbeti tablosunu en sakin haliyle görmek için saat 16:30'dan sonra ziyaret edin.",
        "en": "Visit after 16:30 to see The Night Watch with fewer crowds."
    },

    # BARCELONA
    "Sagrada Familia": {
        "tr": "İçeri giren ışık oyunlarını en iyi görmek için güneşli bir günde öğleden sonrayı tercih edin.",
        "en": "Prefer a sunny afternoon to best see the light play inside."
    },
    "Park Güell": {
        "tr": "Ücretsiz kısımları da güzeldir ama anıtsal bölge için bilet şarttır ve önceden alınmalıdır.",
        "en": "Free parts are nice too, but a ticket is must for the monumental zone and should be bought in advance."
    },

    # DUBAI
    "Burj Khalifa": {
        "tr": "Gün batımı saati biletleri (Prime hours) daha pahalıdır. Hemen öncesine alıp yukarıda bekleyebilirsiniz.",
        "en": "Sunset tickets (Prime hours) correspond to higher prices. Buy for slightly earlier and wait at the top."
    },

    # BRUGGE
    "Belfry of Bruges": {
        "tr": "366 basamak dar ve diktir. Çıkışta ve inişte beklemeler olabilir, klostrofobisi olanlar dikkat etmeli.",
        "en": "The 366 steps are narrow and steep. Expect waits going up and down; claustrophobics beware."
    },
    "Canal Boat Tour": {
        "tr": "Rozenhoedkaai durağı çok kalabalıktır, tura daha sakin noktalardan katılmayı deneyin.",
        "en": "The Rozenhoedkaai stop is very crowded; try joining the tour from quieter spots."
    },

    # ROVANIEMI
    "Santa Claus Village": {
        "tr": "Noel Baba ile fotoğraf çektirmek ücretsizdir ama dijital kopyasını almak ücretlidir.",
        "en": "Taking a photo with Santa is free, but getting the digital copy costs money."
    }
}

# -------------------------------------------------------------------------
# 2. GENERIC SMART TIPS (By Category & Content)
# -------------------------------------------------------------------------
CATEGORY_TIPS = {
    "Tarihi": [
        {"tr": "Rehberli turla gezmek detayları anlamak için çok daha verimli.", "en": "A guided tour is much more efficient to understand the details."},
        {"tr": "Sabah erken saatlerde giderek turist kalabalığından kaçınabilirsiniz.", "en": "Go early in the morning to avoid tourist crowds."},
        {"tr": "Fotoğraf çekimi için en iyi ışık gün batımına yakındır.", "en": "Best light for photography is near sunset."},
        {"tr": "Müze kartınız varsa girişte sıra beklemezsiniz.", "en": "You skip the line if you have a museum pass."},
        {"tr": "Yapı içerisindeki akustik harika, sessizliği dinleyin.", "en": "The acoustics inside satisfy; listen to the silence."}
    ],
    "Müze": [
        {"tr": "Biletinizi online alarak gişe sırasından kurtulun.", "en": "Buy tickets online to skip the box office line."},
        {"tr": "Sesli rehber (audio guide) kiralamak deneyimi ikiye katlar.", "en": "Renting an audio guide doubles the experience."},
        {"tr": "Hafta içi sabah saatleri en sakin zamanıdır.", "en": "Weekday mornings are the quietest times."},
        {"tr": "Bazı günler giriş ücretsiz olabilir, web sitesini kontrol edin.", "en": "Entry might be free on some days, check the website."},
        {"tr": "Çantanızı vestiyere bırakmanız gerekebilir, hazırlıklı olun.", "en": "You might need to leave bags at the cloakroom, be prepared."}
    ],
    "Park": [
        {"tr": "Yanınıza bir örtü alıp çimlerde piknik yapabilirsiniz.", "en": "Bring a blanket and have a picnic on the grass."},
        {"tr": "Gün batımını izlemek için şehirdeki en iyi noktalardan biri.", "en": "One of the best spots in the city to watch the sunset."},
        {"tr": "Yürüyüş ayakkabısı giymeniz önerilir.", "en": "Walking shoes are recommended."},
        {"tr": "Sabah koşusu veya yoga yapan yerlileri görebilirsiniz.", "en": "You can see locals jogging or doing yoga in the morning."},
        {"tr": "Güneş kremi ve şapka almayı unutmayın.", "en": "Don't forget sunscreen and a hat."}
    ],
    "Manzara": [
        {"tr": "Panoramik fotoğraf için geniş açı lensinizi hazırlayın.", "en": "Prepare your wide-angle lens for panoramic photos."},
        {"tr": "Rüzgarlı olabilir, yanınıza ince bir ceket alın.", "en": "It can be windy, bring a light jacket."},
        {"tr": "Gün doğumu burada büyüleyicidir, uykunuzdan feragat etmeye değer.", "en": "Sunrise is magical here, worth sacrificing sleep."},
        {"tr": "Teleskop/dürbün varsa yanınıza alın.", "en": "Bring a telescope/binoculars if you have them."},
        {"tr": "Akşam saatlerinde şehir ışıklarını izlemek çok romantik.", "en": "Watching city lights in the evening is very romantic."}
    ],
    "Restoran": [
        {"tr": "Akşam yemeği için rezervasyon yaptırmak şart.", "en": "Reservation is a must for dinner."},
        {"tr": "Öğle yemeği menüleri genellikle akşamdan daha uygundur.", "en": "Lunch menus are usually cheaper than dinner."},
        {"tr": "Yerel şarapları denemenizi öneririz.", "en": "We recommend trying local wines."},
        {"tr": "Şefin spesiyal tabağını sormaktan çekinmeyin.", "en": "Don't hesitate to ask for the chef's special."},
        {"tr": "Nakite hazırlıklı olun, bazı yerel yerler kart kabul etmeyebilir.", "en": "Be prepared with cash, some local places might not accept cards."}
    ],
    "Kafe": [
        {"tr": "Kahvenin yanında ev yapımı tatlılarını mutlaka deneyin.", "en": "Must try their homemade desserts with coffee."},
        {"tr": "Dışarıdaki masalarda oturup gelen geçeni izlemek çok keyifli.", "en": "Sitting at outdoor tables and people-watching is very pleasant."},
        {"tr": "Laptop ile çalışmak için uygun, Wi-Fi hızı iyi.", "en": "Suitable for working with a laptop, Wi-Fi is good."},
        {"tr": "Sabah kahvaltısı için erken gitmekte fayda var, taze kruvasanlar bitiyor.", "en": "Go early for breakfast, fresh croissants run out."},
        {"tr": "Sessiz bir köşe bulup kitap okumak için ideal.", "en": "Ideal for finding a quiet corner and reading a book."}
    ],
    "Alışveriş": [
        {"tr": "Pazarlık yapmayı deneyebilirsiniz (nazikçe).", "en": "You might try bargaining (politely)."},
        {"tr": "El yapımı hediyelikler fabrikasyon olanlardan daha değerlidir.", "en": "Handmade souvenirs are more valuable than mass-produced ones."},
        {"tr": "Tax-free formunu istemeyi unutmayın.", "en": "Don't forget to ask for the Tax-free form."},
        {"tr": "Pazar günleri kapalı olabilir, kontrol edin.", "en": "Might be closed on Sundays, do check."},
        {"tr": "Yerel tasarımcıların ürünlerine göz atın.", "en": "Check out products from local designers."}
    ],
    "Deneyim": [
        {"tr": "Fotoğraf makinenizin şarjının dolu olduğundan emin olun.", "en": "Make sure your camera battery is full."},
        {"tr": "Rehbere soru sormaktan çekinmeyin, çok ilginç hikayeler biliyorlar.", "en": "Don't hesitate to ask the guide questions, they know interesting stories."},
        {"tr": "Grup indirimi olup olmadığını sorun.", "en": "Ask if there is a group discount."},
        {"tr": "Kıyafetinizin aktiviteye uygun olduğundan emin olun.", "en": "Ensure your outfit is suitable for the activity."}
    ],
    "default": [
        {"tr": "Hafta içi ziyaret etmek daha sakin bir deneyim sunar.", "en": "Visiting on weekdays offers a calmer experience."},
        {"tr": "Yerel halkın favori noktalarından biri.", "en": "One of the favorite spots of the locals."},
        {"tr": "Çevredeki küçük hediyelik eşya dükkanlarına da uğrayın.", "en": "Stop by the small souvenir shops around."},
        {"tr": "Google Maps yorumlarına göz atarak ne yiyeceğinize karar verin.", "en": "Decide what to eat by checking Google Maps reviews."}
    ]
}

# -------------------------------------------------------------------------
# 3. LOGIC
# -------------------------------------------------------------------------

def get_smart_tip(place_name, category, tags_list):
    # 1. Check Specific Match
    if place_name in SPECIFIC_TIPS:
        return SPECIFIC_TIPS[place_name]

    # 2. Tag-based Heuristics (Simple keyword matching)
    tags_str = " ".join(tags_list).lower()
    
    if "sunset" in tags_str:
        return {
            "tr": "Gün batımından 30 dakika önce gelip yerinizi alın, manzara muazzam.", 
            "en": "Arrive 30 mins before sunset to secure a spot, the view is magnificent."
        }
    if "wine" in tags_str:
        return {
            "tr": "Ev yapımı şaraplarını denemeden dönmeyin.", 
            "en": "Don't leave without trying their house wines."
        }
    if "hike" in tags_str or "hiking" in tags_str or "walk" in tags_str:
        return {
            "tr": "Su ve rahat ayakkabı almayı kesinlikle unutmayın.", 
            "en": "Definitely don't forget water and comfortable shoes."
        }
    if "busy" in tags_str or "popular" in tags_str:
        return {
            "tr": "Çok popüler olduğu için rezervasyon yapmak veya erken gitmek şart.", 
            "en": "Since it's very popular, reservation or going early is a must."
        }

    # 3. Random Category Match
    # Use a deterministic seed based on name to ensure same place gets same tip if run again,
    # but different places get different tips.
    seed_val = sum(ord(c) for c in place_name)
    random.seed(seed_val)
    
    cat_key = category if category in CATEGORY_TIPS else "default"
    tips_list = CATEGORY_TIPS[cat_key]
    
    return random.choice(tips_list)


def update_all_cities():
    cities_dir = "assets/cities"
    files = [f for f in os.listdir(cities_dir) if f.endswith('.json')]
    
    total_updated = 0
    
    for filename in files:
        filepath = os.path.join(cities_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except:
                print(f"Skipping corrupt file: {filename}")
                continue
        
        updated_count = 0
        highlights = data.get("highlights", [])
        
        for place in highlights:
            # Always update tip to be safe and ensure variety
            name = place.get("name", "")
            category = place.get("category", "default")
            tags = place.get("tags", [])
            
            new_tip = get_smart_tip(name, category, tags)
            
            place["tips"] = new_tip["tr"]
            place["tips_en"] = new_tip["en"]
            updated_count += 1
            
        if updated_count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"✅ {filename}: Updated tips for {updated_count} places.")
            total_updated += updated_count
            
    print(f"\n🎉 Total tips refreshed: {total_updated}")

if __name__ == "__main__":
    update_all_cities()
