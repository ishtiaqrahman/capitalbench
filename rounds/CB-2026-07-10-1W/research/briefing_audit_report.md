# Prompt 2 Briefing Audit Report - July 10, 2026 Post-Close

Rounds: `CB-2026-07-10-1W` and `CB-2026-07-10-1M`

Research cutoff: 2026-07-10T21:49:00Z

Visibility: audit-only. This file is not model-facing.

## Audit Status

- `market_fact_report.md` is audit-only and records the direct-browser research method, publisher names, source URLs, publication or observation dates, fixed observed facts, scheduled statuses, source forecasts labeled as forecasts, and source-reported uncertainty.
- The weekly and monthly `final_briefing.md` files are facts-only model-facing drafts. They contain publisher names and dates but no URLs, citations, source ledger, recommendation language, rankings, affected-option mapping, scenario analysis, "why it matters" commentary, or manually selected mechanical return rows.
- Both final briefings contain the required neutrality sentence exactly once near the top and a consistent final neutrality statement.
- Both final briefings state that trailing returns are descriptive context rather than forecasts.
- The weekly briefing is limited to facts and scheduled items relevant through the July 17, 2026 close. The monthly briefing extends scheduled coverage through the August 10, 2026 close without converting scheduled events into completed facts.
- The source set and final briefings retain counterbalancing observations across broad equities, rates, labor, inflation, technology, corporate results, capital markets, energy, international markets, and geopolitical conditions. Neither briefing uses row count or ordering to imply expected performance.
- The frozen weekly and monthly `options.yaml` files have the same SHA-256 hash and contain the same 70-option v2.1 universe.
- The generated full-universe price-context artifact exists for both rounds at `market_data/universe_trailing_returns.md` and is byte-identical across the two rounds.
- The generated artifact covers all 70 options in `options.yaml` order, with 69 passing market rows, one cash row, and zero failed options.
- Every non-cash row includes adjusted-close returns, benchmark-relative diagnostics, 30-day volatility, 30-day maximum drawdown, up-day share, 52-week position, and one-year SPY beta and correlation.
- The generated files identify Tiingo EOD adjusted closes as the primary source and mark Yahoo Chart adjusted-close fallback rows after provider throttling. All non-cash observations have an exact July 10, 2026 as-of price date.
- Full-universe entry prices exist for both rounds at `prices/entry_prices.csv`. Each file has 70 option rows plus the CSV header, every row is dated July 10, 2026, and the weekly and monthly files are byte-identical.
- The entry-price snapshot was mechanically reused from the exact-date adjusted closes in the complete price-context artifact after the separate price command was throttled. Source labels preserve whether each row came from Tiingo, Yahoo Chart fallback, or cash; no price was manually entered or selected.
- The prompt builder's approved model-facing inputs are `prompt.md`, round metadata, `briefing.md`, the complete mechanical appendix, and `options.yaml`. The audit-only Prompt 1 and Prompt 2 reports are excluded, and the appendix is appended exactly once.
- After import, round-level `briefing.md` must match `research/final_briefing.md` byte-for-byte for each round.

## Required Corrections Before Hashing

- None.
