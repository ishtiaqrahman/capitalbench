# Prompt 2 - Briefing Audit Report

Research cutoff: 2026-06-23T01:28:00Z

## Scope

This audit checks the June 22, 2026 CapitalBench input package for:

| check | status |
| --- | --- |
| fresh post-close market snapshot | pass |
| source URLs kept out of model-facing final briefing | pass |
| no recommendation, ranking, or option-mapping language in final briefing | pass |
| weekly and monthly horizons explicit | pass |
| no Fable 5 in run configs | pass |
| full-universe trailing returns generated | pass |
| full-universe entry prices generated | pass |
| mechanical source labels accurate after Tiingo 429 | pass |
| provider key presence through CLI loader | pass |

## Staleness And Reconciliation Notes

The research package uses the Monday, June 22 U.S. close because that was the latest closed U.S. trading session available at runtime. The model decision deadline is June 23 at 02:30 UTC. A June 23 U.S. market close did not exist at runtime and was not used.

The AP June 22 index-close article and AP market narrative agree on the closing values: S&P 500 7,472.79, Dow 51,712.71, Nasdaq Composite 26,166.60. The final briefing uses those values.

The Federal Reserve H.15 current release was dated June 22, but it contained market-yield observations through June 18 because June 19 was a market holiday. The final briefing labels the observation dates accordingly rather than implying June 22 Treasury market observations.

Tiingo returned HTTP 429 during full-universe artifact generation. The project fallback path generated complete Yahoo chart adjusted-close files. The price and market-data files were source-labeled as `yahoo_chart_adjclose` after generation.

## Prompt/Input Changes Applied

The June 22 prompts preserve the June 18 guardrails:

1. The S&P 500 benchmark asset is explicitly framed as an allowed holding when expected active edge is weak.
2. Models are instructed to privately compare continuation, mean-reversion, risk-off, and benchmark-asset cases before returning JSON.

These changes are scoped to the June 22 rounds and do not change scoring, constraints, option universe, or output schema.

## No-Fable Check

The June 22 official configs were copied from the prior no-Fable configs and rechecked with text search. Active model IDs:

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
| full-universe trailing returns CSV | rounds/CB-2026-06-22-1W/market_data/universe_trailing_returns.csv | rounds/CB-2026-06-22-1M/market_data/universe_trailing_returns.csv | 70 options, no failures |
| full-universe trailing returns markdown | rounds/CB-2026-06-22-1W/market_data/universe_trailing_returns.md | rounds/CB-2026-06-22-1M/market_data/universe_trailing_returns.md | generated |
| full-universe entry prices | rounds/CB-2026-06-22-1W/prices/entry_prices.csv | rounds/CB-2026-06-22-1M/prices/entry_prices.csv | generated |
| no-Fable model config | rounds/CB-2026-06-22-1W/configs/models.official-20260622-no-fable.yaml | rounds/CB-2026-06-22-1M/configs/models.official-20260622-no-fable.yaml | generated |

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
4. Run `official-20260622-no-fable` for both horizons.
5. Validate submissions, accept runs, publish pending/interim state, sync, commit, push, and deploy.
