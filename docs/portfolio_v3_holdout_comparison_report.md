# Portfolio V3.0 Holdout Comparison

Decision: **REJECT V3.0**

## Bottom Line

- Valid exact V3/V2.2 pairs: 8/12
- V3 mean alpha versus SPY: 1.94%
- Exact V2.2 control mean alpha: -0.51%
- V3 improvement over V2.2: 2.45%
- V3 cells at or above SPY: 8/8
- Historical V1 same-ID reference alpha: -0.15% across 76 unevenly covered cells (not paired)

## Frozen Gate

- valid pairs: FAIL
- positive treatment alpha: PASS
- paired improvement: PASS
- nonnegative alpha cells: PASS
- positive models: PASS
- positive periods: PASS
- worst period alpha: PASS
- top3 capture not worse: PASS

## By Period

| Set | V3 alpha | V2.2 alpha | Improvement |
| --- | ---: | ---: | ---: |
| V3-H1 | 0.31% | 1.80% | -1.48% |
| V3-H2 | 1.31% | -6.02% | 7.32% |
| V3-H3 | 3.99% | 0.86% | 3.13% |

## By Model

| Model | Pairs | V3 alpha | V2.2 alpha | Improvement |
| --- | ---: | ---: | ---: | ---: |
| openai-gpt-5-6-sol | 0 | n/a | n/a | n/a |
| google-gemini-3-1-pro | 3 | 2.03% | -1.75% | 3.78% |
| xai-grok-4-3 | 2 | 2.91% | 0.85% | 2.06% |
| xai-grok-4-5 | 3 | 1.20% | -0.18% | 1.38% |

## Cell Results

| Set | Model | V3 alpha | V2.2 alpha | Improvement | V3 active choices | Valid |
| --- | --- | ---: | ---: | ---: | --- | --- |
| V3-H1 | openai-gpt-5-6-sol | n/a | n/a | n/a | SPY only | no |
| V3-H1 | google-gemini-3-1-pro | 0.00% | 2.08% | -2.08% | SPY only | yes |
| V3-H1 | xai-grok-4-3 | 0.00% | 1.70% | -1.70% | SPY only | yes |
| V3-H1 | xai-grok-4-5 | 0.94% | 1.62% | -0.68% | COMMUNICATIONS | yes |
| V3-H2 | openai-gpt-5-6-sol | n/a | n/a | n/a | SPY only | no |
| V3-H2 | google-gemini-3-1-pro | 2.61% | -7.32% | 9.93% | SEMICONDUCTORS | yes |
| V3-H2 | xai-grok-4-3 | n/a | n/a | n/a | SPY only | no |
| V3-H2 | xai-grok-4-5 | 0.00% | -4.72% | 4.72% | SPY only | yes |
| V3-H3 | openai-gpt-5-6-sol | n/a | n/a | n/a | SPY only | no |
| V3-H3 | google-gemini-3-1-pro | 3.49% | 0.00% | 3.49% | UTILITIES, OIL, CONSUMER_STAPLES | yes |
| V3-H3 | xai-grok-4-3 | 5.81% | 0.00% | 5.81% | OIL, ENERGY | yes |
| V3-H3 | xai-grok-4-5 | 2.67% | 2.58% | 0.10% | ENERGY, DIVIDEND | yes |

## Interpretation Boundary

V2.2 is an exact same-model, same-date control. V1 is not: it ended before these rounds and the newer models have sparse V1 coverage. The V1 number is context only.

The three holdout windows are one-day-shifted from the V3 development windows and share market history. This is a frozen operational decision test, not independent proof of persistent future alpha.

## Execution

- New provider attempts: 12 (maximum 12)
- New V1/V2.2 calls: 0
- Participant tools, browsing, retrieval, follow-up, and best-of-many selection: disabled
- Official score eligibility: no
