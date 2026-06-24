#!/usr/bin/env python3
"""Validate install and distribution packaging for Nature Publication Skills."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_JSON = ROOT / "package.json"
PLUGIN_JSON = ROOT / ".codex-plugin" / "plugin.json"
README = ROOT / "README.md"
INSTALL_DOC = ROOT / "docs" / "installation.md"
DISTRIBUTION_DOC = ROOT / "docs" / "distribution.md"

REQUIRED_PACKAGE_FILES = [
    ".codex-plugin/plugin.json",
    "docs/installation.md",
    "docs/distribution.md",
    "requirements.txt",
    "skills/nature-publication-figure/SKILL.md",
    "skills/nature-publication-figure/agents/openai.yaml",
    "skills/nature-publication-figure/assets/palettes.json",
    "skills/nature-publication-figure/scripts/generate_multi_panel_microscopy_plate.py",
    "skills/nature-publication-figure/templates/multi_panel_microscopy_plate.json",
    "skills/nature-publication-writing/SKILL.md",
    "skills/nature-publication-writing/agents/openai.yaml",
    "skills/nature-publication-writing/references/benchmarks/golden/writing/rubric.md",
    "skills/nature-publication-writing/references/benchmarks/prompts/writing/title.md",
    "skills/nature-publication-submission-qa/SKILL.md",
    "skills/nature-publication-submission-qa/agents/openai.yaml",
    "skills/nature-publication-submission-qa/references/submission-readiness-checklist.md",
    "skills/nature-publication-submission-qa/references/figure-and-image-integrity.md",
    "skills/nature-publication-submission-qa/references/data-code-reporting.md",
    "skills/nature-publication-submission-qa/references/supplementary-consistency.md",
    "scripts/validate_distribution.py",
]
FORBIDDEN_PACKAGE_PREFIXES = [
    "docs/superpowers/",
    ".audit/",
    "references-papers-dai-tsinghua/",
]
REQUIRED_DISTRIBUTION_TERMS = [
    "Codex",
    "Claude Code",
    "npx",
    "Codex Plugin",
    "GitHub CLI",
    "gh skill",
    "public preview",
    "Release checklist",
    "Update safety",
    "npm pack --dry-run",
]


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False)


def npm_pack_files() -> tuple[list[str], str | None]:
    result = run(["npm", "pack", "--dry-run", "--json"])
    if result.returncode != 0:
        return [], f"npm pack --dry-run --json failed:\n{result.stdout}"
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        return [], f"npm pack --dry-run --json returned invalid JSON: {exc}\n{result.stdout}"
    if not payload:
        return [], "npm pack --dry-run --json returned an empty payload"
    files = sorted(item["path"] for item in payload[0].get("files", []))
    return files, None


def main() -> int:
    errors: list[str] = []

    for path in (PACKAGE_JSON, PLUGIN_JSON, README, INSTALL_DOC, DISTRIBUTION_DOC):
        if not path.exists():
            errors.append(f"missing distribution file: {path.relative_to(ROOT)}")

    if PACKAGE_JSON.exists():
        package = json.loads(PACKAGE_JSON.read_text(encoding="utf-8"))
        if "docs" in package.get("files", []):
            errors.append("package.json files must not include raw docs/ because it ships internal docs/superpowers plans")

    if PLUGIN_JSON.exists():
        plugin = json.loads(PLUGIN_JSON.read_text(encoding="utf-8"))
        if plugin.get("skills") != "./skills/":
            errors.append(".codex-plugin/plugin.json must point skills to ./skills/")

    files, pack_error = npm_pack_files()
    if pack_error:
        errors.append(pack_error)
    else:
        file_set = set(files)
        for required in REQUIRED_PACKAGE_FILES:
            if required not in file_set:
                errors.append(f"npm package missing required file: {required}")
        for path in files:
            for prefix in FORBIDDEN_PACKAGE_PREFIXES:
                if path.startswith(prefix):
                    errors.append(f"npm package includes forbidden internal/source path: {path}")

    if DISTRIBUTION_DOC.exists():
        doc = DISTRIBUTION_DOC.read_text(encoding="utf-8")
        for term in REQUIRED_DISTRIBUTION_TERMS:
            if term not in doc:
                errors.append(f"{DISTRIBUTION_DOC.relative_to(ROOT)} missing required term: {term!r}")

    readme_text = README.read_text(encoding="utf-8") if README.exists() else ""
    if "docs/distribution.md" not in readme_text:
        errors.append("README must link docs/distribution.md")
    if "python scripts/validate_distribution.py" not in readme_text:
        errors.append("README validation matrix missing distribution validator")

    install_doc = INSTALL_DOC.read_text(encoding="utf-8") if INSTALL_DOC.exists() else ""
    if "docs/distribution.md" not in install_doc:
        errors.append("installation doc must link distribution doc")

    smoke_root = ROOT / ".audit" / "install-smoke-distribution"
    if smoke_root.exists():
        shutil.rmtree(smoke_root)
    for agent in ("codex", "claude"):
        target_repo = smoke_root / agent
        result = run(
            [
                sys.executable,
                "scripts/install_skills.py",
                "install",
                "--agent",
                agent,
                "--scope",
                "repo",
                "--repo",
                str(target_repo),
                "--mode",
                "copy",
                "--force",
            ]
        )
        if result.returncode != 0:
            errors.append(f"copy install smoke failed for {agent}:\n{result.stdout}")
            continue
        target_root = target_repo / (".agents/skills" if agent == "codex" else ".claude/skills")
        for skill in ("nature-publication-figure", "nature-publication-writing", "nature-publication-submission-qa"):
            skill_dir = target_root / skill
            if not (skill_dir / "SKILL.md").exists():
                errors.append(f"copy install smoke missing {skill}/SKILL.md for {agent}")
        if agent == "codex" and not (target_root / "nature-publication-figure" / "assets" / "palettes.json").exists():
            errors.append("copy install smoke missing figure palette asset for codex")
        if agent == "codex" and not (
            target_root
            / "nature-publication-writing"
            / "references"
            / "benchmarks"
            / "golden"
            / "writing"
            / "rubric.md"
        ).exists():
            errors.append("copy install smoke missing writing benchmark rubric for codex")
        if agent == "codex" and not (
            target_root / "nature-publication-submission-qa" / "references" / "data-code-reporting.md"
        ).exists():
            errors.append("copy install smoke missing submission QA data/code reference for codex")

    if errors:
        print("Distribution validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Distribution validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
