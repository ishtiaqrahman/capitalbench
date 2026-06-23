# Prompt 2 - Briefing Audit Report

Research cutoff: 2026-06-23T21:20:00Z

## Scope

This audit checks the June 23, 2026 CapitalBench input package for:

| check | status |
| --- | --- |
| fresh post-close market snapshot | pass |
| source URLs kept out of model-facing final briefing | pass |
| no recommendation, ranking, or option-mapping language in final briefing | pass |
| weekly and monthly horizons explicit | pass |
| no Fable 5 in run configs | pass |
| prohibited S&P 500 allocation instruction absent | pass |
| full-universe trailing returns generated | pass |
| full-universe entry prices present | pass |
| provider key presence through CLI loader | pass |

## Staleness And Reconciliation Notes

The research package uses the Tuesday, June 23 U.S. close because that was the latest closed U.S. trading session available at runtime. The model decision deadline is June 24 at 02:30 UTC.

The AP June 23 index-close source supplied the closing values: S&P 500 7,365.46, Dow 51,666.84, Nasdaq Composite 25,587.04, and Russell 2000 2,975.48. The final briefing uses those values.

The Federal Reserve H.15 release dated June 23 contained June 22 observations for the selected Treasury and money-market rates. The final briefing labels those observation dates rather than implying June 23 rate observations.

The direct full-universe entry-price command returned HTTP 429. The full-universe trailing-return command had already generated a complete 70-option June 23 `as_of_adj_close` table for both horizons with no failed options, so `prices/entry_prices.csv` was generated from that frozen table for each round and labeled `universe_trailing_returns_adjclose`.

## Prompt/Input Changes Applied

The June 23 prompts were initialized from the current project prompt generator and checked for the previously prohibited S&P 500 allocation instruction. The phrase is absent from both June 23 prompt files and both June 23 briefing files.

The prompt still identifies the S&P 500 as the scoring benchmark, because benchmark identity is part of the round definition and scoring metadata. The removed line was the separate allocation instruction telling models when to allocate to the benchmark.

## No-Fable Check

The June 23 official configs were copied from the June 22 no-Fable configs and saved under a June 23 run identifier. Active model IDs:

| provider | model_id |
| --- | --- |
| openai | openai-gpt-5-5 |
| anthropic | anthropic-claude-opus-4-7 |
| anthropic | anthropic-claude-opus-4-8 |
| google | google-gemini-3-1-pro |
| xai | xai-grok-4-3 |

No config entry contains `fable` or `anthropic-claude-fable-5`.

## Generated Data Artifacts

CapitalBench generated the following local data before final briefing import:

| artifact | weekly path | monthly path | status |
| --- | --- | --- | --- |
| full-universe trailing returns CSV | rounds/CB-2026-06-23-1W/market_data/universe_trailing_returns.csv | rounds/CB-2026-06-23-1M/market_data/universe_trailing_returns.csv | 70 options, no failures |
| full-universe trailing returns markdown | rounds/CB-2026-06-23-1W/market_data/universe_trailing_returns.md | rounds/CB-2026-06-23-1M/market_data/universe_trailing_returns.md | generated |
| full-universe entry prices | rounds/CB-2026-06-23-1W/prices/entry_prices.csv | rounds/CB-2026-06-23-1M/prices/entry_prices.csv | 70 options, derived from frozen universe table |
| no-Fable model config | rounds/CB-2026-06-23-1W/configs/models.official-20260623-no-fable.yaml | rounds/CB-2026-06-23-1M/configs/models.official-20260623-no-fable.yaml | generated |

## Final-Briefing Bias Controls

The final model-facing briefing:

- states that inclusion, order, grouping, and row count are not signals;
- presents facts in publisher/date/value tables;
- includes both weekly and monthly scoring dates in the setup table;
- labels source-reported forecasts and scheduled events;
- avoids source URLs, citations, and recommendation phrases;
- leaves the full 70-option trailing-return table to the normal model-input appender.

## Remaining Run Steps

Before official model calls:

1. Import the three research artifacts into both rounds.
2. Hash and audit both rounds.
3. Validate that the generated model input includes prompt, metadata, briefing, options, and trailing-return table.
4. Run `official-20260623-no-fable` for both horizons.
5. Validate submissions, accept runs, publish pending/interim state, sync, commit, push, and deploy.
