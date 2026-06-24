#!/usr/bin/env python3
"""Validate bundled Nature figure templates by generating a smoke artifact."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_SKILL = ROOT / "skills" / "nature-publication-figure"
GENERATOR = FIGURE_SKILL / "scripts" / "generate_multi_panel_microscopy_plate.py"
PALETTE = FIGURE_SKILL / "assets" / "palettes.json"
TEMPLATE_CONFIG = FIGURE_SKILL / "templates" / "multi_panel_microscopy_plate.json"
OUTPUT_DIR = ROOT / ".audit" / "template-smoke"
PREFIX = "multi_panel_microscopy_plate"
CJK_RE = re.compile(r"[\u3400-\u9fff]")

REQUIRED_PALETTE_TOKENS = ["cyan", "magenta", "orange", "gray", "black"]
REQUIRED_OUTPUTS = [
    OUTPUT_DIR / f"{PREFIX}.pdf",
    OUTPUT_DIR / f"{PREFIX}.png",
    OUTPUT_DIR / f"{PREFIX}.provenance.json",
]
REQUIRED_SIDECAR_KEYS = [
    "template",
    "mock_only",
    "source_files",
    "panel_map",
    "pixel_size_um",
    "scale_bar_um",
    "normalization",
    "software",
    "outputs",
    "palette_tokens",
    "text_labels",
]


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path.relative_to(ROOT)} is invalid JSON: {exc}") from exc


def main() -> int:
    errors: list[str] = []
    required_files = [GENERATOR, PALETTE, TEMPLATE_CONFIG]
    for path in required_files:
        if not path.exists():
            errors.append(f"missing template artifact: {path.relative_to(ROOT)}")

    if not errors:
        try:
            palette = load_json(PALETTE)
            template_config = load_json(TEMPLATE_CONFIG)
        except ValueError as exc:
            errors.append(str(exc))
        else:
            for token in REQUIRED_PALETTE_TOKENS:
                value = palette.get("tokens", {}).get(token)
                if not isinstance(value, str) or not value.startswith("#"):
                    errors.append(f"{PALETTE.relative_to(ROOT)} missing hex token: {token}")
            if template_config.get("template") != PREFIX:
                errors.append(f"{TEMPLATE_CONFIG.relative_to(ROOT)} must declare template {PREFIX!r}")

    if not errors:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [sys.executable, str(GENERATOR), "--output-dir", str(OUTPUT_DIR), "--prefix", PREFIX],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode != 0:
            errors.append(f"template generator failed with exit {result.returncode}:\n{result.stdout}")

    if not errors:
        for path in REQUIRED_OUTPUTS:
            if not path.exists() or path.stat().st_size == 0:
                errors.append(f"missing or empty generated output: {path.relative_to(ROOT)}")

    if not errors:
        try:
            sidecar = load_json(OUTPUT_DIR / f"{PREFIX}.provenance.json")
        except ValueError as exc:
            errors.append(str(exc))
        else:
            for key in REQUIRED_SIDECAR_KEYS:
                if key not in sidecar:
                    errors.append(f"sidecar missing required key: {key}")
            if sidecar.get("template") != PREFIX:
                errors.append("sidecar template does not match generator prefix")
            if sidecar.get("mock_only") is not True:
                errors.append("sidecar must mark deterministic smoke output as mock_only=true")
            panel_map = sidecar.get("panel_map", {})
            for panel in ("a", "b", "c", "d", "e", "f"):
                if panel not in panel_map:
                    errors.append(f"sidecar panel_map missing panel: {panel}")
            labels = sidecar.get("text_labels", [])
            if not labels or any(CJK_RE.search(str(label)) for label in labels):
                errors.append("sidecar text_labels must be non-empty English labels")
            palette_tokens = set(sidecar.get("palette_tokens", []))
            for token in ("cyan", "magenta", "orange"):
                if token not in palette_tokens:
                    errors.append(f"sidecar missing expected palette token: {token}")

    if not errors:
        try:
            import fitz
            from PIL import Image
        except Exception as exc:  # pragma: no cover - dependency check path
            errors.append(f"missing PDF/image validation dependency: {exc}")
        else:
            pdf_text = "\n".join(page.get_text("text") for page in fitz.open(REQUIRED_OUTPUTS[0]))
            if CJK_RE.search(pdf_text):
                errors.append("generated PDF contains CJK figure text")
            for label in ("Raw", "Prediction", "Ground truth", "Error"):
                if label not in pdf_text:
                    errors.append(f"generated PDF missing expected label: {label}")
            with Image.open(REQUIRED_OUTPUTS[1]) as image:
                if image.width < 1000 or image.height < 700:
                    errors.append("generated PNG preview is smaller than expected")

    if errors:
        print("Figure template validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Figure template validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
