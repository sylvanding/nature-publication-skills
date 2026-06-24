# Figure Legend Benchmark Prompt

## Task

Draft a Nature-family figure legend for a multi-panel microscopy figure.

## Source packet

```text
Figure title: Confidence-aware reconstruction of live-cell fluorescence movies
Panels: a Raw image; b Prediction; c Ground truth; d Error map; e Line profile; f Metric summary
Scale bar: 5 um
Error: RMSE and SSIM shown as descriptive metrics
Statistics: no inferential test supplied
Image processing: min-max normalization shared across comparable panels
```

## Expected checks

- Starts with a short whole-figure title.
- Describes panels in order with `a,` `b,` style.
- Defines scale bars, color/error meaning, statistics, and missing inferential tests.
- Keeps method detail concise and routes longer processing details to Methods.

## Do not invent

Do not invent n, p-values, acquisition settings, or extra panels.

## Missing inputs

Ask for sample count, replicate definition, and acquisition settings if the final legend needs them.
