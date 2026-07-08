# Prompt 2 Briefing Audit Report - July 7, 2026 Post-Close

Rounds: `CB-2026-07-07-1W` and `CB-2026-07-07-1M`

Research cutoff: 2026-07-08T05:45:00Z

Visibility: audit-only. This file is not model-facing.

## Audit Status

- `market_fact_report.md` is audit-only and includes source URLs, publisher names, publication or observation dates, and source-reported uncertainty.
- `final_briefing_weekly.md` and `final_briefing_monthly.md` are facts-only model-facing drafts and contain no URLs, source ledger, citations, selected return rows, recommendation language, option rankings, affected-option mapping, or scenario analysis.
- The final briefings include the required neutrality sentence near the top.
- The final briefings state that price history is descriptive context, not a forecast.
- The generated full-universe price-context artifact exists for both new rounds at `market_data/universe_trailing_returns.md`.
- The generated full-universe artifact covers 70 options for each round, has zero failed options, and is sorted in `options.yaml` order.
- The generated artifact includes adjusted-close returns, benchmark-relative diagnostics, 30-day volatility, 30-day max drawdown, up-day share, 52-week position, and one-year SPY beta/correlation where available.
- Tiingo returned rate-limit responses during the initial pull. The CapitalBench pipeline's adjusted-close fallback was used for the July 7 entry snapshot and full-universe context. The generated files mark `yahoo_chart_adjclose` fallback in source fields/messages.
- Assembled model input for `CB-2026-07-07-1W` contains `Full-Universe Price, Risk, And Benchmark Context` exactly once, contains no URLs, and does not include audit-only report text.
- Assembled model input for `CB-2026-07-07-1M` contains `Full-Universe Price, Risk, And Benchmark Context` exactly once, contains no URLs, and does not include audit-only report text.
- Round-level `briefing.md` matches `research/final_briefing.md` for both rounds.

## Required Corrections Before Hashing

- None.
