# Port Contracts — nature-publication-skills

> **Responsibility**: Define cross-layer interface contracts. These are the legal contracts of a layered architecture. Each port documents not only its signature, but also preconditions, postconditions, and error semantics.
>
> **Principle**: Port documentation is not API reference documentation. It is a contract that specifies caller obligations and implementer guarantees.
>
> Philosophical origins: Bertrand Meyer's Design by Contract (Eiffel) + Alistair Cockburn's hexagonal architecture port documentation.

---

## 1. Port Classification

Create a port only for a real boundary: external service, storage, SDK, process, browser/API boundary, permission boundary, or cross-layer dependency. Do not create a port only because an interface might be useful someday.

### 1.1 Driving Ports (Inbound — external calls project tooling)

| Port | Definition Location | Purpose |
| --- | --- | --- |
| `SkillInstallCommand` | `scripts/install_skills.py`, `bin/nature-publication-skills.mjs` | External callers install, update, inspect, or uninstall skill folders for Codex or Claude Code |
| `SkillRepositoryValidationCommand` | `scripts/validate_skills.py` and README validation commands | Maintainers and agents verify skill structure, links, dependencies, and install command coverage |

### 1.2 Driven Ports (Outbound — project tooling touches external state)

| Port | Definition Location | Purpose |
| --- | --- | --- |
| `AgentSkillFilesystemTarget` | `scripts/install_skills.py::default_target`, `install_one`, `write_metadata` | Write symlinks or copies plus install metadata into user or repo agent discovery paths |
| `ReferencePaperAuditInput` | `scripts/build_pdf_figure_inventory.py`, `scripts/make_pdf_contact_sheets.py`, `scripts/analyze_pdf_palette.py` | Read ignored local PDF inputs and emit reproducible audit artifacts under `.audit/**` |

---

## 2. Port Definitions

### 2.1 `SkillInstallCommand`

- **Category**: Driving
- **Definition Location**: `scripts/install_skills.py`, wrapped by `bin/nature-publication-skills.mjs`
- **Contract Class**: CLI command contract

#### Purpose

Install, update, show status for, or uninstall the repository's complete skill directories without copying only `SKILL.md`.

#### Methods

Entrypoints:

- `python scripts/install_skills.py install`
- `python scripts/install_skills.py update`
- `python scripts/install_skills.py status`
- `python scripts/install_skills.py uninstall`
- `node bin/nature-publication-skills.mjs <same arguments>`

**Preconditions** (caller must guarantee):

- The command is run from a checkout containing `skills/nature-publication-writing/` and `skills/nature-publication-figure/`.
- `--repo` is provided when `--scope repo` is selected.
- The target path is safe to write when not using `--dry-run`.
- Existing targets are replaced only when `--force` or update mode is intentionally used.

**Postconditions** (implementer guarantees):

- Each selected skill is installed as either a symlink or full directory copy.
- The target root receives `.nature-publication-skills-install.json` unless `--dry-run` is used.
- `status` reports missing, symlink, or copied directory state for each selected skill.
- `dry-run` prints intended actions without creating, removing, or replacing target files.

**Error Semantics**:

| Exception Type | Trigger Condition | Caller Should |
| --- | --- | --- |
| `SystemExit` | Unknown skill name, missing `--repo` for repo scope, or existing target without replacement permission | Fix arguments or rerun with explicit `--force` only after reviewing the target |
| `subprocess.CalledProcessError` | `update --pull` cannot fast-forward the source checkout | Resolve git state before retrying update |
| Python filesystem exception | Target cannot be written, removed, linked, or copied | Check permissions and target path safety before retry |

**Idempotency**: Yes for already-correct symlink installs and `dry-run`; copy replacement requires `--force` or update mode.

#### Known Implementations

| Adapter | Location | Purpose |
| --- | --- | --- |
| Python installer | `scripts/install_skills.py` | Owns install/update/status/uninstall behavior |
| Node wrapper | `bin/nature-publication-skills.mjs` | Enables npm and `npx` invocation while delegating behavior to Python |

---

### 2.2 `SkillRepositoryValidationCommand`

- **Category**: Driving
- **Definition Location**: `scripts/validate_skills.py`, `README.md#Validation`
- **Contract Class**: CLI validation contract

#### Purpose

Prove that the repository remains a valid Agent Skills source and distribution package after edits.

#### Methods

Entrypoints:

- `python scripts/validate_skills.py`
- `python scripts/check_style_coverage.py`
- `python scripts/install_skills.py install --agent codex --scope repo --repo .audit/install-smoke --mode symlink --dry-run`
- `node bin/nature-publication-skills.mjs status --agent codex --scope repo --repo .audit/install-smoke --dry-run`
- `npm pack --dry-run`

**Preconditions**:

- Python dependencies listed in `requirements.txt` are installed for checks that import PyMuPDF and Pillow.
- Local links in Markdown point to committed files or intentionally ignored local evidence paths.
- `.agents/skills/**` repo-scoped links exist for both source skills.

**Postconditions**:

- Structural, link, plugin, package, dependency, and figure-code-language checks report either pass or explicit failures.
- Dry-run install/status commands exercise the repo-scoped Codex path without mutating `.audit/install-smoke`.
- `npm pack --dry-run` reports the files that would be published.

**Error Semantics**:

| Exception Type | Trigger Condition | Caller Should |
| --- | --- | --- |
| validation failure output | Broken link, missing metadata, missing dependency, missing skill link, invalid frontmatter, or CJK text inside figure code blocks | Patch the reported source file and rerun the exact command |
| missing module report | `fitz` or `PIL` is unavailable | Install `requirements.txt` or record the environment limitation |

**Idempotency**: Yes. Validation commands should not change tracked files; audit-specific commands write only ignored outputs when not in dry-run mode.

#### Known Implementations

| Adapter | Location | Purpose |
| --- | --- | --- |
| Skill validator | `scripts/validate_skills.py` | Main structural validation |
| Style coverage checker | `scripts/check_style_coverage.py` | Confirms skill references cover required style evidence |
| npm pack | `package.json` | Confirms distribution file selection |

---

### 2.3 `AgentSkillFilesystemTarget`

- **Category**: Driven
- **Definition Location**: `scripts/install_skills.py::default_target`, `install_one`, `write_metadata`
- **Contract Class**: Filesystem adapter contract

#### Purpose

Translate agent and scope arguments into concrete Codex or Claude Code discovery directories and write the selected skill directories there.

#### Methods

Operations:

- Resolve default user target paths.
- Resolve repo target paths.
- Create parent directories when installing or writing metadata.
- Write symlinks, copy directories, remove existing targets when authorized, and write metadata.

**Preconditions**:

- Caller supplies valid `agent`, `scope`, `repo`, `mode`, `skill`, `force`, and `dry_run` arguments.
- Source skill directories exist in this checkout.
- Target paths are not confused with the source directory unless intentionally installing repo-scoped links.

**Postconditions**:

- Installed targets contain complete skill folders or symlinks to complete skill folders.
- Metadata records source path, git commit, mode, agent, scope, selected skills, and update time.
- Uninstall removes only selected installed skill targets.

**Error Semantics**:

| Exception Type | Trigger Condition | Caller Should |
| --- | --- | --- |
| filesystem exception | Permission denied, broken parent path, unsupported symlink, copy failure, or remove failure | Inspect target path, choose copy mode if symlinks are unsupported, and rerun |
| explicit `SystemExit` | Existing target would be replaced without authorization | Review target and rerun with `--force` only if replacement is intended |

**Idempotency**: Symlink install is idempotent when the existing symlink already points to the source. Copy mode is intentionally replacement-gated.

#### Known Implementations

| Adapter | Location | Purpose |
| --- | --- | --- |
| Codex target resolver | `scripts/install_skills.py::default_target` | Maps user scope to `~/.agents/skills` and repo scope to `.agents/skills` |
| Claude Code target resolver | `scripts/install_skills.py::default_target` | Maps user scope to `~/.claude/skills` and repo scope to `.claude/skills` |

---

### 2.4 `ReferencePaperAuditInput`

- **Category**: Driven
- **Definition Location**: PDF audit scripts under `scripts/`
- **Contract Class**: Local evidence input contract

#### Purpose

Read user-provided local reference PDFs and generate reviewable audit summaries without committing raw or generated heavy artifacts.

#### Methods

Entrypoints:

- `python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json`
- `python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets`
- `python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json`

**Preconditions**:

- `references-papers-dai-tsinghua/**` exists locally and contains the user-provided PDF corpus.
- PyMuPDF and Pillow are installed.
- `.audit/**` is available for generated outputs.

**Postconditions**:

- Audit outputs are written under `.audit/**`.
- Tracked source references can be updated manually from reviewed audit evidence.
- Raw PDFs remain untracked.

**Error Semantics**:

| Exception Type | Trigger Condition | Caller Should |
| --- | --- | --- |
| missing path or empty corpus | The local raw PDF directory is absent or incomplete | Ask the user for the source corpus or skip with a recorded limitation |
| PDF/image processing exception | A PDF cannot be opened or rendered | Record the affected file and continue only if the script supports partial output |

**Idempotency**: Audit commands are reproducible for the same local PDF corpus and script version, but they overwrite or refresh generated `.audit/**` outputs.

#### Known Implementations

| Adapter | Location | Purpose |
| --- | --- | --- |
| Figure inventory builder | `scripts/build_pdf_figure_inventory.py` | Extracts figure/table coverage inventory |
| Contact sheet generator | `scripts/make_pdf_contact_sheets.py` | Renders page contact sheets for visual review |
| Palette analyzer | `scripts/analyze_pdf_palette.py` | Summarizes visual color usage from PDFs |

---

## 3. Cross-Port Invariants

- Full skill directories must move together; never install or validate only `SKILL.md`.
- Install targets are derived state. Source edits happen under `skills/**`, not in user install copies.
- Validation must remain runnable from a clean checkout with dependencies installed.
- Raw PDFs and `.audit/**` outputs are local evidence artifacts and do not become distribution files.
- Harness governance docs may constrain agent workflow but must not silently alter install behavior or scientific guidance.
- New ports need one clear owner and at least one real caller. Avoid speculative ports without a concrete adapter or testability need.
