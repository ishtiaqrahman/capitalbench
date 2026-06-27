# CapitalBench Briefing Audit Report

Research cutoff: 2026-06-27T02:25:00Z
Scope: audit-only check for the 2026-06-26 weekly and monthly CapitalBench prompt package.

## Prompt 1 Checks

- `market_fact_report.md` is audit-only and includes source URLs, publisher names, publication dates or release dates, observation dates, and source-reported measurement notes where available.
- The report covers current macro releases, rates, index closes, market breadth, scheduled catalysts inside the weekly and monthly scoring windows, energy/geopolitical context, volatility, commodities, crypto, and sector/company facts.
- The report does not rank CapitalBench options, recommend allocations, or map facts to expected winners.
- Mechanical market data is left to the generated `market_data/universe_trailing_returns.md` artifact.

## Prompt 3 Checks

- `final_briefing.md` contains no source URLs, source ledger, citations, recommendation language, rankings, scenario analysis, or affected-option mapping.
- `final_briefing.md` contains the required neutrality sentence near the top.
- `final_briefing.md` includes fixed factual datapoints only, with dates, values, scheduled release times, and measurement notes.
- `final_briefing.md` does not contain a `Selected Mechanical Return Context` section.
- `final_briefing.md` does not include manually selected mechanical return rows.

## Mechanical Appendix Checks To Run After Generation

- Generate the full-universe price, risk, and benchmark-relative context through `capitalbench fetch-universe-performance`.
- Confirm the generated appendix covers every included option in `options.yaml`.
- Confirm the generated appendix is sorted by frozen option order, not by performance.
- Confirm the generated appendix includes return, benchmark-relative, volatility, drawdown, path-quality, 52-week-position, and SPY beta/correlation fields when available.
- Confirm final `model_input.md` contains the `Full-Universe Price, Risk, And Benchmark Context` appendix exactly once.
- Confirm final `model_input.md` does not contain a source ledger or URLs from the audit-only reports.

## Neutrality Statement

Price history in the generated appendix is descriptive context, not a forecast. Inclusion, order, grouping, and row count in the factual briefing and generated appendix are not evidence of expected return.
