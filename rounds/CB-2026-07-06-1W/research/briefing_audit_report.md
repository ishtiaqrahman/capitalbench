# Prompt 2 Briefing Audit Report

Round candidates: CB-2026-07-06-1W and CB-2026-07-06-1M

Audit cutoff UTC: 2026-07-07T01:56:00Z

Purpose: audit-only check of Prompt 1 and Prompt 3 artifacts plus the generated full-universe price/risk appendices. This report is not model-facing.

## Artifact Presence

- Prompt 1 market fact report exists: pass.
- Prompt 3 weekly final briefing exists: pass.
- Prompt 3 monthly final briefing exists: pass.
- Weekly generated price/risk appendix exists: pass.
- Monthly generated price/risk appendix exists: pass.

## Prompt 1 Checks

- Source URLs, publisher names, publication or release dates, observation dates, and source-reported uncertainty notes are present in the audit-only market fact report: pass.
- Prompt 1 separates mechanical market data from public-source factual research and refers to the full generated artifact rather than a selected return table: pass.
- Prompt 1 does not rank options, recommend allocations, or map facts to expected winners: pass.

## Prompt 3 Checks

- Weekly final briefing contains no URLs: pass.
- Monthly final briefing contains no URLs: pass.
- Weekly final briefing contains no markdown citations or source ledger: pass.
- Monthly final briefing contains no markdown citations or source ledger: pass.
- Weekly and monthly final briefings contain the required neutrality statement near the top: pass.
- Weekly and monthly final briefings do not include recommendation language, option rankings, affected-option mapping, or subjective thesis text: pass.
- Weekly and monthly final briefings do not include a `Selected Mechanical Return Context` section: pass.
- Weekly and monthly final briefings do not include manually selected mechanical return rows: pass.
- Weekly and monthly final briefings state that price history is descriptive context and not a forecast: pass.
- Weekly briefing is horizon-specific and excludes scheduled catalysts after the July 13, 2026 exit close: pass.
- Monthly briefing includes scheduled macro, policy, and company-calendar items inside the July 6 to August 6 scoring window: pass.

## Price/Risk Appendix Checks

- Appendix title is exactly `Full-Universe Price, Risk, And Benchmark Context`: pass for both rounds after prompt assembly.
- Appendix row count equals the included universe size of 70 options: pass for both rounds.
- CASH appears first and ETHEREUM_ETF appears last, matching option order: pass for both rounds.
- Failed options count is zero: pass for both rounds.
- Appendix columns include return windows, benchmark-relative diagnostics, volatility, drawdown, up-day share, 52-week positioning, and SPY beta/correlation where available: pass for both rounds.
- Appendix text states the table is sorted by option order, not by performance: pass for both rounds.
- Appendix text states trailing returns are descriptive context, not forecasts: pass for both rounds.
- Mechanical pricing note: a single-symbol Tiingo probe during the operator run returned HTTP 429. The existing CapitalBench adjusted-close fallback path was used through the performance pipeline, producing complete pass rows for all non-cash options and no failed options.

## Model Input Checks

- Final model input appendix count for CB-2026-07-06-1W: exactly 1 occurrence of `Full-Universe Price, Risk, And Benchmark Context`; pass.
- Final model input appendix count for CB-2026-07-06-1M: exactly 1 occurrence of `Full-Universe Price, Risk, And Benchmark Context`; pass.
- Final model input legacy appendix title count for both rounds: zero occurrences of `Full-Universe Trailing Returns`; pass.
- Final model input includes research cutoff UTC `2026-07-07T01:56:00Z` for both rounds: pass.
- Final model input URL count: zero for both rounds; pass.
- Final model input does not include the old S&P 500 allocation instruction; pass.
