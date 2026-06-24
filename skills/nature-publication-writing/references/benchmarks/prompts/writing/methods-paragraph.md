# Methods Paragraph Benchmark Prompt

## Task

Draft one reproducible Methods paragraph for image processing and model inference.

## Source packet

```text
Data: fluorescence microscopy movies
Processing: crop selection, min-max normalization, line-profile extraction
Model: trained neural reconstruction model
Software: Python, PyTorch, Fiji
Missing: exact versions, GPU model, training epochs, loss function
Boundary: no deconvolution unless supplied by user
```

## Expected checks

- Names data, preprocessing, software, parameters, and missing details.
- Distinguishes performed steps from missing inputs.
- Does not hide critical processing in the figure legend.
- Uses reproducible wording rather than promotional wording.

## Do not invent

Do not invent software versions, hardware, loss functions, thresholds, or deconvolution.

## Missing inputs

Ask for versions, hardware, training objective, thresholds, and random seeds.
