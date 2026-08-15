# Portfolio V3 Confidence-and-Evidence Successor

> Historical note: this intermediate design is superseded by the simpler
> overreaction-only candidate in `docs/portfolio_v3_candidate_methodology.md`.
> Preserve this file as research history; do not use its continuation exception
> for a new run.

Status: **prospective design; not production and not historically validated**

This document freezes the strongest successor design learned from the rejected
V3A replay. It does not change V3A, Portfolio V2.2, or any official result.

## Purpose

Improve one-week portfolio alpha versus SPY without asking the model to guess
from all roughly 70 choices, blindly chasing recent winners, or forcing three
active bets when the model has no credible edge.

## What Stays From V3A

1. A deterministic, cutoff-safe slate supplies reversal, medium-strength,
   short-continuation, quality, and volume-dislocation candidates plus SPY.
2. The slate is a search aid, not a recommendation.
3. The model assesses the complete slate in one offline, non-agentic turn.
4. Tools, browsing, retrieval, follow-up, remembered outcomes, and facts after
   the cutoff are prohibited.
5. The model reports a rank, probability of beating SPY, probability of a
   top-three finish, and p10/p50/p90 excess-return estimates for each candidate.
6. Portfolio slot sizes remain 35%, 35%, and 30%.

## What Changes

### 1. Evidence facts receive stable identifiers

Every non-price fact in the frozen briefing receives an identifier such as
`F001`. Price-history rows and mechanical features receive separate identifiers
and cannot count as independent continuation support.

### 2. Every candidate receives an auditable thesis type

The model must classify each candidate as exactly one of:

- `overreaction`
- `supported_continuation`
- `fundamental_deterioration`
- `no_edge`

For `supported_continuation`, the response must list at least one
candidate-specific non-price fact identifier and explain in one sentence why
that fact can affect the exact one-week window. The validator must confirm that
every identifier exists in the frozen packet. Price return, volume, volatility,
drawdown, correlation, beta, or lane membership cannot satisfy this field.

### 3. Active allocations must clear an eligibility gate

An option is eligible for an active slot only when all conditions below hold:

1. The model estimates at least a 55% probability of beating SPY.
2. The thesis is `overreaction`; or it is `supported_continuation` with the
   auditable independent support described above.
3. The option is not labeled `fundamental_deterioration` or `no_edge`.
4. The option exists in the frozen allowed universe.

The 55% hurdle creates a margin above an uninformative 50/50 claim. It is not a
claim that model probabilities are perfectly calibrated.

### 4. SPY fills every unused slot

Preserve the model's original rank among eligible options. Fill the 35%, 35%,
and 30% slots in that order. If fewer than three active options qualify, put
each unused slot in SPY. The validator performs this construction; the model
cannot override it.

Examples:

- Three eligible options: 35/35/30 active.
- Two eligible options: 35/35 active, 30 SPY.
- One eligible option: 35 active, 65 SPY.
- No eligible option: 100 SPY.

This fallback does not manufacture alpha. It prevents low-confidence ideas
from turning an honest abstention into benchmark underperformance.

## Why This Is The Current Lead

V3A's slate contained the eventual winner in all three replay weeks, so search
coverage was no longer the dominant failure. Across the eight valid saved
responses, candidate rows labeled overreaction with at least a 55% probability
of beating SPY beat SPY 6 of 7 times and averaged 4.72% alpha. Equally confident
continuation rows beat SPY only 1 of 9 times and averaged -2.98% alpha.

A zero-call, post-hoc application of the eligibility gate and SPY fallback
produced:

- 1.45% mean alpha versus SPY;
- 2.48 percentage points mean improvement over saved V2.2 controls;
- 7 of 8 nonnegative-alpha cells;
- positive mean alpha for OpenAI, Grok 4.3, and Grok 4.5; and
- a weakest-period mean alpha of -0.05%.

These figures explain the design. They do not validate it: the rule was written
after the outcomes were inspected, candidate observations are clustered inside
only three periods, Gemini had no valid responses, and one OpenAI cell was
missing.

## Fresh Prospective Validation Only

The July 21, July 28, and August 4 replay windows are permanently development
data for this successor. They must not be used to pass its gate.

If the operator authorizes a new validation budget, use the first three
non-overlapping eligible weekly rounds after the protocol, runner, response
schema, model roster, and call budget have all been committed. Do not skip a
round because its market conditions look unfavorable. Freeze every packet and
response before its exit outcome exists.

The successor should not advance unless all pre-registered requirements pass:

- at least 10 valid paired cells;
- positive mean alpha versus SPY;
- at least 1.00 percentage point mean improvement over paired V2.2 controls;
- at least 5 strict SPY beats and at least 8 nonnegative-alpha cells;
- positive mean alpha for at least 3 model families;
- positive mean alpha in at least 2 of 3 periods;
- weakest-period mean alpha no worse than -0.50%; and
- selected top-three capture no worse than paired V2.2 controls.

Passing this small shadow gate permits a larger prospective shadow. It does not
prove persistent alpha and does not automatically change production.

## Cost And Provider Rule

No more calls are authorized by this design document. The completed V3A program
already consumed its twelve-attempt ceiling. A future operator must separately
approve a new maximum call count after OpenAI credits and Google paid quota are
confirmed. Transport failures must be recorded; they must not trigger retries
unless retries were explicitly included in that future frozen budget.
