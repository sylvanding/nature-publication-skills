# Color and Chart Rules

## 语义调色板

`scripts/analyze_pdf_palette.py` 可辅助统计 PDF 页面中的非中性色，但结果会包含期刊页眉、logo、报告页和表格线条等非科学图形颜色。因此 palette 统计用于发现候选色和核验趋势，最终配色仍要回到实际 figure panel 和可访问性要求。

### Statistical Palette

| 角色 | 推荐颜色 | 用途 |
|---|---|---|
| Primary blue | `#3B6FB6` | model output, algorithm result, main quantitative series |
| Cyan | `#00A6D6` | microscopy channel, prediction, reconstructed signal |
| Green | `#2CA25F` | fluorescence channel, accepted/positive condition |
| Orange | `#E07A2D` | residual, error, perturbation, warning highlight |
| Magenta | `#C24ACB` | paired microscopy channel, alternative condition |
| Purple | `#7B61B3` | secondary grouping, spatial cluster family |
| Gray | `#6B7280` | baseline, reference, control, unavailable |
| Black | `#111111` | text, outlines, dark image plate background |

### Microscopy LUT Palette

| 角色 | 推荐颜色 | 用途 |
|---|---|---|
| Cyan | `#00C8D7` | reconstructed signal, blue/green shifted fluorescence |
| Magenta | `#D64ACB` | paired channel, nuclei/protein channel |
| Green | `#37B24D` | fluorescence channel when not paired against red |
| Orange | `#F08A24` | error/residual or warm fluorescence channel |
| Blue | `#2F80ED` | structural channel or model output overlay |
| White | `#F8F8F8` | scale bar and dark-background labels |

### Spatial / Cluster Palette

使用 6-10 个中等饱和度、亮度接近的类别色；legend 必须可见。类别太多时优先直接标注主要 cluster，其他合并为 `Other` 或转入补充图。

### Histology / Tissue Palette

组织切片本身可保留原始染色。覆盖层使用半透明 cyan、magenta、orange 或 blue，避免遮住组织结构。不要用整页 palette 统计结果反推 histology 颜色。

规则：

- 类别数超过 6 个时，先考虑分面、小 multiples 或直接标注，不要无限扩展彩虹色。
- 连续量使用 `viridis`、`magma`、`cividis`、`inferno`；避免 `jet` / rainbow。
- 红色只能作为危险/错误/显著区域的辅助强调，不能和绿色构成唯一对比。
- 显微双通道优先 green/magenta 或 cyan/orange；三通道需要同时检查灰度可读性。

## 图型选择

| 证据问题 | 首选图型 | 避免 |
|---|---|---|
| 方法如何工作 | method schematic + minimal data example | 独立装饰性流程图 |
| 输入输出是否改善 | paired image montage + line profile + error map | 只给单张漂亮图 |
| 多条件鲁棒性 | small multiples + shared scale | 每个条件不同色阶 |
| 组间差异 | strip/box/violin with summary | 只有均值柱状图 |
| 时间动态 | line traces + heatmap summary | 过密 spaghetti plot |
| 空间模式 | tissue image + segmentation/cluster map + embedding | 只给 UMAP 不给组织上下文 |
| 补充验证 | validation matrix | 长图例替代图内结构 |
| 3D/显微重建质量 | image plate + line profile + error map | 只展示最好看的切片 |
| 分类或识别 | confusion matrix + per-class metric | 只给总体准确率 |
| 功能连接或脑区关系 | network/matrix + region legend | 无归一化说明的网络图 |
| 不确定性或置信度 | confidence map + calibration/coverage plot | 只给平均误差 |
| 分布差异 | histogram/density + summary statistic | 只给均值 |

## Panel 组合

- Figure 1：通常承担方法总览。优先 `schematic -> representative data -> key quantitative promise`。
- Figure 2-4：承担性能、机制、应用或生物发现。每张图只讲一个主结论。
- Final main figure：展示更真实、更复杂或更长期的应用场景。
- Extended Data：扩展主文结论，保持与对应主图同一视觉语法。
- Supplementary figures：按验证主题矩阵化，不追求主图级叙事，但必须可扫描。

## 英文图内短语库

可直接使用：

- `Input`
- `Prediction`
- `Ground truth`
- `Raw`
- `Denoised`
- `Reconstruction`
- `Error`
- `Residual`
- `Confidence`
- `Time (min)`
- `Intensity (a.u.)`
- `Resolution (nm)`
- `Tracking accuracy`
- `Cell count`
- `Training`
- `Inference`
- `Validation`

不要把中文短语放进图中。
