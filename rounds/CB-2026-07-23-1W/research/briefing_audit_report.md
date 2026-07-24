# CapitalBench Briefing Audit — July 23, 2026 Close

## Audit scope

- Research cutoff checked: 2026-07-24 03:06:13 UTC.
- Outputs checked: the new `market_fact_report.md` and `final_briefing.md`.
- Generated inputs checked: the weekly and monthly `universe_decision_context` and `universe_quality_evidence` artifacts for the July 23 rounds.
- Frozen option files checked: the weekly and monthly option universes are byte-identical and contain 70 options.

## Prompt 1 checks

Pass:

- The fact report identifies its cutoff, decision date, and both scoring windows.
- Every factual section supplies publisher, publication date or status date, observation date, URL, and relevant limitations.
- The report covers current U.S. macro data, policy rates, July 23 index closes, exchange and sector breadth, energy and Treasury observations, cross-market closes, a same-day company release, and official calendar events inside each scoring window.
- Scheduled events are labeled as scheduled and are separated from completed releases.
- No event or fact first published after the cutoff is included.
- No allocation recommendation, option ranking, expected-return claim, or affected-option mapping appears.
- No manually selected subset of mechanical return rows appears.
- No Q1 rank, score, selected Q1 row, or Q1 summary appears.
- Mechanical context is referred to only by its complete generated artifact.

## Prompt 3 checks

Pass:

- The final briefing contains no URL, hyperlink, footnote citation, or source ledger.
- Publishers, dates, values, completed-versus-scheduled status, and source-reported uncertainty are retained as factual text.
- The required neutrality sentence appears near the top.
- The briefing contains no allocation recommendation, option ranking, expected-return conclusion, subjective commentary, or affected-asset mapping.
- The briefing contains no manually selected mechanical return section or subset.
- The briefing contains no Q1 rank, evidence score, selected Q1 row, or Q1 table summary.
- The briefing does not relabel, merge, rank, or characterize the deterministic economic-exposure clusters.
- The weekly calendar stops at the July 30 close. Amazon's July 30 after-close call is explicitly identified as occurring after that scoring close.
- The monthly calendar stops at the August 21 close.

## Mechanical full-universe context checks

Pass for both horizons:

- `market_data/universe_decision_context.md` exists.
- Each JSON artifact contains all 70 frozen options and reports no failed option.
- Each Markdown table is sorted in frozen option order, not by return.
- The generated fields include horizon-specific return, benchmark-relative return, volatility, maximum drawdown, volume context, SPY beta and correlation, 52-week-high distance, and deterministic economic-exposure cluster.
- The generated text explicitly says the history is descriptive context and not a forecast.
- The weekly artifact uses the weekly profile and the monthly artifact uses the monthly profile.
- No separate hand-selected price table is present in either research output.

## Portfolio V2.2 Q1 evidence checks

Pass for both horizons:

- `market_data/universe_quality_evidence.md` exists.
- Each artifact covers 68 of 68 eligible active options, or 100%, above the 90% minimum.
- CASH and the SP500 benchmark are excluded by the frozen methodology; there is no discretionary omission.
- The stated formula is frozen at 45% prior active rank, 30% recent active pullback rank, 15% low-volatility rank, and 10% shallow-drawdown rank.
- The table is complete and in option order.
- No Q2-style selection quota or reduced candidate universe is applied.
- The final briefing neither repeats nor paraphrases the evidence rows.

## Prompt-package construction checks

Pass:

- The deterministic prompt builder is the only component that appends the complete quality-evidence table and full-universe decision context.
- The builder renders the frozen option table with deterministic economic-exposure clusters.
- The final briefing announces that a complete mechanical appendix follows and states no forecast claim for historical price data.
- The prompt-package verification requires exactly one `Complete Option-Level Quality Evidence` heading and exactly one `Full-Universe Horizon-Specific Decision Context` heading for each round.
- Participant browsing and search remain disabled; all participants receive the same hashed package in one turn.

## Result

The July 23 research package passes the Prompt 1, Prompt 2, and Prompt 3 content controls for both Portfolio V2.2 horizons. Final acceptance remains conditional on import validation, one-copy prompt assembly, round hashing, submission validation, and official-run checks.
