# CapitalBench Briefing Audit Report

Research cutoff: 2026-06-25T23:00:00Z
Scope: audit-only check for the June 25, 2026 weekly and monthly round research package.

## Prompt 1 Coverage Check

- Current macro releases included: BEA May personal income/outlays and PCE prices, BEA Q1 GDP third estimate, Department of Labor weekly claims, Census May durable-goods advance report, BLS CPI/PPI/employment context.
- Rates included: Fed H.15 latest Treasury constant maturity data through June 24, 2026, effective federal funds rate, bank prime loan rate, and June 17 FOMC target range.
- Index close data included: June 25 S&P 500, Dow, Nasdaq, and Russell 2000 close, daily moves, week-to-date moves, and year-to-date moves from AP.
- Broad asset areas included: U.S. equities, rates, energy, precious metals, crypto, U.S. macro, global PMI data, and a company/sector earnings data point for memory semiconductors.
- Scheduled catalysts included: July 2 jobs and M3 full report, July 3 NYSE holiday, July 7 trade, July 8 FOMC minutes, July 14 CPI, July 15 PPI, July 17 import/export prices, July 21 labor releases, July 27 durable goods, July 28-29 FOMC, and July 30 PCE/GDP.
- Source uncertainty included: BEA estimates/revisions, Census advance-estimate and no-probability-sample note, claims revisions, flash PMI preliminary status, and H.15 observation-date limitation.

## Prompt 3 Final Briefing Check

- `final_briefing.md` contains no source URLs.
- `final_briefing.md` contains no source ledger.
- `final_briefing.md` contains no citations.
- `final_briefing.md` contains no recommendations, rankings, allocation language, or affected-option mapping.
- `final_briefing.md` does not include a `Selected Mechanical Return Context` section.
- `final_briefing.md` does not include any manually selected mechanical return rows.
- `final_briefing.md` includes the required neutrality sentence near the top.
- `final_briefing.md` states that the mechanical full-universe appendix follows in the model input.
- `final_briefing.md` includes price-history and measurement discipline by keeping price facts descriptive and adding measurement notes.
- No item in `final_briefing.md` ranks CapitalBench options or maps facts to expected winners.

## Mechanical Appendix Check

- The complete full-universe price, risk, and benchmark-relative appendix must be generated separately by `fetch-universe-performance`.
- The expected generated artifact path is `market_data/universe_trailing_returns.md` inside each round.
- The expected generated section title is `Full-Universe Price, Risk, And Benchmark Context`.
- The expected generated table must cover every included option in option order, not performance order.
- The expected generated table must include returns, benchmark-relative diagnostics, volatility, drawdown, path quality, 52-week position, and SPY beta/correlation when available.
- The final model input must contain the full-universe price-context appendix exactly once.

## Import Readiness

- Prompt 1 audit artifact: `/tmp/capitalbench-20260625-research/market_fact_report.md`.
- Prompt 2 audit artifact: `/tmp/capitalbench-20260625-research/briefing_audit_report.md`.
- Prompt 3 model-facing artifact: `/tmp/capitalbench-20260625-research/final_briefing.md`.
- Research cutoff for import: `2026-06-25T23:00:00Z`.
