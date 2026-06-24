#!/usr/bin/env python3
"""Install, update, inspect, or remove local Agent Skills."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


SKILL_NAMES = ("nature-publication-writing", "nature-publication-figure")
AGENTS = ("codex", "claude")
SCOPES = ("user", "repo")
MODES = ("symlink", "copy")
METADATA_FILE = ".nature-publication-skills-install.json"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def git_commit(root: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def run_git_pull(root: Path, dry_run: bool) -> None:
    cmd = ["git", "-C", str(root), "pull", "--ff-only"]
    if dry_run:
        print("DRY-RUN", " ".join(cmd))
        return
    subprocess.check_call(cmd)


def default_target(agent: str, scope: str, repo: Path | None) -> Path:
    if scope == "repo":
        if repo is None:
            raise SystemExit("--repo is required when --scope repo")
        return repo / (".agents/skills" if agent == "codex" else ".claude/skills")
    home = Path.home()
    return home / (".agents/skills" if agent == "codex" else ".claude/skills")


def selected_agents(agent: str) -> list[str]:
    return list(AGENTS) if agent == "all" else [agent]


def selected_skills(skill_args: list[str]) -> list[str]:
    if not skill_args or "all" in skill_args:
        return list(SKILL_NAMES)
    unknown = sorted(set(skill_args) - set(SKILL_NAMES))
    if unknown:
        raise SystemExit(f"Unknown skills: {', '.join(unknown)}")
    return skill_args


def remove_existing(path: Path, force: bool, dry_run: bool) -> None:
    if not path.exists() and not path.is_symlink():
        return
    if not force:
        raise SystemExit(f"{path} already exists; use --force to replace it")
    if dry_run:
        print(f"DRY-RUN remove {path}")
        return
    if path.is_symlink() or path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


def install_one(src: Path, dst: Path, mode: str, force: bool, dry_run: bool) -> None:
    if mode == "symlink" and dst.is_symlink() and dst.resolve() == src.resolve():
        print(f"Already linked: {dst} -> {src}")
        return
    remove_existing(dst, force=force, dry_run=dry_run)
    if dry_run:
        print(f"DRY-RUN install {src} -> {dst} ({mode})")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    if mode == "symlink":
        dst.symlink_to(src, target_is_directory=True)
    else:
        shutil.copytree(src, dst)
    print(f"Installed {dst}")


def write_metadata(target_root: Path, payload: dict, dry_run: bool) -> None:
    metadata = target_root / METADATA_FILE
    if dry_run:
        print(f"DRY-RUN write {metadata}")
        return
    target_root.mkdir(parents=True, exist_ok=True)
    metadata.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def read_metadata(target_root: Path) -> dict | None:
    metadata = target_root / METADATA_FILE
    if not metadata.exists():
        return None
    return json.loads(metadata.read_text(encoding="utf-8"))


def install_command(args: argparse.Namespace, is_update: bool = False) -> int:
    root = repo_root()
    if is_update and args.pull:
        run_git_pull(root, dry_run=args.dry_run)
    skills = selected_skills(args.skill)
    agents = selected_agents(args.agent)
    for agent in agents:
        target_root = default_target(agent, args.scope, args.repo)
        for skill in skills:
            src = root / "skills" / skill
            dst = target_root / skill
            install_one(src, dst, args.mode, force=args.force or is_update, dry_run=args.dry_run)
        write_metadata(
            target_root,
            {
                "source": str(root),
                "commit": git_commit(root),
                "mode": args.mode,
                "agent": agent,
                "scope": args.scope,
                "skills": skills,
                "updated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            },
            dry_run=args.dry_run,
        )
    return 0


def status_command(args: argparse.Namespace) -> int:
    for agent in selected_agents(args.agent):
        target_root = default_target(agent, args.scope, args.repo)
        print(f"{agent}:{args.scope} -> {target_root}")
        metadata = read_metadata(target_root)
        if metadata:
            print(json.dumps(metadata, indent=2))
        for skill in selected_skills(args.skill):
            dst = target_root / skill
            if dst.is_symlink():
                print(f"  {skill}: symlink -> {os.readlink(dst)}")
            elif dst.exists():
                print(f"  {skill}: copy/directory")
            else:
                print(f"  {skill}: missing")
    return 0


def uninstall_command(args: argparse.Namespace) -> int:
    for agent in selected_agents(args.agent):
        target_root = default_target(agent, args.scope, args.repo)
        for skill in selected_skills(args.skill):
            dst = target_root / skill
            remove_existing(dst, force=True, dry_run=args.dry_run)
            if not args.dry_run:
                print(f"Removed {dst}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage Nature Publication Agent Skills installs.")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--agent", choices=("codex", "claude", "all"), default="codex")
        p.add_argument("--scope", choices=SCOPES, default="user")
        p.add_argument("--repo", type=Path, help="Repository root for repo-scoped installs")
        p.add_argument("--skill", nargs="*", default=["all"], help="Skill names or all")
        p.add_argument("--dry-run", action="store_true")

    install = sub.add_parser("install", help="Install skills into an agent discovery path")
    add_common(install)
    install.add_argument("--mode", choices=MODES, default="symlink")
    install.add_argument("--force", action="store_true")

    update = sub.add_parser("update", help="Refresh installed skills from this checkout")
    add_common(update)
    update.add_argument("--mode", choices=MODES, default="symlink")
    update.add_argument("--force", action="store_true")
    update.add_argument("--pull", action="store_true", help="Run git pull --ff-only before updating")

    status = sub.add_parser("status", help="Show install status")
    add_common(status)

    uninstall = sub.add_parser("uninstall", help="Remove installed skills from a target path")
    add_common(uninstall)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "install":
        return install_command(args)
    if args.command == "update":
        return install_command(args, is_update=True)
    if args.command == "status":
        return status_command(args)
    if args.command == "uninstall":
        return uninstall_command(args)
    raise SystemExit(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
