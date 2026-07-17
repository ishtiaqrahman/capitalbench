# Can CapitalBench Inputs Predict The Winning Asset?

Generated at: `2026-07-17T02:15:10-04:00`

Protocol: `docs/model_performance_predictability_protocol.md`

## Bottom Line

The frozen rule identifies `return_1y_reversal` on the weekly track as eligible only for a future shadow test. Its purged-window top-3 alpha was 0.78%, but the moving-block 95% interval was -2.39% to 3.89%; discovery alpha was -3.09%, and full-history alpha was -1.12%. It captured the realized winner in its top three 29.4% of the time and hit the exact winner as its top choice 0.0% of the time. That regime instability and limited winner precision are not enough to replace V1. The next evidence must be a frozen prospective shadow run with no additional paid model calls.

Most winners were mechanically salient under the broad trace rule but unallocated. Because most individual mechanical signals still failed out of sample, this is not proof that models ignored a reliable rule; it shows that the current inputs create many plausible candidates without separating the eventual winner.

The strongest target is not exact winner prediction by itself. With roughly seventy choices and a short, noisy horizon, top-3 capture, return versus S&P 500, and oracle regret are more stable diagnostics. Exact winner hits are still reported, but they are not allowed to drive the recommendation.

## Data Used

The repository contained 68 candidate round folders. 44 resolved V1 rounds passed the frozen eligibility and leakage rules, producing 3,020 round-asset observations and 228 saved model decisions.

| Track | Rounds | First | Last | Discovery | Holdout | Purged WF |
| --- | --- | --- | --- | --- | --- | --- |
| Weekly | 29 | 2026-05-24 | 2026-07-09 | 20 | 9 | 17 |
| Monthly | 15 | 2026-05-10 | 2026-06-16 | 10 | 5 | 0 |

Excluded folders by reason:

| Reason | Count |
| --- | --- |
| non_v1_round_id | 1 |
| unresolved | 23 |

Leakage audit failures: 0. Timing warnings: 8. Failed rounds, if any, were excluded; after-deadline operational completions that remained before the scoring exit were retained as warnings because their frozen closed-capability inputs did not contain future data.

## Current Performance Gap

| Track | Model decisions | Model return | S&P 500 | Model alpha | Beat rate | Winner alloc | Oracle alpha |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Weekly | 154 | -0.60% | 0.15% | -0.75% | 35.7% | 3.7% | 8.82% |
| Monthly | 74 | -1.57% | -0.15% | -1.42% | 40.5% | 0.0% | 17.73% |

`Oracle alpha` is the return of the best allowed risky option minus S&P 500. It shows that a winning answer existed; it does not show that the answer was knowable before the deadline.

### Model-Level Results

| Track | Model | Rounds | Return | Alpha | Beat S&P | Winner alloc | Top-3 alloc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Monthly | xai-grok-4-3 | 15 | -0.23% | 0.01% | 60.0% | 0.0% | 6.3% |
| Monthly | anthropic-claude-opus-4-7 | 15 | -0.90% | -0.66% | 53.3% | 0.0% | 6.0% |
| Monthly | anthropic-claude-opus-4-8 | 12 | -1.25% | -1.18% | 41.7% | 0.0% | 3.8% |
| Monthly | google-gemini-3-1-pro | 15 | -1.88% | -1.64% | 20.0% | 0.0% | 4.0% |
| Monthly | anthropic-claude-fable-5 | 2 | -1.11% | -3.14% | 0.0% | 0.0% | 0.0% |
| Monthly | openai-gpt-5-5 | 15 | -3.60% | -3.36% | 33.3% | 0.0% | 7.0% |
| Weekly | xai-grok-4-3 | 29 | -0.31% | -0.43% | 44.8% | 3.4% | 6.0% |
| Weekly | anthropic-claude-opus-4-8 | 27 | -0.51% | -0.55% | 33.3% | 2.6% | 4.6% |
| Weekly | anthropic-claude-opus-4-7 | 29 | -0.49% | -0.62% | 34.5% | 2.6% | 6.6% |
| Weekly | anthropic-claude-fable-5 | 9 | 0.04% | -0.63% | 33.3% | 1.7% | 6.7% |
| Weekly | openai-gpt-5-5 | 29 | -0.86% | -0.98% | 31.0% | 6.4% | 14.3% |
| Weekly | google-gemini-3-1-pro | 29 | -0.98% | -1.10% | 34.5% | 4.5% | 8.6% |
| Weekly | xai-grok-4-5 | 2 | -1.23% | -1.80% | 50.0% | 0.0% | 15.0% |

Full-history positive-alpha model/track pairs: `monthly:xai-grok-4-3`. Locked-holdout positive-alpha model/track pairs: none.

## What Happened To The Winner?

| Trace | Weekly rounds | Monthly rounds |
| --- | --- | --- |
| Signal Absent | 4 | 0 |
| Signal Ignored | 16 | 15 |
| Recognized Underweighted | 7 | 0 |
| Recognized | 2 | 0 |

A strong mechanical rank means the realized winner was already in the top 20% on at least one of four frozen trailing-return horizons. With four chances to qualify, `signal ignored` is a broad salience label, not evidence that a profitable signal was ignored. A briefing mention is exact ticker, option ID, or distinctive asset-name matching. These labels do not infer post-deadline news.

### Repeated Winner Episodes

| Track | Winning option | Rounds |
| --- | --- | --- |
| Monthly | BIOTECH | 13 |
| Weekly | OIL | 7 |
| Weekly | BIOTECH | 6 |
| Weekly | SOUTH_KOREA | 6 |
| Weekly | ETHEREUM_ETF | 4 |
| Weekly | HEALTHCARE | 2 |
| Weekly | SOFTWARE | 2 |

These are overlapping observations, not independent victories. BIOTECH accounts for 13 of 15 monthly winners; the largest weekly clusters are OIL (7), SOUTH_KOREA (6), BIOTECH (6), ETHEREUM_ETF (4). The effective number of market episodes is therefore much smaller than 44.

## Frozen Signal Tests

All signals are within-round percentile ranks. Tied scores use fractional selection probabilities, so a sparse mention signal cannot receive an artificial win from option ordering.

### Weekly

Best predefined candidates in the locked holdout:

| Signal | Rounds | Rank IC | Top-3 alpha | Beat S&P | Winner pctile |
| --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 9 | 0.233 | 3.26% | 88.9% | 51.5% |
| return_30d_reversal | 9 | 0.217 | 3.01% | 88.9% | 91.0% |
| return_6m_reversal | 9 | 0.131 | 2.66% | 88.9% | 46.6% |
| return_7d_continuation | 9 | -0.095 | 0.64% | 55.6% | 33.3% |
| return_7d_reversal | 9 | 0.095 | -0.25% | 44.4% | 66.7% |
| briefing_salience | 9 | 0.064 | -0.61% | 44.4% | 51.8% |

The same candidate set on dates with at least eight fully resolved, non-overlapping prior rounds:

| Signal | Rounds | Rank IC | Top-3 alpha | 95% interval | Beat S&P | Leave-best-out |
| --- | --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 17 | 0.162 | 0.78% | -2.39% to 3.89% | 58.8% | 0.30% |
| return_6m_reversal | 17 | 0.095 | 0.37% | -2.62% to 3.38% | 58.8% | -0.10% |
| return_7d_continuation | 17 | -0.069 | 0.10% | -1.02% to 1.22% | 58.8% | -0.28% |
| return_30d_reversal | 17 | 0.022 | 0.03% | -3.38% to 3.24% | 52.9% | -0.46% |
| rationale_salience | 17 | -0.000 | -0.42% | -1.47% to 0.46% | 41.2% | -0.71% |
| briefing_salience | 17 | -0.041 | -0.46% | -1.16% to 0.20% | 41.2% | -0.59% |

### Monthly

Best predefined candidates in the locked holdout:

| Signal | Rounds | Rank IC | Top-3 alpha | Beat S&P | Winner pctile |
| --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 5 | 0.274 | 0.91% | 80.0% | 10.0% |
| return_6m_reversal | 5 | 0.191 | 0.77% | 80.0% | 50.6% |
| briefing_salience | 5 | -0.060 | -1.23% | 40.0% | 52.4% |
| return_30d_reversal | 5 | -0.131 | -2.11% | 40.0% | 56.8% |
| return_7d_reversal | 5 | 0.067 | -3.03% | 40.0% | 19.1% |
| return_7d_continuation | 5 | -0.067 | -3.52% | 40.0% | 80.9% |

The same candidate set on dates with at least eight fully resolved, non-overlapping prior rounds:

| Signal | Rounds | Rank IC | Top-3 alpha | 95% interval | Beat S&P | Leave-best-out |
| --- | --- | --- | --- | --- | --- | --- |

## Fixed Ridge Diagnostic

The ridge ranker uses only preregistered mechanical, briefing-salience, and model-consensus fields. Its penalty is fixed at 10 and is never tuned on the holdout.

| Track | Evaluation | Rounds | Rank IC | Top-3 alpha | Beat S&P |
| --- | --- | --- | --- | --- | --- |
| Weekly | locked holdout | 9 | -0.020 | -0.47% | 44.4% |
| Weekly | purged walk forward | 17 | 0.059 | -0.48% | 52.9% |
| Monthly | locked holdout | 0 | n/a | n/a | n/a |
| Monthly | purged walk forward | 0 | n/a | n/a | n/a |

## Feature Coverage

| Feature | Weekly | Monthly |
| --- | --- | --- |
| return_7d | 29/29 | 15/15 |
| return_30d | 29/29 | 15/15 |
| return_6m | 29/29 | 15/15 |
| return_1y | 29/29 | 15/15 |
| volatility_30d | 11/29 | 0/15 |
| max_drawdown_30d | 11/29 | 0/15 |
| up_day_share_30d | 11/29 | 0/15 |
| distance_from_52w_high | 11/29 | 0/15 |
| distance_from_52w_low | 11/29 | 0/15 |
| corr_to_sp500_1y | 11/29 | 0/15 |
| beta_to_sp500_1y | 11/29 | 0/15 |

The benchmark-relative return columns are retained in the audit dataset but not duplicated in the ridge model. Subtracting the same S&P 500 return from every option in a round cannot change within-round ranks.

| Raw | Relative | Comparable rounds | Identical rank rounds |
| --- | --- | --- | --- |
| return_7d | return_vs_sp500_7d | 11 | 11 |
| return_30d | return_vs_sp500_30d | 11 | 11 |
| return_6m | return_vs_sp500_6m | 11 | 11 |
| return_1y | return_vs_sp500_1y | 11 | 11 |

## Interpretation

1. In-sample winner stories are not sufficient. The decision table requires the same direction in discovery and holdout, positive top-3 alpha in a purged window, a majority beat rate, and a positive result after removing the best round.
2. Overlapping rounds are not independent. The purged walk-forward fit uses only rounds whose exit precedes the next test entry, and moving-block bootstrap intervals are included in `signal_metrics.csv`.
3. Model consensus is analyzed separately from individual portfolios. If consensus ranks well while portfolios do not, allocation construction is the likely bottleneck. If both fail, adding more portfolio rules will not manufacture information.
4. The active July 13 V2 pilot remains untouched and excluded. Its July 20 frozen acceptance rule is the only rule that can accept or reject V2.

## Recommended Next Step

The frozen rule identifies `return_1y_reversal` on the weekly track as eligible only for a future shadow test. Its purged-window top-3 alpha was 0.78%, but the moving-block 95% interval was -2.39% to 3.89%; discovery alpha was -3.09%, and full-history alpha was -1.12%. It captured the realized winner in its top three 29.4% of the time and hit the exact winner as its top choice 0.0% of the time. That regime instability and limited winner precision are not enough to replace V1. The next evidence must be a frozen prospective shadow run with no additional paid model calls.

Do not optimize the prompt around the historical best asset. If a shadow rule is tested, freeze its formula before the next decision, score it without another model API call, and require several non-overlapping observations before spending money on another paired model run.

## Reproducibility

Run:

```bash
python scripts/analyze_model_predictability.py --rounds-dir rounds --output output/model_performance_predictability --report-copy docs/model_performance_predictability_report.md
```

Machine-readable outputs include eligibility, leakage, asset-level data, winner traces, per-round signal metrics, aggregate signal metrics, model diagnostics, ridge predictions, coefficients, actionability decisions, and `summary.json`.

## Method Notes

The design follows the core warning from White's Reality Check that searching many strategies can produce a best-looking rule by chance, uses chronological prediction rather than random splits, and treats forecast combination as a diagnostic rather than proof. Primary references: [White (2000)](https://onlinelibrary.wiley.com/doi/10.1111/1468-0262.00152), [Harvey, Liu, and Zhu (2016)](https://www.nber.org/papers/w20592), [Gu, Kelly, and Xiu (2020)](https://www.nber.org/papers/w25398), and [Bates and Granger (1969)](https://www.tandfonline.com/doi/abs/10.1057/jors.1969.103).
