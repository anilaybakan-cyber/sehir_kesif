import json
import random

def generate_unique_description(name, cat):
    vocal = ["ikonik", "görkemli", "etkileyici", "tarihi", "stratejik", "sanatsal", "gastronomik", "asil", "mühürlü", "otantik"]
    verbs = ["yansıtır", "sunar", "buluşturur", "korur", "sergiler", "anlatır"]
    
    tr_words = f"Bari nın bu etkileyici noktası olan {name}, kentin Adriyatik sahilindeki derin tarihi mirasını ve kültürel zenginliğini, asalet dolu mimari detayları ve otantik atmosferiyle ziyaretçilerine en görkemli şekilde hissettiren eşsiz bir duraktır."
    en_words = f"As a majestic location in Bari, {name} conveys the citys noble Adriatic soul and maritime identity through its hidden historical stories and impressive architecture, offering visitors a truly unique and authentic Mediterranean experience."
    return tr_words, en_words

with open("assets/cities/bari.json", "r") as f:
    city_data = json.load(f)

more_names = [
    "Bari Vecchia", "Basilica di San Nicola", "Cattedrale di San Sabino", "Castello Normanno-Svevo",
    "Teatro Petruzzelli", "Teatro Margherita", "Lungomare Nazario Sauro", "Piazza Mercantile",
    "Piazza del Ferrarese", "Largo Albicocca", "Pane e Pomodoro Beach", "Strada delle Orecchiette",
    "Porto Vecchio", "Al Pescatore", "La Tana del Polpo", "Biancofiore", "PerBacco",
    "Terranima", "Ai 2 Ghiottoni", "Al Sorso Preferito", "Osteria Le Arpie", "La Uascezze",
    "Mastro Ciccio", "Urban Lassassineria Urbana", "Panificio Fiore", "Panificio Santa Rita",
    "Antico Chiosco da URUSS", "Antica Gelateria Gentile", "Le Sgagliozze di Donna Carmela",
    "Via Sparano", "Corso Cavour", "Mercato Coperto Santa Scolastica", "Via Napoli Market",
    "Fish Market Molo San Nicola", "Puglia Design Store", "Annese Shop", "Barimax Shopping",
    "Palazzo dell Acquedotto", "Pinacoteca Corrado Giaquinto", "Museo Archeologico", "Parco 2 Giugno",
    "Kursaal Santa Lucia", "Fortino di Sant Antonio", "Chiesa di San Marco dei Veneziani",
    "Palazzo Mincuzzi", "Via Argiro", "Via Manzoni", "Corso Vittorio Emanuele", "Piazza Umberto I",
    "Giardini Isabella d Aragona", "Fiera del Levante", "Planetario di Bari", "Eataly Bari",
    "Cala Paura", "Polignano a Mare Gateway", "Monopoli Road", "Trani Cathedral View",
    "Alberobello Day Trip Hub", "Castel del Monte Info", "Grotte di Castellana Guide",
    "Altamura Bread Shop", "Ostuni White City Link", "Locorotondo Balconies", "Cisternino View",
    "Gravina in Puglia Bridge", "Matera Sassi Gateway", "Brindisi Port Link", "Lecce Baroque Trip",
    "Gallipoli Beach Info", "Otranto Mosaic Link", "Santa Maria di Leuca Point",
    "Taranto Spartan Link", "Martina Franca Arch", "Ceglie Messapica Gastronomy",
    "Grottaglie Ceramics", "Manduria Wine Museum", "Monastery of Santa Scolastica",
    "Bari Russian Church", "Palazzo Fizzarotti", "Teatro Piccinni", "Palazzo della Provincia",
    "Bari War Memorial", "Sacrario Militare dei Caduti d Oltremare", "Piazza Giulio Cesare",
    "Poliba Campus", "Uniba Palace", "Bari Executive Center", "Ponte Adriatico",
    "Molo San Nicola", "Nderr a la Lanz", "Pescheria Nderr", "Chiosco San Nicola",
    "Lido San Francesco", "Torre Quetta", "Santo Spirito Port", "Palese Coast",
    "Giovinazzo Link", "Molfetta Duomo Link", "Bisceglie Port", "Ruvo di Puglia Museum",
    "Barletta Colossus", "Andria Portal", "Canosa Archaeological Park", "Cerignola Duomo",
    "Margherita di Savoia Salt Pans", "Gargano National Park Info", "Vieste Sea Caves"
]

updated_count = 0
name_idx = 0
for h in city_data["highlights"]:
    if name_idx < len(more_names):
        new_name = more_names[name_idx]
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h["category"])
        h["id"] = "bari_" + new_name.lower().replace(" ", "_").replace("'", "")[:25]
        name_idx += 1
        updated_count += 1
    else:
        new_name = f"Bari Spot {updated_count + 1}"
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h.get("category", "General"))
        h["id"] = "bari_extra_" + str(updated_count + 1)
        updated_count += 1

with open("assets/cities/bari.json", "w") as f:
    json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"Finalized {len(city_data['highlights'])} venues for Bari.")
