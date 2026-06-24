#!/usr/bin/env python3
"""Validate reader-facing documentation productization."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INSTALL_DOC = ROOT / "docs" / "installation.md"
DISTRIBUTION_DOC = ROOT / "docs" / "distribution.md"
PLANNING_DOC = ROOT / "docs" / "planning" / "2026-06-23-nature-publication-skills-plan.md"

README_REQUIRED_TERMS = [
    "## Quickstart",
    "## Which Skill To Use",
    "## Install Mode Decision Table",
    "## Evidence And Provenance",
    "## Validation Matrix",
    "## Roadmap Completion",
    "## Update And Release Workflow",
    "Portable release checks",
    "Source checkout-only checks",
    "Harness/**",
    "nature-publication-writing",
    "nature-publication-figure",
    "nature-publication-submission-qa",
    "references/figure-style-rule-map.md",
    "skills/nature-publication-figure/references/figure-template-catalog.md",
    "skills/nature-publication-writing/references/benchmarks/golden/writing/rubric.md",
    "skills/nature-publication-submission-qa/references/submission-readiness-checklist.md",
    "python scripts/validate_docs_productization.py",
    "node Harness/scripts/validate-harness.mjs --strict",
    "git diff --check",
]
INSTALL_REQUIRED_TERMS = [
    "nature-publication-writing",
    "nature-publication-figure",
    "nature-publication-submission-qa",
    "--mode symlink",
    "--mode copy",
    "docs/distribution.md",
]
DISTRIBUTION_REQUIRED_TERMS = [
    "python scripts/validate_docs_productization.py",
    "Release checklist",
    "Update safety",
]
PLANNING_REQUIRED_TERMS = [
    "nature-publication-submission-qa",
    "submission QA",
    "python scripts/validate_submission_qa.py",
    "python scripts/validate_docs_productization.py",
    "python scripts/validate_distribution.py",
]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def read(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing docs file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_terms(path: Path, text: str, terms: list[str], errors: list[str]) -> None:
    for term in terms:
        if term not in text:
            errors.append(f"{path.relative_to(ROOT)} missing required term: {term!r}")


def validate_local_links(path: Path, text: str, errors: list[str]) -> None:
    for match in LINK_RE.finditer(text):
        target = match.group(1).split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)} broken local link -> {match.group(1)}")


def main() -> int:
    errors: list[str] = []
    docs = {
        README: read(README, errors),
        INSTALL_DOC: read(INSTALL_DOC, errors),
        DISTRIBUTION_DOC: read(DISTRIBUTION_DOC, errors),
        PLANNING_DOC: read(PLANNING_DOC, errors),
    }
    require_terms(README, docs[README], README_REQUIRED_TERMS, errors)
    require_terms(INSTALL_DOC, docs[INSTALL_DOC], INSTALL_REQUIRED_TERMS, errors)
    require_terms(DISTRIBUTION_DOC, docs[DISTRIBUTION_DOC], DISTRIBUTION_REQUIRED_TERMS, errors)
    require_terms(PLANNING_DOC, docs[PLANNING_DOC], PLANNING_REQUIRED_TERMS, errors)
    for path, text in docs.items():
        validate_local_links(path, text, errors)

    if errors:
        print("Docs productization validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Docs productization validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
