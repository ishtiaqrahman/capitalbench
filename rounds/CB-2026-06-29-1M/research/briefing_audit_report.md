# CapitalBench Briefing Audit Report

Research cutoff: 2026-06-29T23:55:00Z
Scope: audit-only check for the 2026-06-29 weekly and monthly CapitalBench prompt package.

## Prompt 1 Checks

- `market_fact_report.md` is audit-only and includes source URLs, publisher names, publication dates or release dates, observation dates, and source-reported measurement notes where available.
- The report covers same-day U.S. index closes, macro releases, rates, policy calendar, energy/geopolitics, volatility, commodities, crypto, business activity, scheduled catalysts, and company/sector facts.
- The report does not rank CapitalBench options, recommend allocations, or map facts to expected winners.
- Mechanical price context is left to the generated `market_data/universe_trailing_returns.md` artifact.

## Prompt 2 Checks

- The model-facing briefing excludes source URLs, source ledgers, citations, recommendation language, rankings, scenario framing, and affected-option mapping.
- The model-facing briefing uses fixed dated facts and scheduled release times rather than directional claims about which assets the facts help or hurt.
- Same-day market facts are cross-checked against AP/Reuters/Investopedia market-close coverage where possible.
- Official macro and calendar items are cross-checked against Federal Reserve, BLS, BEA, EIA, NYSE, Nasdaq, and company pages where possible.
- Known measurement caveats are included in audit-only form and summarized in the model-facing measurement notes.

## Prompt 3 Checks

- `final_briefing.md` contains no source URLs, source ledger, citations, recommendation language, rankings, scenario analysis, or affected-option mapping.
- `final_briefing.md` contains the required neutrality sentence near the top.
- `final_briefing.md` includes factual datapoints only, with dates, values, scheduled release times, and measurement notes.
- `final_briefing.md` does not contain a `Selected Mechanical Return Context` section.
- `final_briefing.md` does not include manually selected mechanical return rows.
- `final_briefing.md` avoids language that frames one option as preferred or dispreferred.

## Mechanical Appendix Checks To Run After Generation

- Generate the full-universe price, risk, and benchmark-relative context through `capitalbench fetch-universe-performance`.
- Confirm the generated appendix covers every included option in `options.yaml`.
- Confirm the generated appendix is sorted by frozen option order, not by performance.
- Confirm the generated appendix includes return, benchmark-relative, volatility, drawdown, path-quality, 52-week-position, and SPY beta/correlation fields when available.
- Confirm final `model_input.md` contains the `Full-Universe Price, Risk, And Benchmark Context` appendix exactly once.
- Confirm final `model_input.md` does not contain a source ledger or URLs from the audit-only reports.

## Neutrality Statement

Price history in the generated appendix is descriptive context, not a forecast. Inclusion, order, grouping, and row count in the factual briefing and generated appendix are not evidence of expected return.
