# 外部规范与 Skills 来源

初始访问日期：2026-06-23。Agent Skills、Codex plugin、Nature figure guide 和 Springer Nature AI guidance 于 2026-06-24 重新核验；Nature final submission、formatting guide、Nature Portfolio reporting standards、image integrity、Springer Nature accessibility 和 AI guidance 于 2026-06-24 为 submission QA skill 重新核验。所有 URL 应在用于投稿政策、格式政策或易变事实前重新核验。

## Agent Skills 结构来源

- OpenAI Codex Agent Skills: <https://developers.openai.com/codex/skills>
  - 要点：skill 是包含 `SKILL.md` 的目录，可含 `scripts/`、`references/`、`assets/`、`agents/`；Codex 通过 `description` 显式或隐式激活 skill；应把关键词前置并清楚限定边界。Codex 扫描 repo/user/admin/system 位置，repo skills 使用 `.agents/skills`，支持 symlinked skill folders；分发给其他开发者时建议使用 plugins。
- Agent Skills specification: <https://agentskills.io/specification>
  - 要点：`SKILL.md` 必须有 YAML frontmatter 和 Markdown 正文；`name` 和 `description` 必填；长内容应拆到按需加载的资源文件；本仓库采用这一结构。
- OpenAI skill creator guidance: <https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md>
  - 要点：`agents/openai.yaml` 可提供 UI 元数据；可重复、确定性任务应放脚本；详细 reference 不应堆在 `SKILL.md`。
- Anthropic public skills repository: <https://github.com/anthropics/skills>
  - 要点：公开示例采用自包含 skill 文件夹，复杂 skill 使用 `scripts/`、`references/`、`assets/`。
- OpenAI Codex Build plugins: <https://developers.openai.com/codex/plugins/build>
  - 要点：可用 `.codex-plugin/plugin.json` 定义 plugin；plugin 可包含 `skills/`、hooks、apps、MCP 配置和资产；manifest 路径应从 plugin root 开始，并用 `./skills/` 指向 bundled skills。
- GitHub CLI Agent Skills changelog: <https://github.blog/changelog/2026-04-16-manage-agent-skills-with-github-cli/>
  - 要点：`gh skill install` 可从 GitHub 仓库安装 skill，支持目标 agent/scope、`@tag` 和 commit pinning，并提供 `gh skill update` 更新入口。
- GitHub CLI `gh skill install` manual: <https://cli.github.com/manual/gh_skill_install>
  - 要点：`gh skill install <repository> [<skill[@version]>]` 可从 GitHub 仓库或本地目录安装 agent skills，支持 Codex、Claude Code、GitHub Copilot、Gemini CLI 等多个 agent；本机 `gh` 版本可能尚未包含该命令，使用前需重新核验。
- K-Dense-AI/scientific-agent-skills: <https://github.com/K-Dense-AI/scientific-agent-skills>
  - 要点：大型科学 skills 库提供 `npx skills add`、`gh skill install`、version pinning 和 update 命令，说明安装/更新入口应一眼可见。

## Nature / Springer Nature 写作与图表来源

- Nature formatting guide: <https://www.nature.com/nature/for-authors/formatting-guide>
  - 要点：Nature Article 的 summary paragraph 面向跨学科读者；figure legends 应以整图短标题开始，随后简述各 panel 和符号；需要定义 error bars 和 statistics；图应尽量小而简单、避免不必要复杂度和过度配色；标准图宽包括 90 mm 和 180 mm，页面深度约 170 mm。
- Nature Research Figure Guide: <https://research-figure-guide.nature.com/figures/>
  - 要点：官方 figure guide 覆盖 colour、resolution、accessibility、sizing、exporting from software 和 image integrity；其 specifications 页面要求坐标轴和单位、可访问配色、Arial/Helvetica、5-7 pt 正文字体、RGB、可编辑文字/矢量对象，并避免装饰 icon、阴影、pattern、overlapping/coloured text、红绿难辨配色和 flatten scale bar。
- Nature final submission: <https://www.nature.com/nature/for-authors/final-submission>
  - 要点：接收后需上传 text、print figures、Extended Data figures/tables、Supplementary Information 等生产级文件。
- Springer Nature accessibility requirements for figures: <https://www.springernature.com/gp/policies/accessibility-figures-images>
  - 要点：图像需要足够 alt text，作者需人工审核自动生成 alt text；研究图应便于理解，并考虑 main/Extended Data figures 的可访问性。
- Nature Portfolio image integrity and standards: <https://www.nature.com/nature-portfolio/editorial-policies/image-integrity>
  - 要点：Nature Portfolio 强调图像处理透明性和图像完整性；图像美化不能改变数据解释。
- Nature Communications image integrity: <https://www.nature.com/ncomms/editorial-policies/image-integrity>
  - 要点：Methods 应列出图像采集/处理软件，图例或方法中应说明关键处理操作。
- Communications Materials submission guidelines: <https://www.nature.com/commsmat/submit/submission-guidelines>
  - 要点：图像建议 RGB、300 dpi 或更高；统一 Arial 或 Helvetica；避免红绿对比，鼓励绿色/品红等色盲友好组合；避免 rainbow color scale；最佳字体约 8 pt；优先可编辑矢量或分层文件。
- Springer Nature AI guidance for researchers and communities: <https://www.springernature.com/gp/group/ai/ai-guidance-for-our-researchers-and-communities>
  - 要点：作者需对 AI 使用负责并透明声明；一般应避免 generative AI images or figures，除有限例外且需明确标注；非生成式 ML 图像处理、合成或增强也应在 caption 或投稿材料中披露，以供个案审查。
- Nature Communications Article guide: <https://www.nature.com/ncomms/submit/article>
  - 要点：主文从 Introduction 开始，随后 Results、Discussion、Methods；Results 和 Methods 应按主题小标题拆分，Discussion 应简洁。
- Nature Methods content types: <https://www.nature.com/nmeth/content>
  - 要点：Nature Methods 常见研究格式采用无标题 Introduction、Results、Discussion、Online Methods；Results/Methods 用主题小标题，Discussion 不加小标题；display items 通常限制在少量主图/表内。
- Yuan1z0825/nature-skills: <https://github.com/Yuan1z0825/nature-skills>
  - 要点：Nature skills 类仓库强调保留完整 skill 目录，不要只复制 `SKILL.md`；router-style skill 还要保留 `manifest.yaml`、`static/`、`references/`、脚本、资产和共享目录。
- Boom5426/Nature-Paper-Skills: <https://github.com/Boom5426/Nature-Paper-Skills>
  - 要点：Nature writing skill 仓库将 Claude/Codex 安装文档拆到 `docs/`，区分全局安装和项目局部安装。

## 使用纪律

- 官方来源优先于社区博客。
- 如果外部网页与本地论文视觉证据冲突，按“政策合规优先，风格观察其次”处理。
- 易变政策必须在线核验；本文件记录 2026-06-23 的初始调研依据和 2026-06-24 已标注条目的复核依据。
