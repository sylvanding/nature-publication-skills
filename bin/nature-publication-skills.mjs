#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(dirname(fileURLToPath(import.meta.url)));
const script = join(root, "scripts", "install_skills.py");
const args = process.argv.slice(2);

for (const python of ["python3", "python"]) {
  const result = spawnSync(python, [script, ...args], { stdio: "inherit" });
  if (result.error && result.error.code === "ENOENT") {
    continue;
  }
  process.exit(result.status ?? 1);
}

console.error("Python 3 is required to run nature-publication-skills.");
process.exit(1);
