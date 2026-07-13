# Prompt 2 Briefing Audit Report - July 13, 2026 Post-Close

Rounds: `CB-2026-07-13-1W` and `CB-2026-07-13-1M`

Research cutoff: 2026-07-13T20:55:45Z

Visibility: audit-only. This report is not model-facing.

## Artifact Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Prompt 1 market fact report exists | pass | Source-ledger report prepared for the July 13 cutoff. |
| Separate Prompt 3 briefings exist | pass | Weekly and monthly files use their exact scoring windows. |
| Final briefings contain no URLs or markdown citations | pass | URLs and source ledger remain in Prompt 1 only. |
| Final briefings contain no recommendations, rankings, subjective analysis, or affected-option mapping | pass | Each section contains dated factual statements, release statuses, or source-reported uncertainty only. |
| Final briefings contain no selected mechanical return rows | pass | Mechanical context is reserved for the complete generated appendix. |
| Required neutrality sentence appears near the top | pass | Present immediately after the round window in both briefings. |
| Price history is labeled descriptive rather than predictive | pass | Final neutrality statement and prompt package state this explicitly. |
| Broad asset-area balance is maintained | pass | Close and breadth, rates and energy, labor and corporate facts, geopolitical status, scheduled events, and uncertainties are each bounded sections. |
| Forecasts and future events are labeled | pass | FactSet earnings estimate, company guidance, and all future releases are identified as forecasts, guidance, or scheduled events. |
| Source-reported caveats are preserved | pass | Conditional policy remarks, unaudited TSMC data, Tesla's metric caveat, payroll revisions, and geopolitical uncertainty are included. |

## Mechanical Appendix Checks

- The appendix must be generated separately for each round with `capitalbench fetch-universe-performance --as-of-date 2026-07-13`.
- The generated Markdown, CSV, and JSON must cover every included option, including CASH.
- The appendix must be sorted in frozen option order rather than by any return or risk field.
- It must include 7-day, 30-day, 6-month, and 1-year returns plus benchmark-relative return, volatility, drawdown, up-day share, 52-week position, and SPY beta or correlation when available.
- The final assembled model input must contain the `Full-Universe Price, Risk, And Benchmark Context` section exactly once.

## Salience And Fairness Review

- No option IDs, tickers, or allocation instructions are introduced by the final briefings.
- The reports do not convert the July 13 facts into asset forecasts or expected winners.
- Technology facts include both revenue data and same-day share declines; energy facts include both the oil move and unresolved operating conditions. Their presence is factual counterbalance, not scenario analysis.
- The weekly briefing is limited to events through July 20. The monthly briefing extends the schedule through August 13 without adding outcome assumptions.
- The same frozen briefing, option universe, generated appendix, prompt, constraints, cutoff, and provider execution policy will be supplied to every eligible model in each track.

## Readiness Decision

Prompt 1 and both Prompt 3 briefings are ready for import. Final round readiness remains conditional on successful research import, complete mechanical appendix generation, round hashing, prompt assembly verification, universe and price validation, provider-run validation, and official-run acceptance.
