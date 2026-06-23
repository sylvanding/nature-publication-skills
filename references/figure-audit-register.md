# Figure Audit Register

审计日期：2026-06-23。审计方法：使用 PyMuPDF/PIL 对全部 PDF 逐页渲染 contact sheet，并结合文本层图号匹配核对主文图、Extended Data、Supplementary figures 和 tables。可用以下命令复现：

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
```

PDF identity is recorded in `references/pdf-hash-manifest.md`. Contact sheets and JSON inventories are reproducible audit artifacts under `.audit/` and are not committed.

## 覆盖表

| 组 | 主文图 | Extended Data | Supplementary figures | Tables | 视觉风格关键词 |
|---|---|---|---|---|---|
| 1 CELLECT | Fig. 1-5 | 无 | Supplementary Fig. 1-20 | Supplementary Table 1-4 | tracking workflow, embedding, segmentation masks, fluorescence image grids, bar/line/scatter |
| 2 acetylcholine dynamics | Fig. 1-5 | 无 | Supplementary Fig. 1-16 | Supplementary Table 1 | brain region schematic, odor response traces, heatmaps, green/cyan/purple activity maps, strip/box statistics |
| 3 physics-driven 3D reconstruction | Fig. 1-5 | 无 | Supplementary Fig. 1-26 | Supplementary Table 1-3 | method schematic, 3D volume, dark image plates, line profiles, reconstruction error maps |
| 4 adaptive SR-LLSM | Fig. 1-5 | Extended Data Fig. 1-10 | Supplementary Fig. 1-28 | Supplementary Table 1-2 | optical workflow, long-term dark microscopy plates, resolution/time traces, organelle image grids |
| 5 neural network SR confidence | Fig. 1-5 | Extended Data Fig. 1-10 | Supplementary Fig. 1-20 | Supplementary Table 1-2 | network schematic, input-output comparison, confidence/error maps, uncertainty statistics |
| 6 zero-shot denoising/SR | Fig. 1-5 | 无 | Supplementary Fig. 1-34 | Supplementary Table 1-4 | denoising comparison grid, orange/blue/cyan microscopy, model flow, performance curves |
| 7 intravital CSLFM | Fig. 1-6 | 无 | Supplementary Fig. 1-21 | Table 1; Supplementary Table 1 | live imaging timeline, green/purple channels, time-series grids, animal/intravital validation |
| 8 MUSE | Fig. 1-6 | Extended Data Fig. 1-6 | 未提供补充 PDF | 无 | tissue morphology, spatial omics, embedding/scatter, heatmap, morphology grids |

## 审计结论

- 主文图通常是少量高密度 multi-panel figures，服务“方法能力 + 关键证据 + 应用展示”。
- Extended Data 承担主文图的完整性扩展，尤其在组 4、5、8 中用于更多样本、更多图像板和更多统计。
- Supplementary figures 主要承担验证矩阵角色，覆盖参数、样本、消融、更多时间点和更多对照。
- 对图表 skill 最关键的不是单一配色，而是图型系统：method schematic、dark microscopy plate、input-output montage、statistical block、spatial omics map、supplementary validation matrix。
