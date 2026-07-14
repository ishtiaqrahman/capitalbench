---
experiment_id: portfolio-v2-2026-07-13
status: active
decision_date: 2026-07-20
decision_after_utc: 2026-07-20T20:00:00Z
paired_v1_round_id: CB-2026-07-13-1W
v2_round_id: CB-2026-07-13-V2-1W
v2_run_id: official-v2-20260713
methodology_version: portfolio-v2.0-pilot
publication_stream: pilot
research_cutoff_utc: 2026-07-13T20:55:45Z
decision_deadline_utc: 2026-07-14T07:30:00Z
entry_date: 2026-07-13
exit_date: 2026-07-20
---

# Portfolio V2 Paired Experiment

## Purpose

Test whether a compact horizon-specific market context and forecast-first,
single-turn decision contract improve the same models' weekly portfolios over
the frozen Portfolio V1 protocol. V2 does not change the option universe,
allocation constraints, entry and exit prices, SPY comparator, or scoring.

This is an official paired experiment, not a replacement benchmark until the
precommitted July 20 decision is recorded. Its results must remain outside the
primary publication stream before that decision.

## Execution Record

The canonical V2 run `official-v2-20260713` was accepted at
`2026-07-14T02:44:29.056058+00:00` with four valid submissions and no invalid
canonical submissions. Resolution is scheduled for `2026-07-20T23:30:00Z`.

The initial GPT-5.5 request was rejected by the provider before inference
because `reasoning_effort: minimal` was unsupported. The one transport/config
retry allowed by this contract ran before the decision deadline with
`reasoning_effort: low` and was valid. The initial attempt is preserved under
the canonical run's `attempts/` directory. The isolated source run
`official-v2-20260713-retry-openai-gpt-5-5` is explicitly not score eligible
and must never be counted as a separate round or submission.

Before the round was committed, generated Windows CRLF line endings were
normalized to the repository-required LF format. This byte-only publication
normalization did not change any model-facing text or data. The original
pre-run hashes and the post-normalization hashes are both preserved under the
V2 round's `experiment/` directory.

## Participants

Exactly these four models participate in both the existing V1 control and the
new V2 treatment:

- `openai-gpt-5-5` (`gpt-5.5`)
- `openai-gpt-5-6-sol` (`gpt-5.6-sol`)
- `xai-grok-4-3` (`grok-4.3`)
- `xai-grok-4-5` (`grok-4.5`)

V1 is not rerun. The accepted submissions in
`rounds/CB-2026-07-13-1W/runs/official-20260713` are the controls. V2 makes one
paid call per listed model. Do not add models, stability replicates, provider
search, or a monthly live V2 round.

## Controlled Inputs

- Use the exact V1 research cutoff: `2026-07-13T20:55:45Z`.
- Use facts known by that cutoff only, even if a source is re-opened later.
- Use the same V1 weekly facts, option order, entry date, exit date, benchmark,
  and portfolio constraints.
- Prepare research by direct Codex browsing. Never use participant model APIs,
  provider search, or model-generated research.
- Mechanical pricing APIs or direct mechanical market-data endpoints are
  allowed. Every history row must stop at the July 13 close.
- Freeze and hash all model-facing inputs before the first V2 call.

## Treatment

V2 replaces the V1 trailing-return appendix with the complete mechanically
generated weekly decision-context table. It adds separate recent and prior
window returns, SPY-relative returns, volatility, drawdown, volume context,
SPY correlation and beta, 52-week position, and a compact market-state header.
Rows remain in option order. There are no ranks, recommendations, or composite
buy scores.

Each model receives one single-turn, non-agentic prompt. It must estimate SPY,
estimate its selected holdings, construct a 1-5 holding portfolio in 5%
increments, and return forecast arithmetic, catalyst, invalidation, concise
rationale, and the probability that the portfolio beats SPY. No follow-up or
post-response allocation optimization is allowed.

## Pre-Run Gate

- The V2 prompt contains its decision-context appendix exactly once and does
  not contain the V1 appendix.
- Every included option has one row; noncash rows have a July 13 close or are
  explicitly marked unavailable.
- V2 model input is no more than 10% larger than the corresponding V1 input.
- All repository tests and a four-model mock run pass.
- OpenAI and xAI credentials are present before the real run begins.
- Content-invalid submissions are preserved and are not retried. Only a
  provider transport failure may be retried before the frozen deadline.

## July 20 Resolution

Resolve only after the July 20 regular-session close is available. Fetch one
price snapshot and use it for both paired rounds. Compare only the four listed
models and calculate for each model:

- V1 and V2 portfolio return.
- V1 and V2 alpha versus SPY.
- Paired improvement: V2 return minus V1 return.
- Whether each portfolio beat SPY.
- Recent-winner concentration, cross-model overlap, theme concentration, and
  V2 forecast error as diagnostics.

Create a paired machine-readable result and a human-readable report under the
V2 round's `experiment/` directory. Realized paired returns are the primary
decision evidence; diagnostics explain the result but do not override it.

The machine-readable experiment definition is
`experiments/portfolio-v2-2026-07-13.yaml`. Treat it and this document as a
single frozen contract. The evaluator reads that file directly.

## Frozen Acceptance Rule

Promote V2 for future weekly and monthly rounds only when all conditions pass:

1. All four V2 submissions were valid, frozen before outcomes, and cutoff-safe.
2. The four-model average V2 alpha versus SPY is greater than zero.
3. Average V2 alpha is greater than average paired V1 alpha.
4. At least three of four models have a positive paired improvement.
5. The number of V2 portfolios beating SPY is not lower than V1.
6. No data leakage, scoring inconsistency, or input mismatch is found.

If every condition passes, set this document's status to `accepted`, record the
metrics and decision timestamp, and make `portfolio-v2` the default for future
weekly and monthly rounds. Do not rewrite historical V1 rounds.

If any condition fails, set the status to `rejected`, record which condition
failed, and retain `portfolio-v1.0` as the default. Do not run another paid
paired round automatically and do not reinterpret a failed condition.

## Resolution Checklist

```bash
capitalbench automation-resolve \
  --rounds-dir rounds \
  --round-id CB-2026-07-13-V2-1W \
  --run-id official-v2-20260713 \
  --no-sync
```

Then resolve the paired V1 round if it has not already resolved, generate the
paired comparison, audit the six acceptance conditions, update this document,
run the full test suite, and only then publish the recorded decision. Pilot
rounds remain excluded from primary latest, cumulative, market-environment,
and insights calculations unless V2 is accepted for future rounds.

Generate the frozen paired decision with:

```bash
capitalbench evaluate-experiment \
  --config experiments/portfolio-v2-2026-07-13.yaml \
  --rounds-dir rounds
```
