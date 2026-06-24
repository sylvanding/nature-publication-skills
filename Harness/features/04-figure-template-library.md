# Figure Template Library

> **Status**: Verified
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [03-paper-evidence-coverage.md](03-paper-evidence-coverage.md)

---

## 1. Requirements

### 1.1 Background

Goal 4 turns the figure skill v2 guidance into a first reusable template library slice. The first executable template is `multi_panel_microscopy_plate`, because it exercises dark microscopy panels, English labels, scale bars, palette tokens, vector/text export, PNG preview, and provenance sidecar behavior.

### 1.2 Goals

- Add skill-contained `assets/`, `templates/`, and `scripts/` for Nature-style figure generation.
- Implement deterministic `multi_panel_microscopy_plate` smoke generation.
- Add `scripts/validate_figure_templates.py` to generate and validate template outputs.
- Record dependencies and validation commands in README and requirements.

### 1.3 Non-Goals

- Do not implement all five template families in this slice.
- Do not present mock output as scientific evidence.
- Do not commit generated `.audit/template-smoke/**` outputs.

### 1.4 Acceptance Criteria

- [x] `skills/nature-publication-figure/assets/palettes.json` exists and defines required color tokens.
- [x] `skills/nature-publication-figure/templates/multi_panel_microscopy_plate.json` exists and declares panel/provenance contract.
- [x] `skills/nature-publication-figure/scripts/generate_multi_panel_microscopy_plate.py` generates PDF, PNG, and sidecar JSON.
- [x] `scripts/validate_figure_templates.py` fails before artifacts exist and passes after implementation.
- [x] Generated smoke output contains English-only figure text, expected palette tokens, and required sidecar keys.
- [x] Visual inspection of `.audit/template-smoke/multi_panel_microscopy_plate.png` finds no obvious overlap/clipping.
- [x] `python scripts/validate_figure_templates.py` passes.
- [x] `python scripts/validate_skills.py` passes.
- [x] `python scripts/check_style_coverage.py` passes.
- [x] `git diff --check` passes.

---

## 2. Design

### 2.1 Impact Scope

| Area | Impacted? | Notes |
| --- | --- | --- |
| `skills/nature-publication-figure/assets/**` | Yes | Palette tokens installed with the skill |
| `skills/nature-publication-figure/templates/**` | Yes | Template contract installed with the skill |
| `skills/nature-publication-figure/scripts/**` | Yes | Runnable generator installed with the skill |
| `scripts/validate_figure_templates.py` | Yes | Repo-level smoke validator |
| `requirements.txt` | Yes | Adds matplotlib/numpy runtime dependencies |
| `.audit/template-smoke/**` | Runtime only | Generated and ignored |

### 2.2 Approach

1. RED: add `scripts/validate_figure_templates.py` and run it before template artifacts exist.
2. GREEN: add palette/config/generator and run the validator.
3. Visual QA: inspect generated PNG and fix overlap/clipping.
4. Wire validation into README and `scripts/validate_skills.py`.
5. Review and close out.

---

## 3. Verification

### 3.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python scripts/validate_figure_templates.py` | Failed as RED | Missing generator, palette asset, and template config |
| `python scripts/validate_figure_templates.py` | Passed | Generated PDF, PNG, and provenance sidecar |
| Visual inspection | Passed after fix | Moved `Mock-only` label away from SNR bar to avoid clipping/overlap |
| `python scripts/validate_skills.py` | Passed | Output: `Validation passed.` |
| `python scripts/validate_figure_v2.py` | Passed | Output: `Figure v2 validation passed.` |
| `python scripts/check_style_coverage.py` | Passed | Output: `Style coverage check passed.` |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Output: `Harness validation passed (strict).` |
| `npm pack --dry-run` | Passed | Tarball includes new figure assets, scripts, and templates |
| `git diff --check` | Passed | Exit 0 with no whitespace findings |

### 3.2 Review Findings

- Aristotle found stale README dependency instructions, sidecar field-name mismatch, and phase metadata drift. Fixed by routing dependency installation through `requirements.txt`, aligning the catalog sidecar fields with `pixel_size_um` and `scale_bar_um`, and syncing `Harness/PLAN.md` phase state.

### 3.3 Closeout

- [x] Acceptance criteria satisfied.
- [x] Verification commands recorded.
- [x] Reviewer findings resolved or documented.
- [x] Remaining risks listed.

Remaining risks:

- Only the first executable template is implemented in this slice; the remaining template families are still contracts and should be implemented incrementally.

---

## 4. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Initial version | Start Goal 4 |
| 2 | 2026-06-24 | Added first executable template, validator, dependency/docs updates, review closeout | Close Goal 4 |
