#!/usr/bin/env python3
"""Check that the style evidence covers all reference paper groups."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_GROUPS = [str(i) for i in range(1, 9)]
REQUIRED_TERMS = [
    "tracking",
    "neural dynamics",
    "3D reconstruction",
    "SR microscopy",
    "intravital",
    "spatial",
    "Supplementary",
    "Extended Data",
    "palette",
    "QA",
]


def main() -> int:
    root = Path(".")
    files = [
        root / "references/source-paper-index.md",
        root / "references/figure-audit-register.md",
        root / "skills/nature-publication-figure/references/figure-style-atlas.md",
        root / "skills/nature-publication-figure/references/color-and-chart-rules.md",
        root / "skills/nature-publication-figure/references/qa-and-export.md",
    ]
    text = "\n".join(path.read_text(encoding="utf-8") for path in files)
    errors = []
    for group in REQUIRED_GROUPS:
        if f"| {group} " not in text and f"组 {group}" not in text:
            errors.append(f"Missing figure style coverage for group {group}")
    for term in REQUIRED_TERMS:
        if term not in text:
            errors.append(f"Missing required style term: {term}")
    if errors:
        print("Style coverage check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Style coverage check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
