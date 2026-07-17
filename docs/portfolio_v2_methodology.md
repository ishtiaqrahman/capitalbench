# CapitalBench Portfolio V2.0 Methodology

Status: production default for new portfolio rounds beginning July 17, 2026.

## Adoption Record

The operator explicitly directed production adoption on July 17, 2026. The
July 13 `portfolio-v2.0-pilot` remains a separate frozen experiment scheduled
to resolve on July 20. Production adoption must not be described as a positive
pilot result, and the pilot's precommitted acceptance test must still be
evaluated and reported without retroactive edits.

## Decision Contract

Every participant receives the same frozen briefing, compact full-universe
decision-context table, neutral allowed-option table, dates, and constraints.
Each participant makes one single-turn, non-agentic model call. Provider tools,
search, retrieval, browsing, follow-up questions, and post-response allocation
optimization are disabled.

The model must first return a candidate ledger of 6-8 unique allowed options.
The ledger must include SP500, span at least four static economic-exposure
clusters, and retain both selected and rejected finalists. Each candidate has:

- low, base, and high return forecasts in percentage points;
- one to three concise evidence statements grounded in the frozen input;
- a continuation case and a reversal case;
- a catalyst that can occur before the exit close, or `none identified`; and
- an observable invalidation condition.

The model then submits a 1-5 holding portfolio in 5% increments totaling 100%.
Every selected non-SP500, non-CASH holding must have a base forecast strictly
greater than the SP500 base forecast. Outside SP500 and CASH, combined holdings
in one static economic-exposure cluster may not exceed 50%. A 100% SP500
portfolio is valid when no active candidate clears the hurdle.

Holding expected returns must equal candidate base forecasts. The weighted
holding forecasts must reproduce the portfolio forecast, and expected alpha
must equal the portfolio forecast minus the SP500 forecast. Confidence remains
the model's stated probability that its portfolio beats SP500; it is recorded
but does not size the portfolio.

## Inputs

Prompt 1, Prompt 2, and Prompt 3 remain the research workflow. Research is
prepared through direct public-source browsing by the operator or Codex, never
through participant model APIs or provider-hosted search. Prompt 1 creates the
audit-only source report, Prompt 2 creates the audit-only bias and completeness
review, and Prompt 3 creates the model-facing factual briefing.

Mechanical market context is generated separately with:

```bash
capitalbench fetch-universe-decision-context \
  --round rounds/<round_id> \
  --as-of-date YYYY-MM-DD
```

Production V2 uses a 12-column option-order table. The weekly and monthly
profiles separate the latest decision window from the prior window and retain
volatility, drawdown, volume, SPY correlation, SPY beta, and 52-week position.
The table contains no ranking, recommendation, or composite buy score.

Economic-exposure clusters are deterministic metadata implemented in
`src/capitalbench/exposures.py`. They are fixed before model calls and are not
created from the current market narrative.

## Scoring And Publication

Only the final frozen portfolio is scored. Official realized return, SP500
alpha, CapitalBench score, regret, and publication rules are unchanged. The
candidate ledger and forecasts are audit and calibration data; they do not
receive a separate official score and cannot be edited after the call.

New production V2 rounds belong to the primary stream. Historical V1 rounds
are not regenerated, and the July 13 pilot remains excluded from primary
aggregates under its frozen experiment contract.

## Success Evaluation

Do not claim V2 improves returns from prompt design alone. Evaluate it
prospectively after resolution using portfolio alpha versus SP500, change from
comparable V1 history, candidate coverage, forecast calibration, and exposure
concentration. Methodology changes require a new version and must never be
backfilled into frozen rounds.
