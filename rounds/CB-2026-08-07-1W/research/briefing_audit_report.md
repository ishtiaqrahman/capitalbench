# CapitalBench Briefing Audit Report

- Audit time: 2026-08-07T09:14:42Z
- Research cutoff checked: 2026-08-07T09:00:00Z
- Human-researched artifacts: `market_fact_report.md` and `final_briefing.md`
- Mechanical artifacts: generated and checked after the research-content review.

## Research provenance and completeness

| Check | Result | Evidence |
|---|---|---|
| Completely new report | PASS | A direct public-source browsing pass produced this August 7 packet; no older CapitalBench report or briefing was used as evidence. |
| Cutoff integrity | PASS | Every included outcome was published or observed by 09:00 UTC; later events are labeled scheduled and have no assumed values. |
| Premarket boundary | PASS | The August 7 Employment Situation and U.S. cash session were unavailable at the cutoff and are not included as outcomes. |
| Traceable ledger | PASS | Each source-ledger section states publisher, page, publication or observation date, URL, extracted facts, and source-reported status or uncertainty. |
| Macro breadth | PASS | Policy, rates, GDP, income, consumption, inflation, saving, productivity, labor costs, labor demand, surveys, and retail spending are covered. |
| Cross-asset/global breadth | PASS | Nominal and real Treasury yields, four broad U.S. indexes, oil, ECB policy, and scheduled international-policy events are covered. |
| Weekly calendar | PASS | Scheduled events through the August 14 close are included without forecast values. |
| Monthly calendar | PASS | Scheduled events through the September 8 close, including the September 7 market holiday, are included without forecast values. |
| Limitations preserved | PASS | Advance, preliminary, survey, revision, estimate, and sampling-interval qualifications are retained. |
| Counterbalancing facts | PASS | Slower headline GDP appears with stronger private domestic final sales; expanding services activity appears with contracting services employment; a down session appears with positive partial-week and year-to-date index changes. |
| No allocation advice | PASS | No option is selected, ranked, recommended, excluded, or linked to an expected return. |
| No manual Q1 evidence | PASS | No quality score, rank, or component value appears in either human-written report. |

## Model-facing briefing review

| Check | Result | Evidence |
|---|---|---|
| Fixed facts only | PASS | The briefing contains dated observations, source-reported qualifications, and explicitly scheduled statuses. |
| Required neutrality sentence | PASS | The fixed neutrality sentence appears near the top and again in the closing status section. |
| No URLs or citations | PASS | The model-facing document has no URLs, hyperlinks, citation markers, footnotes, or source table. |
| No recommendation terms | PASS | It contains no buy, sell, overweight, underweight, preferred, winner, or allocation instruction. |
| No asset mapping | PASS | No factual row is connected to a CapitalBench option or claimed beneficiary. |
| No scenario construction | PASS | Uncertainty is reported without probabilities or conditional portfolio implications. |
| Balanced content | PASS | Activity, demand, prices, productivity, labor, policy, rates, surveys, global policy, markets, oil, and both catalyst windows are present. |

## Mechanical pre-call review

| Check | Result | Evidence |
|---|---|---|
| Universe validation | PASS | Both rounds validated 70 options and 69 distinct non-cash tickers with zero failures. |
| Full-universe context | PASS | Weekly and monthly context artifacts each contain 70/70 options with zero failed options and retain frozen `options.yaml` order. |
| Cutoff-safe market date | PASS | All mechanical inputs stop at the August 6 close, the latest completed market session before the August 7 09:00 UTC research cutoff. The future August 7 close is reserved for scoring entry prices and is not used in the model input. |
| Horizon-matched measures | PASS | The weekly and monthly profiles use their separately frozen session windows and include return, benchmark-relative, volatility, drawdown, volume, beta/correlation, and 52-week fields where applicable. |
| Complete V2.2 Q1 evidence | PASS | Each quality artifact covers 68/68 active non-benchmark, non-cash options, above the 90% floor, and uses the frozen 45/30/15/10 formula. |
| Single primary data source | PASS | Fresh adjusted price and volume histories came directly from Tiingo; no row was imputed, omitted, or supplemented from an older report. |
| Descriptive presentation | PASS | Mechanical evidence is labeled historical/descriptive, contains no recommendation or composite buy score, and is presented in frozen option order. |
| Weekly/monthly separation | PASS | The source close is shared, while the generated context profiles and quality scores differ according to the frozen horizon formulas. |
| Prompt single-inclusion contract | PENDING | The built prompt will be checked immediately after import to confirm each generated appendix appears exactly once. |
| Final hashes | PENDING | Final round hashes will be regenerated after this audit is imported and before provider calls. |

## Current audit decision

The new human-researched packet and deterministic market-input packet are **COMPLETE AND PASSING**. Provider calls may begin only after import, prompt single-inclusion verification, and final pre-call hashing pass.
