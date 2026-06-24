# README And Docs Productization

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [07-submission-qa-skill.md](07-submission-qa-skill.md)

---

## 1. Requirements

### 1.1 Background

Goal 8 turns the repository from a working skill source into a reader-facing package. After Goal 7, the README and packaged planning docs need to explain all three skills, installation choices, provenance, validation, and release/update workflow without stale "two skill" language.

### 1.2 Goals

- Productize `README.md` with quickstart, skill chooser, install-mode decision table, evidence/provenance, validation matrix, roadmap completion, and update/release workflow.
- Keep `docs/installation.md`, `docs/distribution.md`, and packaged planning docs aligned with all three skills.
- Add `scripts/validate_docs_productization.py` so product-doc expectations are repeatable.
- Add the docs validator to repository validation and distribution packaging checks.

### 1.3 Acceptance Criteria

- [x] `python scripts/validate_docs_productization.py` fails before README/docs productization and passes after implementation.
- [x] README includes quickstart, which-skill table, install-mode decision table, evidence/provenance, validation matrix, roadmap completion, and update/release workflow.
- [x] Installation and distribution docs route all three skills and include the docs validator in release checks.
- [x] Packaged planning docs no longer contradict the three-skill package.
- [x] Full validation matrix passes.
- [x] Final reviewer findings are resolved or documented.

---

## 2. Verification

### 2.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_docs_productization.py` | Failed as RED | Missing productized README sections, source links, docs validator command, installation skill names, and packaged planning validation commands |
| `python scripts/validate_docs_productization.py` | Passed | Output: `Docs productization validation passed.` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_submission_qa.py` | Passed | Output: `Submission QA validation passed.` |
| `python scripts/validate_writing_benchmark.py` | Passed | Output: `Writing benchmark validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `python scripts/validate_figure_templates.py` | Passed | Output: `Figure template validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `python scripts/validate_distribution.py` | Passed | Output: `Distribution validation passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `npm pack --dry-run` | Passed | Tarball includes productized README and docs validator |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 2.2 Review Findings

- Ramanujan found a package-facing README issue where Harness checks appeared in the normal validation matrix even though `Harness/**` is not shipped in the npm package. Fixed by splitting portable release checks from source checkout-only checks.
- Ramanujan found the release block was too short and could lead readers to skip required validation. Fixed by repeating the full release command set.
- Ramanujan found the packaged planning doc still described only writing and figure goals. Fixed by adding submission QA to the goal statement.

### 2.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- Goal 8 improves docs and package-facing validation; it does not create a tagged release or PR.

---

## 3. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Added Goal 8 feature record and docs productization RED/GREEN evidence | Start docs productization closeout |
| 2 | 2026-06-24 | Productized README/docs, added docs validator, resolved final reviewer findings, and recorded full verification | Close Goal 8 |
