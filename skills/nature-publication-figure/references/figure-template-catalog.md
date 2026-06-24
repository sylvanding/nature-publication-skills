# Figure Template Catalog

本文件定义可复用模板的目录和输入/输出契约。Goal 2 只定义 template families；真正可运行的模板脚本在 Goal 4 实现。所有模板的图内文字必须是英文。

Goal 4 已实现首个 deterministic smoke template：

- 生成器：`scripts/generate_multi_panel_microscopy_plate.py`
- 配置：`templates/multi_panel_microscopy_plate.json`
- 调色板：`assets/palettes.json`
- 仓库级验证：`python scripts/validate_figure_templates.py`

模板脚本默认生成 mock-only PDF、PNG preview 和 provenance JSON。真实投稿图必须替换为真实 source files，并在 sidecar 中记录 provenance。

## Template contract

每个模板必须声明：

- claim supported by the figure
- expected input data or image files
- panel map
- output files
- provenance sidecar fields
- validation checks

模板可以生成 mock example，但必须在文件名、caption 或 sidecar 中标记 `mock_only: true`。不能让 mock figure 看起来像真实实验结果。

## `multi_panel_microscopy_plate`

用途：荧光显微、超分辨、光片、活体成像、输入/输出/重建对照。

输入：

- image paths or arrays
- crop boxes or slice indices
- channel mapping / LUT
- pixel size and scale bar length
- normalization range

输出：

- editable vector layout when possible
- high-resolution preview
- provenance JSON

必须验证：

- scale bar visible
- no CJK figure text
- channel colors are color-safe
- same crop and scale conventions across comparable panels

## `statistical_evidence_block`

用途：性能比较、组间差异、消融、鲁棒性、uncertainty/calibration。

输入：

- tidy table with group, value, replicate/sample fields
- metric units
- error definition
- statistical test or model description

输出：

- strip/box/violin/line/heatmap panel
- legend or direct labels
- summary statistics table in sidecar

必须验证：

- axis units present
- `n` definition present
- error bars or CI defined
- no unsupported significance marks

## `method_schematic`

用途：算法流程、光路系统、训练/推理、sample-to-analysis workflow。

输入：

- ordered modules
- edges and data flow direction
- optional icons selected from a controlled vocabulary
- adjacent evidence panel reference

输出：

- editable vector schematic
- short English module labels
- sidecar listing modules and data-flow assumptions

必须验证：

- every arrow has a direction and meaning
- no decorative icons
- no isolated schematic without data/evidence context

## `input_output_error_map`

用途：模型输出、denoising、super-resolution、reconstruction、confidence/error comparison。

输入：

- raw/input image
- output/prediction image
- ground truth or reference when available
- error or confidence map
- shared normalization policy

输出：

- paired montage
- zoom-in region
- line profile or error metric
- provenance sidecar

必须验证：

- comparable panels share scale and crop
- error map color scale is explained
- confidence map is not presented as ground truth

## `supplementary_validation_matrix`

用途：补充图、Extended Data、参数敏感性、多样本/多条件验证。

输入：

- row and column variables
- ordered conditions
- shared color scale / axis policy
- caption purpose sentence

输出：

- matrix layout
- compact labels
- sidecar describing row/column semantics

必须验证：

- one validation theme per matrix
- shared scale unless explicitly justified
- row/column labels are English and short
- cross-page figures keep the same logical figure number

## Provenance sidecar minimum

```json
{
  "template": "multi_panel_microscopy_plate",
  "mock_only": false,
  "source_files": [],
  "panel_map": {},
  "pixel_size_um": null,
  "scale_bar_um": null,
  "normalization": null,
  "software": {},
  "outputs": []
}
```

## Sources

- Skill-contained local evidence: `references/figure-style-atlas.md`.
- Source checkout audit evidence: `../../../references/figure-audit-register.md`, `../../../references/source-paper-index.md`, `../../../references/pdf-hash-manifest.md`.
- Skill rules: `references/panel-composition-patterns.md`, `references/color-and-chart-rules.md`, `references/qa-and-export.md`.
- Nature Research Figure Guide, checked 2026-06-24: <https://research-figure-guide.nature.com/figures/>.
- Springer Nature AI guidance, checked 2026-06-24: <https://www.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities>.
