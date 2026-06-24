#!/usr/bin/env python3
"""Validate skill structure, local links, and figure example language."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CJK_RE = re.compile(r"[\u3400-\u9fff]")
REQUIRED_COMMANDS = [
    "python scripts/validate_skills.py",
    "python scripts/validate_figure_v2.py",
    "python scripts/validate_figure_templates.py",
    "python scripts/validate_writing_benchmark.py",
    "python scripts/build_pdf_figure_inventory.py",
    "python scripts/make_pdf_contact_sheets.py",
    "python scripts/analyze_pdf_palette.py",
    "python scripts/check_style_coverage.py",
    "python scripts/install_skills.py install",
    "node bin/nature-publication-skills.mjs status",
    "npm pack --dry-run",
]
REQUIRED_MODULES = ["fitz", "PIL"]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, [f"{path}: missing YAML frontmatter"]
    try:
        end = text.index("\n---", 4)
    except ValueError:
        return {}, [f"{path}: unterminated YAML frontmatter"]
    block = text[4:end].strip().splitlines()
    data: dict[str, str] = {}
    for line in block:
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{path}: invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data, errors


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if ".git" not in path.parts and ".audit" not in path.parts:
            yield path


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(1).split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"{path}: broken local link -> {match.group(1)}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]
    data, fm_errors = parse_frontmatter(skill_md)
    errors.extend(fm_errors)
    name = data.get("name", "")
    desc = data.get("description", "")
    if not name:
        errors.append(f"{skill_md}: missing name")
    elif name != skill_dir.name:
        errors.append(f"{skill_md}: name does not match directory ({name} != {skill_dir.name})")
    elif not NAME_RE.match(name) or "--" in name:
        errors.append(f"{skill_md}: invalid skill name {name!r}")
    if not desc:
        errors.append(f"{skill_md}: missing description")
    elif len(desc) > 1024:
        errors.append(f"{skill_md}: description is longer than 1024 characters")
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if not openai_yaml.exists():
        errors.append(f"{skill_dir}: missing agents/openai.yaml")
    else:
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        for required in ("interface:", "display_name:", "short_description:", "default_prompt:", "policy:", "allow_implicit_invocation:"):
            if required not in yaml_text:
                errors.append(f"{openai_yaml}: missing {required}")
    for md in iter_markdown_files(skill_dir):
        errors.extend(validate_links(md))
    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    readme = root / "README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        for command in REQUIRED_COMMANDS:
            if command not in text:
                errors.append(f"{readme}: missing validation command {command!r}")
    else:
        errors.append("missing README.md")
    req = root / "requirements.txt"
    if not req.exists():
        errors.append("missing requirements.txt")
    docs_install = root / "docs" / "installation.md"
    if not docs_install.exists():
        errors.append("missing docs/installation.md")
    plugin_json = root / ".codex-plugin" / "plugin.json"
    if not plugin_json.exists():
        errors.append("missing .codex-plugin/plugin.json")
    else:
        try:
            plugin = json.loads(plugin_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{plugin_json}: invalid JSON: {exc}")
        else:
            for key in ("name", "version", "description", "skills", "interface"):
                if key not in plugin:
                    errors.append(f"{plugin_json}: missing {key}")
            if plugin.get("skills") != "./skills/":
                errors.append(f"{plugin_json}: skills must be ./skills/")
    package_json = root / "package.json"
    if not package_json.exists():
        errors.append("missing package.json")
    else:
        try:
            package = json.loads(package_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{package_json}: invalid JSON: {exc}")
        else:
            bin_path = package.get("bin", {}).get("nature-publication-skills")
            if bin_path != "bin/nature-publication-skills.mjs":
                errors.append(f"{package_json}: missing nature-publication-skills bin")
            elif not (root / bin_path).exists():
                errors.append(f"{package_json}: bin target missing: {bin_path}")
    installer = root / "scripts" / "install_skills.py"
    if not installer.exists():
        errors.append("missing scripts/install_skills.py")
    repo_skills = root / ".agents" / "skills"
    for skill in ("nature-publication-writing", "nature-publication-figure"):
        link = repo_skills / skill
        if not link.exists():
            errors.append(f"missing repo-scoped skill link: {link}")
    for module in REQUIRED_MODULES:
        if importlib.util.find_spec(module) is None:
            errors.append(f"missing Python module dependency: {module}")
    return errors


def validate_figure_examples(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    for path in iter_markdown_files(skill_dir):
        text = path.read_text(encoding="utf-8")
        in_code = False
        for line_no, line in enumerate(text.splitlines(), start=1):
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code and CJK_RE.search(line):
                errors.append(f"{path}:{line_no}: CJK text found inside a figure code block")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Agent Skills in this repository.")
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    root = Path(args.root)
    skills_root = root / "skills"
    errors: list[str] = []
    if not skills_root.exists():
        errors.append("missing skills/ directory")
    else:
        skill_dirs = [p for p in sorted(skills_root.iterdir()) if p.is_dir() and not p.name.startswith("_")]
        if not skill_dirs:
            errors.append("no skill directories found")
        for skill_dir in skill_dirs:
            errors.extend(validate_skill(skill_dir))
        fig_dir = skills_root / "nature-publication-figure"
        if fig_dir.exists():
            errors.extend(validate_figure_examples(fig_dir))

    for md in iter_markdown_files(root / "references"):
        errors.extend(validate_links(md))
    errors.extend(validate_repository(root))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
