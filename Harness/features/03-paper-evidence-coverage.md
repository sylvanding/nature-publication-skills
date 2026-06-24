# Paper Evidence Coverage Re-Audit

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [WF.md](../WF.md), [02-figure-skill-v2.md](02-figure-skill-v2.md)

---

## 1. Requirements

### 1.1 Background

Goal 3 strengthens the link between the local Dai/Tsinghua reference corpus and the figure skill rules. Goal 2 created deeper panel/template guidance; this slice proves the guidance remains grounded in every local paper group and in the regenerated PDF audit artifacts.

### 1.2 Goals

- Regenerate page-level figure inventory, contact sheets, and palette summaries for all local PDFs under `references-papers-dai-tsinghua/`.
- Add `references/figure-style-rule-map.md` mapping every group to main figures, Extended Data, Supplementary figures, tables, skill rule families, and source evidence.
- Extend `scripts/check_style_coverage.py` so future edits cannot drop the rule map, group coverage, or core style-rule vocabulary.
- Keep generated `.audit/**` artifacts out of git while recording reproducible commands.

### 1.3 Non-Goals

- Do not change the source PDFs.
- Do not implement runnable figure templates; that remains Goal 4.
- Do not claim per-panel scientific conclusions beyond what the source register and visual audit support.

### 1.4 Acceptance Criteria

- [x] `references/figure-style-rule-map.md` exists with `## Group 1` through `## Group 8` sections.
- [x] Each group records Main figures, Extended Data, Supplementary figures, Tables, Skill rule mapping, Source evidence, and Coverage status.
- [x] `scripts/check_style_coverage.py` fails before the rule map exists and passes after it is added.
- [x] Regenerated `.audit/pdf_figure_inventory.json`, `.audit/pdf-page-sheets/*`, and `.audit/pdf_palette_summary.json` cover 15 PDFs.
- [x] `python scripts/check_style_coverage.py` passes.
- [x] `python scripts/validate_skills.py` passes.
- [x] `git diff --check` passes.

---

## 2. Design

### 2.1 Impact Scope

| Area | Impacted? | Notes |
| --- | --- | --- |
| `references/figure-style-rule-map.md` | Yes | New source-backed coverage map |
| `references/figure-audit-register.md` | Maybe | May need date/source pointer refresh |
| `scripts/check_style_coverage.py` | Yes | Strengthen coverage validation |
| `.audit/**` | Runtime only | Regenerated, ignored, not committed |

### 2.2 Allowed Write Set

- `Harness/PLAN.md`
- `Harness/features/03-paper-evidence-coverage.md`
- `references/figure-style-rule-map.md`
- `references/figure-audit-register.md`
- `scripts/check_style_coverage.py`
- `docs/superpowers/plans/2026-06-24-wf-eight-goals.md` only for status sync

### 2.3 Approach

1. RED: update `scripts/check_style_coverage.py` to require the new rule map and run it before the map exists.
2. Audit: rerun PDF inventory, contact sheets, and palette scripts against the local corpus.
3. GREEN: write the rule map from local evidence and known figure families.
4. Verify: run style coverage, skill validation, Harness validation, whitespace check, and reviewer pass.

---

## 3. Verification

### 3.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/check_style_coverage.py` | Failed as RED | Missing `references/figure-style-rule-map.md` |
| `python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json` | Passed | Wrote 15 PDF records |
| `python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets` | Passed | Wrote 15 contact sheets |
| `python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json` | Passed | Wrote palette summaries for 15 PDFs |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 3.2 Review Findings

- Leibniz found no blocking coverage, validator, or regenerated-audit issues. One P2 status drift finding was addressed by syncing this feature record, the eight-goal roadmap, and `Harness/PLAN.md`.

### 3.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- PDF text-layer marker counts include citation mentions and figure-index pages; authoritative per-group ranges remain the curated register and contact-sheet visual audit.

---

## 4. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Initial version | Start Goal 3 |
| 2 | 2026-06-24 | Added rule map, validator strengthening, PDF audit evidence, review closeout | Close Goal 3 |
