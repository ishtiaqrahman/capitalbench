# Portfolio V2 Improvement Research Protocol

Frozen on: `2026-07-17`

Status: frozen before the V2-improvement analysis was run. This protocol does
not modify, reinterpret, resolve, or publish the active July 13 Portfolio V2
pilot. Findings belong in `docs/v2_improvement_research_report.md`.

## Decision Objective

Identify the smallest defensible changes to CapitalBench Portfolio V2 that are
most likely to improve realized one-week and one-month portfolio return and
alpha versus the S&P 500, while preserving:

- one paid, single-turn, non-agentic call per participating model;
- the same complete allowed universe and scoring window for every model;
- cutoff-safe, reproducible model inputs;
- exact saved allocations with no after-the-fact optimization; and
- a benchmark that measures model decisions rather than a hidden trading
  algorithm.

The research does not optimize for explanation quality, exact-winner hits, or
historical fit except where those diagnostics explain prospective return.

## Frozen Samples

### Resolved diagnostic sample

Use the resolved V1 rounds admitted by
`docs/model_performance_predictability_protocol.md`. Weekly and monthly tracks
remain separate. Features must come from artifacts frozen before each round's
decision deadline. Realized returns are outcomes only.

### Active V2 structural sample

Use the frozen prompt, decision-context table, and four accepted submissions
from `CB-2026-07-13-V2-1W` only to inspect contract compliance, input use,
candidate overlap, concentration, and the size of the change from paired V1.
Do not use interim prices or unresolved returns. The frozen July 20 experiment
rule remains the only rule that may accept or reject that pilot.

Historical replay with current models may test parsing and instruction
compliance, but it may not be presented as return evidence because the models
could know subsequent outcomes.

## Failure Decomposition

For each resolved model-round observation, define:

- `U`: return of the best allowed noncash option;
- `S`: return of the best option included in the submitted portfolio;
- `P`: submitted portfolio return; and
- `B`: S&P 500 return.

Report:

- total oracle regret: `U - P`;
- search regret: `U - S`;
- sizing regret: `S - P`;
- portfolio alpha: `P - B`;
- selected-set equal-weight alpha;
- selected holdings and allocation weight that beat `B`; and
- selected-set capture of the realized top 1, top 3, and top 5 options.

Search and sizing regret are ex-post diagnostics, not implementable trading
rules. Their purpose is to identify which stage needs intervention.

## Predefined Hypotheses

1. **Candidate search:** V1 and V2 fail mainly because the selected set omits
   the assets that subsequently outperform, rather than because weights among
   good selected assets are slightly wrong.
2. **Input use:** A long, flat option table and narrative briefing encourage
   selective reading, catalyst anchoring, or row-position sensitivity rather
   than systematic comparison of all options.
3. **Relative hurdle:** Models can produce confident positive-alpha stories
   without a sufficiently demanding, auditable comparison against SPY.
4. **Forecast calibration:** Point forecasts and stated beat-SPY probabilities
   are too sparse and potentially overconfident to support allocation sizing.
5. **Correlated concentration:** Soft wording about correlation does not stop
   multiple holdings from expressing the same economic bet.
6. **Information architecture:** Additional data helps only when it is
   option-specific, complete across the universe, compact, and tied to the
   scoring horizon. Adding unstructured context can reduce decision quality.

## Predefined Historical Portfolio Tests

Apply these transformations to the saved V1 selected holdings without changing
the candidate set:

1. submitted weights;
2. equal weight across submitted holdings;
3. cap each holding at 50%, redirecting excess to SPY;
4. cap each holding at 35%, redirecting excess to SPY;
5. reserve 25% in SPY and scale submitted active weights to 75%; and
6. reserve 50% in SPY and scale submitted active weights to 50%.

These are diagnostics, not candidate V2.1 rules. A rule is not considered
predictive merely because blending a losing portfolio with SPY reduces its
underperformance.

## V1-to-V2 Structural Tests

For each of the four paired July 13 models, report:

- common holdings and holding-set Jaccard similarity;
- allocation turnover (`0.5 * sum(abs(V2 - V1))`);
- concentration by holding and by available metadata group;
- cross-model allocation overlap;
- forecast dispersion, arithmetic validity, and confidence dispersion;
- selected options' positions and mechanical feature percentiles; and
- explicit use of recent/prior windows, SPY-relative evidence, volatility,
  drawdown, volume, beta/correlation, catalysts, and invalidation conditions.

Keyword evidence is a conservative trace of explicit usage, not proof of the
model's internal reasoning.

## Input And Prompt Tests

The research may inspect table structure and create deterministic variants,
but must not make paid participant-model calls. Evaluate:

- input size and field density;
- option-order stability and selected-option positions;
- duplicated or weakly decision-relevant fields;
- whether every requested decision field is auditable;
- whether the prompt requires a full-universe shortlist;
- whether it establishes a hard relative hurdle before active allocation;
- whether correlated economic exposures can be detected from available data;
  and
- whether forecast fields are sufficient for later calibration.

## Additional-Data Evaluation

Rank proposed data families on five predefined dimensions: horizon relevance,
full-universe coverage, cutoff auditability, mechanical reproducibility, and
context cost. Assess scheduled catalysts, analyst revisions, valuation,
breadth/regime, positioning/flows, options-implied information, and explicit
economic-exposure mapping. No family is recommended for the model-facing input
without a complete source and coverage design.

## Evidence Standard

An intervention receives one of four ratings:

- `implement`: directly repairs an observed V2 contract failure at low cost and
  does not claim unproven alpha;
- `prospective_test`: plausible mechanism with sufficient diagnostic support,
  but return value must be tested prospectively;
- `instrument_first`: cannot be judged until V2 records more granular forecasts
  or candidates; or
- `reject`: historical evidence is unstable, redundant, too expensive, or
  likely to compromise benchmark fairness.

No intervention is called return-improving from a single round, an in-sample
winner story, or a result driven by one overlapping market episode.

## V2.1 Promotion Test

The final report may specify one combined V2.1 treatment, but it must be frozen
before a future scoring window and compared prospectively with V2 on the same
date, universe, models, and prices. Primary evidence is paired realized alpha.
One weekly observation is a screen, not an adoption decision. Confirmation
requires multiple non-overlapping weekly windows and later monthly validation.
