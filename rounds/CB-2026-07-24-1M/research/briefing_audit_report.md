# CapitalBench Briefing Audit — CB-2026-07-24-1M

## Prompt 2 result

Status: PASS, subject to the final hash and round-audit gates.

This audit covers the brand-new July 24, 2026 research package, the one-month final briefing, the frozen v2.1 option universe, the monthly mechanical decision context, and the V2.2 quality-evidence artifact.

## Cutoff and source checks

- Research cutoff is 2026-07-25T18:33:00Z, before the 2026-07-25T23:30:00Z decision deadline.
- Every factual observation in the final briefing was available by the cutoff.
- The audit-only market fact report records publishers, dates, observation dates, URLs, and source-reported uncertainty.
- The July 24 market close and July 24 new-home-sales release were gathered in a fresh browsing pass; no July 23 CapitalBench report was copied or used as the report source.

## Model-facing briefing checks

- PASS: no URLs, Markdown links, citations, source ledger, bibliography, or references section.
- PASS: no recommendation, allocation, ranking, option-winner, or affected-asset language.
- PASS: no subjective commentary, causal interpretation, or theme-to-option mapping.
- PASS: no manually selected mechanical return rows and no `Selected Mechanical Return Context` section.
- PASS: no Q1 ranks, quality-evidence score, selected quality subset, or Q1 summary.
- PASS: includes the required neutrality language near the top and at the end.
- PASS: dates, values, publisher-neutral statuses, market-implied probabilities labeled as such, scheduled catalysts, and source-reported uncertainty are stated factually.
- PASS: coverage is balanced across U.S. equities, rates, energy, domestic macro, monetary policy, and international releases without changing the frozen exposure clusters.

## Mechanical context checks

- PASS: `market_data/universe_decision_context.md` and JSON use the monthly profile and the July 24, 2026 as-of close.
- PASS: all 70 frozen options are present, failed option count is zero, and rows match frozen option order rather than performance order.
- PASS: the complete table includes current and prior-window returns, active returns versus SPY, volatility, drawdown, volume, SPY correlation and beta, and 52-week position fields when available.
- PASS: the artifact states that returns, volatility, and drawdown are descriptive rather than forecasts.
- PASS: `prices/entry_prices.csv` contains all 70 options for exactly July 24, in frozen option order, from the repository's same-day full-universe Tiingo snapshot.

## V2.2 quality-evidence checks

- PASS: `market_data/universe_quality_evidence.md` and JSON exist exactly once as dedicated mechanical artifacts.
- PASS: all 68 active evidence-eligible options are complete; coverage is 100%, above the 90% minimum.
- PASS: weights are frozen at 45% prior active-return rank, 30% recent active-reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank.
- PASS: the table is complete and neutral, contains no recommendation, and imposes no Q2-style shortlist or final-portfolio quota.

## Input-assembly and cluster checks

- PASS: the frozen option table supplies deterministic economic-exposure clusters.
- PASS: the research briefing does not rename, merge, rank, or interpret those clusters.
- PASS: `prompt.md` explicitly says price history is descriptive rather than a forecast.
- PASS: the standard v2.2 prompt builder places the complete quality table once and the complete decision-context appendix once; no copies appear inside the briefing.
- PASS: scheduled events stop at the August 24 exit; the August 27-29 Jackson Hole symposium is explicitly identified as outside the scoring window.

## Remaining gates

- Recompute research and round hashes after import.
- Validate the assembled package, frozen eight-model roster, parsed submissions, and accepted run through the standard CLI gates before publication.

