# Portfolio V3 Anti-Extrapolation Replay Results

Decision: **rejected**

## Primary Result

- Valid paired cells: 11/12
- V3A mean alpha versus SPY: -0.19%
- Saved V2.2 control mean alpha: -1.62%
- Mean paired V3A improvement: 1.43%
- V3A SPY beats: 5/11
- Improved pairs: 6/11
- V3A selected top-three captures: 3 (control 1)
- Mean candidate rank correlation: 0.005

## By Test Set

| Set | V3A alpha | Paired improvement | Slate winner present | Slate top-three count |
| --- | ---: | ---: | --- | ---: |
| V3-T1 | -2.46% | -1.79% | yes | 1 |
| V3-T2 | 0.54% | 4.62% | yes | 1 |
| V3-T3 | 1.86% | 1.47% | yes | 1 |

## By Model

| Model | Valid sets | V3A alpha | Paired improvement |
| --- | ---: | ---: | ---: |
| openai-gpt-5-6-sol | 2 | 0.67% | 1.33% |
| google-gemini-3-1-pro | 3 | -2.10% | 1.07% |
| xai-grok-4-3 | 3 | 2.73% | 3.60% |
| xai-grok-4-5 | 3 | -1.77% | -0.32% |

## Frozen Gate

- valid pairs: PASS
- positive treatment alpha: FAIL
- paired improvement: PASS
- positive pairs: FAIL
- positive models: FAIL
- positive periods: PASS
- worst period: FAIL
- top3 capture not worse: PASS

## Interpretation

V3A failed at least one frozen gate and is rejected. Do not tune it on these three test sets or adopt it in production.

The three source windows occur after the first eligible dates of the tested models and do not overlap. Packets were frozen before the scorer loaded outcomes. Historical replay can still reject more strongly than it can prove future alpha, so any passing result requires a fresh prospective shadow.

## Cell Results

| Set | Model | V3A alpha | V2.2 alpha | Improvement | V3A top three | Valid |
| --- | --- | ---: | ---: | ---: | --- | --- |
| V3-T1 | openai-gpt-5-6-sol | 1.31% | 1.91% | -0.60% | CYBERSECURITY, BROAD_COMMODITIES, AEROSPACE_DEFENSE | yes |
| V3-T1 | google-gemini-3-1-pro | -5.25% | -2.98% | -2.27% | OIL, BROAD_COMMODITIES, SEMICONDUCTORS | yes |
| V3-T1 | xai-grok-4-3 | -2.53% | 0.00% | -2.53% | OIL, BROAD_COMMODITIES, ETHEREUM_ETF | yes |
| V3-T1 | xai-grok-4-5 | -3.37% | -1.59% | -1.77% | BROAD_COMMODITIES, OIL, BIOTECH | yes |
| V3-T2 | openai-gpt-5-6-sol | 0.04% | -3.23% | 3.26% | EQUAL_WEIGHT_SP500, SEMICONDUCTORS, AEROSPACE_DEFENSE | yes |
| V3-T2 | google-gemini-3-1-pro | -0.92% | -6.63% | 5.71% | AEROSPACE_DEFENSE, MATERIALS, SEMICONDUCTORS | yes |
| V3-T2 | xai-grok-4-3 | 6.09% | -2.62% | 8.72% | SOUTH_KOREA, SEMICONDUCTORS, SOLAR | yes |
| V3-T2 | xai-grok-4-5 | -3.04% | -3.85% | 0.81% | MATERIALS, AEROSPACE_DEFENSE, ENERGY | yes |
| V3-T3 | openai-gpt-5-6-sol | n/a | n/a | n/a | n/a | no |
| V3-T3 | google-gemini-3-1-pro | -0.13% | 0.09% | -0.22% | DIVIDEND, LOW_VOL, UTILITIES | yes |
| V3-T3 | xai-grok-4-3 | 4.63% | 0.00% | 4.63% | OIL, HEALTHCARE, UTILITIES | yes |
| V3-T3 | xai-grok-4-5 | 1.09% | 1.07% | 0.01% | DIVIDEND, HEALTHCARE, REAL_ESTATE | yes |

## Reproducibility

- Experiment: `portfolio-v3-anti-extrapolation-replay-2026-08-13`
- Planned model-period cells: 12 (maximum 12)
- Initial replay provider attempts: 12
- Explicit transport-recovery attempts: 3
- Total replay provider attempts: 15
- Test sets: 3 (maximum 3)
- Participant tools, browsing, retrieval, and follow-up: disabled
- Official score eligibility: no

The initial execution produced three Gemini quota failures. On August 14, the
operator supplied a different Google credential and explicitly asked for those
same frozen cells to be tried again. The three replacement calls used the exact
same packet hashes and model name. They improve coverage but exceed the original
twelve-attempt ceiling, so they cannot turn the already rejected V3A experiment
into a frozen-gate pass. Two tiny credential smoke checks are not replay calls
and are excluded from the fifteen-attempt total.
