#!/usr/bin/env python3
"""Build a page-level figure marker inventory for reference PDFs."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

import fitz


PATTERNS = [
    ("main_fig", re.compile(r"(?im)^\s*(Fig(?:ure)?\.?\s*\d+[a-z]?)\b")),
    ("extended_data", re.compile(r"(?im)^\s*(Extended Data Fig\.?\s*\d+[a-z]?)\b")),
    ("supp_fig", re.compile(r"(?im)^\s*(Supplementary Fig(?:ure)?\.?\s*\d+[a-z]?)\b")),
    ("table", re.compile(r"(?im)^\s*((?:Supplementary\s+)?Table\s*\d+)\b")),
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def inspect_pdf(path: Path) -> dict:
    doc = fitz.open(path)
    pages = []
    for index, page in enumerate(doc, start=1):
        text = page.get_text("text")
        markers = []
        for kind, pattern in PATTERNS:
            for match in pattern.finditer(text):
                start = max(0, match.start() - 80)
                end = min(len(text), match.end() + 280)
                snippet = " ".join(text[start:end].split())
                markers.append(
                    {
                        "kind": kind,
                        "label": match.group(1).replace("\n", " ").strip(),
                        "snippet": snippet,
                    }
                )
        pages.append(
            {
                "page": index,
                "image_xrefs": len(page.get_images(full=True)),
                "vector_drawings": len(page.get_drawings()),
                "markers": markers,
            }
        )
    return {
        "source_pdf": str(path),
        "sha256": sha256(path),
        "pages": len(doc),
        "title": doc.metadata.get("title") or "",
        "pages_info": pages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a figure marker inventory from PDFs.")
    parser.add_argument("input", type=Path, help="PDF file or directory containing PDFs")
    parser.add_argument("--output", type=Path, default=Path(".audit/pdf_figure_inventory.json"))
    args = parser.parse_args()

    if args.input.is_file():
        pdfs = [args.input]
    else:
        pdfs = sorted(args.input.glob("*/*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found under {args.input}")

    records = [inspect_pdf(path) for path in pdfs]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(records)} PDF records to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
