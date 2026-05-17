import json
import glob
import os

translations = {
  "Agafay Çölü": "Agafay Desert",
  "Agora Meyhanesi": "Agora Tavern",
  "Akvaryum Mağarası Bahçesi": "Aquarium Grotto Garden",
  "Al-Attarine Medresesi": "Al-Attarine Madrasa",
  "Anadolu Kavağı": "Anadolu Kavağı",
  "Anadolu Sofrasi": "Anadolu Sofrasi",
  "Andrássy Bulvarı": "Andrássy Avenue",
  "Antep Evleri": "Antep Houses",
  "Apple Church (Elmalı Kilise)": "Apple Church",
  "Aravan Evi": "Aravan House",
  "ARTISTA PERFETTO (Causeway Bay)": "ARTISTA PERFETTO (Causeway Bay)",
  "Asmalı Cavit": "Asmalı Cavit",
  "Asmalı Konak": "Asmalı Konak",
  "Aspendos Antik Tiyatrosu": "Aspendos Ancient Theatre",
  "At Binme Turu": "Horseback Riding Tour",
  "Atatürk Kültür Merkezi (AKM)": "Atatürk Cultural Center (AKM)",
  "Avanos Çömlekçiler Bazaar": "Avanos Potters' Bazaar",
  "AWANI RESTAURANT AFRICAIN LYON": "AWANI RESTAURANT AFRICAIN LYON",
  "Ayakkabılar Anıtı": "Shoes on the Danube Bank",
  "Aziz Stephen Bazilikası": "St. Stephen's Basilica",
  "Babayan Evi": "Babayan House",
  "Bakırcı Atölyesi Ziyareti": "Coppersmith Workshop Visit",
  "Baklava Yapım Kursu": "Baklava Making Class",
  "Balat Renkli Evler": "Balat Colorful Houses",
  "Balat ve Fener Sokakları": "Streets of Balat and Fener",
  "Balıkçı Tabyası (Fisherman's Bastion)": "Fisherman's Bastion",
  "BAR DE BON-SECOURS": "BAR DE BON-SECOURS",
  "BAR ROSA BARCELONA": "BAR ROSA BARCELONA",
  "Barbayanni Uzo Müzesi": "Barbayanni Ouzo Museum",
  "BARBOUNIA": "BARBOUNIA",
  "Bardini Bahçesi": "Bardini Gardens",
  "BARGANZO": "BARGANZO",
  "Başçarşı": "Baščaršija",
  "Baylan Pastanesi": "Baylan Patisserie",
  "Bayramoğlu Döner": "Bayramoğlu Döner",
  "Beach Park Konyaalti": "Konyaaltı Beach Park",
  "Bebek Sahili": "Bebek Promenade",
  "BEER SPOT CRAFT PUB - Beer - Cocktail - Food": "BEER SPOT CRAFT PUB - Beer - Cocktail - Food",
  "Belgrad Ormanı": "Belgrade Forest",
  "Bezistan (Kapalı Çarşı)": "Bezistan (Covered Market)",
  "BIBOU BEIGNETS Marseille": "BIBOU BEIGNETS Marseille",
  "BLUE PLATE İSTANBUL": "BLUE PLATE ISTANBUL",
  "BOCA": "BOCA",
  "BODEGA OLIVA": "BODEGA OLIVA",
  "Boğaz Turu": "Bosphorus Cruise",
  "Bogi Park": "Bogi Park",
  "BOMBAR": "BOMBAR",
  "Börekçi Tevfik": "Börekçi Tevfik",
  "Brera Sanat Bölgesi": "Brera Art District",
  "Büyük Çamlıca Tepesi": "Grand Çamlıca Hill",
  "Büyük Giza Sfenksi": "Great Sphinx of Giza",
  "Büyük Mısır Museum (GEM)": "Grand Egyptian Museum (GEM)",
  "CHIMNEY CAKE ZONE & CHURRÍA": "CHIMNEY CAKE ZONE & CHURRÍA",
  "CHOCOPANNA COFFEE": "CHOCOPANNA COFFEE",
  "COBBLER COCKTAIL BAR": "COBBLER COCKTAIL BAR",
  "Çömlek Atölyesi": "Pottery Workshop",
  "Deniz Lokantasi": "Deniz Restaurant",
  "Derinkuyu Yeraltı Şehri": "Derinkuyu Underground City",
  "DİLŞEKER Turkish Delight-Baklava-Coffe-Nuts": "DİLŞEKER Turkish Delight-Baklava-Coffee-Nuts",
  "Fener Rum Patrikhanesi": "Fener Greek Patriarchate",
  "Feriköy Antika Market": "Feriköy Antique Market",
  "Gaziantep Savunma ve Kahramanlık Panoramik Museum": "Gaziantep Panorama Museum of Heroism and Defense",
  "Gondol Turu": "Gondola Ride",
  "Göreme Açık Hava Museum": "Göreme Open Air Museum",
  "Göreme Merkez Çarşı": "Göreme Central Market",
  "Göreme Milli Park": "Göreme National Park",
  "Hadrian Kapısı (Üç Kapılar)": "Hadrian's Gate",
  "HAYAT CAFE": "HAYAT CAFE",
  "Kapadokya Balon Turu": "Cappadocia Hot Air Balloon Tour",
  "Kapalıçarşı": "Grand Bazaar",
  "Karadeniz Sahili Yürüyüşü": "Black Sea Coast Walk",
  "Kaymaklı Yeraltı Şehri": "Kaymaklı Underground City",
  "Kuzguncuk Bostanı": "Kuzguncuk Orchard",
  "MASSA BİSTRO (İSTANBUL)": "MASSA BISTRO (ISTANBUL)",
  "Matthias Kilisesi": "Matthias Church",
  "Otağtepe Fatih Korusu": "Otağtepe Fatih Grove",
  "Özkonak Yeraltı Şehri": "Özkonak Underground City",
  "Paşabağ Peribacaları": "Paşabağ Fairy Chimneys",
  "Phaselis Antik Kenti": "Phaselis Ancient City",
  "Refectory (Yemekhane)": "Refectory",
  "Sanatkarlar Parki": "Sanatkarlar Park",
  "Şarap Tadımı": "Wine Tasting",
  "Saraybosna Katedrali": "Sarajevo Cathedral",
  "Svrzo'nun Evi": "Svrzo's House",
  "Tuna Nehir Gezisi": "Danube River Cruise",
  "Türk Bath Deneyimi": "Turkish Bath Experience",
  "Türk Gecesi": "Turkish Night",
  "Üçüncü Dalga Kahvecileri": "Third Wave Coffee Shops",
  "Ürgüp Halı Mağazaları": "Ürgüp Carpet Shops"
}

directories = ["assets/cities", "ota_data_pack/cities"]
total_updated = 0

def clean(s):
    return s.strip().lower()

translations_map = {clean(k): v for k, v in translations.items()}

total_removed = 0

for base_dir in directories:
    if not os.path.exists(base_dir):
        continue
    
    for file_path in glob.glob(os.path.join(base_dir, "*.json")):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
            
        highlights = data.get('highlights', [])
        new_highlights = []
        seen_targets = set()
        
        updated_in_file = 0
        removed_in_file = 0
        
        for h in highlights:
            name_en = h.get('name_en', '')
            cl_name_en = clean(name_en)
            
            # Deduplicate "student prison"
            if "student prison" in cl_name_en or "studentenkarzer" in clean(h.get('name', '')):
                name_to_check = clean(h.get('name_en', h.get('name', '')))
                if name_to_check in seen_targets:
                    removed_in_file += 1
                    total_removed += 1
                    continue
                else:
                    seen_targets.add(name_to_check)

            # Check if name_en is in the map
            if cl_name_en in translations_map:
                new_name_en = translations_map[cl_name_en]
                if h.get('name_en') != new_name_en:
                    h['name_en'] = new_name_en
                    updated_in_file += 1
                    total_updated += 1
            
            new_highlights.append(h)
                
        if updated_in_file > 0 or removed_in_file > 0:
            data['highlights'] = new_highlights
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"Updated {updated_in_file} names, removed {removed_in_file} duplicates in {file_path}")

print(f"Total specific names updated: {total_updated}")
print(f"Total duplicates removed: {total_removed}")
