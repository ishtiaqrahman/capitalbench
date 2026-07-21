# Prompt 2 Briefing Audit Report

Round: CB-2026-07-20-1W
Research cutoff: 2026-07-21T00:10:00Z
Status: audit-only; not model-facing
Overall result: PASS

## Prompt 1 Review

- All stated observations were public by the research cutoff: PASS.
- Direct browser review covered Treasury rates, the July 20 market close, Census, Federal Reserve, BEA, EIA, China NBS, and official calendars: PASS.
- The BLS browser access-denied condition is explicitly disclosed; the report does not misstate those older official facts as a fresh page observation: PASS.
- Publisher, publication date, observation period, URL, forecast status, and source-reported uncertainty are retained in the audit-only ledger: PASS.
- July 20 Treasury yields, U.S. closes, energy, international-market, and shipping facts make this a fresh July 20 report rather than a carry-forward of the July 17 report: PASS.
- The report contains no allocation, rank, expected-winner, or affected-option mapping: PASS.
- Mechanical market data are referenced as one complete generated artifact rather than reproduced as a manually selected subset: PASS.

## Prompt 3 Review

- `final_briefing.md` contains no URL, Markdown citation, bibliography, source ledger, or reference list: PASS.
- It contains no recommendation, allocation, rank, subjective market analysis, scenario section, "why it matters" commentary, or affected-option mapping: PASS.
- Forecast values are explicitly identified as forecasts and scheduled items are distinguished from released facts: PASS.
- The required neutrality statement is near the top and a matching neutrality statement is at the end: PASS.
- The briefing is concise at 701 words and covers catalysts only through the July 27 exit close: PASS.
- The briefing does not contain a `Selected Mechanical Return Context` section or manually selected return rows: PASS.

## Mechanical Appendix Review

- `market_data/universe_decision_context.md` exists with weekly profile and a July 20, 2026 requested close: PASS.
- Frozen universe options: 70. Appendix option rows: 70. Unique option IDs: 70. Failed options: zero: PASS.
- Appendix order exactly matches frozen `options.yaml` order: PASS.
- Weekly columns include three-session return, five-session active return versus SPY, prior-window active return, 21-session volatility and drawdown, volume z-score, 63-session SPY correlation and beta, and 52-week-high distance: PASS.
- Deterministic economic-exposure cluster is populated for every option, with 19 distinct clusters and `capital_preservation` for CASH: PASS.
- The table contains no rank, recommendation, or composite buy score: PASS.

## Assembled Input Review

- The model input explicitly states that price history is descriptive context rather than a forecast: PASS.
- The full-universe decision-context appendix occurs exactly once: PASS.
- Audit-only Prompt 1 and Prompt 2 reports do not occur in model input: PASS.
- Prompt 3 briefing occurs once: PASS.
- The compact option table includes deterministic economic-exposure clusters: PASS.
- The briefing does not relabel, merge, rank, or interpret those clusters: PASS.
- V2 instructions require a 6-8 candidate ledger, SP500, at least four clusters, low/base/high forecasts, continuation and reversal cases, a time-window catalyst, an invalidation condition, the SPY active hurdle, and the 50% cluster cap: PASS.

## Disposition

The weekly package is approved for preflight and the official single-turn, non-agentic run. The audit-only reports must remain outside participant-model input.
