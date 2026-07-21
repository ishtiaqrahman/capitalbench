# VNext Historical Replay Stage 1C Protocol

## Purpose

Stage 1B showed that balanced candidate lanes moved six eventual top-two assets
into model shortlists, but none reached the final five. Stage 1C isolates final
ranking before testing a production-compatible single-turn version.

This is private retrospective research. It is not an official CapitalBench
round and cannot change production V2.1 by itself.

## Frozen Inputs

The diagnostic reuses each model's exact H4 shortlist from D1-D3. Those twelve
H4 response records are frozen by hash before outcomes are loaded. Models may
not replace shortlist candidates during the diagnostic.

The integrated S1 packets and C1-C3 confirmation packets are also frozen before
diagnostic scoring. C1-C3 remain sealed unless both earlier gates pass.

## Models

- Gemini 3.5 Flash
- Grok 4.3
- Grok 4.5
- GPT-5.6 SOL

Calls are temperature zero, single turn, non-agentic, and have no tools,
browsing, or search.

## R1: Ranking Diagnostic

R1 receives only the model's frozen H4 shortlist, its existing lane labels,
the frozen factual briefing, and entry-time market features for those ten
assets. It must assess every candidate using:

- probability of beating SPY;
- probability of finishing in the top decile of active assets;
- probability of a materially negative return;
- one ranking lane: continuation, quality pullback, capitulation rebound,
  context/defensive, or other.

The final five must contain one continuation selection, one quality-pullback
selection, one capitulation-rebound selection, and two unrestricted selections.

R1 is diagnostic only because it uses a second call after candidate generation.

## R1 Gate

R1 advances only when, versus the original H4 final five:

- at least 10 of 12 pairs are valid;
- final-five winner-or-runner-up capture is greater;
- captures occur in at least two replays and for at least two models;
- mean top-five alpha improves by more than 0.50 percentage points;
- at least 7 of 12 pairs improve;
- mean improvement is positive for at least three models and two replays.

## S1: Integrated Single Turn

If R1 passes, S1 combines H4 balanced candidate generation, probability-first
assessment of all ten shortlist names, and the R1 final-five role constraints
in one response. It uses the complete active universe and remains single turn
and non-agentic.

S1 is run for all four models on D1-D3. It must preserve at least six top-two
shortlist captures, exceed H0 final-five top-two recall, and pass the same alpha
and breadth gate as R1.

## Confirmation

Only an S1 development pass opens C1-C3. Confirmation runs fresh H0 and S1
responses for every model and replay. It requires broader final-five top-two
capture than H0, positive mean alpha improvement, at least 7 positive pairs,
and positive mean improvement across at least three models and two replays.

Passing historical confirmation qualifies S1 only for a prospective live
shadow test.
