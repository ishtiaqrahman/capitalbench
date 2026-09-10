# Briefing audit — September 10, 2026

Audit-only artifact. Research cutoff: 2026-09-10T04:05:00Z. Applies to CB-2026-09-10-1W and CB-2026-09-10-1M. The same new public-source factual digest is used with separately generated horizon-specific mechanical context.

## Research checks

- The final briefing has eight broad sections with two factual bullets each. Dates and status labels distinguish older monthly releases, new September 9 data, completed-market observations, forecasts and future calendar events.
- No URLs, citation tokens, source ledger, recommendations, subjective scenarios, affected-option mapping, allocations, selected mechanical return table, quality scores/ranks, or candidate-slate rows appear in the final briefing.
- The required neutrality sentence appears near the top and descriptive-history language at the end. Publisher attribution is retained without source links.
- AP closes and Reuters breadth/quotes are kept distinct. EIA September forecasts retain their September 3 input cutoff and conditional assumptions. China original-language extraction and direct-open limitations are disclosed in the source report. Publication-date uncertainty in undated calendars is explicit.
- September 10 scheduled events occur after the research cutoff and before the future entry close. No outcome information for those events is claimed. The monthly exit rolls Saturday October 10 to Monday October 12, an NYSE equity session.
- The report was freshly authored from direct public browsing. No research-provider API or participating model was used to gather, rank, or synthesize facts. Mechanical pricing API use is separate and allowed.

## Mechanical package checks

- The existing pipeline fetched fresh native Tiingo histories for all 69 traded tickers, with 297 observations each ending September 9; CASH is a deterministic option. No post-cutoff market data or outcome data enters the package.
- Both generated full-universe context artifacts cover all 70 included options in frozen option order, with horizon-specific price/volume, SPY-relative, risk, drawdown, path-quality, 52-week-position and beta/correlation diagnostics.
- Both quality artifacts cover all 68 active non-SPY, non-CASH options (100%, above the 90% requirement), using the existing frozen 45/30/15/10 formula. No Q2 quota is added.
- The unchanged V3 builder generates the candidate slate from the five fixed lanes plus SPY and injects it separately; the research report does not generate or edit its rows. Static exposure clusters remain pipeline-owned.
- Pre-call input integrity is checked after import: complete context, quality table and candidate slate each appear exactly once; quality precedes the briefing; option order and cutoff-safe history are preserved; audit artifacts are not model-facing. Machine-readable results are saved as research/input_integrity.json before hashing and model calls.
- Round manifests freeze Portfolio V3.0, the seven active model IDs, September 10 entry, September 17 weekly exit and October 12 monthly exit. One tool-free, single-turn official decision per model is required; only disclosed technical retries are permitted.
