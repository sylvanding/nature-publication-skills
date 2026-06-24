# Plotting Toolchain

## 默认选择：Python

推荐 Python 作为默认出版图生成和审计工具：

- `matplotlib`：精确控制版面、字体、矢量导出和多面板 figure。
- `seaborn`：统计图默认风格较稳，适合 strip/box/violin/lineplot。
- `PIL` / `OpenCV` / `scikit-image`：显微图像裁剪、拼接、scale bar、像素检查。
- `tifffile` / `imageio`：读取 OME-TIFF、multi-page TIFF 和显微图像栈。
- `napari` / Fiji/ImageJ：人工确认多通道图像、Z stack、LUT 和 crop；用于审计，不替代可复跑脚本。
- `PyMuPDF` / Poppler：PDF 页面渲染、contact sheet、图号审计。
- `numpy` / `pandas`：数据整形和可复验分析。

MATLAB 可用于读取实验室遗留 `.mat` 数据和复现实验室算法，但不作为默认最终组版工具。R/ggplot2 可用于单纯统计图，但对暗底显微图像板、多图像 montage 和 PDF 审计不如 Python 一体化。

## Nature尺寸和可编辑输出

Nature-family 尺寸口径有两类来源：Nature formatting guide 常用约 90 mm / 180 mm；Nature Research Figure Guide 的最终 artwork 口径常用 89 mm / 183 mm。投稿前按目标期刊最新页面确认；默认脚本可用 89 mm 和 183 mm 作为最终 artwork preset。

导出约束：

- main figures 优先保留 editable text 和 editable vector paths。
- 最终文字通常控制在 5-7 pt；草图或审稿预览可临时放大，但最终导出要回到目标尺寸。
- `pdf.fonttype=42` 和 `ps.fonttype=42` 保留 TrueType 字体；SVG 使用 text 而不是 path。
- 位图 panel 保持 RGB，并在 sidecar 记录 DPI、pixel size、normalization 和 crop。

## Python 基础模板

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

NATURE_COLORS = {
    "blue": "#3B6FB6",
    "cyan": "#00A6D6",
    "green": "#2CA25F",
    "orange": "#E07A2D",
    "magenta": "#C24ACB",
    "purple": "#7B61B3",
    "gray": "#6B7280",
    "black": "#111111",
}

def set_nature_style():
    """Configure conservative Nature-family plotting defaults."""
    mpl.rcParams.update({
        "font.family": "Arial",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
        "font.size": 7,
        "axes.linewidth": 0.6,
        "axes.labelsize": 7,
        "axes.titlesize": 7,
        "xtick.labelsize": 6,
        "ytick.labelsize": 6,
        "legend.fontsize": 6,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
    })
    sns.set_theme(context="paper", style="ticks", rc=mpl.rcParams)

def mm_to_inch(value):
    """Convert millimeters to inches."""
    return value / 25.4
```

## 多面板建议

- 单栏：`figsize=(mm_to_inch(89), mm_to_inch(70-120))`
- 双栏：`figsize=(mm_to_inch(183), mm_to_inch(90-170))`
- 如果目标期刊页面仍写 90 mm / 180 mm，则用期刊当前要求覆盖默认值。
- `GridSpec` 优先于手工坐标；需要 hero panel 时用不等宽/不等高 grid。
- 暗底显微图 panel 关闭 axis，但保留 scale bar 和英文短标签。
- 统计图保留 axis 和单位，减少 tick 数量。

## 显微图像 panel provenance

每个 image panel 至少记录：

- source image path
- crop box or slice index
- pixel size and scale bar length
- channel mapping / LUT
- normalization range
- projection method, if any
- software and version for preprocessing
- whether contrast/gamma/filtering was applied

这些信息可放在脚本参数、sidecar JSON 或 Methods/legend 中；不能只存在于人工记忆。

## 英文标签示例

推荐：

- `Input`
- `Prediction`
- `Ground truth`
- `Error`
- `Intensity (a.u.)`
- `Time (min)`
- `Resolution (nm)`
- `Cell count`
- `Tracking accuracy`

不要在图内使用中文标签。
