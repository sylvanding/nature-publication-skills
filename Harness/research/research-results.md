# nature-publication-skills - Research Results

> **Purpose**: Record final research results and decisions. Use [README.md](README.md) for process, tools, queries, and research-agent rules.
> **Principle**: Each candidate has a clear Purpose / Strength / Weakness / Decision.

---

## Research Date

2026-06-24

## Research Goal

Configure `create-harness-vibe-coding` for an existing Agent Skills repository while preserving current project files, install paths, source evidence, and validation commands.

---

## Candidate References

### 1) create-harness-vibe-coding README

- **What it is**: The upstream generator README that defines one-command bootstrap, Agent-link intake, existing-project dry-run, conflict skipping, generated Harness files, and post-bootstrap validation.
- **Source Type**: GitHub repo
- **Checked Date**: 2026-06-24
- **Strengths**: Gives the exact existing-project sequence used here: dry-run first, preserve conflicts with skip behavior, then follow `Harness/SETUP.md`.
- **Weaknesses**: Generic scaffold; it does not know this repository's Nature skills, source evidence, install commands, or ignored raw PDF inputs.
- **Decision**: Adopt for Harness bootstrap process only.
- **Link**: https://github.com/zingspark/create-harness-vibe-coding

### 2) Existing repository README, install docs, and scripts

- **What it is**: Local project source of truth for skills, evidence index, installation/update commands, validation commands, npm wrapper, plugin metadata, and ignored audit inputs.
- **Source Type**: Local project files
- **Checked Date**: 2026-06-24
- **Strengths**: Describes the real repository behavior and command surface; `scripts/validate_skills.py` codifies structural requirements.
- **Weaknesses**: No CI workflow was present, so validation is currently command-driven rather than CI-enforced.
- **Decision**: Adopt as project facts that Harness must preserve.
- **Link**: [../../README.md](../../README.md), [../../docs/installation.md](../../docs/installation.md), [../../scripts/validate_skills.py](../../scripts/validate_skills.py)

### 3) External source register for Agent Skills and Nature guidance

- **What it is**: The repository's curated list of official docs, public skill repositories, Nature/Springer Nature guidance, and source-backed usage discipline.
- **Source Type**: Local evidence register with external links
- **Checked Date**: 2026-06-24
- **Strengths**: Keeps provenance for Agent Skills structure and scientific writing/figure guidance separate from generated Harness docs.
- **Weaknesses**: The file notes that policy-like external facts should be rechecked before publication-sensitive use.
- **Decision**: Adopt as preserved evidence base; Harness should point to it rather than duplicate scientific rules.
- **Link**: [../../references/external-sources.md](../../references/external-sources.md)

---

## Final Decision

- **Architecture Style**: Documentation-first Agent Skills repository with a thin install/update CLI, source-backed skill folders, generated Harness governance, and filesystem-based install targets.
- **Core References**: Upstream create-harness README for bootstrap; local README/install docs/scripts for project behavior; local external-source register for skills and Nature evidence.
- **Key Constraints**:
  - Preserve current project files and skipped `README.md` conflict.
  - Keep skill source under `skills/**`; install targets are derived symlinks or copies.
  - Keep raw paper PDFs and audit outputs outside git.
  - Treat Harness as agent workflow governance, not as the scientific style authority.

---

## Not Adopted But Worth Watching

- Optional React/browser workflow packs from Harness; not relevant until this repository gains a UI.
- Replacing `README.md` with the generated README; rejected because current README owns project commands and evidence overview.
- CI workflow generation; useful later, but the current request only authorized missing Harness conventions.
