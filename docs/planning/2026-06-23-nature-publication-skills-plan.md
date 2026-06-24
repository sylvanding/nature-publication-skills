# Nature Publication Skills Plan

日期：2026-06-23。

## 目标

基于 `references-papers-dai-tsinghua/` 中 8 组 Nature-family 论文和补充材料，开发可供 agent 使用的中文 skills，覆盖论文文字写作风格和图表绘制风格。正式图表和示例图内文字必须使用英文，避免中文乱码。

## 规划

采用“三个核心 skill + 共享证据层 + 校验脚本”的结构：

- `skills/nature-publication-writing/`：论文写作、图例、补充材料文字。
- `skills/nature-publication-figure/`：多面板图、显微图像板、统计图、流程图、空间组学图、导出和 QA。
- `skills/nature-publication-submission-qa/`：投稿前 readiness QA、图像完整性、统计报告、数据/代码可用性、Extended Data 与 Supplementary consistency。
- `references/`：本地论文索引、figure audit register、外部来源。
- `scripts/`：技能结构校验、PDF 图号 inventory、contact sheet、palette 分析。

## 审计

- 仓库初始状态只有 `README.md` 被跟踪，`references-papers-dai-tsinghua/` 为未跟踪原始 PDF 目录。
- 子 Agent 完成仓库结构审计、论文 PDF 清单、外部 skills 仓库调研。
- 主线程使用 PyMuPDF/PIL 生成全部 15 个 PDF 的页面 contact sheets，并逐组视觉审计主图、Extended Data 和补充图的图型/配色/版式。

## 执行

- 写作 skill 使用中文说明和 evidence-first 工作流。
- 图表 skill 强化图内英文硬约束、Python 默认工具链、显微图像板、Supplementary validation matrix 和 QA。
- 所有脚本注释和 CLI 输出使用英文。

## 验证

必须运行：

```bash
python scripts/validate_skills.py
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
python scripts/check_style_coverage.py
git diff --check
```
