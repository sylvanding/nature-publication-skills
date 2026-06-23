# Writing Style Atlas

本文件根据仓库根目录 `references-papers-dai-tsinghua/` 的 8 组论文总结写作风格。不要把这些模式当成万能模板；必须根据用户数据和目标期刊调整。

## 标题

本地论文标题常见结构：

- 方法名 + 核心能力：`CELLECT: contrastive embedding learning for large-scale efficient cell tracking`
- 物理/算法驱动 + 性能目标 + 成像对象：`Physics-driven self-supervised learning for fast high-resolution robust 3D reconstruction of light-field microscopy`
- 技术平台 + 应用场景：`Long-term intravital subcellular imaging with confocal scanning light-field microscopy`
- 生物发现 + 系统范围：`Prominent involvement of acetylcholine dynamics in stable olfactory representation across the Drosophila brain`

写作规则：
- 标题要说清对象和能力，不要只写缩写。
- 方法类标题可以保留方法名，但必须用冒号后短语解释贡献。
- 避免空泛词：`novel`、`powerful`、`robust` 只有在标题中有清晰对象和能力时才可用。

## 摘要 / Summary

常见逻辑：

1. 领域问题或测量瓶颈。
2. 现有方法限制。
3. 本文方法/系统的核心机制。
4. 验证范围：数据规模、样本、显微模式、组织/生物系统、任务。
5. 关键结果：速度、分辨率、准确性、长期稳定性、鲁棒性或生物发现。
6. 意义：打开什么实验能力，而不是简单说“improves performance”。

本地证据：
- 组 1、3、5、6 是方法/算法驱动摘要：先指出成像或追踪瓶颈，再引入学习框架，最后用多数据/多场景验证。
- 组 2 是生物发现摘要：以神经递质动态和稳定嗅觉表征为中心，技术服务于跨脑区证据。
- 组 8 是空间组学/形态学整合摘要：强调连接 morphology 与 transcriptional states。

## Introduction

推荐段落链：

1. Broad need：为什么该测量/分析能力对领域重要。
2. Barrier：现有显微、算法、统计或样本限制。
3. Gap：为什么已有方法不能同时满足速度、分辨率、长期稳定性、鲁棒性或生物解释。
4. Here we：一句话给出本文系统/方法和核心主张。
5. Evidence preview：简要点出验证对象和主要发现。

写作习惯：
- 第一段要让非本领域读者知道问题重要。
- 技术缺口不能只说“仍有挑战”，要具体到 signal/noise、3D reconstruction、long-term imaging、tracking scale、spatial morphology/transcriptomics integration 等。
- `Here we...` 后面应直接承接关键能力，而不是列模块清单。

## Results

Results 小标题应承担结论功能：

- 方法图对应“系统/模型建立”。
- 图像板对应“成像能力或重建质量”。
- 定量图对应“性能、鲁棒性、对照、消融”。
- 生物应用图对应“方法带来的新观察或解释”。

每个 Results 段落建议：

1. 目的：为什么做这个实验/分析。
2. 设计：数据、样本、对照、任务。
3. 观察：直接读图，给出关键方向和必要数字。
4. 解释：说明它支持哪条主张。
5. 边界：说明不能过度外推的部分。

## Discussion

Discussion 不应重复 Results，而应回答：

- 本文改变了哪类实验或分析能力。
- 证据链最强处在哪里。
- 哪些条件、样本、模式或数据类型仍是边界。
- 对后续方法开发或生物问题有什么具体意义。

## Methods

方法类论文尤其需要：

- 数据来源、样本、采集设备、物镜/数值孔径、曝光、通道、时间间隔等。
- 模型架构、训练目标、损失函数、推理设置、硬件、软件版本。
- 图像处理软件和操作：deconvolution、projection、thresholding、filtering、normalization、gamma。
- 统计检验、n 的定义、重复类型、生物/技术重复区分。
