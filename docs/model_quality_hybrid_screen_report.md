# Model-Quality Hybrid Screen Results

Decision: **rejected**

- Eligible rounds: 46
- Reconstructed model decisions: 241
- New model calls: 0

## Frozen Transformations

| Track | Transformation | Return change | Resulting alpha | Pair wins | Positive models | Holdout change | Non-overlap change | Leave-best-out | Gate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| weekly | quality sleeve 25 | 0.32% | -0.60% | 62.96% | 100.00% | 0.50% | 0.20% (8) | 0.21% | fail |
| weekly | conviction quality union | 0.16% | -0.77% | 48.77% | 75.00% | 0.59% | 0.17% (8) | 0.04% | fail |
| weekly | within holdings quality tilt | -0.02% | -0.95% | 48.15% | 37.50% | -0.09% | -0.01% (8) | -0.04% | fail |
| monthly | quality sleeve 25 | -0.26% | -2.17% | 29.11% | 16.67% | 0.93% | -0.62% (2) | -0.46% | fail |
| monthly | conviction quality union | -0.87% | -2.79% | 27.85% | 0.00% | 0.55% | -1.21% (2) | -1.12% | fail |
| monthly | within holdings quality tilt | -0.17% | -2.09% | 37.97% | 0.00% | -0.11% | -0.15% (2) | -0.19% | fail |

## Weekly Model Attribution

### Quality Sleeve 25

| Model | Pairs | Return change | Resulting alpha | Pair wins |
| --- | ---: | ---: | ---: | ---: |
| anthropic-claude-fable-5 | 10 | 0.20% | -0.77% | 60.00% |
| anthropic-claude-opus-4-7 | 30 | 0.27% | -0.43% | 66.67% |
| anthropic-claude-opus-4-8 | 28 | 0.29% | -0.35% | 71.43% |
| google-gemini-3-1-pro | 30 | 0.41% | -0.87% | 56.67% |
| openai-gpt-5-5 | 30 | 0.39% | -0.79% | 60.00% |
| openai-gpt-5-6-sol | 1 | 1.25% | -2.57% | 100.00% |
| xai-grok-4-3 | 30 | 0.23% | -0.31% | 60.00% |
| xai-grok-4-5 | 3 | 0.82% | -1.87% | 66.67% |

SPY regime attribution:

| Regime | Pairs | Return change | Resulting alpha |
| --- | ---: | ---: | ---: |
| down | 72 | 0.93% | -1.14% |
| up | 90 | -0.16% | -0.17% |

### Conviction Quality Union

| Model | Pairs | Return change | Resulting alpha | Pair wins |
| --- | ---: | ---: | ---: | ---: |
| anthropic-claude-fable-5 | 10 | -0.07% | -1.03% | 40.00% |
| anthropic-claude-opus-4-7 | 30 | -0.03% | -0.73% | 40.00% |
| anthropic-claude-opus-4-8 | 28 | 0.17% | -0.46% | 64.29% |
| google-gemini-3-1-pro | 30 | 0.48% | -0.80% | 46.67% |
| openai-gpt-5-5 | 30 | 0.02% | -1.15% | 53.33% |
| openai-gpt-5-6-sol | 1 | 1.54% | -2.28% | 100.00% |
| xai-grok-4-3 | 30 | 0.16% | -0.38% | 40.00% |
| xai-grok-4-5 | 3 | 0.33% | -2.36% | 66.67% |

SPY regime attribution:

| Regime | Pairs | Return change | Resulting alpha |
| --- | ---: | ---: | ---: |
| down | 72 | 0.81% | -1.27% |
| up | 90 | -0.36% | -0.37% |

### Within Holdings Quality Tilt

| Model | Pairs | Return change | Resulting alpha | Pair wins |
| --- | ---: | ---: | ---: | ---: |
| anthropic-claude-fable-5 | 10 | -0.12% | -1.08% | 30.00% |
| anthropic-claude-opus-4-7 | 30 | 0.02% | -0.67% | 43.33% |
| anthropic-claude-opus-4-8 | 28 | 0.02% | -0.62% | 50.00% |
| google-gemini-3-1-pro | 30 | -0.05% | -1.33% | 60.00% |
| openai-gpt-5-5 | 30 | -0.06% | -1.23% | 50.00% |
| openai-gpt-5-6-sol | 1 | 0.48% | -3.34% | 100.00% |
| xai-grok-4-3 | 30 | -0.02% | -0.56% | 43.33% |
| xai-grok-4-5 | 3 | -0.17% | -2.86% | 33.33% |

SPY regime attribution:

| Regime | Pairs | Return change | Resulting alpha |
| --- | ---: | ---: | ---: |
| down | 72 | 0.05% | -2.03% |
| up | 90 | -0.08% | -0.09% |

## Interpretation

Historical reuse makes this a reject-only screen. A passing transformation authorizes only the separately frozen bounded private prompt replay; it does not alter production V2 or official scores.
