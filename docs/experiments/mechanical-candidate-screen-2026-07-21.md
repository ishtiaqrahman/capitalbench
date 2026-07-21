# Mechanical Candidate Strategy Screen

Frozen on: `2026-07-21`

Status: adaptive private research. This experiment is not an official
CapitalBench round and cannot alter Portfolio V2.0, any frozen round, public
leaderboards, cumulative scores, insights, or market-environment results.

## Objective

Test whether four deterministic, entry-time price strategies can rank a useful
five-asset candidate set before spending money on another model-prompt
experiment. The primary target is equal-weight top-five return relative to the
S&P 500. Exact winner capture is diagnostic only.

The hypotheses were informed by earlier CapitalBench research. These results
are therefore development evidence, not independent confirmation.

## Strategies

All inputs are mechanically frozen before the round entry date. No model API,
search API, model-generated research, or outcome field is used as a feature.

1. `continuation` favors recent leaders, weighting 7-day, 30-day, 6-month, and
   1-year within-round ranks by 40%, 30%, 20%, and 10%.
2. `reversal` favors laggards, weighting reversed 7-day, 30-day, 6-month, and
   1-year ranks by 10%, 20%, 30%, and 40%.
3. `quality_pullback` combines established trend, recent pullback, and orderly
   path behavior. It requires complete volatility, drawdown, up-day-share, and
   52-week-range fields and must not silently impute them.
4. `regime_router` uses continuation when the S&P 500 30-day return and broad
   asset breadth are positive, reversal when both are negative, and an equal
   trend/pullback blend in mixed conditions.

The exact weights and thresholds are frozen in
`experiments/mechanical-candidate-screen-2026-07-21.yaml`.

## Data And Leakage Rules

- Include only resolved, official-score-eligible V1 rounds that pass the
  existing artifact and leakage audit.
- Preserve the complete non-cash option universe, including the S&P 500.
- Rank features within each round; never compare raw return levels across
  unrelated assets or dates.
- Exclude a strategy-round cell when required features do not cover at least
  90% of the active universe.
- Freeze source file hashes before scoring.
- Never edit historical round artifacts.

## Evaluation

Report every strategy by track across:

- all eligible chronological rounds;
- the frozen 70/30 chronological discovery/holdout split;
- mature purged windows with at least eight fully resolved prior rounds; and
- a deterministic maximal non-overlapping sequence chosen chronologically.

Metrics are equal-weight top-five alpha versus S&P 500, S&P 500 beat rate,
top-three alpha, rank correlation, realized winner/top-two capture, oracle
regret, and downside when the strategy underperforms.

## Advancement Gate

A strategy-track pair can earn a future paid model-shadow test only when its
non-overlapping evidence has:

- at least six rounds;
- mean top-five alpha of at least 0.50 percentage points;
- an S&P 500 beat rate of at least 60%; and
- positive mean alpha in both discovery and holdout observations.

Passing this screen would not authorize a production change. It would only
justify one additional single-turn challenger call per model in a prospective
weekly shadow test. Monthly experimentation remains blocked when fewer than
six non-overlapping observations are available.
