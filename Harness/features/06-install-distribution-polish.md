# Install And Distribution Polish

> **Status**: Verified
> **Created**: 2026-06-25
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [05-writing-benchmark.md](05-writing-benchmark.md)

---

## 1. Requirements

### 1.1 Background

Goal 6 hardens installation and packaging. Earlier goals noted that `npm pack --dry-run` included internal `docs/superpowers/plans/**`; this slice turns that risk into an automated distribution validator and documents release/update safety.

### 1.2 Goals

- Add `scripts/validate_distribution.py` to check package contents, plugin manifest, docs, and install dry-runs.
- Add `docs/distribution.md` covering Codex, Claude Code, npx, Codex Plugin, GitHub CLI `gh skill`, release checklist, and update safety.
- Update `package.json` so npm packages user-facing docs without shipping internal Harness/superpowers execution plans.
- Add the distribution validator to README and repository validation expectations.

### 1.3 Acceptance Criteria

- [x] `python scripts/validate_distribution.py` fails before distribution docs/package fixes and passes after implementation.
- [x] `npm pack --dry-run` no longer includes `docs/superpowers/**`.
- [x] Package includes skill assets, templates, writing benchmarks, distribution docs, plugin manifest, scripts, and requirements.
- [x] `docs/distribution.md` covers Codex, Claude Code, npx, Codex Plugin, GitHub CLI `gh skill`, Release checklist, and Update safety.
- [x] Repo and Claude/Codex install copy smoke checks pass.
- [x] Full validation matrix passes.

---

## 2. Verification

### 2.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_distribution.py` | Failed as RED | Missing `docs/distribution.md`, raw `docs/` packaging, internal `docs/superpowers/**` included, README/install docs not linked |
| `python scripts/validate_distribution.py` | Passed | Includes npm package boundary and real Codex/Claude repo copy smoke under `.audit/install-smoke-distribution` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_writing_benchmark.py` | Passed | Output: `Writing benchmark validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `python scripts/validate_figure_templates.py` | Passed | Output: `Figure template validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `npm pack --dry-run` | Passed | Tarball excludes `docs/superpowers/**`, `.audit/**`, and `references-papers-dai-tsinghua/**` |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 2.2 Review Findings

- Socrates found npx symlink risk, missing `gh skill` public-preview warning, dry-run-only install smoke, incomplete package-content assertions, and stale closeout state. Fixed by changing npx docs to copy mode, adding public-preview/version-sensitive warnings, turning validator install checks into real copy smoke, expanding required package files, and syncing closeout records.

### 2.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- Local GitHub CLI `gh skill` may be older than the documented command surface; documentation must label this as version-sensitive unless locally verified.

---

## 3. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-25 | Initial version | Start Goal 6 |
| 2 | 2026-06-25 | Added distribution docs, package boundary validator, real copy smoke, public-preview warning, and closeout evidence | Close Goal 6 |
