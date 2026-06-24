# Title Benchmark Prompt

## Task

Draft three Nature-family title options for a method manuscript. The best option should state the method object and core capability without hype.

## Source packet

```text
Target journal: Nature Methods
Method name: LumaTrack
Evidence: long-term fluorescence movies, dense cell tracking, segmentation masks, embedding analysis
Boundary: validation is limited to cultured cells and organoid movies
Forbidden claims: clinical diagnosis, universal tracking, unmeasured speedups
```

## Expected checks

- Includes research object and capability.
- Avoids unsupported broad claims and empty words such as novel or powerful.
- Keeps method name interpretable with a descriptive phrase.
- Matches the target language requested by the user.

## Do not invent

Do not invent performance values, sample counts, biological systems, or downstream applications.

## Missing inputs

Ask for exact validation breadth and measured gains if the user wants a single final title.
