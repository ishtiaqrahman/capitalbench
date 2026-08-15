# Portfolio V3 Robustness Diagnostic

Decision: **development candidate only**

## Candidate Rule

Select at most three model-ranked candidates classified as overreaction with at least a 55% estimated probability of beating SPY; fill unused 35/35/30 slots with SPY.

This analysis made no model calls. It uses the eleven valid responses from the three frozen V3A development weeks. The rule is post-hoc and cannot establish prospective performance.

## Main Result

- Mean alpha versus SPY: 1.04%
- Mean improvement versus paired V2.2: 2.66%
- Strict SPY beats: 4/11
- Nonnegative cells: 9/11
- Active decisions: 6/11 cells and 10/33 available slots
- Positive model families: 3/4
- Positive periods: 2/3
- Weakest period: -0.04%

## Removal Tests

- Lowest mean alpha after removing any one model: 0.39%
- Lowest mean alpha after removing any one period: 0.73%
- Lowest mean alpha after removing any one cell: 0.67%

## Threshold Sensitivity

| Probability hurdle | Alpha vs SPY | SPY beats | Nonnegative | Positive models | Positive periods | Active cells |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 45.0% | 1.28% | 7/11 | 8/11 | 2/4 | 2/3 | 10/11 |
| 50.0% | 1.47% | 7/11 | 8/11 | 3/4 | 3/3 | 10/11 |
| 52.5% | 1.25% | 5/11 | 8/11 | 3/4 | 3/3 | 8/11 |
| 55.0% | 1.04% | 4/11 | 9/11 | 3/4 | 2/3 | 6/11 |
| 57.5% | 0.81% | 4/11 | 11/11 | 3/4 | 2/3 | 4/11 |
| 60.0% | 0.77% | 3/11 | 11/11 | 2/4 | 2/3 | 3/11 |
| 62.5% | 0.33% | 2/11 | 11/11 | 2/4 | 2/3 | 2/11 |
| 65.0% | 0.33% | 2/11 | 11/11 | 2/4 | 2/3 | 2/11 |
| 67.5% | 0.28% | 1/11 | 11/11 | 1/4 | 1/3 | 1/11 |

Every tested nontrivial hurdle from 45% through 67.5% remained above SPY. The 55% hurdle is retained because it was frozen before the Gemini responses; choosing the best-looking cutoff now would be outcome tuning.

## Mechanism Check

| Rule | Alpha vs SPY | SPY beats | Active cells |
| --- | ---: | ---: | ---: |
| probability at least 55 only | -0.12% | 4/11 | 11/11 |
| overreaction any probability | 1.26% | 7/11 | 11/11 |
| overreaction probability at least 55 | 1.04% | 4/11 | 6/11 |
| continuation probability at least 55 | -1.16% | 0/11 | 7/11 |
| overreaction or continuation probability at least 55 | -0.12% | 4/11 | 11/11 |

Confidence alone did not work. Confident continuation lost to SPY, while the overreaction classification produced the positive result. This supports a simple V3 candidate that excludes continuation rather than adding more prompt complexity.

## Interpretation

The positive result is stable to broad probability cutoffs and removal of any one model, period, or cell, but the rule was developed after these historical outcomes were available. It is a V3 development candidate, not prospective validation or a production adoption decision.
