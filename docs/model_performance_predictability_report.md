# Can CapitalBench Inputs Predict The Winning Asset?

Generated at: `2026-07-20T17:01:26-04:00`

Protocol: `docs/model_performance_predictability_protocol.md`

## Bottom Line

The frozen rule identifies `return_1y_reversal` on the weekly track as eligible only for a future shadow test. Its purged-window top-3 alpha was 0.89%, but the moving-block 95% interval was -2.24% to 3.74%; discovery alpha was -2.77%, and full-history alpha was -0.99%. It captured the realized winner in its top three 27.8% of the time and hit the exact winner as its top choice 0.0% of the time. That regime instability and limited winner precision are not enough to replace V1. The next evidence must be a frozen prospective shadow run with no additional paid model calls.

Most winners were mechanically salient under the broad trace rule but unallocated. Because most individual mechanical signals still failed out of sample, this is not proof that models ignored a reliable rule; it shows that the current inputs create many plausible candidates without separating the eventual winner.

The strongest target is not exact winner prediction by itself. With roughly seventy choices and a short, noisy horizon, top-3 capture, return versus S&P 500, and oracle regret are more stable diagnostics. Exact winner hits are still reported, but they are not allowed to drive the recommendation.

## Data Used

The repository contained 72 candidate round folders. 46 resolved V1 rounds passed the frozen eligibility and leakage rules, producing 3,160 round-asset observations and 241 saved model decisions.

| Track | Rounds | First | Last | Discovery | Holdout | Purged WF |
| --- | --- | --- | --- | --- | --- | --- |
| Weekly | 30 | 2026-05-24 | 2026-07-10 | 21 | 9 | 18 |
| Monthly | 16 | 2026-05-10 | 2026-06-17 | 11 | 5 | 0 |

Excluded folders by reason:

| Reason | Count |
| --- | --- |
| missing_frozen_input:universe_trailing_returns.csv | 4 |
| non_v1_round_id | 1 |
| unresolved | 21 |

Leakage audit failures: 0. Timing warnings: 8. Failed rounds, if any, were excluded; after-deadline operational completions that remained before the scoring exit were retained as warnings because their frozen closed-capability inputs did not contain future data.

## Current Performance Gap

| Track | Model decisions | Model return | S&P 500 | Model alpha | Beat rate | Winner alloc | Oracle alpha |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Weekly | 162 | -0.86% | 0.07% | -0.93% | 34.0% | 3.5% | 9.05% |
| Monthly | 79 | -2.02% | -0.10% | -1.91% | 38.0% | 0.1% | 17.26% |

`Oracle alpha` is the return of the best allowed risky option minus S&P 500. It shows that a winning answer existed; it does not show that the answer was knowable before the deadline.

### Model-Level Results

| Track | Model | Rounds | Return | Alpha | Beat S&P | Winner alloc | Top-3 alloc |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Monthly | xai-grok-4-3 | 16 | -0.63% | -0.44% | 56.2% | 0.6% | 6.6% |
| Monthly | anthropic-claude-opus-4-7 | 16 | -1.26% | -1.07% | 50.0% | 0.0% | 5.6% |
| Monthly | anthropic-claude-opus-4-8 | 13 | -1.60% | -1.59% | 38.5% | 0.0% | 3.5% |
| Monthly | google-gemini-3-1-pro | 16 | -2.52% | -2.33% | 18.8% | 0.0% | 3.8% |
| Monthly | anthropic-claude-fable-5 | 2 | -1.11% | -3.14% | 0.0% | 0.0% | 0.0% |
| Monthly | openai-gpt-5-5 | 16 | -4.11% | -3.92% | 31.2% | 0.0% | 6.6% |
| Weekly | xai-grok-4-3 | 30 | -0.47% | -0.54% | 43.3% | 3.3% | 6.5% |
| Weekly | anthropic-claude-opus-4-8 | 28 | -0.65% | -0.64% | 32.1% | 2.5% | 4.5% |
| Weekly | anthropic-claude-opus-4-7 | 30 | -0.63% | -0.70% | 33.3% | 2.5% | 6.3% |
| Weekly | anthropic-claude-fable-5 | 10 | -0.52% | -0.97% | 30.0% | 1.5% | 6.0% |
| Weekly | openai-gpt-5-5 | 30 | -1.10% | -1.17% | 30.0% | 6.2% | 13.8% |
| Weekly | google-gemini-3-1-pro | 30 | -1.21% | -1.28% | 33.3% | 4.3% | 8.3% |
| Weekly | xai-grok-4-5 | 3 | -2.82% | -2.69% | 33.3% | 0.0% | 10.0% |
| Weekly | openai-gpt-5-6-sol | 1 | -5.36% | -3.82% | 0.0% | 0.0% | 10.0% |

Full-history positive-alpha model/track pairs: none. Locked-holdout positive-alpha model/track pairs: none.

## What Happened To The Winner?

| Trace | Weekly rounds | Monthly rounds |
| --- | --- | --- |
| Signal Absent | 4 | 0 |
| Signal Ignored | 17 | 15 |
| Recognized Underweighted | 7 | 1 |
| Recognized | 2 | 0 |

A strong mechanical rank means the realized winner was already in the top 20% on at least one of four frozen trailing-return horizons. With four chances to qualify, `signal ignored` is a broad salience label, not evidence that a profitable signal was ignored. A briefing mention is exact ticker, option ID, or distinctive asset-name matching. These labels do not infer post-deadline news.

### Repeated Winner Episodes

| Track | Winning option | Rounds |
| --- | --- | --- |
| Monthly | BIOTECH | 14 |
| Weekly | OIL | 8 |
| Weekly | BIOTECH | 6 |
| Weekly | SOUTH_KOREA | 6 |
| Weekly | ETHEREUM_ETF | 4 |
| Weekly | HEALTHCARE | 2 |
| Weekly | SOFTWARE | 2 |

These are overlapping observations, not independent victories. BIOTECH accounts for 14 of 16 monthly winners; the largest weekly clusters are OIL (8), SOUTH_KOREA (6), BIOTECH (6), ETHEREUM_ETF (4). The effective number of market episodes is therefore much smaller than 46.

## Frozen Signal Tests

All signals are within-round percentile ranks. Tied scores use fractional selection probabilities, so a sparse mention signal cannot receive an artificial win from option ordering.

### Weekly

Best predefined candidates in the locked holdout:

| Signal | Rounds | Rank IC | Top-3 alpha | Beat S&P | Winner pctile |
| --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 9 | 0.262 | 3.17% | 88.9% | 41.8% |
| return_30d_reversal | 9 | 0.230 | 3.15% | 88.9% | 91.0% |
| return_6m_reversal | 9 | 0.101 | 2.44% | 88.9% | 35.9% |
| return_7d_continuation | 9 | -0.085 | 1.48% | 66.7% | 43.8% |
| return_7d_reversal | 9 | 0.085 | -0.02% | 44.4% | 56.2% |
| briefing_salience | 9 | 0.040 | -0.42% | 55.6% | 52.0% |

The same candidate set on dates with at least eight fully resolved, non-overlapping prior rounds:

| Signal | Rounds | Rank IC | Top-3 alpha | 95% interval | Beat S&P | Leave-best-out |
| --- | --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 18 | 0.178 | 0.89% | -2.24% to 3.74% | 61.1% | 0.44% |
| return_7d_continuation | 18 | -0.064 | 0.49% | -0.92% to 2.10% | 61.1% | 0.10% |
| return_6m_reversal | 18 | 0.093 | 0.38% | -2.45% to 3.27% | 61.1% | -0.06% |
| return_30d_reversal | 18 | 0.035 | 0.24% | -3.22% to 3.30% | 55.6% | -0.21% |
| briefing_salience | 18 | -0.049 | -0.42% | -1.15% to 0.25% | 44.4% | -0.54% |
| short_horizon_momentum | 18 | -0.073 | -0.63% | -1.66% to 0.40% | 33.3% | -0.96% |

### Monthly

Best predefined candidates in the locked holdout:

| Signal | Rounds | Rank IC | Top-3 alpha | Beat S&P | Winner pctile |
| --- | --- | --- | --- | --- | --- |
| return_1y_reversal | 5 | 0.345 | 1.23% | 80.0% | 9.7% |
| return_6m_reversal | 5 | 0.244 | 1.23% | 80.0% | 47.4% |
| return_30d_reversal | 5 | -0.016 | -0.73% | 60.0% | 43.5% |
| return_7d_reversal | 5 | 0.207 | -1.09% | 60.0% | 19.1% |
| briefing_salience | 5 | -0.096 | -1.15% | 40.0% | 46.9% |
| model_consensus_breadth | 5 | -0.179 | -6.03% | 0.0% | 50.7% |

The same candidate set on dates with at least eight fully resolved, non-overlapping prior rounds:

| Signal | Rounds | Rank IC | Top-3 alpha | 95% interval | Beat S&P | Leave-best-out |
| --- | --- | --- | --- | --- | --- | --- |

## Fixed Ridge Diagnostic

The ridge ranker uses only preregistered mechanical, briefing-salience, and model-consensus fields. Its penalty is fixed at 10 and is never tuned on the holdout.

| Track | Evaluation | Rounds | Rank IC | Top-3 alpha | Beat S&P |
| --- | --- | --- | --- | --- | --- |
| Weekly | locked holdout | 9 | -0.022 | -0.06% | 55.6% |
| Weekly | purged walk forward | 18 | 0.056 | -0.36% | 55.6% |
| Monthly | locked holdout | 0 | n/a | n/a | n/a |
| Monthly | purged walk forward | 0 | n/a | n/a | n/a |

## Feature Coverage

| Feature | Weekly | Monthly |
| --- | --- | --- |
| return_7d | 30/30 | 16/16 |
| return_30d | 30/30 | 16/16 |
| return_6m | 30/30 | 16/16 |
| return_1y | 30/30 | 16/16 |
| volatility_30d | 12/30 | 0/16 |
| max_drawdown_30d | 12/30 | 0/16 |
| up_day_share_30d | 12/30 | 0/16 |
| distance_from_52w_high | 12/30 | 0/16 |
| distance_from_52w_low | 12/30 | 0/16 |
| corr_to_sp500_1y | 12/30 | 0/16 |
| beta_to_sp500_1y | 12/30 | 0/16 |

The benchmark-relative return columns are retained in the audit dataset but not duplicated in the ridge model. Subtracting the same S&P 500 return from every option in a round cannot change within-round ranks.

| Raw | Relative | Comparable rounds | Identical rank rounds |
| --- | --- | --- | --- |
| return_7d | return_vs_sp500_7d | 12 | 12 |
| return_30d | return_vs_sp500_30d | 12 | 12 |
| return_6m | return_vs_sp500_6m | 12 | 12 |
| return_1y | return_vs_sp500_1y | 12 | 12 |

## Interpretation

1. In-sample winner stories are not sufficient. The decision table requires the same direction in discovery and holdout, positive top-3 alpha in a purged window, a majority beat rate, and a positive result after removing the best round.
2. Overlapping rounds are not independent. The purged walk-forward fit uses only rounds whose exit precedes the next test entry, and moving-block bootstrap intervals are included in `signal_metrics.csv`.
3. Model consensus is analyzed separately from individual portfolios. If consensus ranks well while portfolios do not, allocation construction is the likely bottleneck. If both fail, adding more portfolio rules will not manufacture information.
4. The active July 13 V2 pilot remains untouched and excluded. Its July 20 frozen acceptance rule is the only rule that can accept or reject V2.

## Recommended Next Step

The frozen rule identifies `return_1y_reversal` on the weekly track as eligible only for a future shadow test. Its purged-window top-3 alpha was 0.89%, but the moving-block 95% interval was -2.24% to 3.74%; discovery alpha was -2.77%, and full-history alpha was -0.99%. It captured the realized winner in its top three 27.8% of the time and hit the exact winner as its top choice 0.0% of the time. That regime instability and limited winner precision are not enough to replace V1. The next evidence must be a frozen prospective shadow run with no additional paid model calls.

Do not optimize the prompt around the historical best asset. If a shadow rule is tested, freeze its formula before the next decision, score it without another model API call, and require several non-overlapping observations before spending money on another paired model run.

## Reproducibility

Run:

```bash
python scripts/analyze_model_predictability.py --rounds-dir rounds --output output/model_performance_predictability --report-copy docs/model_performance_predictability_report.md
```

Machine-readable outputs include eligibility, leakage, asset-level data, winner traces, per-round signal metrics, aggregate signal metrics, model diagnostics, ridge predictions, coefficients, actionability decisions, and `summary.json`.

## Method Notes

The design follows the core warning from White's Reality Check that searching many strategies can produce a best-looking rule by chance, uses chronological prediction rather than random splits, and treats forecast combination as a diagnostic rather than proof. Primary references: [White (2000)](https://onlinelibrary.wiley.com/doi/10.1111/1468-0262.00152), [Harvey, Liu, and Zhu (2016)](https://www.nber.org/papers/w20592), [Gu, Kelly, and Xiu (2020)](https://www.nber.org/papers/w25398), and [Bates and Granger (1969)](https://www.tandfonline.com/doi/abs/10.1057/jors.1969.103).
