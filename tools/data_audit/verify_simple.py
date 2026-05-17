#!/usr/bin/env python3
"""
Hızlı Gemini doğrulama - requests kütüphanesi ile.
"""

import json
import os
import time
import requests
from pathlib import Path

ROOT = Path("/Users/anilebru/Desktop/Uygulamalar/sehir_kesif")
CITIES_DIR = ROOT / "assets" / "cities"
CACHE_PATH = ROOT / "tools" / "data_audit" / "gemini_verdicts.json"

# .env yükle
env_file = ROOT / ".env"
if env_file.exists():
    with open(env_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip()

API_KEY = os.getenv("GEMINI_API_KEY")
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

def load_cache():
    if CACHE_PATH.exists():
        return json.load(open(CACHE_PATH))
    return {}

def save_cache(cache):
    with open(CACHE_PATH, "w") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def load_places():
    places = []
    for f in sorted(CITIES_DIR.glob("*.json")):
        raw = json.load(open(f))
        plist = raw if isinstance(raw, list) else raw.get("highlights", [])
        for p in plist:
            if isinstance(p, dict) and p.get("id"):
                places.append({
                    "id": p["id"],
                    "name": p.get("name", ""),
                    "city": f.stem,
                    "category": p.get("category", ""),
                    "description": p.get("description", "")[:300],
                })
    return places

def verify_batch(places):
    prompt = f"""Aşağıdaki mekanlar için verdict ver (ok/mismatch/wrong_city/uncertain):
{json.dumps(places, ensure_ascii=False)}
JSON array döndür."""
    
    try:
        resp = requests.post(
            f"{API_URL}?key={API_KEY}",
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=60
        )
        resp.raise_for_status()
        text = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
        # JSON parse
        if text.startswith("```"):
            text = text.strip("`").replace("json", "").strip()
        return json.loads(text)
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None

def main():
    cache = load_cache()
    all_places = load_places()
    pending = [p for p in all_places if p["id"] not in cache]
    
    print(f"📦 Total: {len(all_places)}, Cache: {len(cache)}, Pending: {len(pending)}")
    
    batch_size = 10
    rpm = 15
    gap = 60 / rpm
    
    for i in range(0, len(pending), batch_size):
        batch = pending[i:i+batch_size]
        print(f"\n[{i//batch_size + 1}/{(len(pending)-1)//batch_size + 1}] Processing {len(batch)} places")
        
        results = verify_batch(batch)
        if results:
            for r in results:
                pid = r.get("id")
                if pid:
                    # Find matching place in batch
                    place = next((p for p in batch if p["id"] == pid), None)
                    if place:
                        cache[pid] = {
                            "verdict": r.get("verdict", "uncertain"),
                            "reason": r.get("reason", ""),
                            "name": place.get("name", ""),
                            "city": place.get("city", ""),
                            "category": place.get("category", ""),
                        }
            save_cache(cache)
            
            mm = sum(1 for v in cache.values() if v["verdict"] == "mismatch")
            wc = sum(1 for v in cache.values() if v["verdict"] == "wrong_city")
            print(f"  ✅ Cache: {len(cache)}, mismatch: {mm}, wrong_city: {wc}")
        else:
            print(f"  ⚠️  Batch failed, retrying...")
            time.sleep(5)
            i -= batch_size  # Retry
            continue
        
        time.sleep(gap)
    
    print(f"\n✅ Done! Total: {len(cache)}")

if __name__ == "__main__":
    main()
