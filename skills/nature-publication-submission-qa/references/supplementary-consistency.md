# Supplementary Consistency

本文件用于审计 Supplementary Information、Extended Data、补充表格、补充影片/数据文件与主文之间的一致性。

## 来源

- Nature final submission: <https://www.nature.com/nature/for-authors/final-submission>，2026-06-24 核验。
- Nature formatting guide: <https://www.nature.com/nature/for-authors/formatting-guide>，2026-06-24 核验。
- Nature Portfolio reporting standards: <https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards>，2026-06-24 核验。

## 角色边界

| Material | 应承担的角色 | 常见风险 |
| --- | --- | --- |
| Extended Data | 支撑主文结论的在线 display items，如额外验证、方法细节、关键对照 | 主文引用 ED Fig. 3，但文件名/legend 仍是旧编号 |
| Supplementary Information | 直接相关但因篇幅或媒介不能放入印刷版的材料，如 supplementary notes、tables、movies | 把额外 figure 堆进 SI，而不是按期刊规则做 Extended Data |
| Supplementary tables/files | 大表、清单、参数、数据字典、材料列表 | 表号、列名、单位和主文不一致 |
| Source data/code links | 可复核数据和脚本 | accession、DOI、文件名和 Methods 不一致 |

## 一致性检查

1. 建立 file inventory：文件名、版本、用途、主文引用位置、对应 figure/table/panel。
2. 检查所有 cross-reference：主文、Methods、figure legends、Extended Data legends、Supplementary Information 中的编号必须一一对应。
3. 检查 panel labels：图内 a/b/c、legend、主文引用和补充说明必须一致。
4. 检查术语与缩写：方法名、模型名、样本组名、通道名、单位和颜色编码在主文、图、SI 中一致。
5. 检查统计和数据来源：SI 中的额外分析不能引入未声明的数据处理、样本排除或新统计口径。
6. 检查文件大小和格式风险：final production 阶段需要单独确认 Extended Data、tables、movies 和 SI 文件符合目标期刊当前要求。

## 审计表模板

| Item | Seen in manuscript | Seen in figure/ED/SI | Status | Required action |
| --- | --- | --- | --- | --- |
| Claim or reference | Section/paragraph | File/panel/table | Ready / Conditional / Do not approve | Precise fix |

## Do not approve 条件

- Supplementary 或 Extended Data 文件缺失，而主文或图例引用了它。
- Extended Data 和 Supplementary 的边界混乱，导致读者无法找到关键验证。
- panel labels、figure numbers、table numbers 或 cross-reference 错配。
- file inventory 缺失，无法确认哪一版文件是最终提交版本。
- SI 中包含影响主结论的新分析，但主文、Methods、Statistics 或 Data availability 没有同步说明。
