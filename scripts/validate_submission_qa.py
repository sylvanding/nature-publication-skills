#!/usr/bin/env python3
"""Validate the Nature submission QA skill and repository routing."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QA_SKILL = ROOT / "skills" / "nature-publication-submission-qa"
README = ROOT / "README.md"
INSTALLER = ROOT / "scripts" / "install_skills.py"
PLUGIN = ROOT / ".codex-plugin" / "plugin.json"
REPO_LINK = ROOT / ".agents" / "skills" / "nature-publication-submission-qa"

CHECKS = {
    "SKILL.md": [
        "target journal -> submission stage -> files available -> risk areas -> missing inputs",
        "references/submission-readiness-checklist.md",
        "references/figure-and-image-integrity.md",
        "references/data-code-reporting.md",
        "references/supplementary-consistency.md",
        "Do not approve",
    ],
    "references/submission-readiness-checklist.md": [
        "Manuscript text",
        "Main figures",
        "Extended Data",
        "Supplementary Information",
        "Statistics",
        "Editorial policy",
    ],
    "references/figure-and-image-integrity.md": [
        "scale bars",
        "image integrity",
        "generative AI",
        "RGB",
        "editable",
        "accessibility",
    ],
    "references/data-code-reporting.md": [
        "Data availability",
        "Code availability",
        "Reporting summary",
        "statistics",
        "AI use",
    ],
    "references/supplementary-consistency.md": [
        "Supplementary",
        "Extended Data",
        "panel labels",
        "cross-reference",
        "file inventory",
    ],
}


def main() -> int:
    errors: list[str] = []
    if not QA_SKILL.exists():
        errors.append(f"missing submission QA skill directory: {QA_SKILL.relative_to(ROOT)}")
    else:
        for rel, terms in CHECKS.items():
            path = QA_SKILL / rel
            if not path.exists():
                errors.append(f"missing submission QA file: {path.relative_to(ROOT)}")
                continue
            text = path.read_text(encoding="utf-8")
            for term in terms:
                if term not in text:
                    errors.append(f"{path.relative_to(ROOT)} missing required term: {term!r}")
        openai_yaml = QA_SKILL / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            errors.append("submission QA skill missing agents/openai.yaml")

    installer_text = INSTALLER.read_text(encoding="utf-8") if INSTALLER.exists() else ""
    if "nature-publication-submission-qa" not in installer_text:
        errors.append("installer does not include nature-publication-submission-qa")

    plugin_text = PLUGIN.read_text(encoding="utf-8") if PLUGIN.exists() else ""
    if "submission" not in plugin_text.lower():
        errors.append("plugin metadata does not mention submission QA capability")

    readme_text = README.read_text(encoding="utf-8") if README.exists() else ""
    if "nature-publication-submission-qa" not in readme_text:
        errors.append("README does not list nature-publication-submission-qa")
    if "python scripts/validate_submission_qa.py" not in readme_text:
        errors.append("README validation matrix missing submission QA validator")

    if not REPO_LINK.exists():
        errors.append(f"missing repo-scoped skill link: {REPO_LINK.relative_to(ROOT)}")

    if errors:
        print("Submission QA validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Submission QA validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
