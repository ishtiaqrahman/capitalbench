# CapitalBench Briefing Audit — 2026-08-09

## Audit scope

- Audited artifacts: the brand-new `market_fact_report.md`, the model-facing `final_briefing.md`, and the newly generated weekly and monthly mechanical context packages for `CB-2026-08-09-1W` and `CB-2026-08-09-1M`.
- Research cutoff tested: 2026-08-10T03:04:55Z.
- Prior-period input reports were not used to prepare or audit these artifacts.

## Research adequacy

- **Pass — recency:** the report includes the August 7 employment release and August 7 completed equity, rates, and oil observations, the latest completed U.S. session before the cutoff.
- **Pass — macro breadth:** the report covers labor, job openings, GDP, productivity, services activity, retail sales, CPI, PPI, import prices, personal income and spending, PCE inflation, and FOMC policy.
- **Pass — cross-asset breadth:** the audit report records broad U.S. index closes, nominal and real Treasury curves, and Brent crude/geopolitical status. Complete option-level price and risk evidence remains in the mechanical appendices.
- **Pass — horizon coverage:** the event calendar covers every scheduled high-level release identified from August 10 close through the weekly August 17 close and continues through the monthly September 10 close, including the August and September labor/inflation releases, FOMC minutes, Jackson Hole, GDP/PCE, and the Labor Day closure.
- **Pass — provenance and uncertainty:** the audit-only report contains 23 direct public URLs and names publishers, release or observation dates, advance/preliminary statuses, revisions, survey status, and reported retail-sales margins of error where applicable.
- **Pass — neutrality:** neither research artifact ranks options, recommends allocations, maps facts to expected winners, or reproduces selected rows from mechanical context.

## Model-facing briefing checks

- **Pass — no links or citations:** automated text search found zero URLs, `www.` strings, Markdown links, citation blocks, references sections, or source ledger in `final_briefing.md`.
- **Pass — fixed facts only:** the 1,113-word briefing contains dated reported values, scheduled events, publisher attributions, and explicit estimate/status qualifications. It contains no subjective analysis, scenario analysis, “why it matters” section, market-impact claims, or affected-option mapping.
- **Pass — no recommendations or rankings:** no best/worst pick, expected winner, allocation, or outperform/underperform direction is supplied.
- **Pass — required neutrality language:** the exact protocol neutrality sentence appears near the top. The closing neutrality statement repeats that the separate mechanical appendix is complete, descriptive, and non-recommendatory.
- **Pass — no selected mechanical subset:** the briefing contains neither a `Selected Mechanical Return Context` section nor manually selected return, volatility, drawdown, beta, correlation, or Q1 rows.
- **Pass — no Q1 leakage:** the briefing contains no quality-evidence score, Q1 rank, prior-active rank, recent-pullback rank, low-volatility rank, shallow-drawdown rank, Q1 interpretation, or selected Q1 subset.

## Mechanical context checks

- **Pass — complete weekly context:** `CB-2026-08-09-1W` contains 70/70 included options, including cash, with zero failed options and an August 7 as-of date.
- **Pass — complete monthly context:** `CB-2026-08-09-1M` contains 70/70 included options, including cash, with zero failed options and an August 7 as-of date.
- **Pass — permitted disclosed source:** context used `yahoo_chart_adjusted_close_and_reported_volume`, the documented fallback after Tiingo hourly throttling. Separate Tiingo universe validation passed all 69 non-cash tickers for both rounds.
- **Pass — deterministic order:** both context tables are emitted in frozen option order, not sorted by return or any quality measure.
- **Pass — required fields:** the weekly table includes recent return, 5-session active return, prior-window active return, 21-session volatility and drawdown, volume z-score, SPY correlation and beta, and 52-week position. The monthly table contains the horizon-appropriate 5/21/105/63/120/252-session counterparts.
- **Pass — descriptive label:** both context files say returns, volatility, and drawdown are descriptive rather than forecasts and that no recommendation or composite buy score is included.
- **Pass — Q1 coverage and formula:** each complete option-level quality-evidence table covers 68/68 active non-cash, non-benchmark options, or 100%, above the 90% minimum. The frozen formula is 45% prior-active rank, 30% recent-active-reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank.
- **Pass — Q1 neutrality:** each Q1 table is complete and in option order. It does not impose Q2 selection quotas, and the prompt remains free to use or reject the evidence.
- **Pass — cluster exposure:** the separate option table, generated from frozen `options.yaml`, exposes deterministic economic-exposure clusters. The briefing does not relabel, merge, rank, or interpret those clusters.

## Prompt-assembly checks

- **Pass — single inclusion by construction:** the final briefing does not contain either generated appendix heading. The CapitalBench prompt builder injects `universe_quality_evidence.md` once before the briefing and `universe_decision_context.md` once after it; it then adds the complete option table once. Post-import prompt verification must confirm one occurrence of each top-level generated appendix heading before model calls.
- **Pass — descriptive-price guardrail:** the base task, round metadata, briefing, and generated context all state that mechanical price history is descriptive and not a forecast.
- **Pass — closed capability:** manifest notes and round metadata specify one single-turn, non-agentic call per model with browsing, retrieval, tools, and follow-up disabled.

## Audit decision

**Adequate for both runs, conditional only on the standard post-import hash and assembled-prompt checks.** The source report is current to the stated cutoff, balanced across the requested market domains, and explicit about uncertainty. The model-facing briefing passes the salience-bias and research-separation controls. The generated weekly and monthly appendices are complete, horizon-specific, and have zero failed options.
