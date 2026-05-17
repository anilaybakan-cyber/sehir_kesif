#!/usr/bin/env python3
"""Content quality gate for city highlight texts.

Usage:
  python3 scripts/content_quality_gate.py
  python3 scripts/content_quality_gate.py --all
  python3 scripts/content_quality_gate.py --cities istanbul,barcelona,paris
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CITY_DIR = ROOT / "assets" / "cities"
OUTPUT_PATH = ROOT / "quality_gate_report.json"

PILOT_CITIES = [
    "istanbul",
    "barcelona",
    "paris",
    "roma",
    "londra",
    "amsterdam",
    "madrid",
    "venedik",
    "berlin",
    "nice",
]

GENERIC_PATTERNS = [
    "must-see",
    "top spot",
    "worth visiting",
    "great choice",
    "perfect for your trip",
    "mutlaka görmeniz gereken",
    "harika bir yer",
    "kesinlikle görülmeli",
]


def word_count(value: str) -> int:
    if not value:
        return 0
    return len(re.findall(r"\w+", value, re.UNICODE))


def norm_text(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip().lower())


def contains_generic_pattern(value: str) -> bool:
    lowered = norm_text(value)
    return any(pattern in lowered for pattern in GENERIC_PATTERNS)


def quality_score(metrics: dict[str, int], total_highlights: int) -> float:
    if total_highlights <= 0:
        return 0.0
    # Penalty model: lower is better, capped at 100.
    penalties = (
        metrics["missing_tips_en"] * 1.2
        + metrics["short_tr_desc"] * 0.7
        + metrics["short_en_desc"] * 0.8
        + metrics["generic_tr_desc"] * 1.0
        + metrics["generic_en_desc"] * 1.1
        + metrics["repeated_tips"] * 0.6
    )
    normalized = max(0.0, 100.0 - (penalties / total_highlights) * 20.0)
    return round(normalized, 2)


def analyze_city(city_id: str, min_words: int) -> dict[str, Any]:
    city_path = CITY_DIR / f"{city_id}.json"
    if not city_path.exists():
        return {
            "city_id": city_id,
            "error": "city_file_not_found",
        }

    data = json.loads(city_path.read_text(encoding="utf-8"))
    highlights = data.get("highlights", [])
    total = len(highlights)

    metrics = {
        "missing_tips_en": 0,
        "short_tr_desc": 0,
        "short_en_desc": 0,
        "generic_tr_desc": 0,
        "generic_en_desc": 0,
        "repeated_tips": 0,
    }
    examples: dict[str, list[dict[str, str]]] = {
        "missing_tips_en": [],
        "short_tr_desc": [],
        "short_en_desc": [],
        "generic_desc": [],
        "repeated_tips": [],
    }

    tips_counter: Counter[str] = Counter()
    for item in highlights:
        name = item.get("name", "")
        tr_desc = item.get("description", "") or ""
        en_desc = item.get("description_en", "") or ""
        tips_en = item.get("tips_en", "") or ""
        tips_tr = item.get("tips", "") or ""

        if not tips_en.strip():
            metrics["missing_tips_en"] += 1
            if len(examples["missing_tips_en"]) < 6:
                examples["missing_tips_en"].append({"name": name})

        if word_count(tr_desc) < min_words:
            metrics["short_tr_desc"] += 1
            if len(examples["short_tr_desc"]) < 6:
                examples["short_tr_desc"].append({"name": name, "text": tr_desc})

        if word_count(en_desc) < min_words:
            metrics["short_en_desc"] += 1
            if len(examples["short_en_desc"]) < 6:
                examples["short_en_desc"].append({"name": name, "text": en_desc})

        tr_generic = contains_generic_pattern(tr_desc)
        en_generic = contains_generic_pattern(en_desc)
        if tr_generic:
            metrics["generic_tr_desc"] += 1
        if en_generic:
            metrics["generic_en_desc"] += 1
        if (tr_generic or en_generic) and len(examples["generic_desc"]) < 6:
            examples["generic_desc"].append({"name": name, "tr": tr_desc, "en": en_desc})

        tip_signal = norm_text(tips_en) or norm_text(tips_tr)
        if tip_signal:
            tips_counter[tip_signal] += 1

    repeated = [(tip, count) for tip, count in tips_counter.items() if count >= 3]
    metrics["repeated_tips"] = sum(count for _, count in repeated)
    for tip, count in repeated[:6]:
        examples["repeated_tips"].append({"tip": tip, "count": str(count)})

    score = quality_score(metrics, total)
    status = "pass" if score >= 80 else "warn" if score >= 65 else "fail"

    return {
        "city_id": city_id,
        "city_name": data.get("city", city_id),
        "total_highlights": total,
        "score": score,
        "status": status,
        "metrics": metrics,
        "examples": examples,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run content quality checks for city files.")
    parser.add_argument("--all", action="store_true", help="Run on all city JSON files.")
    parser.add_argument(
        "--cities",
        type=str,
        default="",
        help="Comma-separated city ids (e.g. istanbul,paris).",
    )
    parser.add_argument(
        "--min-words",
        type=int,
        default=20,
        help="Minimum word count for description and description_en.",
    )
    return parser.parse_args()


def selected_cities(args: argparse.Namespace) -> list[str]:
    if args.cities:
        return [c.strip().lower() for c in args.cities.split(",") if c.strip()]
    if args.all:
        return sorted(p.stem for p in CITY_DIR.glob("*.json"))
    return PILOT_CITIES


def main() -> None:
    args = parse_args()
    cities = selected_cities(args)
    results = [analyze_city(city_id, args.min_words) for city_id in cities]

    valid_results = [r for r in results if "error" not in r]
    avg_score = round(
        sum(r["score"] for r in valid_results) / max(1, len(valid_results)),
        2,
    )
    summary = {
        "city_count": len(results),
        "analyzed_city_count": len(valid_results),
        "avg_score": avg_score,
        "pass_count": sum(1 for r in valid_results if r["status"] == "pass"),
        "warn_count": sum(1 for r in valid_results if r["status"] == "warn"),
        "fail_count": sum(1 for r in valid_results if r["status"] == "fail"),
    }

    payload = {
        "summary": summary,
        "cities": results,
        "config": {
            "pilot_cities": PILOT_CITIES,
            "min_words": args.min_words,
            "generic_patterns": GENERIC_PATTERNS,
        },
    }
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Quality gate completed for {summary['analyzed_city_count']} cities.")
    print(
        f"Average score: {summary['avg_score']} | "
        f"pass={summary['pass_count']} warn={summary['warn_count']} fail={summary['fail_count']}"
    )
    print(f"Report: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
