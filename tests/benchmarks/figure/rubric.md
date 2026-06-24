# Figure Skill V2 Rubric

本 rubric 用于人工或未来自动 benchmark。每个 pressure scenario 输出都按 0-2 分评分；总分低于 10/12 视为需要继续修订 figure skill。

## Source mapping

- Score 0: 直接给图形建议，没有 `claim -> evidence -> figure type -> target journal -> output files`。
- Score 1: 有 claim/evidence，但未连接本地论文组、`references/figure-style-atlas.md` 或官方规则。
- Score 2: 明确连接 claim、真实或 mock-only evidence、panel role、source style 和目标输出。

## Palette and accessibility

- Score 0: 使用 rainbow/jet、red/green-only、colored text legend 或未说明色盲可读性。
- Score 1: 使用较克制颜色，但未说明 official guidance 或替代编码。
- Score 2: 遵守 Nature Research Figure Guide，使用 solid colours、黑色文字、色块/直接标签、可访问 colormap 和非颜色冗余编码。

## Panel composition

- Score 0: 布局由装饰或视觉冲击驱动，panel 间没有逻辑连接。
- Score 1: 有主次关系，但 schematic、image、statistical evidence 的角色不完整。
- Score 2: 正确选择 hero、method、microscopy plate、statistical evidence、spatial map 或 supplementary matrix，并说明 required companion panel。

## Microscopy provenance

- Score 0: 未要求 scale bar、pixel size、crop、LUT、normalization 或 source path。
- Score 1: 要求部分 provenance，但未覆盖处理软件或 image integrity 边界。
- Score 2: 完整要求 source path、crop/slice、pixel size、scale bar、LUT、normalization、processing/software，并拒绝局部增强和选择性美化。

## Statistical reporting

- Score 0: 添加无依据显著性符号、只给均值柱状图，或缺少单位。
- Score 1: 选择了合理图型，但 `n`、error definition、CI 或统计检验说明不完整。
- Score 2: 图型服务于 claim，包含单位、`n` 定义、error/CI 定义、统计检验或模型说明，并保留真实点位或不确定性。

## Export QA

- Score 0: 只输出扁平截图或未说明导出格式。
- Score 1: 输出 PDF/SVG/PNG，但未说明 editable text/vector、RGB、DPI 或 sidecar。
- Score 2: 输出 editable vector/text、RGB、高分辨 preview 和 provenance sidecar；图像 panel 不被整图 rasterize。
