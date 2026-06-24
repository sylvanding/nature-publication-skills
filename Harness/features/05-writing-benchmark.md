# Writing Skill Benchmark

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [04-figure-template-library.md](04-figure-template-library.md)

---

## 1. Requirements

### 1.1 Background

Goal 5 gives the writing skill an auditable benchmark surface. The benchmark is structural and source-grounded: prompts provide bounded source packets, and the rubric penalizes invented statistics, missing evidence, and section-inappropriate structure.

### 1.2 Goals

- Add benchmark prompts for title, summary abstract, introduction, results, figure legend, methods, discussion, and supplementary caption.
- Add a rubric covering claim/evidence/boundary, no invented statistics, section-specific structure, figure legend completeness, methods reproducibility, and target language.
- Add `scripts/validate_writing_benchmark.py` and route the writing skill to the benchmark materials.

### 1.3 Non-Goals

- Do not run a live LLM benchmark in this slice.
- Do not create golden prose that could be mistaken for manuscript text.
- Do not invent data beyond bounded benchmark source packets.

### 1.4 Acceptance Criteria

- [x] Eight writing prompt files exist under `skills/nature-publication-writing/references/benchmarks/prompts/writing/`.
- [x] Rubric exists under `skills/nature-publication-writing/references/benchmarks/golden/writing/rubric.md`.
- [x] Writing skill routes benchmark work to prompts and rubric.
- [x] `python scripts/validate_writing_benchmark.py` fails before benchmark files exist and passes after implementation.
- [x] README validation matrix includes the writing benchmark validator.
- [x] `python scripts/validate_skills.py` passes.
- [x] `git diff --check` passes.

---

## 2. Verification

### 2.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_writing_benchmark.py` | Failed as RED | Missing eight prompts, rubric, skill route, and README command |
| `python scripts/validate_writing_benchmark.py` | Passed | Output: `Writing benchmark validation passed.` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `python scripts/validate_figure_templates.py` | Passed | Output: `Figure template validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `npm pack --dry-run` | Passed | Tarball includes skill-contained writing benchmark prompts and rubric |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 2.2 Review Findings

- James found broken benchmark routing, roadmap contract drift, ambiguous rubric applicability, and stale closeout status. Fixed by moving benchmark files into the writing skill so copy installs carry them, updating the validator and roadmap to `scripts/validate_writing_benchmark.py`, adding applicable/N/A rubric rules, extending the playbook with Methods and Discussion checks, and syncing this closeout record.

### 2.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- This benchmark validates prompt/rubric structure, not live model quality. Live LLM forward-testing can be added after the benchmark contract is stable.

---

## 3. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Initial version | Start Goal 5 |
| 2 | 2026-06-25 | Added skill-contained benchmark prompts/rubric, validator, playbook additions, review closeout | Close Goal 5 |
