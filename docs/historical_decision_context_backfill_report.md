# Historical Decision-Context Backfill Results

Decision: **accepted_for_shadow**

## Data Coverage

- Price sources: yahoo_chart_adjusted_close_and_reported_volume (69)
- Failed symbols: none
- Weekly eligible rounds: 30/30
- Monthly eligible rounds: 16/16

## Frozen Signal Results

| Track | Signal | All alpha | Discovery | Holdout | Non-overlap alpha | Non-overlap beat | All leave-best-out | Non-overlap leave-best-out | Gate |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| weekly | horizon trend | -1.04% | -0.91% | -1.33% | -0.79% (8) | 25.00% | -1.28% | -1.76% | fail |
| weekly | risk adjusted trend | -0.58% | -0.58% | -0.57% | -0.68% (8) | 37.50% | -0.68% | -0.94% | fail |
| weekly | quality pullback | 0.36% | 0.48% | 0.09% | 0.28% (8) | 62.50% | 0.20% | -0.31% | pass |
| weekly | volume confirmed trend | -0.76% | -0.60% | -1.15% | -0.86% (8) | 25.00% | -0.94% | -1.58% | fail |
| weekly | low beta active strength | -0.67% | -0.78% | -0.42% | -0.54% (8) | 50.00% | -0.84% | -0.92% | fail |
| monthly | horizon trend | -4.87% | -3.25% | -8.43% | -3.01% (2) | 50.00% | -5.28% | -6.89% | fail |
| monthly | risk adjusted trend | -1.43% | -0.08% | -4.38% | 0.09% (2) | 50.00% | -1.73% | -1.36% | fail |
| monthly | quality pullback | -2.76% | -3.20% | -1.78% | -2.07% (2) | 50.00% | -3.26% | -6.41% | fail |
| monthly | volume confirmed trend | -3.49% | -1.03% | -8.92% | -2.62% (2) | 50.00% | -3.94% | -6.89% | fail |
| monthly | low beta active strength | -4.51% | -4.61% | -4.28% | -0.67% (2) | 50.00% | -4.98% | -3.84% | fail |

## Interpretation

The strongest weekly non-overlapping result was `quality_pullback` at 0.28% alpha across 8 rounds. It cleared every frozen gate.
Its non-overlapping alpha falls to -0.31% when the best week is removed, so the result should be treated as fragile even though it passed the predeclared gate.

This is reused historical data. A pass can authorize only a prospective private shadow; it cannot change Portfolio V2.0 or official scores.
