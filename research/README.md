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

The evidence does not support changing the production Portfolio V2.0 method
yet. Historical work has consistently found that selection is the main
bottleneck; construction-only changes, generic context expansion, and simple
mechanical momentum/reversal rules have not produced robust improvement.

Balanced candidate search remains the strongest search lead, but a July 21
validation found that adding a compact event register improved capture without
reliably improving returns. H7 gained only 0.16 percentage points over H4,
worsened shortlist regret, and failed its frozen gate, so pairwise H8 was not
run. The next program is the no-call July 17 production-ledger decomposition
after the July 24 close. This will determine whether search, ranking, or
construction is the dominant loss stage before another prompt treatment is
funded.

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
| 2026-07-24 | July 17 ledger diagnostic | Planned after the close; no model calls and no production change. |

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
- Production methodology changes require a frozen gate and a prospective
  shadow run after historical validation.
