# QA and Export

## 导出规则

- 线图、流程图、统计图：优先 PDF/SVG，保留可编辑文字和矢量线条。
- 含显微图的复合图：同时导出 PDF/SVG 和 300 dpi 或更高 PNG/TIFF；不要把原始显微图反复 JPEG 压缩。
- 图像建议 RGB；最终投稿前按目标期刊要求确认色彩空间、DPI 和格式。
- 字体优先 Arial/Helvetica；最终图内字体通常约 6-8 pt，不要小到缩版后不可读。
- 单栏宽约 90 mm，双栏宽约 180 mm，最大深度约 170 mm。

## Main figures vs Extended Data

- main figures 优先提交 editable vector 或 editable layered artwork；统计图、示意图和文字应保持可编辑。
- 含图像的 main figures 需要同时保留源图像、脚本和高分辨率预览，不能只保留扁平化截图。
- Extended Data 也必须遵守 image integrity、字体、RGB、scale bar 和可访问性要求；不同 Nature-family 期刊对 Extended Data 文件大小、DPI 和格式可能不同，投稿前重新核验目标页面。
- Figure legends 和 Extended Data legends 都要引用 panel label，并定义 scale bars、n、error bars 和统计检验。

## 图像完整性

- 保留原始数据和处理脚本。
- 亮度/对比度调整应全图一致；局部增强、局部擦除、选择性模糊都需要避免。
- Methods 中记录图像采集和处理软件；图例或 Methods 中说明 deconvolution、projection、thresholding、filtering、gamma 等关键处理。
- 所有 crop、scale bar、channel mapping、normalization 范围要可复现。
- generative AI 不得用于生成、填补、重绘或美化科学图像证据；Springer Nature guidance 一般不允许 generative AI images or figures，有限例外也必须清楚标注并由作者负责。非生成式 ML 图像处理也需要在 caption 或 Methods 中披露。

## Editable vector checklist

- PDF/SVG 中文字保持 editable text，而不是全部转曲。
- 线条、箭头、scale bar、legend boxes 和统计图形状保持 editable vector。
- 位图只用于真实图像 panel；不要把整张 figure rasterize 后当作最终矢量文件。
- RGB mode、DPI、font、panel label 和 scale bar 在导出后重新打开检查。

## 视觉 QA 清单

提交或回复前逐项检查：

- [ ] 每个 panel 都服务于主结论或补充验证主题。
- [ ] 图内所有文字为英文。
- [ ] panel label 完整且顺序正确。
- [ ] 所有轴都有英文名称和单位。
- [ ] scale bar 可见且单位正确。
- [ ] 分类色不依赖 red/green 唯一对比。
- [ ] 没有 `jet` / rainbow colormap。
- [ ] 显微图没有被过度压暗、过曝或局部处理。
- [ ] 统计图定义了 n、error bars、统计检验和 P value/CI。
- [ ] 导出文件在目标尺寸下可读，打开检查过渲染结果。
- [ ] 代码可复跑，输入数据路径和输出路径明确。

## 审稿级 QA

contact sheet 只用于扫版式。最终交付前还需要高分辨率检查：

- Render the final PDF/SVG at target print size and at 300-600 dpi.
- Inspect panel crops at 100% zoom for scale bars, thin lines, P values and small labels.
- Check font embedding or SVG text editability.
- Confirm RGB mode and target DPI for bitmap exports.
- Run colorblind-safe review when categories or channels rely on color.
- Verify panel label sequence and that every label is referenced in the legend.
- Map every plotted value or image crop back to source data.
- For microscopy, verify pixel size, crop box, LUT/channel mapping, projection and normalization.

## PDF 审计

使用仓库脚本复核参考 PDF 或新生成 PDF：

```bash
python scripts/build_pdf_figure_inventory.py references-papers-dai-tsinghua --output .audit/pdf_figure_inventory.json
python scripts/make_pdf_contact_sheets.py references-papers-dai-tsinghua --output-dir .audit/pdf-page-sheets
python scripts/analyze_pdf_palette.py references-papers-dai-tsinghua --output .audit/pdf_palette_summary.json
python scripts/check_style_coverage.py
```

不要只看文本层或 `pdfimages` 输出；Nature 复合图经常由多个图像对象和矢量标签组成。`make_pdf_contact_sheets.py` 的默认 JPEG/低分辨率输出不是最终质量检查工具。
