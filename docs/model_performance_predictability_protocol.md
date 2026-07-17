# Model Performance Predictability Research Protocol

Frozen on: `2026-07-17`

Status: frozen before the aggregate analysis was run. This document defines
the eligible sample, candidate signals, validation design, and decision rules.
Later results belong in `docs/model_performance_predictability_report.md`; they
must not be used to rewrite this protocol.

## Research Question

Using only information that was available in each CapitalBench V1 model input,
can a simple, reproducible rule rank the assets that subsequently performed
best over the one-week or one-month scoring window?

The goal is diagnosis, not retroactive optimization. The study asks whether
the current inputs contain usable predictive information, whether models use
that information, and whether any apparent pattern survives chronological
out-of-sample testing.

## Eligible Sample

A round is eligible only when all of the following are true:

- The round ID is a standard `CB-YYYY-MM-DD-1W` or `CB-YYYY-MM-DD-1M` V1 ID.
- `manifest.yaml` identifies `methodology_version: portfolio-v1.0`, or the
  round predates that field but otherwise uses the historical official V1
  contract.
- Exactly one run is both `run_type: official` and
  `operator_selected_official: true`.
- That run is not mock, retrospective, provider smoke, or stability output.
- The selected run has final `returns.csv`, `leaderboard.csv`, and
  `allocations.csv` artifacts and a non-empty `resolved_at_utc` value.
- The round has the frozen prompt, briefing, options, and mechanical
  full-universe trailing-return CSV that models received.

The active `CB-2026-07-13-V2-1W` pilot is explicitly excluded. Open rounds,
unselected retries, example rounds, and generated interim results are also
excluded. Weekly and monthly samples are analyzed separately.

## Unit Of Analysis

The primary dataset has one row per eligible round and allowed option. CASH is
retained for portfolio accounting and baseline checks but excluded from the
primary risky-asset winner and rank-correlation tests. The S&P 500 option stays
in the investable comparison set.

Every feature must come from an artifact frozen before that round's decision
deadline. Realized returns, exit prices, future round files, and later
briefings are outcomes only and may never be features.

## Predefined Inputs

The analysis uses these mechanically available feature families:

1. Trailing returns: 7-day, 30-day, 6-month, and 1-year return.
2. Benchmark-relative returns over the same horizons when present.
3. Path and risk context when present: 30-day volatility, 30-day maximum
   drawdown, 30-day up-day share, 52-week position, beta, and correlation.
4. Static option context: asset class, option group, category, and risk bucket.
5. Briefing salience: exact ticker, option ID, or sufficiently distinctive
   asset-name mentions in the model-facing briefing.
6. Model evidence: share of models allocating to the option, mean allocation,
   median allocation, maximum allocation, and rationale mention rate.

All numeric signals are compared as within-round percentile ranks so that
different scales and historical schema versions remain comparable. Missing
fields stay missing; they are not backfilled with future data.

## Predefined Candidate Rules

The following low-complexity rules are evaluated before any flexible model:

- Random-choice expectation.
- S&P 500.
- Equal weight across all noncash options.
- Each trailing-return signal individually, in both continuation and reversal
  directions.
- Equal-weight short-horizon momentum (`7d` and `30d`).
- Equal-weight medium-horizon momentum (`6m` and `1y`).
- Model consensus mean allocation.
- Model breadth: fraction of models holding an option.
- Briefing salience.
- A fixed ridge ranker using only the predefined numeric and model-evidence
  features.

No deep model, unrestricted tree search, or outcome-driven text labeling is
allowed. The ridge penalty is fixed at `10.0`; it is not tuned on the holdout.

## Outcomes And Metrics

For every signal or rule, report:

- Mean and median within-round Spearman rank correlation with future return.
- Exact winner hit rate.
- Top-3 and top-5 capture rate.
- Mean percentile rank assigned to the realized winner.
- Return of the top-1 pick and equal-weight top-3 picks.
- Excess return versus the S&P 500.
- Oracle regret relative to the best available option.

For saved model portfolios, also report return, alpha versus S&P 500, winner
allocation, top-3 allocation, and whether the portfolio beat S&P 500.

## Chronological Validation

There is no random cross-validation. Overlapping market windows make random
splits invalid.

1. Discovery summary: earliest 70% of eligible rounds in each track.
2. Locked holdout: latest 30% of eligible rounds in each track.
3. Purged walk-forward: a test round may train only on earlier rounds whose
   exit date is strictly earlier than the test round's entry date.
4. A walk-forward prediction requires at least eight prior eligible rounds in
   the same track. If that threshold is not met, the prediction is omitted.
5. Each round receives equal weight in training regardless of option count.

The holdout boundary and purge are computed from dates, not selected after
viewing performance.

## Uncertainty And Multiple Testing

Round-level moving-block bootstrap intervals are reported where the sample is
large enough. Weekly blocks use seven adjacent decision dates and monthly
blocks use thirty adjacent decision dates, approximated by blocks of five and
ten observed rounds respectively when daily sampling is irregular.

Because many signals are inspected, individual in-sample wins are not treated
as discoveries. A candidate is actionable only if its direction is consistent
in discovery and holdout, improves over S&P 500 in purged walk-forward results,
and is not dependent on one round.

## Winner Trace

Each eligible round receives a deterministic winner trace:

- Winner identity and realized return.
- Winner rank on each available frozen mechanical signal.
- Briefing mention count.
- Number of models holding the winner and total/mean winner allocation.
- Best saved model portfolio and its winner allocation.

The trace labels evidence conservatively:

- `signal_absent`: no briefing mention, no model holding, and weak mechanical
  rank.
- `signal_ignored`: a strong frozen mechanical rank or briefing mention exists,
  but no model holds the winner.
- `recognized_underweighted`: at least one model holds the winner, but mean
  allocation is below 15%.
- `recognized`: mean allocation is at least 15%.

These labels diagnose input use; they do not claim that a post-deadline news
event was predictable.

## Decision Rule

The study may recommend a shadow strategy for a future controlled test only
when all of these conditions hold separately for at least one track:

1. The signal has the same directional rank relationship in discovery and
   holdout.
2. Purged walk-forward top-3 return exceeds S&P 500 on average.
3. Purged walk-forward top-3 beats S&P 500 in more than half of test rounds.
4. The result remains positive after removing its single best round.
5. The rule is simple enough to specify before the next round and does not use
   information absent from current model inputs.

Otherwise the conclusion is that the historical sample does not justify a V1
change. V2 remains governed only by its separate frozen July 20 experiment.
