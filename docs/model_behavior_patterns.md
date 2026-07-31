# Model Behavior Patterns

CapitalBench publishes a dynamic model behavior pattern report at `/models/patterns`.
The report classifies allocation behavior across official frozen portfolios;
resolved performance is reported alongside it but does not assign behavior labels.

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

## Behavior Method V2

The public method version is `capitalbench_behavior_evidence_v2`. The generator
keeps a `shadow_v1` comparison so label changes can be audited, but every public
caption and pill is derived from the V2 evidence object.

For each model-round observation and behavior dimension, the generator uses a
leave-one-model-out peer baseline:

```text
peer-relative difference = model value - median value of the other models in the same round
```

A signal qualifies only when all three gates pass:

- at least 8 matched official portfolios
- at least 6 independent decision dates
- a dimension-specific materiality floor and the same directional difference
  in at least 65% of matched portfolios

Weekly and monthly samples are checked separately. Opposite material signals
produce a horizon-dependent confidence caveat. A reversal under the current
methodology produces an evolving-pattern caveat.

The strongest qualifying exposure or risk signal supplies the archetype
modifier. Signal strength is the absolute median peer difference divided by the
dimension's materiality floor, with persistence and then the stable metric key
as tie-breakers. Peer-normalized construction, turnover, or peer overlap
supplies the allocation-style noun. `Peer-balanced allocator` is used only when
no signal passes the gates; it is not a generic rule-ladder fallback.

Evidence becomes established only after 16 independent decision dates and 75%
directional persistence. Otherwise a qualifying profile remains moderate;
small samples, horizon conflicts, and sufficiently sampled current-method
reversals are explicitly marked provisional, horizon-dependent, or evolving.

Every model publishes four fixed-role pills from the same evidence record:

- Signature: persistent peer-relative risk or exposure
- Construction: average holdings and largest position
- Tempo: consecutive same-track turnover
- Now: current open positioning, `No open portfolio` when none exists, or a
  historical lifecycle note for retired models

## Evidence Tiers

- **Headline behavior:** eligible frozen allocations, asset-risk definitions,
  same-round peers, concentration, turnover, and lifecycle metadata.
- **Decision-process context:** structured candidate ledgers, forecasts,
  expected alpha, confidence, and key-risk counts where available. Coverage is
  displayed separately for each input family, but these fields do not override
  allocation evidence.
- **Performance:** resolved returns, ranks, S&P 500 comparisons, and market
  regime results remain separate from allocation-style classification.
- **Narrative:** free-form rationales may be displayed as model-authored context
  but never assign a label.

Ineligible, invalid, pilot, and retrospective runs are excluded by the public
official-run gate. Page-level superlatives use the active-model cohort; retired
models retain their historical profiles but cannot become a current “most” leader.

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

Labels use a small grammar instead of a mutually exclusive threshold ladder:

```text
[persistent signature modifier] + [construction style]
```

Examples include `Real-asset tactical allocator`, `Technology-focused
concentrator`, `Defensive diversified allocator`, and `Benchmark-anchored
allocator`. Models without enough independent evidence are labeled `Emerging
allocation profile`.

## NVIDIA LLM Contract

The NVIDIA model is not the source of truth. It may only rewrite summaries from
the structured report.

The generated prompt packet is:

```text
apiReadModel.model_behavior.pattern_report.llm_input_contract
```

Prompt version:

```text
capitalbench_model_patterns_prompt_v2
```

The packet includes model IDs, deterministic summaries, traits, fixed-role
pills, metric keys, top assets, sample caveats, and comparative candidates.

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
