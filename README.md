# nature-publication-skills

面向 Nature Portfolio / Nature-family 论文写作、图表绘制和投稿前 QA 的 Agent Skills。当前版本基于 `references-papers-dai-tsinghua/` 中 8 组本地论文及补充材料、Nature/Springer Nature 官方作者指南，以及公开 Agent Skills 规范整理。Skills 使用中文说明；正式图表和示例图内文字必须使用英文。

## Quickstart

在当前仓库使用 Codex 时不需要安装：仓库已提供 `.agents/skills/` 软链接，Codex 会在仓库根目录或子目录发现这三个 skills。

安装到个人 Codex 环境：

```bash
python -m pip install -r requirements.txt
python scripts/install_skills.py install --agent codex --scope user --mode symlink
python scripts/install_skills.py status --agent codex --scope user
```

从 GitHub 临时安装到个人 Codex 环境：

```bash
npx github:sylvanding/nature-publication-skills install --agent codex --scope user --mode copy --force
```

详细安装、更新、Claude Code 和 GitHub CLI 说明见 [docs/installation.md](docs/installation.md)；分发、release 和 package 边界见 [docs/distribution.md](docs/distribution.md)。

## Which Skill To Use

| Skill | 何时使用 | 关键资源 |
| --- | --- | --- |
| `nature-publication-writing` | 撰写或审计标题、摘要、引言、结果、讨论、方法、图例、补充材料文字 | [section-and-legend-playbook.md](skills/nature-publication-writing/references/section-and-legend-playbook.md), [rubric.md](skills/nature-publication-writing/references/benchmarks/golden/writing/rubric.md) |
| `nature-publication-figure` | 绘制或审计显微图像板、多 panel 主图、统计图、方法示意图、Supplementary figure matrix | [figure-template-catalog.md](skills/nature-publication-figure/references/figure-template-catalog.md), [qa-and-export.md](skills/nature-publication-figure/references/qa-and-export.md) |
| `nature-publication-submission-qa` | 投稿前或 final upload 前审计主文、主图、Extended Data、Supplementary Information、统计、图像完整性、数据/代码可用性和 AI use | [submission-readiness-checklist.md](skills/nature-publication-submission-qa/references/submission-readiness-checklist.md), [data-code-reporting.md](skills/nature-publication-submission-qa/references/data-code-reporting.md) |

## Install Mode Decision Table

| 场景 | 推荐命令 | 原因 |
| --- | --- | --- |
| 当前仓库内开发或使用 | 无需安装，使用 `.agents/skills/` | 本仓库已有 repo-scoped symlink |
| 个人长期使用 | `python scripts/install_skills.py install --agent codex --scope user --mode symlink` | `git pull` 后 skill 自动更新 |
| 安装到其他项目 | `python scripts/install_skills.py install --agent codex --scope repo --repo /path/to/repo --mode symlink` | 目标项目可发现同一份源码 |
| npx 临时安装 | `npx github:sylvanding/nature-publication-skills install --agent codex --scope user --mode copy --force` | 临时包路径不稳定，copy 比 symlink 更安全 |
| Claude Code | `python scripts/install_skills.py install --agent claude --scope user --mode symlink` | 写入 Claude Code skill discovery path |

## Evidence And Provenance

- [references/source-paper-index.md](references/source-paper-index.md)：本地 15 个 PDF 的题名、DOI、图号覆盖和路径索引。
- [references/figure-audit-register.md](references/figure-audit-register.md)：主图、Extended Data、Supplementary figures 和表格的覆盖登记。
- [references/figure-style-rule-map.md](references/figure-style-rule-map.md)：本地论文图型到 figure skill 规则的映射。
- [references/pdf-hash-manifest.md](references/pdf-hash-manifest.md)：本地参考 PDF 的 SHA256 和页数清单。
- [references/external-sources.md](references/external-sources.md)：外部规范、Nature/Springer Nature 政策和 skills 仓库来源，包含访问日期。
- 每个 skill 的 `references/` 目录包含该 skill 直接使用的风格图谱、工作流或投稿 QA 来源。

`references-papers-dai-tsinghua/` 是用户提供的原始参考材料目录，体积较大，作为本地证据输入使用，不进入 git。审计脚本会把临时图像和清单写入 `.audit/`，该目录也不进入 git。

## Validation Matrix

Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Portable release checks（源码 checkout 和 npm package 内容都应具备这些文件）：

```bash
python scripts/validate_skills.py
python scripts/validate_figure_v2.py
python scripts/validate_figure_templates.py
python scripts/validate_writing_benchmark.py
python scripts/validate_submission_qa.py
python scripts/validate_docs_productization.py
python scripts/validate_distribution.py
python scripts/check_style_coverage.py
npm pack --dry-run
```

Source checkout-only checks（`Harness/**` 和 git metadata 不随 npm package 分发）：

```bash
node Harness/scripts/validate-harness.mjs --strict
git diff --check
```

本地 PDF 存在时运行证据重建：

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
```

安装 smoke：

```bash
python scripts/install_skills.py install --agent codex --scope repo --repo .audit/install-smoke --mode symlink --dry-run
node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo .audit/install-smoke --dry-run
```

## Roadmap Completion

- Harness bootstrap closeout：`Harness/PLAN.md` 记录当前 WF 状态和验证证据。
- Figure skill v2：图表风格、配色、panel composition、toolchain 和 QA 分离到 figure skill references。
- Paper evidence coverage：`references/figure-style-rule-map.md` 将本地论文图型映射到 skill 规则。
- Figure template library：`skills/nature-publication-figure/templates/` 和 `scripts/` 提供可运行模板。
- Writing benchmark：`skills/nature-publication-writing/references/benchmarks/` 提供 prompts 和 rubric。
- Distribution polish：`docs/distribution.md` 和 `scripts/validate_distribution.py` 维护 package/install 边界。
- Submission QA skill：`skills/nature-publication-submission-qa/` 覆盖投稿前 readiness 审计。
- Docs productization：本 README、安装文档、分发文档和验证矩阵保持同步。

## Update And Release Workflow

更新个人 symlink 安装：

```bash
git pull --ff-only
python scripts/install_skills.py update --agent codex --scope user --mode symlink
python scripts/install_skills.py status --agent codex --scope user
```

发布前检查：先运行上面的完整 Validation Matrix；如果是在源码 checkout 中发布，还要运行 source checkout-only checks。最小重复命令如下：

```bash
python scripts/validate_skills.py
python scripts/validate_figure_v2.py
python scripts/validate_figure_templates.py
python scripts/validate_writing_benchmark.py
python scripts/validate_submission_qa.py
python scripts/validate_docs_productization.py
python scripts/validate_distribution.py
python scripts/check_style_coverage.py
node Harness/scripts/validate-harness.mjs --strict
git diff --check
npm pack --dry-run
```

不要发布 `.audit/**`、`references-papers-dai-tsinghua/**`、本地 tarball 或内部 `docs/superpowers/**` 执行计划。
