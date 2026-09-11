# Fresh briefing audit — September 11, 2026

Audit-only. Cutoff: 2026-09-11T03:51:50Z. Applies to CB-2026-09-11-1W and CB-2026-09-11-1M.

## Research integrity

- The new final briefing was written from direct public-source browsing in this session. It does not reuse the previous report. Its seven broad sections each have two bullets, with publishers, observation periods, values and statuses retained.
- No URLs, citation markers, source ledger, subjective market analysis, recommendations, allocation advice, option mapping, quality ranks/scores, candidate-slate rows or selected mechanical returns appear in the model-facing digest.
- Required neutrality wording appears near the top and historical-evidence neutrality is repeated at the end. Raw sources and reconciliation notes remain audit-only.
- Released September 10 PPI, claims, housing, mortgage rates, ECB decisions, oil/gas inventories and market observations are distinguished from future CPI and other calendar events. ECB September 16 implementation is distinguished from September 10 announcement. Staff projections remain forecasts.
- Closing equity values are distinguished from intraday breadth and different-time bond quotations. September 4 inventories and the two different claims reference weeks are explicit. Monthly and annual changes are not confused. Source limitations and uncertain update times are disclosed in the source report.
- The entry close is September 11. Five later equity sessions lead to September 18 weekly exit. The monthly anniversary falls Sunday October 11 and rolls to the next NYSE equity session, Monday October 12. Future entry/exit prices are not claimed to exist.

## Mechanical and execution integrity

- Existing acquisition code fetched fresh native Tiingo histories for all 69 traded symbols, 298 observations each through September 10. Mechanical pipeline reuse is distinct from report or market-data reuse. No participant model API collected the research.
- Both full context tables contain all 70 options, including CASH, in frozen option order. Separate weekly/monthly profiles supply prior and recent active returns, risk, drawdown, volume, price-path and benchmark-relative diagnostics.
- The complete quality evidence tables cover all 68 active non-SPY, non-CASH options (100%), above the 90% requirement. Their 45/30/15/10 formula is unchanged, and no forced-selection quota is added.
- The unchanged prompt builder supplies exactly one deterministic slate, one complete quality table before the briefing, and one full context appendix. The slate follows five frozen lanes and includes SPY. Static economic-exposure clusters remain intact and are not reinterpreted by the report.
- A pre-call programmatic integrity check is recorded in research/input_integrity.json for each round, including option order, complete quality coverage, one-time section inclusion, exclusion of audit reports, briefing equality, prompt hash and market-data cutoff. Required research/input tests run before official calls.
- Both manifests freeze Portfolio V3.0 and the same seven-model roster. Each model receives one single-turn, tool-free official decision request per horizon. The deterministic 35/35/30 rule and SPY fallback are unchanged. Inputs will be hashed before calls and remain frozen thereafter; any technical retry must be separately disclosed.
