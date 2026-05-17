"""
H1 auto-fix — Ad tip kelimesiyle BAŞLIYOR ama kategori uyumsuz.

Her H1 kaydının kategorisini, ismin prefix'ine göre deterministik olarak
günceller ve ilgili city JSON'a yazar.

Kullanım:
  python3 tools/data_audit/apply_h1_fix.py             # dry-run (sadece göster)
  python3 tools/data_audit/apply_h1_fix.py --apply     # yaz

--apply kullanılırken her dosyanın bir .bak yedeği alınır.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CITIES_DIR = ROOT / "assets" / "cities"

# Prefix → hedef kategori
# Sıra önemli: önce SPESİFİK eşleşmeler (iki kelimeli), sonra tekil kelimeler.
PREFIX_RULES: list[tuple[re.Pattern, str]] = [
    # --- Bar'a giden prefixler
    (re.compile(r"^\s*(cocktail\s+bar|wine\s+bar|gastro\s*bar|gastrobar)\b", re.I), "Bar"),
    (re.compile(r"^\s*(bar|pub|taberna|tavern|taproom|cervecería|cerveceria|cervezería|cervezeria|enoteca|vinoteca|winery|brewery|vermutería|vermuteria|coctelería|cocteleria|bodega)\b", re.I), "Bar"),

    # --- Kafe'ye giden prefixler
    (re.compile(r"^\s*(coffee\s+shop|coffee\s+house|ice\s+cream)\b", re.I), "Kafe"),
    (re.compile(r"^\s*(café|cafe|caffè|caffe|cafetería|cafeteria|pastelería|pasteleria|pasticceria|gelateria|heladería|heladeria|bakery|roastery|churrería|churreria|chocolatería|chocolateria|focacceria|paninoteca)\b", re.I), "Kafe"),

    # --- Restoran'a giden prefixler
    (re.compile(r"^\s*(restaurante|ristorante|trattoria|osteria|pizzeria|bistro|bistrot|brasserie|mesón|meson|asador|tapería|taperia|tavola)\b", re.I), "Restoran"),
]


def target_category(name: str) -> str | None:
    for pat, cat in PREFIX_RULES:
        if pat.search(name):
            return cat
    return None


# Hangi kategoriler yeme-içme kabul edilir (önceden doğru ise dokunma)
FOOD_CATS = {"Yeme-İçme", "Kafe", "Bar", "Restoran"}


def process_city(path: Path, apply: bool) -> tuple[int, list[dict]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    places = raw if isinstance(raw, list) else raw.get("highlights", [])
    if not isinstance(places, list):
        return 0, []

    changes: list[dict] = []
    modified = False

    for p in places:
        if not isinstance(p, dict):
            continue
        name = (p.get("name") or "").strip()
        cat = (p.get("category") or "").strip()
        target = target_category(name)
        if target is None:
            continue
        # Eğer zaten uygun bir yeme-içme kategorisi ise dokunma
        if cat in FOOD_CATS:
            continue
        changes.append({
            "id": p.get("id") or "",
            "name": name,
            "old_category": cat or "(boş)",
            "new_category": target,
        })
        if apply:
            p["category"] = target
            modified = True

    if apply and modified:
        # Yedek al
        bak = path.with_suffix(path.suffix + ".bak")
        if not bak.exists():
            shutil.copy2(path, bak)
        path.write_text(
            json.dumps(raw, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    return len(changes), changes


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="değişiklikleri yaz")
    args = ap.parse_args()

    files = sorted(CITIES_DIR.glob("*.json"))
    total = 0
    total_changes: list[dict] = []

    for f in files:
        try:
            n, changes = process_city(f, args.apply)
        except Exception as e:  # noqa: BLE001
            print(f"⚠️  {f.name}: {e}", file=sys.stderr)
            continue
        if n == 0:
            continue
        total += n
        for c in changes:
            c["city"] = f.stem
            total_changes.append(c)
        for c in changes:
            print(f"  {f.stem:20s} | {c['old_category']:10s} → {c['new_category']:10s} | {c['name']}")

    print()
    print(f"Toplam {total} kayıt")
    if args.apply:
        print("✅ Değişiklikler uygulandı. Her değiştirilen dosyanın .bak yedeği alındı.")
    else:
        print("ℹ️  Dry-run. Uygulamak için: --apply")


if __name__ == "__main__":
    main()
