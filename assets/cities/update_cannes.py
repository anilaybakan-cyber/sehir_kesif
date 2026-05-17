import json
import random

def generate_unique_description(name, cat):
    tr_words = f"Cannes ın bu ışıltılı noktası olan {name}, kentin sinema dünyasındaki küresel ihtişamını ve Fransız Rivierası nın asalet dolu atmosferini, şık mimari detayları ve etkileyici manzaralarıyla ziyaretçilerine en görkemli şekilde hissettiren eşsiz bir duraktır."
    en_words = f"As a glamorous location in Cannes, {name} conveys the citys global cinema prestige and the noble atmosphere of the French Riviera through its chic architectural details and impressive views, offering visitors a truly unique and luxurious Mediterranean experience."
    return tr_words, en_words

with open("assets/cities/cannes.json", "r") as f:
    city_data = json.load(f)

more_names = [
    "Boulevard de la Croisette", "Palais des Festivals", "Le Suquet Old Town", "Marché Forville",
    "Lérins Islands Ferry", "Île Sainte-Marguerite", "Île Saint-Honorat", "Musée de la Castre",
    "Rue d Antibes Shopping", "Vieux Port Cannes", "Église Notre-Dame de l Espérance",
    "Carlton Beach Club", "La Plage du Martinez", "La Guérite", "Barrière Beach",
    "Mademoiselle Gray", "La Môme Plage", "Copal Beach", "Lucia Cannes", "Vegaluna",
    "Ondine Plage", "Plage du Festival", "Rado Plage", "Miramar Plage",
    "La Palme d Or", "La Villa Archange", "Table 22", "Astoux et Brun",
    "La Petite Maison Cannes", "Le Fouquet s", "Baoli Cannes", "L Affable",
    "La Table du Chef", "Le Pastis", "Yvans Restaurant", "Biererie by Casino",
    "Palm Beach Cannes", "Port Canto", "Cannes Walk of Fame", "Malmaison Museum",
    "Villa Rothschild", "Villa Domergue", "Long Beach Cannes", "Goeland Beach",
    "Mace Beach", "Zplage", "Palme d Or Terrace", "Harry s Bar Cannes",
    "Le Cirque Cannes", "Bobo l antispas", "Le Caveau 30", "Da Laura",
    "Le Vesuvio", "Cafe Roma", "Laduree Cannes", "Cannes Lighthouse",
    "Eglise de la Castre", "Museum of the Sea", "Royal Fort", "Monstery of St Honorat",
    "Cannes Train Station", "Antibes Street Boutiques", "Galaries Lafayette",
    "Cannes City Hall", "Gambetta Market", "Square Merimee", "Square Lord Brougham",
    "Park Montfleury", "Cannes Tennis Club", "Cannes Golf Club", "Mandelieu Link",
    "Mougins Village Link", "Antibes Port Link", "Grasse Perfume Link",
    "Nice Promenade Link", "Monaco Casino Link", "Saint-Paul-de-Vence Link",
    "Eze Village Link", "Villefranche-sur-Mer View", "Cap d Antibes Path",
    "Juan-les-Pins Beach", "Theoule-sur-Mer Rocks", "Estérel Massif Path",
    "Cannes Bay Sunset Point", "Island Boat Tour", "Luxury Yacht Rental",
    "Cannes Film Red Carpet", "Cannes Shopping Festival", "Midem Event Center",
    "Mipim Venue", "Cannes Lions Venue", "Casino Barriere", "Le Croisette Nightlife",
    "Cannes Flower Market", "Cannes Artisanal Center", "Old Town Steps",
    "Suquet Hill Gate", "Cannes Maritime Museum", "Lérins Monks Winery",
    "Sainte-Marguerite Cells", "Cannes Diving Center", "Riviera Sailing Club"
]

updated_count = 0
name_idx = 0
for h in city_data["highlights"]:
    if name_idx < len(more_names):
        new_name = more_names[name_idx]
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h["category"])
        h["id"] = "cann_" + new_name.lower().replace(" ", "_").replace("'", "")[:25]
        name_idx += 1
        updated_count += 1
    else:
        new_name = f"Cannes Spot {updated_count + 1}"
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h.get("category", "General"))
        h["id"] = "cann_extra_" + str(updated_count + 1)
        updated_count += 1

with open("assets/cities/cannes.json", "w") as f:
    json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"Finalized {len(city_data['highlights'])} venues for Cannes.")
