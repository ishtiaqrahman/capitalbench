# CapitalBench Return Research

This directory is the durable memory for research intended to improve model
portfolio returns. It is written for both human reviewers and future Codex
sessions.

## Read This First

Before proposing or running another return-improvement experiment, read:

1. `research/registry.yaml` - canonical experiment ledger and current state.
2. `research/PROTOCOL.md` - rules for freezing, running, and recording work.
3. The canonical reports linked from the relevant registry entries.

Raw files under `output/` are disposable working artifacts. They are not the
research record. A finding does not become durable until its protocol, report,
and summary are stored in tracked paths and registered in
`research/registry.yaml`.

## Current Conclusion

Portfolio V3.0 is the production default for newly initialized rounds by
explicit operator direction on August 15, 2026. This adoption does not change
the historical research verdict: the frozen holdout gate failed because only
8 of 12 calls were valid against a required 10. Existing V2.2 rounds remain
frozen. Historical work continues to show that selection is the main
bottleneck; construction-only changes, generic context expansion, and simple
mechanical momentum/reversal rules did not produce robust improvement.

The August 13 V3A replay is rejected under its frozen gate. After the three
Gemini transport failures were filled with valid responses, 11 cells produced
-0.19% mean alpha versus SPY, compared with -1.62% for paired V2.2 controls.
The deterministic slate contained the eventual winner in all three periods,
and Grok 4.3 averaged +2.73% alpha, but Gemini averaged -2.10%. The experiment
failed the positive-alpha, breadth, positive-pair, and worst-period gates; one
OpenAI credit failure remains. Do not adopt V3A.

A zero-call post-hoc diagnostic required at least a 55% model-estimated chance
of beating SPY, admitted overreaction calls rather than unaudited continuation,
and put unused slots in SPY. Across the 11 valid cells, it reached +1.04% mean
alpha: 9 of 11 were nonnegative, and three of four represented models had
positive mean alpha while Gemini nearly matched SPY at -0.04%. This is a strong
design lead, not validation. The three V3A test periods must not be reused as
confirmation.
The follow-on robustness audit found the result stayed positive after removing
any one model, period, or cell and across every tested cutoff from 45% through
67.5%. Confidence alone and confident continuation remained negative. The
simplest V3.0 candidate therefore admits only confident overreaction calls and
uses SPY for every unused slot. Its exact method is in
`docs/portfolio_v3_candidate_methodology.md`; it authorizes no additional calls
and makes no production change.

The frozen August 14 holdout then spent exactly twelve attempts on three
different V2.2 rounds. Eight valid V3 cells averaged +1.94% versus SPY and
improved 2.45 points over exact same-model, same-date V2.2 controls. Every valid
cell was at or above SPY, and every represented model family and period was
positive. V3 also exceeded the -0.15% saved V1 same-ID weekly historical
reference, although V1 is not a paired comparison. The result is promising but
did not pass: three SOL calls failed for exhausted OpenAI credits and one Grok
response failed schema validation, leaving 8 valid cells against a frozen
minimum of 10. Do not weaken that rule or describe it as passed. The operator
later adopted this exact V3 rule as a separate forward methodology decision;
see `docs/portfolio_v3_methodology.md`.

Balanced candidate search remains the strongest prompt-search lead, but two
July 21 extensions failed. A compact event register gained only 0.16 points
over H4, and symmetric fixed-lane coverage produced -0.43% alpha while
worsening shortlist regret by 81%. Do not resume either branch.

A separate zero-call backfill found one candidate worth prospective testing.
The weekly quality-pullback rule gained 0.36 points over SPY across all 30
rounds and 0.28 points across eight non-overlapping weeks, with positive
discovery and holdout results. It passed its frozen historical gate but is
fragile: holdout alpha was only 0.09%, and removing the best independent week
makes independent alpha negative. The mechanical portfolio rule may be run
unchanged as a private prospective shadow and does not itself justify changing
submitted allocations. The operator separately adopted the same components as
neutral Q1 model input in Portfolio V2.2. The July 17 production-ledger
decomposition after the July 24 close remains separately scheduled.

The follow-on LLM input test changed direction from post-response overlays to
the actual model call. Q1 added a complete compact evidence table; Q2 also
forced several high-evidence options into the shortlist and final five. On V1
through V3, Q2 improved all eight valid OpenAI/xAI pairs by 2.90 points and
produced +1.50% alpha, but Google quota failures prevented the four-model gate.
Unchanged Q2 then failed on D1 through D3: only 3 of 8 valid pairs and 1 of 3
periods improved, and treatment alpha was -0.42%. Q2 is rejected and must not
be tuned on those failures. Information-only Q1 remains unconfirmed, but the
operator subsequently adopted its fixed evidence table as Portfolio V2.2.
That production decision must not be described as a passed research gate.

## Research Sequence

| Date | Experiment | Conclusion |
| --- | --- | --- |
| 2026-07-20 | Historical predictability audit | One weak weekly reversal signal survived loose screening, but it was unstable and did not justify a method change. |
| 2026-07-20 | V2 improvement diagnosis | Search regret dominated; more unstructured information and construction-only fixes were rejected. |
| 2026-07-20 | VNext Stage 1 | Rank-first and cross-sectional prompts showed small directional gains but failed capture and robustness gates. |
| 2026-07-21 | VNext Stage 1B | Balanced lanes produced the best candidate coverage, but mean alpha and breadth gates failed. |
| 2026-07-21 | VNext Stage 1C | Pairwise reranking was mixed and failed; the same development periods must not be tuned again. |
| 2026-07-21 | Mechanical screen | Continuation, reversal, quality-pullback, and regime-router rules all failed. |
| 2026-07-21 | July 13 V1/V2 pilot | V2 trailed paired V1 by 2.13 percentage points and was rejected under the frozen pilot rule. |
| 2026-07-21 | July 13 diagnostic | Caps, equal weights, and SPY sleeves did not repair the pilot; no retrospective candidate ledger was invented. |
| 2026-07-21 | Event-ranking program | Rejected: +0.16-point mean gain, 8/13 positive pairs, only 2/4 positive episodes, and worse shortlist regret. H8 was not run. |
| 2026-07-21 | Symmetric coverage replay | Rejected: -0.43% treatment alpha, only 3/8 pairs improved, and shortlist regret worsened 81%. |
| 2026-07-21 | Decision-context backfill | Weekly quality-pullback passed the frozen historical gate at +0.28% non-overlapping alpha, but remains a fragile private-shadow candidate. |
| 2026-07-21 | Model-quality overlays | Rejected: the best overlay gained only 0.32 points and still trailed SPY by 0.60%. |
| 2026-07-21 | LLM quality-input development | Q2 gained 2.90 points across all eight valid OpenAI/xAI pairs, but failed the four-model and regret gates after Google quota errors. |
| 2026-07-21 | LLM quality-input confirmation | Rejected: Q2 improved only 3/8 valid pairs and 1/3 periods, with -0.42% treatment alpha. |
| 2026-07-21 | Portfolio V2.2 operator adoption | Q1's information-only table was versioned into new production rounds by explicit direction; it remains prospectively unconfirmed and Q2 remains rejected. |
| 2026-07-24 | July 17 ledger diagnostic | Complete: +1.71% alpha in one week, with regret distributed across search (27%), ranking (42%), and construction (31%); no stage crossed 50%. |
| 2026-08-13 | Portfolio V3A anti-extrapolation replay | Rejected: 11 valid cells averaged -0.19% versus SPY while improving 1.43 points over paired V2.2; breadth and downside gates failed. |
| 2026-08-13 | V3A compliance diagnostic | Post-hoc only: a 55% confidence/evidence gate plus SPY fallback reached +1.04% alpha with 9/11 nonnegative cells. |
| 2026-08-14 | V3 robustness diagnostic | Development candidate only: +1.04% alpha survived every leave-one-model, leave-one-period, and leave-one-cell test; continuation remained negative. |
| 2026-08-14 | V3 holdout comparison | Rejected on validity: 8/12 valid cells averaged +1.94% versus SPY and +2.45 points versus exact V2.2 controls, but the frozen minimum was 10 valid cells. |
| 2026-08-15 | Portfolio V3.0 operator adoption | The unchanged confident-overreaction rule and SPY fallback became the forward production default by explicit direction. The August 14 gate remains recorded as failed. |

## Non-Negotiable Interpretation Rules

- Optimize first for positive portfolio alpha versus SPY, not exact prediction
  of the single best asset among roughly 70 choices.
- Treat top-three capture and shortlist regret as diagnostics, not the primary
  success criterion.
- Historical replay can reject a weak design; it cannot prove prospective
  skill because current models may remember historical outcomes.
- Do not repeatedly adapt prompts on the same periods and then describe those
  periods as confirmation data.
- Do not publish private experiments into latest, cumulative, market-regime,
  insight, or official score streams.
- Research-based acceptance claims require a frozen gate and prospective
  evidence after historical validation. An operator may still make a
  forward-only methodology decision, but it must be recorded separately and
  must not rewrite a failed gate as passed.
