# Figure And Image Integrity

本文件用于投稿 QA 中的图像、图表、显微图、图例和 accessibility 审计。图表绘制细节可同时调用 `nature-publication-figure`。

## 来源

- Nature final submission: <https://www.nature.com/nature/for-authors/final-submission>，2026-06-24 核验。
- Nature Portfolio image integrity and standards: <https://www.nature.com/nature-portfolio/editorial-policies/image-integrity>，2026-06-24 核验。
- Springer Nature accessibility requirements for figures, images and supplementary materials: <https://www.springernature.com/gp/policies/accessibility-figures-images>，2026-06-24 核验。
- Springer Nature AI guidance: <https://www.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities>，2026-06-24 核验。

## 必查项目

| Area | Check | Blocker example |
| --- | --- | --- |
| scale bars | 显微图、空间图和局部放大图必须有 scale bars、单位和对应 pixel size/FOV 依据 | 图例说 10 um，但没有像素尺寸或原图 metadata |
| image integrity | 裁剪、拼接、对比度、gamma、伪彩、LUT、deconvolution、projection、filtering、thresholding 都要可说明 | 局部增强只作用于一个 ROI，却未披露 |
| raw images | 关键显微图/gel/blot 应有 raw files、metadata、unprocessed scans 或处理记录 | 只有压缩 PNG，没有原始图像或处理链 |
| generative AI | 不把生成式 AI 产物当作实验图像；非生成式 ML 图像处理/增强/合成需披露 | AI 修复缺失结构、生成细胞图或改变数据解释 |
| RGB | 在线彩色图优先检查 RGB；Extended Data 的在线图尤其要避免不必要 CMYK 转换 | fluorescent channel 因 CMYK 转换失去可区分性 |
| editable | 线图、流程图和带文字的复合图应保留 editable vector/text/layers，不应把文字全部 rasterize 或 outline | 只有扁平化低分辨率截图 |
| accessibility | 图内文字可读、颜色可区分、alt text/说明覆盖 main 和 Extended Data figures | 红绿作为唯一编码，且没有形状/标签冗余 |

## 图例审计

每张 figure legend 至少检查：

1. 第一短句是否说明整图结论。
2. 每个 panel label 是否存在且与图内一致。
3. 图例是否解释符号、颜色、缩写、scale bars、样本量、误差和统计。
4. 图像处理是否在 legend 或 Methods 中交代；特别是 pseudo-colouring、nonlinear adjustment、channel-specific adjustment、projection、deconvolution、filtering、thresholding。
5. 图内文字是否全英文，字体和大小是否适合目标版面。

## 审计输出模板

```text
Figure X status: Ready / Conditional / Do not approve
Evidence checked: [files, raw data, legend, methods]
Integrity risks: [crop/splice/enhancement/LUT/AI/vector/accessibility]
Required author action: [exact file or sentence needed]
```

## 不批准条件

- 缺 scale bar 或无法证明 scale bar 对应原图尺度。
- 图像处理可能改变解释，但没有处理说明或原始文件。
- generative AI 或非生成式 ML 图像处理影响图像内容，但未披露。
- 关键统计图没有数据来源、n、误差或统计定义。
- 生产文件不可编辑、分辨率不足或图内文字不可读，且没有替代源文件。
