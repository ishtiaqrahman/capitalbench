# CapitalBench Briefing Audit — CB-2026-07-27-1M

## Prompt 2 Result

Status: PASS, subject to the final import, hash, assembled-input, submission-validation, and round-audit gates.

This audit covers the newly browsed July 27, 2026 market fact report, the one-month final briefing, the frozen V2.1 option universe, the monthly mechanical decision context, and the V2.2 quality-evidence artifact.

## Cutoff and Source Checks

- PASS: the research cutoff is 2026-07-28T06:50:00Z, before the 2026-07-28T12:30:00Z decision deadline.
- PASS: factual observations and scheduled events in the final briefing were available by the cutoff; later outcomes are not included.
- PASS: the audit-only market fact report records publisher names, publication or access dates, observation dates, URLs, and source-reported uncertainty.
- PASS: the report is a new July 27 package. Its SHA-256 differs from the July 24 weekly and monthly market fact reports, and it uses the July 27 close and newly available July 27 releases rather than reusing the prior report.
- PASS: research was gathered through direct public-source browsing, without a model API, agent search API, or provider-hosted model browsing feature.

## Model-Facing Briefing Checks

- PASS: `final_briefing.md` contains no URL, Markdown link, citation, source ledger, bibliography, or references section.
- PASS: it contains no recommendation, allocation instruction, ranking, expected-winner claim, affected-asset mapping, scenario analysis, or subjective “why it matters” commentary.
- PASS: it contains no manually selected mechanical return rows and no `Selected Mechanical Return Context` section.
- PASS: it contains no Q1 rank, quality-evidence score, selected quality subset, or Q1 table summary.
- PASS: the required neutrality language appears near the top, and the closing statement again describes the briefing and mechanical history as non-forecast context.
- PASS: market-implied probabilities are labeled as market-implied, unknown scheduled outcomes are identified as unavailable, and sampling or revision uncertainty is retained where reported.
- PASS: the briefing covers equity indexes and breadth, rates and policy, inflation, labor and demand, energy and other cross-assets, and international conditions without interpreting CapitalBench exposure clusters.

## Mechanical Context Checks

- PASS: `market_data/universe_decision_context.md`, JSON, and CSV use the monthly profile and the July 27, 2026 as-of close.
- PASS: all 70 included options are present, the failed-option count is zero, and rows match frozen option order rather than performance order.
- PASS: the complete monthly table provides recent and prior-window returns, active returns versus SPY, volatility, drawdown, volume diagnostics when available, SPY correlation and beta, and 52-week position.
- PASS: the mechanical context is sourced from Yahoo adjusted-price and reported-volume history. For EWC, whose current Yahoo close fields were pending, the pipeline joined the frozen July 27 Tiingo EOD entry close to the prior Yahoo history; its unavailable current-volume diagnostic is left blank rather than inferred.
- PASS: `prices/entry_prices.csv` contains all 70 options for exactly July 27, in frozen option order, from the repository’s full-universe Tiingo EOD snapshot.
- PASS: the frozen option universe is byte-identical to the July 24 universe. The most recent complete Tiingo lookback validation passed all 69 non-cash tickers through July 24, and the new July 27 Tiingo snapshot plus decision-context generation confirms all 70 current rows.

## V2.2 Quality-Evidence Checks

- PASS: `market_data/universe_quality_evidence.md` and JSON exist as dedicated mechanical artifacts.
- PASS: all 68 active evidence-eligible options are complete; coverage is 100%, above the 90% minimum.
- PASS: the fixed formula is 45% prior active-return rank, 30% recent active-reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank.
- PASS: rows remain in frozen option order, the table is descriptive and neutral, and no Q2-style shortlist or final-portfolio quota is imposed.

## Input-Assembly and Cluster Checks

- PASS: the frozen option table supplies deterministic economic-exposure clusters.
- PASS: the research briefing does not rename, merge, rank, or interpret those clusters.
- PASS: `prompt.md` states that price history is descriptive context rather than a forecast.
- PASS: the standard V2.2 prompt builder is expected to place the complete quality-evidence table exactly once and the complete decision-context appendix exactly once; the post-import assembled-input check must confirm these counts.

## Remaining Gates

- Import the three research artifacts and verify that `research/final_briefing.md` exactly matches `briefing.md`.
- Run the research, decision-context, price, and submission-validation tests.
- Recompute and verify research and round hashes.
- Confirm each assembled section occurs exactly once before provider calls.
- Validate all eight official submissions and complete acceptance, publication, deployment, and live-site checks.
