#!/usr/bin/env python3
"""
Mekan kategori audit script.
Mekanın ismindeki ipuçlarından gerçek kategorisini tahmin eder ve mevcut kategori ile
karşılaştırır. Uyuşmazlıkları raporlar (ve --fix ile düzeltir).
"""

import json
import os
import sys
import re
from pathlib import Path
from collections import defaultdict

CITIES_DIR = Path(__file__).parent.parent / "assets" / "cities"

# İsim → doğru kategori eşleştirmeleri (öncelik sırasına göre)
# Daha spesifik olanlar üstte
NAME_RULES = [
    # === EĞLENCE / DENEYİM (yüksek güven) ===
    # Bu mekanlar uygulamada "Deneyim" filtresinde gözükür
    (r"\bcinema\b|\bcinéma\b|\bsinema\b|\bkinos?\b|\bmultiplex\b", "Deneyim"),
    (r"\btheatre\b|\btheater\b|\btiyatro\b|\bopera\b|\bauditorium\b", "Deneyim"),
    (r"\bstadium\b|\bstad\b|\bstadyum\b|\barena\b(?! )", "Deneyim"),
    (r"\bbowling\b|\bgolf course\b|\bgolf club\b|\btennis club\b", "Deneyim"),
    (r"\baqua ?park\b|\baquaport\b|\bwater ?park\b|\bsu park\b", "Deneyim"),
    (r"\bzoo\b|\bhayvanat bahçesi\b|\bsafari park\b", "Deneyim"),
    
    # === MÜZE / KÜLTÜR ===
    (r"\bmuseum\b|\bmüze\b|\bmusée\b|\bmuseo\b|\bmuzeum\b", "Müze"),
    (r"\bgallery\b|\bgalleri\b|\bgaleria\b|\bgalerie\b", "Sanat"),
    (r"\baquarium\b|\bakvaryum\b", "Akvaryum"),
    (r"\bplanetarium\b|\bplanetaryum\b", "Bilim"),
    (r"\blibrary\b|\bkütüphane\b|\bbiblioteca\b|\bbibliothèque\b", "Kültür"),
    
    # === TARİHİ / DİNİ ===
    (r"\bcastle\b|\bkale\b|\bcastello\b|\bschloss\b|\bchâteau\b", "Tarihi"),
    (r"\bpalace\b|\bpalazzo\b|\bsaray\b|\bpalais\b", "Saray"),
    (r"\bbasilica\b|\bbazilika\b|\bcathedral\b|\bkatedral\b|\bduomo\b|\bcattedrale\b", "Tarihi"),
    (r"\bchurch\b|\bkilise\b|\bchiesa\b|\béglise\b|\bkirche\b", "Tarihi"),
    (r"\bmosque\b|\bcamii?\b(?! |hotel)|\bdjami\b|\bmoschee\b", "Tarihi"),
    (r"\bsynagogue\b|\bsinagog\b", "Tarihi"),
    (r"\btemple\b|\btapınak\b|\btempio\b", "Tarihi"),
    (r"\bmonastery\b|\bmanastır\b|\bmonastero\b|\babbey\b|\babbazia\b", "Tarihi"),
    (r"\btomb\b|\bmezar\b|\btombe\b|\btumba\b", "Tarihi"),
    (r"\bruins?\b|\bharabe\b|\bantik kent\b|\bantik şehir\b|\bancient\b", "Tarihi"),
    (r"\bmonument\b|\bmonumento\b|\banıt\b", "Tarihi"),
    (r"\btower\b|\bkule\b|\btorre\b|\bturm\b", "Tarihi"),
    (r"\bgate\b(?! way)|\bkapı\b|\bporta\b|\btor\b", "Tarihi"),
    
    # === MEYDAN / SOKAK ===
    (r"\bsquare\b|\bmeydanı\b|\bplaza\b|\bplatz\b|\bplace de\b|\bpiazza\b|\bpiazzetta\b", "Meydan"),
    (r"\b(caddesi|sokak|sokağı|street|avenue|via |corso |strada|rue )\b", "Sokak"),
    
    # === MANZARA / DOĞA ===
    (r"\bviewpoint\b|\bmanzara\b|\bbelvedere\b|\bmirador\b|\bpanorama\b|\bseyir terası\b", "Manzara"),
    (r"\bgrotto\b|\bcaverna\b|\bmağara\b|\bcave\b|\bgrotta\b", "Manzara"),
    
    # === PARK / DOĞA ===
    (r"\bpark\b|\bparc\b|\bparco\b|\bjardins?\b|\bgarden\b|\bbahçe(si)?\b", "Park"),
    (r"\blake\b|\bgöl\b|\blago\b|\blac\b|\blaguna\b", "Göl"),
    (r"\bforest\b|\borman\b|\bbosco\b|\bforêt\b|\bwald\b", "Doğa"),
    (r"\bnational park\b|\bmilli park\b|\bparco nazionale\b", "Doğa"),
    (r"\bwaterfall\b|\bşelale\b|\bcascata\b|\bcascade\b", "Manzara"),
    
    # === PLAJ / DENİZ ===
    (r"\bbeach\b|\bplaj(ı)?\b|\bspiaggia\b|\bplage\b|\bstrand\b", "Plaj"),
    (r"\bharbor\b|\bharbour\b|\bport\b(?! |o)|\bliman\b|\bporto\b", "Liman"),
    (r"\bmarina\b", "Liman"),
    
    # === ALIŞVERİŞ ===
    (r"\bbazaar\b|\bçarşı\b|\bbazar\b|\bbazaars?\b", "Alışveriş"),
    (r"\bmarket\b|\bpazar\b(?!ı)|\bmercato\b|\bmarché\b|\bmarkt\b", "Alışveriş"),
    (r"\bshopping( center| centre| mall)?\b|\bavm\b|\bcentro commerciale\b", "Alışveriş"),
    (r"\bmall\b|\bgaleri pasajı\b|\bpasajı?\b", "Alışveriş"),
    (r"\bmagazzini\b|\bmağaza\b|\boutlet\b", "Mağaza"),
    
    # === YEMEK / İÇECEK ===
    (r"\b(ristorante|restaurante|restaurant|restoran)\b", "Restoran"),
    (r"\b(osteria|trattoria|taverna|tavern|locanda)\b", "Restoran"),
    (r"\b(pizzeria|pizzerie|pizza)\b", "Restoran"),
    (r"\b(steakhouse|grill|barbecue|bbq)\b", "Restoran"),
    (r"\b(bistro|bistrot|brasserie)\b", "Restoran"),
    (r"\b(café|caffè|caffe|coffee|kahve|kafé|kafe)\b", "Kafe"),
    (r"\b(bar|pub)\b(?! |a |i )", "Bar"),
    (r"\bbakery\b|\bfırın\b|\bforno\b|\bpasticceria\b|\bkonditorei\b|\bboulangerie\b", "Fırın"),
    (r"\bgelateria\b|\bdondurma\b|\bice cream\b|\bglacier\b", "Dondurma"),
    (r"\bwinery\b|\bvineyard\b|\bbağ evi\b|\bcantina\b", "Şarap"),
    (r"\bclub\b(?! |house)|\bnightclub\b|\bdiscotheque\b|\bdiskotek\b", "Gece Hayatı"),
    
    # === HARİÇ TUTULAN (kaldırılacak/işaretlenecek) ===
    (r"\bhotel\b|\bhostel\b|\botel\b|\bresort\b|\bb&b\b|\bguest ?house\b", "Otel"),
    (r"\bpharmacy\b|\beczane\b|\bfarmacia\b|\bapotheke\b", "Sağlık"),
    (r"\bhospital\b|\bhastane\b|\bospedale\b|\bkrankenhaus\b", "Sağlık"),
    (r"\bairport\b|\bhavalimanı\b|\baeroporto\b|\baéroport\b|\bflughafen\b", "Ulaşım"),
    (r"\b(metro|tram|train station|gare|bahnhof|stazione|istasyonu)\b", "Ulaşım"),
    (r"\bschool\b|\bokul\b|\buniversity\b|\büniversite\b|\bskola\b|\buniversità\b", "Eğitim"),
    (r"\bbank\b|\bbanka\b", "İş"),
    (r"\bembassy\b|\bbüyükelçilik\b|\bconsulate\b|\bkonsolosluk\b", "Bilgi"),
]

# Mevcut kategori-ailesi - aynı aile içindeyse uyuşmazlık değil
CATEGORY_FAMILIES = {
    "Yeme-İçme": ["Yeme-İçme", "Restoran", "Yeme & İçme", "Yeme İçme", "Sokak Lezzeti", "Yemek", "Gastronomi"],
    "Kafe": ["Kafe", "Cafe", "Kahve", "Tatlı", "Fırın", "Dondurma", "Atıştırmalık", "Pasticceria"],
    "Müze": ["Müze", "Sanat", "Kültür", "Bilim", "Modern", "Akvaryum", "Galeri"],
    "Park": ["Park", "Doğa", "Göl", "Hayvanat Bahçesi"],
    "Bar": ["Bar", "Gece Hayatı", "Gece Kulübü", "Şarap", "Müzik", "Pub"],
    "Tarihi": ["Tarihi", "Meydan", "Mimari", "Tarih", "Simge", "Landmark", "Heykel", "Saray", "Merkez", "Anıt", "Kale"],
    "Manzara": ["Manzara", "View", "Teras", "Seyir", "Panaromik", "Mağara"],
    "Deneyim": ["Deneyim", "Aktivite", "Eğlence", "Yürüyüş", "Spor", "Gezi", "Macera", "Rahatlama",
                "Günlük Gezi", "Etkinlik", "Atölye", "Mahalle", "Sokak", "Köy", "Kasaba", "Şehir", "Bölge"],
    "Alışveriş": ["Alışveriş", "Mağaza", "Pazar", "Pasaj", "Ticaret", "Kitapçı", "Lüks", "Kompleks"],
    "Plaj": ["Plaj", "Beach", "Sahil"],
    "Liman": ["Liman", "Port", "Marina"],
    "Sağlık": ["Sağlık"],
    "Otel": ["Otel", "Konaklama"],
    "Ulaşım": ["Ulaşım"],
    "Eğitim": ["Eğitim"],
    "İş": ["İş"],
    "Bilgi": ["Bilgi"],
}

# Kategori → ana aile haritası
CATEGORY_TO_FAMILY = {}
for family, members in CATEGORY_FAMILIES.items():
    for m in members:
        CATEGORY_TO_FAMILY[m] = family


def split_camel_case(name: str) -> str:
    """AncheCinema → Anche Cinema (PascalCase compound isimleri ayır)"""
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', name)


def all_matching_categories(name: str) -> list[str]:
    """İsim içindeki tüm kategori ipuçlarını döndür (sıra: spesifikten genele)"""
    # Hem orijinal hem CamelCase ayrılmış formu ara
    variants = [name.lower(), split_camel_case(name).lower()]
    matches = []
    seen = set()
    for variant in variants:
        for pattern, category in NAME_RULES:
            if re.search(pattern, variant, re.IGNORECASE):
                if category not in seen:
                    matches.append(category)
                    seen.add(category)
    return matches


# Sadece bunlarda düzeltme yap - yanlış pozitif riski düşük olan kategoriler
HIGH_CONFIDENCE_CATEGORIES = {
    "Müze", "Akvaryum", "Bilim", "Galeri",
    "Saray", "Tarihi", "Meydan",
    "Park", "Doğa", "Göl",
    "Plaj", "Liman",
    "Sağlık", "Eğitim", "Ulaşım",  # Asla restoran olmayan tipler
    "Manzara",  # Mağara, viewpoint
    "Deneyim",  # Cinema/Theater/Stadium - Deneyim filtresinde gösterilir
}


FOOD_DRINK_FAMILIES = {"Yeme-İçme", "Kafe", "Bar"}

# Yiyecek-içecek mekanları için ÇOK SIKI - sadece şunlar düzeltilebilir
# Park/Garden/Tower/Temple gibi kelimeler restoran isimlerinde geçtiği için riskli
FOOD_OVERRIDE_ALLOWED = {
    "Deneyim",      # Cinema, Theater, Stadium - kesin yiyecek değil
    "Müze",         # Museum - kesin yiyecek değil
    "Akvaryum",
    "Bilim",        # Planetarium
    "Sağlık", "Eğitim", "Ulaşım",
    # Liman, Galeri, Plaj çıkarıldı: "Marina X Restaurant", "Galeri Cafe", "Beach Club" gibi
    # yanlış pozitifler oluyordu
}


def detect_category_for_fix(name: str, current: str) -> str | None:
    """
    İsimden gerçek kategoriyi tespit et.
    Eğer isim mevcut kategoriyi de destekliyorsa None döner (dokunma).
    Sadece yüksek güven kategorilerinde düzeltme önerir.
    """
    matches = all_matching_categories(name)
    if not matches:
        return None
    
    cur_family = CATEGORY_TO_FAMILY.get(current, current)
    
    # 🛡️ Eğer isim mevcut kategoriyi destekleyen bir kelime içeriyorsa, dokunma
    # Örn: "Hotel X Restaurant" - "Hotel" Otel'i, "Restaurant" Restoran'ı destekler
    # Mevcut "Restoran" ise zaten doğru, dokunma
    for m in matches:
        if CATEGORY_TO_FAMILY.get(m, m) == cur_family:
            return None
    
    # 🛡️ Yiyecek-içecek mekanları için EKSTRA SIKI filtre
    # "Le Jardin" (restoran adı), "Burger Turm" gibi yanlış pozitifleri engelle
    if cur_family in FOOD_DRINK_FAMILIES:
        for m in matches:
            if m in FOOD_OVERRIDE_ALLOWED:
                sug_family = CATEGORY_TO_FAMILY.get(m, m)
                if sug_family != cur_family:
                    return m
        return None  # Yiyecek-içecek için diğer kategorilere dokunma
    
    # En spesifik (yüksek güven) eşleşmeyi seç
    for m in matches:
        if m in HIGH_CONFIDENCE_CATEGORIES:
            # Aile farklı mı emin ol
            sug_family = CATEGORY_TO_FAMILY.get(m, m)
            if sug_family != cur_family:
                return m
    
    return None


def main():
    fix_mode = "--fix" in sys.argv
    
    mismatches = []
    by_city = defaultdict(list)
    by_change = defaultdict(int)
    total_places = 0
    
    json_files = sorted(CITIES_DIR.glob("*.json"))
    
    for json_file in json_files:
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"⚠️  {json_file.name}: parse error - {e}")
            continue
        
        # Hem dict (city.highlights) hem list (sadece highlights array) formatını destekle
        if isinstance(data, list):
            highlights = data
        else:
            highlights = data.get("highlights", [])
        modified = False
        
        for h in highlights:
            total_places += 1
            name = h.get("name", "")
            current = h.get("category", "")
            
            suggested = detect_category_for_fix(name, current)
            if not suggested:
                continue
            
            if True:  # detect_category_for_fix already filtered
                mismatches.append({
                    "file": json_file.name,
                    "name": name,
                    "current": current,
                    "suggested": suggested,
                })
                by_city[json_file.name].append((name, current, suggested))
                by_change[f"{current} → {suggested}"] += 1
                
                if fix_mode:
                    h["category"] = suggested
                    modified = True
        
        if fix_mode and modified:
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
    
    # Rapor
    print(f"\n{'=' * 70}")
    print(f"KATEGORI AUDIT RAPORU")
    print(f"{'=' * 70}")
    print(f"Toplam mekan: {total_places}")
    print(f"Tutarsızlık: {len(mismatches)} ({len(mismatches)*100/max(total_places,1):.1f}%)")
    print(f"Etkilenen şehir: {len(by_city)}")
    
    print(f"\n{'─' * 70}")
    print(f"EN YAYGIN DEĞİŞİKLİKLER (üstten 20):")
    print(f"{'─' * 70}")
    for change, count in sorted(by_change.items(), key=lambda x: -x[1])[:20]:
        print(f"  {count:>4}× {change}")
    
    print(f"\n{'─' * 70}")
    print(f"ŞEHİR BAZLI ÖRNEKLERİ (her şehirden 3 mekan):")
    print(f"{'─' * 70}")
    for city, items in sorted(by_city.items()):
        print(f"\n📍 {city} ({len(items)} mekan)")
        for name, cur, sug in items[:3]:
            print(f"   • {name[:50]:<50}  [{cur}] → [{sug}]")
        if len(items) > 3:
            print(f"   ... ve {len(items)-3} mekan daha")
    
    if fix_mode:
        print(f"\n✅ {len(mismatches)} mekan düzeltildi.")
    else:
        print(f"\n💡 Düzeltmek için: python {sys.argv[0]} --fix")


if __name__ == "__main__":
    main()
