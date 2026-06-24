#!/usr/bin/env python3
"""Generate a deterministic mock microscopy plate for template smoke tests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


SKILL_DIR = Path(__file__).resolve().parents[1]
PALETTE_PATH = SKILL_DIR / "assets" / "palettes.json"
TEMPLATE_PATH = SKILL_DIR / "templates" / "multi_panel_microscopy_plate.json"


def mm_to_inch(value: float) -> float:
    return value / 25.4


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def gaussian_field(size: int = 160) -> tuple[np.ndarray, np.ndarray]:
    y, x = np.mgrid[-1:1:complex(size), -1:1:complex(size)]
    spots = [
        (0.55, -0.35, -0.20, 0.20),
        (0.80, 0.25, 0.15, 0.16),
        (0.45, 0.10, -0.45, 0.12),
        (0.60, -0.05, 0.45, 0.18),
    ]
    base = np.zeros((size, size), dtype=float)
    for amplitude, cx, cy, sigma in spots:
        base += amplitude * np.exp(-((x - cx) ** 2 + (y - cy) ** 2) / (2 * sigma**2))
    base = base / base.max()
    second = np.roll(base, shift=18, axis=1) * 0.75
    return base, second


def normalize(image: np.ndarray) -> np.ndarray:
    image = image - image.min()
    max_value = image.max()
    if max_value:
        image = image / max_value
    return np.clip(image, 0, 1)


def colorize(image: np.ndarray, color_hex: str) -> np.ndarray:
    color = np.array([int(color_hex[i : i + 2], 16) for i in (1, 3, 5)], dtype=float) / 255.0
    return np.clip(image[..., None] * color, 0, 1)


def synthetic_images(palette: dict) -> dict[str, np.ndarray]:
    rng = np.random.default_rng(42)
    base, second = gaussian_field()
    raw = normalize(base + 0.55 * second + rng.normal(0, 0.04, base.shape))
    prediction = normalize(0.92 * base + 0.08 * np.roll(base, 1, axis=0))
    ground_truth = normalize(base)
    error = normalize(np.abs(prediction - ground_truth))
    tokens = palette["tokens"]
    overlay = np.clip(colorize(raw, tokens["cyan"]) + colorize(second, tokens["magenta"]), 0, 1)
    return {
        "Raw": overlay,
        "Prediction": colorize(prediction, tokens["cyan"]),
        "Ground truth": colorize(ground_truth, tokens["magenta"]),
        "Error": error,
        "line_x": np.arange(base.shape[1]),
        "line_prediction": prediction[base.shape[0] // 2],
        "line_ground_truth": ground_truth[base.shape[0] // 2],
    }


def draw_scale_bar(ax, image_shape: tuple[int, int], pixel_size_um: float, scale_bar_um: float) -> None:
    pixels = scale_bar_um / pixel_size_um
    y = image_shape[0] - 14
    x0 = image_shape[1] - pixels - 16
    x1 = image_shape[1] - 16
    ax.plot([x0, x1], [y, y], color="white", lw=2.0, solid_capstyle="butt")
    ax.text((x0 + x1) / 2, y - 8, f"{scale_bar_um:g} um", color="white", fontsize=6, ha="center", va="bottom")


def panel_label(ax, label: str) -> None:
    ax.text(-0.08, 1.05, label, transform=ax.transAxes, fontsize=8, fontweight="bold", va="bottom", ha="left")


def portable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(resolved)


def render(output_dir: Path, prefix: str) -> dict:
    palette = load_json(PALETTE_PATH)
    template_config = load_json(TEMPLATE_PATH)
    images = synthetic_images(palette)
    tokens = palette["tokens"]

    plt.rcParams.update(
        {
            "font.family": ["Arial", "Helvetica", "DejaVu Sans"],
            "font.size": 6,
            "axes.linewidth": 0.5,
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
            "svg.fonttype": "none",
        }
    )

    fig = plt.figure(figsize=(mm_to_inch(183), mm_to_inch(104)), facecolor="white")
    grid = fig.add_gridspec(2, 4, width_ratios=[1, 1, 1, 1.05], height_ratios=[1, 0.72], wspace=0.28, hspace=0.42)
    image_axes = [
        fig.add_subplot(grid[0, 0]),
        fig.add_subplot(grid[0, 1]),
        fig.add_subplot(grid[0, 2]),
        fig.add_subplot(grid[0, 3]),
    ]
    image_labels = ["Raw", "Prediction", "Ground truth", "Error"]

    error_cmap = LinearSegmentedColormap.from_list("nature_error", ["#000000", tokens["orange"]])
    for index, (ax, label) in enumerate(zip(image_axes, image_labels, strict=True)):
        ax.set_facecolor(tokens["black"])
        if label == "Error":
            ax.imshow(images[label], cmap=error_cmap, vmin=0, vmax=1)
        else:
            ax.imshow(images[label], vmin=0, vmax=1)
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(False)
        panel_label(ax, chr(ord("a") + index))
        ax.text(0.03, 0.95, label, transform=ax.transAxes, color="white", fontsize=6, va="top", ha="left")
        draw_scale_bar(ax, images["Error"].shape, pixel_size_um=0.108, scale_bar_um=5.0)

    profile_ax = fig.add_subplot(grid[1, :2])
    panel_label(profile_ax, "e")
    profile_ax.plot(images["line_x"], images["line_ground_truth"], color=tokens["magenta"], lw=1.1, label="Ground truth")
    profile_ax.plot(images["line_x"], images["line_prediction"], color=tokens["cyan"], lw=1.1, label="Prediction")
    profile_ax.set_xlabel("Position (pixels)")
    profile_ax.set_ylabel("Intensity (a.u.)")
    profile_ax.legend(frameon=False, fontsize=6, loc="upper right")
    profile_ax.spines[["top", "right"]].set_visible(False)
    profile_ax.tick_params(width=0.5, length=2.5)

    metric_ax = fig.add_subplot(grid[1, 2:])
    panel_label(metric_ax, "f")
    metrics = ["RMSE", "SSIM", "SNR"]
    values = [0.08, 0.94, 18.6]
    colors = [tokens["orange"], tokens["blue"], tokens["gray"]]
    metric_ax.bar(metrics, values, color=colors, width=0.56)
    metric_ax.set_ylabel("Metric value")
    metric_ax.spines[["top", "right"]].set_visible(False)
    metric_ax.tick_params(width=0.5, length=2.5)
    metric_ax.text(0.02, 0.94, "Mock-only", transform=metric_ax.transAxes, ha="left", va="top", fontsize=6, color=tokens["gray"])

    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / f"{prefix}.pdf"
    png_path = output_dir / f"{prefix}.png"
    sidecar_path = output_dir / f"{prefix}.provenance.json"
    fig.savefig(pdf_path, bbox_inches="tight")
    fig.savefig(png_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    sidecar = {
        "template": template_config["template"],
        "mock_only": True,
        "source_files": [],
        "panel_map": template_config["panel_map"],
        "pixel_size_um": 0.108,
        "scale_bar_um": 5.0,
        "normalization": {"mode": "min-max", "range": [0, 1], "shared_policy": "comparable image panels share synthetic normalization"},
        "software": {
            "python": sys_version(),
            "matplotlib": matplotlib.__version__,
            "numpy": np.__version__,
        },
        "outputs": [portable_path(pdf_path), portable_path(png_path)],
        "palette_tokens": ["cyan", "magenta", "orange", "blue", "gray", "black"],
        "text_labels": ["Raw", "Prediction", "Ground truth", "Error", "Line profile", "Metric summary", "Mock-only"],
    }
    sidecar_path.write_text(json.dumps(sidecar, indent=2), encoding="utf-8")
    return {"pdf": pdf_path, "png": png_path, "sidecar": sidecar_path}


def sys_version() -> str:
    import sys

    return ".".join(str(part) for part in sys.version_info[:3])


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a deterministic Nature-style microscopy plate template.")
    parser.add_argument("--output-dir", type=Path, default=Path(".audit/template-smoke"))
    parser.add_argument("--prefix", default="multi_panel_microscopy_plate")
    args = parser.parse_args()

    outputs = render(args.output_dir, args.prefix)
    for kind, path in outputs.items():
        print(f"{kind}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
