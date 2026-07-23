# CapitalBench Briefing Audit — July 22, 2026 Inputs

## Scope

- Audited artifacts: `market_fact_report.md`, `final_briefing.md`, both rounds' generated full-universe decision context, both rounds' generated Portfolio V2.2 quality evidence, and both rounds' frozen option files.
- Research cutoff checked: `2026-07-23T04:04:25Z`.
- Round targets checked: `CB-2026-07-22-1W` and `CB-2026-07-22-1M`.

## Prompt 1 checks

- Pass — the source report identifies publishers, publication or observation dates, URLs, fixed facts, and source-reported status or uncertainty.
- Pass — coverage includes macro releases, monetary policy, the July 22 index close, Treasury yields, oil, international indexes, newly released company results, energy inventories, and catalysts inside both scoring windows.
- Pass — the report does not rank CapitalBench options, recommend allocations, or map facts to expected winners.
- Pass — no manually selected mechanical return table is included.
- Pass — the report does not reproduce, summarize, interpret, or rank the Portfolio V2.2 Q1 evidence table.

## Prompt 3 checks

- Pass — `final_briefing.md` contains no URL, citation marker, or source ledger.
- Pass — the briefing uses fixed factual statements, identifies publishers where needed, labels unaudited results, retains stated sampling or revision uncertainty, and describes scheduled items as scheduled.
- Pass — the required neutrality sentence appears near the top.
- Pass — the briefing contains no recommendation, option ranking, subjective investment analysis, or affected-option mapping.
- Pass — there is no selected mechanical return section or selected subset of mechanical price rows.
- Pass — there is no Q1 rank, quality-evidence score, selected Q1 row, or summary of Q1 evidence.
- Pass — the briefing states that price history is descriptive context and not a forecast.

## Mechanical decision-context checks

- Pass — the weekly artifact uses the weekly profile and the monthly artifact uses the monthly profile.
- Pass — each artifact is as of July 22, contains all 70 frozen options, and reports zero failed options.
- Pass — rows follow frozen option order rather than a performance sort.
- Pass — the generated schemas include horizon returns, benchmark-relative diagnostics, realized volatility, drawdown, path-quality measures, 52-week position, and SPY beta and correlation where available.
- Pass — each entry-price file has one header plus 70 option rows, all non-cash rows use July 22 closes, and the two identical entry-date/universe files match byte for byte.

## Portfolio V2.2 Q1 evidence checks

- Pass — each generated Q1 artifact covers all 68 active non-cash, non-benchmark options, for 100% coverage and above the 90% minimum.
- Pass — the fixed weights are 45% prior active return rank, 30% recent active-return reversal rank, 15% low-volatility rank, and 10% shallow-drawdown rank.
- Pass — the complete table remains mechanically generated in frozen option order.
- Pass — the evidence is information only and does not impose Q2-style category, directional, or implementation quotas.

## Input-assembly requirements

- Required at the freeze gate — the prompt builder must include the complete quality-evidence section exactly once and the complete horizon-specific decision-context section exactly once.
- Required at the freeze gate — the generated option table must preserve deterministic economic-exposure clusters without relabeling, merging, ranking, or interpretation by the research briefing.
- Required at the freeze gate — round hashes must be generated only after the imported research, entry prices, and prompt package are final.

## Audit result

Prompt 1 and Prompt 3 pass the research-content checks. Both generated mechanical packages pass their coverage and methodology checks. Final acceptance remains conditional on the build, hash, validator, and exact-once input-assembly tests succeeding for each round.
