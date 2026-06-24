# PLAN.md - Active Execution Plan

Use this file when work spans more than one step, one file, or one agent.

## Current Goal

WF mode: complete the eight-goal roadmap for `nature-publication-skills` in order:

1. Harness bootstrap closeout audit.
2. Nature figure skill v2 deepening.
3. Paper evidence coverage re-audit.
4. Nature-style chart/template library.
5. Writing skill benchmark.
6. Install and distribution polish.
7. Nature submission QA skill.
8. README and docs productization.

## Phase

Choose one: Idea / Research / PRD / Architecture / Plan / Build / Verify / Feedback.

Current: Verify

## Heartbeat

Mode: wf
Last beat: 2026-06-25T00:55:00+08:00
Current phase: Verify
Current blocker: none
Next beat trigger: after Goal 6 commit and before Goal 7 submission QA skill
Failure count: 0
Recovery action: narrow to the next unfinished roadmap slice, rerun the relevant validator, and dispatch debugger only for reproduced failures

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

- [x] Goal 1: Harness bootstrap closeout audit proves branch, commit, push, `Harness/PLAN.md`, and `Harness/SETUP.md` disposition are consistent.
- [x] Goal 2: Figure skill v2 adds source-backed, executable guidance for colors, panel layouts, microscopy plates, statistical plots, workflows, icon/schematic styles, and export QA without bloating `SKILL.md`.
- [x] Goal 3: Evidence coverage maps every local main, Extended Data, Supplementary figure/table family to skill rules and sources.
- [x] Goal 4: Template library provides runnable Nature-style figure examples or scripts with English labels and deterministic validation.
- [x] Goal 5: Writing benchmark provides prompts, expected checks, and a runner or manual rubric for title, abstract, results, legends, methods, and discussion.
- [x] Goal 6: Install/distribution docs and validation cover Codex, Claude Code, npm/npx, plugin packaging, GitHub CLI skill flow, release checklist, and update safety.
- [ ] Goal 7: Submission QA skill exists or the existing skills gain a clearly routed QA workflow covering figure legends, statistics, image integrity, reporting, data/code availability, and supplementary consistency.
- [ ] Goal 8: README/docs are productized while preserving current project facts and validation commands.
- [ ] All new claims have local or web source evidence recorded in `references/**`, skill references, or `Harness/research/research-results.md`.
- [ ] Final validators pass: `node Harness/scripts/validate-harness.mjs --strict`, `python scripts/validate_skills.py`, `python scripts/check_style_coverage.py`, benchmark/template validators, install smoke checks, PDF audit checks when local corpus is present, `npm pack --dry-run`, and `git diff --check`.

## Scope

Allowed write set for the full roadmap:

- `Harness/**`
- `.claude/**` only if routing or workflow docs need updates
- `docs/**`
- `references/**`
- `skills/**`
- `scripts/**`
- `tests/**`
- `README.md`
- `package.json`
- `requirements.txt`
- `.github/**` if CI is added after plan review
- `.codex-plugin/**` if a new skill is added and plugin metadata must stay aligned

Forbidden without explicit approval:

- `references-papers-dai-tsinghua/**`
- `.audit/**` tracked commits
- destructive git operations
- rewriting existing skill source without preserving source-backed references
- inventing scientific claims, sample counts, statistics, or figure evidence not present in sources

## Loaded Context

Keep this list short. Add only docs/files used for the current phase.

- `AGENTS.md`
- `CLAUDE.md`
- `Harness/MEMORY.md`
- `Harness/README.md`
- `Harness/WF.md`
- `Harness/subagents.md`
- `Harness/dispatch.md`
- `Harness/context-loading.md`
- `Harness/architecture.md`
- `Harness/domain/ports.md`
- `README.md`
- `docs/installation.md`
- `skills/nature-publication-figure/SKILL.md`
- `skills/nature-publication-figure/references/*`
- `skills/nature-publication-writing/SKILL.md`
- `skills/nature-publication-writing/references/*`
- `references/source-paper-index.md`
- `references/figure-audit-register.md`
- `references/external-sources.md`
- `scripts/validate_skills.py`
- `scripts/check_style_coverage.py`
- OpenAI Codex Skills docs, Agent Skills specification, GitHub CLI `gh skill`, Nature formatting guide, Nature research figure guide, Nature Portfolio reporting standards

## Project Facts Discovered Before Editing

- Baseline branch is `harness-vibe-coding-bootstrap`, tracking `origin/harness-vibe-coding-bootstrap`.
- Latest commit before this WF goal is `e36e3b2 chore: configure harness vibe coding`; worktree was clean at WF intake.
- The repository is an Agent Skills source and distribution repo, not a web app or service.
- Existing skills are intentionally concise and use progressive disclosure through `references/`.
- `references-papers-dai-tsinghua/**` contains 15 local PDFs and is intentionally ignored.
- Existing validators are green at WF intake: Harness strict, skill validator, style coverage, and npm pack dry-run.
- `Harness/SETUP.md` was retired in Goal 1 after bootstrap evidence was validated; `CLAUDE.md` no longer routes normal work through setup.

## Tasks

| # | Task | Owner | Verify | Status |
| --- | --- | --- | --- | --- |
| 1 | WF intake and baseline verification | main | `git status --short --branch`; baseline validators | Verified |
| 2 | Dispatch planner, architect, researcher subagents | main | subagent return summaries | Done |
| 3 | Write detailed eight-goal roadmap and acceptance matrix | main | `docs/superpowers/plans/2026-06-24-wf-eight-goals.md` exists and has no placeholders | Done |
| 4 | Goal 1: Harness bootstrap closeout audit | main plus reviewer/verifier | strict Harness validator, status/log/push evidence | Verified |
| 5 | Goal 2: Nature figure skill v2 | main plus test-writer/reviewer | skill validator, style coverage, figure template/QA checks | Verified |
| 6 | Goal 3: Paper evidence coverage re-audit | main plus researcher | PDF audit scripts and coverage table validator | Verified |
| 7 | Goal 4: Nature chart/template library | main plus implementer/reviewer | generated sample outputs and template validator | Verified |
| 8 | Goal 5: Writing skill benchmark | main plus test-writer | benchmark runner or rubric validator | Verified |
| 9 | Goal 6: Install/distribution polish | main plus docs-researcher | install smoke, npm pack, docs link checks | Verified |
| 10 | Goal 7: Nature submission QA skill | main plus architect/reviewer | skill validator and QA pressure scenarios | Pending |
| 11 | Goal 8: README/docs productization | main plus reviewer | README checklist, link validation, final smoke | Pending |
| 12 | Final review, verification, commit/push | main plus verifier | full command matrix, `git diff --check`, pushed branch | Pending |

## Parallel Dispatch

Use [subagents.md](subagents.md) and [dispatch.md](dispatch.md) when more than one agent or bounded pass is useful.

| Task | Agent | Mode | Read Set | Write Set | Depends On | Output | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Eight-goal decomposition | planner subagent `Dirac` | Parallel Read | `README.md`, `Harness/**`, `skills/**`, `references/**`, `docs/**`, `scripts/**`, `package.json` | none | WF intake | task dependencies, write sets, validation plan | Integrated |
| Repository structure and boundaries | architect subagent `Euclid` | Parallel Read | `Harness/architecture.md`, `Harness/domain/ports.md`, `skills/**`, `scripts/**`, `references/**`, `docs/**` | none | WF intake | proposed file tree, boundary rules, new-skill decision | Integrated |
| External sources and skill ecosystem | researcher subagent `Helmholtz` | Parallel Read | `references/external-sources.md`, `docs/installation.md`, `README.md`, skill references plus web sources | none | WF intake | source-backed adopt/reject/watch decisions | Integrated |

## Subagent Synthesis

Agents used: `Dirac` planner, `Euclid` architect, `Helmholtz` researcher
Findings accepted: complete the roadmap as ordered slices with commit boundaries; keep `SKILL.md` files as thin routers; put reusable figure scripts/templates/assets inside the owning figure skill so installed skills stay self-contained; keep repo-level validators and benchmark runners in root `scripts/`; create a third `nature-publication-submission-qa` skill because item 7 is an end-to-end submission readiness workflow; update `gh skill` docs as current but preview and not locally verified; promote Nature Research Figure Guide as a first-class source; fix roadmap checkbox drift before committing Goal 1; add negative validator tests for stale post-bootstrap setup references and missing bootstrap contracts.
Findings rejected: putting reusable figure templates only in root docs or root scripts was rejected because installed skills would not carry their tools; treating third-party blogs as policy sources was rejected.
Conflicts: none
Decisions: Use progressive disclosure; keep `SKILL.md` files concise; implement the roadmap as ordered slices with verification after each slice; retire `Harness/SETUP.md` after Goal 1 because bootstrap is verified and normal WF mode is active.
Next write set: Goal 7 submission QA skill: `skills/nature-publication-submission-qa/**`, installer/plugin metadata, validation scripts, README/docs, and related Harness feature records.
Verification path: baseline validators, slice-specific validators, final full verification matrix
Residual risk: the full objective is large; the goal remains active until all eight items are verified. Goal 6 now excludes internal `docs/superpowers/**` from npm packages; keep watching package contents when new docs or skills are added.

## Agent Handoffs

| Agent | Role | Context Pack | Result |
| --- | --- | --- | --- |
| Dirac | Planner | Eight-goal roadmap, local repo facts, no writes | Recommended slice order, write sets, validators, and commit boundaries |
| Euclid | Architect | Structure/boundary review, no writes | Recommended per-skill scripts/templates/assets, root coverage/benchmark/docs boundaries, and third QA skill if cross-skill |
| Helmholtz | Researcher | Current external sources and skill ecosystem, no writes | Recommended current source updates for Agent Skills, `gh skill`, OpenAI plugins, and Nature/Springer figure and submission guidance |
| Fermat | Reviewer | Goal 1 diff, no writes | Found stale Task 1 roadmap checkboxes and missing negative tests; both addressed |
| Peirce | Reviewer | Goal 2 spec compliance diff, no writes | Found missing pressure scenarios/rubric, shallow validator coverage, and stale feature verification records; all addressed |
| Confucius | Reviewer | Goal 2 source/quality diff, no writes | Found copy-mode evidence gap, unsupported hero-panel range, shallow path validation, stale source date discipline, and old roadmap path; all addressed |
| Leibniz | Reviewer | Goal 3 coverage diff and regenerated `.audit/**` evidence, no writes | Found no blocking coverage issues; requested status closeout sync, now addressed |
| Aristotle | Reviewer | Goal 4 template library diff and generated smoke output, no writes | Found README dependency drift, sidecar contract mismatch, and phase metadata drift; all addressed |
| James | Reviewer | Goal 5 writing benchmark diff, no writes | Found broken benchmark routing, roadmap drift, ambiguous rubric applicability, and stale closeout; all addressed |
| Socrates | Reviewer | Goal 6 install/distribution diff and package dry-run, no writes | Found npx symlink risk, missing `gh skill` preview warning, dry-run-only install smoke, incomplete package assertions, and stale closeout; all addressed |

## Decisions

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-24 | Execute the eight user-approved goals in order under WF mode | User explicitly approved the eight suggested goals and requested WF mode |
| 2026-06-24 | Start with durable roadmap and Goal 1 closeout before heavy skill edits | The previous Harness bootstrap left `PLAN.md` stale; a clean state record reduces later drift |
| 2026-06-24 | Use Python as the default figure/template toolchain unless a specific MATLAB input requires otherwise | Existing figure skill and audit scripts already use Python, PyMuPDF, PIL, matplotlib-friendly guidance, and repo validation |
| 2026-06-24 | Keep `SKILL.md` concise and place detailed figure/writing/QA material in references, scripts, or assets | OpenAI Codex Skills docs and Agent Skills spec emphasize progressive disclosure and optional resources |
| 2026-06-24 | Retire `Harness/SETUP.md` and update the validator to support post-bootstrap mode | Bootstrap is verified, `Harness/SETUP.md` is temporary, and future WF tasks should not re-enter setup |
| 2026-06-24 | Plan item 7 as a third `nature-publication-submission-qa` skill | Submission readiness crosses manuscript text, figures, Extended Data, Supplementary Information, accessibility, image integrity, reporting, and final files |
| 2026-06-24 | Add `references/figure-style-rule-map.md` as the crosswalk from local figures to figure skill rules | Goal 3 needs durable evidence that every local figure/table family is tied to source paths and reusable style rules |
| 2026-06-24 | Implement `multi_panel_microscopy_plate` as the first executable template | It exercises the highest-risk figure requirements: microscopy panels, scale bars, English labels, palette tokens, vector/preview export, and provenance sidecar |
| 2026-06-25 | Keep writing benchmarks inside the writing skill folder | Copy-mode installs only carry the skill directory, so benchmark prompts and rubric must be skill-contained |
| 2026-06-25 | Exclude internal `docs/superpowers/**` from npm packages | Distribution packages should ship user-facing docs and skills, not Harness execution plans |

## Verification

| Check | Result | Notes |
| --- | --- | --- |
| `git status --short --branch` | Passed | Worktree clean on `harness-vibe-coding-bootstrap...origin/harness-vibe-coding-bootstrap` at WF intake |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Baseline strict Harness validation passed |
| `python scripts/validate_skills.py` | Passed | Baseline skill validation passed |
| `python scripts/check_style_coverage.py` | Passed | Baseline style coverage passed |
| `npm pack --dry-run` | Passed | Baseline package dry-run reported `nature-publication-skills@0.2.0` tarball contents |
| `python tests/test_validate_harness.py` | Passed | Three tests cover valid post-bootstrap mode, stale post-bootstrap setup reference rejection, and missing bootstrap contract rejection |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Post-bootstrap strict Harness validation passed after retiring setup |
| `python scripts/validate_skills.py` | Passed | Skill validation still passed after Goal 1 changes |
| `git diff --check` | Passed | No whitespace errors after Goal 1 changes |
| `python scripts/check_style_coverage.py` | Passed | Style coverage still passed after Goal 1 changes |
| `npm pack --dry-run` | Passed | Package dry-run passes; note that `docs/superpowers/plans/**` is included by current `docs/**` package rule |
| `python scripts/validate_figure_v2.py` | Passed | Goal 2 validator passed after RED failure and benchmark/source-path fixes |
| `python scripts/validate_skills.py` | Passed | Skill validation passed after Goal 2 changes |
| `python scripts/check_style_coverage.py` | Passed | Style coverage passed after Goal 2 changes |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict Harness validation passed after Goal 2 feature record updates |
| `git diff --check` | Passed | No whitespace errors after Goal 2 changes |
| `python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json` | Passed | Goal 3 regenerated 15 PDF inventory records |
| `python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets` | Passed | Goal 3 regenerated 15 contact sheets under ignored `.audit/` |
| `python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json` | Passed | Goal 3 regenerated palette summaries for 15 PDFs |
| `python scripts/check_style_coverage.py` | Passed | Goal 3 rule map and strengthened style coverage validator passed |
| `python scripts/validate_skills.py` | Passed | Skill validation passed after Goal 3 changes |
| `python scripts/validate_figure_v2.py` | Passed | Figure v2 validation still passed after Goal 3 changes |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict Harness validation passed after Goal 3 feature record updates |
| `git diff --check` | Passed | No whitespace errors after Goal 3 changes |
| `python scripts/validate_figure_templates.py` | Passed | Goal 4 template smoke generated PDF, PNG, and provenance sidecar |
| Visual inspection | Passed | `.audit/template-smoke/multi_panel_microscopy_plate.png` checked after fixing `Mock-only` overlap |
| `python scripts/validate_skills.py` | Passed | Skill validation passed after Goal 4 changes |
| `python scripts/validate_figure_v2.py` | Passed | Figure v2 validation still passed after Goal 4 changes |
| `python scripts/check_style_coverage.py` | Passed | Style coverage still passed after Goal 4 changes |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict Harness validation passed after Goal 4 feature record updates |
| `npm pack --dry-run` | Passed | Tarball includes new figure template assets, scripts, and templates |
| `git diff --check` | Passed | No whitespace errors after Goal 4 changes |
| `python scripts/validate_writing_benchmark.py` | Passed | Goal 5 writing benchmark structure passed |
| `python scripts/validate_skills.py` | Passed | Skill validation passed after Goal 5 changes |
| `python scripts/validate_figure_v2.py` | Passed | Figure v2 validation still passed after Goal 5 changes |
| `python scripts/validate_figure_templates.py` | Passed | Figure template validation still passed after Goal 5 changes |
| `python scripts/check_style_coverage.py` | Passed | Style coverage still passed after Goal 5 changes |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict Harness validation passed after Goal 5 feature record updates |
| `npm pack --dry-run` | Passed | Tarball includes skill-contained writing benchmarks |
| `git diff --check` | Passed | No whitespace errors after Goal 5 changes |
| `python scripts/validate_distribution.py` | Passed | Goal 6 package boundary and real copy install smoke passed |
| `python scripts/validate_skills.py` | Passed | Skill validation passed after Goal 6 changes |
| `python scripts/validate_writing_benchmark.py` | Passed | Writing benchmark validation still passed after Goal 6 changes |
| `python scripts/validate_figure_v2.py` | Passed | Figure v2 validation still passed after Goal 6 changes |
| `python scripts/validate_figure_templates.py` | Passed | Figure template validation still passed after Goal 6 changes |
| `python scripts/check_style_coverage.py` | Passed | Style coverage still passed after Goal 6 changes |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Strict Harness validation passed after Goal 6 changes |
| `npm pack --dry-run` | Passed | Tarball excludes internal `docs/superpowers/**` and includes required distribution files |
| `git diff --check` | Passed | No whitespace errors after Goal 6 changes |
