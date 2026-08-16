# CapitalBench Briefing Audit — August 15, 2026 Weekly and Monthly Rounds

Audit completed against research cutoff **2026-08-16T01:41:04Z** and the newly generated artifacts for `CB-2026-08-15-1W` and `CB-2026-08-15-1M`.

## Result

**PASS.** The source report, neutral model-facing briefing, universe validation, horizon-specific decision context, complete option-level quality evidence, deterministic Portfolio V3 candidate-slate inputs, and assembled model prompt are complete for both rounds. The imported files were hashed before any model call.

## Checks completed

- The source report contains 76 dated or scheduled facts independently re-opened and re-verified for this package.
- Coverage includes broad U.S. equity closes and breadth, oil, the Treasury curve, CPI, PPI, FOMC policy, retail demand, inventories, payrolls and revisions, labor turnover, GDP, personal income and consumption, PCE inflation, business surveys, industrial production, housing, and scheduled catalysts for both scoring windows.
- The model-facing briefing contains exactly one required neutrality statement, no URLs or citations, no source ledger, no recommendation, no manually selected price rows, no manual quality-evidence summary, and no manual candidate-slate summary.
- Both frozen option files are byte-identical and contain 70 included options: one cash option and 69 non-cash tickers.
- A Tiingo validation covering August 14, 2025 through August 14, 2026 returned 69 passed tickers and zero failures, with 252 observations for every non-cash ticker. The duplicate monthly request encountered Tiingo HTTP 429 throttling; because option files and validation dates are identical, the successful validation artifacts were preserved byte-for-byte for the monthly round.
- Both horizon-specific decision-context histories stop at the August 14 close, contain all 70 options in frozen order, use reported Yahoo adjusted close and volume after the Tiingo hourly limit, and report zero failed options.
- Weekly and monthly quality-evidence artifacts each cover 68/68 eligible active non-cash, non-benchmark options and contain no outcome data.
- The Portfolio V3 deterministic candidate-slate builder completed for both horizons and includes the benchmark. Slate rendering is left exclusively to the prompt builder.

## Final model-input assembly checks

- PASS — the weekly effective prompt is 47,801 characters and the monthly effective prompt is 48,106 characters.
- PASS — each effective prompt contains exactly one required neutrality statement, one deterministic V3 candidate-slate heading, one complete quality-evidence heading, one full-universe decision-context heading, and one neutral options heading.
- PASS — neither effective prompt contains an `http://` or `https://` source URL.
- PASS — the weekly prompt contains no one-month horizon wording and the monthly prompt contains no one-week horizon wording.
- PASS — CapitalBench's model-input guardrails accept both effective prompts.
- PASS — each `hashes.json` matches the current model-facing input files, and each imported `final_briefing.md` matches its round-level `briefing.md`.
- PASS — only `final_briefing.md` is marked model-facing in each research manifest; the market fact and audit reports remain audit-only.
- PASS — the briefing has 1,351 whitespace-delimited words, enough to retain the material fixed facts and both catalyst windows while leaving option-level market evidence to the mechanical appendix.
- PASS — no source report, model response, or outcome data is used to hand-edit the quality table or candidate slate.

Entry and exit price snapshots are intentionally absent before their scheduled closes. That expected state does not affect readiness for the one-shot model calls; price collection and scoring occur later under the close-to-close protocol.

## Source URLs audited

- https://apnews.com/article/stocks-markets-rates-oil-inflation-futures-5d9870d6c5ae735f9b74bf4ceefaa3ec
- https://apnews.com/article/wall-street-home-depot-target-fed-7dd75609981e7e96b40aa82523b0ea57
- https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value=2026
- https://www.bls.gov/news.release/cpi.nr0.htm
- https://www.bls.gov/news.release/ppi.nr0.htm
- https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm
- https://www.census.gov/retail/sales.html
- https://www.census.gov/retail/marts/www/marts_current.pdf
- https://www.census.gov/mtis/current/index.html
- https://www.bls.gov/news.release/empsit.nr0.htm
- https://www.bls.gov/news.release/jolts.nr0.htm
- https://www.bea.gov/news/2026/gdp-advance-estimate-2nd-quarter-2026
- https://www.bea.gov/news/2026/personal-income-and-outlays-june-2026
- https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/pmi/july/
- https://www.ismworld.org/supply-management-news-and-reports/reports/ism-pmi-reports/services/july/
- https://www.federalreserve.gov/releases/g17/current/default.htm
- https://www.census.gov/construction/nrc/current/index.html
- https://www.bls.gov/schedule/2026/08_sched.htm
- https://www.bls.gov/schedule/2026/09_sched.htm
- https://www.census.gov/economic-indicators/calendar-listview.html
- https://www.bea.gov/news/schedule/full
- https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
- https://www.federalreserve.gov/newsevents/2026-august.htm
- https://www.federalreserve.gov/newsevents/2026-september.htm
- https://www.nyse.com/trade/hours-calendars
