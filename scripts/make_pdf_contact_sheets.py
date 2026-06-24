#!/usr/bin/env python3
"""Render PDF pages into compact visual contact sheets for audit."""

from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

import fitz
from PIL import Image, ImageDraw, ImageFont


MARKER_RE = re.compile(
    r"(?im)^\s*((?:Extended Data\s+)?Fig(?:ure)?\.?\s*\d+[a-z]?|Supplementary Fig(?:ure)?\.?\s*\d+[a-z]?|(?:Supplementary\s+)?Table\s*\d+)\b"
)


def render_contact_sheet(pdf: Path, output_dir: Path, scale: float, columns: int) -> Path:
    doc = fitz.open(pdf)
    thumbs = []
    font = ImageFont.load_default()
    for index, page in enumerate(doc, start=1):
        text = page.get_text("text")
        markers = sorted({m.group(1).replace("\n", " ").strip() for m in MARKER_RE.finditer(text)})
        pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
        page_image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        label_h = 26
        thumb = Image.new("RGB", (page_image.width, page_image.height + label_h), "white")
        thumb.paste(page_image, (0, label_h))
        draw = ImageDraw.Draw(thumb)
        header = f"p{index} img={len(page.get_images(full=True))} vec={len(page.get_drawings())}"
        if markers:
            header += " | " + ", ".join(markers)[:90]
        draw.rectangle([0, 0, thumb.width, label_h], fill=(245, 245, 245))
        draw.text((4, 4), header, fill=(0, 0, 0), font=font)
        thumbs.append(thumb)

    cell_w = max(t.width for t in thumbs)
    cell_h = max(t.height for t in thumbs)
    rows = math.ceil(len(thumbs) / columns)
    sheet = Image.new("RGB", (columns * cell_w, rows * cell_h), "white")
    for idx, thumb in enumerate(thumbs):
        x = (idx % columns) * cell_w
        y = (idx // columns) * cell_h
        sheet.paste(thumb, (x, y))

    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{pdf.parent.name}-{pdf.stem}.jpg"
    sheet.save(out, quality=84, optimize=True)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Create PDF page contact sheets.")
    parser.add_argument("input", type=Path, help="PDF file or directory containing PDFs")
    parser.add_argument("--output-dir", type=Path, default=Path(".audit/pdf-page-sheets"))
    parser.add_argument("--scale", type=float, default=0.32)
    parser.add_argument("--columns", type=int, default=4)
    args = parser.parse_args()

    if args.input.is_file():
        pdfs = [args.input]
    else:
        pdfs = sorted(args.input.glob("*/*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found under {args.input}")

    for pdf in pdfs:
        out = render_contact_sheet(pdf, args.output_dir, args.scale, args.columns)
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
