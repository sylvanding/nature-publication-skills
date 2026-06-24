#!/usr/bin/env python3
"""Validate Nature figure skill v2 reference coverage."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_SKILL = ROOT / "skills" / "nature-publication-figure"
BENCHMARK_DIR = ROOT / "tests" / "benchmarks" / "figure"


CHECKS = {
    "SKILL.md": [
        "panel-composition-patterns.md",
        "figure-template-catalog.md",
    ],
    "references/panel-composition-patterns.md": [
        "Source-backed panel contract",
        "Hero panel",
        "Dark microscopy plate",
        "Statistical evidence block",
        "Schematic and icon style",
        "Supplementary validation matrix",
        "Nature Research Figure Guide",
        "references/figure-style-atlas.md",
        "../../../references/source-paper-index.md",
        "../../../references/figure-audit-register.md",
        "../../../references/pdf-hash-manifest.md",
    ],
    "references/figure-template-catalog.md": [
        "multi_panel_microscopy_plate",
        "statistical_evidence_block",
        "method_schematic",
        "input_output_error_map",
        "supplementary_validation_matrix",
        "provenance",
        "references/figure-style-atlas.md",
        "../../../references/figure-audit-register.md",
        "../../../references/source-paper-index.md",
        "../../../references/pdf-hash-manifest.md",
    ],
    "references/color-and-chart-rules.md": [
        "colored text",
        "overlapping",
        "red and green",
        "colour blindness",
        "solid colours",
    ],
    "references/plotting-toolchain.md": [
        "89 mm",
        "183 mm",
        "5-7 pt",
        "pdf.fonttype",
        "editable text",
    ],
    "references/qa-and-export.md": [
        "main figures",
        "Extended Data",
        "editable vector",
        "RGB",
        "generative AI",
    ],
}

SECTION_CHECKS = {
    "references/panel-composition-patterns.md": [
        "## Source-backed panel contract",
        "## Hero panel",
        "## Dark microscopy plate",
        "## Statistical evidence block",
        "## Schematic and icon style",
        "## Supplementary validation matrix",
        "## Quick panel chooser",
        "## Sources",
    ],
    "references/figure-template-catalog.md": [
        "## Template contract",
        "## `multi_panel_microscopy_plate`",
        "## `statistical_evidence_block`",
        "## `method_schematic`",
        "## `input_output_error_map`",
        "## `supplementary_validation_matrix`",
        "## Provenance sidecar minimum",
        "## Sources",
    ],
}

BENCHMARK_CHECKS = {
    "pressure-scenarios.md": [
        "# Figure Skill V2 Pressure Scenarios",
        "## Scenario 1",
        "## Scenario 2",
        "## Scenario 3",
        "## Scenario 4",
        "## Scenario 5",
        "Expected baseline failure",
        "Passing behavior after v2",
        "ungrounded palette choice",
        "overdecorated layout",
        "missing scale bar/provenance",
        "no source mapping to paper evidence",
        "Chinese or ambiguous figure labels",
    ],
    "rubric.md": [
        "# Figure Skill V2 Rubric",
        "Source mapping",
        "Palette and accessibility",
        "Panel composition",
        "Microscopy provenance",
        "Statistical reporting",
        "Export QA",
        "Score 0",
        "Score 2",
    ],
}


def main() -> int:
    errors: list[str] = []
    for rel, terms in CHECKS.items():
        path = FIGURE_SKILL / rel
        if not path.exists():
            errors.append(f"missing required figure v2 file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required term: {term!r}")
        for section in SECTION_CHECKS.get(rel, []):
            if section not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required section: {section!r}")

    for rel in ("references/panel-composition-patterns.md", "references/figure-template-catalog.md"):
        path = FIGURE_SKILL / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "references/figure-style-atlas.md" not in text:
            errors.append(f"{path.relative_to(ROOT)} must cite skill-contained local evidence: references/figure-style-atlas.md")
        if "Source checkout audit evidence" not in text:
            errors.append(f"{path.relative_to(ROOT)} must distinguish source-checkout audit evidence from copied skill evidence")

    panel_text_path = FIGURE_SKILL / "references" / "panel-composition-patterns.md"
    if panel_text_path.exists() and "35-60%" in panel_text_path.read_text(encoding="utf-8"):
        errors.append(f"{panel_text_path.relative_to(ROOT)} contains unsupported hero panel area range '35-60%'")

    for rel, terms in BENCHMARK_CHECKS.items():
        path = BENCHMARK_DIR / rel
        if not path.exists():
            errors.append(f"missing required figure benchmark file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required benchmark term: {term!r}")

    if errors:
        print("Figure v2 validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Figure v2 validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
