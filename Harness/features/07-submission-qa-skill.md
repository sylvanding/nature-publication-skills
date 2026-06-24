# Nature Submission QA Skill

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [06-install-distribution-polish.md](06-install-distribution-polish.md)

---

## 1. Requirements

### 1.1 Background

Goal 7 adds a third skill for end-to-end Nature-family submission readiness QA. This workflow crosses manuscript writing, publication figures, image integrity, reporting standards, data/code availability, AI use, Extended Data, and Supplementary Information, so it is separate from the writing and figure skills.

### 1.2 Goals

- Add `skills/nature-publication-submission-qa/` with a concise `SKILL.md`, `agents/openai.yaml`, and four policy-backed reference files.
- Add `scripts/validate_submission_qa.py` to enforce the skill structure and repository routing.
- Wire the third skill into installer selection, repo-scoped `.agents/skills`, README, plugin metadata, and distribution validation.
- Record current official sources for submission, formatting, reporting, image integrity, accessibility, and AI use.

### 1.3 Acceptance Criteria

- [x] `python scripts/validate_submission_qa.py` fails before the skill exists and passes after implementation.
- [x] The new skill routes to references for submission readiness, figure/image integrity, data-code-reporting, and supplementary consistency.
- [x] The installer, plugin metadata, README validation matrix, and repo-scoped skill link include `nature-publication-submission-qa`.
- [x] Distribution copy smoke installs the third skill for Codex and Claude Code.
- [x] A subagent pressure scenario or review checks likely missed submission QA gaps.
- [x] Full validation matrix passes.

---

## 2. Verification

### 2.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_submission_qa.py` | Failed as RED | Missing skill directory, installer route, plugin metadata, README entries, and repo-scoped link |
| `python scripts/validate_submission_qa.py` | Passed | Output: `Submission QA validation passed.` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_distribution.py` | Passed | Output: `Distribution validation passed.` |
| `python scripts/validate_writing_benchmark.py` | Passed | Output: `Writing benchmark validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `python scripts/validate_figure_templates.py` | Passed | Output: `Figure template validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `npm pack --dry-run` | Passed | Dry-run output includes the third skill and `scripts/validate_submission_qa.py` |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 2.2 Review Findings

- Archimedes ran a read-only pressure scenario against a mock Nature-family submission package without a dedicated QA skill. Likely misses: cross-file figure legend consistency, replicate/statistics completeness, raw microscopy/scale-bar evidence, Reporting Summary, Data availability, Code availability, Supplementary versus Extended Data boundaries, final production source files, and vague AI-use notes.
- The correct stance for the mock package is `Do not approve` because raw microscopy files, a statistics table, data/code accession list, and specific AI-use disclosure are missing.
- The current QA skill covers these findings through its audit contract, file inventory, image integrity gates, data/code/statistics gates, and supplementary consistency reference.
- Lagrange found no blocking Goal 7 issues. It flagged two documentation polish items: future-dated decisions in `Harness/PLAN.md` and a packaged planning doc still saying "two core skills". Both were corrected before commit.

### 2.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- Target journal policies, forms, and file-format requirements are time-sensitive. The skill therefore requires online verification before real submission approvals.

---

## 3. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Added Goal 7 feature record and initial validator evidence | Start submission QA closeout |
| 2 | 2026-06-24 | Marked Goal 7 verified after full validation and subagent pressure review | Close Goal 7 |
