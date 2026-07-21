# Mechanical Candidate Strategy Screen

Generated at: `2026-07-21T07:20:20+00:00`

## Bottom Line

No mechanical candidate strategy passed the frozen development gate. No paid model-shadow experiment is justified by this screen.

## Advancement Decision

| Track | Strategy | Non-overlap N | Non-overlap alpha | Beat S&P | Discovery alpha | Holdout alpha | Gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| weekly | continuation | 6 | -1.27% | 16.67% | -0.84% | -3.42% | Fail |
| weekly | reversal | 6 | -0.60% | 33.33% | -0.62% | -0.46% | Fail |
| weekly | quality_pullback | 2 | -2.54% | 50.00% | -6.10% | 1.02% | Fail |
| weekly | regime_router | 6 | -0.11% | 50.00% | 0.55% | -3.42% | Fail |
| monthly | continuation | 2 | 0.95% | 100.00% | 1.50% | 0.40% | Fail |
| monthly | reversal | 2 | 0.79% | 50.00% | 2.51% | -0.94% | Fail |
| monthly | quality_pullback | 0 | n/a | n/a | n/a | n/a | Fail |
| monthly | regime_router | 2 | -4.73% | 50.00% | 1.50% | -10.96% | Fail |

## Weekly Diagnostics

| Strategy | Rounds | Top-5 alpha | Beat S&P | Top-3 alpha | Winner in top 5 | Mature purged | Purged alpha |
| --- | --- | --- | --- | --- | --- | --- | --- |
| continuation | 30 | -1.35% | 26.67% | -1.80% | 16.67% | 18 | -1.21% |
| reversal | 30 | -0.60% | 43.33% | -1.08% | 13.33% | 18 | 0.31% |
| quality_pullback | 12 | -1.05% | 50.00% | -0.28% | 25.00% | 12 | -1.05% |
| regime_router | 30 | -0.56% | 46.67% | -0.90% | 30.00% | 18 | 0.04% |

## Monthly Diagnostics

| Strategy | Rounds | Top-5 alpha | Beat S&P | Top-3 alpha | Winner in top 5 | Mature purged | Purged alpha |
| --- | --- | --- | --- | --- | --- | --- | --- |
| continuation | 16 | -4.03% | 31.25% | -6.21% | 0.00% | 0 | n/a |
| reversal | 16 | -1.86% | 31.25% | -3.66% | 6.25% | 0 | n/a |
| quality_pullback | 0 | n/a | n/a | n/a | n/a | 0 | n/a |
| regime_router | 16 | -4.92% | 25.00% | -6.58% | 6.25% | 0 | n/a |

## Coverage And Interpretation

- Eligible resolved V1 rounds: 46 (30 weekly, 16 monthly).
- Quality-pullback coverage: 12 weekly rounds and 0 monthly rounds.
- Daily-start rounds overlap. The advancement gate uses the deterministic non-overlapping sequence; all-round figures are correlated diagnostics.
- These hypotheses were selected after earlier CapitalBench analysis and therefore remain development evidence even if a gate passes.
- Exact winner capture is not the adoption target. The decision target is broad, repeatable top-five alpha versus S&P 500.

## Next Action

Do not buy another prompt replay or V2 challenger call from these four hypotheses. Continue unchanged official V2.0 rounds and wait for additional non-overlapping data before defining a materially different feature hypothesis.

## Reproducibility

```bash
python scripts/analyze_mechanical_candidate_strategies.py prepare
python scripts/analyze_mechanical_candidate_strategies.py analyze
```
