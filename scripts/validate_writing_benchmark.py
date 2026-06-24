#!/usr/bin/env python3
"""Validate Nature writing benchmark prompts and rubric structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRITING_SKILL_DIR = ROOT / "skills" / "nature-publication-writing"
PROMPT_DIR = WRITING_SKILL_DIR / "references" / "benchmarks" / "prompts" / "writing"
RUBRIC = WRITING_SKILL_DIR / "references" / "benchmarks" / "golden" / "writing" / "rubric.md"
WRITING_SKILL = WRITING_SKILL_DIR / "SKILL.md"
README = ROOT / "README.md"
CJK_RE = re.compile(r"[\u3400-\u9fff]")

PROMPTS = [
    "title.md",
    "summary-abstract.md",
    "introduction-paragraph.md",
    "results-paragraph.md",
    "figure-legend.md",
    "methods-paragraph.md",
    "discussion-paragraph.md",
    "supplementary-caption.md",
]
REQUIRED_PROMPT_TERMS = [
    "Task",
    "Source packet",
    "Expected checks",
    "Do not invent",
    "Missing inputs",
]
REQUIRED_RUBRIC_TERMS = [
    "Claim/evidence/boundary",
    "No invented statistics",
    "Section-specific structure",
    "Figure legend completeness",
    "Methods reproducibility",
    "Target language",
    "Applicable categories",
    "N/A",
    "Average applicable score",
    "Score 0",
    "Score 2",
]


def main() -> int:
    errors: list[str] = []
    for prompt in PROMPTS:
        path = PROMPT_DIR / prompt
        if not path.exists():
            errors.append(f"missing writing benchmark prompt: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in REQUIRED_PROMPT_TERMS:
            if term not in text:
                errors.append(f"{path.relative_to(ROOT)} missing required term: {term!r}")
        code_blocks = re.findall(r"```(?:text|markdown)?\n(.*?)```", text, flags=re.DOTALL)
        for block in code_blocks:
            if CJK_RE.search(block):
                errors.append(f"{path.relative_to(ROOT)} contains CJK inside benchmark example block")

    if not RUBRIC.exists():
        errors.append(f"missing writing benchmark rubric: {RUBRIC.relative_to(ROOT)}")
    else:
        text = RUBRIC.read_text(encoding="utf-8")
        for term in REQUIRED_RUBRIC_TERMS:
            if term not in text:
                errors.append(f"{RUBRIC.relative_to(ROOT)} missing required term: {term!r}")

    skill_text = WRITING_SKILL.read_text(encoding="utf-8") if WRITING_SKILL.exists() else ""
    if (
        "Benchmark prompts" not in skill_text
        or "references/benchmarks/prompts/writing/" not in skill_text
        or "Benchmark rubric" not in skill_text
        or "references/benchmarks/golden/writing/rubric.md" not in skill_text
    ):
        errors.append("writing skill must route benchmark work to prompts and rubric")

    readme_text = README.read_text(encoding="utf-8") if README.exists() else ""
    if "python scripts/validate_writing_benchmark.py" not in readme_text:
        errors.append("README validation matrix missing writing benchmark validator")

    if errors:
        print("Writing benchmark validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Writing benchmark validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
