---
name: nature-publication-submission-qa
description: Nature-family submission readiness QA skill. Use when auditing a manuscript package before initial submission, revision, acceptance, or final production upload for Nature, Nature Methods, Nature Biotechnology, Nature Communications, or related journals; triggers include 投稿前检查, submission checklist, final files, reporting summary, data/code availability, image integrity, statistics, Extended Data, Supplementary Information, figure legends, declarations, or AI use.
---

# Nature Publication Submission QA

本 skill 用于审计 Nature-family 投稿包是否具备可提交、可复核、可生产的基本条件。说明文字使用中文；若涉及图表本体，图内文字仍必须使用英文。

## 调用后先做三件事

1. 写一行投稿审计契约：`target journal -> submission stage -> files available -> risk areas -> missing inputs`。
2. 按阶段读取 reference：
   - 投稿文件与阶段清单：`references/submission-readiness-checklist.md`
   - 图像、图表和可访问性：`references/figure-and-image-integrity.md`
   - 数据、代码、统计和 AI 使用：`references/data-code-reporting.md`
   - Extended Data 与 Supplementary consistency：`references/supplementary-consistency.md`
3. 输出结论必须分成 `Ready`、`Conditional`、`Do not approve`。证据文件、原始图像、统计定义、数据/代码 accession、伦理/声明或 AI 使用说明缺失时，必须列入 `Missing inputs`；不得把未知内容当作已满足。

## 默认审计顺序

1. 判定阶段：initial submission、revision、accepted in principle、final production upload 的要求不同；先确认目标期刊和阶段。
2. 建立 file inventory：主文、主图、Extended Data、Supplementary Information、表格、Reporting Summary、声明表单、数据/代码说明、原始图像或处理记录。
3. 交叉审计主文和图：每个主文结论应能追溯到 figure/table/panel；每个 figure legend 应定义 panel、样本量、误差、统计和 scale bar。
4. 审计图像完整性：检查裁剪、拼接、局部增强、伪彩、LUT、scale bar、原始文件、软件和处理说明。
5. 审计数据/代码/统计：Data availability、Code availability、repository accession、统计模型、排除标准、重复数和 AI use 声明。
6. 审计补充材料：Supplementary Information 与 Extended Data 不应重复、错号、缺交叉引用或混入应作为 Extended Data 的额外图。
7. 输出缺口清单：按 `blocker / major / minor` 分级，并给出需要作者补充的具体文件或文字。

## 硬门槛

- 没有源文件或用户明确说明的投稿阶段时，不给最终批准，只能给条件审计。
- 图像数据缺原始文件、关键处理说明或 scale bar 时，不批准图像相关 panel。
- 统计结论缺 n、误差定义、检验方法或多重比较说明时，不批准相应 claim。
- Data availability、Code availability、Reporting Summary、competing interests、author contributions、funding 和 AI use 的适用项缺失时，不批准整包提交。
- 不替作者编 accession、样本量、伦理编号、软件版本、统计显著性、声明文本或未提供的补充材料。

## 输出格式

使用以下结构，便于作者逐项修复：

1. `Submission status`：Ready / Conditional / Do not approve。
2. `Blocking gaps`：提交前必须补齐的文件、说明或证据。
3. `Cross-file consistency`：主文、图、Extended Data、Supplementary Information、数据/代码声明之间的错配。
4. `Figure and image integrity`：图像处理、scale bar、字体、RGB/矢量/可编辑性、accessibility 和 alt text 风险。
5. `Statistics and reporting`：n、误差、统计检验、重复、Reporting Summary、Data availability、Code availability、AI use。
6. `Action list`：作者下一轮需要提供或修改的最小清单。

## 禁止事项

- 不要把“语言润色通过”当成“投稿 QA 通过”。
- 不要只看主文，不检查图例、补充材料、数据/代码和声明。
- 不要用本 skill 代替目标期刊的实时作者指南；政策、格式和表单要求可能变化，投稿前必须核验当前官方页面。
- 不要把 Supplementary Information 当成额外主图仓库；需要按期刊规则区分 Extended Data、Supplementary figures/tables 和 SI 文件。
