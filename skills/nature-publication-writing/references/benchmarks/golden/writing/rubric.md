# Writing Benchmark Rubric

Use this rubric for title, summary abstract, introduction, results, figure legend, methods, discussion, and supplementary caption prompts.

## Applicable categories

Always score Claim/evidence/boundary, No invented statistics, Section-specific structure, and Target language. Score Figure legend completeness only for figure legends, supplementary captions, or figure-heavy Results text. Score Methods reproducibility only for Methods or methods-heavy text. Mark non-applicable categories as N/A; do not force a title or introduction to satisfy scale-bar or software-version criteria.

## Claim/evidence/boundary

- Score 0: Makes claims without evidence or omits the boundary.
- Score 1: Includes claim and evidence but boundary is vague.
- Score 2: States claim, source evidence, and boundary explicitly.

## No invented statistics

- Score 0: Invents n, p-values, effect sizes, sample counts, software versions, or performance values.
- Score 1: Avoids some invention but leaves ambiguous quantitative language.
- Score 2: Does not invent; marks Missing inputs where details are absent.

## Section-specific structure

- Score 0: Uses the same generic paragraph shape for every section.
- Score 1: Partly follows the requested section but misses a required move.
- Score 2: Follows the relevant structure from `section-and-legend-playbook.md`.

## Figure legend completeness

- Score 0: Omits panel order, scale bars, color/error meaning, n, or statistics.
- Score 1: Defines some figure elements but misses required reporting fields.
- Score 2: Includes whole-figure title, ordered panels, scale bars, color/error definitions, n/error/statistics status, and concise processing note.

## Methods reproducibility

- Score 0: Describes methods at a promotional or conceptual level only.
- Score 1: Names data/software but omits parameters, versions, or missing details.
- Score 2: Separates performed steps from missing inputs and lists reproducibility details needed for final text.

## Target language

- Score 0: Ignores the user's requested language or mixes languages in manuscript prose.
- Score 1: Mostly follows target language with minor inconsistency.
- Score 2: Fully follows target language; figure-internal labels remain English when figures are involved.

## Passing threshold

An output passes if it has no invented statistics and reaches an Average applicable score of at least 1.7 across non-N/A categories.
