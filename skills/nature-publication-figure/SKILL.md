---
name: nature-publication-figure
description: Nature-family scientific figure design and QA. Use when creating, revising, auditing, or scripting publication figures, figure panels, microscopy image plates, statistical plots, Extended Data, Supplementary figures, Nature Methods/Nature Biotechnology/Nature Communications visual style, or when the user asks about 图表, 绘图, 配色, 版式, panel, scale bar, figure legend, or image integrity. All figure text must be English.
---

# Nature Publication Figure

本 skill 用于生成、改造或审计 Nature-family 论文图表。说明文字使用中文；所有图内文字、坐标轴、legend、panel label、scale bar 标注、示例脚本中的标签必须使用英文。

## 调用后先做三件事

1. 先写一行图表契约：`claim -> evidence -> figure type -> target journal -> output files`。
2. 读取需要的 reference，而不是凭记忆作图：
   - 图表风格与论文证据：`references/figure-style-atlas.md`
   - 配色、图型和英文标签规则：`references/color-and-chart-rules.md`
   - 绘图工具选择与代码模板：`references/plotting-toolchain.md`
   - 导出、图像完整性和 QA：`references/qa-and-export.md`
3. 若用户没有给数据或图像，先要求真实数据/图像或明确写出 mock-only；不得伪造结果。

## 默认工具选择

- 默认推荐 Python：`matplotlib` + `seaborn` + `PIL`/`OpenCV` + `PyMuPDF`。原因是它能同时处理统计图、显微图像板、PDF 渲染审计、矢量/位图混合导出和自动化测试。
- 只有在用户已有 MATLAB 分析管线、`.mat` 数据、或需要复现实验室 MATLAB 脚本时，才把 MATLAB 作为数据生成/预处理后端；最终组版仍优先转入 Python 或矢量编辑流程。
- 不推荐把 Plotly/Altair 作为投稿图的最终输出后端；它们适合探索，不适合复杂多面板显微图版的最终审计。

## 风格原则

- 先故事，后装饰：每张主图只服务一个结论；每个 panel 都要回答“它证明什么”。
- 主图要有 hero panel：方法图、关键显微图、核心空间图或核心定量结果必须占据视觉中心。
- 暗底图像板和白底统计图分区排版，不要把显微图强行塞进普通坐标轴风格。
- 统计图使用克制颜色、细轴线、可读的误差定义和样本量；避免 3D 柱、阴影、渐变背景、彩虹/jet colormap。
- 显微图像通道优先使用 cyan/magenta/green/orange/blue 的色盲友好组合；避免把 red/green 作为唯一对比。
- Supplementary figures 不是垃圾桶，而是验证矩阵：按条件、样本、参数、消融、鲁棒性组织成可扫描的小 multiples。
- 配色必须有语义：蓝/青用于成像或算法输出，橙用于 error/residual/highlight，洋红/绿色用于双通道对比，灰色用于基线或未处理状态；不要为了“丰富”而增加颜色。

## 图内英文硬约束

- 任何图内文本都写英文：`Intensity (a.u.)`、`Time (min)`、`Input`、`Prediction`、`Ground truth`、`Error`。
- 中文可出现在文件名、注释、说明文档和用户回复中，但不能出现在图像本体。
- 代码中设置 `font.family` 为 Arial/Helvetica 优先，缺失时使用 DejaVu Sans；导出前检查字体替换和缺字。

## 最小工作流

1. 建立 panel map：列出 A/B/C... 每个 panel 的类型、数据、结论、依赖文件。
2. 选择图型原型：method schematic、image plate、input-output comparison、time series、scatter/box/strip、heatmap、spatial omics map、network/tree、table-like matrix。
3. 写代码或组版前，确定尺寸：单栏约 90 mm，双栏约 180 mm，最大深度约 170 mm；按目标版面设置 `figsize`。
4. 用英文完成所有标签、legend、scale bar、panel label。
5. 导出可编辑矢量版本和审稿位图版本：线图优先 PDF/SVG，含显微图的复合图同时导出 300 dpi 或更高 PNG/TIFF。
6. 运行 QA：打开渲染图，检查非空、分辨率、panel label、scale bar、统计定义、颜色可访问性、图像处理说明。
7. 在回复中给出：输出文件、使用数据、关键参数、验证命令、剩余风险。

## 禁止事项

- 不要为“像 Nature”而牺牲数据真实性。
- 不要裁掉 scale bar、坐标轴单位、样本量、误差定义。
- 不要在主图中堆满所有补充验证。
- 不要使用无法解释的自动美化、局部对比增强或未记录图像处理。
- 不要把中文文字放进图表。
