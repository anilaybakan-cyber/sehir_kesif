#!/usr/bin/env python3
"""Fill openHours for highlights using Google Place Details.

Usage:
  python3 scripts/fill_open_hours.py --city istanbul --limit 50
  python3 scripts/fill_open_hours.py --all --fix
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[1]
CITIES_DIR = ROOT / "assets" / "cities"
REPORT_PATH = ROOT / "open_hours_fill_report.json"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
FIND_PLACE_URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
ENV_PATH = ROOT / ".env"

DAY_KEYS = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]


def get_api_key() -> str:
    key = (
        os.environ.get("GOOGLE_MAPS_API_KEY", "")
        or os.environ.get("GOOGLE_PLACES_KEY", "")
    ).strip()
    if key:
        return key

    if ENV_PATH.exists():
        for line in ENV_PATH.read_text(encoding="utf-8").splitlines():
            raw = line.strip()
            if not raw or raw.startswith("#") or "=" not in raw:
                continue
            key_name, key_value = raw.split("=", 1)
            if key_name.strip() in {"GOOGLE_MAPS_API_KEY", "GOOGLE_PLACES_KEY"}:
                return key_value.strip().strip('"').strip("'")
    return ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill openHours from Google Place Details.")
    parser.add_argument("--city", type=str, default="", help="Single city id (e.g. istanbul).")
    parser.add_argument("--all", action="store_true", help="Run for all city files.")
    parser.add_argument("--fix", action="store_true", help="Write changes to JSON files.")
    parser.add_argument("--limit", type=int, default=0, help="Max places to process.")
    parser.add_argument("--sleep-ms", type=int, default=120, help="Delay between API calls.")
    parser.add_argument("--overwrite", action="store_true", help="Replace existing openHours.")
    parser.add_argument(
        "--resolve-missing-ids",
        action="store_true",
        help="Resolve missing/non-Google place ids using place name + city query.",
    )
    return parser.parse_args()


def city_files(args: argparse.Namespace) -> list[Path]:
    if args.city:
        path = CITIES_DIR / f"{args.city.lower().strip()}.json"
        return [path] if path.exists() else []
    if args.all:
        return sorted(CITIES_DIR.glob("*.json"))
    # Safe default: no-op unless city/all chosen explicitly
    return []


def normalize_time(raw: str) -> str:
    value = (raw or "").strip()
    if len(value) == 4 and value.isdigit():
        return f"{value[:2]}:{value[2:]}"
    return value


def periods_to_open_hours(periods: list[dict[str, Any]]) -> dict[str, str]:
    day_ranges: dict[str, list[tuple[int, int]]] = {k: [] for k in DAY_KEYS}

    for period in periods:
        open_info = period.get("open") or {}
        close_info = period.get("close") or {}
        open_day = open_info.get("day")
        open_time = normalize_time(open_info.get("time", ""))
        close_day = close_info.get("day")
        close_time = normalize_time(close_info.get("time", ""))

        if open_day is None or not open_time:
            continue

        # 24h-ish records can appear as 00:00 -> 00:00
        if close_day is not None and close_time == "00:00" and open_time == "00:00":
            day_ranges[DAY_KEYS[open_day]].append((0, 24 * 60))
            continue

        if close_day is None or not close_time:
            # If close not provided, keep a conservative same-day fallback.
            day_ranges[DAY_KEYS[open_day]].append((to_minutes(open_time), 24 * 60))
            continue

        open_minutes = to_minutes(open_time)
        close_minutes = to_minutes(close_time)

        if open_day == close_day:
            # Same day interval.
            day_ranges[DAY_KEYS[open_day]].append((open_minutes, close_minutes))
        else:
            # Cross-day interval, split safely.
            day_ranges[DAY_KEYS[open_day]].append((open_minutes, 24 * 60))
            day_ranges[DAY_KEYS[close_day]].append((0, close_minutes))

    result: dict[str, str] = {}
    for day_key, ranges in day_ranges.items():
        if not ranges:
            result[day_key] = "closed"
            continue
        merged = merge_ranges(ranges)
        result[day_key] = ", ".join(
            f"{from_minutes(start)}-{from_minutes(end if end < 24 * 60 else 0)}"
            if end < 24 * 60
            else f"{from_minutes(start)}-24:00"
            for start, end in merged
        )
    return result


def to_minutes(hhmm: str) -> int:
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def from_minutes(total: int) -> str:
    if total >= 24 * 60:
        return "24:00"
    hh = str(total // 60).zfill(2)
    mm = str(total % 60).zfill(2)
    return f"{hh}:{mm}"


def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not ranges:
        return []
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    merged = [sorted_ranges[0]]
    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def fetch_open_hours(api_key: str, place_id: str) -> tuple[dict[str, str] | None, str | None]:
    params = {
        "place_id": place_id,
        "key": api_key,
        "fields": "place_id,business_status,current_opening_hours,opening_hours",
    }
    try:
        response = requests.get(DETAILS_URL, params=params, timeout=20)
        payload = response.json()
    except Exception as exc:  # noqa: BLE001
        return None, f"request_exception:{exc}"

    status = payload.get("status")
    if status != "OK":
        return None, f"api_status:{status}"

    result = payload.get("result", {})
    opening = result.get("current_opening_hours") or result.get("opening_hours") or {}
    periods = opening.get("periods") or []
    if not periods:
        return None, "no_periods"

    mapped = periods_to_open_hours(periods)
    return mapped, None


def resolve_place_id(api_key: str, place_name: str, city_name: str) -> tuple[str | None, str | None]:
    query = f"{place_name}, {city_name}".strip(", ")
    params = {
        "input": query,
        "inputtype": "textquery",
        "fields": "place_id,name",
        "key": api_key,
    }
    try:
        response = requests.get(FIND_PLACE_URL, params=params, timeout=20)
        payload = response.json()
    except Exception as exc:  # noqa: BLE001
        return None, f"resolve_exception:{exc}"

    status = payload.get("status")
    if status not in {"OK", "ZERO_RESULTS"}:
        return None, f"resolve_status:{status}"

    candidates = payload.get("candidates") or []
    if not candidates:
        return None, "resolve_no_candidate"

    pid = candidates[0].get("place_id")
    if not pid:
        return None, "resolve_missing_place_id"
    return pid, None


def should_process_place(place: dict[str, Any], overwrite: bool) -> bool:
    place_id = str(place.get("id", ""))
    if not overwrite and place.get("openHours"):
        return False
    return True


def run(args: argparse.Namespace) -> None:
    api_key = get_api_key()
    if not api_key:
        raise SystemExit("Missing GOOGLE_MAPS_API_KEY or GOOGLE_PLACES_KEY")

    files = city_files(args)
    if not files:
        raise SystemExit("No city file selected. Use --city <id> or --all.")

    total_processed = 0
    total_updated = 0
    total_skipped = 0
    total_errors = 0
    resolved_ids = 0
    place_id_cache: dict[str, str] = {}
    report: dict[str, Any] = {"cities": {}}

    for city_file in files:
        try:
            data = json.loads(city_file.read_text(encoding="utf-8"))
        except Exception:
            continue

        is_list_format = isinstance(data, list)
        highlights = data if is_list_format else data.get("highlights", [])
        city_name = city_file.stem if is_list_format else str(data.get("city", city_file.stem))
        city_stats = {
            "processed": 0,
            "updated": 0,
            "skipped": 0,
            "errors": 0,
            "samples": [],
        }
        dirty = False

        for item in highlights:
            if args.limit and total_processed >= args.limit:
                break
            if not should_process_place(item, args.overwrite):
                city_stats["skipped"] += 1
                total_skipped += 1
                continue

            total_processed += 1
            city_stats["processed"] += 1
            place_id = str(item.get("id", ""))
            if not place_id.startswith("ChIJ"):
                if args.resolve_missing_ids:
                    cache_key = f"{item.get('name','')}|{city_name}"
                    if cache_key in place_id_cache:
                        place_id = place_id_cache[cache_key]
                    else:
                        resolved, resolve_err = resolve_place_id(
                            api_key,
                            str(item.get("name", "")),
                            city_name,
                        )
                        if resolve_err or not resolved:
                            city_stats["errors"] += 1
                            total_errors += 1
                            if len(city_stats["samples"]) < 6:
                                city_stats["samples"].append(
                                    {
                                        "name": item.get("name", ""),
                                        "place_id": place_id,
                                        "status": resolve_err or "resolve_failed",
                                    }
                                )
                            time.sleep(max(0, args.sleep_ms) / 1000)
                            continue
                        place_id = resolved
                        place_id_cache[cache_key] = resolved
                        resolved_ids += 1
                        if args.fix:
                            item["id"] = resolved
                else:
                    city_stats["skipped"] += 1
                    total_skipped += 1
                    continue

            open_hours, err = fetch_open_hours(api_key, place_id)
            if err:
                city_stats["errors"] += 1
                total_errors += 1
                if len(city_stats["samples"]) < 6:
                    city_stats["samples"].append(
                        {"name": item.get("name", ""), "place_id": place_id, "status": err}
                    )
            else:
                city_stats["updated"] += 1
                total_updated += 1
                if args.fix:
                    item["openHours"] = open_hours
                    dirty = True
                if len(city_stats["samples"]) < 6:
                    city_stats["samples"].append(
                        {"name": item.get("name", ""), "place_id": place_id, "status": "updated"}
                    )

            time.sleep(max(0, args.sleep_ms) / 1000)

        if args.fix and dirty:
            city_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

        report["cities"][city_file.stem] = city_stats
        if args.limit and total_processed >= args.limit:
            break

    report["summary"] = {
        "processed": total_processed,
        "updated": total_updated,
        "skipped": total_skipped,
        "errors": total_errors,
        "resolved_ids": resolved_ids,
        "mode": "fix" if args.fix else "dry-run",
        "overwrite": args.overwrite,
        "resolve_missing_ids": args.resolve_missing_ids,
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print(
        f"Done ({report['summary']['mode']}): "
        f"processed={total_processed} updated={total_updated} "
        f"skipped={total_skipped} errors={total_errors}"
    )
    print(f"Report: {REPORT_PATH}")


if __name__ == "__main__":
    run(parse_args())
