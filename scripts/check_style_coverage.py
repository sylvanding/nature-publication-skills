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
REQUIRED_RULE_MAP_TERMS = [
    "Main figures",
    "Extended Data",
    "Supplementary figures",
    "Tables",
    "Skill rule mapping",
    "Source evidence",
    "Coverage status",
    "method schematic",
    "dark microscopy plate",
    "statistical evidence block",
    "supplementary validation matrix",
    "spatial omics map",
    "input-output montage",
]


def main() -> int:
    root = Path(".")
    rule_map = root / "references/figure-style-rule-map.md"
    files = [
        root / "references/source-paper-index.md",
        root / "references/figure-audit-register.md",
        rule_map,
        root / "skills/nature-publication-figure/references/figure-style-atlas.md",
        root / "skills/nature-publication-figure/references/color-and-chart-rules.md",
        root / "skills/nature-publication-figure/references/qa-and-export.md",
    ]
    errors = []
    missing = [path for path in files if not path.exists()]
    for path in missing:
        errors.append(f"Missing style evidence file: {path}")
    if missing:
        print("Style coverage check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    text = "\n".join(path.read_text(encoding="utf-8") for path in files)
    rule_map_text = rule_map.read_text(encoding="utf-8")
    for group in REQUIRED_GROUPS:
        if f"| {group} " not in text and f"组 {group}" not in text:
            errors.append(f"Missing figure style coverage for group {group}")
        if f"## Group {group}" not in rule_map_text:
            errors.append(f"Missing rule-map section for group {group}")
    for term in REQUIRED_TERMS:
        if term not in text:
            errors.append(f"Missing required style term: {term}")
    for term in REQUIRED_RULE_MAP_TERMS:
        if term not in rule_map_text:
            errors.append(f"Missing required rule-map term: {term}")
    if errors:
        print("Style coverage check failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Style coverage check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
