# CapitalBench briefing audit — September 9, 2026

Audit-only Codex review of the newly authored research for weekly and monthly V3 rounds. This is a source and protocol review, not an independent second model call.

## Research review

- Public sources were searched, opened, and reviewed directly; no provider/model API or provider-hosted search generated this research. Prior round briefing content was not reused.
- The ledger preserves publishers, URLs, publication dates where displayed, observation periods, uncertainty, and the cutoff 2026-09-09T05:56:16Z. Undated calendars are described as observed by cutoff. All future events are schedules only.
- BLS employment and CPI, BEA GDP and PCE, Fed/ECB decisions, ISM surveys, China's NBS release, Eurostat flash inflation, and EIA highlights were directly reviewed. AP supplies index closes; Reuters supplies timed cross-asset quotes; Investing.com breadth is identified as publisher-reported, not independently exchange-certified.
- GDP growth is annualized; monthly and annual inflation differ; preliminary releases and revisions remain labeled. Reuters commodity quotes are not mislabeled settlements. Suspect single-stock moves and changing page widgets are excluded.

## Neutrality and salience review

- The final briefing contains no URLs, source ledger, bracketed citations, option rankings, allocation instructions, subjective scenarios, or affected-option mapping. Publishers appear in prose.
- Seven factual areas each contain two items. Opposing observations remain together: GDP versus private domestic sales; payroll improvement versus participation decline; monthly versus annual energy CPI; services headline versus employment; China's headline versus components; euro-area headline versus core; crude stock draw versus lower product supplied.
- No selected mechanical return rows or quality/slate scores are reproduced or summarized in the final briefing or market fact report. The public news index closes are not a handpicked excerpt of the mechanical ETF table.
- The required neutrality sentence is present near the top, and the final statement preserves the descriptive-only contract.

## Mechanical input review

Mechanical generation and final assembly checks are recorded in each round's input-integrity artifact before paid collection. Required gates: complete 70-option frozen universe; all 69 traded instruments validated; all price observations at or before September 8; complete option-order decision context and quality table; at least 90% active-option quality coverage; unchanged 45/30/15/10 formula; deterministic five-lane slate including SPY; exactly one copy of each mechanical section; no audit-only research in the model prompt. Any actual pricing fallback must be disclosed in the integrity artifact.

Actual acquisition: one Tiingo validation passed all 69 traded tickers over August 1, 2025 through September 8, 2026. Both rounds have byte-identical option files, so that successful report is shared. A redundant monthly validation subsequently hit Tiingo's hourly quota and reported 11 failures; these were request failures, not a universe change. No option was removed. The initial weekly context completed with mixed Tiingo/Yahoo sources. Before any participant call, both contexts were regenerated from one freshly retrieved Yahoo history package through CapitalBench's existing fallback and context functions. Every traded symbol has 296 daily observations ending September 8. Both quality tables cover 68/68 active non-SPY, non-cash options (100%). Acquisition provenance is recorded separately; complete histories and generated context/quality files are frozen in round hashes.

## Prospective execution

Both rounds freeze the seven-model V3 roster at initialization. Research and mechanical inputs are frozen before real participant calls, with a September 9 13:25 UTC decision deadline. Entry is September 9 close, weekly exit September 16 close, monthly exit October 9 close. Entry prices are not yet available and must not be fabricated. The participant makes one tool-free judgment; the unchanged 35/35/30 overreaction-at-55% construction and SPY fallback determine its portfolio. Only technical/format failures permit disclosed retries. Valid decisions must not be retried for their investment content.
