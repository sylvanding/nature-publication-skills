# Distribution And Release

本文件用于维护 `nature-publication-skills` 的分发边界。安装命令见 `docs/installation.md`；本文件关注 npm/npx、Codex Plugin、GitHub CLI、release checklist 和 Update safety。

## Distribution Surfaces

| Surface | 用途 | 推荐模式 |
| --- | --- | --- |
| Codex repo install | 当前项目直接使用 `.agents/skills` | symlink |
| Codex user install | 个人全局使用 `~/.agents/skills` | symlink for clone, copy for npx |
| Claude Code install | 用户或项目 `.claude/skills` | symlink for clone, copy for npx |
| npx | 从 GitHub 临时执行 installer | copy |
| Codex Plugin | 多 skill 作为一个 bundle 分发 | package with `.codex-plugin/plugin.json` |
| GitHub CLI `gh skill` | GitHub CLI skill install/update flow | public preview; verify current `gh` version first |

## npm / npx Package Boundary

The package must include:

- `.codex-plugin/plugin.json`
- `bin/nature-publication-skills.mjs`
- `docs/installation.md`
- `docs/distribution.md`
- `docs/planning/**`
- `references/**`
- `scripts/**`
- `skills/**`
- `README.md`
- `requirements.txt`

The package must not include:

- `docs/superpowers/**` internal execution plans
- `.audit/**` generated smoke/audit outputs
- `references-papers-dai-tsinghua/**` source PDFs
- local tarballs or temporary install roots

Verify with:

```bash
npm pack --dry-run
python scripts/validate_distribution.py
```

## Codex Plugin

The Codex Plugin manifest lives at `.codex-plugin/plugin.json`. Keep `"skills": "./skills/"` so the plugin carries complete skill folders, including each skill's `SKILL.md`, `references/`, `scripts/`, `templates/`, `assets/`, and `agents/openai.yaml`.

When adding a new skill:

1. Add the skill folder under `skills/`.
2. Add or update repo-scoped `.agents/skills` links if needed.
3. Update `.codex-plugin/plugin.json` description/default prompts if the new skill changes user-visible capability.
4. Run `python scripts/validate_distribution.py` and `npm pack --dry-run`.

## GitHub CLI `gh skill`

GitHub CLI skill commands are public preview, subject to change, and version-sensitive. Before documenting exact user-facing `gh skill` behavior as verified, run:

```bash
gh --version
gh skill --help
```

Current guidance may include:

```bash
gh skill install sylvanding/nature-publication-skills
gh skill install sylvanding/nature-publication-skills nature-publication-figure --agent codex
gh skill update --all
```

If the local `gh` version lacks `gh skill`, label the command path as externally documented but not locally verified. Recommend inspecting skill contents before installation.

## Release checklist

Run before tagging or announcing a release:

```bash
python scripts/validate_skills.py
python scripts/validate_figure_v2.py
python scripts/validate_figure_templates.py
python scripts/validate_writing_benchmark.py
python scripts/validate_distribution.py
python scripts/check_style_coverage.py
node Harness/scripts/validate-harness.mjs --strict
git diff --check
npm pack --dry-run
```

Optional when local PDFs are present:

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
```

## Update safety

- Prefer `git pull --ff-only` for source clones so local edits are not silently overwritten.
- Prefer `--mode symlink` for personal development clones.
- Prefer `--mode copy --force` for npx or immutable release installs.
- Run `python scripts/install_skills.py status --agent codex --scope user` before destructive reinstall.
- Use `--dry-run` before repo-scoped installs into another project.
- Do not publish or package `.audit/**` outputs or `references-papers-dai-tsinghua/**` PDFs.
