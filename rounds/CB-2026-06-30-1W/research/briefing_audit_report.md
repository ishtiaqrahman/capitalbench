# Prompt 2 Briefing Audit Report

Research cutoff UTC: 2026-07-01T06:30:00Z
Decision package: CB-2026-06-30-1W and CB-2026-06-30-1M

## Scope

This audit checks the Prompt 1 market fact report, the Prompt 3 final briefing, and the generated full-universe price/risk appendix for the June 30, 2026 CapitalBench weekly and monthly portfolio rounds.

## Artifact Checks

| Check | Status | Evidence |
|---|---|---|
| Prompt 1 market fact report exists | pass | `/tmp/capitalbench-20260630/market_fact_report.md` |
| Prompt 3 final briefing exists | pass | `/tmp/capitalbench-20260630/final_briefing.md` |
| Final briefing has no URLs | pass | Manual scan found no `http`, `https`, or `www` strings. |
| Final briefing has no markdown citations or source ledger | pass | Source URLs and ledger are only in Prompt 1. |
| Final briefing has no recommendation, option ranking, scenario analysis, or affected-option mapping | pass | The briefing uses factual dates, values, publishers, and scheduled events only. |
| Final briefing includes required neutrality sentence | pass | The required neutrality paragraph appears near the top and is restated in the data-status section. |
| Final briefing contains no selected mechanical return rows | pass | No manually selected return subset appears in the final briefing. |
| Full-universe appendix exists for weekly round | pass | `rounds/CB-2026-06-30-1W/market_data/universe_trailing_returns.{csv,md,json}` |
| Full-universe appendix exists for monthly round | pass | `rounds/CB-2026-06-30-1M/market_data/universe_trailing_returns.{csv,md,json}` |
| Full-universe appendix covers every included option | pass | CSV row count is 70 for each round, matching the included option count. |
| Full-universe appendix has no failed options | pass | JSON `failed_options` is empty for both rounds. |
| Full-universe appendix is sorted by option order | pass | First included option is `CASH`; final included option is `ETHEREUM_ETF`, matching `options.yaml` order. |
| Full-universe appendix includes price, risk, and benchmark-relative diagnostics | pass | CSV contains return windows, 30-day volatility, drawdown, up-day share, 52-week position, and SPY beta/correlation fields. |
| Price-history discipline statement appears | pass | Appendix text says trailing returns are descriptive context, not forecasts. |

## Source And Timing Checks

- Prompt 1 cites source URLs, publisher names, publication or observation dates, and source-reported uncertainty where available.
- Prompt 3 excludes source URLs and citation mechanics while retaining factual publishers, dates, values, statuses, forecasts or schedules labeled as such, and source-reported data boundaries.
- The June 30 market close is the latest complete U.S. equity close before the July 1 pre-market research window used for these rounds.
- Friday July 3, 2026 is treated as the observed U.S. equity market holiday for the weekly exit-date selection.

## Salience-Bias Check

- The final briefing groups facts by broad topic rather than by allowed option.
- It does not map facts to beneficiaries or expected losers.
- It does not present any manually selected return table.
- It includes counterbalancing context where available: equity index strength, higher Treasury yields, sticky PCE inflation, softer consumer labor-market perceptions, oil-price declines, geopolitical ceasefire uncertainty, and scheduled macro/company events.
- It explicitly tells models that fact order, grouping, row count, option order, and appendix order are not recommendation signals.

## Result

Pass. The prompt package is suitable to import into both June 30, 2026 CapitalBench rounds before final model-input assembly and model calls.
