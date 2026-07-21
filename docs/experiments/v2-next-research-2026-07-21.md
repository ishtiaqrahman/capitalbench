# V2 Next Research Program

Frozen on: `2026-07-21`

Status: waiting for the July 17 weekly round to resolve after the July 24
close. This experiment does not change the production Portfolio V2.0 prompt,
inputs, model roster, scoring, or publication rules. No paid challenger call
is authorized by this document.

## Purpose

Determine whether Portfolio V2.0 primarily loses available return during
candidate search, candidate ranking, or portfolio construction. Only after
that diagnosis may one materially different prospective hypothesis be built.

Earlier CapitalBench research established that:

- V1 underperformed SPY on average;
- historical oracle regret was mostly search regret;
- instruction-only and cross-sectional prompt changes did not pass replay;
- balanced candidate lanes improved top-two shortlist recall but not return;
- a probability reranker improved one historical period but failed breadth;
- four fixed price-only candidate strategies failed their advancement gates.

The next research therefore begins with already-paid prospective V2 decisions,
not another retrospective model replay.

## Frozen Evidence

### July 13 Paired Pilot

The V2 pilot and its paired V1 control share the same universe, entry date,
exit date, research cutoff, and four precommitted models. They must use one
shared full-universe entry/exit price snapshot. The original acceptance rule in
`experiments/portfolio-v2-2026-07-13.yaml` remains authoritative.

### July 17 Complete V2 Round

The eight-model production round exits after the July 24 close. Its frozen
inputs and submissions are included in the pre-outcome freeze, but it must not
be resolved or analyzed before it is due.

The July 13 and July 17 windows overlap. They are diagnostic observations, not
independent confirmations.

## July 13 Execution Record

The paired pilot was resolved from one shared 70-option adjusted-close price
snapshot. Its frozen acceptance decision was **rejected**: mean V2 alpha was
3.34% versus 5.46% for V1, mean paired improvement was -2.13 percentage
points, and 0 of 4 models improved.

The legacy pilot did not retain candidate ledgers, so search and ranking
regret cannot be separated without hindsight reconstruction. The selected
portfolios captured one realized top-three asset per model on average, and
measurable construction regret represented 86.92% of total oracle regret. The
frozen branch rule therefore authorized weight-only counterfactuals.

Those no-call tests did not improve the aggregate result: equal weighting
reduced mean return by 0.22 percentage points, a 50% holding cap redirected to
SPY reduced it by 0.08 points, and a 35% cap reduced it by 0.28 points. No cap
improved any model. No production change, event table, or paid challenger is
authorized from this result.

The next gate is the July 17 production weekly round after the July 24 close.
That round contains the complete candidate ledgers required to distinguish
search, ranking, and construction losses prospectively.

## Loss Decomposition

For every V2 model decision, calculate:

1. `search_regret`: best allowed return minus best candidate-ledger return.
2. `ranking_regret`: best candidate-ledger return minus best selected-holding return.
3. `construction_regret`: best selected-holding return minus realized portfolio return.

The three components must sum to total oracle regret. A stage is called
dominant only when its aggregate share is greater than 50%.

Also report candidate winner/top-three recall, selected and rejected candidate
returns, forecast rank correlation, forecast absolute error, low/high interval
coverage, SPY-hurdle precision, rejected opportunities, candidate overlap, and
paired V1/V2 portfolio performance where a control exists.

## Branch Rule

| Diagnostic | Authorized next design work |
| --- | --- |
| Search regret dominates | Build and audit a neutral option-linked event table |
| Ranking regret dominates | Test event-supported ordinal comparison, not another probability prompt |
| Construction regret dominates | Test equal-weight and capped counterfactuals without model calls |
| No stage dominates | Collect more resolved V2 observations; do not spend |

This rule selects design work only. It does not authorize real model calls.

## Structured Event Hypothesis

If search or ranking dominates, test whether facts already present in the
research become more useful when represented as a complete option-linked event
table. The table may include event date, category, factual description,
affected static exposure clusters, mechanically mapped options, directness,
resolution status, and audit fact ID.

The table must not include sentiment, expected direction, recommendations,
scores, rankings, or manually selected winners. Every option must be mapped or
explicitly marked as having no direct in-window event. It must replace
redundant narrative rather than increase model input by more than 5%.

## Cost Gate

- No model call before both the loss diagnosis and a deterministic event-table
  dry run pass.
- A future first-stage shadow may use only GPT-5.6 SOL, Grok 4.5, and Gemini
  3.1 Pro: three incremental calls per non-overlapping weekly round.
- No Anthropic challenger and no monthly challenger.
- Stop after two rounds unless paired return and search diagnostics improve.
- Hard cap: 12 incremental calls before new operator approval.
- Only a transport failure before inference may be retried.

## Qualification Gate

After four non-overlapping weekly periods, a future event-structured treatment
may qualify for a separately approved all-roster confirmation only if:

- mean challenger alpha versus SPY is positive;
- mean paired improvement over unchanged V2.0 is at least 0.50 percentage points;
- at least 7 of 12 model-period comparisons improve;
- improvement occurs in at least three periods and all three model families;
- candidate search regret falls at least 20%;
- top-three candidate capture improves; and
- concentration, validity, cutoff, and leakage checks pass.

## Commands

```bash
python scripts/analyze_v2_resolution_diagnostics.py prepare
python scripts/analyze_v2_resolution_diagnostics.py fetch-shared-prices --pair july13_pilot
capitalbench automation-resolve --rounds-dir rounds --round-id CB-2026-07-13-1W --run-id official-20260713 --skip-fetch-prices --no-sync
capitalbench automation-resolve --rounds-dir rounds --round-id CB-2026-07-13-V2-1W --run-id official-v2-20260713 --skip-fetch-prices --no-sync
capitalbench evaluate-experiment --config experiments/portfolio-v2-2026-07-13.yaml --rounds-dir rounds
python scripts/analyze_v2_resolution_diagnostics.py analyze --pair july13_pilot
```
