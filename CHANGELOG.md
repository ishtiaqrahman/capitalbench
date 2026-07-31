# Changelog

## 2026-07-31

### Evidence-backed model behavior profiles

- Replaced threshold-order captions with peer-normalized behavior profiles built
  from same-round, leave-one-model-out comparisons across official frozen
  portfolios.
- Added minimum sample, independent-date, materiality, and persistence gates;
  weekly/monthly disagreements and recent methodology reversals now lower or
  qualify confidence instead of producing overconfident labels.
- Standardized every model on four evidence-bearing pills: signature,
  construction, tempo, and current positioning (or lifecycle for retired
  models), with retired models excluded from active superlatives.
- Published the method, evidence tiers, exclusions, and wording provenance on
  the model-patterns page and in the public API, while retaining a V1 shadow for
  migration audits.

## 2026-07-21

### Forward-only model retirement

- Retired Claude Opus 4.7 from all newly initialized weekly and monthly
  production rounds while preserving its historical submissions, results,
  model profile, and benchmark comparison sets.
- Added explicit model lifecycle metadata and date-aware runner eligibility;
  retrospective research can still replay retired models without making those
  calls official.
- New Portfolio V2 round manifests now freeze an immutable roster version and
  exact expected model IDs. Execution and acceptance both validate that
  snapshot, including V2.2, instead of reading a mutable current roster.
- Updated benchmark-set discovery so the first accepted run after a permanent
  retirement opens a successor comparison set, while temporary smaller rosters
  continue to be treated as outages.

### Portfolio V2.2 production adoption

- Made `portfolio-v2.2` the default methodology for newly initialized
  portfolio rounds by explicit operator direction; existing V2.0 rounds stay
  frozen under their original manifests.
- Added the Q1 cutoff-safe option-level evidence table with fixed 45/30/15/10
  prior-trend, recent-pullback, low-volatility, and shallow-drawdown weights.
- Kept model judgment intact: V2.2 adds information but does not impose Q2's
  rejected high-score candidate or holding quotas.
- Added a 90% evidence-coverage guard, separate frozen JSON and Markdown input
  artifacts, and round hashing for both files.
- Recorded that the 8-of-9 development result motivated operator adoption but
  is not prospective validation; V2.2 must be evaluated on fresh resolutions.

### Durable return-research record

- Added `research/registry.yaml`, a human research index, a recording protocol,
  and automated validation so return-improvement findings survive across
  Codex sessions and cannot rely only on ignored `output/` artifacts.
- Registered the historical predictability, V2 diagnosis, replay, mechanical,
  pilot, and construction-diagnostic work with findings, limitations, and next
  actions.
- Ran the gated four-period H4-versus-H7 event-register replay. H7 improved
  mean top-five alpha by only 0.16 percentage points, improved 8 of 13 valid
  pairs and 2 of 4 episodes, and worsened shortlist regret, so it was rejected
  and the H8 pairwise stage was not run.
- Set the no-call July 17 complete-ledger decomposition after the July 24 close
  as the next research gate. Production Portfolio V2.0 remains unchanged.
- Rejected symmetric fixed-lane coverage after it produced -0.43% treatment
  alpha, improved only 3 of 8 valid pairs, and worsened shortlist regret by
  81%.
- Backfilled V2-style cutoff-safe price features for all 69 symbols and 46
  resolved rounds. Weekly quality-pullback was the only frozen rule to pass,
  with +0.28% non-overlapping alpha and a 62.5% beat rate; it is retained only
  as a fragile private-shadow candidate.
- Tested compact quality evidence inside four research LLM calls rather than
  altering portfolios afterward. Q2 initially improved every valid OpenAI/xAI
  development pair, but unchanged confirmation improved only 3 of 8 valid
  pairs and 1 of 3 periods, so the treatment was rejected with no production
  change.

### July 13 V2 pilot resolution

- Resolved the July 13 V1 control and four-model V2 pilot from one shared
  70-option adjusted-close price snapshot.
- Recorded the frozen pilot decision as rejected: V2 retained positive alpha
  versus SPY but trailed V1 by 2.13 percentage points on average, with 0 of 4
  paired models improving.
- Added zero-cost loss diagnostics and weight-only counterfactuals. The pilot
  did not retain candidate ledgers; equal weighting and 35%/50% caps did not
  improve aggregate return, so no production or paid-call change was made.
- Preserved the separately directed Portfolio V2.0 production methodology and
  set the July 17 weekly resolution after the July 24 close as the next
  candidate-ledger evidence gate.

## 2026-07-17

### Portfolio V2.0 production adoption

- Made `portfolio-v2.0` the default methodology for new portfolio rounds by
  explicit operator direction.
- Added a required 6-8 option candidate ledger with SP500, four or more static
  economic-exposure clusters, low/base/high forecasts, continuation and
  reversal cases, catalysts, invalidation conditions, and retained rejected
  finalists.
- Added a holding-level SPY base-forecast hurdle and a 50% cap on each
  non-benchmark economic-exposure cluster. A 100% SPY portfolio remains valid.
- Replaced the pilot's redundant 15-column market table with a compact
  12-column horizon-specific decision context for production V2 rounds.
- Added the complete tracked eight-model V2 production roster and preserved the
  July 13 four-model pilot as a separate unresolved experiment with its
  original frozen rule.
- Continued scoring only the final frozen portfolio. Candidate forecasts are
  retained for prospective calibration and do not alter official scoring.
- Retained the partial July 16 weekly and monthly runs as audit-only artifacts
  and excluded them from official scoring because each contains only four of
  the eight required production models.
- Accepted `CB-2026-07-17-1W` and `CB-2026-07-17-1M` as the first complete
  official V2 weekly and monthly rounds. Each contains all eight production
  models and remains unresolved until its scheduled exit close.
