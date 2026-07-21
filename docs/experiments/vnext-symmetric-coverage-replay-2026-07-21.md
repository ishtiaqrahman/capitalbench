# VNext Symmetric Coverage Replay

Frozen on: `2026-07-21`

Status: private historical development. This experiment is not official-score
eligible and does not change Portfolio V2.0.

## Question

Can symmetric option-level evidence coverage, exhaustive fixed-lane search,
and a hard independent-evidence gate improve weekly selection returns over the
existing H4 balanced-search treatment?

## Why This Test

Resolved V1 decisions allocate disproportionately to options named in the
model-facing briefing even though briefing mentions did not reliably predict
returns. The exact weekly winner was not mentioned in 17 of 30 eligible rounds.
Simple model ensembles, consensus portfolios, trailing-model routing,
construction changes, momentum rules, reversal rules, and the earlier H7
event-register treatment did not repair returns.

H7 presented an event table, but the model still searched through selective
narrative plus mechanical lanes before attaching events to its chosen names.
H9 removes that asymmetry. It presents every active option exactly once in an
option-to-event matrix, explicitly marks options with no mapped event, and
forces the model to choose one finalist from each fixed lane before ranking.

## Sample And Models

The four non-overlapping weekly periods V1-V4 are reused as historical
development data. They are already adaptive and cannot become confirmation
evidence. Current models may also remember historical outcomes. This replay can
reject H9; a pass authorizes only a new prospective shadow test.

Only three model families receive new calls:

- Gemini 3.1 Pro, using the frozen private replay override;
- Grok 4.5; and
- GPT-5.6 SOL.

Nine existing H4 responses are valid controls. Three Gemini H4 cells ended in
transport or quota errors in the earlier experiment, so H9 may repeat those
exact frozen H4 packets before running the challengers. Maximum incremental
cost is 15 single-turn calls: three control repairs and 12 H9 calls. No
Anthropic model is used. This correction was frozen before any H9 provider call
and preserves the 12-pair gate instead of weakening it around missing controls.

## Frozen H9 Input

H9 includes:

1. The compact entry-time mechanical market summary.
2. The complete option comparison table in frozen option order.
3. The frozen factual event register.
4. A complete option evidence matrix with one row per non-cash option. Every
   row lists mapped event IDs or `none`.

H9 excludes the selective narrative briefing and all realized outcomes.

## Fixed Search Lanes

Every non-cash option belongs to exactly one of eight predetermined lanes:

1. U.S. core and style;
2. growth and technology;
3. domestic cyclicals;
4. health and defensive equity;
5. international equity;
6. rates and credit;
7. real assets; and
8. alternatives and currencies.

The ten-name shortlist must contain SPY, one unique winner from each lane, and
one unique wildcard. This structure forces coverage of the complete universe
without turning any mechanical feature or event into a recommendation.

## Independent-Evidence Gate

Every non-SPY final-five candidate must cite at least one event ID that is
actually mapped to that option. Recent or trailing price performance alone is
not independent evidence. If the model cannot identify five valid finalists,
or does not expect the supported basket to beat SPY, it must set
`prefer_spy=true`. Effective return is then SPY return; the unexecuted top five
is retained for diagnostic scoring.

## Frozen Success Gate

H9 advances to a prospective shadow only if all conditions pass:

- at least 10 valid H4/H9 pairs;
- mean effective-return improvement of at least 0.50 percentage points;
- positive mean H9 effective alpha versus SPY;
- at least 7 positive pairs;
- positive mean improvement in all three model families;
- positive mean improvement in at least three of four episodes;
- at least 20% mean shortlist-regret reduction;
- no decrease in total top-three shortlist capture; and
- no deterioration in the worst episode's mean alpha.

Any failure rejects H9. No threshold may be relaxed after outcomes are loaded.

## Interpretation

The primary endpoint is effective return versus SPY. Shortlist capture,
shortlist regret, abstention, and lane coverage explain the result. Historical
success would not prove investment skill and would not change production.
