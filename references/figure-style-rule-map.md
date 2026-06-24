# Figure Style Rule Map

审计日期：2026-06-24。用途：把 `references-papers-dai-tsinghua/` 的 8 组本地论文和补充材料映射到 `nature-publication-figure` 的可执行绘图规则。

本文件不替代原始 PDF。需要逐图核查时，回到 `references/source-paper-index.md`、`references/figure-audit-register.md`、`references/pdf-hash-manifest.md` 和 `.audit/pdf-page-sheets/*.jpg`。`.audit/**` 是可复现审计产物，不进入 git。

## Audit Reproduction

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
```

2026-06-24 复跑结果：15 PDF records、15 contact sheets、15 palette summaries。文本层 marker 会包含正文引用和图索引页，因此每组图号范围以 `references/figure-audit-register.md` 的人工过滤范围为准，`.audit/pdf_figure_inventory.json` 用于定位页面和复查。

## Rule Families

| Skill rule family | 何时使用 | 主要来源 |
| --- | --- | --- |
| method schematic | 方法框架、光路、网络结构、样本流程 | 组 1、3、4、5、6、7 |
| dark microscopy plate | 荧光、SR、light-sheet、intravital、重建图像板 | 组 3、4、5、6、7 |
| statistical evidence block | 性能比较、组间差异、消融、稳定性、置信度 | 组 1、2、5、6、8 |
| supplementary validation matrix | 补充图、参数、样本、时间点、鲁棒性矩阵 | 组 1-7 |
| spatial omics map | tissue morphology、embedding、cluster、region heatmap | 组 8 |
| input-output montage | raw/input、prediction/output、ground truth/reference、error/confidence | 组 3、5、6 |

## Group 1 - CELLECT

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | None in local source set |
| Supplementary figures | Supplementary Fig. 1-20 |
| Tables | Supplementary Table 1-4 |
| Skill rule mapping | method schematic; statistical evidence block; supplementary validation matrix; fluorescence segmentation/tracking image grids |
| Source evidence | `references-papers-dai-tsinghua/1/s41592-025-02886-x.pdf`; `references-papers-dai-tsinghua/1/41592_2025_2886_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/1-s41592-025-02886-x.jpg` and `.audit/pdf-page-sheets/1-41592_2025_2886_MOESM1_ESM.jpg` |
| Coverage status | Covered: main workflow, tracking/embedding/segmentation validation, supplementary tables |

Notes: group 1 anchors the rule that a method figure should combine workflow, representative image evidence, embedding/statistical panels, and validation matrices rather than relying on a decorative overview.

## Group 2 - Acetylcholine Dynamics

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | None in local source set |
| Supplementary figures | Supplementary Fig. 1-16 |
| Tables | Supplementary Table 1 |
| Skill rule mapping | statistical evidence block; supplementary validation matrix; brain/region schematic; neural dynamics trace and heatmap panels |
| Source evidence | `references-papers-dai-tsinghua/2/s41467-025-63823-2.pdf`; `references-papers-dai-tsinghua/2/41467_2025_63823_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/2-s41467-025-63823-2.jpg` and `.audit/pdf-page-sheets/2-41467_2025_63823_MOESM1_ESM.jpg` |
| Coverage status | Covered: main neural dynamics figures and supplementary condition/region matrices |

Notes: group 2 supports the `stimulus/event -> trace matrix -> region map -> summary statistic` pattern and reinforces shared time axes, heatmaps, and labeled region summaries.

## Group 3 - Physics-Driven 3D Reconstruction

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | None in local source set |
| Supplementary figures | Supplementary Fig. 1-26 |
| Tables | Supplementary Table 1-3 |
| Skill rule mapping | method schematic; dark microscopy plate; input-output montage; statistical evidence block; supplementary validation matrix |
| Source evidence | `references-papers-dai-tsinghua/3/s41592-025-02698-z.pdf`; `references-papers-dai-tsinghua/3/41592_2025_2698_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/3-s41592-025-02698-z.jpg` and `.audit/pdf-page-sheets/3-41592_2025_2698_MOESM1_ESM.jpg` |
| Coverage status | Covered: main 3D reconstruction panels, robustness figures, profile/error maps, parameter tables |

Notes: group 3 is the strongest local source for reconstruction pipeline layout, 3D volume/slice presentation, error maps, line profiles, and multi-view supplementary validation.

## Group 4 - Adaptive SR-LLSM

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | Extended Data Fig. 1-10 |
| Supplementary figures | Supplementary Fig. 1-28 |
| Tables | Supplementary Table 1-2 |
| Skill rule mapping | method schematic; dark microscopy plate; supplementary validation matrix; optical workflow; resolution/time statistical evidence block |
| Source evidence | `references-papers-dai-tsinghua/4/s41592-025-02678-3.pdf`; `references-papers-dai-tsinghua/4/41592_2025_2678_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/4-s41592-025-02678-3.jpg` and `.audit/pdf-page-sheets/4-41592_2025_2678_MOESM1_ESM.jpg` |
| Coverage status | Covered: main figures, Extended Data, supplementary SR microscopy and optical validation |

Notes: group 4 backs the separation between dark image plates and white-background quantitative panels, especially for resolution, long-term imaging, organelle grids, and optical-system schematics.

## Group 5 - Neural Network SR Confidence

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | Extended Data Fig. 1-10 |
| Supplementary figures | Supplementary Fig. 1-20 |
| Tables | Supplementary Table 1-2 |
| Skill rule mapping | method schematic; dark microscopy plate; input-output montage; statistical evidence block; confidence/error maps; supplementary validation matrix |
| Source evidence | `references-papers-dai-tsinghua/5/s41587-025-02553-8.pdf`; `references-papers-dai-tsinghua/5/41587_2025_2553_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/5-s41587-025-02553-8.jpg` and `.audit/pdf-page-sheets/5-41587_2025_2553_MOESM1_ESM.jpg` |
| Coverage status | Covered: main/Extended Data confidence presentation, input-output comparisons, uncertainty validation |

Notes: group 5 anchors the rule that confidence maps are not ground truth and must be paired with calibration, error or uncertainty statistics.

## Group 6 - Zero-Shot Denoising And SR

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-5 |
| Extended Data | None in local source set |
| Supplementary figures | Supplementary Fig. 1-34 |
| Tables | Supplementary Table 1-4 |
| Skill rule mapping | method schematic; dark microscopy plate; input-output montage; statistical evidence block; supplementary validation matrix |
| Source evidence | `references-papers-dai-tsinghua/6/s41467-024-48575-9.pdf`; `references-papers-dai-tsinghua/6/41467_2024_48575_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/6-s41467-024-48575-9.jpg` and `.audit/pdf-page-sheets/6-41467_2024_48575_MOESM1_ESM.jpg` |
| Coverage status | Covered: denoising/SR comparison grids, extensive supplementary input-output validation, parameter tables |

Notes: group 6 supports the figure-template requirement that comparable input/output panels share crop, scale, normalization and error-map explanation.

## Group 7 - Intravital CSLFM

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-6 |
| Extended Data | None in local source set |
| Supplementary figures | Supplementary Fig. 1-21 |
| Tables | Table 1; Supplementary Table 1 |
| Skill rule mapping | method schematic; dark microscopy plate; supplementary validation matrix; intravital time grid; statistical evidence block |
| Source evidence | `references-papers-dai-tsinghua/7/s41587-024-02249-5.pdf`; `references-papers-dai-tsinghua/7/41587_2024_2249_MOESM1_ESM.pdf`; contact sheets `.audit/pdf-page-sheets/7-s41587-024-02249-5.jpg` and `.audit/pdf-page-sheets/7-41587_2024_2249_MOESM1_ESM.jpg` |
| Coverage status | Covered: live/intravital main figures, time-series grids, animal/tissue context, supplementary validation |

Notes: group 7 supports long-term imaging layouts where time grids, channel overlays, tissue/animal context and quality metrics must stay visually connected.

## Group 8 - MUSE

| Field | Coverage |
| --- | --- |
| Main figures | Fig. 1-6 |
| Extended Data | Extended Data Fig. 1-6 |
| Supplementary figures | No supplementary PDF provided in local source set |
| Tables | None in local source set |
| Skill rule mapping | spatial omics map; statistical evidence block; morphology gallery; embedding/scatter; heatmap and region comparison |
| Source evidence | `references-papers-dai-tsinghua/8/s41587-022-01251-z.pdf`; contact sheet `.audit/pdf-page-sheets/8-s41587-022-01251-z.jpg` |
| Coverage status | Covered for main and Extended Data; supplementary coverage not applicable because no supplementary PDF was provided |

Notes: group 8 anchors tissue morphology, segmentation/mask, embedding, cluster map, morphology grid and region-level heatmap rules.

## Coverage Summary

- All 8 groups are mapped to at least one source PDF, contact sheet, figure/table range and skill rule family.
- Main figures are covered for all groups.
- Extended Data is present and mapped for groups 4, 5 and 8; the remaining groups have no Extended Data in the local source set.
- Supplementary figures are mapped for groups 1-7; group 8 has no supplementary PDF in the local source set.
- Tables are mapped where present, but tables are treated as evidence support and not as decorative heatmaps unless comparison is the message.
- Palette evidence is taken from `.audit/pdf_palette_summary.json` and interpreted conservatively; it can flag dominant color families but cannot replace visual inspection of contact sheets.
