# Portfolio V3.0 Candidate Methodology

Status: **historical development specification; adopted unchanged as the
forward production default by explicit operator direction on August 15, 2026**

The frozen holdout validity gate later failed at 8 valid cells versus 10
required. Preserve that result as a failed gate. The separate operator adoption
and current production contract are documented in
`docs/portfolio_v3_methodology.md`.

Portfolio V3.0 is a deliberately small change to the rejected V3A replay. It
keeps the balanced candidate search that found the eventual winner in all three
development weeks, but it no longer forces the model's three highest-ranked
ideas into the portfolio.

## Objective

Produce positive one-week portfolio alpha versus SPY while preserving the
single-turn, non-agentic CapitalBench protocol. The participant model receives
no tools, browsing, retrieval, follow-up, or outcome information.

## Model Input

The model receives the same cutoff-safe inputs used by V3A:

1. The frozen factual briefing available at the decision cutoff.
2. A deterministic candidate slate containing shock-reversal, medium-strength,
   short-continuation, quality-pullback, and volume-dislocation candidates plus
   SPY.
3. The complete allowed universe for at most two model-added wildcards.
4. Price, volatility, drawdown, volume, beta, correlation, and quality fields
   available before the entry close.

The slate is a search aid, not a recommendation.

## Required Model Output

In one response, the model ranks every assessed candidate and reports:

- probability of beating SPY;
- probability of finishing in the realized top three;
- p10, p50, and p90 excess-return estimates;
- a recent-return interpretation of `overreaction`,
  `supported_continuation`, `fundamental_deterioration`, or `no_edge`; and
- a short evidence list.

The model does not construct the final portfolio. That step is deterministic.

## Deterministic Portfolio Rule

1. Sort candidates by the model's original rank.
2. A non-SPY candidate is eligible only when:
   - the model labels it `overreaction`; and
   - its estimated probability of beating SPY is at least 55%.
3. Select at most the first three eligible candidates without reranking them.
4. Fill the fixed 35%, 35%, and 30% slots in order.
5. Put every unused slot in SPY.

Examples:

- Three eligible candidates: 35% / 35% / 30% active.
- Two eligible candidates: 35% / 35% active and 30% SPY.
- One eligible candidate: 35% active and 65% SPY.
- No eligible candidates: 100% SPY.

The implementation is `capitalbench.portfolio_v3.build_portfolio_v3_allocation`.
It validates unique option IDs and ranks, the probability range, slot weights,
and the final 100% allocation.

## Why Continuation Is Excluded

Across the eleven valid V3A model-period responses, a 55% probability hurdle by
itself averaged -0.12% versus SPY. Confident continuation alone averaged
-1.16%, and combining confident continuation with overreaction also averaged
-0.12%. The positive result came from the overreaction classification, not from
confidence alone.

V3.0 therefore excludes continuation instead of adding an unvalidated evidence
exception. A future experiment may test continuation separately, but it must
not be silently added to this candidate.

## Historical Development Result

Applying the fixed rule to the eleven valid saved V3A responses produced:

- +1.04% mean alpha versus SPY;
- +2.66 percentage points versus paired V2.2 controls;
- 4 strict SPY beats and 9 nonnegative cells out of 11;
- positive mean alpha for 3 of 4 model families;
- positive mean alpha in 2 of 3 periods; and
- a weakest-period mean of -0.04% versus SPY.

The result stayed positive after removing any one model (+0.39% minimum), any
one period (+0.73% minimum), or any one cell (+0.67% minimum). Every tested
probability hurdle from 45% through 67.5% also remained above SPY. The 55%
hurdle is retained because it was already fixed before the Gemini responses;
selecting the best-looking threshold now would be outcome tuning.

## Evidence Boundary

These are development results, not an accepted validation:

- the rule was developed after outcomes from the three historical weeks were
  available;
- the sample contains only three periods and eleven valid cells;
- five cells used a full SPY fallback, so nonnegative breadth partly reflects
  deliberate abstention; and
- one OpenAI cell remains unavailable because of provider credits.

The July 21, July 28, and August 4 windows cannot be reused as confirmation.
At the time of this development report, Portfolio V2.2 remained production.
Portfolio V3.0 later became the forward default by separate operator decision.

## Next Evidence Gate

If a new call budget is later authorized, freeze this exact rule before the
first fresh weekly outcome exists. Use the first three eligible non-overlapping
weekly rounds without choosing favorable market conditions. At minimum, require:

- at least 10 valid paired cells;
- positive mean alpha versus SPY;
- at least 1.00 percentage point improvement over paired V2.2;
- at least 8 nonnegative cells;
- positive mean alpha for at least 3 model families;
- positive mean alpha in at least 2 of 3 periods;
- weakest-period mean alpha no worse than -0.50%; and
- selected top-three capture no worse than paired V2.2.

Passing that small prospective gate would permit a larger private shadow. It
would not automatically change production or official benchmark results.
