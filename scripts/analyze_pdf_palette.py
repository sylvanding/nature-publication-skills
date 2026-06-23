#!/usr/bin/env python3
"""Estimate dominant non-neutral colors from rendered PDF pages."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

import fitz
from PIL import Image


def is_neutral(rgb: tuple[int, int, int]) -> bool:
    r, g, b = rgb
    if max(rgb) > 238 or min(rgb) < 18:
        return True
    return max(rgb) - min(rgb) < 18


def bin_rgb(rgb: tuple[int, int, int], step: int = 24) -> tuple[int, int, int]:
    return tuple(int(round(channel / step) * step) for channel in rgb)


def hex_color(rgb: tuple[int, int, int]) -> str:
    r, g, b = (max(0, min(255, value)) for value in rgb)
    return f"#{r:02X}{g:02X}{b:02X}"


def page_palette(page, scale: float, max_size: int) -> Counter:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    image.thumbnail((max_size, max_size))
    counts: Counter = Counter()
    pixel_iter = image.get_flattened_data() if hasattr(image, "get_flattened_data") else image.getdata()
    for rgb in pixel_iter:
        if not is_neutral(rgb):
            counts[bin_rgb(rgb)] += 1
    return counts


def inspect_pdf(path: Path, scale: float, max_size: int, top_n: int) -> dict:
    doc = fitz.open(path)
    counts: Counter = Counter()
    for page in doc:
        counts.update(page_palette(page, scale, max_size))
    total = sum(counts.values())
    palette = [
        {"hex": hex_color(rgb), "pixels": count, "fraction": round(count / total, 4) if total else 0}
        for rgb, count in counts.most_common(top_n)
    ]
    return {"source_pdf": str(path), "pages": len(doc), "sampled_pixels": total, "palette": palette}


def main() -> int:
    parser = argparse.ArgumentParser(description="Estimate dominant non-neutral colors from PDFs.")
    parser.add_argument("input", type=Path, help="PDF file or directory containing PDFs")
    parser.add_argument("--output", type=Path, default=Path(".audit/pdf_palette_summary.json"))
    parser.add_argument("--scale", type=float, default=0.18)
    parser.add_argument("--max-size", type=int, default=420)
    parser.add_argument("--top-n", type=int, default=12)
    args = parser.parse_args()

    if args.input.is_file():
        pdfs = [args.input]
    else:
        pdfs = sorted(args.input.glob("*/*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found under {args.input}")

    records = [inspect_pdf(pdf, args.scale, args.max_size, args.top_n) for pdf in pdfs]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"Wrote palette summaries for {len(records)} PDFs to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
