# nature-publication-skills

面向 Nature Portfolio / Nature-family 论文写作与绘图的 Agent Skills。当前版本基于
`references-papers-dai-tsinghua/` 中 8 组本地论文及补充材料、Nature/Springer Nature
官方作者指南，以及公开 Agent Skills 规范整理。

## Skills

- `skills/nature-publication-writing/`：中文说明的 Nature-family 论文写作 skill，覆盖摘要、引言、结果、讨论、方法、图例和补充材料文字。
- `skills/nature-publication-figure/`：中文说明的 Nature-family 图表绘制与审计 skill，重点覆盖显微图像板、方法流程图、统计图、空间组学图和 Supplementary figure matrix。所有示例图表与图内文本必须使用英文。

本仓库还提供 `.agents/skills/` 软链接，所以在仓库根目录或子目录启动 Codex 时可直接发现这两个 skills。

## Evidence

- `references/source-paper-index.md`：本地 15 个 PDF 的题名、DOI、图号覆盖和路径索引。
- `references/figure-audit-register.md`：主图、Extended Data、Supplementary figures 和表格的覆盖登记。
- `references/pdf-hash-manifest.md`：本地参考 PDF 的 SHA256 和页数清单。
- `references/external-sources.md`：外部规范与 skill 仓库来源，包含访问日期。
- 每个 skill 的 `references/` 目录包含该 skill 直接使用的风格图谱和工作流。

## Install And Update

详细说明见 `docs/installation.md`。

推荐个人开发方式：保留一个稳定 clone，然后用 symlink 安装。源码更新后，安装位置自动看到新内容。

```bash
python scripts/install_skills.py install --agent codex --scope user --mode symlink
git pull --ff-only
python scripts/install_skills.py update --agent codex --scope user --mode symlink
python scripts/install_skills.py status --agent codex --scope user
```

安装到某个项目仓库：

```bash
python scripts/install_skills.py install --agent codex --scope repo --repo /path/to/target-repo --mode symlink
```

从 GitHub 用 `npx`：

```bash
npx github:sylvanding/nature-publication-skills install --agent codex --scope user --mode copy --force
```

## Validation

Python dependencies:

```bash
python -m pip install -r requirements.txt
```

```bash
python scripts/validate_skills.py
python scripts/validate_figure_v2.py
python scripts/validate_figure_templates.py
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
python scripts/check_style_coverage.py
python scripts/install_skills.py install --agent codex --scope repo --repo .audit/install-smoke --mode symlink --dry-run
node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo .audit/install-smoke --dry-run
npm pack --dry-run
```

`references-papers-dai-tsinghua/` 是用户提供的原始参考材料目录，体积较大，作为本地证据输入使用。
审计脚本会把临时图像和清单写入 `.audit/`，该目录不进入 git。
