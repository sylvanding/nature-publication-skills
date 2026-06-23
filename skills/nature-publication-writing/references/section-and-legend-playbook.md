# Section and Legend Playbook

## Title

检查问题：

- 是否同时包含研究对象和能力？
- 是否能被非本方向编辑快速理解？
- 是否避免了未被数据支持的泛化？

可用骨架：

- `<Method name>: <mechanism> for <task>`
- `<Capability> enables <biological or imaging application>`
- `<Mechanism> improves <measurement> across <system>`

## Abstract / Summary

写作骨架：

1. `X is essential for Y, but current methods are limited by Z.`
2. `Here we introduce/develop/report ...`
3. `The method/system combines A with B to ...`
4. `Across <datasets/samples/systems>, it ...`
5. `These results enable ...`

注意：
- Nature summary paragraph 面向跨学科读者，减少缩写、数字和过度技术细节。
- Nature Methods/Nature Biotechnology 方法类摘要要尽早说明 capability gain 和 validation breadth。
- 不要写没有证据的应用前景。

## Introduction

段落功能：

- P1：领域重要性。
- P2：现有技术限制。
- P3：本文核心方法/系统。
- P4：证据路线和结果预告。

常见修复：

- 如果开头太专业，先补一个跨领域问题句。
- 如果缺口太空，替换为具体约束：resolution、phototoxicity、speed、3D reconstruction、tracking scale、long-term stability、noise、uncertainty。
- 如果贡献像模块清单，改写成能力句。

## Results

每个小节以证据链组织：

`question -> experiment/design -> figure evidence -> interpretation -> boundary`

小标题示例：

- `CELLECT tracks cells across dense long-term movies`
- `Physics constraints improve 3D reconstruction under sparse views`
- `Confidence maps identify unreliable super-resolution predictions`
- `MUSE links cell morphology to transcriptional states`

## Figure Legends

推荐结构：

1. 整图短标题。
2. `a,` / `b,` / `c,` 逐 panel 简述。
3. 定义颜色、符号、scale bars、error bars、n、统计检验。
4. 有 Methods 时，不在图例里写冗长方法细节。

图例自审：

- panel 顺序是否和图一致？
- 统计和误差是否定义？
- scale bar 是否说明？
- 图像处理是否在 Methods 或图例中透明说明？
- 图内文字是否全英文？

## Supplementary Information

补充材料应按验证主题组织：

- Additional controls
- Ablation experiments
- Robustness across samples
- Parameter sensitivity
- Extended datasets
- Mathematical derivation
- Implementation details

每个 Supplementary Fig. 的 caption 第一行应说明验证目的，而不是只罗列 panel。
