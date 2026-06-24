# PRD: nature-publication-skills

> **Audience**: AI + future you. Not for PM approval — for implementation and review.
> **Principle**: One page max. Use checkboxes, not prose. Negative definitions > positive definitions.
>
> Philosophy source: Miqdad Jaffer (OpenAI)'s lean PRD template for the AI era.

---

## 1. Why

`nature-publication-skills` exists to give agents a source-backed, installable skill set for Nature-family manuscript writing and publication-figure work. The repository must keep the scientific style guidance, visual evidence, installation paths, and validation commands discoverable without asking future agents to infer project rules from chat history.

## 2. MVP Scope

### v0.1 Must Be Able To

> Each item below must be split into a separate `Harness/features/<name>.md` created from `Harness/features/_template.md` before implementation begins. One feature = one doc = one implementation unit.

- [x] Provide two complete Agent Skills: `nature-publication-writing` and `nature-publication-figure`.
- [x] Preserve source-backed references for writing style, figure style, color rules, plotting toolchain, QA/export rules, and external installation sources.
- [x] Install, update, inspect, and uninstall the skills for Codex and Claude Code using symlink or copy modes.
- [x] Expose an npm-compatible CLI wrapper through `bin/nature-publication-skills.mjs`.
- [x] Validate skill structure, local links, dependency presence, and figure example language through repository scripts.
- [x] Provide Harness routing docs so future agents can plan, audit, execute, and verify changes without overwriting existing project files.

### Explicitly Out of Scope

- Building a web application, hosted service, or interactive UI for the skills.
- Replacing root `README.md`, existing skills, source references, install scripts, or plugin metadata during Harness bootstrap.
- Committing raw paper PDFs from `references-papers-dai-tsinghua/` or generated `.audit/` artifacts.
- Adding optional stack-specific workflows such as React, browser E2E, or unrelated ECC automation before a real project need exists.
- Treating Harness docs as scientific authority; Nature writing and figure guidance remains owned by `skills/**` and `references/**`.

## 3. Decision Priorities

1. **Source Preservation** — Existing skill text, source references, and validation scripts are project facts and must not be overwritten by scaffolding.
2. **Verifiability** — Every install or guidance change needs a command, link check, strict Harness check, or recorded manual limitation.
3. **Agent Safety** — Future agents should load the smallest relevant context and update durable files instead of relying on chat transcript state.
4. **Distribution Reliability** — Codex, Claude Code, npm, and plugin metadata paths should stay aligned.
5. **Simplicity** — Add only the Harness governance needed for this skills repository. Avoid speculative abstraction or app architecture.

## 4. Users & Usage Scenarios

| User Role | Core Scenario | Frequency | Pain Point |
| --- | --- | --- | --- |
| Repository maintainer | Update Nature-style writing or figure skills after reading new sources, then validate and publish | Frequent during skill refinement | Easy to lose provenance or break install paths while editing rich Markdown skills |
| Agent user | Install the skills into a Codex or Claude Code user/repo scope and invoke them from another project | Occasional but important | Needs clear install/update/status commands and a predictable skill discovery layout |
| Future coding agent | Modify the repo safely after context loss or handoff | Frequent in agentic work | Needs durable plan, architecture, and verification instructions instead of ad hoc chat memory |

## 5. Acceptance Criteria

- [ ] `node Harness/scripts/validate-harness.mjs --strict` passes with no unresolved project fact placeholders.
- [ ] `python scripts/validate_skills.py` passes.
- [ ] Repo-scoped dry-run install and status commands succeed for Codex.
- [ ] `npm pack --dry-run` succeeds and still includes the existing distributable files.
- [ ] `git diff --check` reports no whitespace errors.
- [ ] The final diff shows existing project files preserved except for generated Harness additions.

## 6. Non-Functional Requirements

| Dimension | Target | Measurement |
| --- | --- | --- |
| Provenance | Every style or installation claim points to local references, official docs, or a recorded external source | Review `references/external-sources.md`, skill references, and Harness research results |
| Install safety | Install and update operations are idempotent unless `--force` or update mode is used | Dry-run install/status and installer code review |
| Context hygiene | Agents load routers first and avoid bulk-reading the whole Harness | `CLAUDE.md`, `AGENTS.md`, `Harness/README.md`, and `Harness/MEMORY.md` routing |
| Repository cleanliness | Raw PDFs and audit artifacts stay out of git | `.gitignore`, `git status --short`, and generated artifact paths |

---

## Fill Completion Standard

- [x] MVP and Non-goals are project facts; no `{{...}}` placeholders remain.
- [x] Decision priorities guide tradeoffs, not generic platitudes.
- [x] Every acceptance criterion is verifiable by test, command, or manual step.
- [x] If implementation diverges from the PRD, update this file before changing code.
