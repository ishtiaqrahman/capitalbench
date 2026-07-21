# VNext Event And Pairwise Ranking Replay

Frozen on: `2026-07-21`

Status: private historical validation. This experiment is not official-score
eligible and does not change Portfolio V2.0.

## Question

Does a compact option-linked event register help balanced candidate search,
and can pairwise candidate-versus-SPY comparison plus evidence-based
abstention convert that coverage into higher weekly selection-basket returns?

## Why This Test

Prior replay found that balanced candidate lanes improved top-two coverage but
did not reliably improve returns. Pairwise ranking was mixed. The remaining
testable hypothesis is that ranking lacked compact, timely, option-linked
evidence rather than more general market prose.

## Sample

The repository does not contain 18 independent resolved weekly windows. The
experiment therefore uses four previously untouched, non-overlapping weekly
rounds: June 17, June 25, July 6, and July 13. These are historical validation,
not sealed proof. No overlapping daily round is counted as an independent
episode merely to enlarge the sample.

Current models may remember historical outcomes, so this replay can reject a
weak design but cannot establish prospective investment skill. Any passing
treatment still requires one prospective shadow weekly run.

## Models

- Gemini private replay endpoint (`gemini-3.5-flash` override)
- Grok 4.3
- Grok 4.5
- GPT-5.6 SOL

Anthropic models are excluded. Every call is single-turn and non-agentic. The
models receive no tools, browsing, search, or external memory instruction.

## Frozen Treatments

### H4: Balanced Search

Ten candidates: three continuation, three reversal, two context/event, one
defensive, and one wildcard. This is the strongest lead from Stage 1B.

### H7: Balanced Search Plus Event Register

The same lane contract, plus the frozen compact event register. Each candidate
must identify event IDs, timing fit, and evidence strength. The register has no
directional label, score, recommendation, or hindsight return.

### H0: Unchanged Replay Control

The existing VNext control packet and schema.

### H8: Event Evidence, Pairwise Ranking, And Abstention

H7 search plus candidate-versus-SPY judgments and all pairwise comparisons
among the final five. `prefer_spy` must be true when no candidate has a timely
event/catalyst, stronger evidence than SPY, and positive expected alpha. This
is still one call; the model performs all reasoning before returning one JSON
object.

## Sequential Execution

1. Run H4 and H7 on all four episodes and models (32 calls).
2. Stop if H7 fails the frozen search gate.
3. Only if H7 passes, run H0 and H8 (32 calls).
4. Evaluate H8's effective return as SPY when it abstains, otherwise the
   equal-weight return of its final five.

This order caps cost at 64 calls and avoids spending on pairwise ranking unless
the event representation first demonstrates incremental value.

## Search Gate

H7 must have at least 14 valid pairs, improve mean top-five alpha over H4 by at
least 0.30 percentage points, improve at least 9 pairs, 3 model families, and 3
episodes, and not reduce top-three capture or increase shortlist regret.

## Final Gate

H8 must have at least 14 valid pairs, improve effective return over H0 by at
least 0.50 percentage points, have positive mean alpha versus SPY, improve at
least 9 pairs, 3 model families, and 3 episodes, improve top-three capture or
shortlist regret, and not worsen the worst episode.

## Interpretation

A failure means stop this branch. A pass authorizes only a prospective weekly
shadow test; it does not authorize a production prompt or methodology change.
Primary success is portfolio-level alpha versus SPY. Top-three capture and
regret are supporting diagnostics.
