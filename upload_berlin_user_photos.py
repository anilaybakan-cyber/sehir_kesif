#!/usr/bin/env python3
"""
Upload kullanıcının verdiği Berlin fotoğraflarını Firebase'e indirir,
hem assets/cities/berlin.json hem de ota_data_pack/cities/berlin.json içindeki
imageUrl alanlarını günceller.
"""
import json
import os
import re
import socket
import ssl
import sys
import time
from pathlib import Path

import requests

import firebase_admin
from firebase_admin import credentials, storage

# --- ISP DNS poisoning workaround (Cloudflare DoH) -----------------------------
# Bazı ISP'ler storage.googleapis.com gibi domainleri sinkhole'a yönlendirebiliyor.
# Sadece riskli hostlar için Cloudflare DoH ile gerçek IP'yi çözüyoruz.
_DOH_HOSTS = {
    "storage.googleapis.com",
    "firebasestorage.googleapis.com",
}
_doh_cache: dict[str, list[str]] = {}


def _resolve_via_doh(hostname: str) -> list[str]:
    if hostname in _doh_cache:
        return _doh_cache[hostname]
    try:
        r = requests.get(
            "https://cloudflare-dns.com/dns-query",
            params={"name": hostname, "type": "A"},
            headers={"accept": "application/dns-json"},
            timeout=8,
        )
        r.raise_for_status()
        data = r.json()
        ips = [ans["data"] for ans in data.get("Answer", []) if ans.get("type") == 1]
        if ips:
            _doh_cache[hostname] = ips
            print(f"  [DoH] {hostname} -> {ips[:3]}")
            return ips
    except Exception as exc:
        print(f"  [DoH] resolve failed for {hostname}: {exc}")
    return []


_orig_getaddrinfo = socket.getaddrinfo


def _patched_getaddrinfo(host, port, *args, **kwargs):
    if host in _DOH_HOSTS:
        ips = _resolve_via_doh(host)
        if ips:
            results = []
            for ip in ips:
                results.append((socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, port)))
            return results
    return _orig_getaddrinfo(host, port, *args, **kwargs)


socket.getaddrinfo = _patched_getaddrinfo

# --- Firebase config -----------------------------------------------------------
SERVICE_ACCOUNT_FILE = "service_account.json"
BUCKET_NAME = "myway-3fe75.firebasestorage.app"
DOWNLOAD_DIR = Path("temp_berlin_photos")
ASSETS_JSON = Path("assets/cities/berlin.json")
OTA_JSON = Path("ota_data_pack/cities/berlin.json")

# --- (place name -> (firebase slug, source url)) ------------------------------
TASKS: list[tuple[str, str, str]] = [
    # display name (matches JSON "name" field), filename slug, source URL
    (
        "HKW Berlin",
        "hkw_berlin",
        "https://upload.wikimedia.org/wikipedia/commons/2/25/Haus_der_Kulturen_der_Welt%2C_Blaue_Stunde%2C_Berlin%2C_160521%2C_ako.jpg",
    ),
    (
        "Bernauer Strasse",
        "bernauer_strasse",
        "https://upload.wikimedia.org/wikipedia/commons/a/a8/Berlin_mauergedenkst%C3%A4tte_strasse_30.07.2012_16-13-07.jpg",
    ),
    (
        "Gleis 17",
        "gleis_17",
        "https://www.berlin.de/binaries/asset/image_assets/9389128/source/1735894597/1000x500/",
    ),
    (
        "Rykestrasse Synagogue",
        "rykestrasse_synagogue",
        "https://www.berlin.de/binaries/asset/image_assets/6426730/ratio_4_3/1738066889/800x600/",
    ),
    (
        "Otto Weidt's Workshop",
        "otto_weidts_workshop",
        "https://www.museum-blindenwerkstatt.de/mbow/Startseite/03_DSC03378_Engels_rgb.jpg",
    ),
    (
        "Altes Museum",
        "altes_museum",
        "https://upload.wikimedia.org/wikipedia/commons/f/f5/Altes_Museum_%28Berlin%29_%286339770591%29.jpg",
    ),
    (
        "James Simon Galeri",
        "james_simon_galeri",
        "https://www.smb.museum/fileadmin/website/Museen_und_Sammlungen/James-Simon-Galerie/Ueber_uns/JSG_Aussenansicht_01.jpg",
    ),
    (
        "Fotoautomat",
        "fotoautomat",
        "https://images.squarespace-cdn.com/content/v1/569e766e69492e9dd5373ef6/1493816818155-QTHHP1R7L2ZN59PCL0QK/all-automat_0007_020217_2875.NEF-web.jpg",
    ),
    (
        "Bergmannkiez",
        "bergmannkiez",
        "https://www.berlin.de/binaries/asset/image_assets/895823/ratio_4_3/1728467569/800x600/",
    ),
    (
        "Haus Schwarzenberg",
        "haus_schwarzenberg",
        "https://media.cntraveler.com/photos/5b9159695cd9e63755f74a13/master/pass/Hackesche-H%C3%B6fe-and-Haus-Schwarzenberg_2018_GettyImages-537087373.jpg",
    ),
    (
        "Arkonaplatz Flea Market",
        "arkonaplatz_flea_market",
        "https://www.berlin.de/binaries/asset/image_assets/7847012/ratio_4_3/1680603745/800x600/",
    ),
    (
        "Viktoriapark",
        "viktoriapark",
        "https://upload.wikimedia.org/wikipedia/commons/2/2d/Viktoriapark_B-Kreuzberg_06-2017_img1.jpg",
    ),
    (
        "Schillerkiez",
        "schillerkiez",
        "https://www.berlin.de/binaries/asset/image_assets/9352555/ratio_4_3/1756971030/800x600/",
    ),
    (
        "Tempodrom",
        "tempodrom",
        "https://www.tempodrom.de/site/assets/files/1038/tempodrom_0061.-700x435.jpg",
    ),
    (
        "Kastanienallee",
        "kastanienallee",
        "https://upload.wikimedia.org/wikipedia/commons/5/59/Kastanienallee_2024.jpg",
    ),
    (
        "Helmholtzplatz",
        "helmholtzplatz",
        "https://www.berlin-lese.de/index.php?rex_media_type=gallery_big&rex_media_file=helmholtzplatz_007.jpg",
    ),
    (
        "Hasenheide",
        "hasenheide",
        "https://www.berlin.de/binaries/asset/image_assets/2018520/ratio_4_3/1738594368/800x600/",
    ),
    (
        "Görlitzer Park",
        "gorlitzer_park",
        "https://www.berlin.de/binaries/asset/image_assets/3921349/ratio_4_3/1693827293/800x600/",
    ),
]


def download(url: str, dest: Path) -> bool:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Referer": "https://www.google.com/",
    }
    try:
        r = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        if r.status_code != 200 or len(r.content) < 2000:
            print(f"  ✗ download failed ({r.status_code}, {len(r.content)} bytes)")
            return False
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        print(f"  ✓ downloaded {len(r.content) // 1024} KB")
        return True
    except Exception as exc:
        print(f"  ✗ download error: {exc}")
        return False


def upload(local_path: Path, remote_path: str, bucket) -> str | None:
    try:
        blob = bucket.blob(remote_path)
        blob.upload_from_filename(str(local_path))
        blob.make_public()
        return f"https://storage.googleapis.com/{BUCKET_NAME}/{remote_path}"
    except Exception as exc:
        print(f"  ✗ upload error: {exc}")
        return None


def update_json(path: Path, place_name: str, new_url: str) -> bool:
    if not path.exists():
        return False
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    target = None
    for h in data.get("highlights", []):
        if h.get("name", "").strip().lower() == place_name.strip().lower():
            target = h
            break
    if target is None:
        return False
    target["imageUrl"] = new_url
    target["source"] = "firebase"
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return True


def main() -> int:
    if not firebase_admin._apps:
        cred = credentials.Certificate(SERVICE_ACCOUNT_FILE)
        firebase_admin.initialize_app(cred, {"storageBucket": BUCKET_NAME})
    bucket = storage.bucket()
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    # CLI ile alt küme: `python3 upload_berlin_user_photos.py "HKW Berlin"`
    only_names = {n.strip().lower() for n in sys.argv[1:]}
    tasks = [t for t in TASKS if not only_names or t[0].strip().lower() in only_names]

    success = 0
    failed = []

    for i, (name, slug, url) in enumerate(tasks, 1):
        print(f"\n[{i}/{len(tasks)}] {name}")
        local_path = DOWNLOAD_DIR / f"{slug}.jpg"
        remote_path = f"cities/berlin/{slug}.jpg"

        if not download(url, local_path):
            failed.append(name)
            continue

        public_url = upload(local_path, remote_path, bucket)
        if not public_url:
            failed.append(name)
            continue
        print(f"  ✓ uploaded -> {public_url}")

        updated_assets = update_json(ASSETS_JSON, name, public_url)
        updated_ota = update_json(OTA_JSON, name, public_url)
        print(
            f"  json updates: assets={'✓' if updated_assets else '–'} "
            f"ota={'✓' if updated_ota else '–'}"
        )
        if not (updated_assets or updated_ota):
            print(f"  ⚠ JSON eşleşmesi yok ({name})")
            failed.append(name)
            continue

        success += 1
        time.sleep(0.2)

    print("\n" + "=" * 40)
    print(f"DONE: success={success}/{len(tasks)}")
    if failed:
        print("Failed:")
        for n in failed:
            print(f"  - {n}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
