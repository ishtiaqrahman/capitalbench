# Model-Quality Hybrid Screen

## Question

Can the frozen weekly quality-pullback signal improve the portfolios that the
models actually submitted, without buying additional model calls?

## Frozen Inputs

The experiment reconstructs every eligible official historical model
allocation admitted by the canonical predictability audit. Realized option
returns come from the matching resolved run. Quality scores come from the
cutoff-safe price-feature panel frozen in
`historical-decision-context-backfill-2026-07-21`.

The quality score remains unchanged: 45% prior active-return rank, 30% reverse
recent active-return rank, 15% low-volatility rank, and 10% shallow-drawdown
rank. Weekly results are gated. Monthly results are diagnostic only.

## Frozen Transformations

1. **25% quality sleeve:** retain 75% of the original model allocation and add
   25% of the equal-weight quality top five.
2. **Conviction-quality union:** take the union of original model holdings and
   the quality top five, combine within-round model-conviction rank and quality
   rank at 50% each, and equal-weight the best five.
3. **Within-holdings quality tilt:** multiply each original non-cash weight by
   `0.50 + quality_rank`, leave cash neutral, and renormalize. This changes
   weighting but cannot add a candidate.

The unchanged model portfolio and standalone quality top five are controls.

## Frozen Gate

A weekly hybrid advances to a bounded private prompt replay only if it:

- improves mean return by at least 0.75 percentage points;
- has positive resulting alpha versus SPY;
- improves more than 60% of model-round pairs;
- has positive mean improvement for more than 60% of represented models;
- remains positive in the chronological holdout;
- remains positive on at least six greedily selected non-overlapping rounds;
- and remains positive after the single best round is removed.

The primary unit is the model-round pair, but non-overlap and leave-best-out
calculations first aggregate by round so a round with more model submissions
cannot dominate robustness checks.

## Attribution

The report must show results by model, SPY-up versus SPY-down environment,
model-quality overlap, and transformation. It must distinguish candidate
addition from within-portfolio reweighting. These diagnostics may explain a
result but cannot change the frozen gate.

Historical reuse can reject a weak hybrid but cannot confirm prospective
skill. A pass authorizes only the separately frozen bounded replay described
in the registry, not a production change.
