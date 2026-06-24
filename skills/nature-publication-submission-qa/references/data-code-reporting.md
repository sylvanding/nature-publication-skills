# Data, Code, Statistics, Reporting, And AI Use

本文件用于审计 Nature-family 投稿包中的 Data availability、Code availability、统计报告、statistics、Reporting summary 和 AI use 声明。

## 来源

- Nature Portfolio reporting standards and availability of data, materials, code and protocols: <https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards>，2026-06-24 核验。
- Nature formatting guide: <https://www.nature.com/nature/for-authors/formatting-guide>，2026-06-24 核验。
- Springer Nature AI guidance: <https://www.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities>，2026-06-24 核验。

## Data availability

审计时不要只检查是否有一句声明，还要检查：

- 关键数据是否能支持主文和 figure 的主要结论。
- 是否给出 repository、accession、DOI、record URL、限制访问理由或受控访问流程。
- 是否把领域强制 repository 与通用 repository 区分清楚。
- 是否解释无法公开的数据、受限人类数据、第三方数据或材料限制。
- 是否与 Supplementary Information、Methods 和 figure source data 一致。

## Code availability

Code availability 至少要覆盖：

- 自研算法、训练/推理代码、数据处理脚本、统计脚本、figure generation scripts。
- repository URL、release/tag/commit、license、依赖、运行环境、随机种子和输入数据路径。
- 若代码不能公开，给出具体限制和可获得方式；不要写成空泛承诺。

## Statistics

每个统计 claim 和 figure legend 检查：

- n 的含义：biological replicates、technical replicates、cells、fields、animals、patients、images、experiments。
- 误差定义：s.d.、s.e.m.、confidence interval、interquartile range 等。
- 检验方法、单双侧、多重比较、配对/非配对、正态性或非参数选择依据。
- 随机化、盲法、样本排除、重复实验、预设终点和 effect size 是否适用。
- 统计软件和版本是否在 Methods 或 Reporting Summary 中可见。

## Reporting Summary

按研究类型检查目标期刊要求的 Reporting Summary 或 reporting checklist。最小审计包括：

- study design、sample size、replication、randomization、blinding。
- data exclusions、inclusion/exclusion criteria、statistical methods。
- reagent/material details、software、protocols。
- 与 Methods、figure legends、Data availability 和 Code availability 是否一致。

## AI use

AI use 审计分三类：

- AI-assisted copy editing：通常不需要声明，但作者仍需负责最终内容。
- 生成式 AI 参与写作、分析、图像或内容生成：需要按当前 Springer Nature/Nature Portfolio 指南核验声明位置和范围。
- 非生成式 ML 用于图像处理、增强、合成、分割或重建：若影响图像/figure 内容，应在 caption、Methods 或投稿材料中披露以便编辑个案审查。

## Do not approve 条件

- Data availability 或 Code availability 缺失、空泛或与主文结论不匹配。
- 统计结论缺 n、误差、检验方法或重复定义。
- Reporting Summary 与 Methods/figures 不一致。
- AI use 声明缺失，且材料显示 AI 工具参与了文本之外的内容生成、图像处理或分析。
- 关键数据/代码 accession 被写成待补，且该 accession 支撑主要结论。
