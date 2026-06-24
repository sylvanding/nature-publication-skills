# PLAN.md - Active Execution Plan

Use this file when work spans more than one step, one file, or one agent.

## Current Goal

Configure `create-harness-vibe-coding` for the existing `nature-publication-skills` repository on branch `harness-vibe-coding-bootstrap`, preserving all current project files and merging only missing Harness conventions.

## Phase

Choose one: Idea / Research / PRD / Architecture / Plan / Build / Verify / Feedback.

Current: Verify

## Heartbeat

Mode: normal
Last beat: 2026-06-24T21:23:12+08:00
Current phase: Verify
Current blocker: none
Next beat trigger: before git diff audit and commit
Failure count: 0
Recovery action: rerun the Harness validator, inspect the failing file, and patch only the reported project fact document

Update this section before long commands, after long commands, before and after subagent handoffs, after failed verification, and before stopping for user input. In `wf-mode`, use this as the resume point after context loss or interruption.

## Progress Rules

- Phase tracks lifecycle progress.
- Task status tracks execution progress.
- Update before handoff, after verification, and when blocked.

Allowed task statuses: Pending / In Progress / Blocked / Done / Verified.

- Pending: not started.
- In Progress: active work.
- Blocked: needs user input or external change.
- Done: task complete, evidence not final.
- Verified: verification evidence is recorded.

## Success Criteria

- [x] Agent-link pre-install questions were asked and the user approved existing-project dry-run, conflict skipping, and generic Harness installation.
- [x] Existing project bootstrap used a dry-run first, then `--on-conflict skip`; the existing `README.md` conflict was preserved.
- [x] Harness project fact files describe the real skill repository instead of generic app placeholders.
- [x] `node Harness/scripts/validate-harness.mjs --strict` passes.
- [x] Existing repository validation commands still pass or any skipped heavyweight checks are explicitly recorded.
- [ ] Git commit records the Harness configuration branch state.

## Scope

Allowed write set:

- `AGENTS.md`
- `CLAUDE.md`
- `.claude/**`
- `Harness/**`
- `tests/.gitkeep`

Forbidden without explicit approval:

- Existing `README.md`
- `package.json`
- `bin/**`
- `scripts/**`
- `skills/**`
- `references/**`
- `docs/installation.md`
- `.codex-plugin/**`
- `.agents/**`
- `references-papers-dai-tsinghua/**`
- Generated `.audit/**`

## Loaded Context

Keep this list short. Add only docs/files used for the current phase.

- `https://github.com/zingspark/create-harness-vibe-coding`
- `AGENTS.md`
- `CLAUDE.md`
- `Harness/SETUP.md`
- `Harness/MEMORY.md`
- `Harness/README.md`
- `Harness/lifecycle.md`
- `Harness/research/README.md`
- `Harness/extension.md`
- `README.md`
- `docs/installation.md`
- `package.json`
- `.codex-plugin/plugin.json`
- `.gitignore`
- `scripts/install_skills.py`
- `scripts/validate_skills.py`
- `bin/nature-publication-skills.mjs`
- `references/external-sources.md`

## Project Facts Discovered Before Editing

- The repository is an Agent Skills source and distribution repo, not a web app or service.
- The source skills are `skills/nature-publication-writing/` and `skills/nature-publication-figure/`; `.agents/skills/` contains repo-scoped symlinks back to these source folders.
- Installation and update entry points are `scripts/install_skills.py` and `bin/nature-publication-skills.mjs`; they support Codex and Claude Code, user and repo scopes, and symlink or copy modes.
- Evidence and policy sources are recorded in `references/*.md`; raw user-provided PDFs live under `references-papers-dai-tsinghua/` and are intentionally git-ignored.
- Temporary audit outputs live under `.audit/` and are intentionally git-ignored.
- `package.json` exposes the `nature-publication-skills` npm bin but has no npm test script.
- No `.github/` workflow files were present during bootstrap.
- `README.md` is the project-facing command source of truth; the Harness generator reported it as the only conflict and skipped it.

## Tasks

| # | Task | Owner | Verify | Status |
| --- | --- | --- | --- | --- |
| 1 | Ask Agent-link intake questions before editing | main | user approval in chat | Done |
| 2 | Create branch `harness-vibe-coding-bootstrap` from `develop-nature-publication-skills` | main | `git branch --show-current` | Done |
| 3 | Run existing-project dry-run | main | `npx --yes create-harness-vibe-coding@latest nature-publication-skills . -y --dry-run --json` | Done |
| 4 | Generate missing Harness files while preserving conflicts | main | `npx --yes create-harness-vibe-coding@latest nature-publication-skills . -y --on-conflict skip` | Done |
| 5 | Audit local project facts before editing Harness docs | main | read files listed in Loaded Context | Done |
| 6 | Replace project placeholders in strict validator scope | main | `rg -n "\\{\\{" Harness/PLAN.md Harness/research/PRD.md Harness/research/research-results.md Harness/architecture.md Harness/domain/ports.md` | Verified |
| 7 | Run Harness and repo verification | main | commands in Verification table | Verified |
| 8 | Review diff and commit | main | `git diff --check`, `git status --short`, `git commit` | Pending |

## Parallel Dispatch

Use [subagents.md](subagents.md) and [dispatch.md](dispatch.md) when more than one agent or bounded pass is useful.

| Task | Agent | Mode | Read Set | Write Set | Depends On | Output | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Harness merge audit | explorer subagent `Aquinas` | Parallel Read | `Harness/**`, root project metadata, generated files | none | generation complete | read-only risk and verification checklist | Done |

## Subagent Synthesis

Agents used: `Aquinas` read-only explorer
Findings accepted: strict validator checks only `PLAN.md`, `PRD.md`, `research-results.md`, `architecture.md`, and `ports.md`; `architecture.md` needed real repository architecture despite having no literal placeholders; ports should document command/filesystem boundaries rather than invented Python interfaces; `README.md` must remain preserved.
Findings rejected: none; the recommendation to restrict the post-generation edit scope to project fact files was applied after scaffold generation, while generated `AGENTS.md`, `CLAUDE.md`, `.claude/**`, `Harness/**`, and `tests/.gitkeep` remain the intentionally added Harness scaffold.
Conflicts: none yet
Decisions: main agent retained write ownership of Harness project fact files
Next write set: final `Harness/PLAN.md` verification update only
Verification path: strict Harness validator, repo skill validator, style coverage checker, install/status smoke checks, PDF audit scripts, npm pack, diff check
Residual risk: `Harness/SETUP.md` remains intentionally present until the user accepts this configured baseline or a later feature slice verifies normal mode

## Agent Handoffs

| Agent | Role | Context Pack | Result |
| --- | --- | --- | --- |
| Aquinas | Read-only Harness reviewer | Current repo path, bootstrap goal, strict validator scope, conflict-preservation rule | Confirmed strict placeholder scope, advised real project architecture and command/filesystem port contracts, found no overwrite requirement |

## Decisions

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-24 | Treat the repo as an existing project, not a new blank app | Current files already define skills, install flow, validation, and evidence sources |
| 2026-06-24 | Preserve root `README.md` and keep build/test commands there | The generator reported `README.md` as the only conflict, and its README says project commands belong in README rather than `CLAUDE.md` |
| 2026-06-24 | Install generic Harness only; defer optional React, Playwright, and ECC stack workflows | The project is a documentation and CLI skills repository with no frontend app |
| 2026-06-24 | Keep `Harness/SETUP.md` during this bootstrap commit | The user explicitly asked to follow it; deletion can happen after the user accepts this configured baseline or a later feature slice verifies normal mode |

## Verification

| Check | Result | Notes |
| --- | --- | --- |
| `npx --yes create-harness-vibe-coding@latest nature-publication-skills . -y --dry-run --json` | Passed | Reported 46 creates and one `README.md` conflict before edits |
| `npx --yes create-harness-vibe-coding@latest nature-publication-skills . -y --on-conflict skip` | Passed | Created 46 files and skipped existing `README.md` |
| `node Harness/scripts/validate-harness.mjs` | Passed | Non-strict scaffold validation passed before project fact replacement |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict placeholder scope passed after project fact replacement |
| `python scripts/validate_skills.py` | Passed | Skill structure, metadata, links, dependencies, and figure code language checks passed |
| `python scripts/check_style_coverage.py` | Passed | Style coverage check passed |
| `python scripts/install_skills.py install --agent codex --scope repo --repo .audit/install-smoke --mode symlink --dry-run` | Passed | Printed intended symlink installs and metadata write without modifying tracked files |
| `node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo .audit/install-smoke --dry-run` | Passed | Exited 0; dry-run status reads target state and does not create missing links |
| `tmp=$(mktemp -d); python scripts/install_skills.py install --agent codex --scope repo --repo "$tmp" --mode symlink; node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo "$tmp"; rm -rf "$tmp"` | Passed | Real temp repo install created both symlinks and status reported both correctly |
| `python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json` | Passed | Wrote 15 PDF records |
| `python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json` | Passed | Wrote palette summaries for 15 PDFs |
| `python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets` | Passed | Wrote contact sheets for all 15 local PDFs |
| `npm pack --dry-run` | Passed | Reported tarball contents for `nature-publication-skills@0.2.0` |
| `git diff --cached --check` | Passed | Staged whitespace check passed |
| `npx --yes create-harness-vibe-coding@latest nature-publication-skills . -y --dry-run --json --on-conflict skip` | Passed | Idempotency dry-run after staging reported created 0, skipped 47, conflicts 0 |
