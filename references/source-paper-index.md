# 本地论文来源索引

访问/审计日期：2026-06-23。来源目录：`references-papers-dai-tsinghua/`。

本索引用于给 writing/figure skills 提供可追溯依据。不要把 PDF 全文或大段图例复制进
skill；agent 需要精读原文时，应回到下列 PDF 路径。

## 覆盖概览

- 实际发现 15 个 PDF：1-7 组包含主文和补充材料，8 组只有主文。
- 页面级视觉审计覆盖全部 PDF。可用 `scripts/make_pdf_contact_sheets.py` 重新生成 contact sheets。
- 图号线索：主图约 42 个，Extended Data 图约 26 个，Supplementary 图约 165 个，表号约 18 个。
- PDF 文本层整体可抽取，但 Nature 论文图常由矢量文字、嵌入图像和面板标签组合而成；抽图必须以页面渲染为主，`pdfimages` 只能作辅助。

## 论文清单

| 组 | 主文 / 补充材料 | 题名与 DOI | 期刊年份 | 图表线索 | 风格证据 |
|---|---|---|---|---|---|
| 1 | `references-papers-dai-tsinghua/1/s41592-025-02886-x.pdf` | CELLECT: contrastive embedding learning for large-scale efficient cell tracking. DOI: `10.1038/s41592-025-02886-x` | Nature Methods, 2025 | Fig. 1-5 | contact sheet `.audit/pdf-page-sheets/1-s41592-025-02886-x.jpg`; tracking workflow, embedding, fluorescence grid |
| 1 | `references-papers-dai-tsinghua/1/41592_2025_2886_MOESM1_ESM.pdf` | 同上补充材料 | Nature Methods, 2025 | Supplementary Fig. 1-20; Supplementary Table 1-4 | `.audit/pdf-page-sheets/1-41592_2025_2886_MOESM1_ESM.jpg`; tracking/segmentation validation matrix |
| 2 | `references-papers-dai-tsinghua/2/s41467-025-63823-2.pdf` | Prominent involvement of acetylcholine dynamics in stable olfactory representation across the Drosophila brain. DOI: `10.1038/s41467-025-63823-2` | Nature Communications, 2025 | Fig. 1-5 | `.audit/pdf-page-sheets/2-s41467-025-63823-2.jpg`; brain maps, odor traces, heatmaps, region statistics |
| 2 | `references-papers-dai-tsinghua/2/41467_2025_63823_MOESM1_ESM.pdf` | 同上补充材料 | Nature Communications, 2025 | Supplementary Fig. 1-16; Supplementary Table 1 | `.audit/pdf-page-sheets/2-41467_2025_63823_MOESM1_ESM.jpg`; neural dynamics small multiples |
| 3 | `references-papers-dai-tsinghua/3/s41592-025-02698-z.pdf` | Physics-driven self-supervised learning for fast high-resolution robust 3D reconstruction of light-field microscopy. DOI: `10.1038/s41592-025-02698-z` | Nature Methods, 2025 | Fig. 1-5 | `.audit/pdf-page-sheets/3-s41592-025-02698-z.jpg`; 3D reconstruction, dark image plates, line profiles |
| 3 | `references-papers-dai-tsinghua/3/41592_2025_2698_MOESM1_ESM.pdf` | 同上补充材料 | Nature Methods, 2025 | Supplementary Fig. 1-26; Supplementary Table 1-3 | `.audit/pdf-page-sheets/3-41592_2025_2698_MOESM1_ESM.jpg`; reconstruction robustness and parameter validation |
| 4 | `references-papers-dai-tsinghua/4/s41592-025-02678-3.pdf` | Fast-adaptive super-resolution lattice light-sheet microscopy for rapid, long-term, near-isotropic subcellular imaging. DOI: `10.1038/s41592-025-02678-3` | Nature Methods, 2025 | Fig. 1-5; Extended Data Fig. 1-10 | `.audit/pdf-page-sheets/4-s41592-025-02678-3.jpg`; optical schematic, dark microscopy hero panels |
| 4 | `references-papers-dai-tsinghua/4/41592_2025_2678_MOESM1_ESM.pdf` | 同上补充材料 | Nature Methods, 2025 | Supplementary Fig. 1-28; Supplementary Table 1-2 | `.audit/pdf-page-sheets/4-41592_2025_2678_MOESM1_ESM.jpg`; SR microscopy supplementary matrices |
| 5 | `references-papers-dai-tsinghua/5/s41587-025-02553-8.pdf` | A neural network for long-term super-resolution imaging of live cells with reliable confidence quantification. DOI: `10.1038/s41587-025-02553-8` | Nature Biotechnology, 2026 | Fig. 1-5; Extended Data Fig. 1-10 | `.audit/pdf-page-sheets/5-s41587-025-02553-8.jpg`; network architecture, confidence/error maps |
| 5 | `references-papers-dai-tsinghua/5/41587_2025_2553_MOESM1_ESM.pdf` | 同上补充材料 | Nature Biotechnology, 2026 | Supplementary Fig. 1-20; Supplementary Table 1-2 | `.audit/pdf-page-sheets/5-41587_2025_2553_MOESM1_ESM.jpg`; uncertainty and image-grid validation |
| 6 | `references-papers-dai-tsinghua/6/s41467-024-48575-9.pdf` | Zero-shot learning enables instant denoising and super-resolution in optical fluorescence microscopy. DOI: `10.1038/s41467-024-48575-9` | Nature Communications, 2024 | Fig. 1-5 | `.audit/pdf-page-sheets/6-s41467-024-48575-9.jpg`; denoising comparison, orange/blue/cyan microscopy |
| 6 | `references-papers-dai-tsinghua/6/41467_2024_48575_MOESM1_ESM.pdf` | 同上补充材料 | Nature Communications, 2024 | Supplementary Fig. 1-34; Supplementary Table 1-4 | `.audit/pdf-page-sheets/6-41467_2024_48575_MOESM1_ESM.jpg`; extensive input-output comparison grids |
| 7 | `references-papers-dai-tsinghua/7/s41587-024-02249-5.pdf` | Long-term intravital subcellular imaging with confocal scanning light-field microscopy. DOI: `10.1038/s41587-024-02249-5` | Nature Biotechnology, 2025 | Fig. 1-6; Table 1 | `.audit/pdf-page-sheets/7-s41587-024-02249-5.jpg`; intravital timeline, green/purple channels, time-series grid |
| 7 | `references-papers-dai-tsinghua/7/41587_2024_2249_MOESM1_ESM.pdf` | 同上补充材料 | Nature Biotechnology, 2025 | Supplementary Fig. 1-21; Supplementary Table 1 | `.audit/pdf-page-sheets/7-41587_2024_2249_MOESM1_ESM.jpg`; intravital supplementary validation |
| 8 | `references-papers-dai-tsinghua/8/s41587-022-01251-z.pdf` | Integrative spatial analysis of cell morphologies and transcriptional states with MUSE. DOI: `10.1038/s41587-022-01251-z` | Nature Biotechnology, 2022 | Fig. 1-6; Extended Data Fig. 1-6 | `.audit/pdf-page-sheets/8-s41587-022-01251-z.jpg`; tissue morphology, spatial omics, embedding, heatmap |

## 使用纪律

1. 写作结论必须回到“题名、摘要、结果小标题、图例、方法”中的可见证据。
2. 绘图风格必须回到“主文图、Extended Data、Supplementary figure”的视觉证据。
3. 若需要判断每个图的细节，先用 `scripts/make_pdf_contact_sheets.py` 重新生成页面 contact sheet，再打开对应 PDF 页或高分辨率渲染图。
4. 不要把正文引用误判成图号；图号 registry 需要人工过滤文本匹配误报。
5. Supplementary figure 可能跨页。一个图号跨页时，应在同一逻辑记录下保留 `part_a` / `part_b`，不要误拆成两个图号。
