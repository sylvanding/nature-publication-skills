#!/usr/bin/env python3
"""Regression tests for the Harness validator."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class HarnessValidatorTests(unittest.TestCase):
    def copy_tracked_repo(self, target: Path) -> None:
        files = subprocess.check_output(
            ["git", "ls-files"],
            cwd=ROOT,
            text=True,
        ).splitlines()
        for rel in files:
            src = ROOT / rel
            dst = target / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_symlink():
                dst.symlink_to(src.readlink())
            elif src.is_file():
                shutil.copy2(src, dst)

    def setup_line(self) -> str:
        return (
            "- If `Harness/SETUP.md` exists, follow it before normal project work; "
            "it is the install/bootstrap contract and may be deleted only after setup is complete.\n"
        )

    def prepare_temp_repo(self) -> tempfile.TemporaryDirectory[str]:
        tmp = tempfile.TemporaryDirectory()
        self.copy_tracked_repo(Path(tmp.name))
        return tmp

    def run_validator(self, tmp_root: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["node", "Harness/scripts/validate-harness.mjs", "--strict"],
            cwd=tmp_root,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_post_bootstrap_without_setup_file_is_valid(self) -> None:
        with self.prepare_temp_repo() as tmp:
            tmp_root = Path(tmp)
            setup = tmp_root / "Harness" / "SETUP.md"
            if setup.exists():
                setup.unlink()

            claude = tmp_root / "CLAUDE.md"
            claude.write_text(
                claude.read_text(encoding="utf-8").replace(self.setup_line(), ""),
                encoding="utf-8",
            )

            result = self.run_validator(tmp_root)
            self.assertEqual(
                result.returncode,
                0,
                msg=f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}",
            )

    def test_post_bootstrap_rejects_stale_setup_reference(self) -> None:
        with self.prepare_temp_repo() as tmp:
            tmp_root = Path(tmp)
            setup = tmp_root / "Harness" / "SETUP.md"
            if setup.exists():
                setup.unlink()

            claude = tmp_root / "CLAUDE.md"
            text = claude.read_text(encoding="utf-8")
            if self.setup_line() not in text:
                text = text.replace(
                    "- Every session: load `Harness/MEMORY.md` first, then `Harness/README.md`.\n",
                    "- Every session: load `Harness/MEMORY.md` first, then `Harness/README.md`.\n"
                    + self.setup_line(),
                )
            claude.write_text(text, encoding="utf-8")

            result = self.run_validator(tmp_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "CLAUDE.md still references retired Harness/SETUP.md bootstrap contract",
                result.stderr,
            )

    def test_bootstrap_setup_file_requires_claude_contract(self) -> None:
        with self.prepare_temp_repo() as tmp:
            tmp_root = Path(tmp)
            setup = tmp_root / "Harness" / "SETUP.md"
            setup.write_text("# Temporary setup\n", encoding="utf-8")

            claude = tmp_root / "CLAUDE.md"
            claude.write_text(
                claude.read_text(encoding="utf-8").replace(self.setup_line(), ""),
                encoding="utf-8",
            )

            result = self.run_validator(tmp_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("CLAUDE.md missing setup bootstrap contract", result.stderr)


if __name__ == "__main__":
    unittest.main()
