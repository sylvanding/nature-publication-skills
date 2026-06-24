# Harness Bootstrap Closeout

> **Status**: Done
> **Created**: 2026-06-24
> **Version**: 1
> **Owner**: main agent
> **Related Docs**: [PLAN.md](../PLAN.md), [WF.md](../WF.md), [architecture.md](../architecture.md)

---

## 1. Requirements

### 1.1 Background

The initial `create-harness-vibe-coding` bootstrap was generated, validated, committed, and pushed on `harness-vibe-coding-bootstrap`. `Harness/SETUP.md` is a bootstrap scaffold, and its own instructions say it is temporary after setup is complete. The active WF roadmap starts by closing this state cleanly so future agents enter normal Harness mode instead of repeatedly re-running setup.

### 1.2 Goals

- Record the current WF roadmap as the active `Harness/PLAN.md` state.
- Retire the temporary setup scaffold after bootstrap verification.
- Keep Harness strict validation green after retiring setup.
- Add a regression test that proves the validator accepts a post-bootstrap repository without `Harness/SETUP.md`.

### 1.3 Non-Goals

- Do not change skill content, install behavior, package metadata, or README content in this slice.
- Do not delete any generated Harness runtime files other than the temporary setup scaffold.
- Do not commit generated `.audit/**` artifacts.

### 1.4 Acceptance Criteria

- [x] `Harness/SETUP.md` is removed after its setup cleanup rule is satisfied.
- [x] `CLAUDE.md` no longer tells agents to follow `Harness/SETUP.md` before normal work.
- [x] `Harness/scripts/validate-harness.mjs` supports both bootstrap mode when `Harness/SETUP.md` exists and post-bootstrap mode when it is absent.
- [x] A regression test covers the post-bootstrap mode.
- [x] `node Harness/scripts/validate-harness.mjs --strict` passes.
- [x] `python tests/test_validate_harness.py` passes.
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
| `Harness/architecture.md` | No | No architecture boundary changes |
| `Harness/domain/ports.md` | No | No port changes |
| `Harness/data-flow.md` | No | No runtime flow changes |
| `Harness/state-machines.md` | No | No state machine changes |
| tests | Yes | Add validator regression test |

### 2.2 Allowed Write Set

- `CLAUDE.md`
- `Harness/PLAN.md`
- `Harness/SETUP.md`
- `Harness/scripts/validate-harness.mjs`
- `Harness/features/01-bootstrap-closeout.md`
- `tests/test_validate_harness.py`
- `docs/superpowers/plans/2026-06-24-wf-eight-goals.md`

### 2.3 Forbidden Scope

- `skills/**`
- `references/**`
- `scripts/install_skills.py`
- `scripts/validate_skills.py`
- `package.json`
- `.codex-plugin/**`
- `README.md`
- `.audit/**`
- `references-papers-dai-tsinghua/**`

### 2.4 Approach

#### Candidate Approaches

| Approach | Pros | Cons | Decision |
| --- | --- | --- | --- |
| Keep `Harness/SETUP.md` indefinitely | No validator changes | Future agents keep re-entering bootstrap path and `PLAN.md` remains conceptually stale | Reject |
| Delete `Harness/SETUP.md` and update validator for post-bootstrap mode | Matches setup closeout instructions and keeps future sessions in normal mode | Requires a small validator regression test | Accept |
| Delete setup without test | Fast | No protection against validator regressions | Reject |

#### Rationale

This repository already completed the bootstrap vertical slice: generated files exist, strict validation passed, the branch was committed and pushed. The smallest durable closeout is to remove the bootstrap-only file, remove the active startup reference, and teach the validator that this is a valid post-bootstrap state.

### 2.5 Edge Cases

- `Harness/SETUP.md` exists but `CLAUDE.md` lacks the setup line -> validator should fail in bootstrap mode.
- `Harness/SETUP.md` is absent but `CLAUDE.md` still points agents to it -> validator should fail in post-bootstrap mode.
- `Harness/SETUP.md` is absent and the setup line is absent -> validator should pass if all other Harness checks pass.

---

## 3. Tasks

| # | Task | Owner | Write Set | Verify |
| --- | --- | --- | --- | --- |
| 1 | Write post-bootstrap validator regression test | main | `tests/test_validate_harness.py` | `python tests/test_validate_harness.py` fails before validator patch |
| 2 | Update validator setup contract logic | main | `Harness/scripts/validate-harness.mjs` | `python tests/test_validate_harness.py` passes |
| 3 | Retire setup scaffold and active startup reference | main | `CLAUDE.md`, `Harness/SETUP.md` | `node Harness/scripts/validate-harness.mjs --strict` |
| 4 | Record closeout evidence | main | `Harness/PLAN.md`, this feature doc | `git diff --check` |

### Subagent Plan

| Agent / Pass | Required? | Mode | Read Boundary | Write Set | Verify |
| --- | --- | --- | --- | --- | --- |
| Planner | Yes | Parallel Read | Roadmap and Harness files | none | `Dirac` handoff |
| Researcher / Docs Researcher | No | Parallel Read | Not needed for this local closeout slice | none | N/A |
| Architect | Yes | Parallel Read | Harness architecture and setup state | none | `Euclid` handoff |
| Explorer Pass | No | Parallel Read | Main agent has small write set | none | N/A |
| Test Writer | No | Serial Write | Main agent writes one regression test | `tests/test_validate_harness.py` | `python tests/test_validate_harness.py` |
| Implementer / Debugger | No | Serial Write | Main agent patch is small and bounded | declared files | validators |
| Reviewer | Pending | Parallel Read | Final diff | none | review handoff if needed |
| Verifier | Pending | Parallel Read | Final command matrix | none | command evidence |

---

## 4. Verification

### 4.1 Test Results

| Command | Result | Notes |
| --- | --- | --- |
| `python tests/test_validate_harness.py` | Failed, then passed | RED failed with `CLAUDE.md missing setup bootstrap contract`; GREEN passed after validator update; negative tests cover stale post-bootstrap reference and missing bootstrap contract |
| `node Harness/scripts/validate-harness.mjs --strict` | Passed | Post-bootstrap strict validation passed |
| `python scripts/validate_skills.py` | Passed | Skill validation unaffected |
| `git diff --check` | Passed | No whitespace errors |

### 4.2 Review Findings

- None.

### 4.3 Docs Sync

- [ ] `Harness/architecture.md`
- [ ] `Harness/domain/ports.md`
- [ ] `Harness/data-flow.md`
- [ ] `Harness/state-machines.md`
- [ ] `Harness/research/research-results.md`
- [x] Not needed because this slice changes bootstrap workflow state, not architecture, ports, data flow, state machines, or research decisions.

### 4.4 Decision Log

| Date | Decision | Reason |
| --- | --- | --- |
| 2026-06-24 | Retire `Harness/SETUP.md` after bootstrap validation | Setup file is explicitly temporary and the branch has a verified bootstrap commit |

### 4.5 Closeout

- [x] Acceptance criteria satisfied.
- [x] Tests or manual verification recorded.
- [x] Boundary impact documented.
- [x] Remaining risks listed or explicitly none.
- [x] If docs/code/tests conflicted, Decision Log records how it was resolved.

Remaining risks:

- None.

---

## 5. Changelog

| Version | Date | What Changed | Reason |
| --- | --- | --- | --- |
| 1 | 2026-06-24 | Initial version | Start Goal 1 closeout |
