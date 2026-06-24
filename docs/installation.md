# Installation And Update

本仓库现在按“一个源码仓库，多目标安装”的方式组织。`skills/` 是唯一源码，安装脚本把完整 skill 目录同步或软链接到各 agent 的发现路径。发布、打包和 release 检查见 `docs/distribution.md`。

## 推荐方式

### Codex 用户级安装

```bash
python scripts/install_skills.py install --agent codex --scope user --mode symlink
```

更新：

```bash
git pull --ff-only
python scripts/install_skills.py update --agent codex --scope user --mode symlink
```

`symlink` 模式适合个人开发：源码仓库更新后，已安装 skill 自动看到新内容。

### Codex 项目级安装

```bash
python scripts/install_skills.py install --agent codex --scope repo --repo /path/to/target-repo --mode symlink
```

这会写入 `/path/to/target-repo/.agents/skills/`。Codex 官方文档说明 repo skills 会从当前目录向上扫描 `.agents/skills`，且支持 symlinked skill folders。

### Claude Code 安装

```bash
python scripts/install_skills.py install --agent claude --scope user --mode symlink
python scripts/install_skills.py install --agent claude --scope repo --repo /path/to/target-repo --mode symlink
```

Claude Code 常用 `~/.claude/skills/` 或项目 `.claude/skills/`。

## npx / GitHub 安装入口

本仓库包含 `package.json` 和 `bin/nature-publication-skills.mjs`。从 GitHub 使用时可运行：

```bash
npx github:sylvanding/nature-publication-skills install --agent codex --scope user --mode copy --force
npx github:sylvanding/nature-publication-skills update --agent codex --scope user --mode copy --force
```

如果通过 `npx` 安装为临时包，`copy` 模式比 `symlink` 更稳；如果是稳定 clone，推荐 `symlink`。

## GitHub CLI `gh skill`

GitHub CLI v2.90.0+ 支持 `gh skill install` / `gh skill update`。该命令仍是 public preview，行为可能变化；安装前应先 inspect skill 内容。当前本机 `gh` 版本较旧，本仓库无法本地验证该命令，但仓库结构遵循 open Agent Skills 标准：每个 skill 是一个带 `SKILL.md` 的完整目录。

```bash
gh skill install sylvanding/nature-publication-skills
gh skill install sylvanding/nature-publication-skills nature-publication-figure --agent codex
gh skill update --all
```

## 状态和卸载

```bash
python scripts/install_skills.py status --agent codex --scope user
python scripts/install_skills.py uninstall --agent codex --scope user
```

安装目标目录会写入 `.nature-publication-skills-install.json`，记录 source、commit、mode、agent、scope 和 installed skills。

## Codex Plugin

仓库根目录包含 `.codex-plugin/plugin.json`，用于 Codex plugin 分发。Codex 官方文档建议：本地 authoring 和 repo-scoped workflow 可直接用 skill folders；需要向其他开发者分发多个 skills 或附带 app/MCP 能力时，用 plugin。

## 设计来源

- OpenAI Codex skills 文档：skill 是含 `SKILL.md` 的目录，可含 `scripts/`、`references/`、`assets/`、`agents/openai.yaml`；Codex 扫描 `.agents/skills`、`~/.agents/skills`，支持 symlinked skill folders。
- OpenAI plugins 示例：plugin 使用 `.codex-plugin/plugin.json`，可通过 `"skills": "./skills/"` 绑定技能目录。
- Yuan1z0825/nature-skills：强调不要只复制 `SKILL.md`，要保留完整 skill 目录、`references/`、`static/`、`manifest.yaml` 和共享目录。
- K-Dense-AI/scientific-agent-skills：提供 `npx`、`gh skill install`、version pinning 和 update flows。
- GitHub changelog：`gh skill install` 会安装到目标 agent 的正确目录，并支持 `@tag` / commit pinning。
