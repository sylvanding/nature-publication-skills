# Nature Figure Skill V2

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 2
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [architecture.md](../architecture.md), [WF.md](../WF.md)

---

## 1. Requirements

### 1.1 Background

The current figure skill already covers Nature-family figure basics, source-paper style families, color rules, plotting toolchain, and QA. The user explicitly prioritized the picture/figure side of the skills: colors, panel layout, microscopy plates, statistical charts, schematic/icon type, and best plotting tools. Goal 2 deepens that guidance while keeping `SKILL.md` concise and source-backed.

### 1.2 Goals

- Add a source-backed panel composition reference for hero panels, dark microscopy plates, statistical blocks, schematics/icons, and supplementary matrices.
- Add a figure template catalog that names template families, inputs, outputs, and provenance expectations without implementing templates yet.
- Refresh figure reference files with current Nature/Springer Nature figure-guide evidence where it affects style, color, export, and plotting defaults.
- Add a deterministic validator so future edits cannot silently remove v2 figure requirements.

### 1.3 Non-Goals

- Do not implement the runnable template library in this slice; that is Goal 4.
- Do not alter writing skill behavior in this slice.
- Do not invent new visual rules without local paper evidence or official Nature/Springer Nature source support.
- Do not add generated `.audit/**` artifacts to git.

### 1.4 Acceptance Criteria

- [x] `skills/nature-publication-figure/SKILL.md` routes to the new v2 reference files without becoming a long manual.
- [x] `skills/nature-publication-figure/references/panel-composition-patterns.md` exists and covers the required panel families.
- [x] `skills/nature-publication-figure/references/figure-template-catalog.md` exists and names the required template families.
- [x] Existing color, plotting, and QA references include current Nature/Springer Nature source-backed constraints.
- [x] `python scripts/validate_figure_v2.py` passes.
- [x] `python scripts/validate_skills.py` passes.
- [x] `python scripts/check_style_coverage.py` passes.
- [x] `git diff --check` passes.

### 1.5 UI Automation Hooks

This is not UI-facing.

| Element / State | Accessible Role / Label | `data-testid` | Verification Target |
| --- | --- | --- | --- |
| Not UI-facing | N/A | N/A | N/A |

---

## 2. Design

### 2.1 Impact Scope

| Area | Impacted? | Notes |
| --- | --- | --- |
| `Harness/architecture.md` | No | Existing progressive-disclosure architecture remains valid |
| `Harness/domain/ports.md` | No | No port changes |
| `Harness/data-flow.md` | No | No runtime flow changes |
| `Harness/state-machines.md` | No | No state machine changes |
| tests | Yes | Add `scripts/validate_figure_v2.py` |

### 2.2 Allowed Write Set

- `Harness/PLAN.md`
- `Harness/features/02-figure-skill-v2.md`
- `skills/nature-publication-figure/SKILL.md`
- `skills/nature-publication-figure/references/panel-composition-patterns.md`
- `skills/nature-publication-figure/references/figure-template-catalog.md`
- `skills/nature-publication-figure/references/color-and-chart-rules.md`
- `skills/nature-publication-figure/references/plotting-toolchain.md`
- `skills/nature-publication-figure/references/qa-and-export.md`
- `scripts/validate_figure_v2.py`
- `scripts/validate_skills.py` only if adding the new validator to repository expectations
- `tests/benchmarks/figure/**` for pressure scenarios and rubric records
- `README.md` only to list the new validator in the repository validation matrix
- `references/external-sources.md` only to record refreshed 2026-06-24 official sources

### 2.3 Forbidden Scope

- `skills/nature-publication-writing/**`
- `skills/nature-publication-submission-qa/**`
- `package.json`
- `.codex-plugin/**`
- `.audit/**`
- `references-papers-dai-tsinghua/**`

### 2.4 Approach

#### Candidate Approaches

| Approach | Pros | Cons | Decision |
| --- | --- | --- | --- |
| Add all details directly to `SKILL.md` | One file to read | Violates progressive disclosure and bloats startup-loaded skill body | Reject |
| Add focused references and route from `SKILL.md` | Keeps entrypoint concise and lets agents load only relevant details | Requires validation to prevent missing files | Accept |
| Implement templates now | Faster visible output | Mixes Goal 2 guidance with Goal 4 executable library | Reject for this slice |

#### Rationale

The current skill already uses references effectively. V2 should deepen the figure system as separate reference files and add a structural validator. Runnable template scripts belong to Goal 4 after the design vocabulary is stable.

### 2.5 Edge Cases

- A future edit removes the v2 reference route from `SKILL.md` -> validator fails.
- A reference mentions color rules but drops accessibility constraints -> validator fails.
- A reference adds templates but omits provenance requirements -> validator fails.
- Official policy and local visual evidence conflict -> policy wins and the conflict is recorded.

---

## 3. Tasks

| # | Task | Owner | Write Set | Verify |
| --- | --- | --- | --- | --- |
| 1 | Write RED validator for v2 figure requirements | main | `scripts/validate_figure_v2.py` | Done: validator failed before v2 files and benchmark records were present |
| 2 | Add panel composition and template catalog references | main | figure skill references | Done: `python scripts/validate_figure_v2.py` |
| 3 | Refresh color, plotting, and QA references | main | existing figure references | Done: `python scripts/validate_figure_v2.py` |
| 4 | Route v2 references from `SKILL.md` | main | `SKILL.md` | Done: `python scripts/validate_skills.py` |
| 5 | Record verification and review | main plus reviewer | feature doc and PLAN | Done: command matrix recorded below |

### Subagent Plan

| Agent / Pass | Required? | Mode | Read Boundary | Write Set | Verify |
| --- | --- | --- | --- | --- | --- |
| Planner | Done | Parallel Read | Full roadmap | none | `Dirac` handoff |
| Researcher / Docs Researcher | Done | Parallel Read | Sources and figure guidance | none | `Helmholtz` handoff |
| Architect | Done | Parallel Read | Repo structure and skill boundaries | none | `Euclid` handoff |
| Test Writer | No | Serial Write | Main agent writes structural validator | `scripts/validate_figure_v2.py` | RED/GREEN command |
| Implementer / Debugger | No | Serial Write | Main agent implements bounded docs | declared files | validators |
| Reviewer | Done | Parallel Read | Final Goal 2 diff | none | Peirce and Confucius handoffs |
| Verifier | Done | Parallel Read | Final command matrix | none | command evidence |

---

## 4. Verification

### 4.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_figure_v2.py` | Failed as RED | Before benchmark/source-path fixes, it reported missing skill-contained evidence, unsupported `35-60%`, and missing benchmark files |
| `python scripts/validate_figure_v2.py` | Passed | After fixes, output: `Figure v2 validation passed.` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 4.2 Review Findings

- Peirce found missing pressure scenarios/rubric, shallow validator coverage, and stale verification records. Fixed by adding `tests/benchmarks/figure/*`, strengthening `scripts/validate_figure_v2.py`, and updating this feature record.
- Confucius found copied installs could lose source evidence, validator path coverage was shallow, the hero-panel `35-60%` range was unsupported, external-source date discipline was stale, and one roadmap path used `template-catalog.md`. Fixed by routing new refs through skill-contained `references/figure-style-atlas.md`, adding source-checkout path checks, removing the unsupported range, updating `references/external-sources.md`, and correcting the roadmap path.

### 4.3 Docs Sync

- [x] `Harness/architecture.md` - no change needed.
- [x] `Harness/domain/ports.md` - no change needed.
- [x] `Harness/data-flow.md` - no change needed.
- [x] `Harness/state-machines.md` - no change needed.
- [x] `Harness/research/research-results.md` - no change needed; source details recorded in `references/external-sources.md` and skill references.

### 4.4 Decision Log

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-24 | Split v2 figure guidance into reference files | Keeps `SKILL.md` concise while adding detailed source-backed figure rules |
| 2026-06-24 | Keep copied installs source-backed through `references/figure-style-atlas.md` | `scripts/install_skills.py` copies only skill folders in copy mode, so critical evidence summaries must travel with the skill |
| 2026-06-24 | Remove numeric hero-panel area range | Review found no local or official source for the `35-60%` range |

### 4.5 Closeout

- [x] Acceptance criteria satisfied.
- [x] Tests or manual verification recorded.
- [x] Boundary impact documented.
- [x] Remaining risks listed or explicitly none.
- [x] If docs/code/tests conflicted, Decision Log records how it was resolved.

Remaining risks:

- Runnable template implementation is intentionally deferred to Goal 4.
- Benchmark scenarios are rubric/structural tests in this slice; full forward-testing with live subagents belongs to later skill-quality iteration if the user wants empirical agent outputs.

---

## 5. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Initial version | Start Goal 2 |
| 2 | 2026-06-24 | Added v2 figure references, validator, pressure benchmarks, reviewer findings, and verification evidence | Close Goal 2 |
