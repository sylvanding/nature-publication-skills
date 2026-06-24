# Supplementary Caption Benchmark Prompt

## Task

Draft a Supplementary Figure caption whose first sentence states the validation purpose.

## Source packet

```text
Supplementary figure: Supplementary Fig. 7
Purpose: parameter sensitivity of reconstruction quality
Panels: a Noise-level examples; b RMSE by noise level; c SSIM by noise level; d Failure cases
Scale bar: 5 um in image panels
Statistics: descriptive only; no inferential test supplied
Boundary: synthetic noise experiment only
```

## Expected checks

- First sentence states the validation theme.
- Describes panels in order and defines scale bars.
- Defines descriptive statistics and missing inferential tests.
- States boundary clearly.

## Do not invent

Do not invent additional parameters, p-values, sample counts, or unseen panels.

## Missing inputs

Ask for replicate definition and exact parameter ranges if final caption needs them.
