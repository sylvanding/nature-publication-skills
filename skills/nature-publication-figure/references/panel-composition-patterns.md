# Panel Composition Patterns

本文件把本地 8 组 Nature-family 参考论文的视觉观察，和 Nature / Springer Nature 官方 figure guidance 连接成可执行的 panel 组合规则。使用时先写 `claim -> evidence -> panel role -> source figure family`，再选布局。

## Source-backed panel contract

每个 panel 必须能回答四个问题：

| 字段 | 要求 |
| --- | --- |
| Claim | 这个 panel 支持哪一句主张 |
| Evidence | 数据、图像、统计或流程证据来自哪里 |
| Panel role | hero、method、microscopy plate、statistical evidence、spatial map、supplementary matrix |
| Source style | 对应本地论文组和官方规则 |

如果缺少真实数据或图像，输出只能标记为 mock-only，不能把示意图伪装成实验证据。

## Hero panel

Hero panel 是主图的视觉中心，不是装饰图。它通常是最先被读者注意到的 evidence block，用来承载“方法能力 + 关键证据”的主张；面积比例必须由目标期刊尺寸、panel 逻辑连接和数据可读性共同决定。

适用场景：

- Figure 1 的方法总览：`schematic -> representative data -> key metric`
- 显微图能力展示：大幅暗底图像板 + zoom-in + scale bar
- 空间组学：组织原图或 cluster map + embedding/heatmap
- 算法/模型：输入输出对照 + error/confidence map

本地证据：

- 组 3、4、5、6 使用暗底显微图和重建/误差图作为视觉中心。
- 组 7 用活体长时程图像和系统示意建立应用场景。
- 组 8 用 tissue morphology、embedding 和 heatmap 组成空间证据中心。

官方约束：

- Nature formatting guide 强调 figures should be small/simple and only use multiple panels when logically connected.
- Nature Research Figure Guide 强调避免 overlapping labels 和 hard-to-read small text。

## Dark microscopy plate

Dark microscopy plate 用于 fluorescence、SR、light-sheet、intravital、input-output comparison 和 reconstruction evidence。

布局 recipe：

1. 黑底或近黑底图像区，白色 scale bar。
2. 同一 plate 内统一 crop size、LUT、normalization、projection 和 scale bar。
3. 右侧或下方接最小定量证据：line profile、SNR、resolution、error、confidence、time trace。
4. 每个图像 panel 只放必要英文短标签：`Raw`、`Input`、`Prediction`、`Ground truth`、`Error`。
5. 图像 provenance 必须记录 source path、crop box/slice、pixel size、LUT、normalization、processing。

局部增强、局部擦除、选择性模糊、未记录 gamma/filtering 都不允许。若用户要求“更好看”，先解释 image integrity 边界。

## Statistical evidence block

Statistical evidence block 用于性能比较、消融、鲁棒性、组间差异和 calibration。

推荐组合：

- strip/box/violin + summary line
- paired line 或 slope graph 用于同一样本前后对比
- small multiples 用于多条件鲁棒性
- calibration/coverage curve 用于 uncertainty/confidence
- heatmap/matrix 用于多类别、多脑区、多参数

必须包含：

- 英文 axis label 和单位
- `n` 的定义
- error bar 或 CI 定义
- 统计检验或模型说明
- 共享轴范围或共享 color scale，除非明确说明不同范围

避免：

- 单独的 3D bar chart
- 无点位的均值柱状图
- 太多颜色的 spaghetti plot
- 没有归一化说明的 confusion matrix 或 network

## Schematic and icon style

Schematic and icon style 用于 method schematic、optical path、network architecture、workflow 和 biological timeline。

规则：

- 图标服务机制，不做装饰。每个 icon 只表达一个实体或操作。
- 使用浅色模块、细线箭头、统一圆角和统一 stroke width。
- 每个模块用 1-3 个英文词：`Training`、`Inference`、`Reconstruction`、`Validation`。
- 箭头方向必须和数据流/实验流程一致。
- 流程图必须与真实 image/statistical evidence 相邻，不能单独充当主证据。
- 不要使用 emoji、拟物插画、阴影、3D 效果或无数据意义的 decorative icons。

适配本地论文：

- optical schematic：组 4、7
- network architecture：组 5、6
- reconstruction pipeline：组 3
- biological workflow / timeline：组 2、7、8

## Supplementary validation matrix

Supplementary validation matrix 用于补充材料、Extended Data 或方法验证矩阵。

组织规则：

- 一页只回答一个验证主题。
- 行列必须有固定含义，如 sample、condition、time point、parameter、ablation、method。
- 同类 panel 共享 axis range、LUT、normalization 或 color scale。
- 长说明放 caption；图内只保留短英文标签。
- 跨页的 Supplementary Figure 保持同一逻辑图号，不要拆成多个独立验证主题。

本地证据：

- 组 1：tracking / embedding / segmentation validation
- 组 2：neural dynamics traces、brain maps、condition matrices
- 组 3：3D reconstruction robustness、views、noise、profile/error maps
- 组 4-6：SR microscopy input-output grids、confidence/error、parameter validation
- 组 7：intravital time grids、animal/tissue context
- 组 8：morphology thumbnails、embedding、cluster and region comparison

## Quick panel chooser

| Claim type | Primary panel | Required companion |
| --- | --- | --- |
| Method exists | Schematic and icon style | representative data panel |
| Image quality improves | Dark microscopy plate | line profile or error map |
| Model is reliable | Input-output montage | confidence/calibration block |
| Group difference exists | Statistical evidence block | sample count and uncertainty |
| Spatial pattern matters | Tissue/spatial map | embedding or region statistic |
| Robustness holds | Supplementary validation matrix | shared axis/LUT and parameter labels |

## Sources

- Skill-contained local evidence: `references/figure-style-atlas.md`.
- Source checkout audit evidence: `../../../references/source-paper-index.md`, `../../../references/figure-audit-register.md`, `../../../references/pdf-hash-manifest.md`.
- Nature formatting guide, checked 2026-06-24: <https://www.nature.com/nature/for-authors/formatting-guide>.
- Nature Research Figure Guide, checked 2026-06-24: <https://research-figure-guide.nature.com/figures/>.
- Springer Nature accessibility requirements for figures, checked 2026-06-24: <https://www.springernature.com/gp/policies/accessibility-figures-images>.
- Springer Nature AI guidance, checked 2026-06-24: <https://www.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities>.
