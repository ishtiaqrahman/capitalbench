# Model Behavior Patterns

CapitalBench publishes a dynamic model behavior pattern report at `/models/patterns`.
The report compares model allocation behavior across official frozen portfolios and
resolved result rows.

## Source Of Truth

The report is generated during the web read-model build in
`apps/web/scripts/generate-api-read-model.mjs`.

The public object is:

```text
apiReadModel.model_behavior.pattern_report
```

The report is deterministic. Page copy must render from generated fields, not
hard-coded model narratives.

## Refresh Flow

1. New official portfolios or resolved scores are committed.
2. `npm run build` runs `scripts/generate-api-read-model.mjs`.
3. `model_behavior.profiles` is recalculated from public portfolios, assets, and
   result rows.
4. `model_behavior.pattern_report` is rebuilt from those profiles.
5. Validation fails the build if any active model is missing from the report.

The report updates automatically when a model changes behavior, a new model
joins, or a model has more resolved performance data.

## Metrics

- `risk_taking_score`: average allocation-weighted 0-100 risk appetite across
  saved portfolios.
- `average_holding_count`: average number of non-zero holdings.
- `average_top_allocation_pct`: average size of the largest holding in each
  saved portfolio.
- `high_risk_pct`: average allocation to assets rated higher risk by the
  CapitalBench asset risk model.
- `defensive_pct`: average allocation to cash, duration, defensive sectors, and
  lower-risk ballast.
- `tech_pct`: average allocation to technology, semiconductors, Nasdaq-style
  growth, and AI-linked technology exposure.
- `peer_similarity`: average cosine similarity to peer portfolios in matching
  official rounds.
- `average_turnover_pct`: one-half summed absolute allocation change between
  consecutive same-track portfolios.
- `average_rank`: average resolved-round finishing rank. Lower is better.
- `average_capitalbench_score`: average oracle-scaled CapitalBench Score across
  resolved rounds.

## Behavior Labels

The generator assigns traits before any LLM wording is used.

- `highest_risk`: model has the highest average risk-taking score.
- `most_concentrated`: model has the highest concentration metric.
- `most_defensive`: model has the highest defensive allocation.
- `lowest_turnover`: model has the smallest measured turnover.
- `most_consensus_aligned`: model has the highest average peer overlap.
- `most_distinctive`: model has the lowest average peer overlap.
- `technology_tilt`, `international_tilt`, `real_assets_tilt`: exposure
  thresholds show a repeated allocation tilt.
- `binary_results`: at least two first-place finishes and at least two last-place
  finishes.
- `middle_stable`: at least five resolved rounds with no first-place or
  last-place finishes.
- `early_sample`: fewer than eight official saved portfolios.

## NVIDIA LLM Contract

The NVIDIA model is not the source of truth. It may only rewrite summaries from
the structured report.

The generated prompt packet is:

```text
apiReadModel.model_behavior.pattern_report.llm_input_contract
```

Prompt version:

```text
capitalbench_model_patterns_prompt_v1
```

The packet includes model IDs, deterministic summaries, traits, metric keys, top
assets, sample caveats, and comparative candidates.

The LLM must not:

- introduce unsupported numbers
- introduce unsupported assets or tickers
- add stale dates
- infer market causes not present in the packet
- make investment recommendations
- remove early-sample caveats

If an LLM rewrite fails validation, the deterministic summary remains publishable.

## Validation

`apps/web/scripts/validate-public-data.mjs` checks the generated data shape.
`apps/web/scripts/validate-rendered-data.mjs` checks that `/models/patterns`
renders the generated rows, summaries, key numbers, top assets, findings, and
methodology.
