# Prompt 2 Briefing Audit Report - July 15, 2026 Post-Close

Rounds: `CB-2026-07-15-1W` and `CB-2026-07-15-1M`

Research cutoff: 2026-07-16T00:52:00Z

Visibility: audit-only. This report is not model-facing.

## Artifact Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Prompt 1 market fact report exists | pass | A source-ledger report was prepared from direct public-source review for the July 15 cutoff. |
| Separate Prompt 3 briefings exist | pass | Weekly and monthly files state their exact scoring windows and contain horizon-specific event schedules. |
| Final briefings contain no URLs or markdown citations | pass | URLs and the source ledger remain in Prompt 1 only. |
| Final briefings contain no recommendations, rankings, subjective analysis, or affected-option mapping | pass | Sections contain dated factual statements, source-reported statuses, scheduled events, or factual uncertainties only. |
| Final briefings contain no selected mechanical return rows | pass | No return rows are copied into either briefing; mechanical context appears only in the complete generated appendix. |
| Required neutrality sentence appears near the top | pass | Present immediately after the round window in both briefings. |
| Price history is labeled descriptive rather than predictive | pass | The final neutrality statement and generated appendix state this explicitly. |
| Broad asset-area balance is maintained | pass | Market breadth, inflation and rates, labor and growth, corporate facts, energy and geopolitical status, scheduled events, and uncertainties are bounded sections. |
| Forecasts and future events are labeled | pass | Corporate guidance and scheduled releases are labeled; no scheduled outcome is stated as known. |
| Source-reported caveats are preserved | pass | Data revisions, collection dates, company metric caveats, geopolitical uncertainty, and schedule-change risk are retained. |

## Mechanical Appendix Checks

| Check | Result | Evidence |
| --- | --- | --- |
| Complete artifact exists for both rounds | pass | Markdown, CSV, and JSON exist in each round's `market_data` directory. |
| Every included option is covered | pass | 70 included options, 70 appendix rows, and no failed options in each round. |
| Rows follow frozen option order | pass | Parsed option IDs and appendix row IDs match exactly in both tracks. |
| Exact cutoff-date prices are present | pass | Every appendix row and every entry-price row is dated 2026-07-15. |
| Required return and risk fields are present | pass | The current pipeline generated 7-day, 30-day, 6-month, and 1-year returns; SPY-relative return; annualized volatility; max drawdown; up-day share; 52-week position; and SPY beta and correlation where available. |
| Source status is disclosed | pass | Yahoo adjusted close is identified as the documented fallback after the Tiingo hourly rate limit. A one-year Tiingo validation passed 61 non-cash tickers; the eight unchanged core ETFs interrupted by HTTP 429 were covered by exact-date and one-year Yahoo adjusted-close fallback data. |
| Weekly and monthly context is identical | pass | Corresponding Markdown, CSV, JSON, and entry-price files match byte for byte across tracks. |

## Salience And Fairness Review

- No option IDs, tickers, allocation instructions, or manually selected price rows are introduced by the final briefings.
- The reports do not convert July 15 facts into asset forecasts, expected winners, scenarios, or allocation suggestions.
- Market-close facts include gains and declines across broad, regional, and company-level observations. Inflation facts retain both monthly declines and elevated year-over-year readings.
- Energy facts include both the oil move and unresolved military, shipping, energy-flow, and diplomatic conditions. Corporate facts include completed results, scheduled results, guidance, and source-reported caveats.
- The weekly briefing stops at the July 22 close and identifies results scheduled after that close as outside the weekly snapshot. The monthly briefing extends through the August 14 close without adding outcome assumptions.
- The same frozen briefing, option universe, generated appendix, prompt, constraints, cutoff, and provider execution policy will be supplied to every eligible model in each track.

## Readiness Decision

Prompt 1, Prompt 2, and both Prompt 3 briefings are complete and ready for import. The research and mechanical context pass the content, coverage, order, exact-date, neutrality, salience, and source-separation checks. Final round readiness still requires successful research import, prompt assembly verification, round hashing, provider-run validation, and official-run acceptance.
