# WF Eight Goals Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Complete the eight user-approved roadmap items for `nature-publication-skills` without losing source provenance, install reliability, or Harness workflow discipline.

**Architecture:** Keep `SKILL.md` files concise and route detailed knowledge into `references/`, deterministic scripts, and optional assets. Treat `skills/**` as canonical skill source, `references/**` as evidence and provenance, `scripts/**` as validators/generators, `docs/**` as user-facing development and release documentation, and `Harness/**` as active workflow state.

**Tech Stack:** Markdown Agent Skills, Python 3, PyMuPDF, Pillow, matplotlib/seaborn-compatible templates, Node npm packaging, Codex/Claude Code skill discovery, Harness WF/subagent workflow.

---

## Source Rules

- Use local paper evidence from `references/source-paper-index.md`, `references/figure-audit-register.md`, PDF hash manifest, and reproducible `.audit/**` outputs.
- Use primary web sources for current policy and skill ecosystem facts: OpenAI Codex Skills, Agent Skills specification, GitHub CLI `gh skill`, Nature/Springer Nature author guidance, Nature research figure guide, Nature Portfolio policies.
- Do not invent figure styles, sample counts, statistics, or claims. If evidence is missing, record the gap and route it to a user/data request.

## File Structure

Planned additions and modifications:

- Modify `Harness/PLAN.md`: active WF heartbeat, dispatch table, verification evidence, and slice status.
- Create `docs/superpowers/plans/2026-06-24-wf-eight-goals.md`: this roadmap and acceptance matrix.
- Modify or create `references/figure-style-rule-map.md`: source figure family to skill-rule mapping for all eight paper groups.
- Modify `references/external-sources.md`: refresh checked dates and add current source evidence from web verification.
- Modify `skills/nature-publication-figure/SKILL.md`: only route to new references/templates; keep core instructions short.
- Modify or create `skills/nature-publication-figure/references/panel-composition-patterns.md`: panel layout, hero panel, microscopy plates, statistical blocks, icons/schematics.
- Modify or create `skills/nature-publication-figure/references/template-catalog.md`: available templates, when to use each, input expectations, outputs.
- Create `skills/nature-publication-figure/scripts/`: deterministic figure helpers installed with the figure skill.
- Create `skills/nature-publication-figure/templates/`: reusable Python figure template entrypoints installed with the figure skill.
- Create `skills/nature-publication-figure/assets/palettes.json`: palette tokens and channel mappings that travel with the installed skill.
- Modify `skills/nature-publication-writing/SKILL.md`: route to benchmark and submission QA where relevant.
- Create `references/benchmarks/prompts/`: benchmark prompts grouped by writing, figure, and submission QA.
- Create `references/benchmarks/golden/`: golden/rubric records that are evidence artifacts, not executable code.
- Create `tests/benchmarks/`: lightweight structural tests for benchmark files.
- Modify `scripts/validate_skills.py` and `scripts/check_style_coverage.py` only when new artifacts need automated validation.
- Modify `docs/installation.md` and `README.md`: distribution, release, validation, and productized docs.
- Create `skills/nature-publication-submission-qa/` for the cross-skill submission readiness workflow, then update installer, repo symlinks, plugin metadata, README, and validators so all three skills stay aligned.
- Update `.codex-plugin/plugin.json` if a third skill is added.

## Task 1: Harness Bootstrap Closeout Audit

**Files:**
- Modify: `Harness/PLAN.md`
- Delete: `Harness/SETUP.md`
- Modify: `CLAUDE.md`
- Modify: `Harness/scripts/validate-harness.mjs`
- Create: `tests/test_validate_harness.py`
- Verify: no project behavior files touched unless a real inconsistency is found

- [x] **Step 1: Inspect current Harness state**

Run:

```bash
git status --short --branch
git log --oneline --decorate -5
node Harness/scripts/validate-harness.mjs --strict
```

Expected: clean branch, latest Harness commit visible, strict validator passes.

- [x] **Step 2: Decide `Harness/SETUP.md` disposition**

Decision rule:

- Delete `Harness/SETUP.md` because the repo has completed initial bootstrap and normal Harness mode should no longer re-run setup instructions.

Record the decision in `Harness/PLAN.md#Decisions`.

- [x] **Step 3: Patch stale bootstrap status**

Update `Harness/PLAN.md` so the previous bootstrap commit/push evidence is not left as pending, and this WF goal is the active state.

- [x] **Step 4: Verify closeout**

Run:

```bash
node Harness/scripts/validate-harness.mjs --strict
git diff --check
```

Expected: both exit 0.

## Task 2: Nature Figure Skill V2

**Files:**
- Modify: `skills/nature-publication-figure/SKILL.md`
- Modify/create: `skills/nature-publication-figure/references/panel-composition-patterns.md`
- Modify/create: `skills/nature-publication-figure/references/template-catalog.md`
- Modify/create: `skills/nature-publication-figure/references/color-and-chart-rules.md`
- Modify/create: `skills/nature-publication-figure/references/plotting-toolchain.md`
- Test: `tests/benchmarks/figure/*`

- [ ] **Step 1: RED pressure scenarios**

Create figure skill pressure scenarios that fail current guidance when an agent is asked to choose panel layout, colors, microscopy channel mapping, statistical plot type, and export QA under sparse input.

Expected baseline failure categories:

- ungrounded palette choice
- overdecorated layout
- missing scale bar/provenance
- no source mapping to paper evidence
- Chinese or ambiguous figure labels inside examples

- [ ] **Step 2: Add minimal v2 references**

Patch references to include:

- semantic palette tokens and no-rainbow/no-red-green rules
- panel layout recipes by figure role
- dark microscopy plate recipe
- statistical block recipe
- schematic/icon style rules
- export and QA contract

- [ ] **Step 3: Route from `SKILL.md`**

Add concise reference routing only; do not paste all details into `SKILL.md`.

- [ ] **Step 4: GREEN validation**

Run:

```bash
python scripts/validate_skills.py
python scripts/check_style_coverage.py
```

Expected: both exit 0 and pressure scenario rubric shows the new references answer the failure categories.

## Task 3: Paper Evidence Coverage Re-Audit

**Files:**
- Create/modify: `references/figure-style-rule-map.md`
- Modify: `references/figure-audit-register.md`
- Modify: `scripts/check_style_coverage.py`

- [ ] **Step 1: Regenerate audit artifacts when local PDFs exist**

Run:

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
```

Expected: 15 PDFs processed, outputs remain ignored.

- [ ] **Step 2: Build rule map**

Map each paper group to:

- main figure families
- Extended Data figure families
- Supplementary figure families
- style rules used by the figure skill
- gaps needing manual PDF inspection

- [ ] **Step 3: Add automated coverage check**

Extend `scripts/check_style_coverage.py` so it checks that `references/figure-style-rule-map.md` mentions all eight groups and core style families.

- [ ] **Step 4: Verify**

Run:

```bash
python scripts/check_style_coverage.py
python scripts/validate_skills.py
```

Expected: both exit 0.

## Task 4: Nature Chart/Template Library

**Files:**
- Create: `skills/nature-publication-figure/scripts/`
- Create: `skills/nature-publication-figure/templates/`
- Create: `skills/nature-publication-figure/assets/`
- Modify: `skills/nature-publication-figure/references/template-catalog.md`
- Test: `tests/benchmarks/figure/`

- [ ] **Step 1: Define template set**

Minimum templates:

- `multi_panel_microscopy_plate`
- `statistical_evidence_block`
- `method_schematic`
- `input_output_error_map`
- `supplementary_validation_matrix`

- [ ] **Step 2: Implement first deterministic template**

Start with `multi_panel_microscopy_plate` because it covers the hardest figure style constraints.

Expected outputs:

- PDF or SVG vector output
- PNG preview
- sidecar JSON with source/provenance fields

- [ ] **Step 3: Add template validator**

Check:

- output files exist
- no CJK labels in generated figure text
- expected color tokens are used
- sidecar JSON has required provenance keys

- [ ] **Step 4: Verify**

Run template generator and validator, then:

```bash
python scripts/validate_skills.py
python scripts/check_style_coverage.py
```

Expected: all exit 0.

## Task 5: Writing Skill Benchmark

**Files:**
- Create: `references/benchmarks/prompts/writing/*.md`
- Create: `references/benchmarks/golden/writing/rubric.md`
- Create: `tests/benchmarks/writing/`
- Create or modify: `scripts/run_writing_benchmark.py`
- Modify: `skills/nature-publication-writing/references/section-and-legend-playbook.md`

- [ ] **Step 1: Define benchmark prompts**

Prompts:

- title
- summary abstract
- introduction paragraph
- results paragraph
- figure legend
- methods paragraph
- discussion paragraph
- supplementary caption

- [ ] **Step 2: Define deterministic rubric**

Rubric checks:

- claim/evidence/boundary present
- no invented statistics
- section-specific structure
- figure legend defines panel labels, n, error, statistics, and scale bars when applicable
- target language respected

- [ ] **Step 3: Add benchmark runner or manual checklist validator**

Prefer deterministic text checks where possible; use manual rubric for semantic quality that cannot be automated safely.

- [ ] **Step 4: Verify**

Run:

```bash
python scripts/validate_skills.py
python scripts/run_writing_benchmark.py --check-only
```

Expected: skill validation passes and benchmark files are structurally valid.

## Task 6: Install And Distribution Polish

**Files:**
- Modify: `README.md`
- Modify: `docs/installation.md`
- Modify: `package.json`
- Consider create: `.github/workflows/validate.yml`
- Modify: `.codex-plugin/plugin.json` if skill set changes

- [ ] **Step 1: Refresh source evidence**

Update `references/external-sources.md` with current dates and current links for OpenAI Codex Skills, Agent Skills spec, GitHub CLI `gh skill`, and relevant repository examples.

- [ ] **Step 2: Add distribution checklist**

Document:

- Codex user/repo install
- Claude Code user/repo install
- `npx github:sylvanding/nature-publication-skills`
- `gh skill install` / `gh skill update` limitations and current preview status
- npm pack contents
- plugin metadata sync
- release verification commands

- [ ] **Step 3: Add CI if safe**

If adding CI, keep it minimal:

```yaml
python scripts/validate_skills.py
python scripts/check_style_coverage.py
npm pack --dry-run
node Harness/scripts/validate-harness.mjs --strict
```

- [ ] **Step 4: Verify**

Run install smoke tests and package dry-run.

## Task 7: Nature Submission QA Skill

**Files:**
- Create: `skills/nature-publication-submission-qa/SKILL.md` and `agents/openai.yaml`
- Create: `skills/nature-publication-submission-qa/references/`
- Modify: `.codex-plugin/plugin.json` and `scripts/validate_skills.py` expectations if a third skill is added

- [ ] **Step 1: Choose skill boundary**

Create a third skill because submission QA is a distinct end-to-end workflow that crosses manuscript text, figures, Extended Data, Supplementary Information, accessibility, image integrity, reporting standards, and final file readiness.

- [ ] **Step 2: RED pressure scenario**

Ask a subagent to audit a mock submission package without QA guidance and document likely missed checks:

- figure legends
- statistics
- scale bars
- image integrity
- data/code availability
- reporting summary
- supplementary consistency

- [ ] **Step 3: Add QA workflow**

Include source-backed QA sections and missing-input behavior.

- [ ] **Step 4: Verify**

Run:

```bash
python scripts/validate_skills.py
python scripts/check_style_coverage.py
```

If a new skill is added, also verify plugin metadata and install smoke.

## Task 8: README And Docs Productization

**Files:**
- Modify: `README.md`
- Modify: `docs/installation.md`
- Consider create: `docs/release-checklist.md`
- Consider create: `docs/benchmarking.md`

- [ ] **Step 1: Preserve existing facts**

Do not remove existing skills, evidence, install, or validation sections. Reorganize only if clarity improves and commands remain intact.

- [ ] **Step 2: Add quickstart and decision tables**

Include:

- what the repo provides
- which skill to use
- install mode decision table
- validation command matrix
- contribution/update workflow

- [ ] **Step 3: Add roadmap completion summary**

Link to:

- figure style rule map
- template catalog
- writing benchmark
- submission QA workflow
- release checklist

- [ ] **Step 4: Final verification**

Run full matrix:

```bash
node Harness/scripts/validate-harness.mjs --strict
python scripts/validate_skills.py
python scripts/check_style_coverage.py
python scripts/install_skills.py install --agent codex --scope repo --repo .audit/install-smoke --mode symlink --dry-run
node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo .audit/install-smoke --dry-run
npm pack --dry-run
git diff --check
```

Expected: all exit 0.

## Commit Strategy

- Commit after each verified roadmap slice when the diff is coherent.
- Push the branch after each major slice or at least after the day’s verified checkpoint.
- Do not mark the full goal complete until all eight roadmap items have evidence in `Harness/PLAN.md` and the final verification matrix passes.
