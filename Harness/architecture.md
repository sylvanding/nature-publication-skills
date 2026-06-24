# Harness Architecture — nature-publication-skills

> **Responsibility**: Defines the system layering structure, component overview, and key design decisions.
> **Does NOT cover**: Code details (AI can read code), API documentation (placed in docstrings).
>
> Philosophical sources: arc42 Chapter 5 (Building Block View) + C4 Model Level 3 (Component) + matklad's lightweight ARCHITECTURE.md.

---

## 1. Layering Rules

`nature-publication-skills` is a documentation-first Agent Skills repository with a small CLI wrapper. It is not a web application, server, or long-running runtime.

```
┌────────────────────────────────────────────┐
│ Agent/User Entry                           │
│ README.md, AGENTS.md, CLAUDE.md, Harness/  │
│ May read: project docs and generated routes│
├────────────────────────────────────────────┤
│ Harness Governance                         │
│ Harness/** and .claude/**                  │
│ May depend on: project facts               │
│ Must not redefine scientific style rules   │
├────────────────────────────────────────────┤
│ Distribution Tooling                       │
│ bin/**, scripts/install_skills.py,         │
│ scripts/validate_skills.py, package.json   │
│ May depend on: skills/** and filesystem    │
├────────────────────────────────────────────┤
│ Skill Source                               │
│ skills/nature-publication-writing/**       │
│ skills/nature-publication-figure/**        │
│ May depend on: local references/**         │
├────────────────────────────────────────────┤
│ Evidence and Audit Inputs                  │
│ references/**, references-papers... local  │
│ .audit/** generated outputs                │
│ Owned by: source/audit workflow            │
├────────────────────────────────────────────┤
│ Install Targets                            │
│ .agents/skills, .claude/skills, user paths │
│ Derived from source by symlink or copy     │
└────────────────────────────────────────────┘
```

**Hard Constraints**:

- `skills/**` is the canonical source for skill content; `.agents/skills/**`, `.claude/skills/**`, and user install paths are derived targets.
- `references/**` records curated evidence and source indexes; raw PDFs under `references-papers-dai-tsinghua/**` are local inputs and must stay out of git.
- `.audit/**` is generated verification output and must stay out of git.
- Harness files route and govern agent work; they do not replace `README.md`, skill instructions, scientific evidence, or installer behavior.
- Existing project command truth stays in `README.md` and `docs/installation.md`.

---

## 2. Interface Decoupling

Use interfaces or ports to protect real boundaries, not to create abstraction for its own sake.

Real boundaries in this repository:

- **CLI process boundary**: `bin/nature-publication-skills.mjs` invokes `scripts/install_skills.py` through a Python subprocess.
- **Filesystem install boundary**: `scripts/install_skills.py` writes symlinks or copies into Codex and Claude Code discovery paths.
- **Evidence input boundary**: audit scripts read large local PDFs from `references-papers-dai-tsinghua/**` and write generated outputs under `.audit/**`.
- **Agent governance boundary**: `AGENTS.md`, `CLAUDE.md`, `.claude/**`, and `Harness/**` guide future coding agents but cannot silently change project facts.

Ports should be documented only around these boundaries. Direct helper functions inside a single script do not need extra abstractions.

Avoid speculative abstraction: do not add factories, service locators, plugin registries, or new app layers unless a second real caller or replacement need appears.

---

## 3. State Design

State must have one owner, legal transitions, and observable recovery behavior.

| State Slice | Owner | Persistence | Notes |
| --- | --- | --- | --- |
| Skill source content | `skills/**` | durable git state | Edited directly and validated by `scripts/validate_skills.py` |
| Repo-scoped skill links | `.agents/skills/**` | durable git state as symlinks | Derived from `skills/**`; validator checks expected links exist |
| User/repo install metadata | target discovery directory | durable external filesystem state | `.nature-publication-skills-install.json` records source, commit, mode, agent, scope, and installed skills |
| Audit outputs | `.audit/**` | generated local state | Recreated by audit scripts and ignored by git |
| Raw paper corpus | `references-papers-dai-tsinghua/**` | local external input | User-provided, large, ignored by git |
| Harness task progress | `Harness/PLAN.md` | durable git state | Updated during multi-step work and handoff |

Long-running implementation work should store resumable progress in `Harness/PLAN.md#Heartbeat`. The current repository has no background job, database, browser session, or service state machine.

---

## 4. Core Components

### 4.1 Skill Corpus

- **Responsibility**: Contains the two Nature-family skills and their progressive-disclosure references.
- **Design Decision**: Keep detailed writing and figure guidance inside each skill's `references/` folder — Rationale: avoids overloading `SKILL.md` and keeps source-backed evidence near the skill that uses it.
- **Does NOT handle**: Installing itself into external agent discovery paths.

### 4.2 Install and Update CLI

- **Responsibility**: Installs, updates, reports status, and uninstalls skills for Codex and Claude Code.
- **Design Decision**: `bin/nature-publication-skills.mjs` stays a thin Node wrapper over the Python installer — Rationale: supports `npx` distribution without duplicating install logic.
- **Does NOT handle**: Scientific style decisions or reference-paper analysis.

### 4.3 Validation and Audit Scripts

- **Responsibility**: Validate skill structure, links, dependencies, figure-language rules, PDF figure inventory, contact sheets, palette summaries, and style coverage.
- **Design Decision**: Keep audit products in `.audit/**` — Rationale: generated image/PDF-derived artifacts are large, local, and reproducible.
- **Does NOT handle**: Publishing artifacts or replacing the curated source references automatically.

### 4.4 Evidence Register

- **Responsibility**: Records local paper indexes, figure audit coverage, PDF hashes, and external source provenance.
- **Design Decision**: Store summary evidence in Markdown under `references/**` — Rationale: future agents can verify claims without re-reading every raw PDF first.
- **Does NOT handle**: Acting as a substitute for rechecking unstable policy facts before submission-sensitive use.

### 4.5 Harness Governance

- **Responsibility**: Provides agent routing, planning, dispatch, review, verification, and memory conventions.
- **Design Decision**: Keep Harness files additive and project-fact-based — Rationale: the repository already has a working skills/install architecture.
- **Does NOT handle**: Replacing root README, generated package metadata, skills, install scripts, or scientific references.

---

## 5. Architectural Constraints (Non-Negotiable)

- Do not overwrite existing project files during Harness upgrades unless the user explicitly approves the exact file scope.
- Keep command and installation truth in `README.md`, `docs/installation.md`, and the scripts that implement it.
- Keep source-backed scientific style rules in `skills/**` and `references/**`; Harness may link or summarize project facts but must not invent new style doctrine.
- New install behavior must update both Python and npm wrapper validation expectations when applicable.
- Rejections and failures must be testable or documented with manual verification steps in the feature doc or `Harness/PLAN.md`.
- Audit outputs and raw paper inputs must remain ignored unless the user explicitly changes repository artifact policy.
