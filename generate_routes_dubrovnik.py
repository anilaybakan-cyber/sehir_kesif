#!/usr/bin/env python3
import json

routes = [
    {
        "id": "dubrovnik_welcome_walk",
        "title": "Eski Şehir ve Surlar",
        "title_en": "Old Town & City Walls",
        "description": "Dubrovnik'in ana kapısından girip tarihi caddede yürüyeceğiniz klasik ilk gün rotası.",
        "description_en": "A classic first-day route entering the main gate and walking down the historic street.",
        "places": [
            "ChIJS4ZSDR4LTBMRJhdsEZdA0do",  # Pile Gate
            "ChIJrRQV8Sl1TBMRQgJUuy8kapE",  # Onofrio Fountain
            "ChIJKU9Y8jILTBMR9V8NPzgOYKA",  # Stradun
            "ChIJV0zVnDILTBMRkekZb2h93ZY"   # City Walls
        ]
    },
    {
        "id": "dubrovnik_historical_heart",
        "title": "Tarihi Meydanlar",
        "title_en": "Historical Squares",
        "description": "Sponza Sarayı'ndan eski limana kadar uzanan büyüleyici tarihi meydanlar keşfi.",
        "description_en": "A fascinating exploration of historical squares stretching from Sponza Palace to the old port.",
        "places": [
            "ChIJkW5gATMLTBMRqGum2B_N_fw",  # Sponza Palace
            "ChIJh3rhADMLTBMRS4ifiDjqUOI",  # St Blaise Church
            "ChIJdTJ5BDMLTBMRgJv4Ds8LC6o",  # Clock Tower
            "ChIJKWCjpjMLTBMRug74-sFoPLs"   # Old Port
        ]
    },
    {
        "id": "dubrovnik_got_locations",
        "title": "King's Landing Rotası",
        "title_en": "King's Landing Route",
        "description": "Game of Thrones dizisine set olan efsanevi yapıları ve utanç yürüyüşü merdivenlerini keşfedin.",
        "description_en": "Discover the legendary structures and walk of shame stairs that served as sets for Game of Thrones.",
        "places": [
            "ChIJ4czHjy0LTBMRvup4wsiWIGk",  # Fort Bokar
            "ChIJEc_hljILTBMRuAoETlUwvys",  # Minčeta
            "ChIJbfhlPzILTBMRlvhFJaB7X78",  # St Ignatius (Walk of Shame)
            "ChIJb1nBXkALTBMRuoGz9vGMVH0"   # Benedictine Monastery Lokrum
        ]
    },
    {
        "id": "dubrovnik_viewpoints",
        "title": "Panoramik Tepeler",
        "title_en": "Panoramic Hills",
        "description": "Teleferik manzaralarından sarp kayalıklara şehrin en büyüleyici seyir noktaları.",
        "description_en": "The city's most breathtaking viewpoints from cable car vistas to steep cliffs.",
        "places": [
            "ChIJ67C5sMx0TBMRkWSlwIfYR6g",  # Cable Car
            "ChIJ_c-i-TgLTBMRvv7VyEWVaz0",  # Fort Royal
            "ChIJHV1uSlELTBMR8Utu6s1XYX8",  # Park Orsula
            "ChIJD-jUeDQLTBMRGXhmaT3ka7M"   # Porporela
        ]
    },
    {
        "id": "dubrovnik_beach_day",
        "title": "Güneş ve Kum",
        "title_en": "Sun and Sand",
        "description": "Adriyatik'in serin sularında şehrin eteklerindeki popüler plajlarda dinlenin.",
        "description_en": "Relax on the popular beaches at the foothills of the city in the cool waters of the Adriatic.",
        "places": [
            "ChIJlczNgQQLTBMRabepoBhtYcA",  # Banje Beach
            "ChIJp7tiGUR1TBMRqSOFDnhsrWM",  # Copacabana
            "ChIJacUZVQB1TBMRO1mApjZQl2c",  # Coral Beach
            "ChIJ0Qrc2Qx1TBMRjk4VAoh6kfo"   # Vis Beach
        ]
    },
    {
        "id": "dubrovnik_romantic_sunset",
        "title": "Romantik Gün Batımı",
        "title_en": "Romantic Sunset",
        "description": "Kayalıkların üzerinde kokteyl yudumlayıp güneşi batıracağınız samimi duraklar.",
        "description_en": "Intimate stops where you can sip cocktails on the cliffs and watch the sun set.",
        "places": [
            "ChIJs4R9FjILTBMRMnlEynjHdms",  # Buža Bar
            "ChIJ63UJLUl1TBMRh4bDvuxByUQ",  # Cave Bar More
            "ChIJFb6cub11TBMR3llbfj3AsGc",  # Bay of sunset2
            "ChIJK4MvdD8LTBMRUgTmV0mvDJI"   # Karaka Sunset Cruise
        ]
    },
    {
        "id": "dubrovnik_island_hopping",
        "title": "Elafiti Adaları Gezisi",
        "title_en": "Elaphiti Islands Trip",
        "description": "Dubrovnik limanından kalkan teknelerle yemyeşil huzurlu adaları gezin.",
        "description_en": "Tour the lush, peaceful islands with boats departing from the Dubrovnik port.",
        "places": [
            "ChIJKWCjpjMLTBMRug74-sFoPLs",  # Old Port
            "ChIJWd8n8duKSxMRkIvywOHyWZ0",  # Koločep
            "ChIJf8ktPKGMSxMRhMd9LygH_-A",  # Lopud
            "ChIJ95zKaTx1TBMRjA1qP2mbLu0"   # Boat Charter
        ]
    },
    {
        "id": "dubrovnik_nightlife",
        "title": "Hareketli Dubrovnik Geceleri",
        "title_en": "Vibrant Dubrovnik Nights",
        "description": "Tarihi kaleler içine gizlenmiş dev gece kulüpleri ve neon ışıklı elit eğlence merkezleri.",
        "description_en": "Giant nightclubs hidden inside historic castles and elite neon-lit entertainment venues.",
        "places": [
            "ChIJZ51lGDMLTBMRToGCUfIYtos",  # Revelin
            "ChIJxWIyUGgLTBMR1OSFezuNR0k",  # Lazareti
            "ChIJqSfStSkLTBMRCAk6Iedqb_4",  # Elyx Night Club
            "ChIJfdSkttQKTBMRT_Nd7ckB6tE"   # Casino Libertas
        ]
    },
    {
        "id": "dubrovnik_culture_religion",
        "title": "Katedral ve Kiliseler",
        "title_en": "Cathedrals and Churches",
        "description": "İhtişamlı freskler ve paha biçilemez dini eserlerle dolu inanç tarihi rotası.",
        "description_en": "A faith history route filled with magnificent frescoes and priceless religious artifacts.",
        "places": [
            "ChIJbbnurzMLTBMRBa8dNgOdjbQ",  # Cathedral of Assumption
            "ChIJh3rhADMLTBMRS4ifiDjqUOI",  # St Blaise
            "ChIJbfhlPzILTBMRlvhFJaB7X78",  # St Ignatius
            "ChIJD7OV-jILTBMRj53kxb0MXjw"   # Pharmacy Domus Christi
        ]
    },
    {
        "id": "dubrovnik_lapad_peninsula",
        "title": "Lapad Yarımadası",
        "title_en": "Lapad Peninsula",
        "description": "Eski Şehre kısa mesafede ormanlık yollar, kayalık kafeler ve sükunetli plajlar.",
        "description_en": "Forested paths, cliffside cafes, and tranquil beaches a short distance from the Old Town.",
        "places": [
            "ChIJEfIknrZ1TBMRF2-wRjN9Cr4",  # Fontana Uvala Lapad
            "ChIJv6cNsDJ1TBMR619KFhPCyrQ",  # Uvala Lapad sunbathing
            "ChIJqwxVmeh1TBMRqPcfmOBeIFw",  # Kayaking Lapad
            "ChIJifGTVlJ1TBMRapdAdLValyE"   # Esperanza Bar
        ]
    },
    {
        "id": "dubrovnik_nature_parks",
        "title": "Doğa ve Botanik",
        "title_en": "Nature and Botanical",
        "description": "Arboretumlar, asırlık ormanlar ve doğayla baş başa kalınan en güzel bahçeler.",
        "description_en": "Arboretums, century-old forests, and the most beautiful gardens to be alone with nature.",
        "places": [
            "ChIJ4z4CXZeLSxMR3xMWF30_XgI",  # Trsteno Arboretum
            "ChIJaQvZLEALTBMRJDp0AaUWW04",  # Charlotte's Well
            "ChIJHV1uSlELTBMR8Utu6s1XYX8",  # Park Orsula
            "ChIJzcmreAJ1TBMRMWcwmnTZFPM"   # Sunset view point Lapad
        ]
    },
    {
        "id": "dubrovnik_active_adventure",
        "title": "Aktif ve Maceracı",
        "title_en": "Active and Adventurous",
        "description": "Kano yapmak, kaçış odasında gizem çözmek ve şehirde koşmak isteyenler için.",
        "description_en": "For those who want to kayak, solve mysteries in an escape room, and run through the city.",
        "places": [
            "ChIJwT7rSE11TBMRZzoEo63JCsY",  # Segway
            "ChIJy8JBdTILTBMRnUoRue5MHd8",  # Running Tours
            "ChIJqwxVmeh1TBMRqPcfmOBeIFw",  # Kayaking
            "ChIJdxR4SM0KTBMR2KWoNw2ume8"   # Puzzle Punks
        ]
    },
    {
        "id": "dubrovnik_local_corners",
        "title": "Yerel Hayatın Sırları",
        "title_en": "Secrets of Local Life",
        "description": "Kalabalıktan izole, sadece yerel halkın bildiği sevimli çeşmeler ve gizli iskeleler.",
        "description_en": "Isolated from the crowds, cute fountains and hidden piers known only to the locals.",
        "places": [
            "ChIJDVPAhV11TBMRtJ02tZ2ayJA",  # Mural Hajduk
            "ChIJC4tyaTl1TBMRmg3G0iVT9pM",  # Mandrac Pier
            "ChIJB697WgB1TBMRq99pBo0m3bw",  # Seahorse statue
            "ChIJ_xFZZyV1TBMRZqo-9BlvA3A"   # Small fountain
        ]
    },
    {
        "id": "dubrovnik_family_trip",
        "title": "Çocuklarla Eğlence",
        "title_en": "Fun with Kids",
        "description": "Akvaryum gezisi, heyecanlı bir teleferik yolculuğu ve sığ güvenli plajlar.",
        "description_en": "An aquarium trip, an exciting cable car ride, and shallow safe beaches.",
        "places": [
            "ChIJt_CbozMLTBMRlgTKPFmeoaU",  # Aquarium
            "ChIJ67C5sMx0TBMRkWSlwIfYR6g",  # Cable Car
            "ChIJv6cNsDJ1TBMR619KFhPCyrQ",  # Uvala Lapad
            "ChIJbQBIDQALTBMRNloB9GfsNdw"   # Burger festival
        ]
    },
    {
        "id": "dubrovnik_luxury_delight",
        "title": "Lüks ve Seçkin",
        "title_en": "Luxury and Exclusive",
        "description": "Özel deniz locaları, lüks yat kiralama ve VIP gece kulübü eğlencesi.",
        "description_en": "Private sea cabanas, luxury yacht charters, and VIP nightclub entertainment.",
        "places": [
            "ChIJo-PFkCp1TBMRTLvmhGLP68w",  # Adriatic Pearl
            "ChIJj4frh7Z1TBMRv0gt4h1AnqI",  # YAKITO lounge
            "ChIJqy_J_TILTBMRdxEXjPdh6bo",  # Small Onofrio
            "ChIJyxjQh5x1TBMRjm2XxNFaEbo"   # Striptease Cristal
        ]
    }
]

filepath = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities/dubrovnik.json.draft'
with open(filepath, 'r', encoding='utf-8') as f:
    data = json.load(f)
    if isinstance(data, list):
        highlights = data
    else:
        highlights = data.get("highlights", [])

data['curated_routes'] = routes

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Generated and injected 15 routes into {filepath}")
