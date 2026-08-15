# Portfolio V3 Anti-Extrapolation Compliance Diagnostic

Decision: **diagnostic only**

## Question

What would have happened if V3A had required a meaningful confidence margin, rejected unaudited continuation, and used SPY whenever too few candidates qualified?

## Counterfactual Rule

An active candidate is eligible only when the model labels the setup as an overreaction and assigns at least a 55% probability of beating SPY. Preserve model rank among eligible candidates and allocate unused 35/35/30 slots to SPY. A prospective version may also admit continuation only when it cites machine-verifiable, candidate-specific non-price evidence.

The rule makes no additional model calls. It uses only each saved response, but it was specified after outcomes were inspected and is therefore not a valid confirmation test.

## Result

- Valid cells: 11/12
- Counterfactual mean alpha versus SPY: 1.04%
- Original V3A mean alpha on the same cells: -0.19%
- Change versus original V3A: 1.23%
- Mean improvement versus saved V2.2 controls: 2.66%
- SPY beats: 4/11
- Nonnegative alpha cells: 9/11
- V2.2 control improvements: 8/11
- Eventual winner captures: 2
- Eventual top-three captures: 2

## By Period

| Set | Valid cells | Alpha vs SPY | Change vs V3A | Improvement vs V2.2 |
| --- | ---: | ---: | ---: | ---: |
| V3-T1 | 4 | -0.04% | 2.42% | 0.63% |
| V3-T2 | 4 | 1.58% | 1.04% | 5.66% |
| V3-T3 | 3 | 1.75% | -0.11% | 1.37% |

## By Model

| Model | Valid sets | Alpha vs SPY | Change vs V3A | Improvement vs V2.2 |
| --- | ---: | ---: | ---: | ---: |
| openai-gpt-5-6-sol | 2 | 0.73% | 0.05% | 1.38% |
| google-gemini-3-1-pro | 3 | -0.04% | 2.06% | 3.13% |
| xai-grok-4-3 | 3 | 2.78% | 0.05% | 3.65% |
| xai-grok-4-5 | 3 | 0.59% | 2.36% | 2.05% |

## Candidate-Level Diagnostic

- Confident overreaction calls beat SPY in 7/10 rows and averaged 3.25% alpha.
- Confident continuation calls beat SPY in 1/12 rows and averaged -3.04% alpha.
- These rows repeat assets and models inside only three periods. They are descriptive and clustered, not independent evidence or a significance test.

## What This Means

The candidate slate was not the main failure: it contained the eventual winner in all three weeks. The strongest remaining lead is to make unsupported continuation claims auditable, require a confidence margin over SPY, and allocate every unfilled active slot to SPY.

This is a design lead, not evidence of a validated strategy. The frozen V3A decision remains rejected, these three periods must not be tuned again, and any successor needs a fresh prospective shadow before production consideration.
