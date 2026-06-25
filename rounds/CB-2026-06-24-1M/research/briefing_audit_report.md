# Prompt 2 - Briefing Audit Report

Research cutoff: 2026-06-24T21:20:00Z

## Scope

This audit checks the June 24, 2026 CapitalBench input package for:

| check | status |
| --- | --- |
| fresh post-close market snapshot | pass |
| source URLs kept out of model-facing final briefing | pass |
| no recommendation, ranking, subjective analysis, or option-mapping language in final briefing | pass |
| weekly and monthly horizons explicit | pass |
| no Fable 5 in run configs | pass |
| prohibited S&P 500 allocation instruction absent | pass |
| full-universe price/risk context generated | pass |
| full-universe entry prices present | pass |
| provider key presence through CLI loader | pass |

## Staleness And Reconciliation Notes

The research package uses the Wednesday, June 24 U.S. close because that was the latest closed U.S. trading session available at runtime. The model decision deadline is June 25 at 02:30 UTC.

The AP June 24 index-close source supplied the closing values: S&P 500 7,358.22, Dow 51,848.90, Nasdaq Composite 25,476.64, and Russell 2000 2,986.63. The final briefing uses those values.

The Federal Reserve H.15 release dated June 24 contained June 23 observations for the selected Treasury and money-market rates. The final briefing labels those observation dates rather than implying June 24 H.15 observations. AP's market narrative supplies June 24 closing-market yield levels for the 10-year and 2-year Treasury notes.

Micron published its fiscal Q3 release at 4:01 p.m. EDT on June 24, before the 21:20 UTC research cutoff, so the final briefing treats those company facts as available. The briefing labels Micron's fiscal Q4 guidance as guidance.

The direct full-universe entry-price command returned HTTP 429. The full-universe price-context command had already generated a complete 70-option June 24 `as_of_adj_close` table with no failed options, so `prices/entry_prices.csv` was generated from that frozen table for each round and labeled `universe_trailing_returns_adjclose`.

## Prompt/Input Checks

The June 24 prompts were initialized from the current project prompt generator. Both prompts include horizon-specific language, price-history discipline, and the rule that models may not browse, use tools, request updated market data, use external retrieval, or intentionally rely on post-cutoff facts.

The phrase from the previously prohibited S&P 500 allocation instruction is absent from both June 24 prompt files and both June 24 briefing files. The prompt still identifies the S&P 500 as the scoring benchmark, because benchmark identity is part of the round definition and scoring metadata.

## No-Fable Check

The June 24 official configs were copied from the June 23 no-Fable configs and saved under a June 24 run identifier. Active model IDs:

| provider | model_id |
| --- | --- |
| openai | openai-gpt-5-5 |
| anthropic | anthropic-claude-opus-4-7 |
| anthropic | anthropic-claude-opus-4-8 |
| google | google-gemini-3-1-pro |
| xai | xai-grok-4-3 |

No config entry contains `fable` or `anthropic-claude-fable-5`.

## Generated Data Artifacts

CapitalBench generated or derived the following local data before final briefing import:

| artifact | weekly path | monthly path | status |
| --- | --- | --- | --- |
| full-universe price/risk CSV | rounds/CB-2026-06-24-1W/market_data/universe_trailing_returns.csv | rounds/CB-2026-06-24-1M/market_data/universe_trailing_returns.csv | 70 options, no failures |
| full-universe price/risk markdown | rounds/CB-2026-06-24-1W/market_data/universe_trailing_returns.md | rounds/CB-2026-06-24-1M/market_data/universe_trailing_returns.md | generated |
| full-universe price/risk JSON | rounds/CB-2026-06-24-1W/market_data/universe_trailing_returns.json | rounds/CB-2026-06-24-1M/market_data/universe_trailing_returns.json | generated |
| full-universe entry prices | rounds/CB-2026-06-24-1W/prices/entry_prices.csv | rounds/CB-2026-06-24-1M/prices/entry_prices.csv | 70 options, derived from frozen universe table |
| no-Fable model config | rounds/CB-2026-06-24-1W/configs/models.official-20260624-no-fable.yaml | rounds/CB-2026-06-24-1M/configs/models.official-20260624-no-fable.yaml | generated |

## Final-Briefing Bias Controls

The final model-facing briefing:

- states that inclusion, order, grouping, and row count are not signals;
- presents facts in publisher/date/value tables;
- includes both weekly and monthly scoring dates in the setup table;
- labels source-reported forecasts and scheduled events;
- avoids source URLs, citations, and recommendation phrases;
- avoids selected mechanical return rows;
- leaves the full 70-option price/risk appendix to the normal model-input appender.

The generated full-universe markdown appendix is sorted by option order, not by performance, and the model input builder is expected to append it exactly once after the briefing.

## Remaining Run Steps

Before official model calls:

1. Import the three research artifacts into both rounds.
2. Hash and audit both rounds.
3. Validate that the generated model input includes prompt, metadata, briefing, options, and the full-universe appendix.
4. Run `official-20260624-no-fable` for both horizons.
5. Validate submissions, accept runs, publish pending/interim state, sync, commit, push, and deploy.
