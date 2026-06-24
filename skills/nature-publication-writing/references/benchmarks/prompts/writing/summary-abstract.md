# Summary Abstract Benchmark Prompt

## Task

Draft a concise Nature-family summary paragraph from the source packet, preserving the chain `problem -> limitation -> method -> evidence -> enabled use`.

## Source packet

```text
Target journal: Nature Biotechnology
System: live-cell super-resolution imaging
Method: confidence-aware neural reconstruction
Evidence: paired low/high resolution microscopy, confidence maps, error maps, long-term imaging tests
Boundary: no animal validation in the provided packet
Forbidden claims: clinical translation, universal microscopy, exact numerical gains
```

## Expected checks

- States the measurement bottleneck before introducing the method.
- Names validation breadth without inventing numbers.
- Includes capability, evidence, and boundary.
- Avoids jargon overload in the opening sentence.

## Do not invent

Do not invent exact accuracy, resolution, speed, sample size, or biological conclusions.

## Missing inputs

Ask for measured values and validation systems if the abstract needs quantitative claims.
