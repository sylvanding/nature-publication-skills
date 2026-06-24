# Results Paragraph Benchmark Prompt

## Task

Draft one Results paragraph using `question -> design -> figure evidence -> interpretation -> boundary`.

## Source packet

```text
Section claim: Confidence maps identify unreliable super-resolution predictions
Figure evidence: Fig. 3a input-output montage, Fig. 3b error map, Fig. 3c calibration curve
Data: live-cell fluorescence movies
Known statistics: no p-values provided
Boundary: confidence is validated against held-out reference images only
```

## Expected checks

- Opens with the question or purpose of the experiment.
- References figure evidence in logical order.
- Separates observed evidence from interpretation.
- States the boundary without weakening the core result.

## Do not invent

Do not invent p-values, sample counts, model architecture, or additional controls.

## Missing inputs

Ask for n, error definitions, and statistical tests if required for final text.
