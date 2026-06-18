# Prompt 2 - Briefing Audit Report

Research cutoff: 2026-06-18T22:05:22Z

## Scope

This audit checks the June 18, 2026 CapitalBench input package for:

| check | status |
| --- | --- |
| fresh post-close market snapshot | pass |
| stale June 17 market close data removed | pass |
| no Fable 5 in run configs | pass |
| weekly and monthly horizons explicit | pass |
| final briefing avoids source links and recommendation language | pass, pending import validation |
| full-universe trailing returns generated | pass |
| full-universe entry prices generated | pass |
| provider key presence through CLI loader | pass |

## Staleness And Reconciliation Notes

The working notes contained a stale June 18 stock-index snapshot that matched a down-market close. Re-browsing AP News showed the actual June 18 close was higher: S&P 500 7,500.58, Dow 51,564.70, Nasdaq 26,517.93, Russell 2000 2,979.77. The final briefing uses the AP June 18 close and does not use the stale values.

The working notes also carried an outdated Philadelphia Fed summary with negative general activity. The official June 2026 MBOS page showed general activity at 10.3, new orders at 27.3, shipments at 14.9, prices paid at 53.2, and prices received at 20.3. The final briefing uses those official values.

The Federal Reserve H.15 table was updated to the June 18 release with observations through June 17. The final briefing uses June 17 rates rather than the June 16 values in the prior round.

## Prompt/Input Changes Applied

The new round prompts add two input-side guardrails derived from the prior performance audit:

1. The S&P 500 benchmark asset is explicitly framed as an allowed holding when expected active edge is weak.
2. Models are instructed to privately compare continuation, mean-reversion, risk-off, and benchmark-asset cases before returning JSON.

These changes are scoped to the new June 18 rounds and do not change scoring, constraints, option universe, or output schema.

## No-Fable Check

The June 18 official configs were copied from the prior no-Fable configs and rechecked with text search. Active model IDs:

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
| full-universe trailing returns CSV | rounds/CB-2026-06-18-1W/market_data/universe_trailing_returns.csv | rounds/CB-2026-06-18-1M/market_data/universe_trailing_returns.csv | 70 options, no failures |
| full-universe trailing returns markdown | rounds/CB-2026-06-18-1W/market_data/universe_trailing_returns.md | rounds/CB-2026-06-18-1M/market_data/universe_trailing_returns.md | generated |
| full-universe entry prices | rounds/CB-2026-06-18-1W/prices/entry_prices.csv | rounds/CB-2026-06-18-1M/prices/entry_prices.csv | generated |
| no-Fable model config | rounds/CB-2026-06-18-1W/configs/models.official-20260618-no-fable.yaml | rounds/CB-2026-06-18-1M/configs/models.official-20260618-no-fable.yaml | generated |

## Final-Briefing Bias Controls

The final model-facing briefing:

- states that inclusion, order, grouping, and row count are not signals;
- presents facts in publisher/date/value tables;
- includes both weekly and monthly scoring dates in the setup table;
- limits scheduled events to the scoring windows;
- avoids source URLs, citations, and recommendation phrases;
- leaves the full 70-option trailing-return table to the normal model-input appender.

## Remaining Run Steps

Before official model calls:

1. Import the three research artifacts into both rounds.
2. Hash and audit both rounds.
3. Validate that the generated model input includes the prompt, metadata, briefing, options, and trailing-return table.
4. Run `official-20260618-no-fable` for both horizons.
5. Validate submissions, accept runs, sync/publish, and deploy.
