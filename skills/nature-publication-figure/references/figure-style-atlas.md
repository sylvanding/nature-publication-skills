# Figure Style Atlas

本文件总结仓库根目录 `references-papers-dai-tsinghua/` 中 8 组论文的图表风格。图内示例文本必须保持英文。

## 全局风格

- 主文图通常是“方法/系统逻辑 + 关键图像证据 + 定量验证”的组合，而不是单一统计图。
- 图版以白底为主；显微图像、时间序列图像、空间图像常采用黑底或深色底，和白底统计图区分明显。
- 面板标签小而稳定，通常在 panel 左上角；复杂图会通过浅灰/淡色框线把模块分区。
- 统计配色克制，常见蓝、青、绿、橙、紫、洋红；图像通道常见 cyan/magenta/green/orange/blue。
- Supplementary figures 大量使用矩阵化 small multiples：条件、样本、时间点、参数、消融项按行列组织。

## 图型原型

### 1. Method Schematic

适用：算法、显微系统、样本处理、训练/推理流程。

风格要点：
- 用浅色模块、箭头、简洁图标组织流程。
- 每个模块只保留一个英文关键词或短语，如 `Training`、`Inference`、`Tracking`、`Reconstruction`。
- 与真实图像或定量输出相邻，避免孤立的装饰流程图。

子类型：
- `optical schematic`：光路、扫描、采集路径、样本位置，适合组 4/7。
- `network architecture`：输入、编码器/解码器、训练目标、置信度输出，适合组 5/6。
- `reconstruction pipeline`：物理模型、forward model、inverse reconstruction、3D volume，适合组 3。
- `biological workflow`：动物/组织/细胞处理、成像时间线、下游分析，适合组 2/7/8。

本地证据：
- 组 1 CELLECT 主文 Fig. 1：方法框架、细胞追踪流程、显微图像和 embedding/统计混排。
- 组 3 light-field microscopy 主文 Fig. 1：物理模型、3D 重建流程、示意图与体数据同页。
- 组 5 neural network super-resolution 主文 Fig. 1：网络模块、输入输出图像、置信度/误差展示。
- 组 7 confocal scanning light-field microscopy 主文 Fig. 1：系统示意、采集流程、图像证据组合。

### 2. Dark Microscopy Image Plate

适用：荧光显微、超分辨、光片、活体成像、输入/输出图像对比。

风格要点：
- 黑底或深灰底，白色 scale bar；通道颜色优先 cyan/magenta/green/orange/blue。
- 统一裁剪比例、scale bar、亮度范围和 panel 间距。
- 图像板旁边放最少量定量图：profile、line scan、SNR、resolution、error、time trace。
- 图像处理必须可追溯；不要局部增强或选择性美化。

本地证据：
- 组 3 主文 Fig. 2-5 与补充 Fig. 1-26：3D 体数据、切片、line profile、误差图组合。
- 组 4 主文 Fig. 1-5、Extended Data Fig. 1-10、补充 Fig. 1-28：大幅暗底显微 hero panel 加分辨率/时间序列统计。
- 组 5 主文/Extended Data/补充图：蓝色、绿色、洋红图像板与置信度/误差统计并置。
- 组 6 主文 Fig. 1-5 和补充 Fig. 1-34：输入/输出/去噪/超分对照网格。
- 组 7 主文 Fig. 2-6 和补充 Fig. 1-21：活体时间序列、绿色/紫色/蓝色通道与曲线组合。

### 3. Statistical Evidence Block

适用：性能比较、消融实验、参数敏感性、样本组比较。

风格要点：
- 优先用 strip/box/violin + summary，而不是只给柱状图。
- 使用浅灰网格或无网格；轴线细，tick 少。
- 每个统计 panel 必须有单位、n、error definition 和统计检验说明。
- 分类颜色控制在 3-6 个主色，避免饱和红绿对冲。

本地证据：
- 组 1 主文/补充：tracking performance、embedding、bar/line/scatter 组合。
- 组 2 主文/补充：跨脑区 trace、heatmap、scatter、box/strip 小图密集组合。
- 组 5 主文/Extended Data：置信度、误差、时间稳定性和模型比较。

### 4. Neural Dynamics / Brain-Wide Activity Panel

适用：神经活动、嗅觉刺激响应、跨脑区动态、功能连接或分类表现。

风格要点：
- 以 `stimulus/event -> trace matrix -> region map -> summary statistic` 组织。
- trace 使用统一时间轴和共享 y 轴范围；条件太多时改用 heatmap 或分面。
- 脑区/区域图使用一致颜色映射，legend 放在图外或右侧。
- connectivity、classification、confusion-like matrix 必须标明行列含义和归一化方式。

本地证据：
- 组 2 主文 Fig. 1-5：brain region schematic、odor response traces、activity heatmaps、region-level statistics 同页组合。
- 组 2 Supplementary Fig. 1-16：多脑区、多刺激、多指标 small multiples。

### 5. Spatial Omics / Morphology Map

适用：组织切片、空间转录组、形态学特征、embedding 和 clustering。

风格要点：
- 同页放组织原图、mask/segmentation、embedding、cluster map、heatmap 和代表性形态网格。
- 颜色用于类别或空间区域时，必须有 legend；连续量用 perceptually uniform colormap。
- 组织图像不要过暗；需要能看见结构边界和定位。
- 推荐 recipe：`histology tile -> segmentation/mask -> embedding/scatter -> morphology gallery -> heatmap -> region-level stats`。

本地证据：
- 组 8 MUSE 主文 Fig. 1-6、Extended Data Fig. 1-6：组织图、scatter/embedding、heatmap、形态网格和区域对比同页组织；contact sheet p4/p6/p8/p9/p15-p23 显示 tissue section、morphology thumbnails、cluster map 和 region comparison 的复合版式。

### 6. Supplementary Validation Matrix

适用：补充图、消融、鲁棒性、更多样本、更多时间点。

风格要点：
- 一页一条验证主题，图号标题必须说明验证目的。
- 按行列固定条件；同类面板共享轴范围或 color scale。
- 文字图例较长可以在图下，但图内标签仍要短且英文。
- 如果一个 Supplementary Fig. 跨页，保持同一逻辑图号，不要误拆。

本地证据：
- 组 1 Supplementary Fig. 1-20：tracking/embedding/segmentation validation、树状/流程、空间切片、小型柱状/曲线。
- 组 2 Supplementary Fig. 1-16：neural dynamics trace matrices、brain maps、odor condition small multiples。
- 组 3 Supplementary Fig. 1-26：3D reconstruction robustness、参数/噪声/视角、dark image grids、profile/error maps。
- 组 4 Supplementary Fig. 1-28：SR microscopy 和光片系统验证，暗底图像矩阵与 resolution/time profiles。
- 组 5 Supplementary Fig. 1-20：confidence/uncertainty、input-output grid、Extended Data 关联验证。
- 组 6 Supplementary Fig. 1-34：denoising/SR 长链条验证，适合 input-output comparison matrix。
- 组 7 Supplementary Fig. 1-21：intravital imaging、时间序列、绿色/紫色通道、动物/组织应用验证。

## Per-Paper Supplementary Taxonomy

| 类型 | 对应组 | 推荐模板 |
|---|---|---|
| Tracking / embedding validation | 1 | `workflow detail -> segmentation/tracking examples -> embedding/scatter -> performance bars/lines` |
| Neural dynamics validation | 2 | `stimulus traces -> brain/region map -> heatmap matrix -> region statistics` |
| 3D reconstruction robustness | 3 | `input views -> reconstructed volume/slices -> line profile -> error map -> metric table` |
| SR microscopy / optical validation | 4, 5, 6 | `raw/input -> output/reconstruction -> zoom-in -> profile/error/confidence -> sample matrix` |
| Intravital long-term validation | 7 | `time grid -> channel overlay -> motion/quality metric -> animal/tissue context` |
| Spatial morphology validation | 8 | `tissue tile -> morphology thumbnails -> embedding/cluster -> heatmap -> region statistic` |
| Tables / parameter summaries | 1-7 | compact table; avoid turning table into decorative heatmap unless comparison is the message |

## 推荐基础调色板

```python
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
```

连续 colormap：`viridis`、`magma`、`cividis`、`inferno`。避免 `jet` / rainbow。
