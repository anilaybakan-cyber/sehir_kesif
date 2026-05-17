import os, json

target_names = [
    "ALAÇATI MEYDANI",
    "Aladja Imaret (Ishak Pasha Mosque)",
    "Aquarium of Rhodes - Hydrobiological Station HCMR",
    "Bacio Nero - Stazione Centrale",
    "Bocatería Harbin",
    "Bongénie Grieder",
    "Boreal Coffee (Eaux-Vives)",
    "Cannes Maritime Museum",
    "Casa Stagnitta",
    "Çeşme Tekne Turu / Grandstar Çeşme Tekne Turları",
    "Chatzi",
    "Costarena",
    "DANICA SJAJ",
    "Dubrovnik Yacht Agent - Dubrovnik Luxury Travel Experts - Croatia",
    "Estinbel Plajı",
    "F.P.Journe Le Restaurant",
    "Grand Hotel et Des Palmes",
    "Port de Ramatuelle",
    "Hotel Hospes Palau de la Mar | Valencia",
    "Hotel ILUNION Valencia 4",
    "Hotel Miramar Valencia",
    "Hotel Porta Felice",
    "HOTEL TURIA VALENCIA",
    "Kas Camping",
    "La Ponche Quarter",
    "Las Arenas Balneario Resort",
    "Luxury Yacht Rental",
    "Maritime Museum",
    "Mr. Pickwick Pub",
    "Oxygen Pub",
    "Perle du Lac",
    "Plage des Canoubiers",
    "Principato",
    "Sala Parpalló",
    "Spomen ploča, Hrvatsko kraljevstvo",
    "Starbucks",
    "Strong Rooster",
    "Villa Igiea, a Rocco Forte hotel"
]

found = {}
assets_dir = '/Users/anilebru/Desktop/Uygulamalar/sehir_kesif/assets/cities'
for f in os.listdir(assets_dir):
    if f.endswith('.json'):
        path = os.path.join(assets_dir, f)
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
                for h in data.get('highlights', []):
                    name = h.get('name')
                    if name in target_names:
                        found[name] = (f, h.get('description', ''), h.get('description_en', ''), h.get('localTip', ''))
        except Exception as e:
            pass

print(f"Found {len(found)} / {len(target_names)} items.")
for name in target_names:
    if name in found:
        print(f"--- {name} ({found[name][0]}) ---")
        print(f"  TR:  {found[name][1]}")
        print(f"  EN:  {found[name][2]}")
        print(f"  TIP: {found[name][3]}")
    else:
        print(f"NOT FOUND: {name}")
