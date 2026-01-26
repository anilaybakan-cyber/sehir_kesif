
import json
import os

cities_dir = "/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities"

replacements = {
    "viyana.json": {
        "Kaffeehäuser": {
            "name": "Café Landtmann",
            "area": "Innere Stadt",
            "description": "Freud'un favori mekanı. Klasik Viyana kahve evi atmosferi, şık garsonlar ve harika pastalar.",
            "description_en": "Freud's favorite spot. Classic Viennese coffee house atmosphere, elegant waiters and great cakes.",
            "tags": ["kafe", "tarihi", "freud"],
            "imageUrl": "PLACEHOLDER"
        },
        "Wiener Schnitzel": {
            "name": "Figlmüller Bäckerstraße",
            "area": "Innere Stadt",
            "description": "Viyana'nın en meşhur şnitselcisi. Tabaktan taşan devasa porsiyonlar.",
            "description_en": "Vienna's most famous schnitzel place. Huge portions overflowing the plate.",
            "tags": ["şnitsel", "geleneksel", "meşhur"],
            "imageUrl": "PLACEHOLDER",
            "tips": "Mutlaka rezervasyon yapın. Bäckerstraße şubesi daha büyük ve rahattır."
        },
        "Wiener Würstelstand": {
            "name": "Bitzinger Würstelstand Albertina",
            "area": "Innere Stadt",
            "description": "Albertina Müzesi'nin hemen önünde efsanevi sosisçi. Opera çıkışı Viyana klasiği.",
            "description_en": "Legendary sausage stand right in front of Albertina Museum. A Vienna classic after Opera.",
            "tags": ["sosis", "sokak", "popüler"],
            "imageUrl": "PLACEHOLDER"
        },
        "Sachertorte": {
            "name": "Café Sacher",
            "area": "Innere Stadt",
            "description": "Orijinal Sachertorte'nin evi. 1832'den beri değişmeyen gizli tarif.",
            "description_en": "Home of the original Sachertorte. Secret recipe unchanged since 1832.",
            "tags": ["pasta", "çikolata", "lüks"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "budapeste.json": {
        "Goulash & Macar Mutfağı": {
            "name": "Gettó Gulyás",
            "area": "Yahudi Mahallesi",
            "description": "Uygun fiyata en iyi Gulaş ve Pörkölt (yahni). Gösterişsiz ama çok lezzetli.",
            "description_en": "Best Goulash and Pörkölt (stew) for reasonable prices. Unpretentious but delicious.",
            "tags": ["gulaş", "yerel", "lezzet"],
            "imageUrl": "PLACEHOLDER"
        },
        "Ruin Barlar": {
            "name": "Instant-Fogas Complex",
            "area": "Yahudi Mahallesi",
            "description": "Budapeşte'nin en büyük ruin bar kompleksi. Labirent gibi odalar, farklı müzikler.",
            "description_en": "Budapest's largest ruin bar complex. Maze-like rooms, different music.",
            "tags": ["bar", "gece", "parti"],
            "imageUrl": "PLACEHOLDER"
        },
        "Lángos": {
            "name": "Retró Lángos Büfé",
            "area": "Pest",
            "description": "Şehrin en iyi ve en popüler Lángosçusu. Klasik peynirli ve kremalıyı deneyin.",
            "description_en": "City's best and most popular Lángos place. Try the classic cheese and sour cream.",
            "tags": ["sokak", "kızartma", "ucuz"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "prag.json": {
        "Çek Birası": {
            "name": "U Fleků",
            "area": "New Town",
            "description": "1499'dan beri bira üreten tarihi taverna. Kendi siyah biraları (dark lager) meşhur.",
            "description_en": "Historic brewing tavern since 1499. Famous for their own dark lager.",
            "tags": ["bira", "tarihi", "müzik"],
            "imageUrl": "PLACEHOLDER"
        },
        "Trdelník": {
            "name": "Good Food Coffee & Bakery",
            "area": "Old Town",
            "description": "Meşhur 'Baca Keki'ni dondurma ve çikolatayla modernleştiren popüler mekan.",
            "description_en": "Popular spot modernizing famous 'Chimney Cake' with ice cream and chocolate.",
            "tags": ["tatlı", "popüler", "baca keki"],
            "imageUrl": "PLACEHOLDER"
        },
        "Svíčková": {
            "name": "Lokál Dlouhááá",
            "area": "Old Town",
            "description": "Taze tank birası ve ev yemekleri. Svíčková (kremalı biftek) için en doğru adres.",
            "description_en": "Fresh tank beer and homemade dishes. Best place for Svíčková (beef with cream).",
            "tags": ["yerel", "bira", "yemek"],
            "imageUrl": "PLACEHOLDER"
        },
        "Kafka Prag": {
            "name": "Franz Kafka - Rotating Head",
            "area": "New Town",
            "description": "David Cerný'nin tasarladığı 11 metre yüksekliğinde, sürekli dönen ve şekil değiştiren dev kafa heykeli.",
            "description_en": "Giant rotating and shape-shifting head sculpture designed by David Cerný, 11 meters high.",
            "tags": ["sanat", "modern", "heykel"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "marakes.json": {
        "Tagine": {
            "name": "Al Fassia",
            "area": "Gueliz",
            "description": "Sadece kadınların çalıştırdığı efsane restoran. Geleneksel Fas mutfağının zirvesi.",
            "description_en": "Legendary restaurant run entirely by women. Pinnacle of traditional Moroccan cuisine.",
            "tags": ["restoran", "geleneksel", "şık"],
            "imageUrl": "PLACEHOLDER",
            "tips": "Kuzu omuz (Lamb Shoulder) spesiyalleri. Rezervasyon şart."
        },
        "Hammam Deneyimi": {
            "name": "Les Bains de Marrakech",
            "area": "Medina",
            "description": "Marakeş'in en ünlü lüks hamam ve spa merkezi. Geleneksel kese ve masaj deneyimi.",
            "description_en": "Marrakech's most famous luxury hammam and spa. Traditional scrub and massage experience.",
            "tags": ["spa", "hamam", "lüks"],
            "imageUrl": "PLACEHOLDER"
        },
        "Riad Konaklama": {
            "name": "El Fenn",
            "area": "Medina",
            "description": "Sanatla dolu, rengarenk ve hip bir Riad. Terasında bir şeyler içmek için harika.",
            "description_en": "Art-filled, colorful and hip Riad. Great for having drinks on the terrace.",
            "tags": ["otel", "tasarım", "teras"],
            "imageUrl": "PLACEHOLDER"
        },
        "Souq'lar": {
            "name": "Souk Semmarine",
            "area": "Medina",
            "description": "Medina'nın ana çarşı caddesi. Halıdan lambaya her şeyi bulabileceğiniz en hareketli nokta.",
            "description_en": "Main market street of Medina. Most lively spot to find everything from rugs to lamps.",
            "tags": ["alışveriş", "pazar", "kalabalık"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "porto.json": {
        "Francesinha": {
            "name": "Café Santiago",
            "area": "Santo Ildefonso",
            "description": "Porto'nun meşhur kalorili sandviçi Francesinha için en iyi ve en orijinal adres.",
            "description_en": "Best and most original address for Porto's famous caloric sandwich Francesinha.",
            "tags": ["sandviç", "meşhur", "doyurucu"],
            "imageUrl": "PLACEHOLDER"
        },
        "Pastel de Nata": {
            "name": "Manteigaria",
            "area": "Bolhão",
            "description": "Sadece Pastel de Nata yapan, gözünüzün önünde üretilen taze tartlar. Çan çalınca taze çıktı demek.",
            "description_en": "Place making only Pastel de Nata, fresh tarts made in front of you. Bell rings when fresh batch is out.",
            "tags": ["tatlı", "taze", "sıcak"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "sevilla.json": {
        "Tapas Deneyimi": {
            "name": "El Rinconcillo",
            "area": "Casco Antiguo",
            "description": "1670'den beri açık! İspanya'nın en eski tapas barı. Ispanaklı nohut (Espinacas con garbanzos) efsane.",
            "description_en": "Open since 1670! Spain's oldest tapas bar. Spinach with chickpeas (Espinacas con garbanzos) is legendary.",
            "tags": ["tarihi", "tapas", "otantik"],
            "imageUrl": "PLACEHOLDER"
        },
        "Semana Santa & Feria": {
            "name": "Basilica de la Macarena",
            "area": "Macarena",
            "description": "Sevilla'nın en kutsal Meryem Ana heykeli burada. Semana Santa festivalinin kalbi.",
            "description_en": "Seville's most sacred Virgin Mary statue is here. Heart of Semana Santa festival.",
            "tags": ["kilise", "kutsal", "altın"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "stockholm.json": {
        "Fika Kültürü": {
            "name": "Vete-Katten",
            "area": "Norrmalm",
            "description": "1928'den beri klasik İsveç pastanesi. Labirent gibi odalar ve en iyi tarçınlı çörek (Kanelbullar).",
            "description_en": "Classic Swedish patisserie since 1928. Maze-like rooms and best cinnamon buns (Kanelbullar).",
            "tags": ["kafe", "klasik", "tarçın"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "kopenhag.json": {
        "Smørrebrød": {
            "name": "Aamanns 1921",
            "area": "Indre By",
            "description": "Geleneksel açık sandviçi Michelin rehberi seviyesine taşıyan modern mekan.",
            "description_en": "Modern place taking traditional open sandwich to Michelin guide level.",
            "tags": ["sandviç", "gurme", "öğle"],
            "imageUrl": "PLACEHOLDER"
        }
    },
    "napoli.json": {
        "Pasticceria Pintauro (Sfogliatella)": {
             "name": "Pintauro",
             "area": "Toledo",
             "description": "Sfogliatella tatlısının mucidi (1785). Sıcak ve çıtır hamur işi için tek adres.",
             "description_en": "Inventor of Sfogliatella dessert (1785). The only address for hot and crispy pastry.",
             "tags": ["tatlı", "tarihi", "hamur"],
             "imageUrl": "PLACEHOLDER"
        }
    }
}

def refine_pois():
    for filename, changes in replacements.items():
        filepath = os.path.join(cities_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            updated_count = 0
            for poi in data['highlights']:
                if poi['name'] in changes:
                    new_info = changes[poi['name']]
                    print(f"Updating {filename}: {poi['name']} -> {new_info['name']}")
                    
                    # Update fields
                    poi['name'] = new_info['name']
                    poi['description'] = new_info['description']
                    poi['description_en'] = new_info['description_en']
                    poi['area'] = new_info.get('area', poi['area']) # Update area if provided
                    poi['tags'] = new_info.get('tags', poi['tags'])
                    poi['imageUrl'] = "PLACEHOLDER" # Reset image to force update
                    
                    if 'tips' in new_info:
                        poi['tips'] = new_info['tips']
                        
                    updated_count += 1
            
            if updated_count > 0:
                with open(filepath, 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"Saved {filename} with {updated_count} updates.")
            else:
                 print(f"No matches found in {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    refine_pois()
