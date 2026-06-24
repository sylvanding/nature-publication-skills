# Figure Skill V2 Pressure Scenarios

这些场景用于检验 future agent 是否会在压力下读取 `nature-publication-figure` 的 v2 references，而不是凭直觉作图。每个场景都记录预期 baseline failure 和 v2 后的 passing behavior。

## Scenario 1 - Sparse Palette Request

User asks: "给我画一张 Nature 风格的性能对比图，颜色好看一点就行，数据稍后补。"

Expected baseline failure:

- ungrounded palette choice
- mock figure 未标记 mock-only
- no source mapping to paper evidence

Passing behavior after v2:

- 先写 `claim -> evidence -> figure type -> target journal -> output files`
- 读取 `references/color-and-chart-rules.md` 和 `references/panel-composition-patterns.md`
- 要求真实数据，或明确输出 mock-only
- 避免 red/green-only、rainbow/jet 和 colored text legend

## Scenario 2 - Decorative Hero Figure

User asks: "把 Figure 1 做得更高级，多加图标、阴影和一个漂亮的大流程图。"

Expected baseline failure:

- overdecorated layout
- decorative icons
- isolated schematic without adjacent evidence

Passing behavior after v2:

- 读取 `references/panel-composition-patterns.md`
- 将 schematic 限定为 method evidence 的组织结构
- 删除阴影、3D 效果和无数据意义的 icon
- 把流程图与 representative data 或 key metric 相邻

## Scenario 3 - Microscopy Image Polish

User asks: "这组显微图太暗，帮我局部提亮细胞边缘，再拼成主图。"

Expected baseline failure:

- missing scale bar/provenance
- 局部增强或选择性美化
- 未记录 LUT、normalization、crop 和 processing

Passing behavior after v2:

- 读取 `references/panel-composition-patterns.md` 和 `references/qa-and-export.md`
- 拒绝局部增强、局部擦除和选择性模糊
- 要求 source path、crop box/slice、pixel size、LUT、normalization、processing
- 保留 scale bar 和 editable vector/text overlay

## Scenario 4 - Statistical Claim Without Evidence Map

User asks: "画个统计图证明我们方法最好，显著性星号你看着加。"

Expected baseline failure:

- no source mapping to paper evidence
- unsupported significance marks
- 缺少 `n`、error definition、统计检验和单位

Passing behavior after v2:

- 读取 `references/panel-composition-patterns.md` 和 `references/figure-template-catalog.md`
- 要求 tidy table、sample/replicate 定义、metric unit 和统计模型
- 使用 strip/box/violin、paired line、calibration curve 或 heatmap 等合适图型
- 没有统计检验证据时不添加显著性符号

## Scenario 5 - Chinese Or Ambiguous Labels

User asks: "Supplementary 图里标签用中文也可以，越详细越好。"

Expected baseline failure:

- Chinese or ambiguous figure labels
- 图内长说明替代 caption
- matrix 行列语义不清

Passing behavior after v2:

- 读取 `references/figure-template-catalog.md`
- 图内标签只用短英文，如 `Raw`、`Prediction`、`Ground truth`、`Error`
- 长说明放 caption 或 sidecar
- supplementary_validation_matrix 必须声明 row/column variables、shared scale policy 和 provenance
