# Prompt 2 Briefing Audit Report - July 9, 2026 Post-Close

Rounds: `CB-2026-07-09-1W` and `CB-2026-07-09-1M`

Research cutoff: 2026-07-10T01:32:00Z

Visibility: audit-only. This file is not model-facing.

## Audit Status

- `market_fact_report.md` is audit-only and records the direct-browser research method, publisher names, source URLs, publication or observation dates, fixed observed facts, scheduled statuses, source forecasts labeled as forecasts, and source-reported uncertainty.
- `final_briefing_weekly.md` and `final_briefing_monthly.md` are facts-only model-facing drafts. They contain publisher names and dates but no URLs, citations, source ledger, recommendation language, rankings, affected-option mapping, scenario analysis, "why it matters" commentary, or manually selected mechanical return rows.
- Both final briefings contain the required neutrality sentence exactly once near the top and a consistent final neutrality statement.
- Both final briefings state that trailing returns are descriptive context rather than forecasts.
- The weekly draft is limited to facts and scheduled items relevant through the July 16, 2026 close. The monthly draft extends scheduled coverage through the August 7, 2026 close without converting scheduled events into completed facts.
- The source set and final drafts retain counterbalancing observations across equities, rates, labor, inflation, business activity, housing, consumer activity, energy, international markets, and geopolitical conditions. Neither final draft uses row count or ordering to imply expected performance.
- The frozen weekly and monthly `options.yaml` files have the same SHA-256 hash and contain the same 70-option v2.1 universe.
- The generated full-universe price-context artifact exists for both rounds at `market_data/universe_trailing_returns.md` and is byte-identical across the two rounds.
- The generated full-universe artifact covers all 70 options in `options.yaml` order, with 69 passing market rows, one cash row, and zero failed options.
- The generated artifact includes adjusted-close returns, benchmark-relative diagnostics, 30-day volatility, 30-day maximum drawdown, up-day share, 52-week position, and one-year SPY beta and correlation for every non-cash option.
- The generated files identify `yahoo_chart_adjclose` fallback after the confirmed Tiingo hourly rate limit. All non-cash observations have an exact July 9, 2026 as-of price date.
- Full-universe entry prices exist for both rounds at `prices/entry_prices.csv`. Each file has 70 option rows plus the CSV header, every row is dated July 9, 2026, and the weekly and monthly files are byte-identical.
- The prompt builder's approved model-facing inputs are `prompt.md`, round metadata, `briefing.md`, the complete mechanical appendix, and `options.yaml`. The audit-only Prompt 1 and Prompt 2 reports are excluded, and the appendix is appended once.
- After import, round-level `briefing.md` must match `research/final_briefing.md` byte-for-byte for each round.

## Required Corrections Before Hashing

- None.
