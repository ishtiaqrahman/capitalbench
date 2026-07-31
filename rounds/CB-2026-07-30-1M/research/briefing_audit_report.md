# CapitalBench Briefing Audit — CB-2026-07-30-1M

## Prompt 2 Result

Status: PASS, subject to the final import, universe-validation, hash, assembled-input, submission-validation, acceptance, and round-audit gates.

This audit covers the newly browsed July 30, 2026 market fact report, the one-month final briefing, the frozen V2.1 option universe, the monthly mechanical decision context, and the V2.2 option-quality artifact.

## Cutoff and Source Checks

- PASS: the research cutoff is 2026-07-31T08:42:00Z, before the 2026-07-31T12:30:00Z decision deadline.
- PASS: factual observations in the final briefing were public by the cutoff. The later July 31 Employment Cost Index and euro-area flash-inflation outcomes are explicitly unavailable and excluded.
- PASS: the audit-only market fact report records publisher names, publication or access dates, observation dates, URLs, source limitations, publisher-reported uncertainty, and company-labeled forecasts.
- PASS: the report uses the July 30 close, July 30 GDP, PCE, claims, Apple, and Amazon releases, and the July 31 Bank of Japan decision; it is not a copy of the July 29 package.
- PASS: research was gathered through direct public-source browsing, without participant model APIs, provider-hosted search, model browsing, or model-agent research.

## Completeness and Balance Review

- PASS: the report covers all four principal U.S. equity indexes, market breadth, Treasury yields, FOMC policy, GDP, PCE, CPI, PPI, labor, consumption, manufacturing, housing, company results, energy, international equities, the Bank of Japan, the ECB, euro-area inflation, and China.
- PASS: scheduled events cover every dated official or company catalyst identified within the one-month window through the August 28 close.
- PASS: source-reported counterweights and uncertainty are preserved: one-day gains and prior losses; year-to-date gains; growth and inflation within GDP; nominal and real consumption; company growth and costs, cash use, one-time valuation effects, or tariff refunds; sampling margins; revisions; unresolved geopolitical conditions; and unknown scheduled outcomes.
- PASS: no audit-report section calculates an answer to model Question 1, selects Q1 rows, imposes Q2 quotas, recommends an asset, ranks an option, or maps a fact to a CapitalBench exposure.

## Model-Facing Briefing Checks

- PASS: the final briefing contains no URL, Markdown link, citation, source ledger, bibliography, or references section.
- PASS: it contains no allocation instruction, recommendation, winner claim, affected-asset mapping, scenario analysis, or subjective “why it matters” commentary.
- PASS: it contains no manually selected mechanical return rows and no summary, interpretation, or selected subset of the V2.2 option-quality table.
- PASS: required neutrality language appears near the top and in the closing statement.
- PASS: company forecasts are labeled; unknown scheduled outcomes remain unknown; sampling and revision uncertainty is retained where reported.
- PASS: salience is controlled with broad factual groups, counterbalancing facts, and no performance-sorted option table or mention-count-based option emphasis.

## Mechanical Context and V2.2 Checks

- PASS: the frozen V2.1 option file is byte-identical to the immediately preceding production round's option file. Its reused Tiingo validation packet covers all 70 options, skips only CASH, passes all 69 tickers, and reports zero failed tickers.
- PASS: the monthly decision-context artifacts use the July 30, 2026 as-of close, include all 70 frozen options in option order, and have zero failed options.
- PASS: the built-in public Yahoo chart fallback supplied adjusted closes and reported volume after Tiingo returned HTTP 429 rate-limit responses. This fallback affects model-input context only; protocol scoring prices retain the Tiingo path.
- PASS: the V2.2 artifact is complete for all 68 evidence-eligible active options, giving 100% coverage, and uses the fixed 45% prior active-return rank, 30% recent active-reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank formula.
- PASS: the standard V2.2 prompt requires a 6-8 option candidate ledger including SP500 and at least four clusters, 1-5 final holdings, low/base/high scenario returns, the active-holding SPY hurdle, and the 50% nonbenchmark exposure-cluster cap.
- PASS: the complete option table, full-universe context, and complete Q1 evidence appendix are each designed to appear exactly once in assembled model input.

## Remaining Gates

- Import the three research artifacts and verify the final briefing exactly matches `briefing.md`.
- Fetch or reconstruct the full-universe July 30 entry-price snapshot from the complete mechanical source history, and recompute hashes.
- Run the research, universe, price, decision-context, and submission-validation tests.
- Confirm each assembled section occurs exactly once before participant calls.
- Validate all eight submissions; retry only transport, provider, or schema failures; accept the clean official run; schedule resolution; publish and sync the pending round; audit the result.
