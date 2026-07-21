# CapitalBench Portfolio V2.2 Methodology

Status: production default for new portfolio rounds beginning July 21, 2026.

## Adoption Record

The operator explicitly directed V2.2 adoption after the Q1 historical
development replay improved 8 of 9 valid OpenAI and xAI model-period pairs by
1.59 percentage points on average. This is an operator adoption, not a claim
that Q1 passed confirmation. Gemini was unavailable during development, the
replay used historical periods, and Q1 has not yet passed an unchanged
four-model confirmation.

V2.2 applies only to newly initialized rounds. Existing V1, V2.0, pilot, and
resolved round artifacts remain frozen and retain their original methodology
versions.

## Change From V2.0

V2.2 preserves the V2.0 single-turn portfolio task, candidate ledger,
forecasts, SPY hurdle, exposure cap, response schema, scoring, and publication
rules. It adds one complete option-level evidence table to the frozen model
input.

For every active option with sufficient cutoff-safe price history, the table
contains entry-date percentile ranks for:

- prior active return relative to SPY;
- a recent active-return pullback;
- lower realized volatility; and
- shallower drawdown.

The quality evidence score is fixed before model calls:

```text
45% prior active-return rank
+ 30% recent active-return pullback rank
+ 15% low-volatility rank
+ 10% shallow-drawdown rank
```

Weekly rounds use the prior 16 sessions excluding the latest 5 sessions, the
latest 5-session active return, and 21-session risk measures. Monthly rounds
use the prior 105 sessions excluding the latest 21 sessions, the latest
21-session active return, and 63-session risk measures.

All ranks and the composite stop at the entry-date close. No future return,
resolved-round outcome, model response, or discretionary adjustment enters
the table. Rows remain in frozen option order.

## Model Instruction

The evidence table is complete context, not a recommendation or reduced
universe. A higher score means stronger prior relative trend, a deeper recent
relative pullback, lower volatility, and shallower drawdown under the fixed
formula. Models may use or reject the evidence as they judge appropriate.

V2.2 does not require a minimum number of high-scoring options in the
candidate ledger or final portfolio. That forced-selection treatment was Q2
and failed unchanged historical confirmation.

## Input Integrity

Generate the decision context and Q1 table together with:

```bash
capitalbench fetch-universe-decision-context \
  --round rounds/<round_id> \
  --as-of-date YYYY-MM-DD
```

The generated files are:

- `market_data/universe_decision_context.csv`
- `market_data/universe_decision_context.json`
- `market_data/universe_decision_context.md`
- `market_data/universe_quality_evidence.json`
- `market_data/universe_quality_evidence.md`
- `market_data/decision_context_source_history.json`

Prompt assembly fails if the quality evidence files are absent or cover less
than 90% of active options. All generated artifacts are included in the
round's SHA-256 hash manifest before model calls.

## Prospective Evaluation

V2.2 is unconfirmed until fresh rounds resolve. Evaluate it using realized
portfolio return and alpha versus SPY, model-level breadth, candidate coverage,
and forecast calibration. Do not describe the 8-of-9 historical development
result as proof of prospective skill or retrospectively apply V2.2 to older
rounds.
