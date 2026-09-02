# CapitalBench briefing audit — September 2, 2026

Audit status: **PASS**

Research cutoff: `2026-09-02T03:13:45Z`

This audit covers a new research pass performed for the September 2 cycle. No prior CapitalBench input report or briefing was opened, copied, summarized, or used as a research source.

## Freshness and source adequacy

- `market_fact_report.md` contains 3,472 words, 32 numbered fact sections, a dated catalyst calendar, and 49 direct source-URL occurrences.
- All included facts were publicly available at or before the frozen cutoff. The latest completed U.S. market session is September 1, 2026.
- The source pass covers the latest U.S. index close and breadth, Treasury yields, oil, gold and the dollar; newly released ISM, JOLTS, and construction data; current inflation, spending, production, housing, and durable-goods baselines; euro-area and Chinese data; Federal Reserve, ECB, and BOJ policy status; oil-supply and geopolitical developments; company results; and dated catalysts through the monthly scoring window.
- Primary publishers are used where available, including BLS, BEA, Census, Federal Reserve, ECB, BOJ, Eurostat, China NBS, ISM, EIA, OPEC, and issuer investor-relations pages. AP and Reuters are used for the latest market close and cross-asset reporting.
- Forecasts, estimates, preliminary values, sampling uncertainty, later revisions, and conditional assumptions are labeled as such.

## Model-facing briefing checks

- `final_briefing.md` contains 1,616 words and no URLs.
- `capitalbench.research.validate_final_briefing` returns no errors or warnings.
- The required neutrality statement appears near the top, and an equivalent statement closes the briefing.
- The briefing contains fixed factual datapoints only. It contains no source ledger, recommendation, ranking, allocation instruction, scenario analysis, affected-asset mapping, or subjective interpretation.
- It contains no manually selected return rows, no `Selected Mechanical Return Context`, no Q1 ranks or quality-evidence scores, and no candidate-slate rows or summaries.
- It does not relabel, merge, rank, or interpret economic-exposure clusters.
- The briefing states that historical price context is descriptive and is not a forecast.

## Mechanical package controls

The following artifacts are intentionally not reproduced manually in either research report. The CapitalBench build must generate and inject them mechanically after import:

- full-universe decision context in frozen option order, including return, benchmark-relative, volatility, drawdown, path-quality, 52-week-position, and SPY beta/correlation diagnostics when available;
- the complete V3 quality-evidence table, covering at least 90% of active options and using the frozen 45/30/15/10 formula without Q2-style quotas;
- the deterministic five-lane V3 candidate slate, including SPY and no outcome data;
- the complete neutral option table with deterministic economic-exposure clusters.

## Post-generation verification

- Both assembled model inputs contain the full-universe decision context, complete quality-evidence table, deterministic V3 slate, and neutral option table exactly once.
- Each decision-context artifact contains all 70 included options in frozen option order, reports zero failed options, and includes the required return, active-return, prior-window, volatility, drawdown, path-quality, volume, 52-week, and SPY beta/correlation fields when available.
- Each complete quality table covers 68 of 68 active non-benchmark, non-cash options (100%, above the 90% requirement). The generated artifact states and uses the frozen 45% prior active-rank, 30% recent active-pullback, 15% low-volatility, and 10% shallow-drawdown formula. It applies no Q2-style selection quota.
- The weekly V3 slate has 13 unique rows and the monthly slate has 15 unique rows. Each follows all five active lane rules, includes SPY exactly once as the benchmark row, and contains no outcome data.
- Each neutral option table contains all 70 included options. The deterministic exposure-cluster function returns a non-empty cluster for every row.
- The weekly and monthly `options.yaml` files are byte-identical (`SHA-256 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729`). The imported briefings are also byte-identical.
- Tiingo universe validation covers July 1, 2025 through September 1, 2026 and passes all 69 non-cash tickers; the identical validation artifacts are attached to both rounds.
- The full assembled inputs contain the required statement that price history is descriptive context rather than a forecast. The final briefing appears once in each input.
