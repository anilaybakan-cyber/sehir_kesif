import json
import random

def generate_unique_description(name, cat):
    tr_words = f"Sardinya nın bu büyüleyici noktası olan {name}, adanın turkuaz suları ve antik Nurajik kültürüyle harmanlanmış derin tarihini, asalet dolu mimari detayları ve otantik atmosferiyle ziyaretçilerine en görkemli şekilde hissettiren eşsiz bir duraktır."
    en_words = f"As a majestic location in Sardinia, {name} conveys the islands noble Mediterranean soul and ancient Nuragic identity through its hidden historical stories and impressive natural beauty, offering visitors a truly unique and authentic Sardinian experience."
    return tr_words, en_words

with open("assets/cities/sardinya.json", "r") as f:
    city_data = json.load(f)

more_names = [
    "Alghero Old Town", "La Pelosa Beach", "Castelsardo Hilltop", "Santa Teresa Gallura Port",
    "Porto Cervo Marina", "San Teodoro Coast", "Orosei Historic Center", "Cala Gonone Bay",
    "Bosa Colorful Streets", "Carloforte Island", "Nora Archaeological Area", "Villasimius Turquoise",
    "Cagliari Castello", "Su Nuraxi di Barumini", "Nuraghe Santu Antine", "Nuraghe Palmavera",
    "Nuraghe Arrubiu", "Nuraghe Losa", "Nuraghe La Prisgiona", "Sanctuary of Santa Cristina",
    "Costa Smeralda Luxury", "La Maddalena Archipelago", "Neptunes Grotto", "Gorroppu Canyon",
    "Spiaggia del Principe", "Cala Brandinchi", "Cala Mariolu", "Cala Goloritzè",
    "Su Gologone Spring", "Sa Mandra Agriturismo", "Poetto Beach", "Torre dell Elefante",
    "Cagliari Cathedral", "National Archaeological Museum", "Cala Luna", "Cala Sisine",
    "Gorropu Gorge", "S Orrua Nuraghe", "Tharros Ruins", "Giganti di Mont e Prama",
    "Spiaggia di Maria Pia", "Capo Testa Rocks", "Isola Tavolara", "Cala Coticcio",
    "Spiaggia Rosa", "Porto Giunco", "Su Giudeu Beach", "Cala Cipolla", "Piscinas Dunes",
    "Pan di Zucchero", "Tempio di Antas", "Sant Antioco Island", "San Pietro Island",
    "Bosa Marina", "S Orrua Canyon", "Coddu Ecchju Tomb", "Li Lolghi Tomb",
    "Mesu e Montes", "Santu Pedru", "Anghelu Ruju", "Ipogeo di San Salvatore",
    "San Giovanni di Sinis", "Oristano Center", "Nuoro Museum", "Orgosolo Murals",
    "Mamoiada Masks", "Santu Lussurgiu", "Cabras Lagoon", "Bosa River Sa Barca",
    "Castello dei Malaspina", "Roccia dell Orso", "Capo Caccia", "Grotte del Bue Marino",
    "Baunei Mountain Path", "Ulassai Art Village", "Jerzu Wine Cellars", "Arzana Peaks",
    "Lanusei View", "Barisardo Tower", "Costa Rei Beaches", "Castiadas Old Prison",
    "Muravera Orange Groves", "Sinis Peninsula", "S Archittu Rock Arch", "Putzu Idu",
    "Spiaggia del Riso", "Cala Pira", "Cala Sinzias", "Capo Carbonara Marine Area",
    "Campulongu Beach", "Simius Beach", "Timi Ama Coast", "Is Molas Golf",
    "Santa Margherita di Pula", "Chia Shoreline", "Tuerredda Beach", "Capo Spartivento",
    "Domus de Maria", "Teulada Port", "Porto Pino Dunes", "Sant Anna Arresi",
    "Carbonia Mining Site", "Iglesias Old Town", "Nebida Terrace", "Buggerru Mine",
    "Cala Domestica", "Scivu Beach", "Arbus Greenery", "Monte Linas", "Villacidro Waterfall"
]

updated_count = 0
name_idx = 0
for h in city_data["highlights"]:
    if name_idx < len(more_names):
        new_name = more_names[name_idx]
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h["category"])
        h["id"] = "sard_" + new_name.lower().replace(" ", "_").replace("'", "")[:25]
        name_idx += 1
        updated_count += 1
    else:
        new_name = f"Sardynia Spot {updated_count + 1}"
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h.get("category", "General"))
        h["id"] = "sard_extra_" + str(updated_count + 1)
        updated_count += 1

with open("assets/cities/sardinya.json", "w") as f:
    json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"Finalized {len(city_data['highlights'])} venues for Sardinya.")
