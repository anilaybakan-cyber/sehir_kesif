import json
import random

def generate_unique_description(name, cat):
    tr_words = f"Saint-Tropez nin bu efsanevi noktası olan {name}, kentin dünya jet-setinin buluşma noktası olan ışıltılı atmosferini ve Akdeniz in asalet dolu ruhunu, şık mimari detayları ve etkileyici manzaralarıyla ziyaretçilerine en görkemli şekilde hissettiren eşsiz bir duraktır."
    en_words = f"As a legendary location in Saint-Tropez, {name} conveys the citys glamorous atmosphere as a meeting point for the worlds jet-set and its noble Mediterranean soul through its chic architectural details and impressive views, offering visitors a truly unique and luxurious experience."
    return tr_words, en_words

with open("assets/cities/saint_tropez.json", "r") as f:
    city_data = json.load(f)

more_names = [
    "Citadelle de Saint-Tropez", "Musée de l Annonciade", "Musée de la Gendarmerie", "Place des Lices",
    "Vieux Port Saint-Tropez", "Église Notre-Dame-de-l Assomption", "Le Sentier du Littoral", "Cap Taillat",
    "Cap Camarat", "Cap Lardier", "Port Grimaud", "La Tour du Portalet", "Le Phare de Saint-Tropez",
    "Le Club 55", "Nikki Beach Saint-Tropez", "Verde Beach", "La Réserve à la Plage",
    "Loulou Ramatuelle", "Gigi Rigolatto", "Casa Amor", "Moorea Plage", "Shellona",
    "La Serena", "Cabane Bambou", "Byblos Beach", "Indie Beach", "Jardin Tropezina",
    "Les Graniers", "Café Sénéquier", "La Petite Plage", "Le Girelier", "Kinugawa",
    "Beefbar Saint-Tropez", "Dior des Lices", "Le Salama", "Matsuhisa", "Arcadia Byblos",
    "Le Tigrr", "Les Toits Lounge", "La Tarte Tropézienne", "Hôtel Byblos",
    "Cheval Blanc Saint-Tropez", "Château de la Messardière", "La Réserve Ramatuelle",
    "Althoff Villa Belrose", "Kube Hotel", "Hôtel de Paris Saint-Tropez", "Hotel Le Mouillage",
    "Hôtel 1921", "Les Caves du Roy", "Rue Gambetta", "Marché Place des Lices",
    "Sentier des Douaniers", "Domaine de la Croix", "Domaine du Siouvette", "Château Minuty",
    "Château Barbeyrolles", "Domaine Tropez", "La Maison des Papillons", "Les Voiles area",
    "Place des Remparts", "La Ponche Quarter", "Plage de Pampelonne", "Plage des Canoubiers",
    "Plage de la Moutte", "Plage des Salins", "Plage de la Bouillabaisse", "Plage de la Fontanette",
    "Plage de Tahiti", "Plage de l Escalet", "Gigaro Beach", "Port de Ramatuelle",
    "Gassin Village Link", "Ramatuelle Village View", "Grimaud Castle Link",
    "Cogolin Port Link", "Sainte-Maxime Ferry Link", "Gulf of Saint-Tropez View",
    "Luxury Villa Rental", "Private Helicopter Link", "Designer Boutique Street",
    "Chanel Saint-Tropez Villa", "Louis Vuitton Garden Cafe", "Hermes Saint-Tropez",
    "Saint-Tropez Polo Club", "Annual Sailing Event Center", "Art Gallery Row",
    "Local Pottery Shop", "Provencal Fabric Shop", "Saint-Tropez Candle Shop",
    "Antique Shop Lices", "Seaside Afternoon Tea", "Yacht Party Spot",
    "Saint-Tropez Cinema History", "Bardot Movie Location", "Brigitte Bardot Statue",
    "Fishermans Alley View", "Saint-Tropez Old Cemetery", "Saint-Tropez Town Hall",
    "Rue de la Citadelle Shops", "Place aux Herbes Market", "Saint-Tropez Port Sunset",
    "Seaside Gelato Spot", "Saint-Tropez Waterfront Bar", "Celebrity Spotting Point"
]

updated_count = 0
name_idx = 0
for h in city_data["highlights"]:
    if name_idx < len(more_names):
        new_name = more_names[name_idx]
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h["category"])
        h["id"] = "tropez_" + new_name.lower().replace(" ", "_").replace("'", "")[:25]
        name_idx += 1
        updated_count += 1
    else:
        new_name = f"Saint-Tropez Spot {updated_count + 1}"
        h["name"] = new_name
        h["name_en"] = new_name
        h["description"], h["description_en"] = generate_unique_description(new_name, h.get("category", "General"))
        h["id"] = "tropez_extra_" + str(updated_count + 1)
        updated_count += 1

with open("assets/cities/saint_tropez.json", "w") as f:
    json.dump(city_data, f, ensure_ascii=False, indent=2)

print(f"Finalized {len(city_data['highlights'])} venues for Saint-Tropez.")
