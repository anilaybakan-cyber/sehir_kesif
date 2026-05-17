#!/usr/bin/env python3
"""
Google Ads App kampanyalari icin goruntu boyutlandirma.

Girdi PNG/JPEG'leri "cover + merkez kirpma" ile su ciktilara donusturur:
  - 1200x1200 (1:1)
  - 1200x628  (1.91:1)
  - 1200x1500 (4:5)

Kullanim:
  pip3 install pillow
  python3 scripts/export_google_ads_images.py --input ~/Desktop/sehir_kesif_ads_raw

Cikti varsayilan: proje kokunde marketing/google_ads_export/
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow gerekli: pip3 install pillow", file=sys.stderr)
    sys.exit(1)

FORMATS: tuple[tuple[str, int, int], ...] = (
    ("1x1", 1200, 1200),
    ("1p91x1", 1200, 628),
    ("4x5", 1200, 1500),
)

EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def cover_center_crop_resize(im: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """Orijinal en-boy korunarak hedefi kaplar, fazlaligi merkezden kirpar."""
    im = im.convert("RGBA")
    src_w, src_h = im.size
    scale = max(target_w / src_w, target_h / src_h)
    new_w = max(1, int(round(src_w * scale)))
    new_h = max(1, int(round(src_h * scale)))
    im = im.resize((new_w, new_h), Image.Resampling.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return im.crop((left, top, left + target_w, top + target_h))


def export_one(src: Path, out_dir: Path, prefix: str) -> None:
    im = Image.open(src)
    stem = prefix or src.stem
    for suffix, w, h in FORMATS:
        cropped = cover_center_crop_resize(im, w, h)
        # Reklam aglari PNG/JPEG kabul eder; UI screenshot icin PNG daha temiz.
        dest = out_dir / f"{stem}_google_ads_{suffix}_{w}x{h}.png"
        cropped.save(dest, "PNG", optimize=True)


def collect_sources(input_path: Path) -> list[Path]:
    if input_path.is_file():
        return [input_path] if input_path.suffix.lower() in EXTENSIONS else []
    files = sorted(
        p for p in input_path.iterdir() if p.is_file() and p.suffix.lower() in EXTENSIONS
    )
    return files


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    default_out = root / "marketing" / "google_ads_export"

    parser = argparse.ArgumentParser(description="Google Ads icin goruntu boyutlari uretir.")
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Kaynak klasor veya tek dosya yolu (orn: ~/Desktop/sehir_kesif_ads_raw)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=default_out,
        help=f"Cikti klasoru (varsayilan: {default_out})",
    )
    args = parser.parse_args()

    inp = args.input.expanduser().resolve()
    out_dir = args.output.expanduser().resolve()

    if not inp.exists():
        print(f"Bulunamadi: {inp}", file=sys.stderr)
        sys.exit(1)

    sources = collect_sources(inp)
    if not sources:
        print(f"PNG/JPEG/WebP bulunamadi: {inp}", file=sys.stderr)
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    for i, src in enumerate(sources, start=1):
        prefix = f"{i:02d}_{src.stem}" if len(sources) > 1 else src.stem
        export_one(src, out_dir, prefix=prefix)
        print(src.name, "->", str(out_dir))

    print(f"\nTamam. Dosyalar: {out_dir}")


if __name__ == "__main__":
    main()
