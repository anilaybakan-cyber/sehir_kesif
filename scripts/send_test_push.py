#!/usr/bin/env python3
"""
Test FCM push gönderici.

Cihazın FCM token'ını uygulamadan kopyaladıktan sonra çalıştır:

    # Berlin rehberi push (varsayılan)
    python3 scripts/send_test_push.py --token "<FCM_TOKEN>"

    # Başka bir route
    python3 scripts/send_test_push.py --token "<TOKEN>" \
        --route /detail-by-id --city-id istanbul --place "Galata Kulesi"

    # Sadece data payload (notification body olmadan, foreground'da görünmez)
    python3 scripts/send_test_push.py --token "<TOKEN>" --silent

Önerilen workflow:
1. Uygulamayı çalıştır → log'larda `🔔 FCM Token: ...` çıkar
2. Token'ı kopyala
3. Burayı çalıştır

Not: Token kullanıcıya değil cihaza özel; uygulamayı silip kurarsan token değişir.
"""
from __future__ import annotations

import argparse
import socket
import sys
from pathlib import Path

import requests
import firebase_admin
from firebase_admin import credentials, messaging

# --- ISP DNS poisoning workaround (Cloudflare DoH) -----------------------------
_DOH_HOSTS = {
    "fcm.googleapis.com",
    "iid.googleapis.com",
    "oauth2.googleapis.com",
    "www.googleapis.com",
    "firebaseappcheck.googleapis.com",
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
        ips = [a["data"] for a in data.get("Answer", []) if a.get("type") == 1]
        if ips:
            _doh_cache[hostname] = ips
        return ips
    except Exception:
        return []


_orig_getaddrinfo = socket.getaddrinfo


def _patched(host, port, *args, **kwargs):
    if host in _DOH_HOSTS:
        ips = _resolve_via_doh(host)
        if ips:
            return [
                (socket.AF_INET, socket.SOCK_STREAM, 6, "", (ip, port))
                for ip in ips
            ]
    return _orig_getaddrinfo(host, port, *args, **kwargs)


socket.getaddrinfo = _patched


SERVICE_ACCOUNT = Path(__file__).resolve().parent.parent / "service_account.json"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--token", required=True, help="Cihazın FCM token'ı")
    p.add_argument("--route", default="/guide", help="App rotası (default: /guide)")
    p.add_argument("--city-id", default="berlin", help="cityId (default: berlin)")
    p.add_argument("--place", default=None, help="placeName (sadece /detail-by-id için)")
    p.add_argument("--tab", default=None, help="tab indeksi (sadece /main için)")
    p.add_argument(
        "--routes-tab",
        dest="routes_tab",
        default=None,
        help="Rotalar iç tab indeksi: 0=Hazır Rotalar, 1=Rotam, 2=Listem",
    )
    p.add_argument(
        "--profile-tab",
        dest="profile_tab",
        default=None,
        help="Profil iç tab indeksi: 0=Favoriler, 1=Ziyaret, 2=Rotalar",
    )
    p.add_argument(
        "--profile-action",
        dest="profile_action",
        default=None,
        help="Profil aksiyonu: add-memory | preferences | memories",
    )
    p.add_argument("--title", default=None, help="Bildirim başlığı")
    p.add_argument("--body", default=None, help="Bildirim metni")
    p.add_argument(
        "--silent",
        action="store_true",
        help="Notification olmadan sadece data payload (foreground'da görünmez)",
    )
    args = p.parse_args()

    if not SERVICE_ACCOUNT.exists():
        print(f"FATAL: {SERVICE_ACCOUNT} bulunamadı.")
        return 1

    if not firebase_admin._apps:
        firebase_admin.initialize_app(credentials.Certificate(str(SERVICE_ACCOUNT)))

    # Default başlık/body içerik route'a göre
    default_titles = {
        "/guide": ("MyWay Rehber", f"{args.city_id.title()} rehberini incele"),
        "/detail-by-id": ("MyWay", f"{args.place or args.city_id} sayfasını aç"),
        "/main": ("MyWay", "Ana ekrana dön"),
        "/paywall": ("MyWay Premium", "Premium'u keşfet"),
        "/city-switch": ("MyWay", "Şehir değiştir"),
    }
    default_title, default_body = default_titles.get(args.route, ("MyWay", "Aç"))
    title = args.title or default_title
    body = args.body or default_body

    data: dict[str, str] = {"route": args.route}
    if args.city_id:
        data["cityId"] = args.city_id
    if args.place:
        data["placeName"] = args.place
    if args.tab is not None:
        data["tab"] = str(args.tab)
    if args.routes_tab is not None:
        data["routesTab"] = str(args.routes_tab)
    if args.profile_tab is not None:
        data["profileTab"] = str(args.profile_tab)
    if args.profile_action is not None:
        data["profileAction"] = str(args.profile_action)

    notification = None if args.silent else messaging.Notification(title=title, body=body)

    msg = messaging.Message(
        token=args.token,
        notification=notification,
        data=data,
        android=messaging.AndroidConfig(priority="high"),
        apns=messaging.APNSConfig(
            headers={"apns-priority": "10"},
            payload=messaging.APNSPayload(
                aps=messaging.Aps(
                    alert=None if args.silent else messaging.ApsAlert(title=title, body=body),
                    sound="default",
                    content_available=True,
                ),
            ),
        ),
    )

    try:
        message_id = messaging.send(msg)
    except Exception as exc:
        print(f"❌ FCM gönderim hatası: {exc}")
        return 2

    print("✅ Push gönderildi")
    print(f"   message_id : {message_id}")
    print(f"   route      : {args.route}")
    print(f"   data       : {data}")
    if notification:
        print(f"   title/body : {title!r} / {body!r}")
    else:
        print("   (silent — sadece data payload)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
