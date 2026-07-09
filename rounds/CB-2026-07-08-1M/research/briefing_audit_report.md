# Prompt 2 Briefing Audit Report - July 8, 2026 Post-Close

Rounds: `CB-2026-07-08-1W` and `CB-2026-07-08-1M`

Research cutoff: 2026-07-09T00:30:00Z

Visibility: audit-only. This file is not model-facing.

## Audit Status

- `market_fact_report.md` is audit-only and includes source URLs, publisher names, publication or observation dates, and source-reported uncertainty.
- `final_briefing_weekly.md` and `final_briefing_monthly.md` are facts-only model-facing drafts and contain no URLs, source ledger, citations, selected return rows, recommendation language, option rankings, affected-option mapping, or scenario analysis.
- The final briefings include the required neutrality sentence near the top.
- The final briefings state that price history is descriptive context, not a forecast.
- The generated full-universe price-context artifact exists for both new rounds at `market_data/universe_trailing_returns.md`.
- The generated full-universe artifact covers 70 options for each round, has zero failed options, and is sorted in `options.yaml` order.
- The generated artifact includes adjusted-close returns, benchmark-relative diagnostics, 30-day volatility, 30-day max drawdown, up-day share, 52-week position, and one-year SPY beta/correlation where available.
- The generated files mark `yahoo_chart_adjclose` fallback in price source fields and CSV messages for non-cash rows.
- Full-universe entry prices exist for both new rounds at `prices/entry_prices.csv`.
- Entry price files contain 70 option rows plus the CSV header for each round.
- Round-level `briefing.md` should match `research/final_briefing.md` for each round after import.

## Required Corrections Before Hashing

- None.
