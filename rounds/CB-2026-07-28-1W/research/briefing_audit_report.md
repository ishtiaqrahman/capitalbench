# CapitalBench Briefing Audit — CB-2026-07-28-1W

## Prompt 2 Result

Status: PASS, subject to the final import, hash, assembled-input, submission-validation, and round-audit gates.

This audit covers the newly browsed July 28, 2026 market fact report, the one-week final briefing, the frozen V2.1 option universe, the weekly mechanical decision context, and the V2.2 option-quality artifact.

## Cutoff and Source Checks

- PASS: the research cutoff is 2026-07-29T07:56:00Z, before the 2026-07-29T12:30:00Z decision deadline.
- PASS: factual observations and scheduled events in the final briefing were available by the cutoff; later outcomes are excluded.
- PASS: the audit-only market fact report records publisher names, publication or access dates, observation dates, URLs, source limitations, and source-reported uncertainty.
- PASS: the report uses the July 28 close and the newly available July 28 consumer-confidence release; it is not a copy of the July 27 package.
- PASS: research was gathered through direct public-source browsing, without participant APIs, model browsing, provider-hosted search, or agent search APIs.

## Model-Facing Briefing Checks

- PASS: the final briefing contains no URL, Markdown link, citation, source ledger, bibliography, or references section.
- PASS: it contains no allocation instruction, recommendation, ranking, winner claim, affected-asset mapping, scenario analysis, or subjective commentary.
- PASS: it contains no manually selected mechanical return rows and no summary of the V2.2 option-quality table.
- PASS: required neutrality language appears near the top and in the closing statement.
- PASS: market-implied probabilities and the secondary-source VIX observation are labeled; unknown scheduled outcomes are unavailable; sampling and revision uncertainty is retained where reported.
- PASS: the briefing covers equity indexes and breadth, rates and policy, inflation, labor and demand, energy and other cross-assets, and international conditions without interpreting CapitalBench exposure clusters.

## Mechanical Context and V2.2 Checks

- PASS: the weekly decision-context artifacts use the July 28, 2026 as-of close, include all 70 frozen options in option order, and have zero failed options.
- PASS: the full-universe entry-price file contains 70 option rows for July 28, including cash; all 69 market symbols use Tiingo EOD adjusted closes.
- PASS: the V2.2 artifact is complete for all 68 active evidence-eligible options, giving 100% coverage, and uses the fixed 45% prior active-return rank, 30% recent active-reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank formula.
- PASS: the standard V2.2 prompt requires a 6-8 asset candidate ledger including SP500 and at least four clusters, 1-5 final holdings, low/base/high scenario returns, the active-holding SPY hurdle, and the 50% nonbenchmark exposure-cluster cap.
- PASS: the complete option table and mechanical appendices are designed to appear once each in the assembled model input.

## Remaining Gates

- Import the three research artifacts and verify the final briefing exactly matches `briefing.md`.
- Run research, universe, price, decision-context, and validation tests.
- Recompute hashes and confirm each assembled section occurs exactly once before participant calls.
- Validate all eight submissions; retry only transport, provider, or schema failures; accept the clean official run; publish and sync the pending round; audit the result.
