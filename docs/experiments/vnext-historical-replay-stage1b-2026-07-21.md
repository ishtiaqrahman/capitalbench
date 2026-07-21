# VNext Historical Replay Stage 1B Protocol

## Purpose

This private retrospective experiment tests whether structured candidate
coverage can improve one-week asset discovery. It is not an official
CapitalBench round and cannot change production V2.1 by itself.

The previous replay showed that no model shortlist contained the eventual
winner or runner-up. Stage 1B therefore treats candidate recall as the primary
problem and top-five return as a required secondary check.

## Controls And Holdout

The twelve valid H0 responses from the frozen July 20 replay are reused for
D1-D3. They must not be regenerated. Their record hashes are stored in this
experiment's freeze manifest.

D1-D3 are adaptive development replays. C1-C3 remain sealed confirmation
replays. Outcomes are loaded only by scoring commands after the corresponding
responses have been saved.

## Models

- Gemini 3.5 Flash
- Grok 4.3
- Grok 4.5
- GPT-5.6 SOL

All calls are closed-capability, temperature zero, single turn, non-agentic,
and have no tools, browsing, or search.

## Shared Input

Every challenger receives the same frozen factual briefing and complete
option table used by the earlier replay, plus deterministic calculations made
only from entry-time trailing returns:

- SPY-relative returns and within-universe ranks
- broad market breadth and dispersion summary
- candidate reference lists for continuation, reversal, contextual catalyst,
  and defensive behavior

The candidate lists are aids, not a reduced universe. Models may inspect and
select from every active option.

## Treatments

### H4: Balanced Candidate Lanes

The final ten-name shortlist must contain exactly three continuation names,
three reversal names, two context/catalyst names, one defensive name, and one
unrestricted wildcard. No more than four names may come from one option group.

### H5: Regime-Routed Candidate Lanes

The model first classifies the environment from supplied entry-time market
statistics. The shortlist must retain at least two continuation, two reversal,
one context/catalyst, and one defensive candidate. Four remaining positions
are routed according to the model's stated regime. The same option-group cap
applies.

### H6: Omitted-Candidate Challenge

H6 is run only if neither H4 nor H5 passes. The model forms an initial ten-name
shortlist, reviews five strong omitted candidates, and then submits a final
ten-name shortlist containing at least two of those challengers. This is one
model call, not an agentic second turn.

## Discovery Execution

H4 and H5 are each run for all four models on all three development replays,
for 24 new calls. Each response is paired with the previously frozen H0
response for the same model and replay.

If neither primary treatment passes, H6 is run for all model-replay cells for
12 additional calls. If a primary treatment passes, H6 is skipped.

## Discovery Gate

A treatment advances only when all conditions hold:

- at least 10 of 12 pairs are valid;
- winner-or-runner-up recall is greater than H0;
- recall occurs in at least two replays and for at least two models;
- mean shortlist oracle regret falls by at least 30% versus H0;
- mean top-five alpha improves by at least 0.50 percentage points;
- top-five alpha improves in at least 7 of 12 pairs;
- mean alpha improvement is positive for at least three models and two replays.

If both H4 and H5 pass, selection is ordered by top-two recall gain, relative
regret reduction, mean alpha improvement, then treatment ID.

## Confirmation

Only the selected treatment is eligible for C1-C3. Confirmation runs fresh H0
and challenger responses for every model and replay, for 24 calls. Confirmation
uses the same breadth requirements and requires positive regret reduction and
positive mean alpha improvement. Passing confirmation qualifies a treatment
only for a prospective live shadow test.

## Interpretation

Exact weekly winners are noisy and the development dates are known after the
fact. A discovery pass is therefore not evidence of live predictive skill.
The untouched confirmation replays reduce adaptive overfitting, and a future
live shadow remains mandatory before any production change.
